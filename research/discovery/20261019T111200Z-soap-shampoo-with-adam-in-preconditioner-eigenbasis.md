# Discovery Report: Round 589 — SOAP (ShampoO with Adam in the Preconditioner's Eigenbasis)

- **Timestamp**: `2026-10-19T11:12:00Z`
- **Selected Concept**: `AIMech:SoapShampooWithAdamInPreconditionerEigenbasis` (*SOAP (ShampoO with Adam in the Preconditioner's Eigenbasis)*)
- **Record Path**: `data/curated/SoapShampooWithAdamInPreconditionerEigenbasis.yaml`
- **Primary Source**: Nikhil Vyas, Depen Morwani, Rosie Zhao, Mujin Kwun, Itai Shapira, David Brandfonbrener, Lucas Janson, Sham Kakade — *SOAP: Improving and Stabilizing Shampoo using Adam* (`https://dblp.org/rec/conf/iclr/0001MZSBJK25`).

## Identity & Boundary Resolution

Distinct from Shampoo in that SOAP establishes an exact equivalence between idealized Shampoo (with exponent 1/2 and trace scaling) and idealized Adafactor in Shampoo's eigenbasis (Claim 1), and replaces rank-1 Adafactor with full coordinatewise Adam second-moment tracking V updated at every step inside the rotated eigenbasis (Q_L, Q_R), preventing stale-preconditioner degradation when Q_L and Q_R are recomputed infrequently every f steps. Distinct from GaLore in that SOAP maintains exponential moving averages of G G^T and G^T G on both sides of a 2D layer and stores first-moment momentum M in the original parameter space before projecting into the updated eigenbasis.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 589 SOAP verified: claim1_diff=8.88e-16, loss_soap=2.2020e-05<loss_sh=1.0655e-04, space=(10485760<12582912<48234496)
```
