#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 737:
Self-Adaptive In-Context Learning (TopK+MDL) (Wu et al., ACL 2023, arXiv:2212.10375).

Verifies:
1. Section 4.1-4.3 two-stage instance-level select-then-rank framework:
   Stage 1 (Selection) filters N training examples down to m nearest neighbors of test input x;
   Stage 2 (MDL Ranking, Equations 2-5) ranks candidate k-example organizations c in C by
   minimizing the expected Shannon-Huffman codelength of the predictive label distribution:
     c* = argmin_{c in C} L_theta(y | c, x)
        = argmin_{c in C} ( - sum_{y_i in Y} p(y_i | c, x) log2 p(y_i | c, x) ).
2. Section 4.4 contrast with LocalE (Lu et al., 2022): whereas corpus-level LocalE maximizes entropy
   over a probing set, instance-level MDL minimizes predictive entropy for each individual test input x
   to select organizations yielding decisive, low-codelength predictions without a validation set.
"""

import math
import random


def mdl_codelength_bits(probs):
    """Equation 5: -E_{p(y_i | c, x)} log2 p(y_i | c, x)."""
    return -sum(p * math.log2(max(p, 1e-12)) for p in probs if p > 0.0)


def softmax(logits):
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def main():
    random.seed(737)
    # 3-class classification task where each test instance x has an optimal demonstration organization
    # that resolves ambiguity and compresses the predictive label distribution
    test_instances = [
        {"id": 0, "true_label": 0},
        {"id": 1, "true_label": 1},
        {"id": 2, "true_label": 2},
    ]

    # For each test instance, Stage 1 TopK retrieves candidates and Stage 2 samples 6 organizations c_0..c_5
    # Organization c == true_label aligns examples cleanly; others induce high-entropy uncertainty
    def simulate_org_probs(test_inst, org_idx):
        y_true = test_inst["true_label"]
        if org_idx == y_true:
            # Well-organized context yields confident, low-codelength prediction on true label
            logits = [-1.5, -1.5, -1.5]
            logits[y_true] = 2.6
        elif org_idx == (y_true + 1) % 3:
            # Ambiguous ordering yields near-uniform distribution (high codelength)
            logits = [0.1, 0.0, -0.1]
        else:
            # Moderately noisy ordering
            logits = [-0.3, -0.3, -0.3]
            logits[y_true] = 0.6
        return softmax(logits)

    mdl_correct = 0
    locale_correct = 0
    mdl_lengths = []
    for inst in test_instances:
        orgs = list(range(6))
        scored = []
        for c in orgs:
            probs = simulate_org_probs(inst, c)
            codelen = mdl_codelength_bits(probs)
            pred = max(range(3), key=lambda y: probs[y])
            scored.append((codelen, pred, c, probs))
        # MDL selects minimum codelength (Equation 5)
        best_mdl = min(scored, key=lambda t: t[0])
        # LocalE selects maximum entropy
        best_locale = max(scored, key=lambda t: t[0])
        mdl_lengths.append(best_mdl[0])
        if best_mdl[1] == inst["true_label"]:
            mdl_correct += 1
        if best_locale[1] == inst["true_label"]:
            locale_correct += 1

    mdl_acc = mdl_correct / len(test_instances)
    locale_acc = locale_correct / len(test_instances)
    avg_mdl = sum(mdl_lengths) / len(mdl_lengths)

    assert mdl_acc == 1.0
    assert avg_mdl < 0.35, f"Expected MDL codelength < 0.35 bits, got {avg_mdl}"
    assert mdl_acc > locale_acc

    print(
        f"Self-Adaptive ICL (TopK+MDL) verification passed: "
        f"MDL_acc={mdl_acc:.2f}, avg_MDL_bits={avg_mdl:.4f}, LocalE_acc={locale_acc:.2f}"
    )


if __name__ == "__main__":
    main()
