# Discovery Report: Round 553 — Quasi-Global Momentum for Heterogeneous Decentralized Deep Learning

- **Timestamp**: `2026-10-19T10:36:00Z`
- **Selected Concept**: `AIMech:QuasiGlobalMomentumForHeterogeneousDecentralizedDeepLearning` (*Quasi-Global Momentum for Heterogeneous Decentralized Deep Learning*)
- **Record Path**: `data/curated/QuasiGlobalMomentumForHeterogeneousDecentralizedDeepLearning.yaml`
- **Primary Source**: Tao Lin, Sai Praneeth Karimireddy, Sebastian U. Stich, Martin Jaggi — *Quasi-Global Momentum: Accelerating Decentralized Deep Learning on Heterogeneous Data* (`https://dblp.org/rec/conf/icml/0004KSJ21`).

## Identity & Boundary Resolution

Introduced by Tao Lin, Sai Praneeth Karimireddy, Sebastian U. Stich, and Martin Jaggi (ICML 2021, PMLR Vol. 139, pp. 6654-6665; arXiv:2102.04761). Distinct from SlowMo (Wang et al., ICLR 2020), which performs periodic global All-Reduce synchronization every tau >> 1 steps and never feeds the slow momentum buffer back into local gradient steps; distinct from MimeLite (Karimireddy et al., 2020), which computes full-batch gradients at a central server in federated learning; and distinct from DMSGD (Balu et al., 2020), which forms a non-recursive convex combination of local and consensus step differences.

## Constructed Boundary & Regime Verification

```text
[PASS] Quasi-Global Momentum boundaries verified: QHM_diff<1e-14, cons_qg=0.0338<cons_simple=0.2876, disagree_qg=0.5466<disagree_local=3.0912
```
