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
import hashlib
import json
import math
import re
import shutil
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlencode

import yaml
from jinja2 import Environment, FileSystemLoader, pass_context, select_autoescape
from markupsafe import Markup, escape

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = REPO_ROOT / "src" / "aimech" / "templates"
AIO_DIR = REPO_ROOT / "data" / "aio"
CURATED_DIR = REPO_ROOT / "data" / "curated"
PAGES_DIR = REPO_ROOT / "pages"
SCHEMA_DIR = REPO_ROOT / "src" / "aimech" / "schema"
HISTORY_DIR = REPO_ROOT / "history"
REVIEWS_DIR = REPO_ROOT / "reviews" / "structured"
CORPUS_MAP = REPO_ROOT / "data" / "embeddings" / "corpus_map.json"

GITHUB_REPO = "https://github.com/CultureBotAI/AIMech"
GITHUB_BLOB = GITHUB_REPO + "/blob/main/"
SITE_URL = "https://culturebotai.github.io/AIMech/pages/"
# GitHub Pages answers a missing address at any depth with the artifact root's
# 404.html, served at the address the reader asked for, so relative links in it
# would resolve against that missing path. .github/workflows/pages.yaml copies
# pages/404.html to the artifact root; its links are site-root-absolute.
NOT_FOUND_ROOT = "/AIMech/pages/"
# Written into the Pages artifact at deploy time by scripts/export_records.py
# (see .github/workflows/pages.yaml), never committed; the landing page links them.
DOWNLOAD_FILES = ("downloads/aimech-records.jsonl.gz", "downloads/manifest.json")

# The two record schemas, documented on schema.html. Anchors there are
# "<key>-class-<Name>" and "<key>-enum-<Name>".
SCHEMAS = (
    ("curated", SCHEMA_DIR / "curated_concept.yaml", "CuratedReviewStatus"),
    ("aio", SCHEMA_DIR / "aimech.yaml", "ReviewStatus"),
)

# How records are produced, quoted from README.md rather than paraphrased, so a
# page cannot claim more about curation or review than the repository does.
# tests/test_site_features.py checks that each sentence still appears there.
README_STATUS_NOTES = {
    "NOT_REVIEWED": (
        "Every generated record is `NOT_REVIEWED`. This is a deterministic import of "
        "terminology, not an independent scientific review."
    ),
    "DRAFT": "These maintained records remain `DRAFT`; scientific reviews are saved separately.",
}
README_GENERATED_AIO = "Generated per-concept records; do not hand-edit"
CLAUDE_CURATED_EDITS = "Curated changes require an append-only history sidecar using `just new-history`"
CLAUDE_AIO_CORRECTIONS = "Fix the importer or propose an upstream ontology correction"

# Readable labels for AIO relationship predicates. Each must be the opening
# phrase of its RelationshipPredicate description in aimech.yaml (tested).
PREDICATE_LABELS = {"BFO:0000051": "has part"}

