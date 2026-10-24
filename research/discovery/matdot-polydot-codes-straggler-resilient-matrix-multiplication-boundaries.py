#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 541:
MatDot and PolyDot Codes: On the Optimal Recovery Threshold of Coded Matrix Multiplication
(Dutta, Fahim, Haddadpour, Jeong, Cadambe, & Grover, IEEE TIT 2020 / arXiv:1801.10292).
"""

MOD = 29


def mod_inv(a, p=MOD):
    return pow(a % p, p - 2, p)


def solve_vandermonde(xs, ys_list, p=MOD):
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


def lagrange_basis(xs_sys, idx, x, p=MOD):
    """Equation (6) (p. 8): L_i(x) = prod_{j != i} (x - x_j) / (x_i - x_j) over F_p."""
    num, den = 1, 1
    for j, xj in enumerate(xs_sys):
        if j != idx:
            num = (num * (x - xj)) % p
            den = (den * (xs_sys[idx] - xj)) % p
    return (num * mod_inv(den, p)) % p


def main():
    # 1. Verify Construction 1 & Theorem 1 (MatDot Code recovery threshold 2m - 1 vs m^2):
    # Let m = 3: Polynomial Codes need m^2 = 9 workers, whereas MatDot needs 2m - 1 = 5 workers!
    m = 3
    k_matdot = 2 * m - 1
    k_poly = m * m
    assert k_matdot == 5 < k_poly == 9

    # Column-blocks A_0, A_1, A_2 and row-blocks B_0, B_1, B_2 (represented as scalars in F_29):
    A_cols = [4, 7, 11]
    B_rows = [3, 5, 8]
    true_AB = sum(A_cols[i] * B_rows[i] for i in range(m)) % MOD

    # Encode p_A(x) = sum_{i=0}^{m-1} A_i x^i and p_B(x) = sum_{j=0}^{m-1} B_j x^{m-1-j}
    worker_xs = [1, 2, 3, 4, 5, 6, 7]
    worker_evals = []
    for x in worker_xs:
        pA = sum(A_cols[i] * pow(x, i, MOD) for i in range(m)) % MOD
        pB = sum(B_rows[j] * pow(x, m - 1 - j, MOD) for j in range(m)) % MOD
        worker_evals.append((pA * pB) % MOD)

    # Decode from any 2m - 1 = 5 workers (e.g. [0, 2, 3, 5, 6]): coefficient of x^{m-1} = x^2 is AB
    surv = [0, 2, 3, 5, 6]
    coeffs = solve_vandermonde(
        [worker_xs[i] for i in surv], [worker_evals[i] for i in surv], MOD
    )
    assert coeffs[m - 1] == true_AB, f"Expected {true_AB}, got {coeffs[m - 1]}"

    # 2. Verify Construction 2, Lemma 1 & Theorem 2 (Systematic MatDot Code, pp. 7-8):
    sys_xs = worker_xs[:m]  # [1, 2, 3]
    sys_evals = []
    for x in worker_xs:
        pA_sys = sum(A_cols[i] * lagrange_basis(sys_xs, i, x, MOD) for i in range(m)) % MOD
        pB_sys = sum(B_rows[i] * lagrange_basis(sys_xs, i, x, MOD) for i in range(m)) % MOD
        sys_evals.append((pA_sys * pB_sys) % MOD)

    # Lemma 1: First m workers output uncoded A_{r-1} B_{r-1} directly!
    for r in range(m):
        assert sys_evals[r] == (A_cols[r] * B_rows[r]) % MOD
    assert sum(sys_evals[:m]) % MOD == true_AB

    # Theorem 2: From any 2m - 1 = 5 non-systematic/mixed workers (surv), interpolate p_C(x),
    # evaluate at x_1, ..., x_m, and sum to recover AB
    sys_coeffs = solve_vandermonde(
        [worker_xs[i] for i in surv], [sys_evals[i] for i in surv], MOD
    )
    reconstructed_sys_sum = 0
    for x_s in sys_xs:
        val = sum(sys_coeffs[d] * pow(x_s, d, MOD) for d in range(k_matdot)) % MOD
        reconstructed_sys_sum = (reconstructed_sys_sum + val) % MOD
    assert reconstructed_sys_sum == true_AB

    # 3. Verify Construction 3, Lemma 2 & Theorem 3 (PolyDot(m=4, s=2, t=2) Code, pp. 9-11):
    s, t = 2, 2
    k_polydot = (t ** 2) * (2 * s - 1)
    assert k_polydot == 12  # Strictly between MatDot (2m-1 = 7) and Polynomial (m^2 = 16)

    # Verify Lemma 2 bijection: f(alpha, beta, gamma) = alpha + t*beta + t*(2s-1)*gamma
    # maps {0..t-1} x {0..2s-2} x {0..t-1} bijectively onto {0..t^2(2s-1)-1}
    image = {
        alpha + t * beta + t * (2 * s - 1) * gamma
        for alpha in range(t)
        for beta in range(2 * s - 1)
        for gamma in range(t)
    }
    assert image == set(range(k_polydot))

    # Verify Example 5 (p. 9): recover all 4 block products C_{i,l} = sum_{k=0}^1 A_{i,k} B_{k,l}
    # from the coefficients of x^{i + t(s-1) + t(2s-1)l} = x^{i + 2 + 6l} in degree-11 polynomial
    A_grid = [[2, 3], [5, 7]]
    B_grid = [[11, 13], [17, 19]]
    poly_xs = list(range(1, 13))
    poly_evals = []
    for x in poly_xs:
        # p_A(x) = A_{0,0} + A_{1,0} x + A_{0,1} x^2 + A_{1,1} x^3 (since y = x^t = x^2)
        pA_pd = (
            A_grid[0][0]
            + A_grid[1][0] * x
            + A_grid[0][1] * pow(x, 2, MOD)
            + A_grid[1][1] * pow(x, 3, MOD)
        ) % MOD
        # p_B(x) = B_{0,0} x^2 + B_{1,0} + B_{0,1} x^8 + B_{1,1} x^6 (since y = x^2, z = x^{t(2s-1)} = x^6)
        pB_pd = (
            B_grid[0][0] * pow(x, 2, MOD)
            + B_grid[1][0]
            + B_grid[0][1] * pow(x, 8, MOD)
            + B_grid[1][1] * pow(x, 6, MOD)
        ) % MOD
        poly_evals.append((pA_pd * pB_pd) % MOD)

    pd_coeffs = solve_vandermonde(poly_xs, poly_evals, MOD)
    for i_row in range(t):
        for l_col in range(t):
            true_blk = sum(A_grid[i_row][k] * B_grid[k][l_col] for k in range(s)) % MOD
            deg_idx = i_row + t * (s - 1) + t * (2 * s - 1) * l_col  # i + 2 + 6*l
            assert pd_coeffs[deg_idx] == true_blk

    print(
        f"[PASS] Round 541 MatDot & PolyDot verified: K_MatDot(m=3)={k_matdot} < K_Poly={k_poly}, "
        f"AB={true_AB}, K_PolyDot(4,2,2)={k_polydot} bijection=12/12"
    )


if __name__ == "__main__":
    main()
