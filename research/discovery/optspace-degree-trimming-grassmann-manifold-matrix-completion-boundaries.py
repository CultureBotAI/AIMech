#!/usr/bin/env python3
"""Boundary and regime verification for Keshavan, Montanari, & Oh (2010)
OptSpace: Degree Trimming, Spectral Projection, and Grassmann Manifold Matrix Completion.
"""

import json
import math
import random


def top_singular_triplet(A, iters=60):
    m, n = len(A), len(A[0])
    v = [1.0 / math.sqrt(n)] * n
    u = [1.0 / math.sqrt(m)] * m
    sigma = 1.0
    for _ in range(iters):
        u_raw = [sum(A[i][j] * v[j] for j in range(n)) for i in range(m)]
        nu = math.sqrt(sum(z * z for z in u_raw))
        if nu < 1e-15:
            return 0.0, u, v
        u = [z / nu for z in u_raw]
        v_raw = [sum(A[i][j] * u[i] for i in range(m)) for j in range(n)]
        sigma = math.sqrt(sum(z * z for z in v_raw))
        if sigma < 1e-15:
            return 0.0, u, v
        v = [z / sigma for z in v_raw]
    return sigma, u, v


def grassmann_metrics_1d(u1, u2):
    """Verify Remark 6.1 (Eq. 24) on G(n, 1) with normalization u^T u = n."""
    n = len(u1)
    cos_theta = min(1.0, max(0.0, abs(sum(a * b for a, b in zip(u1, u2)) / n)))
    theta = math.acos(cos_theta)
    d_geo = theta
    d_chord = 2.0 * math.sin(theta / 2.0)
    d_proj = math.sin(theta)
    return d_geo, d_chord, d_proj


