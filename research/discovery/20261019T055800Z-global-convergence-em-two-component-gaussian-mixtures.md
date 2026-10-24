# Discovery Report: Round 303 — Global Convergence and Stationary-Point Characterization of EM for Two-Component Gaussian Mixtures

- **Timestamp**: `2026-10-19T05:58:00Z`
- **Selected Concept**: `AIMech:GlobalConvergenceOfEMForTwoComponentGaussianMixtures` (*Global Convergence and Stationary-Point Characterization of EM for Two-Component Gaussian Mixtures*)
- **Record Path**: `data/curated/GlobalConvergenceOfEMForTwoComponentGaussianMixtures.yaml`
- **Primary Source**: Ji Xu, Daniel J. Hsu, Arian Maleki — *Global Analysis of Expectation Maximization for Mixtures of Two Gaussians* (`https://doi.org/10.48550/arXiv.1608.07630`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 697 maintained AIMech concepts. Distinct from `AIMech:PopulationToSampleContractionAndFirstOrderStabilityEM` (Balakrishnan, Wainwright, & Yu 2017, which proves only local contraction inside a high-SNR neighborhood $\mathbb{B}_2(\|\theta^*\|_2/4;\theta^*)$) and `AIMech:OverSpecifiedGaussianMixtureEMSingularityAndAnnulusLocalization` (Dwivedi et al. 2020, which analyzes the degenerate $\theta^* = 0$ over-specified null case rather than global convergence from arbitrary non-orthogonal initializations for $\theta^* \ne 0$).

## Constructed Boundary & Regime Verification

```text
{
  "model1_initial_cosine_with_target": 0.07975,
  "model1_final_cosine_with_target": 1.0,
  "model1_final_param_error": 2.2e-05,
  "model1_orthogonal_init_norm": 2.0,
  "model1_orthogonal_after_45_steps_norm": 0.10644,
  "model2_initial_sin_beta": 0.99049,
  "model2_final_sin_beta": 0.0,
  "model2_initial_a_norm": 1.5,
  "model2_final_a_norm": 8.72e-06,
  "sample_em_a_error": 0.01713,
  "sample_em_b_error": 0.0734
}
```
