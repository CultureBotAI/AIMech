# Discovery Report: Round 675 — MiLoRA

- **Timestamp**: `2026-10-19T12:38:00Z`
- **Selected Concept**: `AIMech:MiLoRA` (*MiLoRA*)
- **Record Path**: `data/curated/MiLoRA.yaml`
- **Primary Source**: Hanqing Wang, Yixia Li, Shuo Wang, Guanhua Chen, Yun Chen — *MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning* (`https://dblp.org/search/publ/api?q=MiLoRA+Harnessing+Minor+Singular+Components&format=xml`).

## Identity & Boundary Resolution

Directly complementary to AIMech:PissaPrincipalSingularValuesAndSingularVectorsAdaptation (PiSSA, which initializes the trainable adapter from the top-r principal singular components and freezes the minor residual) and distinct from AIMech:LowRankAdaptation (which initializes A randomly and B to zero in an unguided subspace). MiLoRA (Minor singular component based Low-Rank Adaptation; Hanqing Wang, Yixia Li, Shuo Wang, Guanhua Chen, & Yun Chen, NAACL 2025, arXiv:2406.09044) partitions the SVD W = U Sigma V^T = sum_{i=1}^{m-r} sigma_i u_i v_i^T + sum_{i=m-r+1}^m sigma_i u_i v_i^T = W_p + W_m (Equations 3-5). By freezing W_p and initializing B_m = U_m sqrt(Sigma_m) and A_m = sqrt(Sigma_m) V_m^T, MiLoRA (1) satisfies W = W_p + B_m A_m exactly at initialization without setting B_m = 0 or tuning a separate alpha/r scaling factor, and (2) initializes the trainable adapter in a subspace orthogonal to the principal knowledge subspace (U_p^T B_m = 0, A_m V_p = 0), adapting long-tail/noisy singular directions to the downstream task while minimizing catastrophic forgetting of pre-trained world knowledge.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 675 MiLoRA (Wang et al., NAACL 2025): recon_err=1.31e-15, orth_err=2.29e-15, forgetting_milora=2.7231e-18<<forgetting_pissa=1.7460
```
