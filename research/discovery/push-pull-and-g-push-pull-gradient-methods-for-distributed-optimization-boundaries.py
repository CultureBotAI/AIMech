"""Constructed boundary and numerical verification for Round 438:
Push-Pull and G-Push-Pull Gradient Methods for Distributed Optimization in Networks
(Shi Pu, Wei Shi, Jinming Xu, & Angelia Nedic 2021, IEEE Trans. Autom. Control 66(1):1-15, arXiv:1810.06653).
"""

from __future__ import annotations

import math


def mat_vec(M: list[list[float]], v: list[float]) -> list[float]:
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def vec_norm(v: list[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def main() -> None:
    # 4-node asymmetric directed graphs G_R and G_{C^T} sharing root node 0:
    # R is row-stochastic (R 1 = 1), C is column-stochastic (1^T C = 1^T)
    n = 4
    R = [
        [0.60, 0.40, 0.00, 0.00],
        [0.30, 0.50, 0.20, 0.00],
        [0.20, 0.00, 0.50, 0.30],
        [0.40, 0.00, 0.20, 0.40],
    ]
    C = [
        [0.50, 0.25, 0.20, 0.30],
        [0.50, 0.50, 0.00, 0.00],
        [0.00, 0.25, 0.50, 0.30],
        [0.00, 0.00, 0.30, 0.40],
    ]

    for i in range(n):
        assert abs(sum(R[i]) - 1.0) < 1e-14, "R must be row-stochastic"
    for j in range(n):
        assert abs(sum(C[i][j] for i in range(n)) - 1.0) < 1e-14, "C must be column-stochastic"

    # Heterogeneous strongly convex local objectives f_i(x_i) = 0.5 * a_i * (x_i - b_i)^2
    a = [1.2, 1.8, 2.4, 3.0]
    b = [3.0, -2.0, 1.5, -4.0]
    x_star = sum(a[i] * b[i] for i in range(n)) / sum(a)

    def grad_F(x: list[float]) -> list[float]:
        return [a[i] * (x[i] - b[i]) for i in range(n)]

    # Case 1: Peer-to-peer uncoordinated positive step sizes alpha = diag(0.08, 0.05, 0.06, 0.04)
    alphas_p2p = [0.08, 0.05, 0.06, 0.04]
    x = [1.0, -1.0, 0.5, 2.0]
    y = grad_F(x)
    max_conservation_err = 0.0

    for _ in range(350):
        step_x = [x[i] - alphas_p2p[i] * y[i] for i in range(n)]
        x_next = mat_vec(R, step_x)
        g_curr = grad_F(x)
        g_next = grad_F(x_next)
        Cy = mat_vec(C, y)
        y_next = [Cy[i] + g_next[i] - g_curr[i] for i in range(n)]
        max_conservation_err = max(max_conservation_err, abs(sum(y_next) - sum(g_next)))
        x, y = x_next, y_next

    err_p2p = vec_norm([x[i] - x_star for i in range(n)])
    assert max_conservation_err < 1e-13
    assert err_p2p < 1e-11, f"Peer-to-peer Push-Pull error too large: {err_p2p}"

    # Case 2: Leader-follower semi-centralized topology where ONLY root node 0 has alpha_0 > 0
    # and follower nodes 1, 2, 3 have alpha_i = 0 (Assumption 4: max_i alpha_i > 0 at shared root)
    alphas_leader = [0.12, 0.0, 0.0, 0.0]
    x_lf = [1.0, -1.0, 0.5, 2.0]
    y_lf = grad_F(x_lf)
    for _ in range(500):
        step_x = [x_lf[i] - alphas_leader[i] * y_lf[i] for i in range(n)]
        x_next = mat_vec(R, step_x)
        g_curr = grad_F(x_lf)
        g_next = grad_F(x_next)
        Cy = mat_vec(C, y_lf)
        y_next = [Cy[i] + g_next[i] - g_curr[i] for i in range(n)]
        x_lf, y_lf = x_next, y_next

    err_lf = vec_norm([x_lf[i] - x_star for i in range(n)])
    assert err_lf < 1e-10, f"Leader-follower Push-Pull error too large: {err_lf}"

    print(
        f"[PASS] Round 438 Push-Pull (Pu et al. 2021): conservation_err={max_conservation_err:.2e}, "
        f"err_p2p={err_p2p:.2e}, err_leader_only={err_lf:.2e}"
    )


if __name__ == "__main__":
    main()
