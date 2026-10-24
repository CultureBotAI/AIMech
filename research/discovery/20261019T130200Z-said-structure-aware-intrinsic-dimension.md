# Discovery Report: Round 699 — Structure-Aware Intrinsic Dimension (SAID)

- **Timestamp**: `2026-10-19T13:02:00Z`
- **Selected Concept**: `AIMech:SAIDStructureAwareIntrinsicDimension` (*Structure-Aware Intrinsic Dimension (SAID)*)
- **Record Path**: `data/curated/SAIDStructureAwareIntrinsicDimension.yaml`
- **Primary Source**: Armen Aghajanyan, Luke Zettlemoyer, Sonal Gupta — *Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning* (`https://dblp.org/search/publ/api?q=Intrinsic+Dimensionality+Explains+the+Effectiveness+of+Language+Model+Fine-Tuning&format=xml`).

## Identity & Boundary Resolution

Introduced by Armen Aghajanyan, Luke Zettlemoyer, and Sonal Gupta (ACL/IJCNLP 2021, pp. 7319-7328, arXiv:2012.13255). Extends the layer-unaware Direct Intrinsic Dimension (DID) objective-landscape subspace method of Li et al. (ICLR 2018, theta^D = theta^D_0 + theta^d M with Fastfood matrix M = H G Pi H B) by trading m subspace parameters for m layer-wise scaling weights lambda_i across m layers so capacity concentrates on task-relevant layers. Both SAID and its layer-unaware baseline DID for pre-trained model fine-tuning are covered together in this record.

## Constructed Boundary & Regime Verification

```text
[PASS] SAID boundary verification passed: fwht_err=8.9e-16, mse_SAID=0.0e+00 << mse_DID=0.2511, bound_RoBERTa_Large(d90=207)=0.7877 < bound_RoBERTa_Base(d90=896)=1.6388
```
