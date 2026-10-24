#!/usr/bin/env python3
"""Constructed boundary verification for TinyBERT (Jiao et al., Findings of EMNLP 2020, arXiv:1909.10351)."""

import math


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    r_a, c_a = len(a), len(a[0])
    c_b = len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(c_a)) for j in range(c_b)] for i in range(r_a)]


def mse_mat(a: list[list[float]], b: list[list[float]]) -> float:
    r, c = len(a), len(a[0])
    return sum((a[i][j] - b[i][j]) ** 2 for i in range(r) for j in range(c)) / (r * c)


def layer_mapping(m: int, m_student: int, n_teacher: int, strategy: str = "uniform") -> int:
    """Section 3.1 & 4.6: Layer mapping function n = g(m) with g(0)=0 and g(M+1)=N+1."""
    if m == 0:
        return 0
    if m == m_student + 1:
        return n_teacher + 1
    if strategy == "uniform":
        return (n_teacher // m_student) * m
    if strategy == "top":
        return m + n_teacher - m_student
    if strategy == "bottom":
        return m
    raise ValueError(f"Unknown strategy: {strategy}")


def tinybert_layer_losses(
    a_student_heads: list[list[list[float]]],
    a_teacher_heads: list[list[list[float]]],
    h_student: list[list[float]],
    w_h: list[list[float]],
    h_teacher: list[list[float]],
    e_student: list[list[float]],
    w_e: list[list[float]],
    e_teacher: list[list[float]],
    z_student: list[float],
    z_teacher: list[float],
    temperature: float = 1.0,
) -> tuple[float, float, float, float]:
    """Equations (7)-(10): L_attn (unnormalized A_i), L_hidn, L_embd, and L_pred."""
    num_heads = len(a_student_heads)
    l_attn = sum(
        mse_mat(a_student_heads[i], a_teacher_heads[i]) for i in range(num_heads)
    ) / num_heads

    h_proj = matmul(h_student, w_h)
    l_hidn = mse_mat(h_proj, h_teacher)

    e_proj = matmul(e_student, w_e)
    l_embd = mse_mat(e_proj, e_teacher)

    # Soft cross-entropy CE(z^T / t, z^S / t)
    zt_scaled = [z / temperature for z in z_teacher]
    zs_scaled = [z / temperature for z in z_student]
    mt = max(zt_scaled)
    ms = max(zs_scaled)
    pt = [math.exp(z - mt) for z in zt_scaled]
    ps = [math.exp(z - ms) for z in zs_scaled]
    sum_pt = sum(pt)
    sum_ps = sum(ps)
    pt = [p / sum_pt for p in pt]
    ps = [p / sum_ps for p in ps]
    l_pred = -sum(pt[k] * math.log(ps[k]) for k in range(len(pt)))
    return l_embd, l_attn, l_hidn, l_pred


def main() -> None:
    # 1. Verify layer mapping strategies for M=4, N=12 (Section 4.2 & 4.6):
    m_stu, n_tea = 4, 12
    uniform_map = [layer_mapping(m, m_stu, n_tea, "uniform") for m in range(m_stu + 2)]
    top_map = [layer_mapping(m, m_stu, n_tea, "top") for m in range(m_stu + 2)]
    bottom_map = [layer_mapping(m, m_stu, n_tea, "bottom") for m in range(m_stu + 2)]
    assert uniform_map == [0, 3, 6, 9, 12, 13]
    assert top_map == [0, 9, 10, 11, 12, 13]
    assert bottom_map == [0, 1, 2, 3, 4, 13]

    # 2. Verify Eqs. (7)-(11) projection from d'=2 to d=3 and zero loss when matched:
    w_h = [[1.0, 0.0, 0.5], [0.0, 1.0, -0.5]]
    h_s = [[0.4, 0.6], [-0.2, 0.8]]
    h_t = matmul(h_s, w_h)
    a_heads = [[[0.5, -0.3], [0.2, 0.7]], [[-0.1, 0.4], [0.6, -0.2]]]
    logits = [1.5, -0.5]

    l_embd, l_attn, l_hidn, l_pred_ce = tinybert_layer_losses(
        a_heads, a_heads, h_s, w_h, h_t, h_s, w_h, h_t, logits, logits, temperature=1.0
    )
    assert abs(l_embd) < 1e-12
    assert abs(l_attn) < 1e-12
    assert abs(l_hidn) < 1e-12
    assert l_pred_ce > 0.0

    print("TinyBERT boundary verification passed:")
    print(f"  Uniform mapping (M=4, N=12): {uniform_map}")
    print(f"  Matched L_embd={l_embd:.6f}, L_attn={l_attn:.6f}, L_hidn={l_hidn:.6f}, L_pred={l_pred_ce:.4f}")


if __name__ == "__main__":
    main()
