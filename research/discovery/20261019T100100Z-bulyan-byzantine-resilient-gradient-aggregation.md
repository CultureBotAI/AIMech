# Discovery Report: Round 518 — Bulyan (Byzantine-Resilient Gradient Meta-Aggregation Rule)

- **Timestamp**: `2026-10-19T10:01:00Z`
- **Selected Concept**: `AIMech:BulyanByzantineResilientGradientAggregation` (*Bulyan (Byzantine-Resilient Gradient Meta-Aggregation Rule)*)
- **Record Path**: `data/curated/BulyanByzantineResilientGradientAggregation.yaml`
- **Primary Source**: El Mahdi El Mhamdi, Rachid Guerraoui, Sebastien Rouault — *The Hidden Vulnerability of Distributed Learning in Byzantium* (`https://dblp.org/rec/conf/icml/MhamdiGR18`).

## Identity & Boundary Resolution

Introduced by El Mahdi El Mhamdi, Rachid Guerraoui, and Sebastien Rouault in 'The Hidden Vulnerability of Distributed Learning in Byzantium' (ICML 2018, PMLR 80:3518-3527; arXiv:1802.07927). Distinct from Krum and Multi-Krum (Blanchard et al. NeurIPS 2017), which select and average whole vectors using Euclidean pairwise distance scores without coordinate-wise median trimming and thus remain vulnerable to single-coordinate O(sqrt(d)) poisoning; and distinct from Coordinate-Wise Median and Trimmed Mean (Yin et al. ICML 2018), which apply coordinate-wise order statistics directly to all n submitted vectors without a first-stage (alpha, f)-Byzantine-resilient vector selection quorum S.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 518 Bulyan (El Mhamdi et al. 2018): krum_coord0_err=2.859>>bulyan_coord0_err=0.0237, bracketed_all_d=200
```
