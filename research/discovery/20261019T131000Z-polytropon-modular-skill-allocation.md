# Discovery Report: Round 707 — Polytropon (Latent Task-Skill Allocation for Modular Multitask Learning)

- **Timestamp**: `2026-10-19T13:10:00Z`
- **Selected Concept**: `AIMech:PolytroponModularSkillAllocation` (*Polytropon (Latent Task-Skill Allocation for Modular Multitask Learning)*)
- **Record Path**: `data/curated/PolytroponModularSkillAllocation.yaml`
- **Primary Source**: Edoardo M. Ponti, Alessandro Sordoni, Yoshua Bengio, Siva Reddy — *Combining Modular Skills in Multitask Learning* (`https://dblp.org/search/publ/api?q=Combining+Modular+Skills+in+Multitask+Learning&format=xml`).

## Identity & Boundary Resolution

Introduced by Edoardo M. Ponti, Alessandro Sordoni, Yoshua Bengio, and Siva Reddy (2022/ICLR 2023, arXiv:2202.13914; official implementation github.com/McGill-NLP/polytropon, referred to as SKILLED / Polytropon). Distinct from MoE and MoLE (AIMech Round 686), which route tokens via competitive softmax/top-k gating conditioned on the input rather than learning a non-competitive variable-subset binary soft partition Z over skills conditioned on the task, and distinct from HyperFormer (AIMech Round 703), which entangles task knowledge inside a continuous hypernetwork rather than recombining discrete modular skill parameterizations.

## Constructed Boundary & Regime Verification

```text
[PASS] Polytropon boundaries verified: params_per_skill=3157248, discreteness=0.1409, sparsity=0.5833, usage=0.9832
```
