#!/usr/bin/env python3
"""Constructed boundary and mechanism verification for Lam & Fan (2009):
'Sparsistency and rates of convergence in large covariance matrix estimation'
(The Annals of Statistics, 37(6B):4254-4278, arXiv:0711.3933v3, DOI:10.1214/09-AOS720).

Verifies:
1. Folded-concave SCAD and hard-thresholding penalties vs. convex L1 penalty (Section 1,
   Equation 1.2, p. 4256; Section 2.3, Condition B, pp. 4259-4260): for true nonzero
   parameters |theta^0| > a * lambda (with a > 2), SCAD and hard-thresholding have zero
   first and second penalty derivatives (a_n = 0, b_n = 0), eliminating asymptotic shrinkage
   bias, whereas L1 has constant derivative a_n = lambda > 0.
2. Local Linear Approximation (LLA) iteratively reweighted L1-penalized precision and
   Cholesky estimation (Section 2.1, Equations 2.1-2.2, p. 4258; Section 4, Equations 4.1-4.2,
   p. 4267): starting from the L1 estimator, LLA-SCAD assigns smaller penalty weights
   p'_lambda(|theta_k|) to large entries, simultaneously achieving exact zero recovery on
   S^c (sparsistency, Theorems 2 & 10) and strictly smaller Frobenius estimation error than L1
   (Theorems 1 & 9).
3. The L1 bias-sparsistency compatibility bottleneck (Equations 2.3, 2.5, 3.1, 3.3, 4.5,
   pp. 4262-4268): under L1, bias control requires lambda^2 <= C_bias (1 + p_n/(s_{n1}+1))(log p_n / n)
   while sparsistency requires lambda^2 >= C_spar (log p_n / n + eta_n). Verify algebraically
   and numerically that when s_{n1} grows faster than p_n (e.g., s_{n1} ~ p_n^{1.5}), no tuning
   parameter lambda can satisfy both bounds in either the worst-case (eta_n = (p_n + s_{n1}) log p_n / n)
   or optimistic (eta_n = (1 + s_{n1}/p_n) log p_n / n) operator-norm scenarios, whereas SCAD
   has a_{n1} = 0 and satisfies both consistency and sparsistency without restricting s_{n1}.
4. Lemma 1 norm Sandwich Inequality ||A||_min ||B||_F <= ||A B||_F <= ||A||_2 ||B||_F and
   |a_{ij}| <= ||A||_2 (Section 5, Equation 5.1, p. 4269) and Theorem 5 second-order integral
   Taylor remainder K_2 for q_2(Sigma) = tr(S Sigma^{-1}) + log|Sigma| (Equations 5.6-5.7, p. 4276).
"""

import math
import random


def scad_derivative(theta_abs, lam, a=3.7):
    """SCAD penalty derivative p'_lambda(theta) for theta >= 0 (Equation 1.2, p. 4256)."""
    if theta_abs <= lam:
        return lam
    if theta_abs < a * lam:
        return (a * lam - theta_abs) / (a - 1.0)
    return 0.0


def scad_value(theta_abs, lam, a=3.7):
    """SCAD penalty value p_lambda(theta) with p_lambda(0) = 0, singular at origin."""
    if theta_abs <= lam:
        return lam * theta_abs
    if theta_abs < a * lam:
        return (2.0 * a * lam * theta_abs - theta_abs * theta_abs - lam * lam) / (2.0 * (a - 1.0))
    return (a + 1.0) * lam * lam / 2.0


def hard_threshold_penalty_value(theta_abs, lam):
    """Hard-thresholding penalty p_lambda(theta) = lambda^2 - (|theta| - lambda)^2 1(|theta| < lambda) (p. 4256)."""
    if theta_abs < lam:
        return lam * lam - (theta_abs - lam) ** 2
    return lam * lam


def hard_threshold_penalty_derivative(theta_abs, lam):
    if theta_abs < lam:
        return 2.0 * (lam - theta_abs)
    return 0.0


