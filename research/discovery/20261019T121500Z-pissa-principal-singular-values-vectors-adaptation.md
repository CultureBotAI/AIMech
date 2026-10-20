# Discovery Report: Round 652 — Principal Singular Values and Singular Vectors Adaptation (PiSSA)

- **Timestamp**: `2026-10-19T12:15:00Z`
- **Selected Concept**: `AIMech:PissaPrincipalSingularValuesAndSingularVectorsAdaptation` (*Principal Singular Values and Singular Vectors Adaptation (PiSSA)*)
- **Record Path**: `data/curated/PissaPrincipalSingularValuesAndSingularVectorsAdaptation.yaml`
- **Primary Source**: Fanxu Meng, Zhaohui Wang, Muhan Zhang — *PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models* (`https://dblp.org/rec/conf/nips/MengWZ24.html`).

## Identity & Boundary Resolution

Distinct from standard LoRA (Hu et al., 2022), which freezes the entire pretrained matrix W and initializes A with Gaussian noise and B = 0, resulting in a zero initial gradient for A (partial L / partial A = X^T (partial L / partial Y) B^T = 0) and slow early-stage optimization. Also distinct from LoftQ (Li et al., 2024), which iteratively alternates quantization and SVD to approximate W with Q + A B where A B corrects quantization residuals rather than containing the principal singular components of W.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 652 PiSSA boundary and mathematical verification succeeded.
```
