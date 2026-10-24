# Discovery Report: Round 659 — Compacter (Low-Rank Hypercomplex Adapter Layers)

- **Timestamp**: `2026-10-19T12:22:00Z`
- **Selected Concept**: `AIMech:CompacterLowRankHypercomplexAdapterLayers` (*Compacter (Low-Rank Hypercomplex Adapter Layers)*)
- **Record Path**: `data/curated/CompacterLowRankHypercomplexAdapterLayers.yaml`
- **Primary Source**: Rabeeh Karimi Mahabadi, James Henderson, Sebastian Ruder — *Compacter: Efficient Low-Rank Hypercomplex Adapter Layers* (`https://dblp.org/rec/conf/nips/MahabadiHR21.html`).

## Identity & Boundary Resolution

Distinct from standard bottleneck adapters (Houlsby et al., 2019), which parameterize U^l and D^l as unconstrained dense matrices costing 4 L k d parameters across L encoder-decoder layers, and from PHM-Adapter, which does not share A_i across layers or factorize B_i into rank-one outer products (costing 4 L (k d / n + n^3) parameters). Also distinct from LoRA (Hu et al., 2022), which adds parallel low-rank updates directly to frozen attention weights without a nonlinear GeLU bottleneck or Kronecker hypercomplex multiplication.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 659 Compacter (Karimi Mahabadi et al. 2021): params_adapter=884736 > params_phm=224256 > params_compacter=38080 > params_compacter++=19072, max_diff=4.86e-17, ||W1-W2||_F=0.7716
```
