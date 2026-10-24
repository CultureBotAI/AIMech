#!/usr/bin/env python3
"""Constructed boundary verification for Round 531: FLDetector (Zhang et al., KDD 2022).

Verifies:
1. Section 4.1 Equations (2)-(3) & Algorithm 1: For benign clients with quadratic/L-smooth
   objectives, the Cauchy mean value theorem g_i^t = g_i^{t-1} + H_i^t (w_t - w_{t-1}) holds,
   and the L-BFGS Hessian-vector product H_hat^t (w_t - w_{t-1}) accurately predicts benign
   client updates (small ||g_hat_i^t - g_i^t||_2), whereas FLD-NoHVP (g_hat_i^t = g_i^{t-1})
   incurs large prediction error proportional to ||H_i^t (w_t - w_{t-1})||_2.
2. Section 4.4 Theorem 1 & Appendix A Lemma 1 (Equations 5, 7-26): Under L-smoothness and
   learning rate alpha < 1 / ((N + 2) * L), the quasi-Newton Hessian satisfies
   z^T H_hat^t z <= (N + 1) * L * ||z||_2^2 (Lemma 1), and the expected suspicious score of
   every benign client i in B is strictly smaller than that of every sign-reversing malicious
   client j in M: E[s_i^t] < E[s_j^t].
"""

import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm2(u):
    return math.sqrt(dot(u, u))


def mat_vec(M, v):
    return [dot(row, v) for row in M]


def rank1_outer(u, v, scale=1.0):
    d = len(u)
    return [[scale * u[i] * v[j] for j in range(d)] for i in range(d)]


def mat_add(A, B, scale_b=1.0):
    d = len(A)
    return [[A[i][j] + scale_b * B[i][j] for j in range(d)] for i in range(d)]


def lbfgs_hessian_matrix(dw_list, dg_list):
    """Appendix A Equation (8): Quasi-Hessian recursion B_{t-m+1} from window of N steps."""
    N = len(dw_list)
    d = len(dw_list[0])
    dw0, dg0 = dw_list[0], dg_list[0]
    sigma0 = dot(dg0, dw0) / dot(dw0, dw0)
    B = [[sigma0 if i == j else 0.0 for j in range(d)] for i in range(d)]
    for m in range(N):
        dw = dw_list[m]
        dg = dg_list[m]
        B_dw = mat_vec(B, dw)
        denom1 = dot(dw, B_dw)
        denom2 = dot(dg, dw)
        if abs(denom1) > 1e-14 and abs(denom2) > 1e-14:
            B = mat_add(B, rank1_outer(B_dw, B_dw), scale_b=-1.0 / denom1)
            B = mat_add(B, rank1_outer(dg, dg), scale_b=1.0 / denom2)
    return B


def main():
    # True underlying L-smooth quadratic loss f(w) = 0.5 * w^T H w - b^T w with L = 4.0
    H_true = [[4.0, 0.0], [0.0, 2.0]]
    L = 4.0
    N = 3  # window size N = 3 -> Theorem 1 requires alpha < 1 / ((N + 2) * L) = 1 / 20 = 0.05
    alpha = 0.03
    assert alpha < 1.0 / ((N + 2) * L)

    # Generate N historical global steps
    w_hist = [[2.0, 3.0]]
    g_hist = [mat_vec(H_true, w_hist[0])]
    for t in range(N + 1):
        w_next = [w_hist[-1][k] - alpha * g_hist[-1][k] for k in range(2)]
        w_hist.append(w_next)
        g_hist.append(mat_vec(H_true, w_next))

    dw_list = [[w_hist[t + 1][k] - w_hist[t][k] for k in range(2)] for t in range(N)]
    dg_list = [[g_hist[t + 1][k] - g_hist[t][k] for k in range(2)] for t in range(N)]

    B_hat = lbfgs_hessian_matrix(dw_list, dg_list)

    # 1. Verify Appendix A Lemma 1: z^T H_hat^t z <= (N + 1) * L * ||z||_2^2 for unit vectors z
    for angle in [0.0, 0.5, 1.0, 1.5]:
        z = [math.cos(angle), math.sin(angle)]
        quad = dot(z, mat_vec(B_hat, z))
        bound = (N + 1) * L * dot(z, z)
        assert quad <= bound + 1e-12, f"Expected {quad} <= {bound}"

    # 2. Predict client updates at step t = N: g_hat_i^t = g_i^{t-1} + B_hat (w_t - w_{t-1})
    v_step = [w_hist[N + 1][k] - w_hist[N][k] for k in range(2)]
    hvp = mat_vec(B_hat, v_step)

    # 6 benign clients (with small local bias b_i) and 2 sign-flipping malicious clients (-g_j^t)
    biases = [[0.1, -0.1], [-0.1, 0.1], [0.05, 0.05], [-0.05, -0.05], [0.0, 0.1], [0.1, 0.0], [0.0, 0.0], [0.0, 0.0]]
    d_fld = []
    d_nohvp = []
    for idx, b_i in enumerate(biases):
        g_prev = [mat_vec(H_true, w_hist[N])[k] - b_i[k] for k in range(2)]
        g_true_curr = [mat_vec(H_true, w_hist[N + 1])[k] - b_i[k] for k in range(2)]
        # Clients 6 and 7 are malicious sign-flippers: send -g_true_curr
        g_sent = g_true_curr if idx < 6 else [-x for x in g_true_curr]
        g_pred = [g_prev[k] + hvp[k] for k in range(2)]
        d_fld.append(norm2([g_pred[k] - g_sent[k] for k in range(2)]))
        d_nohvp.append(norm2([g_prev[k] - g_sent[k] for k in range(2)]))

    # Normalize suspicious scores s^t = d^t / ||d^t||_1
    sum_d = sum(d_fld)
    s_t = [x / sum_d for x in d_fld]

    max_benign_s = max(s_t[:6])
    min_mal_s = min(s_t[6:])
    # Verify Theorem 1 separation: benign suspicious scores strictly smaller than malicious scores
    assert max_benign_s < min_mal_s, f"Expected max_benign_s={max_benign_s} < min_mal_s={min_mal_s}"
    # Verify HVP reduces benign prediction error compared to FLD-NoHVP
    assert max(d_fld[:6]) < min(d_nohvp[:6])

    print(
        f"[PASS] Round 531 FLDetector (Zhang et al. 2022): "
        f"benign_err_HVP={max(d_fld[:6]):.6f}<benign_err_NoHVP={min(d_nohvp[:6]):.6f}, "
        f"max_benign_score={max_benign_s:.4f} << min_malicious_score={min_mal_s:.4f}"
    )


if __name__ == "__main__":
    main()
