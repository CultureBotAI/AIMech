# Discovery Report: Round 591 — DoG (Distance over Gradients Parameter-Free Step Size Schedule)

- **Timestamp**: `2026-10-19T11:14:00Z`
- **Selected Concept**: `AIMech:DogDistanceOverGradientsParameterFreeStepSizeSchedule` (*DoG (Distance over Gradients Parameter-Free Step Size Schedule)*)
- **Record Path**: `data/curated/DogDistanceOverGradientsParameterFreeStepSizeSchedule.yaml`
- **Primary Source**: Maor Ivgi, Oliver Hinder, Yair Carmon — *DoG is SGD's Best Friend: A Parameter-Free Dynamic Step Size Schedule* (`https://dblp.org/rec/conf/icml/IvgiHC23`).

## Identity & Boundary Resolution

Distinct from LARS, LAMB, and Fromage in that DoG scales the step size by the maximum distance from the initial point max_{i<=t} ||x_i - x_0|| rather than the current parameter norm ||x_t|| and requires no multiplicative learning-rate hyperparameter (c = 1). Distinct from D-Adaptation and Prodigy in that DoG directly plugs the empirical displacement r_bar_t into the SGD step-size numerator instead of a dual regret lower bound d_hat_t.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 591 DoG verified: lemma3=(8.33>=2.62), nemirovski_ratio_dog=2.00 vs tdog=0.1000<=3.0, lemma1_regret=(196.6887<=981.7060)
```
