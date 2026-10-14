# Nonreversible MCMC discovery — 2026-10-14T20:19:21Z

Two separate DRAFT native algorithms were created with primary evidence and related AIO Markov Chain mappings. This batch does not establish literature saturation.

## Nonreversible Metropolis uniform update

`AIMech:NonreversibleMetropolisUniformUpdate` — `data/curated/NonreversibleMetropolisUniformUpdate.yaml`

A Metropolis transition algorithm that retains a signed uniform acceptance variable, updates it by wrapped translation, and rescales it after an accepted state proposal to preserve a joint target distribution while changing the temporal dependence of acceptance decisions.

Mapping: `AIO:MarkovChain`, `related_match`. The algorithm is associated with a stochastic process/model; no equivalence or inherited network/layer assertion.

## Neal backtracking-suppressed MCMC

`AIMech:NealBacktrackingSuppressedMCMC` — `data/curated/NealBacktrackingSuppressedMCMC.yaml`

A finite-state MCMC construction that augments a reversible chain with its preceding state and replaces a conditional resampling step with a balanced conditional kernel that suppresses immediate backtracking while preserving the target marginal.

Mapping: `AIO:MarkovChain`, `related_match`. The algorithm is associated with a stochastic process/model; no equivalence or inherited network/layer assertion.

## Evidence and boundaries

Root read all 14 pages of Neal 2020 and all 25 pages of Neal 2004, with the documented core-method/figure visual checks. Diaconis–Miclo 2013 was read selectively: PDF pages 2, 31–34, 50; root visually checked page 32. It is correction evidence, not a full review of the spectral paper.

The threshold construction requires a symmetric proposal independent of its persistent signed uniform variable and mandatory acceptance rescaling. Threshold-substep reversibility does not imply reversibility of the composed chain. The pair construction retains the published additional irreducibility assumption and the source’s invalid fast-branch acceptance probability as explicit limitations.

Exact curator calculations check 576 joint-invariance cases, 54 finite pair-chain families and 162 coordinate asymptotic-variance comparisons, plus counterexamples and point-mass boundaries. These are finite arithmetic checks, not a general theorem, author-code replication, performance benchmark or independent scientific approval.

## Identity and frontier

All 442 AIO and 701 preceding native inventory hashes and normalized identities were refreshed immediately before writing. The retained assessment covers all 359 selected semantic rows, 12 complete AIO contexts and 15 complete native neighbors. Ignored-inclusive three-checkout searches and their exact scope are preserved in the JSON report.

The complete 886 prior main-frontier entries were carried forward and these two added entries bring the total to 888. All 393 nested entries remain unchanged. Five newly specified source assessments refine existing parent entries without increasing frontier counts. Ordered overrelaxation and partial-momentum HMC retain their existing keys; Diaconis–Miclo remains correction/further-reading evidence. The broad nonreversible cohort remains partly addressed.

## Provenance

- Full discovery ledger: `research/discovery/20261014T201921Z-nonreversible-mcmc.json`
- Exact calculator: `research/discovery/nonreversible-boundaries.py`
- Bounded supporting audit: `research/discovery/20261014T195934Z-nonreversible-supporting-math-audit.json`

Record objects were validated before creation. Full project gates, canonical saved scientific reviews and publication checks remain separate later work.

## Report metadata correction

Corrected the normalized Neal 2020 experiment description to Bayesian neural-network experiment after the supporting audit; original handoffs remain preserved with an explicit correction annotation. Both concept records and their mappings are unchanged. [Review issue #356](https://github.com/CultureBotAI/AIMech/issues/356).

Audit: `research/discovery/20261014T202221Z-nonreversible-actual-record-audit.json`. Fix verification: `research/discovery/20261014T202307Z-nonreversible-report-fix.json`.
