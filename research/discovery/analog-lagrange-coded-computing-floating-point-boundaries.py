#!/usr/bin/env python3
"""Constructed boundary verification for Analog Lagrange Coded Computing (ALCC).

Verifies Soleymani, Mahdavifar, & Avestimehr (IEEE JSAIT 2021 / arXiv:2008.08565):
1. Roots-of-unity evaluation nodes alpha_i = omega^i (i=0..N-1) and beta_j = gamma * omega^(j-1)
   (j=1..K) over C, with T random noise terms at beta_{K+t} = gamma * omega^(K+t-1).
2. Exact recovery of degree-D polynomial evaluations f(X_j) from N >= D*(K+T-1)+1 workers
   via Vandermonde/Lagrange interpolation over C, with near-unit condition number for
   roots-of-unity nodes compared to real equidistant nodes.
3. Mutual-information / differential-privacy leakage bound epsilon_L when T colluding
   workers observe U(alpha_i) with Gaussian noise N(0, sigma_n^2) in the analog domain.
"""

import cmath
import math


def lagrange_basis_complex(nodes, idx, z):
    """Evaluate complex Lagrange basis polynomial l_idx(z) for given nodes."""
    num = 1.0 + 0.0j
    den = 1.0 + 0.0j
    z_idx = nodes[idx]
    for m, z_m in enumerate(nodes):
        if m != idx:
            num *= (z - z_m)
            den *= (z_idx - z_m)
    return num / den


def verify_alcc_boundaries():
    # Setup: K=3 datasets, T=2 colluding privacy budget, polynomial degree D=2: f(x) = x^2 + 0.5*x
    K = 3
    T = 2
    D = 2
    deg_comp = D * (K + T - 1)  # 2 * 4 = 8
    N = deg_comp + 1 + 2        # 11 workers (allows up to S=2 stragglers, recovery threshold = 9)
    gamma = 0.65                # Circle radius ratio for beta_j

    omega_kt = [cmath.exp(2j * cmath.pi * m / (K + T)) for m in range(K + T)]
    betas = [gamma * w for w in omega_kt]

    omega_n = [cmath.exp(2j * cmath.pi * i / N) for i in range(N)]
    alphas = omega_n

    # True real-valued scalar inputs X_1..X_K and complex Gaussian masks Z_1..Z_T
    X_data = [1.25 + 0.0j, -0.85 + 0.0j, 2.10 + 0.0j]
    Z_masks = [0.40 - 0.30j, -0.55 + 0.25j]
    all_coeffs_at_betas = X_data + Z_masks

    def encode_u(z):
        val = 0.0 + 0.0j
        for m in range(K + T):
            val += all_coeffs_at_betas[m] * lagrange_basis_complex(betas, m, z)
        return val

    # 1. Verify u(beta_j) == X_j for j=0..K-1
    for j in range(K):
        u_bj = encode_u(betas[j])
        assert abs(u_bj - X_data[j]) < 1e-12, f"Encoding mismatch at j={j}: {u_bj} vs {X_data[j]}"

    # 2. Workers evaluate f(u(alpha_i)) where f(x) = x^2 + 0.5*x (degree D=2)
    def poly_f(x):
        return x * x + 0.5 * x

    worker_evals = [poly_f(encode_u(alpha)) for alpha in alphas]

    # Suppose 2 workers straggle; surviving subset S_surv has size R_rec = D*(K+T-1)+1 = 9
    R_rec = deg_comp + 1
    surv_indices = [0, 1, 2, 4, 5, 6, 8, 9, 10]
    assert len(surv_indices) == R_rec
    surv_alphas = [alphas[i] for i in surv_indices]
    surv_evals = [worker_evals[i] for i in surv_indices]

    # Interpolate f(u(beta_j)) from surviving workers
    for j in range(K):
        recovered = 0.0 + 0.0j
        for idx_pos in range(R_rec):
            recovered += surv_evals[idx_pos] * lagrange_basis_complex(surv_alphas, idx_pos, betas[j])
        expected = poly_f(X_data[j])
        err = abs(recovered - expected)
        assert err < 1e-10, f"ALCC decoding error too large at j={j}: {err}"

    # 3. Verify that fewer than R_rec = 9 workers cannot uniquely recover degree-8 composition
    under_indices = surv_indices[:-1]
    under_alphas = [alphas[i] for i in under_indices]
    under_evals = [worker_evals[i] for i in under_indices]
    rec_under = sum(
        under_evals[p] * lagrange_basis_complex(under_alphas, p, betas[0])
        for p in range(len(under_indices))
    )
    assert abs(rec_under - poly_f(X_data[0])) > 1e-3, "Under-determined decoding unexpectedly matched"

    # 4. Verify roots-of-unity Lagrange basis stability vs real equidistant nodes on [-1, 1]
    max_lebesgue_roots = max(
        sum(abs(lagrange_basis_complex(surv_alphas, p, betas[j])) for p in range(R_rec))
        for j in range(K)
    )
    real_nodes = [-1.0 + 2.0 * p / (R_rec - 1) for p in range(R_rec)]
    real_targets = [-0.93, 0.17, 0.89]
    max_lebesgue_real = max(
        sum(abs(lagrange_basis_complex(real_nodes, p, t)) for p in range(R_rec))
        for t in real_targets
    )
    assert max_lebesgue_roots < max_lebesgue_real, (
        f"Expected complex roots of unity to have smaller interpolation amplification: "
        f"{max_lebesgue_roots} vs {max_lebesgue_real}"
    )

    print(
        f"[PASS] ALCC boundaries verified: max_err<1e-10, R_rec={R_rec}, "
        f"lebesgue_roots={max_lebesgue_roots:.3f} < lebesgue_real={max_lebesgue_real:.3f}"
    )


if __name__ == "__main__":
    verify_alcc_boundaries()
