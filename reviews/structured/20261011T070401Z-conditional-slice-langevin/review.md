# Scientific self-review of conditional, slice and Langevin samplers

- Review: 20261011T070401Z-conditional-slice-langevin
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T07:01:55Z
- Finished UTC: 2026-10-11T07:04:01Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain all eight distinct sampler identities and related AIO mappings within their evidence scopes. No actionable record defect was found. The records preserve ULA bias, MALA convergence limits and slice-kernel correctness conditions; all remain DRAFT.

## Scope And Provenance

Eight maintained conditional, slice and Langevin sampling algorithms.

Selection: Exactly the eight added IDs in the conditional-slice-langevin discovery ledger; no sampling.
Coverage: full; 8 reviewed / 8 in the declared population.
Source: working_tree at Git base b797b0f7c64fc69521e66986256e1e055c34e92c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GibbsSampling | data/curated/GibbsSampling.yaml | maintained | Gibbs sampling |
| AIMech:MetropolisWithinGibbs | data/curated/MetropolisWithinGibbs.yaml | maintained | Metropolis-within-Gibbs sampling |
| AIMech:RandomWalkMetropolisHastings | data/curated/RandomWalkMetropolisHastings.yaml | maintained | Random-walk Metropolis–Hastings sampling |
| AIMech:UnadjustedLangevinAlgorithm | data/curated/UnadjustedLangevinAlgorithm.yaml | maintained | Unadjusted Langevin algorithm |
| AIMech:MetropolisAdjustedLangevinAlgorithm | data/curated/MetropolisAdjustedLangevinAlgorithm.yaml | maintained | Metropolis-adjusted Langevin algorithm |
| AIMech:SliceSampling | data/curated/SliceSampling.yaml | maintained | Slice sampling |
| AIMech:SteppingOutSliceSampling | data/curated/SteppingOutSliceSampling.yaml | maintained | Stepping-out slice sampling |
| AIMech:DoublingSliceSampling | data/curated/DoublingSliceSampling.yaml | maintained | Doubling slice sampling |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:GibbsSampling, AIMech:MetropolisWithinGibbs, AIMech:RandomWalkMetropolisHastings, AIMech:UnadjustedLangevinAlgorithm, AIMech:MetropolisAdjustedLangevinAlgorithm, AIMech:SliceSampling, AIMech:SteppingOutSliceSampling, AIMech:DoublingSliceSampling | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate | passed | True | AIMech:GibbsSampling, AIMech:MetropolisWithinGibbs, AIMech:RandomWalkMetropolisHastings, AIMech:UnadjustedLangevinAlgorithm, AIMech:MetropolisAdjustedLangevinAlgorithm, AIMech:SliceSampling, AIMech:SteppingOutSliceSampling, AIMech:DoublingSliceSampling | Checked 442 record(s); 0 failed.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-curated | passed | True | AIMech:GibbsSampling, AIMech:MetropolisWithinGibbs, AIMech:RandomWalkMetropolisHastings, AIMech:UnadjustedLangevinAlgorithm, AIMech:MetropolisAdjustedLangevinAlgorithm, AIMech:SliceSampling, AIMech:SteppingOutSliceSampling, AIMech:DoublingSliceSampling | Checked 167 curated concept record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli seed --check | passed | True | AIMech:GibbsSampling, AIMech:MetropolisWithinGibbs, AIMech:RandomWalkMetropolisHastings, AIMech:UnadjustedLangevinAlgorithm, AIMech:MetropolisAdjustedLangevinAlgorithm, AIMech:SliceSampling, AIMech:SteppingOutSliceSampling, AIMech:DoublingSliceSampling | AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-history --base HEAD | passed | True | AIMech:GibbsSampling, AIMech:MetropolisWithinGibbs, AIMech:RandomWalkMetropolisHastings, AIMech:UnadjustedLangevinAlgorithm, AIMech:MetropolisAdjustedLangevinAlgorithm, AIMech:SliceSampling, AIMech:SteppingOutSliceSampling, AIMech:DoublingSliceSampling | Checked 33 history record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python scripts/record_review.py check | passed | True | AIMech:GibbsSampling, AIMech:MetropolisWithinGibbs, AIMech:RandomWalkMetropolisHastings, AIMech:UnadjustedLangevinAlgorithm, AIMech:MetropolisAdjustedLangevinAlgorithm, AIMech:SliceSampling, AIMech:SteppingOutSliceSampling, AIMech:DoublingSliceSampling | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 33,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class<br> |
| just check | passed | True | AIMech:GibbsSampling, AIMech:MetropolisWithinGibbs, AIMech:RandomWalkMetropolisHastings, AIMech:UnadjustedLangevinAlgorithm, AIMech:MetropolisAdjustedLangevinAlgorithm, AIMech:SliceSampling, AIMech:SteppingOutSliceSampling, AIMech:DoublingSliceSampling | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 61.45s (0:01:01)<br>Checked 442 record(s); 0 failed.<br>Checked 167 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 33 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 33,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:GibbsSampling, AIMech:MetropolisWithinGibbs, AIMech:RandomWalkMetropolisHastings, AIMech:UnadjustedLangevinAlgorithm, AIMech:MetropolisAdjustedLangevinAlgorithm, AIMech:SliceSampling, AIMech:SteppingOutSliceSampling, AIMech:DoublingSliceSampling | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Sampler identity, transition mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:GibbsSampling.

This record denotes exact conditional resampling, including fixed coordinate cycles and fixed random-scan mixtures. It is a sampling procedure, not a Gibbs distribution, Markov random field, annealing schedule or conditional maximization method. Metropolis-within-Gibbs replaces some exact conditional draws by invariant transitions and is represented separately. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases. Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs and slice sampling plus unrelated environment substring hits, not existing concept records. Existing HMM/MRF models and general Metropolis–Hastings were inspected to distinguish model, general transition and specialized algorithm scope.

The full conditional distributions must be compatible with a proper joint target and be sampled correctly. An approximate conditional draw is not automatically an exact Gibbs step. Target invariance alone does not establish irreducibility, aperiodicity, convergence from every start or rapid mixing. Coordinate dependence and disconnected support can obstruct exploration. The finite positive-state convergence theorem in Geman and Geman has explicit site-visit and positivity assumptions; it is not a theorem for every continuous, constrained or parallel Gibbs implementation. Simultaneously updating dependent coordinates using stale neighbors is outside the stated sequential mechanism; valid parallel or adaptive scan schemes need separate arguments. Fixed-temperature posterior sampling and a cooling schedule for optimization are different procedures. No universal convergence rate or image-restoration performance is asserted.

### Sampler identity, transition mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:MetropolisWithinGibbs.

The distinction is between an exact draw from a full conditional and a Markov transition that preserves it. The latter can be used within a cycle or fixed mixture of block updates. This record does not define every hybrid MCMC composition as Metropolis-within-Gibbs and does not require a nested chain to be run to equilibrium at each update. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases. Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs and slice sampling plus unrelated environment substring hits, not existing concept records. Existing HMM/MRF models and general Metropolis–Hastings were inspected to distinguish model, general transition and specialized algorithm scope.

The proposal-density ratio is required unless the block proposal is symmetric at the fixed values of the other coordinates. A rejected proposal leaves the current block unchanged. Repeating until acceptance changes the transition unless its effect is separately accounted for. A valid conditional kernel need not explore its support well. Joint convergence and mixing require additional conditions on the target, proposals and update schedule. Fixed mixtures and cycles preserve the target, but Tierney explicitly warns that convergence properties of an individual component do not transfer indiscriminately to a cycle. History-dependent tuning, stale parallel updates and approximate target evaluations are outside this fixed-kernel definition. No optimal number of inner steps is claimed.

### Sampler identity, transition mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:RandomWalkMetropolisHastings.

The random walk describes the proposal Y=x+Z, not an assertion that accepted chain increments are independent or target-free. The increment density may be asymmetric; the common symmetric random-walk Metropolis case is included. This differs from a fixed independence proposal g(Y), which does not center on x, and from gradient-directed Langevin proposals. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases. Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs and slice sampling plus unrelated environment substring hits, not existing concept records. Existing HMM/MRF models and general Metropolis–Hastings were inspected to distinguish model, general transition and specialized algorithm scope.

The simplification to the target-density ratio requires a symmetric increment law, not merely an additive proposal. Proposal and target support determine irreducibility. An invariant kernel is not a guarantee of rapid convergence or movement between separated modes. Accepted-state increments and retained draws are generally dependent. Rejected states remain in the chain. This definition uses a fixed increment distribution; adaptive scales and state-dependent covariance require their own proposal ratios and validity analysis. No universal acceptance-rate target, optimal scale, dimension-scaling law or benchmark advantage is asserted.

### Sampler identity, transition mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:UnadjustedLangevinAlgorithm.

