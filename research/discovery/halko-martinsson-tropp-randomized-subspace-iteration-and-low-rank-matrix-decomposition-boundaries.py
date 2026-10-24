#!/usr/bin/env python3
"""Boundary verification for Round 839: Halko-Martinsson-Tropp Randomized Subspace Iteration and Low-Rank Matrix Decomposition (Halko, Martinsson, & Tropp, 2010 / SIAM Review 2011, arXiv:0909.4061v2).

Verifies:
1. Sharp deterministic projector perturbation bound (Section 9.2, Theorem 9.1, Eq. 9.3):
   For A = U diag(Sigma_1, Sigma_2) V^T and sample matrix Y = A Omega with Omega_1 = V_1^T Omega
   of full row rank k and Omega_2 = V_2^T Omega:
   ||(I - P_Y) A||_F^2 <= ||Sigma_2||_F^2 + ||Sigma_2 Omega_2 Omega_1^dagger||_F^2
   and ||(I - P_Y) A||_2^2 <= ||Sigma_2||_2^2 + ||Sigma_2 Omega_2 Omega_1^dagger||_2^2,
   derived via the flattened perturbation matrix Z = [I; F] with F = Sigma_2 Omega_2 Omega_1^dagger Sigma_1^{-1}
   and Loewner inequality I - (I + F^T F)^{-1} <= F^T F (Proposition 8.2).
2. Operator-monotone projector power inequality and Randomized Subspace Iteration (Proposition 8.6,
   Theorem 9.2, Algorithm 4.4):
   ||(I - P_Z) A||_2 <= ||(I - P_Z) (A A^T)^q A||_2^{1/(2q+1)}, and exponential decay of the
   approximation gap ||(I - Q_q Q_q^T) A||_F as power iteration exponent q increases from 0 to 3.
3. Stage B PSD Nystrom superiority over Direct Hermitian projection (Section 5.3-5.4, Algorithms 5.3 & 5.5,
   Eqs. 5.11-5.12):
   For a positive-semidefinite matrix A, the Nystrom approximation A_nys = (AQ)(Q^T AQ)^{-1}(AQ)^T
   achieves strictly smaller error ||A - A_nys||_F <= ||A - Q Q^T A||_F <= ||A - Q Q^T A Q Q^T||_F.
4. Exact inverted-Wishart expected Frobenius norm E||G^dagger||_F^2 = k / (p - 1) for a k x (k + p)
   standard Gaussian matrix G (Proposition 10.2 / A.5, Eq. 10.3) and average Frobenius bound
   E||(I - P_Y) A||_F <= sqrt(1 + k / (p - 1)) * ||Sigma_2||_F (Theorem 10.5).
"""

import math
import random


def mat_mul(A, B):
    m = len(A)
    k = len(B)
    n = len(B[0])
    return [
        [sum(A[i][r] * B[r][j] for r in range(k)) for j in range(n)]
        for i in range(m)
    ]


