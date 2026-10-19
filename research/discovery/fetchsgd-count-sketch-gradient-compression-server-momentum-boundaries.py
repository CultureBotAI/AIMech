#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 409:
FetchSGD: Count-Sketch Gradient Compression with Server Momentum and Error Accumulation
(Rothchild et al., ICML 2020, PMLR 119:8253-8265, arXiv:2007.07682).
"""

import random
import statistics


class CountSketch:
    """Algorithm 2 (Charikar et al. 2002; Rothchild et al. 2020 Appendix C):
    Linear sketching operator S: R^d -> R^{r x c} with median-of-rows unsketching U.
    """

    def __init__(self, d, r, c, seed=409):
        self.d = d
        self.r = r
        self.c = c
        rng = random.Random(seed)
        self.hb = [[rng.randrange(c) for _ in range(d)] for _ in range(r)]
        self.hs = [[rng.choice((-1.0, 1.0)) for _ in range(d)] for _ in range(r)]

    def sketch(self, v):
        table = [[0.0] * self.c for _ in range(self.r)]
        for row in range(self.r):
            hb_r = self.hb[row]
            hs_r = self.hs[row]
            t_r = table[row]
            for i, val in enumerate(v):
                if val != 0.0:
                    t_r[hb_r[i]] += hs_r[i] * val
        return table

    def unsketch(self, table):
        out = [0.0] * self.d
        for i in range(self.d):
            ests = [self.hs[row][i] * table[row][self.hb[row][i]] for row in range(self.r)]
            out[i] = statistics.median(ests)
        return out

    @staticmethod
    def add(S1, S2, a=1.0, b=1.0):
        return [
            [a * S1[row][col] + b * S2[row][col] for col in range(len(S1[0]))]
            for row in range(len(S1))
        ]


def top_k_vec(v, k):
    idx = sorted(range(len(v)), key=lambda i: abs(v[i]), reverse=True)[:k]
    keep = set(idx)
    return [v[i] if i in keep else 0.0 for i in range(len(v))]


def main():
    rng = random.Random(409)
    d = 64
    cs = CountSketch(d=d, r=9, c=48, seed=4090)

    # 1. Verify exact linearity of Count Sketch: S(g1 + g2) == S(g1) + S(g2)
    # and server momentum + error accumulation commutativity:
    # S_u^t = rho S_u^{t-1} + S^t == S(u^t) and S_e^{t+1} = eta S_u^t + S_e^t - S(Delta^t) == S(e^{t+1})
    u_vec = [0.0] * d
    e_vec = [0.0] * d
    S_u = cs.sketch(u_vec)
    S_e = cs.sketch(e_vec)
    rho = 0.9
    eta = 0.1
    k = 4

    w_vec = [rng.gauss(0.0, 1.0) for _ in range(d)]
    # Virtual sequence (Appendix B.1): w_tilde^t = w^t - e^t - (eta * rho / (1 - rho)) * u^{t-1}
    # Satisfies w_tilde^t = w_tilde^{t-1} - (eta / (1 - rho)) * g^{t-1}
    w_tilde_prev = [w_vec[i] for i in range(d)]
    max_linearity_err = 0.0
    max_virtual_seq_err = 0.0

    for _ in range(15):
        client_grads = [[rng.gauss(0.0, 1.0) for _ in range(d)] for _ in range(4)]
        g_avg = [sum(client_grads[w][i] for w in range(4)) / 4.0 for i in range(d)]

        S_t = [[0.0] * cs.c for _ in range(cs.r)]
        for cg in client_grads:
            S_t = CountSketch.add(S_t, cs.sketch(cg), 1.0, 0.25)

        u_vec = [rho * u_vec[i] + g_avg[i] for i in range(d)]
        S_u = CountSketch.add(S_u, S_t, rho, 1.0)
        S_u_from_vec = cs.sketch(u_vec)

        q_vec = [eta * u_vec[i] + e_vec[i] for i in range(d)]
        S_q = CountSketch.add(S_u, S_e, eta, 1.0)
        Delta_t = top_k_vec(cs.unsketch(S_q), k)

        e_vec = [q_vec[i] - Delta_t[i] for i in range(d)]
        S_e = CountSketch.add(S_q, cs.sketch(Delta_t), 1.0, -1.0)
        S_e_from_vec = cs.sketch(e_vec)

        w_vec = [w_vec[i] - Delta_t[i] for i in range(d)]

        err_u = max(abs(S_u[r][c] - S_u_from_vec[r][c]) for r in range(cs.r) for c in range(cs.c))
        err_e = max(abs(S_e[r][c] - S_e_from_vec[r][c]) for r in range(cs.r) for c in range(cs.c))
        max_linearity_err = max(max_linearity_err, err_u, err_e)

        w_tilde_curr = [
            w_vec[i] - e_vec[i] - (eta * rho / (1.0 - rho)) * u_vec[i]
            for i in range(d)
        ]
        w_tilde_expected = [
            w_tilde_prev[i] - (eta / (1.0 - rho)) * g_avg[i]
            for i in range(d)
        ]
        v_err = max(abs(w_tilde_curr[i] - w_tilde_expected[i]) for i in range(d))
        max_virtual_seq_err = max(max_virtual_seq_err, v_err)
        w_tilde_prev = w_tilde_curr

    assert max_linearity_err < 1e-13
    assert max_virtual_seq_err < 1e-13

    # 2. Verify one-shot stateless client regime (Scenario 2 / Section 3.2):
    # Suppose 6 signal coordinates (0..5) have true target 1.0, while each one-shot client has 2 local noise spikes
    # of magnitude 1.5 > 1.0 on disjoint background coordinates (which cancel or spread across clients).
    # One-shot local Top-2 picks the 2 local spikes and discards the 6 signal coordinates forever,
    # whereas FetchSGD accumulates the sketched gradients on the server and converges on the 6 signal coordinates.
    w_fetch = [0.0] * d
    w_local_topk = [0.0] * d
    True_target = [1.0 if i < 6 else 0.0 for i in range(d)]
    S_e_server = [[0.0] * cs.c for _ in range(cs.r)]
    eta_sim = 0.25

    for t in range(40):
        S_round = [[0.0] * cs.c for _ in range(cs.r)]
        local_topk_sum = [0.0] * d
        base_coord = 6 + ((2 * t) % (d - 8))
        # Paired clients have opposite-sign local spikes on coordinates base_coord, base_coord+1
        for c_idx in range(4):
            g_c = [w_fetch[i] - True_target[i] for i in range(d)]
            g_c_local = [w_local_topk[i] - True_target[i] for i in range(d)]
            sgn = 1.0 if (c_idx % 2 == 0) else -1.0
            g_c[base_coord] += 1.5 * sgn
            g_c[base_coord + 1] -= 1.5 * sgn
            g_c_local[base_coord] += 1.5 * sgn
            g_c_local[base_coord + 1] -= 1.5 * sgn

            S_round = CountSketch.add(S_round, cs.sketch(g_c), 1.0, 0.25)
            tk_local = top_k_vec([eta_sim * x for x in g_c_local], 2)
            for i in range(d):
                local_topk_sum[i] += 0.25 * tk_local[i]

        S_e_server = CountSketch.add(S_e_server, S_round, 1.0, eta_sim)
        Delta = top_k_vec(cs.unsketch(S_e_server), 2)
        S_e_server = CountSketch.add(S_e_server, cs.sketch(Delta), 1.0, -1.0)
        w_fetch = [w_fetch[i] - Delta[i] for i in range(d)]
        w_local_topk = [w_local_topk[i] - local_topk_sum[i] for i in range(d)]

    err_fetch = sum((w_fetch[i] - True_target[i]) ** 2 for i in range(6))
    err_local_topk = sum((w_local_topk[i] - True_target[i]) ** 2 for i in range(6))
    assert err_fetch < 0.01 and err_local_topk >= 5.99, (
        f"Expected err_fetch < 0.01 and err_local_topk >= 5.99, got {err_fetch}, {err_local_topk}"
    )

    print(
        f"[PASS] Round 409 FetchSGD (Rothchild et al. 2020): "
        f"lin_err={max_linearity_err:.2e}, virt_seq_err={max_virtual_seq_err:.2e}, "
        f"err_fetch={err_fetch:.4e}<<err_local_topk={err_local_topk:.4f}"
    )


if __name__ == "__main__":
    main()
