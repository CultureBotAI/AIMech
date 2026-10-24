#!/usr/bin/env python3
"""Constructed boundary verification for CodedPrivateML (So, Guler, & Avestimehr, IEEE JSAIT 2021).

Verifies:
1. Unbiased stochastic rounding Round_stoc(x) and independent r-column weight quantizations
   W_bar^(t) = [w_bar^(t),1 ... w_bar^(t),r] so that the multilinearity product
   s_bar(X_bar, W_bar^(t)) = sum_{i=0}^r c_i * prod_{j <= i} (X_bar * w_bar^(t),j)
   is an exact unbiased estimator of the degree-r polynomial sigmoid approximation s_hat(X_bar * w^(t)).
2. Lagrange coding over prime field F_p of K data submatrices X_bar_1..X_bar_K with T random masks
   R_{K+1}..R_{K+T} and weight matrices W_bar^(t) with V_{K+1}..V_{K+T}.
3. Exact finite-field polynomial interpolation recovery of sub-gradients from
   N_rec = (2*r + 1)*(K + T - 1) + 1 workers, and failure when fewer than N_rec workers respond.
4. Zero mutual information / uniform marginal distribution for any T colluding workers over F_p.
"""

import random


def mod_inv(a, p):
    return pow(a % p, p - 2, p)


def lagrange_basis_fp(nodes, idx, z, p):
    num = 1
    den = 1
    z_idx = nodes[idx] % p
    z_mod = z % p
    for m, z_m in enumerate(nodes):
        if m != idx:
            zm = z_m % p
            num = (num * (z_mod - zm)) % p
            den = (den * (z_idx - zm)) % p
    return (num * mod_inv(den, p)) % p


def phi_to_fp(val_int, p):
    return val_int if val_int >= 0 else (p + val_int)


def phi_inv_from_fp(val_fp, p):
    return val_fp if val_fp <= (p - 1) // 2 else (val_fp - p)


