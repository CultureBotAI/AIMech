# Discovery Report: Round 733 — GlobalE and LocalE Entropy-Based Prompt Ordering

- **Timestamp**: `2026-10-19T13:36:00Z`
- **Selected Concept**: `AIMech:GlobalEAndLocalEEntropyBasedPromptOrdering` (*GlobalE and LocalE Entropy-Based Prompt Ordering*)
- **Record Path**: `data/curated/GlobalEAndLocalEEntropyBasedPromptOrdering.yaml`
- **Primary Source**: Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, Pontus Stenetorp — *Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity* (`https://dblp.org/rec/conf/acl/LuBMRS22.xml`).

## Identity & Boundary Resolution

Distinct from post-hoc output probability calibration methods such as Contextual Calibration (AIMech:CalibrateBeforeUseContextualCalibration) and Domain-Conditional PMI (AIMech:PMIDCDomainConditionalPointwiseMutualInformation), which rescale label probabilities for a fixed prompt rather than ranking and selecting optimal permutations of in-context demonstrations. Also distinct from retrieval-based example selection methods that choose which examples to include per test query rather than ordering a fixed few-shot support set without any labeled development data.

## Constructed Boundary & Regime Verification

```text
GlobalE/LocalE verification passed: 24 permutations evaluated, best GlobalE=0.6931 (acc=1.00), worst GlobalE=-0.0000 (acc=0.50)
```
