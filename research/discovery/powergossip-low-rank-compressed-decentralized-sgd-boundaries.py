#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 556: PowerGossip (Vogels, Karimireddy, & Jaggi, NeurIPS 2020)."""

import math
import random


def mat_sub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mat_add(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mat_scale(A, c):
    return [[c * a for a in r] for r in A]


def mat_vec(A, v):
    return [sum(a * x for a, x in zip(r, v)) for r in A]


def mat_t_vec(A, u):
    p, q = len(A), len(A[0])
    return [sum(A[r][c] * u[r] for r in range(p)) for c in range(q)]


def outer(u, v):
    return [[x * y for y in v] for x in u]


def frob_sq(A):
    return sum(a * a for r in A for a in r)


def vec_norm(v):
    return math.sqrt(sum(x * x for x in v))


def main():
    rng = random.Random(20200801)
    # 1. Verify linearity of rank-1 projection C_v(X_j - X_i) = (X_j v - X_i v) v^T
    # and Lemma 1 (exact average preservation without consensus stepsize)
    n, p, q = 4, 5, 4
    # 4-ring symmetric doubly stochastic mixing matrix W: W_ii = 0.5, neighbors = 0.25
    W = [
        [0.50, 0.25, 0.00, 0.25],
        [0.25, 0.50, 0.25, 0.00],
        [0.00, 0.25, 0.50, 0.25],
        [0.25, 0.00, 0.25, 0.50],
    ]
    # Eigenvalues of W for 4-ring: 1, 0.5, 0.5, 0.0 -> W^2 eigenvalues: 1, 0.25, 0.25, 0.0 -> rho = 1 - 0.25 = 0.75
    rho = 0.75
    delta = 1.0 / q  # rank-1 random unit projection in R^q has delta = 1/q = 0.25

    X0 = [[[rng.gauss(0.0, 1.0) for _ in range(q)] for _ in range(p)] for _ in range(n)]

    def mean_mat(Xs):
        out = [[0.0] * q for _ in range(p)]
        for X in Xs:
            out = mat_add(out, mat_scale(X, 1.0 / n))
        return out

    X_bar0 = mean_mat(X0)
    init_err = sum(frob_sq(mat_sub(X0[i], X_bar0)) for i in range(n)) / n

    # 2. Verify Theorem I: E[(1/n) sum_i ||X_i^(1) - X_bar^(0)||_F^2] <= (1 - rho * delta) init_err
    # Using exact orthonormal basis averaging over the q canonical directions (which satisfies E[u u^T] = (1/q) I_q)
    expected_err_after_1 = 0.0
    for basis_idx in range(q):
        v = [1.0 if c == basis_idx else 0.0 for c in range(q)]
        X1 = []
        for i in range(n):
            upd = [[0.0] * q for _ in range(p)]
            for j in range(n):
                if W[i][j] > 0 and i != j:
                    # Distributed vector exchange: p_j = X_j v, p_i = X_i v
                    pj = mat_vec(X0[j], v)
                    pi = mat_vec(X0[i], v)
                    diff_p = [pj[r] - pi[r] for r in range(p)]
                    comp_diff = outer(diff_p, v)
                    # Check algebraic identity C_v(X_j - X_i) == (X_j v - X_i v) v^T
                    direct_diff = outer(mat_vec(mat_sub(X0[j], X0[i]), v), v)
                    assert frob_sq(mat_sub(comp_diff, direct_diff)) < 1e-24
                    upd = mat_add(upd, mat_scale(comp_diff, W[i][j]))
            X1.append(mat_add(X0[i], upd))
        # Verify Lemma 1: average is preserved identically on every realization
        X_bar1 = mean_mat(X1)
        assert frob_sq(mat_sub(X_bar1, X_bar0)) < 1e-24
        err1 = sum(frob_sq(mat_sub(X1[i], X_bar0)) for i in range(n)) / n
        expected_err_after_1 += err1 / q

    theoretical_bound = (1.0 - rho * delta) * init_err
    assert expected_err_after_1 <= theoretical_bound + 1e-12

    # 3. Verify Algorithm 2 s-step alternating power iteration improves low-rank approximation over random projection
    # Construct a peaked-spectrum difference matrix D = u_true * s1 * v_true^T + noise
    u_true = [math.sin(r + 1) for r in range(p)]
    un = vec_norm(u_true)
    u_true = [x / un for x in u_true]
    v_true = [math.cos(c + 1) for c in range(q)]
    vn = vec_norm(v_true)
    v_true = [x / vn for x in v_true]
    D = mat_scale(outer(u_true, v_true), 10.0)
    for r in range(p):
        for c in range(q):
            D[r][c] += 0.1 * rng.gauss(0.0, 1.0)

    v_init = [rng.gauss(0.0, 1.0) for _ in range(q)]
    v_hat = [x / vec_norm(v_init) for x in v_init]
    Q_rand = outer(mat_vec(D, v_hat), v_hat)
    err_rand = frob_sq(mat_sub(D, Q_rand))

    # Run 4 alternating power steps (Eq. 3 / Algorithm 2)
    vij = v_init[:]
    for k in range(1, 5):
        if k % 2 == 1:
            v_hat = [x / vec_norm(vij) for x in vij]
            p_vec = mat_vec(D, v_hat)
            Q_hat = outer(p_vec, v_hat)
            vij = p_vec
        else:
            u_hat = [x / vec_norm(vij) for x in vij]
            q_vec = mat_t_vec(D, u_hat)
            Q_hat = outer(u_hat, q_vec)
            vij = q_vec
    err_power = frob_sq(mat_sub(D, Q_hat))
    assert err_power < err_rand

    print(
        f"[PASS] Round 556 PowerGossip verified: E[err1]={expected_err_after_1:.6f} <= (1-rho*delta)*err0={theoretical_bound:.6f}, "
        f"err_power={err_power:.6f} < err_rand={err_rand:.6f}"
    )


if __name__ == "__main__":
    main()
