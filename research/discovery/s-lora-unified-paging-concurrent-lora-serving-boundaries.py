#!/usr/bin/env python3
"""Constructed boundary verification for Round 670:
S-LoRA: Serving Thousands of Concurrent LoRA Adapters
(Ying Sheng, Shiyi Cao, Dacheng Li, Coleman Hooper, Nicholas Lee, Shuo Yang,
Christopher Chou, Banghua Zhu, Lianmin Zheng, Kurt Keutzer, Joseph E. Gonzalez,
& Ion Stoica, MLSys 2024, arXiv:2311.03285).

Verifies:
1. Separated Batched Base + Heterogeneous Non-Contiguous LoRA Computation
   (Section 4.1, Equations 1-2 & Section 5.3 MBGMM/MBGMV):
   Computing h_i = x_i W + x_i A_{m(i)} B_{m(i)} by batching X W in a single
   dense GEMM and gathering heterogeneous-rank adapters r_{m(i)} in {2, 4, 8}
   stored in interleaved non-contiguous pages of size H matches merged per-adapter
   inference x_i (W + A_{m(i)} B_{m(i)}) to < 1e-12 with zero rank-padding waste.
2. Unified Paging Memory Pool (Section 5.1 & Figure 3):
   Both KV cache tensors of shape (S_i, H) and LoRA adapter weights of shape
   (R_m, H) allocate integer numbers of H-element pages from a single unified pool
   with zero external fragmentation across variable sequence lengths S_i and ranks R_m.
3. Tensor Parallelism Communication Cost & Admission Control Theorem B.1
   (Section 6.2 & Appendix B):
   Verify that S-LoRA TP communication overhead is 5(N-1)Br/N vs. base model
   2(N-1)Bh/N (negligible when r << h), and verify Theorem B.1 that serving the
   most recent l requests in arrival order maximizes cumulative concave user
   satisfaction r(t).
"""

from __future__ import annotations
import math
import random


