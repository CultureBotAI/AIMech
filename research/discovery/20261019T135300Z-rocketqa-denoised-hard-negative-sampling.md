# Discovery Report: Round 750 — RocketQA (Cross-Batch and Denoised Hard Negative Dense Passage Retrieval Training)

- **Timestamp**: `2026-10-19T13:53:00Z`
- **Selected Concept**: `AIMech:RocketQADenoisedHardNegativeSampling` (*RocketQA (Cross-Batch and Denoised Hard Negative Dense Passage Retrieval Training)*)
- **Record Path**: `data/curated/RocketQADenoisedHardNegativeSampling.yaml`
- **Primary Source**: Yingqi Qu, Yuchen Ding, Jing Liu, Kai Liu, Ruiyang Ren, Wayne Xin Zhao, Daxiang Dong, Hua Wu, Haifeng Wang — *RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering* (`https://dblp.org/search/publ/api?q=RocketQA+An+Optimized+Training+Approach+to+Dense+Passage+Retrieval+Qu&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Qu, Ding, Liu, Liu, Ren, Zhao, Dong, Wu, and Wang (NAACL-HLT 2021, pp. 5835-5847, arXiv:2010.08191). Distinguished from DPR (Karpukhin et al., 2020), which uses single-GPU in-batch negatives and BM25 hard negatives, from ANCE (Xiong et al., 2021), which asynchronously mines top-k dense negatives without cross-encoder denoising (suffering from ~70% false negatives among unannotated top retrieved MS MARCO passages), and from GPL (Wang et al., 2022), which uses synthetic T5 query generation and MarginMSE soft-label distillation for unsupervised target domain adaptation.

## Constructed Boundary & Regime Verification

```text
RocketQA boundary verification passed: {'cross_batch_negs': 4095, 'loss_denoised': 0.0258, 'loss_unfiltered': 1.1106}
```
