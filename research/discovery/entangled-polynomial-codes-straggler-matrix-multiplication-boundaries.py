"""Constructed boundary verification for Round 542: Entangled Polynomial Codes (Yu, Maddah-Ali, & Avestimehr, IEEE TIT 2020)."""

from __future__ import annotations

import math


def solve_linear_system(mat: list[list[float]], rhs: list[float]) -> list[float]:
    n = len(rhs)
    a = [row[:] + [rhs[i]] for i, row in enumerate(mat)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(a[r][col]))
        a[col], a[piv] = a[piv], a[col]
        div = a[col][col]
        for j in range(col, n + 1):
            a[col][j] /= div
        for r in range(n):
            if r != col and a[r][col] != 0.0:
                factor = a[r][col]
                for j in range(col, n + 1):
                    a[r][j] -= factor * a[col][j]
    return [a[i][n] for i in range(n)]


def main() -> None:
    # Part 1: Verify recovery threshold comparison (Theorem 1, Remark 1-2, p. 3-4)
    # p = 3, m = 2, n = 2
    p, m, n = 3, 2, 2
    k_epc = p * m * n + p - 1  # 14
    k_polydot = m * n * (2 * p - 1)  # 20
    k_random_linear = (p ** 2) * m * n  # 36
    assert k_epc == 14
    assert k_epc < k_polydot < k_random_linear

    # Verify linear-code converse bound when m=1 or n=1 (Theorem 2 & Lemma 1, Eq. 12, 30)
    p1, m1, n1 = 3, 2, 1
    k_epc_m1 = p1 * m1 * n1 + p1 - 1  # 8
    k_converse_m1 = p1 * m1 + p1 * n1 - 1  # 6 + 3 - 1 = 8
    assert k_epc_m1 == k_converse_m1 == 8

    # Part 2: Exact encoding and decoding of Entangled Polynomial Code (Definition 4, Eq. 28-29)
    # Subblocks A_{j,k}, B_{j,k'} are scalars (1x1 blocks) for clarity
    A = [
        [1.5, -0.5],  # j=0, k=0..1
        [2.0, 1.0],   # j=1, k=0..1
        [-1.0, 2.5],  # j=2, k=0..1
    ]
    B = [
        [0.5, -1.5],  # j'=0, k'=0..1
        [1.2, 0.8],   # j'=1, k'=0..1
        [-0.4, 2.0],  # j'=2, k'=0..1
    ]
    # True C = A^T B has entries C_{k, k'} = sum_{j=0}^{p-1} A_{j,k} * B_{j,k'}
    C_true = [[0.0 for _ in range(n)] for _ in range(m)]
    for k in range(m):
        for kp in range(n):
            C_true[k][kp] = sum(A[j][k] * B[j][kp] for j in range(p))

    # Encode across N = 18 workers with distinct Chebyshev evaluation points x_i in [-1, 1]
    N = 18
    xs = [math.cos((2 * i + 1) * math.pi / (2 * N)) for i in range(N)]
    worker_outputs = []
    for x in xs:
        a_tilde = 0.0
        for j in range(p):
            for k in range(m):
                a_tilde += A[j][k] * (x ** (j + k * p))
        b_tilde = 0.0
        for jp in range(p):
            for kp in range(n):
                b_tilde += B[jp][kp] * (x ** ((p - 1 - jp) + kp * p * m))
        worker_outputs.append(a_tilde * b_tilde)

    # Decode from a non-contiguous subset of K_epc = 14 surviving workers
    surviving = [0, 1, 3, 4, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17]
    assert len(surviving) == k_epc
    vand = [[xs[i] ** deg for deg in range(k_epc)] for i in surviving]
    rhs = [worker_outputs[i] for i in surviving]
    coeffs = solve_linear_system(vand, rhs)

    # Extract C_{k,k'} from coefficient of x^{(p - 1) + k*p + k'*p*m}
    max_err = 0.0
    for k in range(m):
        for kp in range(n):
            target_deg = (p - 1) + k * p + kp * p * m
            err = abs(coeffs[target_deg] - C_true[k][kp])
            if err > max_err:
                max_err = err
    assert max_err < 1e-10, f"Decoding error too large: {max_err}"

    # Part 3: Bilinear-complexity improved Entangled Polynomial Code (Theorem 3, Remark 6, p. 5)
    # Using Strassen rank R(2^k, 2^k, 2^k) <= 7^k gives 2*7^k - 1 vs basic 8^k + 2^k - 1
    k_strassen_6 = 2 * (7 ** 6) - 1
    k_basic_6 = (8 ** 6) + (2 ** 6) - 1
    assert k_strassen_6 < k_basic_6

    print(
        f"[PASS] Round 542 Entangled Polynomial Codes verified: "
        f"K_EPC={k_epc} < K_PolyDot={k_polydot} < K_RL={k_random_linear}, "
        f"max_err={max_err:.2e}, K_Strassen(k=6)={k_strassen_6} < K_basic(k=6)={k_basic_6}"
    )


if __name__ == "__main__":
    main()
