# Discovery Report: Round 409 — FetchSGD (Count-Sketch Gradient Compression with Server Momentum and Error Accumulation)

- **Timestamp**: `2026-10-19T08:12:00Z`
- **Selected Concept**: `AIMech:FetchSgdCountSketchGradientCompressionWithServerMomentumAndErrorAccumulation` (*FetchSGD (Count-Sketch Gradient Compression with Server Momentum and Error Accumulation)*)
- **Record Path**: `data/curated/FetchSgdCountSketchGradientCompressionWithServerMomentumAndErrorAccumulation.yaml`
- **Primary Source**: Daniel Rothchild, Ashwinee Panda, Enayat Ullah, Nikita Ivkin, Ion Stoica, Vladimir Braverman, Joseph Gonzalez, Raman Arora — *FetchSGD: Communication-Efficient Federated Learning with Sketching* (`https://proceedings.mlr.press/v119/rothchild20a.html`).

## Identity & Boundary Resolution

Distinct from client-stateful error-feedback compression methods such as Sparsified SGD with Error Memory (AIMech:SparsifiedSgdWithErrorMemoryForKContractiveGradientCompression), PowerSGD (AIMech:PowerSgdLowRankGradientCompressionWithErrorFeedback), and EF21 (AIMech:Ef21MarkovCompressorErrorFeedbackForHeterogeneousNonconvexOptimization), which apply a non-linear biased compressor on each client and therefore must store per-client error accumulation vectors that are never re-introduced when federated clients participate only once, and from multi-step local update methods such as FedAvg and MIME (AIMech:MimeMimickingCentralizedStochasticAlgorithmsInFederatedLearning, which transmit uncompressed full-dimensional parameter vectors).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 409 FetchSGD (Rothchild et al. 2020): lin_err=1.78e-15, virt_seq_err=1.78e-15, err_fetch=2.4702e-15<<err_local_topk=6.0000
```
