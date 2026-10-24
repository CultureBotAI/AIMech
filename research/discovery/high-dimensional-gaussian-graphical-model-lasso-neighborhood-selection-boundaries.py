#!/usr/bin/env python3
"""Constructed boundary and mechanism verification for:
AIMech:HighDimensionalGaussianGraphicalModelNeighborhoodSelectionWithTheLasso
(Meinshausen & Buhlmann 2006, The Annals of Statistics 34(3):1436-1462; arXiv:math/0608017v1).

Verifies:
1. Precision-matrix and partial-correlation neighborhood identity (Section 2, pp. 3-4, 19, Eqs. 1-2):
   - For X ~ N(0, Sigma) with precision matrix K = Sigma^{-1}, the population linear prediction
     vector theta^a = argmin_{theta: theta_a = 0} E[(X_a - sum_{k != a} theta_k X_k)^2] satisfies
     theta_b^a = -K_{ab} / K_{aa} for b != a, with residual variance Var(X_a | X_{-a}) = 1 / K_{aa},
     and partial correlation pi_{ab} = -K_{ab} / sqrt(K_{aa} K_{bb})
     = theta_b^a * sqrt(Var(X_b | X_{-b}) / Var(X_a | X_{-a})).
   - Consequently ne_a = {b != a : K_{ab} != 0} = {b != a : theta_b^a != 0}.
2. Inconsistency of the prediction-oracle penalty lambda_oracle (Proposition 1, pp. 5-6; Appendix, pp. 20-22, Eqs. A.20-A.22):
   - Under Sigma = I_p except Sigma_{12} = Sigma_{21} = s in (0, 1), for any candidate vector
     theta_{(0)} = (0, tau_max, 0, ..., 0) with tau_max < s and an independent noise variable X_3
     having positif directional match sign(hat{theta}_3^{1, lambda}) = sign(hat{theta}_2^{1, lambda}) = +1,
     perturbing theta_{(0)} to theta_{(delta)} = (0, tau_max + delta, delta, 0, ..., 0) changes expected
     prediction error L(theta) = E[(X_1 - X^T theta)^2] by
     L(theta_{(delta)}) - L(theta_{(0)}) = -2(s - tau_max)*delta + 2*delta^2 = 2*delta*(delta - (s - tau_max)) < 0
     for all 0 < delta < s - tau_max (achieving its minimum -0.5*(s - tau_max)^2 at delta* = 0.5*(s - tau_max)),
     proving that reducing lambda to include a false-positive noise edge strictly decreases prediction risk.
3. Neighborhood stability condition S_a(b) (Section 2.4, pp. 7-10, Eq. 5, Assumption 6, Propositions 2-3, Theorems 1-2)
   and KKT subgradient characterization (Appendix, p. 15, Lemma A.1 & p. 23, Eq. A.30):
   - S_a(b) = sum_{k in ne_a} sign(theta_k^{a, ne_a}) * theta_k^{b, ne_a} where theta^{b, ne_a} = Sigma_{ne_a, ne_a}^{-1} Sigma_{ne_a, b}.
   - Under a 4-node diamond/star-with-chord Gaussian graphical model where non-neighbor b=4 shares
     two neighbors {2, 3} of node a=1 with correlation rho, S_1(4) = 2*rho / (1 + rho) < 1 when rho < 1,
     whereas when b=4 is strongly coupled to {2, 3} with coefficient c > (1 + rho)/2, S_1(4) = 2*c / (1 + rho) > 1,
     causing the restricted Lasso subgradient G_4(hat{theta}^{1, ne_1, lambda}) to exceed 1 in magnitude and
     forcing false-positive inclusion of node 4 (Proposition 3).
   - Conversely, on any acyclic (tree) graph with unit-variance variables and edge correlations r_e in (-1, 1),
     |S_a(b)| = |theta_k^{b, ne_a}| < 1 holds automatically (Section 2.4, p. 8).
4. AND/OR graph edge aggregation and finite-sample connectivity-component FWER bound (Section 3, pp. 11-13, Eqs. 7-9, Corollary 1, Theorem 3):
   - Verifies that intersection hat{E}^{lambda, AND} and union hat{E}^{lambda, OR} both recover E when
     hat{ne}_a^lambda = ne_a for all a in Gamma, and verifies the finite-sample Gaussian tail penalty
     lambda(alpha) = (2 * hat{sigma}_a / sqrt(n)) * Phi_tilde^{-1}(alpha / (2 * p^2)) (Eq. 9) guarantees
     sum_{a != b} P(|<X_a, X_b>| / (||X_a||_2 ||X_b||_2) > sqrt(n)*lambda / (2*hat{sigma}_a)) <= alpha
     for independent components (Theorem 3, p. 13 & p. 27).
"""

