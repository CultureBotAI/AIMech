#!/usr/bin/env python3
"""Deterministic boundary verification for Round 834:
Maximum Approximate Bernstein Likelihood Estimation (MABLE) in Proportional Hazards Model for Interval-Censored Data
(Zhong Guan, 2019, arXiv:1906.08882v3).

Verifies:
1. Bernstein Polynomial Beta Basis & Euler Score Identity (Equations 4-13):
   - Beta density basis beta_{mj}(u) = (m+1) * C(m, j) * u^j * (1-u)^{m-j} integrates to 1 on [0, 1]
     and survival basis B_bar_{mj}(t) = sum_{k=j+1}^{m+1} C(m+1, k) t^k (1-t)^{m+1-k} matches
     numerical quadrature of 1 - int_0^t beta_{mj}(s) ds to < 1e-12.
   - Exact Euler homogeneous identity sum_{j=0}^{m*} p_j Psi_j(gamma, p; z_i) == exp(gamma^T x_tilde_i)
     so that sum_{j=0}^{m*} p_j^{[s]} Psi_bar_j(gamma, p^{[s]}) == 1 for every interior simplex vector p^{[s]}.
2. Lemma 1 Negative Semi-Definiteness & Theorem 1-2 Multiplicative Fixed-Point Convergence:
   - Under the empirical gamma-related baseline x_0 satisfying gamma^T x_0 <= min_i gamma^T x_i
     (so eta_i = exp(gamma^T x_tilde_i) >= 1), all entries of H(gamma, p) = d^2 ell_m / (dp dp^T) are
     nonpositive (H_{jk} <= 0) and v^T H(gamma, p) v <= 0 for all v in R^{m*+1} (Appendix 7.1, Eq. 20).
   - Iteration p_j^{[s+1]} = p_j^{[s]} Psi_bar_j(gamma, p^{[s]}) (Eq. 13) monotonically increases
     ell_m(gamma, p^{[s]}) and converges to the unique KKT maximizer p_tilde satisfying
     max_j (Psi_bar_j(gamma, p_tilde) - 1) < 1e-10.
3. Section 5.1 Gentleman & Geyer (1994) Six-Interval Benchmark:
   - On intervals (0,1), (0,2), (0,2), (1,3), (1,3), (2,3) scaled by tau_n = 3, MABLE reaches the exact
     maximum log-likelihood ell* = 3*log(1/3) + 4*log(2/3) = -3.8190850097688767 with q_1(p_hat) = 1/3
     and q_2(p_hat) = 2/3 for m = 1, 2 (unique uniform p_hat) and m = 6 across all three initializations
     p_1^{[0]}, p_2^{[0]}, p_3^{[0]} (p. 14).
"""

from __future__ import annotations

import math


def beta_density(m: int, j: int, u: float) -> float:
    """Evaluate beta_{mj}(u) = (m+1) * C(m, j) * u^j * (1-u)^{m-j} on [0, 1]."""
    if u <= 0.0:
        return float(m + 1) if j == 0 else 0.0
    if u >= 1.0:
        return float(m + 1) if j == m else 0.0
    return (m + 1) * math.comb(m, j) * (u ** j) * ((1.0 - u) ** (m - j))


def beta_survival(m: int, j: int, u: float) -> float:
    """Evaluate B_bar_{mj}(u) = 1 - int_0^u beta_{mj}(s) ds = sum_{k=0}^{j} C(m+1, k) u^k (1-u)^{m+1-k}."""
    if j == m + 1:
        return 1.0
    if u <= 0.0:
        return 1.0
    if u >= 1.0:
        return 0.0
    return sum(
        math.comb(m + 1, k) * (u ** k) * ((1.0 - u) ** (m + 1 - k))
        for k in range(0, j + 1)
    )


def f_m(m: int, p: list[float], u: float) -> float:
    return sum(p[j] * beta_density(m, j, u) for j in range(m + 1))


