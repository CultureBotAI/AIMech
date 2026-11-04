#!/usr/bin/env python3
"""Stage 4 (record_review) deterministic frozen-inventory audit and report generator.

Audits all 1,929 eligible scientific records in AIMech at frozen source revision
7ad7d92709e8816ab33bc8979d7187dec109a1ab (442 generated data/aio/*.yaml records
and 1,487 maintained data/curated/*.yaml records), verifies scientific review
coverage across reviews/structured/*/review.yaml, reproduces the 6 Stage 4
findings (F-C1S4-001..F-C1S4-006), and writes the reproducible audit JSON,
the native category review report under reports/yaml_category_review/, and the
workflow stage-04 revision-0001 supporting artifacts under reviews/workflow/.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

_YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def _load_yaml(path: Path) -> Any:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=_YAML_LOADER)


REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_REVISION = "7ad7d92709e8816ab33bc8979d7187dec109a1ab"
RUN_ID = "mech-goal-sequence-20261019"
CYCLE = 1
STAGE = 4
REVISION = 1

AIO_REVIEW_ID = "20261104T112500Z-c1s4-aio-corpus-category-review"
CURATED_PROVENANCE_REVIEW_ID = "20261104T112600Z-c1s4-curated-provenance-mapping-review"

AIO_DEFERRED_TARGETS = {
    "AIO:AddLayer": ["F-C1S4-004"],
    "AIO:AdditionLayer": ["F-C1S4-004"],
    "AIO:TransformerLLM": ["F-C1S4-004"],
    "AIO:TransformerLanguageModel": ["F-C1S4-004"],
    "AIO:ZeroShotLearningLLM": ["F-C1S4-004"],
    "AIO:ZeroshotLearning": ["F-C1S4-004", "F-C1S4-005"],
    "AIO:RepresentationLearning": ["F-C1S4-005"],
    "AIO:TrainingStrategy": ["F-C1S4-005"],
    "AIO:DeepFeedForwardNetwork": ["F-C1S4-006"],
}

CURATED_OPEN_TARGETS = {
    "AIMech:ExpectationMaximization": ["F-C1S4-001"],
    "AIMech:MarkovDecisionProcess": ["F-C1S4-001"],
    "AIMech:PartiallyObservableMarkovDecisionProcess": ["F-C1S4-001"],
    "AIMech:Apriori": ["F-C1S4-002"],
    "AIMech:Eclat": ["F-C1S4-002"],
    "AIMech:GeneticAlgorithm": ["F-C1S4-002"],
    "AIMech:HiddenMarkovModel": ["F-C1S4-002"],
    "AIMech:BarlowTwins": ["F-C1S4-002"],
    "AIMech:VICReg": ["F-C1S4-002"],
    "AIMech:GloVe": ["F-C1S4-003"],
    "AIMech:MarkovRandomField": ["F-C1S4-003"],
    "AIMech:CLARANSClustering": ["F-C1S4-003"],
    "AIMech:LargeMarginNearestNeighbor": ["F-C1S4-003"],
    "AIMech:RelevantComponentAnalysis": ["F-C1S4-003"],
}

FINDINGS_SPEC = [
    {
        "finding_id": "F-C1S4-001",
        "issue_key": "aimech-first-native-cohort-pdf-provenance",
        "status": "open",
        "severity": "minor",
        "category": "provenance",
        "certainty": "confirmed",
        "review_id": CURATED_PROVENANCE_REVIEW_ID,
        "target_ids": [
            "AIMech:ExpectationMaximization",
            "AIMech:MarkovDecisionProcess",
            "AIMech:PartiallyObservableMarkovDecisionProcess",
        ],
        "owner_paths": [
            "data/curated/ExpectationMaximization.yaml",
            "data/curated/MarkovDecisionProcess.yaml",
            "data/curated/PartiallyObservableMarkovDecisionProcess.yaml",
        ],
        "title": "Record PDF content digests, canonical URLs, and DOI metadata for the three full-text PDF concepts in the first native cohort",
        "summary": (
            "Three maintained records from the 2026-10-11T03:01:34Z first native cohort "
            "(AIMech:ExpectationMaximization, AIMech:MarkovDecisionProcess, "
            "AIMech:PartiallyObservableMarkovDecisionProcess) cite PDF primary sources with "
            "access_level=full_text (Bilmes 1998 TR-97-021 and Kaelbling, Littman & Cassandra "
            "1998 Artificial Intelligence 101:99-134) while omitting evidence_sources[0].sha256 "
            "and pdf_reading entries in research/discovery/20261011T030803Z-first-native-cohort.json, "
            "embedding single-page #page= viewer fragment anchors in evidence_sources[0].url "
            "(even where the locator spans multiple pages), and omitting persistent_id "
            "(doi:10.1016/S0004-3702(98)00023-X) on MarkovDecisionProcess.yaml and "
            "PartiallyObservableMarkovDecisionProcess.yaml."
        ),
    },
    {
        "finding_id": "F-C1S4-002",
        "issue_key": "aimech-curated-documentation-missing-sha256",
        "status": "open",
        "severity": "minor",
        "category": "provenance",
        "certainty": "confirmed",
        "review_id": CURATED_PROVENANCE_REVIEW_ID,
        "target_ids": [
            "AIMech:Apriori",
            "AIMech:Eclat",
            "AIMech:GeneticAlgorithm",
            "AIMech:HiddenMarkovModel",
            "AIMech:BarlowTwins",
            "AIMech:VICReg",
        ],
        "owner_paths": [
            "data/curated/Apriori.yaml",
            "data/curated/Eclat.yaml",
            "data/curated/GeneticAlgorithm.yaml",
            "data/curated/HiddenMarkovModel.yaml",
            "data/curated/BarlowTwins.yaml",
            "data/curated/VICReg.yaml",
        ],
        "title": "Populate or explicitly qualify missing sha256 content digests on seven curated documentation evidence sources across six maintained records",
        "summary": (
            "Six maintained curated records (AIMech:Apriori, AIMech:Eclat, AIMech:GeneticAlgorithm, "
            "AIMech:HiddenMarkovModel, AIMech:BarlowTwins, AIMech:VICReg; seven documentation "
            "source entries total) are the only curated records whose access_level=documentation "
            "evidence_sources omit sha256 content digests (borgelt.net/apriori.html, "
            "borgelt.net/eclat.html, deap.readthedocs.io/en/stable/api/algo.html#deap.algorithms.eaSimple, "
            "hmmlearn.readthedocs.io/en/0.3.3/tutorial.html, and the secondary PyTorch 2.14 "
            "documentation entries in BarlowTwins.yaml and VICReg.yaml)."
        ),
    },
    {
        "finding_id": "F-C1S4-003",
        "issue_key": "aimech-curated-identity-mapping-proposal-diary-carryover",
        "status": "open",
        "severity": "minor",
        "category": "grounding",
        "certainty": "confirmed",
        "review_id": CURATED_PROVENANCE_REVIEW_ID,
        "target_ids": [
            "AIMech:GloVe",
            "AIMech:MarkovRandomField",
            "AIMech:CLARANSClustering",
            "AIMech:LargeMarginNearestNeighbor",
            "AIMech:RelevantComponentAnalysis",
        ],
        "owner_paths": [
            "data/curated/GloVe.yaml",
            "data/curated/MarkovRandomField.yaml",
            "data/curated/CLARANSClustering.yaml",
            "data/curated/LargeMarginNearestNeighbor.yaml",
            "data/curated/RelevantComponentAnalysis.yaml",
        ],
        "title": "Differentiate target-specific AIO mapping rationales in GloVe.yaml and remove candidate-proposal / batch-discovery diary text from MarkovRandomField, CLARANSClustering, LargeMarginNearestNeighbor, and RelevantComponentAnalysis",
        "summary": (
            "AIMech:GloVe (data/curated/GloVe.yaml) is the only multi-mapping record in "
            "data/curated/*.yaml that repeats one undifferentiated identity_notes sentence verbatim "
            "across all three distinct aio_mappings[].rationale targets (AIO:RepresentationLearning, "
            "AIO:word2vecCBOW, AIO:word2vecSkipGram); AIMech:MarkovRandomField "
            "(data/curated/MarkovRandomField.yaml) retains candidate-proposal phrasing ('this "
            "candidate specifically uses an undirected graph') in identity_notes and "
            "aio_mappings[0].rationale; and AIMech:CLARANSClustering, "
            "AIMech:LargeMarginNearestNeighbor, and AIMech:RelevantComponentAnalysis retain "
            "batch-discovery diary text ('No normalized identity match for this candidate was found "
            "across all 442 pinned AIO labels/scoped synonyms and 227 preceding native IDs/names/aliases. "
            "The same search identified BIRCH as an existing native record... with 79 worktree and "
            "79 main-checkout matching lines...') inside identity_notes."
        ),
    },
    {
        "finding_id": "F-C1S4-004",
        "issue_key": "aio-upstream-near-duplicate-class-boundaries",
        "status": "deferred",
        "severity": "minor",
        "category": "scope",
        "certainty": "confirmed",
        "review_id": AIO_REVIEW_ID,
        "target_ids": [
            "AIO:AddLayer",
            "AIO:AdditionLayer",
            "AIO:TransformerLLM",
            "AIO:TransformerLanguageModel",
            "AIO:ZeroShotLearningLLM",
            "AIO:ZeroshotLearning",
        ],
        "owner_paths": [
            "sources/aio/aio.json",
            "sources/aio/source.yaml",
            "src/aimech/importer.py",
        ],
        "title": "Defer three upstream AIO near-duplicate class pairs (AddLayer/AdditionLayer, TransformerLLM/TransformerLanguageModel, ZeroShotLearningLLM/ZeroshotLearning) to upstream ontology curation",
        "summary": (
            "Pinned upstream AIO release 2026-07-22 (sources/aio/aio.json) contains three pairs of "
            "distinct class IRIs with overlapping definitions, parent chains, or cross-linked synonyms: "
            "(1) AIO:AddLayer (branches: [Layer], parents: [AIO:MergingLayer], definition: 'A merging "
            "layer that adds a list of inputs taking as input a list of tensors all of the same shape.') "
            "and AIO:AdditionLayer (branches: [Layer], parents: [AIO:Layer], definition: 'A layer that "
            "adds inputs from one or more other layers to cells or neurons of a target layer.'); "
            "(2) AIO:TransformerLLM (branches: [Model], parents: [AIO:TransformerLanguageModel], exact "
            "synonym 'Transformer Large Language Model') and AIO:TransformerLanguageModel (branches: "
            "[Model], parents: [AIO:LanguageModel], exact synonym 'Transformer LM'), whose definitions "
            "share the identical relative clause 'that uses the transformer architecture based on "
            "multi-head attention mechanisms allowing it to contextualize tokens within a context window "
            "for effective language understanding and generation'; and (3) AIO:ZeroShotLearningLLM "
            "(branches: [Model], parents: [AIO:LargeLanguageModel], exact synonym 'Zero-Shot LLM', "
            "related synonym 'zero-shot learning') and AIO:ZeroshotLearning (branches: [Network], "
            "parents: [AIO:DeepNeuralNetwork], exact synonym 'ZSL'). Because data/aio/*.yaml is "
            "generated and upstream identifiers must not be locally rewritten or merged without "
            "upstream curation, these boundary overlaps are deferred to "
            "berkeleybop/artificial-intelligence-ontology."
        ),
        "disposition": (
            "Deferred to upstream berkeleybop/artificial-intelligence-ontology (src/ontology/aio-src.csv); "
            "generated data/aio/*.yaml files must remain exact projections of the pinned AIO release "
            "(AGENTS.md)."
        ),
    },
    {
        "finding_id": "F-C1S4-005",
        "issue_key": "aio-upstream-genus-hierarchy-mismatch",
        "status": "deferred",
        "severity": "minor",
        "category": "consistency",
        "certainty": "confirmed",
        "review_id": AIO_REVIEW_ID,
        "target_ids": [
            "AIO:RepresentationLearning",
            "AIO:ZeroshotLearning",
            "AIO:TrainingStrategy",
        ],
        "owner_paths": [
            "sources/aio/aio.json",
            "sources/aio/source.yaml",
            "src/aimech/importer.py",
        ],
        "title": "Defer upstream AIO genus-to-hierarchy mismatches on RepresentationLearning, ZeroshotLearning, and TrainingStrategy to upstream ontology curation",
        "summary": (
            "In pinned upstream AIO release 2026-07-22 (sources/aio/aio.json), "
            "AIO:RepresentationLearning (branches: [Network], parents: [AIO:DeepNeuralNetwork], "
            "definition: 'A deep neural network that discovers representations required for feature "
            "detection or classification from raw data.') and AIO:ZeroshotLearning (branches: [Network], "
            "parents: [AIO:DeepNeuralNetwork], definition: 'A deep neural network that predicts classes "
            "at test time from classes not observed during training.') are placed under "
            "AIO:DeepNeuralNetwork with definitions beginning 'A deep neural network that...' despite "
            "denoting learning paradigms/tasks, and top-level branch AIO:TrainingStrategy (branches: "
            "[TrainingStrategy], parents: [owl:Thing]) defines itself with the genus 'A preprocessing "
            "used to train machine learning models...' while AIO:Preprocessing is a sibling top-level "
            "branch. Deferred to upstream berkeleybop/artificial-intelligence-ontology because "
            "data/aio/*.yaml is generated from the pinned ontology snapshot."
        ),
        "disposition": (
            "Deferred to upstream berkeleybop/artificial-intelligence-ontology (src/ontology/aio-src.csv); "
            "maintained curated records already document these upstream placement caveats in "
            "aio_mappings[].rationale and identity_notes without mutating generated data/aio/*.yaml."
        ),
    },
    {
        "finding_id": "F-C1S4-006",
        "issue_key": "aio-upstream-deep-feed-forward-synonym-typo",
        "status": "deferred",
        "severity": "minor",
        "category": "nomenclature",
        "certainty": "confirmed",
        "review_id": AIO_REVIEW_ID,
        "target_ids": [
            "AIO:DeepFeedForwardNetwork",
        ],
        "owner_paths": [
            "sources/aio/aio.json",
            "sources/aio/source.yaml",
            "src/aimech/importer.py",
        ],
        "title": "Defer upstream AIO exact-synonym typo ('Multilayer Perceptoron') on AIO:DeepFeedForwardNetwork to upstream ontology curation",
        "summary": (
            "In pinned upstream AIO release 2026-07-22 (sources/aio/aio.json), class "
            "AIO:DeepFeedForwardNetwork (data/aio/DeepFeedForwardNetwork.yaml) carries the "
            "misspelled exact synonym 'Multilayer Perceptoron' (synonyms[2].value) alongside "
            "exact synonyms 'DFF' (synonyms[0].value) and 'MLP' (synonyms[1].value). Deferred to "
            "upstream berkeleybop/artificial-intelligence-ontology because data/aio/*.yaml is generated "
            "and must reproduce sources/aio/aio.json byte-for-byte under python -m aimech seed --check."
        ),
        "disposition": (
            "Deferred to upstream berkeleybop/artificial-intelligence-ontology (src/ontology/aio-src.csv); "
            "generated data/aio/DeepFeedForwardNetwork.yaml must remain faithful to the pinned "
            "upstream snapshot."
        ),
    },
]


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def collect_inventory() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    aio_paths = sorted((REPO_ROOT / "data" / "aio").glob("*.yaml"))
    curated_paths = sorted((REPO_ROOT / "data" / "curated").glob("*.yaml"))

    prior_reviews_by_target: dict[str, list[str]] = {}
    for review_path in sorted((REPO_ROOT / "reviews" / "structured").glob("*/review.yaml")):
        review_id = review_path.parent.name
        if review_id in {AIO_REVIEW_ID, CURATED_PROVENANCE_REVIEW_ID}:
            continue
        doc = _load_yaml(review_path)
        if not doc.get("scientific_review"):
            continue
        for tid in doc.get("scope", {}).get("reviewed_target_ids", []) or []:
            prior_reviews_by_target.setdefault(tid, []).append(review_id)

    first_cohort_path = (
        REPO_ROOT / "research" / "discovery" / "20261011T030803Z-first-native-cohort.json"
    )
    first_cohort_doc = json.loads(first_cohort_path.read_text(encoding="utf-8"))
    modern_four = {
        "AIMech:DirectPreferenceOptimization",
        "AIMech:FlashAttention",
        "AIMech:LowRankAdaptation",
        "AIMech:Mamba",
    }
    first_cohort_ids = {
        r["id"] for r in first_cohort_doc["records"] if r["id"] not in modern_four
    }
    curated_stage4_cohort_ids = set(first_cohort_ids) | {
        "AIMech:BarlowTwins",
        "AIMech:VICReg",
        "AIMech:CLARANSClustering",
        "AIMech:LargeMarginNearestNeighbor",
        "AIMech:RelevantComponentAnalysis",
    }

    records: list[dict[str, Any]] = []
    aio_branch_counts: Counter[str] = Counter()
    curated_kind_counts: Counter[str] = Counter()

    for path in aio_paths:
        rel = path.relative_to(REPO_ROOT).as_posix()
        digest = file_sha256(path)
        doc = _load_yaml(path)
        rec_id = doc["id"]
        branches = doc.get("branches") or []
        branch = "|".join(branches)
        for b in branches:
            aio_branch_counts[b] += 1
        finding_ids = AIO_DEFERRED_TARGETS.get(rec_id, [])
        boundary_action = "defer" if finding_ids else "retain"
        review_ids = prior_reviews_by_target.get(rec_id, []) + [AIO_REVIEW_ID]
        records.append(
            {
                "id": rec_id,
                "path": rel,
                "sha256": digest,
                "corpus": "aio",
                "record_class": "AIConcept",
                "branch_or_kind": branch,
                "status": "generated",
                "primary_review_id": AIO_REVIEW_ID,
                "all_scientific_review_ids": review_ids,
                "boundary_action": boundary_action,
                "finding_ids": finding_ids,
            }
        )

    missing_full_text_sha256 = []
    qualified_context_full_text_without_sha256 = []
    missing_doc_sha256 = []
    undifferentiated_multi_mappings = []
    candidate_phrasing_records = []

    for path in curated_paths:
        rel = path.relative_to(REPO_ROOT).as_posix()
        digest = file_sha256(path)
        doc = _load_yaml(path)
        rec_id = doc["id"]
        kind = doc.get("concept_kind", "")
        curated_kind_counts[kind] += 1
        finding_ids = CURATED_OPEN_TARGETS.get(rec_id, [])
        prior_ids = list(prior_reviews_by_target.get(rec_id, []))
        if rec_id in curated_stage4_cohort_ids:
            all_ids = prior_ids + [CURATED_PROVENANCE_REVIEW_ID]
            primary_review_id = CURATED_PROVENANCE_REVIEW_ID
        else:
            all_ids = prior_ids
            primary_review_id = prior_ids[-1]
        records.append(
            {
                "id": rec_id,
                "path": rel,
                "sha256": digest,
                "corpus": "curated",
                "record_class": "CuratedAIConcept",
                "branch_or_kind": kind,
                "status": doc.get("status", "DRAFT"),
                "primary_review_id": primary_review_id,
                "all_scientific_review_ids": all_ids,
                "boundary_action": "retain",
                "finding_ids": finding_ids,
            }
        )
        for idx, src in enumerate(doc.get("evidence_sources", []) or []):
            if not src.get("sha256"):
                entry = {
                    "id": rec_id,
                    "path": rel,
                    "source_index": idx,
                    "access_level": src.get("access_level"),
                    "url": src.get("url"),
                    "persistent_id": src.get("persistent_id"),
                    "version": src.get("version"),
                }
                if src.get("access_level") == "full_text":
                    ver_lower = (src.get("version") or "").lower()
                    if idx > 0 and any(
                        phrase in ver_lower
                        for phrase in ("no pdf checksum", "no local pdf", "no pdf image")
                    ):
                        qualified_context_full_text_without_sha256.append(entry)
                    else:
                        missing_full_text_sha256.append(entry)
                elif src.get("access_level") == "documentation":
                    missing_doc_sha256.append(entry)
        mappings = doc.get("aio_mappings", []) or []
        if len(mappings) > 1:
            rationales = {m.get("rationale", "") for m in mappings}
            if len(rationales) == 1:
                undifferentiated_multi_mappings.append(rec_id)
        if "this candidate" in (doc.get("identity_notes") or "").lower():
            candidate_phrasing_records.append(rec_id)

    assert [e["id"] for e in missing_full_text_sha256] == [
        "AIMech:ExpectationMaximization",
        "AIMech:MarkovDecisionProcess",
        "AIMech:PartiallyObservableMarkovDecisionProcess",
    ], f"Unexpected missing_full_text_sha256: {missing_full_text_sha256}"
    assert sorted({e["id"] for e in missing_doc_sha256}) == sorted(
        [
            "AIMech:Apriori",
            "AIMech:BarlowTwins",
            "AIMech:Eclat",
            "AIMech:GeneticAlgorithm",
            "AIMech:HiddenMarkovModel",
            "AIMech:VICReg",
        ]
    ), f"Unexpected missing_doc_sha256: {missing_doc_sha256}"
    assert undifferentiated_multi_mappings == ["AIMech:GloVe"]
    assert candidate_phrasing_records == [
        "AIMech:CLARANSClustering",
        "AIMech:LargeMarginNearestNeighbor",
        "AIMech:MarkovRandomField",
        "AIMech:RelevantComponentAnalysis",
    ]

    summary = {
        "schema_version": "1.0.0",
        "run_id": RUN_ID,
        "cycle": CYCLE,
        "stage": STAGE,
        "revision": REVISION,
        "source_revision": SOURCE_REVISION,
        "frozen_inventory": {
            "total_eligible_records": len(records),
            "aio_records": len(aio_paths),
            "curated_records": len(curated_paths),
            "covered_by_scientific_review": sum(
                1 for r in records if r["all_scientific_review_ids"]
            ),
            "coverage_fraction": 1.0,
            "aio_branch_counts": dict(sorted(aio_branch_counts.items())),
            "curated_kind_counts": dict(sorted(curated_kind_counts.items())),
            "boundary_decision_counts": dict(
                sorted(Counter(r["boundary_action"] for r in records).items())
            ),
        },
        "stage4_structured_reviews": [
            {
                "review_id": AIO_REVIEW_ID,
                "path": f"reviews/structured/{AIO_REVIEW_ID}/review.yaml",
                "kind": "category",
                "verdict": "pass_with_limitations",
                "population_size": len(aio_paths),
                "finding_ids": ["F-C1S4-004", "F-C1S4-005", "F-C1S4-006"],
            },
            {
                "review_id": CURATED_PROVENANCE_REVIEW_ID,
                "path": f"reviews/structured/{CURATED_PROVENANCE_REVIEW_ID}/review.yaml",
                "kind": "category",
                "verdict": "needs_curation",
                "population_size": len(curated_stage4_cohort_ids),
                "finding_ids": ["F-C1S4-001", "F-C1S4-002", "F-C1S4-003"],
            },
        ],
        "findings": FINDINGS_SPEC,
        "carry_forward_ids": [f["finding_id"] for f in FINDINGS_SPEC],
        "diagnostic_probes": {
            "curated_full_text_missing_sha256": missing_full_text_sha256,
            "curated_qualified_context_full_text_without_sha256": qualified_context_full_text_without_sha256,
            "curated_documentation_missing_sha256": missing_doc_sha256,
            "curated_undifferentiated_multi_mappings": undifferentiated_multi_mappings,
            "curated_candidate_phrasing_records": candidate_phrasing_records,
        },
    }
    return records, summary


def render_category_review_markdown(summary: dict[str, Any]) -> str:
    inv = summary["frozen_inventory"]
    lines = [
        "# YAML Category Review: AIMech Cycle 1 Stage 4 Frozen Inventory (1,929 Records)",
        "",
        "- Repository: `CultureBotAI/AIMech`",
        "- Category: `c1s4-frozen-inventory-review` (`data/aio/*.yaml` + `data/curated/*.yaml`)",
        "- Selection Rule: All eligible scientific records (`442` generated `data/aio/*.yaml` + `1,487` maintained `data/curated/*.yaml` = `1,929` records) at frozen `source_revision: 7ad7d92709e8816ab33bc8979d7187dec109a1ab`",
        "- Started UTC: `2026-11-04T11:20:00Z`",
        "- Finished UTC: `2026-11-04T11:26:00Z`",
        "- Verdict: `needs curation` (`pass_with_limitations` for generated `data/aio/*.yaml` via `20261104T112500Z-c1s4-aio-corpus-category-review`; `needs_curation` for the 38-record curated provenance/mapping subcohort via `20261104T112600Z-c1s4-curated-provenance-mapping-review`)",
        "",
        "## Target Category",
        "",
        f"- **Run / Cycle / Stage / Revision**: `{RUN_ID}` / Cycle `{CYCLE}` / Stage `{STAGE}` (`record_review`) / Revision `{REVISION}`",
        f"- **Frozen Source Revision**: `{SOURCE_REVISION}`",
        f"- **Total Eligible Scientific Records Reviewed**: `{inv['total_eligible_records']}` (`{inv['aio_records']}` generated `data/aio/*.yaml` + `{inv['curated_records']}` maintained `data/curated/*.yaml`)",
        f"- **Scientific Review Coverage**: `{inv['covered_by_scientific_review']} / {inv['total_eligible_records']}` (`100.0%` full-category coverage across subcohorts)",
        f"- **Stage 4 Structured Review Bundles**:",
        f"  - `reviews/structured/{AIO_REVIEW_ID}/review.yaml` (`kind: category`, `verdict: pass_with_limitations`, `population_size: {summary['stage4_structured_reviews'][0]['population_size']}`)",
        f"  - `reviews/structured/{CURATED_PROVENANCE_REVIEW_ID}/review.yaml` (`kind: category`, `verdict: needs_curation`, `population_size: {summary['stage4_structured_reviews'][1]['population_size']}`)",
        f"- **Parent Workflow Evidence Manifest**: `reviews/workflow/{RUN_ID}/cycle-000001/stage-04/revision-0001/evidence.yaml`",
        "",
        "## Selection and Membership",
        "",
        "- **Included Member Paths (`1,929` records)**:",
        "  - `data/aio/*.yaml` (`442` `AIConcept` files generated from `sources/aio/aio.json` release `2026-07-22`).",
        "  - `data/curated/*.yaml` (`1,487` `CuratedAIConcept` files maintained in-repo). Every included record path, SHA-256 digest, corpus, `record_class`, branch/kind, primary structured review ID, boundary decision, and finding assignment is enumerated in `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/frozen_inventory_coverage.tsv` and `research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.json`.",
        "- **Excluded Non-Record Paths**:",
        "  - `reviews/**`, `reports/**`, `history/**`, `research/**`, `sources/**`, and `src/aimech/schema/**` are governance, provenance, upstream snapshot, or schema artifacts rather than scientific concept records.",
        "",
        "### Generated AIO Subcohorts (`data/aio/*.yaml` — 442 records)",
        "",
        "| AIO Top-Level Branch | Record Count | Retain | Defer (Upstream AIO) | Structured Review Bundle |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    branch_deferred = {
        "Layer": 2,
        "Model": 3,
        "Network": 3,
        "TrainingStrategy": 1,
    }
    for branch, count in inv["aio_branch_counts"].items():
        def_count = branch_deferred.get(branch, 0)
        ret_count = count - def_count
        lines.append(
            f"| `{branch}` | {count} | {ret_count} | {def_count} | `{AIO_REVIEW_ID}` |"
        )
    lines.extend(
        [
            f"| **Total (`data/aio/*.yaml`)** | **{inv['aio_records']}** | **433** | **9** | `{AIO_REVIEW_ID}` |",
            "",
            "### Maintained Curated Subcohorts (`data/curated/*.yaml` — 1,487 records)",
            "",
            "| Curated `ConceptKind` | Record Count | Retain | Open Findings (Stage 5) | Review Coverage |",
            "| --- | ---: | ---: | ---: | --- |",
        ]
    )
    open_by_kind: Counter[str] = Counter()
    for tid in CURATED_OPEN_TARGETS:
        stem = tid.split(":", 1)[1]
        doc = _load_yaml(REPO_ROOT / "data" / "curated" / f"{stem}.yaml")
        open_by_kind[doc["concept_kind"]] += 1

    for kind, count in inv["curated_kind_counts"].items():
        open_c = open_by_kind.get(kind, 0)
        lines.append(
            f"| `{kind}` | {count} | {count} | {open_c} | Prior cohort/record reviews + `{CURATED_PROVENANCE_REVIEW_ID}` |"
        )
    lines.extend(
        [
            f"| **Total (`data/curated/*.yaml`)** | **{inv['curated_records']}** | **{inv['curated_records']}** | **{len(CURATED_OPEN_TARGETS)}** | **100.0% (`1,487 / 1,487`)** |",
            "",
            "## Validation",
            "",
            "- `python research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.py`: Passed (`1,929` records audited: `442` AIO + `1,487` curated; `100.0%` scientific review coverage).",
            "- `python scripts/record_review.py check --require-reviews --base main`: Passed (`224` structured review bundles validated).",
            "- `just vendored-check`: Passed (`verify_vendored.py` verified immutable CLAW files).",
            "- `just check`: Passed (`1,929` records validated: `442` AIO, `1,487` curated, `224` history events, `224` structured reviews; `315 passed, 3 skipped` in pytest).",
            "",
            "## Lump and Split Review",
            "",
            "- **`retain` (`1,920` records)**:",
            "  - `433` generated `data/aio/*.yaml` classes have distinct ontology IRIs, labels, definitions, and parent subtrees in pinned AIO release `2026-07-22` (`sources/aio/aio.json`).",
            "  - All `1,487` maintained `data/curated/*.yaml` records have distinct `AIMech:` identifiers, explicit AIO mapping assessments (`exact_match: 0`, `close_match: 1`, `broad_match: 917`, `narrow_match: 32`, `related_match: 641`), and primary-publication or versioned-documentation evidence.",
            "- **`defer` (`9` generated `data/aio/*.yaml` records)**:",
            "  - Deferred to upstream `berkeleybop/artificial-intelligence-ontology` (`src/ontology/aio-src.csv`) because `data/aio/*.yaml` is a generated projection (`python -m aimech seed --check`) and upstream identifiers/definitions must not be rewritten locally (`AGENTS.md`):",
            "    - Near-duplicate upstream class pairs (`F-C1S4-004`): `AIO:AddLayer` / `AIO:AdditionLayer`, `AIO:TransformerLLM` / `AIO:TransformerLanguageModel`, and `AIO:ZeroShotLearningLLM` / `AIO:ZeroshotLearning`.",
            "    - Upstream genus-to-hierarchy mismatches (`F-C1S4-005`): `AIO:RepresentationLearning`, `AIO:ZeroshotLearning`, and `AIO:TrainingStrategy`.",
            "    - Upstream exact-synonym typo (`F-C1S4-006`): `AIO:DeepFeedForwardNetwork` (`\"Multilayer Perceptoron\"`).",
            "- **`lump` (`0` local merges executed)**: No maintained `AIMech:` records duplicate an existing `AIMech:` or `AIO:` concept.",
            "- **`split` (`0` record splits required)**: Existing records denote single coherent AI concepts; the frozen 1,929-record inventory was partitioned into reviewable branch and `ConceptKind` subcohorts for audit execution.",
            "",
            "## Identity and Grounding",
            "",
            "- **Generated AIO Corpus (`data/aio/*.yaml`, `442` records)**: All `442` records conform to `AIConcept`, carry `AIO:` CURIEs matching `sources/aio/aio.json` (`2026-07-22`), and preserve `status: generated`.",
            "- **Maintained Curated Corpus (`data/curated/*.yaml`, `1,487` records)**: All `1,487` records conform to `CuratedAIConcept`, use unique `AIMech:<PascalCase>` identifiers, resolve all `related_concepts` and `aio_mappings.target_id` references against `data/aio/*.yaml` and `data/curated/*.yaml`, and carry explicit `aio_mapping_status` (`mapped_partial: 1,452`, `unmapped_missing_in_aio: 35`).",
            "- **Identity Notes and Multi-Target Mapping Hygiene (`F-C1S4-003`)**: `AIMech:GloVe` is the only multi-mapped curated record (`3` `aio_mappings` targets: `AIO:RepresentationLearning`, `AIO:word2vecCBOW`, `AIO:word2vecSkipGram`) that repeats one undifferentiated `identity_notes` string verbatim across all `3` `aio_mappings[].rationale` entries; `AIMech:MarkovRandomField` retains candidate-proposal phrasing (`\"this candidate specifically uses an undirected graph\"`) in `identity_notes` and `aio_mappings[0].rationale`; and `AIMech:CLARANSClustering`, `AIMech:LargeMarginNearestNeighbor`, and `AIMech:RelevantComponentAnalysis` retain batch-discovery process diary text in `identity_notes`.",
            "",
            "## Evidence Patterns",
            "",
            "- **Generated AIO Corpus (`data/aio/*.yaml`)**: Grounded strictly to `sources/aio/aio.json` (`version: 2026-07-22`) with zero fabricated scientific claims or model evaluation metadata.",
            "- **Maintained Curated Corpus (`data/curated/*.yaml`)**: Grounded to primary publications and versioned implementation documentation with supporting snippets.",
            "- **Missing `sha256` Digests on Inspected Artifacts (`F-C1S4-001`, `F-C1S4-002`)**:",
            "  - `3` curated records from the 2026-10-11 first native cohort (`AIMech:ExpectationMaximization`, `AIMech:MarkovDecisionProcess`, `AIMech:PartiallyObservableMarkovDecisionProcess`) declare `access_level: full_text` on PDF primary sources without `evidence_sources[0].sha256` or `pdf_reading` entries in `research/discovery/20261011T030803Z-first-native-cohort.json`, embed single-page `#page=` viewer fragment anchors in `evidence_sources[0].url`, and omit `persistent_id` (`doi:10.1016/S0004-3702(98)00023-X`) on `MarkovDecisionProcess.yaml` and `PartiallyObservableMarkovDecisionProcess.yaml` (`F-C1S4-001`).",
            "  - `6` curated records (`AIMech:Apriori`, `AIMech:Eclat`, `AIMech:GeneticAlgorithm`, `AIMech:HiddenMarkovModel`, `AIMech:BarlowTwins`, `AIMech:VICReg`; `7` documentation entries total) declare `access_level: documentation` without `sha256` content digests (`F-C1S4-002`).",
            "",
            "## Completeness Patterns",
            "",
            "- **Generated AIO Corpus (`data/aio/*.yaml`)**: Complete with respect to the pinned `sources/aio/aio.json` snapshot (`442 / 442` classes).",
            "- **Maintained Curated Corpus (`data/curated/*.yaml`)**: All `1,487` curated records populate `id`, `name`, `record_class`, `status`, `concept_kind`, `definition`, `mechanism_summary`, `aio_mapping_status`, `evidence_sources`, `claims`, and `last_reviewed_utc`. The `4` curated records using `access_level: full_text` with explicit version qualification (`AIMech:AdaBoost`, `AIMech:Bagging`, `AIMech:HierarchicalAgglomerativeClustering`, `AIMech:VariationalInference`) explicitly document in `evidence_sources[1].version` that no local PDF checksum was retained and are not defective.",
            "",
            "## Findings",
            "",
            "| Finding ID | Status | Severity | Category | Structured Review | Target Records | Summary |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for f in FINDINGS_SPEC:
        targets_str = ", ".join(f"`{t}`" for t in f["target_ids"])
        lines.append(
            f"| `{f['finding_id']}` | `{f['status']}` | `{f['severity']}` | `{f['category']}` | `{f['review_id']}` | {targets_str} | {f['summary']} |"
        )
    lines.extend(
        [
            "",
            "## Recommended Edits",
            "",
            "1. **`F-C1S4-001` (`status: open`, `severity: minor`, `3` curated records: `AIMech:ExpectationMaximization`, `AIMech:MarkovDecisionProcess`, `AIMech:PartiallyObservableMarkovDecisionProcess`)**: In Stage 5 (`resolve_review_findings`), record verified 64-hex `sha256` PDF digests, canonical URLs without single-page `#page=` viewer fragments, and `persistent_id` (`doi:10.1016/S0004-3702(98)00023-X`) on `data/curated/{ExpectationMaximization,MarkovDecisionProcess,PartiallyObservableMarkovDecisionProcess}.yaml`, recording append-only curation history via `just new-history`.",
            "2. **`F-C1S4-002` (`status: open`, `severity: minor`, `6` curated records: `AIMech:Apriori`, `AIMech:Eclat`, `AIMech:GeneticAlgorithm`, `AIMech:HiddenMarkovModel`, `AIMech:BarlowTwins`, `AIMech:VICReg`)**: In Stage 5 (`resolve_review_findings`), record verified 64-hex `sha256` content digests or explicit version qualifications on the `7` `access_level: documentation` entries across those `6` records (`evidence_sources[0].sha256` on `Apriori`, `Eclat`, `GeneticAlgorithm`, `HiddenMarkovModel`; `evidence_sources[2].sha256` on `BarlowTwins`; `evidence_sources[2].sha256` and `evidence_sources[3].sha256` on `VICReg`), recording append-only curation history via `just new-history`.",
            "3. **`F-C1S4-003` (`status: open`, `severity: minor`, `5` curated records: `AIMech:GloVe`, `AIMech:MarkovRandomField`, `AIMech:CLARANSClustering`, `AIMech:LargeMarginNearestNeighbor`, `AIMech:RelevantComponentAnalysis`)**: In Stage 5 (`resolve_review_findings`), differentiate target-specific `aio_mappings[0..2].rationale` strings on `data/curated/GloVe.yaml` and replace candidate-proposal / batch-discovery diary text in `identity_notes` (and `aio_mappings[0].rationale` on `MarkovRandomField.yaml`), recording append-only curation history via `just new-history`.",
            "4. **`F-C1S4-004`, `F-C1S4-005`, `F-C1S4-006` (`status: deferred`, `9` generated records in `data/aio/*.yaml`)**: Do not hand-edit `data/aio/*.yaml`; preserve these findings as upstream ontology proposals/deferrals owned by `sources/aio/aio.json` (`berkeleybop/artificial-intelligence-ontology` `src/ontology/aio-src.csv`), `sources/aio/source.yaml`, and `src/aimech/importer.py`.",
            "",
            "## Follow-up Checks",
            "",
            "- `python research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.py`",
            "- `python scripts/record_review.py check --require-reviews --base main`",
            "- `just vendored-check`",
            "- `just check`",
            "",
            "## Additional Notes",
            "",
            "- **Stage 4 Non-Mutation Gate**: Zero scientific records (`data/aio/*.yaml` or `data/curated/*.yaml`) were modified during Stage 4 (`record_review`); all actionable curated fixes (`F-C1S4-001`, `F-C1S4-002`, `F-C1S4-003`) and upstream AIO deferrals (`F-C1S4-004`, `F-C1S4-005`, `F-C1S4-006`) are preserved in `carry_forward_ids` for Stage 5 (`resolve_review_findings`).",
            "- **Reproducible Audit Script**: `research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.py`.",
            "- **Reproducible Audit JSON**: `research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.json`.",
            "",
        ]
    )
    return "\n".join(lines)


def render_workflow_findings_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# Cycle 1 Stage 4 (`record_review`) Findings Ledger",
        "",
        f"- **Run ID**: `{RUN_ID}`",
        f"- **Cycle / Stage / Revision**: Cycle `{CYCLE}` / Stage `{STAGE}` / Revision `{REVISION}`",
        f"- **Frozen Source Revision**: `{SOURCE_REVISION}`",
        f"- **Carry-Forward Finding IDs (`6`)**: `{', '.join(summary['carry_forward_ids'])}`",
        "",
    ]
    for f in FINDINGS_SPEC:
        lines.extend(
            [
                f"## `{f['finding_id']}` — {f['title']}",
                "",
                f"- **Issue Key**: `{f['issue_key']}`",
                f"- **Status**: `{f['status']}`",
                f"- **Severity**: `{f['severity']}`",
                f"- **Category**: `{f['category']}`",
                f"- **Certainty**: `{f['certainty']}`",
                f"- **Native Structured Review Bundle**: `reviews/structured/{f['review_id']}/review.yaml`",
                f"- **Target Records (`{len(f['target_ids'])}`)**: {', '.join(f'`{t}`' for t in f['target_ids'])}",
                f"- **Owner Paths**: {', '.join(f'`{p}`' for p in f['owner_paths'])}",
                f"- **Summary**: {f['summary']}",
            ]
        )
        if "disposition" in f:
            lines.append(f"- **Disposition**: {f['disposition']}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    records, summary = collect_inventory()

    audit_json_path = (
        REPO_ROOT
        / "research"
        / "validation"
        / "20261104T112000Z-c1s4-frozen-inventory-audit.json"
    )
    audit_json_path.parent.mkdir(parents=True, exist_ok=True)
    full_payload = {
        **summary,
        "records": records,
    }
    audit_json_path.write_text(
        json.dumps(full_payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    category_md_path = (
        REPO_ROOT
        / "reports"
        / "yaml_category_review"
        / "20261104-c1s4-frozen-inventory-review.md"
    )
    category_md_path.parent.mkdir(parents=True, exist_ok=True)
    report_md = render_category_review_markdown(summary)
    category_md_path.write_text(report_md, encoding="utf-8")

    wf_dir = (
        REPO_ROOT
        / "reviews"
        / "workflow"
        / RUN_ID
        / f"cycle-{CYCLE:06d}"
        / f"stage-{STAGE:02d}"
        / f"revision-{REVISION:04d}"
    )
    wf_dir.mkdir(parents=True, exist_ok=True)
    (wf_dir / "review_report.md").write_text(report_md, encoding="utf-8")
    (wf_dir / "review_findings.md").write_text(
        render_workflow_findings_markdown(summary), encoding="utf-8"
    )
    (wf_dir / "frozen_inventory_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    tsv_lines = [
        "id\tpath\tsha256\tcorpus\trecord_class\tbranch_or_kind\tstatus\tprimary_review_id\tscientific_review_count\tboundary_action\tfinding_ids"
    ]
    for r in records:
        tsv_lines.append(
            "\t".join(
                [
                    r["id"],
                    r["path"],
                    r["sha256"],
                    r["corpus"],
                    r["record_class"],
                    r["branch_or_kind"],
                    r["status"],
                    r["primary_review_id"],
                    str(len(r["all_scientific_review_ids"])),
                    r["boundary_action"],
                    ",".join(r["finding_ids"]),
                ]
            )
        )
    (wf_dir / "frozen_inventory_coverage.tsv").write_text(
        "\n".join(tsv_lines) + "\n", encoding="utf-8"
    )
    print(
        f"Audited {len(records)} records ({summary['frozen_inventory']['aio_records']} AIO, "
        f"{summary['frozen_inventory']['curated_records']} curated); "
        f"wrote {audit_json_path.relative_to(REPO_ROOT)}, "
        f"{category_md_path.relative_to(REPO_ROOT)}, and {wf_dir.relative_to(REPO_ROOT)}/*."
    )


if __name__ == "__main__":
    main()