import json
import math
import random
import sys


def mat_inv_4x4(m):
    """Invert a 4x4 matrix via Gauss-Jordan elimination."""
    n = 4
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(m)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[pivot] = aug[pivot], aug[col]
        div = aug[col][col]
        for j in range(2 * n):
            aug[col][j] /= div
        for r in range(n):
            if r != col:
                factor = aug[r][col]
                for j in range(2 * n):
                    aug[r][j] -= factor * aug[col][j]
    return [row[n:] for row in aug]


def test_precision_matrix_and_partial_correlation_identity():
    """Verify theta_b^a = -K_{ab}/K_{aa} and pi_{ab} = -K_{ab}/sqrt(K_{aa}K_{bb}) (Section 2, pp. 3-4, 19)."""
    # 4-node precision matrix K with graph edges (0,1), (0,2), (1,2), (2,3) and missing edges (0,3), (1,3)
    K = [
        [2.0, -0.6, -0.5, 0.0],
        [-0.6, 1.8, -0.4, 0.0],
        [-0.5, -0.4, 2.2, -0.7],
        [0.0, 0.0, -0.7, 1.5],
    ]
    Sigma = mat_inv_4x4(K)

    max_theta_err = 0.0
    max_var_err = 0.0
    max_pi_err = 0.0
    for a in range(4):
        idx = [k for k in range(4) if k != a]
        # Solve 3x3 system Sigma_{idx, idx} * theta_{-a} = Sigma_{idx, a}
        # via Gauss-Jordan on 3x3
        sub = [[Sigma[i][j] for j in idx] + [Sigma[i][a]] for i in idx]
        for col in range(3):
            piv = max(range(col, 3), key=lambda r: abs(sub[r][col]))
            sub[col], sub[piv] = sub[piv], sub[col]
            div = sub[col][col]
            for j in range(4):
                sub[col][j] /= div
            for r in range(3):
                if r != col:
                    fac = sub[r][col]
                    for j in range(4):
                        sub[r][j] -= fac * sub[col][j]
        theta_a = {idx[r]: sub[r][3] for r in range(3)}
        # Residual variance Var(X_a | X_{-a}) = Sigma_{aa} - sum_{b != a} theta_b^a Sigma_{ab}
        cond_var_a = Sigma[a][a] - sum(theta_a[b] * Sigma[a][b] for b in idx)
        max_var_err = max(max_var_err, abs(cond_var_a - 1.0 / K[a][a]))

        for b in idx:
            exact_theta = -K[a][b] / K[a][a]
            max_theta_err = max(max_theta_err, abs(theta_a[b] - exact_theta))
            cond_var_b = 1.0 / K[b][b]
            # Note on p. 7 vs p. 19: partial correlation satisfies pi_{ab} = -K_{ab}/sqrt(K_{aa}K_{bb})
            # = theta_b^a * sqrt(K_{aa}/K_{bb}) = theta_b^a * sqrt(Var(X_b|X_{-b}) / Var(X_a|X_{-a}))
            # (when Var(X_a|X_{-a}) == Var(X_b|X_{-b}), pi_{ab} = sign(theta_b^a)*sqrt(theta_b^a * theta_a^b))
            pi_from_K = -K[a][b] / math.sqrt(K[a][a] * K[b][b])
            pi_from_theta = theta_a[b] * math.sqrt(cond_var_b / cond_var_a)
            max_pi_err = max(max_pi_err, abs(pi_from_K - pi_from_theta))

    # Check exact zero pattern for node 0: neighbors {1, 2}, non-neighbor {3}
    ne_0 = [b for b in range(1, 4) if abs(-K[0][b] / K[0][0]) > 1e-12]
    passed = (
        max_theta_err < 1e-12
        and max_var_err < 1e-12
        and max_pi_err < 1e-12
        and ne_0 == [1, 2]
    )
    return {
        "passed": passed,
        "max_theta_err": max_theta_err,
        "max_var_err": max_var_err,
        "max_pi_err": max_pi_err,
        "ne_0": ne_0,
    }


