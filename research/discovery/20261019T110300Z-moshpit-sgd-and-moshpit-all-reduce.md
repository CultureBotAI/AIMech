# Discovery Report: Round 580 — Moshpit SGD and Moshpit All-Reduce

- **Timestamp**: `2026-10-19T11:03:00Z`
- **Selected Concept**: `AIMech:MoshpitSgdAndMoshpitAllReduceForFaultTolerantDecentralizedTraining` (*Moshpit SGD and Moshpit All-Reduce*)
- **Record Path**: `data/curated/MoshpitSgdAndMoshpitAllReduceForFaultTolerantDecentralizedTraining.yaml`
- **Primary Source**: Max Ryabinin, Eduard Gorbunov, Vsevolod Plokhotnyuk, Gennady Pekhimenko — *Moshpit SGD: Communication-Efficient Decentralized Training on Heterogeneous Unreliable Devices* (`https://dblp.org/search/publ/api?q=Moshpit+SGD+Ryabinin+Gorbunov&format=json`).

## Identity & Boundary Resolution

Distinct from global Ring/Butterfly All-Reduce (where a single straggler or failed peer stalls the entire cluster) and from gossip or PushSum decentralized SGD (whose convergence rate degrades with the spectral gap 1 - lambda_2(M) of a fixed sparse communication graph). Moshpit All-Reduce uses DHT-coordinated hypercube chunk-history keys to form disjoint small All-Reduce groups whose expected squared distortion contracts exponentially at rate ((r - 1)/N + r/N^2)^T independent of graph spectral gap.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 580 Moshpit SGD verified: full_grid_err=0.00e+00, thm3_2_factor=0.222222, m1=0.1147, m2=0.0137, t_opt=0.0100<0.0150
```
