#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 415:
Natural Compression and Natural Dithering for Distributed Optimization (Horváth et al. 2022).
"""

import math


def nat_comp_moments(t: float) -> tuple[float, float, float]:
    """Return exact (E[C_nat(t)], E[C_nat(t)^2], Var[C_nat(t)] / t^2) from Definition 1 & Theorem 3."""
    assert t != 0.0
    abs_t = abs(t)
    sgn = 1.0 if t > 0 else -1.0
    a = math.floor(math.log2(abs_t))
    low = float(2 ** a)
    high = float(2 ** (a + 1))
    if abs_t == low:
        return t, t * t, 0.0
    p = (high - abs_t) / low
    mean = sgn * (p * low + (1.0 - p) * high)
    second_moment = p * (low ** 2) + (1.0 - p) * (high ** 2)
    rel_var = (second_moment - t * t) / (t * t)
    return mean, second_moment, rel_var


def dithering_coord_var(xi: float, levels: list[float]) -> float:
    """Exact variance E[(xi_hat - xi)^2] for 0 <= xi <= 1 rounded unbiasedly between adjacent levels."""
    assert 0.0 <= xi <= 1.0
    if xi == 0.0:
        return 0.0
    for u in range(len(levels) - 1):
        l_low = levels[u]
        l_high = levels[u + 1]
        if l_low <= xi <= l_high:
            if l_high == l_low:
                return 0.0
            p = (l_high - xi) / (l_high - l_low)
            second = p * (l_low ** 2) + (1.0 - p) * (l_high ** 2)
            return second - xi * xi
    raise ValueError(f"xi={xi} out of range")


def main() -> None:
    # 1. Theorem 3: C_nat is unbiased and has tight worst-case relative variance omega = 1/8 at |t| = (4/3)*2^a
    t_worst = 4.0 / 3.0
    mean_w, sec_w, rel_var_w = nat_comp_moments(t_worst)
    assert abs(mean_w - t_worst) < 1e-15
    assert abs(sec_w / (t_worst ** 2) - 9.0 / 8.0) < 1e-15
    assert abs(rel_var_w - 1.0 / 8.0) < 1e-15

    # Check across a dense grid in [1, 2]
    max_rel_var = max(nat_comp_moments(1.0 + k / 1000.0)[2] for k in range(1001))
    assert max_rel_var <= 1.0 / 8.0 + 1e-15

    # 2. Theorem 4: Unbiased integer rounding C_int has unbounded relative variance as x -> 0+
    x_small = 1e-4
    c_int_rel_var = (x_small - x_small ** 2) / (x_small ** 2)
    assert abs(c_int_rel_var - (1.0 / x_small - 1.0)) < 1e-9
    assert c_int_rel_var > 9998.0

    # 3. Theorem 5 & Theorem 15: Composition C_nat o S^q has omega = (9/8)*(d/q - 1) + 1/8 = 9d/(8q) - 1
    d, q = 16, 4
    omega_sq = d / q - 1.0
    omega_nat = 1.0 / 8.0
    omega_comp = omega_nat * omega_sq + omega_nat + omega_sq
    assert abs(omega_comp - (9.0 * d / (8.0 * q) - 1.0)) < 1e-15

    # 4. Theorem 7 & Theorem 8: Natural dithering D_nat^{p,s} vs Standard dithering D_sta^{p,s}
    # For s = 5 levels: natural levels are [0, 2^-4, 2^-3, 2^-2, 2^-1, 1], standard levels are [0, 1/5, 2/5, 3/5, 4/5, 1]
    s = 5
    nat_levels = [0.0] + [2.0 ** (u - s + 1) for u in range(s)]
    sta_levels = [u / float(s) for u in range(s + 1)]
    # Evaluate on a vector x with small coordinates where natural dithering has exponentially finer resolution
    x = [0.08, 0.07, 0.06, 0.09, 0.95]
    norm_p = math.sqrt(sum(xi * xi for xi in x))
    var_nat = (norm_p ** 2) * sum(dithering_coord_var(abs(xi) / norm_p, nat_levels) for xi in x)
    var_sta = (norm_p ** 2) * sum(dithering_coord_var(abs(xi) / norm_p, sta_levels) for xi in x)
    omega_nat_bound = 1.0 / 8.0 + (len(x) ** 0.5) * (2.0 ** (1 - s)) * min(1.0, (len(x) ** 0.5) * (2.0 ** (1 - s)))
    assert var_nat / (norm_p ** 2) <= omega_nat_bound
    assert var_nat < 0.25 * var_sta, f"Expected D_nat variance << D_sta variance, got {var_nat} vs {var_sta}"

    print(
        f"[PASS] Natural Compression boundaries verified: omega(C_nat)={rel_var_w:.6f} (1/8), "
        f"omega(C_nat o S^q)={omega_comp:.4f}, var_nat={var_nat:.5f} < var_sta={var_sta:.5f}"
    )


if __name__ == "__main__":
    main()
