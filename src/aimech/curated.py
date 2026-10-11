"""Validate maintained concepts separately from the deterministic AIO projection."""

import os
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

import yaml

from aimech.history import validate_references
from aimech.importer import AIO, load_source
from aimech.validation import read_record, schema_validator


def normalized_name(value):
    return re.sub(r"[^a-z0-9]", "", value.casefold())


def validate_curated_record(record):
    """Closed schema plus claim/source semantics; no network truth claims."""
    validator = schema_validator("curated_concept.yaml", "CuratedAIConcept")
    errors = [f"{'/'.join(map(str, e.absolute_path)) or '$'}: {e.message}"
              for e in validator.iter_errors(record)]
    if errors:
        return sorted(errors)
    sources = {s["source_id"]: s for s in record["evidence_sources"]}
    if len(sources) != len(record["evidence_sources"]):
        errors.append("evidence_sources: duplicate source_id")
    claim_ids = [c["claim_id"] for c in record["claims"]]
    if len(set(claim_ids)) != len(claim_ids):
        errors.append("claims: duplicate claim_id")
    names = [record["name"], *record.get("aliases", [])]
    if len({normalized_name(name) for name in names}) != len(names):
        errors.append("name/aliases: duplicate normalized identity")
    if any(not normalized_name(name) for name in names):
        errors.append("name/aliases: identity must contain letters or digits")
    mappings = [m["target"] for m in record.get("aio_mappings", [])]
    no_match = record.get("aio_no_match")
    if bool(mappings) == bool(no_match):
        errors.append("provide exactly one of aio_mappings or aio_no_match")
    if len(set(mappings)) != len(mappings):
        errors.append("aio_mappings: duplicate or contradictory target mapping")
    if no_match:
        examined = [item["target"] for item in no_match["examined_targets"]]
        if len(set(examined)) != len(examined):
            errors.append("aio_no_match: duplicate examined target")
    cited = set()

    def check_citations(citations, location, require_full=False):
        supporting = []
        for citation in citations:
            sid = citation["source_id"]
            if sid not in sources:
                errors.append(f"{location}: unresolved evidence source {sid}")
                continue
            cited.add(sid)
            if citation["relation"] == "supports":
                supporting.append(sources[sid])
        if not supporting:
            errors.append(f"{location}: an asserted claim needs supporting evidence")
        elif require_full and not any(s["access_level"] != "abstract_only" for s in supporting):
            errors.append(f"{location}: inspect full text or documentation; abstract-only support")

    check_citations(record["definition_evidence"], "definition_evidence", require_full=True)
    for claim in record["claims"]:
        location = f"claims/{claim['claim_id']}"
        check_citations(claim["evidence"], location, require_full=True)
        if claim["kind"] == "performance" and not claim.get("evaluation"):
            errors.append(f"{location}: performance requires evaluation context")
        if claim["kind"] != "performance" and "evaluation" in claim:
            errors.append(f"{location}: evaluation context belongs to a performance claim")
    if set(sources) - cited:
        errors.append("evidence_sources: uncited sources " + ", ".join(sorted(set(sources) - cited)))
    provenance = record["curation"]
    if provenance["method"] == "ai_assisted" and not all(
        provenance.get(key, "").strip() for key in ("model", "agent_tool")
    ):
        errors.append("curation: AI-assisted writes require model and agent_tool")
    stamps = [provenance["created_at"], provenance["updated_at"]]
    stamps.extend(s["accessed_at"] for s in sources.values())
    for stamp in stamps:
        try:
            parsed = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
            if parsed > datetime.now(timezone.utc):
                errors.append(f"timestamp is in the future: {stamp}")
        except ValueError:
            errors.append(f"invalid calendar timestamp: {stamp}")
    if provenance["updated_at"] < provenance["created_at"]:
        errors.append("curation: updated_at precedes created_at")
    for source in sources.values():
        url = urlsplit(source["url"])
        if url.scheme not in {"http", "https"} or not url.netloc:
            errors.append(f"evidence_sources/{source['source_id']}: expected an HTTP(S) source URL")
        if source["accessed_at"] > provenance["updated_at"]:
            errors.append(f"evidence_sources/{source['source_id']}: access postdates curation")
        if ((source["source_type"] == "official_documentation")
                != (source["access_level"] == "documentation")):
            errors.append(f"evidence_sources/{source['source_id']}: source type/access mismatch")
    return sorted(errors)


def validate_curated(root: Path):
    """Validate the complete curated collection, AIO mappings and exact-name collisions."""
    root = root.resolve()
    source, graph = load_source(root)
    schema_validator("curated_concept.yaml", "CuratedAIConcept")
    corpus = root / "data/curated"
    if any(p.is_symlink() for p in (root / "data", corpus)):
        raise ValueError("curated corpus path must not contain a symlink")
    if not corpus.is_dir():
        raise ValueError("curated corpus directory is missing")
    aio_nodes = {"AIO:" + n["id"].removeprefix(AIO): n for n in graph["nodes"]
                 if n.get("type") == "CLASS" and n["id"].startswith(AIO)}
    identities = defaultdict(set)
    for identifier, node in aio_nodes.items():
        values = [node["lbl"], *(s["val"] for s in node.get("meta", {}).get("synonyms", [])
                               if s["pred"] == "hasExactSynonym")]
        for value in values:
            identities[normalized_name(value)].add(identifier)
    errors, records, identifiers = [], [], set()
    paths = []
    for folder, directories, filenames in os.walk(corpus, followlinks=False):
        for name in [*directories, *filenames]:
            path = Path(folder) / name
            if path.is_symlink():
                errors.append(f"curated corpus must not contain a symlink: {path}")
            elif path.is_file():
                if path.parent != corpus or path.suffix != ".yaml":
                    errors.append(f"unexpected curated corpus entry: {path}")
                else:
                    paths.append(path)
    if not paths:
        errors.append("curated corpus must contain at least one record")
    for path in sorted(paths):
        try:
            record = read_record(path)
            problems = validate_curated_record(record)
            if problems:
                errors.extend(f"{path.relative_to(root)}: {problem}" for problem in problems)
                continue
            identifier = record["id"]
            if identifier in identifiers:
                errors.append(f"duplicate curated ID: {identifier}")
            identifiers.add(identifier)
            if path.name != identifier.split(":", 1)[1] + ".yaml":
                errors.append(f"curated filename does not match ID: {path}")
            if record["aio_snapshot"] != {"commit": source["commit"], "sha256": source["sha256"]}:
                errors.append(f"{identifier}: AIO mapping snapshot differs from the current pin")
            for mapping in record.get("aio_mappings", []):
                if mapping["target"] not in aio_nodes:
                    errors.append(f"{identifier}: unresolved AIO mapping {mapping['target']}")
            for examined in record.get("aio_no_match", {}).get("examined_targets", []):
                if examined["target"] not in aio_nodes:
                    errors.append(f"{identifier}: unresolved examined AIO target {examined['target']}")
            for name in [record["name"], *record.get("aliases", [])]:
                key = normalized_name(name)
                collisions = identities[key] - {identifier}
                if collisions:
                    errors.append(f"{identifier}: identity {name!r} collides with "
                                  + ", ".join(sorted(collisions)))
                identities[key].add(identifier)
            errors.extend(f"{identifier}: {error}" for error in
                          validate_references(record, path, root))
            records.append(record)
        except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
    for error in errors:
        print(f"ERROR {error}")
    print(f"Checked {len(paths)} curated concept record(s); {len(errors)} error(s).")
    return int(bool(errors))
