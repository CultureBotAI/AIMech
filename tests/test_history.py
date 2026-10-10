"""Exercise canonical history generation, linkage, and failure boundaries."""

# BSD 3-Clause License
#
# Copyright (c) 2026, CMMMech Contributors
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import copy
import subprocess

import pytest
import yaml

from aimech.cli import main
from aimech.history import append_only_errors, validate_history, validate_references
from aimech.validation import read_record


@pytest.fixture(autouse=True)
def isolate_synthetic_history_base(monkeypatch):
    """CI's real repository revision cannot identify a synthetic fixture's base."""
    monkeypatch.delenv("AIMECH_HISTORY_BASE", raising=False)


@pytest.fixture
def record():
    return {"id": "AIO:SyntheticConcept", "fixture": "not a scientific record"}


@pytest.fixture
def history():
    return {
        "history_version": 1,
        "target": {"kind": "record", "slug": "SyntheticConcept",
                   "path": "data/aio/SyntheticConcept.yaml"},
        "session": {"id": "2026-10-07T120000Z-tester-123abc",
                    "timestamp": "2026-10-07T12:00:00Z",
                    "actors": [{"type": "human", "name": "tester"}]},
        "events": [{"type": "AUDIT", "outcome": "no_change", "summary": "Synthetic check",
                    "details": "A synthetic history fixture; no scientific claims."}],
    }


def write_history(root, history):
    path = (root / "history/records" / history["target"]["slug"]
            / f"{history['session']['id']}.yaml")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(history))
    return path


def test_canonical_history_is_closed(history, tmp_path):
    path = write_history(tmp_path, history)
    assert validate_history(history, path, tmp_path) == []
    history["events"][0]["unexpected"] = True
    assert validate_history(history, path, tmp_path)


@pytest.mark.parametrize("keys,value", [
    (("history_version",), 2),
    (("session", "timestamp"), "2026-02-30T12:00:00Z"),
    (("session", "timestamp"), "2026-10-07T12:00:00+02:00"),
    (("session", "id"), "not-the-file-stem"),
    (("session", "actors"), []),
    (("session", "actors", 0, "name"), "  "),
    (("session", "actors", 0, "type"), "ai_agent"),
    (("target", "path"), "../outside.yaml"),
    (("target", "path"), "/tmp/outside.yaml"),
    (("target", "path"), "data\\outside.yaml"),
    (("target", "slug"), ".."),
    (("events",), []),
    (("events", 0, "type"), "UNKNOWN"),
    (("events", 0, "summary"), " "),
    (("events", 0, "details"), " \nTODO: replace this placeholder before committing"),
    (("events", 0, "details"), ""),
    (("links",), {"issues": ["3"]}),
])
def test_invalid_history_is_rejected(history, tmp_path, keys, value):
    path = write_history(tmp_path, history)
    node = history
    for key in keys[:-1]:
        node = node[key]
    node[keys[-1]] = value
    assert validate_history(history, path, tmp_path)


def test_references_identify_the_exact_record_and_preserve_inline_events(record, history, tmp_path):
    path = write_history(tmp_path, history)
    target = tmp_path / history["target"]["path"]
    record["history_refs"] = [path.relative_to(tmp_path).as_posix()]
    record["curation_history"] = [{
        "timestamp": "2026-10-07T12:00:00Z", "curator": "synthetic-reviewer",
        "action": "synthetic-check", "notes": "Synthetic inline event, not a sidecar path.",
    }]
    before = copy.deepcopy(record)
    assert validate_references(record, target, tmp_path) == []
    assert record == before
    record["id"] = "AIO:Different"
    assert "target does not match" in validate_references(record, target, tmp_path)[0]
    record["id"] = "AIO:SyntheticConcept"
    assert "target does not match" in validate_references(record, tmp_path / "other.yaml", tmp_path)[0]
    path.unlink()
    assert validate_references(record, target, tmp_path)
    record.pop("history_refs")
    assert validate_references(record, target, tmp_path) == []