This is the full-gradient Euler discretization for a differentiable continuous target. It is not deterministic gradient descent, stochastic-gradient Langevin dynamics, the exact continuous-time diffusion or Metropolis-adjusted Langevin sampling. A fixed-step chain generally has a different invariant law from its intended target. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases. Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs and slice sampling plus unrelated environment substring hits, not existing concept records. Existing HMM/MRF models and general Metropolis–Hastings were inspected to distinguish model, general transition and specialized algorithm scope.

At a fixed positive step size, a stationary distribution, when it exists, generally differs from pi. Running longer does not by itself remove that discretization bias. The paper’s convergence results have regularity, drift and step-size assumptions. Merely taking gamma to zero does not establish convergence for every target or schedule. Discrete Euler dynamics can be unstable even when the continuous diffusion is well behaved. Gradients and noise scaling both depend on the step-size convention. Roberts and Tweedie’s introductory ULA display on printed p. 345 / PDF p. 6 appears to omit h in the drift. This record uses the unambiguous Durmus–Moulines Equation (2), consistent with the h-scaled drift in the older paper’s later analysis; it does not claim a published erratum was found. No minibatch gradient approximation, preconditioning, projection, taming or empirical accuracy bound is included in this record.

### Sampler identity, transition mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:MetropolisAdjustedLangevinAlgorithm.

This record covers the fixed-step, identity-diffusion formulation of Roberts and Tweedie. It differs from ULA by its Metropolis correction, from random-walk Metropolis by its gradient-directed mean, and from multi-step Hamiltonian trajectories. Preconditioned and manifold variants are not silently included in the displayed formula. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases. Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs and slice sampling plus unrelated environment substring hits, not existing concept records. Existing HMM/MRF models and general Metropolis–Hastings were inspected to distinguish model, general transition and specialized algorithm scope.

The full target gradient and both proposal densities must be correctly evaluated. Unknown common target normalization cancels, but the reverse proposal factor does not. Target invariance and correction of proposal discretization do not certify rapid mixing, independent draws or accuracy of a finite run. The source gives tail-dependent failures of geometric ergodicity; adding a Metropolis step is not a universal guarantee of exponential convergence. Large steps, problematic geometry and numerical gradient or density errors can make practical sampling ineffective. This record asserts no universal step size or acceptance target. Truncated drift, stochastic gradients, variable metrics and constrained-state extensions need separate definitions and validation.

### Sampler identity, transition mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:SliceSampling.

This is the single-height construction and its valid within-slice transitions, not a claim that every implementation draws independently and uniformly from an entire slice. Univariate stepping-out and doubling algorithms are distinct concrete variants. Multiple-auxiliary-variable, reflective and overrelaxed extensions require their own mechanism descriptions. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases. Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs and slice sampling plus unrelated environment substring hits, not existing concept records. Existing HMM/MRF models and general Metropolis–Hastings were inspected to distinguish model, general transition and specialized algorithm scope.

The target must be proper, and the density and slice updates must be implemented on their valid support. A random move that merely stays inside the slice need not preserve its uniform distribution. Local interval search need not find the entire slice, especially when it has disconnected components. Its acceptance and shrinkage rules determine validity and exploration. Target invariance does not alone establish ergodicity or efficient movement between modes. The retained states need not be independent. Neal’s 2000 report is the inspected version. A later 2003 journal publication was located, but no equivalence of all version details is asserted. No universal advantage over Gibbs or Metropolis, automatic elimination of every tuning parameter, or numerical benchmark result is claimed.

### Sampler identity, transition mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:SteppingOutSliceSampling.

This record specifies Neal’s stepping-out procedure paired with shrinkage, Figures 3 and 5. The interval-search component alone is not a complete sampler. It differs from doubling in expansion increments and in not requiring doubling’s retrospective acceptability test. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases. Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs and slice sampling plus unrelated environment substring hits, not existing concept records. Existing HMM/MRF models and general Metropolis–Hastings were inspected to distinguish model, general transition and specialized algorithm scope.

The finite expansion cap limits the interval length to at most mw. It is not a certificate that all of the slice has been found. The width and expansion budget affect computational work and exploration; this method does not remove all tuning choices. Shrinking the rejected side relative to the current state is essential. Arbitrary interval placement or budget allocation is not the proven kernel. Unimodal shortcuts and tuning width from past draws in Section 4.4 require the source’s additional conditions, including unlimited expansion for that history-based width argument; they are not generalized here. Multimodality, constrained supports, numerical density evaluation and finite precision require care. No universal mixing guarantee is asserted.

### Sampler identity, transition mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:DoublingSliceSampling.

This record specifies Neal’s Figures 4–6, including the extra acceptance test for general slices. It differs from stepping out by geometric interval expansion and the need to reject some in-slice candidates. Its binary interval construction is unrelated to NUTS trajectory-tree doubling. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases. Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs and slice sampling plus unrelated environment substring hits, not existing concept records. Existing HMM/MRF models and general Metropolis–Hastings were inspected to distinguish model, general transition and specialized algorithm scope.

For a general multimodal density, being inside the slice is insufficient for acceptance. Omitting Figure 6 can invalidate the update. Stopping expansion on one side merely because that side is already outside the slice is not the random doubling procedure used in the proof. The test may be omitted under the source’s single-interval slice/unimodality conditions, not as a blanket optimization. The width and maximum doubling count remain parameters; the interval length cap is 2^p w, and finding an interval is not proof of rapid mixing across disconnected slice components. The doubling interval must remain available for the retrospective test even as the proposal interval shrinks. Numerical boundary handling and round-off remain implementation concerns.

### Exact conditional draws, conditional invariant transitions and additive proposals

scope: supported. Targets: AIMech:GibbsSampling, AIMech:MetropolisWithinGibbs, AIMech:RandomWalkMetropolisHastings.

The three mechanisms are distinct: exact conditional resampling, a conditional Metropolis step and an additive proposal within Metropolis–Hastings.

The source supports fixed cycles and fixed mixtures without asserting unconditional ergodicity. Finite positive-state Gibbs results are not generalized to arbitrary continuous or stale parallel updates. Conditional and increment acceptance ratios are explicit substitutions, retain reverse-proposal factors and retain rejected states. No nested conditional chain needs to reach equilibrium for an invariant Metropolis-within-Gibbs step.

### Euler proposal convention, approximation bias and Metropolis correction

scope: supported. Targets: AIMech:UnadjustedLangevinAlgorithm, AIMech:MetropolisAdjustedLangevinAlgorithm.

ULA is explicitly approximate at fixed step size. MALA corrects the asymmetric gradient proposal for target invariance while retaining convergence limitations.

Durmus–Moulines Equation (2) gives the full gradient and Gaussian scaling; setting h=2 gamma yields the MALA proposal convention. The older introductory ULA display’s apparent missing h is documented, not silently copied or claimed to have a published erratum. The ULA AIO mapping does not assert target stationarity. No numerical tail theorem is inferred from garbled text extraction, and no finite-run accuracy guarantee is made.

### Auxiliary slice construction and concrete interval kernels

scope: supported. Targets: AIMech:SliceSampling, AIMech:SteppingOutSliceSampling, AIMech:DoublingSliceSampling.

The general slice mechanism and its two specified interval algorithms retain their different invariance requirements.

