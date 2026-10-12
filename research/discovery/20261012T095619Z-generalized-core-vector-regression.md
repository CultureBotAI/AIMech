# Generalized core vector machines and regression

Added native DRAFT records for [generalized CVM](../../data/curated/GeneralizedCoreVectorMachine.yaml) and [CVR](../../data/curated/CoreVectorRegression.yaml), bringing the maintained collection to517. Both have related mappings to the pinned AIO SupportVectorMachine model. The general constrained-ball solver and its regression-specific formulation remain distinct.

All23 primary PDF pages were visually read. [Exact calculations](generalized-core-vector-boundaries.py) verify objective scaling, a negative learned margin and shift-sensitive approximate stopping. These limits qualify the source claims; no historical implementation or benchmark was executed.

Three newly discovered extension cohorts remain pending full-method inspection. The broader CVM and author-catalogue cohorts are partly addressed. There are443 pending cohorts plus other unresolved work; discovery continues.

Author self-review identified ambiguous objective-sign wording in the generalized-CVM definition. [Issue169](https://github.com/CultureBotAI/AIMech/issues/169) tracks the correction: positive semidefiniteness now explicitly describes the kernel Gram matrix. [Issue170](https://github.com/CultureBotAI/AIMech/issues/170) records the missing precursor citation, now added to definition evidence. Detailed formulas and the CVR record are unchanged.
