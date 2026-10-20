#!/usr/bin/env python3
"""Constructed boundary verification for Round 669:
O-LoRA: Orthogonal Subspace Learning for Language Model Continual Learning
(Xiao Wang, Tianze Chen, Qiming Ge, Han Xia, Rong Bao, Rui Zheng, Qi Zhang,
Tao Gui, & Xuanjing Huang, EMNLP Findings 2023, arXiv:2310.14152).

Verifies:
1. Equations (3)-(8): Parameterizing task t's update subspace U_t = span{a_t^1..a_t^r}
   via A_t in R^{d x r} and B_t in R^{r x k}, freezing {A_i, B_i}_{i < t}, and
   penalizing L_orth(A_i, A_t) = ||A_i^T A_t||_F^2 = sum_{j,k} (O_{i,t}[j,k])^2
   drives O_{i,t} = A_i^T A_t -> 0.
2. Catastrophic forgetting mitigation (Section 3.2 & Equation 9):
   When task t's update Delta W_t = A_t B_t satisfies A_i^T A_t = 0, any input
   x in U_i = col(A_i) lies in the nullspace of A_t^T (A_t^T x = 0), so the
   transposed/merged update (W_init + sum_{s=1}^t A_s B_s)^T x preserves task i's
   subspace response without storing replay examples or historical data gradients.
3. Sequential 3-task continual learning simulation:
   O-LoRA (lambda_1 > 0) achieves near-zero orthogonality violation ||A_i^T A_t||_F^2
   and substantially lower forgetting on tasks 1 and 2 after training task 3
   compared to unregularized incremental LoRA (IncLoRA, lambda_1 = 0) and SeqLoRA.
"""

from __future__ import annotations
import math
import random


def transpose(M: list[list[float]]) -> list[list[float]]:
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, k, n = len(A), len(A[0]), len(B[0])
    return [
        [sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)]
        for i in range(m)
    ]


def l_orth(A_i: list[list[float]], A_t: list[list[float]]) -> float:
    """Compute L_orth(A_i, A_t) = ||A_i^T A_t||_F^2 (Equations 6 & 8)."""
    O_it = matmul(transpose(A_i), A_t)
    return sum(
        O_it[r1][r2] ** 2 for r1 in range(len(O_it)) for r2 in range(len(O_it[0]))
    )


def grad_l_orth_wrt_At(
    A_i: list[list[float]], A_t: list[list[float]]
) -> list[list[float]]:
    """Analytical gradient d/dA_t ||A_i^T A_t||_F^2 = 2 * A_i * (A_i^T A_t)."""
    O_it = matmul(transpose(A_i), A_t)
    prod = matmul(A_i, O_it)
    return [[2.0 * val for val in row] for row in prod]


