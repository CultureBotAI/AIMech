# Discovery Report: Round 545 — ClippedGossip Self-Centered Clipping for Byzantine-Robust Decentralized Learning

- **Timestamp**: `2026-10-19T10:28:00Z`
- **Selected Concept**: `AIMech:ClippedGossipSelfCenteredClippingForByzantineRobustDecentralizedLearning` (*ClippedGossip Self-Centered Clipping for Byzantine-Robust Decentralized Learning*)
- **Record Path**: `data/curated/ClippedGossipSelfCenteredClippingForByzantineRobustDecentralizedLearning.yaml`
- **Primary Source**: Lie He, Sai Praneeth Karimireddy, Martin Jaggi — *Byzantine-Robust Decentralized Learning via ClippedGossip* (`https://dblp.org/rec/journals/corr/abs-2202-01545`).

## Identity & Boundary Resolution

Distinct from server-based Byzantine clipping and bucketing aggregators (such as AIMech:BucketingForAgnosticByzantineRobustAggregationOnHeterogeneousDatasets and AIMech:CrflCertifiablyRobustFederatedLearningViaParameterClippingAndSmoothing) and from decentralized coordinate-wise trimmed-mean / median / Krum screening in BRIDGE (AIMech:BridgeByzantineResilientDecentralizedGradientDescent): ClippedGossip (also termed Self-Centered Clipping; He, Karimireddy, & Jaggi, 2022) clips each neighbor j's model relative to node i's own trusted state x_i^{t+1/2} weighted by doubly stochastic mixing weights W_{ij}, eliminating the requirement of an honest majority in every node's neighborhood and preserving information diffusion across sparse graph cuts (such as a dumbbell bridge) where coordinate-wise trimmed mean and geometric median stall.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 545 ClippedGossip verified: dissensus_gossip_progress=0.0, var_ClippedGossip=0.00 << var_TM=10000.00 (init=10000.0)
```
