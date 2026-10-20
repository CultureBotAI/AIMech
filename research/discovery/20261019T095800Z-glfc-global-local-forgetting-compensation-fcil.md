# Discovery Report: Round 515 — GLFC (Global-Local Forgetting Compensation)

- **Timestamp**: `2026-10-19T09:58:00Z`
- **Selected Concept**: `AIMech:GlfcGlobalLocalForgettingCompensationForFederatedClassIncrementalLearning` (*GLFC (Global-Local Forgetting Compensation)*)
- **Record Path**: `data/curated/GlfcGlobalLocalForgettingCompensationForFederatedClassIncrementalLearning.yaml`
- **Primary Source**: Jiahua Dong, Lixu Wang, Zhen Fang, Gan Sun, Shichao Xu, Xiao Wang, Qi Zhu — *Federated Class-Incremental Learning* (`https://dblp.org/rec/conf/cvpr/DongWFSXW022`).

## Identity & Boundary Resolution

Introduced by Jiahua Dong, Lixu Wang, Zhen Fang, Gan Sun, Shichao Xu, Xiao Wang, and Qi Zhu in 'Federated Class-Incremental Learning' (CVPR 2022, pp. 10154-10163, DOI:10.1109/CVPR52688.2022.00992; arXiv:2203.11473). Distinct from FedWeIT (Yoon et al. ICML 2021), which addresses task-incremental federated continual learning with known task IDs at test time and parameter decomposition into masked base weights and sparse task-adaptive weights rather than single-head class-incremental learning; and distinct from centralized class-incremental learning methods (iCaRL, Rebuffi et al. CVPR 2017; PODNet, Douillard et al. ECCV 2020), which assume a single centralized exemplar store without heterogeneous client groups S_o, S_b, S_n or proxy-server prototype gradient reconstruction.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 515 GLFC (Dong et al. 2022): mean_w_old=1.00==mean_w_new=1.00, KL_forgetting=0.9818>>KL_matched=0.0e+00, entropy_jump=1.436>=1.2
```
