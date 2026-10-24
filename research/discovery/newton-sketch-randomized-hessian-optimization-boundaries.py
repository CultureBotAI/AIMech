#!/usr/bin/env python3
"""Constructed boundary and verification checks for Round 225:
Newton Sketch: Randomized Hessian-Projected Second-Order Optimization and
Sketched Interior-Point Barrier Methods (Pilanci & Wainwright 2017,
SIAM J. Optim. 27(1):205-245, arXiv:1505.02250v1, DOI:10.1137/15M1021106).

Verifies:
1. Local Linear-Quadratic and Super-Linear Convergence (Section 3.3 & 6.1,
   Theorem 1, Corollary 1, Eq. 14 & 27):
   - Basic inequality recursion ||Delta^{t+1}||_2 <= (6*beta*Z_1^t / (gamma*Z_2^t)) ||Delta^t||_2
     + (4*L / (gamma*Z_2^t)) ||Delta^t||_2^2 for ||Delta^t||_2 < gamma/(2L).
   - Empirical verification of Partial Newton Sketch on a regularized logistic
     regression objective f(x) = sum_{i=1}^n log(1 + exp(-y_i <a_i, x>)) + (lambda/2)||x||_2^2
     comparing fixed-sketch Newton Sketch (linear-quadratic convergence) and
     increasing-sketch Newton Sketch (Corollary 1 super-linear convergence).
2. Global Self-Concordant Two-Phase Analysis (Section 4.1-4.2 & 6.2,
   Algorithms 1-2, Theorems 2-3, Lemmas 2-7, Eqs. 18, 37, 41-46):
   - Exact verification of the Phase I decrement parameter eta and guaranteed
     per-step function decrease nu(epsilon, a, b) in Eq. (18) and Lemma 3(a),
     including the exact positivity threshold
     eps < (sqrt(2*(1-a)) - 1) / (sqrt(2*(1-a)) + 1) (<= 3 - 2*sqrt(2) ~= 0.17157)
     where 1 - 0.5*((1+eps)/(1-eps))^2 - a > 0.
   - Exact verification of the Phase II Newton-decrement evolution bound in
     Lemma 6 (Eq. 44a & 46):
     lambda_f(x_NSK) <= ((1+eps)*lambda_f(x)^2 + eps*lambda_f(x)) / (1 - (1+eps)*lambda_f(x))^2 <= (16/25)*lambda_f(x)
     for all eps in (0, 1/2) when (1+eps)*lambda_f(x) <= 1/16.
3. Sketched Interior-Point Barrier Central Path and Sparse Tangent-Cone Width
   (Section 3.2, 4.3, 5.1, Appendix C, Algorithm 3, Theorem 4, Lemma 8):
   - Verification of central-path log-barrier suboptimality f_0(x_hat(tau)) - f_0(x^*) <= r/tau
     on a polytope linear program.
   - Verification of the l_1-ball tangent-cone inclusion ||z||_1 <= 2*sqrt(s)*||z||_2
     at an s-sparse optimizer x^* used in Lemma 8.
"""

from __future__ import annotations

import json
import math
import random


def dot(u: list[float], v: list[float]) -> float:
    return sum(ui * vi for ui, vi in zip(u, v))


def norm2(u: list[float]) -> float:
    return math.sqrt(dot(u, u))


def solve_spd(A: list[list[float]], b: list[float]) -> list[float]:
    """Solve A x = b for symmetric positive definite A via Cholesky."""
    d = len(b)
    L = [[0.0] * d for _ in range(d)]
    for i in range(d):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                val = A[i][i] - s
                L[i][j] = math.sqrt(max(val, 1e-15))
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]
    y = [0.0] * d
    for i in range(d):
        y[i] = (b[i] - sum(L[i][k] * y[k] for k in range(i))) / L[i][i]
    x = [0.0] * d
    for i in range(d - 1, -1, -1):
        x[i] = (y[i] - sum(L[k][i] * x[k] for k in range(i + 1, d))) / L[i][i]
    return x


