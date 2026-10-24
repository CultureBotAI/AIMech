# Discovery Report: Round 803 — DistilBERT: Knowledge Distillation During Pre-training

- **Timestamp**: `2026-10-19T14:46:00Z`
- **Selected Concept**: `AIMech:DistilBERTKnowledgeDistillationDuringPretraining` (*DistilBERT: Knowledge Distillation During Pre-training*)
- **Record Path**: `data/curated/DistilBERTKnowledgeDistillationDuringPretraining.yaml`
- **Primary Source**: Victor Sanh, Lysandre Debut, Julien Chaumond, Thomas Wolf — *DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter* (`https://arxiv.org/bibtex/1910.01108`).

## Identity & Boundary Resolution

Introduced by Sanh, Debut, Chaumond, and Wolf (NeurIPS 2019 Workshop on Energy Efficient Machine Learning and Cognitive Computing, EMC^2, arXiv:1910.01108). Distinct from task-specific fine-tuning distillation methods such as BERT-PKD (Round 802, which distills normalized intermediate patience representations during downstream fine-tuning), from TinyBERT (Round 800, which enforces MSE on layer-wise attention matrices and projected hidden states across both pre-training and data-augmented fine-tuning), and from MiniLM (Round 801, which transfers only the last layer's query-key attention and value-relation distributions without intermediate layer initialization or cosine hidden-state loss). DistilBERT retains identical hidden dimension d between teacher and student so that every other teacher layer directly initializes a corresponding student layer without linear projection matrices.

## Constructed Boundary & Regime Verification

```text
{"concept": "DistilBERTKnowledgeDistillationDuringPretraining", "non_top1_mass_T1": 0.112306, "non_top1_mass_T4": 0.52143, "kl_good_T4": 0.00029, "kl_bad_dark_T4": 0.185142, "l_cos_collinear": 0.0, "l_cos_misaligned": 0.977622, "triple_loss_init": 3.562764, "triple_loss_trained": 0.35029, "bert_base_params": 109482240, "distilbert_params": 66362880, "param_reduction_fraction": 0.3938, "status": "ok"}
```