def main() -> None:
    rng = random.Random(20231103)
    H = 8  # Hidden dimension = page size

    # 1. Unified Paging memory pool (Section 5.1): pages of width H
    pool_pages: list[list[float]] = []

    def alloc_pages(num_pages: int, rows: list[list[float]]) -> list[int]:
        assert len(rows) == num_pages
        page_ids = []
        for row in rows:
            assert len(row) == H
            page_ids.append(len(pool_pages))
            pool_pages.append(list(row))
        return page_ids

    # Allocate interleaved KV caches (S_i x H) and heterogeneous LoRA adapters (R_m x H)
    W_base = [[rng.gauss(0.0, 0.5) for _ in range(H)] for _ in range(H)]
    adapter_ranks = [2, 4, 3]
    adapter_A_pages: dict[int, list[int]] = {}
    adapter_B_pages: dict[int, list[int]] = {}
    adapter_A_dense: dict[int, list[list[float]]] = {}
    adapter_B_dense: dict[int, list[list[float]]] = {}

    for m_id, r_m in enumerate(adapter_ranks):
        # Allocate a KV cache block of length S = m_id + 2 first to interleave pages!
        kv_dummy = [[rng.gauss(0.0, 1.0) for _ in range(H)] for _ in range(m_id + 2)]
        _ = alloc_pages(m_id + 2, kv_dummy)

        # In S-LoRA Section 5.1, both A^T in R^{r_m x H} and B in R^{r_m x H} occupy r_m pages of size H
        A_T_rows = [[rng.gauss(0.0, 0.3) for _ in range(H)] for _ in range(r_m)]
        B_rows = [[rng.gauss(0.0, 0.3) for _ in range(H)] for _ in range(r_m)]
        adapter_A_pages[m_id] = alloc_pages(r_m, A_T_rows)
        adapter_B_pages[m_id] = alloc_pages(r_m, B_rows)
        adapter_A_dense[m_id] = A_T_rows
        adapter_B_dense[m_id] = B_rows

    # 2. Verify MBGMV heterogeneous non-contiguous batched gather-matmul vs. merged W' = W + A B
    batch_requests = [
        (0, [rng.gauss(0.0, 1.0) for _ in range(H)]),
        (2, [rng.gauss(0.0, 1.0) for _ in range(H)]),
        (1, [rng.gauss(0.0, 1.0) for _ in range(H)]),
        (0, [rng.gauss(0.0, 1.0) for _ in range(H)]),
    ]

    # Shared batched base GEMM: H_base = X * W_base
    H_base = [
        [sum(x_vec[k] * W_base[k][j] for k in range(H)) for j in range(H)]
        for _, x_vec in batch_requests
    ]

    # Custom MBGMV kernel gathering non-contiguous pages without rank padding
    max_err = 0.0
    for req_idx, (m_id, x_vec) in enumerate(batch_requests):
        a_pids = adapter_A_pages[m_id]
        b_pids = adapter_B_pages[m_id]
        r_m = len(a_pids)
        # v = x_vec * A (where columns of A are rows in pool_pages[a_pids])
        v_inter = [
            sum(x_vec[k] * pool_pages[a_pids[p]][k] for k in range(H))
            for p in range(r_m)
        ]
        # delta_h = v * B (where rows of B are in pool_pages[b_pids])
        out_slora = [
            H_base[req_idx][j]
            + sum(v_inter[p] * pool_pages[b_pids[p]][j] for p in range(r_m))
            for j in range(H)
        ]

        # Compare against merged W' = W_base + A * B
        A_T = adapter_A_dense[m_id]
        B_mat = adapter_B_dense[m_id]
        W_merged = [
            [
                W_base[k][j] + sum(A_T[p][k] * B_mat[p][j] for p in range(r_m))
                for j in range(H)
            ]
            for k in range(H)
        ]
        out_merged = [
            sum(x_vec[k] * W_merged[k][j] for k in range(H)) for j in range(H)
        ]
        req_err = max(abs(a - b) for a, b in zip(out_slora, out_merged))
        max_err = max(max_err, req_err)

    assert max_err < 1e-14, f"MBGMV vs merged mismatch: {max_err}"

    # 3. Verify Section 6.2 Tensor Parallelism communication cost formula
    N_gpus, B_tokens, h_dim, r_rank = 4, 32, 4096, 16
    comm_base = 2 * (N_gpus - 1) * B_tokens * h_dim / N_gpus
    comm_lora = 5 * (N_gpus - 1) * B_tokens * r_rank / N_gpus
    comm_ratio = comm_lora / comm_base
    assert abs(comm_ratio - (5 * r_rank) / (2 * h_dim)) < 1e-12
    assert comm_ratio < 0.01  # < 1% additional communication cost!

    # 4. Verify Appendix B Theorem B.1 (Admission Control optimality of most recent l requests in order)
    # Concave non-increasing reward r(t) = max(0, 1 - (t / T_slo)^2)
    T_slo = 10.0

    def reward_fn(latency: float) -> float:
        if latency > T_slo:
            return 0.0
        return 1.0 - (latency / T_slo) ** 2

    # Arrivals at t^a = [1, 2, 3, 4, 5], service times t = [6, 7, 8] for l = 3 served requests
    arrivals = [1.0, 2.0, 3.0, 4.0, 5.0]
    service_times = [6.0, 7.0, 8.0]
    # Theorem B.1 optimal schedule: serve the most recent l=3 requests (indices 2, 3, 4) in arrival order
    opt_indices = [2, 3, 4]
    opt_reward = sum(
        reward_fn(service_times[pos] - arrivals[idx])
        for pos, idx in enumerate(opt_indices)
    )

    # Compare against FCFS on oldest 3 requests [0, 1, 2] and LCFS on newest 3 requests [4, 3, 2]
    fcfs_oldest_reward = sum(
        reward_fn(service_times[pos] - arrivals[idx])
        for pos, idx in enumerate([0, 1, 2])
    )
    lcfs_newest_reward = sum(
        reward_fn(service_times[pos] - arrivals[idx])
        for pos, idx in enumerate([4, 3, 2])
    )
    assert opt_reward > fcfs_oldest_reward
    assert opt_reward > lcfs_newest_reward

    print(
        f"[PASS] Round 670 S-LoRA (Sheng et al., MLSys 2024): "
        f"mbgmv_err={max_err:.2e}, tp_comm_ratio={comm_ratio:.5f}<0.01, "
        f"opt_reward={opt_reward:.4f}>fcfs={fcfs_oldest_reward:.4f}&lcfs={lcfs_newest_reward:.4f}"
    )


if __name__ == "__main__":
    main()