The slice augmentation gives the required x marginal; merely remaining inside the slice is not enough. Stepping out retains random initial alignment and the random left/right budget. Doubling expands a randomly selected side even when already outside the slice and retains Figure 6’s retrospective rejection test. The original doubled interval is distinct from the shrinking proposal interval. Unimodal shortcuts are conditional and do not justify omitting the test for arbitrary multimodal targets.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:GibbsSampling, AIMech:MetropolisWithinGibbs, AIMech:RandomWalkMetropolisHastings, AIMech:UnadjustedLangevinAlgorithm, AIMech:MetropolisAdjustedLangevinAlgorithm, AIMech:SliceSampling, AIMech:SteppingOutSliceSampling, AIMech:DoublingSliceSampling. Retain exact Gibbs resampling, conditional Metropolis transitions, additive random-walk proposals, unadjusted Euler Langevin, Metropolis-corrected Langevin, general single-height slice sampling and its stepping-out/doubling variants. Shared target invariance or components do not establish identity. The variants have distinct proposal, bias or acceptability mechanisms. Method-to-process related mappings do not assert a network/model subclass.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T070134Z-conditional-slice-langevin.json | supports | No normalized identity match across all 442 AIO labels/scoped synonyms and 159 preceding native IDs/names/aliases. Ignored-inclusive full-checkout searches found two prior Gibbs/slice discovery-ledger lines in each checkout and forty additional main-environment substring matches, primarily MALA within unrelated words. All matched lines were inspected. These are leads or environment text, not existing records. HMM, MRF and general Metropolis–Hastings YAMLs were read to separate models, a general transition rule and these distinct samplers or specializations. |
| mapping | sources/aio/aio.json; Exact MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction CLASS definitions, synonyms and incident edges | supports | All eight have related_match to the exact MarkovChain CLASS. Its definition, MC/MP/Markov Process synonyms, Network parent and ProbabilisticHiddenLayer part edge were inspected, along with exact BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction nodes/edges. A sampling algorithm is related to the stochastic process it constructs, not a subclass of the exported network/model. The ULA rationale explicitly avoids claiming exact target stationarity. Graphical factorization or a generic mathematical function is not equivalent to these transition procedures. |
| existing-models | data/curated/HiddenMarkovModel.yaml; Definition and mechanism, alongside data/curated/MarkovRandomField.yaml | supports | The existing HMM and MRF records describe probabilistic models with hidden-state/emission or undirected-factor structures, rather than these posterior-sampling transitions, acceptance rules or tuning procedures. |
| gibbssampling-0 | https://conservancy.umn.edu/server/api/core/bitstreams/f87bc468-91ac-45bc-a1cf-5d4b0f8fbcd6/content; Section 2.2, Conditioning and the Gibbs Sampler, and Section 2.4, Combining Strategies; printed pp. 2 and 8 / PDF pp. 4 and 10 | supports | A Markov chain Monte Carlo algorithm that repeatedly draws a coordinate or block from its full conditional distribution given the current values of the remaining coordinates. Version: University of Minnesota Technical Report No. 560, August 8, 1991; 28 PDF pages; not the 1994 published version. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Attested visual pages: 4, 6, 10. |
| gibbssampling-1 | https://www.dam.brown.edu/people/geman/Homepage/Image%20processing,%20image%20analysis,%20Markov%20random%20fields,%20and%20MCMC/stochastic%20relaxation.pdf; Sections XI–XII, Gibbs Sampler and Theorems A–B, printed pp. 730–731 / PDF pp. 10–11 | supports | Geman and Geman update one image site by drawing from its Gibbs conditional using current neighboring states. Their fixed-temperature sampling construction is distinct from the later cooling procedure for minimum-energy configurations. The finite-state convergence discussion assumes strictly positive configuration probabilities and repeated site visits. Version: IEEE Transactions on Pattern Analysis and Machine Intelligence PAMI-6(6), 1984, pp. 721–741; 21-page author-hosted published scan. Attested PDF text pages: 7, 8, 9, 10, 11, 12. Attested visual pages: 1, 10, 11. |
| metropoliswithingibbs-0 | https://conservancy.umn.edu/server/api/core/bitstreams/f87bc468-91ac-45bc-a1cf-5d4b0f8fbcd6/content; Sections 2.2–2.4: conditional-invariant kernels, Metropolis ratio, and the two-component Gibbs/Metropolis example; printed pp. 2–4 and 8 / PDF pp. 4–6 and 10 | supports | A componentwise Monte Carlo scheme that uses Metropolis–Hastings transitions targeting full conditional distributions for one or more coordinate blocks, optionally combined with exact Gibbs updates for other blocks. Version: University of Minnesota Technical Report No. 560, August 8, 1991; 28 PDF pages; not the 1994 published version. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Attested visual pages: 4, 6, 10. |
| randomwalkmetropolishastings-0 | https://conservancy.umn.edu/server/api/core/bitstreams/f87bc468-91ac-45bc-a1cf-5d4b0f8fbcd6/content; Section 2.3, Metropolis Kernels and Random Walk Chains; printed pp. 3–4 / PDF pp. 5–6 | supports | A Metropolis–Hastings sampler that proposes a new state by adding an increment drawn from a fixed distribution independent of the current state. Version: University of Minnesota Technical Report No. 560, August 8, 1991; 28 PDF pages; not the 1994 published version. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Attested visual pages: 4, 6, 10. |
| unadjustedlangevinalgorithm-0 | https://arxiv.org/pdf/1507.05021v3; Introduction, Equations (1)–(2) and constant/decreasing step-size discussion, PDF/printed pp. 1–2; Section 2, assumptions and kernel, pp. 3–4 | supports | An approximate sampling algorithm that discretizes overdamped Langevin dynamics by an explicit gradient drift and Gaussian noise without a Metropolis acceptance correction. Version: arXiv:1507.05021v3, submitted 2016-12-19; 37-page author preprint with December 20, 2016 footer; not a downloaded publisher version. Attested PDF text pages: 1, 2, 3, 4. Attested visual pages: 2. |
| unadjustedlangevinalgorithm-1 | https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/Langevin/RobertsTweedieBernoulli1996.pdf; Section 3.1, printed pp. 351–354 / PDF pp. 12–15 | supports | Roberts and Tweedie distinguish ULA’s generally biased stationary law from the intended continuous-diffusion target and show that discretization can qualitatively change recurrence and convergence behavior. These are conditional results, not a blanket claim that every ULA run is unstable. Version: Bernoulli 2(4), 1996, pp. 341–363; 25-page hosted PDF including a JSTOR cover. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20. Attested visual pages: 6, 7. |
| metropolisadjustedlangevinalgorithm-0 | https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/Langevin/RobertsTweedieBernoulli1996.pdf; Section 1.4.2, proposal and Equations (9)–(11), printed pp. 345–346 / PDF pp. 6–7; Section 4 introductory discussion, printed p. 355 / PDF p. 16 | supports | A Metropolis–Hastings sampler that proposes a Gaussian step with drift proportional to the target log-density gradient and corrects the asymmetric proposal with an accept/reject test. Version: Bernoulli 2(4), 1996, pp. 341–363; 25-page hosted PDF including a JSTOR cover. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20. Attested visual pages: 6, 7. |
| metropolisadjustedlangevinalgorithm-1 | https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/Langevin/RobertsTweedieBernoulli1996.pdf; Sections 4.1–4.3, printed pp. 355–359 / PDF pp. 16–20 | supports | The paper separates conditions for geometric convergence from counterexamples and non-geometric cases. Its rejection and tail analysis shows that correcting the invariant target does not universally supply fast convergence. Version: Bernoulli 2(4), 1996, pp. 341–363; 25-page hosted PDF including a JSTOR cover. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20. Attested visual pages: 6, 7. |
| slicesampling-0 | https://arxiv.org/pdf/physics/0009028v1; Section 3, The idea of slice sampling, Equations (1)–(2), PDF/printed p. 6; Section 4.3 correctness argument, pp. 12–16 | supports | An auxiliary-variable Monte Carlo method that augments a target density with a uniform height below its graph and updates the state using a transition preserving the uniform distribution on the resulting density slice. Version: arXiv:physics/0009028v1, submitted 2000-09-07; title page dated 29 August 2000, Technical Report No. 2005; 40 pages; not the 2003 journal version. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17. Attested visual pages: 6, 11, 13. |
| steppingoutslicesampling-0 | https://arxiv.org/pdf/physics/0009028v1; Sections 4.1–4.3, Figures 3 and 5, budget construction and correctness proof, PDF/printed pp. 8–16 | supports | A univariate slice-sampling algorithm that randomly places a width-w interval around the current point, expands it in width-w steps under a randomly divided budget, and samples by slice-aware interval shrinkage. Version: arXiv:physics/0009028v1, submitted 2000-09-07; title page dated 29 August 2000, Technical Report No. 2005; 40 pages; not the 2003 journal version. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17. Attested visual pages: 6, 11, 13. |
| doublingslicesampling-0 | https://arxiv.org/pdf/physics/0009028v1; Sections 4.1–4.3, Figures 4–6 and detailed-balance argument, PDF/printed pp. 10–16 | supports | A univariate slice-sampling algorithm that expands a randomly placed initial interval by randomly directed doublings and uses shrinkage with a retrospective acceptability test to preserve the target. Version: arXiv:physics/0009028v1, submitted 2000-09-07; title page dated 29 August 2000, Technical Report No. 2005; 40 pages; not the 2003 journal version. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17. Attested visual pages: 6, 11, 13. |
| tierney-ratio-visual | https://conservancy.umn.edu/server/api/core/bitstreams/f87bc468-91ac-45bc-a1cf-5d4b0f8fbcd6/content; Printed p. 3 / PDF p. 5, general Metropolis algorithm | supports | During formal review, additionally viewed the rendered general Metropolis ratio, rejection self-transition and detailed-balance expression. This supplements the discovery ledger’s earlier visual pp. 4, 6 and 10. |

## Limits And Additional Notes

