# Constraint-repair methods — 2026-10-11T14:53:01Z

Added three native DRAFT records, bringing the maintained collection to 313.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:MinConflicts](../../data/curated/MinConflicts.yaml) | A constraint-repair value-selection heuristic that uses a complete assignment to choose a value for a conflicted variable with as few conflicts as possible, breaking tied minimum choices randomly in the inspected formulation. |
| [AIMech:BreakoutMethod](../../data/curated/BreakoutMethod.yaml) | A finite constraint-satisfaction search method that takes strictly improving local assignment changes under a weighted nogood cost and increases the weights of all currently violated nogoods at a non-solution local minimum to change the search landscape. |
| [AIMech:GSAT](../../data/curated/GSAT.yaml) | A randomized local-search SAT procedure that repeatedly flips a Boolean variable giving the largest change toward more satisfied CNF clauses, breaks tied choices randomly, and restarts from a random complete assignment under specified flip and attempt budgets. |

All three methods have bounded AIO no-match assessments. The records distinguish a value heuristic from its outer search, nogood reweighting from idealized state-cost filling, and GSAT model finding from an unsatisfiability proof. The literal GSAT final-flip test boundary remains explicit.

The [finite examples](constraint-repair-boundaries.py) and JSON ledger document scope, evidence, actual reading, mapping and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 183 pending inspection leads.
