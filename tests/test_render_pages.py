"""Tests for AIMech static site generation and GitHub Pages artifacts."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
PAGES_DIR = REPO_ROOT / "pages"
AIO_DIR = REPO_ROOT / "data" / "aio"
CURATED_DIR = REPO_ROOT / "data" / "curated"


def test_render_pages_check_passes():
    result = subprocess.run(
        [sys.executable, "scripts/render_pages.py", "--check"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, f"render_pages --check failed:\n{result.stderr}\n{result.stdout}"
    assert "pages/ is current" in result.stdout


def test_required_site_assets_exist():
    assert (PAGES_DIR / ".nojekyll").is_file()
    assert (PAGES_DIR / "style.css").is_file()
    assert (PAGES_DIR / "theme-toggle.js").is_file()
    assert (PAGES_DIR / "record-browser.js").is_file()
    assert (PAGES_DIR / "index.html").is_file()
    assert (PAGES_DIR / "browse.html").is_file()
    assert (PAGES_DIR / "404.html").is_file()
    assert (PAGES_DIR / "index.json").is_file()
    assert (REPO_ROOT / "index.html").is_file()

    root_redirect = (REPO_ROOT / "index.html").read_text(encoding="utf-8")
    assert 'url=pages/index.html' in root_redirect


def test_index_json_covers_all_records():
    data = json.loads((PAGES_DIR / "index.json").read_text(encoding="utf-8"))
    aio_files = list(AIO_DIR.glob("*.yaml"))
    curated_files = list(CURATED_DIR.glob("*.yaml"))
    expected_total = len(aio_files) + len(curated_files)

    assert len(data) == expected_total
    assert len(data) >= 912

    origins = {r["origin"] for r in data}
    assert origins == {"curated", "aio"}

    curated_in_index = [r for r in data if r["origin"] == "curated"]
    aio_in_index = [r for r in data if r["origin"] == "aio"]
    assert len(curated_in_index) == len(curated_files)
    assert len(curated_in_index) >= 470
    assert len(aio_in_index) == len(aio_files) == 442

    for r in data:
        assert r["id"].startswith("AIO:") or r["id"].startswith("AIMech:")
        assert r["slug"]
        assert r["name"]
        assert r["page"].endswith(".html")
        page_file = PAGES_DIR / r["page"]
        assert page_file.is_file(), f"Missing page for {r['id']}: {page_file}"


def test_curated_concept_page_content():
    adam_html = (PAGES_DIR / "curated" / "Adam.html").read_text(encoding="utf-8")
    assert "Adam</h1>" in adam_html
    assert "AIMech:Adam" in adam_html
    assert "Algorithms" in adam_html
    assert "AIO:TrainingStrategy" in adam_html
    assert "Adam: A Method for Stochastic Optimization" in adam_html
    assert "arXiv:1412.6980v9" in adam_html
    assert "Curated Limitations" in adam_html


def test_aio_concept_page_content():
    ts_html = (PAGES_DIR / "aio" / "TrainingStrategy.html").read_text(encoding="utf-8")
    assert "TrainingStrategy</h1>" in ts_html
    assert "AIO:TrainingStrategy" in ts_html
    assert "https://w3id.org/aio/TrainingStrategy" in ts_html
    assert "Curated AIMech Concepts Grounded to this Class" in ts_html
    assert "AdaMax" in ts_html
    assert "AMSGrad" in ts_html


def test_curated_kind_pages():
    kinds_dir = PAGES_DIR / "kinds"
    assert kinds_dir.is_dir()

    curated_docs = [yaml.safe_load(p.read_text()) for p in CURATED_DIR.glob("*.yaml")]
    unique_kinds = {d["concept_kind"] for d in curated_docs if d.get("concept_kind")}

    schema = yaml.safe_load(
        (REPO_ROOT / "src/aimech/schema/curated_concept.yaml").read_text()
    )
    declared_kinds = set(schema["enums"]["ConceptKind"]["permissible_values"])
    assert unique_kinds <= declared_kinds
    assert {p.stem for p in kinds_dir.glob("*.html")} == unique_kinds
    for kind in unique_kinds:
        kind_file = kinds_dir / f"{kind}.html"
        assert kind_file.is_file(), f"Missing kind page: {kind_file}"
        content = kind_file.read_text(encoding="utf-8")
        assert "conceptTable" in content


def test_aio_branch_pages():
    branches_dir = PAGES_DIR / "branches"
    assert branches_dir.is_dir()

    aio_docs = [yaml.safe_load(p.read_text()) for p in AIO_DIR.glob("*.yaml")]
    unique_branches = {b for d in aio_docs for b in d.get("branches", [])}

    assert len(unique_branches) == 8
    for branch in unique_branches:
        branch_file = branches_dir / f"{branch}.html"
        assert branch_file.is_file(), f"Missing branch page: {branch_file}"
        content = branch_file.read_text(encoding="utf-8")
        assert "conceptTable" in content


def test_theme_toggle_is_vendored_and_loaded():
    toggle_script = (PAGES_DIR / "theme-toggle.js").read_text(encoding="utf-8")
    assert "Mech theme toggle" in toggle_script
    assert "mech-theme" in toggle_script

    for page_name in ["index.html", "browse.html", "404.html", "map.html"]:
        content = (PAGES_DIR / page_name).read_text(encoding="utf-8")
        assert "theme-toggle.js" in content
        assert "style.css" in content


def test_embedding_map_and_unified_layout():
    map_json = REPO_ROOT / "data" / "embeddings" / "corpus_map.json"
    assert map_json.is_file()
    map_data = json.loads(map_json.read_text(encoding="utf-8"))
    assert map_data["model"] == "BAAI/bge-large-en-v1.5"
    assert map_data["method"] == "pacmap"
    assert map_data["n"] == len(map_data["points"])
    assert map_data["n"] >= 1200

    map_html = (PAGES_DIR / "map.html").read_text(encoding="utf-8")
    assert 'id="corpus-map"' in map_html
    assert 'id="corpus-map-data"' in map_html
    assert 'class="facet-sidebar"' in map_html
    assert 'class="browse-layout"' in map_html

    index_html = (PAGES_DIR / "index.html").read_text(encoding="utf-8")
    assert 'class="hero-search"' in index_html
    assert 'action="browse.html"' in index_html
    assert 'href="map.html"' in index_html

    browse_html = (PAGES_DIR / "browse.html").read_text(encoding="utf-8")
    assert 'class="facet-sidebar"' in browse_html
    assert 'class="browse-layout"' in browse_html

    adam_html = (PAGES_DIR / "curated" / "Adam.html").read_text(encoding="utf-8")
    assert 'class="page-search"' in adam_html
    assert 'action="../browse.html"' in adam_html

