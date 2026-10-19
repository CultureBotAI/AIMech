#!/usr/bin/env python3
"""Boundary and verification script for Round 340:
A Universal Catalyst for First-Order Optimization
(Lin, Mairal, & Harchaoui, NeurIPS 2015 pp. 3384-3392, arXiv:1506.02186; JMLR 2018).
"""

import math
import sys


def main():
    # 1. Verify Canonical Estimate Sequence Identities (Appendix A.1, Lemma A.6 & Lemma A.8, Equations 20-28, pp. 11-14)
    mu = 0.02
    L = 2.0
    kappa = L - 2.0 * mu  # Optimal choice for full gradient descent (Section 4.1, p. 6)
    q = mu / (mu + kappa)

    # Choose alpha_0 in (0, 1) (test general alpha_0 != sqrt(q) to verify full recurrence)
    alpha = 0.35
    gamma = (alpha * ((kappa + mu) * alpha - mu)) / (1.0 - alpha)
    x_prev = [2.4, -1.7, 0.9]
    y_prev = x_prev[:]
    v_prev = x_prev[:]

    max_eq27_err = 0.0
    max_eq28_err = 0.0
    max_eq26_err = 0.0
    for k in range(1, 25):
        # Simulate an inner iterate x_k of auxiliary problem G_k
        x_curr = [0.7 * y_prev[i] + 0.05 * math.sin(k + i) for i in range(3)]
        # Update gamma_k = (1 - alpha_{k-1}) gamma_{k-1} + alpha_{k-1} mu (Equation 20)
        gamma_curr = (1.0 - alpha) * gamma + alpha * mu
        # Identity (27): 1 - (kappa + mu) alpha_{k-1}^2 / gamma_k == 0
        max_eq27_err = max(max_eq27_err, abs(1.0 - (kappa + mu) * (alpha ** 2) / gamma_curr))

        # Update v_k via Equation 21:
        v_curr = [
            (
                (1.0 - alpha) * gamma * v_prev[i]
                + alpha * mu * x_curr[i]
                - alpha * kappa * (y_prev[i] - x_curr[i])
            )
            / gamma_curr
            for i in range(3)
        ]
        # Identity (28): v_k == (1 / alpha_{k-1}) (x_k - (1 - alpha_{k-1}) x_{k-1})
        v_eq28 = [(x_curr[i] - (1.0 - alpha) * x_prev[i]) / alpha for i in range(3)]
        max_eq28_err = max(
            max_eq28_err,
            math.sqrt(sum((v_curr[i] - v_eq28[i]) ** 2 for i in range(3))),
        )

        # Solve alpha_k^2 = (1 - alpha_k) alpha_{k-1}^2 + q * alpha_k (Algorithm 1 line 4):
        # alpha_k^2 + (alpha_{k-1}^2 - q) alpha_k - alpha_{k-1}^2 = 0
        b_coef = (alpha ** 2) - q
        alpha_next = 0.5 * (-b_coef + math.sqrt(b_coef * b_coef + 4.0 * (alpha ** 2)))
        beta_k = (alpha * (1.0 - alpha)) / (alpha * alpha + alpha_next)
        y_curr = [x_curr[i] + beta_k * (x_curr[i] - x_prev[i]) for i in range(3)]

        # Identity (26) at step k+1 (Lemma A.8, p. 13):
        # (1 - alpha_k) gamma_k v_k - alpha_k kappa y_k + alpha_k (1 - alpha_k) (kappa + mu) x_k == 0
        eq26_vec = [
            (1.0 - alpha_next) * gamma_curr * v_curr[i]
            - alpha_next * kappa * y_curr[i]
            + alpha_next * (1.0 - alpha_next) * (kappa + mu) * x_curr[i]
            for i in range(3)
        ]
        max_eq26_err = max(max_eq26_err, math.sqrt(sum(val * val for val in eq26_vec)))

        alpha, gamma = alpha_next, gamma_curr
        x_prev, y_prev, v_prev = x_curr, y_curr, v_curr

    # 2. Verify Lemma A.10 (Non-Negative Sequence Bound, Equations 30-31, p. 15)
    S_seq = [1.0 + 0.4 * k for k in range(15)]
    a_seq = [0.2 / (k + 1) for k in range(15)]
    u_seq = [0.8]
    for k in range(1, 15):
        # Construct worst-case u_k satisfying u_k^2 = S_k + sum_{i=1}^k a_i u_i:
        # u_k^2 - a_k u_k - (S_k + sum_{i=1}^{k-1} a_i u_i) = 0
        prev_sum = S_seq[k] + sum(a_seq[i] * u_seq[i] for i in range(1, k))
        uk = 0.5 * (a_seq[k] + math.sqrt(a_seq[k] ** 2 + 4.0 * prev_sum))
        u_seq.append(uk)
    lemma_a10_holds = all(
        S_seq[k] + sum(a_seq[i] * u_seq[i] for i in range(1, k + 1))
        <= (math.sqrt(S_seq[k]) + sum(a_seq[1 : k + 1])) ** 2 + 1e-12
        for k in range(1, 15)
    )

    # 3. Verify Theorem 3.1 (Strongly Convex Catalyst with Inexact Inner Minimization, Eq. 7, p. 4)
    # and the failure boundary when inner error epsilon_k = const fails to decay geometrically:
    mu_sc = 0.01
    L_sc = 2.0
    kappa_sc = 0.24  # q = mu / (mu + kappa) = 0.01 / 0.25 = 0.04, sqrt(q) = 0.20 >> q = 0.04
    q_sc = mu_sc / (mu_sc + kappa_sc)
    rho_sc = 0.9 * math.sqrt(q_sc)  # = 0.18
    eigs = [mu_sc, 0.25, L_sc]
    x0 = [3.0, -2.0, 1.5]
    F0 = 0.5 * sum(eigs[i] * (x0[i] ** 2) for i in range(3))

    # Unaccelerated proximal point (rate 1 - q_sc = 0.96 per outer step) for K = 35 outer steps:
    x_unacc = x0[:]
    for _ in range(35):
        x_unacc = [(kappa_sc / (eigs[i] + kappa_sc)) * x_unacc[i] for i in range(3)]
    F_unacc = 0.5 * sum(eigs[i] * (x_unacc[i] ** 2) for i in range(3))

    # Catalyst with inexact inner iterates x_k satisfying G_k(x_k) - G_k^* <= epsilon_k = (2/9) F0 (1 - rho)^k
    # vs failure boundary with non-decaying constant inner error epsilon_const = 0.05:
    alpha_cat = math.sqrt(q_sc)
    beta_cat = (alpha_cat * (1.0 - alpha_cat)) / (alpha_cat * alpha_cat + alpha_cat)
    x_cat = x0[:]
    y_cat = x0[:]
    x_stall = x0[:]
    y_stall = x0[:]
    thm31_holds = True
    for k in range(1, 36):
        eps_k = 1e-5 * F0 * ((1.0 - rho_sc) ** k)  # Satisfies Theorem 3.1 hypothesis eps_k <= (2/9) F0 (1 - rho)^k
        # Exact minimizer of G_k(x) is x_k^*[i] = (kappa_sc / (eigs[i] + kappa_sc)) * y_{k-1}[i];
        # perturb by inner error achieving G_k(x_k) - G_k^* = eps_k:
        x_next = [
            (kappa_sc / (eigs[i] + kappa_sc)) * y_cat[i] + math.sqrt(2.0 * eps_k / (3.0 * (eigs[i] + kappa_sc)))
            for i in range(3)
        ]
        y_cat = [x_next[i] + beta_cat * (x_next[i] - x_cat[i]) for i in range(3)]
        x_cat = x_next
        F_k = 0.5 * sum(eigs[i] * (x_cat[i] ** 2) for i in range(3))
        thm31_bound = (8.0 / ((math.sqrt(q_sc) - rho_sc) ** 2)) * ((1.0 - rho_sc) ** (k + 1)) * F0
        if F_k > thm31_bound + 1e-12:
            thm31_holds = False

        # Non-decaying inner error epsilon_const = 0.05:
        eps_const = 0.05
        x_next_stall = [
            (kappa_sc / (eigs[i] + kappa_sc)) * y_stall[i] + math.sqrt(2.0 * eps_const / (3.0 * (eigs[i] + kappa_sc)))
            for i in range(3)
        ]
        y_stall = [x_next_stall[i] + beta_cat * (x_next_stall[i] - x_stall[i]) for i in range(3)]
        x_stall = x_next_stall

    F_cat = 0.5 * sum(eigs[i] * (x_cat[i] ** 2) for i in range(3))
    F_stall = 0.5 * sum(eigs[i] * (x_stall[i] ** 2) for i in range(3))

    # 4. Verify Theorem 3.3 & Lemma B.3 (Convex mu = 0 Case, Equations 11 & 18, pp. 5, 19):
    # With alpha_0 = (sqrt(5)-1)/2 and mu = 0, verify 2/(k+2)^2 <= lambda_k <= 4/(k+2)^2 for all k >= 0
    alpha_0_cvx = 0.5 * (math.sqrt(5.0) - 1.0)
    lam_k = 1.0
    alpha_cvx = alpha_0_cvx
    lemma_b3_holds = True
    for k in range(30):
        low_b = 2.0 / ((k + 2) ** 2)
        high_b = 4.0 / ((k + 2) ** 2)
        if not (low_b - 1e-14 <= lam_k <= high_b + 1e-14):
            lemma_b3_holds = False
        lam_k *= 1.0 - alpha_cvx
        # Next alpha_cvx satisfies alpha_{k+1}^2 = (1 - alpha_{k+1}) alpha_k^2
        a2 = alpha_cvx * alpha_cvx
        alpha_cvx = 0.5 * (-a2 + math.sqrt(a2 * a2 + 4.0 * a2))

    ok = (
        max_eq27_err < 1e-14
        and max_eq28_err < 1e-13
        and max_eq26_err < 1e-13
        and lemma_a10_holds
        and lemma_b3_holds
        and thm31_holds
        and F_cat < 0.05 * F_unacc
        and F_stall > 20.0 * F_cat
    )
    if not ok:
        print(
            f"Verification failed: eq27={max_eq27_err}, eq28={max_eq28_err}, eq26={max_eq26_err}, "
            f"a10={lemma_a10_holds}, b3={lemma_b3_holds}, thm31={thm31_holds}, "
            f"F_cat={F_cat}, F_unacc={F_unacc}, F_stall={F_stall}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(
        f"[PASS] Round 340 Catalyst Acceleration (Lin, Mairal, & Harchaoui 2015): "
        f"max_eq27_err={max_eq27_err:.2e}, max_eq28_err={max_eq28_err:.2e}, "
        f"max_eq26_err={max_eq26_err:.2e}, F_cat={F_cat:.4e} << F_unacc={F_unacc:.4e}, F_stall={F_stall:.4e}"
    )


if __name__ == "__main__":
    main()
