# Discovery Report: Round 729 — Noisy Channel Language Model Prompting

- **Timestamp**: `2026-10-19T13:32:00Z`
- **Selected Concept**: `AIMech:NoisyChannelLanguageModelPrompting` (*Noisy Channel Language Model Prompting*)
- **Record Path**: `data/curated/NoisyChannelLanguageModelPrompting.yaml`
- **Primary Source**: Sewon Min, Mike Lewis, Hannaneh Hajishirzi, Luke Zettlemoyer — *Noisy Channel Language Model Prompting for Few-Shot Text Classification* (`https://dblp.org/search/publ/api?q=Noisy+Channel+Language+Model+Prompting+for+Few-Shot+Text+Classification+Min&format=xml`).

## Identity & Boundary Resolution

Distinct from direct prompting and direct Prompt Tuning (AIMech:InContextLearning, AIMech:PromptTuning), which compute P_LM(v(c_i) | x) and collapse when training labels are imbalanced or when test labels are unseen during training, and from zero-shot Domain Conditional PMI (Holtzman et al., EMNLP 2021, AIMech:PMIDCDomainConditionalPointwiseMutualInformation), which reweights zero-shot direct continuations by a domain premise rather than training continuous channel prompts u_1...u_n or multiplying K reversed demonstration likelihoods.

## Constructed Boundary & Regime Verification

```text
Noisy Channel Language Model Prompting verification passed.
```
