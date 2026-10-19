# Discovery Report: Round 359 — GreeDi Two-Stage Distributed Greedy Submodular Maximization

- **Timestamp**: `2026-10-19T07:22:00Z`
- **Selected Concept**: `AIMech:GreeDiTwoStageDistributedSubmodularMaximization` (*GreeDi Two-Stage Distributed Greedy Submodular Maximization*)
- **Record Path**: `data/curated/GreeDiTwoStageDistributedSubmodularMaximization.yaml`
- **Primary Source**: Baharan Mirzasoleiman, Amin Karbasi, Rik Sarkar, Andreas Krause — *Distributed Submodular Maximization* (`https://jmlr.org/papers/v17/mirzasoleiman16a.html`).

## Identity & Boundary Resolution

Distinct from AIMech:StochasticGreedyLinearTimeMonotoneSubmodularMaximization (Round 348), which accelerates centralized sequential greedy selection by random subsampling on a single machine, and from AIMech:SieveStreamingAndSieveStreamingPlusPlusForSubmodularMaximization (Round 350), which processes elements in a single streaming pass using Geometric marginal-gain thresholds. Also distinct from AIMech:ContinuousGreedyAndMultilinearExtensionForMatroidSubmodularMaximization (Round 349), which solves continuous multilinear relaxations over matroid polytopes centrally rather than two-round distributed MapReduce partitioning.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 359 GreeDi Distributed Submodular (Mirzasoleiman et al. 2016): wc_ratio=0.3333==1/min(m,k), lip_lhs=0.0000<=lip_rhs=0.2400, greedi=19.9771>=thm8_bound=12.5521 (opt=19.9771)
```
