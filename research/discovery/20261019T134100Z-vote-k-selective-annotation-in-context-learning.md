# Discovery Report: Round 738 — Vote-k Selective Annotation for In-Context Learning

- **Timestamp**: `2026-10-19T13:41:00Z`
- **Selected Concept**: `AIMech:VoteKSelectiveAnnotationForInContextLearning` (*Vote-k Selective Annotation for In-Context Learning*)
- **Record Path**: `data/curated/VoteKSelectiveAnnotationForInContextLearning.yaml`
- **Primary Source**: Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf, Luke Zettlemoyer, Noah A. Smith, Tao Yu — *Selective Annotation Makes Language Models Better Few-Shot Learners* (`https://dblp.org/search/publ/api?q=Selective+Annotation+Makes+Language+Models+Better+Few-Shot+Learners+Su&h=5&format=xml`).

## Identity & Boundary Resolution

Distinct from test-time prompt retrieval methods such as KATE (AIMech:KATEkNNAugmentedInContextExampleSelection) and EPR (AIMech:EPREfficientPromptRetrievalForInContextLearning), which assume the entire training pool is already annotated and select prompts per test query, whereas Vote-k operates before annotation to choose a compact, diverse, and representative subset L of size M from an unlabeled pool X to be human-annotated. Also distinct from pure facility-location or greedy embedding-diversity coreset selection, which do not combine exponentially discounted kNN graph voting with in-context LM confidence stratification.

## Constructed Boundary & Regime Verification

```text
Vote-k verification passed: selected_clusters=[0, 1, 2] (vs undiscounted=[0])
```
