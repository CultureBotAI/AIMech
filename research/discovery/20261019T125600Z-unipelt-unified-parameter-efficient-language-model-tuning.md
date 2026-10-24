# Discovery Report: Round 693 — UniPELT

- **Timestamp**: `2026-10-19T12:56:00Z`
- **Selected Concept**: `AIMech:UniPELT` (*UniPELT*)
- **Record Path**: `data/curated/UniPELT.yaml`
- **Primary Source**: Yuning Mao, Lambert Mathias, Rui Hou, Amjad Almahairi, Hao Ma, Jiawei Han, Wen-tau Yih, Madian Khabsa — *UniPELT: A Unified Framework for Parameter-Efficient Language Model Tuning* (`https://dblp.org/search/publ/api?q=UniPELT+Unified+Framework+Mao&format=xml`).

## Identity & Boundary Resolution

Distinct from individual PELT methods (AIMech:LowRankAdaptation, AIMech:PrefixTuning, AIMech:BottleneckAdapter, AIMech:BitFit), which modify only a single locus of the Transformer layer with static scaling, and from ungated hybrid combinations (UniPELT-NoGate) or homogeneous parallel Mixture-of-Experts (MoE) layers: UniPELT combines heterogeneous submodules sequentially across multi-head attention projections, attention prefixes, and post-FFN residual bottlenecks under input-conditioned sigmoid gates G_L, G_P, and G_A.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 693 UniPELT (Mao et al., ACL 2022): bypass_err=0.00e+00, err_unipelt=1.99e-07 < oracle_single=0.2133 < best_single=0.8800, err_nogate=0.1133
```
