#!/usr/bin/env python3
"""Boundary and regime verification for Cai, Candes, & Shen (2010)
A Singular Value Thresholding (SVT) Algorithm for Matrix Completion.
"""

import json
import math


def jacobi_sym_eig_4x4(A, sweeps=25):
    """Exact Jacobi eigendecomposition for 4x4 symmetric matrix."""
    n = len(A)
    D = [row[:] for row in A]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(sweeps):
        for p in range(n):
            for q in range(p + 1, n):
                if abs(D[p][q]) < 1e-15:
                    continue
                tau = (D[q][q] - D[p][p]) / (2.0 * D[p][q])
                t = math.copysign(1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau)), tau)
                c = 1.0 / math.sqrt(1.0 + t * t)
                s = t * c
                app = c * c * D[p][p] - 2.0 * s * c * D[p][q] + s * s * D[q][q]
                aqq = s * s * D[p][p] + 2.0 * s * c * D[p][q] + c * c * D[q][q]
                D[p][q] = D[q][p] = 0.0
                D[p][p], D[q][q] = app, aqq
                for r in range(n):
                    if r != p and r != q:
                        arp = c * D[r][p] - s * D[r][q]
                        arq = s * D[r][p] + c * D[r][q]
                        D[r][p] = D[p][r] = arp
                        D[r][q] = D[q][r] = arq
                for r in range(n):
                    vrp = c * V[r][p] - s * V[r][q]
                    vrq = s * V[r][p] + c * V[r][q]
                    V[r][p], V[r][q] = vrp, vrq
    eigs = [D[i][i] for i in range(n)]
    return eigs, V


def svd_4x4(Y):
    """Compute SVD of 4x4 matrix Y via Jacobi eigendecomposition of Y^T Y."""
    n = 4
    YtY = [
        [sum(Y[k][i] * Y[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]
    eigs, V_cols = jacobi_sym_eig_4x4(YtY)
    order = sorted(range(n), key=lambda idx: eigs[idx], reverse=True)
    sigmas = []
    U_cols = []
    V_ord = []
    for idx in order:
        sig = math.sqrt(max(0.0, eigs[idx]))
        v = [V_cols[r][idx] for r in range(n)]
        if sig > 1e-12:
            u = [sum(Y[r][c] * v[c] for c in range(n)) / sig for r in range(n)]
        else:
            u = [0.0] * n
        sigmas.append(sig)
        U_cols.append(u)
        V_ord.append(v)
    return sigmas, U_cols, V_ord


def shrink_svt(Y, tau):
    n = 4
    sigmas, U_cols, V_cols = svd_4x4(Y)
    X = [[0.0] * n for _ in range(n)]
    nuc = 0.0
    rank_out = 0
    for sig, u, v in zip(sigmas, U_cols, V_cols):
        sh = max(0.0, sig - tau)
        if sh > 0.0:
            rank_out += 1
            nuc += sh
            for i in range(n):
                for j in range(n):
                    X[i][j] += sh * u[i] * v[j]
    return X, nuc, rank_out


def frob_sq(A, B):
    return sum((A[i][j] - B[i][j]) ** 2 for i in range(4) for j in range(4))


def main():
    n = 4
    # 1. Verify Theorem 2.1: D_tau(Y) uniquely minimizes 0.5 ||X - Y||_F^2 + tau ||X||_*
    Y_test = [
        [3.2, 1.1, 0.4, -0.5],
        [1.1, 2.8, -0.3, 0.2],
        [0.4, -0.3, 1.5, 0.6],
        [-0.5, 0.2, 0.6, 0.9],
    ]
    tau = 1.2
    X_hat, nuc_hat, _ = shrink_svt(Y_test, tau)
    obj_hat = 0.5 * frob_sq(X_hat, Y_test) + tau * nuc_hat

    # Perturb X_hat in multiple directions and verify strict optimality
    min_diff = float("inf")
    for di in range(n):
        for dj in range(n):
            X_pert = [row[:] for row in X_hat]
            X_pert[di][dj] += 0.05
            sigs_p, _, _ = svd_4x4(X_pert)
            obj_pert = 0.5 * frob_sq(X_pert, Y_test) + tau * sum(sigs_p)
            min_diff = min(min_diff, obj_pert - obj_hat)
    assert min_diff > 1e-4

    # 2. Verify Theorem 4.2: SVT Uzawa iteration (Eq. 2.7) with 0 < delta < 2 converges to KKT point P_Omega(X - M) = 0
    u_true = [1.0, -1.0, 1.0, -1.0]
    v_true = [1.0, 1.0, -1.0, -1.0]
    M = [[2.0 * u_true[i] * v_true[j] for j in range(n)] for i in range(n)]
    # Observe 12 out of 16 entries
    Omega = {(i, j) for i in range(n) for j in range(n) if (i + j) % 4 != 3}

    Y = [[0.0] * n for _ in range(n)]
    delta = 1.5  # satisfies 0 < delta < 2 in Theorem 4.2
    tau_mc = 4.0
    X = [[0.0] * n for _ in range(n)]
    for _ in range(180):
        X, _, rk = shrink_svt(Y, tau_mc)
        for (i, j) in Omega:
            Y[i][j] += delta * (M[i][j] - X[i][j])

    kkt_feas_err = math.sqrt(sum((X[i][j] - M[i][j]) ** 2 for (i, j) in Omega))
    full_rel_err = math.sqrt(frob_sq(X, M) / frob_sq(M, [[0.0] * n for _ in range(n)]))
    _, _, final_rank = shrink_svt(Y, tau_mc)
    assert kkt_feas_err < 1e-10
    assert final_rank == 1
    assert full_rel_err < 1e-9

    # 3. Verify step-size instability when delta > 2 violates Theorem 4.2
    Y_bad = [[0.0] * n for _ in range(n)]
    for _ in range(25):
        X_bad, _, _ = shrink_svt(Y_bad, tau_mc)
        for (i, j) in Omega:
            Y_bad[i][j] += 3.2 * (M[i][j] - X_bad[i][j])
    bad_feas_err = math.sqrt(sum((X_bad[i][j] - M[i][j]) ** 2 for (i, j) in Omega))
    assert bad_feas_err > 1.0

    summary = {
        "concept": "SingularValueThresholdingAlgorithmForMatrixCompletion",
        "proximal_optimality_min_margin": round(min_diff, 6),
        "svt_kkt_feasibility_err": kkt_feas_err,
        "svt_recovered_rank": final_rank,
        "svt_full_matrix_rel_err": full_rel_err,
        "unstable_delta32_feas_err": round(bad_feas_err, 6),
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
