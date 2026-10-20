# Discovery Report: Round 558 — PermK Permutation Compressors for Distributed Nonconvex Optimization

- **Timestamp**: `2026-10-19T10:41:00Z`
- **Selected Concept**: `AIMech:PermKPermutationCompressorsForDistributedNonconvexOptimization` (*PermK Permutation Compressors for Distributed Nonconvex Optimization*)
- **Record Path**: `data/curated/PermKPermutationCompressorsForDistributedNonconvexOptimization.yaml`
- **Primary Source**: Rafal Szlendak, Alexander Tyurin, Peter Richtarik — *Permutation Compressors for Provably Faster Distributed Nonconvex Optimization* (`https://dblp.org/rec/conf/iclr/SzlendakTR22`).

## Identity & Boundary Resolution

Introduced by Rafal Szlendak, Alexander Tyurin, and Peter Richtarik (ICLR 2022; arXiv:2110.03300). Distinct from independent RandK sparsification, where each node independently samples k coordinates yielding B = 0 and A = (d - k) / (n * k) without inter-node variance cancellation; and distinct from MARINA (Gorbunov et al., ICML 2021; Round 391), which provides the variance-reduced distributed framework analyzed under independent compressors whereas PermK introduces the AB-assumption and negatively correlated permutation compressors that strictly improve MARINA's theoretical complexity.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 558 PermK verified: Var_PermK(d>=n)=1.864039==IV(1)=1.864039, Var_PermK(n>=d)=0.303369==A2*Var=0.303369, M_PermK=5.00 < M_RandK=10.77
```