def check_local_linear_quadratic_and_partial_sketch() -> dict:
    """Verify Theorem 1, Corollary 1, and Partial Sketch (Eq. 8) on regularized logistic regression."""
    rng = random.Random(20261018)
    n, d = 120, 6
    lam = 0.25
    A = [[rng.gauss(0.0, 1.0) / math.sqrt(d) for _ in range(d)] for _ in range(n)]
    x_true = [0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
    y = []
    for i in range(n):
        margin = dot(A[i], x_true)
        prob = 1.0 / (1.0 + math.exp(-margin))
        y.append(1.0 if rng.random() < prob else -1.0)

    def grad(x: list[float]) -> list[float]:
        g = [lam * xj for xj in x]
        for i in range(n):
            u = y[i] * dot(A[i], x)
            sig = 1.0 / (1.0 + math.exp(u))
            coeff = -y[i] * sig
            for j in range(d):
                g[j] += coeff * A[i][j]
        return g

    def hess_sqrt_rows(x: list[float]) -> list[list[float]]:
        """Rows of nabla^2 f_0(x)^{1/2} in R^{n x d}."""
        rows = []
        for i in range(n):
            u = y[i] * dot(A[i], x)
            p = 1.0 / (1.0 + math.exp(-u))
            w = math.sqrt(p * (1.0 - p))
            rows.append([w * A[i][j] for j in range(d)])
        return rows

    def exact_hess(x: list[float]) -> list[list[float]]:
        rows = hess_sqrt_rows(x)
        H = [[lam if i == j else 0.0 for j in range(d)] for i in range(d)]
        for r in rows:
            for i in range(d):
                for j in range(d):
                    H[i][j] += r[i] * r[j]
        return H

    # Compute exact minimizer x^* via 12 steps of exact Newton
    x_star = [0.0] * d
    for _ in range(12):
        g = grad(x_star)
        H = exact_hess(x_star)
        step = solve_spd(H, g)
        x_star = [x_star[j] - step[j] for j in range(d)]
    grad_norm_star = norm2(grad(x_star))

    # Run Partial Newton Sketch (sketching f_0 with m=36 Rademacher rows, keeping lam*I exact)
    x_psk = [0.0] * d
    m_fixed = 36
    psk_errors = [norm2([x_psk[j] - x_star[j] for j in range(d)])]
    for _ in range(8):
        g = grad(x_psk)
        rows = hess_sqrt_rows(x_psk)
        scale = 1.0 / math.sqrt(m_fixed)
        S_rows = [[0.0] * d for _ in range(m_fixed)]
        for k in range(m_fixed):
            for i in range(n):
                s_ki = scale if rng.random() < 0.5 else -scale
                for j in range(d):
                    S_rows[k][j] += s_ki * rows[i][j]
        Q = [[lam if i == j else 0.0 for j in range(d)] for i in range(d)]
        for sr in S_rows:
            for i in range(d):
                for j in range(d):
                    Q[i][j] += sr[i] * sr[j]
        step = solve_spd(Q, g)
        x_psk = [x_psk[j] - step[j] for j in range(d)]
        psk_errors.append(norm2([x_psk[j] - x_star[j] for j in range(d)]))

    # Verify Corollary 1 super-linear schedule m(t) = ceil(24 * (1 + log(1+t))^2)
    x_super = [0.0] * d
    super_errors = [norm2([x_super[j] - x_star[j] for j in range(d)])]
    for t in range(1, 9):
        g = grad(x_super)
        rows = hess_sqrt_rows(x_super)
        m_t = int(math.ceil(24 * (1.0 + math.log(1.0 + t)) ** 2))
        scale = 1.0 / math.sqrt(m_t)
        S_rows = [[0.0] * d for _ in range(m_t)]
        for k in range(m_t):
            for i in range(n):
                s_ki = scale if rng.random() < 0.5 else -scale
                for j in range(d):
                    S_rows[k][j] += s_ki * rows[i][j]
        Q = [[lam if i == j else 0.0 for j in range(d)] for i in range(d)]
        for sr in S_rows:
            for i in range(d):
                for j in range(d):
                    Q[i][j] += sr[i] * sr[j]
        step = solve_spd(Q, g)
        x_super = [x_super[j] - step[j] for j in range(d)]
        super_errors.append(norm2([x_super[j] - x_star[j] for j in range(d)]))

    # Verify algebraic step in Section 6.1 (p. 23):
    gamma, beta, L = 1.0, 3.0, 2.0
    delta_norm = gamma / (8.0 * L)
    z1, z2 = 0.05, 0.9
    exact_pre = (2.0 * z1 * (beta + L * delta_norm)) / (z2 * (gamma - L * delta_norm)) * delta_norm + (
        2.0 * L / ((gamma - L * delta_norm) * z2)
    ) * (delta_norm**2)
    bound_27 = (6.0 * beta * z1 / (gamma * z2)) * delta_norm + (4.0 * L / (gamma * z2)) * (delta_norm**2)

    passed = (
        grad_norm_star < 1e-12
        and psk_errors[-1] < 1e-2 * psk_errors[0]
        and super_errors[-1] < 1e-6 * super_errors[0]
        and super_errors[-1] < 1e-3 * psk_errors[-1]
        and exact_pre <= bound_27 + 1e-15
    )
    return {
        "passed": passed,
        "grad_norm_star": grad_norm_star,
        "psk_initial_error": psk_errors[0],
        "psk_final_error": psk_errors[-1],
        "super_final_error": super_errors[-1],
        "exact_pre_bound_27": exact_pre,
        "bound_27": bound_27,
    }


def check_self_concordant_two_phase_bounds() -> dict:
    """Verify Lemma 3, Lemma 4, Lemma 5, Lemma 6, and Eq. (18) for self-concordant functions."""
    a = 0.1
    b = 0.5
    eps_max_pos = (math.sqrt(2.0 * (1.0 - a)) - 1.0) / (math.sqrt(2.0 * (1.0 - a)) + 1.0)
    phase1_checks = []
    phase2_checks = []

    for eps in [0.02, 0.05, 0.10, 0.14]:
        ratio = (1.0 + eps) / (1.0 - eps)
        eta = (1.0 / 8.0) * (1.0 - 0.5 * (ratio**2) - a) / (ratio**3)
        nu = a * b * (eta**2) / (1.0 + ratio * eta)

        # Verify Eq. (45) on p. 27: ((1+eps)/(1-eps)) * eta <= 1/16
        lhs_45 = ratio * eta
        # Verify Step (40a) on p. 26: u_hat = 1 / (1 + ratio * lambda_tilde)
        lam_tilde = 1.5 * eta
        u_hat = 1.0 / (1.0 + ratio * lam_tilde)
        eps_prime = 2.0 * eps / (1.0 - eps)
        dec_upper = (
            -u_hat * (lam_tilde**2)
            - u_hat * (1.0 + eps_prime) * lam_tilde
            - math.log(1.0 - u_hat * (1.0 + eps_prime) * lam_tilde)
        )
        line_search_rhs = -a * u_hat * (lam_tilde**2)
        phase1_checks.append(
            eps < eps_max_pos
            and eta > 0.0
            and nu > 0.0
            and lhs_45 <= (1.0 / 16.0) + 1e-15
            and dec_upper <= line_search_rhs + 1e-15
        )

    # Verify that for eps = 0.20 in (eps_max_pos, 0.25), Eq. (18) gives eta < 0
    ratio_20 = 1.2 / 0.8
    eta_20 = (1.0 / 8.0) * (1.0 - 0.5 * (ratio_20**2) - a) / (ratio_20**3)

    # Verify Phase II Lemma 6 (Eq. 44a and Eq. 46) for eps in (0, 1/2):
    for eps in [0.05, 0.10, 0.20, 0.40]:
        for lam_f in [0.005, 0.01, 0.03, (1.0 / 16.0) / (1.0 + eps)]:
            next_lam_bound = ((1.0 + eps) * (lam_f**2) + eps * lam_f) / (
                (1.0 - (1.0 + eps) * lam_f) ** 2
            )
            contracted = (16.0 / 25.0) * lam_f
            phase2_checks.append(next_lam_bound <= contracted + 1e-15)

    passed = all(phase1_checks) and (eta_20 < 0.0) and all(phase2_checks)
    return {
        "passed": passed,
        "eps_max_positive_eta_for_a_0_1": eps_max_pos,
        "eta_at_eps_0_20": eta_20,
        "num_phase1_checks": len(phase1_checks),
        "num_phase2_checks": len(phase2_checks),
    }


def check_barrier_central_path_and_sparse_cone() -> dict:
    """Verify barrier central path suboptimality and Lemma 8 l1-tangent cone inclusion."""
    rng = random.Random(42)
    d = 20
    s = 4
    cone_checks = []
    for _ in range(50):
        z_support = [rng.gauss(0.0, 1.0) for _ in range(s)]
        l1_supp = sum(abs(v) for v in z_support)
        raw_comp = [abs(rng.gauss(0.0, 1.0)) for _ in range(d - s)]
        sum_comp = sum(raw_comp)
        scale = (0.95 * l1_supp / sum_comp) if sum_comp > 0 else 0.0
        z_comp = [v * scale for v in raw_comp]
        z = z_support + z_comp
        l1_norm = sum(abs(v) for v in z)
        l2_norm = norm2(z)
        cone_checks.append(l1_norm <= 2.0 * math.sqrt(s) * l2_norm + 1e-12)

    c = [1.0, 2.0]
    r = 4
    f0_star = -3.0
    central_path_checks = []
    for tau in [2.0, 10.0, 50.0, 200.0]:
        x_tau = []
        for cj in c:
            a_q = tau * cj
            root = (2.0 - math.sqrt(4.0 + 4.0 * (a_q**2))) / (2.0 * a_q)
            x_tau.append(root)
        gap = dot(c, x_tau) - f0_star
        central_path_checks.append(0.0 < gap <= (r / tau) + 1e-12)

    passed = all(cone_checks) and all(central_path_checks)
    return {
        "passed": passed,
        "num_cone_checks": len(cone_checks),
        "num_central_path_checks": len(central_path_checks),
    }


def main() -> None:
    res1 = check_local_linear_quadratic_and_partial_sketch()
    res2 = check_self_concordant_two_phase_bounds()
    res3 = check_barrier_central_path_and_sparse_cone()
    all_passed = res1["passed"] and res2["passed"] and res3["passed"]
    summary = {
        "concept_id": "AIMech:NewtonSketchRandomizedHessianProjectedOptimization",
        "all_passed": all_passed,
        "local_linear_quadratic_and_partial_sketch": res1,
        "self_concordant_two_phase_bounds": res2,
        "barrier_central_path_and_sparse_cone": res3,
    }
    print(json.dumps(summary, indent=2))
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
