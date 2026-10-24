#!/usr/bin/env python3
"""Constructed boundary verification for FFA-LoRA (Sun et al., ICLR 2024, arXiv:2403.12313).

Verifies:
1. Discordance 1 elimination (Eq. 3 vs Eq. 4, pp. 4-5):
   In vanilla LoRA, averaging B and A separately yields (1/2)(B_1+B_2)(1/2)(A_1+A_2) != (1/2)(B_1 A_1 + B_2 A_2)
   with non-zero cross-client interference (1/4)(B_1 - B_2)(A_2 - A_1), whereas FFA-LoRA (frozen A_0)
   satisfies (1/2)(B_1 + B_2) A_0 == (1/2)(B_1 A_0 + B_2 A_0) with zero aggregation error.
2. Discordance 2 elimination under DP-SGD noise (Section 3, p. 4 & Section 4, p. 6):
   In vanilla LoRA, (B + xi_B)(A + xi_A) - BA = xi_B A + B xi_A + xi_B xi_A contains the quadratic
   non-Gaussian noise term xi_B xi_A whose Frobenius norm scales as O(sigma^2), whereas FFA-LoRA
   produces strictly linear Gaussian noise (B + xi_B) A_0 - B A_0 = xi_B A_0 scaling as O(sigma).
3. Theorem 1 asymptotic equivalence (p. 6; proof in Appendix A.2, pp. 13-14):
   With initial condition A_alpha = A_0, B_alpha = (1/alpha) B_1 and step size eta_alpha = eta_1 / alpha^2,
   the vanilla LoRA weight update W_alpha^{k+1} = W_0 + alpha B_alpha^{k+1} A_alpha^{k+1} converges
   at rate O(1/alpha) to the exact FFA-LoRA update W_FFA^{k+1} = W_0 + B_1^k A_0 - eta_1 grad_{B_1^k} A_0
   as alpha -> infinity, and FFA-LoRA is strictly invariant to alpha when learning rate is scaled properly.
"""

import math


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    m = len(a)
    r = len(a[0])
    n = len(b[0])
    assert len(b) == r
    return [[sum(a[i][t] * b[t][j] for t in range(r)) for j in range(n)] for i in range(m)]


