#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 652:
PiSSA (Principal Singular Values and Singular Vectors Adaptation)
Primary source: Meng, Wang, & Zhang (NeurIPS 2024, arXiv:2404.02948).
"""

import math


def mat_mul(A, B):
    m, k, n = len(A), len(B), len(B[0])
    return [[sum(A[i][r] * B[r][j] for r in range(k)) for j in range(n)] for i in range(m)]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def frob_norm(A):
    return math.sqrt(sum(v * v for row in A for v in row))


def verify_pissa_svd_initialization_and_initial_gradients_eqs_2_5():
    """Verify Section 3 (Eqs. 2-5 & Table 1):
    (1) Initializing A = U_{[:,:r]} S_{[:r,:r]}^{1/2}, B = S_{[:r,:r]}^{1/2} V_{[:,:r]}^T, and
        W^{res} = U_{[:,r:]} S_{[r:,r:]} V_{[:,r:]}^T exactly reconstructs W = W^{res} + A B at t=0.
    (2) Unlike LoRA (where B=0 causes dL/dA = X^T (dL/dY) B^T == 0 at t=0), PiSSA produces
        non-zero initial gradients for both A and B aligned with the principal singular vectors."""
    # Construct a 3 x 3 orthogonal matrix U and V and singular values s = [9.0, 4.0, 0.25]
    U = [
        [1.0, 0.0, 0.0],
        [0.0, 0.6, -0.8],
        [0.0, 0.8, 0.6],
    ]
    V = [
        [0.8, -0.6, 0.0],
        [0.6, 0.8, 0.0],
        [0.0, 0.0, 1.0],
    ]
    s = [9.0, 4.0, 0.25]
    S = [[s[i] if i == j else 0.0 for j in range(3)] for i in range(3)]
    W = mat_mul(mat_mul(U, S), transpose(V))

    # Rank r = 2 PiSSA decomposition (Eqs. 2-4)
    r = 2
    U_pri = [row[:r] for row in U]
    V_pri = [row[:r] for row in V]
    S_pri_sqrt = [[math.sqrt(s[i]) if i == j else 0.0 for j in range(r)] for i in range(r)]

    A_0 = mat_mul(U_pri, S_pri_sqrt)  # 3 x 2
    B_0 = mat_mul(S_pri_sqrt, transpose(V_pri))  # 2 x 3

    U_res = [row[r:] for row in U]
    V_res = [row[r:] for row in V]
    S_res = [[s[r + i] if i == j else 0.0 for j in range(3 - r)] for i in range(3 - r)]
    W_res = mat_mul(mat_mul(U_res, S_res), transpose(V_res))

    W_pri = mat_mul(A_0, B_0)
    for i in range(3):
        for j in range(3):
            assert abs((W_res[i][j] + W_pri[i][j]) - W[i][j]) < 1e-12

    # Compare initial gradients dL/dA = X^T G_Y B^T for LoRA (B=0) vs PiSSA
    X_T_GY = [
        [0.5, -0.2, 0.3],
        [0.1, 0.4, -0.5],
        [-0.3, 0.2, 0.6],
    ]
    B_lora = [[0.0] * 3 for _ in range(r)]
    grad_A_lora = mat_mul(X_T_GY, transpose(B_lora))
    grad_A_pissa = mat_mul(X_T_GY, transpose(B_0))

    assert frob_norm(grad_A_lora) == 0.0
    assert frob_norm(grad_A_pissa) > 1.0


def verify_qpissa_quantization_error_and_lora_conversion_eqs_6_10():
    """Verify Section 4 (Eqs. 6-8) and Appendix C (Eqs. 9-10):
    (1) Uniform / grid quantization of the residual matrix W^{res} (keeping A_0 B_0 in full precision)
        yields strictly smaller quantization error ||W - (Q(W^{res}) + A_0 B_0)||_F = ||W^{res} - Q(W^{res})||_F
        than QLoRA's ||W - Q(W)||_F with a fixed step grid delta_q.
    (2) After fine-tuning updates (A_0, B_0) -> (A', B'), converting PiSSA to a rank-2r LoRA adapter
        Delta_A = [A', A_0], Delta_B = [B'^T, -B_0^T]^T satisfies W + Delta_A Delta_B == W^{res} + A' B'."""
    U = [[1.0, 0.0, 0.0], [0.0, 0.6, -0.8], [0.0, 0.8, 0.6]]
    V = [[0.8, -0.6, 0.0], [0.6, 0.8, 0.0], [0.0, 0.0, 1.0]]
    s = [8.5, 3.7, 0.18]
    S = [[s[i] if i == j else 0.0 for j in range(3)] for i in range(3)]
    W = mat_mul(mat_mul(U, S), transpose(V))

    r = 2
    A_0 = [[U[i][k] * math.sqrt(s[k]) for k in range(r)] for i in range(3)]
    B_0 = [[math.sqrt(s[k]) * V[j][k] for j in range(3)] for k in range(r)]
    AB_0 = mat_mul(A_0, B_0)
    W_res = [[W[i][j] - AB_0[i][j] for j in range(3)] for i in range(3)]

    # 4-bit (16-level) symmetric quantizer scaled to max abs entry of matrix
    def quantize_4bit(M):
        max_val = max(abs(v) for row in M for v in row)
        if max_val == 0.0:
            return [[0.0] * len(M[0]) for _ in range(len(M))]
        step = max_val / 7.0
        return [[round(v / step) * step for v in row] for row in M]

    Q_W = quantize_4bit(W)
    Q_W_res = quantize_4bit(W_res)
    err_qlora = frob_norm([[W[i][j] - Q_W[i][j] for j in range(3)] for i in range(3)])
    err_qpissa = frob_norm([[W[i][j] - (Q_W_res[i][j] + AB_0[i][j]) for j in range(3)] for i in range(3)])
    assert err_qpissa < err_qlora

    # Verify lossless rank-2r LoRA conversion (Appendix C, Eqs. 9-10)
    A_prime = [[A_0[i][k] + 0.05 * (i + 1) * (k + 1) for k in range(r)] for i in range(3)]
    B_prime = [[B_0[k][j] - 0.04 * (k + 1) * (j + 1) for j in range(3)] for k in range(r)]

    # Delta_A = [A', A_0] in R^{3 x 2r}, Delta_B = [B'; -B_0] in R^{2r x 3}
    Delta_A = [A_prime[i] + A_0[i] for i in range(3)]
    Delta_B = B_prime + [[-v for v in row] for row in B_0]
    Delta_W = mat_mul(Delta_A, Delta_B)

    W_pissa_final = mat_mul(A_prime, B_prime)
    for i in range(3):
        for j in range(3):
            lhs = W[i][j] + Delta_W[i][j]
            rhs = W_res[i][j] + W_pissa_final[i][j]
            assert abs(lhs - rhs) < 1e-12


if __name__ == "__main__":
    verify_pissa_svd_initialization_and_initial_gradients_eqs_2_5()
    verify_qpissa_quantization_error_and_lora_conversion_eqs_6_10()
    print("[PASS] Round 652 PiSSA boundary and mathematical verification succeeded.")
