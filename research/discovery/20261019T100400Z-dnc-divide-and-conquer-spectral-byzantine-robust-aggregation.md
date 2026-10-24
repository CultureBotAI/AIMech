# Discovery Report: Round 521 — Divide-and-Conquer Spectral Byzantine-Robust Aggregation

- **Timestamp**: `2026-10-19T10:04:00Z`
- **Selected Concept**: `AIMech:DncDivideAndConquerSpectralByzantineRobustAggregation` (*Divide-and-Conquer Spectral Byzantine-Robust Aggregation*)
- **Record Path**: `data/curated/DncDivideAndConquerSpectralByzantineRobustAggregation.yaml`
- **Primary Source**: Virat Shejwalkar, Amir Houmansadr — *Manipulating the Byzantine: Optimizing Model Poisoning Attacks and Defenses for Federated Learning* (`https://dblp.org/rec/conf/ndss/ShejwalkarH21.json`).

## Identity & Boundary Resolution

Distinct from Euclidean distance-based filtering rules (Krum, Multi-Krum, Bulyan), coordinate-wise robust estimators (Coordinate-Wise Median, Coordinate-Wise Trimmed-Mean, Geometric Median / RFA), cosine-similarity server-root-dataset trust bootstrapping (FLTrust), and loss-based suspicion scoring (Zeno). Specifically denotes the Divide-and-Conquer (DnC) spectral aggregation rule of Shejwalkar & Houmansadr (NDSS 2021, Algorithm 2, Section VII-B) backed by epsilon-spectral separability guarantees (Definition 1, Lemma 1, and Appendix B Lemmas 2-3).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 521 DnC (Shejwalkar & Houmansadr 2021): <Delta,v>^2=3.9054>=2/3||Delta||^2=2.6133, malicious_kept=0, err_dnc=0.0000 < err_trmean=0.1789 < err_avg=0.4013
```
