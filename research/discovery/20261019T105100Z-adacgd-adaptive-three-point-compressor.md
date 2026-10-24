# Discovery Report: Round 568 — AdaCGD and Ada3PC Adaptive Three-Point Compression for Distributed Optimization

- **Timestamp**: `2026-10-19T10:51:00Z`
- **Selected Concept**: `AIMech:AdaCgdAndAda3PcAdaptiveThreePointCompressionForDistributedOptimization` (*AdaCGD and Ada3PC Adaptive Three-Point Compression for Distributed Optimization*)
- **Record Path**: `data/curated/AdaCgdAndAda3PcAdaptiveThreePointCompressionForDistributedOptimization.yaml`
- **Primary Source**: Maksim Makarenko, Elnur Gasanov, Rustem Islamov, Abdurakhmon Sadiev, Peter Richtárik — *Adaptive Compression for Communication-Efficient Distributed Training* (`https://api.openalex.org/works/W4308015852`).

## Identity & Boundary Resolution

Distinct from fixed-parameter Three Point Compressors (3PC, Richtárik et al. 2022, which use a single static 3PC operator or a single binary lazy-aggregation threshold) and distinct from heuristic adaptive gradient compression schemes lacking error-feedback convergence guarantees: Ada3PC proves closure of the 3PC class under arbitrary data-dependent switching among m distinct 3PC compressors with worst-case constants A_min = min_j A_j and B_max = max_j B_j (Lemma 2), and further extends 3PC to convex objectives (Theorem 5) and bidirectional server-and-worker 3PC compression (3PC-BD, Algorithm 2, Theorem 6).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 568 AdaCGD/Ada3PC verified: A_min=0.0646, B_max=13.5479, avg_k=2.35, level_counts={1: 469, 2: 686, 4: 373, 6: 72}, err_ada=9.471e-08
```
