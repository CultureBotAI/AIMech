# Discovery Report: Round 744 — UPR (Unsupervised Passage Re-ranking with Zero-Shot Question Generation)

- **Timestamp**: `2026-10-19T13:47:00Z`
- **Selected Concept**: `AIMech:UPRUnsupervisedPassageRerankingWithQuestionGeneration` (*UPR (Unsupervised Passage Re-ranking with Zero-Shot Question Generation)*)
- **Record Path**: `data/curated/UPRUnsupervisedPassageRerankingWithQuestionGeneration.yaml`
- **Primary Source**: Devendra Singh Sachan, Mike Lewis, Mandar Joshi, Armen Aghajanyan, Wen-tau Yih, Joelle Pineau, Luke Zettlemoyer — *Improving Passage Retrieval with Zero-Shot Question Generation* (`https://dblp.org/search/publ/api?q=Improving+Passage+Retrieval+with+Zero-Shot+Question+Generation+Sachan&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Sachan, Lewis, Joshi, Aghajanyan, Yih, Pineau, and Zettlemoyer (EMNLP 2022, pp. 3781-3797, arXiv:2204.07496). Distinguished from classical unigram query-likelihood language models (Ponte & Croft, 1998; Zhai & Lafferty, 2001), from supervised relevance-token cross-encoders such as monoT5 (Nogueira et al., 2020), and from synthetic query-generation dataset augmentation methods such as Doc2Query, InPars, or Promptagator that train a downstream retriever rather than re-scoring test queries zero-shot via p(q | z_i).

## Constructed Boundary & Regime Verification

```text
UPR boundary verification passed: {'upr_z2': -0.7248, 'upr_z1': -2.588}
```
