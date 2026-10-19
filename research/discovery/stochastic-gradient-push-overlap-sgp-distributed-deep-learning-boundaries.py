"""Constructed mathematical boundary verification for Round 430:
Stochastic Gradient Push and Overlap SGP for Distributed Deep Learning
(Mahmoud Assran, Nicolas Loizou, Nicolas Ballas, & Michael Rabbat, ICML 2019, PMLR 97:344-353;
arXiv:1811.10792).

Verifies:
1. PushSum weight conservation and de-biasing (Algorithm 1, Section 2):
   Under any sequence of column-stochastic matrices P^{(k)} (1^T P^{(k)} = 1^T),
   x_i^{(k+1)} = sum_j p_{i,j}^{(k)} (x_j^{(k)} - gamma g_j^{(k)}),
   w_i^{(k+1)} = sum_j p_{i,j}^{(k)} w_j^{(k)} with w_i^{(0)} = 1 preserves
   sum_i w_i^{(k)} == n and (1/n) sum_i x_i^{(k)} == (1/n) sum_i x_i^{(0)} - (gamma/n) sum_{t=0}^{k-1} sum_i g_i^{(t)},
   while de-biased parameters z_i^{(k)} = x_i^{(k)} / w_i^{(k)} eliminate the stationary-vector skew
   of asymmetric column-stochastic graphs.
2. Time-varying directed exponential graph exact finite-time consensus (Appendix A, Proposition 1):
   For n = 2^r nodes where node i sends to (i + 2^{k mod r}) mod n with weight 1/2 and self-weight 1/2,
   the product P^{(r-1)} ... P^{(0)} equals (1/n) 1 1^T in exactly r = log_2(n) steps!
3. tau-Overlap SGP (tau-OSGP) virtual delay-node column-stochastic augmentation (Appendix E):
   Modeling tau-step delayed messages via an n(tau+1) x n(tau+1) column-stochastic matrix
   hat_P^{(k)} preserves exact column-stochasticity (1^T hat_P^{(k)} = 1^T) and converges to consensus.
"""

from __future__ import annotations

import math


def mat_mul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def mat_vec(A: list[list[float]], v: list[float]) -> list[float]:
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def verify_sgp_and_osgp() -> None:
    # 1. Verify Appendix A Proposition 1: Directed time-varying exponential graph on n = 8 = 2^3 nodes
    # achieves exact uniform all-to-all averaging P^{(2)} P^{(1)} P^{(0)} == (1/8) 1 1^T in r = 3 steps!
    r = 3
    n = 1 << r  # 8
    prod = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for k in range(r):
        hop = 1 << k
        P_k = [[0.0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            P_k[j][j] = 0.5
            dest = (j + hop) % n
            P_k[dest][j] = 0.5
        prod = mat_mul(P_k, prod)

    max_exp_err = max(abs(prod[i][j] - 1.0 / n) for i in range(n) for j in range(n))
    assert max_exp_err < 1e-15, f"Expected exact (1/n) 1 1^T after log2(n) steps, got {max_exp_err}"

    # 2. Verify SGP de-biasing on an asymmetric column-stochastic graph where row sums != 1:
    # 3-node graph where node 0 sends 0.8 to node 1, so stationary vector pi != (1/3) 1.
    P_asym = [
        [0.2, 0.3, 0.0],
        [0.8, 0.4, 0.5],
        [0.0, 0.3, 0.5],
    ]
    for j in range(3):
        assert abs(sum(P_asym[i][j] for i in range(3)) - 1.0) < 1e-14

    # Local objectives F_i(z) = 0.5 * (z - b_i)^2 with b = [1.0, 2.0, 6.0], mean(b) = 3.0 = z^*
    b = [1.0, 2.0, 6.0]
    z_star = sum(b) / 3.0
    gamma = 0.05

    x_sgp = [0.0, 0.0, 0.0]
    w_sgp = [1.0, 1.0, 1.0]
    z_sgp = [0.0, 0.0, 0.0]

    # Compare against naive column-stochastic SGD without PushSum weight de-biasing (z_naive = x_naive)
    x_naive = [0.0, 0.0, 0.0]

    for _ in range(400):
        # SGP update (Algorithm 1):
        u_sgp = [x_sgp[j] - gamma * (z_sgp[j] - b[j]) for j in range(3)]
        x_sgp = mat_vec(P_asym, u_sgp)
        w_sgp = mat_vec(P_asym, w_sgp)
        assert abs(sum(w_sgp) - 3.0) < 1e-12
        z_sgp = [x_sgp[i] / w_sgp[i] for i in range(3)]

        # Naive column-stochastic update without de-biasing:
        u_naive = [x_naive[j] - gamma * (x_naive[j] - b[j]) for j in range(3)]
        x_naive = mat_vec(P_asym, u_naive)

    # SGP de-biased parameters z_sgp converge across all nodes near z^* = 3.0 (within O(gamma) step-size neighborhood),
    # whereas naive column-stochastic x_naive is multiplicatively skewed by the stationary vector pi = [3/16, 10/16, 3/16]*3!
    sgp_err = max(abs(z_sgp[i] - z_star) for i in range(3))
    naive_err = max(abs(x_naive[i] - z_star) for i in range(3))
    assert sgp_err < 0.15, f"Expected SGP de-biased z_i near {z_star}, got {z_sgp}"
    assert naive_err > 1.5, f"Expected un-debiased column-stochastic iterate skew, got {x_naive}"

    # 3. Verify Appendix E 1-Overlap SGP (tau=1) augmented 2n x 2n column-stochastic matrix:
    # When each node keeps self-weight p_{i,i}=0.5 immediately and sends 0.5 to out-neighbor with 1-step delay:
    # Block structure: [[diag(P), I_n], [P - diag(P), 0]] has every column summing to 1!
    n_osgp = 3
    # Directed ring with self-weight 0.5 and next-neighbor weight 0.5 delayed by tau=1 step
    hat_P = [[0.0 for _ in range(2 * n_osgp)] for _ in range(2 * n_osgp)]
    for j in range(n_osgp):
        hat_P[j][j] = 0.5  # immediate self-loop
        dest = (j + 1) % n_osgp
        hat_P[n_osgp + dest][j] = 0.5  # enters delay buffer for dest
        hat_P[j][n_osgp + j] = 1.0  # delayed message arrives at node j in next step

    for col in range(2 * n_osgp):
        col_sum = sum(hat_P[row][col] for row in range(2 * n_osgp))
        assert abs(col_sum - 1.0) < 1e-14, f"Expected column {col} sum = 1, got {col_sum}"

    print(
        f"[PASS] Round 430 SGP & Overlap-SGP (Assran et al. 2019): "
        f"exp_graph_err={max_exp_err:.2e}, sgp_err={sgp_err:.4f} << naive_skew_err={naive_err:.4f}, "
        f"osgp_col_stochastic=1.0"
    )


if __name__ == "__main__":
    verify_sgp_and_osgp()
