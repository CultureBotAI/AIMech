# Discovery Report: Round 562 — GradSkip and GradSkip+ Communication-Accelerated Local Gradient Methods with Gradient Skipping

- **Timestamp**: `2026-10-19T10:45:00Z`
- **Selected Concept**: `AIMech:GradSkipAndGradSkipPlusCommunicationAcceleratedLocalGradientMethodsWithGradientSkipping` (*GradSkip and GradSkip+ Communication-Accelerated Local Gradient Methods with Gradient Skipping*)
- **Record Path**: `data/curated/GradSkipAndGradSkipPlusCommunicationAcceleratedLocalGradientMethodsWithGradientSkipping.yaml`
- **Primary Source**: Artavazd Maranjyan, Mher Safaryan, Peter Richtarik — *GradSkip: Communication-Accelerated Local Gradient Methods with Better Computational Complexity* (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2210.16402`).

## Identity & Boundary Resolution

Distinct from ProxSkip / Scaffnew (Mishchenko et al., ICML 2022; which sets q_i = 1 for all clients and forces every client to compute 1/p local gradients per communication round regardless of local condition number kappa_i = L_i / mu). GradSkip and GradSkip+ (Maranjyan, Safaryan, & Richtarik, arXiv:2210.16402) decouple local gradient computation frequency q_i from communication frequency p.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 562 GradSkip verified: psi 494.410 -> 1.818e-29, E[steps]=20.08 vs Scaffnew=40.00, real_grads=2431, fake_steps=2369
```
