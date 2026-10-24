# Discovery Report: Round 587 — Lion (EvoLved Sign Momentum)

- **Timestamp**: `2026-10-19T11:10:00Z`
- **Selected Concept**: `AIMech:LionEvolvedSignMomentumOptimization` (*Lion (EvoLved Sign Momentum)*)
- **Record Path**: `data/curated/LionEvolvedSignMomentumOptimization.yaml`
- **Primary Source**: Xiangning Chen, Chen Liang, Da Huang, Esteban Real, Kaiyuan Wang, Yao Liu, Hieu Pham, Xuanyi Dong, Thang Luong, Cho-Jui Hsieh, Yifeng Lu, Quoc V. Le — *Symbolic Discovery of Optimization Algorithms* (`https://dblp.org/rec/conf/nips/ChenLHRW0DLHLL23`).

## Identity & Boundary Resolution

Distinct from Adam, AdamW, AdaBelief, Sophia, and Adafactor in that Lion stores no second-moment or Hessian buffer and applies an elementwise binary sign operation sign(c_t) in {-1, 0, +1} yielding uniform coordinate update magnitudes. Distinct from signSGD with momentum in that Lion decouples the interpolation weight beta_1 = 0.9 used to form the sign-update direction c_t from the longer-horizon EMA decay beta_2 = 0.99 used to update the stored momentum m_t.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 587 Lion verified: simp_diff=2.91e-16, loss_lion=0.3368<(ab90=2.5730, ab99=0.7423), state_ratio=0.50
```
