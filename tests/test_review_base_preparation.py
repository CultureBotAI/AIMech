"""Exercise missing review provenance after squash and feature-branch deletion."""

import importlib.util
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def preparation(monkeypatch):
    monkeypatch.syspath_prepend(str(ROOT / "scripts"))
    spec = importlib.util.spec_from_file_location(
        "fetch_review_bases", ROOT / "scripts/fetch_review_bases.py",
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], stderr=subprocess.PIPE,
                                   text=True).strip()


def bundle(root, name, revision):
    directory = root / "reviews/structured" / name
    directory.mkdir(parents=True)
    (directory / "review.yaml").write_text(yaml.safe_dump({"source": {"git_revision": revision}}))
    (directory / "review.md").write_text("Fixture for retrieval, not a validated review.\n")


@pytest.fixture
def deleted_branch(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    git(source, "init", "-b", "main")
    git(source, "config", "user.name", "Review fixture")
    git(source, "config", "user.email", "fixture@example.invalid")
    (source / "file").write_text("initial\n")
    git(source, "add", "file")
    git(source, "commit", "-m", "Initial")
    git(source, "switch", "-c", "feature")
    (source / "file").write_text("feature\n")
    git(source, "commit", "-am", "Historical review base")
    historical = git(source, "rev-parse", "HEAD")
    git(source, "update-ref", "refs/pull/1/head", historical)
    git(source, "switch", "main")
    git(source, "merge", "--squash", "feature")
    git(source, "commit", "-m", "Squash feature")
    git(source, "branch", "-D", "feature")
    clone = tmp_path / "clone"
    subprocess.run(["git", "clone", "--no-local", "--single-branch", "--no-tags",
                    str(source), str(clone)], capture_output=True, check=True)
    return clone, historical


def test_recovers_deleted_branch_base_and_retains_it_without_changing_worktree(
    preparation, deleted_branch,
):
    clone, historical = deleted_branch
    assert preparation.git(clone, "cat-file", "-e", historical).returncode != 0
    (clone / ".gitignore").write_text("reviews/structured/\n")
    bundle(clone, "ignored-review", historical)
    bundle(clone, "same-base", historical)
    before = git(clone, "status", "--porcelain"), git(clone, "rev-parse", "HEAD")
    review_bytes = (clone / "reviews/structured/ignored-review/review.yaml").read_bytes()
    revisions, fetched = preparation.prepare_bases(clone)
    assert revisions == fetched == [historical]
    assert git(clone, "cat-file", "-t", historical) == "commit"
    assert git(clone, "rev-parse", f"refs/aimech/review-bases/{historical}") == historical
    assert (git(clone, "status", "--porcelain"), git(clone, "rev-parse", "HEAD")) == before
    assert (clone / "reviews/structured/ignored-review/review.yaml").read_bytes() == review_bytes
    assert preparation.prepare_bases(clone) == ([historical], [])


@pytest.mark.parametrize("bad_revision", ["--upload-pack=untrusted", "HEAD", "0" * 40, None])
def test_rejects_all_bad_revisions_before_git_operations(preparation, tmp_path, monkeypatch,
                                                        bad_revision):
    bundle(tmp_path, "a-valid-first", "a" * 40)
    bundle(tmp_path, "z-invalid-later", bad_revision)
    def unexpected(*args):
        pytest.fail("Git must not run until every revision has been validated")
    monkeypatch.setattr(preparation, "git", unexpected)
    with pytest.raises(preparation.ReviewError, match="full nonzero commit"):
        preparation.prepare_bases(tmp_path)


def test_unavailable_commit_fails_and_is_not_retained(preparation, deleted_branch):
    clone, _ = deleted_branch
    missing = "f" * 40
    bundle(clone, "unavailable", missing)
    assert preparation.main(["--repo-root", str(clone)]) == 1
    assert preparation.git(clone, "show-ref", "--verify",
                           f"refs/aimech/review-bases/{missing}").returncode != 0


def test_blob_cannot_masquerade_as_a_review_commit(preparation, deleted_branch):
    clone, _ = deleted_branch
    blob = git(clone, "rev-parse", "HEAD:file")
    bundle(clone, "wrong-type", blob)
    with pytest.raises(preparation.ReviewError, match="commit object"):
        preparation.prepare_bases(clone)
