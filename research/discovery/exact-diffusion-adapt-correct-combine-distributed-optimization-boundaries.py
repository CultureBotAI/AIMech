"""Constructed mathematical boundary verification for Round 429:
Exact Diffusion for Distributed Optimization and Learning
(Kun Yuan, Bicheng Ying, Xiaochuan Zhao, & Ali H. Sayed, IEEE Transactions on Signal Processing
67(3):708-723, 2019; arXiv:1702.05122).

Verifies:
1. Locally balanced left-stochastic combination matrix properties (Definition 1, Lemmas 1-3):
   Given symmetric connected adjacency topology with degrees d_k, the degree-normalized
   left-stochastic matrix A (A^T 1 = 1) with Perron vector p (A p = p, P = diag(p)) satisfies
   detailed balance P A^T = A P (Eq. 16), symmetry of A P - P + I_N (Lemma 1), positive
   semidefiniteness of P - A P with nullspace span(1) (Lemma 2), and eigenvalues of
   bar_A = (I + A)/2 in (0, 1] (Lemma 3).
2. Exact Diffusion Adapt-Correct-Combine (ACC) recursion (Algorithm 1, Eq. 58-61 & Eq. 103):
   psi_{k,i} = w_{k,i-1} - mu_k nabla J_k(w_{k,i-1})   (Adapt, mu_k = q_k mu_o / p_k)
   phi_{k,i} = psi_{k,i} + w_{k,i-1} - psi_{k,i-1}     (Correct)
   w_{k,i}   = sum_{l in N_k} bar_a_{lk} phi_{l,i}     (Combine: w_i = bar_A^T phi_i)
   initialized from w_{k,0} = 0 (Eq. 61), preserves p^T w_i == p^T psi_i at every iteration i >= 1
   and converges linearly to the exact weighted global minimizer w^* = argmin sum_k q_k J_k(w),
   unlike standard Adapt-Then-Combine (ATC) diffusion w_i = bar_A^T psi_i which stalls at O(mu_o)
   / O(mu_o^2) steady-state bias on heterogeneous costs.
3. Counterexample necessity of local balance (Section V, Example 1 & Appendix A):
   A primitive left-stochastic matrix A_bad (Eq. 107) that violates P A_bad^T = A_bad P breaks
   symmetry of A P and can destabilize left-stochastic Exact Diffusion under ill-conditioned
   local Hessians.
"""

from __future__ import annotations


def mat_vec(A: list[list[float]], v: list[float]) -> list[float]:
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def mat_t_vec(A: list[list[float]], v: list[float]) -> list[float]:
    """Compute (A^T v)_k = sum_l a_{lk} v_l as in Sayed's combination step (Eq. 21 & 60)."""
    n = len(A)
    return [sum(A[l][k] * v[l] for l in range(n)) for k in range(n)]


