# Discovery Report: Round 677 — Tied-LoRA

- **Timestamp**: `2026-10-19T12:40:00Z`
- **Selected Concept**: `AIMech:TiedLoRA` (*Tied-LoRA*)
- **Record Path**: `data/curated/TiedLoRA.yaml`
- **Primary Source**: Adithya Renduchintala, Tugrul Konuk, Oleksii Kuchaiev — *Tied-LoRA: Enhancing parameter efficiency of LoRA with Weight Tying* (`https://dblp.org/rec/conf/naacl/RenduchintalaKK24.xml`).

## Identity & Boundary Resolution

Distinct from standard LoRA (AIMech:LoRA, which assigns independent untied projection matrices B_i and A_i to every adapted layer without diagonal scaling vectors), from VeRA (AIMech:VeRA, which freezes untied randomly initialized matrices B_i and A_i and trains only scaling vectors, a special case termed LoRA_vbuA in the Tied-LoRA taxonomy), and from PRoLoRA (AIMech:PRoLoRA, which tiles intra-layer chunks via roll-based partial rotation and block-shared submatrices rather than tying full low-rank projection matrices across transformer layers with selective training of {v, B, u, A}). Formulated by Renduchintala, Konuk, and Kuchaiev (NAACL 2024, arXiv:2311.09578).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 677 Tied-LoRA (Renduchintala et al., NAACL 2024): tl5_reduction=96.875%, tl6_r64_pct=4.30%, max_merge_err=9.33e-16
```
