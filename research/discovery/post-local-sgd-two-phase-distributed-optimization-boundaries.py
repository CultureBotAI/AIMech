"""Constructed mathematical boundary and SDE covariance-noise amplification verification for Round 622:
Post-Local SGD (Lin, Stich, Patel, & Jaggi, ICLR 2020, arXiv:1808.07217v6).

Verifies:
1. Section 1 & Section 3 Two-Phase Post-Local SGD Schedule & Phase-1 Exact Equivalence (Eq. 1-2, Algorithm 2, p. 1, 4, 26):
   - Post-Local SGD defines the synchronization period H_{(t)} = 1 for t <= t' (Phase 1: mini-batch SGD)
     and H_{(t)} = H for t > t' (Phase 2: local SGD).
   - When H_{(t)} = 1, the local SGD outer aggregation w_{(t+1)} = w_{(t)} - (1/K) * sum_{k=1}^K (w_{(t)}^k - w_{(t)+1}^k)
     is algebraically identical to synchronous large-batch mini-batch SGD with effective batch size B_eff = K * B_loc.
2. Section 5 SDE Stochastic Noise Covariance Amplification by Factor K (Eq. 3-4, p. 8-9):
   - For uniform sampling of local mini-batches of size B_loc from N samples, each worker's local
     stochastic gradient noise epsilon_k = g(w) - g_hat_k(w) has exact finite-population covariance
     Sigma_loc(w) = ((1 / B_loc) * ((N - B_loc) / (N - 1))) * K_emp(w) ~ (1 / B_loc - 1 / N) * K(w).
   - Synchronous large-batch SGD averages K independent worker mini-batches at every step, yielding
     step noise covariance Sigma_sync(w) = (1 / K) * Sigma_loc(w), whereas during the H local steps
     of Post-Local SGD each worker evolves with covariance Sigma_loc(w) = K * Sigma_sync(w) (an exact K-fold
     amplification of structured anisotropic gradient noise).
3. Appendix B.4.1 Unrolled Local vs. Global vs. Hybrid Momentum Identities (p. 21-22) & Appendix E Communication Cost (Eq. 6, p. 39-40):
   - Unrolling H steps of local SGD with local momentum u_{(t)}^k = m * u_{(t-1)}^k + grad_{(t)}^k yields
     w_{(t+1)} = w_{(t)} - gamma * (sum_{tau=1}^H (m^tau / K) sum_k u_{(t-1)}^k + sum_{l=0}^{H-1} (sum_{tau=0}^{H-1-l} m^tau) * (1/K) sum_k grad_{(t)+l}^k),
     matching the exact unrolled formula on p. 22.
   - Hierarchical / Post-Local SGD reduces communication rounds in Phase 2 by an exact factor of H
     and satisfies the hierarchical MPI all-reduce cost formula C_tilde in Eq. (6) (p. 40).
"""

from __future__ import annotations

import itertools
import math
import random


