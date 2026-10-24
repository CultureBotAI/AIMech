# Discovery Report: Round 258 — Degree-Corrected Stochastic Blockmodel and Edge-Stub Kullback-Leibler Divergence Profile Log-Likelihood

- **Timestamp**: `2026-10-19T02:08:00Z`
- **Selected Concept**: `AIMech:DegreeCorrectedStochasticBlockmodelAndEdgeStubKLDivergenceProfileLikelihood` (*Degree-Corrected Stochastic Blockmodel and Edge-Stub Kullback-Leibler Divergence Profile Log-Likelihood*)
- **Record Path**: `data/curated/DegreeCorrectedStochasticBlockmodelAndEdgeStubKLDivergenceProfileLikelihood.yaml`
- **Primary Source**: Brian Karrer and M. E. J. Newman (2011), *Stochastic blockmodels and community structure in networks*, *Physical Review E* 83(1):016107 (`DOI:10.1103/PhysRevE.83.016107`, `arXiv:1008.3926v1`).

## Identity & Boundary Resolution

`AIMech:DegreeCorrectedStochasticBlockmodelAndEdgeStubKLDivergenceProfileLikelihood` was checked against all 442 pinned AIO concepts and 652 maintained AIMech concepts:

1. **`AIMech:TensorSpectralDecompositionForDirichletMixedMembershipCommunityModels`**: Models mixed Dirichlet community memberships via centered 3-star subgraph count tensors without vertex degree parameters $\theta_i$, whereas Karrer & Newman (2011) introduce within-group-normalized degree propensities $\theta_i$, closed-form MLEs $\hat{\theta}_i = k_i / \kappa_{g_i}$ and $\hat{\omega}_{rs} = m_{rs}$ that preserve exact expected degrees, and the edge-stub Kullback-Leibler profile log-likelihood $\sum_{rs} m_{rs} \log(m_{rs}/(\kappa_r \kappa_s))$.

## Constructed Boundary & Regime Verification

```text
Karrer & Newman (2011) DC-SBM verified: MLE deg/block err=(1.78e-15,8.88e-16), KL identity err=0.00e+00, Eq.25 DeltaL err=4.26e-14, lambda=0.5 gap(planted-deg): SBM=-2616.2 vs DC-SBM=+2616.2.
```

Verified in pure Python: (1) on a 6-vertex 3-group multigraph with self-edges and multi-edges, the closed-form MLEs theta_hat_i = k_i / kappa_{g_i} and omega_hat_{rs} = m_{rs} (Eq. 18) preserve expected vertex degrees to 1.78e-15 and expected block edge counts to 8.88e-16 (Eqs. 19-20), and L_DC(G|g) = 2m D_KL(p_K || p_degree) - 2m log(2m) holds to 0.00e+00 (Eqs. 23-24); (2) the local single-vertex shift formula Eq. (25) (with the corrected m_{rt} - k_{it} term) matches exact recomputation across all moves to 4.26e-14; and (3) on the Section IV.C bimodal-degree benchmark (degrees 10 and 30, lambda = 0.5), uncorrected L_SBM favors the spurious degree split over the planted split by -2616.2, whereas L_DC favors the true planted split by +2616.2.
