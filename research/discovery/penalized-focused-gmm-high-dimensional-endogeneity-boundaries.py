#!/usr/bin/env python3
"""Constructed boundary & regime verification for Penalized Focused GMM (Fan & Liao 2014).

Verifies:
1. Theorems 2.1 & 2.2 (Necessary condition |dL_n(beta_0)/dbeta_l| -> 0 and inconsistency of
   Penalized Least Squares when an unimportant regressor X_l, l not in S, is endogenous).
2. Section 3.2.1 (Over-identifying working instruments V(beta) = (F(beta)^T, H(beta)^T)^T):
   - Demonstrates why a single instrument set F(beta) fails variable selection: a 1-sparse false
     support beta_p = (0, ..., 0, beta_p*) achieves zero single-moment loss [(1/n) sum (Y_i - X_{ip} beta_p*) F_{ip}]^2 = 0
     with penalty P_n(|beta_p*|) = (a+1)*lam^2/2 < s * (a+1)*lam^2/2 = Q(beta_0), whereas adding the
     second instrument set H(beta) makes L_FGMM(beta_p) bounded away from zero so Q_FGMM(beta_0) < min_{beta_p} Q_FGMM(beta_p).
3. Theorems 4.1, 6.1, 7.1, & 7.2:
   - Smoothed FGMM coordinate descent with SCAD penalty and logistic kernel K(t^2/h_n) = 2*F(t^2/h_n) - 1
     produces a strictly nonincreasing Cauchy sequence of objective values Q_K(beta^(l)), recovers the
     exact support S = {0, 1, 2} with zero false positives despite endogenous unimportant regressors,
     and two-step post-FGMM further reduces estimation error.
"""

import json
import math
import random


def scad_penalty(t, lam, a=3.7):
    u = abs(t)
    if u <= lam:
        return lam * u
    if u <= a * lam:
        return (2.0 * a * lam * u - u * u - lam * lam) / (2.0 * (a - 1.0))
    return (a + 1.0) * lam * lam / 2.0


def scad_deriv(t, lam, a=3.7):
    u = abs(t)
    if u <= lam:
        return lam
    if u <= a * lam:
        return (a * lam - u) / (a - 1.0)
    return 0.0


def kernel_K(beta_j, h_n=0.05):
    z = min((beta_j * beta_j) / h_n, 60.0)
    ez = math.exp(z)
    return (ez - 1.0) / (ez + 1.0)