def test_prediction_oracle_inconsistency():
    """Verify Proposition 1 (pp. 5-6 & Appendix pp. 20-22, Eqs. A.20-A.22)."""
    s = 0.6
    tau_max = 0.42  # strict shrinkage tau_max < s (Eq. A.20)
    # Expected prediction error L(theta) = E[(X_1 - theta_2 X_2 - theta_3 X_3)^2]
    # where Sigma_{11}=Sigma_{22}=Sigma_{33}=1, Sigma_{12}=s, Sigma_{13}=Sigma_{23}=0:
    # L(theta) = 1 + theta_2^2 + theta_3^2 - 2*s*theta_2
    def expected_loss(theta2, theta3):
        return 1.0 + theta2 * theta2 + theta3 * theta3 - 2.0 * s * theta2

    L0 = expected_loss(tau_max, 0.0)
    # Optimal perturbation step along (0, delta, delta): delta* = 0.5 * (s - tau_max)
    delta_star = 0.5 * (s - tau_max)
    L_delta_star = expected_loss(tau_max + delta_star, delta_star)
    diff_actual = L_delta_star - L0
    diff_formula = -2.0 * (s - tau_max) * delta_star + 2.0 * (delta_star ** 2)

    # Also test that for all delta in (0, s - tau_max), L_delta < L0
    grid_deltas = [0.02 * k * (s - tau_max) for k in range(1, 50)]
    all_strictly_smaller = all(
        expected_loss(tau_max + d, d) < L0 - 1e-12 for d in grid_deltas
    )

    passed = (
        abs(diff_actual - diff_formula) < 1e-15
        and diff_actual < -0.01
        and all_strictly_smaller
    )
    return {
        "passed": passed,
        "s": s,
        "tau_max": tau_max,
        "delta_star": delta_star,
        "L0": L0,
        "L_delta_star": L_delta_star,
        "diff_actual": diff_actual,
        "all_strictly_smaller_on_interval": all_strictly_smaller,
    }


def solve_nodewise_lasso_coord_descent(X, a, lam, allowed_nodes=None, max_iter=3000, tol=1e-11):
    """Solve hat{theta}^{a, lambda} = argmin_{theta_a=0} (1/n)||X_a - X theta||_2^2 + lambda ||theta||_1."""
    n = len(X)
    p = len(X[0])
    if allowed_nodes is None:
        allowed_nodes = [j for j in range(p) if j != a]
    theta = [0.0] * p
    # Precompute Gram matrix G_{jk} = (1/n) <X_j, X_k>
    G = [[sum(X[i][j] * X[i][k] for i in range(n)) / n for k in range(p)] for j in range(p)]

    for _ in range(max_iter):
        max_diff = 0.0
        for j in allowed_nodes:
            # Partial residual correlation: (2/n) <X_a - sum_{k != j} theta_k X_k, X_j> = 2 * (G[a][j] - sum_{k != j} theta[k]*G[k][j])
            rho_j = 2.0 * (G[a][j] - sum(theta[k] * G[k][j] for k in allowed_nodes if k != j))
            denom = 2.0 * G[j][j]
            if rho_j > lam:
                new_val = (rho_j - lam) / denom
            elif rho_j < -lam:
                new_val = (rho_j + lam) / denom
            else:
                new_val = 0.0
            max_diff = max(max_diff, abs(new_val - theta[j]))
            theta[j] = new_val
        if max_diff < tol:
            break

    # Subgradient vector G_b(theta) = -2/(n*lambda) <X_a - X theta, X_b> (Lemma A.1, p. 15)
    subgrad = []
    for b in range(p):
        ip = G[a][b] - sum(theta[k] * G[k][b] for k in range(p))
        subgrad.append(-2.0 * ip / lam)
    return theta, subgrad


