# Discovery Report: Round 735 — EPR Efficient Prompt Retrieval for In-Context Learning

- **Timestamp**: `2026-10-19T13:38:00Z`
- **Selected Concept**: `AIMech:EPREfficientPromptRetrievalForInContextLearning` (*EPR Efficient Prompt Retrieval for In-Context Learning*)
- **Record Path**: `data/curated/EPREfficientPromptRetrievalForInContextLearning.yaml`
- **Primary Source**: Ohad Rubin, Jonathan Herzig, Jonathan Berant — *Learning To Retrieve Prompts for In-Context Learning* (`https://dblp.org/search/publ/api?q=Learning+To+Retrieve+Prompts+for+In-Context+Learning+Rubin&h=5&format=xml`).

## Identity & Boundary Resolution

Distinct from unsupervised or transfer sentence-embedding nearest-neighbor retrieval (AIMech:KATEkNNAugmentedInContextExampleSelection), which does not use language-model conditional decoding probabilities to supervise the retriever. Also distinct from determinantal point process subset selection (CEIL), which models pairwise diversity and joint subset interactions across multiple exemplars rather than scoring individual prompt candidates independently.

## Constructed Boundary & Regime Verification

```text
EPR verification passed: loss_init=0.9300 -> loss_final=0.0052, sim_structural=7.9467 > sim_surface=1.7584
```
