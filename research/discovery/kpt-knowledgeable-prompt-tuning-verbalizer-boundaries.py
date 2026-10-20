#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 723: KPT (Hu et al., ACL 2022)."""

import math


def verify_kpt() -> None:
    # 1. Contextualized prior estimation over unlabeled support set C_tilde (Eq. 3):
    # P_D(v) = (1 / |C_tilde|) * sum_{x in C_tilde} P_M([MASK] = v | x_p)
    q_v0_cls1 = [0.40, 0.35, 0.10, 0.12]  # anchor class 1 ("science")
    q_v0_cls2 = [0.12, 0.10, 0.35, 0.40]  # anchor class 2 ("sports")
    q_v1 = [0.38, 0.32, 0.09, 0.11]       # "physics" (belongs to class 1)
    q_v2 = [0.001, 0.001, 0.001, 0.001]   # rare KB word
    q_v3 = [0.15, 0.15, 0.35, 0.35]       # noisy word assigned to class 1 but closer to class 2

    def prior(q: list[float]) -> float:
        return sum(q) / len(q)

    # Frequency refinement filters out lower-prior rare words (v2)
    assert prior(q_v1) > 0.20 and prior(q_v2) < 0.01

    # 2. Relevance refinement (TF-IDF style cosine relevance ratio, Eq. 5-6):
    # r(v, y) = cos(q^v, q^{v_0}), R(v) = r(v, f(v)) * (|Y| - 1) / sum_{y != f(v)} r(v, y)
    def cos_sim(a: list[float], b: list[float]) -> float:
        num = sum(x * y for x, y in zip(a, b))
        den = math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b))
        return num / den

    r_v1 = cos_sim(q_v1, q_v0_cls1) / cos_sim(q_v1, q_v0_cls2)
    r_v3 = cos_sim(q_v3, q_v0_cls1) / cos_sim(q_v3, q_v0_cls2)
    assert r_v1 > 1.5  # retained (R(v) >= 1)
    assert r_v3 < 1.0  # filtered out (R(v) < 1)

    # 3. Contextualized Calibration (Eq. 7) & Learnable Refinement (Eq. 8, 10-11):
    # P_tilde([MASK]=v | x_p) proportional to P_M([MASK]=v | x_p) / P_D(v)
    p_raw = {"science": 0.20, "physics": 0.15}
    p_prior = {"science": 0.25, "physics": 0.10}
    p_cal = {w: p_raw[w] / p_prior[w] for w in p_raw}
    assert p_cal["physics"] > p_cal["science"]

    # Learnable softmax weights alpha_v = exp(w_v) / sum_{u in V_y} exp(w_u)
    w_learn = {"science": 0.5, "physics": 1.2}
    z_w = sum(math.exp(val) for val in w_learn.values())
    alpha = {u: math.exp(val) / z_w for u, val in w_learn.items()}
    assert math.isclose(sum(alpha.values()), 1.0, rel_tol=1e-12)
    print("KPT verification passed.")


if __name__ == "__main__":
    verify_kpt()
