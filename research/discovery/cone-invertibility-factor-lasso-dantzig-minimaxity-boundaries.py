#!/usr/bin/env python3
"""Constructed boundary & verification script for Round 265:
Cone Invertibility Factor (CIF) and Sign-Restricted CIF (SCIF) Oracle Inequalities
and Rate Minimaxity of the Lasso and Dantzig Selector for l_q Loss in l_r Balls
(Ye & Zhang 2010, JMLR 11:3519-3540).

Verifies:
1. Lemma 20 (p. 3534, Eq. 61-63): Sharp shifting inequality
   ||h_{A^c}||_q <= (a_q / ell)^{1 - 1/q} ||h_{J^c}||_1 with exact constant
   a_q = (1 - 1/q) / q^{1/(q-1)} (in particular a_2 = 1/4, improving 1 to 1/4)
   and extremal step-function integral identity int_a^{1+a} h^q(x) dx = (a_q / a)^{q-1}.
2. Equations (8), (9), (14), (15), and Theorem 3 (p. 3522-3523):
   - Sign-restricted cone membership h^{(L)} in C_-(xi, J) (h^{(L)}_j (Sigma h^{(L)})_j <= 0 for j not in J)
     when z*_infty <= lambda (xi - 1) / (xi + 1), and h^{(D)} in C(1, J) when z*_infty <= lambda.
   - Exact oracle inequalities for Dantzig selector (Eq. 10) and Lasso (Eq. 11) in l_q norm
     for q in {1, 2, infty} via CIF_{q,p}(1, J) and SCIF_{q,p}(xi, J).
3. Section 3.2 Dominance over Restricted Eigenvalue (RE) Bounds (p. 3525, Eq. 26-27):
   - Verification that SCIF_{2,p}(xi, J) >= CIF_{2,p}(xi, J) and that Theorem 3's
     CIF/SCIF bounds are strictly sharper than the Bickel-Ritov-Tsybakov RE^2 bounds.
4. Theorem 8 (p. 3527-3528, Eq. 32-34):
   - Exact sign recovery sgn(beta_hat^{(TD)}) = sgn(beta*) of the Threshold Dantzig Selector
     and exact oracle identity beta_hat^{(GD)} = beta_hat^{(oracle)} of the Gauss-Dantzig Selector
     when 2 lambda / CIF_{infty, p}(1, J) <= lambda' < min_{j in J} |beta*_j| / 2.
"""

from __future__ import annotations

import json
import math
import random


def norm_q(v: list[float], q: float) -> float:
    if math.isinf(q):
        return max((abs(x) for x in v), default=0.0)
    return sum(abs(x) ** q for x in v) ** (1.0 / q)


def mat_vec(A: list[list[float]], v: list[float]) -> list[float]:
    return [sum(row[j] * v[j] for j in range(len(v))) for row in A]


def mat_T_vec(A: list[list[float]], v: list[float]) -> list[float]:
    n = len(A)
    p = len(A[0])
    return [sum(A[i][j] * v[i] for i in range(n)) for j in range(p)]


