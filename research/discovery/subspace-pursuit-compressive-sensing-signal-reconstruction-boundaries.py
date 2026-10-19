#!/usr/bin/env python3
"""Boundary and regime verification for Dai & Milenkovic (2009)
Subspace Pursuit (SP) for Compressive Sensing Signal Reconstruction.
"""

import json
import math
import random


def norm(v):
    return math.sqrt(sum(z * z for z in v))


def top_k_indices(v, k):
    return sorted(range(len(v)), key=lambda i: (-abs(v[i]), i))[:k]


def solve_spd(A, b):
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[piv] = M[piv], M[i]
        div = M[i][i]
        for c in range(i, n + 1):
            M[i][c] /= div
        for r in range(n):
            if r != i:
                fac = M[r][i]
                for c in range(i, n + 1):
                    M[r][c] -= fac * M[i][c]
    return [M[i][n] for i in range(n)]


def project_and_resid(Phi, y, I_list):
    m = len(Phi)
    k = len(I_list)
    G = [
        [sum(Phi[i][I_list[a]] * Phi[i][I_list[b]] for i in range(m)) for b in range(k)]
        for a in range(k)
    ]
    rhs = [sum(Phi[i][I_list[a]] * y[i] for i in range(m)) for a in range(k)]
    xp_sub = solve_spd(G, rhs)
    xp = [0.0] * len(Phi[0])
    for idx, val in zip(I_list, xp_sub):
        xp[idx] = val
    yp = [sum(Phi[i][j] * xp[j] for j in I_list) for i in range(m)]
    yr = [y[i] - yp[i] for i in range(m)]
    return xp, yp, yr


def main():
    rng = random.Random(20261019)
    m, N, K = 24, 32, 4

    Phi_raw = [[rng.gauss(0.0, 1.0 / math.sqrt(m)) for _ in range(N)] for _ in range(m)]
    Phi = [[0.0] * N for _ in range(m)]
    for j in range(N):
        cn = math.sqrt(sum(Phi_raw[i][j] ** 2 for i in range(m)))
        for i in range(m):
            Phi[i][j] = Phi_raw[i][j] / cn

    # Zero-one K-sparse signal (Section III-C & IV-A Example 1: challenging for OMP, fast for SP)
    true_supp = [1, 7, 15, 23]
    x_true = [1.0 if j in true_supp else 0.0 for j in range(N)]
    y = [sum(Phi[i][j] * x_true[j] for j in range(N)) for i in range(m)]

    # Initialization (Algorithm 1): T^0 = top K of Phi^* y, y_r^0 = resid(y, Phi_{T^0})
    corr0 = [sum(Phi[i][j] * y[i] for i in range(m)) for j in range(N)]
    T_cur = sorted(top_k_indices(corr0, K))
    _, _, yr = project_and_resid(Phi, y, T_cur)

    # Verify Lemma 2(1): Orthogonality of residue Phi_{T^0}^* y_r^0 == 0
    max_orth_err = max(
        abs(sum(Phi[i][j] * yr[i] for i in range(m))) for j in T_cur
    )
    assert max_orth_err < 1e-14

    # Verify Theorem 5: Initial support intersection T^0 \cap T != empty
    init_overlap = len(set(T_cur) & set(true_supp))
    assert init_overlap >= 1

    res_norms = [norm(yr)]
    for ell in range(1, 10):
        corr = [sum(Phi[i][j] * yr[i] for i in range(m)) for j in range(N)]
        T_tilde = sorted(set(T_cur) | set(top_k_indices(corr, K)))
        xp, _, _ = project_and_resid(Phi, y, T_tilde)
        T_next = sorted(top_k_indices(xp, K))
        x_hat, _, yr_next = project_and_resid(Phi, y, T_next)
        res_norms.append(norm(yr_next))
        T_cur = T_next
        yr = yr_next
        if norm(yr) < 1e-13:
            break

    x_hat, _, _ = project_and_resid(Phi, y, T_cur)
    final_x_err = norm([x_true[j] - x_hat[j] for j in range(N)])
    assert final_x_err < 1e-13
    # Verify monotonic decrease of residual norms ||y_r^ell||_2 < ||y_r^{ell-1}||_2 (Theorem 2 Eq. 7)
    for idx in range(1, len(res_norms)):
        assert res_norms[idx] < res_norms[idx - 1]

    # Verify Theorem 9 (noisy measurement stability)
    e = [0.01 * math.sin(i + 2) for i in range(m)]
    y_noisy = [y[i] + e[i] for i in range(m)]
    corr0_n = [sum(Phi[i][j] * y_noisy[i] for i in range(m)) for j in range(N)]
    Tn = sorted(top_k_indices(corr0_n, K))
    _, _, yrn = project_and_resid(Phi, y_noisy, Tn)
    for _ in range(6):
        corr_n = [sum(Phi[i][j] * yrn[i] for i in range(m)) for j in range(N)]
        T_tilde_n = sorted(set(Tn) | set(top_k_indices(corr_n, K)))
        xpn, _, _ = project_and_resid(Phi, y_noisy, T_tilde_n)
        Tn_next = sorted(top_k_indices(xpn, K))
        _, _, yrn_next = project_and_resid(Phi, y_noisy, Tn_next)
        if norm(yrn_next) > norm(yrn):
            break
        Tn, yrn = Tn_next, yrn_next
    x_hat_n, _, _ = project_and_resid(Phi, y_noisy, Tn)
    noisy_err = norm([x_true[j] - x_hat_n[j] for j in range(N)])
    assert noisy_err < 3.0 * norm(e)

    summary = {
        "concept": "SubspacePursuitForCompressiveSensingSignalReconstruction",
        "init_support_overlap": init_overlap,
        "lemma2_residue_orthogonality_err": max_orth_err,
        "residual_norm_trajectory": [round(r, 6) for r in res_norms],
        "noiseless_final_x_err": final_x_err,
        "noisy_final_x_err": round(noisy_err, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
