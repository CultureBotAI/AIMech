#!/usr/bin/env python3
"""Constructed boundary verification for BERT-PKD (Sun, Cheng, Gan, & Liu, EMNLP 2019, arXiv:1908.09355)."""

import math


def pkd_layer_indices(n_teacher: int, n_student: int, strategy: str) -> list[int]:
    """Section 3.2: I_pt layer indices for k = n_student - 1 intermediate layers."""
    k = n_student - 1
    if strategy == "skip":
        step = n_teacher // n_student
        return [step * j for j in range(1, k + 1)]
    if strategy == "last":
        return [n_teacher - k + j - 1 for j in range(1, k + 1)]
    raise ValueError(f"Unknown PKD strategy: {strategy}")


def l2_normalize(vec: list[float], eps: float = 1e-12) -> list[float]:
    norm = math.sqrt(sum(x * x for x in vec)) + eps
    return [x / norm for x in vec]


def patient_loss(
    student_cls_layers: list[list[float]],
    teacher_cls_layers: dict[int, list[float]],
    i_pt: list[int],
) -> float:
    """Equation (7): L_PT = sum_{j=1}^M || h_{i,j}^s / ||h_{i,j}^s||_2 - h_{i,I_pt(j)}^t / ||h_{i,I_pt(j)}^t||_2 ||_2^2."""
    total = 0.0
    for j_idx, t_layer in enumerate(i_pt):
        hs_norm = l2_normalize(student_cls_layers[j_idx])
        ht_norm = l2_normalize(teacher_cls_layers[t_layer])
        total += sum((hs_norm[c] - ht_norm[c]) ** 2 for c in range(len(hs_norm)))
    return total


def main() -> None:
    # 1. Verify Section 3.2 example for distilling BERT_12 to BERT_6 (k = 5 intermediate layers):
    ipt_skip = pkd_layer_indices(n_teacher=12, n_student=6, strategy="skip")
    ipt_last = pkd_layer_indices(n_teacher=12, n_student=6, strategy="last")
    assert ipt_skip == [2, 4, 6, 8, 10]
    assert ipt_last == [7, 8, 9, 10, 11]

    # 2. Verify Eq. (7) L_PT scale invariance on [CLS] hidden states:
    teacher_cls = {
        2: [1.0, 2.0, -1.0],
        4: [0.5, -1.5, 2.0],
        6: [-1.0, 0.5, 1.5],
        8: [2.0, 1.0, 0.5],
        10: [1.5, -0.5, -2.0],
    }
    # Student [CLS] vectors are positive scalar multiples of teacher's [CLS] vectors at I_pt:
    student_cls_scaled = [[3.5 * x for x in teacher_cls[layer]] for layer in ipt_skip]
    l_pt_zero = patient_loss(student_cls_scaled, teacher_cls, ipt_skip)
    assert l_pt_zero < 1e-12, f"Expected ~0 patient loss for collinear [CLS] states, got {l_pt_zero}"

    # Perturbed student [CLS] states incur strictly positive L_PT:
    student_cls_bad = [[-x for x in teacher_cls[layer]] for layer in ipt_skip]
    l_pt_bad = patient_loss(student_cls_bad, teacher_cls, ipt_skip)
    assert abs(l_pt_bad - 20.0) < 1e-9  # 5 layers * ||u - (-u)||_2^2 = 5 * 4 = 20

    print("BERT-PKD boundary verification passed:")
    print(f"  PKD-Skip I_pt (12->6): {ipt_skip}")
    print(f"  PKD-Last I_pt (12->6): {ipt_last}")
    print(f"  L_PT (collinear scaled vs antipodal): {l_pt_zero:.6f} vs {l_pt_bad:.2f}")


if __name__ == "__main__":
    main()
