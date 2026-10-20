# Discovery Report: Round 685 — LoRA-Flow

- **Timestamp**: `2026-10-19T12:48:00Z`
- **Selected Concept**: `AIMech:LoRAFlow` (*LoRA-Flow*)
- **Record Path**: `data/curated/LoRAFlow.yaml`
- **Primary Source**: Hanqing Wang, Bowen Ping, Shuo Wang, Xu Han, Yun Chen, Zhiyuan Liu, Maosong Sun — *LoRA-Flow: Dynamic LoRA Fusion for Large Language Models in Generative Tasks* (`https://dblp.org/rec/conf/acl/WangPWH0L024.xml`).

## Identity & Boundary Resolution

Distinct from LoraHub (AIMech:LoraHub, which learns static task-level scalar weights shared across all layers and tokens and composes internal factors (sum_i w_i A_i)(sum_i w_i B_i) requiring identical rank r across all modules), from HydraLoRA (AIMech:HydraLoRA, which jointly trains a shared down-projection A and multiple up-projection heads B_i from scratch rather than fusing independently pre-trained, frozen skill and language LoRAs), and from standard LoRA (AIMech:LoRA). Formulated by Wang et al. (ACL 2024, pages 12871-12882; arXiv:2402.11455).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 685 LoRA-Flow (Wang et al., ACL 2024): w_lang=(0.850,0.100), w_math=(-0.150,1.100), flow_loss=0.00067 << static_loss=1.96440
```
