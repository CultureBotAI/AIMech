# Discovery Report: Round 567 — TAMUNA Doubly Accelerated Distributed Optimization with Local Training, Compression, and Partial Participation

- **Timestamp**: `2026-10-19T10:50:00Z`
- **Selected Concept**: `AIMech:TamunaDoublyAcceleratedDistributedOptimizationWithLocalTrainingCompressionAndPartialParticipation` (*TAMUNA Doubly Accelerated Distributed Optimization with Local Training, Compression, and Partial Participation*)
- **Record Path**: `data/curated/TamunaDoublyAcceleratedDistributedOptimizationWithLocalTrainingCompressionAndPartialParticipation.yaml`
- **Primary Source**: Laurent Condat, Ivan Agarský, Grigory Malinovsky, Peter Richtárik — *TAMUNA: Doubly Accelerated Distributed Optimization under Partial Participation* (`https://api.openalex.org/works/W4321471475`).

## Identity & Boundary Resolution

Distinct from Scaffnew / ProxSkip (which uses uncompressed full-client communication without partial participation or sparsification), distinct from CompressedScaffnew (which requires full client participation c = n), and distinct from Scaffold (which does not achieve O(sqrt(kappa)) accelerated communication complexity or support correlated coordinate-mask compression): TAMUNA unifies CompressedScaffnew and Cohort-Squeeze via an active-cohort correlated permutation mask with sparsity parameter s in {2, ..., c}, preserving the zero-sum control variate invariant sum_{i=1}^n h_i^{(r)} = 0 under partial participation and achieving doubly accelerated communication complexity with respect to both the condition number kappa = L/mu and model dimension d.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 567 TAMUNA verified: mse_factor=0.3333, tau=0.9925, err_tamuna=2.108e-23, drift_err=1.007e-22
```
