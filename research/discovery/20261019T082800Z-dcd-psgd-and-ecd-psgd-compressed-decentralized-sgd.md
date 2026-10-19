# Discovery Report: Round 425 — DCD-PSGD and ECD-PSGD (Difference-Compression and Extrapolation-Compression Decentralized Parallel SGD)

- **Timestamp**: `2026-10-19T08:28:00Z`
- **Selected Concept**: `AIMech:DcdPsgdAndEcdPsgdCompressedDecentralizedParallelStochasticGradientDescent` (*DCD-PSGD and ECD-PSGD (Difference-Compression and Extrapolation-Compression Decentralized Parallel SGD)*)
- **Record Path**: `data/curated/DcdPsgdAndEcdPsgdCompressedDecentralizedParallelStochasticGradientDescent.yaml`
- **Primary Source**: Hanlin Tang, Shaoduo Gan, Ce Zhang, Tong Zhang, Ji Liu — *Communication Compression for Decentralized Training* (`https://papers.nips.cc/paper/2018/hash/2b8a61594b1f4c4db0902a8a395ced93-Abstract.html`).

## Identity & Boundary Resolution

Distinct from Choco-SGD and Choco-Gossip (AIMech:ChocoSgdAndChocoGossipDecentralizedCompressedOptimization, Koloskova, Stich, & Jaggi 2019), which introduce a consensus stepsize gamma in (0, 1] on the gossip step x_{t+1} = x_t - eta g_t + gamma sum_j w_{ij} (x_hat_j - x_hat_i) to support biased contractive compressors, whereas DCD-PSGD applies full-weight gossip W to unbiasedly compressed differences and ECD-PSGD uses harmonic O(1/t) extrapolation-averaging.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 425 DCD-PSGD & ECD-PSGD (Tang et al. 2018): DCD alpha_crit=0.50 (safe=0.360>0, unsafe=-0.540<0), ECD exact_err=4.4e-16, ECD var(t=2)=2.0000 -> var(t=20)=0.1368 <= O(1/T)
```
