"""AIMech's local, offline command interface."""

import argparse
from pathlib import Path

import yaml

from aimech.history import validate_references
from aimech.importer import load_source, seed
from aimech.validation import read_record, record_validator, validate_record


def validate(paths):
    record_validator()
    selected = set()
    for path in paths:
        if not path.exists():
            raise ValueError(f"path does not exist: {path}")
        if path.is_dir():
            selected.update(p for p in path.rglob("*") if p.suffix in {".yaml", ".yml"})
        else:
            selected.add(path)
    if not selected:
        raise ValueError("no records found")
    failed, identifiers = 0, set()
    for path in sorted(selected):
        try:
            record = read_record(path)
            errors = validate_record(record)
            if not errors:
                errors.extend(validate_references(record, path, Path.cwd()))
            if not errors:
                if record["id"] in identifiers:
                    errors.append(f"duplicate record ID: {record['id']}")
                identifiers.add(record["id"])
        except (OSError, UnicodeError, yaml.YAMLError) as exc:
            errors = [str(exc)]
        if errors:
            failed += 1
            for error in errors:
                print(f"ERROR {path}: {error}")
    print(f"Checked {len(selected)} record(s); {failed} failed.")
    return int(failed > 0)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="aimech")
    commands = parser.add_subparsers(dest="command", required=True)
    validator = commands.add_parser("validate")
    validator.add_argument("paths", nargs="*", type=Path)
    importer = commands.add_parser("seed", help="reproduce AIO records offline; dry run by default")
    modes = importer.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true")
    modes.add_argument("--write", action="store_true")
    commands.add_parser("check-source", help="check the pinned source checksum and release")
    commands.add_parser("validate-curated", help="validate maintained concepts and AIO mappings")
    from aimech.history import add_commands
    add_commands(commands)
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            return validate(args.paths or [Path("data/aio")])
        if args.command == "seed":
            return seed(Path.cwd(), check=args.check, write=args.write)
        if args.command == "check-source":
            source, _ = load_source(Path.cwd())
            print(f"Verified AIO {source['version_iri']} at {source['commit']}")
            return 0
        if args.command == "validate-curated":
            from aimech.curated import validate_curated
            return validate_curated(Path.cwd())
        return args.handler(args)
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
