# Discovery Report: Round 542 — Entangled Polynomial Codes for Straggler-Resilient Distributed Matrix Multiplication

- **Timestamp**: `2026-10-19T10:25:00Z`
- **Selected Concept**: `AIMech:EntangledPolynomialCodesForStragglerResilientDistributedMatrixMultiplication` (*Entangled Polynomial Codes for Straggler-Resilient Distributed Matrix Multiplication*)
- **Record Path**: `data/curated/EntangledPolynomialCodesForStragglerResilientDistributedMatrixMultiplication.yaml`
- **Primary Source**: Qian Yu, Mohammad Ali Maddah-Ali, A. Salman Avestimehr — *Straggler Mitigation in Distributed Matrix Multiplication: Fundamental Limits and Optimal Coding* (`https://dblp.org/rec/journals/tit/YuMA20`).

## Identity & Boundary Resolution

Distinct from Polynomial Codes (AIMech:PolynomialCodesForStragglerResilientHighDimensionalCodedMatrixMultiplication, which restrict p = 1 and partition input matrices only along their outer dimensions) and from MatDot and PolyDot Codes (AIMech:MatDotAndPolyDotCodesForStragglerResilientCodedMatrixMultiplication, where PolyDot achieves recovery threshold m^2 (2p - 1) for m = n because unaligned inner-dimension cross-terms double the polynomial degree in p): Entangled Polynomial Codes (Yu, Maddah-Ali, & Avestimehr, ISIT 2018 / IEEE TIT 2020) assign exponent strides (alpha, beta, theta) = (1, p, p m) with reversed inner-dimension powers x_i^j and x_i^{p-1-j'} to align all p summands of each C_{k,k'} onto x_i^{p-1 + k p + k' p m}, reducing the recovery threshold by a factor of 2 to p m n + p - 1 and further to 2 R(p, m, n) - 1 via bilinear-complexity tensor decompositions.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 542 Entangled Polynomial Codes verified: K_EPC=14 < K_PolyDot=20 < K_RL=36, max_err=9.94e-12, K_Strassen(k=6)=235297 < K_basic(k=6)=262207
```
