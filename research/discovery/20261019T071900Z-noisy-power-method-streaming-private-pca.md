# Discovery Report: Round 356 — Noisy Power Method for Perturbed Subspace Iteration, Streaming PCA, and Differentially Private Spectral Analysis

- **Timestamp**: `2026-10-19T07:19:00Z`
- **Selected Concept**: `AIMech:NoisyPowerMethodForStreamingAndDifferentiallyPrivatePCA` (*Noisy Power Method for Perturbed Subspace Iteration, Streaming PCA, and Differentially Private Spectral Analysis*)
- **Record Path**: `data/curated/NoisyPowerMethodForStreamingAndDifferentiallyPrivatePCA.yaml`
- **Primary Source**: Moritz Hardt, Eric Price — *The Noisy Power Method: A Meta Algorithm with Applications* (`https://dblp.org/rec/conf/nips/HardtP14.xml`).

## Identity & Boundary Resolution

Distinct from generic PrincipalComponentAnalysis (AIO:PrincipalComponentAnalysis) and DimensionalityReduction (AIO:DimensionalityReduction), which do not model adversarial or stochastic per-step perturbations G_ell in QR subspace iteration or differential privacy. Distinct from AIMech:RandomizedBlockKrylovMethodsForApproximateSingularValueDecomposition (Round 355), which analyzes exact noise-free block Krylov iterations using Chebyshev polynomials rather than perturbed block power iterations under adaptive noise. Also distinct from AIMech:ShiftAndInvertPreconditioningForFasterEigenvectorComputation (Round 354), which pre-inverts (lambda I - A) via SVRG rather than analyzing principal-angle tangent contraction and Gram-Schmidt sign-symmetry coherence preservation.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 356 Noisy Power Method (Hardt & Price 2014): tan_0=2.4717->tan_L=0.00618<=eps=0.080, gs_comm_err=0.00e+00, lemma412_err=0.00e+00
```