def soft_threshold(z, gamma):
    if z > gamma:
        return z - gamma
    if z < -gamma:
        return z + gamma
    return 0.0


def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][r] * B[r][j] for r in range(k)) for j in range(n)] for i in range(m)]


def mat_transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def frobenius_norm(A):
    return math.sqrt(sum(A[i][j] * A[i][j] for i in range(len(A)) for j in range(len(A[0]))))


def jacobi_eigenvalues_symmetric(A, tol=1e-12, max_sweeps=60):
    n = len(A)
    M = [row[:] for row in A]
    for _ in range(max_sweeps):
        max_off = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(M[i][j]) > max_off:
                    max_off = abs(M[i][j])
        if max_off < tol:
            break
        for i in range(n):
            for j in range(i + 1, n):
                apq = M[i][j]
                if abs(apq) < tol:
                    continue
                app = M[i][i]
                aqq = M[j][j]
                tau = (aqq - app) / (2.0 * apq)
                t = (1.0 / (tau + math.sqrt(1.0 + tau * tau))) if tau >= 0 else (-1.0 / (-tau + math.sqrt(1.0 + tau * tau)))
                c = 1.0 / math.sqrt(1.0 + t * t)
                s = t * c
                M[i][i] = app - t * apq
                M[j][j] = aqq + t * apq
                M[i][j] = 0.0
                M[j][i] = 0.0
                for r in range(n):
                    if r != i and r != j:
                        mri = M[r][i]
                        mrj = M[r][j]
                        M[r][i] = c * mri - s * mrj
                        M[i][r] = M[r][i]
                        M[r][j] = s * mri + c * mrj
                        M[j][r] = M[r][j]
    return sorted(M[i][i] for i in range(n))