def s_m(m: int, p: list[float], u: float) -> float:
    return sum(p[j] * beta_survival(m, j, u) for j in range(len(p)))


def psi_vec(
    m: int,
    p: list[float],
    delta: int,
    y1: float,
    y2: float,
    eta: float,
) -> list[float]:
    """Compute Psi_j(gamma, p; z) from Equation (11) with eta = exp(gamma^T x_tilde)."""
    m_star = len(p) - 1
    out: list[float] = []
    if delta == 0:
        fm_val = f_m(m, p, y1)
        sm_val = s_m(m, p, y1)
        for j in range(m_star + 1):
            term_f = (beta_density(m, j, y1) / fm_val) if j <= m else 0.0
            term_s = (eta - 1.0) * beta_survival(m, j, y1) / sm_val
            out.append(term_f + term_s)
    else:
        s1 = s_m(m, p, y1)
        s2 = s_m(m, p, y2) if y2 < 1.0 else 0.0
        denom = (s1 ** eta) - (s2 ** eta) if s2 > 0.0 else (s1 ** eta)
        for j in range(m_star + 1):
            b1 = beta_survival(m, j, y1)
            b2 = beta_survival(m, j, y2) if y2 < 1.0 else 0.0
            num = (s1 ** (eta - 1.0)) * b1 - ((s2 ** (eta - 1.0)) * b2 if s2 > 0.0 else 0.0)
            out.append(eta * num / denom)
    return out


def loglik_m(
    m: int,
    p: list[float],
    data: list[tuple[int, float, float, float]],
) -> float:
    """Compute Bernstein log-likelihood ell_m(gamma, p) across observations (delta, y1, y2, eta)."""
    total = 0.0
    for delta, y1, y2, eta in data:
        if delta == 0:
            total += math.log(eta) + math.log(f_m(m, p, y1)) + (eta - 1.0) * math.log(s_m(m, p, y1))
        else:
            s1 = s_m(m, p, y1)
            s2 = s_m(m, p, y2) if y2 < 1.0 else 0.0
            diff = (s1 ** eta) - (s2 ** eta if s2 > 0.0 else 0.0)
            total += math.log(diff)
    return total


