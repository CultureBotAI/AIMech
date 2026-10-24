# Discovery Report: Round 632 — CSER (Communication-Efficient SGD with Error Reset)

- **Timestamp**: `2026-10-19T11:55:00Z`
- **Selected Concept**: `AIMech:CSERCommunicationEfficientSgdWithErrorReset` (*CSER (Communication-Efficient SGD with Error Reset)*)
- **Record Path**: `data/curated/CSERCommunicationEfficientSgdWithErrorReset.yaml`
- **Primary Source**: Cong Xie, Shuai Zheng, Oluwasanmi Koyejo, Indranil Gupta, Mu Li, Haibin Lin — *CSER: Communication-efficient SGD with Error Reset* (`https://dblp.org/rec/conf/nips/XieZKGLL20`).

## Identity & Boundary Resolution

Distinct from Error-Feedback SGD / Sparsified SGD with Memory (AIMech:SparsifiedSgdWithMemory, Stich et al. 2018; Karimireddy et al. 2019) and QSparse-local-SGD (Basu et al. 2019), which keep local models fully synchronized after communication and set residual compression errors e_{i,t} aside from gradient evaluation for up to H local steps; CSER immediately assimilates residuals into bifurcated local models x_{i,t} so that x_{i,t} - e_{i,t} = x_{j,t} - e_{j,t} holds for all workers (Lemma 1) and the compression error vanishes when n = 1 (Remark 2).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 632 CSER verified: inv_err=1.78e-15, n1_err=1.11e-16, remark1=832->576, budget_split_err=400.0->235.56
```