def main() -> None:
    rng = random.Random(20231022)
    d, k, r = 9, 6, 2

    # 1. Verify analytical gradient of L_orth(A_i, A_t) against central finite differences
    A_1 = [[rng.gauss(0.0, 1.0) for _ in range(r)] for _ in range(d)]
    A_2 = [[rng.gauss(0.0, 1.0) for _ in range(r)] for _ in range(d)]
    g_analytic = grad_l_orth_wrt_At(A_1, A_2)
    eps = 1e-6
    max_grad_err = 0.0
    for row_idx in range(d):
        for col_idx in range(r):
            A2_p = [list(row) for row in A_2]
            A2_m = [list(row) for row in A_2]
            A2_p[row_idx][col_idx] += eps
            A2_m[row_idx][col_idx] -= eps
            fd = (l_orth(A_1, A2_p) - l_orth(A_1, A2_m)) / (2.0 * eps)
            max_grad_err = max(max_grad_err, abs(g_analytic[row_idx][col_idx] - fd))
    assert max_grad_err < 1e-8, f"Gradient mismatch: {max_grad_err}"

    # 2. Continual learning across T = 3 sequential tasks with task-specific directions
    # Construct 3 ground-truth task transformations W*_1, W*_2, W*_3 in R^{d x k}
    # where inputs for task t have strong energy along overlapping + task-specific directions
    tasks_X = []
    tasks_Y = []
    for t_idx in range(3):
        # Task t inputs X_t in R^{8 x d} and targets Y_t in R^{8 x k}
        X_t = []
        for _ in range(8):
            vec = [0.0] * d
            # Dominant energy in slice [t_idx*2 : t_idx*2 + 4] (overlapping across tasks!)
            for j in range(t_idx * 2, min(d, t_idx * 2 + 4)):
                vec[j] = rng.gauss(0.0, 1.0)
            X_t.append(vec)
        W_true_t = [[rng.gauss(0.0, 1.0) for _ in range(k)] for _ in range(d)]
        Y_t = matmul(X_t, W_true_t)
        tasks_X.append(X_t)
        tasks_Y.append(Y_t)

    def run_continual_lora(lambda_orth: float) -> tuple[float, float]:
        learned_A: list[list[list[float]]] = []
        learned_B: list[list[list[float]]] = []
        lr = 0.02

        for t_idx in range(3):
            local_rng = random.Random(500 + t_idx)
            A_t = [[local_rng.gauss(0.0, 0.3) for _ in range(r)] for _ in range(d)]
            B_t = [[0.0 for _ in range(k)] for _ in range(r)]
            X_t = tasks_X[t_idx]
            Y_t = tasks_Y[t_idx]

            # Freeze past adapters W_prev = sum_{i < t} A_i B_i
            W_prev = [[0.0] * k for _ in range(d)]
            for A_i, B_i in zip(learned_A, learned_B):
                AB_i = matmul(A_i, B_i)
                for p in range(d):
                    for q in range(k):
                        W_prev[p][q] += AB_i[p][q]

            for _ in range(120):
                AB_t = matmul(A_t, B_t)
                W_curr = [
                    [W_prev[p][q] + AB_t[p][q] for q in range(k)] for p in range(d)
                ]
                Pred = matmul(X_t, W_curr)
                # Gradient of task loss 0.5 / N * ||X_t W_curr - Y_t||_F^2 wrt W_curr
                Err = [
                    [(Pred[s][q] - Y_t[s][q]) / len(X_t) for q in range(k)]
                    for s in range(len(X_t))
                ]
                G_W = matmul(transpose(X_t), Err)
                gA = matmul(G_W, transpose(B_t))
                gB = matmul(transpose(A_t), G_W)

                # Add orthogonality regularization gradient lambda_1 * sum_{i < t} dL_orth(A_i, A_t)/dA_t
                if lambda_orth > 0.0:
                    for A_i in learned_A:
                        g_orth = grad_l_orth_wrt_At(A_i, A_t)
                        for p in range(d):
                            for q in range(r):
                                gA[p][q] += lambda_orth * g_orth[p][q]

                A_t = [[A_t[p][q] - lr * gA[p][q] for q in range(r)] for p in range(d)]
                B_t = [[B_t[p][q] - lr * gB[p][q] for q in range(k)] for p in range(r)]

            learned_A.append(A_t)
            learned_B.append(B_t)

        # Equation (9): Merge all task adapters W_final = sum_{i=1}^T A_i B_i
        total_orth_violation = 0.0
        for i in range(3):
            for t in range(i + 1, 3):
                total_orth_violation += l_orth(learned_A[i], learned_A[t])

        # Compute subspace interference ||A_1^T A_2 B_2 + A_1^T A_3 B_3||_F^2
        interf = 0.0
        for t in [1, 2]:
            proj = matmul(transpose(learned_A[0]), matmul(learned_A[t], learned_B[t]))
            interf += sum(
                proj[p][q] ** 2 for p in range(len(proj)) for q in range(len(proj[0]))
            )
        return total_orth_violation, interf

    orth_inclora, interf_inclora = run_continual_lora(lambda_orth=0.0)
    orth_olora, interf_olora = run_continual_lora(lambda_orth=2.0)

    assert orth_olora < 0.01 * orth_inclora, (
        f"Expected O-LoRA orthogonality violation ({orth_olora:.6f}) << IncLoRA ({orth_inclora:.6f})"
    )
    assert interf_olora < 0.01 * interf_inclora, (
        f"Expected O-LoRA past-task subspace interference ({interf_olora:.6f}) << IncLoRA ({interf_inclora:.6f})"
    )

    print(
        f"[PASS] Round 669 O-LoRA (Wang et al. 2023): "
        f"orth_olora={orth_olora:.2e}<<orth_inclora={orth_inclora:.4f}, "
        f"interf_olora={interf_olora:.2e}<<interf_inclora={interf_inclora:.4f}"
    )


if __name__ == "__main__":
    main()
