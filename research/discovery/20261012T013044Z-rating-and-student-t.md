# Rating models and Student-t boundaries — 2026-10-12T01:30:44Z

Added three native DRAFT records, bringing the maintained collection to 450.

| Record | Defining scope |
| --- | --- |
| [RBM-CF](../../data/curated/RestrictedBoltzmannMachineCollaborativeFiltering.yaml) | Shared categorical-rating models indexed by observed item set |
| [PoT](../../data/curated/ProductOfStudentT.yaml) | Proper product density of Student-t-shaped filter factors |
| [IWF](../../data/curated/IteratedWienerFilter.yaml) | Iterative MAP denoising under a fixed PoT prior |

Generic sparse coding already exists as [AIO:SparseLearning](../../data/aio/SparseLearning.yaml); no duplicate was added.

All 31 primary PDF pages were visually read. [Finite calculations](rating-and-student-t-boundaries.py) distinguish omitted and marginalized items, exact and plug-in predictions, target and pseudoinverse sampling variances, and initialization-dependent local minima. No author implementation or benchmark ran.

Eleven new provisional cohorts leave 337 pending leads and other unresolved dispositions; discovery continues.
