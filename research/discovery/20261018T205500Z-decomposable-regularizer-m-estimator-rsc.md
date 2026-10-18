# Discovery Report: Decomposable Regularizer and Restricted Strong Convexity M-Estimator Framework (Round 228)

- **Report ID**: `20261018T205500Z-decomposable-regularizer-m-estimator-rsc`
- **Created At**: `2026-10-18T20:55:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:DecomposableRegularizerAndRestrictedStrongConvexityMEstimatorFramework` (`data/curated/DecomposableRegularizerAndRestrictedStrongConvexityMEstimatorFramework.yaml`)
- **Verification Script**: `research/discovery/decomposable-regularizer-m-estimator-rsc-boundaries.py` (SHA-256: `9f1b568151707af7216e27c6c4c70a8450f67a94c527a40842efd11a45c6a09e`)

## Summary of Primary Sources Inspected

1. **Sahand N. Negahban, Pradeep Ravikumar, Martin J. Wainwright, & Bin Yu (2012)**, *A Unified Framework for High-Dimensional Analysis of M-Estimators with Decomposable Regularizers*, *Statistical Science* 27(4):538-557 (`DOI:10.1214/12-STS400`, `arXiv:1010.2731v1/v3`).
   - Read all 20 pages of the published *Statistical Science* electronic reprint (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/0c59f4dfa9b34d26.pdf`, `458465` bytes, SHA-256 `c11181ffbb6938d80317fb7ae0463d97f69be9a92a81f3a49cdc8f5b6c971f60`), all 45 pages of the full technical version with Appendices A-D (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/b0930658e646e2c4.pdf`, `571156` bytes, SHA-256 `e28e8dee9baa8bb6cbc20b0a7a624724a72e6801eab71c4c66cde323f6c662fd`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3593/content.md`, `7263` bytes, SHA-256 `752eeba039acb52576f510569555498cd80e0a85ce8ff561c13fd97babc4a257`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3595/content.md`, `7684` bytes, SHA-256 `350e12aa38171b14e7fedc72045ab1a57d06f1c4b8ee80471eb647339f7e9052`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:DecomposableRegularizerAndRestrictedStrongConvexityMEstimatorFramework",
  "subspace_decomposability": {
    "l1_decomp_err": 0.0,
    "group_decomp_err": 0.0,
    "dual_norm_bound_satisfied": true,
    "nuc_decomp_err": 0.0,
    "dim_M_UV": 1,
    "dim_M_bar_UV": 7,
    "psi_M_bar_UV_ratio": 1.414213562373095,
    "passed": true
  },
  "lemma1_and_theorem1": {
    "cone_satisfied": true,
    "delta_exact_l2": 0.12764419120038414,
    "cor1_l2_bound": 0.5982443001348092,
    "thm1_v3_sq_bound": 0.8052665459485224,
    "lemma3_dev_ok": true,
    "star_shaped_satisfied": true,
    "star_ray_ok": true,
    "non_cone_witness_verified": true,
    "passed": true
  },
  "lq_weak_sparsity_and_glm_truncation": {
    "lq_card": 4,
    "lq_card_bound": 27.128988761931105,
    "lq_approx_l1": 0.13490623857362094,
    "lq_approx_bound": 0.8138696628579332,
    "rate_alpha_2": 0.11912023005428146,
    "rate_alpha_inf": 0.6791202300542813,
    "phi_tau_max_lip": 2.3699999999999988,
    "passed": true
  },
  "all_passed": true
}
```

Executed pure-Python verification in research/discovery/decomposable-regularizer-m-estimator-rsc-boundaries.py (SHA-256 9f1b568151707af7216e27c6c4c70a8450f67a94c527a40842efd11a45c6a09e): verified (1) subspace decomposability R(theta + gamma) = R(theta) + R(gamma) across coordinate l_1 (error 0.0), block-(1, alpha_vec) group norms (error 0.0, Holder dual bound satisfied), and nuclear norm on 4x4 matrices (error 0.0, dim M(U, V) = 1 < dim M_bar(U, V) = 7, Psi(M_bar(U, V)) = sqrt(2r) = 1.414214); (2) Lemma 3 deviation inequalities, Lemma 1 cone vs. star-shaped error constraint set C(M, M_bar^perp; theta*) membership and non-cone scaling witness under weak sparsity, and Theorem 1 / Corollary 1 deterministic error bounds (||Delta||_2 = 0.127644 <= 0.598244, ||Delta||_2^2 = 0.016293 <= 0.805267); and (3) Corollary 3 l_q-ball thresholding bounds (|S_eta| = 4 <= 27.129, ||theta*_{S_eta^c}||_1 = 0.134906 <= 0.813870), Corollary 4 group-norm rate ordering (alpha = 2 rate 0.119120 < alpha = infty rate 0.679120), and Proposition 2 GLM Lipschitz quadratic truncation function phi_tau(u) (max Lipschitz ratio 2.37 <= tau = 2.4).
