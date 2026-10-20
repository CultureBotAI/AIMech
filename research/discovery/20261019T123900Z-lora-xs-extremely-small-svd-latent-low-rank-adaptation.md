# Discovery Report: Round 676 — LoRA-XS

- **Timestamp**: `2026-10-19T12:39:00Z`
- **Selected Concept**: `AIMech:LoRAXS` (*LoRA-XS*)
- **Record Path**: `data/curated/LoRAXS.yaml`
- **Primary Source**: Klaudia Balazy, Mohammadreza Banaei, Karl Aberer, Jacek Tabor — *LoRA-XS: Low-Rank Adaptation with Extremely Small Number of Parameters* (`https://dblp.org/search/publ/api?q=LoRA-XS+Low-Rank+Adaptation+Extremely+Small&format=xml`).

## Identity & Boundary Resolution

Distinct from AIMech:LowRankAdaptation (which trains A in R^{m x r} and B in R^{r x n} requiring (m+n)r parameters per module), AIMech:VeraVectorBasedRandomMatrixAdaptation (which shares frozen random matrices and learns diagonal scaling vectors of size n + r per module that still grow linearly with hidden dimension n), and AIMech:PissaPrincipalSingularValuesAndSingularVectorsAdaptation (which initializes A and B with the top-r SVD of W but updates all (m+n)r entries of A and B during training). LoRA-XS (Low-Rank Adaptation with eXtremely Small number of parameters; Klaudia Balazy, Mohammadreza Banaei, Karl Aberer, & Jacek Tabor, ECAI 2025, arXiv:2405.17604) proves (Section 3.2, Theorem 1 & Appendix B) that for fixed orthonormal U_r, V_r, the mapping p_{U_r, V_r}(X) = U_r (U_r^T X V_r) V_r^T is the Frobenius-orthogonal projection onto the r^2-dimensional subspace S^r_{U_r, V_r} = {U_r R V_r^T : R in R^{r x r}}, and that the top-r SVD factors of W minimize the Frobenius approximation distance under the pre-training gradient alignment assumption W ~ (1/k) sum_i G_i. By freezing A = U_r Sigma_r and B = V_r^T and training only R ~ N(0, sigma^2) in R^{r x r}, LoRA-XS reduces trainable parameters by a factor of 2n/r relative to LoRA and (n+r)/r^2 relative to VeRA while merging into W post-training with zero inference latency.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 676 LoRA-XS (Balazy et al., ECAI 2025): param_ratio_lora_vs_xs=128x, idemp_err=8.08e-16, dist_svd=2.3027<dist_rand=18.0575<dist_bot=19.1387
```
