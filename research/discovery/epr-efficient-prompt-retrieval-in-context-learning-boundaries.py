#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 735:
EPR Efficient Prompt Retrieval for In-Context Learning (Rubin, Herzig, & Berant, NAACL 2022, arXiv:2112.08633).

Verifies:
1. Section 3.1 Scoring-LM supervision generation: given training instance (x_i, y_i) and candidate
   pool E_bar retrieved by Ru(y_i, D), each candidate e_l is scored by
   s(e_l) = Prob_{g_hat}(y_i | e_l, x_i), labeling top-k as E_pos and bottom-k as hard negatives E_neg.
2. Section 3.2 Equation 1 contrastive bi-encoder training objective:
   L(x_i, e_i^+, e_{i,1}^-, ..., e_{i,2B-1}^-) =
     -log( exp(sim(x_i, e_i^+)) / (exp(sim(x_i, e_i^+)) + sum_{j=1}^{2B-1} exp(sim(x_i, e_{i,j}^-))) )
   where sim(x, e) = E_X(x)^T E_P(e).
3. Test-time maximum inner-product search (MIPS) retrieves structural-match prompts that outperform
   surface lexical similarity baselines.
"""

import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def main():
    # Suppose each example has a 4D feature representation:
    # dims 0..1 = surface topic words, dims 2..3 = latent compositional logical-form structure
    # Scoring LM Prob_{g_hat}(y | e, x) depends on structural alignment (dims 2..3), not surface topic!
    train_examples = [
        # (x_feat, e_feat, structural_type)
        ([1.0, 0.1, 0.9, 0.1], [1.0, 0.1, 0.9, 0.1], 0),  # ex 0: topic A, structure S0
        ([0.1, 1.0, 0.9, 0.1], [0.1, 1.0, 0.9, 0.1], 0),  # ex 1: topic B, structure S0 (true positive for ex 0!)
        ([0.9, 0.2, 0.1, 0.9], [0.9, 0.2, 0.1, 0.9], 1),  # ex 2: topic A, structure S1 (surface trap / hard negative for ex 0!)
        ([0.2, 0.9, 0.1, 0.9], [0.2, 0.9, 0.1, 0.9], 1),  # ex 3: topic B, structure S1 (true positive for ex 2!)
    ]

    def scoring_lm_prob(x_idx, cand_idx):
        """s(e_l) = Prob_{g_hat}(y_i | e_l, x_i) from Section 3.1."""
        x_f = train_examples[x_idx][0]
        e_f = train_examples[cand_idx][1]
        # Scoring LM rewards shared logical-form structure (dims 2, 3)
        struct_dot = x_f[2] * e_f[2] + x_f[3] * e_f[3]
        return 1.0 / (1.0 + math.exp(-3.0 * (struct_dot - 0.5)))

    # 1. Label positive and hard-negative candidates for each training example using s(e_l)
    labeled_triples = []
    for i in range(len(train_examples)):
        other_indices = [j for j in range(len(train_examples)) if j != i]
        scored = sorted(other_indices, key=lambda j: scoring_lm_prob(i, j), reverse=True)
        e_pos_idx = scored[0]
        e_neg_idx = scored[-1]
        assert train_examples[e_pos_idx][2] == train_examples[i][2]
        assert train_examples[e_neg_idx][2] != train_examples[i][2]
        labeled_triples.append((i, e_pos_idx, e_neg_idx))

    # 2. Train diagonal projection weights w in R^4 for bi-encoder sim(x, e) = (w * x)^T (w * e)
    # Initialized uniformly (so surface dims 0..1 initially confuse the retriever)
    w = [1.0, 1.0, 1.0, 1.0]

    def sim_w(x_f, e_f, weights):
        return sum((weights[d] ** 2) * x_f[d] * e_f[d] for d in range(4))

    def contrastive_loss(weights):
        total = 0.0
        for i, pos_idx, neg_idx in labeled_triples:
            x_f = train_examples[i][0]
            s_pos = sim_w(x_f, train_examples[pos_idx][1], weights)
            # In-batch negatives + hard negative (Equation 1)
            neg_indices = [j for j in range(len(train_examples)) if j != i and j != pos_idx]
            denom_terms = [math.exp(s_pos)] + [math.exp(sim_w(x_f, train_examples[n_j][1], weights)) for n_j in neg_indices]
            total -= s_pos - math.log(sum(denom_terms))
        return total / len(labeled_triples)

    loss_init = contrastive_loss(w)

    # Optimize w via finite-difference gradient descent on Equation 1
    lr = 0.4
    eps = 1e-5
    for _ in range(80):
        base = contrastive_loss(w)
        grad = [0.0] * 4
        for d in range(4):
            w_plus = list(w)
            w_plus[d] += eps
            grad[d] = (contrastive_loss(w_plus) - base) / eps
        for d in range(4):
            w[d] = max(0.05, w[d] - lr * grad[d])

    loss_final = contrastive_loss(w)
    assert loss_final < loss_init * 0.25, f"Expected contrastive loss reduction, got {loss_init} -> {loss_final}"

    # Verify test-time MIPS retrieves structurally matching prompt over surface distractor
    test_x = [0.95, 0.05, 0.92, 0.08]  # surface topic A, structure S0
    # Candidate 1 has topic B, structure S0; Candidate 2 has topic A, structure S1
    s_struct = sim_w(test_x, train_examples[1][1], w)
    s_surface = sim_w(test_x, train_examples[2][1], w)
    assert s_struct > s_surface, "EPR bi-encoder must rank structural prompt above surface distractor"

    print(
        f"EPR verification passed: loss_init={loss_init:.4f} -> loss_final={loss_final:.4f}, "
        f"sim_structural={s_struct:.4f} > sim_surface={s_surface:.4f}"
    )


if __name__ == "__main__":
    main()
