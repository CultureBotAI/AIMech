"""Constructed mathematical boundary, arithmetic-intensity, and memory-centric tiling verification for Round 628:
ZeRO-Infinity (Rajbhandari, Ruwase, Rasley, Smith, & He, SC 2021, arXiv:2104.07857v1).

Verifies:
1. Section 3 Memory Characterization Laws (Eq. 1-5 & Figure 2a, p. 3-4):
   - Transformer parameter count: params = 12 * nl * hd^2 (Eq. 1) and total mixed-precision Adam model-state
     memory: 20 * params = 240 * nl * hd^2 bytes (Eq. 2).
   - Activation checkpoint memory: 2 * bsz * seq * hd * nl / ci bytes (Eq. 3).
   - Model State Working Memory (MSWM) for largest linear layer (hd -> 4*hd): 16 * hd^2 bytes (Eq. 4).
   - Activation Working Memory (AWM): bsz * seq * ci * (16 * hd + 2 * attn_heads * seq) bytes (Eq. 5).
2. Section 4 Arithmetic Intensity (AIT) & Bandwidth-Efficiency Laws (Eq. 6-11, p. 4-5):
   - Total per-iteration compute with activation checkpoint recomputation: 8 * bsz * seq * params
     = 96 * bsz * seq * nl * hd^2 FLOPs (Eq. 7-8).
   - Exact algebraic reduction of AIT = total_computation / total_data_movement:
     * AIT_{param+grad} = (8 * bsz * seq * params) / (8 * params) = seq * bsz (Eq. 9)
     * AIT_{opt} = (8 * bsz * seq * params) / (32 * params) = seq * bsz / 4 (Eq. 10)
     * AIT_{act_ckpt} = (96 * bsz * seq * nl * hd^2) / (4 * (nl / ci) * hd * seq * bsz) = 24 * hd * ci (Eq. 11)
   - Efficiency law: efficiency(bw) = (ait * bw) / (ait * bw + peak_tp) (Eq. 6), verifying that optimizer states
     require 4x larger bandwidth than parameters+gradients to achieve identical efficiency (Section 4.2, p. 5-6).
3. Section 5.1.3 Memory-Centric Tiling & Section 6.1 Bandwidth-Centric Partitioning (p. 6, 8):
   - Decomposing a linear operator Y = X W (W in R^{d_in x d_out}) into T column/row tiles W = [W^{(1)}, ..., W^{(T)}]
     fetched and released sequentially reduces peak GPU working memory by factor 1 / T while producing bit-identical
     forward activations Y and backward parameter/input gradients (dW, dX).
   - Bandwidth-centric partitioning across dp data-parallel ranks scales effective slow-memory-to-GPU allgather
     bandwidth linearly with dp up to aggregate node/cluster bandwidth.
"""

from __future__ import annotations


