# Delayed, multiple-try and adaptive sampling — 2026-10-11T07:28:09Z

Added six concepts; the native collection contains 181 DRAFT records.

| Record | Scope |
| --- | --- |
| [AIMech:DelayedRejectionMetropolis](../../data/curated/DelayedRejectionMetropolis.yaml) | A Metropolis-Hastings sampling procedure that can propose another candidate after rejection within the same transition, correcting acceptance for the probabilities of the forward and reversed rejected paths. |
| [AIMech:SymmetricDelayedRejection](../../data/curated/SymmetricDelayedRejection.yaml) | The delayed-rejection specialization using the same symmetric proposal kernel at every stage, centered through the last rejected candidate, with acceptance determined by the largest previous rejected target density. |
| [AIMech:MultipleTryMetropolis](../../data/curated/MultipleTryMetropolis.yaml) | A Metropolis sampling algorithm that selects a candidate from several weighted forward proposals, draws a backward reference set containing the original state, and corrects acceptance using the ratio of their total weights. |
| [AIMech:MultipleTryMetropolisWithinGibbs](../../data/curated/MultipleTryMetropolisWithinGibbs.yaml) | A coordinate-update sampler that applies a multiple-try Metropolis transition to a conditional target while holding all other coordinates fixed. |
| [AIMech:ConjugateGradientMonteCarlo](../../data/curated/ConjugateGradientMonteCarlo.yaml) | A population Markov sampler that obtains a local-optimization anchor from one population member and updates another member along the anchor line with a multiple-try transition targeting a radial-Jacobian-adjusted density. |
| [AIMech:RobustAdaptiveMetropolis](../../data/curated/RobustAdaptiveMetropolis.yaml) | An adaptive random-walk Metropolis algorithm that updates the proposal shape factor by a rank-one transformation driven by the proposal direction and the difference between its acceptance probability and a chosen target rate. |

All six have explicit method-to-process related mappings to AIO Markov Chain. RAM’s history-dependent adaptation and CGMC’s population state are stated explicitly.

The source audit preserves rejected-path corrections, backward reference sets, the radial Jacobian, and RAM’s conditional stability assumptions. Two source equation inconsistencies are documented; the records use the verified core rules.

AM/DRAM full-method access, auxiliary multiple-try variants, original adaptive direction sampling and the broader discovery frontier remain open. Six additions do not establish saturation.
