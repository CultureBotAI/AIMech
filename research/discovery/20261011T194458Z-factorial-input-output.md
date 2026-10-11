# Factorial and input-output hidden Markov concepts — 2026-10-11T19:44:58Z

Added two native DRAFT model families and a structured variational inference procedure, bringing the maintained collection to 379.

| Record | Definition |
| --- | --- |
| [AIMech:FactorialHiddenMarkovModel](../../data/curated/FactorialHiddenMarkovModel.yaml) | A directed latent sequence-model family in which several independently evolving hidden Markov chains jointly determine the observation distribution at each time. |
| [AIMech:InputOutputHiddenMarkovModel](../../data/curated/InputOutputHiddenMarkovModel.yaml) | A conditional latent sequence-model family whose discrete hidden-state transitions and state-specific observation distributions depend on the current external input. |
| [AIMech:StructuredVariationalInferenceForFactorialHMMs](../../data/curated/StructuredVariationalInferenceForFactorialHMMs.yaml) | A variational inference procedure for factorial hidden Markov models that approximates the posterior by independent chain-path distributions while retaining temporal dependence within each chain. |

Both model families have broad Bayesian-network mappings; FHMM has a related Markov-chain mapping, and IOHMM a related recurrent-network mapping. The inference procedure has related model/process mappings.

The [finite examples](factorial-input-output-boundaries.py) and JSON ledger document actual reading of 37 PDF pages, identity and mapping checks, posterior dependence, conditional sequence likelihoods, structured approximation and source-formula qualifications. No benchmark result is asserted.

Adversarial author self-review is required. Discovery remains active with 208 pending inspection leads.
