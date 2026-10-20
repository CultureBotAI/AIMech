# Discovery Report: Round 650 — Improved Variational Online Newton (IVON)

- **Timestamp**: `2026-10-19T12:13:00Z`
- **Selected Concept**: `AIMech:IvonImprovedVariationalOnlineNewtonForLargeDeepNetworks` (*Improved Variational Online Newton (IVON)*)
- **Record Path**: `data/curated/IvonImprovedVariationalOnlineNewtonForLargeDeepNetworks.yaml`
- **Primary Source**: Yuesong Shen, Nico Daheim, Bai Cong, Peter Nickl, Gian Maria Marconi, Clement Bazan, Rio Yokota, Iryna Gurevych, Daniel Cremers, Mohammad Emtiyaz Khan, Thomas Möllenhoff — *Variational Learning is Effective for Large Deep Networks* (`https://dblp.org/rec/conf/icml/ShenDCNMBYGCKM24.html`).

## Identity & Boundary Resolution

Must be distinguished from standard deterministic adaptive optimizers (Adam, AdamW, AdaHessian) which maintain point estimates m without sampling theta ~ N(m, diag(sigma^2)) and therefore neither optimize the variational free energy L(q) = lambda * E_q[ell_bar(theta)] + D_KL(q || p) nor yield posterior weight variances sigma^2 for Bayesian model averaging, weight pruning, or uncertainty calibration. Also distinct from Variational Online Newton (VON, Khan et al., 2018) and Variational Online Gauss-Newton (VOGN, Osawa et al., 2019), which require per-example gradient squares or explicit Hessian-vector products that incur prohibitive memory and runtime overhead on large language models such as GPT-2 and ResNet-50.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 650 IVON boundary and mathematical verification succeeded.
```