- Adversarial author self-review only; all eight records remain DRAFT.
- Tierney 1991, Neal 2000 and Durmus–Moulines 2016 are explicitly identified author versions, not mislabeled downloaded journal publications.
- Geman’s scan required OCR and visual verification; only stated pages were read. Garbled text from a different Neal PDF was not treated as inspected evidence.
- The apparent omitted step-size factor in the older ULA introduction is documented and the algorithm uses a corroborating primary equation; no published erratum is claimed.
- Invariance, convergence, mixing, independent draws and finite-run accuracy are distinct. Fixed-step ULA is not asserted to preserve its intended target.
- No sampler was run, no benchmark result reproduced and no universal tuning or performance claim asserted.
- Repeated passages from one paper are not independent evidence. The review attests only declared text and visual inspection scopes.
- All required checks passed. This review does not retire unrelated findings or establish literature saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T070401Z-conditional-slice-langevin
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of conditional, slice and Langevin samplers
started_at: '2026-10-11T07:01:55Z'
finished_at: '2026-10-11T07:04:01Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all eight actual
    YAMLs against inspected methods, equations, pseudocode, convergence qualifications
    and AIO mapping definitions. No independent reviewer or approval is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain all eight distinct sampler identities and related AIO mappings within
  their evidence scopes. No actionable record defect was found. The records preserve
  ULA bias, MALA convergence limits and slice-kernel correctness conditions; all remain
  DRAFT.
source:
  git_revision: b797b0f7c64fc69521e66986256e1e055c34e92c
  state: working_tree
  inputs:
  - path: data/curated/DoublingSliceSampling.yaml
    sha256: 9de4028afbf3c1217076bf4bc3ae0b228b86545356393dae8d0cc157593b8ac4
    role: target
  - path: data/curated/GibbsSampling.yaml
    sha256: 8175215986c0507e3664a3aedf8074fc067d85b4a89002091d1bcb9b637a522a
    role: target
  - path: data/curated/HiddenMarkovModel.yaml
    sha256: 062a31bd525cb90e8077d4889c177f55cb7b29dea4e71c33be95bae9e72a5240
    role: context
  - path: data/curated/MarkovRandomField.yaml
    sha256: 03b1f2a66b2183a5bf5943bee7ec0619b9e07947d6c9187263e279ee475f9149
    role: context
  - path: data/curated/MetropolisAdjustedLangevinAlgorithm.yaml
    sha256: 6e815be8054929061e44ef8ddd5a63c5b1361d8c518fb3ec5fd7f9bba884b6f7
    role: target
  - path: data/curated/MetropolisHastings.yaml
    sha256: 01cb22a25242e8564e2a7bb839ecb46da1bc49eb09b3c85200f9a596e05b99b4
    role: context
  - path: data/curated/MetropolisWithinGibbs.yaml
    sha256: 0e9cfedc93c7e46cc6316809d5a9ec9488b33891a9c9862f914a0adf8f7cb140
    role: target
  - path: data/curated/RandomWalkMetropolisHastings.yaml
    sha256: aeff822517db546b4e3dee3421a54d5887ed178f3b9e6e3df46283eceb39677d
    role: target
  - path: data/curated/SliceSampling.yaml
    sha256: a87319788a5d2966dd1484b6672a968642fb5514cc6f81184908576304bf6aaa
    role: target
  - path: data/curated/SteppingOutSliceSampling.yaml
    sha256: 8d2d0155c2e1d462b093935f19f4fe11fefb61e19e3ed93336e30b7257dda4c8
    role: target
  - path: data/curated/UnadjustedLangevinAlgorithm.yaml
    sha256: 4c09ef556111d807d01b68678691453752de613610bb23239c9480b90b8535eb
    role: target
  - path: research/discovery/20261011T070134Z-conditional-slice-langevin.json
    sha256: b9916561d9a6ab5e33f07a2a9786074c1756121f2a7520928860a1c7e30913b6
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 0600ec8ca628d2dac611f2a068074ebcd4b83b6b5f31832a32dbc4f4bfa35b06
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:GibbsSampling
  path: data/curated/GibbsSampling.yaml
  label: Gibbs sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GibbsSampling.yaml
    role: maintained_record
- target_id: AIMech:MetropolisWithinGibbs
  path: data/curated/MetropolisWithinGibbs.yaml
  label: Metropolis-within-Gibbs sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MetropolisWithinGibbs.yaml
    role: maintained_record
- target_id: AIMech:RandomWalkMetropolisHastings
  path: data/curated/RandomWalkMetropolisHastings.yaml
  label: Random-walk Metropolis–Hastings sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RandomWalkMetropolisHastings.yaml
    role: maintained_record
- target_id: AIMech:UnadjustedLangevinAlgorithm
  path: data/curated/UnadjustedLangevinAlgorithm.yaml
  label: Unadjusted Langevin algorithm
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/UnadjustedLangevinAlgorithm.yaml
    role: maintained_record
- target_id: AIMech:MetropolisAdjustedLangevinAlgorithm
  path: data/curated/MetropolisAdjustedLangevinAlgorithm.yaml
  label: Metropolis-adjusted Langevin algorithm
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MetropolisAdjustedLangevinAlgorithm.yaml
    role: maintained_record
- target_id: AIMech:SliceSampling
  path: data/curated/SliceSampling.yaml
  label: Slice sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SliceSampling.yaml
    role: maintained_record
- target_id: AIMech:SteppingOutSliceSampling
  path: data/curated/SteppingOutSliceSampling.yaml
  label: Stepping-out slice sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SteppingOutSliceSampling.yaml
    role: maintained_record
- target_id: AIMech:DoublingSliceSampling
  path: data/curated/DoublingSliceSampling.yaml
  label: Doubling slice sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DoublingSliceSampling.yaml
    role: maintained_record
scope:
  description: Eight maintained conditional, slice and Langevin sampling algorithms.
  selection: Exactly the eight added IDs in the conditional-slice-langevin discovery
    ledger; no sampling.
  coverage: full
  population_size: 8
  reviewed_target_ids:
  - AIMech:GibbsSampling
  - AIMech:MetropolisWithinGibbs
  - AIMech:RandomWalkMetropolisHastings
  - AIMech:UnadjustedLangevinAlgorithm
  - AIMech:MetropolisAdjustedLangevinAlgorithm
  - AIMech:SliceSampling
  - AIMech:SteppingOutSliceSampling
  - AIMech:DoublingSliceSampling
  exclusions:
  - target: Unread source sections, later versions and additional sampler variants
    reason: Only declared source pages were inspected; other algorithms, theory and
      version comparisons remain in the discovery frontier.
  - target: Sampler execution, numerical experiments and benchmark replication
    reason: No algorithm implementation, model fit or experiment was executed.
checks:
- check_id: required-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:GibbsSampling
  - AIMech:MetropolisWithinGibbs
  - AIMech:RandomWalkMetropolisHastings
  - AIMech:UnadjustedLangevinAlgorithm
  - AIMech:MetropolisAdjustedLangevinAlgorithm
  - AIMech:SliceSampling
  - AIMech:SteppingOutSliceSampling
  - AIMech:DoublingSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
- check_id: required-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate
  status: passed
  required: true
  target_ids:
  - AIMech:GibbsSampling
  - AIMech:MetropolisWithinGibbs
  - AIMech:RandomWalkMetropolisHastings
  - AIMech:UnadjustedLangevinAlgorithm
  - AIMech:MetropolisAdjustedLangevinAlgorithm
  - AIMech:SliceSampling
  - AIMech:SteppingOutSliceSampling
  - AIMech:DoublingSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 442 record(s); 0 failed.

    '
- check_id: required-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:GibbsSampling
  - AIMech:MetropolisWithinGibbs
  - AIMech:RandomWalkMetropolisHastings
  - AIMech:UnadjustedLangevinAlgorithm
  - AIMech:MetropolisAdjustedLangevinAlgorithm
  - AIMech:SliceSampling
  - AIMech:SteppingOutSliceSampling
  - AIMech:DoublingSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 167 curated concept record(s); 0 error(s).

    '
- check_id: required-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:GibbsSampling
  - AIMech:MetropolisWithinGibbs
  - AIMech:RandomWalkMetropolisHastings
  - AIMech:UnadjustedLangevinAlgorithm
  - AIMech:MetropolisAdjustedLangevinAlgorithm
  - AIMech:SliceSampling
  - AIMech:SteppingOutSliceSampling
  - AIMech:DoublingSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: 'AIO: 442 records; 0 missing, 0 changed, 0 unexpected.

    '
- check_id: required-4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-history --base HEAD
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-history --base HEAD
  status: passed
  required: true
  target_ids:
  - AIMech:GibbsSampling
  - AIMech:MetropolisWithinGibbs
  - AIMech:RandomWalkMetropolisHastings
  - AIMech:UnadjustedLangevinAlgorithm
  - AIMech:MetropolisAdjustedLangevinAlgorithm
  - AIMech:SliceSampling
  - AIMech:SteppingOutSliceSampling
  - AIMech:DoublingSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 33 history record(s); 0 error(s).

    '
- check_id: required-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:GibbsSampling
  - AIMech:MetropolisWithinGibbs
  - AIMech:RandomWalkMetropolisHastings
  - AIMech:UnadjustedLangevinAlgorithm
  - AIMech:MetropolisAdjustedLangevinAlgorithm
  - AIMech:SliceSampling
  - AIMech:SteppingOutSliceSampling
  - AIMech:DoublingSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 33,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\ntopClass is deprecated - use top_class\n"
