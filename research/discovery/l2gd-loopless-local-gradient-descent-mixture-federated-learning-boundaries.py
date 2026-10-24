#!/usr/bin/env python3
"""Boundary verification for Round 445: L2GD (Hanzely & Richtarik 2020, arXiv:2002.05516)."""
import math

def solve_exact_l2gd(a_list, b_list, lam):
    # Each client i has f_i(x_i) = 0.5 * a_i * (x_i - b_i)^2
    # Optimality condition (Theorem 3.2, Eq. 5): a_i * (x_i - b_i) + lam * (x_i - x_bar) = 0
    # => x_i(lam) = (a_i * b_i + lam * x_bar) / (a_i + lam)
    # Averaging over i=1..n solves for x_bar(lam) in closed form:
    n = len(a_list)
    if lam == 0.0:
        x_opt = list(b_list)
        return x_opt, sum(x_opt) / n
    num = sum(a_list[i] * b_list[i] / (a_list[i] + lam) for i in range(n)) / n
    den = 1.0 - sum(lam / (a_list[i] + lam) for i in range(n)) / n
    x_bar = num / den
    x_opt = [(a_list[i] * b_list[i] + lam * x_bar) / (a_list[i] + lam) for i in range(n)]
    return x_opt, x_bar

def eval_f_psi(a_list, b_list, x_vec):
    n = len(a_list)
    x_bar = sum(x_vec) / n
    f_val = sum(0.5 * a_list[i] * ((x_vec[i] - b_list[i]) ** 2) for i in range(n)) / n
    psi_val = sum(0.5 * ((x_vec[i] - x_bar) ** 2) for i in range(n)) / n
    return f_val, psi_val

def main():
    a_list = [2.0, 4.0, 3.0, 5.0]
    b_list = [-3.0, 1.0, 4.0, -2.0]
    n = len(a_list)
    L = max(a_list)
    mu = min(a_list)
    x_inf = sum(a_list[i] * b_list[i] for i in range(n)) / sum(a_list)
    f_inf, _ = eval_f_psi(a_list, b_list, [x_inf] * n)

    # Verify Theorem 3.1 monotonicity and Theorem 3.2 structural identity across lambda
    lams = [0.5, 2.0, 10.0, 50.0]
    f_vals = []
    psi_vals = []
    max_thm32_err = 0.0
    max_zero_sum_grad_err = 0.0
    for lam in lams:
        x_opt, x_bar = solve_exact_l2gd(a_list, b_list, lam)
        f_v, psi_v = eval_f_psi(a_list, b_list, x_opt)
        f_vals.append(f_v)
        psi_vals.append(psi_v)
        grads = [a_list[i] * (x_opt[i] - b_list[i]) for i in range(n)]
        # Theorem 3.2 Eq. (5): x_i(lam) = x_bar(lam) - (1/lam) * grad f_i(x_i(lam))
        for i in range(n):
            err = abs(x_opt[i] - (x_bar - grads[i] / lam))
            if err > max_thm32_err:
                max_thm32_err = err
        grad_sum_err = abs(sum(grads))
        if grad_sum_err > max_zero_sum_grad_err:
            max_zero_sum_grad_err = grad_sum_err

    for k in range(len(lams) - 1):
        assert psi_vals[k] >= psi_vals[k + 1]
        assert f_vals[k] <= f_vals[k + 1] <= f_inf
    assert max_thm32_err < 1e-14
    assert max_zero_sum_grad_err < 1e-13

    # Verify Corollary 4.6 optimal communication probability p^* = lam / (L + lam)
    lam_test = 1.25  # L = 5.0 -> p^* = 1.25 / 6.25 = 0.20
    p_star = lam_test / (L + lam_test)
    comm_l2gd = 2.0 * (lam_test / (lam_test + L)) * (L / mu)
    comm_gd = 2.0 * (L / mu)
    assert abs(p_star - 0.20) < 1e-12
    assert comm_l2gd < 0.25 * comm_gd
    print(f"[PASS] Round 445 L2GD (Hanzely & Richtarik 2020): thm32_err={max_thm32_err:.2e}, grad_sum_err={max_zero_sum_grad_err:.2e}, p_star={p_star:.2f}, comm_ratio={comm_l2gd/comm_gd:.2f}")

if __name__ == "__main__":
    main()
