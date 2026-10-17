#!/usr/bin/env python3
"""Constructed analytic and numerical boundary checks for AIMech:MixtureApproximationNodeSplittingDiagnostic.

Verifies:
1. Closed-form Gaussian mixture convolution for the split-node difference
   delta = theta_2^(1) - theta_2^(2) (Yang, Nott, & Presanis 2026, Section 3.2,
   Equations 16-20, Algorithm 2, pp. 17-20, and Appendix C, pp. 40-42):
   - Exact mixture density p_delta(delta) = sum_{k,j} w_k * v_j * N(delta; mu_k - m_j, Sigma_k + S_j).
   - Multimodal conflict masking boundary: when the parent-side posterior is a
     symmetric bimodal mixture 0.5*N(-d, s^2) + 0.5*N(+d, s^2) and the child-side
     posterior is N(0, s^2), the difference delta has mean 0. A single-Gaussian
     Mahalanobis approximation evaluates chi^2_1(0) and gives p_mahalanobis = 1.0
     (complete masking), whereas the exact 2-component Gaussian mixture convolution
     places a low-density valley at delta = 0 and detects the conflict via the
     density-level tail P(p_delta(delta) <= p_delta(0)).
2. Shared parent nuisance pairing vs. independent mixture convolution:
   - When theta_2^(1) = theta_1 + eps_1 and theta_2^(2) = theta_1 + eps_2 share the
     same parent draw theta_1 ~ N(0, tau^2), the paired difference cancels theta_1
     with variance 2*sigma^2, whereas independent marginalization across two separate
     draws of theta_1 inflates the difference variance to 2*(tau^2 + sigma^2).
"""
from __future__ import annotations

import json
import math


def normal_pdf(x: float, mu: float, var: float) -> float:
    return math.exp(-0.5 * ((x - mu) ** 2) / var) / math.sqrt(2.0 * math.pi * var)


def mixture_pdf(x: float, weights: list[float], means: list[float], vars_: list[float]) -> float:
    return sum(w * normal_pdf(x, m, v) for w, m, v in zip(weights, means, vars_))


def check_multimodal_mixture_vs_single_gaussian() -> dict[str, float]:
    # Parent split posterior: 0.5 * N(-3, 0.5) + 0.5 * N(+3, 0.5)
    # Child split posterior: 1.0 * N(0, 0.5)
    # Convolved difference delta = theta_2^(1) - theta_2^(2):
    # 0.5 * N(-3, 1.0) + 0.5 * N(+3, 1.0)
    w_conv = [0.5, 0.5]
    m_conv = [-3.0, 3.0]
    v_conv = [1.0, 1.0]

    # Single-Gaussian moment match of delta: mean = 0.0, variance = 0.5*(1+9) + 0.5*(1+9) = 10.0
    mean_single = 0.0
    var_single = 10.0
    mahalanobis_zero = (0.0 - mean_single) ** 2 / var_single
    p_mahalanobis = math.erfc(math.sqrt(0.5 * mahalanobis_zero))
    assert math.isclose(p_mahalanobis, 1.0, rel_tol=1e-12)

    # Exact mixture density at delta = 0
    p_zero = mixture_pdf(0.0, w_conv, m_conv, v_conv)
    # Peak density near delta = +/- 3.0
    p_peak = mixture_pdf(3.0, w_conv, m_conv, v_conv)
    assert p_zero < p_peak

    # Deterministic midpoint quadrature on [-12, 12] to compute P(p_delta(delta) <= p_delta(0))
    n_grid = 24000
    a, b = -12.0, 12.0
    h = (b - a) / n_grid
    mass_below_zero_level = 0.0
    total_mass = 0.0
    for i in range(n_grid):
        x = a + (i + 0.5) * h
        px = mixture_pdf(x, w_conv, m_conv, v_conv)
        total_mass += px * h
        if px <= p_zero:
            mass_below_zero_level += px * h

    assert math.isclose(total_mass, 1.0, rel_tol=1e-6)
    assert 0.0 < mass_below_zero_level < 0.05

    return {
        "single_gaussian_mahalanobis_p": round(p_mahalanobis, 8),
        "mixture_density_at_zero": round(p_zero, 8),
        "mixture_density_at_mode": round(p_peak, 8),
        "mixture_density_level_p": round(mass_below_zero_level, 8),
    }


def check_shared_nuisance_pairing_boundary() -> dict[str, float]:
    # Suppose theta_1 ~ N(0, tau^2) is a shared parent nuisance parameter,
    # and given theta_1, theta_2^(1) | theta_1 ~ N(theta_1 + delta_true, sigma^2),
    # theta_2^(2) | theta_1 ~ N(theta_1, sigma^2).
    tau2 = 2.0
    sigma2 = 0.5
    delta_true = 2.0

    # Paired difference conditioning on the same draw theta_1^(m):
    # delta_paired = theta_2^(1) - theta_2^(2) ~ N(delta_true, 2*sigma^2)
    var_paired = 2.0 * sigma2
    p_paired = math.erfc(abs(delta_true) / math.sqrt(2.0 * var_paired))

    # Unpaired marginal convolution ignoring shared theta_1 covariance:
    # delta_unpaired ~ N(delta_true, 2*(tau^2 + sigma^2))
    var_unpaired = 2.0 * (tau2 + sigma2)
    p_unpaired = math.erfc(abs(delta_true) / math.sqrt(2.0 * var_unpaired))

    assert var_unpaired > var_paired
    assert p_unpaired > p_paired

    return {
        "var_paired": round(var_paired, 8),
        "var_unpaired": round(var_unpaired, 8),
        "p_paired": round(p_paired, 8),
        "p_unpaired": round(p_unpaired, 8),
        "variance_inflation_ratio": round(var_unpaired / var_paired, 8),
    }


def main() -> None:
    results = {
        "multimodal_mixture_vs_single_gaussian": check_multimodal_mixture_vs_single_gaussian(),
        "shared_nuisance_pairing_boundary": check_shared_nuisance_pairing_boundary(),
        "limits": (
            "Constructed analytic Gaussian mixture convolution and deterministic quadrature checks only; "
            "no EM fitting, MCMC sampling, or real-data epidemic model execution."
        ),
    }
    print(json.dumps(results, sort_keys=True))


if __name__ == "__main__":
    main()