- check_id: required-6
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:GibbsSampling
  - AIMech:MetropolisWithinGibbs
  - AIMech:RandomWalkMetropolisHastings
  - AIMech:UnadjustedLangevinAlgorithm
  - AIMech:MetropolisAdjustedLangevinAlgorithm
  - AIMech:SliceSampling
  - AIMech:SteppingOutSliceSampling
  - AIMech:DoublingSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 61.45s (0:01:01)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 167 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 33 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 33,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-7
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:GibbsSampling
  - AIMech:MetropolisWithinGibbs
  - AIMech:RandomWalkMetropolisHastings
  - AIMech:UnadjustedLangevinAlgorithm
  - AIMech:MetropolisAdjustedLangevinAlgorithm
  - AIMech:SliceSampling
  - AIMech:SteppingOutSliceSampling
  - AIMech:DoublingSliceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T070134Z-conditional-slice-langevin.json
  accessed_at: '2026-10-11T07:01:55Z'
  support: supports
  summary: No normalized identity match across all 442 AIO labels/scoped synonyms
    and 159 preceding native IDs/names/aliases. Ignored-inclusive full-checkout searches
    found two prior Gibbs/slice discovery-ledger lines in each checkout and forty
    additional main-environment substring matches, primarily MALA within unrelated
    words. All matched lines were inspected. These are leads or environment text,
    not existing records. HMM, MRF and general Metropolis–Hastings YAMLs were read
    to separate models, a general transition rule and these distinct samplers or specializations.
  search_scope: All 442 pinned AIO labels/scoped synonyms and 159 preceding native
    IDs/names/aliases; both updated checkouts with ignored and hidden files included.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Exact MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction
    CLASS definitions, synonyms and incident edges
  accessed_at: '2026-10-11T07:01:55Z'
  support: supports
  summary: All eight have related_match to the exact MarkovChain CLASS. Its definition,
    MC/MP/Markov Process synonyms, Network parent and ProbabilisticHiddenLayer part
    edge were inspected, along with exact BayesianNetwork, ProbabilisticGraphicalModel
    and MathematicalFunction nodes/edges. A sampling algorithm is related to the stochastic
    process it constructs, not a subclass of the exported network/model. The ULA rationale
    explicitly avoids claiming exact target stationarity. Graphical factorization
    or a generic mathematical function is not equivalent to these transition procedures.
- evidence_id: existing-models
  kind: record_content
  reference: data/curated/HiddenMarkovModel.yaml
  locator: Definition and mechanism, alongside data/curated/MarkovRandomField.yaml
  accessed_at: '2026-10-11T07:01:55Z'
  support: supports
  summary: The existing HMM and MRF records describe probabilistic models with hidden-state/emission
    or undirected-factor structures, rather than these posterior-sampling transitions,
    acceptance rules or tuning procedures.
- evidence_id: gibbssampling-0
  kind: primary_source
  reference: https://conservancy.umn.edu/server/api/core/bitstreams/f87bc468-91ac-45bc-a1cf-5d4b0f8fbcd6/content
  locator: Section 2.2, Conditioning and the Gibbs Sampler, and Section 2.4, Combining
    Strategies; printed pp. 2 and 8 / PDF pp. 4 and 10
  accessed_at: '2026-10-11T06:52:00Z'
  snapshot_sha256: cfde8fc2fa3c390da09badda81394a0a334d70f13403031ac9d4c0b5a1e11fde
  support: supports
  summary: 'A Markov chain Monte Carlo algorithm that repeatedly draws a coordinate
    or block from its full conditional distribution given the current values of the
    remaining coordinates. Version: University of Minnesota Technical Report No. 560,
    August 8, 1991; 28 PDF pages; not the 1994 published version. Attested PDF text
    pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Attested visual pages: 4, 6, 10.'
- evidence_id: gibbssampling-1
  kind: primary_source
  reference: https://www.dam.brown.edu/people/geman/Homepage/Image%20processing,%20image%20analysis,%20Markov%20random%20fields,%20and%20MCMC/stochastic%20relaxation.pdf
  locator: Sections XI–XII, Gibbs Sampler and Theorems A–B, printed pp. 730–731 /
    PDF pp. 10–11
  accessed_at: '2026-10-11T06:52:00Z'
  snapshot_sha256: 6adab117ea49d7569a1f4563c33d8c9b393335d084a09e6c22609ed231a1bc31
  support: supports
  summary: 'Geman and Geman update one image site by drawing from its Gibbs conditional
    using current neighboring states. Their fixed-temperature sampling construction
    is distinct from the later cooling procedure for minimum-energy configurations.
    The finite-state convergence discussion assumes strictly positive configuration
    probabilities and repeated site visits. Version: IEEE Transactions on Pattern
    Analysis and Machine Intelligence PAMI-6(6), 1984, pp. 721–741; 21-page author-hosted
    published scan. Attested PDF text pages: 7, 8, 9, 10, 11, 12. Attested visual
    pages: 1, 10, 11.'
- evidence_id: metropoliswithingibbs-0
  kind: primary_source
  reference: https://conservancy.umn.edu/server/api/core/bitstreams/f87bc468-91ac-45bc-a1cf-5d4b0f8fbcd6/content
  locator: 'Sections 2.2–2.4: conditional-invariant kernels, Metropolis ratio, and
    the two-component Gibbs/Metropolis example; printed pp. 2–4 and 8 / PDF pp. 4–6
    and 10'
  accessed_at: '2026-10-11T06:52:00Z'
  snapshot_sha256: cfde8fc2fa3c390da09badda81394a0a334d70f13403031ac9d4c0b5a1e11fde
  support: supports
  summary: 'A componentwise Monte Carlo scheme that uses Metropolis–Hastings transitions
    targeting full conditional distributions for one or more coordinate blocks, optionally
    combined with exact Gibbs updates for other blocks. Version: University of Minnesota
    Technical Report No. 560, August 8, 1991; 28 PDF pages; not the 1994 published
    version. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Attested visual
    pages: 4, 6, 10.'
- evidence_id: randomwalkmetropolishastings-0
  kind: primary_source
  reference: https://conservancy.umn.edu/server/api/core/bitstreams/f87bc468-91ac-45bc-a1cf-5d4b0f8fbcd6/content
  locator: Section 2.3, Metropolis Kernels and Random Walk Chains; printed pp. 3–4
    / PDF pp. 5–6
  accessed_at: '2026-10-11T06:52:00Z'
  snapshot_sha256: cfde8fc2fa3c390da09badda81394a0a334d70f13403031ac9d4c0b5a1e11fde
  support: supports
  summary: 'A Metropolis–Hastings sampler that proposes a new state by adding an increment
    drawn from a fixed distribution independent of the current state. Version: University
    of Minnesota Technical Report No. 560, August 8, 1991; 28 PDF pages; not the 1994
    published version. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Attested
    visual pages: 4, 6, 10.'
- evidence_id: unadjustedlangevinalgorithm-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1507.05021v3
  locator: Introduction, Equations (1)–(2) and constant/decreasing step-size discussion,
    PDF/printed pp. 1–2; Section 2, assumptions and kernel, pp. 3–4
  accessed_at: '2026-10-11T06:57:57Z'
  snapshot_sha256: 5794a1e4a70145a3708e149304e9f4744cfb651f94bddc9a51301799ee56eb63
  support: supports
  summary: 'An approximate sampling algorithm that discretizes overdamped Langevin
    dynamics by an explicit gradient drift and Gaussian noise without a Metropolis
    acceptance correction. Version: arXiv:1507.05021v3, submitted 2016-12-19; 37-page
    author preprint with December 20, 2016 footer; not a downloaded publisher version.
    Attested PDF text pages: 1, 2, 3, 4. Attested visual pages: 2.'
- evidence_id: unadjustedlangevinalgorithm-1
  kind: primary_source
  reference: https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/Langevin/RobertsTweedieBernoulli1996.pdf
  locator: Section 3.1, printed pp. 351–354 / PDF pp. 12–15
  accessed_at: '2026-10-11T06:52:00Z'
  snapshot_sha256: 410e26b08534801112aaa020edcc2a9e483dd76328d950a1a4dee65dc424a9c9
  support: supports
  summary: 'Roberts and Tweedie distinguish ULA’s generally biased stationary law
    from the intended continuous-diffusion target and show that discretization can
    qualitatively change recurrence and convergence behavior. These are conditional
    results, not a blanket claim that every ULA run is unstable. Version: Bernoulli
    2(4), 1996, pp. 341–363; 25-page hosted PDF including a JSTOR cover. Attested
    PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20.
    Attested visual pages: 6, 7.'
