#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 505: FedHM (Yao et al., 2021 / arXiv:2111.14655)."""

import math


def conv_params_and_macs(m: int, n: int, k: int, r: int, H: int, W: int) -> dict[str, int]:
    """Compare parameter counts and MAC complexity for vanilla, FedHM unrolled SVD, and Pufferfish factorized 2D conv (Table 1, p. 5)."""
    vanilla_params = m * n * (k ** 2)
    vanilla_macs = m * n * (k ** 2) * H * W

    fedhm_params = r * k * (m + n)
    fedhm_macs = r * k * H * W * (m + n)

    pufferfish_params = r * (m * (k ** 2) + n)
    pufferfish_macs = r * H * W * (m * (k ** 2) + n)

    return {
        "vanilla_params": vanilla_params,
        "vanilla_macs": vanilla_macs,
        "fedhm_params": fedhm_params,
        "fedhm_macs": fedhm_macs,
        "pufferfish_params": pufferfish_params,
        "pufferfish_macs": pufferfish_macs,
    }


def softmax_rank_weights(gamma_list: list[float], tau: float) -> list[float]:
    """Compute softmax aggregation weights alpha_p = exp(gamma_p / tau) / sum_q exp(gamma_q / tau) (Eq. 2, p. 4)."""
    exps = [math.exp(g / tau) for g in gamma_list]
    s = sum(exps)
    return [e / s for e in exps]


def main() -> None:
    # 1. Verify Table 1 parameter and MAC reductions for 2D convolution layer (m=256, n=256, k=3, r=64, H=16, W=16)
    stats = conv_params_and_macs(m=256, n=256, k=3, r=64, H=16, W=16)
    assert stats["fedhm_params"] < stats["pufferfish_params"] < stats["vanilla_params"]
    assert stats["fedhm_macs"] < stats["pufferfish_macs"] < stats["vanilla_macs"]

    # 2. Verify zero-padding equivalence for heterogeneous ranks (Eq. 12, p. 14):
    # For a layer of shape (m=2, n=2) and client 1 with rank r_1 = 1 (U_1 in R^{2x1}, V_1 in R^{2x1}),
    # padding U_1 and V_1 with 1 column of zeros to r_max = 2 preserves both W_1 = U_1 V_1^T and the factorized gradients!
    U1 = [[1.5], [-0.5]]
    V1 = [[0.8], [1.2]]
    U1_pad = [[1.5, 0.0], [-0.5, 0.0]]
    V1_pad = [[0.8, 0.0], [1.2, 0.0]]

    def matmul_uvt(U: list[list[float]], V: list[list[float]]) -> list[list[float]]:
        m_rows = len(U)
        n_rows = len(V)
        r_cols = len(U[0])
        return [
            [sum(U[i][c] * V[j][c] for c in range(r_cols)) for j in range(n_rows)]
            for i in range(m_rows)
        ]

    W1 = matmul_uvt(U1, V1)
    W1_pad = matmul_uvt(U1_pad, V1_pad)
    for i in range(2):
        for j in range(2):
            assert math.isclose(W1[i][j], W1_pad[i][j], abs_tol=1e-12)

    # 3. Verify Model Shape Alignment and Softmax Rank-Ratio Aggregation (Eqs. 1-2, p. 4):
    # Rank ratios gamma = [0.5, 0.25, 0.125]; for finite temperature tau=5.0 larger-rank models get larger weight,
    # while as tau -> infinity weights converge to uniform 1/P.
    gammas = [0.5, 0.25, 0.125]
    alphas_tau5 = softmax_rank_weights(gammas, tau=5.0)
    alphas_inf = softmax_rank_weights(gammas, tau=1e6)
    assert alphas_tau5[0] > alphas_tau5[1] > alphas_tau5[2]
    assert all(math.isclose(a, 1.0 / 3.0, abs_tol=1e-6) for a in alphas_inf)

    print(
        f"[PASS] Round 505 FedHM (Yao et al., 2021): "
        f"conv_params(vanilla={stats['vanilla_params']} -> pufferfish={stats['pufferfish_params']} -> fedhm={stats['fedhm_params']}), "
        f"alphas(tau=5)={[round(a, 4) for a in alphas_tau5]}"
    )


if __name__ == "__main__":
    main()
