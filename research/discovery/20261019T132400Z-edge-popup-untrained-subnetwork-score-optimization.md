# Discovery Report: Round 721 — Edge-Popup Untrained Subnetwork Score Optimization

- **Timestamp**: `2026-10-19T13:24:00Z`
- **Selected Concept**: `AIMech:EdgePopupUntrainedSubnetworkScoreOptimization` (*Edge-Popup Untrained Subnetwork Score Optimization*)
- **Record Path**: `data/curated/EdgePopupUntrainedSubnetworkScoreOptimization.yaml`
- **Primary Source**: Vivek Ramanujan, Mitchell Wortsman, Aniruddha Kembhavi, Ali Farhadi, Mohammad Rastegari — *What's Hidden in a Randomly Weighted Neural Network?* (`https://dblp.org/search/publ/api?q=What%27s+Hidden+in+a+Randomly+Weighted+Neural+Network+Ramanujan&format=xml`).

## Identity & Boundary Resolution

Distinct from stochastic Bernoulli supermask sampling (Zhou et al., NeurIPS 2019), which samples binary masks stochastically on every forward pass and suffers high gradient variance at scale, from Discovering Neural Wirings (DNW, Wortsman et al., NeurIPS 2019), which selects top-k% edges by weight magnitude while modifying the weights themselves, from Piggyback (AIMech:PiggybackBinaryWeightMaskMultiTaskAdaptation), which thresholds masks on ImageNet-pretrained backbones with a trained linear classifier head, and from SupSup (AIMech:SupSupSupermasksInSuperposition), which extends Edge-Popup to multi-task superposition and one-shot entropy-based task inference.

## Constructed Boundary & Regime Verification

```text
Edge-Popup verification passed.
```
