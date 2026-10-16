#!/usr/bin/env python3
"""Embed every AIMech record (curated concepts + AIO classes) into a dense text vector.

Writes under ``data/embeddings/`` (vectors and raw metadata are gitignored;
``corpus_map.json`` produced by ``scripts/embed_map.py`` is committed):
  vectors.npy     float32 (N, D), L2-normalized so dot product == cosine
  ids.json        [identifier, ...] in row order
  meta.json       model name, corpus_fingerprint, and per-row metadata

Runs on a Python environment with ``sentence-transformers`` and ``torch``
installed (e.g. ``/Users/marcin/miniforge3/bin/python3 scripts/embed_records.py``).
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CURATED_DIR = REPO_ROOT / "data" / "curated"
AIO_DIR = REPO_ROOT / "data" / "aio"
OUT_DIR = REPO_ROOT / "data" / "embeddings"

MODEL_NAME = "BAAI/bge-large-en-v1.5"

EXCLUDED = (
    "curation",
    "provenance",
    "aio_snapshot",
    "definition_evidence",
    "evidence_sources",
    "history",
    "review_status",
    "ontology_iri",
    "subsets",
)


def _clean(text: str) -> str:
    return " ".join(str(text).split())


def build_document(record: dict, aio_names: dict[str, str] | None = None) -> str:
    """Assemble the embeddable text for one curated or AIO record."""
    aio_names = aio_names or {}
    rec_id = str(record.get("id") or "")
    name = _clean(record.get("name") or rec_id)
    is_curated = rec_id.startswith("AIMech:") or "concept_kind" in record

    parts: list[str] = []
    if is_curated:
        kind = _clean(record.get("concept_kind") or "concept").replace("_", " ")
        aliases = [_clean(a) for a in (record.get("aliases") or []) if a]
        head = f"{name} — curated AI and machine learning {kind}"
        if aliases:
            head += f" (also known as {', '.join(aliases[:8])})"
        parts.append(head + ".")

        if record.get("definition"):
            parts.append(_clean(record["definition"]))
        if record.get("identity_notes"):
            parts.append("Identity and scope: " + _clean(record["identity_notes"]))

        mappings = record.get("aio_mappings") or []
        if mappings:
            map_strs = []
            for m in mappings[:6]:
                if isinstance(m, dict) and m.get("target"):
                    target = str(m["target"])
                    label = aio_names.get(target, target.removeprefix("AIO:"))
                    rel = str(m.get("relation") or "mapped").replace("_", " ")
                    map_strs.append(f"{label} ({rel})")
            if map_strs:
                parts.append("Ontology grounding: " + "; ".join(map_strs) + ".")

        claims = record.get("claims") or []
        claim_texts = [
            _clean(c["statement"])
            for c in claims[:5]
            if isinstance(c, dict) and c.get("statement")
        ]
        if claim_texts:
            parts.append("Mechanistic and empirical claims: " + " ".join(claim_texts))

        limitations = record.get("limitations") or []
        lim_texts = [_clean(lim) for lim in limitations[:4] if isinstance(lim, str) and lim.strip()]
        if lim_texts:
            parts.append("Limitations: " + " ".join(lim_texts))
    else:
        branches = [_clean(b) for b in (record.get("branches") or []) if b]
        branch_str = ", ".join(branches) if branches else "AI ontology"
        synonyms = [
            _clean(s["value"])
            for s in (record.get("synonyms") or [])
            if isinstance(s, dict) and s.get("value")
        ]
        head = f"{name} — Artificial Intelligence Ontology class in {branch_str}"
        if synonyms:
            head += f" (synonyms: {', '.join(synonyms[:8])})"
        parts.append(head + ".")

        if record.get("definition"):
            parts.append(_clean(record["definition"]))

        parents = [
            aio_names.get(str(p), str(p).removeprefix("AIO:"))
            for p in (record.get("parents") or [])
            if p and str(p) != "owl:Thing"
        ]
        if parents:
            parts.append("Subclass of: " + ", ".join(parents[:6]) + ".")

    parts.append(f"identifier: {rec_id}.")
    return " ".join(parts)


def record_class(record: dict) -> str:
    """Return the primary display category used for coloring on the corpus map."""
    rec_id = str(record.get("id") or "")
    if rec_id.startswith("AIMech:") or "concept_kind" in record:
        kind = str(record.get("concept_kind") or "other").strip()
        return f"curated:{kind}"
    branches = record.get("branches") or []
    branch = str(branches[0]).strip() if branches else "Other"
    return f"aio:{branch}"


def load_corpus() -> tuple[list[str], list[str], list[dict]]:
    aio_records: list[tuple[Path, dict]] = []
    aio_names: dict[str, str] = {}
    for path in sorted(AIO_DIR.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and doc.get("id"):
            aio_records.append((path, doc))
            aio_names[str(doc["id"])] = str(doc.get("name") or doc["id"])

    curated_records: list[tuple[Path, dict]] = []
    for path in sorted(CURATED_DIR.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and doc.get("id"):
            curated_records.append((path, doc))

    ids: list[str] = []
    docs: list[str] = []
    meta: list[dict] = []

    for path, rec in curated_records:
        rec_id = str(rec["id"])
        text = build_document(rec, aio_names)
        ids.append(rec_id)
        docs.append(text)
        meta.append(
            {
                "identifier": rec_id,
                "label": str(rec.get("name") or rec_id),
                "origin": "curated",
                "class": record_class(rec),
                "concept_kind": rec.get("concept_kind") or "",
                "path": str(path.relative_to(REPO_ROOT)),
                "char_len": len(text),
            }
        )

    for path, rec in aio_records:
        rec_id = str(rec["id"])
        text = build_document(rec, aio_names)
        ids.append(rec_id)
        docs.append(text)
        branches = rec.get("branches") or []
        meta.append(
            {
                "identifier": rec_id,
                "label": str(rec.get("name") or rec_id),
                "origin": "aio",
                "class": record_class(rec),
                "branch": branches[0] if branches else "",
                "path": str(path.relative_to(REPO_ROOT)),
                "char_len": len(text),
            }
        )

    return ids, docs, meta


def corpus_fingerprint(docs: list[str]) -> str:
    h = hashlib.sha256()
    for d in docs:
        h.update(d.encode("utf-8"))
        h.update(b"\0")
    return h.hexdigest()[:16]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--model", default=MODEL_NAME)
    ap.add_argument("--batch-size", type=int, default=32)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    ids, docs, meta = load_corpus()
    if args.limit:
        ids, docs, meta = ids[: args.limit], docs[: args.limit], meta[: args.limit]

    lengths = sorted(len(d) for d in docs)
    n = len(lengths)
    print(
        f"{n} documents  chars: min={lengths[0]} p50={lengths[n // 2]} "
        f"p95={lengths[int(n * 0.95)]} max={lengths[-1]}"
    )

    if args.dry_run:
        return 0

    import numpy as np
    import torch
    from sentence_transformers import SentenceTransformer

    device = (
        "mps"
        if torch.backends.mps.is_available()
        else ("cuda" if torch.cuda.is_available() else "cpu")
    )
    print(f"loading {args.model} on {device} ...")
    model = SentenceTransformer(args.model, device=device)

    vecs = model.encode(
        docs,
        batch_size=args.batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype(np.float32)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    np.save(OUT_DIR / "vectors.npy", vecs)
    (OUT_DIR / "ids.json").write_text(json.dumps(ids, indent=2) + "\n", encoding="utf-8")
    (OUT_DIR / "meta.json").write_text(
        json.dumps(
            {
                "model": args.model,
                "dim": int(vecs.shape[1]),
                "n": int(vecs.shape[0]),
                "corpus_fingerprint": corpus_fingerprint(docs),
                "excluded_fields": list(EXCLUDED),
                "records": meta,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUT_DIR}/vectors.npy {vecs.shape} and meta.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
