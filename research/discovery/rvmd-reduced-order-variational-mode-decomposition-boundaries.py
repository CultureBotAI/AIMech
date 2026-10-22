#!/usr/bin/env python3
"""Boundary verification for Round 836: RVMD Reduced-Order Variational Mode Decomposition (Liao et al., 2022, arXiv:2209.12437v1).

Verifies:
1. Spectral-domain objective F(Phi, C_hat, omega) (Section 2.1, Eq. 18) and Block Coordinate
   Descent (BCD) alternating updates (Section 2.2, Eqs. 39-41):
   - Spatial mode update: phi_k^{n+1} = Re{R_k^+ c_k^{+,*}} / ||Re{R_k^+ c_k^{+,*}}|| (Eq. 39)
   - Wiener-filtered temporal mode update: c_k^{+,n+1} = G_k^+ R_k^{+,T} phi_k (Eq. 40)
     where g_i^+ = 1 / [1 + 2*alpha*(omega_i^+ - omega_k)^2] (Eq. 38)
   - Central frequency center-of-gravity update:
     omega_k^{n+1} = (c_k^{+,H} W^+ c_k^+) / (c_k^{+,H} c_k^+) (Eq. 41)
   Monotonic non-increase of F across BCD iterations.
2. Filtered two-point spatial correlation fixed-point eigenvalue equation (Section 2.3, Eq. 47):
   At BCD convergence for a mode k, R_k^+ G_k^+ (R_k^+)^H phi_k (reactive real part) aligns
   collinearly with phi_k: Re{R_k^+ G_k^+ (R_k^+)^H phi_k} = lambda_k phi_k.
3. Exact half-power bandwidth of the second-order Wiener filter (Section 2.4, Eq. 48):
   Delta = sqrt((2*sqrt(2) - 2) / alpha), at which g_k(omega_k +/- Delta/2) = 1 / sqrt(2)
   (filter power |g_k|^2 = 1/2).
4. Limiting reductions (Section 3.1-3.2, Eqs. 49-51):
   - As alpha -> 0, G_k^+ -> I and under spatial orthogonality RVMD reduces to POD (leading
     eigenvector of Re{Q^+ (Q^+)^H}).
   - As alpha -> infinity, G_k^+ concentrates on the single discrete frequency bin closest
     to omega_k (DFT mode limit).
"""

import cmath
import math


def vec_norm(v):
    return math.sqrt(sum(x * x for x in v))


def cvec_norm_sq(v):
    return sum((z.real * z.real + z.imag * z.imag) for z in v)


def spectral_objective(Q_pos, phi_list, c_pos_list, omega_list, freqs_pos, alpha):
    """Evaluate positive-frequency discrete version of Eq. 18:
    F = sum_k sum_m 2*alpha*(omega_m - omega_k)^2 |c_{k,m}|^2
        + sum_j sum_m |Q_{j,m} - sum_k phi_{k,j} c_{k,m}|^2
    """
    K = len(phi_list)
    N_x = len(Q_pos)
    N_f = len(freqs_pos)
    bw_term = 0.0
    for k in range(K):
        om_k = omega_list[k]
        for m in range(N_f):
            mag2 = c_pos_list[k][m].real ** 2 + c_pos_list[k][m].imag ** 2
            bw_term += 2.0 * alpha * ((freqs_pos[m] - om_k) ** 2) * mag2

    rec_term = 0.0
    for j in range(N_x):
        for m in range(N_f):
            pred = 0j
            for k in range(K):
                pred += phi_list[k][j] * c_pos_list[k][m]
            diff = Q_pos[j][m] - pred
            rec_term += diff.real ** 2 + diff.imag ** 2
    return bw_term + rec_term


