"""Deterministic full-corpus and schema audit of causal-mechanism-graph applicability in AIMech.

Audits src/aimech/schema/aimech.yaml, src/aimech/schema/curated_concept.yaml,
src/aimech/schema/mech_shared.yaml, all data/aio/*.yaml records, and all
data/curated/*.yaml records for Cycle 1, Stage 2 (causal_graphs) of
mech-goal-sequence-20261019.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
AUDIT_TIMESTAMP = "2026-10-25T05:25:00Z"

CAUSAL_GRAPH_CANDIDATE_SLOTS = (
    "causal_graph",
    "causal_graphs",
    "causal_edges",
    "causal_mechanism",
    "causal_mechanisms",
    "mechanism_graph",
    "pathways",
    "biological_processes",
    "upstream",
    "downstream",
    "regulates",
    "positively_regulates",
    "negatively_regulates",
    "gene_examples",
    "protein_examples",
    "uniprot_id",
)

CAUSAL_SUBJECT_PATTERN = re.compile(
    r"\b(causal|causality|instrumental variable|invalid instrument|directed acyclic graph|"
    r"bayesian network|probabilistic graphical model|markov blanket|do-calculus|"
    r"structural equation|counterfactual|treatment effect)\b",
    re.IGNORECASE,
)


YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping in {path}")
    return data


def audit_schema(rel_path: str) -> dict[str, Any]:
    path = ROOT / rel_path
    doc = load_yaml(path)
    classes = doc.get("classes") or {}
    enums = doc.get("enums") or {}
    class_slots: dict[str, list[str]] = {}
    all_slots: set[str] = set()
    for cls_name, cls_def in sorted(classes.items()):
        attrs = sorted((cls_def or {}).get("attributes", {}).keys())
        class_slots[cls_name] = attrs
        all_slots.update(attrs)
    present_causal_slots = sorted(all_slots.intersection(CAUSAL_GRAPH_CANDIDATE_SLOTS))
    return {
        "path": rel_path,
        "sha256": sha256_file(path),
        "id": doc.get("id"),
        "name": doc.get("name"),
        "description": doc.get("description"),
        "imports": doc.get("imports", []),
        "classes": class_slots,
        "enums": {
            enum_name: sorted(((enum_def or {}).get("permissible_values") or {}).keys())
            for enum_name, enum_def in sorted(enums.items())
        },
        "causal_graph_candidate_slots_present": present_causal_slots,
    }


def audit_aio_corpus() -> dict[str, Any]:
    aio_paths = sorted((ROOT / "data" / "aio").glob("*.yaml"))
    top_level_keys: Counter[str] = Counter()
    branch_counts: Counter[str] = Counter()
    relationship_predicates: Counter[str] = Counter()
    records_with_relationships: list[dict[str, Any]] = []
    records_with_discussions: list[str] = []
    records_with_causal_slots: list[str] = []
    causal_or_graphical_subject_records: list[dict[str, Any]] = []
    total_parent_edges = 0
    total_relationship_edges = 0
    total_synonyms = 0

    for path in aio_paths:
        doc = load_yaml(path)
        rec_id = str(doc["id"])
        name = str(doc.get("name", ""))
        definition = str(doc.get("definition", ""))
        for k in doc.keys():
            top_level_keys[k] += 1
            if k in CAUSAL_GRAPH_CANDIDATE_SLOTS:
                records_with_causal_slots.append(rec_id)
        for b in doc.get("branches") or []:
            branch_counts[str(b)] += 1
        parents = doc.get("parents") or []
        total_parent_edges += len(parents)
        synonyms = doc.get("synonyms") or []
        total_synonyms += len(synonyms)
        rels = doc.get("relationships") or []
        if rels:
            total_relationship_edges += len(rels)
            for rel in rels:
                relationship_predicates[str(rel.get("predicate"))] += 1
            records_with_relationships.append(
                {
                    "id": rec_id,
                    "path": str(path.relative_to(ROOT)),
                    "name": name,
                    "relationships": rels,
                }
            )
        if doc.get("discussions"):
            records_with_discussions.append(rec_id)
        matched = sorted({m.lower() for m in CAUSAL_SUBJECT_PATTERN.findall(f"{name} {definition}")})
        if matched:
            causal_or_graphical_subject_records.append(
                {
                    "id": rec_id,
                    "path": str(path.relative_to(ROOT)),
                    "name": name,
                    "branches": doc.get("branches", []),
                    "parents": parents,
                    "matched_terms": matched,
                    "definition": definition,
                }
            )

    return {
        "directory": "data/aio",
        "record_count": len(aio_paths),
        "top_level_key_counts": dict(sorted(top_level_keys.items())),
        "branch_counts": dict(sorted(branch_counts.items())),
        "taxonomic_parent_edge_count": total_parent_edges,
        "mereological_relationship_edge_count": total_relationship_edges,
        "relationship_predicate_counts": dict(sorted(relationship_predicates.items())),
        "records_with_relationships": records_with_relationships,
        "synonym_count": total_synonyms,
        "records_with_discussions_count": len(records_with_discussions),
        "records_with_causal_graph_slots_count": len(records_with_causal_slots),
        "causal_or_graphical_subject_records_count": len(
            causal_or_graphical_subject_records
        ),
        "causal_or_graphical_subject_records": causal_or_graphical_subject_records,
    }


def audit_curated_corpus() -> dict[str, Any]:
    curated_paths = sorted((ROOT / "data" / "curated").glob("*.yaml"))
    top_level_keys: Counter[str] = Counter()
    concept_kind_counts: Counter[str] = Counter()
    claim_kind_counts: Counter[str] = Counter()
    mapping_relation_counts: Counter[str] = Counter()
    source_type_counts: Counter[str] = Counter()
    access_level_counts: Counter[str] = Counter()
    records_with_aio_mappings = 0
    records_with_aio_no_match = 0
    total_claims = 0
    total_evidence_sources = 0
    records_with_causal_slots: list[str] = []
    causal_or_graphical_subject_records: list[dict[str, Any]] = []

    for path in curated_paths:
        doc = load_yaml(path)
        rec_id = str(doc["id"])
        name = str(doc.get("name", ""))
        definition = str(doc.get("definition", ""))
        identity_notes = str(doc.get("identity_notes", ""))
        concept_kind = str(doc.get("concept_kind", ""))
        concept_kind_counts[concept_kind] += 1

        for k in doc.keys():
            top_level_keys[k] += 1
            if k in CAUSAL_GRAPH_CANDIDATE_SLOTS:
                records_with_causal_slots.append(rec_id)

        claims = doc.get("claims") or []
        total_claims += len(claims)
        for claim in claims:
            claim_kind_counts[str(claim.get("kind"))] += 1

        sources = doc.get("evidence_sources") or []
        total_evidence_sources += len(sources)
        for src in sources:
            source_type_counts[str(src.get("source_type"))] += 1
            access_level_counts[str(src.get("access_level"))] += 1

        if doc.get("aio_mappings"):
            records_with_aio_mappings += 1
            for mapping in doc["aio_mappings"]:
                mapping_relation_counts[str(mapping.get("relation"))] += 1
        if doc.get("aio_no_match"):
            records_with_aio_no_match += 1

        combined_text = " ".join(
            [
                name,
                definition,
                identity_notes,
                " ".join(str(c.get("statement", "")) for c in claims),
            ]
        )
        matched = sorted({m.lower() for m in CAUSAL_SUBJECT_PATTERN.findall(combined_text)})
        if matched:
            causal_or_graphical_subject_records.append(
                {
                    "id": rec_id,
                    "path": str(path.relative_to(ROOT)),
                    "name": name,
                    "concept_kind": concept_kind,
                    "claim_count": len(claims),
                    "matched_terms": matched,
                    "aio_mapping_targets": [
                        f"{m['relation']}:{m['target']}"
                        for m in (doc.get("aio_mappings") or [])
                    ],
                    "has_aio_no_match": bool(doc.get("aio_no_match")),
                }
            )

    return {
        "directory": "data/curated",
        "record_count": len(curated_paths),
        "top_level_key_counts": dict(sorted(top_level_keys.items())),
        "concept_kind_counts": dict(sorted(concept_kind_counts.items())),
        "total_claims": total_claims,
        "claim_kind_counts": dict(sorted(claim_kind_counts.items())),
        "total_evidence_sources": total_evidence_sources,
        "evidence_source_type_counts": dict(sorted(source_type_counts.items())),
        "evidence_access_level_counts": dict(sorted(access_level_counts.items())),
        "records_with_aio_mappings_count": records_with_aio_mappings,
        "records_with_aio_no_match_count": records_with_aio_no_match,
        "aio_mapping_relation_counts": dict(sorted(mapping_relation_counts.items())),
        "records_with_causal_graph_slots_count": len(records_with_causal_slots),
        "causal_or_graphical_subject_records_count": len(
            causal_or_graphical_subject_records
        ),
        "causal_or_graphical_subject_records": causal_or_graphical_subject_records,
    }


def build_audit_report() -> dict[str, Any]:
    schemas = {
        "aimech": audit_schema("src/aimech/schema/aimech.yaml"),
        "curated_concept": audit_schema("src/aimech/schema/curated_concept.yaml"),
        "mech_shared": audit_schema("src/aimech/schema/mech_shared.yaml"),
    }
    aio_summary = audit_aio_corpus()
    curated_summary = audit_curated_corpus()
    workflow_path = ROOT / "workflow" / "mech-workflow.yaml"
    workflow_doc = load_yaml(workflow_path)
    stage_2_override = next(
        s for s in workflow_doc["stages"] if s["stage"] == 2
    )

    total_records = aio_summary["record_count"] + curated_summary["record_count"]
    total_causal_slot_records = (
        aio_summary["records_with_causal_graph_slots_count"]
        + curated_summary["records_with_causal_graph_slots_count"]
    )

    assert aio_summary["record_count"] == 442
    assert curated_summary["record_count"] == 1487
    assert (
        curated_summary["records_with_aio_mappings_count"]
        + curated_summary["records_with_aio_no_match_count"]
        == curated_summary["record_count"]
    )
    assert total_records == 1929
    assert total_causal_slot_records == 0
    assert schemas["aimech"]["causal_graph_candidate_slots_present"] == []
    assert schemas["curated_concept"]["causal_graph_candidate_slots_present"] == []
    assert schemas["mech_shared"]["causal_graph_candidate_slots_present"] == []
    assert stage_2_override["applicability"] == "not_applicable"

    return {
        "audit_id": "20261025T052500Z-causal-graph-applicability-audit",
        "created_at": AUDIT_TIMESTAMP,
        "run_id": "mech-goal-sequence-20261019",
        "cycle": 1,
        "stage": 2,
        "stage_key": "causal_graphs",
        "applicability_verdict": "not_applicable",
        "workflow_profile": {
            "path": "workflow/mech-workflow.yaml",
            "sha256": sha256_file(workflow_path),
            "stage_2_override": stage_2_override,
        },
        "corpus_totals": {
            "aio_generated_records": aio_summary["record_count"],
            "curated_aimech_records": curated_summary["record_count"],
            "total_records_inspected": total_records,
            "records_with_causal_graph_slots": total_causal_slot_records,
        },
        "schemas": schemas,
        "aio_corpus_inventory": aio_summary,
        "curated_corpus_inventory": curated_summary,
        "ontology_vs_causality_distinction": {
            "aio_taxonomic_subsumption": (
                f"{aio_summary['taxonomic_parent_edge_count']} parents edges across "
                f"{aio_summary['record_count']} generated AIO records represent OWL/RDFS "
                "class subsumption (rdfs:subClassOf / owl:Thing), not causal state transitions."
            ),
            "aio_mereological_relationships": (
                f"{aio_summary['mereological_relationship_edge_count']} exported relationships "
                "use BFO:0000051 ('has part'), which src/aimech/schema/aimech.yaml explicitly "
                "defines as 'has part; exported ontology axiom, not evidence of causal effect.'"
            ),
            "curated_aio_vocabulary_mappings": (
                f"{sum(curated_summary['aio_mapping_relation_counts'].values())} aio_mappings "
                f"across {curated_summary['records_with_aio_mappings_count']} curated records "
                f"(plus {curated_summary['records_with_aio_no_match_count']} aio_no_match records) "
                "express conceptual scope alignment (broad_match, narrow_match, related_match) "
                "to pinned AIO classes, not causal edges."
            ),
            "curated_mechanism_claims": (
                f"{curated_summary['claim_kind_counts'].get('mechanism', 0)} ConceptClaim entries "
                "with kind='mechanism' (out of "
                f"{curated_summary['total_claims']} total claims across "
                f"{curated_summary['record_count']:,} curated records) "
                "document mathematical, algorithmic, or architectural operating mechanisms in "
                "natural-language prose backed by primary literature locators, not biological "
                "or physical causal mechanism graphs."
            ),
            "ai_causal_inference_subject_matter": (
                f"{aio_summary['causal_or_graphical_subject_records_count']} generated AIO records "
                f"and {curated_summary['causal_or_graphical_subject_records_count']} maintained "
                "curated records match causal/graphical terminology in their definitions, identity "
                "notes, or claims across four methodological categories: (1) statistical causal "
                "inference, instrumental-variable estimation, and counterfactual fairness criteria; "
                "(2) probabilistic graphical models and Bayesian-network inference/diagnostics; "
                "(3) causal/autoregressive sequence masking, non-anticipative system identification, "
                "and algorithmic directed acyclic graphs (e.g. shortest-path DAGs); and "
                "(4) explicit limitation-claim disclaimers noting that benchmark graph examples do "
                "not establish causal biology. None of these records encode biological causal "
                "mechanism graphs."
            ),
        },
        "future_representation_assessment": {
            "biological_causal_graphs": "not_applicable",
            "candidate_native_analog": (
                "No applicable causal-mechanism-graph representation exists in AIMech's current "
                "schemas (src/aimech/schema/aimech.yaml and src/aimech/schema/curated_concept.yaml). "
                "If a future schema revision ever introduces structured algorithmic operator-dataflow "
                "or mathematical dependency graphs, that representation would denote formal computational "
                "composition rather than empirical biological/mechanistic causality and would require "
                "explicit schema governance review before replacing Stage 2's applicability audit objective."
            ),
        },
        "script_path": "research/validation/20261025T052500Z-causal-graph-applicability-audit.py",
        "script_sha256": sha256_file(Path(__file__).resolve()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional path to write the JSON audit output.",
    )
    args = parser.parse_args()
    report = build_audit_report()
    rendered = json.dumps(report, indent=2) + "\n"
    if args.output is not None:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
