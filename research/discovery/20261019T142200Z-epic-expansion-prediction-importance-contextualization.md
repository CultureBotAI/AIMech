# Discovery Report: Round 779 — EPIC Expansion via Prediction of Importance with Contextualization

- **Timestamp**: `2026-10-19T14:22:00Z`
- **Selected Concept**: `AIMech:EPICExpansionViaPredictionOfImportanceWithContextualization` (*EPIC Expansion via Prediction of Importance with Contextualization*)
- **Record Path**: `data/curated/EPICExpansionViaPredictionOfImportanceWithContextualization.yaml`
- **Primary Source**: Sean MacAvaney, Franco Maria Nardini, Raffaele Perego, Nicola Tonellotto, Nazli Goharian, Ophir Frieder — *Expansion via Prediction of Importance with Contextualization* (`https://arxiv.org/bibtex/2004.14245`).

## Identity & Boundary Resolution

Distinct from SPLADE (AIMech:SPLADESparseLexicalAndExpansionModel), which applies log(1 + ReLU(.)) directly to MLM logits with explicit FLOPS regularization for first-stage inverted-index retrieval without separate token-salience factors w_d(t_j) or a sigmoid [CLS] document-quality gate c(d); and distinct from SPARTA (AIMech:SPARTASparseTransformerMatchingForRetrieval), which computes non-contextualized query-to-contextualized-document token max dot products followed by ReLU(b + .) and log(1 + .) without query contextualization or a learned vocabulary expansion projection matrix Theta_2.

## Constructed Boundary & Regime Verification

```text
[PASS] EPIC boundaries verified: phi_d_pos['cost']=1.1773, score_pos=2.6711 (pruned=2.6711) > score_neg=0.2785
```