- evidence_id: metropolisadjustedlangevinalgorithm-0
  kind: primary_source
  reference: https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/Langevin/RobertsTweedieBernoulli1996.pdf
  locator: Section 1.4.2, proposal and Equations (9)–(11), printed pp. 345–346 / PDF
    pp. 6–7; Section 4 introductory discussion, printed p. 355 / PDF p. 16
  accessed_at: '2026-10-11T06:52:00Z'
  snapshot_sha256: 410e26b08534801112aaa020edcc2a9e483dd76328d950a1a4dee65dc424a9c9
  support: supports
  summary: 'A Metropolis–Hastings sampler that proposes a Gaussian step with drift
    proportional to the target log-density gradient and corrects the asymmetric proposal
    with an accept/reject test. Version: Bernoulli 2(4), 1996, pp. 341–363; 25-page
    hosted PDF including a JSTOR cover. Attested PDF text pages: 1, 2, 3, 4, 5, 6,
    7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20. Attested visual pages: 6, 7.'
- evidence_id: metropolisadjustedlangevinalgorithm-1
  kind: primary_source
  reference: https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/Langevin/RobertsTweedieBernoulli1996.pdf
  locator: Sections 4.1–4.3, printed pp. 355–359 / PDF pp. 16–20
  accessed_at: '2026-10-11T06:52:00Z'
  snapshot_sha256: 410e26b08534801112aaa020edcc2a9e483dd76328d950a1a4dee65dc424a9c9
  support: supports
  summary: 'The paper separates conditions for geometric convergence from counterexamples
    and non-geometric cases. Its rejection and tail analysis shows that correcting
    the invariant target does not universally supply fast convergence. Version: Bernoulli
    2(4), 1996, pp. 341–363; 25-page hosted PDF including a JSTOR cover. Attested
    PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20.
    Attested visual pages: 6, 7.'
- evidence_id: slicesampling-0
  kind: primary_source
  reference: https://arxiv.org/pdf/physics/0009028v1
  locator: Section 3, The idea of slice sampling, Equations (1)–(2), PDF/printed p.
    6; Section 4.3 correctness argument, pp. 12–16
  accessed_at: '2026-10-11T06:53:34Z'
  snapshot_sha256: c6cf46fb834b637b95357ec12f3247540fecd64248051001d7236f469832902d
  support: supports
  summary: 'An auxiliary-variable Monte Carlo method that augments a target density
    with a uniform height below its graph and updates the state using a transition
    preserving the uniform distribution on the resulting density slice. Version: arXiv:physics/0009028v1,
    submitted 2000-09-07; title page dated 29 August 2000, Technical Report No. 2005;
    40 pages; not the 2003 journal version. Attested PDF text pages: 1, 2, 3, 4, 5,
    6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17. Attested visual pages: 6, 11, 13.'
- evidence_id: steppingoutslicesampling-0
  kind: primary_source
  reference: https://arxiv.org/pdf/physics/0009028v1
  locator: Sections 4.1–4.3, Figures 3 and 5, budget construction and correctness
    proof, PDF/printed pp. 8–16
  accessed_at: '2026-10-11T06:53:34Z'
  snapshot_sha256: c6cf46fb834b637b95357ec12f3247540fecd64248051001d7236f469832902d
  support: supports
  summary: 'A univariate slice-sampling algorithm that randomly places a width-w interval
    around the current point, expands it in width-w steps under a randomly divided
    budget, and samples by slice-aware interval shrinkage. Version: arXiv:physics/0009028v1,
    submitted 2000-09-07; title page dated 29 August 2000, Technical Report No. 2005;
    40 pages; not the 2003 journal version. Attested PDF text pages: 1, 2, 3, 4, 5,
    6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17. Attested visual pages: 6, 11, 13.'
- evidence_id: doublingslicesampling-0
  kind: primary_source
  reference: https://arxiv.org/pdf/physics/0009028v1
  locator: Sections 4.1–4.3, Figures 4–6 and detailed-balance argument, PDF/printed
    pp. 10–16
  accessed_at: '2026-10-11T06:53:34Z'
  snapshot_sha256: c6cf46fb834b637b95357ec12f3247540fecd64248051001d7236f469832902d
  support: supports
  summary: 'A univariate slice-sampling algorithm that expands a randomly placed initial
    interval by randomly directed doublings and uses shrinkage with a retrospective
    acceptability test to preserve the target. Version: arXiv:physics/0009028v1, submitted
    2000-09-07; title page dated 29 August 2000, Technical Report No. 2005; 40 pages;
    not the 2003 journal version. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8,
    9, 10, 11, 12, 13, 14, 15, 16, 17. Attested visual pages: 6, 11, 13.'
- evidence_id: tierney-ratio-visual
  kind: primary_source
  reference: https://conservancy.umn.edu/server/api/core/bitstreams/f87bc468-91ac-45bc-a1cf-5d4b0f8fbcd6/content
  locator: Printed p. 3 / PDF p. 5, general Metropolis algorithm
  accessed_at: '2026-10-11T07:01:55Z'
  snapshot_sha256: cfde8fc2fa3c390da09badda81394a0a334d70f13403031ac9d4c0b5a1e11fde
  support: supports
  summary: During formal review, additionally viewed the rendered general Metropolis
    ratio, rejection self-transition and detailed-balance expression. This supplements
    the discovery ledger’s earlier visual pp. 4, 6 and 10.
assessments:
- assessment_id: gibbssampling
  area: evidence
  topic: Sampler identity, transition mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:GibbsSampling
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - gibbssampling-0
  - gibbssampling-1
  summary: This record denotes exact conditional resampling, including fixed coordinate
    cycles and fixed random-scan mixtures. It is a sampling procedure, not a Gibbs
    distribution, Markov random field, annealing schedule or conditional maximization
    method. Metropolis-within-Gibbs replaces some exact conditional draws by invariant
    transitions and is represented separately. No normalized identity match was found
    across all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases.
    Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs
    and slice sampling plus unrelated environment substring hits, not existing concept
    records. Existing HMM/MRF models and general Metropolis–Hastings were inspected
    to distinguish model, general transition and specialized algorithm scope.
  details: The full conditional distributions must be compatible with a proper joint
    target and be sampled correctly. An approximate conditional draw is not automatically
    an exact Gibbs step. Target invariance alone does not establish irreducibility,
    aperiodicity, convergence from every start or rapid mixing. Coordinate dependence
    and disconnected support can obstruct exploration. The finite positive-state convergence
    theorem in Geman and Geman has explicit site-visit and positivity assumptions;
    it is not a theorem for every continuous, constrained or parallel Gibbs implementation.
    Simultaneously updating dependent coordinates using stale neighbors is outside
    the stated sequential mechanism; valid parallel or adaptive scan schemes need
    separate arguments. Fixed-temperature posterior sampling and a cooling schedule
    for optimization are different procedures. No universal convergence rate or image-restoration
    performance is asserted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: All eight records denote sampling algorithms at explicitly stated
      levels of specialization. None denotes a probability model, trained model instance
      or finite-run empirical result.
    evidence_ids:
    - gibbssampling-0
    - gibbssampling-1
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The procedure constructs Markov transitions for sampling a specified
      target, with the invariance and convergence qualifications stated in this record.
      AIO MarkovChain denotes the stochastic process/model and is exported beneath
      Network. This is a method-to-process related match, not equivalence, subclass
      membership or a claim that the algorithm is a trained network.
    evidence_ids:
    - mapping
    - identity
- assessment_id: metropoliswithingibbs
  area: evidence
  topic: Sampler identity, transition mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:MetropolisWithinGibbs
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - metropoliswithingibbs-0
  summary: The distinction is between an exact draw from a full conditional and a
    Markov transition that preserves it. The latter can be used within a cycle or
    fixed mixture of block updates. This record does not define every hybrid MCMC
    composition as Metropolis-within-Gibbs and does not require a nested chain to
    be run to equilibrium at each update. No normalized identity match was found across
    all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases.
    Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs
    and slice sampling plus unrelated environment substring hits, not existing concept
    records. Existing HMM/MRF models and general Metropolis–Hastings were inspected
    to distinguish model, general transition and specialized algorithm scope.
  details: The proposal-density ratio is required unless the block proposal is symmetric
    at the fixed values of the other coordinates. A rejected proposal leaves the current
    block unchanged. Repeating until acceptance changes the transition unless its
    effect is separately accounted for. A valid conditional kernel need not explore
    its support well. Joint convergence and mixing require additional conditions on
    the target, proposals and update schedule. Fixed mixtures and cycles preserve
    the target, but Tierney explicitly warns that convergence properties of an individual
    component do not transfer indiscriminately to a cycle. History-dependent tuning,
    stale parallel updates and approximate target evaluations are outside this fixed-kernel
    definition. No optimal number of inner steps is claimed.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: All eight records denote sampling algorithms at explicitly stated
      levels of specialization. None denotes a probability model, trained model instance
      or finite-run empirical result.
    evidence_ids:
    - metropoliswithingibbs-0
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The procedure constructs Markov transitions for sampling a specified
      target, with the invariance and convergence qualifications stated in this record.
      AIO MarkovChain denotes the stochastic process/model and is exported beneath
      Network. This is a method-to-process related match, not equivalence, subclass
      membership or a claim that the algorithm is a trained network.
    evidence_ids:
    - mapping
    - identity
