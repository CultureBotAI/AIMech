#!/usr/bin/env python3
"""Constructed boundary verification for Quasi-Global Momentum / QG-DSGDm (Lin et al., ICML 2021).

Verifies:
1. Single-worker equivalence to Quasi-Hyperbolic Momentum (QHM) (Section 4.2 & Appendix B.3.1):
   When W = [1] (n=1), QG-DSGDm iterates
     x^(t+1) = x^(t) - eta * (beta * m^(t-1) + g^(t))
     m^(t)   = mu * m^(t-1) + (1 - mu) * (x^(t) - x^(t+1)) / eta
   match QHM with m_hat^(t) = m^(t)/(1-mu), beta_hat = mu + (1-mu)*beta, and
     x^(t+1) = x^(t) - eta * ((1 - mu/beta_hat)*m_hat^(t) + (mu/beta_hat)*g^(t)).
2. Faster average-consensus contraction (Section 4.1, Equation 4):
   X^(t+1) = W * (X^(t) - beta * M^(t-1)), M^(t) = mu * M^(t-1) + (1 - mu)*(X^(t) - X^(t+1))
   reduces consensus distance ||X^(t) - X_bar^(t)||_F faster than plain gossip X^(t+1) = W * X^(t).
3. Stabilization under heterogeneous local gradients (Section 3.2, Algorithm 1):
   QG-DSGDm suppresses the local-momentum oscillation of DSGDm on heterogeneous objectives.
"""

import math


def verify_qg_momentum_boundaries():
    # 1. Verify exact algebraic equivalence between single-worker QG-DSGDm and QHM (Appendix B.3.1, Eq. 5)
    eta = 0.05
    beta = 0.9
    mu = 0.9
    beta_hat = mu + (1.0 - mu) * beta
    grads = [1.4, -0.8, 0.5, 1.1, -0.3, 0.2, -0.6, 0.9]

    # Run single-worker QG-DSGDm
    x_qg = 2.5
    m_qg = 0.0
    traj_qg = []
    for g in grads:
        x_next = x_qg - eta * (beta * m_qg + g)
        m_qg = mu * m_qg + (1.0 - mu) * (x_qg - x_next) / eta
        x_qg = x_next
        traj_qg.append(x_qg)

    # Run QHM reparameterization (Eq. 5 on page 19)
    x_qhm = 2.5
    m_hat = 0.0
    traj_qhm = []
    for g in grads:
        m_hat = beta_hat * m_hat + g
        x_qhm = x_qhm - eta * ((1.0 - mu / beta_hat) * m_hat + (mu / beta_hat) * g)
        traj_qhm.append(x_qhm)

    for t, (xq, xh) in enumerate(zip(traj_qg, traj_qhm)):
        assert abs(xq - xh) < 1e-14, f"QG-SGDm vs QHM mismatch at step {t}: {xq} vs {xh}"

    # 2. Verify faster average consensus contraction on a 10-node ring (Section 4.1, Eq. 4)
    n = 10
    W = [[0.0] * n for _ in range(n)]
    for i in range(n):
        W[i][i] = 0.5
        W[i][(i - 1) % n] = 0.25
        W[i][(i + 1) % n] = 0.25

    x0 = [math.sin(2.0 * math.pi * i / n) * 5.0 for i in range(n)]
    x_simple = list(x0)
    x_qg_cons = list(x0)
    m_qg_cons = [0.0] * n
    beta_c = 0.5
    mu_c = 0.5

    for _ in range(25):
        x_simple = [sum(W[i][j] * x_simple[j] for j in range(n)) for i in range(n)]
        pre_step = [x_qg_cons[j] - beta_c * m_qg_cons[j] for j in range(n)]
        x_qg_next = [sum(W[i][j] * pre_step[j] for j in range(n)) for i in range(n)]
        m_qg_cons = [
            mu_c * m_qg_cons[i] + (1.0 - mu_c) * (x_qg_cons[i] - x_qg_next[i])
            for i in range(n)
        ]
        x_qg_cons = x_qg_next

    err_simple = math.sqrt(sum(v * v for v in x_simple) / n)
    err_qg_cons = math.sqrt(sum(v * v for v in x_qg_cons) / n)
    assert err_qg_cons < err_simple, f"Expected QG consensus error < simple gossip: {err_qg_cons} vs {err_simple}"

    # 3. Verify lower consensus drift on heterogeneous 2-worker 2D problem (Section 3.2, Figure 2 setup)
    # Worker 0 optimum at (0, 5), Worker 1 optimum at (4, 0) -> global optimum at (2, 2.5)
    # On sparse gossip matrix W = [[0.85, 0.15], [0.15, 0.85]]
    W2 = [[0.85, 0.15], [0.15, 0.85]]
    targets = [(0.0, 5.0), (4.0, 0.0)]

    def run_2d_het(use_qg, steps=120, lr=0.04, mom=0.9):
        pos = [[0.0, 0.0], [0.0, 0.0]]
        buf = [[0.0, 0.0], [0.0, 0.0]]
        for _ in range(steps):
            half = [[0.0, 0.0], [0.0, 0.0]]
            for i in range(2):
                g0 = pos[i][0] - targets[i][0]
                g1 = pos[i][1] - targets[i][1]
                if not use_qg:
                    buf[i][0] = mom * buf[i][0] + g0
                    buf[i][1] = mom * buf[i][1] + g1
                    m0, m1 = buf[i][0], buf[i][1]
                else:
                    m0 = mom * buf[i][0] + g0
                    m1 = mom * buf[i][1] + g1
                half[i][0] = pos[i][0] - lr * m0
                half[i][1] = pos[i][1] - lr * m1
            nxt = [
                [W2[i][0] * half[0][0] + W2[i][1] * half[1][0], W2[i][0] * half[0][1] + W2[i][1] * half[1][1]]
                for i in range(2)
            ]
            if use_qg:
                for i in range(2):
                    d0 = (pos[i][0] - nxt[i][0]) / lr
                    d1 = (pos[i][1] - nxt[i][1]) / lr
                    buf[i][0] = mom * buf[i][0] + (1.0 - mom) * d0
                    buf[i][1] = mom * buf[i][1] + (1.0 - mom) * d1
            pos = nxt
        # Disagreement between the two workers
        disagree = math.hypot(pos[0][0] - pos[1][0], pos[0][1] - pos[1][1])
        return disagree

    disagree_local_mom = run_2d_het(use_qg=False)
    disagree_qg_mom = run_2d_het(use_qg=True)
    assert disagree_qg_mom < disagree_local_mom, (
        f"Expected QG-DSGDm worker disagreement < local-momentum DSGDm: "
        f"{disagree_qg_mom} vs {disagree_local_mom}"
    )

    print(
        f"[PASS] Quasi-Global Momentum boundaries verified: QHM_diff<1e-14, "
        f"cons_qg={err_qg_cons:.4f}<cons_simple={err_simple:.4f}, "
        f"disagree_qg={disagree_qg_mom:.4f}<disagree_local={disagree_local_mom:.4f}"
    )


if __name__ == "__main__":
    verify_qg_momentum_boundaries()