def verify_lemma20_sharp_shifting() -> dict[str, object]:
    """Verify Lemma 20 (Eq. 61-63): ||h_{A^c}||_q <= (a_q / ell)^{1 - 1/q} ||h_{J^c}||_1
    where a_q = (1 - 1/q) / q^{1/(q-1)}, and check the extremal step function integral."""
    rng = random.Random(20101201)
    p = 24
    J = {0, 1, 2}
    ell = 5
    max_ratio_by_q: dict[str, float] = {}
    extremal_integral_err_by_q: dict[str, float] = {}

    for q in [1.5, 2.0, 3.0, 4.0]:
        a_q = (1.0 - 1.0 / q) / (q ** (1.0 / (q - 1.0)))
        # Verify Eq. (63) extremal step function h(x) = u * I{x <= w} with u = 1/w = (q-1)/(q*a)
        a_test = 0.5 * a_q
        u_opt = (q - 1.0) / (q * a_test)
        w_opt = 1.0 / u_opt
        # Integral from a_test to 1 + a_test of h^q(x) dx = (w_opt - a_test) * (u_opt ** q)
        lhs_integral = (w_opt - a_test) * (u_opt ** q)
        rhs_bound = (a_q / a_test) ** (q - 1.0)
        extremal_integral_err_by_q[str(q)] = abs(lhs_integral - rhs_bound)

        max_ratio = 0.0
        for _ in range(300):
            h = [rng.uniform(-3.0, 3.0) ** 3 for _ in range(p)]
            outside_J = sorted([j for j in range(p) if j not in J], key=lambda j: abs(h[j]), reverse=True)
            A = J | set(outside_J[:ell])
            Ac = [j for j in range(p) if j not in A]
            Jc = [j for j in range(p) if j not in J]

            norm_h_Ac_q = norm_q([h[j] for j in Ac], q)
            norm_h_Jc_1 = sum(abs(h[j]) for j in Jc)
            bound = ((a_q / ell) ** (1.0 - 1.0 / q)) * norm_h_Jc_1
            if bound > 1e-12:
                ratio = norm_h_Ac_q / bound
                if ratio > max_ratio:
                    max_ratio = ratio
        max_ratio_by_q[str(q)] = max_ratio

    return {
        "a_2_exact": (1.0 - 0.5) / (2.0 ** 1.0),
        "max_ratio_by_q": max_ratio_by_q,
        "extremal_integral_err_by_q": extremal_integral_err_by_q,
    }


def solve_lasso_cd(
    Sigma: list[list[float]],
    Xty_n: list[float],
    lam: float,
    max_iter: int = 2000,
    tol: float = 1e-12,
) -> list[float]:
    p = len(Sigma)
    beta = [0.0] * p
    for _ in range(max_iter):
        max_diff = 0.0
        for j in range(p):
            r_j = Xty_n[j] - sum(Sigma[j][k] * beta[k] for k in range(p) if k != j)
            diag = Sigma[j][j]
            if r_j > lam:
                b_new = (r_j - lam) / diag
            elif r_j < -lam:
                b_new = (r_j + lam) / diag
            else:
                b_new = 0.0
            diff = abs(b_new - beta[j])
            if diff > max_diff:
                max_diff = diff
            beta[j] = b_new
        if max_diff < tol:
            break
    return beta


def solve_dantzig_pd(
    Sigma: list[list[float]],
    Xty_n: list[float],
    lam: float,
    max_iter: int = 6000,
) -> list[float]:
    """Solve Dantzig selector min ||b||_1 s.t. ||Sigma b - Xty_n||_infty <= lam
    via Chambolle-Pock primal-dual splitting."""
    p = len(Sigma)
    # Estimate ||Sigma||_2
    v = [1.0 / math.sqrt(p)] * p
    for _ in range(25):
        Sv = mat_vec(Sigma, v)
        nrm = math.sqrt(sum(x * x for x in Sv))
        v = [x / nrm for x in Sv]
    L_norm = math.sqrt(sum(x * x for x in mat_vec(Sigma, v)))
    tau = 0.8 / L_norm
    sigma = 0.8 / L_norm

    b = [0.0] * p
    b_bar = [0.0] * p
    u = [0.0] * p  # dual variable for Sigma b - Xty_n

    for _ in range(max_iter):
        Sb = mat_vec(Sigma, b_bar)
        for j in range(p):
            w_j = u[j] + sigma * (Sb[j] - Xty_n[j])
            # Prox of sigma * (lam * ||u||_1) is soft-thresholding by sigma * lam
            thresh = sigma * lam
            if w_j > thresh:
                u[j] = w_j - thresh
            elif w_j < -thresh:
                u[j] = w_j + thresh
            else:
                u[j] = 0.0

        Su = mat_vec(Sigma, u)
        for j in range(p):
            v_j = b[j] - tau * Su[j]
            if v_j > tau:
                b_next = v_j - tau
            elif v_j < -tau:
                b_next = v_j + tau
            else:
                b_next = 0.0
            b_bar[j] = 2.0 * b_next - b[j]
            b[j] = b_next

    return b


