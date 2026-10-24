# Discovery Report: Round 798 — LM Distill + Ranker Distill (Two-Round Knowledge Distillation for BERT Rankers)

- **Timestamp**: `2026-10-19T14:41:00Z`
- **Selected Concept**: `AIMech:LMDistillPlusRankerDistillForBERTRankers` (*LM Distill + Ranker Distill (Two-Round Knowledge Distillation for BERT Rankers)*)
- **Record Path**: `data/curated/LMDistillPlusRankerDistillForBERTRankers.yaml`
- **Primary Source**: Luyu Gao, Zhuyun Dai, Jamie Callan — *Understanding BERT Rankers Under Distillation* (`https://arxiv.org/bibtex/2007.11088`).

## Identity & Boundary Resolution

Distinct from single-stage Ranker Distill (which distills a fine-tuned BERT ranker directly onto a randomly initialized student and fails to recover general language modeling knowledge) and from LM Distill + Fine-tuning (which fine-tunes a distilled LM directly on hard search labels and degrades or overfits under high compression such as 4-layer H=312 students). By pairing LM Distill initialization with Ranker Distill intermediate-attention and output supervision, LM Distill + Ranker Distill prevents overfitting past 5M training pairs and achieves statistical non-inferiority on both 6-layer (H=768) and 4-layer (H=312) rankers.

## Constructed Boundary & Regime Verification

```text
LM Distill + Ranker Distill boundary verification passed:
  4L LM+Ranker Distill MRR@10=0.3501 (non-inferior to BERT-12 0.3527)
  Attention KL (LM-init vs random): 0.0053 < 0.2766
  4L Depth-100 throughput: 30.3 QPS with 3.57% MRR@10 drop
```
