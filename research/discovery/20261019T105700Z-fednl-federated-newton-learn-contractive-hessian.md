# Discovery Report: Round 574 — FedNL (Federated Newton Learn)

- **Timestamp**: `2026-10-19T10:57:00Z`
- **Selected Concept**: `AIMech:FedNlFederatedNewtonLearnWithCompressedHessianLearning` (*FedNL (Federated Newton Learn)*)
- **Record Path**: `data/curated/FedNlFederatedNewtonLearnWithCompressedHessianLearning.yaml`
- **Primary Source**: Mher Safaryan, Rustem Islamov, Xun Qian, Peter Richtarik — *FedNL: Making Newton-Type Methods Applicable to Federated Learning* (`https://proceedings.mlr.press/v162/safaryan22a.html`).

## Identity & Boundary Resolution

Distinct from Newton Learn (NL1/NL2, Islamov et al., 2021), which is restricted to generalized linear models f_i(x) = (1/m) sum_{j=1}^m phi_{ij}(a_{ij}^T x), requires transmitting private training vectors a_{ij} to the server, only supports unbiased compressors, and has local convergence dependent on the number of data points m. Also distinct from first-order compressed federated methods such as DIANA (Round 389) and ADIANA (Round 390), whose rates depend on the condition number kappa = L/mu.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 574 FedNL verified: delta=0.25, H_err=1.0803e-01->2.5639e-34, fednl_ratio=0.1232->7.4590e-08 < n0_ratio=5.1756e-03, err_fednl=0.000e+00
```
