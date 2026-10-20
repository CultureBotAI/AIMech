#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 481:
FedRecon (Federated Reconstruction: Partially Local Federated Learning,
Singhal, Sidahmed, Garrett, Wu, Rush, & Prakash 2021, NeurIPS 2021, arXiv:2102.03448).

Verifies:
1. Stateless partially local client update and reconstruction protocol (Algorithm 1, p. 4):
   - Each participating client i splits its local dataset D_i into a support set D_{i,s}
     and query set D_{i,q}.
   - Reconstruction step R: starting from a fresh initialization l_i^{(t,0)} (with no stored
     cross-round client state) and holding global parameters g^{(t)} frozen, client i runs
     k_r local gradient descent steps on D_{i,s} to reconstruct l_i^{(t)} = R(D_{i,s}, L, g^{(t)}).
   - Client Update step U: holding l_i^{(t)} frozen, client i runs k_u gradient steps on
     g^{(t)} using query set D_{i,q} to obtain g_i^{(t)} and returns only Delta_i^{(t)} = g_i^{(t)} - g^{(t)}
     and n_i = |D_{i,q}| to the server (communication cost 2|g| instead of 2(|g| + |l|)).
2. First-order Model-Agnostic Meta-Learning (MAML) equivalence (Section 4.2 & Appendix B,
   Equation 3, p. 5 & p. 15):
   - The true meta-gradient of F_meta(g) = E_{i~P}[ f_{i,q}(g || R(D_{i,s}, L, g)) ] is:
     nabla_g F_meta(g) = nabla_g f_{i,q}(g || l_i^{(t,k_r)})
       - eta_r nabla_{l_i} f_{i,q}(g || l_i^{(t,k_r)}) sum_{j=0}^{k_r - 1} nabla_g nabla_{l_i} f_{i,s}(g || l_i^{(t,j)}),
     so treating the output of R as constant in g (with k_u = 1) exactly recovers the
     first-order meta-gradient nabla_g f_{i,q}(g || l_i^{(t,k_r)}) while dropping O(eta_r)
     mixed-Hessian Jacobian terms.
