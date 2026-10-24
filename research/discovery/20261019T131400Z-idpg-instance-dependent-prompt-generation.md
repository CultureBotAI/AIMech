# Discovery Report: Round 711 — Instance-Dependent Prompt Generation

- **Timestamp**: `2026-10-19T13:14:00Z`
- **Selected Concept**: `AIMech:IDPGInstanceDependentPromptGeneration` (*Instance-Dependent Prompt Generation*)
- **Record Path**: `data/curated/IDPGInstanceDependentPromptGeneration.yaml`
- **Primary Source**: Zhuofeng Wu, Sinong Wang, Jiatao Gu, Rui Hou, Yuxiao Dong, V. G. Vinod Vydiswaran, Hao Ma — *IDPG: An Instance-Dependent Prompt Generation Method* (`https://dblp.org/search/publ/api?q=IDPG+An+Instance-Dependent+Prompt+Generation+Method&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Zhuofeng Wu, Sinong Wang, Jiatao Gu, Rui Hou, Yuxiao Dong, V. G. Vinod Vydiswaran, and Hao Ma (NAACL 2022, arXiv:2204.04497) as Instance-Dependent Prompt Generation (IDPG / S-IDPG-PHM / M-IDPG-PHM). Distinct from static Prompt Tuning and SPoT (AIMech:SPoTSoftPromptTransfer), which use a fixed input-independent prompt per task (recovered as the degenerate case W = 0 in IDPG where only the second-layer bias is active); from ATTEMPT (AIMech:ATTEMPTAttentionalMixturesOfSoftPrompts), which interpolates pre-trained source-task prompts via sub-query attention rather than generating prompts through a PHM bottleneck MLP; and from Hyperdecoder (AIMech:HyperdecoderInstanceSpecificDecoderAdapter), which generates decoder adapter weights from encoder hidden states rather than layer-wise soft prompt tokens.

## Constructed Boundary & Regime Verification

```text
[PASS] IDPG boundaries verified: S-IDPG-PHM=105.25K vs DNN=1541.2K, M-IDPG-PHM=134K, diff_inst=8.4362>0, diff_static=0.0e+00
```
