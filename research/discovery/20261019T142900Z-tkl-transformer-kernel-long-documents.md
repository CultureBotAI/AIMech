# Discovery Report: Round 786 — TKL: Transformer-Kernel Model with Local Self-Attention for Long Document Retrieval

- **Timestamp**: `2026-10-19T14:29:00Z`
- **Selected Concept**: `AIMech:TKLTransformerKernelForLongDocuments` (*TKL: Transformer-Kernel Model with Local Self-Attention for Long Document Retrieval*)
- **Record Path**: `data/curated/TKLTransformerKernelForLongDocuments.yaml`
- **Primary Source**: Sebastian Hofstätter, Hamed Zamani, Bhaskar Mitra, Nick Craswell, Allan Hanbury — *Local Self-Attention over Long Text for Efficient Document Retrieval* (`https://arxiv.org/bibtex/2005.04908`).

## Identity & Boundary Resolution

Distinct from the short-text TK model (AIMech:TKTransformerKernelModelForReRanking, which applies full self-attention over the first ~200 tokens and uses fixed log saturation over the entire document). TKL introduces overlapping local self-attention windows with minibatch padding-chunk skipping, a learned non-linear power saturation function conditioned on query-term salience e_i and region token count c_len, and two-stage local/global topography pooling via top-local-max_{t,f}.

## Constructed Boundary & Regime Verification

```text
TKL boundary verification passed:
  Packed non-padding windows: 2 (from 4 total chunks)
  Learned saturation values:  s(1)=0.000000, s(4)=0.043236, s(8)=0.065067
  Top-2 local maxima indices: [14, 3]
```
