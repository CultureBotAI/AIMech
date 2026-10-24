# Discovery Report: Round 576 — CompressedScaffnew

- **Timestamp**: `2026-10-19T10:59:00Z`
- **Selected Concept**: `AIMech:CompressedScaffnewDoublyAcceleratedLocalTrainingAndCompression` (*CompressedScaffnew*)
- **Record Path**: `data/curated/CompressedScaffnewDoublyAcceleratedLocalTrainingAndCompression.yaml`
- **Primary Source**: Laurent Condat, Ivan Agarsky, Peter Richtarik — *Doubly Accelerated Federated Learning: Improved Rate with Local Training and Communication Compression* (`https://dblp.org/search/publ/api?q=CompressedScaffnew&format=json`).

## Identity & Boundary Resolution

Distinct from uncommitted or uncompressed Scaffnew/ProxSkip (which requires full d-dimensional vector communication at every triggered sync round) and from independent random sparsifiers (which break Scaffnew's zero-sum control-variate invariant sum_{i=1}^n h_i^t = 0). CompressedScaffnew couples local training with a shared s-active-per-row permutation mask so that the control-variate updates sum to zero coordinatewise while compressing uplink communication by factor s/n.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 576 CompressedScaffnew verified: eta=0.5714, rho=0.9869, psi_0=5.099e+03 -> psi_T=1.435e-15
```