def test_references_refuse_aliases_before_reading(record, history, tmp_path, monkeypatch):
    from aimech import history as module

    path = write_history(tmp_path, history)
    (tmp_path / "history").rename(tmp_path / "archive")
    (tmp_path / "history").symlink_to(tmp_path / "archive", target_is_directory=True)
    record["history_refs"] = [path.relative_to(tmp_path).as_posix()]

    def unexpected_read(*args):
        raise AssertionError("An alias must be rejected before reading the sidecar")

    monkeypatch.setattr(module, "read_record", unexpected_read)
    assert validate_references(record, tmp_path / history["target"]["path"], tmp_path)


def new_args(tmp_path):
    return ["new-history", "--repo-root", str(tmp_path), "--slug", "SyntheticConcept",
            "--actor-name", "tester", "--actor-type", "human", "--event", "AUDIT",
            "--outcome", "no_change", "--summary", "Synthetic test",
            "--details", "Verified a synthetic fixture, without making scientific claims.",
            "--issue", "3"]


def test_scaffolder_creates_distinct_sessions_without_touching_target(tmp_path, record, capsys):
    target = tmp_path / "data/aio/SyntheticConcept.yaml"
    target.parent.mkdir(parents=True)
    target.write_text("# Preserve curator formatting and comments.\n" + yaml.safe_dump(record))
    before = target.read_bytes()
    paths = []
    for _ in range(2):
        assert main(new_args(tmp_path)) == 0
        paths.append(tmp_path / capsys.readouterr().out.strip())
    assert paths[0] != paths[1]
    assert target.read_bytes() == before
    for path in paths:
        data = read_record(path)
        assert validate_history(data, path, tmp_path) == []
        assert data["links"]["issues"] == ["https://github.com/CultureBotAI/AIMech/issues/3"]
    assert main(["validate-history", "--repo-root", str(tmp_path)]) == 0


def test_collision_never_overwrites_existing_history(tmp_path, record, monkeypatch, capsys):
    from aimech import history as module

    target = tmp_path / "data/aio/SyntheticConcept.yaml"
    target.parent.mkdir(parents=True)
    target.write_text(yaml.safe_dump(record))
    assert main(new_args(tmp_path)) == 0
    existing = tmp_path / capsys.readouterr().out.strip()
    before = existing.read_bytes()
    real_link = module.os.link
    monkeypatch.setattr(module.os, "link", lambda src, dst: real_link(src, existing))
    assert main(new_args(tmp_path)) == 1
    assert existing.read_bytes() == before
    assert list(existing.parent.glob(".new-history-*")) == []


@pytest.mark.parametrize("extra", [
    ["--slug", ".."], ["--path", "../outside.yaml"], ["--path", "/tmp/outside.yaml"],
    ["--details", "  "], ["--actor-type", "ai_agent"], ["--issue", "not-a-uri"],
])
def test_scaffolder_refuses_bad_metadata_without_creating_files(tmp_path, record, extra):
    target = tmp_path / "data/aio/SyntheticConcept.yaml"
    target.parent.mkdir(parents=True)
    target.write_text(yaml.safe_dump(record))
    before = target.read_bytes()
    assert main(new_args(tmp_path) + extra) == 1
    assert target.read_bytes() == before
    assert not (tmp_path / "history").exists()


def test_scaffolder_refuses_history_symlink_escape(tmp_path, record):
    target = tmp_path / "data/aio/SyntheticConcept.yaml"
    target.parent.mkdir(parents=True)
    target.write_text(yaml.safe_dump(record))
    outside = tmp_path.parent / f"outside-{tmp_path.name}"
    outside.mkdir()
    (tmp_path / "history").symlink_to(outside, target_is_directory=True)
    assert main(new_args(tmp_path)) == 1
    assert list(outside.iterdir()) == []


@pytest.mark.parametrize("alias", ["history", "history/records", "history/records/SyntheticConcept"])
def test_scaffolder_rejects_in_repository_ancestor_aliases(tmp_path, record, alias):
    target = tmp_path / "data/aio/SyntheticConcept.yaml"
    target.parent.mkdir(parents=True)
    target.write_text(yaml.safe_dump(record))
    before = target.read_bytes()
    archive = tmp_path / "archive"
    archive.mkdir()
    link = tmp_path / alias
    link.parent.mkdir(parents=True, exist_ok=True)
    link.symlink_to(archive, target_is_directory=True)
    assert main(new_args(tmp_path)) == 1
    assert list(archive.rglob("*")) == []
    assert target.read_bytes() == before


