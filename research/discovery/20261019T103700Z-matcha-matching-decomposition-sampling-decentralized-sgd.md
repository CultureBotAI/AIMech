# Discovery Report: Round 554 — MATCHA Matching Decomposition Sampling for Decentralized SGD

- **Timestamp**: `2026-10-19T10:37:00Z`
- **Selected Concept**: `AIMech:MatchaMatchingDecompositionSamplingForDecentralizedSgd` (*MATCHA Matching Decomposition Sampling for Decentralized SGD*)
- **Record Path**: `data/curated/MatchaMatchingDecompositionSamplingForDecentralizedSgd.yaml`
- **Primary Source**: Jianyu Wang, Anit Kumar Sahu, Zhouyi Yang, Gauri Joshi, Soummya Kar — *MATCHA: Speeding Up Decentralized SGD via Matching Decomposition Sampling* (`https://dblp.org/rec/journals/corr/abs-1905-09435`).

## Identity & Boundary Resolution

Introduced by Jianyu Wang, Anit Kumar Sahu, Zhouyi Yang, Gauri Joshi, and Soummya Kar (MLSys 2020; arXiv:1905.09435). Distinct from vanilla Decentralized SGD (Lian et al., NeurIPS 2017) and Periodic DecenSGD, which activate all edges of the base graph simultaneously with equal frequency; and distinct from Stochastic Gradient Push (Assran et al., ICML 2019), which uses a deterministic time-varying directed exponential graph rather than algebraic-connectivity-optimized random matching decomposition.

## Constructed Boundary & Regime Verification

```text
[PASS] MATCHA boundaries verified: L_j^2==2*L_j exact, Eq(26) exact, rho_matcha=0.8069 < rho_bad=0.9551 < 1.0
```