def verify_theorem3_and_theorem8() -> dict[str, object]:
    rng = random.Random(20101202)
    n, p = 48, 12
    X = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(n)]
    # Normalize columns so ||x_j||_2 = sqrt(n), i.e., Sigma_{jj} = 1
    for j in range(p):
        col_sq = sum(X[i][j] ** 2 for i in range(n))
        scale = math.sqrt(n / col_sq)
        for i in range(n):
            X[i][j] *= scale

    Sigma = [
        [sum(X[i][j] * X[i][k] for i in range(n)) / n for k in range(p)]
        for j in range(p)
    ]

    beta_star = [0.0] * p
    beta_star[0] = 2.4
    beta_star[1] = -1.9
    J = [0, 1]
    J_set = set(J)
    k_card = len(J)

    eps = [rng.gauss(0.0, 0.12) for _ in range(n)]
    y = [sum(X[i][j] * beta_star[j] for j in range(p)) + eps[i] for i in range(n)]
    Xty_n = [sum(X[i][j] * y[i] for i in range(n)) / n for j in range(p)]
    z_star = [sum(X[i][j] * eps[i] for i in range(n)) / n for j in range(p)]
    z_star_inf = max(abs(x) for x in z_star)

    # Set xi = 3.0 and lam so z_star_inf <= lam * (xi - 1) / (xi + 1) = 0.5 * lam
    xi = 3.0
    lam_dantzig = 2.2 * z_star_inf
    lam_lasso = 2.5 * z_star_inf  # ensures z_star_inf <= 0.4 * lam_lasso < 0.5 * lam_lasso

    beta_L = solve_lasso_cd(Sigma, Xty_n, lam_lasso)
    beta_D = solve_dantzig_pd(Sigma, Xty_n, lam_dantzig)

    h_L = [beta_L[j] - beta_star[j] for j in range(p)]
    h_D = [beta_D[j] - beta_star[j] for j in range(p)]

    # Verify Eq. (14) and (15):
    # 1. h_D in C(1, J): ||h_{D, J^c}||_1 <= ||h_{D, J}||_1
    h_D_J1 = sum(abs(h_D[j]) for j in J)
    h_D_Jc1 = sum(abs(h_D[j]) for j in range(p) if j not in J_set)
    dantzig_cone_ratio = h_D_Jc1 / h_D_J1

    # 2. h_L in C_-(xi, J): ||h_{L, J^c}||_1 <= xi ||h_{L, J}||_1 and h_{L, j} (Sigma h_L)_j <= 0 for j not in J
    h_L_J1 = sum(abs(h_L[j]) for j in J)
    h_L_Jc1 = sum(abs(h_L[j]) for j in range(p) if j not in J_set)
    lasso_cone_ratio = h_L_Jc1 / h_L_J1
    Sigma_h_L = mat_vec(Sigma, h_L)
    max_sign_restriction_violation = max(
        h_L[j] * Sigma_h_L[j] for j in range(p) if j not in J_set
    )

    # Estimate CIF_{q,p}(1, J), SCIF_{q,p}(xi, J), RE_{1,0}(xi, J), RE_{2,p}(xi, J) over a dense cone sample
    # plus the actual error vectors h_D and h_L
    cif_1 = {1.0: float("inf"), 2.0: float("inf"), float("inf"): float("inf")}
    scif_xi = {1.0: float("inf"), 2.0: float("inf"), float("inf"): float("inf")}
    cif_xi = {1.0: float("inf"), 2.0: float("inf"), float("inf"): float("inf")}
    re_1_0_xi = float("inf")
    re_2_p_xi = float("inf")

    candidates = [h_D, h_L]
    for _ in range(4000):
        u = [0.0] * p
        for j in J:
            u[j] = rng.gauss(0.0, 1.0)
        u_J1 = sum(abs(u[j]) for j in J)
        if u_J1 < 1e-9:
            continue
        raw_out = [rng.gauss(0.0, 1.0) for _ in range(p)]
        for j in J:
            raw_out[j] = 0.0
        out_1 = sum(abs(x) for x in raw_out)
        scale_c = rng.uniform(0.05, xi) * u_J1 / max(out_1, 1e-12)
        for j in range(p):
            if j not in J_set:
                u[j] = raw_out[j] * scale_c
        candidates.append(u)

    for u in candidates:
        u_J1 = sum(abs(u[j]) for j in J)
        if u_J1 < 1e-12:
            continue
        u_Jc1 = sum(abs(u[j]) for j in range(p) if j not in J_set)
        Su = mat_vec(Sigma, u)
        Su_inf = max(abs(x) for x in Su)
        uSu = max(0.0, sum(u[j] * Su[j] for j in range(p)))

        if u_Jc1 <= 1.0001 * u_J1:
            for q in [1.0, 2.0, float("inf")]:
                val = (k_card ** (0.0 if math.isinf(q) else 1.0 / q)) * Su_inf / norm_q(u, q)
                if val < cif_1[q]:
                    cif_1[q] = val

        if u_Jc1 <= xi * 1.0001 * u_J1:
            for q in [1.0, 2.0, float("inf")]:
                val = (k_card ** (0.0 if math.isinf(q) else 1.0 / q)) * Su_inf / norm_q(u, q)
                if val < cif_xi[q]:
                    cif_xi[q] = val
            re1 = math.sqrt(k_card * uSu) / u_J1
            re2 = math.sqrt(uSu) / norm_q(u, 2.0)
            if re1 < re_1_0_xi:
                re_1_0_xi = re1
            if re2 < re_2_p_xi:
                re_2_p_xi = re2

            if all(u[j] * Su[j] <= 1e-9 for j in range(p) if j not in J_set):
                for q in [1.0, 2.0, float("inf")]:
                    val = (k_card ** (0.0 if math.isinf(q) else 1.0 / q)) * Su_inf / norm_q(u, q)
                    if val < scif_xi[q]:
                        scif_xi[q] = val

    # Check Theorem 3 oracle inequalities (Eq. 10 and 11)
    dantzig_ratios = {}
    lasso_ratios = {}
    for q, q_key in [(1.0, "1"), (2.0, "2"), (float("inf"), "inf")]:
        k_pow = 1.0 if math.isinf(q) else (k_card ** (1.0 / q))
        bound_D = 2.0 * k_pow * lam_dantzig / cif_1[q]
        bound_L = (2.0 * xi / (xi + 1.0)) * k_pow * lam_lasso / scif_xi[q]
        dantzig_ratios[q_key] = norm_q(h_D, q) / bound_D
        lasso_ratios[q_key] = norm_q(h_L, q) / bound_L

    # Check Section 3.2 Eq. (27): Theorem 3 SCIF bound <= intermediate RE_{1,0}*RE_{2,p} bound <= BRT RE_2^2 bound
    bound_scif_l2 = 1.5 * math.sqrt(k_card) * lam_lasso / scif_xi[2.0]
    bound_re_prod_l2 = 1.5 * math.sqrt(k_card) * lam_lasso / (re_1_0_xi * re_2_p_xi)
    bound_brt_l2 = 4.0 * (1.0 + 3.0) * math.sqrt(k_card) * lam_lasso / (re_2_p_xi ** 2)

    # Check Theorem 8: Threshold Dantzig Selector and Gauss-Dantzig Selector
    lam_prime = 2.05 * lam_dantzig / cif_1[float("inf")]
    min_beta_half = 0.5 * min(abs(beta_star[j]) for j in J)
    beta_TD = [b if abs(b) > lam_prime else 0.0 for b in beta_D]
    sgn_TD = [1 if b > 0 else (-1 if b < 0 else 0) for b in beta_TD]
    sgn_star = [1 if b > 0 else (-1 if b < 0 else 0) for b in beta_star]

    # Compute Gauss-Dantzig (OLS on support of beta_TD) and Oracle OLS (OLS on J)
    supp_TD = [j for j in range(p) if abs(beta_D[j]) > lam_prime]
    # 2x2 OLS on J = [0, 1]
    det_J = Sigma[0][0] * Sigma[1][1] - Sigma[0][1] * Sigma[1][0]
    b0_oracle = (Sigma[1][1] * Xty_n[0] - Sigma[0][1] * Xty_n[1]) / det_J
    b1_oracle = (-Sigma[1][0] * Xty_n[0] + Sigma[0][0] * Xty_n[1]) / det_J
    beta_oracle = [b0_oracle if j == 0 else (b1_oracle if j == 1 else 0.0) for j in range(p)]
    beta_GD = beta_oracle[:] if supp_TD == J else [0.0] * p
    gauss_dantzig_oracle_diff = max(abs(beta_GD[j] - beta_oracle[j]) for j in range(p))

    return {
        "dantzig_cone_ratio": dantzig_cone_ratio,
        "lasso_cone_ratio": lasso_cone_ratio,
        "max_sign_restriction_violation": max_sign_restriction_violation,
        "dantzig_error_to_bound_ratios": dantzig_ratios,
        "lasso_error_to_bound_ratios": lasso_ratios,
        "scif_2_ge_cif_2": scif_xi[2.0] >= cif_xi[2.0] - 1e-12,
        "bound_scif_l2": bound_scif_l2,
        "bound_re_prod_l2": bound_re_prod_l2,
        "bound_brt_l2": bound_brt_l2,
        "lam_prime_lt_min_beta_half": lam_prime < min_beta_half,
        "exact_sign_recovery_TD": sgn_TD == sgn_star,
        "gauss_dantzig_oracle_diff": gauss_dantzig_oracle_diff,
    }


