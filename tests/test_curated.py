"""Scientific evidence and identity invariants for the maintained collection."""

from copy import deepcopy
from pathlib import Path
from shutil import copytree

import pytest
import yaml

from aimech.cli import main
from aimech.curated import validate_curated, validate_curated_record
from aimech.validation import read_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def record():
    source = read_record(ROOT / "sources/aio/source.yaml")
    citation = {"source_id": "method-paper", "locator": "Section 2, equation 1",
                "relation": "supports"}
    return {
        "id": "AIMech:ExampleMethod", "name": "Example test method",
        "definition": "A fictional method used only in validator tests.",
        "concept_kind": "algorithm", "identity_notes": "Synthetic test fixture, not curated data.",
        "definition_evidence": [citation],
        "claims": [{"claim_id": "procedure", "kind": "mechanism", "statement": "Test claim.",
                    "evidence": [deepcopy(citation)]}],
        "evidence_sources": [{"source_id": "method-paper", "title": "Synthetic test source",
                              "authors": ["Test Author"], "source_type": "primary_paper",
                              "url": "https://example.org/test", "version": "test version",
                              "access_level": "full_text", "accessed_at": "2026-01-01T00:00:00Z"}],
        "aio_snapshot": {"commit": source["commit"], "sha256": source["sha256"]},
        "aio_mappings": [{"target": "AIO:MachineLearningTask", "relation": "related_match",
                          "rationale": "Test relation, not an asserted is-a edge."}],
        "limitations": ["This is a test fixture."], "review_status": "DRAFT",
        "curation": {"created_at": "2026-01-01T00:00:00Z", "updated_at": "2026-01-01T00:00:00Z",
                     "curator": "Test curator", "method": "human"},
    }


@pytest.fixture
def corpus(tmp_path, record):
    copytree(ROOT / "sources/aio", tmp_path / "sources/aio")
    directory = tmp_path / "data/curated"
    directory.mkdir(parents=True)
    (directory / "ExampleMethod.yaml").write_text(yaml.safe_dump(record))
    return tmp_path


@pytest.mark.parametrize("kind", ["coordination_mechanism", "computational_paradigm"])
def test_source_defined_computational_kinds_are_closed(record, kind):
    record["concept_kind"] = kind
    assert validate_curated_record(record) == []
    record["concept_kind"] = kind + "_typo"
    assert any("concept_kind" in error for error in validate_curated_record(record))


def test_primary_monograph_type_keeps_evidence_requirements(record):
    source = record["evidence_sources"][0]
    source["source_type"] = "primary_monograph"
    assert validate_curated_record(record) == []
    source["access_level"] = "abstract_only"
    assert any("abstract-only" in error for error in validate_curated_record(record))
    source["access_level"] = "full_text"
    source["source_type"] = "primary_monograph_typo"
    assert any("source_type" in error for error in validate_curated_record(record))


def test_supported_record_and_collection_pass(record, corpus):
    assert validate_curated_record(record) == []
    assert validate_curated(corpus) == 0


@pytest.mark.parametrize("mutation,fragment", [
    (lambda r: r["definition_evidence"][0].update(source_id="missing"), "unresolved evidence"),
    (lambda r: r["evidence_sources"][0].update(access_level="abstract_only"), "abstract-only"),
    (lambda r: r["claims"][0]["evidence"][0].update(relation="context"), "supporting evidence"),
    (lambda r: r["claims"][0].update(kind="performance"), "evaluation context"),
    (lambda r: r["curation"].update(method="ai_assisted"), "model and agent_tool"),
    (lambda r: r["curation"].update(created_at="2026-02-30T00:00:00Z"), "calendar timestamp"),
    (lambda r: r["evidence_sources"][0].update(url="file:///tmp/paper.pdf"), "HTTP(S)"),
    (lambda r: r.update(id="AIO:ExampleMethod"), "does not match"),
    (lambda r: r.update(review_status="REVIEWED"), "REVIEWED"),
    (lambda r: r.update(unrecognized_assertion=True), "Additional properties"),
])
def test_rejects_invalid_evidence_and_provenance(record, mutation, fragment):
    mutation(record)
    assert any(fragment in error for error in validate_curated_record(record))


