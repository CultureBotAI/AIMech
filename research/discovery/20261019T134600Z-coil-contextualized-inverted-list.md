# Discovery Report: Round 743 — COIL Contextualized Inverted List

- **Timestamp**: `2026-10-19T13:46:00Z`
- **Selected Concept**: `AIMech:COILContextualizedInvertedList` (*COIL Contextualized Inverted List*)
- **Record Path**: `data/curated/COILContextualizedInvertedList.yaml`
- **Primary Source**: Luyu Gao, Zhuyun Dai, Jamie Callan — *COIL: Revisit Exact Lexical Match in Information Retrieval with Contextualized Inverted List* (`https://dblp.org/rec/conf/naacl/GaoDC21.xml`).

## Identity & Boundary Resolution

Distinct from classical bag-of-words inverted-list retrievers such as BM25 and scalar LM term-weighting methods such as DeepCT (Dai & Callan, SIGIR 2019, equivalent to n_t = 1 scalar term importance without context-dependent vector similarity); distinct from single-vector dense retrievers such as DPR (AIMech:DensePassageRetrieval), which rely solely on global [CLS] matching without token-level exact match; and distinct from ColBERT (Khattab & Zaharia, SIGIR 2020, AIMech:ColBERTContextualizedLateInteraction), which computes Cartesian all-to-all soft MaxSim across all query and document token vectors rather than traversing inverted lists of exact overlapping surface tokens.

## Constructed Boundary & Regime Verification

```text
Round 743 COIL boundary verification passed.
```
