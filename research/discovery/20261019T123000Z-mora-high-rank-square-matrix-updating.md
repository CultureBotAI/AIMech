# Discovery Report: Round 667 — MoRA

- **Timestamp**: `2026-10-19T12:30:00Z`
- **Selected Concept**: `AIMech:MoRA` (*MoRA*)
- **Record Path**: `data/curated/MoRA.yaml`
- **Primary Source**: Ting Jiang, Shaohan Huang, Shengyue Luo, Zihan Zhang, Haizhen Huang, Furu Wei, Weiwei Deng, Feng Sun, Qi Zhang, Deqing Wang, Fuzhen Zhuang — *MoRA: High-Rank Updating for Parameter-Efficient Fine-Tuning* (`https://dblp.org/search/publ/api?q=MoRA+High-Rank+Updating+Parameter-Efficient&format=xml`).

## Identity & Boundary Resolution

Distinct from AIMech:LowRankAdaptation (LoRA), which uses (d + k) r trainable parameters across two rectangular matrices A in R^{r x k} and B in R^{d x r} and is algebraically restricted to rank(Delta_W) <= r, and from AIMech:MELoRA, which trains n separate mini-LoRA adapters B_i A_i along the block diagonal. MoRA (Ting Jiang, Shaohan Huang, Shengyue Luo, Zihan Zhang, Haizhen Huang, Furu Wei, Weiwei Deng, Feng Sun, Qi Zhang, Deqing Wang, and Fuzhen Zhuang, arXiv:2405.12130) maximizes update rank under the exact same parameter budget (d + k) r by allocating a single square matrix M in R^{r_hat x r_hat} with r_hat = floor(sqrt((d + k) r)) >> r (for example, r_hat = 256 versus r = 8 when d = k = 4096). Non-parameterized linear operators f_comp: R^k -> R^{r_hat} (or R^{n x r_hat}) and f_decomp: R^{r_hat} -> R^d—instantiated via row/column group sharing (Equations 6-7) for large ranks or input chunk reshaping with RoPE-inspired 2D block-diagonal rotations R_{theta_j, i} (Equations 8-11) for smaller ranks—satisfy f_decomp(M f_comp(x)) = Delta_W x for all x in R^k, allowing M to be merged into W_0 with zero inference latency overhead.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 667 MoRA (Jiang et al. 2024): r_hat_4096=256 (vs r=8), merge_rot_err=4.44e-16, rank_share=4, rank_rot=8>>r=1
```
