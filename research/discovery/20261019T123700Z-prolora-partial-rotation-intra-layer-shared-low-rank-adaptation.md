# Discovery Report: Round 674 — PRoLoRA

- **Timestamp**: `2026-10-19T12:37:00Z`
- **Selected Concept**: `AIMech:PRoLoRA` (*PRoLoRA*)
- **Record Path**: `data/curated/PRoLoRA.yaml`
- **Primary Source**: Sheng Wang, Boyang Xue, Jiacheng Ye, Jiyue Jiang, Liheng Chen, Lingpeng Kong, Chuan Wu — *PRoLoRA: Partial Rotation Empowers More Parameter-Efficient LoRA* (`https://dblp.org/search/publ/api?q=PRoLoRA+Partial+Rotation+Empowers&format=xml`).

## Identity & Boundary Resolution

Distinct from AIMech:LowRankAdaptation (which leaves all r*(h+o) adapter entries unshared, corresponding to the special case u = r) and from inter-layer weight-tying methods such as AIMech:VeraVectorBasedRandomMatrixAdaptation (VeRA) and Tied-LoRA (which share matrices across layers and require matching layer dimensions). PRoLoRA (Partially Rotation-enhanced Low-Rank Adaptation; Sheng Wang, Boyang Xue, Jiacheng Ye, Jiyue Jiang, Liheng Chen, Lingpeng Kong, & Chuan Wu, ACL 2024, arXiv:2402.16902) operates strictly within each layer via four components (Section 3.1, Equations 2-5): (1) Broadcast Reduction partitions the shared rank-(r-u) portion of A and B into m horizontal chunks of width h/m and n vertical chunks of height o/n; (2) Rotation Enhancement differentiates broadcast chunks i in {0..m-1} and j in {0..n-1} by circularly shifting along the rank dimension via A_i = Roll(A_0, i*s_A) and B_j = Roll(B_0, j*s_B); (3) Partially-Sharing Refinement reserves u unshared ranks (A_u in R^{u x h}, B_u in R^{o x u}) so that Delta W = (B_u (+)_h (B_0 (+)_v ... (+)_v B_{n-1})) (A_u (+)_v (A_0 (+)_h ... (+)_h A_{m-1})), breaking the equal-displacement block symmetry of pure rotation with total trainable parameters u(h+o) + h(r-u)/m + o(r-u)/n; and (4) Rectified Initialization samples A_0 ~ U(-g sqrt(3/h), g sqrt(3/h)) using the full matrix fan-in h rather than chunk width h/m.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 674 PRoLoRA (Wang et al., ACL 2024): params=44<80, rolora_diag_err=0.00e+00, prolora_diag_diff=4.7956>1.0, init_bound_ratio=1.4142
```
