#!/usr/bin/env python3
"""Write every AIMech record, complete, as one deterministic JSON Lines export.

Usage:
    python scripts/export_records.py --out DIR [--commit SHA]

Each record under data/curated/ and data/aio/ becomes one JSON object per line,
exactly as its YAML file states it, sorted by id and gzip-compressed with a zero
timestamp, so the same records always produce the same bytes. manifest.json
beside it gives the record counts and the SHA-256 of the compressed and the
uncompressed bytes.

The Pages workflow runs this at deploy time into the uploaded artifact
(.github/workflows/pages.yaml), so the export always matches the deployed
commit's records. Its output is never committed.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
RECORD_DIRS = (("curated", "data/curated"), ("aio", "data/aio"))
RECORDS_FILE = "aimech-records.jsonl.gz"
MANIFEST_FILE = "manifest.json"
# What LICENSE and LICENSE-DATA say, and no more: the repository states no
# licence for the curated concepts.
LICENCES = {
    "code": "BSD-3-Clause (LICENSE)",
    "data/aio": "CC-BY-4.0, attributed to the Artificial Intelligence Ontology authors (LICENSE-DATA)",
    "data/curated": "no licence is stated in the repository",
}


def load_records(root: Path = REPO_ROOT) -> list[tuple[str, dict[str, Any]]]:
    """(origin, record) for every record file, in id order.

    libyaml is used when PyYAML has it; it returns the same documents as
    SafeLoader for this corpus and is roughly nine times faster.
    """
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    records = []
    for origin, directory in RECORD_DIRS:
        for path in sorted((root / directory).glob("*.yaml")):
            with path.open(encoding="utf-8") as handle:
                doc = yaml.load(handle, Loader=loader)
            if not isinstance(doc, dict) or not doc.get("id"):
                raise ValueError(f"{path.relative_to(root)}: not a record with an id")
            records.append((origin, doc))
    ids = [doc["id"] for _, doc in records]
    if len(set(ids)) != len(ids):
        raise ValueError("duplicate record ids")
    return sorted(records, key=lambda item: item[1]["id"])


def export(out_dir: Path, *, commit: str | None = None, root: Path = REPO_ROOT) -> dict[str, Any]:
    """Write the gzip-compressed JSON Lines file and its manifest; return the manifest."""
    records = load_records(root)
    lines = "".join(
        json.dumps(doc, ensure_ascii=False, separators=(",", ":")) + "\n" for _, doc in records
    ).encode("utf-8")
    buffer = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buffer, compresslevel=9, mtime=0) as gz:
        gz.write(lines)
    compressed = buffer.getvalue()
    counts = {origin: sum(1 for o, _ in records if o == origin) for origin, _ in RECORD_DIRS}
    manifest = {
        "file": RECORDS_FILE,
        "format": "JSON Lines, gzip-compressed: one complete record per line, sorted by id",
        "records": len(records),
        "counts": counts,
        "bytes": len(compressed),
        "sha256": hashlib.sha256(compressed).hexdigest(),
        "uncompressed_bytes": len(lines),
        "uncompressed_sha256": hashlib.sha256(lines).hexdigest(),
        "sources": [f"{directory}/*.yaml" for _, directory in RECORD_DIRS],
        "schemas": {
            "curated": "src/aimech/schema/curated_concept.yaml",
            "aio": "src/aimech/schema/aimech.yaml",
        },
        "licences": LICENCES,
        "commit": commit,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / RECORDS_FILE).write_bytes(compressed)
    (out_dir / MANIFEST_FILE).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", type=Path, required=True, help="directory to write into")
    parser.add_argument("--commit", help="the commit the export was built from")
    args = parser.parse_args(argv)
    try:
        manifest = export(args.out, commit=args.commit)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1
    print(f"Wrote {manifest['records']} records to {args.out / RECORDS_FILE} "
          f"(sha256 {manifest['sha256']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
