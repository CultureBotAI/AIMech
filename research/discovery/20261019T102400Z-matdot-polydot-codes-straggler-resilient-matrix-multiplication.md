# Discovery Report: Round 541 — MatDot and PolyDot Codes for Straggler-Resilient Coded Matrix Multiplication

- **Timestamp**: `2026-10-19T10:24:00Z`
- **Selected Concept**: `AIMech:MatDotAndPolyDotCodesForStragglerResilientCodedMatrixMultiplication` (*MatDot and PolyDot Codes for Straggler-Resilient Coded Matrix Multiplication*)
- **Record Path**: `data/curated/MatDotAndPolyDotCodesForStragglerResilientCodedMatrixMultiplication.yaml`
- **Primary Source**: Sanghamitra Dutta, Mohammad Fahim, Farzin Haddadpour, Haewon Jeong, Viveck R. Cadambe, Pulkit Grover — *On the Optimal Recovery Threshold of Coded Matrix Multiplication* (`https://dblp.org/rec/journals/tit/DuttaFHJCG20.xml`).

## Identity & Boundary Resolution

Distinct from Polynomial Codes (AIMech:PolynomialCodesForStragglerResilientHighDimensionalCodedMatrixMultiplication, which split A horizontally and B vertically into outer-product blocks requiring recovery threshold m^2 with O(N^2 / m^2) per-worker output communication). Dutta et al. (Allerton 2017 / IEEE Trans. Inf. Theory 2020 / arXiv:1801.10292, Constructions 1-5 & Theorems 1-6, pp. 4-17) introduce four coupled constructions: (1) MatDot Codes (Construction 1, Theorem 1), which encode column-blocks of A as p_A(x) = sum_{i=0}^{m-1} A_i x^i and row-blocks of B as p_B(x) = sum_{j=0}^{m-1} B_j x^{m-1-j} so that AB = sum_{i=0}^{m-1} A_i B_i is the coefficient of x^{m-1} in the degree-(2m-2) product polynomial p_C(x) = p_A(x) p_B(x), achieving recovery threshold k = 2m - 1; (2) Systematic MatDot Codes (Construction 2, Lemma 1, Theorem 2), which encode p_A(x) = sum_{i=1}^m A_{i-1} L_i(x) and p_B(x) = sum_{i=1}^m B_{i-1} L_i(x) using Lagrange basis polynomials L_i(x) so the first m workers output uncoded A_{r-1} B_{r-1} while any 2m - 1 workers suffice for interpolation; (3) PolyDot(m, s, t) Codes (Construction 3, Lemma 2, Theorem 3), which partition A into a t x s block grid and B into an s x t block grid (st = m) to achieve recovery threshold t^2(2s - 1) (improved to t^2 s + s - 1 under generalized substitution x = y^t, z = y^{st}, Table I); and (4) n-Matrix Multiplication Codes (Constructions 4-5, Theorems 4-6).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 541 MatDot & PolyDot verified: K_MatDot(m=3)=5 < K_Poly=9, AB=19, K_PolyDot(4,2,2)=12 bijection=12/12
```
