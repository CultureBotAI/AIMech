# Entropy Search and Predictive Entropy Search — 2026-10-15T00:57:14Z

Two narrow DRAFT algorithms were created from inspected primary evidence.

## Entropy Search

`AIMech:EntropySearch` — `data/curated/EntropySearch.yaml`

A Bayesian global optimization algorithm that approximates the location of a function minimum on sampled representer points using expectation propagation, and chooses evaluations by an approximate expected reduction in relative-entropy loss for that minimizer belief.

## Predictive Entropy Search

`AIMech:PredictiveEntropySearch` — `data/curated/PredictiveEntropySearch.yaml`

A Bayesian global optimization algorithm that approximates information about the global maximizer by subtracting maximizer-conditioned predictive entropy from ordinary predictive entropy, using approximate maximizer samples and Gaussian constraint approximations.

## Evidence and scope

ES and PES share an ideal fixed-hyperparameter optimizer-information objective after a consistent minimum/maximum convention. ES uses representer-point probabilities, EP derivatives and prospective relative-loss approximation; PES uses approximate maximizer draws and constraint-based predictive-entropy inference. Shared ideal information does not collapse these algorithms or imply their selected evaluations always differ.

ES proposal correction, boundary atoms and unresolved literal innovation/Taylor notation remain explicit. PES finite-feature posterior approximation, interior derivative constraints, Hessian limitations, block ordering, variance degeneracy and conditional hyperparameter averaging remain qualified. No author implementation or empirical advantage is claimed.

One unchanged successor curator calculator is retained with its original script/result, five-site absolute-tolerance correction, actual original/successor executions and distinct root reproductions. Rational probabilities and finite matrix algebra are separate from floating natural-log entropy checks at absolute tolerance 2e-14 with zero relative tolerance. The preparation-only six-versus-five call-count failure is retained; no mathematical execution failure is invented.

All 1157 current canonical identities were refreshed; four complete checkouts were searched including ignored and hidden files with fixed-string word matching. Existing owners 176 and 177 were updated in place. Main frontier 898 and all 393 nested entries remain unchanged; no duplicate leaves or saturation claim.

The official PES supplement PDF is pinned separately from its downloaded ZIP; archive access time is explicitly inherited for the extracted member. Precise acquisition and source-reading roles remain distinct.

Full structured ledger: `research/discovery/20261015T005714Z-entropy-search-and-predictive-entropy-search.json`

Root and supporting agents belong to one author workflow. Formal reviews, full gates and publication remain later actions.