- assessment_id: randomwalkmetropolishastings
  area: evidence
  topic: Sampler identity, transition mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:RandomWalkMetropolisHastings
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - randomwalkmetropolishastings-0
  summary: The random walk describes the proposal Y=x+Z, not an assertion that accepted
    chain increments are independent or target-free. The increment density may be
    asymmetric; the common symmetric random-walk Metropolis case is included. This
    differs from a fixed independence proposal g(Y), which does not center on x, and
    from gradient-directed Langevin proposals. No normalized identity match was found
    across all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases.
    Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs
    and slice sampling plus unrelated environment substring hits, not existing concept
    records. Existing HMM/MRF models and general Metropolis–Hastings were inspected
    to distinguish model, general transition and specialized algorithm scope.
  details: The simplification to the target-density ratio requires a symmetric increment
    law, not merely an additive proposal. Proposal and target support determine irreducibility.
    An invariant kernel is not a guarantee of rapid convergence or movement between
    separated modes. Accepted-state increments and retained draws are generally dependent.
    Rejected states remain in the chain. This definition uses a fixed increment distribution;
    adaptive scales and state-dependent covariance require their own proposal ratios
    and validity analysis. No universal acceptance-rate target, optimal scale, dimension-scaling
    law or benchmark advantage is asserted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: All eight records denote sampling algorithms at explicitly stated
      levels of specialization. None denotes a probability model, trained model instance
      or finite-run empirical result.
    evidence_ids:
    - randomwalkmetropolishastings-0
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The procedure constructs Markov transitions for sampling a specified
      target, with the invariance and convergence qualifications stated in this record.
      AIO MarkovChain denotes the stochastic process/model and is exported beneath
      Network. This is a method-to-process related match, not equivalence, subclass
      membership or a claim that the algorithm is a trained network.
    evidence_ids:
    - mapping
    - identity
- assessment_id: unadjustedlangevinalgorithm
  area: evidence
  topic: Sampler identity, transition mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:UnadjustedLangevinAlgorithm
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - unadjustedlangevinalgorithm-0
  - unadjustedlangevinalgorithm-1
  summary: This is the full-gradient Euler discretization for a differentiable continuous
    target. It is not deterministic gradient descent, stochastic-gradient Langevin
    dynamics, the exact continuous-time diffusion or Metropolis-adjusted Langevin
    sampling. A fixed-step chain generally has a different invariant law from its
    intended target. No normalized identity match was found across all 442 pinned
    AIO labels/scoped synonyms and 159 prior native IDs/names/aliases. Ignored-inclusive
    full-checkout searches found prior discovery leads for Gibbs and slice sampling
    plus unrelated environment substring hits, not existing concept records. Existing
    HMM/MRF models and general Metropolis–Hastings were inspected to distinguish model,
    general transition and specialized algorithm scope.
  details: At a fixed positive step size, a stationary distribution, when it exists,
    generally differs from pi. Running longer does not by itself remove that discretization
    bias. The paper’s convergence results have regularity, drift and step-size assumptions.
    Merely taking gamma to zero does not establish convergence for every target or
    schedule. Discrete Euler dynamics can be unstable even when the continuous diffusion
    is well behaved. Gradients and noise scaling both depend on the step-size convention.
    Roberts and Tweedie’s introductory ULA display on printed p. 345 / PDF p. 6 appears
    to omit h in the drift. This record uses the unambiguous Durmus–Moulines Equation
    (2), consistent with the h-scaled drift in the older paper’s later analysis; it
    does not claim a published erratum was found. No minibatch gradient approximation,
    preconditioning, projection, taming or empirical accuracy bound is included in
    this record.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: All eight records denote sampling algorithms at explicitly stated
      levels of specialization. None denotes a probability model, trained model instance
      or finite-run empirical result.
    evidence_ids:
    - unadjustedlangevinalgorithm-0
    - unadjustedlangevinalgorithm-1
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: ULA constructs a discrete Markov process intended to approximate sampling
      from a target. At fixed positive step size its invariant law generally differs
      from that target. The AIO CLASS denotes the stochastic process/model, so this
      is a method-to-process related match, not equivalence, subclass membership or
      an assertion of exact target stationarity.
    evidence_ids:
    - mapping
    - identity
- assessment_id: metropolisadjustedlangevinalgorithm
  area: evidence
  topic: Sampler identity, transition mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:MetropolisAdjustedLangevinAlgorithm
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - metropolisadjustedlangevinalgorithm-0
  - metropolisadjustedlangevinalgorithm-1
  summary: This record covers the fixed-step, identity-diffusion formulation of Roberts
    and Tweedie. It differs from ULA by its Metropolis correction, from random-walk
    Metropolis by its gradient-directed mean, and from multi-step Hamiltonian trajectories.
    Preconditioned and manifold variants are not silently included in the displayed
    formula. No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 159 prior native IDs/names/aliases. Ignored-inclusive full-checkout
    searches found prior discovery leads for Gibbs and slice sampling plus unrelated
    environment substring hits, not existing concept records. Existing HMM/MRF models
    and general Metropolis–Hastings were inspected to distinguish model, general transition
    and specialized algorithm scope.
  details: The full target gradient and both proposal densities must be correctly
    evaluated. Unknown common target normalization cancels, but the reverse proposal
    factor does not. Target invariance and correction of proposal discretization do
    not certify rapid mixing, independent draws or accuracy of a finite run. The source
    gives tail-dependent failures of geometric ergodicity; adding a Metropolis step
    is not a universal guarantee of exponential convergence. Large steps, problematic
    geometry and numerical gradient or density errors can make practical sampling
    ineffective. This record asserts no universal step size or acceptance target.
    Truncated drift, stochastic gradients, variable metrics and constrained-state
    extensions need separate definitions and validation.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: All eight records denote sampling algorithms at explicitly stated
      levels of specialization. None denotes a probability model, trained model instance
      or finite-run empirical result.
    evidence_ids:
    - metropolisadjustedlangevinalgorithm-0
    - metropolisadjustedlangevinalgorithm-1
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The procedure constructs Markov transitions for sampling a specified
      target, with the invariance and convergence qualifications stated in this record.
      AIO MarkovChain denotes the stochastic process/model and is exported beneath
      Network. This is a method-to-process related match, not equivalence, subclass
      membership or a claim that the algorithm is a trained network.
    evidence_ids:
    - mapping
    - identity
- assessment_id: slicesampling
  area: evidence
  topic: Sampler identity, transition mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:SliceSampling
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - slicesampling-0
  summary: This is the single-height construction and its valid within-slice transitions,
    not a claim that every implementation draws independently and uniformly from an
    entire slice. Univariate stepping-out and doubling algorithms are distinct concrete
    variants. Multiple-auxiliary-variable, reflective and overrelaxed extensions require
    their own mechanism descriptions. No normalized identity match was found across
    all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases.
    Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs
    and slice sampling plus unrelated environment substring hits, not existing concept
    records. Existing HMM/MRF models and general Metropolis–Hastings were inspected
    to distinguish model, general transition and specialized algorithm scope.
  details: The target must be proper, and the density and slice updates must be implemented
    on their valid support. A random move that merely stays inside the slice need
    not preserve its uniform distribution. Local interval search need not find the
    entire slice, especially when it has disconnected components. Its acceptance and
    shrinkage rules determine validity and exploration. Target invariance does not
    alone establish ergodicity or efficient movement between modes. The retained states
    need not be independent. Neal’s 2000 report is the inspected version. A later
    2003 journal publication was located, but no equivalence of all version details
    is asserted. No universal advantage over Gibbs or Metropolis, automatic elimination
    of every tuning parameter, or numerical benchmark result is claimed.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: All eight records denote sampling algorithms at explicitly stated
      levels of specialization. None denotes a probability model, trained model instance
      or finite-run empirical result.
    evidence_ids:
    - slicesampling-0
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The procedure constructs Markov transitions for sampling a specified
      target, with the invariance and convergence qualifications stated in this record.
      AIO MarkovChain denotes the stochastic process/model and is exported beneath
      Network. This is a method-to-process related match, not equivalence, subclass
      membership or a claim that the algorithm is a trained network.
    evidence_ids:
    - mapping
    - identity
