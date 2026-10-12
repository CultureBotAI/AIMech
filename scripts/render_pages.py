#!/usr/bin/env python3
"""Render the browsable GitHub Pages site under pages/ from data/aio/ and data/curated/.

Usage:
    python scripts/render_pages.py
    python scripts/render_pages.py --check
    python scripts/render_pages.py --out /tmp/site
"""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = REPO_ROOT / "src" / "aimech" / "templates"
AIO_DIR = REPO_ROOT / "data" / "aio"
CURATED_DIR = REPO_ROOT / "data" / "curated"
PAGES_DIR = REPO_ROOT / "pages"

KIND_LABELS = {
    "algorithm": "Algorithms",
    "model_family": "Model Families",
    "architecture": "Architectures",
    "mathematical_method": "Mathematical Methods",
    "layer": "Layers & Modules",
    "evaluation_criterion": "Evaluation Criteria",
    "evaluation_method": "Evaluation Methods",
    "learning_paradigm": "Learning Paradigms",
    "preprocessing_method": "Preprocessing Methods",
}

KIND_BLURBS = {
    "algorithm": "Defined computational procedures, solvers, optimizers, and search techniques.",
    "model_family": "Pinned classes and model lineages sharing core design characteristics.",
    "architecture": "Structural blueprints and macro-designs for deep learning models.",
    "mathematical_method": "Formal mathematical formulations, kernels, transforms, and sampling algorithms.",
    "layer": "Defined neural network components that transform representations between stages.",
    "evaluation_criterion": "Defined conditions and loss metrics used to assess model behavior or predictions.",
    "evaluation_method": "Empirical protocols and test methodologies for measuring AI system performance.",
    "learning_paradigm": "High-level training frameworks such as contrastive or self-supervised learning.",
    "preprocessing_method": "Feature engineering, data augmentation, and tokenization procedures.",
}

BRANCH_LABELS = {
    "Layer": "Layers",
    "Model": "Models",
    "Bias": "Biases",
    "MachineLearningTask": "ML Tasks",
    "Network": "Networks",
    "MathematicalFunction": "Mathematical Functions",
    "Preprocessing": "Preprocessing",
    "TrainingStrategy": "Training Strategies",
}

BRANCH_BLURBS = {
    "Layer": "Neural network layer definitions and functional primitives.",
    "Model": "Concrete model architectures and family designations cataloged in AIO.",
    "Bias": "Inductive biases, algorithmic biases, and representational priors.",
    "MachineLearningTask": "Problem formulations and learning task classifications.",
    "Network": "Network topologies, graphs, and connection frameworks.",
    "MathematicalFunction": "Activation functions, loss formulations, and mathematical operators.",
    "Preprocessing": "Input transformations and representation preparation steps.",
    "TrainingStrategy": "Training regimens, scheduling, and optimization strategies.",
}

FEATURED_CURATED_SLUGS = [
    "Adam",
    "KernelPCA",
    "FastICA",
    "SetTransformer",
    "GraphAttentionNetwork",
    "DiffusionMaps",
    "AdaBoost",
    "ProbabilisticPCA",
    "MarkovRandomField",
    "ResidualAttentionNetwork",
    "HiddenMarkovModel",
    "OjaLearningRule",
]


def curie_url(curie: str) -> str | None:
    if not isinstance(curie, str):
        return None
    if curie.startswith("http://") or curie.startswith("https://"):
        return curie
    if curie.startswith("arXiv:"):
        arxiv_id = curie.split(":", 1)[1]
        return f"https://arxiv.org/abs/{arxiv_id}"
    if curie.startswith("DOI:"):
        doi = curie.split(":", 1)[1]
        return f"https://doi.org/{doi}"
    if curie.startswith("PMID:"):
        pmid = curie.split(":", 1)[1]
        return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    if curie.startswith("AIO:"):
        local = curie.split(":", 1)[1]
        return f"https://w3id.org/aio/{local}"
    return None


def truncate_preview(text: str, max_chars: int = 140) -> str:
    cleaned = " ".join(text.split())
    if len(cleaned) <= max_chars:
        return cleaned
    return cleaned[:max_chars].rstrip() + "…"