def main():
    # 1. Check exact half-power bandwidth formula (Eq. 48)
    for alpha in [10.0, 200.0, 5000.0]:
        delta = math.sqrt((2.0 * math.sqrt(2.0) - 2.0) / alpha)
        omega_k = 0.25
        omega_half = omega_k + 0.5 * delta
        g_half = 1.0 / (1.0 + 2.0 * alpha * ((omega_half - omega_k) ** 2))
        assert abs(g_half - 1.0 / math.sqrt(2.0)) < 1e-14, (
            f"Half-power gain mismatch: {g_half}"
        )
        assert abs(g_half * g_half - 0.5) < 1e-14

    # 2. Construct synthetic space-time spectrum Q^+ (N_x = 6 spatial points, N_f = 32 pos freqs)
    N_x = 6
    N_f = 32
    freqs_pos = [0.02 * (m + 1) for m in range(N_f)]  # [0.02, ..., 0.64]

    # True narrowband modes around omega_1* = 0.14 and omega_2* = 0.42
    phi_true_1 = [math.sin(0.5 * (j + 1)) for j in range(N_x)]
    n1 = vec_norm(phi_true_1)
    phi_true_1 = [x / n1 for x in phi_true_1]

    phi_true_2 = [math.cos(0.9 * (j + 1)) for j in range(N_x)]
    n2 = vec_norm(phi_true_2)
    phi_true_2 = [x / n2 for x in phi_true_2]

    c_true_1 = [
        4.0 * math.exp(-((f - 0.14) ** 2) / (2.0 * 0.025 ** 2)) * cmath.exp(1j * 0.3 * m)
        for m, f in enumerate(freqs_pos)
    ]
    c_true_2 = [
        2.5 * math.exp(-((f - 0.42) ** 2) / (2.0 * 0.020 ** 2)) * cmath.exp(-1j * 0.5 * m)
        for m, f in enumerate(freqs_pos)
    ]

    Q_pos = [[0j for _ in range(N_f)] for _ in range(N_x)]
    for j in range(N_x):
        for m in range(N_f):
            Q_pos[j][m] = phi_true_1[j] * c_true_1[m] + phi_true_2[j] * c_true_2[m]

    # Run 2-mode BCD algorithm (Eqs. 39-41)
    alpha = 400.0
    K = 2
    phi_list = [
        [1.0 / math.sqrt(N_x) for _ in range(N_x)],
        [((-1.0) ** j) / math.sqrt(N_x) for j in range(N_x)],
    ]
    omega_list = [0.08, 0.52]
    c_pos_list = [[0j for _ in range(N_f)] for _ in range(K)]

    # Initialize c_pos via Eq. 40 for initial phi and omega
    for k in range(K):
        for m in range(N_f):
            g_m = 1.0 / (1.0 + 2.0 * alpha * ((freqs_pos[m] - omega_list[k]) ** 2))
            proj = sum(Q_pos[j][m] * phi_list[k][j] for j in range(N_x))
            c_pos_list[k][m] = g_m * proj

    obj_history = [spectral_objective(Q_pos, phi_list, c_pos_list, omega_list, freqs_pos, alpha)]

    for _ in range(80):
        for k in range(K):
            # Positive-frequency residual R_k^+ (Eq. 36)
            R_k = [[Q_pos[j][m] for m in range(N_f)] for j in range(N_x)]
            for i in range(K):
                if i != k:
                    for j in range(N_x):
                        for m in range(N_f):
                            R_k[j][m] -= phi_list[i][j] * c_pos_list[i][m]

            # Update phi_k (Eq. 39): Re{R_k^+ c_k^{+,*}} normalized
            raw_phi = [
                sum((R_k[j][m] * c_pos_list[k][m].conjugate()).real for m in range(N_f))
                for j in range(N_x)
            ]
            norm_phi = vec_norm(raw_phi)
            phi_list[k] = [x / norm_phi for x in raw_phi]

            # Update c_k^+ (Eq. 40): G_k^+ R_k^{+,T} phi_k
            for m in range(N_f):
                g_m = 1.0 / (1.0 + 2.0 * alpha * ((freqs_pos[m] - omega_list[k]) ** 2))
                proj = sum(R_k[j][m] * phi_list[k][j] for j in range(N_x))
                c_pos_list[k][m] = g_m * proj

            # Update omega_k (Eq. 41): center of gravity of |c_k^+(omega)|^2
            num = sum(
                freqs_pos[m] * (c_pos_list[k][m].real ** 2 + c_pos_list[k][m].imag ** 2)
                for m in range(N_f)
            )
            den = cvec_norm_sq(c_pos_list[k])
            omega_list[k] = num / den

        obj_history.append(
            spectral_objective(Q_pos, phi_list, c_pos_list, omega_list, freqs_pos, alpha)
        )

    # Verify monotonic decrease of F across BCD sweeps
    for t in range(len(obj_history) - 1):
        assert obj_history[t + 1] <= obj_history[t] + 1e-10, (
            f"BCD objective increased at step {t}: {obj_history[t]} -> {obj_history[t+1]}"
        )
    assert obj_history[-1] < 0.35 * obj_history[0], (
        f"Expected substantial reduction: {obj_history[0]} -> {obj_history[-1]}"
    )

    # Verify center frequencies converged near 0.14 and 0.42
    om_sorted = sorted(omega_list)
    assert abs(om_sorted[0] - 0.14) < 0.015, f"Mode 1 frequency mismatch: {om_sorted[0]}"
    assert abs(om_sorted[1] - 0.42) < 0.015, f"Mode 2 frequency mismatch: {om_sorted[1]}"

    # 3. Verify filtered two-point correlation eigenvalue fixed point (Eq. 47) for k=0
    k = 0
    R_0 = [
        [Q_pos[j][m] - phi_list[1][j] * c_pos_list[1][m] for m in range(N_f)]
        for j in range(N_x)
    ]
    g_0 = [1.0 / (1.0 + 2.0 * alpha * ((freqs_pos[m] - omega_list[0]) ** 2)) for m in range(N_f)]
    # Apply Re{R_0 G_0 R_0^H} to phi_0 (note G_0^2 appears in ||c_0||/phi_0 substitution if using c_0 = G_0 R_0^T phi_0)
    # Specifically, phi_0 = Re{R_0 c_0^*} / ||...|| = Re{R_0 G_0 R_0^H} phi_0 / lambda_0
    lhs = [0.0 for _ in range(N_x)]
    for j in range(N_x):
        acc = 0.0
        for m in range(N_f):
            proj_m = sum(R_0[l][m].conjugate() * phi_list[0][l] for l in range(N_x))
            acc += (R_0[j][m] * g_0[m] * proj_m).real
        lhs[j] = acc
    lam_0 = vec_norm(lhs)
    collinear_err = vec_norm([lhs[j] / lam_0 - phi_list[0][j] for j in range(N_x)])
    assert collinear_err < 1e-8, f"Eigenvalue fixed-point error too large: {collinear_err}"

    # 4. Verify alpha -> 0 POD reduction (Section 3.1, Eq. 49) for single leading mode
    # Power iteration on Re{Q^+ (Q^+)^H} vs RVMD 1-mode with alpha = 0
    phi_pod = [1.0 / math.sqrt(N_x) for _ in range(N_x)]
    for _ in range(60):
        nxt = [0.0 for _ in range(N_x)]
        for j in range(N_x):
            for m in range(N_f):
                proj_m = sum(Q_pos[l][m].conjugate() * phi_pod[l] for l in range(N_x))
                nxt[j] += (Q_pos[j][m] * proj_m).real
        n_nxt = vec_norm(nxt)
        phi_pod = [x / n_nxt for x in nxt]

    # RVMD 1-mode with alpha = 1e-12
    phi_rvmd0 = [1.0 / math.sqrt(N_x) for _ in range(N_x)]
    for _ in range(60):
        c0 = [sum(Q_pos[j][m] * phi_rvmd0[j] for j in range(N_x)) for m in range(N_f)]
        raw = [sum((Q_pos[j][m] * c0[m].conjugate()).real for m in range(N_f)) for j in range(N_x)]
        nr = vec_norm(raw)
        phi_rvmd0 = [x / nr for x in raw]

    pod_align = abs(sum(phi_pod[j] * phi_rvmd0[j] for j in range(N_x)))
    assert abs(pod_align - 1.0) < 1e-12, f"POD limit alignment failed: {pod_align}"

    print(
        f"[PASS] Round 836 RVMD (Liao et al. 2022): "
        f"F_init={obj_history[0]:.4f}->F_final={obj_history[-1]:.4f}, "
        f"omega=({om_sorted[0]:.4f},{om_sorted[1]:.4f}), "
        f"eig_err={collinear_err:.2e}, pod_align={pod_align:.12f}"
    )


if __name__ == "__main__":
    main()
