"""Prepare historical review commits before running the unchanged offline gate."""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

from record_review import ReviewError, load_document, read_bytes, review_paths

ROOT = Path(__file__).resolve().parents[1]


def review_revisions(root):
    """Read every bundle, including ignored ones, before fetching anything."""
    revisions = set()
    for path in review_paths(root):
        document = load_document(read_bytes(root, path))
        source = document.get("source")
        revision = source.get("git_revision") if isinstance(source, dict) else None
        if (not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40}", revision)
                or revision == "0" * 40):
            raise ReviewError(f"{path}: source.git_revision must be a full nonzero commit ID")
        revisions.add(revision)
    return sorted(revisions)


def git(root, *args):
    return subprocess.run(
        ["git", "-C", str(root), *args], text=True, capture_output=True, timeout=60,
        env={**os.environ, "GIT_TERMINAL_PROMPT": "0", "GIT_NO_LAZY_FETCH": "1"},
    )


def require_success(result):
    if result.returncode:
        raise ReviewError(result.stderr.strip() or "Git operation failed")


def prepare_bases(root):
    revisions = review_revisions(root)
    fetched = []
    for revision in revisions:
        present = git(root, "cat-file", "-t", revision)
        if present.returncode:
            result = git(root, "fetch", "--no-tags", "--no-write-fetch-head",
                         "--no-recurse-submodules", "origin", revision)
            require_success(result)
            present = git(root, "cat-file", "-t", revision)
            fetched.append(revision)
        require_success(present)
        if present.stdout.strip() != "commit":
            raise ReviewError(f"{revision}: review source must identify a commit object")
        # Retain historical objects even after their original branch is deleted.
        # This namespace never changes the checkout, branches, tags or review bytes.
        require_success(git(root, "update-ref", f"refs/aimech/review-bases/{revision}", revision))
    return revisions, fetched


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    try:
        revisions, fetched = prepare_bases(args.repo_root.resolve())
    except (OSError, subprocess.TimeoutExpired, ReviewError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1
    print(f"Prepared {len(revisions)} review base(s); fetched {len(fetched)} missing commit(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
