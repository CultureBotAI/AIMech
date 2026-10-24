# Discovery Report: Round 377 — signSGD and Majority-Vote Compressed Non-Convex Optimization

- **Timestamp**: `2026-10-19T07:40:00Z`
- **Selected Concept**: `AIMech:SignSgdAndMajorityVoteCompressedNonconvexOptimization` (*signSGD and Majority-Vote Compressed Non-Convex Optimization*)
- **Record Path**: `data/curated/SignSgdAndMajorityVoteCompressedNonconvexOptimization.yaml`
- **Primary Source**: Jeremy Bernstein, Yu-Xiang Wang, Kamyar Azizzadenesheli, Animashree Anandkumar — *signSGD: Compressed Optimisation for Non-Convex Problems* (`https://proceedings.mlr.press/v80/bernstein18a.html`).

## Identity & Boundary Resolution

Distinct from randomized unbiased multi-level l_2-norm quantization QSGD (Alistarh et al. 2017, Round 378), which preserves unbiasedness E[Q_s(v)] = v via stochastic rounding and transmits ||v||_2 plus Elias-coded integer levels; from deterministic Rprop (Riedmiller & Braun 1993), which adapts per-coordinate step sizes heuristic-ally across epochs based on consecutive sign agreement without stochastic minibatch convergence guarantees or M-worker majority voting; and from Adam (Kingma & Ba 2015), which divides momentum by the root-mean-square gradient second moment rather than transmitting pure 1-bit signs.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 377 signSGD (Bernstein et al. 2018): phi_sparse=0.0156 vs phi_dense=1.0000, p_single=0.1908 -> p_maj(M=15)=0.0031, asymmetric_sign_bias=-0.3333
```
