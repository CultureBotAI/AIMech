# Discovery Report: Round 535 — SLSGD Secure Local Stochastic Gradient Descent with Trimmed Mean and Moving Average

- **Timestamp**: `2026-10-19T10:18:00Z`
- **Selected Concept**: `AIMech:SlsgdSecureLocalStochasticGradientDescentWithTrimmedMeanAndMovingAverage` (*SLSGD Secure Local Stochastic Gradient Descent with Trimmed Mean and Moving Average*)
- **Record Path**: `data/curated/SlsgdSecureLocalStochasticGradientDescentWithTrimmedMeanAndMovingAverage.yaml`
- **Primary Source**: Cong Xie, Oluwasanmi Koyejo, Indranil Gupta — *SLSGD: Secure and Efficient Distributed On-device Machine Learning* (`https://dblp.org/rec/conf/pkdd/XieKG19.xml`).

## Identity & Boundary Resolution

Distinct from single-step synchronous Coordinate-Wise Median and Trimmed Mean Gradient Aggregation (AIMech:CoordinateWiseMedianAndTrimmedMeanByzantineRobustGradientAggregation, which aggregates single-step gradients without multi-step local SGD updates or server-side moving-average variance reduction) and from standard Federated Averaging / Local SGD (which corresponds to SLSGD Option I with b = 0 and alpha = 1). SLSGD (Xie et al., ECML-PKDD 2019, pp. 213-228 / arXiv:1903.06996, Algorithm 1, p. 6) samples a subset S_t of k workers in each global epoch t, runs H_t^i >= H_{min} heterogeneous local SGD iterations x_{t,h}^i <- x_{t,h-1}^i - gamma nabla f(x_{t,h-1}^i; z_{t,h}^i) from x_{t,0}^i = x_{t-1} on each device i in S_t, aggregates the resulting local models via coordinate-wise b-trimmed mean x_t' = Trmean_b({x_{t,H_t^i}^i : i in S_t}) = (1 / (k - 2b)) sum_{i=b+1}^{k-b} u_{i:k} (Option II, Definition 3), and updates the global model via the moving average x_t <- (1 - alpha) x_{t-1} + alpha x_t' (with alpha in (0, 1]).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 535 SLSGD verified: err_slsgd=0.15390 << err_fedavg=97.51, beta(q=1,b=2)=3.550 < beta(q=2,b=2)=4.448 < beta(q=2,b=4)=9.865
```
