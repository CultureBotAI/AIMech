# Discovery Report: Round 540 — Polynomial Codes for Straggler-Resilient High-Dimensional Coded Matrix Multiplication

- **Timestamp**: `2026-10-19T10:23:00Z`
- **Selected Concept**: `AIMech:PolynomialCodesForStragglerResilientHighDimensionalCodedMatrixMultiplication` (*Polynomial Codes for Straggler-Resilient High-Dimensional Coded Matrix Multiplication*)
- **Record Path**: `data/curated/PolynomialCodesForStragglerResilientHighDimensionalCodedMatrixMultiplication.yaml`
- **Primary Source**: Qian Yu, Mohammad Ali Maddah-Ali, A. Salman Avestimehr — *Polynomial Codes: an Optimal Design for High-Dimensional Coded Matrix Multiplication* (`https://dblp.org/rec/conf/nips/YuMA17.xml`).

## Identity & Boundary Resolution

Distinct from Lagrange Coded Computing (AIMech:LagrangeCodedComputingForResilientSecureAndPrivateDistributedLearning, which encodes a dataset of K separate inputs via Lagrange interpolation polynomials to evaluate a single multivariate polynomial f(X_i) on each batch), from Gradient Coding (AIMech:GradientCodingForStragglerResilientDistributedOptimization, which encodes partial loss gradients over replicated data blocks), and from MatDot and PolyDot Codes (AIMech:MatDotAndPolyDotCodesForStragglerResilientCodedMatrixMultiplication, which split A into column blocks and B into row blocks to compute inner-product sums sum_i A_i B_i with recovery threshold 2m - 1 at higher worker-to-master communication cost). Polynomial Codes (Yu, Maddah-Ali, & Avestimehr, NeurIPS 2017, pp. 4403-4413 / arXiv:1705.10464, Section II-IV, Definition 2, Equations 14-18, Theorems 1-5) achieve the information-theoretically minimum recovery threshold K_{poly} = mn = Theta(1) independent of N under minimum worker-to-master communication load L* = r t log_2 q (Theorems 1-3), and extend via the (alpha, beta) = (1, 1) code (Equations 31-33, Theorem 4) to distributed convolution c = a * b with recovery threshold K_{conv-poly} = m + n - 1.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 540 Polynomial Codes verified: K_poly(400)=100 < K_prod=280 < K_1D=370, decoded_C=[4, 1, 16, 4], K_conv=5 decoded_conv=[6, 5, 1, 7, 8]
```
