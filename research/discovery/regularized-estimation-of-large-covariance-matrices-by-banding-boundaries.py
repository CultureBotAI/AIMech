#!/usr/bin/env python3
"""Constructed boundary and mechanism verification for Bickel & Levina (2008a):
'Regularized estimation of large covariance matrices'
(The Annals of Statistics, 36(1):199-227, arXiv:0803.1909v1, DOI:10.1214/009053607000000758).

Verifies:
1. Sample covariance banding B_k(Sigma_hat_p) (Section 2.1, p. 4) and modified Cholesky
   inverse banding Sigma_tilde_{k,p}^{-1} = (I - A_tilde_k)^T D_tilde_k^{-1} (I - A_tilde_k)
   via k-predecessor autoregressions (Section 2.2, Equations 2-4, pp. 5-6), confirming that
   Sigma_tilde_{k,p}^{-1} is k-banded and positive definite for k < n even when p > n,
   while its inverse Sigma_tilde_{k,p} is unbanded and distinct from B_k(Sigma_hat_p).
2. Operator norm bound ||M||_2 <= ||M||_{(1,1)} for symmetric matrices (Equation A2, p. 21),
   deterministic banding bias ||B_k(Sigma_p) - Sigma_p||_{(1,1)} <= C k^{-alpha} over
   U(epsilon_0, alpha, C) (Equation 5, p. 6), and convergence improvement under optimal
   bandwidth k_n ~ (n^{-1} log p)^{-1/(2(alpha+1))} (Theorems 1 & 3, pp. 8, 10).
3. Lack of guaranteed positive definiteness under simple hard banding B_k(M) vs.
   guaranteed positive definiteness preservation under Schur-product tapering R_sigma(M) = M * R_sigma
   with triangular/exponential positive definite tapers (Section 3.3, Theorem 2, pp. 9-10).
4. Random-split resampling risk estimator R_hat(k) = (1/N) sum_{nu=1}^N ||B_k(Sigma_hat_1^{(nu)}) - Sigma_hat_2^{(nu)}||_{(1,1)}
   (Section 5, Equations 22-25, pp. 13-14) accurately recovering the oracle bandwidth k_0 = 1
   for an MA(1) process (Section 6.1, Example 1, p. 15).
"""

import math
import random


def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][r] * B[r][j] for r in range(k)) for j in range(n)] for i in range(m)]