def test_validate_history_reports_bad_yaml_and_does_not_skip_yml(tmp_path, history, capsys):
    path = write_history(tmp_path, history)
    (path.parent / "bad.yml").write_text("session: [\n")
    assert main(["validate-history", "--repo-root", str(tmp_path)]) == 1
    assert "2 history record(s)" in capsys.readouterr().out


def test_validate_history_rejects_duplicate_yaml_keys(tmp_path, history):
    path = write_history(tmp_path, history)
    path.write_text(path.read_text() + "history_version: 1\n")
    assert main(["validate-history", "--repo-root", str(tmp_path)]) == 1


def test_validate_history_rejects_malformed_scalars(tmp_path):
    folder = tmp_path / "history"
    folder.mkdir()
    (folder / "bad.yaml").write_text("null\n")
    assert main(["validate-history", "--repo-root", str(tmp_path)]) == 1


@pytest.mark.parametrize("alias", ["history", "history/records", "history/records/SyntheticConcept"])
def test_discovery_rejects_ancestor_directory_aliases(tmp_path, history, alias, capsys):
    write_history(tmp_path, history)
    link = tmp_path / alias
    archive = tmp_path / "archive"
    link.rename(archive)
    link.symlink_to(archive, target_is_directory=True)
    assert main(["validate-history", "--repo-root", str(tmp_path)]) == 1
    assert "must not contain a symlink" in capsys.readouterr().out


def test_discovery_rejects_dangling_links(tmp_path, capsys):
    directory = tmp_path / "history"
    directory.mkdir()
    (directory / "missing").symlink_to(tmp_path / "not-present", target_is_directory=True)
    assert main(["validate-history", "--repo-root", str(tmp_path)]) == 1
    assert "must not contain a symlink" in capsys.readouterr().out


def test_history_backing_outside_a_symlinked_history_tree_cannot_bypass_git_guard(tmp_path, history):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True, capture_output=True)
    path = write_history(tmp_path, history)
    (tmp_path / "history").rename(tmp_path / "archive")
    (tmp_path / "history").symlink_to(tmp_path / "archive", target_is_directory=True)
    target = tmp_path / history["target"]["path"]
    target.parent.mkdir(parents=True)
    target.write_text("Synthetic target.\n")
    git_commit(tmp_path, "alias fixture")
    backing = tmp_path / "archive" / path.relative_to(tmp_path / "history")
    backing.write_text(backing.read_text().replace("Synthetic check", "Altered historical claim"))
    assert append_only_errors(tmp_path, "HEAD") == []  # Git sees only the unchanged history link.
    assert main(["validate-history", "--repo-root", str(tmp_path), "--base", "HEAD"]) == 1


def test_valid_yml_content_is_still_checked_for_canonical_filename(tmp_path, history, capsys):
    path = write_history(tmp_path, history)
    path.rename(path.with_suffix(".yml"))
    assert main(["validate-history", "--repo-root", str(tmp_path)]) == 1
    assert "history path must match" in capsys.readouterr().out


def test_same_session_id_cannot_reappear_for_a_different_target(tmp_path, history, capsys):
    write_history(tmp_path, history)
    history["target"]["slug"] = "another"
    history["target"]["path"] = "data/aio/another.yaml"
    write_history(tmp_path, history)
    assert main(["validate-history", "--repo-root", str(tmp_path)]) == 1
    assert "duplicate history session" in capsys.readouterr().out


