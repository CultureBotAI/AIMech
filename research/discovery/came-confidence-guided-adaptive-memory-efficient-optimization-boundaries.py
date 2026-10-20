#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 598: CAME (Luo et al., ACL 2023)."""

from __future__ import annotations

import math
import random


def test_came_nmf_instability_and_memory() -> tuple[float, float, float]:
    """Verify Section 3.1-3.3 Eq. (2), Algorithm 2 rank-1 NMF of U_t, and optimizer state memory savings."""
    n, m = 4096, 4096
    # Optimizer state float counts for an n x m weight matrix:
    # Adam / LAMB: m_t (n*m) + v_t (n*m) = 2*n*m
    # Adafactor (with momentum, Alg 1): m_t (n*m) + r_t (n) + c_t (m)
    # CAME (Alg 2): m_t (n*m) + r_t (n) + c_t (m) + R_t (n) + C_t (m)
    mem_adam = 2 * n * m
    mem_adafactor = n * m + n + m
    mem_came = n * m + 2 * (n + m)
    came_vs_adam_ratio = mem_came / mem_adam
    came_vs_adafactor_overhead = (mem_came - mem_adafactor) / mem_adafactor
    assert came_vs_adam_ratio < 0.501, f"Expected CAME state < 50.1% of Adam, got {came_vs_adam_ratio}"
    assert came_vs_adafactor_overhead < 0.001, f"Expected <0.1% overhead vs Adafactor, got {came_vs_adafactor_overhead}"

    # Verify Eq. (2) rank-1 NMF reconstruction identity on an exact rank-1 instability matrix U = a b^T
    a = [0.2, 0.5, 1.1, 0.8]
    b = [0.4, 0.9, 0.3]
    U = [[av * bv for bv in b] for av in a]
    R = [sum(row) for row in U]
    C = [sum(U[i][j] for i in range(len(a))) for j in range(len(b))]
    sum_R = sum(R)
    S = [[R[i] * C[j] / sum_R for j in range(len(b))] for i in range(len(a))]
    nmf_err = max(abs(S[i][j] - U[i][j]) for i in range(len(a)) for j in range(len(b)))
    assert nmf_err < 1e-15, f"Expected exact rank-1 NMF reconstruction, got {nmf_err}"
    return came_vs_adam_ratio, came_vs_adafactor_overhead, nmf_err


