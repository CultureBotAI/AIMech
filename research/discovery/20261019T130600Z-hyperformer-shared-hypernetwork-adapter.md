# Discovery Report: Round 703 — HyperFormer (Shared Hypernetwork Multi-Task Adapter)

- **Timestamp**: `2026-10-19T13:06:00Z`
- **Selected Concept**: `AIMech:HyperFormerSharedHypernetworkAdapter` (*HyperFormer (Shared Hypernetwork Multi-Task Adapter)*)
- **Record Path**: `data/curated/HyperFormerSharedHypernetworkAdapter.yaml`
- **Primary Source**: Rabeeh Karimi Mahabadi, Sebastian Ruder, Mostafa Dehghani, James Henderson — *Parameter-efficient Multi-task Fine-tuning for Transformers via Shared Hypernetworks* (`https://dblp.org/search/publ/api?q=Parameter-efficient+Multi-task+Fine-tuning+for+Transformers+via+Shared+Hypernetworks&format=xml`).

## Identity & Boundary Resolution

Introduced by Rabeeh Karimi Mahabadi, Sebastian Ruder, Mostafa Dehghani, and James Henderson (ACL/IJCNLP 2021, pp. 565-576, arXiv:2106.04489). Both per-layer HyperFormer (which places a task-conditioned hypernetwork in each Transformer layer) and the compact HyperFormer++ variant (which shares a single pair of adapter and LayerNorm hypernetworks across all layers and tasks conditioned on concatenated task z_tau, layer-ID l_i, and position p_j embeddings) are lumping-cohesive variants covered together in this record.

## Constructed Boundary & Regime Verification

```text
[PASS] HyperFormer++ boundary verification passed: p_hf_pp=4,983,040 vs p_adapters=14,745,600 (2.96x reduction), const_hn_params=4,980,736
```
