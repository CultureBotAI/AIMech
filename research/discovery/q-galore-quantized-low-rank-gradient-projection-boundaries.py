#!/usr/bin/env python3
"""Boundary verification for Round 641: Q-GaLore (Zhang et al., CPAL 2025 / arXiv:2407.08296)."""

from __future__ import annotations

import math
import random


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    m, k, n = len(a), len(a[0]), len(b[0])
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for p in range(k):
            aip = a[i][p]
            for j in range(n):
                out[i][j] += aip * b[p][j]
    return out


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]


def frob_norm(a: list[list[float]]) -> float:
    return math.sqrt(sum(v * v for row in a for v in row))


def top_r_left_singular_vectors(g: list[list[float]], r: int, iters: int = 80) -> list[list[float]]:
    """Compute top-r left singular vectors P in R^{m x r} of G in R^{m x n} via deflated power iteration."""
    m = len(g)
    gt = transpose(g)
    ggt = matmul(g, gt)
    cols: list[list[float]] = []
    for col_idx in range(r):
        v = [math.sin((i + 1) * (col_idx + 2)) + 0.1 for i in range(m)]
        for _ in range(iters):
            # Multiply by ggt
            nv = [sum(ggt[i][j] * v[j] for j in range(m)) for i in range(m)]
            # Orthogonalize against previous columns
            for prev in cols:
                dot = sum(nv[i] * prev[i] for i in range(m))
                for i in range(m):
                    nv[i] -= dot * prev[i]
            nrm = math.sqrt(sum(x * x for x in nv))
            v = [x / nrm for x in nv]
        cols.append(v)
    return transpose(cols)


def subspace_cosine_similarity(p1: list[list[float]], p2: list[list[float]]) -> float:
    """Equation (5): CosSim(P_t, P_{t-dt}) = (1/r) sum_{i=1}^r sigma_i(P_t^T P_{t-dt})."""
    r = len(p1[0])
    m = matmul(transpose(p1), p2)
    mtm = matmul(transpose(m), m)
    # Compute eigenvalues of r x r symmetric positive semi-definite matrix mtm via Jacobi rotations
    a = [row[:] for row in mtm]
    for _ in range(60):
        for i in range(r):
            for j in range(i + 1, r):
                if abs(a[i][j]) < 1e-14:
                    continue
                tau = (a[j][j] - a[i][i]) / (2.0 * a[i][j])
                t = math.copysign(1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau)), tau)
                c = 1.0 / math.sqrt(1.0 + t * t)
                s = t * c
                aii, ajj, aij = a[i][i], a[j][j], a[i][j]
                a[i][i] = c * c * aii - 2.0 * s * c * aij + s * s * ajj
                a[j][j] = s * s * aii + 2.0 * s * c * aij + c * c * ajj
                a[i][j] = a[j][i] = 0.0
                for k in range(r):
                    if k != i and k != j:
                        aki, akj = a[k][i], a[k][j]
                        a[k][i] = a[i][k] = c * aki - s * akj
                        a[k][j] = a[j][k] = s * aki + c * akj
    sigmas = [math.sqrt(max(0.0, a[i][i])) for i in range(r)]
    return sum(sigmas) / r


def quantize_int4_dequantize(p: list[list[float]]) -> list[list[float]]:
    """Symmetric column-wise INT4 quantization [-7, 7] and dequantization of projection matrix P."""
    m, r = len(p), len(p[0])
    p_hat = [[0.0] * r for _ in range(m)]
    for j in range(r):
        max_abs = max(abs(p[i][j]) for i in range(m))
        scale = max_abs / 7.0 if max_abs > 0 else 1.0
        for i in range(m):
            q = max(-7, min(7, int(round(p[i][j] / scale))))
            p_hat[i][j] = q * scale
    return p_hat


