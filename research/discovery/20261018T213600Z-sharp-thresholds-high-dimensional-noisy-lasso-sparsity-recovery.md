# Discovery Report: Primal-Dual Witness Method and Sharp Thresholds for High-Dimensional Noisy Lasso Sparsity Recovery (Round 232)

- **Report ID**: `20261018T213600Z-sharp-thresholds-high-dimensional-noisy-lasso-sparsity-recovery`
- **Created At**: `2026-10-18T21:36:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:PrimalDualWitnessAndSharpThresholdsForHighDimensionalNoisyLassoSparsityRecovery` (`data/curated/PrimalDualWitnessAndSharpThresholdsForHighDimensionalNoisyLassoSparsityRecovery.yaml`)
- **Verification Script**: `research/discovery/sharp-thresholds-high-dimensional-noisy-lasso-sparsity-recovery-boundaries.py` (SHA-256: `93bc1611096775960e835b53456f7372be0d65f26d1b2192c869516d77014dea`)

## Summary of Primary Sources Inspected

1. **Martin J. Wainwright (2009)**, *Sharp Thresholds for High-Dimensional and Noisy Sparsity Recovery Using l_1-Constrained Quadratic Programming (Lasso)*, *IEEE Transactions on Information Theory* 55(5):2183-2202 (`arXiv:math/0605740v1`, `DOI:10.1109/TIT.2009.2016018`).
   - Read all 29 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/af786fb3e3b8b581.pdf`, `724217` bytes, SHA-256 `0e6c3f08ca171c14c8e29b8d1c68a070da414ada2e9a01100035e04e2c4e521f`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3692/content.md`, `6135` bytes, SHA-256 `0635b8a0f63ad56ae5f4d009f500b69c5217ab8071208c9a0755882274e8d1ec`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3699/content.md`, `2246` bytes, SHA-256 `bde884e6e5b2e9ab6bbddaed8a9ad8f702b8f255bbd6f8e891d053de1e472c55`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:PrimalDualWitnessAndSharpThresholdsForHighDimensionalNoisyLassoSparsityRecovery",
  "Check1_primal_dual_witness_kkt_equivalence": {
    "kkt_stationarity_max_residual": 1.5265566588595902e-16,
    "max_off_support_subgradient": 0.8676411984924539,
    "max_on_support_perturbation": 0.10533941171061126,
    "min_signal_magnitude_rho_n": 0.9,
    "exact_signed_support_recovered": true,
    "passed": true
  },
  "Check2_threshold_formulas_and_toeplitz_bounds": {
    "uniform_theta_l": 1.0,
    "uniform_theta_u": 1.0,
    "toeplitz_rho_0_10_theta_l": 0.12587297072998554,
    "toeplitz_rho_0_10_theta_u": 2.3225927243099425,
    "noisy_linear_sparsity_n_crit_at_p512": 1652.364493462458,
    "passed": true
  },
  "Check3_conditional_covariance_and_schur_complement": {
    "projection_idempotency_error": 3.3306690738754696e-16,
    "projection_trace": 18.0,
    "expected_trace_n_minus_s": 18,
    "projection_rx_s_error": 3.5388358909926865e-16,
    "h2_relative_variance_at_df20": 0.11764705882352941,
    "h2_relative_variance_at_df2000": 0.0010015022533801101,
    "schur_complement_block_inverse_error": 2.220446049250313e-16,
    "passed": true
  },
  "all_passed": true
}
```

Executed pure-Python verification in research/discovery/sharp-thresholds-high-dimensional-noisy-lasso-sparsity-recovery-boundaries.py (SHA-256 93bc1611096775960e835b53456f7372be0d65f26d1b2192c869516d77014dea): verified (1) exact KKT stationarity residual 1.53e-16 and exact signed support recovery for the primal-dual witness pair (beta_hat, z_hat) under M(V) and M(U) (max off-support subgradient 0.8676 < 1, max on-support perturbation 0.1053 < rho_n = 0.9); (2) exact threshold collapse theta_l = theta_u = 1.0 for the uniform Gaussian ensemble and 0 < theta_l = 0.1259 < 1 < theta_u = 2.3226 for the Toeplitz ensemble with rho = 0.10; and (3) projection idempotency error 3.33e-16, trace 18.0 = n - s, inverse-Wishart relative variance decay from 0.1176 (df=20) to 0.00100 (df=2000), and exact Schur complement block-inverse identity error 2.22e-16.
