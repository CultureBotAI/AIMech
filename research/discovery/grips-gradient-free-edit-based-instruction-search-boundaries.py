#!/usr/bin/env python3
"""Boundary and algorithmic verification for Round 732:
GrIPS Gradient-Free Edit-Based Instruction Search (Prasad et al., EACL 2023, arXiv:2203.07281).

Verifies:
1. Section 3 iterative edit-based discrete instruction search over phrase-level operations
   {delete, swap, paraphrase/substitute, add} without requiring model gradients or hidden states.
2. Section 3.2 composite scoring metric combining balanced classification accuracy and predicted
   label-distribution entropy regularization to break accuracy ties on small score sets.
3. Monotonic improvement of the selected instruction candidate across beam/greedy search iterations
   under a black-box API evaluation oracle.
"""

import math


def shannon_entropy(probs):
    return -sum(p * math.log(max(p, 1e-12)) for p in probs if p > 0.0)


def generate_phrase_edits(phrases, lexicon_subs, deleted_pool):
    """Generate phrase-level delete, swap, paraphrase, and add candidates (Section 3.1)."""
    candidates = []
    # 1. Delete one phrase
    if len(phrases) > 1:
        for i in range(len(phrases)):
            candidates.append(("delete", phrases[:i] + phrases[i + 1 :]))
    # 2. Swap two phrases
    for i in range(len(phrases)):
        for j in range(i + 1, len(phrases)):
            swapped = list(phrases)
            swapped[i], swapped[j] = swapped[j], swapped[i]
            candidates.append(("swap", swapped))
    # 3. Paraphrase / substitute one phrase
    for i, ph in enumerate(phrases):
        for sub in lexicon_subs.get(ph, []):
            replaced = list(phrases)
            replaced[i] = sub
            candidates.append(("paraphrase", replaced))
    # 4. Add back a previously deleted phrase
    for d_ph in deleted_pool:
        if d_ph not in phrases:
            candidates.append(("add", phrases + [d_ph]))
    return candidates


def main():
    # Initial base instruction split into constituent phrases
    base_phrases = ["Read the text", "maybe guess", "the sentiment polarity"]
    lexicon_subs = {
        "Read the text": ["Classify this review"],
        "maybe guess": ["determine accurately"],
        "the sentiment polarity": ["whether it is positive or negative"],
    }

    # Simulated black-box LM accuracy + label-entropy oracle on a balanced validation set
    def black_box_score(phrases):
        text = " ".join(phrases)
        acc = 0.55
        if "Classify this review" in text:
            acc += 0.15
        if "determine accurately" in text:
            acc += 0.12
        if "maybe guess" not in text:
            acc += 0.10
        if "whether it is positive or negative" in text:
            acc += 0.12
        acc = min(acc, 0.95)
        # Entropy bonus when predictions are balanced across classes
        balance_probs = [0.5, 0.5] if "whether it is positive or negative" in text else [0.75, 0.25]
        ent = shannon_entropy(balance_probs)
        return acc + 0.05 * ent, acc

    current = list(base_phrases)
    current_score, init_acc = black_box_score(current)
    deleted_pool = []

    for step in range(3):
        cands = generate_phrase_edits(current, lexicon_subs, deleted_pool)
        assert len(cands) > 0
        best_cand = current
        best_score = current_score
        best_op = "none"
        for op, cand_phrases in cands:
            sc, _ = black_box_score(cand_phrases)
            if sc > best_score:
                best_score = sc
                best_cand = cand_phrases
                best_op = op
        if best_op == "delete":
            for ph in current:
                if ph not in best_cand and ph not in deleted_pool:
                    deleted_pool.append(ph)
        assert best_score >= current_score
        current = best_cand
        current_score = best_score

    _, final_acc = black_box_score(current)
    assert final_acc > init_acc + 0.25, f"Expected accuracy improvement > 0.25, got {init_acc} -> {final_acc}"
    print(
        f"GrIPS verification passed: init_acc={init_acc:.2f} -> final_acc={final_acc:.2f}, "
        f"final_instruction='{' '.join(current)}'"
    )


if __name__ == "__main__":
    main()