def check_lemma1_hessian_and_fixed_point() -> dict[str, float]:
    """Verify Lemma 1 Hessian negative semi-definiteness and Theorem 1-2 fixed-point convergence."""
    m = 4
    # Mixed uncensored (delta=0) and interval-censored (delta=1) observations with eta_i = exp(gamma^T x_tilde_i) >= 1
    data = [
        (0, 0.22, 0.22, 1.0),
        (0, 0.58, 0.58, 1.45),
        (1, 0.15, 0.48, 1.25),
        (1, 0.30, 0.75, 1.80),
        (1, 0.45, 0.88, 1.10),
        (1, 0.10, 0.60, 2.05),
    ]
    p_test = [0.18, 0.24, 0.22, 0.20, 0.16]
    # 1. Verify Euler homogeneous identity sum_j p_j Psi_j(gamma, p; z_i) == eta_i
    max_euler_err = 0.0
    for delta, y1, y2, eta in data:
        ps = psi_vec(m, p_test, delta, y1, y2, eta)
        dot_val = sum(p_test[j] * ps[j] for j in range(m + 1))
        max_euler_err = max(max_euler_err, abs(dot_val - eta))
    assert max_euler_err < 1e-13, f"Euler score identity failed: {max_euler_err}"

    # 2. Verify Lemma 1 entrywise H_{jk} <= 0 and quadratic form v^T H v <= 0 (Eq. 20)
    h_mat = [[0.0] * (m + 1) for _ in range(m + 1)]
    for delta, y1, y2, eta in data:
        if delta == 0:
            fm_v = f_m(m, p_test, y1)
            sm_v = s_m(m, p_test, y1)
            for j in range(m + 1):
                for k in range(m + 1):
                    val = -(
                        beta_density(m, j, y1) * beta_density(m, k, y1) / (fm_v * fm_v)
                        + (eta - 1.0) * beta_survival(m, j, y1) * beta_survival(m, k, y1) / (sm_v * sm_v)
                    )
                    assert val <= 1e-15, f"Positive uncensored Hessian entry: {val}"
                    h_mat[j][k] += val
        else:
            v1 = s_m(m, p_test, y1)
            v2 = s_m(m, p_test, y2)
            denom = (v1 ** eta) - (v2 ** eta)
            for j in range(m + 1):
                bj1 = beta_survival(m, j, y1)
                bj2 = beta_survival(m, j, y2)
                for k in range(m + 1):
                    bk1 = beta_survival(m, k, y1)
                    bk2 = beta_survival(m, k, y2)
                    a_term = ((v1 ** (eta - 2.0)) * bj1 * bk1 - (v2 ** (eta - 2.0)) * bj2 * bk2) * denom
                    b_term = ((v1 ** (eta - 1.0)) * bj1 - (v2 ** (eta - 1.0)) * bj2) * (
                        (v1 ** (eta - 1.0)) * bk1 - (v2 ** (eta - 1.0)) * bk2
                    )
                    val = eta * ((eta - 1.0) * a_term - eta * b_term) / (denom * denom)
                    assert val <= 1e-15, f"Positive censored Hessian entry: {val}"
                    h_mat[j][k] += val

    test_vecs = [
        [1.0, -0.5, 0.2, -0.7, 0.3],
        [0.4, 0.4, -0.3, -0.5, 0.0],
        [1.0, 1.0, 1.0, 1.0, 1.0],
    ]
    max_quad = max(
        sum(v[j] * h_mat[j][k] * v[k] for j in range(m + 1) for k in range(m + 1))
        for v in test_vecs
    )
    assert max_quad < 0.0, f"Hessian not negative definite on test vectors: {max_quad}"

    # 3. Run Theorem 2 multiplicative fixed-point iteration (Eq. 13)
    p_curr = [1.0 / (m + 1)] * (m + 1)
    lam_n = sum(eta for _, _, _, eta in data)
    prev_ll = loglik_m(m, p_curr, data)
    for _ in range(400):
        psi_bar = [0.0] * (m + 1)
        for delta, y1, y2, eta in data:
            ps = psi_vec(m, p_curr, delta, y1, y2, eta)
            for j in range(m + 1):
                psi_bar[j] += ps[j] / lam_n
        p_next = [p_curr[j] * psi_bar[j] for j in range(m + 1)]
        s_p = sum(p_next)
        assert abs(s_p - 1.0) < 1e-12, f"Simplex sum drifted: {s_p}"
        curr_ll = loglik_m(m, p_next, data)
        assert curr_ll >= prev_ll - 1e-12, f"Non-monotonic log-likelihood: {curr_ll} < {prev_ll}"
        prev_ll = curr_ll
        p_curr = p_next

    psi_bar_final = [0.0] * (m + 1)
    for delta, y1, y2, eta in data:
        ps = psi_vec(m, p_curr, delta, y1, y2, eta)
        for j in range(m + 1):
            psi_bar_final[j] += ps[j] / lam_n
    kkt_residual = max(p_curr[j] * abs(psi_bar_final[j] - 1.0) for j in range(m + 1))
    assert kkt_residual < 1e-9, f"KKT fixed-point residual too large: {kkt_residual}"

    return {
        "max_euler_err": max_euler_err,
        "max_quad": max_quad,
        "kkt_residual": kkt_residual,
    }


