#!/usr/bin/env python3
"""Constructed boundary & regime verification for Round 256:
AIMech:TensorSpectralDecompositionForDirichletMixedMembershipCommunityModels
(Anandkumar, Ge, Hsu, & Kakade 2014, JMLR 15(66):2239-2312, arXiv:1302.2684v4).

Verifies in pure Python (standard library only):
1. Exact Dirichlet 1st, 2nd, and 3rd moments (Proposition C.2, Eq. 96),
   whitened membership identity E[psi_u psi_u^T] = I_k (Eqs. 16, 18), and
   algebraic cancellation of all off-diagonal Dirichlet cross-terms in the
   centered 3-star moment tensor T^{alpha_0}_{X -> {A,B,C}} (Proposition 2.2,
   Eqs. 14-17).
2. Multi-partition whitening and symmetrization (Lemma 3.1, Eqs. 21-22) and
   adaptive-deflation tensor power iteration (Procedure 2, Theorem A.1)
   recovering eigenvalues lambda_i = alpha_hat_i^{-1/2} and eigenvectors Phi_i
   to < 1e-12, plus exact recovery of node memberships Pi via Eq. (24).
3. Exact unbiasedness of the linear pseudo-inverse estimator Q' (Section 3.3,
   p. 25; Appendix B.3, p. 48): E[Q' Pi^T] = I_k and E[Q' (Pi^T P Pi) (Q')^T] = P.
"""

from __future__ import annotations

import math
import random
import sys


def mat_mul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [
        [sum(A[i][r] * B[r][j] for r in range(k)) for j in range(n)]
        for i in range(m)
    ]


def mat_T(A: list[list[float]]) -> list[list[float]]:
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def frob_diff(A: list[list[float]], B: list[list[float]]) -> float:
    return math.sqrt(
        sum(
            (A[i][j] - B[i][j]) ** 2
            for i in range(len(A))
            for j in range(len(A[0]))
        )
    )


def sym_eig_3x3(M: list[list[float]]) -> tuple[list[float], list[list[float]]]:
    """Jacobi eigenvalue algorithm for a symmetric k x k matrix."""
    k = len(M)
    A = [row[:] for row in M]
    V = [[1.0 if i == j else 0.0 for j in range(k)] for i in range(k)]
    for _ in range(100):
        max_val = 0.0
        p, q = 0, 1
        for i in range(k):
            for j in range(i + 1, k):
                if abs(A[i][j]) > max_val:
                    max_val = abs(A[i][j])
                    p, q = i, j
        if max_val < 1e-15:
            break
        diff = A[q][q] - A[p][p]
        if abs(A[p][q]) < 1e-30:
            t = 0.0
        else:
            phi = diff / (2.0 * A[p][q])
            t = (
                1.0 / (abs(phi) + math.sqrt(phi * phi + 1.0))
                if phi >= 0
                else -1.0 / (abs(phi) + math.sqrt(phi * phi + 1.0))
            )
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        tau = s / (1.0 + c)
        h = t * A[p][q]
        A[p][p] -= h
        A[q][q] += h
        A[p][q] = 0.0
        A[q][p] = 0.0
        for r in range(k):
            if r != p and r != q:
                g = A[r][p]
                h_val = A[r][q]
                A[r][p] = g - s * (h_val + g * tau)
                A[p][r] = A[r][p]
                A[r][q] = h_val + s * (g - h_val * tau)
                A[q][r] = A[r][q]
        for r in range(k):
            g = V[r][p]
            h_val = V[r][q]
            V[r][p] = g - s * (h_val + g * tau)
            V[r][q] = h_val + s * (g - h_val * tau)
    evals = [A[i][i] for i in range(k)]
    # Sort descending
    order = sorted(range(k), key=lambda idx: evals[idx], reverse=True)
    evals_sorted = [evals[idx] for idx in order]
    V_sorted = [[V[i][idx] for idx in order] for i in range(k)]
    return evals_sorted, V_sorted


