#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 632: CSER (Xie et al., NeurIPS 2020)."""

from __future__ import annotations


def block_sparsify(v: list[float], active_blocks: set[int], block_size: int) -> list[float]:
    """Deterministic block sparsifier selecting coordinates in active_blocks."""
    out = [0.0] * len(v)
    for b in active_blocks:
        start = b * block_size
        for j in range(start, start + block_size):
            out[j] = v[j]
    return out


def psync(
    worker_tensors: list[list[float]],
    active_blocks: set[int],
    block_size: int,
) -> tuple[list[list[float]], list[list[float]]]:
    """Algorithm 3 Partial Synchronization (PSync)."""
    n = len(worker_tensors)
    d = len(worker_tensors[0])
    v_primes = [block_sparsify(v, active_blocks, block_size) for v in worker_tensors]
    residuals = [
        [worker_tensors[i][j] - v_primes[i][j] for j in range(d)]
        for i in range(n)
    ]
    v_bar = [
        sum(v_primes[i][j] for i in range(n)) / n
        for j in range(d)
    ]
    synced = [
        [v_bar[j] + residuals[i][j] for j in range(d)]
        for i in range(n)
    ]
    return synced, residuals


def verify_lemma1_bifurcated_model_invariant() -> tuple[float, float]:
    """Verify Lemma 1: x_{i,t} - e_{i,t} == x_{j,t} - e_{j,t} across all workers i, j and steps t,
    and Remark 2: when n = 1, model variance across workers is identically 0.
    """
    n_workers = 4
    d = 8
    block_size = 2
    eta = 0.05
    h_interval = 3

    x0 = [0.5 * ((-1) ** j) * (j + 1) for j in range(d)]
    x_workers = [list(x0) for _ in range(n_workers)]
    e_workers = [[0.0] * d for _ in range(n_workers)]

    max_invariant_err = 0.0
    for t in range(1, 10):
        grads = [
            [0.1 * (t + 1) * (i + 1) * ((-1) ** (i + j)) for j in range(d)]
            for i in range(n_workers)
        ]
        # C_2 selects 1 block out of 4
        c2_blocks = {t % 4}
        g_primes, r_t = psync(grads, c2_blocks, block_size)
        x_half = [
            [x_workers[i][j] - eta * g_primes[i][j] for j in range(d)]
            for i in range(n_workers)
        ]
        e_half = [
            [e_workers[i][j] - eta * r_t[i][j] for j in range(d)]
            for i in range(n_workers)
        ]
        if t % h_interval != 0:
            x_workers = x_half
            e_workers = e_half
        else:
            # Error reset with C_1 selecting 2 blocks out of 4
            c1_blocks = {(t // h_interval) % 4, ((t // h_interval) + 1) % 4}
            e_primes, e_new = psync(e_half, c1_blocks, block_size)
            x_workers = [
                [x_half[i][j] - e_half[i][j] + e_primes[i][j] for j in range(d)]
                for i in range(n_workers)
            ]
            e_workers = e_new

        # Check Lemma 1: x_{i,t} - e_{i,t} == x_{0,t} - e_{0,t} for all i
        ref = [x_workers[0][j] - e_workers[0][j] for j in range(d)]
        for i in range(1, n_workers):
            diff = max(abs((x_workers[i][j] - e_workers[i][j]) - ref[j]) for j in range(d))
            max_invariant_err = max(max_invariant_err, diff)

    assert max_invariant_err < 1e-13, f"Lemma 1 invariant violated: {max_invariant_err}"

    # Verify Remark 2: for n = 1 worker, CSER trajectory is identical to uncompressed SGD!
    x_cser_1 = [list(x0)]
    e_cser_1 = [[0.0] * d]
    x_sgd_1 = list(x0)
    for t in range(1, 7):
        g = [0.15 * t * ((-1) ** j) for j in range(d)]
        x_sgd_1 = [x_sgd_1[j] - eta * g[j] for j in range(d)]
        g_p, r_p = psync([g], {t % 4}, block_size)
        xh = [[x_cser_1[0][j] - eta * g_p[0][j] for j in range(d)]]
        eh = [[e_cser_1[0][j] - eta * r_p[0][j] for j in range(d)]]
        if t % h_interval == 0:
            ep, en = psync(eh, {0, 1}, block_size)
            x_cser_1 = [[xh[0][j] - eh[0][j] + ep[0][j] for j in range(d)]]
            e_cser_1 = en
        else:
            x_cser_1, e_cser_1 = xh, eh

    n1_err = max(abs(x_cser_1[0][j] - x_sgd_1[j]) for j in range(d))
    assert n1_err < 1e-15, f"Remark 2 single-worker equivalence violated: {n1_err}"
    return max_invariant_err, n1_err


def verify_remark1_and_budget_tradeoff() -> tuple[float, float, float, float]:
    """Verify Remark 1 error factor reduction (832 -> 576) and Section 4.2 budget split (400 -> 235.59)."""
    # Remark 1: H = 8, delta1 = 0.5, delta2 = 0
    h = 8.0
    delta1 = 0.5
    qsparse_factor = (4.0 * (1.0 - delta1 ** 2) / (delta1 ** 2) + 1.0) * (h ** 2)
    cser_factor = (4.0 * (1.0 - delta1) / (delta1 ** 2) + 1.0) * (h ** 2)
    assert abs(qsparse_factor - 832.0) < 1e-12
    assert abs(cser_factor - 576.0) < 1e-12

    # Section 4.2 budget trade-off at identical overall compression ratio R_C = 12:
    # Config A: H = 4, delta1 = 1/3 (R_{C1}=3), delta2 = 0 (R_{C2}=inf) -> R_C = 1 / (0 + 1/(3*4)) = 12
    h_a, d1_a, d2_a = 4.0, 1.0 / 3.0, 0.0
    rc_a = 1.0 / (d2_a + d1_a / h_a)
    err_a = (4.0 * (1.0 - d1_a) / (d1_a ** 2) + 1.0) * (1.0 - d2_a) * (h_a ** 2)

    # Config B: H = 12, delta1 = 7/8 (R_{C1}=8/7), delta2 = 1/96 (R_{C2}=96) -> R_C = 1 / (1/96 + (7/8)/12) = 12
    h_b, d1_b, d2_b = 12.0, 7.0 / 8.0, 1.0 / 96.0
    rc_b = 1.0 / (d2_b + d1_b / h_b)
    err_b = (4.0 * (1.0 - d1_b) / (d1_b ** 2) + 1.0) * (1.0 - d2_b) * (h_b ** 2)

    assert abs(rc_a - 12.0) < 1e-12 and abs(rc_b - 12.0) < 1e-12
    assert abs(err_a - 400.0) < 1e-12 and err_b < 236.0
    return qsparse_factor, cser_factor, err_a, err_b


if __name__ == "__main__":
    inv_err, n1_err = verify_lemma1_bifurcated_model_invariant()
    qf, cf, err_a, err_b = verify_remark1_and_budget_tradeoff()
    print(
        f"[PASS] Round 632 CSER verified: inv_err={inv_err:.2e}, n1_err={n1_err:.2e}, "
        f"remark1={qf:.0f}->{cf:.0f}, budget_split_err={err_a:.1f}->{err_b:.2f}"
    )
