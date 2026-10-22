#!/usr/bin/env python3
"""Deterministic boundary verification for Round 832:
TSHT Two-Stage Hard Thresholding with Plurality Voting for Invalid Instruments
(Guo, Kang, Cai, & Small, JRSS-B 2018, arXiv:1603.05224v3).

Verifies:
1. Plurality condition IN1-P (Section 2.2, Theorem 1, pp. 6-7):
   Even when valid instruments are a minority of relevant instruments (e.g., 4 out of 9,
   violating the 50% majority rule), if the valid cluster (pi_j / gamma_j = 0) is strictly
   larger than any single invalid ratio cluster (pi_j / gamma_j = c != 0), the causal
   effect beta^* is uniquely identified and recovered by TSHT with plurality voting.
2. Two-Stage Hard Thresholding with Symmetric Voting Matrix (Section 3.2-3.5, Equations 5-12):
   - Stage 1 (Eq. 5): Selects relevant instruments S_hat = {j : |gamma_hat_j| >= tau_1}.
   - Stage 2 (Eqs. 7-11): Forms candidate beta^[j] = Gamma_hat_j / gamma_hat_j, residuals
     pi_hat_k^[j] = Gamma_hat_k - beta^[j] * gamma_hat_k, symmetric voting matrix V_{k,j},
     and plurality winner S_hat_V = argmax_j ||V_{.,j}||_0.
"""

import math


def run_tsht_plurality_voting():
    beta_true = 2.5
    # 12 candidate instruments:
    # - j=0..3 (4 instruments): valid & relevant (gamma != 0, pi = 0 -> ratio = 2.5)
    # - j=4..5 (2 instruments): invalid cluster A (pi/gamma = +1.5 -> ratio = 4.0)
    # - j=6..7 (2 instruments): invalid cluster B (pi/gamma = -1.2 -> ratio = 1.3)
    # - j=8    (1 instrument):  invalid singleton C (pi/gamma = +3.0 -> ratio = 5.5)
    # - j=9..11 (3 instruments): irrelevant noise instruments (gamma = 0, pi = 0)
    # Note: Valid instruments are 4/9 < 50% of relevant instruments (majority rule fails!),
    #       but plurality holds: 4 > max(2, 2, 1) = 2.
    gamma_true = [1.2, -1.0, 1.5, 1.1, 1.0, 1.2, -1.0, 1.0, 1.0, 0.0, 0.0, 0.0]
    pi_true = [
        0.0, 0.0, 0.0, 0.0,
        1.5 * 1.0, 1.5 * 1.2,
        -1.2 * (-1.0), -1.2 * 1.0,
        3.0 * 1.0,
        0.0, 0.0, 0.0,
    ]
    # Small finite-sample estimation noise (n = 5000)
    noise_gamma = [0.004, -0.003, 0.002, -0.004, 0.003, -0.002, 0.003, 0.001, -0.002, 0.012, -0.015, 0.009]
    noise_Gamma = [-0.005, 0.004, 0.006, -0.003, 0.005, -0.004, 0.002, -0.005, 0.003, -0.011, 0.014, -0.008]

    p_z = len(gamma_true)
    se = 1.0 / math.sqrt(5000.0)
    gamma_hat = [g + ng for g, ng in zip(gamma_true, noise_gamma)]
    Gamma_hat = [beta_true * g + p + nG for g, p, nG in zip(gamma_true, pi_true, noise_Gamma)]

    # Stage 1: First-stage hard thresholding (Eq. 5-6)
    tau_1 = se * math.sqrt(2.01 * math.log(p_z))
    s_hat = [j for j in range(p_z) if abs(gamma_hat[j]) >= tau_1]
    assert s_hat == list(range(9)), f"Expected relevant set 0..8, got {s_hat}"

    # Stage 2: Pairwise invalidity thresholding & symmetric voting matrix (Eq. 7-11)
    m_rel = len(s_hat)
    vote_matrix = [[0] * m_rel for _ in range(m_rel)]
    for idx_j, j in enumerate(s_hat):
        beta_j = Gamma_hat[j] / gamma_hat[j]
        for idx_k, k in enumerate(s_hat):
            pi_k_given_j = Gamma_hat[k] - beta_j * gamma_hat[k]
            se_kj = se * math.sqrt(1.0 + (gamma_hat[k] / gamma_hat[j]) ** 2)
            tau_2_kj = se_kj * math.sqrt(2.01 * math.log(m_rel))
            if abs(pi_k_given_j) <= tau_2_kj:
                vote_matrix[idx_k][idx_j] = 1

    # Symmetrize voting matrix (Eq. 11)
    sym_votes = [
        [1 if (vote_matrix[a][b] == 1 and vote_matrix[b][a] == 1) else 0 for b in range(m_rel)]
        for a in range(m_rel)
    ]
    vote_counts = [sum(sym_votes[k][j] for k in range(m_rel)) for j in range(m_rel)]
    max_votes = max(vote_counts)
    v_hat_winners = [s_hat[j] for j in range(m_rel) if vote_counts[j] == max_votes]
    assert v_hat_winners == [0, 1, 2, 3], f"Expected valid plurality [0,1,2,3], got {v_hat_winners}"

    # Post-voting two-stage estimator (Eq. 12) vs naive all-relevant TSLS
    num_tsht = sum(Gamma_hat[j] * gamma_hat[j] for j in v_hat_winners)
    den_tsht = sum(gamma_hat[j] ** 2 for j in v_hat_winners)
    beta_tsht = num_tsht / den_tsht

    num_naive = sum(Gamma_hat[j] * gamma_hat[j] for j in s_hat)
    den_naive = sum(gamma_hat[j] ** 2 for j in s_hat)
    beta_naive = num_naive / den_naive

    err_tsht = abs(beta_tsht - beta_true)
    err_naive = abs(beta_naive - beta_true)
    assert err_tsht < 0.02 and err_naive > 0.35
    print(
        f"[PASS] Round 832 TSHT Plurality Voting verified: S_hat={s_hat}, S_hat_V={v_hat_winners} (4/9 < 50%), "
        f"|beta_TSHT - beta*|={err_tsht:.4f} << |beta_naive - beta*|={err_naive:.4f}"
    )


if __name__ == "__main__":
    run_tsht_plurality_voting()
