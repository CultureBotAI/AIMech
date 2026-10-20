# Discovery Report: Round 665 — Delta-LoRA

- **Timestamp**: `2026-10-19T12:28:00Z`
- **Selected Concept**: `AIMech:DeltaLoRA` (*Delta-LoRA*)
- **Record Path**: `data/curated/DeltaLoRA.yaml`
- **Primary Source**: Bojia Zi, Xianbiao Qi, Lingzhi Wang, Jianan Wang, Kam-Fai Wong, Lei Zhang — *Delta-LoRA: Fine-Tuning High-Rank Parameters with the Delta of Low-Rank Matrices* (`https://dblp.org/search/publ/api?q=Delta-LoRA+Fine-Tuning+High-Rank+Parameters&format=xml`).

## Identity & Boundary Resolution

Distinct from AIMech:LowRankAdaptation (LoRA), which keeps the pretrained matrix W frozen throughout training and restricts the cumulative weight update to a rank-r subspace, and from AIMech:ReLoRA, which periodically merges A B into W and reinitializes the low-rank factors with partial optimizer resets. Delta-LoRA (Bojia Zi, Xianbiao Qi, Lingzhi Wang, Jianan Wang, Kam-Fai Wong, and Lei Zhang, arXiv:2309.02411) observes that when the Dropout layer inside the LoRA branch is removed, the forward transformation h_{i+1} = W h_i + (alpha/r) A B h_i yields identical partial derivatives g_W = dL/dW = (dL/dh_{i+1}) h_i^T = dL/d(AB) = g_{AB}. Rather than allocating O(c d) gradient and first/second-moment optimizer buffers for W, Delta-LoRA updates A and B via AdamW and uses the consecutive step difference Delta_AB = A^{(t+1)} B^{(t+1)} - A^{(t)} B^{(t)} as a memory-free surrogate update direction for W after K warm-up steps: W^{(t+1)} = W^{(t)} + lambda * (alpha/r) * (A^{(t+1)} B^{(t+1)} - A^{(t)} B^{(t)}).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 665 Delta-LoRA (Zi et al. 2023): drop_disparity=12.9720>0, eq8_err=4.06e-16, loss_delta_lora=5.0129<loss_lora=5.4239
```
