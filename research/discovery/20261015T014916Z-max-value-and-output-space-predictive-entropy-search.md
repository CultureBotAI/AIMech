# Max-value and Output-space Predictive Entropy Search — 2026-10-15T01:49:16Z

Two narrow DRAFT algorithms were created from inspected primary evidence.

## Max-value Entropy Search

`AIMech:MaxValueEntropySearch` — `data/curated/MaxValueEntropySearch.yaml`

A Bayesian global optimization algorithm that chooses evaluations using an approximate information acquisition for the latent maximum function value, averaging local truncated-Gaussian entropy differences over approximate maximum-value samples.

## Output-space Predictive Entropy Search

`AIMech:OutputSpacePredictiveEntropySearch` — `data/curated/OutputSpacePredictiveEntropySearch.yaml`

A Bayesian global optimization algorithm that selects evaluations using an approximation to information about the latent maximum function value, combining Gaussian expectation-propagation constraints at observed inputs with candidate truncation, moment matching and predictive observation entropy.

## Evidence and scope

MES and OPES share an ideal maximum-value information target while their operational approximations differ. MES uses local truncated-latent entropy; OPES combines observed-latent EP constraints, candidate moment matching and noisy Gaussian observation entropy. Shared ideal information does not make the algorithms aliases or imply different decisions for every dataset.

The finite attained maximum assumption is explicit. Local inequalities do not equal global-maximum conditioning; zero variance, noise, matrix inversion, tail stability and maximum sampling remain qualified. No author implementation, general regret theorem or empirical advantage is claimed.

Two unchanged accepted curator calculators are retained. The original MES CDF witness run failed; its empty stdout, traceback, exact correction and successful successor/root executions remain separate. OPES passed its first scalar diagnostic and root reproduction. Exact rational finite examples are distinguished from floating normal, Gumbel and entropy calculations.

All 1159 current canonical identities were refreshed; four complete checkouts were searched including ignored and hidden files with fixed-string word matching. All 898 prior main rows and 393 nested rows are unchanged. Two assessed distinct leaves bring the main frontier to 900; ES/PES owners are not relabeled and no source family is declared exhausted.

The OPES author catalog attributes the workshop to December 2015. Its pinned PDF has a February 28, 2016 embedded build date; the hosting modification header and actual 2026 acquisition are separate provenance. Its advertised longer derivation remains unlocated in bounded searches. The official MES 2017 paper and appendix support the records; later arXiv comparison is separately scoped.

Full structured ledger: `research/discovery/20261015T014916Z-max-value-and-output-space-predictive-entropy-search.json`

Root and supporting agents belong to one author workflow. Formal reviews, full gates and publication remain later actions.
