# Discovery Report: Round 363 — Frequent Directions Deterministic Row-Update Matrix Sketching via Singular-Value Shrinkage

- **Timestamp**: `2026-10-19T07:26:00Z`
- **Selected Concept**: `AIMech:FrequentDirectionsDeterministicMatrixSketching` (*Frequent Directions Deterministic Row-Update Matrix Sketching via Singular-Value Shrinkage*)
- **Record Path**: `data/curated/FrequentDirectionsDeterministicMatrixSketching.yaml`
- **Primary Source**: Mina Ghashami, Edo Liberty, Jeff M. Phillips, David P. Woodruff — *Frequent Directions: Simple and Deterministic Matrix Sketching* (`https://api.crossref.org/works/10.1137/15m1009718`).

## Identity & Boundary Resolution

Distinct from AIMech:FrequentDirectionsDeterministicStreamingMatrixSketching (Round 330, Liberty KDD 2013), which established only the flat-spectrum Frobenius covariance error bound ||A^T A - B^T B||_2 <= 2||A||_F^2/ell without rank-k tail residuals or relative-error projection bounds; this record captures Ghashami, Liberty, Phillips, and Woodruff's (2015, 2016) tail-residual relative-error covariance and rank-k projection analysis (||A^T A - B^T B||_2 <= ||A - A_k||_F^2/(ell - k), ||A - pi_B^k(A)||_F^2 <= (ell/(ell - k))||A - A_k||_F^2) and matching Grassmannian/Index space-optimality lower bounds. Also distinct from AIMech:NoisyPowerMethodForStreamingAndDifferentiallyPrivatePCA (Round 356) and AIMech:StreamingPCANearOptimalFiniteSampleOjaAlgorithm (Round 357), which are randomized iterative subspace estimators rather than deterministic Misra-Gries-style singular-value shrinkage sketches.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 363 Frequent Directions (Ghashami et al. 2016): prop1_min=2.87e+00, Delta=12.3685<=14.9785, prop3_err=1.49e-13, merge_err=7.82e-14, adv_cov_fd=4.0000<<inc=32.4000
```