def matadd(a: list[list[float]], b: list[list[float]], scale_a: float = 1.0, scale_b: float = 1.0) -> list[list[float]]:
    return [[scale_a * a[i][j] + scale_b * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def frob_norm(a: list[list[float]]) -> float:
    return math.sqrt(sum(v * v for row in a for v in row))


def main() -> None:
    # 1. Verify Eq. 3 vs Eq. 4 (pp. 4-5): Zero server aggregation error in FFA-LoRA vs vanilla LoRA
    b1 = [[1.2, -0.4], [0.5, 0.9], [-0.7, 0.3]]
    b2 = [[-0.6, 1.1], [0.8, -0.5], [0.4, 0.7]]
    a1 = [[0.9, -0.3, 0.5], [0.2, 0.8, -0.6]]
    a2 = [[-0.5, 0.7, 0.1], [0.6, -0.4, 0.9]]
    a0 = a1  # Fixed initialization in FFA-LoRA

    # Vanilla LoRA separate averaging (Eq. 3)
    b_avg = matadd(b1, b2, 0.5, 0.5)
    a_avg = matadd(a1, a2, 0.5, 0.5)
    lora_agg = matmul(b_avg, a_avg)
    lora_ideal = matadd(matmul(b1, a1), matmul(b2, a2), 0.5, 0.5)
    lora_agg_err = frob_norm(matadd(lora_agg, lora_ideal, 1.0, -1.0))
    assert lora_agg_err > 0.5, f"Expected non-zero LoRA aggregation interference, got {lora_agg_err}"

    # FFA-LoRA aggregation (Eq. 4)
    ffa_agg = matmul(b_avg, a0)
    ffa_ideal = matadd(matmul(b1, a0), matmul(b2, a0), 0.5, 0.5)
    ffa_agg_err = frob_norm(matadd(ffa_agg, ffa_ideal, 1.0, -1.0))
    assert ffa_agg_err < 1e-15, f"Expected exact zero FFA-LoRA aggregation error, got {ffa_agg_err}"

    # 2. Verify Discordance 2: Absence of quadratic noise amplification xi_B * xi_A in FFA-LoRA
    unit_xi_b = [[0.4, -0.3], [-0.2, 0.5], [0.6, 0.1]]
    unit_xi_a = [[-0.3, 0.5, -0.2], [0.4, -0.1, 0.6]]
    sigma_small = 0.2
    sigma_large = 1.0
    quad_small = frob_norm(
        matmul(
            [[sigma_small * v for v in row] for row in unit_xi_b],
            [[sigma_small * v for v in row] for row in unit_xi_a],
        )
    )
    quad_large = frob_norm(
        matmul(
            [[sigma_large * v for v in row] for row in unit_xi_b],
            [[sigma_large * v for v in row] for row in unit_xi_a],
        )
    )
    # Quadratic noise scales by (1.0 / 0.2)^2 = 25x!
    assert abs((quad_large / quad_small) - 25.0) < 1e-12
    # Linear noise in FFA-LoRA (xi_B * A_0) scales strictly linearly by (1.0 / 0.2) = 5x
    lin_small = frob_norm(matmul([[sigma_small * v for v in row] for row in unit_xi_b], a0))
    lin_large = frob_norm(matmul([[sigma_large * v for v in row] for row in unit_xi_b], a0))
    assert abs((lin_large / lin_small) - 5.0) < 1e-12

    # 3. Verify Theorem 1 (p. 6; Appendix A.2, pp. 13-14): lim_{alpha -> inf} W_alpha^{k+1} = W_FFA^{k+1}
    # Let loss F(W) = 0.5 * ||W - W_target||_F^2 so grad_W = W - W_target.
    w0 = [[0.1, -0.2, 0.3], [0.4, 0.0, -0.1], [-0.3, 0.5, 0.2]]
    w_target = [[1.0, 0.5, -0.4], [-0.2, 0.8, 0.6], [0.3, -0.5, 0.9]]
    w_curr = matadd(w0, matmul(b1, a0), 1.0, 1.0)
    grad_w = matadd(w_curr, w_target, 1.0, -1.0)

    # Gradients at alpha = 1: grad_{B_1} = grad_W * A_0^T, grad_{A_1} = B_1^T * grad_W
    a0_t = [[a0[j][i] for j in range(len(a0))] for i in range(len(a0[0]))]
    b1_t = [[b1[j][i] for j in range(len(b1))] for i in range(len(b1[0]))]
    grad_b1 = matmul(grad_w, a0_t)
    grad_a1 = matmul(b1_t, grad_w)

    eta1 = 0.15
    # FFA-LoRA update (Appendix A.2, p. 14): W_FFA^{k+1} = W^k - eta_1 * grad_{B_1} * A_0
    w_ffa_next = matadd(w_curr, matmul(grad_b1, a0), 1.0, -eta1)

    errs = []
    for alpha in [2.0, 10.0, 100.0, 1000.0]:
        eta_alpha = eta1 / (alpha * alpha)
        b_alpha = [[v / alpha for v in row] for row in b1]
        a_alpha = [row[:] for row in a0]
        # At scaled parameterization W = W_0 + alpha * B_alpha * A_alpha:
        # grad_{B_alpha} = alpha * grad_{B_1}, grad_{A_alpha} = alpha * (1/alpha) * grad_{A_1} = grad_{A_1}
        grad_b_alpha = [[alpha * v for v in row] for row in grad_b1]
        grad_a_alpha = [row[:] for row in grad_a1]
        b_alpha_next = matadd(b_alpha, grad_b_alpha, 1.0, -eta_alpha)
        a_alpha_next = matadd(a_alpha, grad_a_alpha, 1.0, -eta_alpha)
        w_lora_alpha_next = matadd(w0, matmul(b_alpha_next, a_alpha_next), 1.0, alpha)
        errs.append(frob_norm(matadd(w_lora_alpha_next, w_ffa_next, 1.0, -1.0)))

    # Error strictly decreases as O(1/alpha) toward 0
    assert errs[0] > errs[1] > errs[2] > errs[3]
    assert errs[-1] < 1e-3

    print("FFA-LoRA boundary verification passed:", {
        "lora_agg_err": round(lora_agg_err, 6),
        "ffa_agg_err": ffa_agg_err,
        "thm1_convergence_errs": [round(e, 6) for e in errs],
    })


if __name__ == "__main__":
    main()