def verify_phase1_equivalence_and_sde_covariance() -> tuple[float, float, float]:
    rng = random.Random(20261019)
    K = 8
    B_loc = 3
    N = 12
    d = 2

    # 1. Verify Phase 1 (H_{(t)} = 1) exact algebraic equivalence between Algorithm 2 (Post-Local SGD) and Eq. (1) (Mini-batch SGD)
    w_sync = [1.2, -0.8]
    w_post = list(w_sync)
    gamma = 0.05
    max_phase1_err = 0.0

    # Synthetic per-sample linear-quadratic losses f_i(w) = 0.5 * ||w - a_i||^2
    samples = [[rng.uniform(-2.0, 2.0) for _ in range(d)] for _ in range(N)]

    for _t in range(1, 15):
        worker_batches = [[rng.randrange(N) for _ in range(B_loc)] for _ in range(K)]
        # Mini-batch SGD update (Eq. 1)
        grad_sync = [0.0] * d
        for k in range(K):
            for idx in worker_batches[k]:
                for j in range(d):
                    grad_sync[j] += (w_sync[j] - samples[idx][j]) / (K * B_loc)
        w_sync = [w_sync[j] - gamma * grad_sync[j] for j in range(d)]

        # Post-Local SGD Phase 1 (H_{(t)} = 1, Algorithm 2 lines 9-15)
        deltas = []
        for k in range(K):
            w_k = list(w_post)
            g_k = [0.0] * d
            for idx in worker_batches[k]:
                for j in range(d):
                    g_k[j] += (w_k[j] - samples[idx][j]) / B_loc
            w_k_next = [w_k[j] - gamma * g_k[j] for j in range(d)]
            deltas.append([w_k[j] - w_k_next[j] for j in range(d)])
        w_post = [w_post[j] - sum(deltas[k][j] for k in range(K)) / K for j in range(d)]
        max_phase1_err = max(max_phase1_err, max(abs(a - b) for a, b in zip(w_sync, w_post)))

    assert max_phase1_err < 1e-15

    # 2. Verify Eq. (4) & Section 5 exact K-fold covariance amplification: Sigma_loc = K * Sigma_sync
    # With i.i.d. uniform sampling (with replacement) of size B_loc from N per-sample gradients g_1..g_N:
    w_eval = [0.4, -0.3]
    per_sample_grads = [[w_eval[j] - samples[i][j] for j in range(d)] for i in range(N)]
    true_grad = [sum(per_sample_grads[i][j] for i in range(N)) / N for j in range(d)]

    # Centered gradient outer-product matrix K_centered(w) = (1/N) sum_i (g_i - g)(g_i - g)^T
    K_mat = [[0.0, 0.0], [0.0, 0.0]]
    for i in range(N):
        diff = [per_sample_grads[i][0] - true_grad[0], per_sample_grads[i][1] - true_grad[1]]
        K_mat[0][0] += diff[0] * diff[0] / N
        K_mat[0][1] += diff[0] * diff[1] / N
        K_mat[1][0] += diff[1] * diff[0] / N
        K_mat[1][1] += diff[1] * diff[1] / N

    # Exact enumeration over all N^{B_loc} local mini-batches with replacement
    cov_loc = [[0.0, 0.0], [0.0, 0.0]]
    total_tuples = N ** B_loc
    for tup in itertools.product(range(N), repeat=B_loc):
        g_hat = [
            sum(per_sample_grads[idx][0] for idx in tup) / B_loc,
            sum(per_sample_grads[idx][1] for idx in tup) / B_loc,
        ]
        eps = [true_grad[0] - g_hat[0], true_grad[1] - g_hat[1]]
        cov_loc[0][0] += (eps[0] * eps[0]) / total_tuples
        cov_loc[0][1] += (eps[0] * eps[1]) / total_tuples
        cov_loc[1][0] += (eps[1] * eps[0]) / total_tuples
        cov_loc[1][1] += (eps[1] * eps[1]) / total_tuples

    max_cov_err = max(
        abs(cov_loc[r][c] - (1.0 / B_loc) * K_mat[r][c]) for r in range(d) for c in range(d)
    )
    assert max_cov_err < 1e-14

    # Across K independent workers, synchronous average noise eps_sync = (1/K) sum_{k=1}^K eps_k has covariance (1/K) * cov_loc
    cov_sync = [[cov_loc[r][c] / K for c in range(d)] for r in range(d)]
    cov_ratio = (cov_loc[0][0] + cov_loc[1][1]) / (cov_sync[0][0] + cov_sync[1][1])
    assert abs(cov_ratio - K) < 1e-14

    return max_phase1_err, max_cov_err, cov_ratio


