# Discovery Report: Round 512 — FedWeIT (Federated Weighted Inter-Client Transfer)

- **Timestamp**: `2026-10-19T09:55:00Z`
- **Selected Concept**: `AIMech:FedWeitFederatedContinualLearningWithWeightedInterClientTransfer` (*FedWeIT (Federated Weighted Inter-Client Transfer)*)
- **Record Path**: `data/curated/FedWeitFederatedContinualLearningWithWeightedInterClientTransfer.yaml`
- **Primary Source**: Jaehong Yoon, Wonyong Jeong, Giwoong Lee, Eunho Yang, Sung Ju Hwang — *Federated Continual Learning with Weighted Inter-client Transfer* (`https://dblp.org/rec/conf/icml/YoonJLYH21`).

## Identity & Boundary Resolution

Introduced by Jaehong Yoon, Wonyong Jeong, Giwoong Lee, Eunho Yang, and Sung Ju Hwang in 'Federated Continual Learning with Weighted Inter-client Transfer' (ICML 2021, PMLR 139:12073-12086; arXiv:2003.03196). Distinct from single-machine Additive Parameter Decomposition (APD, Yoon et al. ICLR 2020), which has no cross-client attention transfer term sum_{i != c} alpha_{i,j}^{(t)} A_i^{(j)} nor sparse masked base-parameter aggregation theta_G = (1/|C^{(r)}|) sum_c B_c^{(t,r)} odot m_c^{(t,r)}; distinct from FedCurv (Shoham et al. 2019) and FedProx (Li et al. 2018), which store all task knowledge in a single shared parameter vector theta_G without task-adaptive decomposition; and distinct from GLFC (Dong et al. CVPR 2022), which addresses class-incremental federated learning via gradient compensation and relation distillation rather than task-incremental parameter decomposition.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 512 FedWeIT (Yoon et al. 2021): forgetting_retro=6.61e-05 << forgetting_no_retro=2.447, alpha0=1.111, err_fedweit=0.109 << err_naive=4.368, c2s_ratio=0.3015
```