@pytest.mark.parametrize("field,value,fragment", [
    ("aio_mappings", [{"target": "AIO:DoesNotExist", "relation": "related_match",
                       "rationale": "Invalid target."}], "unresolved AIO mapping"),
    ("aio_snapshot", {"commit": "0" * 40, "sha256": "0" * 64}, "snapshot differs"),
    ("name", "Cluster analysis", "collides"),
    ("aliases", ["MLP"], "collides"),
])
def test_collection_checks_aio_identity_and_pin(corpus, record, field, value, fragment, capsys):
    record[field] = value
    (corpus / "data/curated/ExampleMethod.yaml").write_text(yaml.safe_dump(record))
    assert validate_curated(corpus) == 1
    assert fragment in capsys.readouterr().out


def test_cross_record_alias_collision_and_filename(corpus, record, capsys):
    record["id"] = "AIMech:AnotherMethod"
    record["name"] = "Another test method"
    record["aliases"] = ["example-test-method"]
    (corpus / "data/curated/wrong.yaml").write_text(yaml.safe_dump(record))
    assert validate_curated(corpus) == 1
    output = capsys.readouterr().out
    assert "collides" in output and "filename does not match" in output


def test_greek_pi_alias_is_distinct_from_aio_model(corpus, record, capsys):
    record.update(name="Pi-model", aliases=["Π-model"])
    path = corpus / "data/curated/ExampleMethod.yaml"
    path.write_text(yaml.safe_dump(record))
    assert validate_curated(corpus) == 0
    record["aliases"].append("Model")
    path.write_text(yaml.safe_dump(record))
    assert validate_curated(corpus) == 1
    assert "collides with AIO:Model" in capsys.readouterr().out


@pytest.mark.parametrize("name,alias", [("Π-model", "π MODEL"),
                                       ("Café method", "Cafe\u0301 METHOD")])
def test_unicode_equivalent_aliases_collide_across_records(corpus, record, capsys,
                                                         name, alias):
    record["name"] = name
    (corpus / "data/curated/ExampleMethod.yaml").write_text(yaml.safe_dump(record))
    duplicate = deepcopy(record)
    duplicate.update(id="AIMech:Duplicate", name="Different method", aliases=[alias])
    (corpus / "data/curated/Duplicate.yaml").write_text(yaml.safe_dump(duplicate))
    assert validate_curated(corpus) == 1
    assert "collides" in capsys.readouterr().out


def test_uncomposed_combining_mark_is_preserved(corpus, record):
    record["name"] = "q method"
    (corpus / "data/curated/ExampleMethod.yaml").write_text(yaml.safe_dump(record))
    distinct = deepcopy(record)
    distinct.update(id="AIMech:AccentedMethod", name="q\u0301 method")
    (corpus / "data/curated/AccentedMethod.yaml").write_text(yaml.safe_dump(distinct))
    assert validate_curated(corpus) == 0


def test_non_ascii_letters_are_valid_identity_content(record):
    record["name"] = "Π"
    assert validate_curated_record(record) == []


def test_plus_variants_coexist_but_equivalent_aliases_collide(corpus, record, capsys):
    for suffix, identifier in [("", "ExampleMethod"), ("+", "ExamplePlus"),
                               ("++", "ExamplePlusPlus")]:
        variant = deepcopy(record)
        variant.update(id=f"AIMech:{identifier}", name=f"PointNet{suffix}")
        (corpus / f"data/curated/{identifier}.yaml").write_text(yaml.safe_dump(variant))
    assert validate_curated(corpus) == 0
    duplicate = deepcopy(record)
    duplicate.update(id="AIMech:Duplicate", name="Different label", aliases=["POINT NET + +"])
    (corpus / "data/curated/Duplicate.yaml").write_text(yaml.safe_dump(duplicate))
    assert validate_curated(corpus) == 1
    output = capsys.readouterr().out
    assert "collides" in output
    assert "AIMech:ExamplePlusPlus" in output and "AIMech:Duplicate" in output