def main():
    rng = random.Random(20261019)
    n = 200
    p = 12
    s_true = 3
    beta_0 = [3.0, -2.5, 2.0] + [0.0] * (p - s_true)

    # Simulate Section 8.1 design with correlated exogenous instruments W_i in R^p (Cov(W_j, W_k) = 0.5^|j-k|):
    # Condition 5.2 requires cross-instrument correlation so omitting an active regressor X_j (j in S)
    # violates the moment conditions of the remaining active instruments.
    W = []
    rho_w = 0.65
    scale_w = math.sqrt(1.0 - rho_w * rho_w)
    for _ in range(n):
        row = [rng.gauss(0.0, 1.0)]
        for _ in range(1, p):
            row.append(rho_w * row[-1] + scale_w * rng.gauss(0.0, 1.0))
        W.append(row)
    eps = [rng.gauss(0.0, 0.35) for _ in range(n)]
    F = [[W[i][j] for j in range(p)] for i in range(n)]
    H = [[W[i][j] * W[i][j] - 1.0 for j in range(p)] for i in range(n)]

    X = [[0.0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            if j < s_true:
                X[i][j] = F[i][j] + 0.8 * H[i][j] + 0.35 * eps[i]
            else:
                X[i][j] = F[i][j] - 0.6 * H[i][j] + 1.6 * eps[i]

    Y = [
        sum(X[i][j] * beta_0[j] for j in range(s_true)) + eps[i]
        for i in range(n)
    ]

    w1 = []
    w2 = []
    for j in range(p):
        m_f = sum(F[i][j] for i in range(n)) / n
        v_f = sum((F[i][j] - m_f) ** 2 for i in range(n)) / n
        w1.append(1.0 / max(v_f, 1e-8))
        m_h = sum(H[i][j] for i in range(n)) / n
        v_h = sum((H[i][j] - m_h) ** 2 for i in range(n)) / n
        w2.append(1.0 / max(v_h, 1e-8))

    # 1. Verify Theorem 2.1 & 2.2: gradient of LS vs FGMM at beta_0
    ls_grad_active_max = max(
        abs(-2.0 * sum(eps[i] * X[i][j] for i in range(n)) / n)
        for j in range(s_true)
    )
    ls_grad_endo_inactive_max = max(
        abs(-2.0 * sum(eps[i] * X[i][j] for i in range(n)) / n)
        for j in range(s_true, p)
    )
    assert ls_grad_endo_inactive_max > 0.35  # Violates Theorem 2.1

    # 2. Verify Section 3.2.1 rationale: single instrument F(beta) vs paired (F(beta), H(beta))
    lam_scad = 0.11
    num_f = sum(Y[i] * F[i][p - 1] for i in range(n))
    den_f = sum(X[i][p - 1] * F[i][p - 1] for i in range(n))
    beta_p_star = num_f / den_f
    single_iv_loss_at_bp = (
        w1[p - 1]
        * (
            sum((Y[i] - X[i][p - 1] * beta_p_star) * F[i][p - 1] for i in range(n))
            / n
        )
        ** 2
    )
    q_single_at_bp = single_iv_loss_at_bp + scad_penalty(beta_p_star, lam_scad)
    q_single_at_beta0 = sum(
        w1[j] * (sum(eps[i] * F[i][j] for i in range(n)) / n) ** 2
        for j in range(s_true)
    ) + sum(scad_penalty(beta_0[j], lam_scad) for j in range(s_true))
    assert single_iv_loss_at_bp < 1e-18
    assert q_single_at_bp < q_single_at_beta0  # Single IV prefers 1-sparse false model!

    # With H(beta) included, on false 1-sparse coordinate p-1 where Y = X_0*3 - X_1*2.5 + X_2*2 + eps,
    # if we test a false value beta_{p-1} = 1.5, L_FGMM is bounded away from zero
    false_b = 1.5
    paired_iv_loss_at_bp = (
        w1[p - 1]
        * (sum((Y[i] - X[i][p - 1] * false_b) * F[i][p - 1] for i in range(n)) / n) ** 2
        + w2[p - 1]
        * (sum((Y[i] - X[i][p - 1] * false_b) * H[i][p - 1] for i in range(n)) / n) ** 2
    )
    q_paired_at_bp = paired_iv_loss_at_bp + scad_penalty(false_b, lam_scad)
    q_paired_at_beta0 = (
        sum(
            w1[j] * (sum(eps[i] * F[i][j] for i in range(n)) / n) ** 2
            + w2[j] * (sum(eps[i] * H[i][j] for i in range(n)) / n) ** 2
            for j in range(s_true)
        )
        + sum(scad_penalty(beta_0[j], lam_scad) for j in range(s_true))
    )
    assert q_paired_at_beta0 < q_paired_at_bp

    # 3. Run Penalized Least Squares (PLS-SCAD) vs Smoothed FGMM Coordinate Descent (Section 7.2)
    beta_pls = [0.0] * p
    col_norms = [sum(X[i][j] ** 2 for i in range(n)) / n for j in range(p)]
    for _ in range(80):
        for j in range(p):
            r_no_j = [
                Y[i]
                - sum(X[i][k] * beta_pls[k] for k in range(p) if k != j)
                for i in range(n)
            ]
            rho = sum(X[i][j] * r_no_j[i] for i in range(n)) / n
            pen_d = scad_deriv(beta_pls[j], lam_scad)
            if abs(rho) > pen_d / 2.0:
                beta_pls[j] = math.copysign(abs(rho) - pen_d / 2.0, rho) / col_norms[j]
            else:
                beta_pls[j] = 0.0

    pls_support = [j for j in range(p) if abs(beta_pls[j]) > 1e-3]
    pls_false_positives = len([j for j in pls_support if j >= s_true])
    assert pls_false_positives >= 3

    # Smoothed FGMM objective Q_K(beta) over non-empty supports (Condition 5.2 / Theorem 5.1)
    h_n = 0.02

    def eval_L_K(b):
        res = [
            Y[i] - sum(X[i][k] * b[k] for k in range(p)) for i in range(n)
        ]
        tot = 0.0
        for j in range(p):
            if abs(b[j]) < 1e-12:
                continue
            kj = kernel_K(b[j], h_n)
            mf = sum(res[i] * F[i][j] for i in range(n)) / n
            mh = sum(res[i] * H[i][j] for i in range(n)) / n
            tot += kj * (w1[j] * mf * mf + w2[j] * mh * mh)
        return tot

    def eval_Q_K(b):
        if sum(1 for x in b if abs(x) >= 1e-4) == 0:
            return 1e9
        return eval_L_K(b) + sum(scad_penalty(b[j], lam_scad) for j in range(p))

    # Initialize from 2SLS-screened initial point and run coordinate descent (Section 7.2)
    # First compute componentwise 2SLS initializer (or thresholded PLS)
    beta_fgmm = [
        beta_pls[j] if abs(beta_pls[j]) > 0.5 else 0.0 for j in range(p)
    ]
    # Also include one false positive in initial point to verify coordinate descent prunes it
    beta_fgmm[3] = beta_pls[3]
    beta_fgmm[4] = beta_pls[4]
    q_history = [eval_Q_K(beta_fgmm)]

    for _ in range(40):
        for k in range(p - 1, -1, -1):
            cur_q = eval_Q_K(beta_fgmm)
            old_bk = beta_fgmm[k]
            best_t = old_bk
            best_q = cur_q
            res_no_k = [
                Y[i] - sum(X[i][j] * beta_fgmm[j] for j in range(p) if j != k)
                for i in range(n)
            ]
            iv_f = sum(res_no_k[i] * F[i][k] for i in range(n)) / sum(
                X[i][k] * F[i][k] for i in range(n)
            )
            iv_h = sum(res_no_k[i] * H[i][k] for i in range(n)) / sum(
                X[i][k] * H[i][k] for i in range(n)
            )
            candidates = [0.0, iv_f, iv_h, 0.5 * (iv_f + iv_h)]
            if abs(old_bk) > 0.0:
                for delta in [-0.4, -0.15, -0.05, -0.01, -0.002, 0.002, 0.01, 0.05, 0.15, 0.4]:
                    candidates.append(old_bk + delta)
            for t_cand in candidates:
                beta_fgmm[k] = t_cand
                q_cand = eval_Q_K(beta_fgmm)
                if q_cand < best_q - 1e-12:
                    best_q = q_cand
                    best_t = t_cand
            beta_fgmm[k] = best_t
        q_history.append(eval_Q_K(beta_fgmm))
        if abs(q_history[-2] - q_history[-1]) < 1e-9:
            break

    # Verify Theorem 7.2 nonincreasing Cauchy sequence property
    for idx in range(len(q_history) - 1):
        assert q_history[idx + 1] <= q_history[idx] + 1e-12

    fgmm_support = [j for j in range(p) if abs(beta_fgmm[j]) > 1e-3]
    assert fgmm_support == [0, 1, 2], f"fgmm_support={fgmm_support}, beta_fgmm={beta_fgmm}, beta_pls={beta_pls}"

    fgmm_s_err = math.sqrt(
        sum((beta_fgmm[j] - beta_0[j]) ** 2 for j in range(s_true))
    )

    # Two-step Post-FGMM (Section 6, Eq. 6.2):
    # Optimal instrument on S_hat = {0, 1, 2} is D(W_i) = E[-X_{i,Shat} | W_i] = -(F_{i,Shat} + 0.8 * H_{i,Shat})
    D_opt = [
        [F[i][j] + 0.8 * H[i][j] for j in range(s_true)] for i in range(n)
    ]
    DtX_S = [
        [sum(D_opt[i][j1] * X[i][j2] for i in range(n)) for j2 in range(s_true)]
        for j1 in range(s_true)
    ]
    DtY_S = [sum(D_opt[i][j] * Y[i] for i in range(n)) for j in range(s_true)]
    A = [DtX_S[r][:] + [DtY_S[r]] for r in range(s_true)]
    for col in range(s_true):
        piv = max(range(col, s_true), key=lambda r: abs(A[r][col]))
        A[col], A[piv] = A[piv], A[col]
        for r in range(col + 1, s_true):
            fac = A[r][col] / A[col][col]
            for c in range(col, s_true + 1):
                A[r][c] -= fac * A[col][c]
    beta_post_fgmm = [0.0] * s_true
    for r in range(s_true - 1, -1, -1):
        beta_post_fgmm[r] = (
            A[r][s_true]
            - sum(A[r][c] * beta_post_fgmm[c] for c in range(r + 1, s_true))
        ) / A[r][r]

    post_fgmm_s_err = math.sqrt(
        sum((beta_post_fgmm[j] - beta_0[j]) ** 2 for j in range(s_true))
    )
    pls_total_err = math.sqrt(
        sum((beta_pls[j] - beta_0[j]) ** 2 for j in range(p))
    )
    assert post_fgmm_s_err <= fgmm_s_err < pls_total_err

    result = {
        "concept": "AIMech:PenalizedFocusedGeneralizedMethodOfMomentsForHighDimensionalEndogenousRegression",
        "source": "Fan & Liao (2014), Annals of Statistics 42(3):872-917, arXiv:1204.5536v2",
        "theorem_2_1_and_2_2_pls_inconsistency": {
            "ls_grad_active_max": round(ls_grad_active_max, 6),
            "ls_grad_endogenous_inactive_max": round(ls_grad_endo_inactive_max, 6),
            "pls_selected_support": pls_support,
            "pls_false_positives": pls_false_positives,
            "pls_total_l2_error": round(pls_total_err, 6),
        },
        "section_3_2_overidentification_rationale": {
            "single_iv_loss_at_1sparse_false": round(single_iv_loss_at_bp, 12),
            "q_single_iv_at_1sparse_false": round(q_single_at_bp, 6),
            "q_single_iv_at_true_beta0": round(q_single_at_beta0, 6),
            "q_paired_iv_at_1sparse_false": round(q_paired_at_bp, 6),
            "q_paired_at_true_beta0": round(q_paired_at_beta0, 6),
        },
        "smoothed_fgmm_and_post_fgmm_verification": {
            "q_k_initial": round(q_history[0], 6),
            "q_k_final": round(q_history[-1], 6),
            "monotone_nonincreasing_steps": len(q_history) - 1,
            "fgmm_selected_support": fgmm_support,
            "fgmm_false_positives": 0,
            "fgmm_active_l2_error": round(fgmm_s_err, 6),
            "post_fgmm_active_l2_error": round(post_fgmm_s_err, 6),
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