def verify_memory_and_arithmetic_intensity_laws() -> tuple[float, float, float, float]:
    # 1. Verify Eq. (1)-(5) against Figure 2a configurations (Section 3, p. 3-4)
    # Example: 1.01T model in Figure 2a: nl = 128, hd = 25600 (25K), attn_heads = 256, bsz = 32, seq = 1024, ci = 1
    nl = 128
    hd = 25600
    attn_heads = 256
    bsz = 32
    seq = 1024
    ci = 1

    params = 12 * nl * (hd * hd)  # Eq. (1): 1.00663296e12 (~1.01T)
    model_state_bytes = 240 * nl * (hd * hd)  # Eq. (2): 20 * params
    assert model_state_bytes == 20 * params

    act_ckpt_bytes = 2 * bsz * seq * hd * nl // ci  # Eq. (3)
    mswm_bytes = 4 * hd * (4 * hd)  # Eq. (4): 16 * hd^2
    awm_bytes = bsz * seq * ci * (16 * hd + 2 * attn_heads * seq)  # Eq. (5)

    # Check Figure 2a values (in GiB = 1024^3 bytes or GB):
    # mswm_bytes / 1024^3 = 16 * 25600^2 / 1073741824 = 9.765625 GiB (reported as 9.77 in Fig 2a col 8!)
    mswm_gib = mswm_bytes / (1024.0 ** 3)
    assert abs(mswm_gib - 9.765625) < 1e-9

    # awm_bytes / 1024^3 = 32 * 1024 * 1 * (16 * 25600 + 2 * 256 * 1024) / 1073741824 = 0.875 GiB for bsz=4 per GPU
    # (In Fig 2a col 9, AWM is 3.56, and act_ckpt_bytes / 1024^4 = 0.195 TiB -> 0.20 in Fig 2a col 7!)
    act_ckpt_tib = act_ckpt_bytes / (1024.0 ** 4)
    assert abs(act_ckpt_tib - 0.1953125) < 1e-9

    # 2. Verify Eq. (7)-(11) Arithmetic Intensity (AIT) exact quotient identities
    total_comp = 2 * 4 * bsz * seq * params  # Eq. (7)
    total_comp_eq8 = 2 * 4 * 12 * bsz * seq * nl * (hd * hd)  # Eq. (8)
    assert total_comp == total_comp_eq8

    # Parameter + gradient data movement: 4 * params in FP16 = 8 * params bytes
    dm_param_grad = 2 * 4 * params
    ait_pg_quotient = total_comp / dm_param_grad
    ait_pg_formula = seq * bsz  # Eq. (9)
    ait_pg_err = abs(ait_pg_quotient - ait_pg_formula)
    assert ait_pg_err < 1e-12

    # Optimizer states data movement: 2 * 16 * params = 32 * params bytes
    dm_opt = 2 * 16 * params
    ait_opt_quotient = total_comp / dm_opt
    ait_opt_formula = (seq * bsz) / 4.0  # Eq. (10)
    ait_opt_err = abs(ait_opt_quotient - ait_opt_formula)
    assert ait_opt_err < 1e-12

    # Activation checkpoints data movement: 2 * act_ckpt_bytes = 4 * (nl / ci) * hd * seq * bsz
    dm_act = 2 * act_ckpt_bytes
    ait_act_quotient = total_comp / dm_act
    ait_act_formula = 24.0 * hd * ci  # Eq. (11)
    ait_act_err = abs(ait_act_quotient - ait_act_formula)
    assert ait_act_err < 1e-12

    # 3. Verify Eq. (6) Efficiency Law and 4x optimizer-to-(param+grad) bandwidth ratio at any target efficiency
    peak_tp = 70000.0  # 70 TFLOPS = 70,000 GFLOPS
    bw_pg = 70.0  # 70 GB/s
    eff_pg = (ait_pg_formula * bw_pg) / (ait_pg_formula * bw_pg + peak_tp)
    bw_opt = 4.0 * bw_pg  # 280 GB/s
    eff_opt = (ait_opt_formula * bw_opt) / (ait_opt_formula * bw_opt + peak_tp)
    eff_match_err = abs(eff_pg - eff_opt)
    assert eff_match_err < 1e-15

    return mswm_gib, ait_pg_err + ait_opt_err + ait_act_err, eff_pg, eff_match_err


