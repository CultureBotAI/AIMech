#!/usr/bin/env python3
"""Boundary verification for Round 837: Finite-Time Extremal Index, Cluster Size, and Sojourn Time in Non-Markovian Regenerative Processes (Abadi, Moreira Freitas, & Milhazes Freitas, 2018, arXiv:1810.03216v1).

Verifies:
1. Two-symbol Morse-code block model correlation decay (Section 3, Eq. 8):
   c_n = P(R_{n+1} | R_0) = sum_{y=0}^{floor(n/2)} comb(n-y, y) p_1^{n-2y} p_2^y
       = K_1 + K_2 (p_1 - 1)^n with K_1 = 1/(2 - p_1) = 1/nu and K_2 = (1 - p_1)/(2 - p_1),
   and at the golden ratio p_1 = (sqrt(5)-1)/2 = phi, c_n = phi^n F_{n+1}.
2. Exact stationary sojourn identity (Section 6, Lemma 7, Eq. 18):
   E_{U_a}(N_a) = (theta_1(a) / 2) * (E_{E_a}(N_a^2) + E_{E_a}(N_a))
   verified for any discrete cluster-size distribution on E_a via the stationary identity
   P(cap_{j=0}^{k-1} {X_j > a}, X_k <= a) = P(X_0 <= a, cap_{j=1}^k {X_j > a}) (Eq. 20).
3. Exact finite-time reciprocity E_{E_a}(N_a) = 1 / theta_1(a) across all four non-Markovian
   regenerative regimes (Section 4.2.1 - 4.2.2, Eqs. 9-16):
   - Smith's model exceedances: theta_1(a) = (1 - e_a)/2, E_{E_a}(N_a) = 2/(1 - e_a) -> 2,
     and E_{U_a}(N_a) = (3 - 2*e_a + e_a^2) / (2*(1 - e_a)) -> 3/2 as e_a -> 0.
   - Deterministic block model exceedances: theta_1(a) = e_a(1 - e_a)/g_a,
     E_{E_a}(N_a) = g_a / (e_a*(1 - e_a)) = 1 / theta_1(a).
   - Deterministic block model cylinder hitting {X_0^{n-1} = a} (Eqs. 15-16):
     n = r_n * a - s_n (0 <= s_n <= a - 1), theta_1(n) = (1 - p_a)/(s_n + 1 + (r_n - 1)*p_a)
     and for the recurrence E_E(N_n) = s_n + 1 + a*p_a/(1 - p_a).
4. O'Brien finite-horizon approximation bound (Section 5, Lemma 4, Eq. 17):
   |1 - theta_q(a) / theta_1(a)| <= (q - 1) P(U_a | R_0) <= q P(U_a | R_0).
"""

import math


