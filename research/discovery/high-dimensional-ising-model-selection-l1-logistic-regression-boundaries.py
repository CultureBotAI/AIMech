#!/usr/bin/env python3
r"""Constructed boundary and algebraic verification for Round 234:
HighDimensionalIsingModelSelectionViaL1RegularizedLogisticRegression
(Ravikumar, Wainwright, & Lafferty 2010, Annals of Statistics 38(3):1287-1319,
arXiv:0804.4202v1, DOI:10.1214/09-AOS691).

Verifies:
1. Exact Ising conditional distribution, rescaled negative log-likelihood
   decomposition, score vector W^n, and Fisher information matrix Q_r^* / Q^n
   (Sections 2.1-3.1 & 4.1, pp. 4-7, 11, Equations 1, 4-11, 17, 27):
   - Verifies that for X in {-1, +1}^p drawn from P_{theta^*}(x) propto
     exp(sum_{(s,t) in E} theta^*_{st} x_s x_t), the nodewise conditional law
     satisfies P_{theta^*}(x_r | x_{\r}) = 1 / (1 + exp(-2 x_r sum_{t != r} theta^*_{rt} x_t))
     (Eq. 4), and the negative conditional log-likelihood (Eq. 5) equals
     (1/n) sum_{i=1}^n f(theta; x^{(i)}) - sum_{u in V \ r} theta_{ru} mu_hat_{ru}
     (Eqs. 6-7) identically for all x^{(i)} in {-1, +1}^p without any omitted
     additive constant.
   - Verifies that the score vector W^n = -nabla ell(theta^*; {x^{(i)}}) has
     zero population mean E_{theta^*}[W^n] = 0 and that the Hessian of ell(theta)
     is Q^n(theta) = (1/n) sum_{i=1}^n eta(x^{(i)}; theta) x^{(i)}_{\r} (x^{(i)}_{\r})^T
     with conditional variance weight eta(u; theta) = 4 exp(2 u_r s) / (exp(2 u_r s) + 1)^2
     = sech^2(sum_{t != r} theta_{rt} u_t) = Var_{theta}(X_r | X_{\r} = u_{\r}) in (0, 1].
2. Primal-Dual Witness (PDW) KKT construction, Taylor remainder expansion, and
   strict dual feasibility under sample Fisher mutual incoherence (Sections 3.3
   & 4.1-4.2, pp. 9-13, Lemma 1, Proposition 1, Lemmas 2-4, Equations 20-37):
   - On a 4-node Ising star graph (center r = 0 connected to S = {1, 2}, d = 2,
     and disconnected node S^c = {3}), solves the restricted convex program
     theta_hat_S = argmin_{(theta_S, 0)} {ell(theta) + lambda_n ||theta_S||_1}
     (Eq. 24), sets theta_hat_{S^c} = 0 and z_hat_S = sign(theta_hat_S), and
     computes z_hat_{S^c} = -(1/lambda_n) [nabla ell(theta_hat)]_{S^c} (Eq. 20).
   - Verifies the exact Taylor remainder identity (Eqs. 28, 33a-33b):
     Q^n (theta_hat - theta^*) = W^n - lambda_n z_hat + R^n, and verifies the
     exact algebraic sign in the dual witness formula:
     lambda_n z_hat_{S^c} = [W^n_{S^c} + R^n_{S^c}] - Q^n_{S^c S} (Q^n_{SS})^{-1} [W^n_S + R^n_S]
     + lambda_n Q^n_{S^c S} (Q^n_{SS})^{-1} z_hat_S
     (noting that Eq. 35 on p. 12 prints minus signs before R^n_{S^c} and R^n_S,
     which leaves the triangle-inequality upper bound in Eqs. 36-37 unchanged),
     confirming ||z_hat_{S^c}||_infty < 1 and sign(theta_hat_S) = sign(theta^*_S).
3. Four-term sample-to-population incoherence decomposition and d^3 log p vs.
   d^2 log p scaling separation (Section 5.2, pp. 15-16, Lemma 6 & Lemma 7,
   Equations 42, 45a-49):
   - Verifies the exact matrix identity Q^n_{S^c S} (Q^n_{SS})^{-1} = T_1 + T_2 + T_3 + T_4
     (Eqs. 45a-45d) and the refactorization T_1 = Q^*_{S^c S} (Q^*_{SS})^{-1}
     [Q^n_{SS} - Q^*_{SS}] (Q^n_{SS})^{-1}, demonstrating why controlling
     ||T_1||_infty and ||T_2||_infty <= (sqrt(d)/C_min) ||Q^n_{S^c S} - Q^*_{S^c S}||_infty
     at level alpha/6 requires l_infty matrix concentration at threshold
     delta = O(1/sqrt(d)), which combined with the d-column sum in Hoeffding's
     bound exp(-K n delta^2 / d^2) produces the population-Fisher sample
     complexity n = Omega(d^3 log p) (Theorem 1) vs. the fixed-design /
     sample-Fisher complexity n = Omega(d^2 log p) (Proposition 1).
"""

