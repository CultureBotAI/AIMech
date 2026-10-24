# Discovery Report: Round 315 — CoSaMP (Compressive Sampling Matching Pursuit)

- **Timestamp**: `2026-10-19T06:22:00Z`
- **Selected Concept**: `AIMech:CoSaMPCompressiveSamplingMatchingPursuit` (*CoSaMP (Compressive Sampling Matching Pursuit)*)
- **Record Path**: `data/curated/CoSaMPCompressiveSamplingMatchingPursuit.yaml`
- **Primary Source**: Deanna Needell, Joel A. Tropp — *CoSaMP: Iterative signal recovery from incomplete and inaccurate samples* (`https://doi.org/10.1016/j.acha.2008.07.002`).

## Identity & Boundary Resolution

Distinct from single-atom Orthogonal Matching Pursuit (AIMech:OrthogonalMatchingPursuitTroppGilbertSignalRecovery), projection-free Iterative Hard Thresholding (AIMech:IterativeHardThresholdingForCompressedSensing), and Subspace Pursuit (which identifies s rather than 2s proxy coordinates and re-projects after pruning). Specifically captures the Needell-Tropp (2009) five-step CoSaMP iteration (Algorithm 2.1), its five component lemmas for identification, support merger, least-squares estimation, and pruning (Lemmas 4.2-4.5), its uniform mixed-norm compressible recovery guarantee (Theorem 2.1), and its Richardson/conjugate-gradient fast least-squares complexity analysis (Section 5, Lemma 5.1 and Theorem 5.2).

## Constructed Boundary & Regime Verification

```text
{"concept": "CoSaMPCompressiveSamplingMatchingPursuit", "exact_recovery_iterations": 1, "noiseless_final_err": 6.280369834735101e-16, "noisy_compressible_err": 0.058743, "richardson_3step_ls_err": 2.11495, "status": "VERIFIED", "unrecoverable_energy_nu": 0.125467}
```
