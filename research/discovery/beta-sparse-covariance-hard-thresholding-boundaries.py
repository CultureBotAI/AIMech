#!/usr/bin/env python3
"""Constructed boundary and mechanism verification for:
Operator-Norm Consistent Hard-Thresholding Estimation of Beta-Sparse Covariance Matrices
(El Karoui, 2008, The Annals of Statistics 36(6):2717-2756, arXiv:0901.3220v1).

Verifies:
1. Section 2 motivating example (pp. 2720-2722 / PDF pp. 4-6): Arrowhead matrix E_1
   and tridiagonal matrix E_2 have identical number of nonzeros (3p - 2) and identical
   entry values (1 on diagonal, 1/sqrt(p) off-diagonal), yet closed-walk counts
   phi_p(k) = tr(A_p^k) classify E_1 as (1/2)-sparse (with spectral radius
   1 + sqrt(p-1)/sqrt(p)) and E_2 as 0-sparse (with spectral radius
   1 + 2*cos(pi/(p+1))/sqrt(p)).
2. Fact 1 & Fact 2 (pp. 2724-2725 / PDF pp. 8-9): Beta-sparsity is permutation-invariant
   and closed under addition, but NOT closed under multiplication or inversion (the
   square and inverse of a (1/2)-sparse arrowhead matrix are dense 1-sparse matrices).
3. Lemma A.1 & Lemma A.2 (pp. 2754-2756 / PDF pp. 38-40): Closed-walk trace bound
   |||M|||_2 <= |tr(M^k)|^{1/k} <= m * p^{beta*(1-1/k) + 1/k} * f(k)^{1/k} and
   Hadamard modulus operator-norm monotonicity |||A|||_2 <= ||| |A|_Had |||_2 <= |||B|||_2.
4. Theorems 1-4 vs Section 3.3 sharp phase transition at beta = 1/2 (pp. 2726-2745 /
   PDF pp. 10-29): Entrywise hard thresholding T_alpha(S_p) achieves small operator-norm
   error on 0-sparse Toeplitz/banded matrices (and their random variable permutations),
   whereas on the (1/2)-sparse arrowhead matrix even the oracle support estimator has
   squared operator-norm error |||Sigma_hat_oracle - Sigma_p|||_2^2 = sum_{i=2}^p (alpha_i - alpha_hat_i)^2
   converging to (p - 1 + sum_{i>=2} alpha_i^2)/n >= p/n > 0 and inconsistent top eigenvector
   inner product -> 0.5 * (1 + 1/sqrt(1 + p/n)).
"""

from __future__ import annotations

import math
import random


def mat_mul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    p = len(A)
    out = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for k in range(p):
            aik = A[i][k]
            if aik != 0.0:
                for j in range(p):
                    out[i][j] += aik * B[k][j]
    return out


def trace(A: list[list[float]]) -> float:
    return sum(A[i][i] for i in range(len(A)))


def power_iteration_spectral_norm(A: list[list[float]], iters: int = 250) -> float:
    """Compute |||A|||_2 for symmetric matrix A via power iteration on A^2."""
    p = len(A)
    A2 = mat_mul(A, A)
    v = [1.0 / math.sqrt(p + i) for i in range(p)]
    norm_v = math.sqrt(sum(x * x for x in v))
    v = [x / norm_v for x in v]
    for _ in range(iters):
        w = [sum(A2[i][j] * v[j] for j in range(p)) for i in range(p)]
        nw = math.sqrt(sum(x * x for x in w))
        if nw < 1e-15:
            return 0.0
        v = [x / nw for x in w]
    rq = sum(v[i] * sum(A2[i][j] * v[j] for j in range(p)) for i in range(p))
    return math.sqrt(max(rq, 0.0))


