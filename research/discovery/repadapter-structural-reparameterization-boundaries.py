#!/usr/bin/env python3
"""Constructed boundary and algebraic verification for Round 701:
Towards Efficient Visual Adaption via Structural Re-parameterization (RepAdapter)
(Luo et al., 2023, arXiv:2302.08106).
"""

import random


def matmul(A, B):
    R = len(A)
    K = len(A[0])
    C = len(B[0])
    assert len(B) == K
    return [
        [sum(A[r][k] * B[k][c] for k in range(K)) for c in range(C)]
        for r in range(R)
    ]


def add_bias(X, b):
    return [[ row[j] + b[j] for j in range(len(b)) ] for row in X]


def group_up_projection_train(X_hidden, W_groups, b_u):
    """Section 3.2.2 Eq. 11: phi_u(X') = [X'_{g_0} W_{g_0}, ..., X'_{g_{k-1}} W_{g_{k-1}}] + b_u."""
    n = len(X_hidden)
    c = len(X_hidden[0])
    k = len(W_groups)
    assert c % k == 0
    c_g = c // k
    group_outs = []
    for g_idx, W_g in enumerate(W_groups):
        sub_X = [row[g_idx * c_g : (g_idx + 1) * c_g] for row in X_hidden]
        group_outs.append(matmul(sub_X, W_g))
    # Concatenate along feature dimension
    concat = []
    for r in range(n):
        row = []
        for g_idx in range(k):
            row.extend(group_outs[g_idx][r])
        concat.append(row)
    return add_bias(concat, b_u)


def zero_pad_group_weights(W_groups):
    """Section 3.2.2: Convert group-wise weights W_{g_i} in R^{(c/k) x (d/k)} to a single
    block-diagonal matrix W_u in R^{c x d} via zero padding.
    """
    k = len(W_groups)
    c_g = len(W_groups[0])
    d_g = len(W_groups[0][0])
    c = k * c_g
    d = k * d_g
    W_u = [[0.0] * d for _ in range(c)]
    for g_idx, W_g in enumerate(W_groups):
        for r in range(c_g):
            for col in range(d_g):
                W_u[g_idx * c_g + r][g_idx * d_g + col] = W_g[r][col]
    return W_u


def repadapter_train_forward(X, W_d, b_d, W_groups, b_u, scale_s=1.0):
    """Section 3.2.1 Eq. 8 & Section 4.2: Training-time forward pass of RepAdapter:
    f(X; theta) = X + s * phi_u(phi_d(X)).
    """
    hidden = add_bias(matmul(X, W_d), b_d)
    up = group_up_projection_train(hidden, W_groups, b_u)
    n = len(X)
    d = len(X[0])
    return [[X[r][j] + scale_s * up[r][j] for j in range(d)] for r in range(n)]


def reparameterize_repadapter(W_d, b_d, W_groups, b_u, W_0, b_0, scale_s=1.0):
    """Section 3.2.1 Eqs. 9-10:
    1) W_u = zero_pad(W_groups)
    2) W_ada = s * W_d W_u + I_d,  b_ada = s * (b_d W_u + b_u)
    3) W_rep = W_ada W_0,          b_rep = b_ada W_0 + b_0.
    """
    d = len(W_d)
    W_u = zero_pad_group_weights(W_groups)
    W_d_W_u = matmul(W_d, W_u)
    W_ada = [
        [scale_s * W_d_W_u[r][col] + (1.0 if r == col else 0.0) for col in range(d)]
        for r in range(d)
    ]
    bd_Wu = matmul([b_d], W_u)[0]
    b_ada = [scale_s * (bd_Wu[j] + b_u[j]) for j in range(d)]

    W_rep = matmul(W_ada, W_0)
    b_ada_W_0 = matmul([b_ada], W_0)[0]
    b_rep = [b_ada_W_0[j] + b_0[j] for j in range(len(b_0))]
    return W_ada, b_ada, W_rep, b_rep


def main():
    rng = random.Random(2023)
    n_tokens = 6
    d = 12
    c = 8  # Hidden dimension c = 8 (Section 4.2)
    k = 2  # Number of groups k = 2 (Section 4.2)
    d_out = 10
    scale_s = 0.5

    # 1. Verify 25% weight parameter savings of dense-to-sparse structure when k = 2 (Section 1 & 3.2.2):
    dense_weight_params = d * c + c * d
    sparse_weight_params = d * c + k * (c // k) * (d // k)
    saving_ratio = (dense_weight_params - sparse_weight_params) / dense_weight_params
    assert abs(saving_ratio - 0.25) < 1e-12

    # 2. Verify exact algebraic equivalence between training-time sequential RepAdapter + projection (W_0, b_0)
    # and inference-time structurally re-parameterized single projection (W_rep, b_rep) (Eqs. 9-12):
    X = [[rng.gauss(0.0, 1.0) for _ in range(d)] for _ in range(n_tokens)]
    W_d = [[rng.gauss(0.0, 0.2) for _ in range(c)] for _ in range(d)]
    b_d = [rng.gauss(0.0, 0.1) for _ in range(c)]
    W_groups = [
        [[rng.gauss(0.0, 0.2) for _ in range(d // k)] for _ in range(c // k)]
        for _ in range(k)
    ]
    b_u = [rng.gauss(0.0, 0.1) for _ in range(d)]
    W_0 = [[rng.gauss(0.0, 0.3) for _ in range(d_out)] for _ in range(d)]
    b_0 = [rng.gauss(0.0, 0.1) for _ in range(d_out)]

    # Training-time two-step forward: Y_train = f(X; theta) W_0 + b_0
    f_X = repadapter_train_forward(X, W_d, b_d, W_groups, b_u, scale_s=scale_s)
    Y_train = add_bias(matmul(f_X, W_0), b_0)

    # Inference-time re-parameterized forward: Y_infer = X W_rep + b_rep
    W_ada, b_ada, W_rep, b_rep = reparameterize_repadapter(
        W_d, b_d, W_groups, b_u, W_0, b_0, scale_s=scale_s
    )
    f_X_ada = add_bias(matmul(X, W_ada), b_ada)
    Y_infer = add_bias(matmul(X, W_rep), b_rep)

    max_ada_err = max(
        abs(f_X[r][j] - f_X_ada[r][j]) for r in range(n_tokens) for j in range(d)
    )
    max_rep_err = max(
        abs(Y_train[r][j] - Y_infer[r][j]) for r in range(n_tokens) for j in range(d_out)
    )
    assert max_ada_err < 1e-14
    assert max_rep_err < 1e-14

    # Verify inference parameter shape matches W_0 and b_0 exactly (zero extra inference parameters):
    assert len(W_rep) == len(W_0) and len(W_rep[0]) == len(W_0[0])
    assert len(b_rep) == len(b_0)

    print(
        f"[PASS] RepAdapter boundary verification passed: "
        f"k2_weight_saving={saving_ratio*100:.1f}%, "
        f"max_ada_err={max_ada_err:.2e}, max_rep_err={max_rep_err:.2e}, "
        f"delta_P_infer=0, delta_FLOPs_infer=0"
    )


if __name__ == "__main__":
    main()
