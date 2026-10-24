# Discovery Report: Round 777 — CLEAR Complementing Lexical Retrieval with Semantic Residual Embedding

- **Timestamp**: `2026-10-19T14:20:00Z`
- **Selected Concept**: `AIMech:CLEARComplementingLexicalRetrievalWithSemanticResidualEmbedding` (*CLEAR Complementing Lexical Retrieval with Semantic Residual Embedding*)
- **Record Path**: `data/curated/CLEARComplementingLexicalRetrievalWithSemanticResidualEmbedding.yaml`
- **Primary Source**: Luyu Gao, Zhuyun Dai, Tongfei Chen, Zhen Fan, Benjamin Van Durme, Jamie Callan — *Complementing Lexical Retrieval with Semantic Residual Embedding* (`https://arxiv.org/bibtex/2004.13969`).

## Identity & Boundary Resolution

Distinct from post-hoc score interpolation of independently trained BM25 and dense dual-encoder models (such as DPR + BM25 in AIMech:DensePassageRetrieval or ME-BERT hybrids in AIMech:MEBERTMultiVectorDenseRetrieval), where the dense encoder is trained independently without conditioning its loss margin on the lexical score difference s_lex(q, d+) - s_lex(q, d-).

## Constructed Boundary & Regime Verification

```text
[PASS] CLEAR boundaries verified: m_r_easy=-0.40 (loss=0.00), m_r_hard=1.80 > xi=1.00, clear_pos=10.25 > clear_neg=8.75
```
