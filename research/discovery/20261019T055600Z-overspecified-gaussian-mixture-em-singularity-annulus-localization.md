# Discovery Report: Round 302 — Over-Specified Gaussian Mixture EM Singularity Dichotomy and Annulus-Based Epoch Localization

- **Timestamp**: `2026-10-19T05:56:00Z`
- **Selected Concept**: `AIMech:OverSpecifiedGaussianMixtureEMSingularityAndAnnulusLocalization` (*Over-Specified Gaussian Mixture EM Singularity Dichotomy and Annulus-Based Epoch Localization*)
- **Record Path**: `data/curated/OverSpecifiedGaussianMixtureEMSingularityAndAnnulusLocalization.yaml`
- **Primary Source**: Raaz Dwivedi, Nhat Ho, Koulik Khamaru, Martin J. Wainwright, Michael I. Jordan, Bin Yu — *Singularity, Misspecification, and the Convergence Rate of EM* (`https://doi.org/10.1214/19-AOS1924`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 696 maintained AIMech concepts. Distinct from `AIMech:PopulationToSampleContractionAndFirstOrderStabilityEM` (Balakrishnan, Wainwright, & Yu 2017), which requires well-separated components ($\|\theta^*\|_2/\sigma > \eta$) and $\lambda$-strong concavity of $Q(\cdot\mid\theta^*)$ and whose one-shot framework yields only the loose $(d/n)^{1/6}$ bound (Equation 21) in the singular balanced over-specified regime.

## Constructed Boundary & Regime Verification

```text
{
  "fisher_beta_unbalanced": 0.36,
  "fisher_beta_balanced": 0.0,
  "unbalanced_pop_ratio_at_0_35": 0.6363,
  "balanced_pop_ratio_at_0_35": 0.90017,
  "balanced_gamma_bounds_at_0_35": [
    0.80321,
    0.95144
  ],
  "balanced_pop_ratio_at_0_05": 0.997512,
  "annulus_alpha_1_naive": 0.166667,
  "annulus_alpha_12_localized": 0.25,
  "sample_em_unbalanced_error": 0.01271,
  "sample_em_balanced_error": 0.1859,
  "theorem4_balanced_fixed_point_lower_bound": 0.17961
}
```
