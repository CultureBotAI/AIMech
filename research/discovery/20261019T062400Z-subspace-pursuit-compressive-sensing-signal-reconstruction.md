# Discovery Report: Round 316 — Subspace Pursuit for Compressive Sensing Signal Reconstruction

- **Timestamp**: `2026-10-19T06:24:00Z`
- **Selected Concept**: `AIMech:SubspacePursuitForCompressiveSensingSignalReconstruction` (*Subspace Pursuit for Compressive Sensing Signal Reconstruction*)
- **Record Path**: `data/curated/SubspacePursuitForCompressiveSensingSignalReconstruction.yaml`
- **Primary Source**: Wei Dai, Olgica Milenkovic — *Subspace Pursuit for Compressive Sensing Signal Reconstruction* (`https://doi.org/10.1109/TIT.2009.2016006`).

## Identity & Boundary Resolution

Distinct from CoSaMP (AIMech:CoSaMPCompressiveSamplingMatchingPursuit, which selects 2K atoms per step, operates on 3K supports under delta_{4K}, and omits the post-pruning subspace projection), Orthogonal Matching Pursuit (AIMech:OrthogonalMatchingPursuitTroppGilbertSignalRecovery), and Iterative Hard Thresholding (AIMech:IterativeHardThresholdingForCompressedSensing). Specifically captures the Dai-Milenkovic (2009) Subspace Pursuit algorithm (Algorithm 1), its post-pruning orthogonal residue property Phi_{T^l}^* y_r^l = 0 (Lemma 2), its 3K-RIP geometric contraction under delta_{3K} < 0.205 (Theorems 1-2) and noisy/compressible stability under delta_{3K} < 0.083 (Theorem 9).

## Constructed Boundary & Regime Verification

```text
{"concept": "SubspacePursuitForCompressiveSensingSignalReconstruction", "init_support_overlap": 3, "lemma2_residue_orthogonality_err": 2.307724324135396e-16, "noiseless_final_x_err": 5.20740757162067e-16, "noisy_final_x_err": 0.009708, "residual_norm_trajectory": [0.949911, 0.0], "status": "VERIFIED"}
```