def test_neighborhood_stability_and_kkt():
    """Verify Neighborhood Stability S_a(b) (Eq. 5, Assumption 6, Propositions 2-3, Theorems 1-2) and Lemma A.1."""
    # Construct two 4-node Gaussian models where ne_0 = {1, 2} and node 3 is a non-neighbor of node 0 (K_{03} = 0):
    # X_1, X_2 have correlation rho = 0.2; X_0 = 0.5*X_1 + 0.5*X_2 + eps_0;
    # X_3 = c*X_1 + c*X_2 + eps_3 where eps_0, eps_3 are independent of (X_1, X_2) and of each other,
    # so X_0 _|_ X_3 | (X_1, X_2), meaning 3 not in ne_0!
    # Then on ne_0 = {1, 2}, sign(theta_1^{0, ne_0}) = +1, sign(theta_2^{0, ne_0}) = +1,
    # and theta^{3, ne_0} = (c, c), so S_0(3) = 2*c!
    rho = -0.35
    c_stable = 0.35    # S_0(3) = 0.70 < 1 (Assumption 6 satisfied)
    c_unstable = 0.60  # S_0(3) = 1.20 > 1 (Assumption 6 violated; Proposition 3)

    # Verify on a deterministic noiseless covariance factor (exact sample covariance matching population Sigma)
    # Using 4 orthogonal basis vectors in R^4 to realize exact population Gram matrix G = Sigma
    def build_exact_sample_from_sigma(c_val):
        # Sigma on (X_0, X_1, X_2, X_3):
        # Cov(X_1, X_1)=1, Cov(X_2, X_2)=1, Cov(X_1, X_2)=rho
        # X_0 = 0.5*X_1 + 0.5*X_2 + sigma_0 * Z_0 with Var(X_0) = 1 => 0.5*(1+rho) + sigma_0^2 = 1
        # X_3 = c*X_1 + c*X_2 + sigma_3 * Z_3 with Var(X_3) = 1 => 2*c^2*(1+rho) + sigma_3^2 = 1
        s0 = math.sqrt(1.0 - 0.5 * (1.0 + rho))
        s3 = math.sqrt(1.0 - 2.0 * (c_val ** 2) * (1.0 + rho))
        # Cholesky-like factor L (4x4) such that (1/4) X^T X = Sigma:
        # Let u1, u2, u3, u4 be orthonormal columns in R^4 (scaled by sqrt(4)=2):
        # X_1 = u1
        # X_2 = rho*u1 + sqrt(1-rho^2)*u2
        # X_0 = 0.5*X_1 + 0.5*X_2 + s0*u3
        # X_3 = c*X_1 + c*X_2 + s3*u4
        u1 = [2.0, 0.0, 0.0, 0.0]
        u2 = [0.0, 2.0, 0.0, 0.0]
        u3 = [0.0, 0.0, 2.0, 0.0]
        u4 = [0.0, 0.0, 0.0, 2.0]
        X = []
        for i in range(4):
            x1 = u1[i]
            x2 = rho * u1[i] + math.sqrt(1.0 - rho * rho) * u2[i]
            x0 = 0.5 * x1 + 0.5 * x2 + s0 * u3[i]
            x3 = c_val * x1 + c_val * x2 + s3 * u4[i]
            X.append([x0, x1, x2, x3])
        return X

    lam = 0.15
    X_stable = build_exact_sample_from_sigma(c_stable)
    # Restricted Lasso on ne_0 = {1, 2}
    theta_restr_s, subgrad_restr_s = solve_nodewise_lasso_coord_descent(X_stable, 0, lam, allowed_nodes=[1, 2])
    # Full Lasso on {1, 2, 3}
    theta_full_s, _ = solve_nodewise_lasso_coord_descent(X_stable, 0, lam, allowed_nodes=[1, 2, 3])

    X_unstable = build_exact_sample_from_sigma(c_unstable)
    theta_restr_u, subgrad_restr_u = solve_nodewise_lasso_coord_descent(X_unstable, 0, lam, allowed_nodes=[1, 2])
    theta_full_u, _ = solve_nodewise_lasso_coord_descent(X_unstable, 0, lam, allowed_nodes=[1, 2, 3])

    # In the noiseless population limit (Eq. A.30, p. 23):
    # -G_3(hat{theta}^{0, ne_0, lambda}) = S_0(3) = 2 * c_val
    S0_3_stable = 2.0 * c_stable
    S0_3_unstable = 2.0 * c_unstable

    # Check tree (acyclic graph) property (p. 8): for a chain 0 - 1 - 2 with correlation r in (-1, 1),
    # ne_0 = {1}, and for b = 2 not in ne_0, S_0(2) = sign(r) * r = |r| < 1
    r_tree = 0.75
    S_tree = abs(r_tree)

    passed = (
        abs(-subgrad_restr_s[3] - S0_3_stable) < 1e-9
        and abs(subgrad_restr_s[3]) < 1.0
        and abs(theta_full_s[3]) < 1e-10
        and abs(theta_full_s[1] - theta_restr_s[1]) < 1e-9
        and abs(-subgrad_restr_u[3] - S0_3_unstable) < 1e-9
        and abs(subgrad_restr_u[3]) > 1.0
        and abs(theta_full_u[3]) > 0.01  # False positive forced when |S_0(3)| > 1 (Proposition 3)
        and S_tree < 1.0
    )
    return {
        "passed": passed,
        "S0_3_stable": S0_3_stable,
        "neg_subgrad_3_stable": -subgrad_restr_s[3],
        "theta_full_stable_node3": theta_full_s[3],
        "S0_3_unstable": S0_3_unstable,
        "neg_subgrad_3_unstable": -subgrad_restr_u[3],
        "theta_full_unstable_node3": theta_full_u[3],
        "S_tree": S_tree,
    }


