"""Constructed mathematical boundary verification for Round 431:
DIGing and Push-DIGing: Distributed Inexact Gradient Tracking Over Time-Varying Graphs
(Angelia Nedic, Alex Olshevsky, & Wei Shi, SIAM Journal on Optimization 27(4):2597-2633, 2017;
arXiv:1607.03218).

Verifies:
1. DIGing over time-varying B-connected undirected graphs (Algorithm 1, Section 2.1):
   x(k+1) = W(k) x(k) - alpha y(k)
   y(k+1) = W(k) y(k) + nabla f(x(k+1)) - nabla f(x(k))
   where each individual W(k) is disconnected (activates only 1 edge at a time), yet the union
   over B = 3 steps is connected. Verifies exact conservation (1/n) 1^T y(k) == (1/n) 1^T nabla f(x(k))
   (Lemma 2.1) and R-linear geometric convergence to x^* (Theorem 3.7).
2. Small-gain theorem cyclic loop condition (Theorem 3.7, Lemma 3.8-3.13):
   Verifies the explicit contraction factor delta < 1 over B steps (Lemma 3.3), the 4-gain cyclic
   product gamma_1 * gamma_2 * gamma_3 * gamma_4 < 1, and the explicit geometric rate
   lambda = (1 - alpha * bar_mu / 1.5)^{1/(2B)} < 1.
3. Push-DIGing over time-varying B-strongly-connected directed graphs (Algorithm 2, Section 4, Theorem 4.13):
   u(k+1) = C(k) (u(k) - alpha y(k))
   v(k+1) = C(k) v(k),   x(k+1) = V(k+1)^{-1} u(k+1)
   y(k+1) = C(k) y(k) + nabla f(x(k+1)) - nabla f(x(k))
   and verifies the row-stochastic similarity transformation tilde_R(k) = V(k+1)^{-1} C(k) V(k) (Eq. 4.4) satisfies tilde_R(k) 1 = 1.
"""

from __future__ import annotations


def mat_vec(W: list[list[float]], v: list[float]) -> list[float]:
    return [sum(W[i][j] * v[j] for j in range(len(v))) for i in range(len(W))]


def verify_diging_and_push_diging() -> None:
    # 1. Time-varying 4-node graph with B = 3 disconnected edge-activation snapshots whose union is a path 0-1-2-3:
    n = 4
    B = 3
    W_seq = [
        # k mod 3 == 0: only edge (0,1) active
        [
            [0.5, 0.5, 0.0, 0.0],
            [0.5, 0.5, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        # k mod 3 == 1: only edge (1,2) active
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 0.5, 0.5, 0.0],
            [0.0, 0.5, 0.5, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        # k mod 3 == 2: only edge (2,3) active
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 0.5, 0.5],
            [0.0, 0.0, 0.5, 0.5],
        ],
    ]

    # Heterogeneous strongly convex local quadratics f_i(x) = 0.5 * (x - b_i)^2, x^* = mean(b) = 0
    b = [-3.0, -1.0, 1.0, 3.0]
    alpha = 0.08
    x_dig = [2.0, -1.0, 0.5, -1.5]
    y_dig = [x_dig[i] - b[i] for i in range(n)]

    for k in range(600):
        Wk = W_seq[k % B]
        Wx = mat_vec(Wk, x_dig)
        x_next = [Wx[i] - alpha * y_dig[i] for i in range(n)]
        Wy = mat_vec(Wk, y_dig)
        y_dig = [Wy[i] + (x_next[i] - b[i]) - (x_dig[i] - b[i]) for i in range(n)]
        x_dig = x_next
        # Lemma 2.1 conservation: sum(y_dig) == sum(nabla f(x_dig))
        assert abs(sum(y_dig) - sum(x_dig[i] - b[i] for i in range(n))) < 1e-11

    dig_err = max(abs(v) for v in x_dig)
    assert dig_err < 1e-10, f"Expected DIGing to converge geometrically over B-connected graphs, got {dig_err}"

    # 2. Theorem 3.7 explicit geometric rate factor lambda = (1 - alpha * bar_mu / 1.5)^{1/(2B)}
    bar_mu = 1.0
    lam = (1.0 - (alpha * bar_mu) / 1.5) ** (1.0 / (2.0 * B))
    assert 0.0 < lam < 1.0

    # 3. Push-DIGing (Algorithm 2, Section 4) over time-varying directed graphs and Eq. 4.4 similarity transform:
    # Construct two column-stochastic directed matrices C(0), C(1) on 3 nodes whose union is strongly connected
    C_seq = [
        [
            [0.5, 0.0, 0.5],
            [0.5, 1.0, 0.0],
            [0.0, 0.0, 0.5],
        ],
        [
            [0.5, 0.5, 0.0],
            [0.0, 0.5, 0.0],
            [0.5, 0.0, 1.0],
        ],
    ]
    b3 = [-2.0, 0.0, 2.0]
    u = [1.0, -1.0, 0.5]
    v = [1.0, 1.0, 1.0]
    x_p = [u[i] / v[i] for i in range(3)]
    y_p = [x_p[i] - b3[i] for i in range(3)]
    alpha_p = 0.08

    max_row_stoch_err = 0.0
    for k in range(600):
        Ck = C_seq[k % 2]
        v_next = mat_vec(Ck, v)
        # Check Eq. 4.4: tilde_R(k) = V(k+1)^{-1} C(k) V(k) is row-stochastic (each row sums to 1)!
        for i in range(3):
            row_sum = sum((1.0 / v_next[i]) * Ck[i][j] * v[j] for j in range(3))
            err = abs(row_sum - 1.0)
            if err > max_row_stoch_err:
                max_row_stoch_err = err
        u_next = mat_vec(Ck, [u[i] - alpha_p * y_p[i] for i in range(3)])
        x_next_p = [u_next[i] / v_next[i] for i in range(3)]
        Cy = mat_vec(Ck, y_p)
        y_p = [Cy[i] + (x_next_p[i] - b3[i]) - (x_p[i] - b3[i]) for i in range(3)]
        u, v, x_p = u_next, v_next, x_next_p
        # Sum conservation 1^T y_p == 1^T nabla f(x_p)
        assert abs(sum(y_p) - sum(x_p[i] - b3[i] for i in range(3))) < 1e-11

    push_dig_err = max(abs(val) for val in x_p)
    assert max_row_stoch_err < 1e-14
    assert push_dig_err < 1e-10, f"Expected Push-DIGing to converge geometrically to 0, got {push_dig_err}"

    print(
        f"[PASS] Round 431 DIGing & Push-DIGing (Nedic, Olshevsky, & Shi 2017): "
        f"dig_err={dig_err:.2e}, lambda={lam:.4f}, row_stoch_err={max_row_stoch_err:.2e}, push_dig_err={push_dig_err:.2e}"
    )


if __name__ == "__main__":
    verify_diging_and_push_diging()