def test_append_only_comparison_detects_edits_and_deletions(tmp_path, history):
    path = write_history(tmp_path, history)
    def git(*args):
        return subprocess.run(["git", *args], cwd=tmp_path, check=True, capture_output=True)

    git("init", "-q")
    git("add", "history")
    git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "base")
    assert append_only_errors(tmp_path, "HEAD") == []
    path.write_text(path.read_text() + "# changed after publication\n")
    assert "append-only" in append_only_errors(tmp_path, "HEAD")[0]
    path.unlink()
    assert "D " in append_only_errors(tmp_path, "HEAD")[0]
    new = copy.deepcopy(history)
    new["session"]["id"] = "2026-10-07T120000Z-tester-456def"
    write_history(tmp_path, new)
    assert len(append_only_errors(tmp_path, "HEAD")) == 1  # The deletion, never the new session.
    assert "cannot compare" in append_only_errors(tmp_path, "missing-revision")[0]


def git_commit(root, message):
    subprocess.run(["git", "add", "."], cwd=root, check=True, capture_output=True)
    subprocess.run(["git", "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                    "commit", "-qm", message], cwd=root, check=True, capture_output=True)


def test_history_base_environment_is_used_unless_explicitly_overridden(
    tmp_path, history, monkeypatch, capsys,
):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True, capture_output=True)
    path = write_history(tmp_path, history)
    target = tmp_path / history["target"]["path"]
    target.parent.mkdir(parents=True)
    target.write_text("Synthetic target.\n")
    git_commit(tmp_path, "reviewed baseline")
    baseline = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=tmp_path, text=True,
    ).strip()
    path.write_text(path.read_text().replace("Synthetic check", "Rewritten historical claim"))
    git_commit(tmp_path, "committed rewrite")
    monkeypatch.setenv("AIMECH_HISTORY_BASE", baseline)
    args = ["validate-history", "--repo-root", str(tmp_path)]
    assert main(args) == 1
    assert "history is append-only" in capsys.readouterr().out
    # A CLI flag takes precedence over the environment. The exact same committed
    # bytes have no diff from HEAD, while the environment's reviewed base does.
    assert main(args + ["--base", "HEAD"]) == 0


def test_new_imported_history_must_identify_an_existing_target(tmp_path, history, capsys):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True, capture_output=True)
    (tmp_path / "README").write_text("Synthetic history test.\n")
    git_commit(tmp_path, "base")
    write_history(tmp_path, history)
    args = ["validate-history", "--repo-root", str(tmp_path)]
    assert main(args) == 0  # Standalone validation cannot infer a reviewed Git baseline.
    assert main(args + ["--base", "HEAD"]) == 1
    assert "new history target must be an existing file" in capsys.readouterr().out
    target = tmp_path / history["target"]["path"]
    target.parent.mkdir(parents=True)
    target.mkdir()  # A directory with a YAML filename still is not a target file.
    assert main(args + ["--base", "HEAD"]) == 1
    target.rmdir()
    target.write_text("Synthetic target content; validity is checked by the domain gate.\n")
    assert main(args + ["--base", "HEAD"]) == 0


def test_immutable_history_remains_valid_after_its_historical_target_is_removed(tmp_path, history):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True, capture_output=True)
    path = write_history(tmp_path, history)
    target = tmp_path / history["target"]["path"]
    target.parent.mkdir(parents=True)
    target.write_text("Synthetic historical target.\n")
    git_commit(tmp_path, "reviewed historical session")
    before = path.read_bytes()
    target.unlink()
    assert main(["validate-history", "--repo-root", str(tmp_path), "--base", "HEAD"]) == 0
    assert path.read_bytes() == before


def test_absent_default_history_is_allowed_but_explicit_missing_path_fails(tmp_path):
    assert main(["validate-history", "--repo-root", str(tmp_path)]) == 0
    assert main(["validate-history", "--repo-root", str(tmp_path), "history/missing"]) == 1


def test_explicit_empty_base_cannot_disable_integrity_check(tmp_path):
    assert main(["validate-history", "--repo-root", str(tmp_path), "--base", ""]) == 1


def test_generation_requires_explicit_event_and_outcome(tmp_path):
    args = new_args(tmp_path)
    for flag in ("--event", "--outcome"):
        selected = list(args)
        index = selected.index(flag)
        del selected[index:index + 2]
        with pytest.raises(SystemExit) as error:
            main(selected)
        assert error.value.code == 2
