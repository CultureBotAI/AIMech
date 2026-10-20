# Discovery Report: Round 653 — Vector-based Random Matrix Adaptation (VeRA)

- **Timestamp**: `2026-10-19T12:16:00Z`
- **Selected Concept**: `AIMech:VeraVectorBasedRandomMatrixAdaptation` (*Vector-based Random Matrix Adaptation (VeRA)*)
- **Record Path**: `data/curated/VeraVectorBasedRandomMatrixAdaptation.yaml`
- **Primary Source**: Dawid Jan Kopiczko, Tijmen Blankevoort, Yuki M. Asano — *VeRA: Vector-based Random Matrix Adaptation* (`https://dblp.org/rec/conf/iclr/KopiczkoBA24.html`).

## Identity & Boundary Resolution

Distinct from standard Low-Rank Adaptation (LoRA, Hu et al., 2022), which trains and stores separate full matrices B and A per layer (costing 2 L_{tuned} d_{model} r parameters) rather than freezing a single shared random pair (B, A) and training only scaling vectors (b, d). Also distinct from (IA)^3 (Liu et al., 2022) and RED (Wu et al., 2024), which apply learned element-wise scaling directly to activation vectors at every forward pass without frozen random basis projections B and A.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 653 VeRA boundary and mathematical verification succeeded.
```
