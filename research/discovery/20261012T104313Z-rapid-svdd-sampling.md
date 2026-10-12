# RAPID support vector data description sampling

Added [RAPID](../../data/curated/RapidSupportVectorDataDescriptionSampling.yaml) as a native DRAFT preprocessing method, with a broader AIO Preprocessing mapping. The collection now contains519 native concepts and442 unchanged generated AIO records.

All27 final paper pages were visually read and versioned author source was inspected. [Exact calculations](rapid-svdd-boundaries.py) distinguish the printed pseudocode from the intended rule, and finite SVDD boundaries from unweighted density thresholds. The record also preserves the kernel-formula discrepancy and the unpinned historical sampling revision. No Julia code, model fit or benchmark was executed.

Two new source cohorts cover one-class active learning and SVDD bandwidth criteria. There are449 pending cohorts plus partly addressed work; discovery continues.

Review issue [#174](https://github.com/CultureBotAI/AIMech/issues/174) was addressed by making the input, kernel and singleton-stop conventions explicit and extending the pseudocode locator through its deletion step. The stricter public-code stopping rule remains separately documented.
