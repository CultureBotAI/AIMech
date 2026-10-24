# Discovery Report: Newton Sketch Randomized Hessian-Projected Second-Order Optimization and Sketched Interior-Point Barrier Method (Round 225)

- **Report ID**: `20261018T202000Z-newton-sketch-randomized-hessian-optimization`
- **Created At**: `2026-10-18T20:20:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:NewtonSketchRandomizedHessianProjectedOptimization` (`data/curated/NewtonSketchRandomizedHessianProjectedOptimization.yaml`)
- **Verification Script**: `research/discovery/newton-sketch-randomized-hessian-optimization-boundaries.py` (SHA-256: `c5cb5f5f7f4f276b74416389910c19374a70f889dc0eb70d32cfc15c3ffce601`)

## Summary of Primary Sources Inspected

1. **Mert Pilanci & Martin J. Wainwright (2017)**, *Newton Sketch: A Near Linear-Time Optimization Algorithm with Linear-Quadratic Convergence*, *SIAM Journal on Optimization* 27(1):205-245 (`DOI:10.1137/15M1021106`, `arXiv:1505.02250v1`).
   - Read all 35 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/290591ef54c06f1e.pdf`, `832028` bytes, SHA-256 `c5fb649d2da871645581ea88f5721f8c57fcde7dc5c754e407091aeb26e98a68`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3514/content.md`, `6179` bytes, SHA-256 `fcdada05a6d2ce0caf69158a3596cbeba4e726c91b01bd0ec5b6af6e8bee10a3`), and SIAM J. Optim. Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3516/content.md`, `3258` bytes, SHA-256 `91aa7dc0bc05ae7986daf1aa6fd92152a7608ada010ea47c26a57d680f8ba291`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:NewtonSketchRandomizedHessianProjectedOptimization",
  "all_passed": true,
  "local_linear_quadratic_and_partial_sketch": {
    "passed": true,
    "grad_norm_star": 5.406134278079866e-16,
    "psk_initial_error": 1.2997705392584087,
    "psk_final_error": 0.007031969022786603,
    "super_final_error": 3.5481223179665453e-07,
    "exact_pre_bound_27": 0.044642857142857144,
    "bound_27": 0.09722222222222222
  },
  "self_concordant_two_phase_bounds": {
    "passed": true,
    "eps_max_positive_eta_for_a_0_1": 0.14589803375031546,
    "eta_at_eps_0_20": -0.008333333333333321,
    "num_phase1_checks": 4,
    "num_phase2_checks": 16
  },
  "barrier_central_path_and_sparse_cone": {
    "passed": true,
    "num_cone_checks": 50,
    "num_central_path_checks": 4
  }
}
```

Executed pure-Python verification in research/discovery/newton-sketch-randomized-hessian-optimization-boundaries.py (SHA-256 c5cb5f5f7f4f276b74416389910c19374a70f889dc0eb70d32cfc15c3ffce601): verified (1) Section 6.1 Equation (27) basic inequality pre-bound (0.044643 <= 0.097222) and empirical convergence of Partial Newton Sketch (Equation 8, reducing error from 1.29977 to 0.007032 in 8 steps with m = 36) vs. Corollary 1 increasing-sketch super-linear schedule (reducing error to 3.548e-7); (2) Lemma 3, Lemma 4, Lemma 5, Lemma 6, and Equation (18) self-concordant Phase-I and Phase-II bounds across 4 Phase-I and 16 Phase-II test configurations, plus the exact positivity threshold eps < (sqrt(2(1-a)) - 1)/(sqrt(2(1-a)) + 1) approx 0.145898 for a = 0.1 (showing eta = -0.008333 < 0 at eps = 0.20); and (3) Section 4.3 log-barrier central-path suboptimality f_0(x_hat(tau)) - f_0(x^*) <= r/tau across 4 barrier parameters and Lemma 8 l_1-ball tangent-cone inclusion ||z||_1 <= 2 sqrt(s) ||z||_2 across 50 random sparse tangent vectors.