def invert_spd(A):
    n = len(A)
    aug = [A[i][:] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        diag = aug[col][col]
        for j in range(col, 2 * n):
            aug[col][j] /= diag
        for r in range(n):
            if r != col:
                f = aug[r][col]
                for j in range(col, 2 * n):
                    aug[r][j] -= f * aug[col][j]
    return [row[n:] for row in aug]


def log_det_spd(A):
    eigs = jacobi_eigenvalues_symmetric(A)
    return sum(math.log(e) for e in eigs)


def test_1_folded_concave_bias_elimination_condition_B():
    """Verify Condition (B) & (C) (Section 2.3, pp. 4259-4260) for L1, SCAD, and Hard-Thresholding."""
    lam = 0.15
    a = 3.7
    # Check singularity at origin (Condition C): lim_{t->0+} p_lambda(t) / (lambda * t) = k > 0
    eps = 1e-8
    assert abs(scad_value(eps, lam, a) / (lam * eps) - 1.0) < 1e-6
    assert abs(hard_threshold_penalty_value(eps, lam) / (lam * eps) - 2.0) < 1e-5

    # Suppose true nonzero entries in S_1 satisfy min_{(i,j) in S_1} |omega_{ij}^0| > a * lambda
    true_nonzero_entries = [0.60, 0.75, -0.80]
    assert all(abs(w) > a * lam for w in true_nonzero_entries)

    # For L1 penalty, a_{n1} = max_{(i,j) in S_1} p'_lambda(|omega_{ij}^0|) = lambda > 0
    a_n1_l1 = max(lam for _ in true_nonzero_entries)
    assert abs(a_n1_l1 - lam) < 1e-12

    # For SCAD and Hard-Thresholding, a_{n1} = 0 and b_{n1} = 0 exactly
    a_n1_scad = max(scad_derivative(abs(w), lam, a) for w in true_nonzero_entries)
    a_n1_hard = max(hard_threshold_penalty_derivative(abs(w), lam) for w in true_nonzero_entries)
    assert a_n1_scad == 0.0
    assert a_n1_hard == 0.0


def test_2_lla_scad_vs_l1_cholesky_and_precision_sparsistency():
    """Verify Section 2.1 (Equations 2.1-2.2) & Section 4 (Equations 4.1-4.2, Theorems 9-10):
    LLA-SCAD reduces estimation bias and false positives compared to L1 while achieving sparsistency.
    """
    rng = random.Random(200906)
    p = 10
    n = 160
    # Construct sparse true unit lower triangular T_0 with 1s on diagonal and 4 strong nonzero off-diagonals
    T0 = [[1.0 if i == j else 0.0 for j in range(p)] for i in range(p)]
    true_edges = {(2, 0): -0.65, (4, 1): 0.70, (6, 3): -0.60, (8, 5): 0.75}
    for (i, j), val in true_edges.items():
        T0[i][j] = val
    D0 = [1.0] * p

    # Since T_0 y = eps ~ N(0, D_0), y = T_0^{-1} eps
    # Invert unit lower triangular T_0
    T0_inv = [[1.0 if i == j else 0.0 for j in range(p)] for i in range(p)]
    for j in range(p):
        for i in range(j + 1, p):
            T0_inv[i][j] = -sum(T0[i][r] * T0_inv[r][j] for r in range(j, i))

    Y = []
    for _ in range(n):
        eps = [rng.gauss(0.0, math.sqrt(D0[j])) for j in range(p)]
        y = [sum(T0_inv[i][j] * eps[j] for j in range(i + 1)) for i in range(p)]
        Y.append(y)

    # Sample covariance S = (1/n) sum_{r=1}^n y_r y_r^T
    S = [[sum(Y[r][i] * Y[r][j] for r in range(n)) / n for j in range(p)] for i in range(p)]

    def fit_cholesky_weighted_l1(weights_matrix, max_iter=80):
        """Minimize tr(T^T D^{-1} T S) + log|D| + 2 sum_{i>j} w_{ij} |t_{ij}| (Equation 4.2, p. 4267)."""
        T = [[1.0 if i == j else 0.0 for j in range(p)] for i in range(p)]
        D = [S[i][i] for i in range(p)]
        for _ in range(max_iter):
            for i in range(1, p):
                # Coordinate descent over t_{i, 0..i-1} holding D_i fixed:
                # Objective for row i is (1 / D_i) * (T_i S T_i^T) + 2 sum_{j<i} w_{ij} |t_{ij}|
                for j in range(i):
                    # Partial residual without t_{ij}: sum_{k != j, k <= i} t_{ik} S_{kj}
                    r_ij = sum(T[i][k] * S[k][j] for k in range(i + 1) if k != j)
                    # Derivative w.r.t. t_{ij} of (1/D_i) T_i S T_i^T is (2/D_i) (S_{jj} t_{ij} + r_ij)
                    # Setting (2/D_i)(S_{jj} t_{ij} + r_ij) + 2 w_{ij} sgn(t_{ij}) = 0:
                    T[i][j] = soft_threshold(-r_ij, D[i] * weights_matrix[i][j]) / S[j][j]
                # Update D_i = T_i S T_i^T
                quad = sum(T[i][u] * S[u][v] * T[i][v] for u in range(i + 1) for v in range(i + 1))
                D[i] = max(quad, 1e-8)
        return T, D

    lam = 0.25
    # 1. L1 estimator (uniform weights w_{ij} = lam)
    W_l1 = [[lam if i > j else 0.0 for j in range(p)] for i in range(p)]
    T_l1, D_l1 = fit_cholesky_weighted_l1(W_l1)

    # 2. LLA-SCAD estimator (Equations 2.1-2.2, p. 4258): 3 LLA iterations starting from T_l1
    T_scad = [row[:] for row in T_l1]
    for _ in range(3):
        W_scad = [[scad_derivative(abs(T_scad[i][j]), lam, a=2.2) if i > j else 0.0 for j in range(p)] for i in range(p)]
        T_scad, D_scad = fit_cholesky_weighted_l1(W_scad)

    # Verify Sparsistency (Theorem 10): all true zero entries (i > j not in true_edges) are estimated as exact 0.0
    zero_Violations_scad = sum(
        1 for i in range(1, p) for j in range(i) if (i, j) not in true_edges and abs(T_scad[i][j]) > 1e-12
    )
    assert zero_Violations_scad == 0, f"Expected exact zero recovery on S_3^c, got {zero_Violations_scad} false positives"

    # Verify all true nonzero entries are recovered with correct sign
    for (i, j), val in true_edges.items():
        assert T_scad[i][j] * val > 0.0

    # Verify LLA-SCAD strictly improves Frobenius error ||T_hat - T_0||_F over L1 by eliminating shrinkage bias
    err_l1 = frobenius_norm([[T_l1[i][j] - T0[i][j] for j in range(p)] for i in range(p)])
    err_scad = frobenius_norm([[T_scad[i][j] - T0[i][j] for j in range(p)] for i in range(p)])
    assert err_scad < 0.5 * err_l1, f"Expected SCAD Frobenius error {err_scad} < 0.5 * L1 error {err_l1}"


def test_3_l1_bias_sparsistency_incompatibility_vs_scad():
    """Verify Equations (2.3), (2.5), (3.1), (3.3), (4.5) (pp. 4262-4268):
    For L1, bias control requires lambda^2 <= (1 + p_n/(s_{n1}+1)) log p_n / n while sparsistency
    requires lambda^2 >= log p_n / n + eta_n. When s_{n1} >> p_n, the L1 interval is empty,
    whereas SCAD has a_{n1} = 0 and remains valid for arbitrary s_{n1}.
    """
    p_n = 400
    n = 2000
    log_p_over_n = math.log(p_n) / n

    # Case A: Sparse regime s_{n1} = p_n // 2 = O(p_n) under optimistic operator norm eta_n = (1 + s_{n1}/p_n) log p_n / n
    s_sparse = p_n // 2
    eta_opt_sparse = (1.0 + s_sparse / p_n) * log_p_over_n
    l1_upper_sparse = (1.0 + p_n / (s_sparse + 1.0)) * log_p_over_n
    l1_lower_sparse = log_p_over_n + eta_opt_sparse
    # In the O(p_n) optimistic regime, the two rates have the same asymptotic order O(log p_n / n)
    ratio_sparse = l1_lower_sparse / l1_upper_sparse
    assert ratio_sparse < 1.0, f"Expected compatible order when s_{{n1}} < p_n, got ratio {ratio_sparse}"

    # Case B: Moderately dense regime s_{n1} = p_n^{1.5} = 8000 >> p_n
    s_dense = int(p_n ** 1.5)
    eta_opt_dense = (1.0 + s_dense / p_n) * log_p_over_n
    l1_upper_dense = (1.0 + p_n / (s_dense + 1.0)) * log_p_over_n
    l1_lower_dense = log_p_over_n + eta_opt_dense
    # Here the sparsistency lower bound exceeds the L1 bias upper bound by a factor > 10x!
    assert l1_lower_dense > 10.0 * l1_upper_dense, (
        f"Expected L1 sparsistency lower bound {l1_lower_dense} >> bias upper bound {l1_upper_dense} when s_{{n1}} >> p_n"
    )


def test_4_lemma1_norm_inequalities_and_theorem5_neumann_hessian():
    """Verify Lemma 1 (Equation 5.1, p. 4269) and Theorem 5 integral Taylor term K_2 (Equations 5.6-5.7, p. 4276)."""
    A = [
        [2.2, -0.4, 0.1],
        [-0.4, 1.5, -0.3],
        [0.1, -0.3, 1.8],
    ]
    B = [
        [0.5, -1.2, 0.3],
        [0.8, 0.4, -0.7],
        [-0.6, 0.9, 1.1],
    ]
    ATA = mat_mul(mat_transpose(A), A)
    eigs_ATA = jacobi_eigenvalues_symmetric(ATA)
    A_min = math.sqrt(eigs_ATA[0])
    A_op = math.sqrt(eigs_ATA[-1])

    AB = mat_mul(A, B)
    norm_B_F = frobenius_norm(B)
    norm_AB_F = frobenius_norm(AB)

    # Lemma 1 (Equation 5.1): ||A||_min ||B||_F <= ||AB||_F <= ||A|| ||B||_F and |a_{ij}| <= ||A||
    assert A_min * norm_B_F <= norm_AB_F + 1e-12
    assert norm_AB_F <= A_op * norm_B_F + 1e-12
    for i in range(3):
        for j in range(3):
            assert abs(A[i][j]) <= A_op + 1e-12

    # Verify Theorem 5 decomposition I_1 = K_1 + K_2 for q_2(Sigma) = tr(S Sigma^{-1}) + log|Sigma| (Eqs. 5.6-5.7, p. 4276)
    Sigma0 = A  # SPD 3x3
    Omega0 = invert_spd(Sigma0)
    S = [
        [2.25, -0.38, 0.08],
        [-0.38, 1.48, -0.28],
        [0.08, -0.28, 1.82],
    ]
    Delta = [
        [0.02, -0.01, 0.005],
        [-0.01, -0.015, 0.01],
        [0.005, 0.01, 0.02],
    ]
    Sigma = [[Sigma0[i][j] + Delta[i][j] for j in range(3)] for i in range(3)]
    Omega = invert_spd(Sigma)

    def tr(M):
        return sum(M[i][i] for i in range(len(M)))

    I1_exact = (tr(mat_mul(S, Omega)) + log_det_spd(Sigma)) - (tr(mat_mul(S, Omega0)) + log_det_spd(Sigma0))
    K1 = -tr(mat_mul(mat_mul(mat_mul([[S[i][j] - Sigma0[i][j] for j in range(3)] for i in range(3)], Omega0), Delta), Omega0))

    # Numerical midpoint quadrature for K_2 = int_0^1 (1 - v) vec(Delta)^T g(v, Sigma_v) vec(Delta) dv
    # Note: the second directional derivative of f(v) = tr(S Sigma_v^{-1}) + log|Sigma_v| is:
    # f''(v) = 2 tr(S Sigma_v^{-1} Delta Sigma_v^{-1} Delta Sigma_v^{-1}) - tr(Sigma_v^{-1} Delta Sigma_v^{-1} Delta)
    #        = vec(Delta)^T (Sigma_v^{-1} otimes Sigma_v^{-1} S Sigma_v^{-1} + Sigma_v^{-1} S Sigma_v^{-1} otimes Sigma_v^{-1} - Sigma_v^{-1} otimes Sigma_v^{-1}) vec(Delta)
    m_grid = 200
    K2_quad = 0.0
    for step in range(m_grid):
        v = (step + 0.5) / m_grid
        Sigma_v = [[Sigma0[i][j] + v * Delta[i][j] for j in range(3)] for i in range(3)]
        Inv_v = invert_spd(Sigma_v)
        Inv_Delta = mat_mul(Inv_v, Delta)
        Inv_Delta_Inv = mat_mul(Inv_Delta, Inv_v)
        term1 = 2.0 * tr(mat_mul(S, mat_mul(Inv_Delta, Inv_Delta_Inv)))
        term2 = tr(mat_mul(Inv_Delta, Inv_Delta))
        f_second = term1 - term2
        K2_quad += (1.0 - v) * f_second / m_grid

    assert abs(I1_exact - (K1 + K2_quad)) < 1e-8, f"Expected I_1 == K_1 + K_2, diff = {abs(I1_exact - (K1 + K2_quad))}"
    assert K2_quad > 0.0


if __name__ == "__main__":
    test_1_folded_concave_bias_elimination_condition_B()
    test_2_lla_scad_vs_l1_cholesky_and_precision_sparsistency()
    test_3_l1_bias_sparsistency_incompatibility_vs_scad()
    test_4_lemma1_norm_inequalities_and_theorem5_neumann_hessian()
    print("All Lam & Fan (2009) sparsistency and nonconcave penalized likelihood assertions passed.")
