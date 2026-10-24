# Discovery Report: Round 390 — ADIANA Accelerated Distributed Nesterov Gradient Descent with Compression

- **Timestamp**: `2026-10-19T07:53:00Z`
- **Selected Concept**: `AIMech:AdianaAcceleratedDistributedNesterovGradientDescentWithCompression` (*ADIANA Accelerated Distributed Nesterov Gradient Descent with Compression*)
- **Record Path**: `data/curated/AdianaAcceleratedDistributedNesterovGradientDescentWithCompression.yaml`
- **Primary Source**: Zhize Li, Dmitry Kovalev, Xun Qian, Peter Richtárik — *Acceleration for Compressed Gradient Descent in Distributed and Federated Optimization* (`https://proceedings.mlr.press/v119/li20g.html`).

## Identity & Boundary Resolution

Distinct from non-accelerated DIANA (AIMech:DianaDistributedLearningWithCompressedGradientDifferences, which scales linearly with condition number kappa = L/mu rather than sqrt(L/mu) and updates shifts h_i^k at the current iterate x^k rather than a loopless reference w^k), from Katyusha (AIMech:KatyushaDirectNegativeMomentumAccelerationForStochasticVarianceReducedOptimization, which accelerates centralized finite-sum SVRG without communication compression), and from Linear Coupling AGM (AIMech:LinearCouplingOfGradientAndMirrorDescentForFirstOrderOptimization, which operates on uncompressed oracles). No pinned AIO class covers ADIANA or Nesterov-accelerated compressed distributed optimization.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 390 ADIANA (Li et al. 2020): Lemma2_var=18911.09<=30055.34, Lemma3_H=25649.11~=25588.34, err_adiana=1.73e-06 << err_diana=1.23e-02
```
