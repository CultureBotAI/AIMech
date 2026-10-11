"""Run the same strict, offline gate locally and in CI."""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def commands(environment):
    base = environment.get("RECORD_REVIEW_BASE", "HEAD")
    if not base.strip() or (environment.get("CI") == "true" and base == "HEAD"):
        raise ValueError("RECORD_REVIEW_BASE must identify the trusted event base in CI")
    return [
        [sys.executable, "-m", "ruff", "check", "src", "tests", "scripts"],
        [sys.executable, "-m", "pytest", "-q"],
        [sys.executable, "-m", "aimech", "validate"],
        [sys.executable, "-m", "aimech", "validate-curated"],
        [sys.executable, "-m", "aimech", "seed", "--check"],
        [sys.executable, "-m", "aimech", "validate-history", "--base", base],
        [sys.executable, "scripts/record_review.py", "check", "--base", base],
    ]


def main():
    try:
        checks = commands(os.environ)
    except ValueError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1
    for command in checks:
        result = subprocess.run(command, cwd=ROOT, check=False)
        if result.returncode:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
