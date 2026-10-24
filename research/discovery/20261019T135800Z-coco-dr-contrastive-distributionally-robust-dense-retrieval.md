# Discovery Report: Round 755 — COCO-DR Contrastive and Distributionally Robust Zero-Shot Dense Retrieval

- **Timestamp**: `2026-10-19T13:58:00Z`
- **Selected Concept**: `AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning` (*COCO-DR Contrastive and Distributionally Robust Zero-Shot Dense Retrieval*)
- **Record Path**: `data/curated/COCODRDenseRetrievalDistributionallyRobustContrastiveLearning.yaml`
- **Primary Source**: Yue Yu, Chenyan Xiong, Si Sun, Chao Zhang, Arnold Overwijk — *COCO-DR: Combating Distribution Shifts in Zero-Shot Dense Retrieval with Contrastive and Distributionally Robust Learning* (`https://arxiv.org/bibtex/2210.15212`).

## Identity & Boundary Resolution

Distinct from coCondenser (Gao & Callan, ACL 2022, AIMech:CoCondenserUnsupervisedCorpusAwareLanguageModelPreTraining), which pre-trains on the source corpus (e.g., MS MARCO) and fine-tunes with uniform Empirical Risk Minimization without target-corpus adaptation or iDRO query-cluster reweighting; distinct from GPL (Wang et al., NAACL 2022, AIMech:GPLGenerativePseudoLabelingForDenseRetrieval), which generates synthetic queries and cross-encoder pseudo-labels to train a separate model per target task rather than a single unified zero-shot model; and distinct from GroupDRO (Sagawa et al., ICLR 2020, AIMech:GroupDistributionallyRobustOptimization), which weights groups solely by loss magnitude without the cross-cluster gradient dot-product similarity r_{ij}.

## Constructed Boundary & Regime Verification

```text
Round 755 COCO-DR boundary verification passed.
```