def main():
    # 1. Verify Remark 6.1 (Eq. 24): equivalence of geodesic, chordal, and projection distances on G(n, r)
    n = 16
    u = [1.0 if i % 2 == 0 else -1.0 for i in range(n)]
    x = [1.0 if i < 12 else -1.0 for i in range(n)]
    d_geo, d_chord, d_proj = grassmann_metrics_1d(u, x)
    assert (1.0 / math.pi) * d_geo <= (1.0 / math.sqrt(2.0)) * d_chord + 1e-12
    assert (1.0 / math.sqrt(2.0)) * d_chord <= d_proj + 1e-12
    assert d_proj <= d_chord + 1e-12
    assert d_chord <= d_geo + 1e-12

    # 2. Verify Section 1.2 & Theorem 1.1: Degree Trimming suppresses high-degree hub artifacts
    # Construct rank-1 incoherent matrix M = u v^T in R^{16x16} with |M_{ij}| = 1
    v = [1.0 if (j // 2) % 2 == 0 else -1.0 for j in range(n)]
    M = [[u[i] * v[j] for j in range(n)] for i in range(n)]

    # Reveal a sparse edge set E with an over-represented hub row i = 0 (heavy-tail degree artifact)
    rng = random.Random(20261019)
    E = set()
    # Add all entries in row 0 (degree 16 >> 2|E|/n)
    for j in range(n):
        E.add((0, j))
    # Add uniform random entries elsewhere (~3 per row)
    for i in range(1, n):
        for j in range(n):
            if rng.random() < 0.22:
                E.add((i, j))

    num_E = len(E)
    ME = [[M[i][j] if (i, j) in E else 0.0 for j in range(n)] for i in range(n)]

    # Untrimmed projection T_1(M^E)
    sig_raw, u_raw, v_raw = top_singular_triplet(ME)
    scale = (n * n) / num_E
    rmse_untrimmed = math.sqrt(
        sum(
            (M[i][j] - scale * sig_raw * u_raw[i] * v_raw[j]) ** 2
            for i in range(n)
            for j in range(n)
        )
        / (n * n)
    )

    # Trimmed matrix M_tilde^E: zero out rows/cols with degree > 2|E|/n
    row_deg = [sum(1 for j in range(n) if (i, j) in E) for i in range(n)]
    col_deg = [sum(1 for i in range(n) if (i, j) in E) for j in range(n)]
    deg_thresh = 2.0 * num_E / n
    ME_trim = [
        [
            ME[i][j]
            if (row_deg[i] <= deg_thresh and col_deg[j] <= deg_thresh)
            else 0.0
            for j in range(n)
        ]
        for i in range(n)
    ]
    sig_trim, u_trim, v_trim = top_singular_triplet(ME_trim)
    # Concentration of top left singular vector on hub row 0 before vs after trimming
    hub_weight_untrimmed = abs(u_raw[0])
    hub_weight_trimmed = abs(u_trim[0])
    assert hub_weight_untrimmed > 0.65
    assert hub_weight_trimmed == 0.0
    # Full subspace cosine alignment with true left singular vector u / sqrt(n) improves after trimming
    align_untrimmed = abs(sum(u_raw[i] * (u[i] / math.sqrt(n)) for i in range(n)))
    align_trimmed = abs(sum(u_trim[i] * (u[i] / math.sqrt(n)) for i in range(n)))
    assert align_trimmed > align_untrimmed

    # 3. Verify Section 6 (Theorem 1.2, Lemmas 6.4-6.5): Grassmann manifold cleaning converges to exact M
    # Observe uniform random subset E_clean with ~55% entries
    E_clean = set()
    for i in range(n):
        for j in range(n):
            if rng.random() < 0.60:
                E_clean.add((i, j))
    ME_c = [[M[i][j] if (i, j) in E_clean else 0.0 for j in range(n)] for i in range(n)]
    _, u0, v0 = top_singular_triplet(ME_c)
    # Normalize to X^T X = n, Y^T Y = n
    X = [z * math.sqrt(n) for z in u0]
    Y = [z * math.sqrt(n) for z in v0]

    def eval_F_and_S(Xc, Yc):
        # Minimize 0.5 * sum_{(i,j) in E_clean} (M_{ij} - S X_i Y_j)^2 over scalar S
        num = sum(M[i][j] * Xc[i] * Yc[j] for (i, j) in E_clean)
        den = sum((Xc[i] * Yc[j]) ** 2 for (i, j) in E_clean)
        S = num / den
        F_val = 0.5 * sum((M[i][j] - S * Xc[i] * Yc[j]) ** 2 for (i, j) in E_clean)
        return F_val, S

    F_init, _ = eval_F_and_S(X, Y)
    step = 0.08
    for _ in range(250):
        _, S = eval_F_and_S(X, Y)
        # Euclidean gradients on E_clean
        gX = [0.0] * n
        gY = [0.0] * n
        for (i, j) in E_clean:
            res = X[i] * S * Y[j] - M[i][j]
            gX[i] += res * S * Y[j]
            gY[j] += res * X[i] * S
        # Project onto Grassmann tangent space (Eq. 28-31): W_X^T X = 0, W_Y^T Y = 0
        QX = sum(X[i] * gX[i] for i in range(n)) / n
        QY = sum(Y[j] * gY[j] for j in range(n)) / n
        gradX = [gX[i] - X[i] * QX for i in range(n)]
        gradY = [gY[j] - Y[j] * QY for j in range(n)]
        # Geodesic step (Eq. 25)
        n_gx = math.sqrt(sum(z * z for z in gradX) / n)
        n_gy = math.sqrt(sum(z * z for z in gradY) / n)
        if n_gx > 1e-15:
            L_x = [-z / n_gx for z in gradX]
            th_x = step * n_gx
            X = [X[i] * math.cos(th_x) + L_x[i] * math.sin(th_x) for i in range(n)]
        if n_gy > 1e-15:
            L_y = [-z / n_gy for z in gradY]
            th_y = step * n_gy
            Y = [Y[j] * math.cos(th_y) + L_y[j] * math.sin(th_y) for j in range(n)]

    F_final, S_final = eval_F_and_S(X, Y)
    full_rmse_final = math.sqrt(
        sum((M[i][j] - X[i] * S_final * Y[j]) ** 2 for i in range(n) for j in range(n))
        / (n * n)
    )
    assert F_final < 1e-22
    assert full_rmse_final < 1e-11

    summary = {
        "concept": "OptSpaceDegreeTrimmingSpectralProjectionAndGrassmannManifoldMatrixCompletion",
        "remark_6_1_distances": [round(d_geo, 6), round(d_chord, 6), round(d_proj, 6)],
        "hub_weight_untrimmed": round(hub_weight_untrimmed, 6),
        "hub_weight_trimmed": round(hub_weight_trimmed, 6),
        "nonhub_alignment_untrimmed": round(align_untrimmed, 6),
        "nonhub_alignment_trimmed": round(align_trimmed, 6),
        "grassmann_cleaning_init_loss": round(F_init, 6),
        "grassmann_cleaning_final_rmse": full_rmse_final,
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