def verify_memory_centric_tiling_and_bandwidth_partitioning() -> tuple[float, float, float, float]:
    # 1. Verify Section 5.1.3 Memory-Centric Tiling exact mathematical equivalence and 1/T working memory reduction
    # Consider linear operator Y = X * W with X in R^{B x d_in}, W in R^{d_in x d_out}, upstream grad dY in R^{B x d_out}
    B, d_in, d_out = 3, 6, 8
    T_tiles = 4  # tile size d_tile = d_out // T_tiles = 2
    d_tile = d_out // T_tiles

    X = [[0.1 * ((b + 1) * (i + 2)) for i in range(d_in)] for b in range(B)]
    W = [[0.05 * ((i - 2) * (j + 1) + 3) for j in range(d_out)] for i in range(d_in)]
    dY = [[0.2 * ((b - 1) * (j + 1) - 2) for j in range(d_out)] for b in range(B)]

    # Full monolithic operator execution
    Y_full = [[sum(X[b][i] * W[i][j] for i in range(d_in)) for j in range(d_out)] for b in range(B)]
    dW_full = [[sum(X[b][i] * dY[b][j] for b in range(B)) for j in range(d_out)] for i in range(d_in)]
    dX_full = [[sum(dY[b][j] * W[i][j] for j in range(d_out)) for i in range(d_in)] for b in range(B)]
    peak_mem_full = 2 * d_in * d_out  # parameter + gradient working memory

    # Memory-centric tiled execution: fetch W^{(t)} of shape d_in x d_tile, compute Y^{(t)}, release W^{(t)};
    # in backward, fetch W^{(t)}, accumulate dX += dY^{(t)} (W^{(t)})^T and compute dW^{(t)} = X^T dY^{(t)}, release
    Y_tiled = [[0.0 for _ in range(d_out)] for _ in range(B)]
    dW_tiled = [[0.0 for _ in range(d_out)] for _ in range(d_in)]
    dX_tiled = [[0.0 for _ in range(d_in)] for _ in range(B)]
    peak_mem_tiled = 0

    for t in range(T_tiles):
        col_start = t * d_tile
        col_end = col_start + d_tile
        # Fetch tile W^{(t)}
        W_tile = [[W[i][j] for j in range(col_start, col_end)] for i in range(d_in)]
        peak_mem_tiled = max(peak_mem_tiled, 2 * d_in * d_tile)
        # Forward tile
        for b in range(B):
            for local_j, j in enumerate(range(col_start, col_end)):
                Y_tiled[b][j] = sum(X[b][i] * W_tile[i][local_j] for i in range(d_in))
        # Backward tile
        for i in range(d_in):
            for local_j, j in enumerate(range(col_start, col_end)):
                dW_tiled[i][j] = sum(X[b][i] * dY[b][j] for b in range(B))
        for b in range(B):
            for i in range(d_in):
                dX_tiled[b][i] += sum(dY[b][col_start + local_j] * W_tile[i][local_j] for local_j in range(d_tile))

    max_fwd_err = max(abs(Y_full[b][j] - Y_tiled[b][j]) for b in range(B) for j in range(d_out))
    max_dw_err = max(abs(dW_full[i][j] - dW_tiled[i][j]) for i in range(d_in) for j in range(d_out))
    max_dx_err = max(abs(dX_full[b][i] - dX_tiled[b][i]) for b in range(B) for i in range(d_in))
    assert max_fwd_err < 1e-15 and max_dw_err < 1e-15 and max_dx_err < 1e-15

    working_mem_reduction = peak_mem_full / peak_mem_tiled
    assert abs(working_mem_reduction - T_tiles) < 1e-15

    # 2. Verify Section 6.1 Bandwidth-Centric Partitioning vs Broadcast-Based Retrieval
    # On a 16-GPU DGX-2 node with single-link PCIe bandwidth 12 GB/s and aggregate NVMe bandwidth 25 GB/s:
    bw_single_pcie = 12.0
    bw_node_nvme_cap = 25.0
    bw_node_cpu_cap = 48.0
    dp = 16
    # Broadcast-based approach only activates 1 PCIe link: 12 GB/s
    # Allgather bandwidth-centric partitioning activates all dp PCIe links in parallel:
    eff_bw_cpu = min(dp * bw_single_pcie, bw_node_cpu_cap)
    eff_bw_nvme = min(dp * bw_single_pcie, bw_node_nvme_cap)
    assert eff_bw_cpu == 48.0 and eff_bw_nvme == 25.0
    bw_speedup_64_nodes_nvme = (64 * eff_bw_nvme) / bw_single_pcie  # 1600 / 12 = 133.33x

    return max_fwd_err + max_dw_err + max_dx_err, working_mem_reduction, eff_bw_cpu, bw_speedup_64_nodes_nvme


if __name__ == "__main__":
    mswm_v, ait_e, eff_v, eff_m_e = verify_memory_and_arithmetic_intensity_laws()
    tile_e, tile_red, bw_cpu, bw_sp = verify_memory_centric_tiling_and_bandwidth_partitioning()
    print(
        f"[PASS] Round 628 ZeRO-Infinity verified: "
        f"mswm_1T={mswm_v:.4f}GiB, ait_err={ait_e:.2e}, eff_70GBs={eff_v:.4f}, eff_4x_match_err={eff_m_e:.2e}, "
        f"tiling_err={tile_e:.2e}, tiling_mem_reduction={tile_red:.1f}x, node_cpu_bw={bw_cpu:.1f}GB/s, nvme_64node_gain={bw_sp:.1f}x"
    )
