# Discovery Report: Nonconcave Penalized Quasi-Likelihood for Sparse Covariance and Precision Matrix Estimation (Round 243)

- **Report ID**: `20261018T232500Z-nonconcave-penalized-likelihood-sparse-covariance-precision-estimation`
- **Created At**: `2026-10-18T23:25:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:NonconcavePenalizedQuasiLikelihoodForSparseCovarianceAndPrecisionMatrixEstimation` (`data/curated/NonconcavePenalizedQuasiLikelihoodForSparseCovarianceAndPrecisionMatrixEstimation.yaml`)
- **Verification Script**: `research/discovery/nonconcave-penalized-likelihood-sparse-covariance-precision-estimation-boundaries.py` (SHA-256: `d54a1b5716718ea52647620c2618b61ccb6ccf61429e2b426a7a4569c013d4b7`)

## Summary of Primary Sources Inspected

1. **Clifford Lam and Jianqing Fan (2009)**, *Sparsistency and rates of convergence in large covariance matrix estimation*, *The Annals of Statistics* 37(6B):4254-4278 (`arXiv:0711.3933v3`, `DOI:10.1214/09-AOS720`).
   - Read all 27 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/a118e609eda6e2d8.pdf`, `298191` bytes, SHA-256 `01f07baced6cc851ec20daec9c20c8ca3e9a1f83dc577bfb958b1d8cbdf0ade4`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4090/content.md`, `6795` bytes, SHA-256 `f7f2af94933aa571b61304fa93d8ad964bf17bd77efad6e4249724a0e5a004e6`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4092/content.md`, `3784` bytes, SHA-256 `16a7c3d8f8ac5a2d1770403736f09d1c1e0cad836f17ccb3efb0ef9b2f62a6f9`).

## Constructed Boundary & Regime Verification

```text
All Lam & Fan (2009) sparsistency and nonconcave penalized likelihood assertions passed.
```

Executed pure-Python verification in research/discovery/nonconcave-penalized-likelihood-sparse-covariance-precision-estimation-boundaries.py (SHA-256 d54a1b5716718ea52647620c2618b61ccb6ccf61429e2b426a7a4569c013d4b7): verified (1) origin singularity Condition (C) and exact vanishing of penalty derivatives a_{n1} = b_{n1} = 0 for SCAD and hard-thresholding when |theta^0| > a * lambda versus constant bias derivative a_{n1} = lambda > 0 for L1 (Section 2.3, Condition B); (2) Local Linear Approximation (LLA) iteratively reweighted L1 modified Cholesky estimation (Section 2.1, Eqs. 2.1-2.2; Section 4, Eq. 4.2), confirming exact zero recovery on all true zero entries S_3^c (sparsistency, Theorem 10) and >50% Frobenius error reduction relative to unweighted L1; (3) the L1 bias-sparsistency compatibility bottleneck (Eqs. 2.3, 2.5, 3.1, 3.3, 4.5), confirming that when s_{n1} = p_n^{1.5} >> p_n, the sparsistency lower bound log p_n / n + eta_n exceeds the L1 bias upper bound (1 + p_n/(s_{n1}+1)) log p_n / n by more than 10x, whereas SCAD eliminates the upper bound; and (4) Lemma 1 Frobenius-operator norm sandwich inequality ||A||_min ||B||_F <= ||A B||_F <= ||A||_2 ||B||_F (Eq. 5.1) and Theorem 5 second-order integral Taylor decomposition I_1 = K_1 + K_2 for q_2(Sigma) = tr(S Sigma^{-1}) + log|Sigma| (Eqs. 5.6-5.7, abs_err < 1e-8).
