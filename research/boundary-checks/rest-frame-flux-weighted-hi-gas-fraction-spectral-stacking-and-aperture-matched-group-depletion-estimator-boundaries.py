#!/usr/bin/env python3
"""Boundary verification for AIMech:RestFrameFluxWeightedHIGasFractionSpectralStackingAndApertureMatchedGroupDepletionEstimator.

Verifies Equations 1-6 of Roychowdhury et al. (2022; arXiv:2201.03575v1):
1. Observed-frame to rest-frame 21 cm H I differential mass spectrum transformation:
   M_{HI,nu_obs} = 4.98e7 * S_{nu_obs} * D_L^2 (Eq. 1),
   nu_em = nu_obs * (1 + z) (Eq. 2),
   M_{HI,nu_em} = M_{HI,nu_obs} / (1 + z) (Eq. 3),
   confirming exact conservation of integrated H I mass across redshift z.
2. Quadrature spatial aperture summation R_ap = sqrt(R_{beam,HWHM}^2 + R_{group/gal}^2) (Eq. 4).
3. Inverse-variance weighted gas-fraction stack <f_HI> = sum(w_i f_{HI,em,i}) / sum(w_i)
   with w_i = 1 / sigma_i^2 (Eqs. 5-6), confirming minimum-variance Cramér-Rao optimality.
"""

import math


def m_hi_nu_obs(s_nu_jy: float, d_l_mpc: float) -> float:
    """Differential H I mass per observed frequency interval [M_sun Hz^-1] (Eq. 1)."""
    return 4.98e7 * s_nu_jy * (d_l_mpc ** 2)


def transform_to_rest_frame(nu_obs_hz: float, m_obs: float, z: float) -> tuple[float, float]:
    """Transform (nu_obs, M_{HI,nu_obs}) to rest-frame (nu_em, M_{HI,nu_em}) (Eqs. 2-3)."""
    nu_em = nu_obs_hz * (1.0 + z)
    m_em = m_obs / (1.0 + z)
    return nu_em, m_em


def quadrature_aperture(r_beam_hwhm: float, r_target: float) -> float:
    """Quadrature-summed spatial extraction radius R_ap (Eq. 4)."""
    return math.sqrt(r_beam_hwhm ** 2 + r_target ** 2)


def inverse_variance_stack(f_hi_list: list[float], sigma_list: list[float]) -> tuple[float, float]:
    """Return inverse-variance weighted stack <f_HI> and its standard error (Eqs. 5-6)."""
    weights = [1.0 / (s * s) for s in sigma_list]
    w_sum = sum(weights)
    f_avg = sum(w * f for w, f in zip(weights, f_hi_list)) / w_sum
    sigma_avg = math.sqrt(1.0 / w_sum)
    return f_avg, sigma_avg


def main() -> None:
    # 1. Verify integrated H I mass invariance under rest-frame transformation (Eqs. 1-3)
    nu0_hz = 1.42040575e9
    for z in [0.02, 0.05, 0.08]:
        d_l_mpc = 200.0
        dnu_obs = 1.0e4  # 10 kHz channel width
        channels_obs = [nu0_hz / (1.0 + z) + (k - 20) * dnu_obs for k in range(41)]
        flux_jy = [0.05 * math.exp(-0.5 * ((k - 20) / 5.0) ** 2) for k in range(41)]

        m_obs_spec = [m_hi_nu_obs(s, d_l_mpc) for s in flux_jy]
        integral_obs = sum(m * dnu_obs for m in m_obs_spec)

        dnu_em = dnu_obs * (1.0 + z)
        m_em_spec = [transform_to_rest_frame(nu, m, z)[1] for nu, m in zip(channels_obs, m_obs_spec)]
        integral_em = sum(m * dnu_em for m in m_em_spec)

        assert abs(integral_obs - integral_em) / integral_obs < 1e-14

    # 2. Verify quadrature aperture summation bounds (Eq. 4)
    for r_beam, r_gal in [(1.75, 0.5), (0.25, 1.2), (1.75, 2.5)]:
        r_ap = quadrature_aperture(r_beam, r_gal)
        assert r_ap > max(r_beam, r_gal)
        assert r_ap <= r_beam + r_gal + 1e-12
        assert abs(r_ap * r_ap - (r_beam * r_beam + r_gal * r_gal)) < 1e-14

    # 3. Verify inverse-variance weighted gas-fraction stack optimality (Eqs. 5-6)
    f_samples = [0.12, 0.25, 0.08, 0.19, 0.31]
    sigmas = [0.04, 0.08, 0.02, 0.05, 0.10]
    f_opt, sig_opt = inverse_variance_stack(f_samples, sigmas)
    var_opt = sig_opt * sig_opt

    # Compare against arbitrary normalized linear weights
    alt_weights = [0.2, 0.2, 0.2, 0.2, 0.2]
    var_alt = sum((w * s) ** 2 for w, s in zip(alt_weights, sigmas))
    assert var_opt < var_alt, "Inverse-variance weights must strictly minimize stack variance"

    # Equal-rms limit reduces to unweighted arithmetic mean
    f_eq, _ = inverse_variance_stack(f_samples, [0.05] * len(f_samples))
    assert abs(f_eq - sum(f_samples) / len(f_samples)) < 1e-14

    print("All rest-frame H I gas-fraction spectral stacking boundary checks passed.")


if __name__ == "__main__":
    main()
