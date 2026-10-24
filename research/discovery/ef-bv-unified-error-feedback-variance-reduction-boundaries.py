#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 564: EF-BV (Condat, Yi, & Richtarik, NeurIPS 2022)."""

import itertools
import math
import random


def comp_k_kprime(vec, k, k_prime, rng):
    """comp-(k, k') compressor (Section A.2): top-k' followed by rand-k."""
    d = len(vec)
    ranked = sorted(range(d), key=lambda idx: abs(vec[idx]), reverse=True)
    top_k_prime = ranked[:k_prime]
    chosen = set(rng.sample(top_k_prime, k))
    scale = k_prime / k
    return [scale * vec[idx] if idx in chosen else 0.0 for idx in range(d)]


def vec_add(u, v):
    return [a + b for a, b in zip(u, v)]


def vec_sub(u, v):
    return [a - b for a, b in zip(u, v)]


def vec_scale(u, c):
    return [c * a for a in u]


def sq_norm(u):
    return sum(a * a for a in u)


def main():
    rng = random.Random(20220509)
    d, k, k_prime, n = 6, 1, 3, 12

    # 1. Verify Proposition 5 exact bias-variance parameters (eta, omega) for comp-(k, k')
    eta = math.sqrt((d - k_prime) / d)
    omega = (k_prime - k) / k
    omega_av = omega / n  # independent compressors across n workers

    x_test = [3.2, -1.5, 2.7, -0.4, 1.9, -0.8]
    ranked = sorted(range(d), key=lambda idx: abs(x_test[idx]), reverse=True)
    top_kp = ranked[:k_prime]
    subsets = list(itertools.combinations(top_kp, k))
    outputs = []
    for sub in subsets:
        chosen = set(sub)
        scale = k_prime / k
        outputs.append([scale * x_test[idx] if idx in chosen else 0.0 for idx in range(d)])
    mean_c = [sum(out[c] for out in outputs) / len(outputs) for c in range(d)]
    emp_bias = math.sqrt(sq_norm(vec_sub(mean_c, x_test)) / sq_norm(x_test))
    emp_var = (
        sum(sq_norm(vec_sub(out, mean_c)) for out in outputs)
        / len(outputs)
        / sq_norm(x_test)
    )
    assert emp_bias <= eta + 1e-12
    assert emp_var <= omega + 1e-12
    # Note that eta^2 + omega = 0.5 + 2.0 = 2.5 > 1, so comp-(1, 3) is NOT contractive without scaling!
    assert (eta ** 2) + omega > 1.0

    # 2. Verify Proposition 2 and Section 4 optimal scaling parameters lambda^*, nu^*
    lam_star = min((1.0 - eta) / (((1.0 - eta) ** 2) + omega), 1.0)
    nu_star = min((1.0 - eta) / (((1.0 - eta) ** 2) + omega_av), 1.0)
    r = ((1.0 - lam_star + lam_star * eta) ** 2) + (lam_star ** 2) * omega
    r_av = ((1.0 - nu_star + nu_star * eta) ** 2) + (nu_star ** 2) * omega_av
    assert 0.0 < r_av < r < 1.0
    assert nu_star > lam_star

    s_star = math.sqrt((1.0 + r) / (2.0 * r)) - 1.0
    assert abs(((1.0 + s_star) ** 2) * r - 0.5 * (r + 1.0)) < 1e-12

    L = 2.0
    gamma_efbv = 1.0 / (L + L * math.sqrt(r_av / r) * (1.0 / s_star))
    gamma_ef21 = 1.0 / (L + L * (1.0 / s_star))  # EF21 corresponds to nu = lambda = lam_star, so r_av = r
    assert gamma_efbv > gamma_ef21

    # 3. Compare EF-BV (Algorithm 1, nu = nu^*, gamma = gamma_efbv) vs scaled EF21 (nu = lam_star, gamma = gamma_ef21)
    targets = [[(i - 5.5) * 1.1 + 0.3 * c for c in range(d)] for i in range(n)]
    x_star = [sum(targets[i][c] for i in range(n)) / n for c in range(d)]

    def grad_i(i, x):
        return [L * (x[c] - targets[i][c]) for c in range(d)]

    def f_val(x):
        return 0.5 * L * sq_norm(vec_sub(x, x_star))

    def run_method(lam, nu, gamma_step, seed_val):
        local_rng = random.Random(seed_val)
        x = [2.5] * d
        h_workers = [[0.0] * d for _ in range(n)]
        h_bar = [0.0] * d
        for _ in range(250):
            d_workers = [
                comp_k_kprime(vec_sub(grad_i(i, x), h_workers[i]), k, k_prime, local_rng)
                for i in range(n)
            ]
            for i in range(n):
                h_workers[i] = vec_add(h_workers[i], vec_scale(d_workers[i], lam))
            d_bar = [sum(d_workers[i][c] for i in range(n)) / n for c in range(d)]
            g_next = vec_add(h_bar, vec_scale(d_bar, nu))
            h_bar = vec_add(h_bar, vec_scale(d_bar, lam))
            x = vec_sub(x, vec_scale(g_next, gamma_step))
        return f_val(x)

    err_efbv = run_method(lam_star, nu_star, gamma_efbv, 42)
    err_ef21 = run_method(lam_star, lam_star, gamma_ef21, 42)
    assert err_efbv < err_ef21

    print(
        f"[PASS] Round 564 EF-BV verified: r={r:.4f}, r_av={r_av:.4f}, "
        f"gamma_efbv={gamma_efbv:.5f}>gamma_ef21={gamma_ef21:.5f}, err_efbv={err_efbv:.4e}<err_ef21={err_ef21:.4e}"
    )


if __name__ == "__main__":
    main()