KIND_LABELS = {
    "algorithm": "Algorithms",
    "model_family": "Model Families",
    "architecture": "Architectures",
    "mathematical_method": "Mathematical Methods",
    "layer": "Layers & Modules",
    "evaluation_criterion": "Evaluation Criteria",
    "evaluation_method": "Evaluation Methods",
    "learning_paradigm": "Learning Paradigms",
    "coordination_mechanism": "Coordination Mechanisms",
    "computational_paradigm": "Computational Paradigms",
    "preprocessing_method": "Preprocessing Methods",
    "task": "Tasks",
    "bias": "Biases",
    "risk": "Risks",
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
    "coordination_mechanism": "Source-defined computational designs that coordinate activity through specified information or state changes.",
    "computational_paradigm": "Source-defined approaches to organizing computational problem solving through shared design principles.",
    "preprocessing_method": "Feature engineering, data augmentation, and tokenization procedures.",
    "task": "Formalized problem settings, learning objectives, and benchmark task definitions.",
    "bias": "Systematic distortions in data collection, representation, evaluation, or model predictions.",
    "risk": "Failure modes, privacy vulnerabilities, and operational hazards in AI systems.",
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


# Bibliographic identifiers as the curated text and persistent_id values spell
# them: new-style and archive-style arXiv IDs, and DOIs. A DOI ends at
# whitespace, a quote, a backtick, a bracket or an angle bracket; no DOI in the
# corpus contains one, and stopping there keeps "`DOI:10.x/y`" from becoming a
# link to "10.x/y`" (the TraitMech autolinker's first defect, TraitMech #2022).
ARXIV_ID = r"(?:[0-9]{4}\.[0-9]{4,5}|[a-z][a-z-]*(?:\.[A-Z]{2})?/[0-9]{7})(?:v[0-9]+)?"
DOI_SUFFIX = r"10\.[0-9]{4,9}/[^\s<>\"'`\\\[\]]+"

PREFIX_URL = {
    "AIO": "https://w3id.org/aio/{local}",
    "BFO": "http://purl.obolibrary.org/obo/BFO_{local}",
    "owl": "http://www.w3.org/2002/07/owl#{local}",
}
# AIMech: is a local namespace whose HTTP resolution is not claimed
# (docs/curated-concepts.md), so an AIMech: CURIE links only to its record page.
LOCAL_PREFIX = "AIMech"
CURIE_SHAPE = re.compile(r"[A-Za-z][A-Za-z0-9_.-]*:[^\s<>\"'`\\]+")


def reference_url(value: object) -> str | None:
    """Resolve a bibliographic reference -- URL, DOI, arXiv ID or PMID -- or None.

    Prefixes are matched without regard to case, as persistent_id values write
    both ``doi:`` and ``DOI:``, ``arXiv:`` and ``arxiv:``. Anything else, such as
    a technical-report number or a repository@commit pin, is not a reference this
    site can resolve and stays text.
    """
    if not isinstance(value, str):
        return None
    ref = value.strip()
    if re.fullmatch(r"(?i:https?)://[^\s<>\"]+", ref):
        return ref
    prefix, sep, local = ref.partition(":")
    scheme = prefix.lower() if sep else ""
    local = local.strip()
    if scheme == "arxiv" and re.fullmatch(ARXIV_ID, local):
        return f"https://arxiv.org/abs/{local}"
    if scheme == "pmid" and re.fullmatch(r"[0-9]{1,9}", local):
        return f"https://pubmed.ncbi.nlm.nih.gov/{local}/"
    doi = local if scheme == "doi" else ref
    if re.fullmatch(DOI_SUFFIX, doi):
        return "https://doi.org/" + quote(doi, safe="/:;()._-")
    return None


def curie_url(curie: object) -> str | None:
    """Resolve a displayed CURIE to a public page about the term.

    References resolve as references; known prefixes use PREFIX_URL; any other
    well-formed CURIE falls back to bioregistry.io, which resolves or explains
    every registered prefix. The local AIMech: namespace never resolves here.
    """
    if not isinstance(curie, str):
        return None
    value = curie.strip()
    ref = reference_url(value)
    if ref:
        return ref
    if not CURIE_SHAPE.fullmatch(value):
        return None
    prefix, local = value.split(":", 1)
    template = PREFIX_URL.get(prefix)
    if template:
        return template.format(local=local)
    if prefix == LOCAL_PREFIX:
        return None
    return "https://bioregistry.io/" + quote(value, safe=":/")


def _own_id(context: Any) -> str | None:
    record = context.get("c")
    return record.get("id") if isinstance(record, dict) else None


# Reference tokens inside record prose. Matching runs on the raw string and every
# piece is escaped on the way out, so record text can never become markup. A URL
# matches first, so a DOI or arXiv ID inside it stays part of that URL. AIMech:
# and AIO: CURIEs link only when they name a record of this site.
AUTOLINK_TOKEN = re.compile(
    r"(?P<url>\b(?i:https?)://[^\s<>\"'`\\\]]+)"
    rf"|(?P<doi>(?:\b(?i:doi):\s?)?(?<![\w./]){DOI_SUFFIX})"
    rf"|(?P<arxiv>\b(?i:arxiv)(?::\s?|\s)?(?P<arxiv_id>{ARXIV_ID})(?!\w))"
    r"|(?P<pmid>\b(?i:pmid):?\s?(?P<pmid_number>[0-9]{1,9})\b)"
    r"|(?P<curie>\b(?:AIMech:[A-Za-z][A-Za-z0-9]*|AIO:[A-Za-z0-9]+)(?![\w-]))"
)
TOKEN_KINDS = ("url", "doi", "arxiv", "pmid", "curie")
CLOSING = {")": "(", "]": "[", "}": "{"}
# Sentence punctuation, plus the emphasis and code marks that close a token
# written as **10.x/y** or `10.x/y`.
TRAILING = ".,;:!?'\"*`"


def _trim_token(token: str) -> str:
    """Drop punctuation, emphasis and code marks, and unbalanced closers ending a token."""
    while token:
        last = token[-1]
        if last in TRAILING or (last in CLOSING and token.count(last) > token.count(CLOSING[last])):
            token = token[:-1]
            continue
        break
    return token


def _external_link(url: str, text: str) -> Markup:
    return Markup('<a href="{}" target="_blank" rel="noopener">{}</a>').format(url, text)


@pass_context
def autolink(context: Any, value: object) -> Markup:
    """Escape record prose and link the references and record CURIEs in it.

    URLs, DOIs, arXiv IDs and PMIDs open their resolvers; an AIMech: or AIO: CURIE
    naming another record of this site opens its page. Only the token becomes the
    anchor and its text is kept verbatim, so prose without a token renders exactly
    as plain escaping would. Applied to record content only: schema and
    documentation prose carries format examples that must stay text.
    """
    if value is None:
        return Markup("")
    text = str(value)
    pages = context.get("page_by_id") or {}
    own = _own_id(context)
    root = context.get("root") or ""
    out: list[str] = []
    position = 0
    for match in AUTOLINK_TOKEN.finditer(text):
        kind = next(name for name in TOKEN_KINDS if match.group(name) is not None)
        token = match.group(0)
        if kind in ("url", "doi"):
            token = _trim_token(token)
        if kind == "curie":
            if token == own:
                continue
            page = pages.get(token)
            if page:
                anchor = Markup('<a href="{}">{}</a>').format(root + page, token)
            else:
                url = curie_url(token) if token.startswith("AIO:") else None
                if not url:
                    continue
                anchor = _external_link(url, token)
        else:
            if kind == "url":
                url = reference_url(token)
            elif kind == "doi":
                url = reference_url("doi:" + token[token.index("10."):])
            elif kind == "arxiv":
                url = f"https://arxiv.org/abs/{match.group('arxiv_id')}"
            else:
                url = f"https://pubmed.ncbi.nlm.nih.gov/{match.group('pmid_number')}/"
            if not url:
                continue
            anchor = _external_link(url, token)
        out.append(escape(text[position:match.start()]))
        out.append(anchor)
        position = match.start() + len(token)
    out.append(escape(text[position:]))
    return Markup("").join(out)


def reference_link(value: object) -> Markup:
    """A persistent identifier, linked when it is a reference this site can resolve."""
    url = reference_url(value)
    if url:
        return _external_link(url, str(value).strip())
    return escape("" if value is None else str(value))


def link_label(url: object) -> str:
    """A short label for a GitHub issue or pull request URL; any other URL as written."""
    match = re.fullmatch(r"https://github\.com/([^/]+/[^/]+)/(issues|pull)/([0-9]+)/?", str(url))
    if not match:
        return str(url)
    kind = "issue" if match.group(2) == "issues" else "pull request"
    repo = "" if match.group(1) == "CultureBotAI/AIMech" else match.group(1) + " "
    return f"{repo}{kind} #{match.group(3)}"


def inline_code(value: object) -> Markup:
    """Escape a quoted repository sentence, rendering its `backtick` spans as code."""
    parts = str(value or "").split("`")
    return Markup("").join(
        Markup("<code>{}</code>").format(part) if index % 2 else escape(part)
        for index, part in enumerate(parts)
    )


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


def _load_mapping(path: Path) -> dict[str, Any]:
    """Parse a history sidecar or saved review, with libyaml when PyYAML has it.

    Used only for the ~2,200 files under history/ and reviews/structured/: the C
    loader returns the same documents as SafeLoader for them and keeps the render
    from spending a further minute in the pure-Python parser. A file that is not
    a mapping stops the render rather than silently dropping its events.
    """
    with path.open(encoding="utf-8") as handle:
        doc = yaml.load(handle, Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
    if not isinstance(doc, dict):
        raise ValueError(f"{path.relative_to(REPO_ROOT)}: expected a mapping")
    return doc


def _report_record_ids(path: Path) -> list[str]:
    """The record IDs a discovery report says it covers: selected_concept and entries[].

    A session naming a report that is missing or unreadable stops the render: its
    records would otherwise lose that history without any sign.
    """
    report = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(report, dict):
        raise ValueError(f"{path.relative_to(REPO_ROOT)}: expected a JSON object")
    found = []
    selected = report.get("selected_concept")
    if isinstance(selected, dict) and isinstance(selected.get("id"), str):
        found.append(selected["id"])
    for entry in report.get("entries") or []:
        if isinstance(entry, dict) and isinstance(entry.get("id"), str):
            found.append(entry["id"])
    return list(dict.fromkeys(found))


def load_curation_sessions(id_by_path: dict[str, str]) -> dict[str, list[dict[str, Any]]]:
    """Recorded curation sessions per record, from the append-only history/ sidecars.

    A record sidecar (history/records/) names the record's YAML as its target. A
    report sidecar (history/reports/) names the discovery report it wrote, and the
    report lists the records it covers in selected_concept or entries[]. Those two
    joins are the only ones made; a session is shown as recorded, with its own
    timestamp, which can differ from the record's curation timestamps.
    """
    known = set(id_by_path.values())
    report_ids: dict[str, list[str]] = {}
    sessions: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path in sorted(HISTORY_DIR.glob("*/*/*.yaml")):
        doc = _load_mapping(path)
        target = doc.get("target") or {}
        session = doc.get("session") or {}
        target_path = str(target.get("path") or "")
        report = None
        if target.get("kind") == "record":
            ids = [id_by_path[target_path]] if target_path in id_by_path else []
        elif target.get("kind") == "report" and target_path.endswith(".json"):
            if target_path not in report_ids:
                report_ids[target_path] = _report_record_ids(REPO_ROOT / target_path)
            ids = [i for i in report_ids[target_path] if i in known]
            report = target_path
        else:
            ids = []
        if not ids:
            continue
        links = doc.get("links") or {}
        view = {
            "id": str(session.get("id") or ""),
            "timestamp": str(session.get("timestamp") or ""),
            "actors": [
                {key: str(actor.get(key) or "") for key in ("name", "type", "model", "agent_tool")}
                for actor in session.get("actors") or []
                if isinstance(actor, dict)
            ],
            "events": [
                {key: event.get(key) for key in ("type", "outcome", "summary", "details")}
                for event in doc.get("events") or []
                if isinstance(event, dict)
            ],
            "links": [
                str(url) for key in ("issues", "prs", "urls") for url in links.get(key) or []
            ],
            "source_url": GITHUB_BLOB + path.relative_to(REPO_ROOT).as_posix(),
            "report_path": report,
            "report_url": GITHUB_BLOB + report if report else None,
        }
        for record_id in ids:
            sessions[record_id].append(view)
    for items in sessions.values():
        items.sort(key=lambda s: (s["timestamp"], s["id"]))
    return sessions


def load_saved_reviews(known_ids: set[str]) -> dict[str, list[dict[str, Any]]]:
    """Saved structured reviews per record, joined on each review's targets[].target_id."""
    reviews: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path in sorted(REVIEWS_DIR.glob("*/review.yaml")):
        doc = _load_mapping(path)
        targets = [
            t.get("target_id") for t in doc.get("targets") or []
            if isinstance(t, dict) and isinstance(t.get("target_id"), str)
        ]
        reviewer = doc.get("reviewer") or {}
        markdown = path.with_name("review.md")
        view = {
            "id": str(doc.get("review_id") or path.parent.name),
            "finished_at": str(doc.get("finished_at") or ""),
            "reviewer": str(reviewer.get("identity") or ""),
            "reviewer_kind": str(reviewer.get("kind") or ""),
            "model": str(reviewer.get("model") or ""),
            "independence": str(reviewer.get("independence") or ""),
            "verdict": str(doc.get("verdict") or ""),
            "completion": str(doc.get("completion") or ""),
            "summary": doc.get("summary") or "",
            "target_count": len(targets),
            "url": GITHUB_BLOB + path.relative_to(REPO_ROOT).as_posix(),
            "md_url": (GITHUB_BLOB + markdown.relative_to(REPO_ROOT).as_posix()
                       if markdown.is_file() else None),
        }
        for record_id in dict.fromkeys(targets):
            if record_id in known_ids:
                reviews[record_id].append(view)
    for items in reviews.values():
        items.sort(key=lambda r: (r["finished_at"], r["id"]))
    return reviews


def schema_reference(key: str, schema_path: Path) -> dict[str, Any]:
    """Readable documentation of one record schema, read from the schema itself.

    Every class with its induced slots (imports and slot_usage applied) and every
    enum with its permissible values, in the schema's own declaration order and
    with no clock, so an unchanged schema renders byte-identically under
    ``--check``. docs/ is not deployed, so this is the site's schema reference.
    """
    from linkml_runtime.utils.schemaview import SchemaView

    view = SchemaView(str(schema_path))
    view.imports_closure()
    module_file = {}
    for name, schema in view.schema_map.items():
        source = schema_path.parent / f"{name}.yaml"
        if source.exists():
            module_file[schema.id] = source.relative_to(REPO_ROOT).as_posix()
    classes = view.all_classes()
    enums = view.all_enums()
    local = list(view.all_classes(imports=False))
    ordered = local + [name for name in classes if name not in local]
    local_enums = list(view.all_enums(imports=False))
    ordered_enums = local_enums + [name for name in enums if name not in local_enums]

    def range_kind(name: str | None) -> str:
        if name in classes:
            return "class"
        if name in enums:
            return "enum"
        return "type"

    def slot_row(slot: Any) -> dict[str, Any]:
        names = [alt.range for alt in (slot.any_of or slot.exactly_one_of or []) if alt.range]
        ranges = names or [slot.range or view.schema.default_range or "string"]
        return {
            "name": slot.name,
            "ranges": [{"name": name, "kind": range_kind(name)} for name in ranges],
            "required": bool(slot.required or slot.identifier),
            "multivalued": bool(slot.multivalued),
            "identifier": bool(slot.identifier),
            "pattern": slot.pattern or "",
            "description": slot.description or "",
        }

    def source_of(element: Any) -> str:
        return module_file.get(element.from_schema, "")

    return {
        "key": key,
        "title": view.schema.title or view.schema.name,
        "description": view.schema.description or "",
        "license": view.schema.license or "",
        "source": schema_path.relative_to(REPO_ROOT).as_posix(),
        "modules": sorted(set(module_file.values())),
        "classes": [{
            "name": name,
            "description": classes[name].description or "",
            "is_a": classes[name].is_a or "",
            "tree_root": bool(classes[name].tree_root),
            "source": source_of(classes[name]),
            "slots": [slot_row(slot) for slot in view.class_induced_slots(name)],
        } for name in ordered],
        "enums": [{
            "name": name,
            "description": enums[name].description or "",
            "source": source_of(enums[name]),
            "permissible": [{"text": text, "description": value.description or ""}
                            for text, value in (enums[name].permissible_values or {}).items()],
        } for name in ordered_enums],
    }


def status_meanings(schemas: list[dict[str, Any]]) -> dict[str, dict[str, str]]:
    """Each review status with its definition as the governing schema states it."""
    meanings = {}
    for (key, _path, enum_name), schema in zip(SCHEMAS, schemas):
        enum = next(e for e in schema["enums"] if e["name"] == enum_name)
        for value in enum["permissible"]:
            meanings[value["text"]] = {
                "description": value["description"],
                "anchor": f"{key}-enum-{enum_name}",
                "schema_title": schema["title"],
                "readme": README_STATUS_NOTES.get(value["text"], ""),
            }
    return meanings


def map_coverage(points: list[list[Any]], records: list[dict[str, Any]]) -> dict[str, Any]:
    """How many of the listed records the text map plots, and why any are missing.

    The map is drawn from data/embeddings/corpus_map.json, which is regenerated
    separately from the records, so it can lag them. The reason given is derived
    from the records: when every missing record is a curated concept created
    after the newest plotted one, the map predates them.
    """
    by_id = {r["id"]: r for r in records}
    plotted = {p[3] for p in points if p[3] in by_id}
    missing = [r for r in records if r["id"] not in plotted]

    def created(record: dict[str, Any]) -> str:
        return str((record.get("curation") or {}).get("created_at") or "")

    newest = max((created(by_id[i]) for i in plotted if by_id[i]["origin"] == "curated"), default="")
    missing_curated = [r for r in missing if r["origin"] == "curated"]
    created_missing = sorted(created(r) for r in missing_curated if created(r))
    return {
        "total": len(records),
        "plotted": len(plotted),
        "missing": len(missing),
        "missing_curated": len(missing_curated),
        "missing_aio": len(missing) - len(missing_curated),
        "stale": sum(1 for p in points if p[3] not in by_id),
        "first_missing": created_missing[0][:10] if created_missing else "",
        "last_missing": created_missing[-1][:10] if created_missing else "",
        "newest_plotted": newest[:10],
        "predates_missing": bool(missing) and len(created_missing) == len(missing)
        and bool(newest) and created_missing[0] > newest,
    }


def curation_notice(curated: list[dict[str, Any]],
                    reviews: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    """Counts behind the landing page's statement of how curated records are produced."""
    distinct = {r["id"]: r for c in curated for r in reviews.get(c["id"], [])}
    return {
        "methods": sorted(Counter(str(c["curation"].get("method") or "") for c in curated).items()),
        "curators": Counter(str(c["curation"].get("curator") or "") for c in curated).most_common(),
        "review_count": len(distinct),
        "reviewer_kinds": sorted(Counter(r["reviewer_kind"] for r in distinct.values()).items()),
        "independence": sorted(Counter(r["independence"] for r in distinct.values()).items()),
    }


def feedback_urls(record_id: str, page: str, source_path: str) -> dict[str, str]:
    """A prefilled GitHub issue naming the record and its page, and the YAML edit route."""
    query = urlencode({"title": f"Problem with {record_id}", "body": SITE_URL + page},
                      quote_via=quote)
    return {
        "issue_url": f"{GITHUB_REPO}/issues/new?{query}",
        "edit_url": f"{GITHUB_REPO}/edit/main/{source_path}",
    }


def render(out_dir: Path) -> None:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["curie_url"] = curie_url
    env.filters["autolink"] = autolink
    env.filters["reference_link"] = reference_link
    env.filters["reference_url"] = reference_url
    env.filters["inline_code"] = inline_code
    env.filters["link_label"] = link_label

    aio_raw, curated_raw = load_all_records()

    aio_by_id = {doc["id"]: (p, doc) for p, doc in aio_raw}

    # Every record's page, so a CURIE naming one of them in record prose opens it
    # (autolink).
    page_by_id = {doc["id"]: f"curated/{p.stem}.html" for p, doc in curated_raw}
    page_by_id.update({doc["id"]: f"aio/{p.stem}.html" for p, doc in aio_raw})
    env.globals["page_by_id"] = page_by_id
    env.globals["github_blob"] = GITHUB_BLOB
    env.globals["readme_generated_aio"] = README_GENERATED_AIO
    env.globals["claude_curated_edits"] = CLAUDE_CURATED_EDITS
    env.globals["claude_aio_corrections"] = CLAUDE_AIO_CORRECTIONS
    id_by_path = {
        p.relative_to(REPO_ROOT).as_posix(): doc["id"] for p, doc in curated_raw + aio_raw
    }
    sessions_by_id = load_curation_sessions(id_by_path)
    reviews_by_id = load_saved_reviews(set(page_by_id))
    schemas = [schema_reference(key, path) for key, path, _enum in SCHEMAS]
    env.globals["status_meanings"] = status_meanings(schemas)
    predicate_meanings = {
        value["text"]: value["description"]
        for enum in schemas[1]["enums"] if enum["name"] == "RelationshipPredicate"
        for value in enum["permissible"]
    }

    map_data = json.loads(CORPUS_MAP.read_text(encoding="utf-8")) if CORPUS_MAP.exists() else None
    map_ids = {p[3] for p in map_data["points"]} if map_data else set()
    env.globals["has_map"] = map_data is not None

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

        # The definition's own citations, with source titles like claim evidence
        definition_evidence = [
            dict(ev, source_title=sources_map.get(ev.get("source_id"), ev.get("source_id")))
            for ev in doc.get("definition_evidence") or []
        ]

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
                    target_path, target_doc = aio_by_id[target]
                    ex_copy["aio_page"] = f"aio/{target_path.stem}.html"
                    ex_copy["target_name"] = target_doc.get("name", target)
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
            "definition_evidence": definition_evidence,
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
            "sessions": sessions_by_id.get(doc["id"], []),
            "reviews": reviews_by_id.get(doc["id"], []),
            "on_map": doc["id"] in map_ids,
            **feedback_urls(doc["id"], f"curated/{slug}.html", p.relative_to(REPO_ROOT).as_posix()),
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
            else:
                # owl:Thing and any AIO class outside the snapshot open their resolver
                p_info["url"] = curie_url(parent_id)
            parent_links.append(p_info)

        # Relationship links
        rel_links = []
        for rel in relationships:
            r_target = rel.get("target", "")
            r_pred = rel.get("predicate", "")
            r_info = {
                "predicate": r_pred,
                "predicate_label": PREDICATE_LABELS.get(r_pred, ""),
                "predicate_url": curie_url(r_pred),
                "predicate_meaning": predicate_meanings.get(r_pred, ""),
                "target": r_target,
            }
            if r_target in aio_by_id:
                r_path, r_doc = aio_by_id[r_target]
                r_info["page"] = f"aio/{r_path.stem}.html"
                r_info["name"] = r_doc.get("name", r_target)
            else:
                r_info["url"] = curie_url(r_target)
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
            "sessions": sessions_by_id.get(doc["id"], []),
            "reviews": reviews_by_id.get(doc["id"], []),
            "on_map": doc["id"] in map_ids,
            **feedback_urls(doc["id"], f"aio/{slug}.html", p.relative_to(REPO_ROOT).as_posix()),
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

    # Deterministic corpus build provenance
    curation_dates: list[str] = []
    digest_hasher = hashlib.sha256()
    for r in sorted(all_records, key=lambda x: x["id"]):
        digest_hasher.update(
            f"{r['id']}|{r['name']}|{r['origin']}|{r['claims_count']}|{r['sources_count']}\n".encode("utf-8")
        )
        if r["origin"] == "curated":
            cur = r.get("curation") or {}
            for k in ("updated_at", "created_at"):
                val = str(cur.get(k) or "").strip()
                if val:
                    curation_dates.append(val[:10])
        else:
            prov = r.get("provenance") or {}
            val = str(prov.get("imported_at") or "").strip()
            if val:
                curation_dates.append(val[:10])

    build_provenance = {
        "total_concepts": total_concepts,
        "curated_count": curated_count,
        "aio_count": aio_count,
        "total_claims": total_claims,
        "total_sources": total_sources,
        "latest_curation": max(curation_dates) if curation_dates else "2026-04",
        "corpus_digest": digest_hasher.hexdigest()[:12],
    }
    env.globals["build_provenance"] = build_provenance

    # Build Ontology & Grounding Network Graph data
    graph_nodes: list[dict[str, Any]] = []
    graph_edges: list[dict[str, Any]] = []
    node_idx_by_id: dict[str, int] = {}

    def _add_node(node: dict[str, Any]) -> int:
        nid = node["id"]
        if nid in node_idx_by_id:
            return node_idx_by_id[nid]
        idx = len(graph_nodes)
        node_idx_by_id[nid] = idx
        graph_nodes.append(node)
        return idx

    # Ring 1: Hub nodes for 8 AIO branches + 11 Curated concept kinds
    hub_entries: list[tuple[str, str, str, str, int]] = []
    for b in branches_meta:
        hub_entries.append((f"branch:{b['id']}", b["label"], "branch", b["page"], b["count"]))
    for k in kinds_meta:
        hub_entries.append((f"kind:{k['id']}", k["label"], "kind", k["page"], k["count"]))

    hub_angles: dict[str, float] = {}
    n_hubs = max(1, len(hub_entries))
    for i, (hid, hlabel, htype, hpage, hcount) in enumerate(hub_entries):
        angle = 2.0 * math.pi * i / n_hubs
        hub_angles[hid] = angle
        _add_node({
            "id": hid,
            "name": hlabel,
            "type": htype,
            "origin": "aio" if htype == "branch" else "curated",
            "group": hid.split(":", 1)[1],
            "href": hpage,
            "count": hcount,
            "x": round(0.5 + 0.17 * math.cos(angle), 4),
            "y": round(0.5 + 0.17 * math.sin(angle), 4),
        })

    # Ring 2: AIO classes (grouped around their primary branch hub)
    aio_sorted = sorted(aio_items, key=lambda x: x["id"])
    for idx_a, a in enumerate(aio_sorted):
        primary_branch = a["branches"][0] if a["branches"] else "Model"
        base_angle = hub_angles.get(f"branch:{primary_branch}", 0.0)
        jitter = ((idx_a % 37) - 18) * 0.014
        ring_r = 0.30 if a["mapped_curated"] else (0.34 + (idx_a % 5) * 0.018)
        angle = base_angle + jitter
        _add_node({
            "id": a["id"],
            "name": a["name"],
            "type": "aio",
            "origin": "aio",
            "group": primary_branch,
            "href": a["page"],
            "count": len(a["mapped_curated"]) + len(a["parents"]) + len(a["relationships"]),
            "x": round(min(0.95, max(0.05, 0.5 + ring_r * math.cos(angle))), 4),
            "y": round(min(0.95, max(0.05, 0.5 + ring_r * math.sin(angle))), 4),
        })

    # Ring 3: Curated AI concepts (grouped around their concept_kind hub)
    curated_sorted = sorted(curated_items, key=lambda x: x["id"])
    for idx_c, c in enumerate(curated_sorted):
        k_id = c["kind_id"]
        base_angle = hub_angles.get(f"kind:{k_id}", 0.0)
        jitter = ((idx_c % 41) - 20) * 0.013
        ring_r = 0.42 + (idx_c % 4) * 0.014
        angle = base_angle + jitter
        _add_node({
            "id": c["id"],
            "name": c["name"],
            "type": "curated",
            "origin": "curated",
            "group": k_id,
            "href": c["page"],
            "count": c["claims_count"],
            "x": round(min(0.95, max(0.05, 0.5 + ring_r * math.cos(angle))), 4),
            "y": round(min(0.95, max(0.05, 0.5 + ring_r * math.sin(angle))), 4),
        })

    # Edges: curated -> kind hub, curated -> mapped AIO class
    for c in curated_sorted:
        src_idx = node_idx_by_id[c["id"]]
        kind_hid = f"kind:{c['kind_id']}"
        if kind_hid in node_idx_by_id:
            graph_edges.append({
                "source": src_idx,
                "target": node_idx_by_id[kind_hid],
                "type": "kind",
                "label": "has_kind",
            })
        for m in c["aio_mappings"]:
            t_id = m.get("target", "")
            if t_id in node_idx_by_id:
                graph_edges.append({
                    "source": src_idx,
                    "target": node_idx_by_id[t_id],
                    "type": "mapping",
                    "label": m.get("relation", "maps_to"),
                })

    # Edges: AIO class -> parent AIO class, axiomatic relationships, and primary branch hub
    for a in aio_sorted:
        src_idx = node_idx_by_id[a["id"]]
        if a["branches"]:
            b_hid = f"branch:{a['branches'][0]}"
            if b_hid in node_idx_by_id:
                graph_edges.append({
                    "source": src_idx,
                    "target": node_idx_by_id[b_hid],
                    "type": "branch",
                    "label": "in_branch",
                })
        for p_id in a["parents"]:
            if p_id in node_idx_by_id:
                graph_edges.append({
                    "source": src_idx,
                    "target": node_idx_by_id[p_id],
                    "type": "parent",
                    "label": "subClassOf",
                })
        for rel in a["relationships"]:
            rt_id = rel.get("target", "")
            if rt_id in node_idx_by_id:
                graph_edges.append({
                    "source": src_idx,
                    "target": node_idx_by_id[rt_id],
                    "type": "relationship",
                    "label": rel.get("predicate", "related_to"),
                })

    graph_data = {
        "n_nodes": len(graph_nodes),
        "n_edges": len(graph_edges),
        "nodes": graph_nodes,
        "edges": graph_edges,
    }

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
        notice=curation_notice(curated_items, reviews_by_id),
        downloads=DOWNLOAD_FILES,
    )
    (out_dir / "index.html").write_text(index_html, encoding="utf-8")

    # Render schema.html: readable documentation generated from the LinkML schemas
    schema_html = env.get_template("schema.html").render(
        root="",
        schemas=schemas,
        governs={"curated": (curated_count, "data/curated"), "aio": (aio_count, "data/aio")},
    )
    (out_dir / "schema.html").write_text(schema_html, encoding="utf-8")

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

    # Render 404.html. The Pages workflow also serves it from the artifact root for
    # every missing address, so its links are site-root-absolute (NOT_FOUND_ROOT).
    page_404_html = env.get_template("404.html").render(root=NOT_FOUND_ROOT)
    (out_dir / "404.html").write_text(page_404_html, encoding="utf-8")

    # Render map.html and copy corpus_map.json if corpus_map.json exists
    if map_data is not None:
        shutil.copy(CORPUS_MAP, out_dir / "corpus_map.json")
        map_data["hrefs"] = {r["id"]: r["page"] for r in all_records}
        map_html = env.get_template("map.html").render(
            root="",
            map_data=map_data,
            coverage=map_coverage(map_data["points"], all_records),
            map_data_json=json.dumps(map_data, separators=(",", ":")).replace("</", "<\\/"),
        )
        (out_dir / "map.html").write_text(map_html, encoding="utf-8")

    # Render graph.html
    if (TEMPLATES_DIR / "graph.html").exists():
        graph_html = env.get_template("graph.html").render(
            root="",
            graph_data=graph_data,
            graph_data_json=json.dumps(graph_data, separators=(",", ":")).replace("</", "<\\/"),
            kinds_meta=kinds_meta,
            branches_meta=branches_meta,
        )
        (out_dir / "graph.html").write_text(graph_html, encoding="utf-8")

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
