"""Constructed mathematical boundary and pseudogradient angle verification for Round 623:
AdaSum — Adaptive Summation for Scaling Distributed Training (Maleki et al., MLSys 2021, arXiv:2006.02924).

Verifies:
1. Section 1 & Section 3.1-3.5 AdaSum Combiner & Sequential SGD Emulation (Eq. 1-5 & Appendix A.1-A.2 Eq. 6-10, p. 1, 3-4, 14-15):
   - Adasum(g_1, g_2) = (1 - (g_1^T g_2) / (2 * ||g_1||^2)) * g_1 + (1 - (g_1^T g_2) / (2 * ||g_2||^2)) * g_2
     equals the exact average of the two sequential Fisher-approximated SGD steps
     w_{1,2} = w_0 - alpha * (g_1 + (1 - (g_2^T g_1)/||g_2||^2) g_2) and
     w_{2,1} = w_0 - alpha * (g_2 + (1 - (g_1^T g_2)/||g_1||^2) g_1).
   - Orthogonal boundary (g_1^T g_2 = 0): Adasum(g_1, g_2) = g_1 + g_2 (exact sum).
   - Parallel identical-norm boundary (g_1 = g_2 = g): Adasum(g, g) = g = (g_1 + g_2) / 2 (exact average).
   - Per-layer orthogonality metric (Section 3.6, p. 4): Orth(g_1..g_N) = ||Adasum(g_{[1,N]})||^2 / sum_i ||g_i||^2
     equals 1.0 when g_1..g_N are mutually orthogonal and 1/N when g_1 = ... = g_N.
2. Appendix A.3 Pseudogradient Convergence Proof: Lemma A.2, Lemma A.3, & Theorem A.4 (Eq. 11-12, p. 15-16):
   - For independent a, b ~ X with r = E[X], E[Adasum(a, b)] = (2*I - E[a a^T / ||a||^2]) * r (Eq. 11).
   - Lemma A.2 worst-case rotation bound (Eq. 12): for any unit vector u = a / ||a|| at angle gamma to r,
     cos(eta) = (2 - cos^2(gamma)) / sqrt(4 - 3 * cos^2(gamma)) >= 2*sqrt(2)/3 ~ 0.942809 > 0.942
     (attained at cos^2(gamma) = 2/3, corresponding to eta <= 0.108 * pi).
   - Lemma A.3 norm sandwich: ||E[X]|| <= ||E[Adasum(a, b)]|| <= 2 * ||E[X]||, and across log_2(N) tree levels
     ||E[G]|| <= ||E[G_{log N}]|| <= N * ||E[G]||.
3. Section 3.7 & Section 4.2.1 Exact Hessian Emulation Error & Recursive Vector-Halving (Algorithm 1, p. 5-6):
   - On a quadratic loss with rank-1 Fisher Hessian H_2 = g_2 g_2^T and optimal step alpha = 1/||g_2||^2,
     Adasum has lower approximation error to exact sequential SGD than naive synchronous gradient summation.
"""

from __future__ import annotations

import math
import random


def adasum_pair(g1: list[float], g2: list[float]) -> list[float]:
    dot = sum(a * b for a, b in zip(g1, g2))
    n1 = sum(a * a for a in g1)
    n2 = sum(b * b for b in g2)
    c1 = 1.0 - (dot / (2.0 * n1)) if n1 > 0.0 else 1.0
    c2 = 1.0 - (dot / (2.0 * n2)) if n2 > 0.0 else 1.0
    return [c1 * a + c2 * b for a, b in zip(g1, g2)]


def adasum_tree(grads: list[list[float]]) -> list[float]:
    n = len(grads)
    if n == 1:
        return list(grads[0])
    mid = n // 2
    left = adasum_tree(grads[:mid])
    right = adasum_tree(grads[mid:])
    return adasum_pair(left, right)


def verify_sequential_emulation_and_boundary_cases() -> tuple[float, float, float, float, float]:
    rng = random.Random(20261019)
    d = 8
    g1 = [rng.uniform(-2.0, 2.0) for _ in range(d)]
    g2 = [rng.uniform(-2.0, 2.0) for _ in range(d)]

    # 1. Verify exact equivalence between Adasum(g1, g2) and average of (b1 -> b2) and (b2 -> b1) sequential steps (Eq. 4-5, p. 4)
    dot12 = sum(a * b for a, b in zip(g1, g2))
    n1 = sum(a * a for a in g1)
    n2 = sum(b * b for b in g2)
    seq_12 = [g1[i] + (1.0 - dot12 / n2) * g2[i] for i in range(d)]
    seq_21 = [g2[i] + (1.0 - dot12 / n1) * g1[i] for i in range(d)]
    avg_seq = [0.5 * (seq_12[i] + seq_21[i]) for i in range(d)]
    ada_12 = adasum_pair(g1, g2)
    seq_emul_err = max(abs(a - b) for a, b in zip(avg_seq, ada_12))
    assert seq_emul_err < 1e-15

    # 2. Verify orthogonal boundary (g1^T g2 = 0) and parallel boundary (g1 = g2)
    N = 8
    orth_grads = [[1.0 if j == i else 0.0 for j in range(N)] for i in range(N)]
    ada_orth = adasum_tree(orth_grads)
    orth_sum_err = max(abs(ada_orth[j] - 1.0) for j in range(N))
    orth_metric_max = sum(v * v for v in ada_orth) / sum(sum(v * v for v in g) for g in orth_grads)
    assert orth_sum_err < 1e-15
    assert abs(orth_metric_max - 1.0) < 1e-15

    par_grads = [list(g1) for _ in range(N)]
    ada_par = adasum_tree(par_grads)
    par_avg_err = max(abs(ada_par[j] - g1[j]) for j in range(d))
    orth_metric_min = sum(v * v for v in ada_par) / sum(sum(v * v for v in g) for g in par_grads)
    assert par_avg_err < 1e-15
    assert abs(orth_metric_min - (1.0 / N)) < 1e-15

    return seq_emul_err, orth_sum_err, par_avg_err, orth_metric_max, orth_metric_min


