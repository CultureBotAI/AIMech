# Literature Discovery Report: Self-Consistency and Dependency Control Framework for False Discovery Rate Control

- **Report ID**: `20261017T153000Z-self-consistency-and-dependency-control-fdr-framework`
- **Created At**: `2026-10-17T15:30:00Z`
- **Curated Concept**: `AIMech:SelfConsistencyAndDependencyControlFDRFramework` (`data/curated/SelfConsistencyAndDependencyControlFDRFramework.yaml`, SHA-256 `03444e07e1d84f9bdc618210e31fc12764d6e8dc40c4311bef2fe5a40c0e7a80`)
- **Verification Script**: `research/discovery/self-consistency-and-dependency-control-fdr-framework-boundaries.py` (SHA-256 `f15ec6f49ba57c20957030ee69fe11bf53cb9ae1849cf6c6b9961e348e1f547a`)

## Primary Sources Inspected

1. **Gilles Blanchard & Etienne Roquain (2008)** — *Two simple sufficient conditions for FDR control*, *Electronic Journal of Statistics* 2:963–992, `DOI:10.1214/08-EJS180`, `arXiv:0802.1406v2`. Complete full-text HTML conversion read (`sha256: 475022ac6bda3b24dd97d657ea03968fe49a4ae6fe32c367771f4d8d1a414d7f`), Crossref metadata (`sha256: 02a775523a7b4c76ed516c0c92483a8e30d93e48f907fff4be9e02dbcd4f27c2`), and arXiv abstract (`sha256: 56c8e17d84115e0ad99c76372d88b7469fa71988c75bf9a4d57a9b07bcfda651`).

## Candidate Decisions

- **`AIMech:SelfConsistencyAndDependencyControlFDRFramework`** (`ADD_CURATED`): Two-line coupled Self-Consistency `SC(alpha, pi, beta)` and Dependency Control `DC(beta)` doubly weighted FDR factorization (Definitions 2.2–2.6, Proposition 2.7), order-free maximal self-consistent step-up characterization `R_SU = L_Delta(r_hat)` with `|L_Delta(r_hat)| = r_hat` and generalized step-up-down unification (Definition 3.1, Theorem 4.5), prior-integrated shape function family `beta_nu(r) = int_0^r x d_nu(x)` under arbitrary dependence (Lemma 3.2, Proposition 3.7, Theorem 4.2), and two-stage adaptive FWER+FDR and step-down log-convexity bounds (Lemma 4.3, Corollary 4.4, Theorem 4.6).

## Constructed Mathematical Verification Summary

```json
{
  "all_assertions_passed": true,
  "arbitrary_dependence_beta_nu_family": {
    "adversarial_sup_expectations_over_c": {
      "BY_harmonic": 0.9999999999999998,
      "Dirac_k3": 1.0,
      "Sarkar_uniform_quadratic": 1.0,
      "linear_prior_cubic": 0.9999999999999998,
      "linear_simes": 2.4500000000000006
    },
    "alpha": 0.1,
    "concentrated_signal_tier1_rejections": {
      "BY_harmonic": 0,
      "Sarkar_uniform_quadratic": 5,
      "linear_prior_cubic": 5
    },
    "concentrated_signal_tier2_rejections": {
      "BY_harmonic": 0,
      "Sarkar_uniform_quadratic": 0,
      "linear_prior_cubic": 5
    },
    "gamma_m": 2.45,
    "m": 6,
    "worst_case_fdr_at_alpha_0_10": {
      "BY_harmonic": 0.10000000000000013,
      "Dirac_k3": 0.10000000000000002,
      "Sarkar_uniform_quadratic": 0.09999999999999998,
      "linear_prior_cubic": 0.09999999999999999,
      "linear_simes": 0.24500000000000027
    }
  },
  "concept_id": "AIMech:SelfConsistencyAndDependencyControlFDRFramework",
  "order_free_self_consistency": {
    "contiguous_self_consistent_subset": [
      2,
      3
    ],
    "disconnected_r_su": [
      0,
      2,
      3
    ],
    "fixed_point_checks": 4,
    "maximality_checks": 4,
    "pi_lambda_integral": 1.0,
    "total_volume_lambda_H": 6.0
  },
  "primary_source": "Blanchard & Roquain (2008), Electronic Journal of Statistics 2:963-992 (arXiv:0802.1406v2, DOI:10.1214/08-EJS180)",
  "step_down_log_convexity": {
    "bl_step_down_i1_to_i5_m10": [
      0.005,
      0.006172839506172839,
      0.0078125,
      0.01020408163265306,
      0.013888888888888888
    ],
    "checked_m_m0_pairs": 300,
    "holm_step_down_i1_to_i5_m10": [
      0.005,
      0.005555555555555556,
      0.00625,
      0.0071428571428571435,
      0.008333333333333333
    ],
    "max_log_convex_endpoint_ratio": 1.0000000000000002
  }
}
```
