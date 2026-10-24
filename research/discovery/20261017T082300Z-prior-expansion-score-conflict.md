# Literature Discovery Report: Prior-Expansion Score Conflict Diagnostic

- **Report ID**: `20261017T082300Z-prior-expansion-score-conflict`
- **Created At**: `2026-10-17T08:23:00Z`
- **Updated At**: `2026-10-24T10:55:00Z`
- **Curated Concept**: `AIMech:PriorExpansionScoreConflictDiagnostic` (`data/curated/PriorExpansionScoreConflictDiagnostic.yaml`, SHA-256 `a4273d15d5b0aab65f1e895e0600f1a0e528c3b49faa328024f1e326e1e59c29`)
- **Verification Script**: `research/discovery/prior-expansion-score-conflict-boundaries.py` (SHA-256 `be07cba05309d97d625aecfd1f061b04de4c88850dcd2088e5f70ae25a2b74d0`)

## Primary Sources Inspected

1. **Nott, Seah, Al-Labadi, Evans, Ng, & Englert (2020/2021)** — *Using prior expansions for prior-data conflict checking*, `arXiv:1902.10393v2` (published in *Bayesian Analysis* 16(1):203–231, 2021, DOI `https://doi.org/10.1214/20-BA1204`). Complete 31-page PDF read (`sha256: 2d36e3af352ac38b3811af3540aed3d115be5f4b4f6ecdadb4ec8fec74d07a99`).
2. **Yang, Nott, & Presanis (2026)** — *Detecting Conflicts in Evidence Synthesis Models Using Score Discrepancies*, `arXiv:2511.02977v2` (DOI `https://doi.org/10.48550/arXiv.2511.02977`). Complete 52-page PDF read (`sha256: 4829e0d63d562483aa6aab88a418c62e6d336cd63e9205ee175bf9e9c1bade2d`).

## Candidate Decisions

- **`AIMech:PriorExpansionScoreConflictDiagnostic`** (`ADD_CURATED`): Embeds an elicited baseline prior $g(\theta)$ into a smooth expansion family $g(\theta\mid\gamma)$ with $g(\theta\mid\gamma_0)=g(\theta)$, evaluates the marginal-likelihood score $S(y)=\left.\frac{d}{d\gamma}\log p(y\mid\gamma)\right|_{\gamma=\gamma_0}$ via Fisher's identity as the baseline posterior expectation $\mathbb{E}_{\theta\sim g(\theta\mid y)}\!\left[\left.\frac{d}{d\gamma}\log g(\theta\mid\gamma)\right|_{\gamma=\gamma_0}\right]$ when prior support is fixed, and calibrates $S(y_{\text{obs}})$ against prior-predictive or hierarchical mixed-predictive reference distributions.
- **Sequential score-discrepancy conflict diagnostic (Yang, Nott, & Presanis, 2026)** (`DEFER_PENDING_PRIMARY_SOURCE`): Full 52-page v2 PDF read and hashed; queued for dedicated curation next as `AIMech:SequentialScoreDiscrepancyConflictDiagnostic`.

## Constructed Mathematical Verification Summary

```json
{
  "coordinate_wise_directional_expansions": {
    "location_two_sided_matches_scale_upper_tail": true,
    "one_at_a_time_identities_agree": true,
    "rows": [
      {
        "p_location_two_sided": 0.00040695,
        "p_scale_upper_tail": 0.00040695,
        "s_location": 5.0,
        "s_scale": 2.875,
        "tau0_sq": 0.25
      },
      {
        "p_location_two_sided": 0.02534732,
        "p_scale_upper_tail": 0.02534732,
        "s_location": 2.0,
        "s_scale": 1.6,
        "tau0_sq": 1.0
      },
      {
        "p_location_two_sided": 0.22525291,
        "p_scale_upper_tail": 0.22525291,
        "s_location": 0.58823529,
        "s_scale": 0.22145329,
        "tau0_sq": 4.0
      }
    ]
  },
  "evans_moshonov_equivalence": {
    "exact_equivalence": true,
    "p_evans_moshonov": 0.02534732,
    "p_score_upper_tail": 0.02534732,
    "tested_tau0_sq_values": [
      0.25,
      1.0,
      2.0,
      4.0
    ],
    "z_obs": 2.23606798
  },
  "fisher_and_renyi": {
    "d_varying_kl_analytic": -0.88,
    "finite_alpha_matches_escort_and_differs_from_kl": true,
    "identities_agree": true,
    "neg_d_fixed_posterior_kl": 1.6,
    "neg_d_varying_posterior_kl": 0.88,
    "non_unit_tau0_sq_4_v_025_score": 0.22145329,
    "non_unit_tau0_sq_4_v_025_tau2_derivative": 0.05536332,
    "renyi_varying_orders_tau0_sq_1": {
      "alpha_0.5": {
        "d_kl_limit": -0.88,
        "d_renyi_escort": -0.51111111,
        "d_renyi_fd": -0.51111111
      },
      "alpha_2.0": {
        "d_kl_limit": -0.88,
        "d_renyi_escort": -1.17530864,
        "d_renyi_fd": -1.17530864
      }
    },
    "renyi_varying_orders_tau0_sq_4": {
      "alpha_0.5": {
        "d_kl_limit": -0.1677183,
        "d_renyi_escort": -0.12422573,
        "d_renyi_fd": -0.12422573
      },
      "alpha_2.0": {
        "d_kl_limit": -0.1677183,
        "d_renyi_escort": -0.19313614,
        "d_renyi_fd": -0.19313614
      }
    },
    "s_claim_expanded": 1.6,
    "s_direct": 1.6,
    "s_fisher": 1.6,
    "s_tau2_example_4_1": 1.6,
    "tested_grid_size": 20,
    "varying_posterior_differs_by_cov_term": true
  },
  "hierarchical_normal_random_effects": {
    "s1_lower_mixed": 0.22687596,
    "s2_upper_marginal": 0.99722992,
    "ss_between": 2.48,
    "upper_score_positive_for_grand_mean_shift": true,
    "y_grand": 2.0
  },
  "support_dependent_boundary": {
    "boundary_posterior_density": 0.31303529,
    "naive_fails_by_boundary_term": true,
    "reparameterized_matches_exact": true,
    "s_exact_fd": -0.68696471,
    "s_naive_eq_1_3": -1.0,
    "s_reparameterized": -0.68696471
  }
}
```
