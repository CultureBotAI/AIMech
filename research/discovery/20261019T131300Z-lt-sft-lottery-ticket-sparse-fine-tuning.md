# Discovery Report: Round 710 — Lottery Ticket Sparse Fine-Tuning

- **Timestamp**: `2026-10-19T13:13:00Z`
- **Selected Concept**: `AIMech:LTSFTLotteryTicketSparseFineTuning` (*Lottery Ticket Sparse Fine-Tuning*)
- **Record Path**: `data/curated/LTSFTLotteryTicketSparseFineTuning.yaml`
- **Primary Source**: Alan Ansell, Edoardo Maria Ponti, Anna Korhonen, Ivan Vulic — *Composable Sparse Fine-Tuning for Cross-Lingual Transfer* (`https://dblp.org/search/publ/api?q=Composable+Sparse+Fine-Tuning+for+Cross-Lingual+Transfer&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Alan Ansell, Edoardo Maria Ponti, Anna Korhonen, and Ivan Vulic (ACL 2022, pp. 1778-1796, arXiv:2110.07560) as Lottery Ticket Sparse Fine-Tuning (LT-SFT). Distinct from DiffPruning (AIMech:DiffPruning), which learns continuous L0-relaxed binary masks end-to-end in a single training phase; from FISH Mask (AIMech:FISHMask), which selects sparse masks before training using empirical Fisher information without Phase-1 magnitude-change selection and rewinding; and from MAD-X / AdapterFusion (AIMech:AdapterFusion), which insert serial bottleneck adapter layers that increase inference latency.

## Constructed Boundary & Regime Verification

```text
[PASS] LT-SFT boundaries verified: k=20/200, max_comm_err=0.00e+00, overlap_sparse=0.020 < overlap_dense=1.000
```
