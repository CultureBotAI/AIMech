#!/usr/bin/env python3
"""Constructed boundary verification for SMITH (Yang et al., CIKM 2020, arXiv:2004.12297)."""

import math


def greedy_sentence_filling(sentences: list[list[str]], max_block_len: int) -> list[list[str]]:
    """Section 4.1.1: Pack complete sentences greedily into blocks of max length L_s; truncate oversize sentences."""
    blocks: list[list[str]] = []
    current: list[str] = []
    for sent in sentences:
        if not sent:
            continue
        if len(sent) > max_block_len:
            if current:
                blocks.append(current)
                current = []
            blocks.append(sent[:max_block_len])
        elif len(current) + len(sent) <= max_block_len:
            current.extend(sent)
        else:
            blocks.append(current)
            current = list(sent)
    if current:
        blocks.append(current)
    return blocks


def count_padding_tokens(blocks: list[list[str]], max_block_len: int) -> int:
    """Count total [PAD] tokens across all blocks when padded to max_block_len."""
    return sum(max_block_len - len(b) for b in blocks)


def smith_attention_memory_ops(n_tokens: int, block_len: int) -> tuple[int, int]:
    """Section 4.1.3, Eq. (3): Compare full Transformer N^2 vs SMITH (L_s * N + (N / L_s)^2)."""
    full_ops = n_tokens * n_tokens
    num_blocks = n_tokens // block_len
    smith_ops = block_len * n_tokens + num_blocks * num_blocks
    return full_ops, smith_ops


def masked_sentence_block_loss(pred_blocks: list[list[float]], true_blocks: list[list[float]]) -> float:
    """Section 4.2.2, Eqs. (4)-(6): In-batch contrastive cross-entropy over B masked sentence blocks."""
    b_size = len(pred_blocks)
    dim = len(pred_blocks[0])
    total_loss = 0.0
    for j in range(b_size):
        logits = [sum(pred_blocks[j][d] * true_blocks[r][d] for d in range(dim)) for r in range(b_size)]
        m = max(logits)
        exps = [math.exp(x - m) for x in logits]
        prob_jj = exps[j] / sum(exps)
        total_loss += -math.log(prob_jj + 1e-12)
    return total_loss / b_size


def main() -> None:
    # 1. Greedy sentence filling reduces padding tokens and total blocks vs one-sentence-per-block:
    sentences = [
        ["w1", "w2", "w3"],
        ["w4", "w5"],
        ["w6", "w7", "w8", "w9"],
        ["w10", "w11"],
        ["w12", "w13", "w14", "w15", "w16", "w17", "w18", "w19", "w20"],  # Oversize sentence (> 8)
    ]
    max_len = 8
    greedy_blocks = greedy_sentence_filling(sentences, max_len)
    naive_blocks = [s[:max_len] for s in sentences]

    assert len(greedy_blocks) == 3, f"Expected 3 greedy blocks, got {len(greedy_blocks)}"
    assert len(greedy_blocks[0]) == 5  # [3 + 2] packed together
    assert len(greedy_blocks[1]) == 6  # [4 + 2] packed together
    assert len(greedy_blocks[2]) == 8  # truncated 9-token sentence to 8
    pad_greedy = count_padding_tokens(greedy_blocks, max_len)
    pad_naive = count_padding_tokens(naive_blocks, max_len)
    assert pad_greedy < pad_naive, f"Greedy padding ({pad_greedy}) must be strictly less than naive ({pad_naive})"

    # 2. Eq. (3) memory complexity reduction for N=2048, L_s=32:
    full_ops, smith_ops = smith_attention_memory_ops(2048, 32)
    assert full_ops == 4_194_304
    assert smith_ops == 32 * 2048 + 64 * 64 == 69_632
    assert full_ops / smith_ops > 60.0

    # 3. Eqs. (4)-(6) Masked sentence block prediction loss is lower when aligned than permuted:
    true_blocks = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ]
    pred_aligned = [
        [2.5, 0.1, -0.1],
        [0.1, 2.5, 0.0],
        [-0.1, 0.0, 2.5],
    ]
    pred_swapped = [
        [0.1, 2.5, 0.0],
        [2.5, 0.1, -0.1],
        [-0.1, 0.0, 2.5],
    ]
    loss_aligned = masked_sentence_block_loss(pred_aligned, true_blocks)
    loss_swapped = masked_sentence_block_loss(pred_swapped, true_blocks)
    assert loss_aligned < 0.20 < loss_swapped

    print("SMITH boundary verification passed:")
    print(f"  Greedy blocks={len(greedy_blocks)} (pad={pad_greedy}) vs Naive blocks={len(naive_blocks)} (pad={pad_naive})")
    print(f"  Attention ops (N=2048, L_s=32): full={full_ops} vs SMITH={smith_ops} ({full_ops / smith_ops:.1f}x reduction)")
    print(f"  Masked sentence block loss: aligned={loss_aligned:.4f} < swapped={loss_swapped:.4f}")


if __name__ == "__main__":
    main()
