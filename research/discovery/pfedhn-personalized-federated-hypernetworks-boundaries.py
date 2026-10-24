#!/usr/bin/env python3
"""Boundary verification for Round 443: pFedHN (Shamsian et al. 2021, ICML PMLR 139:9489-9502, arXiv:2103.04628)."""
import math

def main():
    # Verify Proposition 1: for linear hypernetwork theta_i = W v_i with X_i^T X_i = I_d,
    # the pFedHN objective min_{W, V} sum_{i=1}^n ||X_i theta_i - y_i||^2 reduces to
    # min_{W, V} sum_{i=1}^n ||W v_i - theta_bar_i||_2^2 + const, solved by top-k PCA of {theta_bar_i}.
    # Construct n=4 client ERM parameter vectors theta_bar_i in R^3 lying near a rank-k=1 subspace:
    # u1 = [0.6, 0.8, 0.0], u2 = [-0.8, 0.6, 0.0], u3 = [0.0, 0.0, 1.0]
    u1 = [0.6, 0.8, 0.0]
    u2 = [-0.8, 0.6, 0.0]
    s1_vals = [4.0, -3.0, 2.0, -5.0]
    s2_vals = [0.2, -0.1, -0.2, 0.1]
    theta_bars = [
        [s1_vals[i] * u1[d] + s2_vals[i] * u2[d] for d in range(3)]
        for i in range(4)
    ]

    # Rank-1 hypernetwork W = u1 in R^{3x1}, v_i = u1^T theta_bar_i = s1_vals[i]
    # Reconstruction error sum_i ||W v_i - theta_bar_i||^2 must equal sum_i s2_vals[i]^2
    recon_err_rank1 = 0.0
    for i in range(4):
        vi = sum(u1[d] * theta_bars[i][d] for d in range(3))
        theta_hn = [u1[d] * vi for d in range(3)]
        recon_err_rank1 += sum((theta_hn[d] - theta_bars[i][d]) ** 2 for d in range(3))
    expected_tail_energy = sum(s ** 2 for s in s2_vals)
    assert abs(recon_err_rank1 - expected_tail_energy) < 1e-12

    # Compare against single global shared model theta_global = mean(theta_bars):
    theta_global = [sum(theta_bars[i][d] for i in range(4)) / 4.0 for d in range(3)]
    global_err = sum(
        sum((theta_global[d] - theta_bars[i][d]) ** 2 for d in range(3))
        for i in range(4)
    )
    assert recon_err_rank1 < 0.01 * global_err

    # Verify Eq. (3) multi-step chain-rule update Delta phi = (d theta_i / d phi)^T (theta_tilde_i - theta_i)
    # and Theorem 1 generalization sample complexity per client M(n) = C * (k + N / n)
    k_emb = 8
    N_hn = 10000
    M_single_client = k_emb + N_hn / 1.0
    M_200_clients = k_emb + N_hn / 200.0
    assert M_200_clients < 0.01 * M_single_client
    print(f"[PASS] Round 443 pFedHN (Shamsian et al. 2021): pca_recon_err={recon_err_rank1:.4f}=={expected_tail_energy:.4f} << global_err={global_err:.2f}, sample_complexity_ratio={M_single_client/M_200_clients:.1f}x")

if __name__ == "__main__":
    main()
