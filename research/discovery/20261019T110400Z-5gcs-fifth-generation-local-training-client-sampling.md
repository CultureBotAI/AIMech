# Discovery Report: Round 581 — 5GCS (Fifth-Generation Local Training with Client Sampling)

- **Timestamp**: `2026-10-19T11:04:00Z`
- **Selected Concept**: `AIMech:FiveGcsFifthGenerationLocalTrainingWithClientSampling` (*5GCS (Fifth-Generation Local Training with Client Sampling)*)
- **Record Path**: `data/curated/FiveGcsFifthGenerationLocalTrainingWithClientSampling.yaml`
- **Primary Source**: Michal Grudzien, Grigory Malinovsky, Peter Richtarik — *Can 5th Generation Local Training Methods Support Client Sampling? Yes!* (`https://dblp.org/search/publ/api?q=Can+5th+Generation+Local+Training+Methods+Support+Client+Sampling&format=json`).

## Identity & Boundary Resolution

Distinct from fourth-generation LT methods such as ProxSkip / Scaffnew (AIMech:ProxSkipLocalTrainingAlgorithm, which require full client participation to achieve O(sqrt(L/mu) log(1/epsilon)) communication complexity and lacks a known extension to client sampling with O((n/s) sqrt(L/mu)) rates) and from third-generation methods such as Scaffold (which achieve unaccelerated O((n/s)(L/mu) log(1/epsilon)) rates). 5GCS reformulates accelerated primal-dual LT around client-sampled Approximate Proximal Point (APP) local solvers.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 581 5GCS verified: eq11_lhs=18.6800==18.6800, K_local=16, psi_0=8.013e+00 -> psi_T=1.024e-30
```
