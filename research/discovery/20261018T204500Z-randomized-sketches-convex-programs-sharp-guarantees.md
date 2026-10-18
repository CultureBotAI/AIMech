# Discovery Report: Randomized Sketches of Convex Programs with Tangent-Cone Gaussian-Width Cost-Approximation and Privacy Mutual-Information Guarantees (Round 227)

- **Report ID**: `20261018T204500Z-randomized-sketches-convex-programs-sharp-guarantees`
- **Created At**: `2026-10-18T20:45:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees` (`data/curated/RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.yaml`)
- **Verification Script**: `research/discovery/randomized-sketches-convex-programs-sharp-guarantees-boundaries.py` (SHA-256: `c9fd8f5cd7b66fd03ff1122bfa039b9e705515f20a95ad956e462b443a891a03`)

## Summary of Primary Sources Inspected

1. **Mert Pilanci & Martin J. Wainwright (2015)**, *Randomized Sketches of Convex Programs with Sharp Guarantees*, *IEEE Transactions on Information Theory* 61(9):5096-5115 (`DOI:10.1109/TIT.2015.2450722`, `arXiv:1404.7203v1`).
   - Read all 37 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/328def08bc042f61.pdf`, `400673` bytes, SHA-256 `899110b22c4ad05f9d27efd82d3d77cc3071bfd638e50d3b6907e42335dd860f`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3567/content.md`, `6954` bytes, SHA-256 `456699d94d7316fb287e723936a65211ee170cd6c3c00a64954d1458c2c26c16`), and IEEE Trans. Inf. Theory Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3569/content.md`, `2937` bytes, SHA-256 `27b3fe6046311afa141ca9a1db13a28454e2dec09179ae37b99e555546e5c26e`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees",
  "all_passed": true,
  "lemma1_and_corollary1_privacy": {
    "passed": true,
    "f_star": 49.067043781522855,
    "f_hat": 52.74937743533492,
    "approx_ratio": 1.0750469840858585,
    "lhs_error_ratio": 0.27394704613457416,
    "rhs_2z2_over_z1": 0.9339985897644327,
    "lemma1_cost_upper_bound": 183.5279439601019,
    "mi_rate_n200": 0.4256815599614018,
    "mi_rate_n4000": 0.02128407799807009
  },
  "corollary4_denoising_and_corollary5_svm": {
    "passed": true,
    "noiseless_cs_recovery_err": 1.6691059580047844e-15,
    "noisy_denoise_ratio": 1.7371440177078805,
    "dual_svm_approx_ratio": 1.4376573178420367
  },
  "lemma8_and_lemma13_convex_hull": {
    "passed": true,
    "all_lemma13_passed": true,
    "max_support_ratio_observed": 1.973747104582024,
    "lemma8_eq84_passed": true
  }
}
```

Executed pure-Python verification in research/discovery/randomized-sketches-convex-programs-sharp-guarantees-boundaries.py (SHA-256 c9fd8f5cd7b66fd03ff1122bfa039b9e705515f20a95ad956e462b443a891a03): verified (1) Lemma 1 deterministic tangent-cone cost approximation inequality (relative error ratio 0.273947 <= 2 Z_2(AK)/Z_1(AK) = 0.933999, f(x_hat) = 52.749377 <= 183.527944, approximation ratio 1.075047) and Corollary 1 vanishing mutual information rate per matrix symbol (0.425682 at n = 200 vs. 0.021284 at n = 4000); (2) Corollary 4 noiseless compressed sensing exact recovery via sketched l_1 denoising (recovery error 1.669e-15), folded-noise denoising cost ratio (1.737144), and Corollary 5 dual squared-hinge SVM simplex sketching cost ratio (1.437657); and (3) Lemma 13 support-function inequality phi_1(X) <= 3 phi_0(X) across 90 random test matrices (maximum ratio 1.973747 <= 2 <= 3) and Lemma 8 Equation (84) convex-hull difference quadratic-form bound across 50 random convex combinations.
