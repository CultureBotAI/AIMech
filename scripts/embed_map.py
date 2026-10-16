#!/usr/bin/env python3
"""Project ``data/embeddings/vectors.npy`` to 2D with PaCMAP for AIMech.

Writes ``data/embeddings/corpus_map.json`` (committed), which ``render_pages.py``
embeds into ``pages/map.html``.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
EMB_DIR = REPO_ROOT / "data" / "embeddings"
OUT_PATH = EMB_DIR / "corpus_map.json"


def project(vecs: np.ndarray, seed: int) -> np.ndarray:
    import pacmap

    reducer = pacmap.PaCMAP(
        n_components=2,
        n_neighbors=15,
        MN_ratio=0.5,
        FP_ratio=2.0,
        random_state=seed,
    )
    return reducer.fit_transform(vecs)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    vecs = np.load(EMB_DIR / "vectors.npy")
    meta = json.loads((EMB_DIR / "meta.json").read_text(encoding="utf-8"))
    records = meta["records"]
    assert len(records) == len(vecs), "vectors.npy and meta.json disagree on row count"

    xy = project(vecs, args.seed)
    lo = xy.min(axis=0)
    span = np.where((xy.max(axis=0) - lo) == 0, 1.0, xy.max(axis=0) - lo)
    xy = (xy - lo) / span

    classes = sorted({r.get("class") or "other" for r in records})
    cls_idx = {c: i for i, c in enumerate(classes)}

    points = [
        [
            round(float(xy[i, 0]), 4),
            round(float(xy[i, 1]), 4),
            cls_idx[r.get("class") or "other"],
            r["identifier"],
            r["label"],
        ]
        for i, r in enumerate(records)
    ]

    payload = {
        "model": meta["model"],
        "method": "pacmap",
        "n": len(points),
        "corpus_fingerprint": meta.get("corpus_fingerprint", ""),
        "classes": classes,
        "points": points,
    }
    OUT_PATH.write_text(json.dumps(payload, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"wrote {OUT_PATH} ({OUT_PATH.stat().st_size // 1024} KB, {len(points)} points)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
