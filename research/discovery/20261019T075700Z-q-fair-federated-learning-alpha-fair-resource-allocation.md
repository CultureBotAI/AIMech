# Discovery Report: Round 394 — q-Fair Federated Learning (q-FFL) and q-FedAvg for Alpha-Fair Resource Allocation

- **Timestamp**: `2026-10-19T07:57:00Z`
- **Selected Concept**: `AIMech:QFairFederatedLearningAlphaFairResourceAllocation` (*q-Fair Federated Learning (q-FFL) and q-FedAvg for Alpha-Fair Resource Allocation*)
- **Record Path**: `data/curated/QFairFederatedLearningAlphaFairResourceAllocation.yaml`
- **Primary Source**: Tian Li, Maziar Sanjabi, Ahmad Beirami, Virginia Smith — *Fair Resource Allocation in Federated Learning* (`https://doi.org/10.48550/arXiv.1905.10497`).

## Identity & Boundary Resolution

Distinct from standard Federated Averaging (AIMech:FederatedAveragingClientServerOptimization, which is the q = 0 special case that minimizes average loss without controlling cross-device accuracy variance) and from Ditto (AIMech:DittoFairAndRobustPersonalizedFederatedMultiTaskLearning, which achieves device fairness via personalized models v_k regularized toward w^* rather than learning a single fair global model w via (q+1)-power loss reweighting).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 394 q-FFL verified: var(q=0)=2.8743 > var(q=1)=1.2042 > var(q=5)=0.3848; max(q=0)=4.3928 > max(q=5)=3.3104
```
