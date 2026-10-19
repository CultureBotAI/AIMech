# Discovery Report: Round 322 — Anchor Words and RecoverL2 Topic-Word Matrix Factorization

- **Timestamp**: `2026-10-19T06:36:00Z`
- **Selected Concept**: `AIMech:AnchorWordsAndRecoverL2TopicWordMatrixFactorization` (*Anchor Words and RecoverL2 Topic-Word Matrix Factorization*)
- **Record Path**: `data/curated/AnchorWordsAndRecoverL2TopicWordMatrixFactorization.yaml`
- **Primary Source**: Sanjeev Arora, Rong Ge, Yoni Halpern, David Mimno, Ankur Moitra, David Sontag, Yichen Wu, Michael Zhu — *A Practical Algorithm for Topic Modeling with Provable Guarantees* (`https://proceedings.mlr.press/v28/arora13.html`).

## Identity & Boundary Resolution

Distinct from variational Bayes or Gibbs sampling for Latent Dirichlet Allocation (`AIO:LatentDirichletAllocation`) and from general linear-programming Separable NMF (AIMech:SeparableNonnegativeMatrixFactorizationAndRobustLonerRecovery). Specifically captures the Arora et al. (2013) word-word co-occurrence formulation Q = A R A^T with unbiased diagonal correction tilde{H}_d tilde{H}_d^T - hat{H}_d (Section 2.1 and Appendix D.1), the Bayesian posterior simplex reformulation C_{i,k} = P(z_1 = k | w_1 = i) (Section 3.1), the RecoverKL/RecoverL2 Exponentiated Gradient solver (Algorithms 3 and 5, Theorem 3.1), and the FastAnchorWords greedy subspace-distance anchor selection algorithm and its simplex-volume perturbation proof (Algorithm 4, Theorem 4.2, and Lemma A.3 / Claim A.4).

## Constructed Boundary & Regime Verification

```text
{"appendix_d1_estimator_err": 0.0, "claim_a4_det_ratio": 0.939575, "claim_a4_lower_bound": 0.926859, "concept": "AnchorWordsAndRecoverL2TopicWordMatrixFactorization", "fast_anchor_words_selected": [0, 1, 2], "recoverl2_max_entry_err": 2.242e-05, "status": "VERIFIED"}
```