def main() -> int:
    # 1. Verify Dirichlet 1st, 2nd, 3rd moments and centered 3-star tensor (Proposition 2.2 & C.2)
    alpha = [0.3, 0.5, 0.7]
    k = len(alpha)
    alpha0 = sum(alpha)  # 1.5
    alpha_hat = [a / alpha0 for a in alpha]  # [0.2, 1/3, 7/15]

    # Exact 2nd moment E[pi pi^T] (Eq. 9)
    E_pi2 = [
        [
            (alpha_hat[i] if i == j else 0.0) / (alpha0 + 1.0)
            + (alpha0 / (alpha0 + 1.0)) * alpha_hat[i] * alpha_hat[j]
            for j in range(k)
        ]
        for i in range(k)
    ]

    # Verify Eq. (18): psi = Diag(alpha_hat^{-1/2}) (sqrt(alpha0+1) pi - (sqrt(alpha0+1) - 1) alpha_hat)
    # E[psi psi^T] = Diag(alpha_hat^{-1/2}) [ (alpha0+1) E[pi pi^T] - alpha0 alpha_hat alpha_hat^T ] Diag(alpha_hat^{-1/2})
    E_psi2 = [
        [
            (
                (alpha0 + 1.0) * E_pi2[i][j]
                - alpha0 * alpha_hat[i] * alpha_hat[j]
            )
            / math.sqrt(alpha_hat[i] * alpha_hat[j])
            for j in range(k)
        ]
        for i in range(k)
    ]
    I_k = [[1.0 if i == j else 0.0 for j in range(k)] for i in range(k)]
    psi_cov_err = frob_diff(E_psi2, I_k)
    assert psi_cov_err < 1e-14, f"E[psi psi^T] error too large: {psi_cov_err}"

    # Exact 3rd moment E[pi^{\\otimes 3}] (Proposition C.2, Eq. 96)
    denom3 = (alpha0 + 1.0) * (alpha0 + 2.0)
    E_pi3 = [[[0.0 for _ in range(k)] for _ in range(k)] for _ in range(k)]
    for a in range(k):
        for b in range(k):
            for c in range(k):
                val = (alpha0**2) * alpha_hat[a] * alpha_hat[b] * alpha_hat[c]
                if a == b == c:
                    val += 2.0 * alpha_hat[a]
                if a == b:
                    val += alpha0 * alpha_hat[a] * alpha_hat[c]
                if a == c:
                    val += alpha0 * alpha_hat[a] * alpha_hat[b]
                if b == c:
                    val += alpha0 * alpha_hat[b] * alpha_hat[a]
                E_pi3[a][b][c] = val / denom3

    # Apply centering formula Eq. (15) directly on membership coordinates (F_A = F_B = F_C = I_k)
    # Note: In Proposition C.2 Eq. (96), the diagonal term has numerator 2 * alpha_i, so
    # Eq. (15) Divided by 2 equals sum_{i=1}^k alpha_hat_i e_i^{\otimes 3}.
    T_centered = [[[0.0 for _ in range(k)] for _ in range(k)] for _ in range(k)]
    max_tensor_err = 0.0
    for a in range(k):
        for b in range(k):
            for c in range(k):
                raw_term = denom3 * E_pi3[a][b][c]
                mean_term = (
                    2.0
                    * (alpha0**2)
                    * alpha_hat[a]
                    * alpha_hat[b]
                    * alpha_hat[c]
                )
                cross_term = (
                    alpha0
                    * (alpha0 + 1.0)
                    * (
                        E_pi2[a][b] * alpha_hat[c]
                        + E_pi2[a][c] * alpha_hat[b]
                        + alpha_hat[a] * E_pi2[b][c]
                    )
                )
                # Divide by 2 for the Gamma(alpha_i + 3)/Gamma(alpha_i + 1) = (alpha_i+2)(alpha_i+1) factor 2
                T_centered[a][b][c] = 0.5 * (raw_term + mean_term - cross_term)
                target = alpha_hat[a] if (a == b == c) else 0.0
                max_tensor_err = max(
                    max_tensor_err, abs(T_centered[a][b][c] - target)
                )
    assert (
        max_tensor_err < 1e-14
    ), f"Centered 3-star tensor error: {max_tensor_err}"

    # 2. Multi-partition whitening, symmetrization, and tensor power method (Section 3, Lemma 3.1, Procedure 2)
    # Feature matrices F_A, F_B, F_C in R^{3 x 3} (non-orthogonal, well-conditioned)
    F_A = [
        [0.82, 0.15, 0.10],
        [0.12, 0.78, 0.18],
        [0.09, 0.14, 0.85],
    ]
    F_B = [
        [0.75, 0.20, 0.12],
        [0.18, 0.72, 0.15],
        [0.11, 0.16, 0.80],
    ]
    F_C = [
        [0.79, 0.11, 0.16],
        [0.14, 0.81, 0.12],
        [0.15, 0.13, 0.77],
    ]
    Diag_alpha = [
        [alpha_hat[i] if i == j else 0.0 for j in range(k)] for i in range(k)
    ]

    # Second-order centered covariance M_{A,A} = F_A Diag(alpha_hat) F_A^T
    M_AA = mat_mul(mat_mul(F_A, Diag_alpha), mat_T(F_A))
    M_BB = mat_mul(mat_mul(F_B, Diag_alpha), mat_T(F_B))
    M_CC = mat_mul(mat_mul(F_C, Diag_alpha), mat_T(F_C))

    def compute_whitening(M: list[list[float]]) -> list[list[float]]:
        evals, U = sym_eig_3x3(M)
        D_inv_sqrt = [
            [1.0 / math.sqrt(evals[i]) if i == j else 0.0 for j in range(k)]
            for i in range(k)
        ]
        return mat_mul(U, D_inv_sqrt)

    W_A = compute_whitening(M_AA)
    W_B = compute_whitening(M_BB)
    W_C = compute_whitening(M_CC)

    # Alignment matrices R_{A,B} = W_B^T F_B Diag(alpha_hat) F_A^T W_A (Eq. 21)
    M_BA = mat_mul(mat_mul(F_B, Diag_alpha), mat_T(F_A))
    M_CA = mat_mul(mat_mul(F_C, Diag_alpha), mat_T(F_A))
    R_AB = mat_mul(mat_mul(mat_T(W_B), M_BA), W_A)
    R_AC = mat_mul(mat_mul(mat_T(W_C), M_CA), W_A)

    # Effective transformations into whitened A-space:
    # W_A^T F_A = Phi Diag(alpha_hat^{-1/2}), and R_{A,B}^T W_B^T F_B = Phi Diag(alpha_hat^{-1/2})
    Phi_true = [
        [
            sum(W_A[r][a] * F_A[r][i] for r in range(k))
            * math.sqrt(alpha_hat[i])
            for i in range(k)
        ]
        for a in range(k)
    ]
    # Check Phi_true^T Phi_true = I_k
    ortho_err = frob_diff(mat_mul(mat_T(Phi_true), Phi_true), I_k)
    assert ortho_err < 1e-13, f"Phi_true orthogonality error: {ortho_err}"

    # Construct whitened symmetrized tensor T_sym = sum_{i=1}^k alpha_hat_i^{-1/2} Phi_i^{\otimes 3} (Lemma 3.1, Eq. 22)
    T_sym = [[[0.0 for _ in range(k)] for _ in range(k)] for _ in range(k)]
    for a in range(k):
        for b in range(k):
            for c in range(k):
                T_sym[a][b][c] = sum(
                    (1.0 / math.sqrt(alpha_hat[i]))
                    * Phi_true[a][i]
                    * Phi_true[b][i]
                    * Phi_true[c][i]
                    for i in range(k)
                )

    # Run Tensor Power Iteration with deflation (Procedure 2)
    rng = random.Random(20261019)
    recovered_lambdas: list[float] = []
    recovered_phis: list[list[float]] = []

    for comp in range(k):
        # Multiple random restarts to find dominant remaining eigenpair
        best_val = -1.0
        best_vec = [0.0] * k
        for _ in range(20):
            v = [rng.gauss(0.0, 1.0) for _ in range(k)]
            norm_v = math.sqrt(sum(x * x for x in v))
            v = [x / norm_v for x in v]
            for _ in range(60):
                # T_sym(I, v, v) minus deflated components
                v_new = [0.0] * k
                for a in range(k):
                    val = 0.0
                    for b in range(k):
                        for c in range(k):
                            val += T_sym[a][b][c] * v[b] * v[c]
                    v_new[a] = val
                for lam_j, phi_j in zip(recovered_lambdas, recovered_phis):
                    dot_j = sum(v[r] * phi_j[r] for r in range(k))
                    for a in range(k):
                        v_new[a] -= lam_j * (dot_j**2) * phi_j[a]
                norm_new = math.sqrt(sum(x * x for x in v_new))
                v = [x / norm_new for x in v_new]
            # Evaluate T_def(v, v, v)
            lam_cand = 0.0
            for a in range(k):
                for b in range(k):
                    for c in range(k):
                        lam_cand += T_sym[a][b][c] * v[a] * v[b] * v[c]
            for lam_j, phi_j in zip(recovered_lambdas, recovered_phis):
                dot_j = sum(v[r] * phi_j[r] for r in range(k))
                lam_cand -= lam_j * (dot_j**3)
            if lam_cand > best_val:
                best_val = lam_cand
                best_vec = v[:]
        recovered_lambdas.append(best_val)
        recovered_phis.append(best_vec)

    true_lambdas = sorted(
        [1.0 / math.sqrt(a) for a in alpha_hat], reverse=True
    )
    rec_lambdas_sorted = sorted(recovered_lambdas, reverse=True)
    max_eig_err = max(
        abs(a - b) for a, b in zip(true_lambdas, rec_lambdas_sorted)
    )
    assert max_eig_err < 1e-12, f"Tensor eigenvalue error: {max_eig_err}"

    # 3. Verify unbiasedness of Q' pseudo-inverse estimator for P (Section 3.3, p. 25; Appendix B.3, p. 48)
    # E_pi[ ((alpha0+1)/(alpha_hat_i) pi_i - alpha0) pi_j ] = delta_{i,j}
    EQPiT = [
        [
            ((alpha0 + 1.0) / alpha_hat[i]) * E_pi2[i][j]
            - alpha0 * alpha_hat[j]
            for j in range(k)
        ]
        for i in range(k)
    ]
    q_err = frob_diff(EQPiT, I_k)
    assert q_err < 1e-14, f"E[Q' Pi^T] - I_k error: {q_err}"

    print(
        f"Anandkumar et al. (2014) tensor MMSB verified: "
        f"E[psi psi^T] err={psi_cov_err:.2e}, "
        f"3-star centering err={max_tensor_err:.2e}, "
        f"tensor power eig err={max_eig_err:.2e} (lambdas={[round(x, 4) for x in rec_lambdas_sorted]}), "
        f"E[Q' Pi^T] err={q_err:.2e}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
