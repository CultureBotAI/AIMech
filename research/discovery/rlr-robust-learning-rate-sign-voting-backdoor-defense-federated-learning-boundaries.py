#!/usr/bin/env python3
"""Constructed boundary verification for Round 529: Robust Learning Rate (RLR, Ozdayi et al., AAAI 2021).

Verifies:
1. Equations (5)-(6) & Appendix D.1 Equations (8)-(9): Per-dimension server learning rate
   eta_{theta, i} = +eta if |sum_{k in S_t} sgn(Delta_{t,i}^k)| >= theta else -eta,
   represented via diagonal operator 2*I_t - I with unit operator norm ||2*I_t - I||_2 = 1.
2. Backdoor vs. Main Task separation (Section 3): When K=10 agents contain K_adv=2 corrupt
   agents pushing a backdoor coordinate (dim 1) with large boosted magnitude while honest
   agents have zero-mean symmetric noise on dim 1 and coherent consensus on main-task
   coordinate (dim 0), standard FedAvg moves strongly toward the backdoor target w_adv on
   dim 1, whereas RLR with threshold theta=4 (> K_adv=2) flips the learning rate on dim 1
   to -eta (ascent on backdoor loss) while keeping +eta on dim 0 (descent on main task).
"""


def sgn(x):
    if x > 0.0:
        return 1
    if x < 0.0:
        return -1
    return 0


def rlr_step(w, updates, eta, theta):
    """Equations (5)-(6): Dimension-wise sign-voting learning rate adjustment."""
    K = len(updates)
    d = len(w)
    avg_update = [sum(updates[k][i] for k in range(K)) / K for i in range(d)]
    eta_vec = []
    for i in range(d):
        vote_sum = abs(sum(sgn(updates[k][i]) for k in range(K)))
        eta_i = eta if vote_sum >= theta else -eta
        eta_vec.append(eta_i)
    w_next = [w[i] + eta_vec[i] * avg_update[i] for i in range(d)]
    return w_next, eta_vec, avg_update


def main():
    # K = 10 total agents: 8 honest agents, 2 backdoor attackers (F = 0.2), threshold theta = 4
    # Dimension 0: main task (w_hon^*[0] = +1.0); all 8 honest agents + 2 attackers push +0.5
    # Dimension 1: backdoor trojan feature (w_adv^*[1] = +2.0, w_hon^*[1] = 0.0);
    #   8 honest agents have zero-mean +/-0.05 updates (4 positive, 4 negative -> sign sum = 0),
    #   while 2 attackers boost backdoor update +3.0 each (sign sum = +2).
    # Total sign sum on dim 0 is |8*(+1) + 2*(+1)| = 10 >= theta=4 -> eta_{theta,0} = +eta.
    # Total sign sum on dim 1 is |4*(+1) + 4*(-1) + 2*(+1)| = 2 < theta=4 -> eta_{theta,1} = -eta!
    updates = []
    for k in range(8):
        noise_sign = 1.0 if (k % 2 == 0) else -1.0
        updates.append([0.5, 0.05 * noise_sign])
    for _ in range(2):
        updates.append([0.5, 3.0])

    w0 = [0.0, 0.0]
    eta = 1.0
    theta = 4

    # Standard FedAvg (equivalent to theta=0)
    w_fedavg, _, avg_upd = rlr_step(w0, updates, eta=eta, theta=0)
    # RLR with theta=4
    w_rlr, eta_vec, _ = rlr_step(w0, updates, eta=eta, theta=theta)

    # 1. Verify operator norm ||2*I_t - I||_2 = 1 (all diagonal entries in {+1, -1})
    diag_op = [e / eta for e in eta_vec]
    assert all(abs(d_i) == 1.0 for d_i in diag_op)
    assert diag_op == [1.0, -1.0]

    # 2. Both FedAvg and RLR make identical progress +0.5 toward w_hon^* on main-task dim 0
    assert abs(w_fedavg[0] - 0.5) < 1e-12 and abs(w_rlr[0] - 0.5) < 1e-12

    # 3. On backdoor dim 1, FedAvg moves +0.60 toward w_adv^*, whereas RLR moves -0.60 away from w_adv^*!
    assert w_fedavg[1] > 0.5 and w_rlr[1] == -w_fedavg[1] < -0.5

    print(
        f"[PASS] Round 529 RLR (Ozdayi et al. 2021): "
        f"diag(2*I_t-I)={diag_op}, main_dim_step={w_rlr[0]:.2f}, "
        f"backdoor_dim_fedavg=+{w_fedavg[1]:.2f} vs backdoor_dim_rlr={w_rlr[1]:.2f}"
    )


if __name__ == "__main__":
    main()
