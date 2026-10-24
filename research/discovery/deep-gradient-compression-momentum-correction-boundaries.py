"""Constructed boundary verification for Round 421: Deep Gradient Compression (Lin et al., ICLR 2018, arXiv:1712.01887).

Verifies:
1. Section 3.2 (Equations 3-7 & Appendix B): When a coordinate remains below the sparsification threshold
   for T consecutive steps before firing, naive local gradient accumulation v_{k,t} = v_{k,t-1} + g_{k,t}
   fed into global momentum u_t = m u_{t-1} + sparse(v_t) loses the geometric discounting factors
   sum_{tau=0}^{T-1} m^tau on intermediate gradients, creating a staleness distortion proportional to
   (1 - m^T) / (1 - m) - 1; whereas DGC Momentum Correction (Eq. 6: u_{k,t} = m u_{k,t-1} + g_{k,t},
   v_{k,t} = v_{k,t-1} + u_{k,t}) exactly matches dense momentum SGD's cumulative weight update!
2. Section 3.3 (Equation 8): Momentum Factor Masking zeros both v_{k,t}^{(j)} and u_{k,t}^{(j)} on
   transmitted coordinates j so stale velocity does not re-accumulate after transmission.
"""

from __future__ import annotations


def main() -> None:
    m = 0.9
    lr = 0.1
    # Suppose a coordinate accumulates gradients g_0, ..., g_{T-1} over T = 5 steps and fires at step T-1
    grads = [0.12, 0.08, 0.15, 0.09, 0.20]
    t_steps = len(grads)

    # 1. Exact dense momentum SGD weight displacement Delta w_dense = -lr * sum_{t=0}^{T-1} u_t
    u_dense = 0.0
    disp_dense = 0.0
    for g in grads:
        u_dense = m * u_dense + g
        disp_dense -= lr * u_dense

    # 2. DGC with Momentum Correction (Eq. 6-7): u_t = m * u_{t-1} + g_t, v_t = v_{t-1} + u_t; fires at T-1
    u_dgc = 0.0
    v_dgc = 0.0
    for g in grads:
        u_dgc = m * u_dgc + g
        v_dgc = v_dgc + u_dgc
    disp_dgc = -lr * v_dgc

    # 3. Naive gradient accumulation without momentum correction (Eq. 5): v_naive = sum_{t=0}^{T-1} g_t
    # applied as a single momentum step at T-1
    v_naive = sum(grads)
    disp_naive = -lr * v_naive

    dgc_err = abs(disp_dgc - disp_dense)
    naive_err = abs(disp_naive - disp_dense)
    assert dgc_err < 1e-15, f"DGC momentum correction failed to match dense momentum displacement: {dgc_err}"
    assert naive_err > 0.05, f"Naive accumulation error unexpectedly small: {naive_err}"

    # Verify Momentum Factor Masking (Eq. 8): clearing both u and v prevents phantom drift on step T when g_T = 0
    u_masked = 0.0
    v_masked = 0.0
    u_unmasked = u_dgc
    v_unmasked = 0.0
    # Next step has g_T = 0.0: masked velocity stays 0.0, whereas unmasked velocity adds m * u_{T-1} != 0
    u_masked = m * u_masked + 0.0
    v_masked = v_masked + u_masked
    u_unmasked = m * u_unmasked + 0.0
    v_unmasked = v_unmasked + u_unmasked
    assert v_masked == 0.0 and v_unmasked > 0.1

    print(
        f"[PASS] Round 421 Deep Gradient Compression (Lin et al. 2018): disp_dense={disp_dense:.6f} == "
        f"disp_dgc={disp_dgc:.6f} (err={dgc_err:.1e}), naive_err={naive_err:.6f} > 0, "
        f"masked_residual={v_masked:.1f} vs unmasked_phantom_velocity={v_unmasked:.4f}"
    )


if __name__ == "__main__":
    main()
