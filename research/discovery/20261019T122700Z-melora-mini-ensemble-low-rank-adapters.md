# Discovery Report: Round 664 — MELoRA

- **Timestamp**: `2026-10-19T12:27:00Z`
- **Selected Concept**: `AIMech:MELoRA` (*MELoRA*)
- **Record Path**: `data/curated/MELoRA.yaml`
- **Primary Source**: Pengjie Ren, Chengshun Shi, Shiguang Wu, Mengqi Zhang, Zhaochun Ren, Maarten de Rijke, Zhumin Chen, Jiahuan Pei — *MELoRA: Mini-Ensemble Low-Rank Adapters for Parameter-Efficient Fine-Tuning* (`https://dblp.org/rec/conf/acl/RenSWZRCP24.xml`).

## Identity & Boundary Resolution

Distinct from AIMech:LowRankAdaptation (LoRA), which applies a single dense low-rank update B A in R^{d_{out} x d_{in}} of rank r using r(d_{in} + d_{out}) parameters, and from multi-head or mixture-of-LoRA architectures that sum multiple full-dimension low-rank matrices across the entire feature space. MELoRA (Pengjie Ren, Chengshun Shi, Shiguang Wu, Mengqi Zhang, Zhaochun Ren, Maarten de Rijke, Zhumin Chen, and Jiahuan Pei, ACL 2024, pp. 3052-3064, arXiv:2402.17263) splits the input vector x in R^{d_{in}} into n contiguous segments x_i in R^{d_{in}/n} and applies an independent mini-LoRA module B_i A_i of inner rank r/n (with A_i in R^{(r/n) x (d_{in}/n)} and B_i in R^{(d_{out}/n) x (r/n)}) to each segment, concatenating the outputs. Equivalently, the overall weight update is the block-diagonal matrix Delta_W = diag(B_1 A_1, ..., B_n A_n) in R^{d_{out} x d_{in}}. Because the rank of a block-diagonal matrix equals the sum of the ranks of its diagonal blocks, rank(Delta_W) = sum_{i=1}^n rank(B_i A_i) <= n * (r/n) = r, while the total number of trainable parameters is n * (r/n) * (d_{in}/n + d_{out}/n) = r(d_{in} + d_{out}) / n.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 664 MELoRA (Ren et al. 2024): CaseA(params=64<256, rank=8==8), CaseB(params=96==96, rank=12>3), eq5_diff=0.00e+00
```