- assessment_id: steppingoutslicesampling
  area: evidence
  topic: Sampler identity, transition mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:SteppingOutSliceSampling
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - steppingoutslicesampling-0
  summary: This record specifies Neal’s stepping-out procedure paired with shrinkage,
    Figures 3 and 5. The interval-search component alone is not a complete sampler.
    It differs from doubling in expansion increments and in not requiring doubling’s
    retrospective acceptability test. No normalized identity match was found across
    all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases.
    Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs
    and slice sampling plus unrelated environment substring hits, not existing concept
    records. Existing HMM/MRF models and general Metropolis–Hastings were inspected
    to distinguish model, general transition and specialized algorithm scope.
  details: The finite expansion cap limits the interval length to at most mw. It is
    not a certificate that all of the slice has been found. The width and expansion
    budget affect computational work and exploration; this method does not remove
    all tuning choices. Shrinking the rejected side relative to the current state
    is essential. Arbitrary interval placement or budget allocation is not the proven
    kernel. Unimodal shortcuts and tuning width from past draws in Section 4.4 require
    the source’s additional conditions, including unlimited expansion for that history-based
    width argument; they are not generalized here. Multimodality, constrained supports,
    numerical density evaluation and finite precision require care. No universal mixing
    guarantee is asserted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: All eight records denote sampling algorithms at explicitly stated
      levels of specialization. None denotes a probability model, trained model instance
      or finite-run empirical result.
    evidence_ids:
    - steppingoutslicesampling-0
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The procedure constructs Markov transitions for sampling a specified
      target, with the invariance and convergence qualifications stated in this record.
      AIO MarkovChain denotes the stochastic process/model and is exported beneath
      Network. This is a method-to-process related match, not equivalence, subclass
      membership or a claim that the algorithm is a trained network.
    evidence_ids:
    - mapping
    - identity
- assessment_id: doublingslicesampling
  area: evidence
  topic: Sampler identity, transition mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:DoublingSliceSampling
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - doublingslicesampling-0
  summary: This record specifies Neal’s Figures 4–6, including the extra acceptance
    test for general slices. It differs from stepping out by geometric interval expansion
    and the need to reject some in-slice candidates. Its binary interval construction
    is unrelated to NUTS trajectory-tree doubling. No normalized identity match was
    found across all 442 pinned AIO labels/scoped synonyms and 159 prior native IDs/names/aliases.
    Ignored-inclusive full-checkout searches found prior discovery leads for Gibbs
    and slice sampling plus unrelated environment substring hits, not existing concept
    records. Existing HMM/MRF models and general Metropolis–Hastings were inspected
    to distinguish model, general transition and specialized algorithm scope.
  details: For a general multimodal density, being inside the slice is insufficient
    for acceptance. Omitting Figure 6 can invalidate the update. Stopping expansion
    on one side merely because that side is already outside the slice is not the random
    doubling procedure used in the proof. The test may be omitted under the source’s
    single-interval slice/unimodality conditions, not as a blanket optimization. The
    width and maximum doubling count remain parameters; the interval length cap is
    2^p w, and finding an interval is not proof of rapid mixing across disconnected
    slice components. The doubling interval must remain available for the retrospective
    test even as the proposal interval shrinks. Numerical boundary handling and round-off
    remain implementation concerns.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: All eight records denote sampling algorithms at explicitly stated
      levels of specialization. None denotes a probability model, trained model instance
      or finite-run empirical result.
    evidence_ids:
    - doublingslicesampling-0
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The procedure constructs Markov transitions for sampling a specified
      target, with the invariance and convergence qualifications stated in this record.
      AIO MarkovChain denotes the stochastic process/model and is exported beneath
      Network. This is a method-to-process related match, not equivalence, subclass
      membership or a claim that the algorithm is a trained network.
    evidence_ids:
    - mapping
    - identity
- assessment_id: conditional-and-random-walk
  area: scope
  topic: Exact conditional draws, conditional invariant transitions and additive proposals
  outcome: supported
  target_ids:
  - AIMech:GibbsSampling
  - AIMech:MetropolisWithinGibbs
  - AIMech:RandomWalkMetropolisHastings
  evidence_ids:
  - gibbssampling-0
  - gibbssampling-1
  - metropoliswithingibbs-0
  - randomwalkmetropolishastings-0
  - tierney-ratio-visual
  summary: 'The three mechanisms are distinct: exact conditional resampling, a conditional
    Metropolis step and an additive proposal within Metropolis–Hastings.'
  details: The source supports fixed cycles and fixed mixtures without asserting unconditional
    ergodicity. Finite positive-state Gibbs results are not generalized to arbitrary
    continuous or stale parallel updates. Conditional and increment acceptance ratios
    are explicit substitutions, retain reverse-proposal factors and retain rejected
    states. No nested conditional chain needs to reach equilibrium for an invariant
    Metropolis-within-Gibbs step.
- assessment_id: langevin-bias-correction
  area: scope
  topic: Euler proposal convention, approximation bias and Metropolis correction
  outcome: supported
  target_ids:
  - AIMech:UnadjustedLangevinAlgorithm
  - AIMech:MetropolisAdjustedLangevinAlgorithm
  evidence_ids:
  - unadjustedlangevinalgorithm-0
  - unadjustedlangevinalgorithm-1
  - metropolisadjustedlangevinalgorithm-0
  - metropolisadjustedlangevinalgorithm-1
  summary: ULA is explicitly approximate at fixed step size. MALA corrects the asymmetric
    gradient proposal for target invariance while retaining convergence limitations.
  details: Durmus–Moulines Equation (2) gives the full gradient and Gaussian scaling;
    setting h=2 gamma yields the MALA proposal convention. The older introductory
    ULA display’s apparent missing h is documented, not silently copied or claimed
    to have a published erratum. The ULA AIO mapping does not assert target stationarity.
    No numerical tail theorem is inferred from garbled text extraction, and no finite-run
    accuracy guarantee is made.
- assessment_id: slice-validity
  area: scope
  topic: Auxiliary slice construction and concrete interval kernels
  outcome: supported
  target_ids:
  - AIMech:SliceSampling
  - AIMech:SteppingOutSliceSampling
  - AIMech:DoublingSliceSampling
  evidence_ids:
  - slicesampling-0
  - steppingoutslicesampling-0
  - doublingslicesampling-0
  summary: The general slice mechanism and its two specified interval algorithms retain
    their different invariance requirements.
  details: The slice augmentation gives the required x marginal; merely remaining
    inside the slice is not enough. Stepping out retains random initial alignment
    and the random left/right budget. Doubling expands a randomly selected side even
    when already outside the slice and retains Figure 6’s retrospective rejection
    test. The original doubled interval is distinct from the shrinking proposal interval.
    Unimodal shortcuts are conditional and do not justify omitting the test for arbitrary
    multimodal targets.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:GibbsSampling
  - AIMech:MetropolisWithinGibbs
  - AIMech:RandomWalkMetropolisHastings
  - AIMech:UnadjustedLangevinAlgorithm
  - AIMech:MetropolisAdjustedLangevinAlgorithm
  - AIMech:SliceSampling
  - AIMech:SteppingOutSliceSampling
  - AIMech:DoublingSliceSampling
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - gibbssampling-0
  - gibbssampling-1
  - metropoliswithingibbs-0
  - randomwalkmetropolishastings-0
  - unadjustedlangevinalgorithm-0
  - unadjustedlangevinalgorithm-1
  - metropolisadjustedlangevinalgorithm-0
  - metropolisadjustedlangevinalgorithm-1
  - slicesampling-0
  - steppingoutslicesampling-0
  - doublingslicesampling-0
  - tierney-ratio-visual
  rationale: Retain exact Gibbs resampling, conditional Metropolis transitions, additive
    random-walk proposals, unadjusted Euler Langevin, Metropolis-corrected Langevin,
    general single-height slice sampling and its stepping-out/doubling variants. Shared
    target invariance or components do not establish identity. The variants have distinct
    proposal, bias or acceptability mechanisms. Method-to-process related mappings
    do not assert a network/model subclass.
limitations:
- Adversarial author self-review only; all eight records remain DRAFT.
- Tierney 1991, Neal 2000 and Durmus–Moulines 2016 are explicitly identified author
  versions, not mislabeled downloaded journal publications.
- Geman’s scan required OCR and visual verification; only stated pages were read.
  Garbled text from a different Neal PDF was not treated as inspected evidence.
- The apparent omitted step-size factor in the older ULA introduction is documented
  and the algorithm uses a corroborating primary equation; no published erratum is
  claimed.
- Invariance, convergence, mixing, independent draws and finite-run accuracy are distinct.
  Fixed-step ULA is not asserted to preserve its intended target.
- No sampler was run, no benchmark result reproduced and no universal tuning or performance
  claim asserted.
- Repeated passages from one paper are not independent evidence. The review attests
  only declared text and visual inspection scopes.
- All required checks passed. This review does not retire unrelated findings or establish
  literature saturation.
tags:
- native-concepts
- mcmc
- gibbs
- slice-sampling
- langevin
- primary-methods
- self-review
- discovery-ongoing
```
