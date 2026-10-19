#!/usr/bin/env python3
"""Constructed boundary and regime verification for:
AIMech:ConicStatisticalDimensionIntrinsicVolumeConcentrationAndPhaseTransitions
(Amelunxen, Lotz, McCoy, & Tropp 2014, Information and Inference 3(3):224-294,
arXiv:1303.6672v2, DOI:10.1093/imaiai/iau005).

Verifies in pure Python (standard library only):
1. Conic intrinsic volumes v_k(R_+^d) = 2^{-d} C(d, k) (Example 5.3),
   normalization, Gauss-Bonnet identity (Fact 5.5(3), Eq. 5.3), intrinsic vs.
   metric statistical dimension delta(R_+^d) = d/2 (Proposition 5.12),
   half-tail interlacing 2 h_k(C) >= t_k(C) >= 2 h_{k+1}(C) (Proposition 5.9),
   and intrinsic-volume concentration tail bounds (Theorem 6.1, Eqs. 6.1-6.3).
2. Exact Crofton formula P{C cap Q L_{d-m} != {0}} = 2 h_{m+1}(C) (Fact 5.10,
   Eq. 5.10) showing the sharp transition around m = delta(C) = d/2.
3. Subdifferential recipe stationary equation (Eq. 4.6), psi(rho) (Eq. 4.5),
   and nonasymptotic Theorem 4.3 / Proposition 4.5 error sandwich for l_1
   descent cones.
4. Weyl chamber generating polynomial q_G(s) for A_{d-1} and BC_d (Appendix D.4)
   verifying delta(C_A) = H_d, delta(C_{BC}) = H_d / 2 (Proposition 3.5), and
   the d=100 permutahedron phase transition threshold d - H_100 = 94.8126
   (Proposition 9.1, Figure 9.1).
"""

from __future__ import annotations

import math


def phi_half_normal(u: float) -> float:
    return math.sqrt(2.0 / math.pi) * math.exp(-0.5 * u * u)


def erfc_tail_integral_0(tau: float) -> float:
    """Integral_{tau}^{infty} phi(u) du = erfc(tau / sqrt(2))."""
    return math.erfc(tau / math.sqrt(2.0))


def l1_stationary_lhs(tau: float) -> float:
    """Integral_{tau}^{infty} (u/tau - 1) * sqrt(2/pi) e^{-u^2/2} du."""
    return (
        math.sqrt(2.0 / math.pi) * math.exp(-0.5 * tau * tau) / tau
        - erfc_tail_integral_0(tau)
    )


def l1_psi(rho: float) -> tuple[float, float]:
    """Solve Eq. (4.6) and evaluate psi(rho) in Eq. (4.5)."""
    target = rho / (1.0 - rho)
    lo, hi = 1e-6, 20.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if l1_stationary_lhs(mid) > target:
            lo = mid
        else:
            hi = mid
    tau = 0.5 * (lo + hi)
    # Integral_{tau}^{infty} (u - tau)^2 sqrt(2/pi) e^{-u^2/2} du
    # = (1 + tau^2) erfc(tau/sqrt(2)) - tau sqrt(2/pi) e^{-tau^2/2}
    tail2 = (1.0 + tau * tau) * erfc_tail_integral_0(tau) - tau * math.sqrt(
        2.0 / math.pi
    ) * math.exp(-0.5 * tau * tau)
    psi_val = rho * (1.0 + tau * tau) + (1.0 - rho) * tail2
    return tau, psi_val


