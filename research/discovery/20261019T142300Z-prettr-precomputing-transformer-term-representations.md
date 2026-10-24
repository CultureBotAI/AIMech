# Discovery Report: Round 780 — PreTTR Precomputing Transformer Term Representations

- **Timestamp**: `2026-10-19T14:23:00Z`
- **Selected Concept**: `AIMech:PreTTRPrecomputingTermRepresentationsForReranking` (*PreTTR Precomputing Transformer Term Representations*)
- **Record Path**: `data/curated/PreTTRPrecomputingTermRepresentationsForReranking.yaml`
- **Primary Source**: Sean MacAvaney, Franco Maria Nardini, Raffaele Perego, Nicola Tonellotto, Nazli Goharian, Ophir Frieder — *Efficient Document Re-Ranking for Transformers by Precomputing Term Representations* (`https://arxiv.org/bibtex/2004.14255`).

## Identity & Boundary Resolution

Distinct from ColBERT (AIMech:ColBERTContextualizedLateInteraction), which encodes queries and documents completely independently through all Transformer layers and interacts only via a parameter-free sum-of-MaxSim dot-product operator at the output; and distinct from standard cross-encoder Transformer distillation (such as TinyBERT or DistilBERT), which reduces total layer count for both query and document at query time rather than precomputing the first l document layers at index time and executing only the upper n - l interaction layers online.

## Constructed Boundary & Regime Verification

```text
[PASS] PreTTR boundaries verified: decoupled_diff=0.00e+00, compressed_dim=2/4, attn_mse_loss=0.001563
```
