# Discovery Report: Round 714 — UDapter Typology-Conditioned Contextual Parameter Adapter

- **Timestamp**: `2026-10-19T13:17:00Z`
- **Selected Concept**: `AIMech:UDapterTypologyConditionedContextualParameterAdapter` (*UDapter Typology-Conditioned Contextual Parameter Adapter*)
- **Record Path**: `data/curated/UDapterTypologyConditionedContextualParameterAdapter.yaml`
- **Primary Source**: Ahmet Ustun, Arianna Bisazza, Gosse Bouma, Gertjan van Noord — *UDapter: Language Adaptation for Truly Universal Dependency Parsing* (`https://dblp.org/search/publ/api?q=UDapter+Language+Adaptation+for+Truly+Universal+Dependency+Parsing&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Ahmet Ustun, Arianna Bisazza, Gosse Bouma, and Gertjan van Noord (EMNLP 2020, pp. 2302-2315, arXiv:2004.14327) as UDapter. Distinct from MAD-X (AIMech:MADXMultipleAdaptersForCrossLingualTransfer), which trains separate per-language MLM adapters rather than generating adapter and parser weights from URIEL typological features via a Contextual Parameter Generator; and from HyperFormer (AIMech:HyperFormerSharedHypernetworkAdapter), which generates multi-task NLU adapters from learned task/layer embeddings without linguistic typology vectors or biaffine head generation.

## Constructed Boundary & Regime Verification

```text
[PASS] UDapter boundaries verified: d_uriel=289, params=550M vs 2483M, max_lin_err=4.44e-16, dist_zs_rel=0.7826 < dist_zs_unrel=18.6141
```
