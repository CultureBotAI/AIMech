# Core and ball vector machines

Added native DRAFT records for [CVM](../../data/curated/CoreVectorMachine.yaml) and [BVM](../../data/curated/BallVectorMachine.yaml), bringing the maintained collection to515. Both have explicit related mappings to the pinned AIO SupportVectorMachine model. The algorithms remain distinct: CVM recomputes core minimum enclosing balls; BVM uses fixed-radius center movement and optional refinement.

All49 pages of the original CVM paper, its published critique and the BVM paper were visually read. The authors’ response is retained as abstract-only context because its full PDF could not be accessed. [Exact calculations](core-ball-vector-boundaries.py) document formulation, radius and sampling limits. No historical implementation or benchmark was executed.

The author publication catalogue adds a source cohort, while CVM extensions remain partially addressed. There are441 pending cohorts and other unresolved work; discovery continues.

Author self-review identified five inaccurate CVM source locators. [Issue167](https://github.com/CultureBotAI/AIMech/issues/167) tracks their correction; scientific statements and identities are unchanged. The initial and successor structured reviews preserve the finding and its resolution.