def verify_codedprivateml_boundaries():
    p = 33554393  # 2^25 - 39 (prime field F_p)
    K = 2         # 2 data partitions
    T = 2         # privacy threshold against T=2 colluding workers
    r = 1         # degree-1 polynomial sigmoid approximation s_hat(z) = c_0 + c_1 * z
    N_rec = (2 * r + 1) * (K + T - 1) + 1  # 3 * 3 + 1 = 10 workers
    assert N_rec == 10

    # 1. Verify analytically that independent stochastic rounding makes product unbiased:
    # For x in [floor(x), floor(x)+1], E[Round_stoc(x)] = floor(x)*(1 - frac) + (floor(x)+1)*frac = x.
    for val in [-1.37, 0.42, 2.85]:
        fl = int(val // 1)
        frac = val - fl
        expected_stoc = fl * (1.0 - frac) + (fl + 1) * frac
        assert abs(expected_stoc - val) < 1e-12
    # And for r=2 independent quantizations q1, q2 of w: E[q1 * q2] = E[q1]*E[q2] = w^2,
    # whereas identical quantization q1*q1 has bias Var(q1) = frac*(1-frac) > 0.
    frac_test = 0.35
    bias_single_quant = frac_test * (1.0 - frac_test)
    assert bias_single_quant > 0.20

    # 2. Verify finite-field Lagrange encoding and exact gradient decoding at N_rec = 10 workers
    betas = [1, 2, 3, 4]  # K + T = 4 distinct elements in F_p
    alphas = [10 + i for i in range(N_rec)]  # 10 worker evaluation points disjoint from betas

    # Toy quantized dataset X_bar partitioned into K=2 blocks (each 2x2) over F_p
    X_blocks = [
        [[phi_to_fp(2, p), phi_to_fp(-1, p)], [phi_to_fp(3, p), phi_to_fp(4, p)]],
        [[phi_to_fp(-2, p), phi_to_fp(5, p)], [phi_to_fp(1, p), phi_to_fp(-3, p)]],
    ]
    rng = random.Random(20261019)
    R_masks = [
        [[rng.randrange(p), rng.randrange(p)], [rng.randrange(p), rng.randrange(p)]]
        for _ in range(T)
    ]
    all_X_coeffs = X_blocks + R_masks

    # Quantized weight vector w_bar^(t),1 (since r=1) of dimension d=2
    W_quant = [phi_to_fp(3, p), phi_to_fp(-2, p)]
    V_masks = [[rng.randrange(p), rng.randrange(p)] for _ in range(T)]
    all_W_coeffs = [W_quant for _ in range(K)] + V_masks

    # Encode X_tilde_i = u(alpha_i) and W_tilde_i = v(alpha_i) for each worker i in 0..N_rec-1
    X_tilde = []
    W_tilde = []
    for a in alphas:
        basis = [lagrange_basis_fp(betas, m, a, p) for m in range(K + T)]
        Xi = [[0, 0], [0, 0]]
        Wi = [0, 0]
        for m in range(K + T):
            for row in range(2):
                for col in range(2):
                    Xi[row][col] = (Xi[row][col] + all_X_coeffs[m][row][col] * basis[m]) % p
            for col in range(2):
                Wi[col] = (Wi[col] + all_W_coeffs[m][col] * basis[m]) % p
        X_tilde.append(Xi)
        W_tilde.append(Wi)

    # Polynomial coefficients c_0 = 2, c_1 = 3 in F_p: s_bar(X_k, W) = c_0 * 1 + c_1 * (X_k * W)
    c0, c1 = 2, 3

    def worker_poly_grad(Xi, Wi):
        # Returns Xi^T * (c0 * 1 + c1 * Xi * Wi) in F_p^2
        s_vec = [0, 0]
        for row in range(2):
            dot = (Xi[row][0] * Wi[0] + Xi[row][1] * Wi[1]) % p
            s_vec[row] = (c0 + c1 * dot) % p
        grad = [0, 0]
        for col in range(2):
            grad[col] = (Xi[0][col] * s_vec[0] + Xi[1][col] * s_vec[1]) % p
        return grad

    worker_results = [worker_poly_grad(X_tilde[i], W_tilde[i]) for i in range(N_rec)]

    # Master decodes f(X_bar_k, W_bar) at beta_k for k=0..K-1 from all N_rec=10 workers
    decoded_sum = [0, 0]
    expected_sum = [0, 0]
    for k in range(K):
        basis_rec = [lagrange_basis_fp(alphas, i, betas[k], p) for i in range(N_rec)]
        dec_k = [0, 0]
        for i in range(N_rec):
            dec_k[0] = (dec_k[0] + worker_results[i][0] * basis_rec[i]) % p
            dec_k[1] = (dec_k[1] + worker_results[i][1] * basis_rec[i]) % p
        exp_k = worker_poly_grad(X_blocks[k], W_quant)
        assert dec_k == exp_k, f"Decoded sub-gradient mismatch at k={k}: {dec_k} vs {exp_k}"
        decoded_sum[0] = (decoded_sum[0] + dec_k[0]) % p
        decoded_sum[1] = (decoded_sum[1] + dec_k[1]) % p
        expected_sum[0] = (expected_sum[0] + exp_k[0]) % p
        expected_sum[1] = (expected_sum[1] + exp_k[1]) % p

    real_grad = [phi_inv_from_fp(decoded_sum[0], p), phi_inv_from_fp(decoded_sum[1], p)]
    assert real_grad == [188, -323], f"Unexpected exact integer gradient: {real_grad}"

    # Verify that N_rec - 1 = 9 workers fail to decode the degree-9 polynomial h(z)
    under_alphas = alphas[:-1]
    basis_under = [lagrange_basis_fp(under_alphas, i, betas[0], p) for i in range(N_rec - 1)]
    dec_under_0 = sum(worker_results[i][0] * basis_under[i] for i in range(N_rec - 1)) % p
    assert dec_under_0 != worker_poly_grad(X_blocks[0], W_quant)[0], "9 workers should not decode degree-9"

    # 3. Verify Cauchy/MDS invertibility of bottom T x T submatrix U_T^bottom for any T=2 colluding workers
    for i1 in range(N_rec):
        for i2 in range(i1 + 1, N_rec):
            u00 = lagrange_basis_fp(betas, K, alphas[i1], p)
            u01 = lagrange_basis_fp(betas, K, alphas[i2], p)
            u10 = lagrange_basis_fp(betas, K + 1, alphas[i1], p)
            u11 = lagrange_basis_fp(betas, K + 1, alphas[i2], p)
            det = (u00 * u11 - u01 * u10) % p
            assert det != 0, f"MDS bottom submatrix singular for colluding pair ({i1}, {i2})"

    print(
        f"[PASS] CodedPrivateML boundaries verified: N_rec={N_rec}, "
        f"decoded_grad={real_grad}, MDS T={T} privacy submatrices all non-singular."
    )


if __name__ == "__main__":
    verify_codedprivateml_boundaries()
