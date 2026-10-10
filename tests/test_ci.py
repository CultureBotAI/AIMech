"""Protect the unconditional local/CI gate and its trusted review baseline."""

import importlib.util
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / f"scripts/{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ci_runs_unconditionally_with_trusted_fetched_base_and_locked_environment():
    workflow = yaml.safe_load((ROOT / ".github/workflows/validate-strict.yaml").read_text())
    triggers = workflow.get("on", workflow.get(True))  # YAML 1.1 interprets 'on' as boolean.
    assert set(triggers) == {"pull_request", "push", "merge_group"}
    assert triggers["push"] == {"branches": ["main"]}
    assert triggers["merge_group"] == {"types": ["checks_requested"]}
    job = workflow["jobs"]["validate-strict"]
    assert "if" not in job
    assert job["env"]["RECORD_REVIEW_BASE"] == (
        "${{ github.event.pull_request.base.sha || "
        "github.event.merge_group.base_sha || github.event.before }}"
    )
    steps = job["steps"]
    assert all("if" not in step and not step.get("continue-on-error") for step in steps)
    checkout = next(s for s in steps if s.get("uses", "").startswith("actions/checkout@"))
    assert checkout["with"]["persist-credentials"] is False
    assert checkout["with"]["fetch-depth"] == 0
    runs = [step["run"] for step in steps if "run" in step]
    assert any('git fetch --no-tags origin "$RECORD_REVIEW_BASE"' in run for run in runs)
    assert "uv sync --locked --extra dev" in runs
    setup_just = next(s for s in steps if s.get("uses", "").startswith("extractions/setup-just@"))
    assert len(setup_just["uses"].split("@", 1)[1]) == 40
    assert setup_just["with"]["just-version"]
    assert "just check" in runs
    assert "just vendored-check" in runs
    assert runs.index("just vendored-check") > runs.index("just check")
    assert "uv run --locked --extra dev python scripts/check.py" in (ROOT / "justfile").read_text()


def test_standard_recipes_keep_the_supported_checkers():
    recipes = (ROOT / "justfile").read_text()
    assert "vendored-check:\n    bash scripts/check_vendored_sync.sh" in recipes
    assert "test:\n    uv run --locked --extra dev pytest -q" in recipes
    assert "lint:\n    uv run --locked --extra dev ruff check src tests scripts" in recipes
    assert ("review-check *args:\n    uv run --locked python "
            "scripts/record_review.py check {{args}}") in recipes


@pytest.mark.parametrize("environment", [
    {"RECORD_REVIEW_BASE": ""},
    {"RECORD_REVIEW_BASE": " "},
    {"CI": "true"},
    {"CI": "true", "RECORD_REVIEW_BASE": "HEAD"},
])
def test_check_refuses_a_missing_ci_baseline_before_running_commands(environment):
    with pytest.raises(ValueError, match="trusted event base"):
        load_script("check").commands(environment)


def test_all_integrity_checks_use_the_same_event_base(monkeypatch):
    check = load_script("check")
    baseline = "a" * 40
    monkeypatch.setenv("RECORD_REVIEW_BASE", baseline)
    seen = []

    def run(command, **kwargs):
        assert kwargs["cwd"] == ROOT
        seen.append(command)
        return subprocess.CompletedProcess(command, 0)

    monkeypatch.setattr(check.subprocess, "run", run)
    assert check.main() == 0
    assert seen[-2][-3:] == ["validate-history", "--base", baseline]
    assert seen[-1][-3:] == ["check", "--base", baseline]
    assert any(command[-2:] == ["seed", "--check"] for command in seen)
    assert any(command[-2:] == ["aimech", "validate"] for command in seen)


def test_seed_drift_fails_the_local_gate(monkeypatch):
    check = load_script("check")
    monkeypatch.setenv("RECORD_REVIEW_BASE", "a" * 40)
    seen = []

    def run(command, **kwargs):
        seen.append(command)
        return subprocess.CompletedProcess(command, 1 if command[-2:] == ["seed", "--check"] else 0)

    monkeypatch.setattr(check.subprocess, "run", run)
    assert check.main() == 1
    assert seen[-1][-2:] == ["seed", "--check"]


def test_missing_review_base_is_an_error_even_without_reports(tmp_path):
    reviews = load_script("record_review")
    assert reviews.main(["--repo-root", str(tmp_path), "check", "--base", ""]) == 1
