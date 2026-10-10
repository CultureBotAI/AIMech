"""AIMech-owned adapter for the vendored, canonical HistoryRecord contract.

The adapter creates sidecars only; generated AIO records are never reserialized.
Adapted from CMMMech history.py under BSD-3-Clause (notice retained below).
"""

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

import argparse
import datetime as dt
import os
import re
import secrets
import subprocess
import tempfile
from pathlib import Path, PurePosixPath

import yaml
from jsonschema import FormatChecker

from aimech.validation import read_record, schema_validator

# Directory vocabulary defined by CLAW's kg_microbe_history scaffold contract.
KIND_DIRS = {
    "record": "records", "schema": "schema", "mapping": "mappings",
    "report": "reports", "infrastructure": "infrastructure", "other": "other",
}
REPO_URL = "https://github.com/CultureBotAI/AIMech"
PLACEHOLDER = "TODO: replace this placeholder"


def history_validator():
    return schema_validator("history.yaml", "HistoryRecord")


def safe_relative(value: str, root: Path) -> Path:
    """Accept canonical repository paths, including no symlink escape."""
    path = PurePosixPath(value)
    if (not value or path.is_absolute() or ".." in path.parts or "\\" in value
            or str(path) != value or path == PurePosixPath(".")):
        raise ValueError(f"not a canonical repository-relative path: {value!r}")
    resolved = (root / value).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError(f"path escapes repository through a symlink: {value!r}")
    return root.resolve() / value


def check_history_path(path: Path, root: Path) -> None:
    """History must be physically under its Git-audited tree, without aliases."""
    root = root.resolve()
    try:
        relative = path.absolute().relative_to(root)
    except ValueError as exc:
        raise ValueError(f"history path is outside the repository: {path}") from exc
    if not relative.parts or relative.parts[0] != "history" or ".." in relative.parts:
        raise ValueError(f"history path must be under the repository's history directory: {path}")
    current = root
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            raise ValueError(f"history path must not contain a symlink: {current}")


def validate_history(data, path: Path, root: Path) -> list[str]:
    try:
        check_history_path(path, root)
    except ValueError as exc:
        return [str(exc)]
    errors = [
        f"{'/'.join(map(str, error.absolute_path)) or '$'}: {error.message}"
        for error in history_validator().iter_errors(data)
    ]
    if errors:
        return sorted(errors)
    if data["history_version"] != 1:
        errors.append("history_version: only version 1 is supported")
    target, session = data["target"], data["session"]
    slug = target.get("slug", "")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", slug):
        errors.append("target/slug: a filename-safe slug is required")
    try:
        safe_relative(target["path"], root)
    except ValueError as exc:
        errors.append(f"target/path: {exc}")
    expected = root / "history" / KIND_DIRS[target["kind"]] / slug / f"{session['id']}.yaml"
    if path.absolute() != expected.absolute() or path.is_symlink():
        errors.append("history path must match kind, slug, and session id without a symlink")
    timestamp = session["timestamp"]
    if not FormatChecker().conforms(timestamp, "date-time"):
        errors.append("session/timestamp: invalid calendar date or timezone")
    else:
        parsed = dt.datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        if parsed.utcoffset() != dt.timedelta(0):
            errors.append("session/timestamp: use UTC")
        prefix = parsed.strftime("%Y-%m-%dT%H%M%SZ-")
        if not re.fullmatch(re.escape(prefix) + r"[a-z0-9]+(?:-[a-z0-9]+)*-[0-9a-f]{6}",
                            session["id"]):
            errors.append("session/id: expected timestamp-actor-six_hex_chars")
    for index, actor in enumerate(session["actors"]):
        if not actor["name"].strip():
            errors.append(f"session/actors/{index}/name: must be nonempty")
        if actor["type"] == "ai_agent" and not all(
            actor.get(key, "").strip() for key in ("model", "agent_tool")
        ):
            errors.append(f"session/actors/{index}: AI agents require model and agent_tool")
    for index, event in enumerate(data["events"]):
        for key in ("summary", "details"):
            if not event[key].strip() or event[key].lstrip().startswith(PLACEHOLDER):
                errors.append(f"events/{index}/{key}: blank or unfilled placeholder")
    return sorted(errors)


def read_history(path: Path, root: Path) -> tuple[object, list[str]]:
    try:
        check_history_path(path, root)  # Refuse alias reads before opening the document.
        data = read_record(path)
        return data, validate_history(data, path, root)
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
        return None, [str(exc)]


