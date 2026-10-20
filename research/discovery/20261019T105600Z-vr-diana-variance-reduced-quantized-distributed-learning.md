# Discovery Report: Round 573 — VR-DIANA and SVRG-DIANA (Variance-Reduced Distributed Learning with Gradient Quantization)

- **Timestamp**: `2026-10-19T10:56:00Z`
- **Selected Concept**: `AIMech:VrDianaAndSvrgDianaVarianceReducedQuantizedDistributedOptimization` (*VR-DIANA and SVRG-DIANA (Variance-Reduced Distributed Learning with Gradient Quantization)*)
- **Record Path**: `data/curated/VrDianaAndSvrgDianaVarianceReducedQuantizedDistributedOptimization.yaml`
- **Primary Source**: Samuel Horvath, Dmitry Kovalev, Konstantin Mishchenko, Peter Richtarik, Sebastian U. Stich — *Stochastic Distributed Learning with Gradient Quantization and Variance Reduction* (`https://dblp.org/search/publ/api?q=Stochastic+Distributed+Learning+with+Gradient+Quantization+and+Variance+Reduction+Horvath&format=json`).

## Identity & Boundary Resolution

Distinct from baseline DIANA (Mishchenko et al., 2019; Round 389), which does not incorporate local finite-sum variance reduction and only converges to an O(sigma^2 / (mu^2 * n)) neighborhood under stochastic gradients. Also distinct from ADIANA (Li et al., 2020; Round 390), which accelerates full-batch or L-SVRG DIANA via Nesterov momentum, and from QSVRG (Alistarh et al., 2017; Round 378), which requires broadcasting exact uncompressed full gradients at the start of every epoch.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 573 VR-DIANA verified: omega=4.0, err_vr=1.047e-31 << err_diana=7.186e-02, H_K=1.914e-30
```