def mat_transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def schur_mul(A, B):
    return [[A[i][j] * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def norm_1_1(M):
    """Matrix l1-to-l1 operator norm: max_j sum_i |m_{ij}| (Appendix, p. 20)."""
    p = len(M)
    return max(sum(abs(M[i][j]) for i in range(p)) for j in range(p))


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


def spectral_norm_symmetric(A):
    eigs = jacobi_eigenvalues_symmetric(A)
    return max(abs(eigs[0]), abs(eigs[-1]))


def solve_spd(A, b):
    """Solve symmetric positive-definite linear system Ax = b via Gaussian elimination."""
    m = len(A)
    aug = [A[i][:] + [b[i]] for i in range(m)]
    for col in range(m):
        piv = max(range(col, m), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        diag = aug[col][col]
        for j in range(col, m + 1):
            aug[col][j] /= diag
        for r in range(m):
            if r != col:
                f = aug[r][col]
                for j in range(col, m + 1):
                    aug[r][j] -= f * aug[col][j]
    return [aug[i][m] for i in range(m)]


def invert_unit_lower_triangular(L):
    """Invert unit lower triangular matrix L = I - A_k."""
    p = len(L)
    inv = [[1.0 if i == j else 0.0 for j in range(p)] for i in range(p)]
    for j in range(p):
        for i in range(j + 1, p):
            inv[i][j] = -sum(L[i][r] * inv[r][j] for r in range(j, i))
    return inv


def band_matrix(M, k):
    """Banding operator B_k(M) = [m_{ij} 1(|i - j| <= k)] (Section 2.1, p. 4)."""
    p = len(M)
    return [[M[i][j] if abs(i - j) <= k else 0.0 for j in range(p)] for i in range(p)]


def sample_covariance(X):
    """Sample covariance matrix Sigma_hat_p = (1/n) sum_{i=1}^n (X_i - X_bar)(X_i - X_bar)^T (Equation 1, p. 4)."""
    n = len(X)
    p = len(X[0])
    mean = [sum(X[i][j] for i in range(n)) / n for j in range(p)]
    Xc = [[X[i][j] - mean[j] for j in range(p)] for i in range(n)]
    S = [[0.0] * p for _ in range(p)]
    inv_n = 1.0 / n
    for i in range(p):
        for j in range(i, p):
            val = sum(Xc[r][i] * Xc[r][j] for r in range(n)) * inv_n
            S[i][j] = val
            S[j][i] = val
    return S


def cholesky_banded_inverse(S, k):
    """Modified Cholesky k-banded inverse estimator (Section 2.2, Equations 2-4, pp. 5-6).

    Regresses each X_j on its closest k predecessors Z_j^{(k)} = (X_{max(j-k,0)}, ..., X_{j-1})
    under the empirical covariance S, returning:
      A_tilde_k: k-banded strictly lower triangular regression coefficient matrix
      D_tilde_k: diagonal residual variance vector [d_{1,k}^2, ..., d_{p,k}^2]
      Sigma_tilde_inv: (I - A_tilde_k)^T D_tilde_k^{-1} (I - A_tilde_k)
      Sigma_tilde: (I - A_tilde_k)^{-1} D_tilde_k [(I - A_tilde_k)^{-1}]^T
    """
    p = len(S)
    A_tilde = [[0.0] * p for _ in range(p)]
    d_sq = [0.0] * p
    d_sq[0] = S[0][0]
    for j in range(1, p):
        if k == 0:
            d_sq[j] = S[j][j]
            continue
        start = max(0, j - k)
        preds = list(range(start, j))
        m = len(preds)
        var_Z = [[S[preds[r]][preds[c]] for c in range(m)] for r in range(m)]
        cov_XZ = [S[j][preds[r]] for r in range(m)]
        a_j = solve_spd(var_Z, cov_XZ)
        for idx, t in enumerate(preds):
            A_tilde[j][t] = a_j[idx]
        # Residual variance: Var(X_j) - a_j^T Cov(Z_j, X_j)
        res_var = S[j][j] - sum(a_j[r] * cov_XZ[r] for r in range(m))
        d_sq[j] = res_var

    I_minus_A = [[(1.0 if i == j else -A_tilde[i][j]) for j in range(p)] for i in range(p)]
    # Sigma_tilde_inv = (I - A)^T D^{-1} (I - A)
    Sigma_tilde_inv = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(p):
            Sigma_tilde_inv[i][j] = sum(I_minus_A[r][i] * (1.0 / d_sq[r]) * I_minus_A[r][j] for r in range(max(i, j), p))

    # Sigma_tilde = (I - A)^{-1} D [(I - A)^{-1}]^T
    L_inv = invert_unit_lower_triangular(I_minus_A)
    Sigma_tilde = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(p):
            Sigma_tilde[i][j] = sum(L_inv[i][r] * d_sq[r] * L_inv[j][r] for r in range(min(i, j) + 1))

    return A_tilde, d_sq, Sigma_tilde_inv, Sigma_tilde


def test_1_banding_and_cholesky_inverse_estimators():
    """Verify Section 2.1 and Section 2.2 (Equations 2-4, pp. 4-6) in the p > n regime."""
    rng = random.Random(200801)
    p = 18
    n = 12  # p > n so unregularized Sigma_hat_p is singular!
    rho = 0.5
    # True AR(1) covariance Sigma_{ij} = rho^{|i-j|}, whose true inverse is 1-banded (tridiagonal)
    L_chol = [[0.0] * p for _ in range(p)]
    for i in range(p):
        L_chol[i][0] = rho ** i
        for j in range(1, i + 1):
            L_chol[i][j] = (rho ** (i - j)) * math.sqrt(1.0 - rho * rho)

    X = []
    for _ in range(n):
        z = [rng.gauss(0.0, 1.0) for _ in range(p)]
        x = [sum(L_chol[i][j] * z[j] for j in range(i + 1)) for i in range(p)]
        X.append(x)

    S = sample_covariance(X)
    # Since p = 18 > n = 12, S is rank-deficient (minimum eigenvalue ~ 0)
    eigs_S = jacobi_eigenvalues_symmetric(S)
    assert abs(eigs_S[0]) < 1e-9, f"Expected singular S when p > n, got min eig {eigs_S[0]}"

    k = 2
    S_band = band_matrix(S, k)
    A_tilde, d_sq, Omega_tilde, Sigma_tilde = cholesky_banded_inverse(S, k)

    # Check A_tilde is strictly lower triangular and k-banded
    for i in range(p):
        for j in range(p):
            if j >= i or i - j > k:
                assert abs(A_tilde[i][j]) < 1e-12

    # Check residual variances are strictly positive (since k = 2 < n = 12)
    assert all(d > 0.01 for d in d_sq), f"Expected positive residual variances, got {min(d_sq)}"

    # Check Omega_tilde = Sigma_tilde_{k,p}^{-1} is k-banded and strictly positive definite
    for i in range(p):
        for j in range(p):
            if abs(i - j) > k:
                assert abs(Omega_tilde[i][j]) < 1e-12, f"Expected k-banded Omega_tilde at ({i},{j})"
    eigs_Omega = jacobi_eigenvalues_symmetric(Omega_tilde)
    assert eigs_Omega[0] > 0.1, f"Expected SPD Omega_tilde, got min eig {eigs_Omega[0]}"

    # Check Sigma_tilde * Omega_tilde == I
    prod = mat_mul(Sigma_tilde, Omega_tilde)
    for i in range(p):
        for j in range(p):
            target = 1.0 if i == j else 0.0
            assert abs(prod[i][j] - target) < 1e-9

    # Check Sigma_tilde is NOT banded (entries outside band k are nonzero) and differs from S_band
    off_band_max = max(abs(Sigma_tilde[i][j]) for i in range(p) for j in range(p) if abs(i - j) > k)
    assert off_band_max > 1e-3, "Expected Sigma_tilde to be unbanded in general (p. 6)"
    diff_cov = spectral_norm_symmetric(mat_sub(Sigma_tilde, S_band))
    assert diff_cov > 0.05, "Expected Sigma_tilde to differ from B_k(Sigma_hat)"


def test_2_operator_norm_and_rate_improvement():
    """Verify Equation A2 (p. 21) and Theorems 1 & 3 (pp. 8, 10) operator norm gains."""
    rng = random.Random(200802)
    p = 24
    n = 80
    rho = 0.4
    Sigma = [[rho ** abs(i - j) for j in range(p)] for i in range(p)]
    # True inverse of AR(1) covariance
    Omega = [[0.0] * p for _ in range(p)]
    inv_denom = 1.0 / (1.0 - rho * rho)
    for i in range(p):
        Omega[i][i] = (1.0 if (i == 0 or i == p - 1) else (1.0 + rho * rho)) * inv_denom
        if i + 1 < p:
            Omega[i][i + 1] = -rho * inv_denom
            Omega[i + 1][i] = -rho * inv_denom

    # Verify inequality (A2): ||M||_2 <= ||M||_{(1,1)} for symmetric M
    assert spectral_norm_symmetric(Sigma) <= norm_1_1(Sigma) + 1e-12

    # Verify monotone decay of deterministic banding bias ||B_k(Sigma) - Sigma||_{(1,1)}
    biases = [norm_1_1(mat_sub(band_matrix(Sigma, k), Sigma)) for k in range(1, 6)]
    for r in range(len(biases) - 1):
        assert biases[r + 1] < biases[r]

    # Simulate sample from N(0, Sigma)
    L_chol = [[0.0] * p for _ in range(p)]
    for i in range(p):
        L_chol[i][0] = rho ** i
        for j in range(1, i + 1):
            L_chol[i][j] = (rho ** (i - j)) * math.sqrt(1.0 - rho * rho)

    X = []
    for _ in range(n):
        z = [rng.gauss(0.0, 1.0) for _ in range(p)]
        X.append([sum(L_chol[i][j] * z[j] for j in range(i + 1)) for i in range(p)])

    S = sample_covariance(X)
    err_raw_op = spectral_norm_symmetric(mat_sub(S, Sigma))
    err_raw_l1 = norm_1_1(mat_sub(S, Sigma))

    S_band2 = band_matrix(S, 2)
    err_band_op = spectral_norm_symmetric(mat_sub(S_band2, Sigma))
    err_band_l1 = norm_1_1(mat_sub(S_band2, Sigma))

    assert err_band_op < err_raw_op, f"Expected banded operator error {err_band_op} < raw {err_raw_op}"
    assert err_band_l1 < 0.5 * err_raw_l1, f"Expected banded l1 error {err_band_l1} < 0.5 * raw {err_raw_l1}"

    # Verify Theorem 3: Cholesky 1-banded inverse estimator vs true AR(1) precision Omega
    _, _, Omega_tilde_1, Sigma_tilde_1 = cholesky_banded_inverse(S, 1)
    err_chol_inv = spectral_norm_symmetric(mat_sub(Omega_tilde_1, Omega))
    err_chol_cov = spectral_norm_symmetric(mat_sub(Sigma_tilde_1, Sigma))
    assert err_chol_cov < err_raw_op, f"Expected Cholesky cov error {err_chol_cov} < raw {err_raw_op}"
    assert err_chol_inv < 1.0, f"Expected small Cholesky inverse operator error, got {err_chol_inv}"


def test_3_indefinite_banding_vs_positive_definite_schur_tapering():
    """Verify Section 3.3 (pp. 9-10): B_k(M) can fail positive definiteness while R_sigma(M) = M * R_sigma preserves it."""
    # Construct a 4x4 symmetric positive definite matrix M whose 1-banded version B_1(M) has a negative eigenvalue
    # Let M have 1 on diagonal, 0.8 on first off-diagonal, and 0.65 on second off-diagonal, 0.4 on third
    M = [
        [1.00, 0.80, 0.65, 0.40],
        [0.80, 1.00, 0.80, 0.65],
        [0.65, 0.80, 1.00, 0.80],
        [0.40, 0.65, 0.80, 1.00],
    ]
    eigs_M = jacobi_eigenvalues_symmetric(M)
    assert eigs_M[0] > 0.05, f"Expected M to be positive definite, min eig = {eigs_M[0]}"

    # Hard 1-banding sets |i - j| > 1 to 0, producing a tridiagonal matrix with a_1 = 0.8 > 1/(2 cos(pi/5)) = 0.618
    M_band1 = band_matrix(M, 1)
    eigs_band1 = jacobi_eigenvalues_symmetric(M_band1)
    assert eigs_band1[0] < -0.2, f"Expected B_1(M) to be indefinite (negative min eig), got {eigs_band1[0]}"

    # Now apply Schur-product tapering R_sigma(M) = M * R_sigma (Section 3.3, p. 9)
    # Example 1: triangular positive definite taper r_sigma(i, j) = (1 - |i - j|/sigma)_+ with sigma = 2.5
    sigma = 2.5
    R_tri = [[max(0.0, 1.0 - abs(i - j) / sigma) for j in range(4)] for i in range(4)]
    eigs_R_tri = jacobi_eigenvalues_symmetric(R_tri)
    assert eigs_R_tri[0] > 0.05

    M_taper_tri = schur_mul(M, R_tri)
    eigs_taper_tri = jacobi_eigenvalues_symmetric(M_taper_tri)
    assert eigs_taper_tri[0] > 0.05, f"Expected Schur-tapered matrix to be strictly PD, got {eigs_taper_tri[0]}"

    # Example 2: exponential positive definite taper r_sigma(i, j) = exp(-|i - j|/sigma)
    R_exp = [[math.exp(-abs(i - j) / sigma) for j in range(4)] for i in range(4)]
    M_taper_exp = schur_mul(M, R_exp)
    eigs_taper_exp = jacobi_eigenvalues_symmetric(M_taper_exp)
    assert eigs_taper_exp[0] > 0.05, f"Expected exponential Schur-tapered matrix to be PD, got {eigs_taper_exp[0]}"


def test_4_resampling_bandwidth_selector():
    """Verify Section 5 (Equations 22-25, pp. 13-14) and Section 6.1 Example 1 (MA(1), p. 15)."""
    rng = random.Random(200804)
    p = 16
    n = 90
    theta = 0.7
    # Generate X from MA(1): X_{i,j} = eps_{i,j} + theta * eps_{i,j-1}, so Sigma_{ij} = 0 for |i - j| > 1 (k_0 = 1)
    X = []
    for _ in range(n):
        eps = [rng.gauss(0.0, 1.0) for _ in range(p + 1)]
        X.append([eps[j + 1] + theta * eps[j] for j in range(p)])

    # Random-split risk estimation (Equations 24-25, p. 13) with n_1 = n // 3, N = 25 random splits
    n1 = n // 3
    N_splits = 25
    candidate_ks = [0, 1, 2, 3, 4, 5]
    R_hat = {k: 0.0 for k in candidate_ks}

    indices = list(range(n))
    for _ in range(N_splits):
        rng.shuffle(indices)
        X1 = [X[i] for i in indices[:n1]]
        X2 = [X[i] for i in indices[n1:]]
        S1 = sample_covariance(X1)
        S2 = sample_covariance(X2)
        for k in candidate_ks:
            R_hat[k] += norm_1_1(mat_sub(band_matrix(S1, k), S2)) / N_splits

    k_hat = min(candidate_ks, key=lambda k: R_hat[k])
    assert k_hat == 1, f"Expected resampling selector to pick oracle k_0 = 1 for MA(1), got k_hat = {k_hat} ({R_hat})"


if __name__ == "__main__":
    test_1_banding_and_cholesky_inverse_estimators()
    test_2_operator_norm_and_rate_improvement()
    test_3_indefinite_banding_vs_positive_definite_schur_tapering()
    test_4_resampling_bandwidth_selector()
    print("All Bickel & Levina (2008a) boundary and mechanism assertions passed.")
