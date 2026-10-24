#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 540:
Polynomial Codes: an Optimal Design for High-Dimensional Coded Matrix Multiplication
(Yu, Maddah-Ali, & Avestimehr, NeurIPS 2017, pp. 4403-4413 / arXiv:1705.10464).
"""

import math

MOD = 17


def mod_inv(a, p=MOD):
    return pow(a % p, p - 2, p)


def solve_vandermonde(xs, ys_list, p=MOD):
    """Given k distinct evaluation points xs and k scalar values ys_list = [h(xs[0]), ..., h(xs[k-1])],
    recover the k coefficients [c_0, c_1, ..., c_{k-1}] of h(x) = sum_{d=0}^{k-1} c_d x^d over F_p
    via Gaussian elimination on the Vandermonde system.
    """
    k = len(xs)
    mat = [
        [(pow(xs[r], col, p)) for col in range(k)] + [ys_list[r] % p]
        for r in range(k)
    ]
    for col in range(k):
        piv = col
        while piv < k and mat[piv][col] % p == 0:
            piv += 1
        assert piv < k, "Singular Vandermonde matrix"
        mat[col], mat[piv] = mat[piv], mat[col]
        inv_p = mod_inv(mat[col][col], p)
        for j in range(col, k + 1):
            mat[col][j] = (mat[col][j] * inv_p) % p
        for r in range(k):
            if r != col and mat[r][col] != 0:
                factor = mat[r][col]
                for j in range(col, k + 1):
                    mat[r][j] = (mat[r][j] - factor * mat[col][j]) % p
    return [mat[i][k] % p for i in range(k)]


def main():
    # 1. Verify Theorem 1 & Equations (1)-(3): Recovery threshold comparison
    # For N = 100 workers, m = 10, n = 10:
    N, m, n = 100, 10, 10
    k_1d_mds = N - (N // n) + m
    k_product = 2 * (m - 1) * int(math.isqrt(N)) - (m - 1) ** 2 + 1
    k_poly = m * n
    assert k_poly == 100 and k_1d_mds == 100
    # For N = 400 workers, m = 10, n = 10 (Figure 3, p. 4):
    N2 = 400
    k_1d_mds_400 = N2 - (N2 // n) + m  # 370
    k_product_400 = 2 * (m - 1) * int(math.isqrt(N2)) - (m - 1) ** 2 + 1  # 280
    k_poly_400 = m * n  # 100 (independent of N!)
    assert k_poly_400 == 100 < k_product_400 == 280 < k_1d_mds_400 == 370

    # 2. Verify Section III-A & III-B ((1, m)-Polynomial Code for C = A^T B over F_17):
    # m = 2, n = 2 (k_poly = mn = 4), N = 6 workers with x_i = i + 1 in F_17.
    # Let A_0, A_1, B_0, B_1 be scalars (1x1 blocks) in F_17:
    A_blocks = [3, 5]
    B_blocks = [7, 11]
    true_C = [
        (A_blocks[0] * B_blocks[0]) % MOD,  # j=0, k=0 -> coeff of x^0
        (A_blocks[1] * B_blocks[0]) % MOD,  # j=1, k=0 -> coeff of x^1
        (A_blocks[0] * B_blocks[1]) % MOD,  # j=0, k=1 -> coeff of x^2
        (A_blocks[1] * B_blocks[1]) % MOD,  # j=1, k=1 -> coeff of x^3
    ]

    xs_all = [1, 2, 3, 4, 5, 6]
    worker_prods = []
    for x in xs_all:
        # Equation (17): tilde_A_i = sum_{j=0}^{m-1} A_j x^j, tilde_B_i = sum_{k=0}^{n-1} B_k x^{k m}
        tilde_A = sum(A_blocks[j] * pow(x, j, MOD) for j in range(2)) % MOD
        tilde_B = sum(B_blocks[k] * pow(x, 2 * k, MOD) for k in range(2)) % MOD
        worker_prods.append((tilde_A * tilde_B) % MOD)

    # Pick any 4 non-straggling workers (e.g. workers at indices [1, 3, 4, 5])
    surv_idx = [1, 3, 4, 5]
    coeffs = solve_vandermonde(
        [xs_all[i] for i in surv_idx], [worker_prods[i] for i in surv_idx], MOD
    )
    assert coeffs == true_C, f"Expected {true_C}, got {coeffs}"

    # 3. Verify Section IV & Theorem 4 ((1, 1)-Polynomial Code for Distributed Convolution c = a * b):
    # For m = 3, n = 3, naive Polynomial Code needs m*n = 9 workers, while (1, 1)-convolution code
    # needs only K_{conv-poly} = m + n - 1 = 5 workers (Equations 31-33, p. 10)!
    a_vec = [2, 4, 6]
    b_vec = [3, 5, 7]
    m_c, n_c = 3, 3
    k_conv = m_c + n_c - 1
    assert k_conv == 5

    # True discrete convolution c_j = sum_{k} a_{j-k} * b_k for j = 0..4
    true_conv = [0] * k_conv
    for j in range(m_c):
        for k in range(n_c):
            true_conv[j + k] = (true_conv[j + k] + a_vec[j] * b_vec[k]) % MOD

    conv_xs = [1, 2, 3, 4, 5]
    conv_evals = []
    for x in conv_xs:
        ta = sum(a_vec[j] * pow(x, j, MOD) for j in range(m_c)) % MOD
        tb = sum(b_vec[k] * pow(x, k, MOD) for k in range(n_c)) % MOD
        conv_evals.append((ta * tb) % MOD)

    recovered_conv = solve_vandermonde(conv_xs, conv_evals, MOD)
    assert recovered_conv == true_conv, f"Expected {true_conv}, got {recovered_conv}"

    print(
        f"[PASS] Round 540 Polynomial Codes verified: K_poly(400)={k_poly_400} < K_prod={k_product_400} "
        f"< K_1D={k_1d_mds_400}, decoded_C={coeffs}, K_conv={k_conv} decoded_conv={recovered_conv}"
    )


if __name__ == "__main__":
    main()
