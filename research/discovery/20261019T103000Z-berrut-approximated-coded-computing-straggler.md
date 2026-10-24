# Discovery Report: Round 547 — Berrut Approximated Coded Computing for Straggler-Resilient Non-Polynomial Distributed Computation

- **Timestamp**: `2026-10-19T10:30:00Z`
- **Selected Concept**: `AIMech:BerrutApproximatedCodedComputingForStragglerResilientNonPolynomialDistributedComputation` (*Berrut Approximated Coded Computing for Straggler-Resilient Non-Polynomial Distributed Computation*)
- **Record Path**: `data/curated/BerrutApproximatedCodedComputingForStragglerResilientNonPolynomialDistributedComputation.yaml`
- **Primary Source**: Tayyebeh Jahani-Nezhad, Mohammad Ali Maddah-Ali — *Berrut Approximated Coded Computing: Straggler Resistance Beyond Polynomial Computing* (`https://dblp.org/rec/journals/pami/Jahani-NezhadM23`).

## Identity & Boundary Resolution

Distinct from Lagrange Coded Computing (AIMech:LagrangeCodedComputingForResilientSecureAndPrivateDistributedLearning, which is restricted to multivariate polynomials of degree deg(f), requires a hard recovery threshold of (K - 1) deg(f) + 1 workers, and suffers exponential Vandermonde ill-conditioning over R): Berrut Approximated Coded Computing (BACC, Jahani-Nezhad & Maddah-Ali, IEEE TPAMI 2023) replaces polynomial interpolation with Berrut's alternating-sign barycentric rational interpolant over first- and second-kind Chebyshev nodes, enabling straggler-resilient approximate evaluation of arbitrary non-polynomial functions (such as deep neural network gradients) from any number of surviving workers with a logarithmically bounded Lebesgue constant.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 547 BACC verified: rel_err(s=2)=0.0000 < rel_err(s=6)=0.0119 < rel_err(s=12)=0.0138, emp_Lebesgue=5.99 <= theo_bound=4607.9
```
