#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 725: DART (Zhang et al., ICLR 2022)."""

import math


def verify_dart() -> None:
    # 1. Joint differentiable template h_{0:m} and continuous pseudo-label tokens M(Y_j) = {h_{m+j}}
    # with auxiliary Fluency Constraint Objective (Eq. 4-10):
    # L = L_C + lambda * L_F, where L_C = CE(g(y | X_prompt)) and L_F = sum_{m in M} BCE(h(x^m | x', y))
    class_logits = [2.2, -0.8, -0.5]
    z_c = sum(math.exp(v) for v in class_logits)
    p_c = [math.exp(v) / z_c for v in class_logits]
    l_c = -math.log(p_c[0])

    masked_tok_logits = [1.9, 0.1, -0.4, -1.0]
    z_f = sum(math.exp(v) for v in masked_tok_logits)
    h_xm = math.exp(masked_tok_logits[0]) / z_f
    l_f = -math.log(h_xm)
    lam = 0.5
    total_loss = l_c + lam * l_f
    assert total_loss > l_c > 0.0

    # 2. Discriminative representation ratio R_D = D_bar_intra / D_bar_inter (Eq. 11):
    # Differentiable prompt optimization yields more compact intra-class clusters (smaller R_D) than fixed prompts
    def euclid(a: list[float], b: list[float]) -> float:
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

    def compute_r_d(clusters: list[list[list[float]]]) -> float:
        c_num = len(clusters)
        d_intra = 0.0
        for hc in clusters:
            nc = len(hc)
            d_intra += sum(euclid(hc[i], hc[j]) for i in range(nc) for j in range(nc)) / (nc * nc)
        d_intra /= c_num
        d_inter = 0.0
        for c1 in range(c_num):
            for c2 in range(c_num):
                if c1 != c2:
                    hc1, hc2 = clusters[c1], clusters[c2]
                    d_inter += sum(euclid(u, v) for u in hc1 for v in hc2) / (len(hc1) * len(hc2))
        d_inter /= c_num * (c_num - 1)
        return d_intra / d_inter

    fixed_clusters = [[[0.0, 0.0], [0.8, 0.6]], [[2.0, 2.0], [2.8, 1.4]]]
    diff_clusters = [[[0.0, 0.0], [0.2, 0.1]], [[2.5, 2.5], [2.6, 2.4]]]
    assert compute_r_d(diff_clusters) < compute_r_d(fixed_clusters)
    print("DART verification passed.")


if __name__ == "__main__":
    verify_dart()
