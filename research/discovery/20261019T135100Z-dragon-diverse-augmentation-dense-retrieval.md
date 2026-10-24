# Discovery Report: Round 748 — DRAGON (Diverse Augmentation for Generalizable Dense Retrieval)

- **Timestamp**: `2026-10-19T13:51:00Z`
- **Selected Concept**: `AIMech:DRAGONDiverseAugmentationGeneralizableDenseRetrieval` (*DRAGON (Diverse Augmentation for Generalizable Dense Retrieval)*)
- **Record Path**: `data/curated/DRAGONDiverseAugmentationGeneralizableDenseRetrieval.yaml`
- **Primary Source**: Sheng-Chieh Lin, Akari Asai, Minghan Li, Barlas Oguz, Jimmy Lin, Yashar Mehdad, Wen-tau Yih, Xilun Chen — *How to Train Your DRAGON: Diverse Augmentation Towards Generalizable Dense Retrieval* (`https://dblp.org/search/publ/api?q=How+to+Train+Your+DRAGON+Diverse+Augmentation+Lin&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Lin, Asai, Li, Oguz, Lin, Mehdad, Yih, and Chen (Findings of EMNLP 2023, pp. 6385-6400, arXiv:2302.07452). Distinguished from single-teacher cross-encoder distillation methods (such as RocketQAv2, CL-DRD, or GPL) which rely on computationally expensive cross-encoder soft labels, and from unsupervised contrastive pre-training (such as Contriever or coCondenser) which assumes the originating document is the sole positive for a cropped span.

## Constructed Boundary & Regime Verification

```text
DRAGON boundary verification passed: {'union_sizes': [4, 6, 9], 'p_consensus': 0.25}
```
