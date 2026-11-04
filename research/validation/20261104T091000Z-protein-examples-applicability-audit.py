"""Deterministic full-corpus and schema audit of UniProt protein-example applicability in AIMech.

Audits src/aimech/schema/aimech.yaml, src/aimech/schema/curated_concept.yaml,
src/aimech/schema/mech_shared.yaml, all data/aio/*.yaml records, and all
data/curated/*.yaml records for Cycle 1, Stage 3 (protein_examples) of
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
AUDIT_TIMESTAMP = "2026-11-04T09:10:00Z"

PROTEIN_EXAMPLE_CANDIDATE_SLOTS = (
    "protein_examples",
    "protein_example",
    "proteins",
    "uniprot",
    "uniprot_id",
    "uniprot_ids",
    "uniprot_accession",
    "uniprot_kb",
    "gene_examples",
    "gene_symbol",
    "gene_id",
    "ncbi_gene_id",
    "hgnc_id",
    "protein_targets",
    "enzymes",
    "substrates",
    "products",
    "sequence",
    "amino_acid_sequence",
    "pdb_id",
    "causal_graph",
    "causal_graphs",
    "pathways",
    "biological_processes",
)

BIOLOGICAL_PREFIX_CANDIDATES = (
    "UniProt",
    "UniProtKB",
    "uniprot",
    "HGNC",
    "NCBIGene",
    "PR",
    "GO",
    "PDB",
    "ENSEMBL",
    "REFSEQ",
)

PROTEIN_DIRECT_PATTERN = re.compile(
    r"\b(uniprot|uniprotkb|swiss-prot|trembl|protein|proteins|proteome|proteomic|"
    r"proteomics|peptide|polypeptide|amino acid|alphafold|esmfold|rosettafold|pdb)\b",
    re.IGNORECASE,
)

UNIPROT_CURIE_PATTERN = re.compile(
    r"\b(?:UniProt(?:KB)?|Swiss-Prot|TrEMBL):[A-Za-z0-9_-]+\b"
)

BROAD_BIOLOGICAL_PATTERN = re.compile(
    r"\b(uniprot|swiss-prot|trembl|protein|proteins|proteome|proteomic|proteomics|"
    r"peptide|polypeptide|amino acid|alphafold|esmfold|rosettafold|pdb|gene|genes|"
    r"genomic|genomics|genome|dna|rna|enzyme|metabolic|bioinformatics|biological|"
    r"biomedical)\b",
    re.IGNORECASE,
)

BIO_INSPIRED_METAPHOR_RECORDS = frozenset(
    {
        "AIMech:AntColonyOptimization",
        "AIMech:EstimationOfDistributionAlgorithms",
        "AIMech:GeneticAlgorithm",
        "AIMech:GuidedGeneticAlgorithm",
        "AIMech:OjaLearningRule",
        "AIMech:ParticleSwarmOptimization",
        "AIMech:RegularizedEvolution",
        "AIMech:Stigmergy",
        "AIMech:SwarmIntelligence",
        "AIMech:UnivariateMarginalDistributionAlgorithm",
    }
)

ACRONYM_HOMONYM_RECORDS = frozenset(
    {
        "AIMech:GENET",
        "AIMech:LSvrgAndLKatyushaLooplessVarianceReducedGradientMethods",
        "AIMech:RegularizedNonlinearAccelerationOfFixedPointIterations",
    }
)

DOWNSTREAM_DATASET_CONTEXT_RECORDS = frozenset(
    {
        "AIMech:AutoPoissonMarkovRandomField",
        "AIMech:BayesOptimalPValueWeightingUnderGaussianPrior",
        "AIMech:CliXO",
        "AIMech:CovariatePoweredCrossWeightedMultipleTesting",
        "AIMech:DARTDifferentiablePromptFewShotTuning",
        "AIMech:ExactPoClustering",
        "AIMech:FedKdCommunicationEfficientFederatedLearningViaKnowledgeDistillation",
        "AIMech:HACE",
        "AIMech:HACES",
        "AIMech:HACQ",
        "AIMech:HiddenMarkovModelWithAuxiliaryMemory",
        "AIMech:INLAGroupNodeConflictDiagnostic",
        "AIMech:LeftTruncatedCauchyCombinationTest",
        "AIMech:MoRA",
        "AIMech:NeXOOntologyAlignment",
        "AIMech:NeXOOntologyConstruction",
        "AIMech:OptimalSpjotvollAndSieveGroupedPValueWeighting",
        "AIMech:PARADEPassageRepresentationAggregationForDocumentReranking",
        "AIMech:RandomizedLatentScoreConflictDiagnostic",
        "AIMech:SupervisedPrincipalComponents",
    }
)

YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def classify_broad_biological_record(rec_id: str) -> str:
    if rec_id in BIO_INSPIRED_METAPHOR_RECORDS:
        return "bio_inspired_metaphor"
    if rec_id in ACRONYM_HOMONYM_RECORDS:
        return "acronym_or_homonym"
    if rec_id in DOWNSTREAM_DATASET_CONTEXT_RECORDS:
        return "downstream_dataset_context"
    return "negative_scope_or_benchmark_disclaimer"


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
    prefixes = doc.get("prefixes") or {}
    classes = doc.get("classes") or {}
    enums = doc.get("enums") or {}
    class_slots: dict[str, list[str]] = {}
    all_slots: set[str] = set()
    for cls_name, cls_def in sorted(classes.items()):
        attrs = sorted((cls_def or {}).get("attributes", {}).keys())
        class_slots[cls_name] = attrs
        all_slots.update(attrs)
    present_protein_slots = sorted(
        all_slots.intersection(PROTEIN_EXAMPLE_CANDIDATE_SLOTS)
    )
    present_bio_prefixes = sorted(
        set(prefixes.keys()).intersection(BIOLOGICAL_PREFIX_CANDIDATES)
    )
    return {
        "path": rel_path,
        "sha256": sha256_file(path),
        "id": doc.get("id"),
        "name": doc.get("name"),
        "description": doc.get("description"),
        "prefixes": dict(sorted(prefixes.items())),
        "imports": doc.get("imports", []),
        "classes": class_slots,
        "enums": {
            enum_name: sorted(
                ((enum_def or {}).get("permissible_values") or {}).keys()
            )
            for enum_name, enum_def in sorted(enums.items())
        },
        "biological_prefixes_present": present_bio_prefixes,
        "protein_example_candidate_slots_present": present_protein_slots,
    }


def audit_aio_corpus() -> dict[str, Any]:
    aio_paths = sorted((ROOT / "data" / "aio").glob("*.yaml"))
    top_level_keys: Counter[str] = Counter()
    branch_counts: Counter[str] = Counter()
    relationship_predicates: Counter[str] = Counter()
    records_with_relationships: list[dict[str, Any]] = []
    records_with_discussions: list[str] = []
    records_with_protein_slots: list[str] = []
    records_with_uniprot_curies: list[dict[str, Any]] = []
    protein_direct_records: list[dict[str, Any]] = []
    broad_biological_records: list[dict[str, Any]] = []
    total_parent_edges = 0
    total_relationship_edges = 0
    total_synonyms = 0

    for path in aio_paths:
        raw_text = path.read_text(encoding="utf-8")
        doc = yaml.load(raw_text, Loader=YAML_LOADER)
        rec_id = str(doc["id"])
        name = str(doc.get("name", ""))
        definition = str(doc.get("definition", ""))
        for k in doc.keys():
            top_level_keys[k] += 1
            if k in PROTEIN_EXAMPLE_CANDIDATE_SLOTS:
                records_with_protein_slots.append(rec_id)
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

        curies = sorted(set(UNIPROT_CURIE_PATTERN.findall(raw_text)))
        if curies:
            records_with_uniprot_curies.append(
                {
                    "id": rec_id,
                    "path": str(path.relative_to(ROOT)),
                    "curies": curies,
                }
            )

        direct_matched = sorted(
            {m.lower() for m in PROTEIN_DIRECT_PATTERN.findall(raw_text)}
        )
        if direct_matched:
            protein_direct_records.append(
                {
                    "id": rec_id,
                    "path": str(path.relative_to(ROOT)),
                    "name": name,
                    "branches": doc.get("branches", []),
                    "matched_terms": direct_matched,
                    "definition": definition,
                }
            )

        broad_matched = sorted(
            {m.lower() for m in BROAD_BIOLOGICAL_PATTERN.findall(raw_text)}
        )
        if broad_matched:
            broad_biological_records.append(
                {
                    "id": rec_id,
                    "path": str(path.relative_to(ROOT)),
                    "name": name,
                    "branches": doc.get("branches", []),
                    "matched_terms": broad_matched,
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
        "records_with_relationships_count": len(records_with_relationships),
        "synonym_count": total_synonyms,
        "records_with_discussions_count": len(records_with_discussions),
        "records_with_protein_example_slots_count": len(records_with_protein_slots),
        "records_with_uniprot_curies_count": len(records_with_uniprot_curies),
        "protein_direct_records_count": len(protein_direct_records),
        "protein_direct_records": protein_direct_records,
        "broad_biological_records_count": len(broad_biological_records),
        "broad_biological_records": broad_biological_records,
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
    records_with_protein_slots: list[str] = []
    records_with_uniprot_curies: list[dict[str, Any]] = []
    protein_direct_records: list[dict[str, Any]] = []
    broad_biological_records: list[dict[str, Any]] = []

    for path in curated_paths:
        raw_text = path.read_text(encoding="utf-8")
        doc = yaml.load(raw_text, Loader=YAML_LOADER)
        rec_id = str(doc["id"])
        name = str(doc.get("name", ""))
        concept_kind = str(doc.get("concept_kind", ""))
        concept_kind_counts[concept_kind] += 1

        for k in doc.keys():
            top_level_keys[k] += 1
            if k in PROTEIN_EXAMPLE_CANDIDATE_SLOTS:
                records_with_protein_slots.append(rec_id)

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

        curies = sorted(set(UNIPROT_CURIE_PATTERN.findall(raw_text)))
        if curies:
            records_with_uniprot_curies.append(
                {
                    "id": rec_id,
                    "path": str(path.relative_to(ROOT)),
                    "curies": curies,
                }
            )

        direct_matched = sorted(
            {m.lower() for m in PROTEIN_DIRECT_PATTERN.findall(raw_text)}
        )
        if direct_matched:
            matching_claims = [
                {
                    "claim_id": str(c.get("claim_id")),
                    "kind": str(c.get("kind")),
                    "statement": str(c.get("statement")),
                }
                for c in claims
                if PROTEIN_DIRECT_PATTERN.search(str(c.get("statement", "")))
            ]
            protein_direct_records.append(
                {
                    "id": rec_id,
                    "path": str(path.relative_to(ROOT)),
                    "name": name,
                    "concept_kind": concept_kind,
                    "matched_terms": direct_matched,
                    "matching_claims": matching_claims,
                }
            )

        broad_matched = sorted(
            {m.lower() for m in BROAD_BIOLOGICAL_PATTERN.findall(raw_text)}
        )
        if broad_matched:
            category = classify_broad_biological_record(rec_id)
            broad_biological_records.append(
                {
                    "id": rec_id,
                    "path": str(path.relative_to(ROOT)),
                    "name": name,
                    "concept_kind": concept_kind,
                    "matched_terms": broad_matched,
                    "category": category,
                }
            )

    broad_category_counts = Counter(r["category"] for r in broad_biological_records)

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
        "records_with_protein_example_slots_count": len(records_with_protein_slots),
        "records_with_uniprot_curies_count": len(records_with_uniprot_curies),
        "protein_direct_records_count": len(protein_direct_records),
        "protein_direct_records": protein_direct_records,
        "broad_biological_records_count": len(broad_biological_records),
        "broad_biological_category_counts": dict(sorted(broad_category_counts.items())),
        "broad_biological_records": broad_biological_records,
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
    stage_3_override = next(
        s for s in workflow_doc["stages"] if s["stage"] == 3
    )

    total_records = aio_summary["record_count"] + curated_summary["record_count"]
    total_protein_slot_records = (
        aio_summary["records_with_protein_example_slots_count"]
        + curated_summary["records_with_protein_example_slots_count"]
    )
    total_uniprot_curie_records = (
        aio_summary["records_with_uniprot_curies_count"]
        + curated_summary["records_with_uniprot_curies_count"]
    )

    assert aio_summary["record_count"] == 442
    assert curated_summary["record_count"] == 1487
    assert (
        curated_summary["records_with_aio_mappings_count"]
        + curated_summary["records_with_aio_no_match_count"]
        == curated_summary["record_count"]
    )
    assert total_records == 1929
    assert total_protein_slot_records == 0
    assert total_uniprot_curie_records == 0
    assert aio_summary["protein_direct_records_count"] == 0
    assert curated_summary["protein_direct_records_count"] == 3
    assert aio_summary["broad_biological_records_count"] == 3
    assert curated_summary["broad_biological_records_count"] == 95
    cat_counts = curated_summary["broad_biological_category_counts"]
    assert sum(cat_counts.values()) == 95
    assert schemas["aimech"]["protein_example_candidate_slots_present"] == []
    assert schemas["curated_concept"]["protein_example_candidate_slots_present"] == []
    assert schemas["mech_shared"]["protein_example_candidate_slots_present"] == []
    assert schemas["aimech"]["biological_prefixes_present"] == []
    assert schemas["curated_concept"]["biological_prefixes_present"] == []
    assert schemas["mech_shared"]["biological_prefixes_present"] == []
    assert stage_3_override["key"] == "protein_examples"
    assert stage_3_override["applicability"] == "not_applicable"

    return {
        "audit_id": "20261104T091000Z-protein-examples-applicability-audit",
        "created_at": AUDIT_TIMESTAMP,
        "run_id": "mech-goal-sequence-20261019",
        "cycle": 1,
        "stage": 3,
        "stage_key": "protein_examples",
        "applicability_verdict": "not_applicable",
        "workflow_profile": {
            "path": "workflow/mech-workflow.yaml",
            "sha256": sha256_file(workflow_path),
            "stage_3_override": stage_3_override,
        },
        "corpus_totals": {
            "aio_generated_records": aio_summary["record_count"],
            "curated_aimech_records": curated_summary["record_count"],
            "total_records_inspected": total_records,
            "records_with_protein_example_slots": total_protein_slot_records,
            "records_with_uniprot_curies": total_uniprot_curie_records,
            "aio_records_matching_protein_terms": aio_summary[
                "protein_direct_records_count"
            ],
            "curated_records_matching_protein_terms": curated_summary[
                "protein_direct_records_count"
            ],
            "aio_records_matching_broad_biological_terms": aio_summary[
                "broad_biological_records_count"
            ],
            "curated_records_matching_broad_biological_terms": curated_summary[
                "broad_biological_records_count"
            ],
        },
        "schemas": schemas,
        "aio_corpus_inventory": aio_summary,
        "curated_corpus_inventory": curated_summary,
        "ontology_and_entity_boundary_distinction": {
            "zero_uniprot_prefixes_or_slots": (
                "All 3 LinkML schema modules (src/aimech/schema/aimech.yaml, "
                "src/aimech/schema/curated_concept.yaml, src/aimech/schema/mech_shared.yaml) "
                "declare 0 biological entity prefixes (UniProt, UniProtKB, HGNC, NCBIGene, "
                "GO, PR, PDB) and 0 protein-example or gene-example slots. In mech_shared.yaml, "
                "the word 'protein' appears only in cross-fleet docstrings warning that "
                "'Sharing a protein or a reaction supplies a curation lead, not an assertion "
                "of record equivalence or biological mechanism' and in DatasetTypeEnum.PROTEOMICS "
                "(an unimported class in AIMech records)."
            ),
            "aio_taxonomic_and_mereological_axioms": (
                f"{aio_summary['taxonomic_parent_edge_count']} parents edges and "
                f"{aio_summary['mereological_relationship_edge_count']} BFO:0000051 ('has part') "
                f"relationships across {aio_summary['record_count']} generated AIO records "
                "classify AI layers, models, networks, tasks, mathematical functions, "
                "preprocessing methods, training strategies, and biases; 0 AIO records "
                "mention UniProt or proteins, and only 3 AIO records (AIO:ArtificialNeuralNetwork, "
                "AIO:SpikingHiddenLayer, AIO:SurvivalAnalysis) mention 'biological' to contrast "
                "artificial neural units with biological neurons or note time-to-event subjects."
            ),
            "curated_protein_term_occurrences_are_limitation_disclaimers": (
                "Across all 1,487 maintained curated AI-concept records, 0 records contain "
                "UniProt accessions/CURIEs and only 3 records (AIMech:BrandesPichPivotCentralityEstimation, "
                "AIMech:ZhouAttractorCommunityDetection, AIMech:ZhouRandomWalkDissimilarity) "
                "mention the token 'protein'. In all 3 records, the token appears strictly "
                "inside kind='limitation' claims noting that historical benchmark evaluations "
                "on yeast protein-interaction networks do not establish biological-function "
                "prediction, protein transport/essentiality mechanisms, or causal biology."
            ),
            "broad_biological_term_classification": (
                f"Across all {curated_summary['broad_biological_records_count']} curated records "
                "matching broad biological/bioinformatics/genomic/biomedical tokens, every match "
                "falls into one of four mutually exclusive non-protein-instance categories: "
                f"(1) explicit negative-scope or benchmark disclaimers in limitations or claims "
                f"({cat_counts['negative_scope_or_benchmark_disclaimer']} records, including the 3 "
                "historical yeast protein-interaction network disclaimers); "
                f"(2) bio-inspired optimization/neural-learning metaphors where 'genes' or 'biological' "
                f"denote candidate solution encodings or heuristics ({cat_counts['bio_inspired_metaphor']} "
                "records, e.g. GeneticAlgorithm, GuidedGeneticAlgorithm, "
                "EstimationOfDistributionAlgorithms, RegularizedEvolution, OjaLearningRule, SwarmIntelligence); "
                f"(3) acronym/homonym collisions ({cat_counts['acronym_or_homonym']} records: 'RNA' = "
                "Regularized Nonlinear Acceleration in RegularizedNonlinearAccelerationOfFixedPointIterations "
                "and LSvrgAndLKatyushaLooplessVarianceReducedGradientMethods; 'GENET' = constraint-satisfaction "
                "neural network); and "
                f"(4) downstream biomedical/genomic/ontology evaluation dataset contexts for general-purpose "
                f"statistical, graph-clustering, or NLP methods ({cat_counts['downstream_dataset_context']} "
                "records, e.g. CliXO, NeXOOntologyAlignment, NeXOOntologyConstruction, HACE, HACES, HACQ, "
                "CovariatePoweredCrossWeightedMultipleTesting, LeftTruncatedCauchyCombinationTest, "
                "SupervisedPrincipalComponents, HiddenMarkovModelWithAuxiliaryMemory)."
            ),
        },
        "future_representation_assessment": {
            "biological_uniprot_protein_examples": "not_applicable",
            "candidate_native_analog": (
                "Biological UniProt protein examples do not apply to AIMech's AI-concept domain "
                "or LinkML schemas. Even if AIMech later curates AI architectures designed for "
                "computational biology (such as protein language models or equivariant structure-prediction "
                "networks), those records will represent the mathematical/algorithmic architecture or "
                "model family under CuratedAIConcept (with benchmark datasets captured in "
                "EvaluationContext.dataset_and_split when performance claims are curated), never "
                "biological UniProt protein records or molecular mechanism assertions. Stage 3 "
                "(protein_examples) should remain not_applicable in workflow/mech-workflow.yaml."
            ),
        },
        "script_path": "research/validation/20261104T091000Z-protein-examples-applicability-audit.py",
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
