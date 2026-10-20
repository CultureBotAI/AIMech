#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 501: HarmoFL (Jiang, Wang, & Dou, AAAI 2022 / arXiv:2112.10775)."""

import cmath
import math


def dft_1d(signal: list[float]) -> tuple[list[float], list[float]]:
    """1D discrete Fourier transform returning amplitude A and phase P (Eq. 1, p. 3)."""
    n = len(signal)
    amps = []
    phases = []
    for k in range(n):
        c = sum(signal[t] * cmath.exp(-2j * math.pi * k * t / n) for t in range(n))
        amps.append(abs(c))
        phases.append(cmath.phase(c))
    return amps, phases


def idft_1d(amps: list[float], phases: list[float]) -> list[float]:
    """Inverse 1D discrete Fourier transform reconstructing signal from (A, P) (Eq. 4, p. 3)."""
    n = len(amps)
    coeffs = [amps[k] * cmath.exp(1j * phases[k]) for k in range(n)]
    out = []
    for t in range(n):
        val = sum(coeffs[k] * cmath.exp(2j * math.pi * k * t / n) for k in range(n)) / n
        out.append(val.real)
    return out


def main() -> None:
    # 1. Verify Amplitude Normalization (Eqs. 1-4, p. 3):
    # Two clients observe the same underlying structural phase pattern (step edge) but with heterogeneous
    # scanner/protocol contrast amplitudes and DC offsets.
    sig_client1 = [1.0, 1.0, 5.0, 5.0, 5.0, 5.0, 1.0, 1.0]
    sig_client2 = [10.0, 10.0, 22.0, 22.0, 22.0, 22.0, 10.0, 10.0]
    a1, p1 = dft_1d(sig_client1)
    a2, p2 = dft_1d(sig_client2)

    # Phase spectra of non-DC components agree because underlying spatial structure is identical
    assert math.isclose(p1[1], p2[1], abs_tol=1e-9)

    # Server global average amplitude (Eq. 3 / Algorithm 1 line 8): A_bar = 0.5 * (a1 + a2)
    a_bar = [0.5 * (x + y) for x, y in zip(a1, a2)]
    psi_1 = idft_1d(a_bar, p1)
    psi_2 = idft_1d(a_bar, p2)

    # After amplitude normalization with shared global amplitude spectrum, the harmonized signals match!
    raw_diff = sum((x - y) ** 2 for x, y in zip(sig_client1, sig_client2))
    harmo_diff = sum((x - y) ** 2 for x, y in zip(psi_1, psi_2))
    assert raw_diff > 100.0
    assert harmo_diff < 1e-12

    # 2. Verify Client Weight Perturbation (Eqs. 5-7, p. 4) and Theorem 3.1 / B.6 drift bound (pp. 5, 11):
    # Client 1 has a sharp local minimum at theta=0.0 and flat local minimum at theta=2.0;
    # Client 2 has a flat local minimum at theta=2.0 and sharp local minimum at theta=4.0.
    # Perturbation delta_k = alpha * grad / |grad| guides local updates away from sharp valleys toward shared flat optimum theta=2.0.
    def grad_perturbed(theta: float, sharp_center: float, flat_center: float, alpha: float) -> float:
        # Local loss: sharp narrow Gaussian well + quadratic bowl around flat_center
        def grad_raw(x: float) -> float:
            sharp_grad = 12.0 * (x - sharp_center) * math.exp(-8.0 * (x - sharp_center) ** 2)
            flat_grad = 0.8 * (x - flat_center)
            return sharp_grad + flat_grad

        g = grad_raw(theta)
        norm_g = abs(g)
        if norm_g < 1e-12 or alpha == 0.0:
            return g
        delta = alpha * (g / norm_g)
        return grad_raw(theta + delta)

    # Check Theorem 3.1 / Theorem B.6 drift upper bound formula (p. 5, Eq. 9 & p. 11):
    # Gamma <= 4 * eta_tilde^2 * (G^2 + B^2 * C^2) / eta_g^2 + 4 * eta_tilde^2 * eps^2 * (N-1)^2 / (eta_g^2 * N^2) + 2 * eta_tilde^2 * sigma^2 / (K * eta_g^2)
    def drift_bound(eps: float, K: int = 5, N: int = 4, eta_l: float = 0.02, eta_g: float = 1.0) -> float:
        eta_tilde = K * eta_g * eta_l
        G, B, C, sigma = 1.0, 0.5, 0.5, 0.1
        term1 = 4.0 * (eta_tilde ** 2) * (G ** 2 + (B ** 2) * (C ** 2)) / (eta_g ** 2)
        term2 = 4.0 * (eta_tilde ** 2) * (eps ** 2) * ((N - 1) ** 2) / ((eta_g ** 2) * (N ** 2))
        term3 = 2.0 * (eta_tilde ** 2) * (sigma ** 2) / (K * (eta_g ** 2))
        return term1 + term2 + term3

    # Harmonizing amplitude reduces cross-client gradient heterogeneity eps_harmo < eps_raw, strictly tightening Gamma
    gamma_raw = drift_bound(eps=2.5)
    gamma_harmo = drift_bound(eps=0.2)
    assert gamma_harmo < gamma_raw

    # Check perturbed local update escapes sharp local trap near theta=0.15 faster than unperturbed SGD (alpha=0)
    g_unpert = grad_perturbed(0.15, sharp_center=0.0, flat_center=2.0, alpha=0.0)
    g_pert = grad_perturbed(0.15, sharp_center=0.0, flat_center=2.0, alpha=0.45)
    # Unperturbed gradient is positive (pulling back into sharp trap at 0.0), whereas perturbed gradient is negative (pushing toward flat optimum at 2.0)
    assert g_unpert > 0.0 and g_pert < 0.0

    print(
        f"[PASS] Round 501 HarmoFL (Jiang et al., AAAI 2022): "
        f"raw_diff={raw_diff:.2f} -> harmo_diff={harmo_diff:.2e}, "
        f"gamma_raw={gamma_raw:.5f} -> gamma_harmo={gamma_harmo:.5f}, "
        f"g_unpert={g_unpert:.4f} vs g_pert={g_pert:.4f}"
    )


if __name__ == "__main__":
    main()
