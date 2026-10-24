# Discovery Report: Round 549 — RelaySum Spanning-Tree Information Propagation for Decentralized Learning

- **Timestamp**: `2026-10-19T10:32:00Z`
- **Selected Concept**: `AIMech:RelaySumSpanningTreeInformationPropagationForDecentralizedLearning` (*RelaySum Spanning-Tree Information Propagation for Decentralized Learning*)
- **Record Path**: `data/curated/RelaySumSpanningTreeInformationPropagationForDecentralizedLearning.yaml`
- **Primary Source**: Thijs Vogels, Lie He, Anastasia Koloskova, Tao Lin, Sai Praneeth Karimireddy, Sebastian U. Stich, Martin Jaggi — *RelaySum for Decentralized Deep Learning on Heterogeneous Data* (`https://dblp.org/rec/conf/nips/VogelsHKKLSJ21`).

## Identity & Boundary Resolution

Introduced by Thijs Vogels, Lie He, Anastasia Koloskova, Tao Lin, Sai Praneeth Karimireddy, Sebastian U. Stich, and Martin Jaggi (NeurIPS 2021, pp. 28004-28015; arXiv:2110.04175). Distinct from standard gossip averaging / DP-SGD (Lian et al., NeurIPS 2017) and Stochastic Gradient Push (Assran et al., ICML 2019), which decay message weights by mixing-matrix entries < 1 at every hop and suffer from data heterogeneity drift; and distinct from gradient-tracking / exact-diffusion algorithms (D^2, NEXT, SONATA, Push-Pull), which subtract previous gradients or maintain gradient trackers rather than relaying unattenuated model sums over spanning trees.

## Constructed Boundary & Regime Verification

```text
[PASS] RelaySum & RelaySGD boundaries verified: diameter=4, mean_low_het=8.08e-08, mean_high_het=1.21e-08
```
