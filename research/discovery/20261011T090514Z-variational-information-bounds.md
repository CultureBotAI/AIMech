# Variational information bounds — 2026-10-11T09:05:14Z

Added six concepts; AIMech now contains 214 native DRAFT records.

| Record | Scope |
| --- | --- |
| [AIMech:BarberAgakovBound](../../data/curated/BarberAgakovBound.yaml) | A variational lower bound on mutual information formed by adding input entropy to the expected log probability assigned by a normalized conditional decoder to the input given the output. |
| [AIMech:VariationalInformationMaximizationIMAlgorithm](../../data/curated/VariationalInformationMaximizationIMAlgorithm.yaml) | An alternating optimization procedure that adjusts a noisy encoder and a variational decoder to increase the Barber–Agakov lower bound on transmitted information for a fixed input distribution. |
| [AIMech:NguyenWainwrightJordanBound](../../data/curated/NguyenWainwrightJordanBound.yaml) | A variational lower bound on Kullback–Leibler divergence that subtracts a product-distribution exponential critic moment from a joint-distribution critic expectation when specialized to mutual information. |
| [AIMech:TUBABound](../../data/curated/TUBABound.yaml) | A tractable unnormalized Barber–Agakov lower-bound parameterization that uses a real critic and a positive output-dependent normalizer to replace an intractable log partition term by a linear upper bound. |
| [AIMech:InterpolatedVariationalInformationBound](../../data/curated/InterpolatedVariationalInformationBound.yaml) | A family of multi-sample mutual-information lower bounds that interpolates the critic’s empirical partition estimate with a positive variational normalizer inside a ratio, connecting NWJ and InfoNCE parameterizations. |
| [AIMech:LeaveOneOutMutualInformationUpperBound](../../data/curated/LeaveOneOutMutualInformationUpperBound.yaml) | An expectation-level upper bound on mutual information that compares a known conditional density for each paired sample with a mixture of conditional densities from the other independent inputs in its batch. |

The IM procedure remains separate from its BA objective. TUBA explicitly reparameterizes NWJ; its separate record preserves the named normalizer parameterization. The interpolated bound changes the denominator rather than averaging scalar bounds. The leave-one-out upper bound requires normalized, evaluable conditionals and independent examples.

Five mathematical bounds have explicit no-match assessments for the pinned AIO snapshot; IM has a qualified FeatureExtraction relation.

A [deterministic calculation](poole-interpolation-ceiling.py) evaluates the displayed interpolation formula and yields 2.08113, above the paper’s printed log(4)=1.38629 ceiling but below true information and the conservative ceiling including +1. The record labels this curator analysis and preserves paper/supplement/notebook differences. No model was trained.

[Issue46](https://github.com/CultureBotAI/AIMech/issues/46) addresses missing source metadata/citations for implementation limitations. The corrected drafts and original/final hashes are preserved in the JSON ledger. The scientific review is author self-review, not independent approval.

Original kernel density-ratio estimators, JS-trained NWJ estimation, DV and other information constructions, plus the earlier frontier, remain pending. Discovery continues.
