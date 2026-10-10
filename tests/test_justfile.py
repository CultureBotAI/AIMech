"""Exercise recipe argument forwarding through just and its real shell."""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(("recipe", "command"), [
    ("validate", ["aimech", "validate"]),
    ("seed", ["aimech", "seed"]),
    ("new-history", ["aimech", "new-history"]),
    ("validate-history", ["aimech", "validate-history"]),
    ("check-reviews", ["python", "scripts/record_review.py", "check"]),
    ("review-check", ["python", "scripts/record_review.py", "check"]),
])
@pytest.mark.parametrize("arguments", [
    [],
    ["--summary", "Created an AIO record", "--details",
     "Quotes 'single' \"double\" (parentheses); $(printf expanded) `printf expanded` *",
     "--path", "folder with spaces/record.yaml", "--details", "line one\nline two",
     "--actor-name", "René α", "--model", ""],
])
def test_recipe_preserves_literal_arguments(tmp_path, recipe, command, arguments):
    just = shutil.which("just")
    assert just, "Install just to run recipe integration tests (also required by CI)."
    (tmp_path / "justfile").write_bytes((ROOT / "justfile").read_bytes())
    # Replace only uv: just still parses the production recipe and invokes bash.
    stub = tmp_path / "uv"
    stub.write_text(
        f"#!{sys.executable}\nimport json, sys\nprint(json.dumps(sys.argv[1:]))\n"
    )
    stub.chmod(0o755)
    environment = dict(os.environ, PATH=str(tmp_path) + os.pathsep + os.environ["PATH"])
    result = subprocess.run(
        [just, "--justfile", str(tmp_path / "justfile"), recipe, *arguments],
        env=environment, text=True, capture_output=True, check=False,
    )
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout) == ["run", "--locked", *command, *arguments]
