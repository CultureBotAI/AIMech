# Discovery Report: Round 806 — DynaBERT: Dynamic BERT with Adaptive Width and Depth

- **Timestamp**: `2026-10-19T14:49:00Z`
- **Selected Concept**: `AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth` (*DynaBERT: Dynamic BERT with Adaptive Width and Depth*)
- **Record Path**: `data/curated/DynaBERTDynamicBERTWithAdaptiveWidthAndDepth.yaml`
- **Primary Source**: Lu Hou, Zhiqi Huang, Lifeng Shang, Xin Jiang, Xiao Chen, Qun Liu — *DynaBERT: Dynamic BERT with Adaptive Width and Depth* (`https://arxiv.org/bibtex/2004.04037`).

## Identity & Boundary Resolution

Introduced by Lu Hou, Zhiqi Huang, Lifeng Shang, Xin Jiang, Xiao Chen, and Qun Liu (NeurIPS 2020, arXiv:2004.04037). Distinct from fixed-size BERT compression methods such as TinyBERT (Round 800), MiniLM (Round 801), BERT-PKD (Round 802), DistilBERT (Round 803), MobileBERT (Round 804), and BERT-of-Theseus (Round 805), and from depth-only early-exit or layer-dropping methods such as FastBERT (Round 807), PABEE (Round 808), and LayerDrop: DynaBERT adapts both Transformer width (via parallel head and FFN-neuron slicing in Eqs. 1-2 after Taylor-importance network rewiring) and depth (via strided layer dropping and last-layer-preserving hidden-state matching in Eq. 4) inside a single deployed checkpoint.

## Constructed Boundary & Regime Verification

```text
{"concept": "DynaBERTDynamicBERTWithAdaptiveWidthAndDepth", "num_subnetwork_configs": 12, "top2_importance_unrewired": 1.8, "top2_importance_rewired": 4.1, "dropped_layers_md_075": [4, 8, 12], "teacher_matched_layers_md_075": [1, 2, 4, 5, 6, 8, 9, 10, 12], "dropped_layers_md_050": [2, 4, 6, 8, 10, 12], "teacher_matched_layers_md_050": [2, 4, 6, 8, 10, 12], "status": "ok"}
```
