# Discovery Report: Round 705 — Hyperdecoder (Encoder-Conditioned Instance-Specific Decoder Adapter Hypernetwork)

- **Timestamp**: `2026-10-19T13:08:00Z`
- **Selected Concept**: `AIMech:HyperdecoderInstanceSpecificDecoderAdapter` (*Hyperdecoder (Encoder-Conditioned Instance-Specific Decoder Adapter Hypernetwork)*)
- **Record Path**: `data/curated/HyperdecoderInstanceSpecificDecoderAdapter.yaml`
- **Primary Source**: Hamish Ivison, Matthew E. Peters — *Hyperdecoders: Instance-specific decoders for multi-task NLP* (`https://dblp.org/search/publ/api?q=Hyperdecoders+Instance-specific+decoders&format=xml`).

## Identity & Boundary Resolution

Introduced by Hamish Ivison and Matthew E. Peters (Findings of EMNLP 2022, pp. 1715-1730, arXiv:2203.08304). Distinct from HyperFormer (Karimi Mahabadi et al., ACL/IJCNLP 2021; AIMech Round 703), which generates sequential adapters for both the encoder and decoder conditioned on learned static task embeddings (producing identical parameters for all instances within a task and requiring task IDs at inference), whereas Hyperdecoder uses non-generated shared parallel adapters in the encoder and generates instance-specific parallel adapters solely in the decoder conditioned on the encoded input text without requiring task embeddings.

## Constructed Boundary & Regime Verification

```text
[PASS] Hyperdecoder boundaries verified: total_params=14731296, inst_diff=10.2337, layer_diff=0.6525, zero_init_err=0.0
```
