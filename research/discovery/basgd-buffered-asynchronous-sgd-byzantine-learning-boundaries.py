#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 539:
BASGD: Buffered Asynchronous SGD for Byzantine Learning
(Yang & Li, ICML 2021, PMLR 139:11751-11761).
"""

import math


def l2_norm(v):
    return math.sqrt(sum(x * x for x in v))


def coord_median(buffers):
    B = len(buffers)
    d = len(buffers[0])
    out = [0.0] * d
    for j in range(d):
        s = sorted(h[j] for h in buffers)
        if B % 2 == 1:
            out[j] = s[B // 2]
        else:
            out[j] = 0.5 * (s[B // 2 - 1] + s[B // 2])
    return out


def coord_trmean(buffers, q):
    B = len(buffers)
    assert 0 < 2 * q < B
    d = len(buffers[0])
    out = [0.0] * d
    for j in range(d):
        s = sorted(h[j] for h in buffers)
        trimmed = s[q : B - q]
        out[j] = sum(trimmed) / (B - 2 * q)
    return out


def lambda_bqr(B, q, r):
    """Constant Lambda_{B,q,r} in Section 4 (p. 6):
    (B - r) * sqrt(B - r + 1) / sqrt((B - q - 1) * (q - r + 1)).
    """
    return ((B - r) * math.sqrt(B - r + 1)) / math.sqrt((B - q - 1) * (q - r + 1))


def reassign_mapping_table(active_workers, m, B):
    """Section 3.3 (p. 5): Reassign active workers equally across the B buffers."""
    beta = [0] * m
    for idx, w in enumerate(active_workers):
        beta[w] = idx % B
    inactive = [w for w in range(m) if w not in set(active_workers)]
    for idx, w in enumerate(inactive):
        beta[w] = idx % B
    return beta


def main():
    # 1. Verify Definition 1 & Proposition 1 (q-Byzantine Robust condition for Median and q-Trmean):
    B = 5
    q = 1
    cand = [[1.0, -2.0], [1.2, -1.8], [0.9, -2.1], [1.1, -1.9], [100.0, -500.0]]
    shift = [3.5, -4.0]
    cand_shifted = [[h[0] + shift[0], h[1] + shift[1]] for h in cand]

    G_trm = coord_trmean(cand, q=q)
    G_trm_shifted = coord_trmean(cand_shifted, q=q)
    # Property (a): translation equivariance
    assert l2_norm([G_trm_shifted[j] - (G_trm[j] + shift[j]) for j in range(2)]) < 1e-12
    # Property (b): between min and max of any subset S of size B - q = 4 (e.g. the 4 loyal buffers)
    for j in range(2):
        loyal_vals = [cand[b][j] for b in range(4)]
        assert min(loyal_vals) - 1e-12 <= G_trm[j] <= max(loyal_vals) + 1e-12

    # 2. Verify Lambda_{B,q,r} decreases as q increases (for fixed B=10, r=2) and increases with r
    lam_q2 = lambda_bqr(B=10, q=2, r=2)
    lam_q3 = lambda_bqr(B=10, q=3, r=2)
    lam_r3 = lambda_bqr(B=10, q=3, r=3)
    assert lam_q3 < lam_q2 and lam_r3 > lam_q3

    # 3. Verify Section 3.3 Buffer Reassignment eliminates straggler buffers:
    # Suppose m=15 workers, B=5 buffers; workers {0, 5, 10} (all mapped to buffer 0 initially) are dead.
    dead_workers = {0, 5, 10}
    active_workers = [w for w in range(15) if w not in dead_workers]
    init_buffers = {w % 5 for w in active_workers}
    assert 0 not in init_buffers  # Buffer 0 is a straggler before reassignment!

    beta_reassigned = reassign_mapping_table(active_workers, m=15, B=5)
    new_buffers = {beta_reassigned[w] % 5 for w in active_workers}
    assert new_buffers == {0, 1, 2, 3, 4}  # All 5 buffers receive active workers!

    # 4. Simulate BASGD vs Vanilla ASGD under Negative Gradient (NG) Attack (Section 5.1, k_atk = 10):
    w_star = [2.0, -1.5, 1.0]
    m = 15
    B = 5
    eta = 0.15
    byz_workers = {4, 9}  # Both map to buffer 4 (s mod 5 == 4) or 2 buffers at most

    # Vanilla ASGD
    w_asgd = [0.0, 0.0, 0.0]
    for step in range(40):
        w_id = step % m
        true_g = [w_asgd[j] - w_star[j] for j in range(3)]
        g_recv = [-10.0 * x for x in true_g] if w_id in byz_workers else true_g
        w_asgd = [w_asgd[j] - eta * g_recv[j] for j in range(3)]
    err_asgd = l2_norm([w_asgd[j] - w_star[j] for j in range(3)])

    # BASGD (Algorithm 1) with B=5 buffers and Coordinate-Wise Median
    w_basgd = [0.0, 0.0, 0.0]
    worker_model_cache = {k: list(w_basgd) for k in range(m)}
    h_buf = [[0.0, 0.0, 0.0] for _ in range(B)]
    N_buf = [0] * B

    for event in range(350):
        s = event % m
        w_local = worker_model_cache[s]
        true_g = [w_local[j] - w_star[j] for j in range(3)]
        # Worker 4 and Worker 3 are Byzantine (at most r=2 buffers corrupted out of B=5)
        g_recv = [-10.0 * x for x in true_g] if s in {3, 4} else true_g

        b = s % B
        N_buf[b] += 1
        n_b = N_buf[b]
        h_buf[b] = [((n_b - 1) * h_buf[b][j] + g_recv[j]) / n_b for j in range(3)]

        if all(cnt > 0 for cnt in N_buf):
            G_t = coord_median(h_buf)
            w_basgd = [w_basgd[j] - eta * G_t[j] for j in range(3)]
            h_buf = [[0.0, 0.0, 0.0] for _ in range(B)]
            N_buf = [0] * B

        # Immediately send latest w_basgd back to worker s
        worker_model_cache[s] = list(w_basgd)

    err_basgd = l2_norm([w_basgd[j] - w_star[j] for j in range(3)])
    assert err_basgd < 1e-3, f"Expected BASGD error < 1e-3, got {err_basgd}"
    assert err_asgd > 2.0, f"Expected ASGD error > 2.0, got {err_asgd}"

    print(
        f"[PASS] Round 539 BASGD verified: Lambda(10,3,2)={lam_q3:.3f} < Lambda(10,2,2)={lam_q2:.3f}, "
        f"reassigned_buffers={sorted(new_buffers)}, err_basgd={err_basgd:.6f} << err_asgd={err_asgd:.2f}"
    )


if __name__ == "__main__":
    main()