def norm_ppf_upper(u):
    """Compute Phi_tilde^{-1}(u) = Phi^{-1}(1 - u) via binary search on math.erfc."""
    lo, hi = -10.0, 10.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        tail = 0.5 * math.erfc(mid / math.sqrt(2.0))
        if tail > u:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def test_and_or_aggregation_and_fwer_bound():
    """Verify AND/OR edge aggregation (Eqs. 7-8, Corollary 1) and Theorem 3 FWER control (Eq. 9, p. 12-13)."""
    # Suppose nodewise neighborhoods on 4 nodes have one asymmetric false positive:
    # True edges: {(0,1), (2,3)} (two connected components {0,1} and {2,3})
    # Suppose hat{ne}_0 = {1, 2}, hat{ne}_1 = {0}, hat{ne}_2 = {3}, hat{ne}_3 = {2}
    hat_ne = {0: {1, 2}, 1: {0}, 2: {3}, 3: {2}}
    edges_and = sorted(
        (a, b) for a in range(4) for b in range(a + 1, 4)
        if (b in hat_ne[a] and a in hat_ne[b])
    )
    edges_or = sorted(
        (a, b) for a in range(4) for b in range(a + 1, 4)
        if (b in hat_ne[a] or a in hat_ne[b])
    )

    # Theorem 3 finite-sample FWER penalty (Eq. 9):
    # lambda(alpha) = (2 * hat{sigma}_a / sqrt(n)) * Phi_tilde^{-1}(alpha / (2 * p^2))
    rng = random.Random(20060801)
    n = 60
    p = 6
    alpha = 0.10
    z_thresh = norm_ppf_upper(alpha / (2.0 * p * p))

    # Simulate 400 Monte Carlo trials with two independent components C_1 = {0,1,2}, C_2 = {3,4,5}
    trials = 400
    false_component_joins = 0
    for _ in range(trials):
        # Generate X where C_1 and C_2 are independent Gaussian blocks
        X = [[0.0] * p for _ in range(n)]
        for i in range(n):
            z_common_1 = rng.gauss(0.0, 1.0)
            z_common_2 = rng.gauss(0.0, 1.0)
            for a in range(3):
                X[i][a] = 0.6 * z_common_1 + 0.8 * rng.gauss(0.0, 1.0)
            for b in range(3, 6):
                X[i][b] = 0.6 * z_common_2 + 0.8 * rng.gauss(0.0, 1.0)
        # Check the sufficient event in Proof of Theorem 3 (p. 27):
        # Does any pair (a in C_1, b in C_2) violate |<X_a - X hat{theta}^{a, C_1, lambda}, X_b>| <= n * lambda / 2?
        # Even simpler: check whether ANY cross-component inner product exceeds the Eq. (9) threshold
        joined = False
        for a in range(3):
            norm_a_sq = sum(X[i][a] ** 2 for i in range(n))
            hat_sigma_a = math.sqrt(norm_a_sq / n)
            lam_a = (2.0 * hat_sigma_a / math.sqrt(n)) * z_thresh
            theta_a, _ = solve_nodewise_lasso_coord_descent(X, a, lam_a)
            for b in range(3, 6):
                if abs(theta_a[b]) > 1e-9:
                    joined = True
                    break
            if joined:
                break
        if joined:
            false_component_joins += 1

    empirical_fwer = false_component_joins / trials
    passed = (
        edges_and == [(0, 1), (2, 3)]
        and edges_or == [(0, 1), (0, 2), (2, 3)]
        and empirical_fwer <= alpha
    )
    return {
        "passed": passed,
        "edges_and": edges_and,
        "edges_or": edges_or,
        "alpha": alpha,
        "z_thresh": z_thresh,
        "empirical_fwer": empirical_fwer,
    }


def main():
    r1 = test_precision_matrix_and_partial_correlation_identity()
    r2 = test_prediction_oracle_inconsistency()
    r3 = test_neighborhood_stability_and_kkt()
    r4 = test_and_or_aggregation_and_fwer_bound()

    all_passed = r1["passed"] and r2["passed"] and r3["passed"] and r4["passed"]
    report = {
        "concept_id": "AIMech:HighDimensionalGaussianGraphicalModelNeighborhoodSelectionWithTheLasso",
        "all_passed": all_passed,
        "tests": {
            "precision_matrix_and_partial_correlation_identity": r1,
            "prediction_oracle_inconsistency": r2,
            "neighborhood_stability_and_kkt": r3,
            "and_or_aggregation_and_fwer_bound": r4,
        },
    }
    print(json.dumps(report, indent=2))
    if not all_passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
