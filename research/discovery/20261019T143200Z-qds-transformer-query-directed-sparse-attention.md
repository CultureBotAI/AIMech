# Discovery Report: Round 789 — QDS-Transformer: Query-Directed Sparse Transformer for Long Document Ranking

- **Timestamp**: `2026-10-19T14:32:00Z`
- **Selected Concept**: `AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking` (*QDS-Transformer: Query-Directed Sparse Transformer for Long Document Ranking*)
- **Record Path**: `data/curated/QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking.yaml`
- **Primary Source**: Jyun-Yu Jiang, Chenyan Xiong, Chia-Jung Lee, Wei Wang — *Long Document Ranking with Query-Directed Sparse Transformer* (`https://arxiv.org/bibtex/2010.12683`).

## Identity & Boundary Resolution

Distinct from general-purpose sparse Transformers such as Sparse Transformer (local/strided attention only) and Longformer-QA (which places global attention only on two task tokens without sentence-level [SOS] hierarchy or full query-directed paths), and from passage-splitting rankers such as BERT-MaxP or PARADE. QDS-Transformer encodes the entire long document up to 2,048 tokens in a unified cross-encoder with IR-axiomatic sparse attention compiled via TVM CUDA kernels.

## Constructed Boundary & Regime Verification

```text
QDS-Transformer boundary verification passed:
  Dense edges: 10000, QDS edges: 2152 (21.52%), Local-only edges: 880
  A_QDS[85,2]=1, A_QDS[85,65]=1, A_QDS[20,85]=0
```