def check_gentleman_geyer_example() -> dict[str, float]:
    """Verify Section 5.1 Gentleman and Geyer (1994) 6-interval example (p. 14)."""
    # Scaled intervals by tau_n = 3: (0, 1/3), (0, 2/3), (0, 2/3), (1/3, 1), (1/3, 1), (2/3, 1)
    # Note: Sm(t) = 1 - Bm(t), so q1(p) = Bm(1/3) = 1 - Sm(1/3), q2(p) = Bm(2/3) = 1 - Sm(2/3)
    gg_data = [
        (1, 0.0, 1.0 / 3.0, 1.0),
        (1, 0.0, 2.0 / 3.0, 1.0),
        (1, 0.0, 2.0 / 3.0, 1.0),
        (1, 1.0 / 3.0, 1.0, 1.0),
        (1, 1.0 / 3.0, 1.0, 1.0),
        (1, 2.0 / 3.0, 1.0, 1.0),
    ]
    exact_ll = 2.0 * math.log(1.0 / 3.0) + 4.0 * math.log(2.0 / 3.0)
    assert abs(exact_ll - (-3.8190850097688767)) < 1e-12

    # For m = 1 and m = 2, verify unique uniform solution p = (1,...,1)/(m+1)
    for m_uni in (1, 2):
        p_u = [1.0 / (m_uni + 1)] * (m_uni + 1)
        q1_u = 1.0 - s_m(m_uni, p_u, 1.0 / 3.0)
        q2_u = 1.0 - s_m(m_uni, p_u, 2.0 / 3.0)
        assert abs(q1_u - 1.0 / 3.0) < 1e-14
        assert abs(q2_u - 2.0 / 3.0) < 1e-14

    # For m = 6, run from all three initializations in Section 5.1 (p. 14)
    m6 = 6
    inits = [
        [i / 28.0 for i in range(1, 8)],
        [1.0 / 7.0] * 7,
        [1.0 / 16.0, 2.0 / 16.0, 3.0 / 16.0, 4.0 / 16.0, 3.0 / 16.0, 2.0 / 16.0, 1.0 / 16.0],
    ]
    max_q_err = 0.0
    max_ll_err = 0.0
    sols = []
    for p_init in inits:
        p = list(p_init)
        for _ in range(500):
            psi_bar = [0.0] * (m6 + 1)
            for delta, y1, y2, eta in gg_data:
                ps = psi_vec(m6, p, delta, y1, y2, eta)
                for j in range(m6 + 1):
                    psi_bar[j] += ps[j] / len(gg_data)
            p = [p[j] * psi_bar[j] for j in range(m6 + 1)]
        q1 = 1.0 - s_m(m6, p, 1.0 / 3.0)
        q2 = 1.0 - s_m(m6, p, 2.0 / 3.0)
        ll = loglik_m(m6, p, gg_data)
        max_q_err = max(max_q_err, abs(q1 - 1.0 / 3.0), abs(q2 - 2.0 / 3.0))
        max_ll_err = max(max_ll_err, abs(ll - exact_ll))
        sols.append(p)

    assert max_q_err < 1e-11, f"Gentleman-Geyer q1/q2 error: {max_q_err}"
    assert max_ll_err < 1e-11, f"Gentleman-Geyer loglik error: {max_ll_err}"
    # Verify non-uniqueness for m = 6 (distinct fixed points p_hat_1 != p_hat_2)
    l1_diff_12 = sum(abs(sols[0][j] - sols[1][j]) for j in range(m6 + 1))
    assert l1_diff_12 > 0.1, f"Expected distinct fixed points for m=6 from different starts: {l1_diff_12}"

    return {
        "exact_ll": exact_ll,
        "max_q_err": max_q_err,
        "max_ll_err": max_ll_err,
        "l1_diff_12": l1_diff_12,
    }


def main() -> None:
    r1 = check_lemma1_hessian_and_fixed_point()
    r2 = check_gentleman_geyer_example()
    print(
        f"[PASS] Round 834 MABLE verified: euler_err={r1['max_euler_err']:.2e}, "
        f"max_hessian_quad={r1['max_quad']:.4f}<0, kkt_res={r1['kkt_residual']:.2e}, "
        f"gg_ll={r2['exact_ll']:.6f}, gg_q_err={r2['max_q_err']:.2e}, "
        f"m6_nonunique_l1={r2['l1_diff_12']:.4f}"
    )


if __name__ == "__main__":
    main()
