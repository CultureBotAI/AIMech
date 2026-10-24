#!/usr/bin/env python3
"""Constructed boundary verification for HIBERT (Zhang, Wei, & Zhou, ACL 2019, arXiv:1905.06566)."""

import math


def mask_document_sentences(
    sentences: list[list[str]],
    selected_indices: set[int],
    modes: dict[int, str],
    random_pool: list[str],
) -> list[list[str]]:
    """Section 3.2: 80% all-[MASK], 10% unchanged, 10% random sentence replacement."""
    masked_doc: list[list[str]] = []
    for idx, sent in enumerate(sentences):
        if idx not in selected_indices:
            masked_doc.append(list(sent))
            continue
        mode = modes[idx]
        if mode == "mask":
            masked_doc.append(["[MASK]"] * len(sent))
        elif mode == "keep":
            masked_doc.append(list(sent))
        elif mode == "random":
            masked_doc.append(list(random_pool))
        else:
            raise ValueError(f"Unknown masking mode: {mode}")
    return masked_doc


def hibert_decoder_step(
    h_dec: list[float],
    d_tilde_k: list[float],
    w1_ff: list[list[float]],
    b1: list[float],
    w2_ff: list[list[float]],
    b2: list[float],
    w_out: list[list[float]],
) -> list[float]:
    """Eqs. (4)-(6): Inject context-sensitive sentence vector d_tilde_k via x_tilde = h_tilde + d_tilde_k."""
    x_tilde = [h_dec[i] + d_tilde_k[i] for i in range(len(h_dec))]
    hidden = [
        max(0.0, sum(w1_ff[r][c] * x_tilde[c] for c in range(len(x_tilde))) + b1[r])
        for r in range(len(w1_ff))
    ]
    g_tilde = [
        sum(w2_ff[r][c] * hidden[c] for c in range(len(hidden))) + b2[r]
        for r in range(len(w2_ff))
    ]
    logits = [sum(w_out[v][c] * g_tilde[c] for c in range(len(g_tilde))) for v in range(len(w_out))]
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    z_sum = sum(exps)
    return [e / z_sum for e in exps]


def main() -> None:
    # 1. Verify sentence-level document masking transformation (80% [MASK], 10% keep, 10% random):
    doc = [
        ["William", "Shakespeare", "is", "a", "poet", "."],
        ["He", "died", "in", "1616", "."],
        ["He", "is", "regarded", "as", "the", "greatest", "writer", "."],
    ]
    masked = mask_document_sentences(
        doc,
        selected_indices={1},
        modes={1: "mask"},
        random_pool=["Birds", "can", "fly", "."],
    )
    assert masked[0] == doc[0]
    assert masked[1] == ["[MASK]"] * 5
    assert masked[2] == doc[2]

    replaced = mask_document_sentences(
        doc,
        selected_indices={1},
        modes={1: "random"},
        random_pool=["Birds", "can", "fly", "."],
    )
    assert replaced[1] == ["Birds", "can", "fly", "."]

    # 2. Verify Eqs. (4)-(6): injecting d_tilde_k shifts next-word distribution toward target word 0:
    h_dec = [0.2, 0.1]
    d_tilde_informative = [2.0, 1.5]
    d_tilde_zero = [0.0, 0.0]
    w1_ff = [[1.0, 0.5], [0.5, 1.0]]
    b1 = [0.0, 0.0]
    w2_ff = [[1.0, 0.0], [0.0, 1.0]]
    b2 = [0.0, 0.0]
    w_out = [
        [1.2, 1.0],   # Target word 0 aligned with d_tilde_informative
        [-0.5, -0.5],
        [0.1, -0.2],
    ]
    probs_with_ctx = hibert_decoder_step(h_dec, d_tilde_informative, w1_ff, b1, w2_ff, b2, w_out)
    probs_no_ctx = hibert_decoder_step(h_dec, d_tilde_zero, w1_ff, b1, w2_ff, b2, w_out)
    assert abs(sum(probs_with_ctx) - 1.0) < 1e-9
    assert probs_with_ctx[0] > 0.95 > probs_no_ctx[0]

    print("HIBERT boundary verification passed:")
    print(f"  Masked sentence 1:   {masked[1]}")
    print(f"  Replaced sentence 1: {replaced[1]}")
    print(f"  P(target word | d_tilde_k)={probs_with_ctx[0]:.4f} > P(target word | 0)={probs_no_ctx[0]:.4f}")


if __name__ == "__main__":
    main()