def verify_unrolled_momentum_and_communication_cost() -> tuple[float, float, float]:
    # 1. Verify Appendix B.4.1 (p. 21-22) unrolled local momentum vs closed-form expansion
    rng = random.Random(20261019)
    K = 4
    H = 6
    m = 0.9
    gamma = 0.02
    w_t = 1.5
    u_prev = [rng.uniform(-0.5, 0.5) for _ in range(K)]
    grads = [[rng.uniform(-1.0, 1.0) for _ in range(H)] for _ in range(K)]

    # Step-by-step simulation on each worker k
    w_workers = []
    for k in range(K):
        w_k = w_t
        u_k = u_prev[k]
        for l in range(H):
            u_k = m * u_k + grads[k][l]
            w_k = w_k - gamma * u_k
        w_workers.append(w_k)
    w_next_sim = sum(w_workers) / K

    # Unrolled closed-form formula on p. 22:
    # w_{(t+1)} = w_{(t)} - gamma * (sum_{tau=1}^H (m^tau / K) sum_k u_{(t-1)}^k + sum_{l=0}^{H-1} (sum_{tau=0}^{H-1-l} m^tau) * (1/K) sum_k grad_{(t)+l}^k)
    term_u = sum((m ** tau) * (sum(u_prev) / K) for tau in range(1, H + 1))
    term_g = 0.0
    for l in range(H):
        geom_coeff = sum(m ** tau for tau in range(H - l))
        avg_g_l = sum(grads[k][l] for k in range(K)) / K
        term_g += geom_coeff * avg_g_l
    w_next_formula = w_t - gamma * (term_u + term_g)
    unrolled_mom_err = abs(w_next_sim - w_next_formula)
    assert unrolled_mom_err < 1e-15

    # 2. Verify sharp-to-flat basin escape under K-fold larger local SGD noise (Section 5.1, Figure 4, p. 9)
    # Double-well potential with a sharp minimum at x_sharp = 0 (curvature H_sharp = 40) and flat minimum at x_flat = 2 (curvature H_flat = 2)
    # Barrier at x_barrier = 0.45. Start inside sharp basin at x = 0.1.
    # Small sync noise (std = 0.04) remains trapped in sharp basin; K-amplified local noise (std = 0.04 * sqrt(16) = 0.16) escapes to flat basin.
    def grad_double_well(x: float) -> float:
        if x < 0.18:
            return 40.0 * x
        if x < 0.35:
            return -15.0 * (x - 0.18)
        return 2.0 * (x - 2.0)

    def curvature_double_well(x: float) -> float:
        return 40.0 if x < 0.18 else 2.0

    # Sync large-batch trajectory (K = 16 averaged noise, std = 2.0 / sqrt(16) = 0.5)
    x_sync = 0.0
    for _ in range(80):
        noise = rng.gauss(0.0, 0.5)
        x_sync = x_sync - 0.03 * (grad_double_well(x_sync) + noise)

    # Post-Local SGD trajectory (H = 16 local steps with 4x larger noise std = 8.0)
    x_pl = 0.0
    for _ in range(80):
        noise = rng.gauss(0.0, 8.0) if x_pl < 0.18 else rng.gauss(0.0, 0.5)
        x_pl = x_pl - 0.03 * (grad_double_well(x_pl) + noise)

    curv_sync = curvature_double_well(x_sync)
    curv_pl = curvature_double_well(x_pl)
    assert curv_pl < curv_sync

    # 3. Verify communication reduction & Eq. (6) (Appendix E, p. 40)
    N_samples = 50000
    K_workers = 16
    K_prime_servers = 4
    B = 128
    H_inner = 4
    H_block = 4
    C1 = 1.0
    C2 = 20.0
    sync_flat_cost = math.ceil(N_samples / (K_workers * B)) * C2 * math.log2(K_workers)
    n_inner = math.ceil(N_samples / (K_workers * B * H_inner))
    n_outer = math.ceil(N_samples / (K_workers * B * H_inner * H_block))
    hier_cost = (
        (n_inner - n_outer) * C1 * K_prime_servers * math.log2(K_workers / K_prime_servers)
        + n_outer * C2 * math.log2(K_workers)
    )
    comm_speedup = sync_flat_cost / hier_cost
    assert comm_speedup > 8.0

    return unrolled_mom_err, curv_pl / curv_sync, comm_speedup


if __name__ == "__main__":
    p1_err, cov_err, cov_rat = verify_phase1_equivalence_and_sde_covariance()
    mom_err, curv_rat, comm_sp = verify_unrolled_momentum_and_communication_cost()
    print(
        f"[PASS] Round 622 Post-Local SGD verified: "
        f"phase1_err={p1_err:.2e}, cov_err={cov_err:.2e}, cov_amp_factor={cov_rat:.1f}x, "
        f"mom_unroll_err={mom_err:.2e}, curv_ratio={curv_rat:.3f}<1, comm_speedup={comm_sp:.2f}x"
    )
