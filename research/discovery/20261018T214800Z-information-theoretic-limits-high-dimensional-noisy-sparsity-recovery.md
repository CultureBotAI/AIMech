# Discovery Report: Information-Theoretic Limits of High-Dimensional Noisy Sparsity Recovery (Round 233)

- **Report ID**: `20261018T214800Z-information-theoretic-limits-high-dimensional-noisy-sparsity-recovery`
- **Created At**: `2026-10-18T21:48:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:InformationTheoreticLimitsOfHighDimensionalNoisySparsityRecovery` (`data/curated/InformationTheoreticLimitsOfHighDimensionalNoisySparsityRecovery.yaml`)
- **Verification Script**: `research/discovery/information-theoretic-limits-high-dimensional-noisy-sparsity-recovery-boundaries.py` (SHA-256: `4c370b9d579bfd9b4572c7e89223d9e30827ac636d02903bc17fe4717cfa52a3`)

## Summary of Primary Sources Inspected

1. **Martin J. Wainwright (2009)**, *Information-Theoretic Limits on Sparsity Recovery in the High-Dimensional and Noisy Setting*, *IEEE Transactions on Information Theory* 55(12):5728-5741 (`arXiv:math/0702301v2`, `DOI:10.1109/TIT.2009.2032816`).
   - Read all 16 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/652465cab09bc87c.pdf`, `201812` bytes, SHA-256 `d102257bf09627556031822b6ca712b587ce157ef6bfa86db7b63bb2f9f6dcf1`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3691/content.md`, `6303` bytes, SHA-256 `24ca09c196ed8fefbc2c9a381037ba3551e720387604715c3084fa9859a03b05`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3731/content.md`, `3224` bytes, SHA-256 `9f4eb210c09faebbf443b25c5f680c3862be3242e5dbc9be280c6cd01645b011`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:InformationTheoreticLimitsOfHighDimensionalNoisySparsityRecovery",
  "all_passed": true,
  "projection_decoder_and_lemma1": {
    "passed": true,
    "f_u_ols": 24.42773373,
    "f_u_lemma1": 24.42773373,
    "f_s_noise": 14.06874937,
    "delta_u": 10.35898435,
    "lhs_perp_diff": -1.20751204,
    "rhs_exact_pi_s_minus_pi_u": -1.20751204
  },
  "lemma2_exponent_and_vandermonde": {
    "passed": true,
    "birge_min_over_a": 2.64423077,
    "closed_form_d_bsq_over_16_bsq_plus_4": 2.64423077,
    "lemma2_eq15_exponent": 5.28846154,
    "vandermonde_overlap_sum": 4367,
    "total_other_supports": 4367
  },
  "fano_kl_and_linear_sparsity_gap": {
    "passed": true,
    "expected_kl_uv": 50.0,
    "upper_bound_kl": 75.0,
    "fano_ratio_exact_vs_eq30": 2.0,
    "lasso_to_it_sample_ratio_p100_1000_10000": [
      4.3862,
      6.3471,
      8.3432
    ]
  }
}
```

Executed pure-Python verification in research/discovery/information-theoretic-limits-high-dimensional-noisy-sparsity-recovery-boundaries.py (SHA-256 4c370b9d579bfd9b4572c7e89223d9e30827ac636d02903bc17fe4717cfa52a3): verified (1) exact identity between OLS residual squared norm f(U) = 24.42773373, projection norm ||Pi_U^perp (X_{S \ U} beta*_{S \ U} + W)||_2^2 = 24.42773373, and Lemma 1 test statistic Delta(U) = 10.35898435, plus the orthogonal-projection difference identity ||Pi_U^perp W||_2^2 - ||Pi_S^perp W||_2^2 = ||Pi_S W||_2^2 - ||Pi_U W||_2^2 = -1.20751204; (2) Birge's non-central chi-squared Chernoff exponent lower bound 2.64423077 = (n - s)||beta*_{S \ U}||_2^2 / (16(||beta*_{S \ U}||_2^2 + 4)) on event A and Vandermonde overlap sum sum_{k=1}^s binom(s, k) binom(p - s, k) = 4367 = binom(16, 5) - 1; and (3) expected conditional KL divergence E[D(P_U || P_V | X)] = 50.0 < n s M^2(beta*) = 75.0, factor-of-2 ratio 2.0 between Eq. 30 and p. 11 bottom display, and diverging Lasso-to-optimal sample complexity ratio [4.3862, 6.3471, 8.3432] across p in {100, 1000, 10000} for linear sparsity s = 0.1 p.
