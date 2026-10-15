# K-SVD and continuous-time Bayesian networks — 2026-10-15T00:11:24Z

Two narrowly scoped DRAFT concepts were created from inspected primary evidence.

## K-SVD

`AIMech:KSVD` — `data/curated/KSVD.yaml`

A dictionary-learning algorithm that alternates sparse coding of training samples with sequential updates of each dictionary atom and its active coefficients using a leading rank-one singular-value approximation of the support-restricted reconstruction residual.

## Continuous-time Bayesian network

`AIMech:ContinuousTimeBayesianNetwork` — `data/curated/ContinuousTimeBayesianNetwork.yaml`

A finite-state continuous-time model family combining a separate initial Bayesian-network distribution with a directed, possibly cyclic graph of current-parent-dependent conditional intensity matrices, whose single-variable jump rates amalgamate into a homogeneous joint Markov generator.

## Evidence and scope

K-SVD alternates sparse coding with sequential support-restricted atom/coefficient updates. Exact block descent does not establish arbitrary recoding descent, a unique dictionary or convergence to a local minimizer. The broader BatchOMP/approximate-K-SVD owner remains partial.

CTBN represents a finite homogeneous process with a separate initial BN and possibly cyclic local-rate graph. Single-coordinate instantaneous jumps can compose into multiple changes over time. Zero-rate guards and correlated initial-law qualifications remain explicit. A unique stationary limiting law independent of initial distribution is not guaranteed.

Two unchanged original curator calculators and their actual first executions/root reproductions are retained. K-SVD uses supplied rational SVD certificates; CTBN uses exact finite algebra and rational enclosures of nonrational exponential probabilities. Neither executes author code, trains a model or reproduces a benchmark.

Source page/index/display caveats, K-SVD locator-only research corrections, CTBN case-list metadata correction and the draft convergence clarification retain their original/current lineage. Source acquisition precision and source-reading roles remain distinct.

All 1155 current canonical identities were refreshed; four complete checkouts were searched including ignored and hidden files. Existing main-frontier owners 461 and 690 were updated in place. The main count remains 898 and all 393 nested entries remain unchanged. No duplicate leaves or saturation claim.

Full structured ledger: `research/discovery/20261015T001124Z-ksvd-and-continuous-time-bayesian-networks.json`

Supporting agents and root belong to the same author workflow. Canonical reviews, full project gates and publication remain separate later actions.