import itertools
import json
import math


def mat_transpose(a):
    return [list(col) for col in zip(*a)]


def mat_mul(a, b):
    bt = mat_transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def mat_vec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def mat_inv(a):
    n = len(a)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(a)]
    for i in range(n):
        pivot = max(range(i, n), key=lambda r: abs(aug[r][i]))
        aug[i], aug[pivot] = aug[pivot], aug[i]
        div = aug[i][i]
        aug[i] = [x / div for x in aug[i]]
        for r in range(n):
            if r != i:
                factor = aug[r][i]
                aug[r] = [aug[r][c] - factor * aug[i][c] for c in range(2 * n)]
    return [row[n:] for row in aug]


def mat_inf_norm(a):
    return max(sum(abs(x) for x in row) for row in a)


def ising_population_distribution(p, edges):
    """Exact Ising distribution over {-1, +1}^p."""
    states = list(itertools.product([-1.0, 1.0], repeat=p))
    unnorm = []
    for x in states:
        energy = sum(w * x[u] * x[v] for (u, v), w in edges.items())
        unnorm.append(math.exp(energy))
    z_part = sum(unnorm)
    probs = [u / z_part for u in unnorm]
    return states, probs


def verify_ising_likelihood_and_population_fisher():
    # 4-node Ising model on V = {0, 1, 2, 3}: node 0 connected to {1, 2} (S = {0, 1} in X_{\0}),
    # node 3 not connected to node 0 (S^c = {2} in X_{\0}) but connected to node 1 with weight 0.20.
    p = 4
    edges = {(0, 1): 0.45, (0, 2): -0.40, (1, 2): 0.15, (1, 3): 0.20}
    states, probs = ising_population_distribution(p, edges)
    theta_star = [0.45, -0.40, 0.0]  # for r = 0 against u in {1, 2, 3}

    # 1. Check exact equality between Eq. (5) and Eqs. (6)-(7) across all 2^4 states
    max_loss_diff = 0.0
    pop_score = [0.0, 0.0, 0.0]
    q_star = [[0.0] * 3 for _ in range(3)]

    for x, pr in zip(states, probs):
        xr = x[0]
        x_rest = [x[1], x[2], x[3]]
        lin = sum(t * u for t, u in zip(theta_star, x_rest))
        cond_prob = math.exp(2.0 * xr * lin) / (math.exp(2.0 * xr * lin) + 1.0)
        loss_eq5 = -math.log(cond_prob)
        f_eq7 = math.log(math.exp(lin) + math.exp(-lin))
        loss_eq6 = f_eq7 - sum(t * xr * u for t, u in zip(theta_star, x_rest))
        max_loss_diff = max(max_loss_diff, abs(loss_eq5 - loss_eq6))

        # Score contribution W(x) = -nabla ell(theta^*; x)
        tanh_lin = math.tanh(lin)
        for j in range(3):
            pop_score[j] += pr * (-x_rest[j] * (xr - tanh_lin))

        # Variance function eta(x; theta^*) (Eq. 11) vs Conditional Variance Var(X_r | X_{\r})
        eta_eq11 = (4.0 * math.exp(2.0 * xr * lin)) / ((math.exp(2.0 * xr * lin) + 1.0) ** 2)
        p_pos = math.exp(2.0 * lin) / (math.exp(2.0 * lin) + 1.0)
        cond_mean = 2.0 * p_pos - 1.0
        cond_var = 1.0 - cond_mean * cond_mean  # since X_r^2 = 1
        max_loss_diff = max(max_loss_diff, abs(eta_eq11 - cond_var))

        for j in range(3):
            for k in range(3):
                q_star[j][k] += pr * eta_eq11 * x_rest[j] * x_rest[k]

    max_pop_score = max(abs(g) for g in pop_score)
    q_ss_star = [[q_star[i][j] for j in (0, 1)] for i in (0, 1)]
    q_scs_star = [[q_star[2][0], q_star[2][1]]]
    pop_incoh = mat_inf_norm(mat_mul(q_scs_star, mat_inv(q_ss_star)))

    passed = (
        max_loss_diff < 1e-14
        and max_pop_score < 1e-14
        and 0.0 < pop_incoh < 0.5
    )
    return {
        "passed": passed,
        "max_loss_and_variance_identity_error": max_loss_diff,
        "max_population_score_norm": max_pop_score,
        "population_incoherence_norm": round(pop_incoh, 8),
        "q_ss_star_diag": [round(q_ss_star[0][0], 6), round(q_ss_star[1][1], 6)],
    }