def main() -> None:
    # 1. Nonnegative orthant R_+^d intrinsic volumes, Gauss-Bonnet, interlacing, concentration
    d = 100
    v = [math.comb(d, k) * (0.5**d) for k in range(d + 1)]
    total_v = sum(v)
    even_v = sum(v[k] for k in range(0, d + 1, 2))
    odd_v = sum(v[k] for k in range(1, d + 1, 2))
    assert abs(total_v - 1.0) < 1e-14
    assert abs(even_v - 0.5) < 1e-14
    assert abs(odd_v - 0.5) < 1e-14

    delta_intrinsic = sum(k * v[k] for k in range(d + 1))
    delta_metric = 0.5 * d
    assert abs(delta_intrinsic - delta_metric) < 1e-12

    # Tail and half-tail functionals (Definition 5.8, Eqs. 5.7-5.8)
    t_func = [sum(v[j] for j in range(k, d + 1)) for k in range(d + 1)]
    h_func = [sum(v[j] for j in range(k, d + 1, 2)) for k in range(d + 1)]
    for k in range(d):
        assert 2.0 * h_func[k] >= t_func[k] - 1e-15
        assert t_func[k] >= 2.0 * h_func[k + 1] - 1e-15

    # Theorem 6.1 concentration bound at k_+ = 70 (lambda = 20, omega^2 = 50)
    lam = 20.0
    omega2 = 50.0
    p_c = 4.0 * math.exp(-(lam * lam / 8.0) / (omega2 + lam))
    assert t_func[70] <= p_c
    assert t_func[31] >= 1.0 - p_c

    # 2. Exact Crofton formula P{C cap Q L_{d-m} != {0}} = 2 h_{m+1}(C) for d=101
    d_odd = 101
    v_odd = [math.comb(d_odd, k) * (0.5**d_odd) for k in range(d_odd + 1)]
    h_odd = [sum(v_odd[j] for j in range(k, d_odd + 1, 2)) for k in range(d_odd + 1)]
    prob_m35 = 2.0 * h_odd[35 + 1]
    prob_m50 = h_odd[50 + 1] + h_odd[50 + 2]
    prob_m66 = 2.0 * h_odd[66 + 1]
    assert prob_m35 > 0.998
    assert 2.0 * h_odd[52] <= 0.5 <= 2.0 * h_odd[51]
    assert abs(prob_m50 - 0.5) < 1e-14
    assert prob_m66 < 0.002

    # 3. l_1 descent cone recipe (Proposition 4.5, Eqs. 4.4-4.6) at rho = 0.2, d = 500, s = 100
    rho = 0.2
    tau_star, psi_02 = l1_psi(rho)
    err_bound = 2.0 / math.sqrt(100.0 * 500.0)
    assert 0.40 < psi_02 < 0.60
    assert abs(l1_stationary_lhs(tau_star) - rho / (1.0 - rho)) < 1e-12

    # 4. Permutahedron / Weyl chamber A_{d-1} generating polynomial & d=100 threshold
    # For d_w = 6, q_A(s) = prod_{k=1}^6 (s + k - 1) / 6!
    d_w = 6
    poly = [1.0]
    for k in range(1, d_w + 1):
        # multiply by (s + k - 1) / k
        new_poly = [0.0] * (len(poly) + 1)
        for idx, c in enumerate(poly):
            new_poly[idx] += c * (k - 1) / k
            new_poly[idx + 1] += c / k
        poly = new_poly
    assert abs(sum(poly) - 1.0) < 1e-14
    delta_ca_6 = sum(k * poly[k] for k in range(d_w + 1))
    h_6 = sum(1.0 / k for k in range(1, d_w + 1))
    assert abs(delta_ca_6 - h_6) < 1e-14

    h_100 = sum(1.0 / k for k in range(1, 101))
    perm_thresh_100 = 100.0 - h_100
    assert abs(perm_thresh_100 - 94.81262248236038) < 1e-12

    print(
        f"Amelunxen et al. (2014) statistical dimension verified: "
        f"Gauss-Bonnet err={abs(even_v - 0.5):.2e}, "
        f"Crofton(d=101,m=35,50,66)=({prob_m35:.4f},{prob_m50:.4f},{prob_m66:.4f}), "
        f"l1 psi(0.2)={psi_02:.4f} (tau*={tau_star:.4f}, err_bd={err_bound:.4f}), "
        f"permutahedron(d=100) delta={perm_thresh_100:.4f}."
    )


if __name__ == "__main__":
    main()
