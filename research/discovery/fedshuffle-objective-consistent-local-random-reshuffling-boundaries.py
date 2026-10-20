#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 565: FedShuffle (Horvath et al., TMLR 2022)."""

import itertools
import math
import random


def main():
    rng = random.Random(20220427)

    # 1. Verify Lemma B.5 (Page 20): without-replacement sampling variance formula
    # E[||zeta_pi^k - zeta_bar||^2] == ((m - k) / (k * (m - 1))) * sigma^2
    pop = [-2.4, -0.8, 0.3, 1.1, 1.8, 3.0]
    m_pop = len(pop)
    zeta_bar = sum(pop) / m_pop
    sigma_sq = sum((z - zeta_bar) ** 2 for z in pop) / m_pop
    for k_sub in (1, 2, 3, 4, 6):
        all_perms_k = list(itertools.combinations(pop, k_sub))
        emp_var = sum(((sum(sub) / k_sub) - zeta_bar) ** 2 for sub in all_perms_k) / len(all_perms_k)
        theo_var = ((m_pop - k_sub) / (k_sub * (m_pop - 1))) * sigma_sq
        assert abs(emp_var - theo_var) < 1e-12

    # 2. Verify Section 4.2 (Page 8) exact counterexample: Sum-One (SO) aggregation bias vs FedShuffle (wi / pi)
    # 3 clients with |D_1|=1, |D_2|=2, |D_3|=3 (total |D|=6), weights w = (1/6, 2/6, 3/6).
    # Sample b=2 clients uniformly at random from {0, 1, 2}: S in {(0,1), (0,2), (1,2)}, each with prob 1/3, p_i = 2/3.
    d_sizes = [1, 2, 3]
    total_d = sum(d_sizes)
    w = [sz / total_d for sz in d_sizes]
    p_i = 2.0 / 3.0
    subsets = list(itertools.combinations(range(3), 2))

    so_expected = [0.0, 0.0, 0.0]
    fs_expected = [0.0, 0.0, 0.0]
    for sub in subsets:
        w_sum_sub = sum(w[idx] for idx in sub)
        for idx in sub:
            so_expected[idx] += (1.0 / len(subsets)) * (w[idx] / w_sum_sub)
            fs_expected[idx] += (1.0 / len(subsets)) * (w[idx] / p_i)

    # Verify exact paper values 7/36, 16/45, 9/20 for Sum-One vs exact (1/6, 2/6, 3/6) for FedShuffle
    assert abs(so_expected[0] - (7.0 / 36.0)) < 1e-12
    assert abs(so_expected[1] - (16.0 / 45.0)) < 1e-12
    assert abs(so_expected[2] - (9.0 / 20.0)) < 1e-12
    for idx in range(3):
        assert abs(fs_expected[idx] - w[idx]) < 1e-12

    # 3. Verify Section 4.1 & Appendix F Eq. (36) quadratic objective:
    # FedShuffle converges to true optimum x^*, whereas FedAvgRR converges to biased x_tilde = sum |D_i|^2 e_i / sum |D_i|^2
    # Client 0 owns [0.0], Client 1 owns [2.0, 4.0], Client 2 owns [6.0, 8.0, 12.0] -> true mean x^* = 32 / 6 = 5.333333
    client_data = [[0.0], [2.0, 4.0], [6.0, 8.0, 12.0]]
    x_star = sum( sum(di) for di in client_data ) / total_d
    e_means = [sum(di) / len(di) for di in client_data]
    x_tilde_fedavg = sum((len(client_data[i]) ** 2) * e_means[i] for i in range(3)) / sum(
        len(client_data[i]) ** 2 for i in range(3)
    )
    assert abs(x_star - x_tilde_fedavg) > 1.0

    # Run FedShuffle (Algorithm 1) vs FedAvgRR (Algorithm 2) with random reshuffling and partial participation (b=2)
    x_fs = 0.0
    x_fa = 0.0
    eta_l = 0.01
    eta_g = 1.0
    E_epochs = 2
    fs_tail = []
    fa_tail = []

    for r in range(1600):
        sub = rng.sample(range(3), 2)
        # FedShuffle update: step size scaled by 1/|D_i|, server aggregation weighted by w_i / p_i
        delta_fs = 0.0
        for i in sub:
            yi = x_fs
            di_len = len(client_data[i])
            for _ in range(E_epochs):
                perm = client_data[i][:]
                rng.shuffle(perm)
                for sample_val in perm:
                    yi = yi - (eta_l / di_len) * (yi - sample_val)
            delta_fs += (w[i] / p_i) * (yi - x_fs)
        x_fs = x_fs + eta_g * delta_fs

        # FedAvgRR update: unscaled local step size eta_l / max|D_i|, Sum-One aggregation w_i / sum_{j in S} w_j
        delta_fa = 0.0
        w_sub = sum(w[j] for j in sub)
        for i in sub:
            yi = x_fa
            for _ in range(E_epochs):
                perm = client_data[i][:]
                rng.shuffle(perm)
                for sample_val in perm:
                    yi = yi - (eta_l / 3.0) * (yi - sample_val)
            delta_fa += (w[i] / w_sub) * (yi - x_fa)
        x_fa = x_fa + eta_g * delta_fa
        if r >= 800:
            fs_tail.append(x_fs)
            fa_tail.append(x_fa)

    err_fs = abs((sum(fs_tail) / len(fs_tail)) - x_star)
    err_fa = abs((sum(fa_tail) / len(fa_tail)) - x_star)
    assert err_fs < 0.05
    assert err_fa > 0.7

    print(
        f"[PASS] Round 565 FedShuffle verified: SO_weights=({so_expected[0]:.4f},{so_expected[1]:.4f},{so_expected[2]:.4f}) "
        f"vs w=({w[0]:.4f},{w[1]:.4f},{w[2]:.4f}), err_fs={err_fs:.4f} << err_fa={err_fa:.4f}"
    )


if __name__ == "__main__":
    main()
