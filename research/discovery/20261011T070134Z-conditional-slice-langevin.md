# Conditional, slice and Langevin sampling — 2026-10-11T07:01:34Z

Added eight concepts; the native collection now contains 167 DRAFT records.

| Record | Method boundary |
| --- | --- |
| [AIMech:GibbsSampling](../../data/curated/GibbsSampling.yaml) | A Markov chain Monte Carlo algorithm that repeatedly draws a coordinate or block from its full conditional distribution given the current values of the remaining coordinates. |
| [AIMech:MetropolisWithinGibbs](../../data/curated/MetropolisWithinGibbs.yaml) | A componentwise Monte Carlo scheme that uses Metropolis–Hastings transitions targeting full conditional distributions for one or more coordinate blocks, optionally combined with exact Gibbs updates for other blocks. |
| [AIMech:RandomWalkMetropolisHastings](../../data/curated/RandomWalkMetropolisHastings.yaml) | A Metropolis–Hastings sampler that proposes a new state by adding an increment drawn from a fixed distribution independent of the current state. |
| [AIMech:UnadjustedLangevinAlgorithm](../../data/curated/UnadjustedLangevinAlgorithm.yaml) | An approximate sampling algorithm that discretizes overdamped Langevin dynamics by an explicit gradient drift and Gaussian noise without a Metropolis acceptance correction. |
| [AIMech:MetropolisAdjustedLangevinAlgorithm](../../data/curated/MetropolisAdjustedLangevinAlgorithm.yaml) | A Metropolis–Hastings sampler that proposes a Gaussian step with drift proportional to the target log-density gradient and corrects the asymmetric proposal with an accept/reject test. |
| [AIMech:SliceSampling](../../data/curated/SliceSampling.yaml) | An auxiliary-variable Monte Carlo method that augments a target density with a uniform height below its graph and updates the state using a transition preserving the uniform distribution on the resulting density slice. |
| [AIMech:SteppingOutSliceSampling](../../data/curated/SteppingOutSliceSampling.yaml) | A univariate slice-sampling algorithm that randomly places a width-w interval around the current point, expands it in width-w steps under a randomly divided budget, and samples by slice-aware interval shrinkage. |
| [AIMech:DoublingSliceSampling](../../data/curated/DoublingSliceSampling.yaml) | A univariate slice-sampling algorithm that expands a randomly placed initial interval by randomly directed doublings and uses shrinkage with a retrospective acceptability test to preserve the target. |

All eight map to AIO Markov Chain by a method-to-process related match. ULA explicitly retains its fixed-step approximation bias. Gibbs exact conditional draws, Metropolis-within-Gibbs transitions and gradient-directed MALA proposals remain distinct.

The slice variants preserve their different interval-search and acceptance rules. Stepping out needs the random expansion-budget split; general doubling also needs the retrospective acceptance test.

An apparent omitted step-size factor in the older ULA introduction was checked against a later primary formula. The record uses the corroborated convention and does not claim a published erratum. The source ledger distinguishes OCR, garbled extraction, readable author versions and pages actually inspected.

The next frontier includes further slice methods, rejection/proposal variants, adapted Langevin methods and earlier broad AI leads. Discovery has not saturated.