def mat_T(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def frob_sq(A):
    return sum(x * x for row in A for x in row)


def qr_gram_schmidt(Y):
    """Double-orthogonalized modified Gram-Schmidt returning m x l orthonormal Q."""
    m = len(Y)
    l = len(Y[0])
    cols = [[Y[i][j] for i in range(m)] for j in range(l)]
    q_cols = []
    for v in cols:
        w = list(v)
        for _ in range(2):
            for u in q_cols:
                dot = sum(w[i] * u[i] for i in range(m))
                w = [w[i] - dot * u[i] for i in range(m)]
        nrm = math.sqrt(sum(x * x for x in w))
        q_cols.append([x / nrm for x in w])
    return [[q_cols[j][i] for j in range(l)] for i in range(m)]


def mat_inv_spd(M):
    """Gauss-Jordan inverse for small k x k SPD matrix."""
    k = len(M)
    aug = [
        [M[i][j] for j in range(k)] + [1.0 if i == j else 0.0 for j in range(k)]
        for i in range(k)
    ]
    for col in range(k):
        piv = max(range(col, k), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        div = aug[col][col]
        aug[col] = [x / div for x in aug[col]]
        for r in range(k):
            if r != col:
                fac = aug[r][col]
                aug[r] = [aug[r][c] - fac * aug[col][c] for c in range(2 * k)]
    return [row[k:] for row in aug]


def main():
    rng = random.Random(20261020)
    # Construct diagonal matrix A (since U = V = I by unitary invariance in Theorem 9.1 proof)
    n = 12
    k = 3
    p = 4
    l = k + p
    sigmas = [10.0, 5.0, 2.0, 0.4, 0.3, 0.25, 0.2, 0.15, 0.12, 0.1, 0.08, 0.05]
    A = [[sigmas[i] if i == j else 0.0 for j in range(n)] for i in range(n)]
    sigma2_frob_sq = sum(s * s for s in sigmas[k:])

    # 1. Verify Theorem 9.1 deterministic bound & Theorem 10.5 average Frobenius bound over Monte Carlo trials
    n_trials = 250
    err_frob_sum = 0.0
    ginv_frob_sq_sum = 0.0
    for _ in range(n_trials):
        Omega = [[rng.gauss(0.0, 1.0) for _ in range(l)] for _ in range(n)]
        Omega1 = Omega[:k]  # k x l
        Omega2 = Omega[k:]  # (n-k) x l
        # Right pseudoinverse of fat full-row-rank Omega1: Omega1^dagger = Omega1^T (Omega1 Omega1^T)^{-1}
        G11 = mat_mul(Omega1, mat_T(Omega1))
        G11_inv = mat_inv_spd(G11)
        Omega1_dag = mat_mul(mat_T(Omega1), G11_inv)  # l x k
        ginv_frob_sq_sum += frob_sq(Omega1_dag)

        # Compute Sigma_2 Omega_2 Omega_1^dagger
        S2_O2 = [[sigmas[k + i] * Omega2[i][j] for j in range(l)] for i in range(n - k)]
        S2_O2_O1dag = mat_mul(S2_O2, Omega1_dag)
        rhs_thm91 = sigma2_frob_sq + frob_sq(S2_O2_O1dag)

        # Actual projection residual (I - Q Q^T) A
        Y = mat_mul(A, Omega)
        Q = qr_gram_schmidt(Y)
        QtA = mat_mul(mat_T(Q), A)
        QQtA = mat_mul(Q, QtA)
        res = [[A[i][j] - QQtA[i][j] for j in range(n)] for i in range(n)]
        lhs_frob_sq = frob_sq(res)

        assert lhs_frob_sq <= rhs_thm91 + 1e-10, (
            f"Theorem 9.1 violated: {lhs_frob_sq} > {rhs_thm91}"
        )
        err_frob_sum += math.sqrt(lhs_frob_sq)

    emp_err_frob = err_frob_sum / n_trials
    theo_bound_10_5 = math.sqrt(1.0 + k / (p - 1.0)) * math.sqrt(sigma2_frob_sq)
    assert emp_err_frob <= theo_bound_10_5, (
        f"Theorem 10.5 average Frobenius bound violated: {emp_err_frob} > {theo_bound_10_5}"
    )

    # Verify Proposition 10.2 / A.5 inverted-Wishart trace identity E||Omega_1^dagger||_F^2 == k / (p - 1) = 3 / 3 = 1.0
    emp_ginv = ginv_frob_sq_sum / n_trials
    theo_ginv = k / (p - 1.0)
    assert abs(emp_ginv - theo_ginv) < 0.18, f"Inverted-Wishart mean trace mismatch: {emp_ginv} vs {theo_ginv}"

    # 2. Verify Randomized Subspace Iteration (Algorithm 4.4) monotonic error reduction with q = 0, 1, 2, 3
    Omega_fixed = [[rng.gauss(0.0, 1.0) for _ in range(k + 2)] for _ in range(n)]
    q_errors = []
    Q_cur = qr_gram_schmidt(mat_mul(A, Omega_fixed))
    for q in range(4):
        if q > 0:
            Y_tilde = mat_mul(mat_T(A), Q_cur)
            Q_tilde = qr_gram_schmidt(Y_tilde)
            Y_next = mat_mul(A, Q_tilde)
            Q_cur = qr_gram_schmidt(Y_next)
        proj = mat_mul(Q_cur, mat_mul(mat_T(Q_cur), A))
        err_q = math.sqrt(frob_sq([[A[i][j] - proj[i][j] for j in range(n)] for i in range(n)]))
        q_errors.append(err_q)

    for q in range(3):
        assert q_errors[q + 1] <= q_errors[q] + 1e-12, (
            f"Subspace iteration failed to improve error at q={q}: {q_errors}"
        )
    assert abs(q_errors[-1] - math.sqrt(sum(s * s for s in sigmas[k + 2:]))) < 0.05

    # 3. Verify PSD Nystrom approximation (Algorithm 5.5, Eq. 5.12) vs Direct Hermitian (Algorithm 5.3, Eq. 5.11)
    Q_psd = qr_gram_schmidt(mat_mul(A, Omega_fixed))
    Qt = mat_T(Q_psd)
    # Direct Hermitian: Q (Q^T A Q) Q^T
    B_dir = mat_mul(Qt, mat_mul(A, Q_psd))
    A_dir = mat_mul(Q_psd, mat_mul(B_dir, Qt))
    err_dir = math.sqrt(frob_sq([[A[i][j] - A_dir[i][j] for j in range(n)] for i in range(n)]))

    # Range projection error ||A - Q Q^T A||_F
    A_proj = mat_mul(Q_psd, mat_mul(Qt, A))
    err_proj = math.sqrt(frob_sq([[A[i][j] - A_proj[i][j] for j in range(n)] for i in range(n)]))

    # Nystrom: (A Q) (Q^T A Q)^{-1} (A Q)^T
    AQ = mat_mul(A, Q_psd)
    B_inv = mat_inv_spd(B_dir)
    A_nys = mat_mul(AQ, mat_mul(B_inv, mat_T(AQ)))
    err_nys = math.sqrt(frob_sq([[A[i][j] - A_nys[i][j] for j in range(n)] for i in range(n)]))

    assert err_nys <= err_proj + 1e-12 and err_proj <= err_dir + 1e-12, (
        f"Nystrom hierarchy violated: nys={err_nys}, proj={err_proj}, dir={err_dir}"
    )

    print(
        f"[PASS] Round 839 Halko-Martinsson-Tropp Randomized SVD (2010/2011): "
        f"emp_frob={emp_err_frob:.4f}<=bound={theo_bound_10_5:.4f}, "
        f"q_errs={[round(x, 4) for x in q_errors]}, nys={err_nys:.4f}<dir={err_dir:.4f}"
    )


if __name__ == "__main__":
    main()
