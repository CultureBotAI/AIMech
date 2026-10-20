# Discovery Report: Round 539 — BASGD Buffered Asynchronous Stochastic Gradient Descent for Byzantine Learning

- **Timestamp**: `2026-10-19T10:22:00Z`
- **Selected Concept**: `AIMech:BasgdBufferedAsynchronousStochasticGradientDescentForByzantineLearning` (*BASGD Buffered Asynchronous Stochastic Gradient Descent for Byzantine Learning*)
- **Record Path**: `data/curated/BasgdBufferedAsynchronousStochasticGradientDescentForByzantineLearning.yaml`
- **Primary Source**: Yi-Rui Yang, Wu-Jun Li — *BASGD: Buffered Asynchronous SGD for Byzantine Learning* (`https://dblp.org/rec/conf/icml/YangL21.xml`).

## Identity & Boundary Resolution

Distinct from Kardam (AIMech:KardamLipschitzAndFrequencyFilteredAsynchronousByzantineStochasticGradientDescent, which filters individual incoming gradients via empirical Lipschitz quantiles and a 2f-window frequency filter without server buffers) and from Zeno++ (AIMech:ZenoPlusPlusRobustFullyAsynchronousStochasticGradientDescent, which requires a clean validation dataset stored on the server to compute candidate loss-descent scores). Also distinct from synchronous s-Bucketing (AIMech:BucketingForAgnosticByzantineRobustAggregationOnHeterogeneousDatasets, which randomly reshuffles synchronous worker momentum vectors at every barrier step). BASGD (Yang & Li, ICML 2021, PMLR 139:11751-11761, Algorithm 1 & Section 3.1-3.3, pp. 3-5) routes each arriving asynchronous gradient g from worker s into buffer b = beta_s mod B via the online mean update N_b^t <- N_b^t + 1, h_b <- ((N_b^t - 1) h_b + g) / N_b^t, immediately replies to worker s with the latest w^t without synchronization barriers, triggers a parameter update w^{t+1} <- w^t - eta Aggr([h_1, ..., h_B]) and zeroes all buffers as soon as N_b^t > 0 for every b in [B], and resets the mapping table {beta_s} to redistribute active workers across all B buffers whenever the step timer exceeds the reassignment interval Delta.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 539 BASGD verified: Lambda(10,3,2)=6.928 < Lambda(10,2,2)=9.071, reassigned_buffers=[0, 1, 2, 3, 4], err_basgd=0.000001 << err_asgd=2.62
```
