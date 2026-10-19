#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 413:
MOON: Model-Contrastive Federated Learning (Li, He, & Song, CVPR 2021).
"""

import math


def norm(v: list[float]) -> float:
    return math.sqrt(sum(vi * vi for vi in v))


def cosine_sim(u: list[float], v: list[float]) -> float:
    return sum(ui * vi for ui, vi in zip(u, v)) / (norm(u) * norm(v))


def grad_cosine_sim(z: list[float], v: list[float]) -> list[float]:
    nz = norm(z)
    nv = norm(v)
    sim = cosine_sim(z, v)
    return [(vi / nv - sim * (zi / nz)) / nz for zi, vi in zip(z, v)]


def moon_loss(z: list[float], z_glob: list[float], z_prev: list[float], tau: float) -> float:
    s_glob = cosine_sim(z, z_glob) / tau
    s_prev = cosine_sim(z, z_prev) / tau
    m = max(s_glob, s_prev)
    log_denom = m + math.log(math.exp(s_glob - m) + math.exp(s_prev - m))
    return -(s_glob - log_denom)


def moon_grad_z(z: list[float], z_glob: list[float], z_prev: list[float], tau: float) -> list[float]:
    s_glob = cosine_sim(z, z_glob) / tau
    s_prev = cosine_sim(z, z_prev) / tau
    # p_prev = exp(s_prev) / (exp(s_glob) + exp(s_prev)) = 1 / (1 + exp(s_glob - s_prev))
    p_prev = 1.0 / (1.0 + math.exp(s_glob - s_prev))
    g_glob = grad_cosine_sim(z, z_glob)
    g_prev = grad_cosine_sim(z, z_prev)
    return [(p_prev / tau) * (gp - gg) for gg, gp in zip(g_glob, g_prev)]


def main() -> None:
    tau = 0.5
    z = [0.6, 0.8, -0.2]
    z_glob = [1.0, 0.2, 0.5]
    z_prev = [-0.4, 0.9, -0.5]

    # 1. Boundary case: when z_glob == z_prev, l_con == log(2) and grad_z l_con == 0 (reduces to FedAvg)
    loss_eq = moon_loss(z, z_glob, z_glob, tau)
    grad_eq = moon_grad_z(z, z_glob, z_glob, tau)
    assert abs(loss_eq - math.log(2.0)) < 1e-12
    assert max(abs(g) for g in grad_eq) < 1e-12

    # 2. Verify analytical gradient against central finite differences
    g_analytic = moon_grad_z(z, z_glob, z_prev, tau)
    eps = 1e-7
    g_fd = []
    for i in range(len(z)):
        z_plus = list(z)
        z_minus = list(z)
        z_plus[i] += eps
        z_minus[i] -= eps
        g_fd.append((moon_loss(z_plus, z_glob, z_prev, tau) - moon_loss(z_minus, z_glob, z_prev, tau)) / (2.0 * eps))
    fd_err = max(abs(ga - gn) for ga, gn in zip(g_analytic, g_fd))
    assert fd_err < 1e-8, f"Gradient mismatch: {fd_err}"

    # 3. Verify representation drift reduction under gradient descent on l_con
    sim_glob_init = cosine_sim(z, z_glob)
    sim_prev_init = cosine_sim(z, z_prev)
    z_cur = list(z)
    for _ in range(25):
        g = moon_grad_z(z_cur, z_glob, z_prev, tau)
        z_cur = [zi - 0.1 * gi for zi, gi in zip(z_cur, g)]
    sim_glob_final = cosine_sim(z_cur, z_glob)
    sim_prev_final = cosine_sim(z_cur, z_prev)
    assert sim_glob_final > sim_glob_init + 0.35
    assert sim_prev_final < sim_prev_init - 0.25

    print(
        f"[PASS] MOON boundaries verified: l_con(z_glob=z_prev)={loss_eq:.6f} (log2={math.log(2.0):.6f}), "
        f"grad_fd_err={fd_err:.2e}, sim_glob: {sim_glob_init:.3f}->{sim_glob_final:.3f}, "
        f"sim_prev: {sim_prev_init:.3f}->{sim_prev_final:.3f}"
    )


if __name__ == "__main__":
    main()
