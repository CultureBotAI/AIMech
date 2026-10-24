# Discovery Report: Round 440 — NIDS (Network-Independent Step-Size Decentralized Proximal-Gradient Method)

- **Timestamp**: `2026-10-19T08:43:00Z`
- **Selected Concept**: `AIMech:NidsNetworkIndependentStepSizeDecentralizedProximalGradientMethod` (*NIDS (Network-Independent Step-Size Decentralized Proximal-Gradient Method)*)
- **Record Path**: `data/curated/NidsNetworkIndependentStepSizeDecentralizedProximalGradientMethod.yaml`
- **Primary Source**: Zhi Li, Wei Shi, Ming Yan — *A Decentralized Proximal-Gradient Method With Network Independent Step-Sizes and Separated Convergence Rates* (`https://doi.org/10.1109/TSP.2019.2926022`).

## Identity & Boundary Resolution

Distinct from EXTRA (AIMech:ExtraExactFirstOrderAlgorithmForDecentralizedConsensusOptimization, Shi et al. 2015) and PG-EXTRA, which apply the raw mixing matrix W in the gradient difference term X^{k+1} = W X^k + X^k - W_tilde X^{k-1} - alpha(nabla S(X^k) - nabla S(X^{k-1})) and therefore restrict step sizes by the spectral gap of W (alpha < 2 lambda_min(W_tilde) / L), whereas NIDS multiplies the previous gradient by W_tilde inside the proximal argument so the maximal stable step size alpha < 2 / L is completely independent of the network topology.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 440 NIDS (Li, Shi, & Yan 2019): nids_err=8.44e-15 << pge_err=2.77e+11, alpha=0.25 > pge_max=0.10, rho_decoupled=0.5000
```