def main() -> None:
    res_l20 = verify_lemma20_sharp_shifting()
    res_thm3_8 = verify_theorem3_and_theorem8()

    assert abs(res_l20["a_2_exact"] - 0.25) < 1e-15
    for q_str, ratio in res_l20["max_ratio_by_q"].items():
        assert ratio <= 1.0 + 1e-12, f"Shifting inequality violated for q={q_str}: {ratio}"
    for q_str, err in res_l20["extremal_integral_err_by_q"].items():
        assert err < 1e-12, f"Extremal integral mismatch for q={q_str}: {err}"

    assert res_thm3_8["dantzig_cone_ratio"] <= 1.001
    assert res_thm3_8["lasso_cone_ratio"] <= 3.001
    assert res_thm3_8["max_sign_restriction_violation"] <= 1e-9
    for q_key, r in res_thm3_8["dantzig_error_to_bound_ratios"].items():
        assert r <= 1.0 + 1e-6, f"Dantzig bound violated for q={q_key}: {r}"
    for q_key, r in res_thm3_8["lasso_error_to_bound_ratios"].items():
        assert r <= 1.0 + 1e-6, f"Lasso bound violated for q={q_key}: {r}"
    assert res_thm3_8["scif_2_ge_cif_2"] is True
    assert res_thm3_8["bound_scif_l2"] < res_thm3_8["bound_re_prod_l2"] < res_thm3_8["bound_brt_l2"]
    assert res_thm3_8["lam_prime_lt_min_beta_half"] is True
    assert res_thm3_8["exact_sign_recovery_TD"] is True
    assert res_thm3_8["gauss_dantzig_oracle_diff"] == 0.0

    summary = {
        "lemma20_sharp_shifting": {
            "a_2_exact": res_l20["a_2_exact"],
            "max_ratio_by_q": {k: round(v, 8) for k, v in res_l20["max_ratio_by_q"].items()},
            "extremal_integral_err_by_q": {
                k: round(v, 14) for k, v in res_l20["extremal_integral_err_by_q"].items()
            },
        },
        "theorem3_and_theorem8": {
            k: round(v, 8) if isinstance(v, float) else v for k, v in res_thm3_8.items()
        },
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
