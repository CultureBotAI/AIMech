# Fairness criteria — 2026-10-11T04:49:36Z

Added five evidence-backed criteria, bringing the native collection to 99 DRAFT records.

| Record | AIO relationship |
| --- | --- |
| [AIMech:EqualizedOdds](../../data/curated/EqualizedOdds.yaml) | related_match to AIO:Classification |
| [AIMech:EqualOpportunity](../../data/curated/EqualOpportunity.yaml) | related_match to AIO:BinaryClassification |
| [AIMech:DemographicParity](../../data/curated/DemographicParity.yaml) | related_match to AIO:Classification |
| [AIMech:LipschitzIndividualFairness](../../data/curated/LipschitzIndividualFairness.yaml) | related_match to AIO:Classification |
| [AIMech:CounterfactualFairness](../../data/curated/CounterfactualFairness.yaml) | related_match to AIO:CausalGraphicalModel |

The schema now distinguishes evaluation criteria from evaluation procedures and enforcement algorithms. The records retain conditioning variables, metric assumptions, causal-model dependence and finite-data limits.

The JSON companion records primary PDF versions, hashes, actual visual reads, identity searches, source caveats and the active frontier. Counterfactual/parity relationships retain their assumptions; criterion satisfaction is not an overall fairness verdict. Discovery continues.
