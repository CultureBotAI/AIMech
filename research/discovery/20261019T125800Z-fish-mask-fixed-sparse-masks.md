# Discovery Report: Round 695 — FISH Mask

- **Timestamp**: `2026-10-19T12:58:00Z`
- **Selected Concept**: `AIMech:FISHMask` (*FISH Mask*)
- **Record Path**: `data/curated/FISHMask.yaml`
- **Primary Source**: Yi-Lin Sung, Varun Nair, Colin Raffel — *Training Neural Networks with Fixed Sparse Masks* (`https://dblp.org/search/publ/api?q=Training+Neural+Networks+Fixed+Sparse+Masks+Sung&format=xml`).

## Identity & Boundary Resolution

Distinct from Diff Pruning (AIMech:DiffPruning), which optimizes a trainable stretched Hard-Concrete mask over an additive diff vector throughout training at the cost of extra memory and 1.5x-2x slower minibatches, and from BitFit (AIMech:BitFit), which heuristically updates only bias vectors (and cannot be applied to bias-free architectures such as T5). Also distinct from Fisher weight pruning methods, which zero out weights to sparsify the network rather than keeping all pre-trained weights intact while restricting gradient updates to the top-k Fisher coordinates.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 695 FISH Mask (Sung et al., NeurIPS 2021): fish_mask=[0, 3, 6], loss_fish=0.01094 ~= loss_dense=0.01094 << loss_random=0.60910, ckpt_factor(s=10%)=5.0x
```