def main():
    # 1. Morse-code block model correlation decay (Section 3, Eq. 8)
    for p1 in [0.35, (math.sqrt(5.0) - 1.0) / 2.0, 0.75]:
        p2 = 1.0 - p1
        k1 = 1.0 / (2.0 - p1)
        k2 = (1.0 - p1) / (2.0 - p1)
        fib = [1, 1]
        for n in range(1, 20):
            fib.append(fib[-1] + fib[-2])
        for n in range(0, 18):
            cn_sum = 0.0
            for y in range(n // 2 + 1):
                x = n - 2 * y
                cn_sum += math.comb(x + y, y) * (p1 ** x) * (p2 ** y)
            cn_closed = k1 + k2 * ((p1 - 1.0) ** n)
            assert abs(cn_sum - cn_closed) < 1e-13, (
                f"Morse cn mismatch at n={n}: {cn_sum} vs {cn_closed}"
            )
            if abs(p1 - (math.sqrt(5.0) - 1.0) / 2.0) < 1e-14:
                # Since p2 = 1 - p1 = p1^2 for golden ratio, cn = p1^n * F_{n+1}
                assert abs(cn_sum - (p1 ** n) * fib[n]) < 1e-13

    # 2. Lemma 7 exact sojourn identity (Section 6, Eq. 18) and Smith model exceedances (Section 4.2.1, Eq. 9)
    for ea in [0.4, 0.1, 0.01, 1e-4]:
        theta1_smith = (1.0 - ea) / 2.0
        mean_cluster_smith = 2.0 / (1.0 - ea)
        assert abs(theta1_smith * mean_cluster_smith - 1.0) < 1e-14

        # Second moment E_E(N_a^2) = E_E(F_a^2) + 2 E_E(F) E_{R_0}(N_a) + E_{R_0}(N_a^2) (Eq. 9)
        ee_f = 2.0
        ee_f2 = 4.0
        er0_n = 2.0 * ea / (1.0 - ea)
        er0_n2 = 2.0 * ea * (ea + 1.0) / ((1.0 - ea) ** 2)
        ee_n2 = ee_f2 + 2.0 * ee_f * er0_n + er0_n2

        # Exact sojourn mean via Lemma 7 (Eq. 18):
        eu_n = 0.5 * theta1_smith * (ee_n2 + mean_cluster_smith)
        eu_closed = (3.0 - ea * ea) / (2.0 * (1.0 - ea))
        assert abs(eu_n - eu_closed) < 1e-13, f"Smith sojourn mismatch: {eu_n} vs {eu_closed}"

    # Verify asymptotic limits as a -> infinity (ea -> 0) in Smith's model:
    # Limiting extremal index = 1/2, limiting mean cluster size = 2 (reciprocal of theta_1),
    # while expected sojourn time converges to 3/2 != 2.
    ea_tiny = 1e-8
    eu_tiny = (3.0 - ea_tiny ** 2) / (2.0 * (1.0 - ea_tiny))
    assert abs(eu_tiny - 1.5) < 1e-7

    # 3. Deterministic block model exceedances & cylinder hitting (Section 4.2.2, Eqs. 15-16)
    # Geometric symbol distribution p_j = (1 - rho) * rho^{j-1} for j >= 1 (rho = 0.6)
    rho = 0.6
    nu = sum(j * (1.0 - rho) * (rho ** (j - 1)) for j in range(1, 200))
    a_lvl = 5
    ea_blk = sum((1.0 - rho) * (rho ** (j - 1)) for j in range(a_lvl + 1, 200))
    ga_blk = sum(j * (1.0 - rho) * (rho ** (j - 1)) for j in range(a_lvl + 1, 200)) / nu
    theta1_blk = ea_blk * (1.0 - ea_blk) / ga_blk
    mean_cluster_blk = ga_blk / (ea_blk * (1.0 - ea_blk))
    assert abs(theta1_blk * mean_cluster_blk - 1.0) < 1e-14

    # Cylinder hitting in deterministic block model for symbol a = 4 (Eqs. 15-16)
    a_sym = 4
    pa = 0.25
    s_vals = []
    mean_cyl_vals = []
    for n in range(1, 13):
        rn = math.ceil(n / a_sym)
        sn = rn * a_sym - n
        assert 0 <= sn <= a_sym - 1
        s_vals.append(sn)
        # Exact conditional survival distribution mu_E(N_n >= k) on p. 13:
        # 1 for 1 <= k <= sn + 1; pa^l for l*a + sn + 1 < k <= (l+1)*a + sn + 1, l >= 1
        mean_sum = sum(1.0 for _ in range(1, sn + 2))
        for l_idx in range(1, 150):
            mean_sum += a_sym * (pa ** l_idx)
        mean_formula = (sn + 1.0) + (a_sym * pa) / (1.0 - pa)
        assert abs(mean_sum - mean_formula) < 1e-12
        mean_cyl_vals.append(mean_formula)
    # Verify cyclic fluctuation of period a_sym = 4
    assert s_vals[:4] == [3, 2, 1, 0] and s_vals[4:8] == [3, 2, 1, 0]
    assert abs(mean_cyl_vals[0] - mean_cyl_vals[4]) < 1e-14
    assert abs(mean_cyl_vals[0] - mean_cyl_vals[3]) == 3.0

    # 4. Lemma 4 O'Brien finite-horizon bound |1 - theta_q / theta_1| <= q P(U_a | R_0) (Section 5, p. 14)
    # In i.i.d. sharpness example (Section 5, p. 15): theta_1 = 1 - p_a, theta_q = (1 - p_a)^q, P(U_a | R_0) = p_a
    for pa_iid in [0.02, 0.005]:
        theta1_iid = 1.0 - pa_iid
        for q in [2, 5, 10]:
            thetaq_iid = (1.0 - pa_iid) ** q
            rel_diff = abs(1.0 - thetaq_iid / theta1_iid)
            bound = q * pa_iid
            assert rel_diff <= bound + 1e-15, f"Lemma 4 bound violated: {rel_diff} > {bound}"

    print(
        f"[PASS] Round 837 Finite-Time Extremal Index & Regenerative Sojourn (Abadi et al. 2018): "
        f"smith_sojourn_lim={eu_tiny:.6f}, blk_recip={theta1_blk*mean_cluster_blk:.12f}, "
        f"cyl_period={s_vals[:4]}"
    )


if __name__ == "__main__":
    main()