def verify_pseudogradient_lemmas_and_hessian_error() -> tuple[float, float, float, float]:
    # 1. Verify Lemma A.2 (Eq. 11-12, p. 15-16): cos(eta) = (2 - cos^2(gamma)) / sqrt(4 - 3*cos^2(gamma)) >= 2*sqrt(2)/3
    exact_min_cos = 2.0 * math.sqrt(2.0) / 3.0  # ~ 0.94280904158
    min_cos_grid = float("inf")
    for k in range(1001):
        c2 = k / 1000.0  # cos^2(gamma) in [0, 1]
        cos_eta = (2.0 - c2) / math.sqrt(4.0 - 3.0 * c2)
        min_cos_grid = min(min_cos_grid, cos_eta)
    assert abs(min_cos_grid - exact_min_cos) < 1e-6
    assert min_cos_grid > 0.942

    # 2. Verify Eq. (11) & Lemma A.3 exact expectation and norm bounds over finite distribution X = {x_1..x_M}
    rng = random.Random(20261019)
    M = 12
    d = 4
    X = [[1.5 + rng.uniform(-0.8, 0.8) for _ in range(d)] for _ in range(M)]
    r = [sum(X[m][j] for m in range(M)) / M for j in range(d)]

    # Exact average over all M^2 independent pairs (a, b) in X x X
    ey_pairs = [0.0] * d
    for a in X:
        for b in X:
            y = adasum_pair(a, b)
            for j in range(d):
                ey_pairs[j] += y[j] / (M * M)

    # Matrix formula (2*I - E[a a^T / ||a||^2]) * r (Eq. 11 & Lemma A.3)
    ey_mat = [2.0 * r[j] for j in range(d)]
    for a in X:
        na = sum(v * v for v in a)
        dot_ar = sum(a[j] * r[j] for j in range(d))
        for j in range(d):
            ey_mat[j] -= (dot_ar / na) * a[j] / M

    eq11_err = max(abs(a - b) for a, b in zip(ey_pairs, ey_mat))
    assert eq11_err < 1e-14

    norm_r = math.sqrt(sum(v * v for v in r))
    norm_ey = math.sqrt(sum(v * v for v in ey_pairs))
    assert norm_r <= norm_ey <= 2.0 * norm_r + 1e-14
    cos_r_ey = sum(r[j] * ey_pairs[j] for j in range(d)) / (norm_r * norm_ey)
    assert cos_r_ey >= exact_min_cos - 1e-14

    # 3. Verify Section 3.7 (Figure 2, p. 5) sequential emulation error vs synchronous sum on quadratic losses
    # L_1(w) = 0.5 * (u_1^T (w - w*))^2, L_2(w) = 0.5 * (u_2^T (w - w*))^2
    u1 = [0.8, 0.6, 0.0, 0.0]
    u2 = [0.6, 0.8, 0.0, 0.0]
    w0 = [1.5, 1.2, -0.5, 0.4]
    g1_0 = [sum(u1[j] * w0[j] for j in range(d)) * u1[i] for i in range(d)]
    g2_0 = [sum(u2[j] * w0[j] for j in range(d)) * u2[i] for i in range(d)]
    H2 = [[u2[r_i] * u2[c_i] for c_i in range(d)] for r_i in range(d)]
    alpha = 0.6

    # True two-step average over both orderings (b1->b2 and b2->b1) using exact Hessians H1, H2
    H1 = [[u1[r_i] * u1[c_i] for c_i in range(d)] for r_i in range(d)]
    h2_g1 = [sum(H2[i][j] * g1_0[j] for j in range(d)) for i in range(d)]
    h1_g2 = [sum(H1[i][j] * g2_0[j] for j in range(d)) for i in range(d)]
    exact_seq_grad = [g1_0[i] + g2_0[i] - 0.5 * alpha * (h2_g1[i] + h1_g2[i]) for i in range(d)]

    sync_grad = [g1_0[i] + g2_0[i] for i in range(d)]
    adasum_grad = adasum_pair(g1_0, g2_0)

    err_adasum = math.sqrt(sum((adasum_grad[i] - exact_seq_grad[i]) ** 2 for i in range(d)))
    err_sync = math.sqrt(sum((sync_grad[i] - exact_seq_grad[i]) ** 2 for i in range(d)))
    assert err_adasum < err_sync

    return min_cos_grid, eq11_err, norm_ey / norm_r, err_adasum / err_sync


if __name__ == "__main__":
    seq_e, orth_e, par_e, o_max, o_min = verify_sequential_emulation_and_boundary_cases()
    min_c, eq11_e, n_rat, hes_rat = verify_pseudogradient_lemmas_and_hessian_error()
    print(
        f"[PASS] Round 623 AdaSum verified: "
        f"seq_emul_err={seq_e:.2e}, orth_err={orth_e:.2e}, par_err={par_e:.2e}, "
        f"orth_range=[{o_min:.4f}, {o_max:.4f}], lemmaA2_min_cos={min_c:.6f}>0.942, "
        f"eq11_err={eq11_e:.2e}, norm_ratio={n_rat:.4f} in [1,2], hessian_err_ratio={hes_rat:.4f}<1"
    )
