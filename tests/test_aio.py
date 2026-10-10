"""Projection, negative provenance, and closed-schema regression checks."""

import copy
import json
import shutil
from pathlib import Path

import pytest
import yaml

from aimech import importer
from aimech.cli import main, validate
from aimech.validation import read_record, validate_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def records():
    return importer.build_records(ROOT)


def test_import_covers_pinned_aio_without_claiming_review(records):
    assert len(records) == 442
    branches = set()
    for text in records.values():
        record = yaml.safe_load(text)
        assert not validate_record(record)
        assert record["review_status"] == "NOT_REVIEWED"
        assert "curation_history" not in record
        branches.update(record["branches"])
    assert branches == {"Bias", "Layer", "MachineLearningTask", "MathematicalFunction",
                        "Model", "Network", "Preprocessing", "TrainingStrategy"}


def test_source_attribution_and_import_reproducible(records):
    assert records == importer.build_records(ROOT)
    record = yaml.safe_load(records["Model.yaml"])
    assert record["parents"] == ["owl:Thing"]
    assert record["provenance"]["source_commit"] == "397851c547d1c4d8f06ef184f63c1d40bc86937a"
    assert record["provenance"]["license"] == "CC-BY-4.0"


def test_all_named_hierarchy_and_component_edges_preserved(records):
    _, graph = importer.load_source(ROOT)
    parsed = [yaml.safe_load(text) for text in records.values()]
    assert sum(len(r["parents"]) for r in parsed) == sum(
        e["pred"] == "is_a" for e in graph["edges"]
    )
    assert sum(len(r.get("relationships", [])) for r in parsed) == sum(
        e["pred"] == importer.HAS_PART for e in graph["edges"]
    )
    assert sum(len(r.get("synonyms", [])) for r in parsed) == sum(
        len(n.get("meta", {}).get("synonyms", [])) for n in graph["nodes"]
    )


@pytest.mark.parametrize("mutation", [
    lambda r: r.update(unknown_field=True),
    lambda r: r.update(definition=""),
    lambda r: r.update(id="AIO:Different"),
    lambda r: r.update(parents=["not a curie"]),
    lambda r: r.update(review_status="REVIEWED"),
    lambda r: r["provenance"].update(license="CC0"),
    lambda r: r["provenance"].update(imported_at="2026-02-31T00:00:00Z"),
    lambda r: r["provenance"].update(unrecognized="value"),
    lambda r: r.update(branches=[]),
    lambda r: r.update(curation_history=[{"timestamp": "2206-01-01T00:00:00Z",
        "curator": "test", "action": "EDIT", "notes": "test"}]),
])
def test_mutations_fail_closed(records, mutation):
    record = yaml.safe_load(records["Model.yaml"])
    mutation(record)
    assert validate_record(record)


def test_duplicate_yaml_keys_rejected(tmp_path):
    path = tmp_path / "duplicate.yaml"
    path.write_text("id: AIO:Model\nid: AIO:Network\n")
    with pytest.raises(yaml.YAMLError, match="duplicate"):
        read_record(path)


def test_seed_is_dry_run_and_refuses_overwrite(tmp_path):
    shutil.copytree(ROOT / "sources", tmp_path / "sources")
    assert importer.seed(tmp_path) == 0
    assert not (tmp_path / "data").exists()
    assert importer.seed(tmp_path, check=True) == 1
    assert importer.seed(tmp_path, write=True) == 0
    assert importer.seed(tmp_path, check=True) == 0
    target = tmp_path / "data/aio/Model.yaml"
    target.write_text(target.read_text() + "# curator edit\n")
    before = target.read_bytes()
    assert importer.seed(tmp_path, check=True) == 1
    with pytest.raises(ValueError, match="refusing to overwrite"):
        importer.seed(tmp_path, write=True)
    assert target.read_bytes() == before


def test_unexpected_and_symlink_output_refused(tmp_path):
    shutil.copytree(ROOT / "sources", tmp_path / "sources")
    destination = tmp_path / "data/aio"
    destination.mkdir(parents=True)
    (destination / "unexpected.txt").write_text("user data")
    with pytest.raises(ValueError, match="unexpected"):
        importer.seed(tmp_path, write=True)
    assert (destination / "unexpected.txt").read_text() == "user data"


def test_reproduction_detects_line_ending_byte_changes(tmp_path, records, monkeypatch):
    one = {"Model.yaml": records["Model.yaml"]}
    monkeypatch.setattr(importer, "build_records", lambda root: one)
    assert importer.seed(tmp_path, write=True) == 0
    target = tmp_path / "data/aio/Model.yaml"
    target.write_bytes(target.read_bytes().replace(b"\n", b"\r\n"))
    assert importer.seed(tmp_path, check=True) == 1


def test_source_corruption_rejected(tmp_path):
    shutil.copytree(ROOT / "sources", tmp_path / "sources")
    path = tmp_path / "sources/aio/aio.json"
    path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="checksum"):
        importer.load_source(tmp_path)


@pytest.mark.parametrize("component", ["data", "data/aio"])
def test_seed_rejects_symlink_directory_components(tmp_path, component):
    root = tmp_path / "repo"
    shutil.copytree(ROOT / "sources", root / "sources")
    outside = tmp_path / "outside"
    outside.mkdir()
    link = root / component
    link.parent.mkdir(parents=True, exist_ok=True)
    link.symlink_to(outside, target_is_directory=True)
    for mode in ({"write": True}, {"check": True}, {}):
        with pytest.raises(ValueError, match="symlink"):
            importer.seed(root, **mode)
    assert list(outside.iterdir()) == []


@pytest.mark.parametrize("defect", ["cycle", "missing_edge_target", "duplicate_id", "relation"])
def test_bad_graph_rejected(monkeypatch, defect):
    source, graph = copy.deepcopy(importer.load_source(ROOT))
    if defect == "cycle":
        graph["edges"].append({"sub": importer.AIO + "Model", "pred": "is_a",
                               "obj": importer.AIO + "Model"})
    elif defect == "missing_edge_target":
        graph["edges"][0]["obj"] = importer.AIO + "DoesNotExist"
    elif defect == "duplicate_id":
        graph["nodes"].append(next(n for n in graph["nodes"] if n.get("type") == "CLASS"))
    else:
        graph["edges"][0]["pred"] = "unsupported"
    monkeypatch.setattr(importer, "load_source", lambda root: (source, graph))
    with pytest.raises(ValueError):
        importer.build_records(ROOT)


def test_empty_and_missing_validation_fail(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="no records"):
        validate([tmp_path])
    monkeypatch.chdir(tmp_path)
    assert main(["validate"]) == 1
    assert main(["check-source"]) == 1


def test_cli_rejects_dangling_history_references(tmp_path, monkeypatch, records):
    record = yaml.safe_load(records["Model.yaml"])
    record["history_refs"] = ["history/record/Model/missing.yaml"]
    target = tmp_path / "Model.yaml"
    target.write_text(yaml.safe_dump(record))
    monkeypatch.chdir(tmp_path)
    assert validate([target]) == 1


def test_snapshot_json_is_unchanged_format():
    source, graph = importer.load_source(ROOT)
    assert json.loads((ROOT / source["snapshot"]).read_text())["graphs"][0] == graph
