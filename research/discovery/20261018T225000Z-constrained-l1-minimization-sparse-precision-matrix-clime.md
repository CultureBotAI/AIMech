# Discovery Report: Constrained L1 Minimization for Sparse Precision Matrix Estimation (Round 239)

- **Report ID**: `20261018T225000Z-constrained-l1-minimization-sparse-precision-matrix-clime`
- **Created At**: `2026-10-18T22:50:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:ConstrainedL1MinimizationForSparsePrecisionMatrixEstimation` (`data/curated/ConstrainedL1MinimizationForSparsePrecisionMatrixEstimation.yaml`)
- **Verification Script**: `research/discovery/constrained-l1-minimization-sparse-precision-matrix-clime-boundaries.py` (SHA-256: `ca862efa1df1ad3c35fcc34822d7465f6537e7d1ff238547be44bc72ed88107b`)

## Summary of Primary Sources Inspected

1. **Tony Cai, Weidong Liu, and Xi Luo (2011)**, *A Constrained l1 Minimization Approach to Sparse Precision Matrix Estimation*, *Journal of the American Statistical Association* 106(494):594-607 (`arXiv:1102.2233v1`, `DOI:10.1198/jasa.2011.tm10155`).
   - Read all 41 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/eb302e6c48bfa15d.pdf`, `445193` bytes, SHA-256 `32c1984fb425daec3a32a0677b73f7be579497a95d93cf78d2292bfff892ae63`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3934/content.md`, `5935` bytes, SHA-256 `f8dd832d7fe28ad0450c556a532bf1920cf68662b23963131a3a33c7510e679f`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3935/content.md`, `1518` bytes, SHA-256 `d99ccafbe878b7d18d642a8fd2345303a0ca2db7d835ce6fd5a4eaf625ce830c`).

## Constructed Boundary & Regime Verification

```text
{"actual_cov_err": 0.00195506, "all_passed": true, "checks": {"cone_decomposition_hj2_le_hj1": true, "eq13_linf_bound_holds": true, "eq14_l1_bound_holds": true, "eq15_frob_bound_holds": true, "eq24_omega0_feasible": true, "eq25_column_l1_optimality": true, "eq26_sample_residual_bound": true, "eq27_hj1_bound_holds": true, "glasso_incoherence_violated_gt_1": true, "pop_residual_bound_4lambda": true, "thm7_exact_signed_support_recovery": true, "thm7_theta_min_gt_2tau_n": true}, "eq13_rhs": 0.02264055, "eq14_rhs": 1.08674642, "eq15_rhs": 0.02460454, "eq24_lhs": 0.00272012, "eq26_lhs": 0.00591117, "frob_avg": 0.00013627, "glasso_incoherence_param": 1.0736, "l1_omega_hat": 1.68540576, "l1_omega_hat_1": 1.68550576, "lambda_n": 0.00332655, "linf_err_tn": 0.0093, "max_col_l1_err": 0.0313, "omega0_l1_norm_M": 1.70150576, "pop_res_lhs": 0.005868, "rho_diamond": 0.22, "sparsity_s0_q0": 4, "tau_n": 0.02264055, "theta_min": 0.10717449}
```

Executed pure-Python verification in research/discovery/constrained-l1-minimization-sparse-precision-matrix-clime-boundaries.py (SHA-256 ca862efa1df1ad3c35fcc34822d7465f6537e7d1ff238547be44bc72ed88107b): verified (1) on a 4-node diamond precision matrix with rho = 0.22 where the graphical Lasso edge-Hessian irrepresentable parameter 4|rho|(|rho|+1) = 1.0736 > 1 is violated (Section 3.3, Eq. 17), CLIME satisfies exact feasibility |I - Sigma_n Omega_0|_infty = 0.00272012 <= lambda_n = 0.00332655 (Eq. 24) and column L1 optimality ||Omega_hat||_{L1} = 1.68540576 <= ||Omega_hat_1||_{L1} = 1.68550576 <= ||Omega_0||_{L1} = 1.70150576 (Eq. 25); and (2) sample residual |Sigma_n(Omega_hat_1 - Omega_0)|_infty = 0.00591117 <= 2*lambda_n = 0.0066531 (Eq. 26), population residual |Sigma_0(Omega_hat_1 - Omega_0)|_infty = 0.005868 <= 4*lambda_n = 0.0133062, elementwise l_infty bound |Omega_hat - Omega_0|_infty = 0.0093 <= 4*||Omega_0||_{L1}*lambda_n = 0.02264055 (Theorem 6, Eq. 13), cone decomposition |h^2_j|_1 <= |h^1_j|_1 and Eq. (27), matrix L1 bound 0.0313 <= 1.08674642 (Eq. 14), average Frobenius bound 0.00013627 <= 0.02460454 (Eq. 15), and exact Theorem 7 signed support recovery M(Omega_tilde) = M(Omega_0) with theta_min = 0.10717449 > 2*tau_n = 0.0452811.
