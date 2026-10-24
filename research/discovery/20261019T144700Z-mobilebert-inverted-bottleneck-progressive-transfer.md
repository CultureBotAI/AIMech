# Discovery Report: Round 804 — MobileBERT: Compact Task-Agnostic BERT with Bottleneck Structures and Progressive Knowledge Transfer

- **Timestamp**: `2026-10-19T14:47:00Z`
- **Selected Concept**: `AIMech:MobileBERTCompactTaskAgnosticBERTWithBottlenecks` (*MobileBERT: Compact Task-Agnostic BERT with Bottleneck Structures and Progressive Knowledge Transfer*)
- **Record Path**: `data/curated/MobileBERTCompactTaskAgnosticBERTWithBottlenecks.yaml`
- **Primary Source**: Zhiqing Sun, Hongkun Yu, Xiaodan Song, Renjie Liu, Yiming Yang, Denny Zhou — *MobileBERT: a Compact Task-Agnostic BERT for Resource-Limited Devices* (`https://arxiv.org/bibtex/2004.02984`).

## Identity & Boundary Resolution

Introduced by Zhiqing Sun, Hongkun Yu, Xiaodan Song, Renjie Liu, Yiming Yang, and Denny Zhou (ACL 2020, pp. 2158-2170, arXiv:2004.02984, doi:10.18653/v1/2020.acl-main.195). Distinct from shallow-and-wide BERT distillation methods such as DistilBERT (Round 803), BERT-PKD (Round 802), TinyBERT (Round 800), and MiniLM (Round 801): MobileBERT preserves the full 24-layer depth of BERT_LARGE to avoid the capacity loss of depth reduction and narrows intra-block hidden dimensions via matched inter-block linear bottlenecks (d_inter = 512) so that Feature Map Transfer (Eq. 2) and Attention Transfer (Eq. 3) require no auxiliary projection matrices.

## Constructed Boundary & Regime Verification

```text
{"concept": "MobileBERTCompactTaskAgnosticBERTWithBottlenecks", "mha_to_ffn_ratio_1_ffn": 2.0, "mha_to_ffn_ratio_4_ffn": 0.5, "fmt_loss_identical": 0.0, "fmt_loss_perturbed": 0.16000000000000003, "at_loss_identical": 0.0, "at_loss_mismatched": 0.710027, "l_pd_combined": 1.15, "status": "ok"}
```
