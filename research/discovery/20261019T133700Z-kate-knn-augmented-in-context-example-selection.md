# Discovery Report: Round 734 — KATE kNN-Augmented In-Context Example Selection

- **Timestamp**: `2026-10-19T13:37:00Z`
- **Selected Concept**: `AIMech:KATEkNNAugmentedInContextExampleSelection` (*KATE kNN-Augmented In-Context Example Selection*)
- **Record Path**: `data/curated/KATEkNNAugmentedInContextExampleSelection.yaml`
- **Primary Source**: Jiachang Liu, Dinghan Shen, Yizhe Zhang, Bill Dolan, Lawrence Carin, Weizhu Chen — *What Makes Good In-Context Examples for GPT-3?* (`https://dblp.org/search/publ/api?q=What+Makes+Good+In-Context+Examples+for+GPT-3+Liu&h=5&format=xml`).

## Identity & Boundary Resolution

Distinct from datastore-interpolated language modeling such as kNN-LM and kNN-MT, which interpolate a language model's next-token output probability distribution with a non-parametric kNN distribution over cached hidden states, because KATE operates purely at the input prompt level using an external sentence encoder without accessing the target language model's internal hidden states or modifying its decoding distribution. Also distinct from LM-scored contrastive prompt retrieval (AIMech:EPREfficientPromptRetrievalForInContextLearning), which trains a custom bi-encoder using positive and hard-negative labels scored by the target language model itself.

## Constructed Boundary & Regime Verification

```text
KATE verification passed: KATE_acc=1.00, random_mean=0.38, farthest_acc=0.00
```