def load_all_records() -> tuple[list[tuple[Path, dict[str, Any]]], list[tuple[Path, dict[str, Any]]]]:
    aio_records = []
    for path in sorted(AIO_DIR.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and doc.get("id"):
            aio_records.append((path, doc))

    curated_records = []
    for path in sorted(CURATED_DIR.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and doc.get("id"):
            curated_records.append((path, doc))

    return aio_records, curated_records


def render(out_dir: Path) -> None:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["curie_url"] = curie_url

    aio_raw, curated_raw = load_all_records()

    aio_by_id = {doc["id"]: (p, doc) for p, doc in aio_raw}

    # Map AIO ID -> list of curated concepts that map to it
    aio_to_curated = defaultdict(list)
    for p, c_doc in curated_raw:
        c_slug = p.stem
        c_kind = c_doc.get("concept_kind", "")
        kind_label = KIND_LABELS.get(c_kind, c_kind.replace("_", " ").title())
        for m in c_doc.get("aio_mappings") or []:
            target_id = m.get("target")
            if target_id:
                aio_to_curated[target_id].append({
                    "id": c_doc["id"],
                    "name": c_doc.get("name", c_slug),
                    "slug": c_slug,
                    "kind_id": c_kind,
                    "kind_label": kind_label,
                    "relation": m.get("relation", ""),
                    "rationale": m.get("rationale", ""),
                    "page": f"curated/{c_slug}.html",
                })

    # Prepare curated records
    curated_items = []
    for p, doc in curated_raw:
        slug = p.stem
        name = doc.get("name", slug)
        kind_id = doc.get("concept_kind", "other")
        kind_label = KIND_LABELS.get(kind_id, kind_id.replace("_", " ").title())
        definition = doc.get("definition", "").strip()
        identity_notes = doc.get("identity_notes", "").strip()
        aliases = doc.get("aliases") or []
        claims = doc.get("claims") or []
        sources = doc.get("evidence_sources") or []
        limitations = doc.get("limitations") or []

        # Sources map
        sources_map = {s.get("source_id"): s.get("title") for s in sources if s.get("source_id")}

        # Enriched claims with source titles
        enriched_claims = []
        for cl in claims:
            cl_copy = dict(cl)
            enriched_ev = []
            for ev in cl.get("evidence") or []:
                ev_copy = dict(ev)
                ev_copy["source_title"] = sources_map.get(ev.get("source_id"), ev.get("source_id"))
                enriched_ev.append(ev_copy)
            cl_copy["evidence"] = enriched_ev
            enriched_claims.append(cl_copy)

        # Enriched AIO mappings with local page links if target exists
        enriched_mappings = []
        for m in doc.get("aio_mappings") or []:
            m_copy = dict(m)
            target = m.get("target", "")
            if target in aio_by_id:
                target_path, target_doc = aio_by_id[target]
                m_copy["aio_page"] = f"aio/{target_path.stem}.html"
                m_copy["target_name"] = target_doc.get("name", target)
            enriched_mappings.append(m_copy)

        # Enriched AIO no-match examined targets
        aio_no_match = doc.get("aio_no_match")
        enriched_no_match = None
        if isinstance(aio_no_match, dict):
            enriched_no_match = dict(aio_no_match)
            ex_targets = []
            for ex in aio_no_match.get("examined_targets") or []:
                ex_copy = dict(ex)
                target = ex.get("target", "")
                if target in aio_by_id:
                    target_path, _ = aio_by_id[target]
                    ex_copy["aio_page"] = f"aio/{target_path.stem}.html"
                ex_targets.append(ex_copy)
            enriched_no_match["examined_targets"] = ex_targets

        search_tokens = [
            name,
            slug,
            doc["id"],
            kind_label,
            kind_id,
            definition,
            identity_notes,
            " ".join(aliases),
            " ".join(cl.get("statement", "") for cl in claims),
            " ".join(s.get("title", "") for s in sources),
            " ".join(" ".join(s.get("authors") or []) for s in sources),
        ]
        search_text = " ".join(filter(None, search_tokens)).lower()

        curated_items.append({
            "path": p,
            "slug": slug,
            "id": doc["id"],
            "name": name,
            "origin": "curated",
            "kind_id": kind_id,
            "concept_kind": kind_id,
            "kind_label": kind_label,
            "branches": [],
            "branches_str": "",
            "definition": definition,
            "definition_preview": truncate_preview(definition),
            "identity_notes": identity_notes,
            "aliases": aliases,
            "claims": enriched_claims,
            "claims_count": len(claims),
            "evidence_sources": sources,
            "sources_count": len(sources),
            "limitations": limitations,
            "aio_mappings": enriched_mappings,
            "aio_no_match": enriched_no_match,
            "review_status": doc.get("review_status", "DRAFT"),
            "curation": doc.get("curation") or {},
            "page": f"curated/{slug}.html",
            "search_text": search_text,
            "source_path": str(p.relative_to(REPO_ROOT)),
            "raw_doc": doc,
        })

    # Prepare AIO records
    aio_items = []
    for p, doc in aio_raw:
        slug = p.stem
        name = doc.get("name", slug)
        branches = doc.get("branches") or []
        definition = doc.get("definition", "").strip()
        parents = doc.get("parents") or []
        relationships = doc.get("relationships") or []
        synonyms = doc.get("synonyms") or []
        definition_sources = doc.get("definition_sources") or []
        subsets = doc.get("subsets") or []

        # Parent links
        parent_links = []
        for parent_id in parents:
            p_info = {"id": parent_id}
            if parent_id in aio_by_id:
                p_path, p_doc = aio_by_id[parent_id]
                p_info["page"] = f"aio/{p_path.stem}.html"
                p_info["name"] = p_doc.get("name", parent_id)
            elif parent_id.startswith("AIO:"):
                p_info["url"] = f"https://w3id.org/aio/{parent_id.split(':', 1)[1]}"
            parent_links.append(p_info)

        # Relationship links
        rel_links = []
        for rel in relationships:
            r_target = rel.get("target", "")
            r_pred = rel.get("predicate", "")
            r_info = {"predicate": r_pred, "target": r_target}
            if r_target in aio_by_id:
                r_path, r_doc = aio_by_id[r_target]
                r_info["page"] = f"aio/{r_path.stem}.html"
                r_info["name"] = r_doc.get("name", r_target)
            rel_links.append(r_info)

        # Curated concepts that map to this AIO class
        mapped_curated = aio_to_curated.get(doc["id"], [])

        search_tokens = [
            name,
            slug,
            doc["id"],
            definition,
            " ".join(branches),
            " ".join(parents),
            " ".join(s.get("value", "") for s in synonyms),
            " ".join(definition_sources),
        ]
        search_text = " ".join(filter(None, search_tokens)).lower()

        aio_items.append({
            "path": p,
            "slug": slug,
            "id": doc["id"],
            "name": name,
            "origin": "aio",
            "kind_id": "",
            "kind_label": "",
            "branches": branches,
            "branches_str": " ".join(branches),
            "definition": definition,
            "definition_preview": truncate_preview(definition),
            "ontology_iri": doc.get("ontology_iri", f"https://w3id.org/aio/{slug}"),
            "parents": parents,
            "parent_links": parent_links,
            "relationships": relationships,
            "rel_links": rel_links,
            "synonyms": synonyms,
            "aliases": [s.get("value") for s in synonyms if s.get("value")],
            "definition_sources": definition_sources,
            "subsets": subsets,
            "provenance": doc.get("provenance") or {},
            "review_status": doc.get("review_status", "NOT_REVIEWED"),
            "mapped_curated": mapped_curated,
            "claims_count": 0,
            "sources_count": len(definition_sources),
            "page": f"aio/{slug}.html",
            "search_text": search_text,
            "source_path": str(p.relative_to(REPO_ROOT)),
            "raw_doc": doc,
        })

    # Combined records for catalogue and browsing
    all_records = sorted(curated_items + aio_items, key=lambda x: x["name"].lower())

    # Grouping
    by_kind = defaultdict(list)
    for c in curated_items:
        by_kind[c["kind_id"]].append(c)

    by_branch = defaultdict(list)
    for a in aio_items:
        for b in a["branches"]:
            by_branch[b].append(a)

    kinds_meta = [
        {
            "id": k,
            "label": KIND_LABELS.get(k, k.replace("_", " ").title()),
            "count": len(by_kind[k]),
            "blurb": KIND_BLURBS.get(k, ""),
            "page": f"kinds/{k}.html",
        }
        for k in sorted(by_kind.keys(), key=lambda x: len(by_kind[x]), reverse=True)
    ]

    branches_meta = [
        {
            "id": b,
            "label": BRANCH_LABELS.get(b, b),
            "count": len(by_branch[b]),
            "blurb": BRANCH_BLURBS.get(b, ""),
            "page": f"branches/{b}.html",
        }
        for b in sorted(by_branch.keys(), key=lambda x: len(by_branch[x]), reverse=True)
    ]

    # Featured concepts
    curated_by_slug = {c["slug"]: c for c in curated_items}
    featured = [curated_by_slug[s] for s in FEATURED_CURATED_SLUGS if s in curated_by_slug]

    total_concepts = len(all_records)
    curated_count = len(curated_items)
    aio_count = len(aio_items)
    total_claims = sum(c["claims_count"] for c in curated_items)
    total_sources = sum(c["sources_count"] for c in curated_items)

    # Directories
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "curated").mkdir(parents=True, exist_ok=True)
    (out_dir / "aio").mkdir(parents=True, exist_ok=True)
    (out_dir / "kinds").mkdir(parents=True, exist_ok=True)
    (out_dir / "branches").mkdir(parents=True, exist_ok=True)

    # Static assets
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")
    shutil.copy(TEMPLATES_DIR / "style.css", out_dir / "style.css")
    shutil.copy(TEMPLATES_DIR / "theme-toggle.js", out_dir / "theme-toggle.js")
    shutil.copy(TEMPLATES_DIR / "record-browser.js", out_dir / "record-browser.js")

    # Render index.html
    index_html = env.get_template("index.html").render(
        root="",
        total_concepts=total_concepts,
        curated_count=curated_count,
        aio_count=aio_count,
        total_claims=total_claims,
        total_sources=total_sources,
        kinds_meta=kinds_meta,
        branches_meta=branches_meta,
        featured=featured,
    )
    (out_dir / "index.html").write_text(index_html, encoding="utf-8")

    # Render browse.html
    browse_html = env.get_template("browse.html").render(
        root="",
        records=all_records,
        total_concepts=total_concepts,
        curated_count=curated_count,
        aio_count=aio_count,
        kinds_meta=kinds_meta,
        branches_meta=branches_meta,
    )
    (out_dir / "browse.html").write_text(browse_html, encoding="utf-8")

    # Render 404.html
    page_404_html = env.get_template("404.html").render(root="")
    (out_dir / "404.html").write_text(page_404_html, encoding="utf-8")

    # Write index.json
    index_json_data = [
        {
            "id": r["id"],
            "slug": r["slug"],
            "name": r["name"],
            "origin": r["origin"],
            "kind": r["kind_id"],
            "branches": r["branches"],
            "page": r["page"],
            "claims_count": r["claims_count"],
            "sources_count": r["sources_count"],
        }
        for r in all_records
    ]
    (out_dir / "index.json").write_text(
        json.dumps(index_json_data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    # Render curated/*.html
    for c in curated_items:
        c_html = env.get_template("curated_concept.html").render(
            root="../",
            c=c,
            kind_label=c["kind_label"],
            source_path=c["source_path"],
        )
        (out_dir / "curated" / f"{c['slug']}.html").write_text(c_html, encoding="utf-8")

    # Render aio/*.html
    for a in aio_items:
        a_html = env.get_template("aio_concept.html").render(
            root="../",
            c=a,
            source_path=a["source_path"],
        )
        (out_dir / "aio" / f"{a['slug']}.html").write_text(a_html, encoding="utf-8")

    # Render kinds/*.html
    for k_meta in kinds_meta:
        k_id = k_meta["id"]
        k_records = sorted(by_kind[k_id], key=lambda x: x["name"].lower())
        k_html = env.get_template("kind.html").render(
            root="../",
            kind=k_meta,
            records=k_records,
            kinds_meta=kinds_meta,
        )
        (out_dir / "kinds" / f"{k_id}.html").write_text(k_html, encoding="utf-8")

    # Render branches/*.html
    for b_meta in branches_meta:
        b_id = b_meta["id"]
        b_records = sorted(by_branch[b_id], key=lambda x: x["name"].lower())
        b_html = env.get_template("branch.html").render(
            root="../",
            branch=b_meta,
            records=b_records,
            branches_meta=branches_meta,
        )
        (out_dir / "branches" / f"{b_id}.html").write_text(b_html, encoding="utf-8")

    # Root redirect index.html
    if out_dir.resolve() == PAGES_DIR.resolve():
        root_index = (
            '<!DOCTYPE html>\n'
            '<html lang="en">\n'
            '<head>\n'
            '<meta charset="utf-8">\n'
            '<meta http-equiv="refresh" content="0; url=pages/index.html">\n'
            '<link rel="canonical" href="pages/index.html">\n'
            '<title>Redirecting to AIMech...</title>\n'
            '</head>\n'
            '<body>\n'
            '<p>Redirecting to <a href="pages/index.html">AIMech</a>...</p>\n'
            '</body>\n'
            '</html>\n'
        )
        (REPO_ROOT / "index.html").write_text(root_index, encoding="utf-8")


def _tree_differs(a: Path, b: Path) -> list[str]:
    diffs: list[str] = []

    def walk(cmp: filecmp.dircmp, prefix: str) -> None:
        diffs.extend(f"{prefix}{n}" for n in cmp.left_only + cmp.right_only + cmp.diff_files)
        for name, sub in cmp.subdirs.items():
            walk(sub, f"{prefix}{name}/")

    walk(filecmp.dircmp(a, b), "")
    return diffs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=PAGES_DIR)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Render to a temp dir and diff against --out.",
    )
    args = parser.parse_args(argv)

    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            render(Path(tmp))
            if not args.out.exists():
                print(f"{args.out} does not exist; run `just render`", file=sys.stderr)
                return 1
            diffs = _tree_differs(Path(tmp), args.out)
        if diffs:
            print(
                f"pages/ is stale ({len(diffs)} file(s) differ), e.g. {diffs[:5]}; run `just render`",
                file=sys.stderr,
            )
            return 1
        print("pages/ is current")
        return 0

    if args.out.exists():
        shutil.rmtree(args.out)
    render(args.out)
    print(f"Rendered AIMech site under {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
