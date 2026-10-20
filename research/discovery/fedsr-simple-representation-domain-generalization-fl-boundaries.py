#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 498: FedSR (Nguyen, Torr, & Lim, NeurIPS 2022)."""

import math


def gaussian_kl_1d(mu_p, var_p, mu_q, var_q):
    """Exact KL[N(mu_p, var_p) || N(mu_q, var_q)]."""
    return 0.5 * (math.log(var_q / var_p) + (var_p + (mu_p - mu_q) ** 2) / var_q - 1.0)


def gaussian_entropy_1d(var_p):
    """Differential entropy H(N(mu, var_p)) = 0.5 * log(2 * pi * e * var_p)."""
    return 0.5 * math.log(2.0 * math.pi * math.e * var_p)


def gaussian_cross_entropy_1d(mu_p, var_p, mu_q, var_q):
    """Cross entropy H(p, q) = E_p[-log q(z)] for 1D Gaussians."""
    return 0.5 * math.log(2.0 * math.pi * var_q) + (var_p + (mu_p - mu_q) ** 2) / (2.0 * var_q)


def verify_l2r_marginal_alignment():
    """Verify Eqs. (12)-(15): E_{p_i(z)}[||z||_2^2] = 2*sigma^2 * (H(p_i(z)) + KL[p_i(z) || q(z)]) - D*sigma^2*log(2*pi*sigma^2)."""
    mu_i = 1.75
    var_i = 0.64
    sigma_ref = 0.5
    var_ref = sigma_ref ** 2

    # E_{p_i(z)}[z^2] = mu_i^2 + var_i
    l2r = mu_i ** 2 + var_i
    ce = gaussian_cross_entropy_1d(mu_i, var_i, 0.0, var_ref)
    h_p = gaussian_entropy_1d(var_i)
    kl_pq = gaussian_kl_1d(mu_i, var_i, 0.0, var_ref)

    # Check Eq. (15): H(p_i(z), q(z)) = H(p_i(z)) + KL[p_i(z) || q(z)]
    eq15_err = abs(ce - (h_p + kl_pq))
    # Check Eq. (14): l2r = 2 * sigma^2 * (ce - 0.5 * log(2 * pi * sigma^2))
    const_term = 0.5 * math.log(2.0 * math.pi * var_ref)
    eq14_err = abs(l2r - 2.0 * var_ref * (ce - const_term))
    return eq15_err, eq14_err


def verify_cmi_lemmas_1_and_2():
    """Verify Lemma 1 (Eq. 17) and Lemma 2 (Eq. 19) on a discrete mixture p_i(x | y) with Gaussian encoder p(z | x)."""
    # Suppose for class y=1, client i has two inputs x_1, x_2 with p_i(x_1|y=1)=0.5, p_i(x_2|y=1)=0.5
    # Encoder p(z|x_1) = N(-1.0, 0.5), p(z|x_2) = N(1.0, 0.5)
    # Variational conditional reference r(z|y=1) = N(0.2, 1.2)
    mu_1, var_1 = -1.0, 0.5
    mu_2, var_2 = 1.0, 0.5
    mu_r, var_r = 0.2, 1.2

    # Numerical integration over z in [-8, 8]
    dz = 0.005
    zs = [-8.0 + k * dz for k in range(int(16.0 / dz) + 1)]

    def pdf(z, mu, var):
        return math.exp(-0.5 * ((z - mu) ** 2) / var) / math.sqrt(2.0 * math.pi * var)

    # p_i(z | y=1) = 0.5 * p(z|x_1) + 0.5 * p(z|x_2)
    kl_x1_r = gaussian_kl_1d(mu_1, var_1, mu_r, var_r)
    kl_x2_r = gaussian_kl_1d(mu_2, var_2, mu_r, var_r)
    ell_cmi = 0.5 * kl_x1_r + 0.5 * kl_x2_r

    # Compute exact I_i(x, z | y=1) = 0.5 * KL[p(z|x_1) || p_i(z|y=1)] + 0.5 * KL[p(z|x_2) || p_i(z|y=1)]
    # and KL[p_i(z|y=1) || r(z|y=1)] via numerical quadrature
    cmi_y1 = 0.0
    kl_pi_r = 0.0
    for z in zs:
        p1 = pdf(z, mu_1, var_1)
        p2 = pdf(z, mu_2, var_2)
        pi_z = 0.5 * p1 + 0.5 * p2
        pr = pdf(z, mu_r, var_r)
        if p1 > 1e-15:
            cmi_y1 += 0.5 * p1 * math.log(p1 / pi_z) * dz
        if p2 > 1e-15:
            cmi_y1 += 0.5 * p2 * math.log(p2 / pi_z) * dz
        if pi_z > 1e-15:
            kl_pi_r += pi_z * math.log(pi_z / pr) * dz

    # Exact identity underlying Lemmas 1 and 2: ell_cmi = I_i(x, z | y) + KL[p_i(z|y) || r(z|y)]
    decomp_err = abs(ell_cmi - (cmi_y1 + kl_pi_r))
    assert ell_cmi >= cmi_y1 - 1e-9, "Lemma 1 violated: ell_cmi must upper-bound I_i(x, z | y)"
    assert ell_cmi >= kl_pi_r - 1e-9, "Lemma 2 violated: ell_cmi must upper-bound KL[p_i(z|y) || r(z|y)]"
    return ell_cmi, cmi_y1, kl_pi_r, decomp_err


def main():
    eq15_err, eq14_err = verify_l2r_marginal_alignment()
    assert eq15_err < 1e-14 and eq14_err < 1e-14

    ell_cmi, cmi_y1, kl_pi_r, decomp_err = verify_cmi_lemmas_1_and_2()
    assert decomp_err < 1e-5, f"Expected exact CMI + KL decomposition, got {decomp_err}"

    print(
        f"[PASS] Round 498 FedSR (Nguyen, Torr, & Lim 2022): "
        f"eq15_err={eq15_err:.2e}, ell_CMI={ell_cmi:.4f} >= I(x,z|y)={cmi_y1:.4f} & KL[p_i||r]={kl_pi_r:.4f}, "
        f"decomp_err={decomp_err:.2e}"
    )


if __name__ == "__main__":
    main()
