# Bounded search and sequence decoding — 2026-10-11T06:17:04Z

Added six concepts; the native collection now contains 141 DRAFT records.

| Record | AIO assessment |
| --- | --- |
| [AIMech:BreadthFirstBranchAndBound](../../data/curated/BreadthFirstBranchAndBound.yaml) | No suitable match in the inspected pin |
| [AIMech:BreadthFirstIDAStar](../../data/curated/BreadthFirstIDAStar.yaml) | No suitable match in the inspected pin |
| [AIMech:DivideConquerBeamSearch](../../data/curated/DivideConquerBeamSearch.yaml) | No suitable match in the inspected pin |
| [AIMech:SequenceBestFirstBeamSearch](../../data/curated/SequenceBestFirstBeamSearch.yaml) | Related to Natural Language Processing |
| [AIMech:SequenceAStarBeamSearch](../../data/curated/SequenceAStarBeamSearch.yaml) | Related to Natural Language Processing |
| [AIMech:MemoryReducedSequenceBeamSearch](../../data/curated/MemoryReducedSequenceBeamSearch.yaml) | Related to Natural Language Processing |

The records separate inclusive hypothetical cost bounds, actual-incumbent improvement pruning, permanent beam truncation, per-length decoding budgets, heuristic priorities and earliest-length queue eviction.

The monotone decoder retains its conditional beam-equivalence claim. A portable [curator illustration](../../research/validation/20261011T061704Z-nonmonotone-beam-counterexample.py) and [actual result](../../research/validation/20261011T061704Z-nonmonotone-beam-counterexample.json) document why an unrestricted nonmonotonic stop-only extension is not asserted. This is not execution of the authors’ decoder.

The JSON companion records primary sources, exact reading scope, ignored-inclusive identity checks, mapping decisions and unresolved leads. BSIDA-star remains deferred pending a sufficiently explicit contour specification. Discovery continues.
