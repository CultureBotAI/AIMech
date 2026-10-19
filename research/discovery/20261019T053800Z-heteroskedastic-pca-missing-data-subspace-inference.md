# Discovery Report: Round 293 — Heteroskedastic PCA Principal Subspace Confidence Regions and Spiked Covariance Inference with Missing Data

- **Timestamp**: `2026-10-19T05:38:00Z`
- **Selected Concept**: `AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData` (*Heteroskedastic PCA Principal Subspace Confidence Regions and Spiked Covariance Inference with Missing Data*)
- **Record Path**: `data/curated/HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData.yaml`
- **Primary Source**: Yuling Yan, Yuxin Chen, Jianqing Fan — *Inference for Heteroskedastic PCA with Missing Data* (`https://doi.org/10.1214/24-AOS2366`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 687 maintained AIMech concepts. Distinct from `AIMech:AsymmetricLowRankEigenvalueAndLinearFormEigenvectorPerturbationAnalysis` (Chen, Cheng, & Fan 2021, which analyzes a single $n \times n$ asymmetric noisy matrix with independent entries rather than sample Gram matrices $\frac{1}{n}\sum_{t=1}^n \boldsymbol{z}_t\boldsymbol{z}_t^\top$ whose entries have dependent Wishart-type products across $n$ observations, diagonal noise-variance inflation, and multi-rank $\chi_r^2$ Wald subspace confidence regions) and from `AIMech:DebiasedNoisyMatrixCompletionInferenceAndUncertaintyQuantification` (Chen, Fan, Ma, & Yan 2019, which addresses homoskedastic matrix completion where $d_1 \asymp d_2$ rather than spiked covariance PCA with $d \ll n$ or $d \gtrsim n$ under heteroskedastic column observations).

## Constructed Boundary & Regime Verification

```text
{
  "dimension_d": 16,
  "sample_size_n": 450,
  "observation_prob_p": 0.65,
  "mean_vanilla_sin_theta": 0.21321,
  "mean_deflated_sin_theta": 0.07536,
  "bias_reduction_ratio": 2.829,
  "coordinate_0_wald_95_coverage": 0.9667,
  "linear_form_95_coverage": 0.875
}
```
