# Discovery Report: Round 551 — ByRDiE Byzantine-Resilient Distributed Coordinate Descent for Decentralized Learning

- **Timestamp**: `2026-10-19T10:34:00Z`
- **Selected Concept**: `AIMech:ByrdieByzantineResilientDistributedCoordinateDescentForDecentralizedLearning` (*ByRDiE Byzantine-Resilient Distributed Coordinate Descent for Decentralized Learning*)
- **Record Path**: `data/curated/ByrdieByzantineResilientDistributedCoordinateDescentForDecentralizedLearning.yaml`
- **Primary Source**: Zhixiong Yang, Waheed U. Bajwa — *ByRDiE: Byzantine-resilient Distributed Coordinate Descent for Decentralized Learning* (`https://dblp.org/rec/journals/tsipn/YangB19`).

## Identity & Boundary Resolution

Introduced by Zhixiong Yang and Waheed U. Bajwa (IEEE Transactions on Signal and Information Processing over Networks, Vol. 5, No. 4, pp. 611-627, 2019; arXiv:1708.08155). Distinct from BRIDGE (Fang, Yang, & Bajwa, IEEE TSIPN 2022, Round 546), which performs simultaneous full-vector gradient descent with coordinate-wise trimmed mean in a single loop rather than sequential coordinate-by-coordinate T-step inner updates; and distinct from ClippedGossip (He, Karimireddy, & Jaggi, 2022, Round 545), which clips neighbor model differences in L2 norm around a node's own iterate.

## Constructed Boundary & Regime Verification

```text
[PASS] ByRDiE boundaries verified: max_err=4.02e-12, consensus_gap=0.00e+00, unscreened_err=244.1
```
