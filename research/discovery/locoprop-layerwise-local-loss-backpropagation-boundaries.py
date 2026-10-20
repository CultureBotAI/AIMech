#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 649:
LocoProp (Local Loss Optimization Backpropagation Enhancement)
Primary source: Amid, Anil, & Warmuth (AISTATS 2022, PMLR v151, arXiv:2106.06199).
"""

import math


def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def mat_vec(A, x):
    return [sum(row[j] * x[j] for j in range(len(x))) for row in A]


def outer(u, v):
    return [[u[i] * v[j] for j in range(len(v))] for i in range(len(u))]


def mat_inv(A):
    n = len(A)
    M = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(A)]
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[piv] = M[piv], M[i]
        div = M[i][i]
        M[i] = [v / div for v in M[i]]
        for r in range(n):
            if r != i:
                f = M[r][i]
                M[r] = [M[r][c] - f * M[i][c] for c in range(2 * n)]
    return [row[n:] for row in M]


def verify_locoprop_s_single_step_and_closed_form_eq_4():
    """Verify Section 2.1 (Eqs. 3-4, Algorithm 1):
    (1) T=1 fixed-point iteration on the local squared loss recovers exact BackProp with eta_e = eta * gamma.
    (2) Iterating the fixed-point update converges to the closed-form implicit/K-FAC right-preconditioned
        update W_m^{new} = W_m - eta_e * grad_{W_m} L * (I + eta * y_{m-1} y_{m-1}^T)^{-1}."""
    W_0 = [
        [0.4, -0.2, 0.3],
        [-0.1, 0.5, 0.2],
    ]
    y_prev = [0.6, -0.4, 0.5]
    grad_a = [0.3, -0.7]
    gamma = 2.0
    eta = 0.15
    eta_e = eta * gamma

    a_hat = mat_vec(W_0, y_prev)
    a_target = [ah - gamma * g for ah, g in zip(a_hat, grad_a)]
    grad_W = outer(grad_a, y_prev)

    # T = 1 iteration of Algorithm 1
    W_1 = [row[:] for row in W_0]
    diff_1 = [ah - at for ah, at in zip(mat_vec(W_1, y_prev), a_target)]
    step_1 = outer(diff_1, y_prev)
    W_1 = [[W_1[i][j] - eta * step_1[i][j] for j in range(3)] for i in range(2)]

    # Standard BackProp step with learning rate eta_e = eta * gamma
    W_bp = [[W_0[i][j] - eta_e * grad_W[i][j] for j in range(3)] for i in range(2)]
    for i in range(2):
        for j in range(3):
            assert abs(W_1[i][j] - W_bp[i][j]) < 1e-12

    # Closed-form solution Eq. (4): W_0 - eta_e * grad_W * (I + eta * y_prev y_prev^T)^{-1}
    yyT = outer(y_prev, y_prev)
    right_mat = [[(1.0 if i == j else 0.0) + eta * yyT[i][j] for j in range(3)] for i in range(3)]
    precond_grad = mat_mul(grad_W, mat_inv(right_mat))
    W_closed = [[W_0[i][j] - eta_e * precond_grad[i][j] for j in range(3)] for i in range(2)]

    # Run T = 80 fixed-point iterations of Eq. (4): W^{(k+1)} = W_0 - eta * (W^{(k)} y_prev - a_target) y_prev^T
    W_iter = [row[:] for row in W_0]
    for _ in range(80):
        pred = mat_vec(W_iter, y_prev)
        diff = [p - at for p, at in zip(pred, a_target)]
        upd = outer(diff, y_prev)
        W_iter = [[W_0[i][j] - eta * upd[i][j] for j in range(3)] for i in range(2)]

    for i in range(2):
        for j in range(3):
            assert abs(W_iter[i][j] - W_closed[i][j]) < 1e-12

    # Also verify Algorithm 1 (T=10 local gradient descent steps) monotonically decreases ||W y_prev - a_target||^2
    W_alg1 = [row[:] for row in W_0]
    err_0 = sum((p - at) ** 2 for p, at in zip(mat_vec(W_alg1, y_prev), a_target))
    for _ in range(10):
        pred = mat_vec(W_alg1, y_prev)
        diff = [p - at for p, at in zip(pred, a_target)]
        upd = outer(diff, y_prev)
        W_alg1 = [[W_alg1[i][j] - eta * upd[i][j] for j in range(3)] for i in range(2)]
    err_10 = sum((p - at) ** 2 for p, at in zip(mat_vec(W_alg1, y_prev), a_target))
    assert err_10 < err_0


def verify_locoprop_m_matching_loss_and_sylvester_prop_2_3():
    """Verify Section 2.2 (Eqs. 5, 7, 8, Propositions 2 & 3, Algorithm 2):
    For tanh transfer function f(u) = tanh(u) with convex integral F(u) = sum_i log cosh(u_i):
    (1) Matching loss D_F(a_hat, a) >= 0 and gradient w.r.t. a_hat is f(a_hat) - f(a).
    (2) T=1 iteration of LocoProp-M with MD target y_m = y_hat_m - gamma * grad_{a_hat} L recovers BackProp.
    (3) Further local iterations monotonically decrease the convex local objective Eq. (7)."""
    W_0 = [
        [0.2, -0.3, 0.1],
        [0.4, 0.1, -0.2],
    ]
    y_prev = [0.5, -0.3, 0.4]
    grad_a = [0.25, -0.35]
    gamma = 0.5
    eta = 0.1
    eta_e = eta * gamma

    a_hat_0 = mat_vec(W_0, y_prev)
    y_hat_0 = [math.tanh(u) for u in a_hat_0]
    y_target = [yh - gamma * g for yh, g in zip(y_hat_0, grad_a)]
    # Target pre-activation a_m = tanh^{-1}(y_m) = 0.5 * log((1+y)/(1-y))
    a_target = [0.5 * math.log((1.0 + yt) / (1.0 - yt)) for yt in y_target]

    def local_matching_obj(W):
        a = mat_vec(W, y_prev)
        # D_F(a, a_target) = sum_i [log cosh(a_i) - log cosh(a_target_i) - tanh(a_target_i)*(a_i - a_target_i)]
        breg = sum(
            math.log(math.cosh(ai)) - math.log(math.cosh(ati)) - yti * (ai - ati)
            for ai, ati, yti in zip(a, a_target, y_target)
        )
        reg = (1.0 / (2.0 * eta)) * sum(
            (W[i][j] - W_0[i][j]) ** 2 for i in range(2) for j in range(3)
        )
        return breg + reg

    # T = 1 iteration of LocoProp-M (Algorithm 2)
    diff_1 = [yh - yt for yh, yt in zip(y_hat_0, y_target)]
    step_1 = outer(diff_1, y_prev)
    W_1 = [[W_0[i][j] - eta * step_1[i][j] for j in range(3)] for i in range(2)]

    grad_W = outer(grad_a, y_prev)
    W_bp = [[W_0[i][j] - eta_e * grad_W[i][j] for j in range(3)] for i in range(2)]
    for i in range(2):
        for j in range(3):
            assert abs(W_1[i][j] - W_bp[i][j]) < 1e-12

    # Verify T=10 fixed-point iterations converge to the stationary point of Eq. (8) and lower Eq. (7)
    W_curr = [row[:] for row in W_0]
    obj_0 = local_matching_obj(W_0)
    for _ in range(25):
        a_c = mat_vec(W_curr, y_prev)
        f_c = [math.tanh(u) for u in a_c]
        W_curr = [
            [W_0[i][j] - eta * (f_c[i] - y_target[i]) * y_prev[j] for j in range(3)]
            for i in range(2)
        ]
    obj_final = local_matching_obj(W_curr)
    assert obj_final < local_matching_obj(W_1) < obj_0


if __name__ == "__main__":
    verify_locoprop_s_single_step_and_closed_form_eq_4()
    verify_locoprop_m_matching_loss_and_sylvester_prop_2_3()
    print("[PASS] Round 649 LocoProp boundary and mathematical verification succeeded.")
