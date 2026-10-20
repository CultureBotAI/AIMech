# Discovery Report: Round 680 — LoRA-drop

- **Timestamp**: `2026-10-19T12:43:00Z`
- **Selected Concept**: `AIMech:LoRADrop` (*LoRA-drop*)
- **Record Path**: `data/curated/LoRADrop.yaml`
- **Primary Source**: Hongyun Zhou, Xiangyu Lu, Wang Xu, Conghui Zhu, Tiejun Zhao, Muyun Yang — *LoRA-drop: Efficient LoRA Parameter Pruning based on Output Evaluation* (`https://dblp.org/rec/conf/coling/ZhouLXZZY25.xml`).

## Identity & Boundary Resolution

Distinct from AdaLoRA (AIMech:AdaLoRA, which dynamically prunes singular triplets of SVD-parameterized adapters based on weight-gradient sensitivity scores without cross-layer parameter sharing), from Tied-LoRA (AIMech:TiedLoRA, which uniformly ties projection matrices across all layers with diagonal scaling vectors rather than partitioning layers by data-dependent output norms ||Delta W_i x_i||^2), and from standard LoRA (AIMech:LoRA, which trains independent untied adapters across all layers). Formulated by Zhou et al. (COLING 2025, pages 5530-5543; arXiv:2402.07721).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 680 LoRA-drop (Zhou et al., COLING 2025): sum_I=1.000000, k=4/12 (param_ratio=41.67%), top_energy=0.9030 vs bottom_energy=0.0006
```