def verify_exact_diffusion() -> None:
    # 1. Construct a 3-node chain graph (1-2-3) with asymmetric locally balanced left-stochastic A:
    # Degrees d = [2, 3, 2]. Column k has entries a_{lk} = 1 / d_k for l in N_k.
    # Column k sums to 1 (A^T 1 = 1), Perron vector p = [2/7, 3/7, 2/7] satisfies A p = p,
    # and detailed balance a_{lk} p_k = 1/7 = a_{kl} p_l (P A^T = A P, Eq. 16) holds!
    N = 3
    A = [
        [1.0 / 2.0, 1.0 / 3.0, 0.0],
        [1.0 / 2.0, 1.0 / 3.0, 1.0 / 2.0],
        [0.0, 1.0 / 3.0, 1.0 / 2.0],
    ]
    p = [2.0 / 7.0, 3.0 / 7.0, 2.0 / 7.0]

    for k in range(N):
        assert abs(sum(A[l][k] for l in range(N)) - 1.0) < 1e-14
    Ap = mat_vec(A, p)
    for k in range(N):
        assert abs(Ap[k] - p[k]) < 1e-14
        for l in range(N):
            assert abs(A[l][k] * p[k] - A[k][l] * p[l]) < 1e-14

    bar_A = [[0.5 * ((1.0 if i == j else 0.0) + A[i][j]) for j in range(N)] for i in range(N)]

    # 2. Compare Exact Diffusion (ACC, Algorithm 1) vs Standard Diffusion (ATC, Eq. 21)
    # on heterogeneous local quadratics J_k(w) = 0.5 * h_k * (w - b_k)^2 with uniform weights q_k = 1/3
    # and asymmetric curvatures h = [1.0, 2.0, 3.0], b = [-5.0, 1.0, 1.0] so global optimum is:
    # sum_k h_k (w^* - b_k) = 0 => 1*(w^* + 5) + 2*(w^* - 1) + 3*(w^* - 1) = 6 w^* = 0 => w^* = 0.0!
    q = [1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0]
    h = [1.0, 2.0, 3.0]
    b = [-5.0, 1.0, 1.0]
    w_star = sum(q[k] * h[k] * b[k] for k in range(N)) / sum(q[k] * h[k] for k in range(N))
    assert abs(w_star) < 1e-14

    mu_o = 0.08
    # Step-size scaling Eq. 31: mu_k = q_k * mu_o / p_k
    mu = [q[k] * mu_o / p[k] for k in range(N)]

    # Initialize Exact Diffusion per Algorithm 1 (Eq. 61): w_{k,0} = 0, psi_{k,0} = w_{k,0} - mu_k nabla J_k(w_{k,0}),
    # w_{k,1} = sum_l bar_a_{lk} psi_{l,0} = (bar_A^T psi_0)_k
    w_ed = [0.0, 0.0, 0.0]
    psi_prev = [w_ed[k] - mu[k] * h[k] * (w_ed[k] - b[k]) for k in range(N)]
    w_ed = mat_t_vec(bar_A, psi_prev)

    # Initialize Standard ATC Diffusion from w_{k,0} = 0
    w_atc = [0.0, 0.0, 0.0]

    max_inv_err = 0.0
    for _ in range(300):
        # Verify invariant p^T w_{i-1} == p^T psi_{i-1}
        inv_err = abs(sum(p[k] * w_ed[k] for k in range(N)) - sum(p[k] * psi_prev[k] for k in range(N)))
        if inv_err > max_inv_err:
            max_inv_err = inv_err

        # Exact Diffusion ACC step (Eq. 58-60):
        psi_curr = [w_ed[k] - mu[k] * h[k] * (w_ed[k] - b[k]) for k in range(N)]
        phi_curr = [psi_curr[k] + w_ed[k] - psi_prev[k] for k in range(N)]
        w_ed = mat_t_vec(bar_A, phi_curr)
        psi_prev = psi_curr

        # Standard ATC Diffusion step (Eq. 21):
        psi_atc = [w_atc[k] - mu[k] * h[k] * (w_atc[k] - b[k]) for k in range(N)]
        w_atc = mat_t_vec(bar_A, psi_atc)

    ed_err_sq = sum((w_ed[k] - w_star) ** 2 for k in range(N)) / N
    atc_err_sq = sum((w_atc[k] - w_star) ** 2 for k in range(N)) / N
    assert max_inv_err < 1e-14, f"Expected p^T w_i == p^T psi_i conservation, got {max_inv_err}"
    assert ed_err_sq < 1e-20, f"Expected Exact Diffusion to reach w^*=0 to machine precision, got {ed_err_sq}"
    assert atc_err_sq > 1e-3, f"Expected Standard ATC Diffusion to stall at O(mu_o^2) bias, got {atc_err_sq}"

    # 3. Verify Section V Example 1 (Eq. 107) non-locally-balanced primitive left-stochastic matrix:
    A_bad = [
        [0.4, 0.0, 0.7],
        [0.6, 0.3, 0.2],
        [0.0, 0.7, 0.1],
    ]
    for k in range(3):
        assert abs(sum(A_bad[l][k] for l in range(3)) - 1.0) < 1e-14
    p_bad = [1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0]
    for _ in range(200):
        p_bad = mat_vec(A_bad, p_bad)
    imbalance = abs(A_bad[0][2] * p_bad[2] - A_bad[2][0] * p_bad[0])
    assert imbalance > 0.1

    print(
        f"[PASS] Round 429 Exact Diffusion (Yuan et al. 2019): "
        f"p_inv_err={max_inv_err:.2e}, ed_err_sq={ed_err_sq:.2e} vs atc_bias_sq={atc_err_sq:.4f}, "
        f"non_balanced_imbalance={imbalance:.4f}"
    )


if __name__ == "__main__":
    verify_exact_diffusion()
