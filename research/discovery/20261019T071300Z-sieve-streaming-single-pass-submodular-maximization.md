# Discovery Report: Round 350 — Sieve-Streaming and Sieve-Streaming++ for Single-Pass Monotone Submodular Maximization

- **Timestamp**: `2026-10-19T07:13:00Z`
- **Selected Concept**: `AIMech:SieveStreamingAndSieveStreamingPlusPlusForSubmodularMaximization` (*Sieve-Streaming and Sieve-Streaming++ for Single-Pass Monotone Submodular Maximization*)
- **Record Path**: `data/curated/SieveStreamingAndSieveStreamingPlusPlusForSubmodularMaximization.yaml`
- **Primary Source**: Ehsan Kazemi, Marko Mitrovic, Morteza Zadimoghaddam, Silvio Lattanzi, Amin Karbasi — *Submodular Streaming in All Its Glory: Tight Approximation, Minimum Memory and Low Adaptive Complexity* (`https://api.crossref.org/works/10.1145/2623330.2623637`).

## Identity & Boundary Resolution

Distinct from Stochastic-Greedy Linear-Time Monotone Submodular Maximization (`AIMech:StochasticGreedyLinearTimeMonotoneSubmodularMaximization`), which requires random-access memory to the entire ground set V across k sequential passes to achieve (1 - 1/e - varepsilon), whereas Sieve-Streaming and Sieve-Streaming++ process an arbitrarily long stream V in a single pass with O(k / varepsilon) memory independent of n = |V| and achieve the tight 1/2 - varepsilon single-pass streaming ratio.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 350 Sieve-Streaming & Sieve-Streaming++ (Badanidiyuru et al. 2014; Kazemi et al. 2019): val_ss=79.4891, val_sspp=79.4891 >= (1/2-eps)*OPT_ub=35.0671, mem_ss=132 -> mem_sspp=122 (7.6% reduction)
```
