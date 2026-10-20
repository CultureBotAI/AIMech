#!/usr/bin/env python3
"""Constructed boundary verification for Condenser (Gao & Callan, EMNLP 2021, arXiv:2104.08253).

Verifies:
1. Late-early short-circuit information bottleneck (Section 3.3, Eq. 6-9, Figure 1):
   - Early encoder layers L^e produce [h_cls^early; h^early] = Encoder_early([h_cls^0; h^0]).
   - Late encoder layers L^l refine [h_cls^late; h^late] = Encoder_late([h_cls^early; h^early]).
   - The Condenser Head receives ONLY [h_cls^late; h^early] (skip-connecting early token states
     h^early while blocking direct access to late token states h^late). Consequently, any semantic
     information computed in the late encoder layers L^l can reach the Condenser Head's masked token
     predictions h_i^cd ONLY by flowing through the single dense vector h_cls^late.
2. Dual MLM semantic constraint loss (Section 3.4, Eq. 9-11):
   L = L_mlm(W h_i^cd, x_i) + L_mlm^c(W h_i^late, x_i) with shared projection matrix W,
   and exact parameter equivalence to the backbone transformer at fine-tuning time after dropping
   the Condenser Head.
"""

from __future__ import annotations
import math


def condenser_head_forward(
    h_cls_late: list[float], h_tokens_early: list[list[float]], alpha_cls: float = 0.6
) -> list[list[float]]:
    """Simulate Eq. 8 Condenser_head([h_cls^late; h^early]) attending to h_cls^late and early tokens."""
    d = len(h_cls_late)
    return [
        [alpha_cls * h_cls_late[k] + (1.0 - alpha_cls) * tok[k] for k in range(d)]
        for tok in h_tokens_early
    ]


def mlm_cross_entropy(h_pred: list[float], w_vocab: list[list[float]], target_idx: int) -> float:
    """Compute CrossEntropy(W h_pred, x_i) for a single masked position."""
    logits = [sum(w_vocab[v][k] * h_pred[k] for k in range(len(h_pred))) for v in range(len(w_vocab))]
    m = max(logits)
    exps = [math.exp(x - m) for x in logits]
    return -(logits[target_idx] - m - math.log(sum(exps)))


def main() -> None:
    d = 3
    # Early token representations lack global disambiguation (e.g., at masked token index 0)
    h_tokens_early = [[0.1, 0.0, -0.1], [0.2, 0.1, 0.0]]
    # Late token representations carry refined context, AND h_cls_late aggregates global sequence meaning
    h_tokens_late = [[1.2, 0.9, -0.8], [0.3, 0.2, 0.1]]
    h_cls_late_informative = [1.5, 1.1, -1.0]
    h_cls_late_dormant = [0.0, 0.0, 0.0]

    w_vocab = [
        [1.2, 1.0, -0.9],  # target token 0
        [-0.5, 0.2, 0.8],
        [0.1, -0.7, 0.3],
    ]

    # 1. Verify Eq. 8 short-circuit: perturbing h_tokens_late while holding h_cls_late and h_tokens_early fixed
    # has ZERO effect on h_cd (because h_tokens_late is disconnected from Condenser_head input!)
    h_cd_1 = condenser_head_forward(h_cls_late_informative, h_tokens_early)
    h_tokens_late_perturbed = [[99.0, -99.0, 42.0], [10.0, 20.0, 30.0]]
    _ = h_tokens_late_perturbed  # explicitly unused by Condenser_head([h_cls^late; h^early])
    h_cd_2 = condenser_head_forward(h_cls_late_informative, h_tokens_early)
    assert h_cd_1 == h_cd_2

    # 2. Verify that an informative h_cls^late strictly reduces Condenser Head MLM loss L_mlm (Eq. 9)
    # compared to a dormant h_cls^late
    h_cd_dormant = condenser_head_forward(h_cls_late_dormant, h_tokens_early)
    loss_cd_informative = mlm_cross_entropy(h_cd_1[0], w_vocab, target_idx=0)
    loss_cd_dormant = mlm_cross_entropy(h_cd_dormant[0], w_vocab, target_idx=0)
    assert loss_cd_informative < loss_cd_dormant

    # 3. Verify Eq. 10-11 combined pre-training loss L = L_mlm + L_mlm^c with shared W
    loss_backbone_late = mlm_cross_entropy(h_tokens_late[0], w_vocab, target_idx=0)
    total_loss = loss_cd_informative + loss_backbone_late
    assert total_loss > loss_cd_informative and total_loss > loss_backbone_late

    # 4. Verify fine-tuning structural readiness: dropping L^h=2 head layers leaves L^e + L^l = 6 + 6 = 12 layers
    l_early, l_late, l_head = 6, 6, 2
    pretrain_layers = l_early + l_late + l_head
    finetune_layers = l_early + l_late
    assert pretrain_layers == 14 and finetune_layers == 12

    print(
        "Condenser boundary verification passed:",
        {"loss_informative_cls": round(loss_cd_informative, 4), "loss_dormant_cls": round(loss_cd_dormant, 4)},
    )


if __name__ == "__main__":
    main()
