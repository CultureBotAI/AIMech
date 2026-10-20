# Discovery Report: Round 715 — Supermasks in Superposition

- **Timestamp**: `2026-10-19T13:18:00Z`
- **Selected Concept**: `AIMech:SupSupSupermasksInSuperposition` (*Supermasks in Superposition*)
- **Record Path**: `data/curated/SupSupSupermasksInSuperposition.yaml`
- **Primary Source**: Mitchell Wortsman, Vivek Ramanujan, Rosanne Liu, Aniruddha Kembhavi, Mohammad Rastegari, Jason Yosinski, Ali Farhadi — *Supermasks in Superposition* (`https://dblp.org/search/publ/api?q=Supermasks+in+Superposition+Wortsman&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Mitchell Wortsman, Vivek Ramanujan, Rosanne Liu, Aniruddha Kembhavi, Mohammad Rastegari, Jason Yosinski, and Ali Farhadi (NeurIPS 2020, pp. 15173-15184, arXiv:2006.14769) as Supermasks in Superposition (SupSup) and HopSupSup. Distinct from LT-SFT (AIMech:LTSFTLotteryTicketSparseFineTuning), which fine-tunes real-valued sparse difference vectors from a pretrained language model and sums them unconditionally; and from Polytropon (AIMech:PolytroponModularSkillAllocation), which jointly learns LoRA skill modules and a binary task-skill allocation matrix.

## Constructed Boundary & Regime Verification

```text
[PASS] SupSup boundaries verified: One-Shot recovery=6/6, Lemma I.1/I.2/I.3/J.2 verified, NNs_conf=4.858 > 1.125
```
