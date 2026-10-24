# Discovery Report: Round 835 — Hitting-Set IP Relaxation and Tiled Interval Cover for Paging with Time Windows and Delays

- **Timestamp**: `2026-10-19T15:18:00Z`
- **Selected Concept**: `AIMech:HittingSetIPAndTiledIntervalCoverOnlinePagingWithTimeWindowsAndDelays` (*Hitting-Set IP Relaxation and Tiled Interval Cover for Paging with Time Windows and Delays*)
- **Record Path**: `data/curated/HittingSetIPAndTiledIntervalCoverOnlinePagingWithTimeWindowsAndDelays.yaml`
- **Primary Source**: Anupam Gupta, Amit Kumar, Debmalya Panigrahi — *Caching with Time Windows and Delays* (`https://arxiv.org/abs/2006.09665`).

## Identity & Boundary Resolution

No AIO class represents online primal-dual hitting-set LP/IP relaxations for paging with time windows and delays; MachineLearningTask (AIO:MachineLearningTask) is the closest broad match covering online sequential decision-making and optimization tasks.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 835 PageTW/PageD Hitting-Set IP verified: frac_cost=8401.0 vs int_lb=20000.0 (hitting_ip_lb=20000.0), hall_ratio=1.9000<=2, tu_submatrices=791, paged_red_err=0.00e+00
```
