# Discovery Report: Round 737 — Self-Adaptive In-Context Learning

- **Timestamp**: `2026-10-19T13:40:00Z`
- **Selected Concept**: `AIMech:SelfAdaptiveInContextLearning` (*Self-Adaptive In-Context Learning*)
- **Record Path**: `data/curated/SelfAdaptiveInContextLearning.yaml`
- **Primary Source**: Zhiyong Wu, Yaoxiang Wang, Jiacheng Ye, Lingpeng Kong — *Self-Adaptive In-Context Learning: An Information Compression Perspective for In-Context Example Selection and Ordering* (`https://dblp.org/search/publ/api?q=Self-Adaptive+In-Context+Learning+Zhiyong+Wu&h=5&format=xml`).

## Identity & Boundary Resolution

Distinct from corpus-level entropy prompt ordering (AIMech:GlobalEAndLocalEEntropyBasedPromptOrdering), which selects a single demonstration permutation for the entire dataset by maximizing predictive entropy over a generated probing set, whereas Self-Adaptive In-Context Learning selects a custom combination and ordering per test instance by minimizing predictive codelength (entropy). Also distinct from single-stage nearest-neighbor selection (AIMech:KATEkNNAugmentedInContextExampleSelection), which fixes a single distance-based ordering without MDL organization ranking.

## Constructed Boundary & Regime Verification

```text
Self-Adaptive ICL (TopK+MDL) verification passed: MDL_acc=1.00, avg_MDL_bits=0.2368, LocalE_acc=0.33
```
