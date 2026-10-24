"""Constructed mathematical boundary and operator-equivalence verification for Round 609:
Quasi-Hyperbolic Momentum (QHM) and QHAdam (Ma & Yarats, ICLR 2019, arXiv:1810.06801).

Verifies:
1. QHM discounted sum representation (Eqs. 3-5, 7, p. 2, 16, 18) and linear operator
   transition matrix A_QHM (Appendix C.2, Eq. 11, p. 20-21):
   theta_t = theta_0 - alpha * sum_{i=1}^t (1 - nu * beta^i) * grad_{t-i}.
2. Fact A.2 limit covariance scaling factor of QHWMA (Appendix A.6 & G, p. 17, 31):
   rho(nu, beta) = (1 - nu * beta)^2 + [nu * beta * (1 - beta)]^2 / (1 - beta^2),
   recovering Fact A.1 (1 - beta)/(1 + beta) at nu = 1, and satisfying tight lower bound (1 - nu)^2.
3. Exact trajectory bijections with Synthesized Nesterov Variants (SNV, Appendix C.4, p. 22-23),
   Triple Momentum (Van Scoy et al. 2018), PID control (Appendix C.3, p. 21-22), and AccSGD
   (Appendix C.5, p. 23-24), plus proof that AccSGD cannot recover NAG because xi_NAG > sqrt(kappa).
4. Fact F.1 tight per-coordinate step-size upper bound for QHAdam and Adam (Appendix F, Eqs. 14-19, p. 28-29):
   verifies that the worst-case gradient sequence x_i (Eq. 17) achieves the exact analytical bound
   and exceeds Kingma & Ba (2015)'s claimed bound max{1, (1 - beta1)/sqrt(1 - beta2)} for Adam (7.2709 vs 3.1623),
   while setting nu2 < 1 in QHAdam tightens the maximum per-step update.
"""

from __future__ import annotations

import math
import random


def verify_qhm_unrolled_and_covariance() -> tuple[float, float, float]:
    rng = random.Random(20261019)
    alpha = 0.25
    beta = 0.92
    nu = 0.7
    T = 25
    theta0 = 1.35
    grads = [rng.uniform(-2.0, 2.0) for _ in range(T)]

    # Online QHM recursion (Eqs. 3-4)
    g = 0.0
    theta = theta0
    for t in range(T):
        g = beta * g + (1.0 - beta) * grads[t]
        theta = theta - alpha * ((1.0 - nu) * grads[t] + nu * g)

    # Unrolled linear operator formula (Appendix C.2, Eq. 11)
    theta_unrolled = theta0 - alpha * sum(
        (1.0 - nu * (beta ** i)) * grads[T - i] for i in range(1, T + 1)
    )
    unrolled_err = abs(theta - theta_unrolled)
    assert unrolled_err < 1e-14, f"Unrolled QHM mismatch: {unrolled_err}"

    # Fact A.2 covariance scaling factor (Appendix G, p. 31)
    t_large = 2000
    weights_sq_sum = ((1.0 - nu * beta) ** 2) + sum(
        (nu * (1.0 - beta) * (beta ** i)) ** 2 for i in range(1, t_large + 1)
    )
    rho_analytic = ((1.0 - nu * beta) ** 2) + ((nu * beta * (1.0 - beta)) ** 2) / (1.0 - beta * beta)
    cov_err = abs(weights_sq_sum - rho_analytic)
    assert cov_err < 1e-15, f"Fact A.2 mismatch: {cov_err}"

    # At nu = 1, recovers Fact A.1: (1 - beta)^2 / (1 - beta^2) = (1 - beta) / (1 + beta)
    rho_ewma = ((1.0 - beta) ** 2) / (1.0 - beta * beta)
    rho_nu1 = ((1.0 - 1.0 * beta) ** 2) + ((1.0 * beta * (1.0 - beta)) ** 2) / (1.0 - beta * beta)
    assert abs(rho_ewma - rho_nu1) < 1e-16

    # Tight lower bound (1 - nu)^2 on rho as beta -> 1^-
    beta_near1 = 0.999999
    rho_near1 = ((1.0 - nu * beta_near1) ** 2) + ((nu * beta_near1 * (1.0 - beta_near1)) ** 2) / (
        1.0 - beta_near1 * beta_near1
    )
    lb_gap = rho_near1 - ((1.0 - nu) ** 2)
    assert 0.0 < lb_gap < 1e-5
    return unrolled_err, cov_err, lb_gap


