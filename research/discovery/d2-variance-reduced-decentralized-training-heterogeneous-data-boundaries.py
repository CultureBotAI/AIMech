"""Constructed boundary verification for Round 427: D^2 (Tang et al., ICML 2018, arXiv:1803.07068).

Verifies:
1. Section 4 (Algorithm 1, Equations 3-4) & Section 5 (Theorem 2):
   On heterogeneous quadratic objectives f_i(x) = (1/2)(x - b_i)^2 with sum_i b_i = 0 (so global x^* = 0
   and outer gradient heterogeneity zeta^2 = (1/n) sum_i ||nabla f_i(0)||^2 = (1/n) sum_i b_i^2 > 0):
   - Standard D-PSGD X_{t+1} = (X_t - gamma G(X_t)) W cannot converge to consensus at x^* = 0 under a
     constant step size gamma > 0: its fixed point X_infty satisfies ||X_infty||_F^2 > 0 proportional to
     gamma^2 * zeta^2 / (1 - lambda_2(W))^2!
   - D^2 recurrence X_{t+1} = (2 X_t - X_{t-1} - gamma G(X_t) + gamma G(X_{t-1})) W with X_1 = (X_0 - gamma G(X_0)) W
     completely cancels the heterogeneous stationary bias G(X^*) - G(X^*) = 0 and converges geometrically
     to the exact global optimum X_t -> 0 as long as lambda_n(W) > -1/3!
2. Lemma 6 & Lemma 7 (Supplemental Material, Eq. 13-14):
   For eigenvalue lambda_n <= -1/3, the characteristic root v_n = lambda_n - sqrt(lambda_n^2 - lambda_n)
   satisfies |v_n| >= 1 (with |v_n| = 1 at lambda_n = -1/3), causing the eigenmode y_t^{(n)} to diverge!
"""

from __future__ import annotations


def mat_vec_W(x: list[float], w: list[list[float]]) -> list[float]:
    n = len(x)
    return [sum(x[j] * w[j][i] for j in range(n)) for i in range(n)]


def main() -> None:
    # 1. Verify Lemma 6 & Lemma 7 characteristic root boundary at lambda_n = -1/3
    lam_crit = -1.0 / 3.0
    v_crit = lam_crit - ((lam_crit * lam_crit - lam_crit) ** 0.5)
    assert abs(abs(v_crit) - 1.0) < 1e-15, f"At lambda=-1/3, |v| must equal 1.0, got {abs(v_crit)}"

    lam_stable = -0.25  # > -1/3
    v_stable = lam_stable - ((lam_stable * lam_stable - lam_stable) ** 0.5)
    lam_unstable = -0.50  # < -1/3
    v_unstable = lam_unstable - ((lam_unstable * lam_unstable - lam_unstable) ** 0.5)
    assert abs(v_stable) < 1.0 and abs(v_unstable) > 1.0

    # 2. Compare D-PSGD vs D^2 on heterogeneous deterministic quadratics f_i(x) = 0.5 * (x - b_i)^2
    # 3 workers with b = [3.0, -1.0, -2.0] -> sum(b) = 0 -> x^* = 0, zeta^2 = (9 + 1 + 4)/3 = 14/3 > 0
    b = [3.0, -1.0, -2.0]
    n = 3
    # Doubly stochastic ring mixing matrix W with eigenvalues 1, 0.25, 0.25 (all > -1/3)
    w = [
        [0.5, 0.25, 0.25],
        [0.25, 0.5, 0.25],
        [0.25, 0.25, 0.5],
    ]
    gamma = 0.2
    T = 80

    # Run D-PSGD from X_0 = [0, 0, 0]
    x_dpsgd = [0.0] * n
    for _ in range(T):
        g = [x_dpsgd[i] - b[i] for i in range(n)]
        step = [x_dpsgd[i] - gamma * g[i] for i in range(n)]
        x_dpsgd = mat_vec_W(step, w)
    dpsgd_err = sum(v * v for v in x_dpsgd) ** 0.5

    # Run D^2 (Algorithm 1) from X_0 = [0, 0, 0]
    x_prev = [0.0] * n
    g_prev = [x_prev[i] - b[i] for i in range(n)]
    x_curr = mat_vec_W([x_prev[i] - gamma * g_prev[i] for i in range(n)], w)
    for _ in range(1, T):
        g_curr = [x_curr[i] - b[i] for i in range(n)]
        inside = [2.0 * x_curr[i] - x_prev[i] - gamma * g_curr[i] + gamma * g_prev[i] for i in range(n)]
        x_next = mat_vec_W(inside, w)
        x_prev, g_prev = x_curr, g_curr
        x_curr = x_next
    d2_err = sum(v * v for v in x_curr) ** 0.5

    assert d2_err < 1e-12, f"D^2 failed to eliminate heterogeneous stationary drift: {d2_err}"
    assert dpsgd_err > 0.2, f"D-PSGD unexpectedly eliminated heterogeneous bias: {dpsgd_err}"

    print(
        f"[PASS] Round 427 D^2 (Tang et al. 2018): |v(-1/3)|={abs(v_crit):.4f}==1.0 "
        f"(|v(-0.25)|={abs(v_stable):.4f}<1<|v(-0.50)|={abs(v_unstable):.4f}), "
        f"d2_err={d2_err:.1e} << dpsgd_heterogeneity_err={dpsgd_err:.4f}"
    )


if __name__ == "__main__":
    main()
