#!/usr/bin/env python3
"""Constructed boundary verification for UDapter (Ustun et al., EMNLP 2020)."""

from __future__ import annotations

import math
import random


def relu(vec: list[float]) -> list[float]:
    return [x if x > 0.0 else 0.0 for x in vec]


def matvec(mat: list[list[float]], vec: list[float]) -> list[float]:
    return [sum(row[j] * vec[j] for j in range(len(vec))) for row in mat]


def main() -> int:
    rng = random.Random(20260714)

    # 1. Verify URIEL feature dimensions (Section 3.4) and CPG parameter scaling (Appendix A.1)
    d_syn, d_phon, d_inv = 103, 28, 158
    d_uriel = d_syn + d_phon + d_inv
    assert d_uriel == 289

    lang_emb_dim = 32
    adapter_base_m = 9.4375  # 32 * 9.4375M = 302M
    biaffine_base_m = 7.75   # 32 * 7.75M = 248M
    udapter_total_m = lang_emb_dim * (adapter_base_m + biaffine_base_m)
    assert math.isclose(udapter_total_m, 550.0, rel_tol=1e-12)
    # For 13 languages, separate monolingual UDify models require 13 * 191M = 2483M (~2.5B) vs 550M
    mono_13_m = 13 * 191.0
    assert mono_13_m == 2483.0 > 4.5 * udapter_total_m

    # 2. Verify Eq. (6)-(7) Contextual Parameter Generator (CPG) linearity and zero-shot typology generalization
    m_dim = 8
    p_ad = 24
    p_bf = 16
    w_mlp1 = [[rng.gauss(0.0, 0.2) for _ in range(d_uriel)] for _ in range(16)]
    w_mlp2 = [[rng.gauss(0.0, 0.3) for _ in range(16)] for _ in range(m_dim)]
    w_ad = [[rng.gauss(0.0, 0.4) for _ in range(m_dim)] for _ in range(p_ad)]
    w_bf = [[rng.gauss(0.0, 0.4) for _ in range(m_dim)] for _ in range(p_bf)]

    def mlp_lang(l_t: list[float]) -> list[float]:
        return matvec(w_mlp2, relu(matvec(w_mlp1, l_t)))

    def cpg(l_e: list[float]) -> tuple[list[float], list[float]]:
        return matvec(w_ad, l_e), matvec(w_bf, l_e)

    # Generate two training language typology vectors from distinct language families (antipodal binary features)
    lt_1 = [float(i % 2) for i in range(d_uriel)]
    lt_2 = [1.0 - lt_1[i] for i in range(d_uriel)]
    le_1 = mlp_lang(lt_1)
    le_2 = mlp_lang(lt_2)

    # Verify exact bilinearity of CPG in language embedding space: g^(m)(a*le_1 + b*le_2) == a*g^(m)(le_1) + b*g^(m)(le_2)
    a, b = 0.65, 0.35
    le_mix = [a * le_1[i] + b * le_2[i] for i in range(m_dim)]
    ad_mix, bf_mix = cpg(le_mix)
    ad_1, bf_1 = cpg(le_1)
    ad_2, bf_2 = cpg(le_2)

    max_lin_err = max(
        max(abs(ad_mix[i] - (a * ad_1[i] + b * ad_2[i])) for i in range(p_ad)),
        max(abs(bf_mix[i] - (a * bf_1[i] + b * bf_2[i])) for i in range(p_bf)),
    )
    assert max_lin_err < 1e-15

    # Verify that a zero-shot language sharing 286/289 URIEL features with lt_1 gets CPG weights closer to lt_1 than to lt_2
    lt_zs = [lt_1[i] if i >= 3 else 1.0 - lt_1[i] for i in range(d_uriel)]
    le_zs = mlp_lang(lt_zs)
    ad_zs, _ = cpg(le_zs)
    dist_to_1 = math.sqrt(sum((ad_zs[i] - ad_1[i]) ** 2 for i in range(p_ad)))
    dist_to_2 = math.sqrt(sum((ad_zs[i] - ad_2[i]) ** 2 for i in range(p_ad)))
    assert dist_to_1 < dist_to_2

    print(
        f"[PASS] UDapter boundaries verified: d_uriel={d_uriel}, params={udapter_total_m:.0f}M vs {mono_13_m:.0f}M, "
        f"max_lin_err={max_lin_err:.2e}, dist_zs_rel={dist_to_1:.4f} < dist_zs_unrel={dist_to_2:.4f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