def test_came_confidence_scaling_vs_adafactor() -> tuple[float, float]:
    """Verify Algorithm 2 (CAME) vs Algorithm 1 (Adafactor) under non-rank-1 second-moment curvature & noise."""
    rng = random.Random(59801)
    n, m = 4, 4
    # Target optimum theta* = 0 with non-rank-1 curvature C_{ij} so Adafactor's rank-1 v_t incurs approximation error
    curv = [
        [100.0, 1.0, 1.0, 1.0],
        [1.0, 80.0, 1.0, 1.0],
        [1.0, 1.0, 60.0, 1.0],
        [1.0, 1.0, 1.0, 40.0],
    ]
    theta0 = [[1.5 for _ in range(m)] for _ in range(n)]

    def loss_val(th: list[list[float]]) -> float:
        return 0.5 * sum(curv[i][j] * (th[i][j] ** 2) for i in range(n) for j in range(m))

    steps = 120
    beta1, beta2, beta3 = 0.9, 0.999, 0.9999
    eps1, eps2 = 1e-30, 1e-16
    d_clip = 1.0

    # 1. Adafactor (Algorithm 1, p. 4) with lr = 0.05
    th_ada = [row[:] for row in theta0]
    m_ada = [[0.0] * m for _ in range(n)]
    r_ada = [0.0] * n
    c_ada = [0.0] * m
    lr_ada = 0.05
    rng_ada = random.Random(59802)
    for _ in range(steps):
        g = [[curv[i][j] * th_ada[i][j] + rng_ada.gauss(0.0, 0.5) for j in range(m)] for i in range(n)]
        for i in range(n):
            r_ada[i] = beta2 * r_ada[i] + (1.0 - beta2) * sum(g[i][j] ** 2 + eps1 for j in range(m))
        for j in range(m):
            c_ada[j] = beta2 * c_ada[j] + (1.0 - beta2) * sum(g[i][j] ** 2 + eps1 for i in range(n))
        sum_r = sum(r_ada)
        v = [[r_ada[i] * c_ada[j] / sum_r for j in range(m)] for i in range(n)]
        u = [[g[i][j] / math.sqrt(v[i][j]) for j in range(m)] for i in range(n)]
        rms_u = math.sqrt(sum(u[i][j] ** 2 for i in range(n) for j in range(m)) / (n * m))
        clip_denom = max(1.0, rms_u / d_clip)
        u_hat = [[u[i][j] / clip_denom for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                m_ada[i][j] = beta1 * m_ada[i][j] + (1.0 - beta1) * u_hat[i][j]
                th_ada[i][j] -= lr_ada * m_ada[i][j]
    loss_ada = loss_val(th_ada)

    # 2. CAME (Algorithm 2, p. 5) with confidence-guided instability matrix U_t = (u_hat_t - m_t)^2
    th_came = [row[:] for row in theta0]
    m_came = [[0.0] * m for _ in range(n)]
    r_came = [0.0] * n
    c_came = [0.0] * m
    R_came = [0.0] * n
    C_came = [0.0] * m
    lr_came = 0.02
    rng_came = random.Random(59802)
    for _ in range(steps):
        g = [[curv[i][j] * th_came[i][j] + rng_came.gauss(0.0, 0.5) for j in range(m)] for i in range(n)]
        for i in range(n):
            r_came[i] = beta2 * r_came[i] + (1.0 - beta2) * sum(g[i][j] ** 2 + eps1 for j in range(m))
        for j in range(m):
            c_came[j] = beta2 * c_came[j] + (1.0 - beta2) * sum(g[i][j] ** 2 + eps1 for i in range(n))
        sum_r = sum(r_came)
        v = [[r_came[i] * c_came[j] / sum_r for j in range(m)] for i in range(n)]
        u = [[g[i][j] / math.sqrt(v[i][j]) for j in range(m)] for i in range(n)]
        rms_u = math.sqrt(sum(u[i][j] ** 2 for i in range(n) for j in range(m)) / (n * m))
        clip_denom = max(1.0, rms_u / d_clip)
        u_hat = [[u[i][j] / clip_denom for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                m_came[i][j] = beta1 * m_came[i][j] + (1.0 - beta1) * u_hat[i][j]
        U = [[(u_hat[i][j] - m_came[i][j]) ** 2 for j in range(m)] for i in range(n)]
        for i in range(n):
            R_came[i] = beta3 * R_came[i] + (1.0 - beta3) * sum(U[i][j] + eps2 for j in range(m))
        for j in range(m):
            C_came[j] = beta3 * C_came[j] + (1.0 - beta3) * sum(U[i][j] + eps2 for i in range(n))
        sum_R = sum(R_came)
        S = [[R_came[i] * C_came[j] / sum_R for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                th_came[i][j] -= (lr_came / math.sqrt(S[i][j])) * m_came[i][j]
    loss_came = loss_val(th_came)

    assert loss_came < 0.2 * loss_ada, f"Expected CAME loss ({loss_came}) < 0.2 * Adafactor loss ({loss_ada})"
    return loss_came, loss_ada


def main() -> None:
    mem_ratio, mem_ovh, nmf_err = test_came_nmf_instability_and_memory()
    loss_came, loss_ada = test_came_confidence_scaling_vs_adafactor()
    print(
        f"[PASS] Round 598 CAME verified: mem_vs_adam={mem_ratio:.4f}, ovh_vs_adaf={mem_ovh:.5f}, "
        f"nmf_err={nmf_err:.2e}, loss_came={loss_came:.4e}<loss_ada={loss_ada:.4e}"
    )


if __name__ == "__main__":
    main()
