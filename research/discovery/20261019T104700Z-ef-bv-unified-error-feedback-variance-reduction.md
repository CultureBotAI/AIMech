# Discovery Report: Round 564 — EF-BV Unified Error Feedback and Variance Reduction with Bias-Variance Decomposition

- **Timestamp**: `2026-10-19T10:47:00Z`
- **Selected Concept**: `AIMech:EfBvUnifiedErrorFeedbackAndVarianceReductionWithBiasVarianceDecomposition` (*EF-BV Unified Error Feedback and Variance Reduction with Bias-Variance Decomposition*)
- **Record Path**: `data/curated/EfBvUnifiedErrorFeedbackAndVarianceReductionWithBiasVarianceDecomposition.yaml`
- **Primary Source**: Laurent Condat, Kai Yi, Peter Richtarik — *EF-BV: A Unified Theory of Error Feedback and Variance Reduction Mechanisms for Biased and Unbiased Compression in Distributed Optimization* (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2205.04180`).

## Identity & Boundary Resolution

Distinct from standalone DIANA (Mishchenko et al., 2019; restricted to unbiased compressors eta = 0 with nu = 1) and standalone EF21 (Richtarik et al., NeurIPS 2021; restricted to nu = lambda and unable to exploit 1/n parallel variance reduction when omega_av = omega/n < omega). EF-BV (Condat, Yi, & Richtarik, NeurIPS 2022, arXiv:2205.04180) unifies both mechanisms and introduces the C(eta, omega) compressor class including mix-(k, k') and comp-(k, k').

## Constructed Boundary & Regime Verification

```text
[PASS] Round 564 EF-BV verified: r=0.9589, r_av=0.6667, gamma_efbv=0.00632>gamma_ef21=0.00528, err_efbv=2.6352e-02<err_ef21=6.2551e-02
```
