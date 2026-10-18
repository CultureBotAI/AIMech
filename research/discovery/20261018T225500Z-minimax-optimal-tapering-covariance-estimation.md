# Discovery Report: Minimax-Optimal Tapering for High-Dimensional Covariance Matrix Estimation (Round 240)

- **Report ID**: `20261018T225500Z-minimax-optimal-tapering-covariance-estimation`
- **Created At**: `2026-10-18T22:55:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:MinimaxOptimalTaperingForHighDimensionalCovarianceMatrixEstimation` (`data/curated/MinimaxOptimalTaperingForHighDimensionalCovarianceMatrixEstimation.yaml`)
- **Verification Script**: `research/discovery/minimax-optimal-tapering-covariance-estimation-boundaries.py` (SHA-256: `ea382b6d54477373aef2d5342734e824704c09891b91fe2a11d32ed5dad43fe6`)

## Summary of Primary Sources Inspected

1. **T. Tony Cai, Cun-Hui Zhang, and Harrison H. Zhou (2010)**, *Optimal rates of convergence for covariance matrix estimation*, *The Annals of Statistics* 38(4):2118-2144 (`arXiv:1010.3866v1`, `DOI:10.1214/09-AOS752`).
   - Read all 29 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/354f475dc9ef3f36.pdf`, `373880` bytes, SHA-256 `eab388616ad6ff62f658b598fa78b16d0665ae7c8d2fa427cf7e3fb25273f5ad`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4015/content.md`, `6297` bytes, SHA-256 `5f276e324e82aed0d5b06f68518a72b88ecd46996729cd08905b7743a03f7368`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4009/content.md`, `3266` bytes, SHA-256 `c519319b248be8728ba011964b553803387f02648d4eba1d80c95cea15f3acd4`).

## Constructed Boundary & Regime Verification

```text
{
  "lemma1_block_sum_identity": {
    "p": 14,
    "k": 6,
    "k_h": 3,
    "max_abs_diff_direct_vs_block_sum": 4.440892098500626e-16,
    "p23_count_identity_rhs_at_dist4": 2,
    "kh_times_w_correct": 2.0,
    "k_times_w_p23_typo": 4.0
  },
  "bias_and_lemma2_block_bound": {
    "p": 18,
    "k": 6,
    "alpha": 1.5,
    "bias_op_norm": 0.046885,
    "bias_l1_norm": 0.058774,
    "theoretical_kh_tail_bound": 0.091398,
    "lemma2_lhs_op_norm": 1.02816,
    "lemma2_rhs_3x_max_block_op": 3.199881,
    "lemma2_ratio_lhs_over_rhs": 0.321312
  },
  "lemma5_and_rate_dichotomy": {
    "lemma5_op_norm_sq": 0.0225,
    "lemma5_rhs_bound": 0.0225,
    "k_op_at_n1000_alpha1": 10.0,
    "k_frob_at_n1000_alpha1": 5.6234,
    "tapering_minimax_op_rate": 0.018517,
    "bickel_levina_banding_bound": 0.092289
  },
  "all_assertions_passed": true
}
```

Executed pure-Python verification in research/discovery/minimax-optimal-tapering-covariance-estimation-boundaries.py (SHA-256 ea382b6d54477373aef2d5342734e824704c09891b91fe2a11d32ed5dad43fe6): verified (1) Lemma 1 exact block-sum identity Sigma_hat_k = k_h^{-1}(S^{*(k)} - S^{*(k_h)}) on a 14x14 sample covariance matrix with k=6, k_h=3 to machine precision (max_abs_diff = 4.44e-16) and confirmed the p. 23 proof display typo (k_h * w_{ij} = 2.0 vs k * w_{ij} = 4.0 at |i-j|=4); (2) operator-norm bias bound ||E[Sigma_breve] - Sigma||_2 = 0.046885 <= ||E[Sigma_breve] - Sigma||_1 = 0.058774 <= M * k_h^{-alpha} = 0.091398 on a power-law Toeplitz covariance matrix in G_alpha (p=18, k=6, alpha=1.5), and Lemma 2 block-norm inequality ||Sigma_breve - E[Sigma_breve]||_2 = 1.02816 <= 3 * max_l ||M_l^{(k)} - E[M_l^{(k)}]||_2 = 3.199881 (ratio 0.321312); and (3) Lemma 5 Assouad operator-norm separation ||Sigma(theta) - Sigma(theta')||_2^2 = 0.0225 >= H(theta, theta') * tau^2 * k_h * a^2 = 0.0225, norm-dependent bandwidth dichotomy k_op = 10.0 > k_frob = 5.6234 at n=1000, alpha=1.0, and rate improvement 0.018517 < 0.092289 over Bickel-Levina (2008a) banding.