def validate_references(record: dict, record_path: Path, root: Path) -> list[str]:
    """Validate explicit links without adding them to generated records."""
    errors = []
    for reference in record.get("history_refs", []):
        try:
            path = safe_relative(reference, root)
        except ValueError as exc:
            errors.append(f"history_refs: {exc}")
            continue
        data, problems = read_history(path, root.resolve())
        errors.extend(f"history_refs/{reference}: {problem}" for problem in problems)
        if problems:
            continue
        target = data["target"]
        if (target["kind"] != "record" or target["slug"] != record["id"].split(":", 1)[1]
                or safe_relative(target["path"], root) != record_path.resolve()):
            errors.append(f"history_refs/{reference}: target does not match this record")
    return errors


def resolve_base(root: Path, base: str) -> tuple[str, list[str]]:
    revision = subprocess.run(
        ["git", "rev-parse", "--verify", "--end-of-options", f"{base}^{{commit}}"],
        cwd=root, capture_output=True, text=True, check=False,
    )
    if revision.returncode:
        return "", [f"cannot compare history with {base!r}: {revision.stderr.strip()}"]
    return revision.stdout.strip(), []


def append_only_errors(root: Path, base: str) -> list[str]:
    """Reject edits/deletions of sidecars already present in a reviewed base."""
    revision, errors = resolve_base(root, base)
    if errors:
        return errors
    result = subprocess.run(
        ["git", "diff", "--name-status", "--no-renames", "-z", revision,
         "--", "history"],
        cwd=root, capture_output=True, text=True, check=False,
    )
    if result.returncode:
        return [f"cannot compare history with {base!r}: {result.stderr.strip()}"]
    fields = result.stdout.split("\0")
    return [f"history is append-only: {status} {path}; add a correction in a new session"
            for status, path in zip(fields[0::2], fields[1::2])
            if path.endswith((".yaml", ".yml")) and status != "A"]


def new_target_errors(root: Path, base: str, records: list[tuple[Path, dict]]) -> list[str]:
    """New sessions need a current target; retained history can outlive its target."""
    revision, errors = resolve_base(root, base)
    if errors:
        return errors
    for path, data in records:
        if safe_relative(data["target"]["path"], root).is_file():
            continue
        relative = path.relative_to(root).as_posix()
        original = subprocess.run(
            ["git", "cat-file", "-t", f"{revision}:{relative}"],
            cwd=root, capture_output=True, text=True, check=False,
        )
        if original.returncode or original.stdout.strip() != "blob":
            errors.append(f"{relative}: new history target must be an existing file: "
                          f"{data['target']['path']}")
    return errors


def cmd_validate(args: argparse.Namespace) -> int:
    root = args.repo_root.resolve()
    history_validator()  # A missing governed schema must fail even for an empty directory.
    selected = args.paths or ([root / "history"] if (root / "history").exists()
                              or (root / "history").is_symlink() else [])
    paths = set()
    errors = []
    for selected_path in selected:
        path = selected_path if selected_path.is_absolute() else root / selected_path
        try:
            check_history_path(path, root)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if not path.exists():
            errors.append(f"history path does not exist: {path}")
        elif path.is_dir():
            # rglob silently skips symlink directories. Walk without following
            # them and reject every alias explicitly, including dangling links.
            for folder, directories, filenames in os.walk(path, followlinks=False):
                for name in [*directories, *filenames]:
                    item = Path(folder) / name
                    if item.is_symlink():
                        errors.append(f"history path must not contain a symlink: {item}")
                    elif item.is_file() and item.suffix in {".yaml", ".yml"}:
                        paths.add(item)
        else:
            paths.add(path)
    sessions = set()
    valid_records = []
    for path in sorted(paths):
        data, problems = read_history(path, root)
        errors.extend(f"{path}: {problem}" for problem in problems)
        if not problems:
            valid_records.append((path, data))
            session_id = data["session"]["id"]
            if session_id in sessions:
                errors.append(f"duplicate history session id: {session_id}")
            sessions.add(session_id)
    if args.base is not None:
        base_errors = append_only_errors(root, args.base)
        errors.extend(base_errors)
        if not base_errors:
            errors.extend(new_target_errors(root, args.base, valid_records))
    for error in errors:
        print(f"ERROR {error}")
    print(f"Checked {len(paths)} history record(s); {len(errors)} error(s).")
    return int(bool(errors))


