#!/usr/bin/env python3
"""Constructed boundary verification for MAD-X and Invertible Adapters (Pfeiffer et al., EMNLP 2020)."""

from __future__ import annotations

import math
import random


def relu(vec: list[float]) -> list[float]:
    return [x if x > 0.0 else 0.0 for x in vec]


def matvec(mat: list[list[float]], vec: list[float]) -> list[float]:
    return [sum(row[j] * vec[j] for j in range(len(vec))) for row in mat]


def bottleneck(x: list[float], d_mat: list[list[float]], u_mat: list[list[float]]) -> list[float]:
    return matvec(u_mat, relu(matvec(d_mat, x)))


def main() -> int:
    rng = random.Random(20260713)
    h = 16
    half_h = h // 2
    quarter_h = h // 4

    # 1. Verify NICE-coupled Invertible Adapter exact bijectivity (Eqs. 3-5)
    # F, G: R^{h/2} -> R^{h/4} -> R^{h/2} with ReLU
    d_f = [[rng.gauss(0.0, 0.5) for _ in range(half_h)] for _ in range(quarter_h)]
    u_f = [[rng.gauss(0.0, 0.5) for _ in range(quarter_h)] for _ in range(half_h)]
    d_g = [[rng.gauss(0.0, 0.5) for _ in range(half_h)] for _ in range(quarter_h)]
    u_g = [[rng.gauss(0.0, 0.5) for _ in range(quarter_h)] for _ in range(half_h)]

    def a_inv_forward(e: list[float]) -> list[float]:
        e1 = e[:half_h]
        e2 = e[half_h:]
        f_e2 = bottleneck(e2, d_f, u_f)
        o1 = [f_e2[i] + e1[i] for i in range(half_h)]
        g_o1 = bottleneck(o1, d_g, u_g)
        o2 = [g_o1[i] + e2[i] for i in range(half_h)]
        return o1 + o2

    def a_inv_inverse(o: list[float]) -> list[float]:
        o1 = o[:half_h]
        o2 = o[half_h:]
        g_o1 = bottleneck(o1, d_g, u_g)
        e2 = [o2[i] - g_o1[i] for i in range(half_h)]
        f_e2 = bottleneck(e2, d_f, u_f)
        e1 = [o1[i] - f_e2[i] for i in range(half_h)]
        return e1 + e2

    max_inv_err = 0.0
    for _ in range(25):
        e = [rng.gauss(0.0, 1.0) for _ in range(h)]
        o = a_inv_forward(e)
        e_rec = a_inv_inverse(o)
        err = max(abs(e[i] - e_rec[i]) for i in range(h))
        if err > max_inv_err:
            max_inv_err = err
    assert max_inv_err < 1e-15

    # 2. Verify stacked Language Adapter (Eq. 1) and Task Adapter (Eq. 2) with shared FFN residual r_l
    d_la = h // 2
    d_ta = h // 4
    d_lang_src = [[rng.gauss(0.0, 0.4) for _ in range(h)] for _ in range(d_la)]
    u_lang_src = [[rng.gauss(0.0, 0.4) for _ in range(d_la)] for _ in range(h)]
    d_lang_trg = [[rng.gauss(0.0, 0.4) for _ in range(h)] for _ in range(d_la)]
    u_lang_trg = [[rng.gauss(0.0, 0.4) for _ in range(d_la)] for _ in range(h)]
    d_task = [[rng.gauss(0.0, 0.4) for _ in range(h)] for _ in range(d_ta)]
    u_task = [[rng.gauss(0.0, 0.4) for _ in range(d_ta)] for _ in range(h)]

    h_l = [rng.gauss(0.0, 1.0) for _ in range(h)]
    r_l = [rng.gauss(0.0, 1.0) for _ in range(h)]

    la_src_out = [bottleneck(h_l, d_lang_src, u_lang_src)[i] + r_l[i] for i in range(h)]
    ta_src_out = [bottleneck(la_src_out, d_task, u_task)[i] + r_l[i] for i in range(h)]

    # Zero-shot substitution of target language adapter preserves task adapter weights and residual r_l
    la_trg_out = [bottleneck(h_l, d_lang_trg, u_lang_trg)[i] + r_l[i] for i in range(h)]
    ta_trg_out = [bottleneck(la_trg_out, d_task, u_task)[i] + r_l[i] for i in range(h)]
    diff_transfer = math.sqrt(sum((ta_src_out[i] - ta_trg_out[i]) ** 2 for i in range(h)))
    assert diff_transfer > 0.1

    # When task adapter up-projection U_task = 0, TA_l(h_l, r_l) == r_l
    u_task_zero = [[0.0 for _ in range(d_ta)] for _ in range(h)]
    ta_zero_out = [bottleneck(la_trg_out, d_task, u_task_zero)[i] + r_l[i] for i in range(h)]
    assert ta_zero_out == r_l

    print(
        f"[PASS] MAD-X boundaries verified: max_inv_err={max_inv_err:.2e} (<1e-15), "
        f"diff_transfer={diff_transfer:.4f}, residual_identity=exact"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