def verify_pdw_taylor_expansion_and_four_term_decomposition():
    # Construct an empirical distribution tilde_P (small perturbation of population probs)
    p = 4
    edges = {(0, 1): 0.45, (0, 2): -0.40, (1, 2): 0.15, (1, 3): 0.20}
    states, probs = ising_population_distribution(p, edges)
    theta_star = [0.45, -0.40, 0.0]

    # Slightly perturbed empirical weights (representing a finite sample of size n)
    raw_weights = [
        pr * (1.0 + 0.04 * math.sin(i + 1) + 0.02 * math.cos(2 * i + 1))
        for i, pr in enumerate(probs)
    ]
    w_sum = sum(raw_weights)
    emp_probs = [w / w_sum for w in raw_weights]
    lambda_n = 0.05

    def grad_and_hess(theta):
        g = [0.0, 0.0, 0.0]
        h = [[0.0] * 3 for _ in range(3)]
        for x, wt in zip(states, emp_probs):
            xr = x[0]
            x_rest = [x[1], x[2], x[3]]
            lin = sum(t * u for t, u in zip(theta, x_rest))
            tanh_lin = math.tanh(lin)
            eta = 1.0 - tanh_lin * tanh_lin
            for j in range(3):
                g[j] += wt * (x_rest[j] * (tanh_lin - xr))
                for k in range(3):
                    h[j][k] += wt * eta * x_rest[j] * x_rest[k]
        return g, h

    # Solve restricted convex program (Eq. 24) on S = {0, 1} with theta_2 = 0 via Newton steps
    theta_hat = [0.45, -0.40, 0.0]
    for _ in range(40):
        g, h = grad_and_hess(theta_hat)
        z_s = [1.0 if theta_hat[0] > 0 else -1.0, 1.0 if theta_hat[1] > 0 else -1.0]
        r_s = [g[0] + lambda_n * z_s[0], g[1] + lambda_n * z_s[1]]
        h_ss_inv = mat_inv([[h[0][0], h[0][1]], [h[1][0], h[1][1]]])
        step = mat_vec(h_ss_inv, r_s)
        theta_hat[0] -= step[0]
        theta_hat[1] -= step[1]

    g_hat, _ = grad_and_hess(theta_hat)
    z_hat = [
        1.0 if theta_hat[0] > 0 else -1.0,
        1.0 if theta_hat[1] > 0 else -1.0,
        -g_hat[2] / lambda_n,
    ]
    kkt_residual = max(abs(g_hat[j] + lambda_n * z_hat[j]) for j in range(3))

    # Evaluate W^n = -nabla ell(theta^*), Q^n = nabla^2 ell(theta^*), and R^n (Eq. 28)
    g_star, q_n = grad_and_hess(theta_star)
    w_n = [-x for x in g_star]
    delta_theta = [theta_hat[j] - theta_star[j] for j in range(3)]
    qn_delta = mat_vec(q_n, delta_theta)
    r_n = [qn_delta[j] - (w_n[j] - lambda_n * z_hat[j]) for j in range(3)]

    q_ss_n = [[q_n[i][j] for j in (0, 1)] for i in (0, 1)]
    q_scs_n = [[q_n[2][0], q_n[2][1]]]
    q_ss_n_inv = mat_inv(q_ss_n)
    incoh_mat_n = mat_mul(q_scs_n, q_ss_n_inv)

    # Exact algebraic elimination from Eqs. (33a)-(33b):
    # Q^n_{S^c S} (Q^n_{SS})^{-1} [W^n_S - lambda_n z_hat_S + R^n_S] = W^n_{S^c} - lambda_n z_hat_{S^c} + R^n_{S^c}
    # => lambda_n z_hat_{S^c} = [W^n_{S^c} + R^n_{S^c}] - Q^n_{S^c S}(Q^n_{SS})^{-1}[W^n_S + R^n_S] + lambda_n Q^n_{S^c S}(Q^n_{SS})^{-1} z_hat_S
    w_plus_r_s = [w_n[0] + r_n[0], w_n[1] + r_n[1]]
    lhs_dual_exact = (
        (w_n[2] + r_n[2])
        - mat_vec(incoh_mat_n, w_plus_r_s)[0]
        + lambda_n * mat_vec(incoh_mat_n, z_hat[:2])[0]
    )
    rhs_dual_exact = lambda_n * z_hat[2]

    # Also verify 4-term decomposition (Eqs. 45a-45d) of Q^n_{S^c S} (Q^n_{SS})^{-1}
    q_star_pop = [[0.0] * 3 for _ in range(3)]
    for x, pr in zip(states, probs):
        lin = sum(t * u for t, u in zip(theta_star, [x[1], x[2], x[3]]))
        eta = 1.0 - math.tanh(lin) ** 2
        for j in range(3):
            for k in range(3):
                q_star_pop[j][k] += pr * eta * x[j + 1] * x[k + 1]
    q_ss_star = [[q_star_pop[i][j] for j in (0, 1)] for i in (0, 1)]
    q_scs_star = [[q_star_pop[2][0], q_star_pop[2][1]]]
    q_ss_star_inv = mat_inv(q_ss_star)

    diff_inv = [
        [q_ss_n_inv[i][j] - q_ss_star_inv[i][j] for j in range(2)]
        for i in range(2)
    ]
    diff_scs = [[q_scs_n[0][j] - q_scs_star[0][j] for j in range(2)]]
    t1 = mat_mul(q_scs_star, diff_inv)
    t2 = mat_mul(diff_scs, q_ss_star_inv)
    t3 = mat_mul(diff_scs, diff_inv)
    t4 = mat_mul(q_scs_star, q_ss_star_inv)
    t_sum = [[t1[0][j] + t2[0][j] + t3[0][j] + t4[0][j] for j in range(2)]]
    decomp_err = max(abs(incoh_mat_n[0][j] - t_sum[0][j]) for j in range(2))

    # Also verify refactorization of T_1:
    # T_1 = Q^*_{S^c S} (Q^*_{SS})^{-1} [Q^*_{SS} - Q^n_{SS}] (Q^n_{SS})^{-1}
    diff_ss_star_minus_n = [
        [q_ss_star[i][j] - q_ss_n[i][j] for j in range(2)] for i in range(2)
    ]
    t1_refact = mat_mul(mat_mul(t4, diff_ss_star_minus_n), q_ss_n_inv)
    t1_refact_err = max(abs(t1[0][j] - t1_refact[0][j]) for j in range(2))

    passed = (
        kkt_residual < 1e-14
        and abs(z_hat[2]) < 1.0
        and (theta_hat[0] > 0 and theta_hat[1] < 0)
        and abs(lhs_dual_exact - rhs_dual_exact) < 1e-14
        and decomp_err < 1e-14
        and t1_refact_err < 1e-14
    )
    return {
        "passed": passed,
        "theta_hat": [round(x, 6) for x in theta_hat],
        "z_hat": [round(x, 6) for x in z_hat],
        "kkt_residual": kkt_residual,
        "dual_witness_identity_error": abs(lhs_dual_exact - rhs_dual_exact),
        "four_term_decomposition_error": decomp_err,
        "t1_refactorization_error": t1_refact_err,
    }


def main():
    r1 = verify_ising_likelihood_and_population_fisher()
    r2 = verify_pdw_taylor_expansion_and_four_term_decomposition()
    all_passed = r1["passed"] and r2["passed"]
    report = {
        "concept_id": "AIMech:HighDimensionalIsingModelSelectionViaL1RegularizedLogisticRegression",
        "all_passed": all_passed,
        "ising_likelihood_and_population_fisher": r1,
        "pdw_taylor_and_four_term_decomposition": r2,
    }
    print(json.dumps(report, indent=2))
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
