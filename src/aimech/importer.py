"""Deterministic, offline AIO OBO Graphs projection. No OWL reasoning is performed."""

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

from aimech.validation import read_record, validate_record

AIO = "https://w3id.org/aio/"
OWL_THING = "http://www.w3.org/2002/07/owl#Thing"
HAS_PART = "http://purl.obolibrary.org/obo/BFO_0000051"
TOP_LEVEL = "http://purl.obolibrary.org/obo/IAO_0000700"


def curie(iri):
    if iri == OWL_THING:
        return "owl:Thing"
    if not isinstance(iri, str) or not re.fullmatch(re.escape(AIO) + r"[A-Za-z0-9]+", iri):
        raise ValueError(f"unexpected AIO class IRI: {iri!r}")
    return "AIO:" + iri.removeprefix(AIO)


def load_source(root: Path):
    source = read_record(root / "sources/aio/source.yaml")
    path = root / source["snapshot"]
    if path.resolve() != (root / "sources/aio/aio.json").resolve():
        raise ValueError("source snapshot must be sources/aio/aio.json")
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != source["sha256"]:
        raise ValueError("AIO snapshot checksum mismatch")
    document = json.loads(raw)
    if len(document["graphs"]) != 1:
        raise ValueError("expected exactly one AIO graph")
    graph = document["graphs"][0]
    if graph["meta"]["version"] != source["version_iri"]:
        raise ValueError("snapshot version differs from source manifest")
    return source, graph


def build_records(root: Path):
    source, graph = load_source(root)
    nodes = [n for n in graph["nodes"]
             if n.get("type") == "CLASS" and n["id"].startswith(AIO)]
    by_id = {n["id"]: n for n in nodes}
    if len(by_id) != len(nodes) or len(nodes) != source["expected_aio_classes"]:
        raise ValueError("unexpected class count or duplicate source class ID")
    if any(n.get("meta", {}).get("deprecated") for n in nodes):
        raise ValueError("deprecated classes need an explicit import policy")
    roots = {x["val"] for x in graph["meta"]["basicPropertyValues"] if x["pred"] == TOP_LEVEL}
    if not roots or not roots <= by_id.keys():
        raise ValueError("top-level branch metadata missing or unresolved")
    parents, parts = defaultdict(set), defaultdict(set)
    for edge in graph["edges"]:
        subject, predicate, target = (edge[k] for k in ("sub", "pred", "obj"))
        if subject not in by_id:
            raise ValueError(f"unknown edge subject: {subject}")
        if target not in by_id and target != OWL_THING:
            raise ValueError(f"unknown edge target: {target}")
        if predicate == "is_a":
            parents[subject].add(target)
        elif predicate == HAS_PART and target in by_id:
            parts[subject].add(target)
        else:
            raise ValueError(f"unsupported relationship: {predicate} -> {target}")

    def branches(iri, visiting=frozenset()):
        if iri == OWL_THING:
            return set()
        if iri in visiting:
            raise ValueError(f"cyclic hierarchy at {iri}")
        found = {iri.removeprefix(AIO)} if iri in roots else set()
        for parent in parents[iri]:
            found.update(branches(parent, visiting | {iri}))
        return found

    records = {}
    for iri, node in sorted(by_id.items()):
        identifier = curie(iri)
        meta = node.get("meta", {})
        record = {
            "id": identifier, "name": node["lbl"], "definition": meta["definition"]["val"],
            "ontology_iri": iri, "branches": sorted(branches(iri)),
            "parents": sorted(curie(p) for p in parents[iri]),
            "provenance": {
                "source": source["repository"], "source_commit": source["commit"],
                "source_version": source["version_iri"], "source_sha256": source["sha256"],
                "source_file": source["source_path"], "source_node": iri,
                "imported_at": source["retrieved_at"], "license": source["license"],
            },
            "review_status": "NOT_REVIEWED",
        }
        if parts[iri]:
            record["relationships"] = [{"predicate": "BFO:0000051", "target": curie(p)}
                                       for p in sorted(parts[iri])]
        synonyms = []
        for synonym in meta.get("synonyms", []):
            scope = {"hasExactSynonym": "exact", "hasRelatedSynonym": "related"}.get(
                synonym["pred"]
            )
            if scope is None or set(synonym) != {"pred", "val"}:
                raise ValueError(f"unsupported synonym metadata: {synonym}")
            synonyms.append({"value": synonym["val"], "scope": scope})
        if synonyms:
            record["synonyms"] = sorted(synonyms, key=lambda s: (s["scope"], s["value"]))
        for field in ("subsets", "comments"):
            if meta.get(field):
                record[field] = sorted(meta[field])
        if meta["definition"].get("xrefs"):
            record["definition_sources"] = sorted(set(meta["definition"]["xrefs"]))
        errors = validate_record(record)
        if errors:
            raise ValueError(f"invalid generated {identifier}: {errors}")
        records[identifier.removeprefix("AIO:") + ".yaml"] = yaml.safe_dump(
            record, sort_keys=False, allow_unicode=True, width=100
        )
    return records


def seed(root: Path, *, check=False, write=False):
    destination = root / "data/aio"
    if any(path.is_symlink() for path in (root / "data", destination)):
        raise ValueError("generated corpus path must not contain a symlink")
    records = build_records(root)
    existing = {p.name: p for p in destination.glob("*")} if destination.exists() else {}
    missing = sorted(set(records) - existing.keys())
    extra = sorted(existing.keys() - records.keys())
    changed = sorted(name for name in records.keys() & existing.keys()
                     if existing[name].is_symlink() or not existing[name].is_file()
                     or existing[name].read_bytes() != records[name].encode("utf-8"))
    print(f"AIO: {len(records)} records; {len(missing)} missing, "
          f"{len(changed)} changed, {len(extra)} unexpected.")
    if check:
        return int(bool(missing or changed or extra))
    if write:
        if changed or extra:
            raise ValueError("refusing to overwrite changed records or remove unexpected files")
        destination.mkdir(parents=True, exist_ok=True)
        for name in missing:
            with (destination / name).open("xb") as stream:
                stream.write(records[name].encode("utf-8"))
        print(f"Wrote {len(missing)} new records; existing matching records left untouched.")
    else:
        print("Dry run; use --write to create missing records.")
    return 0
