# Discovery Report: Round 301 — Population-to-Sample Contraction, First-Order Stability (FOS), and Gradient Stability (GS) Framework for the EM Algorithm

- **Timestamp**: `2026-10-19T05:54:00Z`
- **Selected Concept**: `AIMech:PopulationToSampleContractionAndFirstOrderStabilityEM` (*Population-to-Sample Contraction, First-Order Stability (FOS), and Gradient Stability (GS) Framework for the EM Algorithm*)
- **Record Path**: `data/curated/PopulationToSampleContractionAndFirstOrderStabilityEM.yaml`
- **Primary Source**: Sivaraman Balakrishnan, Martin J. Wainwright, Bin Yu — *Statistical guarantees for the EM algorithm: From population to sample-based analysis* (`https://doi.org/10.1214/16-AOS1435`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 695 maintained AIMech concepts. Distinct from `AIO:Clustering` and `AIO:LinearRegression`, which define general task/model classes without the population-to-sample EM operator decomposition, First-Order Stability $\mathrm{FOS}(\gamma)$, Gradient Stability $\mathrm{GS}(\gamma)$, or non-asymptotic sample-based contraction bounds.

## Constructed Boundary & Regime Verification

```text
{
  "snr": 2.5,
  "basin_radius": 0.625,
  "init_dist": 0.5895,
  "empirical_fos_contraction_gamma": 0.02089,
  "sample_em_opt_error": 0.0,
  "sample_grad_em_opt_error": 2.2215299868541707e-16,
  "sample_em_stat_error": 0.05975,
  "missing_covariate_kappa_moderate_snr": 0.57653,
  "missing_covariate_kappa_excessive_snr": 2.03
}
```
