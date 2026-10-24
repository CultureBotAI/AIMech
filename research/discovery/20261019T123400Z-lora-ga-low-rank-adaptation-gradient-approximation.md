# Discovery Report: Round 671 — LoRA-GA

- **Timestamp**: `2026-10-19T12:34:00Z`
- **Selected Concept**: `AIMech:LoRAGA` (*LoRA-GA*)
- **Record Path**: `data/curated/LoRAGA.yaml`
- **Primary Source**: Shaowen Wang, Linxi Yu, Jian Li — *LoRA-GA: Low-Rank Adaptation with Gradient Approximation* (`https://dblp.org/search/publ/api?q=LoRA-GA+Low-Rank+Adaptation+Gradient+Approximation&format=xml`).

## Identity & Boundary Resolution

Distinct from AIMech:LowRankAdaptation (which uses Kaiming uniform initialization for A and zeros for B, restricting the initial update to rank r) and from AIMech:PissaPrincipalSingularValuesAndSingularVectorsAdaptation (PiSSA, which decomposes the pre-trained weight matrix W_0 via SVD rather than the task loss gradient nabla_W L). LoRA-GA (Shaowen Wang, Linxi Yu, & Jian Li, NeurIPS 2024, arXiv:2407.05000) minimizes ||eta^2 (nabla_W L A_init^T A_init + B_init B_init^T nabla_W L) - zeta nabla_W L||_F (Equation 3). Given SVD nabla_W L = U S V^T, Theorem 3.1 proves that choosing disjoint index sets I_A = {1, ..., r} and I_B = {r+1, ..., 2r} with A_init = (sqrt(zeta)/eta) V_{[1:r]}^T and B_init = (sqrt(zeta)/eta) U_{[r+1:2r]} produces the exact rank-2r Eckart-Young-Mirsky optimal Frobenius approximation zeta sum_{i=1}^{2r} sigma_i u_i v_i^T. Combined with Theorem 3.2's scale-stability analysis (eta = alpha / sqrt(r) and zeta = (alpha^2 / gamma^2) sqrt(d_out) / r^2), LoRA-GA sets A_init = (d_out^{1/4} / gamma) V_{[1:r]}^T, B_init = (d_out^{1/4} / gamma) U_{[r+1:2r]}, and adjusts the frozen base weight to W_init = W_0 - eta B_init A_init via layer-by-layer backward hooks.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 671 LoRA-GA (Wang et al., NeurIPS 2024): ey_2r_diff=2.90e-15, err_ga=1.1998<err_overlap=12.1064<err_lora=18.9085, weight_inv_err=1.47e-16
```
