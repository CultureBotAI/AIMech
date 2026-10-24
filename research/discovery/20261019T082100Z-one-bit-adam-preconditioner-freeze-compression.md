# Discovery Report: Round 418 — 1-bit Adam (Two-Stage Preconditioner-Frozen Error-Compensated Adam)

- **Timestamp**: `2026-10-19T08:21:00Z`
- **Selected Concept**: `AIMech:OneBitAdamPreconditionerFreezeCommunicationCompression` (*1-bit Adam (Two-Stage Preconditioner-Frozen Error-Compensated Adam)*)
- **Record Path**: `data/curated/OneBitAdamPreconditionerFreezeCommunicationCompression.yaml`
- **Primary Source**: Hanlin Tang, Shaoduo Gan, Ammar Ahmad Awan, Samyam Rajbhandari, Conglong Li, Xiangru Lian, Ji Liu, Ce Zhang, Yuxiong He — *1-bit Adam: Communication Efficient Large-Scale Training with Adam's Convergence Speed* (`https://proceedings.mlr.press/v139/tang21a.html`).

## Identity & Boundary Resolution

Distinct from linear error-compensated SGD methods such as DoubleSqueeze (AIMech:DoubleSqueezeDoublePassErrorCompensatedCompression) and Sparsified SGD with Error Memory (AIMech:SparsifiedSgdWithErrorMemoryForKContractiveGradientCompression), which lack adaptive coordinate-wise preconditioning V^{-1}, and from server-adaptive FedOpt (AIMech:FedOptAdaptiveServerOptimizationFedAdagradFedYogiFedAdam), which updates adaptive moments on the server after uncompressed pseudo-gradient aggregation rather than freezing Adam's second moment to restore linear error-feedback cancellation.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 418 1-bit Adam (Tang et al. 2021): unfrozen_non_telescoping_gap=1.8442 > 0, frozen_telescoping_err=7.9e-15 == 0
```
