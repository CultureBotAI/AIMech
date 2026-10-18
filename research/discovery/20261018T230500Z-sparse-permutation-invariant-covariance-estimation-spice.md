# Discovery Report: Sparse Permutation Invariant Covariance Estimation (Round 241)

- **Report ID**: `20261018T230500Z-sparse-permutation-invariant-covariance-estimation-spice`
- **Created At**: `2026-10-18T23:05:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:SparsePermutationInvariantCovarianceEstimation` (`data/curated/SparsePermutationInvariantCovarianceEstimation.yaml`)
- **Verification Script**: `research/discovery/sparse-permutation-invariant-covariance-estimation-spice-boundaries.py` (SHA-256: `4f9e9af31049691239427ab35ea518469a605d2995151c28300c9793c9e31279`)

## Summary of Primary Sources Inspected

1. **Adam J. Rothman, Peter J. Bickel, Elizaveta Levina, and Ji Zhu (2008)**, *Sparse permutation invariant covariance estimation*, *Electronic Journal of Statistics* 2:494-515 (`arXiv:0801.4837v2`, `DOI:10.1214/08-EJS176`).
   - Read all 22 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/ce4582c3bf4dc428.pdf`, `330771` bytes, SHA-256 `a20de3d4d4e9783a243609b8059bf012b70839d64793ca3a901ac0d29b91afd2`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4033/content.md`, `6041` bytes, SHA-256 `90510b2771e6d0f783dcd396b8a0b674d7274b9d33c9da317cf0a3602437270b`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4027/content.md`, `4396` bytes, SHA-256 `71687006edbc5fe020120b021b9e1f8e3de1be0a2a3b29d80c598294c1af9a1b`).

## Constructed Boundary & Regime Verification

```text
{
  "theorem1_and_correlation_scaling": {
    "eq9_taylor_lhs": 0.01347665,
    "eq9_taylor_rhs": 0.01347665,
    "eq9_abs_err": 5.989919393822873e-10,
    "eq11_penalty_diff_lhs": 0.045,
    "eq11_triangle_lower_bound_rhs": 0.015,
    "term_ii_covariance_diagonal_error": 0.005667,
    "term_ii_correlation_diagonal_error": 1.2212453270876722e-17
  },
  "cholesky_lqa_and_proposition1": {
    "eq22_trace_abs_diff": 4.440892098500626e-16,
    "eq23_logdet_abs_diff": 0.0,
    "eq24_penalty_abs_diff": 0.0,
    "lqa_monotone_descent": true,
    "converged_f_tilde_obj": 2.99572549,
    "prop1_max_convex_gradient_norm_at_T0T_T0": 1.1102230246251565e-16
  },
  "all_assertions_passed": true
}
```

Executed pure-Python verification in research/discovery/sparse-permutation-invariant-covariance-estimation-spice-boundaries.py (SHA-256 4f9e9af31049691239427ab35ea518469a605d2995151c28300c9793c9e31279): verified (1) Theorem 1 integral Taylor expansion log|Omega_0 + Delta| - log|Omega_0| = tr(Sigma_0 Delta) - int_0^1 (1-v) Delta_tilde^T ((Omega_0 + v Delta)^{-1} otimes (Omega_0 + v Delta)^{-1}) Delta_tilde dv (Eq. 9, abs_err = 5.99e-10), triangle inequality penalty decomposition lambda(|Omega_0^- + Delta^-|_1 - |Omega_0^-|_1) = 0.045 >= lambda(|Delta_{S_bar}^-|_1 - |Delta_S^-|_1) = 0.015 (Eq. 11), and exact cancellation of diagonal Term II under correlation rescaling (0.005667 for Sigma_hat vs 1.22e-17 for Gamma_hat); and (2) exact Cholesky reparameterization identities Eqs. (22)-(24) to machine precision (4.44e-16), strict monotonic descent of the Appendix A closed-form Cholesky LQA coordinate updates (Eqs. 30-32), and Proposition 1 global optimality max_ij |nabla f_tilde(T_0^T T_0)_{ij}| = 1.11e-16 at the converged lower-triangular stationary point T_0.
