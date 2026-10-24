#!/usr/bin/env python3
"""Constructed boundary verification for Margin-MSE Cross-Architecture KD (Hofstätter et al., 2021, arXiv:2010.02666)."""


def margin_mse_loss(
    student_pos: list[float],
    student_neg: list[float],
    teacher_pos: list[float],
    teacher_neg: list[float],
) -> float:
    """Eqs. (11)-(12): MSE(M_s(Q, P^+) - M_s(Q, P^-), M_t(Q, P^+) - M_t(Q, P^-))."""
    n = len(student_pos)
    return sum(
        ((student_pos[i] - student_neg[i]) - (teacher_pos[i] - teacher_neg[i])) ** 2
        for i in range(n)
    ) / n


def pointwise_mse_loss(
    student_pos: list[float],
    student_neg: list[float],
    teacher_pos: list[float],
    teacher_neg: list[float],
) -> float:
    """Eq. (13): MSE(M_s(Q, P^+), M_t(Q, P^+)) + MSE(M_s(Q, P^-), M_t(Q, P^-))."""
    n = len(student_pos)
    mse_pos = sum((student_pos[i] - teacher_pos[i]) ** 2 for i in range(n)) / n
    mse_neg = sum((student_neg[i] - teacher_neg[i]) ** 2 for i in range(n)) / n
    return mse_pos + mse_neg


def ensemble_teacher_margins(
    teachers_pos: list[list[float]],
    teachers_neg: list[list[float]],
) -> tuple[list[float], list[float], list[float]]:
    """Section 6.1: Average scores across teacher ensemble (e.g., BERT-Base, BERT-Large-WM, ALBERT-Large)."""
    k = len(teachers_pos)
    n = len(teachers_pos[0])
    ens_pos = [sum(teachers_pos[t][i] for t in range(k)) / k for i in range(n)]
    ens_neg = [sum(teachers_neg[t][i] for t in range(k)) / k for i in range(n)]
    margins = [ens_pos[i] - ens_neg[i] for i in range(n)]
    return ens_pos, ens_neg, margins


def main() -> None:
    # Figure 1 observation:
    # Teacher BERT_CAT outputs scores centered near 0 (e.g., pos=+4.0, neg=-5.0 -> margin = +9.0),
    # whereas Student BERT_DOT or ColBERT outputs large positive dot products (e.g., pos=154.0, neg=145.0 -> margin = +9.0),
    # and Student TK outputs negative scores (e.g., pos=-4.0, neg=-13.0 -> margin = +9.0).
    t_pos = [4.0, 3.5, -1.0]   # Triple 2 is a false negative where teacher margin is negative (-1.0 - 0.5 = -1.5)
    t_neg = [-5.0, -4.5, 0.5]

    # Student ColBERT perfectly matches every pairwise margin (+9.0, +8.0, -1.5) at its natural offset +150:
    s_colbert_pos = [154.0, 153.5, 149.0]
    s_colbert_neg = [145.0, 145.5, 150.5]

    # 1. Margin-MSE is identically 0.0 when student matches teacher margins regardless of architecture offset:
    l_margin = margin_mse_loss(s_colbert_pos, s_colbert_neg, t_pos, t_neg)
    l_pointwise = pointwise_mse_loss(s_colbert_pos, s_colbert_neg, t_pos, t_neg)
    assert abs(l_margin) < 1e-12, f"Expected 0.0 Margin-MSE loss, got {l_margin}"
    assert l_pointwise > 40000.0, "Pointwise MSE severely penalizes natural cross-architecture score offsets"

    # 2. Negative teacher margin reverses false-negative ordering when optimizing student margin:
    assert (t_pos[2] - t_neg[2]) < 0.0 and (s_colbert_pos[2] - s_colbert_neg[2]) < 0.0

    # 3. Multi-teacher ensemble averaging (T2):
    t1_pos, t1_neg = [4.0, 3.0], [-4.0, -3.0]
    t2_pos, t2_neg = [6.0, 5.0], [-6.0, -4.0]
    t3_pos, t3_neg = [5.0, 4.0], [-5.0, -5.0]
    ens_pos, ens_neg, margins = ensemble_teacher_margins([t1_pos, t2_pos, t3_pos], [t1_neg, t2_neg, t3_neg])
    assert margins == [10.0, 8.0]

    print("Margin-MSE Cross-Architecture KD boundary verification passed:")
    print(f"  ColBERT vs BERT_CAT Margin-MSE:    {l_margin:.6f}")
    print(f"  ColBERT vs BERT_CAT Pointwise-MSE: {l_pointwise:.2f}")
    print(f"  Top-3 Teacher Ensemble margins:    {margins}")


if __name__ == "__main__":
    main()