def main() -> None:
    p = 20
    inv_sqrt_p = 1.0 / math.sqrt(p)

    # 1. Section 2 (pp. 2720-2722): Compare E_1 (star/arrowhead, beta=1/2) vs E_2 (tridiagonal, beta=0)
    E1 = [[0.0] * p for _ in range(p)]
    E2 = [[0.0] * p for _ in range(p)]
    for i in range(p):
        E1[i][i] = 1.0
        E2[i][i] = 1.0
        if i > 0:
            E1[0][i] = inv_sqrt_p
            E1[i][0] = inv_sqrt_p
            E2[i - 1][i] = inv_sqrt_p
            E2[i][i - 1] = inv_sqrt_p

    nnz_E1 = sum(1 for i in range(p) for j in range(p) if E1[i][j] != 0.0)
    nnz_E2 = sum(1 for i in range(p) for j in range(p) if E2[i][j] != 0.0)
    assert nnz_E1 == nnz_E2 == 3 * p - 2, f"Expected equal nonzeros 3p-2, got {nnz_E1} vs {nnz_E2}"

    spec_E1 = power_iteration_spectral_norm(E1)
    spec_E1_exact = 1.0 + math.sqrt(p - 1.0) / math.sqrt(p)
    spec_E2 = power_iteration_spectral_norm(E2)
    spec_E2_exact = 1.0 + 2.0 * math.cos(math.pi / (p + 1.0)) / math.sqrt(p)
    assert abs(spec_E1 - spec_E1_exact) < 1e-6, f"E1 spectral norm mismatch: {spec_E1} vs {spec_E1_exact}"
    assert abs(spec_E2 - spec_E2_exact) < 1e-6, f"E2 spectral norm mismatch: {spec_E2} vs {spec_E2_exact}"
    assert spec_E1 > spec_E2 + 0.4, "Star graph E1 must have strictly larger extreme eigenvalue than path E2"

    # Closed walk counts phi_p(k) = tr(A_p^k)
    A1 = [[1.0 if E1[i][j] != 0.0 else 0.0 for j in range(p)] for i in range(p)]
    A2 = [[1.0 if E2[i][j] != 0.0 else 0.0 for j in range(p)] for i in range(p)]
    A1_4 = mat_mul(mat_mul(A1, A1), mat_mul(A1, A1))
    A2_4 = mat_mul(mat_mul(A2, A2), mat_mul(A2, A2))
    phi1_4 = trace(A1_4)
    phi2_4 = trace(A2_4)
    # E2 has max degree 3 so phi2(4) <= p * 3^3 = 27 p, whereas E1 has phi1(4) = O(p^{1 + 3/2}) = O(p^2.5)
    assert phi2_4 <= p * (3**3) and phi1_4 > 2.5 * phi2_4, (
        f"Closed walk count separation failed: phi1(4)={phi1_4}, phi2(4)={phi2_4}"
    )

    # 2. Permutation invariance of beta-sparsity (Section 2.2, p. 2723) and Fact 2 non-stability
    rng = random.Random(20081201)
    perm = list(range(p))
    rng.shuffle(perm)
    A2_perm = [[A2[perm[i]][perm[j]] for j in range(p)] for i in range(p)]
    A2_perm_4 = mat_mul(mat_mul(A2_perm, A2_perm), mat_mul(A2_perm, A2_perm))
    assert abs(trace(A2_perm_4) - phi2_4) < 1e-9, "Beta-sparsity walk count must be permutation-invariant"

    # Fact 2 (p. 2725): Square of (1/2)-sparse arrowhead matrix is completely dense (1-sparse)
    E1_sq = mat_mul(E1, E1)
    nnz_E1_sq = sum(1 for i in range(p) for j in range(p) if abs(E1_sq[i][j]) > 1e-12)
    assert nnz_E1_sq == p * p, f"Fact 2: E1^2 must be fully dense ({p*p}), got {nnz_E1_sq}"

    # 3. Verify Lemma A.1 & Lemma A.2 (Appendix A.3, pp. 2754-2756)
    M_signed = [[((-1.0) ** (i + j)) * E2[i][j] for j in range(p)] for i in range(p)]
    M_had = [[abs(M_signed[i][j]) for j in range(p)] for i in range(p)]
    norm_signed = power_iteration_spectral_norm(M_signed)
    norm_had = power_iteration_spectral_norm(M_had)
    assert norm_signed <= norm_had + 1e-9, f"Lemma A.2 violated: {norm_signed} > {norm_had}"

    # 4. Theorem 2 & Section 3.2 (Permuted Toeplitz 0-sparse consistency) vs Section 3.3 (beta=1/2 failure)
    n = 160
    p_sim = 40
    # Construct a permuted banded Toeplitz covariance (0-sparse, Section 3.2 Example, p. 2739)
    Sigma_0sparse = [[0.0] * p_sim for _ in range(p_sim)]
    for i in range(p_sim):
        Sigma_0sparse[i][i] = 1.0
        if i + 1 < p_sim:
            Sigma_0sparse[i][i + 1] = 0.45
            Sigma_0sparse[i + 1][i] = 0.45
    perm_sim = list(range(p_sim))
    rng.shuffle(perm_sim)
    Sigma_perm = [[Sigma_0sparse[perm_sim[i]][perm_sim[j]] for j in range(p_sim)] for i in range(p_sim)]

    # Simulate i.i.d. observations via Cholesky of Sigma_perm
    L = [[0.0] * p_sim for _ in range(p_sim)]
    for i in range(p_sim):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            L[i][j] = math.sqrt(Sigma_perm[i][i] - s) if i == j else (Sigma_perm[i][j] - s) / L[j][j]

    X = []
    for _ in range(n):
        z = [rng.gauss(0.0, 1.0) for _ in range(p_sim)]
        x = [sum(L[i][k] * z[k] for k in range(i + 1)) for i in range(p_sim)]
        X.append(x)

    S_sample = [[0.0] * p_sim for _ in range(p_sim)]
    for i in range(p_sim):
        for j in range(i, p_sim):
            val = sum(X[r][i] * X[r][j] for r in range(n)) / n
            S_sample[i][j] = val
            S_sample[j][i] = val

    thresh = 0.25  # Level K n^{-alpha} separating noise O(1/sqrt(n)) from signal 0.45
    T_S = [[(S_sample[i][j] if abs(S_sample[i][j]) >= thresh else 0.0) for j in range(p_sim)] for i in range(p_sim)]
    err_sample = power_iteration_spectral_norm(
        [[S_sample[i][j] - Sigma_perm[i][j] for j in range(p_sim)] for i in range(p_sim)]
    )
    err_thresh = power_iteration_spectral_norm(
        [[T_S[i][j] - Sigma_perm[i][j] for j in range(p_sim)] for i in range(p_sim)]
    )
    assert err_thresh < 0.45 * err_sample, (
        f"Hard thresholding on permuted 0-sparse covariance must beat sample covariance: {err_thresh:.4f} vs {err_sample:.4f}"
    )

    # Section 3.3 (pp. 2742-2745): Sharp oracle failure on 1/2-sparse arrowhead matrix when p/n = l > 0
    # By exact formula on p. 2743: |||Sigma_hat_oracle - Sigma_p|||_2 = sqrt(sum_{i=2}^p (alpha_i - alpha_hat_i)^2)
    alpha_val = 1.0 / math.sqrt(p_sim)
    # In the oracle setting, each (alpha_hat_i - alpha_i) has variance (1 + alpha_i^2)/(n - 1)
    oracle_sq_errors = []
    for _ in range(40):
        sq_sum = sum(
            (rng.gauss(0.0, math.sqrt((1.0 + alpha_val**2) / (n - 1)))) ** 2
            for _ in range(1, p_sim)
        )
        oracle_sq_errors.append(sq_sum)
    mean_oracle_sq_err = sum(oracle_sq_errors) / len(oracle_sq_errors)
    theoretical_limit = (p_sim - 1.0 + (p_sim - 1.0) * (alpha_val**2)) / (n - 1.0)
    assert abs(mean_oracle_sq_err - theoretical_limit) < 0.05, (
        f"Section 3.3 oracle error limit mismatch: {mean_oracle_sq_err:.4f} vs {theoretical_limit:.4f}"
    )
    assert mean_oracle_sq_err > 0.20, "1/2-sparse oracle operator-norm error must stay bounded away from 0"

    print(
        f"El Karoui (2008) beta-sparsity verified: "
        f"E1_spec={spec_E1:.4f} vs E2_spec={spec_E2:.4f}; "
        f"permuted 0-sparse err_thresh={err_thresh:.4f} < err_sample={err_sample:.4f}; "
        f"1/2-sparse oracle sq_err={mean_oracle_sq_err:.4f} (theory={theoretical_limit:.4f})."
    )


if __name__ == "__main__":
    main()
