# Discovery Report: Round 578 — Basis Learn (BL1, BL2, and BL3)

- **Timestamp**: `2026-10-19T11:01:00Z`
- **Selected Concept**: `AIMech:BasisLearnCustomMatrixBasisSecondOrderFederatedOptimization` (*Basis Learn (BL1, BL2, and BL3)*)
- **Record Path**: `data/curated/BasisLearnCustomMatrixBasisSecondOrderFederatedOptimization.yaml`
- **Primary Source**: Xun Qian, Rustem Islamov, Mher Safaryan, Peter Richtarik — *Basis Matters: Better Communication-Efficient Second Order Methods for Federated Learning* (`https://proceedings.mlr.press/v151/qian22a.html`).

## Identity & Boundary Resolution

Distinct from standard-basis FedNL (which compresses dense d x d Hessian differences directly in the canonical matrix basis E_{jl} = e_j e_l^T) and from NewtonLearn (which requires revealing raw local data vectors a_{ij} to the server to send m scalar coefficients). Basis Learn sends only the r subspace basis vectors {v_{it}}_{t=1}^r once before training and learns the sparse r x r basis coefficient matrix L_i^k under bidirectional compression and partial participation.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 578 BasisLearn (BL1) verified: r^2=4<<d^2=25, err_bl1=3.469e-17, hess_err_bl1=1.328e-33 << hess_err_fnl=2.687e-15
```