def verify_bijections_snv_pid_accsgd() -> tuple[float, float, float, float]:
    rng = random.Random(20261020)
    alpha = 0.18
    beta = 0.88
    nu = 0.65
    theta0 = -0.75
    T = 20
    grads = [rng.uniform(-1.5, 1.5) for _ in range(T)]

    # Run QHM (with g_0 = 0)
    g = 0.0
    theta_qhm = theta0
    qhm_traj = []
    for gr in grads:
        g = beta * g + (1.0 - beta) * gr
        theta_qhm = theta_qhm - alpha * ((1.0 - nu) * gr + nu * g)
        qhm_traj.append(theta_qhm)

    # 1. SNV bijection (Appendix C.4, p. 22-23):
    # gamma = alpha * (1 - beta), beta1 = beta, beta2 = (1 - nu) * beta / (1 - beta)
    gamma = alpha * (1.0 - beta)
    beta1 = beta
    beta2 = (1.0 - nu) * beta / (1.0 - beta)
    xi_curr = theta0
    xi_prev = theta0
    snv_traj = []
    for gr in grads:
        xi_next = xi_curr - gamma * gr + beta1 * (xi_curr - xi_prev)
        theta_snv = xi_next + beta2 * (xi_next - xi_curr)
        xi_prev, xi_curr = xi_curr, xi_next
        snv_traj.append(theta_snv)

    snv_err = max(abs(a - b) for a, b in zip(qhm_traj, snv_traj))
    assert snv_err < 1e-14, f"SNV bijection error: {snv_err}"

    # 2. PID bijection (Appendix C.3, p. 21-22):
    # k_P = -alpha * nu * beta / (1 - beta), k_I = alpha, k_D = alpha * nu * beta^2 / (1 - beta)^2
    k_P = -alpha * nu * beta / (1.0 - beta)
    k_I = alpha
    k_D = alpha * nu * (beta * beta) / ((1.0 - beta) ** 2)
    e_prev = 0.0
    v_pid = 0.0
    w_pid = 0.0
    pid_traj = []
    for gr in grads:
        e_curr = -gr
        v_pid = beta * v_pid + (1.0 - beta) * (e_curr - e_prev)
        w_pid = w_pid + e_curr
        theta_pid = theta0 + k_P * e_curr + k_I * w_pid + k_D * v_pid
        e_prev = e_curr
        pid_traj.append(theta_pid)

    pid_err = max(abs(a - b) for a, b in zip(qhm_traj, pid_traj))
    assert pid_err < 1e-14, f"PID bijection error: {pid_err}"

    # 3. AccSGD bijection (Appendix C.5, p. 23-24):
    eps = 0.7
    delta = alpha * (1.0 - nu)
    kappa = (beta + eps) * (eps * nu + 1.0) / ((1.0 - nu) * (1.0 - beta))
    xi = (eps * nu + 1.0) / (eps * (1.0 - nu))
    w_bar = theta0
    w_curr = theta0
    accsgd_traj = []
    for gr in grads:
        c1 = (eps * eps * xi) / kappa
        w_bar = (1.0 - c1) * w_bar + c1 * (w_curr - (kappa * delta / eps) * gr)
        w_curr = (kappa / (kappa + eps * xi)) * (w_curr - delta * gr) + (
            eps * xi / (kappa + eps * xi)
        ) * w_bar
        accsgd_traj.append(w_curr)

    accsgd_err = max(abs(a - b) for a, b in zip(qhm_traj, accsgd_traj))
    assert accsgd_err < 1e-14, f"AccSGD bijection error: {accsgd_err}"

    # Verify proof that AccSGD cannot recover NAG: xi_NAG > sqrt(kappa) for eps in (0, 1)
    kappa_test = 25.0
    xi_nag = (1.0 - eps + math.sqrt(4.0 * kappa_test + ((1.0 - eps) ** 2))) / (2.0 * eps)
    nag_gap = xi_nag - math.sqrt(kappa_test)
    assert nag_gap > 0.0, f"Expected xi_NAG > sqrt(kappa), got gap={nag_gap}"
    return snv_err, pid_err, accsgd_err, nag_gap


