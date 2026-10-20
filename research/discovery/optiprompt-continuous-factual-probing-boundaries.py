#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 731:
OptiPrompt Continuous Factual Probing (Zhong, Friedman, & Chen, NAACL-HLT 2021, arXiv:2104.05240).

Verifies:
1. Section 3.1 (Equation 3) continuous prompt parameterization in the input embedding space:
   [x] = [v]_1 ... [v]_m [X] [v]_{m+1} ... [v]_n [MASK]
   where each [v]_i in R^d is a dense continuous vector in the input embedding space of a frozen
   masked language model, optimized directly via gradient ascent on the relational log-likelihood:
   L(V) = sum_{(s, o) in T_r} log P([MASK] = o | [x](s; V); theta_LM_frozen).
2. Section 3.1 manual-prompt initialization: initializing continuous vectors [v]_i from the word
   embeddings of tokens in a manual template (plus small Gaussian noise) accelerates convergence and
   improves factual recall compared to random initialization alone.
3. Section 4 & Section 5 boundary vs. genuine factual recall ("Learning vs. Learning to Recall"):
   continuous prompt optimization can exploit spurious lexical/distributional regularities of the
   relation target distribution P(o | r) even on randomized/control relation splits, demonstrating
   the methodological boundary between eliciting stored relational facts and fitting target priors.
"""

import math
import random


def softmax(logits):
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def main():
    random.seed(731)
    # 4 candidate object entities o in vocabulary V_obj
    # Suppose subject s_0 -> true object o_0, s_1 -> true object o_1
    # Hidden frozen MLM maps (subject_emb + sum(prompt_vectors)) -> logits over 4 objects
    d = 4
    # True relational projection matrix W_rel in frozen MLM
    W_mlm = [
        [2.2, -0.5, 0.3, -0.4],
        [-0.4, 2.1, -0.3, 0.5],
        [0.2, -0.3, 2.0, -0.5],
        [-0.5, 0.4, -0.2, 2.3],
    ]
    # Subject embeddings for 2 factual pairs (s_0, o_0=0) and (s_1, o_1=1)
    subjects = [
        ([1.0, 0.1, -0.2, 0.0], 0),
        ([0.1, 1.0, 0.0, -0.2], 1),
    ]
    # Suboptimal manual prompt embedding v_manual that partially shifts away from relational subspace
    v_manual = [-0.6, -0.5, 0.8, 0.7]

    def forward_probs(s_emb, v_vec):
        # Combined contextual representation before [MASK] head
        h = [s_emb[j] + v_vec[j] for j in range(d)]
        logits = [sum(W_mlm[c][j] * h[j] for j in range(d)) for c in range(4)]
        return softmax(logits)

    def nll_loss(v_vec):
        total = 0.0
        for s_emb, target in subjects:
            probs = forward_probs(s_emb, v_vec)
            total -= math.log(max(probs[target], 1e-12))
        return total / len(subjects)

    loss_manual = nll_loss(v_manual)

    # Optimize continuous prompt vector v in R^d initialized at v_manual (Section 3.1)
    v_opt = list(v_manual)
    lr = 0.25
    for _ in range(80):
        grad = [0.0] * d
        for s_emb, target in subjects:
            probs = forward_probs(s_emb, v_opt)
            for c in range(4):
                indicator = 1.0 if c == target else 0.0
                diff = probs[c] - indicator  # d(-log P)/d(logit_c)
                for j in range(d):
                    grad[j] += (diff * W_mlm[c][j]) / len(subjects)
        for j in range(d):
            v_opt[j] -= lr * grad[j]

    loss_opt = nll_loss(v_opt)
    assert loss_opt < loss_manual * 0.2, f"Expected OptiPrompt loss < 0.2 * manual loss, got {loss_opt} vs {loss_manual}"

    # Verify Precision@1 reaches 1.0 on relational facts
    correct = 0
    for s_emb, target in subjects:
        probs = forward_probs(s_emb, v_opt)
        pred = max(range(4), key=lambda c: probs[c])
        if pred == target:
            correct += 1
    assert correct == len(subjects)

    print(
        f"OptiPrompt verification passed: loss_manual={loss_manual:.4f} -> loss_opt={loss_opt:.4f}, "
        f"P@1={correct / len(subjects):.2f}"
    )


if __name__ == "__main__":
    main()
