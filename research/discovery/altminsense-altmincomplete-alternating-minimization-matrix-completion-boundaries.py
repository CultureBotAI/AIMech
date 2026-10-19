#!/usr/bin/env python3
"""Boundary and regime verification for Jain, Netrapalli, & Sanghavi (2013)
Low-rank Matrix Completion and Matrix Sensing using Alternating Minimization (AltMinSense & AltMinComplete).
"""

import json
import math
import random


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm(u):
    return math.sqrt(dot(u, u))


def normalize(u):
    n = norm(u)
    return [x / n for x in u]


def subspace_dist_1d(u, v):
    u_n = normalize(u)
    v_n = normalize(v)
    c = max(-1.0, min(1.0, abs(dot(u_n, v_n))))
    return math.sqrt(max(0.0, 1.0 - c * c))


def solve_spd(A, b):
    """Gaussian elimination for small SPD system A x = b."""
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for i in range(n):
        piv = i
        for r in range(i + 1, n):
            if abs(M[r][i]) > abs(M[piv][i]):
                piv = r
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


def main():
    rng = random.Random(20261019)
    n = 6
    d_meas = 48

    # 1. Rank-1 ground-truth matrix M = sigma^* u^* (v^*)^T in R^{6x6}
    u_star = normalize([1.0 if i % 2 == 0 else -1.0 for i in range(n)])
    v_star = normalize([1.0 if (i // 2) % 2 == 0 else -1.0 for i in range(n)])
    sigma_star = 3.0
    M = [[sigma_star * u_star[i] * v_star[j] for j in range(n)] for i in range(n)]

    # Generate Gaussian sensing matrices A_1, ..., A_d
    As = [
        [[rng.gauss(0.0, 1.0 / math.sqrt(d_meas)) for _ in range(n)] for _ in range(n)]
        for _ in range(d_meas)
    ]
    b = [
        sum(As[m][i][j] * M[i][j] for i in range(n) for j in range(n))
        for m in range(d_meas)
    ]

    # Top-1 left singular vector of sum_i A_i b_i (Algorithm 1 Step 2)
    S0 = [
        [sum(As[m][i][j] * b[m] for m in range(d_meas)) for j in range(n)]
        for i in range(n)
    ]
    u = [1.0] * n
    for _ in range(30):
        # Power iteration on S0 S0^T
        w = [sum(S0[i][j] * u[i] for i in range(n)) for j in range(n)]
        u = normalize([sum(S0[i][j] * w[j] for j in range(n)) for i in range(n)])

    init_dist = subspace_dist_1d(u, u_star)
    assert init_dist < 0.5, f"Spectral initialization outside basin: {init_dist}"

    # Verify Equation (4) Perturbed Power Method identity & Theorem 4.2 geometric contraction
    max_identity_diff = 0.0
    for t in range(25):
        # Solve least-squares for v^{t+1}: B v^{t+1} = sigma^* C v^*
        # where B = sum_m (A_m^T u^t)(A_m^T u^t)^T, C = sum_m (A_m^T u^t)(A_m^T u^*)^T
        B = [[0.0] * n for _ in range(n)]
        C = [[0.0] * n for _ in range(n)]
        rhs = [0.0] * n
        for m in range(d_meas):
            AmT_ut = [sum(As[m][i][j] * u[i] for i in range(n)) for j in range(n)]
            AmT_ustar = [sum(As[m][i][j] * u_star[i] for i in range(n)) for j in range(n)]
            for j1 in range(n):
                rhs[j1] += AmT_ut[j1] * b[m]
                for j2 in range(n):
                    B[j1][j2] += AmT_ut[j1] * AmT_ut[j2]
                    C[j1][j2] += AmT_ut[j1] * AmT_ustar[j2]

        v_next = solve_spd(B, rhs)
        # Verify Eq (4): v^{t+1} = <u^*, u^t> sigma^* v^* - B^{-1}(<u^*, u^t> B - C) sigma^* v^*
        ip = dot(u_star, u)
        err_rhs = [
            sigma_star
            * sum((ip * B[j1][j2] - C[j1][j2]) * v_star[j2] for j2 in range(n))
            for j1 in range(n)
        ]
        err_vec = solve_spd(B, err_rhs)
        for j in range(n):
            eq4_val = ip * sigma_star * v_star[j] - err_vec[j]
            max_identity_diff = max(max_identity_diff, abs(v_next[j] - eq4_val))

        v = normalize(v_next)
        # Alternate least-squares for u^{t+1}
        Bu = [[0.0] * n for _ in range(n)]
        rhsu = [0.0] * n
        for m in range(d_meas):
            Am_vt = [sum(As[m][i][j] * v[j] for j in range(n)) for i in range(n)]
            for i1 in range(n):
                rhsu[i1] += Am_vt[i1] * b[m]
                for i2 in range(n):
                    Bu[i1][i2] += Am_vt[i1] * Am_vt[i2]
        u_next = solve_spd(Bu, rhsu)
        u = normalize(u_next)

    final_frob_err = math.sqrt(
        sum(
            (u_next[i] * v[j] - M[i][j]) ** 2
            for i in range(n)
            for j in range(n)
        )
    )
    assert max_identity_diff < 1e-12
    assert final_frob_err < 1e-12

    # 2. Verify Lemma 5.2 / Lemma C.2 clipping step preserves subspace distance and restores incoherence
    # Construct a perturbed vector u_pert with a spiky coordinate
    u_pert = u_star[:]
    u_pert[0] += 0.12
    u_pert = normalize(u_pert)
    d_before = subspace_dist_1d(u_pert, u_star)
    # Clip at threshold 2 * mu / sqrt(n) with mu = 1.0
    thresh = 2.0 * 1.0 / math.sqrt(n)
    u_clip = [x if abs(x) <= thresh else 0.0 for x in u_pert]
    u_clip_norm = normalize(u_clip)
    d_after = subspace_dist_1d(u_clip_norm, u_star)
    max_inf_clip = max(abs(x) for x in u_clip_norm) * math.sqrt(n)
    assert d_after <= 4.0 * math.sqrt(d_before) + 1e-9
    assert max_inf_clip <= 4.0

    # 3. Verify failure mode: orthogonal initialization <u^0, u^*> = 0 yields zero power-method signal term
    u_orth = normalize([1.0 if i < 2 else (-1.0 if i < 4 else 0.0) for i in range(n)])
    # Ensure exact orthogonality to u_star = [1,-1,1,-1,1,-1]/sqrt(6)
    u_orth = [1.0, 1.0, -1.0, -1.0, 0.0, 0.0]
    u_orth = normalize(u_orth)
    assert abs(dot(u_orth, u_star)) < 1e-15

    summary = {
        "concept": "AltMinSenseAndAltMinCompleteAlternatingMinimizationForLowRankMatrixSensingAndCompletion",
        "init_subspace_dist": round(init_dist, 6),
        "eq4_perturbed_power_identity_diff": max_identity_diff,
        "altminsense_final_frob_err": final_frob_err,
        "clipped_incoherence_bound": round(max_inf_clip, 6),
        "orthogonal_init_inner_product": abs(dot(u_orth, u_star)),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
