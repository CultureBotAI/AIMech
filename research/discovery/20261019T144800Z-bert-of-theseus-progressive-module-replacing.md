# Discovery Report: Round 805 — BERT-of-Theseus: Compressing BERT by Progressive Module Replacing

- **Timestamp**: `2026-10-19T14:48:00Z`
- **Selected Concept**: `AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing` (*BERT-of-Theseus: Compressing BERT by Progressive Module Replacing*)
- **Record Path**: `data/curated/BERToftheseusCompressingBERTByProgressiveModuleReplacing.yaml`
- **Primary Source**: Canwen Xu, Wangchunshu Zhou, Tao Ge, Furu Wei, Ming Zhou — *BERT-of-Theseus: Compressing BERT by Progressive Module Replacing* (`https://arxiv.org/bibtex/2002.02925`).

## Identity & Boundary Resolution

Introduced by Canwen Xu, Wangchunshu Zhou, Tao Ge, Furu Wei, and Ming Zhou (EMNLP 2020, pp. 7859-7869, arXiv:2002.02925, doi:10.18653/v1/2020.emnlp-main.633). Distinct from knowledge distillation methods such as TinyBERT (Round 800), MiniLM (Round 801), BERT-PKD (Round 802), DistilBERT (Round 803), and MobileBERT (Round 804): BERT-of-Theseus requires zero auxiliary feature-matching, attention-matching, or logit KL-divergence losses and no balancing hyperparameters between task and distillation losses, relying instead on closed-loop gradient interactions between frozen predecessor modules and trainable successor modules inside the hybrid computational graph.

## Constructed Boundary & Regime Verification

```text
{"concept": "BERToftheseusCompressingBERTByProgressiveModuleReplacing", "num_modules": 6, "num_hybrid_paths": 64, "y_predecessor_only": 3.984192, "y_hybrid_mid_curriculum": 3.518925, "y_successor_only": 3.158203, "curriculum_transition_step": 9000, "effective_lr_t0": 2.0000000000000003e-06, "effective_lr_t9000": 2e-05, "status": "ok"}
```
