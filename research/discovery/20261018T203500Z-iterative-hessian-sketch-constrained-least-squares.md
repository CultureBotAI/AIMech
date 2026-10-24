# Discovery Report: Iterative Hessian Sketch for Constrained Least-Squares and Information-Theoretic Classical Sketching Lower Bounds (Round 226)

- **Report ID**: `20261018T203500Z-iterative-hessian-sketch-constrained-least-squares`
- **Created At**: `2026-10-18T20:35:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:IterativeHessianSketchForConstrainedLeastSquares` (`data/curated/IterativeHessianSketchForConstrainedLeastSquares.yaml`)
- **Verification Script**: `research/discovery/iterative-hessian-sketch-constrained-least-squares-boundaries.py` (SHA-256: `951b71668675b9b5a1accae2ee73efaf02772c1b7e993a59901ac79827889ee5`)

## Summary of Primary Sources Inspected

1. **Mert Pilanci & Martin J. Wainwright (2016)**, *Iterative Hessian Sketch: Fast and Accurate Solution Approximation for Constrained Least-Squares*, *Journal of Machine Learning Research* 17(53):1-38 (`arXiv:1411.0347v1`).
   - Read all 33 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/e2600e31baf9d089.pdf`, `682666` bytes, SHA-256 `dea3c1364a748d6a428dbfd16ba058ab9265c83fb8c11374812bd487c4c4d147`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3540/content.md`, `6449` bytes, SHA-256 `e6cc8cea30c1d6a8c76f9cc0ff30bd1174521c5ca0054a42c36a0078f3745634`), and JMLR v17/14-460 metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3542/content.md`, `6239` bytes, SHA-256 `19fa92bd87c2ef95c737af6a6b880d52e2afd761eb83825ac636628fe0d41401`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:IterativeHessianSketchForConstrainedLeastSquares",
  "all_passed": true,
  "unconstrained_ihs_and_theorem1_2": {
    "passed": true,
    "ols_stat_err": 0.04088827677040154,
    "ihs_stat_err": 0.04109504420070216,
    "classical_stat_err": 0.12727772242146404,
    "ihs_ols_gap": 0.0003819292885153705,
    "classical_ols_gap": 0.11646909834560103,
    "theorem2_product_bound": 0.12175253124797426,
    "all_step_inequalities_39_passed": true
  },
  "sparse_l1_constrained_ihs": {
    "passed": true,
    "initial_gap": 1.4140436263049643,
    "round1_gap": 0.28177805056510624,
    "final_gap": 0.011687177300639338
  }
}
```

Executed pure-Python verification in research/discovery/iterative-hessian-sketch-constrained-least-squares-boundaries.py (SHA-256 951b71668675b9b5a1accae2ee73efaf02772c1b7e993a59901ac79827889ee5): verified (1) Theorem 1 and Corollary 2 statistical sub-optimality of single-shot classical sketching (prediction error 0.127278, OLS gap 0.116469) vs. unconstrained Iterative Hessian Sketch over N = 12 rounds (prediction error 0.041095 matching exact OLS error 0.040888, OLS gap 3.819e-4); (2) Proposition 1 and Theorem 2 deterministic per-step inequality ||x^{t+1} - x^{LS}||_A <= (Z_2(S^{t+1})/Z_1(S^{t+1})) ||x^t - x^{LS}||_A (Equation 39) across all 12 steps and cumulative product bound (0.000382 <= 0.121753); and (3) Section 3.2 Corollary 3 geometric convergence of constrained IHS on l_1-constrained sparse least squares (reducing prediction-norm gap to x^{LS} from 1.414044 to 0.281778 after 1 round and 0.011687 after 5 rounds).
