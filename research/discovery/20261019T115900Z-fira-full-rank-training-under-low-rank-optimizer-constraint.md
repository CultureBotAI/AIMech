# Discovery Report: Round 636 — Fira (Full-Rank Training under Low-Rank Optimizer Constraint)

- **Timestamp**: `2026-10-19T11:59:00Z`
- **Selected Concept**: `AIMech:FiraFullRankTrainingUnderLowRankOptimizerConstraint` (*Fira (Full-Rank Training under Low-Rank Optimizer Constraint)*)
- **Record Path**: `data/curated/FiraFullRankTrainingUnderLowRankOptimizerConstraint.yaml`
- **Primary Source**: Xi Chen, Kaituo Feng, Changsheng Li, Xunhao Lai, Xiangyu Yue, Ye Yuan, Guoren Wang — *Fira: Can We Achieve Full-rank Training of LLMs Under Low-rank Constraint?* (`https://dblp.org/rec/conf/nips/ChenFLLYYW25`).

## Identity & Boundary Resolution

Distinct from GaLore (AIMech:GaLoreGradientLowRankProjection), which projects the full-rank gradient G_t into a rank-r subspace R_t = P_t^T G_t and completely discards the orthogonal residual (I - P_t P_t^T) G_t = G_t - P_t R_t; Fira retains the same low-rank optimizer states (mr + 2nr + 1 floats per m x n matrix) but scales and adds back G_t - P_t R_t using the low-rank adaptive scaling factor phi_t(R_t) = ||psi_t(R_t)|| / ||R_t|| alongside a multiplicative norm-growth limiter gamma.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 636 Fira verified: thm1_kappa4=0.0427<=bound4=0.1144, thm2_var_ratio_n64=0.0455, limited_norm=2.0200, state_saving=84.37%
```