def cmd_new(args: argparse.Namespace) -> int:
    root = args.repo_root.resolve()
    try:
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", args.slug):
            raise ValueError("--slug must be a filename-safe identifier")
        target_path = args.path or f"data/aio/{args.slug}.yaml"
        if not args.path and args.kind != "record":
            raise ValueError("--path is required for non-record targets")
        if not safe_relative(target_path, root).is_file():
            raise ValueError(f"target must be an existing file: {target_path}")
        now = dt.datetime.now(dt.timezone.utc)
        timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        actor_token = re.sub(r"[^a-z0-9]+", "-", args.actor_name.lower()).strip("-")
        if not actor_token:
            raise ValueError("--actor-name must contain letters or digits")
        sid = f"{now.strftime('%Y-%m-%dT%H%M%SZ')}-{actor_token}-{secrets.token_hex(3)}"
        relative = f"history/{KIND_DIRS[args.kind]}/{args.slug}/{sid}.yaml"
        path = safe_relative(relative, root)
        check_history_path(path, root)
        actor = {"name": args.actor_name, "type": args.actor_type}
        for key in ("model", "agent_tool", "agent_version"):
            if getattr(args, key):
                actor[key] = getattr(args, key)
        event = {"type": args.event, "outcome": args.outcome,
                 "summary": args.summary, "details": args.details}
        if args.sections:
            event["sections"] = [item.strip() for item in args.sections.split(",") if item.strip()]
        data = {
            "history_version": 1,
            "target": {"kind": args.kind, "slug": args.slug, "path": target_path},
            "session": {"id": sid, "timestamp": timestamp, "actors": [actor]},
            "events": [event],
        }
        links = {}
        for arg, key, prefix in ((args.issue, "issues", "issues"), (args.pr, "prs", "pull")):
            if arg:
                links[key] = [f"{REPO_URL}/{prefix}/{item.lstrip('#')}"
                              if re.fullmatch(r"#?[1-9][0-9]*", item) else item for item in arg]
        if args.url:
            links["urls"] = args.url
        if links:
            data["links"] = links
        problems = validate_history(data, path, root)
        if problems:
            raise ValueError("; ".join(problems))
        path.parent.mkdir(parents=True, exist_ok=True)
        # Link a complete temporary file atomically; linking never overwrites an
        # existing name. A collision or interruption cannot truncate an old session.
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=".new-history-", suffix=".tmp") as stream:
            yaml.safe_dump(data, stream, sort_keys=False, allow_unicode=True, width=88)
            stream.flush()
            os.fsync(stream.fileno())
            os.link(stream.name, path)
        print(relative)
        return 0
    except (OSError, ValueError) as exc:
        print(f"ERROR {exc}")
        return 1


def add_commands(commands) -> None:
    validate = commands.add_parser("validate-history", help="validate canonical history sidecars")
    validate.add_argument("paths", nargs="*", type=Path)
    validate.add_argument("--repo-root", type=Path, default=Path("."))
    validate.add_argument("--base", default=os.environ.get("AIMECH_HISTORY_BASE"),
                          help="Git base revision for append-only comparison")
    validate.set_defaults(handler=cmd_validate)
    new = commands.add_parser("new-history", help="record an actual session without editing its target")
    new.add_argument("--repo-root", type=Path, default=Path("."))
    new.add_argument("--kind", choices=sorted(KIND_DIRS), default="record")
    new.add_argument("--slug", required=True)
    new.add_argument("--path", default="")
    new.add_argument("--event", choices=("GENERAL", "CREATE", "EDIT", "REVIEW", "AUDIT"),
                     required=True)
    new.add_argument("--outcome", choices=("changed", "no_change", "needs_followup", "blocked"),
                     required=True)
    new.add_argument("--summary", required=True)
    new.add_argument("--details", required=True)
    new.add_argument("--sections", default="")
    new.add_argument("--actor-name", required=True)
    new.add_argument("--actor-type", choices=("human", "ai_agent", "automation", "other"),
                     required=True)
    for name in ("model", "agent-tool", "agent-version"):
        new.add_argument(f"--{name}", default="")
    for name in ("issue", "pr", "url"):
        new.add_argument(f"--{name}", action="append", default=[])
    new.set_defaults(handler=cmd_new)
