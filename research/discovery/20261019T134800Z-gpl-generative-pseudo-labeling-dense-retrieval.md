# Discovery Report: Round 745 — GPL (Generative Pseudo Labeling for Unsupervised Domain Adaptation of Dense Retrieval)

- **Timestamp**: `2026-10-19T13:48:00Z`
- **Selected Concept**: `AIMech:GPLGenerativePseudoLabelingForDenseRetrieval` (*GPL (Generative Pseudo Labeling for Unsupervised Domain Adaptation of Dense Retrieval)*)
- **Record Path**: `data/curated/GPLGenerativePseudoLabelingForDenseRetrieval.yaml`
- **Primary Source**: Kexin Wang, Nandan Thakur, Nils Reimers, Iryna Gurevych — *GPL: Generative Pseudo Labeling for Unsupervised Domain Adaptation of Dense Retrieval* (`https://dblp.org/search/publ/api?q=GPL+Generative+Pseudo+Labeling+for+Unsupervised+Domain+Adaptation+Wang&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Wang, Thakur, Reimers, and Gurevych (NAACL-HLT 2022, pp. 2345-2360, arXiv:2112.07577). Distinguished from QGen (Ma et al., 2021; Thakur et al., 2021), which trains on generated queries with binary 0-1 MultipleNegativesRanking loss (MNRL) and degrades when combined with hard negatives, and from InPars (Bonifacio et al., 2022) or Promptagator (Dai et al., 2023), which rely on few-shot LLM prompt generation and top-k likelihood or dual-encoder consistency filtering rather than cross-encoder MarginMSE soft-margin distillation.

## Constructed Boundary & Regime Verification

```text
GPL boundary verification passed: {'loss_false_neg_gpl': 0.01, 'loss_true_neg_gpl': 64.0}
```
