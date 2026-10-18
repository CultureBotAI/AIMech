# Discovery Report: Minimax-Optimal Sparse Additive Models Over Kernel Classes via Convex Programming (Round 230)

- **Report ID**: `20261018T211800Z-minimax-optimal-sparse-additive-models-kernel-classes`
- **Created At**: `2026-10-18T21:18:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:MinimaxOptimalSparseAdditiveModelsOverKernelClassesViaConvexProgramming` (`data/curated/MinimaxOptimalSparseAdditiveModelsOverKernelClassesViaConvexProgramming.yaml`)
- **Verification Script**: `research/discovery/minimax-optimal-sparse-additive-models-kernel-classes-boundaries.py` (SHA-256: `5ac422c4dacb5cce97d9bb2c6fc210ff97867676e3230e341a6973923802e9a3`)

## Summary of Primary Sources Inspected

1. **Garvesh Raskutti, Martin J. Wainwright, & Bin Yu (2012)**, *Minimax-Optimal Rates for Sparse Additive Models Over Kernel Classes via Convex Programming*, *Journal of Machine Learning Research* 13:389-427 (`arXiv:1008.3654v2`).
   - Read all 38 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/5e6c7266bb57a11b.pdf`, `444347` bytes, SHA-256 `e1a233b53aa11551fe58ad5d8e92f41c915a4e39d68ce2489c13124332284847`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3636/content.md`, `6799` bytes, SHA-256 `10e05ec0cb82be342b9fb42735fa3c96d0ea5eef3bf4de42a968322ba783f1be`), and JMLR v13 metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3638/content.md`, `6654` bytes, SHA-256 `e9bd64ab813f9bf36fc7e58acb92896b1d7a8d0e6958eace5b05a15c5f6b2aa1`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:MinimaxOptimalSparseAdditiveModelsOverKernelClassesViaConvexProgramming",
  "critical_univariate_rates_and_corollaries": {
    "nu_finite_sq": 1.2499999999999997e-05,
    "expected_nu_finite_sq": 1.25e-05,
    "sobolev_scaled_values": [
      0.003358737186716891,
      0.0033768520909520944,
      0.0033951526170273613
    ],
    "rwy_rate": 0.0654512185534475,
    "meier_rate": 0.12688585255186446,
    "passed": true
  },
  "representer_socp_decomposability_and_fourth_moment": {
    "representer_ok": true,
    "lemma2_ok": true,
    "sup_norm_g": 50.0,
    "exact_fourth_moment": 3.739648,
    "bound_p30": 5.0176,
    "bound_10_delta_sq": 6.4,
    "passed": true
  },
  "global_boundedness_phase_transition": {
    "lemma10_l1_sum": 2.0,
    "lemma10_rhs": 6.0,
    "unbounded_rate_n100k": 1.0,
    "kb_n100": 0.4821340852028949,
    "kb_n100k": 0.09597051824376164,
    "bounded_rate_n100k": 0.09597051824376164,
    "passed": true
  },
  "all_passed": true
}
```

Executed pure-Python verification in research/discovery/minimax-optimal-sparse-additive-models-kernel-classes-boundaries.py (SHA-256 5ac422c4dacb5cce97d9bb2c6fc210ff97867676e3230e341a6973923802e9a3): verified (1) the critical univariate rate nu_n^2 = m / (1600 n) = 1.25e-05 for rank-m kernels (Corollary 1), the Sobolev scaling nu_n^2 * n^{2 alpha / (2 alpha + 1)} in [0.003359, 0.003395] for alpha = 2 (Corollary 2), and the strict improvement of the Raskutti-Wainwright-Yu rate (0.065451) over the Meier et al. (2009) coupled-penalty rate (0.126886); (2) exact representer-theorem SOCP norm equivalence (Equations 10-11), the Lemma 2 decomposability cone inequality (Equations 33 & 40a), and the Lemma 3 fourth-moment bound E[g^4(x)] = 3.739648 <= 4 delta_tilde_n^2 + 6 delta_tilde_n^4 = 5.0176 <= 10 delta_tilde_n^2 = 6.4 despite ||g||_infty = 2s = 50.0; and (3) Lemma 10 Fourier l_1 bound (2.0 <= 6.0) and the Theorem 3 / Corollary 3 global boundedness phase transition at alpha = 2, s = n^{4/5} (unbounded rate = 1.0 vs. globally bounded rate 0.095971 at n = 10^5).
