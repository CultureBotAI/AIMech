# Discovery Report: Round 669 — O-LoRA

- **Timestamp**: `2026-10-19T12:32:00Z`
- **Selected Concept**: `AIMech:OLoRA` (*O-LoRA*)
- **Record Path**: `data/curated/OLoRA.yaml`
- **Primary Source**: Xiao Wang, Tianze Chen, Qiming Ge, Han Xia, Rong Bao, Rui Zheng, Qi Zhang, Tao Gui, Xuanjing Huang — *Orthogonal Subspace Learning for Language Model Continual Learning* (`https://dblp.org/search/publ/api?q=Orthogonal+Subspace+Learning+Language+Model+Continual+Learning+Xiao+Wang&format=xml`).

## Identity & Boundary Resolution

Distinct from AIMech:LowRankAdaptation (LoRA), which adapts a model to a single static task and suffers catastrophic forgetting when sequentially updated across multiple tasks, and from Orthogonal Gradient Descent (OGD), which requires storing explicit historical data gradients across all model parameters. O-LoRA (Xiao Wang, Tianze Chen, Qiming Ge, Han Xia, Rong Bao, Rui Zheng, Qi Zhang, Tao Gui, and Xuanjing Huang, Findings of EMNLP 2023, arXiv:2310.14152) treats the column space U_i = span(a_i^1, ..., a_i^r) of each past task's frozen LoRA factor A_i in R^{d x r} as a parameter-efficient proxy for that task's gradient subspace. When learning task t on dataset D_t, O-LoRA optimizes sum_{(x,y) in D_t} log p_Theta(y | x) + lambda_1 sum_{i=1}^{t-1} L_orth(A_i, A_t), where O_{i,t} = A_i^T A_t in R^{r x r} and L_orth(A_i, A_t) = sum_{j,k} ||O_{i,t}[j, k]||^2. At inference time (or periodically during training), all learned adapters are summed into the base weights W_init := W_init + sum_{i=1}^t A_i B_i without requiring task IDs or replay buffers.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 669 O-LoRA (Wang et al. 2023): orth_olora=2.20e-02<<orth_inclora=13.6582, interf_olora=1.97e-01<<interf_inclora=51.5458
```
