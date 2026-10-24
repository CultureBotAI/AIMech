# Discovery Report: Minimax Estimation Rates for High-Dimensional Linear Regression Over l_q-Balls (Round 229)

- **Report ID**: `20261018T210800Z-minimax-rates-high-dimensional-linear-regression-lq-balls`
- **Created At**: `2026-10-18T21:08:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:MinimaxEstimationRatesForHighDimensionalLinearRegressionOverLqBalls` (`data/curated/MinimaxEstimationRatesForHighDimensionalLinearRegressionOverLqBalls.yaml`)
- **Verification Script**: `research/discovery/minimax-rates-high-dimensional-linear-regression-lq-balls-boundaries.py` (SHA-256: `1b469c490a7643a3435e01b0f1da65c99f1a661c923094dfb63af6222284f956`)

## Summary of Primary Sources Inspected

1. **Garvesh Raskutti, Martin J. Wainwright, & Bin Yu (2011)**, *Minimax Rates of Estimation for High-Dimensional Linear Regression Over $\ell_q$-Balls*, *IEEE Transactions on Information Theory* 57(10):6976-6994 (`DOI:10.1109/TIT.2011.2165799`, `arXiv:0910.2042v1`).
   - Read all 38 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/16245e79e0009c9a.pdf`, `437689` bytes, SHA-256 `5e57de2c4f3312304da5cf4f0dd86cc885cb10a14442e7f6e533ec8a5c945778`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3605/content.md`, `6702` bytes, SHA-256 `9a6993ea8b2ef5e73df3de810fa22f57aa983269cbf0c7adfa768661d6ee40c3`), and IEEE Trans. Inf. Theory Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3607/content.md`, `2478` bytes, SHA-256 `046e870f92902753d44fc1691470e3bed8b9cb0ede36cb48809e0d8df607dfac`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:MinimaxEstimationRatesForHighDimensionalLinearRegressionOverLqBalls",
  "section_3_3_1_counterexample": {
    "det_2x2_submatrices": [
      1.0,
      -1.0,
      3.0
    ],
    "kappa_l_on_B0_2": 0.16692526771109398,
    "delta_in_nullspace": true,
    "delta_in_Gamma_1_1": true,
    "delta_not_in_B0_2": true,
    "l1_norm_beta_star": 1.0,
    "l1_norm_beta_hat_wrong": 0.6666666666666666,
    "passed": true
  },
  "lemma1_lemma2_and_theorem2a": {
    "lemma2_ok": true,
    "x_root_sq": 3.3488722290691033,
    "four_max_b2_c": 5.1166214700950965,
    "diam2_nq": 0.7698003589195009,
    "f_l_over_kappa_l": 3.0792014356780038,
    "passed": true
  },
  "lemma5_packing_and_role_reversal": {
    "h_set_card": 3360,
    "packing_card": 181,
    "lemma5_min_card_bound": 9.0,
    "min_dist_sq": 0.5000000000000001,
    "max_dist_sq": 2.0000000000000004,
    "target_delta_n_sq": 0.25,
    "role_reversal_ok": true,
    "passed": true
  },
  "all_passed": true
}
```

Executed pure-Python verification in research/discovery/minimax-rates-high-dimensional-linear-regression-lq-balls-boundaries.py (SHA-256 1b469c490a7643a3435e01b0f1da65c99f1a661c923094dfb63af6222284f956): verified (1) the explicit 2x3 design matrix X = [[1, -2, -1], [2, -3, -3]] in Section 3.3.1 (p. 12, Equation 29) where ker(X) = span{[1, 1/3, 1/3]^T} satisfies B_0(2) cap ker(X) = {0} (so l_0-constrained least squares exactly recovers beta* = [1, 0, 0]^T) yet Delta = [1, 1/3, 1/3]^T in Gamma(1, 1) cap ker(X) violates the l_1 Restricted Eigenvalue condition RE(1; 1) and causes noiseless Basis Pursuit / Lasso on Y = [1, 2]^T to recover beta_hat = [0, -1/3, -1/3]^T with ||beta_hat||_1 = 2/3 < 1 = ||beta*||_1; (2) Lemma 1 nullspace diameter bound diam_2(N_q(X)) <= f_l / kappa_l, Lemma 2 l_p/l_2 interpolation over B_q(2 R_q), and Lemma 7 quadratic root bound x_root^2 = 3.348872 <= 4 max{b^2, c} = 5.116621 in Theorem 2(a); and (3) Lemma 5 greedy ternary Hamming packing on H(s) for d = 10, s = 4 (yielding 181 packing points >= ((d-s)/(s/2))^{s/2} = 9 with pairwise distances in [delta_n^2, 8 delta_n^2] = [0.25, 2.0]) and the exact role reversal of design eigenvalue sensitivity between l_2-parameter risk (ratio 100.0x) and l_2-prediction risk (ratio 1.0x).
