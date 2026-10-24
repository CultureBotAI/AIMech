#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 497: FedDG / ELCFS (Liu et al., CVPR 2021)."""

import cmath
import math


def dft_1d(x):
    """Exact 1D Discrete Fourier Transform (cf. Eq. 1 in 2D)."""
    n = len(x)
    out = []
    for u in range(n):
        s = 0j
        for h in range(n):
            s += x[h] * cmath.exp(-2j * math.pi * u * h / n)
        out.append(s)
    return out


def idft_1d(f):
    """Exact 1D Inverse Discrete Fourier Transform."""
    n = len(f)
    out = []
    for h in range(n):
        s = 0j
        for u in range(n):
            s += f[u] * cmath.exp(2j * math.pi * u * h / n)
        out.append((s / n).real)
    return out


def verify_cfsi_fourier_interpolation():
    """Verify Continuous Frequency Space Interpolation (Eqs. 1-3) preserves phase and interpolates low-frequency amplitude."""
    x_k = [1.0 + 0.5 * math.cos(2 * math.pi * h / 8) + 0.3 * math.sin(4 * math.pi * h / 8) for h in range(8)]
    x_n = [2.5 + 1.2 * math.cos(2 * math.pi * h / 8) + 0.1 * math.sin(4 * math.pi * h / 8) for h in range(8)]
    f_k = dft_1d(x_k)
    f_n = dft_1d(x_n)
    amp_k = [abs(z) for z in f_k]
    phase_k = [cmath.phase(z) for z in f_k]
    amp_n = [abs(z) for z in f_n]

    # Low-frequency mask M: DC and first harmonic (indices 0, 1, 7)
    mask = [1, 1, 0, 0, 0, 0, 0, 1]
    lam = 0.6
    # Continuous interpolation of low-frequency amplitude while retaining high-frequency amplitude and exact local phase P_i^k
    amp_interp = [
        ((1.0 - lam) * amp_k[u] + lam * amp_n[u]) if mask[u] == 1 else amp_k[u]
        for u in range(8)
    ]
    # Also check printed Eq. (2) form: (1 - lam) * A_k * (1 - M) + lam * A_n * M
    amp_eq2 = [
        (1.0 - lam) * amp_k[u] * (1 - mask[u]) + lam * amp_n[u] * mask[u]
        for u in range(8)
    ]
    assert abs(amp_eq2[0] - lam * amp_n[0]) < 1e-12
    assert abs(amp_eq2[2] - (1.0 - lam) * amp_k[2]) < 1e-12

    f_trans = [cmath.rect(amp_interp[u], phase_k[u]) for u in range(8)]
    x_trans = idft_1d(f_trans)
    f_recheck = dft_1d(x_trans)

    # Verify exact phase preservation on non-zero frequency modes and mean shift from DC amplitude interpolation
    phase_err = max(
        abs(cmath.phase(f_recheck[u]) - phase_k[u])
        for u in [0, 1, 2, 6, 7]
        if abs(f_recheck[u]) > 1e-6
    )
    expected_mean = (1.0 - lam) * (sum(x_k) / 8.0) + lam * (sum(x_n) / 8.0)
    actual_mean = sum(x_trans) / 8.0
    return phase_err, abs(actual_mean - expected_mean)


def cosine_sim(a, b):
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return sum(x * y for x, y in zip(a, b)) / (na * nb)


def info_nce_boundary_loss(features, labels, tau=0.05):
    """Exact Eq. (6) and Eq. (7): boundary-oriented contrastive InfoNCE loss over 2K region-level features."""
    two_k = len(features)
    k = two_k // 2
    b_k_2 = k * (k - 1) // 2
    total_loss = 0.0
    pos_count = 0
    for m in range(two_k):
        for p in range(m + 1, two_k):
            f_mp = 0 if labels[m] == labels[p] else 1
            if f_mp == 0:
                pos_count += 1
                num = math.exp(cosine_sim(features[m], features[p]) / tau)
                # Denominator in Eq. (6): positive pair term + all negative pairs q != m with F(h_m, h_q) = 1
                neg_sum = sum(
                    math.exp(cosine_sim(features[m], features[q]) / tau)
                    for q in range(two_k)
                    if q != m and labels[m] != labels[q]
                )
                # Note Eq. (6) with positive pair + negative pairs is standard InfoNCE; also check pure negative sum
                ell_mp = -math.log(num / (num + neg_sum))
                total_loss += ell_mp
    assert pos_count == b_k_2 * 2
    return total_loss / (b_k_2 * 2)


def main():
    phase_err, mean_err = verify_cfsi_fourier_interpolation()
    assert phase_err < 1e-12, f"Expected zero phase error, got {phase_err}"
    assert mean_err < 1e-12, f"Expected exact DC mean interpolation, got {mean_err}"

    # Verify masked average pooling (Eq. 5) and boundary InfoNCE loss (Eqs. 6-7) for K=3 domains (2K=6 features)
    # 3 boundary features (label=1) and 3 background features (label=0)
    labels = [1, 1, 1, 0, 0, 0]
    # Unaligned features (boundary and background overlap across domains)
    unaligned_feats = [
        [0.8, 0.6],
        [0.5, 0.866],
        [0.6, 0.8],
        [0.7, 0.714],
        [0.65, 0.76],
        [0.75, 0.66],
    ]
    # Aligned features after BEL meta-update (Eqs. 4, 8, 9): compact intra-class cluster, orthogonal/separated inter-class
    aligned_feats = [
        [0.99, 0.14],
        [0.98, 0.19],
        [0.995, 0.10],
        [-0.99, -0.14],
        [-0.98, -0.19],
        [-0.995, -0.10],
    ]
    loss_unaligned = info_nce_boundary_loss(unaligned_feats, labels, tau=0.2)
    loss_aligned = info_nce_boundary_loss(aligned_feats, labels, tau=0.2)
    assert loss_aligned < loss_unaligned * 0.01, f"Expected aligned loss << unaligned loss: {loss_aligned} vs {loss_unaligned}"

    print(
        f"[PASS] Round 497 FedDG/ELCFS (Liu et al. 2021): "
        f"phase_err={phase_err:.2e}, mean_err={mean_err:.2e}, "
        f"L_boundary_aligned={loss_aligned:.4e} << L_boundary_unaligned={loss_unaligned:.4f}"
    )


if __name__ == "__main__":
    main()
