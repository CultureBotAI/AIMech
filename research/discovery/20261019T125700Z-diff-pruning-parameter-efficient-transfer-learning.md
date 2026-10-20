# Discovery Report: Round 694 — Diff Pruning

- **Timestamp**: `2026-10-19T12:57:00Z`
- **Selected Concept**: `AIMech:DiffPruning` (*Diff Pruning*)
- **Record Path**: `data/curated/DiffPruning.yaml`
- **Primary Source**: Demi Guo, Alexander M. Rush, Yoon Kim — *Parameter-Efficient Transfer Learning with Diff Pruning* (`https://dblp.org/search/publ/api?q=Parameter+Efficient+Transfer+Learning+Diff+Pruning+Guo&format=xml`).

## Identity & Boundary Resolution

Distinct from standard weight pruning and Movement Pruning (AIMech:MovementPruning), which mask the pre-trained parameters theta directly (setting masked weights to zero) rather than masking the additive task difference delta_tau = theta_tau - theta (which preserves the unpruned pre-trained value theta_i when delta_{tau,i} = 0). Also distinct from low-rank additive adapters such as LoRA (AIMech:LowRankAdaptation), which constrain delta_tau to a low-rank matrix product rather than an L0-sparse coordinate/group-gated difference vector.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 694 Diff Pruning (Guo et al., ACL 2021): p_init(alpha=5)=0.9933, E[L0]_struct=2.878, zero_groups(struct=3 > unstruct=0), mse_struct=0.0001 << mse_non_adap=0.4698
```
