# Discovery Report: Round 739 — CEIL Compositional Exemplars for In-Context Learning

- **Timestamp**: `2026-10-19T13:42:00Z`
- **Selected Concept**: `AIMech:CEILCompositionalExemplarsForInContextLearning` (*CEIL Compositional Exemplars for In-Context Learning*)
- **Record Path**: `data/curated/CEILCompositionalExemplarsForInContextLearning.yaml`
- **Primary Source**: Jiacheng Ye, Zhiyong Wu, Jiangtao Feng, Tao Yu, Lingpeng Kong — *Compositional Exemplars for In-context Learning* (`https://dblp.org/search/publ/api?q=Compositional+Exemplars+for+In-context+Learning+Ye&h=5&format=xml`).

## Identity & Boundary Resolution

Distinct from singleton dense prompt retrieval (AIMech:EPREfficientPromptRetrievalForInContextLearning) and kNN example selection (AIMech:KATEkNNAugmentedInContextExampleSelection), which score and retrieve each demonstration independently and can select redundant near-duplicate examples, whereas CEIL optimizes the determinant of a conditional DPP submatrix log det(L'_S) = (1/lambda) sum_{i in S} r_i + log det(L_S) to capture negative pairwise interactions and compositional coverage across the selected subset.

## Constructed Boundary & Regime Verification

```text
CEIL verification passed: TopK_set=[0, 1] (log_det=1.1233) vs CEIL_MAP_set=[0, 2] (log_det=5.6000)
```