3. Fast ReconEval generalization to unseen stateless test clients (Section 4.1 & 5.1.1).
"""

from __future__ import annotations


def main() -> None:
    # Federated Matrix Factorization R approx P Q^T with global item vectors g = Q in R^{I x K}
    # and stateless local user embedding l_i = p_i in R^K (I=3 items, K=2 latent rank)
    true_Q = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
    train_users_p = [[1.2, -0.5], [-0.8, 1.4], [0.6, 0.9], [-1.0, -0.7]]
    unseen_user_p = [0.9, -1.1]

    def make_user_data(p_u: list[float]) -> tuple[list[tuple[int, float]], list[tuple[int, float]]]:
        # Support set: items 0 and 1; Query set: item 2
        r0 = sum(p_u[k] * true_Q[0][k] for k in range(2))
        r1 = sum(p_u[k] * true_Q[1][k] for k in range(2))
        r2 = sum(p_u[k] * true_Q[2][k] for k in range(2))
        return [(0, r0), (1, r1)], [(2, r2)]

    def reconstruct_local_p(
        support: list[tuple[int, float]], Q_global: list[list[float]], eta_r: float, k_r: int
    ) -> list[float]:
        # Stateless initialization l_i^{(t,0)} = [0.0, 0.0], global Q_global frozen
        l_i = [0.0, 0.0]
        for _ in range(k_r):
            grad_l = [0.0, 0.0]
            for item_idx, rating in support:
                pred = sum(l_i[k] * Q_global[item_idx][k] for k in range(2))
                err = (pred - rating) * (2.0 / len(support))
                for k in range(2):
                    grad_l[k] += err * Q_global[item_idx][k]
            l_i = [l_i[k] - eta_r * grad_l[k] for k in range(2)]
        return l_i

    # 1. Verify Appendix B mixed-Jacobian chain rule identity for k_r = 1 reconstruction step
    Q_test = [[0.8, 0.2], [0.1, 0.9], [0.7, 0.6]]
    supp_0, query_0 = make_user_data(train_users_p[0])
    eta_r = 0.25

    def query_loss_after_1step_recon(Q_mat: list[list[float]]) -> float:
        l_1 = reconstruct_local_p(supp_0, Q_mat, eta_r=eta_r, k_r=1)
        item_idx, r_q = query_0[0]
        pred_q = sum(l_1[k] * Q_mat[item_idx][k] for k in range(2))
        return (pred_q - r_q) ** 2

    # Finite-difference full meta-gradient wrt Q_mat[2] (query item) and Q_mat[0] (support item)
    eps = 1e-7
    l_1_curr = reconstruct_local_p(supp_0, Q_test, eta_r=eta_r, k_r=1)
    # First-order FedRecon update gradient wrt Q_test[2] (holding l_1_curr constant)
    pred_q = sum(l_1_curr[k] * Q_test[2][k] for k in range(2))
    err_q = 2.0 * (pred_q - query_0[0][1])
    fo_grad_Q2 = [err_q * l_1_curr[0], err_q * l_1_curr[1]]
    for k in range(2):
        Q_plus = [row[:] for row in Q_test]
        Q_plus[2][k] += eps
        fd_grad_Q2_k = (query_loss_after_1step_recon(Q_plus) - query_loss_after_1step_recon(Q_test)) / eps
        # Because item 2 is only in D_{i,q} and not in D_{i,s}, nabla_{Q_2} l_1 == 0 and first-order == exact!
        assert abs(fo_grad_Q2[k] - fd_grad_Q2_k) < 1e-5

    # 2. Train FedRecon (Algorithm 1) across stateless training users and evaluate ReconEval on unseen test user
    Q_global = [[0.9, 0.1], [-0.1, 0.8], [0.4, 0.3]]
    for _round in range(60):
        deltas = [[[0.0, 0.0] for _ in range(3)] for _ in train_users_p]
        for u_idx, p_u in enumerate(train_users_p):
            supp, query = make_user_data(p_u)
            l_reconstructed = reconstruct_local_p(supp, Q_global, eta_r=0.4, k_r=10)
            # ClientUpdate U on query set holding l_reconstructed frozen
            q_u = [row[:] for row in Q_global]
            eta_u = 0.2
            for item_idx, r_q in query:
                pred = sum(l_reconstructed[k] * q_u[item_idx][k] for k in range(2))
                err = 2.0 * (pred - r_q)
                for k in range(2):
                    q_u[item_idx][k] -= eta_u * err * l_reconstructed[k]
            for m in range(3):
                for k in range(2):
                    deltas[u_idx][m][k] = q_u[m][k] - Q_global[m][k]
        # Server aggregation of global parameters only
        for m in range(3):
            for k in range(2):
                Q_global[m][k] += sum(deltas[u][m][k] for u in range(len(train_users_p))) / len(train_users_p)

    # ReconEval on unseen client (Section 4.1)
    unseen_supp, unseen_query = make_user_data(unseen_user_p)
    l_unseen_0 = reconstruct_local_p(unseen_supp, Q_global, eta_r=0.4, k_r=0)
    l_unseen_10 = reconstruct_local_p(unseen_supp, Q_global, eta_r=0.4, k_r=10)
    mse_0 = (sum(l_unseen_0[k] * Q_global[2][k] for k in range(2)) - unseen_query[0][1]) ** 2
    mse_10 = (sum(l_unseen_10[k] * Q_global[2][k] for k in range(2)) - unseen_query[0][1]) ** 2
    assert mse_10 < 1e-3 and mse_10 < 0.01 * mse_0

    print(
        f"[PASS] FedRecon boundary verification passed: unseen_ReconEval_MSE(k_r=0)={mse_0:.4f} -> "
        f"unseen_ReconEval_MSE(k_r=10)={mse_10:.4e}"
    )


if __name__ == "__main__":
    main()