@pytest.mark.parametrize("name", ["+", "++", " - + + ", "\u0301", "∑∫"])
def test_plus_symbols_alone_are_not_identities(record, name):
    record["name"] = name
    assert any("letters or digits" in error for error in validate_curated_record(record))


def test_duplicate_plus_alias_within_record_is_rejected(record):
    record.update(name="PointNet++", aliases=["point-net + +"])
    assert any("duplicate normalized identity" in error
               for error in validate_curated_record(record))


def test_cli_checks_complete_collection_and_rejects_symlink(corpus, monkeypatch):
    monkeypatch.chdir(corpus)
    assert main(["validate-curated"]) == 0
    (corpus / "data/curated/alias.yaml").symlink_to("ExampleMethod.yaml")
    assert main(["validate-curated"]) == 1


def test_missing_and_empty_collections_fail(corpus):
    (corpus / "data/curated/ExampleMethod.yaml").unlink()
    assert validate_curated(corpus) == 1
    (corpus / "data/curated").rmdir()
    with pytest.raises(ValueError, match="missing"):
        validate_curated(corpus)


def test_quality_gate_includes_native_collection():
    from importlib.util import module_from_spec, spec_from_file_location
    spec = spec_from_file_location("native_check", ROOT / "scripts/check.py")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    assert any(command[-2:] == ["aimech", "validate-curated"]
               for command in module.commands({}))


@pytest.fixture
def unmapped(record):
    record.pop("aio_mappings")
    record["aio_no_match"] = {
        "search_scope": "All pinned AIO labels, synonyms and candidate definitions; test fixture.",
        "rationale": "No suitable counterpart was identified in the inspected snapshot.",
        "examined_targets": [{"target": "AIO:MachineLearningTask",
                              "rejection_reason": "This test concept is not a learning task."}],
    }
    return record


def test_no_match_assessment_passes_without_weakening_evidence(unmapped, corpus):
    assert validate_curated_record(unmapped) == []
    (corpus / "data/curated/ExampleMethod.yaml").write_text(yaml.safe_dump(unmapped))
    assert validate_curated(corpus) == 0
    unmapped["evidence_sources"][0]["access_level"] = "abstract_only"
    assert any("abstract-only" in error for error in validate_curated_record(unmapped))


@pytest.mark.parametrize("mutation,fragment", [
    (lambda r: r.pop("aio_no_match"), "exactly one"),
    (lambda r: r.update(aio_mappings=[{"target": "AIO:MachineLearningTask",
                                     "relation": "related_match", "rationale": "Conflicting."}]),
     "exactly one"),
    (lambda r: r["aio_no_match"].pop("search_scope"), "search_scope"),
    (lambda r: r["aio_no_match"].update(rationale=" "), "rationale"),
    (lambda r: r["aio_no_match"].update(examined_targets=[]), "examined_targets"),
    (lambda r: r["aio_no_match"]["examined_targets"][0].pop("rejection_reason"), "rejection_reason"),
    (lambda r: r["aio_no_match"]["examined_targets"].append(
        deepcopy(r["aio_no_match"]["examined_targets"][0])), "duplicate examined target"),
])
def test_rejects_missing_or_conflicting_mapping_assessment(unmapped, mutation, fragment):
    mutation(unmapped)
    assert any(fragment in error for error in validate_curated_record(unmapped))


@pytest.mark.parametrize("mutation,fragment", [
    (lambda r: r["aio_no_match"]["examined_targets"][0].update(target="AIO:DoesNotExist"),
     "unresolved examined AIO target"),
    (lambda r: r["aio_snapshot"].update(commit="0" * 40), "snapshot differs"),
    (lambda r: r.update(name="Cluster analysis"), "collides"),
])
def test_no_match_still_enforces_pin_and_identity(unmapped, corpus, mutation, fragment, capsys):
    mutation(unmapped)
    (corpus / "data/curated/ExampleMethod.yaml").write_text(yaml.safe_dump(unmapped))
    assert validate_curated(corpus) == 1
    assert fragment in capsys.readouterr().out
