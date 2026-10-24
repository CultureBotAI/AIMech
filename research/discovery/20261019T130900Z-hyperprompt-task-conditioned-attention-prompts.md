# Discovery Report: Round 706 — HyperPrompt (HyperNetwork-Generated Task-Conditioned Self-Attention Prompts)

- **Timestamp**: `2026-10-19T13:09:00Z`
- **Selected Concept**: `AIMech:HyperPromptTaskConditionedAttentionPrompt` (*HyperPrompt (HyperNetwork-Generated Task-Conditioned Self-Attention Prompts)*)
- **Record Path**: `data/curated/HyperPromptTaskConditionedAttentionPrompt.yaml`
- **Primary Source**: Yun He, Huaixiu Steven Zheng, Yi Tay, Jai Gupta, Yu Du, Vamsi Aribandi, Zhe Zhao, YaGuang Li, Zhao Chen, Donald Metzler, Heng-Tze Cheng, Ed H. Chi — *HyperPrompt: Prompt-based Task-Conditioning of Transformers* (`https://dblp.org/search/publ/api?q=HyperPrompt+Prompt-based+Task-Conditioning&format=xml`).

## Identity & Boundary Resolution

Introduced by Yun He, Huaixiu Steven Zheng, Yi Tay, Jai Gupta, Yu Du, Vamsi Aribandi, Zhe Zhao, YaGuang Li, Zhao Chen, Donald Metzler, Heng-Tze Cheng, and Ed H. Chi (ICML 2022, PMLR 162:8678-8690, arXiv:2203.00759). Distinct from Prefix-Tuning (Li & Liang, ACL 2021; AIMech:PrefixTuning), which optimizes single-task per-layer prefixes without cross-task hypernetworks or global-to-local bottleneck projections, and distinct from HyperFormer (Karimi Mahabadi et al., ACL 2021; AIMech Round 703), which generates post-FFN sequential adapter layers rather than self-attention key/value memory tokens. All three architectural variants (HyperPrompt-Share, HyperPrompt-Sep, and HyperPrompt-Global) are covered within this single record.

## Constructed Boundary & Regime Verification

```text
[PASS] HyperPrompt boundaries verified: params_global=4842752 < params_sep=7176192, rel_increase_2xT=0.0204, out_shape=(3, 4)
```
