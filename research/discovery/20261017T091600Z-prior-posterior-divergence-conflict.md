# Literature Discovery Report: Prior-to-Posterior Divergence Conflict Diagnostic

- **Report ID**: `20261017T091600Z-prior-posterior-divergence-conflict`
- **Created At**: `2026-10-17T09:16:00Z`
- **Curated Concept**: `AIMech:PriorToPosteriorDivergenceConflictDiagnostic` (`data/curated/PriorToPosteriorDivergenceConflictDiagnostic.yaml`, SHA-256 `d1df8267a5bde0e2caf13c64e51c1f826b3374cfa784565af3c1755c779933a1`)
- **Verification Script**: `research/discovery/prior-posterior-divergence-conflict-boundaries.py` (SHA-256 `719ee995c73face4d9ecf3026295f95780c28a15101b5f3ba45188afe700d004`)

## Primary Sources Inspected

1. **Nott, Wang, Evans, & Englert (2020)** — *Checking for Prior-Data Conflict Using Prior to Posterior Divergences*, *Statistical Science* 35(2):234–253, `arXiv:1611.00113v1` (DOI `https://doi.org/10.1214/19-STS731`). Complete full-text HTML conversion read (`sha256: 8347841fa2b6835fceedd13af2a6148ce621cfd94c64c2bddde275020d86eb70`).
2. **Nott, Seah, Al-Labadi, Evans, Ng, & Englert (2020)** — *Using Prior Expansions for Prior-Data Conflict Checking*, *Bayesian Analysis* 16(1):203–231, `arXiv:1902.10393v2` (DOI `https://doi.org/10.1214/20-BA1204`). Complete 31-page PDF read (`sha256: 2d36e3af352ac38b3811af3540aed3d115be5f4b4f6ecdadb4ec8fec74d07a99`).

## Candidate Decisions

- **`AIMech:PriorToPosteriorDivergenceConflictDiagnostic`** (`ADD_CURATED`): Bayesian prior-data conflict diagnostic algorithm that measures belief change from prior to posterior via the Rényi divergence of order $\alpha > 0$, calibrates the observed divergence under the prior predictive distribution, decomposes hierarchical priors into marginal and posterior-integrated conditional divergence checks, and approximates intractable repeated posterior divergences via exponential-family or Hershey–Olsen Gaussian mixture variational approximations.

## Constructed Mathematical Verification Summary

```json
{
  "binomial_uniform_prior_boundary": {
    "kl_at_y0": 2.09214151,
    "kl_at_y10": 0.84350482,
    "n": 20,
    "p_evans_moshonov_uniform_prior": 1.0,
    "p_kl_at_y0_or_y20": 0.0952381,
    "p_kl_at_y10": 1.0
  },
  "hershey_olsen_mixture_kl_bound": {
    "abs_approximation_gap": 1.28717209,
    "kl_hershey_olsen_eq21": 1.68062394,
    "kl_numerical_quadrature": 0.39345184
  },
  "hierarchical_nig_double_use_boundary": {
    "p_value_divergence_mixed_t_2a_prime": 0.01248693,
    "p_value_evans_moshonov_t_2a_prime_minus_1": 0.00087847,
    "sigma_star_full_posterior": 1.57094148,
    "sigma_tilde_ancillary_conditioned": 1.04880885,
    "t_stat_divergence_mixed": 2.86452427,
    "t_stat_evans_moshonov": 4.29058165
  },
  "normal_location_renyi_equivalence": {
    "MR_alpha_inf": 3.30471896,
    "R_KL_alpha_1.0": 2.40471896,
    "R_alpha_0.5": 1.96056,
    "R_alpha_2.0": 2.73304785,
    "p_value_all_alpha_and_EM": 0.02534732
  }
}
```