def verify_fact_f1_qhadam_update_bound() -> tuple[float, float, float, float]:
    # Fact F.1 (Appendix F, Eqs. 14-19, p. 28-30)
    beta1 = 0.9
    beta2 = 0.999
    t = 40

    def worst_case_update(nu1: float, nu2: float) -> tuple[float, float]:
        # Worst-case gradient sequence from Eq. 17:
        # x_t = (1 - nu1 * beta1) / (1 - nu2 * beta2)
        # x_{t-i} = (nu1 * (1 - beta1) * beta1^i) / (nu2 * (1 - beta2) * beta2^i) for 1 <= i <= t
        x_t = (1.0 - nu1 * beta1) / (1.0 - nu2 * beta2)
        g_tilde = (1.0 - nu1 * beta1) * x_t
        s_tilde = (1.0 - nu2 * beta2) * (x_t * x_t)
        for i in range(1, t + 1):
            x_ti = (nu1 * (1.0 - beta1) * (beta1 ** i)) / (nu2 * (1.0 - beta2) * (beta2 ** i))
            g_tilde += nu1 * (1.0 - beta1) * (beta1 ** i) * x_ti
            s_tilde += nu2 * (1.0 - beta2) * (beta2 ** i) * (x_ti * x_ti)
        empirical = abs(g_tilde) / math.sqrt(s_tilde)
        analytic = math.sqrt(
            ((1.0 - nu1 * beta1) ** 2) / (1.0 - nu2 * beta2)
            + (((nu1 * beta1 * (1.0 - beta1)) ** 2) * (1.0 - ((beta1 * beta1 / beta2) ** t)))
            / (nu2 * (1.0 - beta2) * (beta2 - beta1 * beta1))
        )
        return empirical, analytic

    emp_adam, ana_adam = worst_case_update(1.0, 1.0)
    f1_err = abs(emp_adam - ana_adam)
    assert f1_err < 1e-14

    # Limit bound Eq. 19 for vanilla Adam (nu1 = nu2 = 1):
    adam_limit_bound = (1.0 - beta1) * math.sqrt(beta2 / ((1.0 - beta2) * (beta2 - beta1 * beta1)))
    kingma_ba_claimed = max(1.0, (1.0 - beta1) / math.sqrt(1.0 - beta2))
    assert adam_limit_bound > 7.27 > kingma_ba_claimed  # ~7.2709 vs ~3.1623

    # QHAdam stability bound tightening with nu2 < 1 (Figure 3, p. 30: nu1=0.8, beta1=0.95, beta2=0.98)
    b1_nmt, b2_nmt, nu1_nmt = 0.95, 0.98, 0.8

    def limit_bound(nu2_val: float) -> float:
        return math.sqrt(
            ((1.0 - nu1_nmt * b1_nmt) ** 2) / (1.0 - nu2_val * b2_nmt)
            + ((nu1_nmt * b1_nmt * (1.0 - b1_nmt)) ** 2)
            / (nu2_val * (1.0 - b2_nmt) * (b2_nmt - b1_nmt * b1_nmt))
        )

    bound_nu2_1 = limit_bound(1.0)
    bound_nu2_07 = limit_bound(0.7)
    assert bound_nu2_07 < bound_nu2_1, f"Expected nu2=0.7 to tighten bound: {bound_nu2_07} vs {bound_nu2_1}"
    return f1_err, adam_limit_bound, kingma_ba_claimed, bound_nu2_07 / bound_nu2_1


if __name__ == "__main__":
    u_err, c_err, lb_gap = verify_qhm_unrolled_and_covariance()
    snv_err, pid_err, acc_err, nag_gap = verify_bijections_snv_pid_accsgd()
    f1_err, adam_b, kb_b, nmt_rat = verify_fact_f1_qhadam_update_bound()
    print(
        f"[PASS] Round 609 QHM/QHAdam verified: "
        f"unrolled_err={u_err:.2e}, cov_err={c_err:.2e}, snv_err={snv_err:.2e}, pid_err={pid_err:.2e}, "
        f"acc_err={acc_err:.2e}, xi_nag_gap={nag_gap:.4f}>0, f1_err={f1_err:.2e}, "
        f"adam_bound={adam_b:.4f}>kb={kb_b:.4f}, nmt_bound_ratio={nmt_rat:.4f}<1"
    )
