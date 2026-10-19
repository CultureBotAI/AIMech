# Discovery Report: Round 443 — pFedHN (Personalized Federated Hypernetworks)

- **Timestamp**: `2026-10-19T08:46:00Z`
- **Selected Concept**: `AIMech:PFedHnPersonalizedFederatedHypernetworks` (*pFedHN (Personalized Federated Hypernetworks)*)
- **Record Path**: `data/curated/PFedHnPersonalizedFederatedHypernetworks.yaml`
- **Primary Source**: Aviv Shamsian, Aviv Navon, Ethan Fetaya, Gal Chechik — *Personalized Federated Learning using Hypernetworks* (`https://proceedings.mlr.press/v139/shamsian21a.html`).

## Identity & Boundary Resolution

Distinct from Per-FedAvg (AIMech:PerFedAvgPersonalizedFederatedLearningWithTheoreticalGuarantees, Fallah et al. 2020) and pFedMe (AIMech:PFedMePersonalizedFederatedLearningWithMoreauEnvelopes, T. Dinh et al. 2020), which transmit and regularize a single shared d-dimensional model init across all clients rather than generating client-conditioned parameters theta_i = h(v_i; varphi) from a low-dimensional client descriptor v_i on the server.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 443 pFedHN (Shamsian et al. 2021): pca_recon_err=0.1000==0.1000 << global_err=53.10, sample_complexity_ratio=172.6x
```