def main() -> None:
    rng = random.Random(641)
    m, n, r = 24, 32, 4

    # 1. Verify Theorem 3.1 & Layer-Adaptive Subspace Schedule (Section 3.1, Eq. 3-5):
    # Early-stage rapidly changing gradient subspace vs converged stationary subspace
    u_base = [[rng.gauss(0.0, 1.0) for _ in range(r)] for _ in range(m)]
    v_base = [[rng.gauss(0.0, 1.0) for _ in range(n)] for _ in range(r)]
    g_base = matmul(u_base, v_base)

    # Early training / rapidly changing subspace (Theorem 3.1 non-stationary regime): CosSim <= gamma (0.4)
    u_orth = [[rng.gauss(0.0, 1.0) for _ in range(r)] for _ in range(m)]
    v_orth = [[rng.gauss(0.0, 1.0) for _ in range(n)] for _ in range(r)]
    g_early = matmul(u_orth, v_orth)
    p_base = top_r_left_singular_vectors(g_base, r)
    p_early = top_r_left_singular_vectors(g_early, r)
    cos_early = subspace_cosine_similarity(p_base, p_early)

    # Stationary region (Theorem 3.1 converged regime W_{t+T1} approx W_{t+T2}): CosSim > gamma -> double interval dt <- 2 * dt
    noise_small = [[rng.gauss(0.0, 0.25) for _ in range(n)] for _ in range(m)]
    g_stationary = [[g_base[i][j] + noise_small[i][j] for j in range(n)] for i in range(m)]
    p_stationary = top_r_left_singular_vectors(g_stationary, r)
    cos_stationary = subspace_cosine_similarity(p_base, p_stationary)

    gamma = 0.4
    assert cos_early < gamma < cos_stationary, (
        f"Expected cos_early < {gamma} < cos_stationary, got {cos_early:.4f} vs {cos_stationary:.4f}"
    )

    # Simulate Layer-Adaptive SVD schedule (Eq. 5) across 1000 steps with initial dt_0 = 20
    # Stationary layer doubles dt at each check: t=20, 60, 140, 300, 620 -> 5 SVDs instead of 50 (90% reduction)
    t, dt_adapt, svd_count_adapt = 20, 20, 0
    while t <= 1000:
        svd_count_adapt += 1
        if cos_stationary > gamma:
            dt_adapt *= 2
        t += dt_adapt
    svd_count_fixed = 1000 // 20
    assert svd_count_adapt == 5 and svd_count_fixed == 50

    # 2. Verify INT4 Projection Matrix Quantization Fidelity (Section 3.2):
    p_int4 = quantize_int4_dequantize(p_base)
    cos_int4 = subspace_cosine_similarity(p_base, p_int4)
    assert cos_int4 > 0.99, f"INT4 projection subspace cosine similarity too low: {cos_int4:.5f}"

    # 3. Verify Unbiased Stochastic Rounding xi(.) on INT8 Weight Trajectory (Algorithm 1 line 12):
    # Suppose INT8 quantization step size is delta = 0.01, and per-step update is u = -0.002 (< delta / 2).
    # Deterministic rounding rounds u to 0 every step (stalling completely), whereas stochastic rounding
    # accumulates exact expected movement E[xi(u)] = u.
    delta = 0.01
    u_step = -0.002
    w_det = 1.0
    w_stoch = 1.0
    steps = 2000
    for _ in range(steps):
        # Deterministic INT8 rounding
        q_det = round((w_det + u_step) / delta) * delta
        w_det = q_det
        # Stochastic rounding xi(.)
        target = w_stoch + u_step
        low = math.floor(target / delta) * delta
        prob_up = (target - low) / delta
        w_stoch = (low + delta) if rng.random() < prob_up else low

    expected_final = 1.0 + steps * u_step  # -3.0
    assert abs(w_det - 1.0) < 1e-12, "Deterministic rounding must stall when |u_step| < delta/2"
    assert abs(w_stoch - expected_final) < 0.15, f"Stochastic rounding failed: {w_stoch:.4f} vs {expected_final:.4f}"

    # 4. Verify Memory Complexity Accounting (Table 1 & Section 3.2, page 5):
    # For m = 4096, n = 4096, r = 256:
    # BF16 Adam: 2*m*n (weights) + 4*m*n (FP16/BF16 moments) = 6*m*n bytes
    # BF16 GaLore: 2*m*n (weights) + 2*m*r (P_t) + 4*n*r (low-rank moments) bytes
    # Q-GaLore: 1*m*n (INT8 weights) + 0.5*m*r (INT4 P_t) + 2*n*r (INT8 low-rank moments) bytes
    M, N, R = 4096, 4096, 256
    mem_adam = 6 * M * N
    mem_galore = 2 * M * N + 2 * M * R + 4 * N * R
    mem_qgalore = 1 * M * N + int(0.5 * M * R) + 2 * N * R
    proj_saving = 1.0 - (0.5 * M * R) / (2.0 * M * R)
    total_saving_vs_adam = 1.0 - mem_qgalore / mem_adam
    assert abs(proj_saving - 0.75) < 1e-12
    assert total_saving_vs_adam > 0.79

    print(
        f"[PASS] Round 641 Q-GaLore verified: cos_early={cos_early:.4f}<gamma={gamma}<cos_stat={cos_stationary:.4f}, "
        f"SVD_calls={svd_count_adapt}/{svd_count_fixed}, cos_INT4={cos_int4:.5f}, "
        f"w_stoch={w_stoch:.3f}(target={expected_final:.1f}) vs w_det={w_det:.1f}, mem_save={total_saving_vs_adam:.1%}"
    )


if __name__ == "__main__":
    main()
