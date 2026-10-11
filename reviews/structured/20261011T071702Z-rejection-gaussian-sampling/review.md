# Scientific self-review of rejection and Gaussian-reference samplers

- Review: 20261011T071702Z-rejection-gaussian-sampling
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T07:14:45Z
- Finished UTC: 2026-10-11T07:17:02Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain all eight distinct sampler identities, six related AIO mappings and two bounded no-match assessments. No actionable record defect was found. Independent generation, adaptive envelopes, angular slice search and Gaussian-reference proposal variants remain distinct; all records stay DRAFT.

## Scope And Provenance

Eight maintained rejection and Gaussian-reference sampling algorithms.

Selection: Exactly the eight added IDs in the rejection-gaussian-sampling discovery ledger; no sampling.
Coverage: full; 8 reviewed / 8 in the declared population.
Source: working_tree at Git base 7583609697d5c3b5e8820534fd130dd4e24debae.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:RejectionSampling | data/curated/RejectionSampling.yaml | maintained | Rejection sampling |
| AIMech:AdaptiveRejectionSampling | data/curated/AdaptiveRejectionSampling.yaml | maintained | Adaptive rejection sampling |
| AIMech:EllipticalSliceSampling | data/curated/EllipticalSliceSampling.yaml | maintained | Elliptical slice sampling |
| AIMech:RejectionDrivenIndependenceMetropolis | data/curated/RejectionDrivenIndependenceMetropolis.yaml | maintained | Rejection-driven independence Metropolis sampling |
| AIMech:CrankNicolsonMetropolis | data/curated/CrankNicolsonMetropolis.yaml | maintained | Crank–Nicolson Metropolis sampling |
| AIMech:PreconditionedCrankNicolson | data/curated/PreconditionedCrankNicolson.yaml | maintained | Preconditioned Crank–Nicolson sampling |
| AIMech:CrankNicolsonLangevin | data/curated/CrankNicolsonLangevin.yaml | maintained | Crank–Nicolson Langevin sampling |
| AIMech:PreconditionedCrankNicolsonLangevin | data/curated/PreconditionedCrankNicolsonLangevin.yaml | maintained | Preconditioned Crank–Nicolson Langevin sampling |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:RejectionSampling, AIMech:AdaptiveRejectionSampling, AIMech:EllipticalSliceSampling, AIMech:RejectionDrivenIndependenceMetropolis, AIMech:CrankNicolsonMetropolis, AIMech:PreconditionedCrankNicolson, AIMech:CrankNicolsonLangevin, AIMech:PreconditionedCrankNicolsonLangevin | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate | passed | True | AIMech:RejectionSampling, AIMech:AdaptiveRejectionSampling, AIMech:EllipticalSliceSampling, AIMech:RejectionDrivenIndependenceMetropolis, AIMech:CrankNicolsonMetropolis, AIMech:PreconditionedCrankNicolson, AIMech:CrankNicolsonLangevin, AIMech:PreconditionedCrankNicolsonLangevin | Checked 442 record(s); 0 failed.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-curated | passed | True | AIMech:RejectionSampling, AIMech:AdaptiveRejectionSampling, AIMech:EllipticalSliceSampling, AIMech:RejectionDrivenIndependenceMetropolis, AIMech:CrankNicolsonMetropolis, AIMech:PreconditionedCrankNicolson, AIMech:CrankNicolsonLangevin, AIMech:PreconditionedCrankNicolsonLangevin | Checked 175 curated concept record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli seed --check | passed | True | AIMech:RejectionSampling, AIMech:AdaptiveRejectionSampling, AIMech:EllipticalSliceSampling, AIMech:RejectionDrivenIndependenceMetropolis, AIMech:CrankNicolsonMetropolis, AIMech:PreconditionedCrankNicolson, AIMech:CrankNicolsonLangevin, AIMech:PreconditionedCrankNicolsonLangevin | AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-history --base HEAD | passed | True | AIMech:RejectionSampling, AIMech:AdaptiveRejectionSampling, AIMech:EllipticalSliceSampling, AIMech:RejectionDrivenIndependenceMetropolis, AIMech:CrankNicolsonMetropolis, AIMech:PreconditionedCrankNicolson, AIMech:CrankNicolsonLangevin, AIMech:PreconditionedCrankNicolsonLangevin | Checked 34 history record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python scripts/record_review.py check | passed | True | AIMech:RejectionSampling, AIMech:AdaptiveRejectionSampling, AIMech:EllipticalSliceSampling, AIMech:RejectionDrivenIndependenceMetropolis, AIMech:CrankNicolsonMetropolis, AIMech:PreconditionedCrankNicolson, AIMech:CrankNicolsonLangevin, AIMech:PreconditionedCrankNicolsonLangevin | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 34,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class<br> |
| just check | passed | True | AIMech:RejectionSampling, AIMech:AdaptiveRejectionSampling, AIMech:EllipticalSliceSampling, AIMech:RejectionDrivenIndependenceMetropolis, AIMech:CrankNicolsonMetropolis, AIMech:PreconditionedCrankNicolson, AIMech:CrankNicolsonLangevin, AIMech:PreconditionedCrankNicolsonLangevin | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 71.52s (0:01:11)<br>Checked 442 record(s); 0 failed.<br>Checked 175 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 34 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 34,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:RejectionSampling, AIMech:AdaptiveRejectionSampling, AIMech:EllipticalSliceSampling, AIMech:RejectionDrivenIndependenceMetropolis, AIMech:CrankNicolsonMetropolis, AIMech:PreconditionedCrankNicolson, AIMech:CrankNicolsonLangevin, AIMech:PreconditionedCrankNicolsonLangevin | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Identity, sampling mechanism, evidence scope and AIO assessment

evidence: supported. Targets: AIMech:RejectionSampling.

This is ordinary accept-reject generation with a valid global envelope. A rejected candidate is discarded, not recorded as a repeated chain state. The method differs from Metropolis acceptance, rejection-driven Metropolis proposals, importance weighting and selective filtering of model answers. The inspected primary source presents the scalar density case. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 167 prior native IDs/names/aliases. Full-checkout searches in both worktrees included ignored and hidden files; the 15 lines in each were shared Tierney source-title references or an adaptive-rejection discovery lead, not matching records. Existing Gibbs, Metropolis-within-Gibbs, random-walk and independence Metropolis mechanisms were inspected to resolve specialization boundaries.

A valid dominating envelope and an exact sampler for its normalized distribution are required. Clipping an invalid envelope ratio at one does not preserve the intended independent-sample law. An envelope with excessive mass can make acceptance rare. No universal efficiency, dimensional scaling or bound on the number of trials is claimed. The optional squeezing bound must be valid everywhere it is used; it is an evaluation shortcut, not a replacement target. Numerical approximation, finite precision and inaccurate envelope sampling can change the output distribution. Log concavity is not required by ordinary rejection sampling itself.

### Identity, sampling mechanism, evidence scope and AIO assessment

evidence: supported. Targets: AIMech:AdaptiveRejectionSampling.

This record scopes ARS to the derivative-based tangent construction in Gilks and Wild (1992), for a fixed log-concave scalar target on a connected domain. Derivative-free envelope constructions and adaptive rejection Metropolis sampling are distinct variants requiring their own evidence. Exact conditional draws do not make successive joint Gibbs states independent. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 167 prior native IDs/names/aliases. Full-checkout searches in both worktrees included ignored and hidden files; the 15 lines in each were shared Tierney source-title references or an adaptive-rejection discovery lead, not matching records. Existing Gibbs, Metropolis-within-Gibbs, random-walk and independence Metropolis mechanisms were inspected to resolve specialization boundaries.

Concavity of log g is essential for the tangent and chord bounds. Unimodality alone is insufficient, and non-log-concave targets are not covered by this construction. The displayed baseline assumes usable derivatives and connected scalar support. It does not assert validity for every nonsmooth density or a direct multivariate joint draw. Tail slopes and support endpoints must make the proposal integrable. Concentrated or skewed densities require numerical care. When a Gibbs conditional changes, hull values must be computed for that conditional; reusing stale density bounds is not justified. No universal evaluation savings or benchmark result is asserted. ARMS and its 1997 correction remain separate uninspected-method leads.

### Identity, sampling mechanism, evidence scope and AIO assessment

evidence: supported. Targets: AIMech:EllipticalSliceSampling.

This is the full-circle default algorithm in Murray et al. Figure 2 for a fixed Gaussian prior covariance. It differs from a fixed-angle Gaussian autoregressive Metropolis proposal and from scalar interval stepping-out or doubling. ESS here denotes this sampler, not the effective-sample-size diagnostic. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 167 prior native IDs/names/aliases. Full-checkout searches in both worktrees included ignored and hidden files; the 15 lines in each were shared Tierney source-title references or an adaptive-rejection discovery lead, not matching records. Existing Gibbs, Metropolis-within-Gibbs, random-walk and independence Metropolis mechanisms were inspected to resolve specialization boundaries.

A Gaussian prior draw and likelihood evaluation are required. A nonzero prior mean must be handled by centering the ellipse; an arbitrary non-Gaussian prior is outside this formula. Fixing the initial bracket deterministically to [−pi,pi] is not the proved algorithm; the paper explicitly explains why its random placement matters. The algorithm may reject multiple internal angle trials before returning an update. Its lack of an outer Metropolis rejection is not a claim of one likelihood evaluation or independent retained states. The default full-circle algorithm avoids a user-specified proposal scale, but covariance, model hyperparameters and optional narrower angular variants still involve choices. Strong offsets, covariance structure and likelihood geometry can impede exploration. No universal mixing rate, finite-run accuracy or timing advantage is asserted.

### Identity, sampling mechanism, evidence scope and AIO assessment

evidence: supported. Targets: AIMech:RejectionDrivenIndependenceMetropolis.

This is Tierney’s rejection sampling chain in Section 2.3.4. It specializes independence Metropolis by an inner proposal generator; it is not ordinary rejection sampling unless the envelope dominates everywhere. It is distinct from adaptive rejection Metropolis sampling, because h and c are fixed here. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 167 prior native IDs/names/aliases. Full-checkout searches in both worktrees included ignored and hidden files; the 15 lines in each were shared Tierney source-title references or an adaptive-rejection discovery lead, not matching records. Existing Gibbs, Metropolis-within-Gibbs, random-walk and independence Metropolis mechanisms were inspected to resolve specialization boundaries.

The inner proposal must have positive acceptance mass and cover the target support required for irreducibility. A poor choice of h or c can make either stage inefficient. The inner rejected trials are discarded, while rejection by the outer Metropolis test repeats the chain state; these two rejection events have different roles. A non-dominating envelope without the outer correction generally gives the clipped density rather than pi. Correcting it does not guarantee fast mixing. The inspected 1991 technical report prints the reciprocal of the mixed-case factor and omits the minimum with one in the final case. This record uses the visually verified 1994 published expressions, consistent with the general independence ratio; no separate erratum is asserted. Adapting h or c from chain history is outside the fixed-proposal definition and needs its own validity argument.

### Identity, sampling mechanism, evidence scope and AIO assessment

evidence: supported. Targets: AIMech:CrankNicolsonMetropolis.

This is the CN proposal of Cotter et al. Section 4.2 paired with its Metropolis test, not the generic Crank–Nicolson numerical integration scheme. Unlike pCN, its proposal requires an operator or matrix solve involving C and the step size. It contains no likelihood-gradient drift. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 167 prior native IDs/names/aliases. Full-checkout searches in both worktrees included ignored and hidden files; the 15 lines in each were shared Tierney source-title references or an adaptive-rejection discovery lead, not matching records. Existing Gibbs, Metropolis-within-Gibbs, random-walk and independence Metropolis mechanisms were inspected to resolve specialization boundaries.

The target must be proper relative to the Gaussian reference. The explicit density-ratio implementation here is finite-dimensional with symmetric positive-definite C; function-space extensions require the source’s operator, regularity and absolute-continuity assumptions. Target invariance does not imply independent draws, good exploration or finite-run accuracy. Mesh-robust behavior under stated assumptions is not a universal dimension-free performance guarantee. C and the step size are fixed in the stated kernel. Adaptive covariance or step-size policies need separate validity arguments. The reprint’s later Equation (6.2) reverses signs relative to Equation (6.1) and the explicit Section 4 proposals. This record uses Section 4 and does not claim a published erratum or use the inconsistent expression. An accurate linear solve and Gaussian draw are required. Replacing the noise by an incorrectly scaled standard Gaussian changes the proposal and invalidates the stated cancellation.

### Identity, sampling mechanism, evidence scope and AIO assessment

evidence: supported. Targets: AIMech:PreconditionedCrankNicolson.

This is the pCN proposal and likelihood-ratio test in Cotter et al. Section 4.2. It preserves the Gaussian reference before correction and differs from an additive random walk, the unpreconditioned CN solve and an angular slice search. The displayed nonnegative coefficient form uses the source’s delta≤2 parameterization. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 167 prior native IDs/names/aliases. Full-checkout searches in both worktrees included ignored and hidden files; the 15 lines in each were shared Tierney source-title references or an adaptive-rejection discovery lead, not matching records. Existing Gibbs, Metropolis-within-Gibbs, random-walk and independence Metropolis mechanisms were inspected to resolve specialization boundaries.

The target must be proper relative to the Gaussian reference. The explicit density-ratio implementation here is finite-dimensional with symmetric positive-definite C; function-space extensions require the source’s operator, regularity and absolute-continuity assumptions. Target invariance does not imply independent draws, good exploration or finite-run accuracy. Mesh-robust behavior under stated assumptions is not a universal dimension-free performance guarantee. C and the step size are fixed in the stated kernel. Adaptive covariance or step-size policies need separate validity arguments. The reprint’s later Equation (6.2) reverses signs relative to Equation (6.1) and the explicit Section 4 proposals. This record uses Section 4 and does not claim a published erratum or use the inconsistent expression. Beta=0 would give no movement and is excluded from this stated sampler. Delta&gt;2 in the original linear form gives a negative autoregressive coefficient and is not represented by the positive square-root parameterization here.

### Identity, sampling mechanism, evidence scope and AIO assessment

evidence: supported. Targets: AIMech:CrankNicolsonLangevin.

This is Cotter et al. CNL, with unpreconditioned dynamics and a precision-dependent linear solve. The potential gradient is of Phi relative to the Gaussian reference, not of the entire Lebesgue log density. It differs from CN by its gradient term and from pCNL by its preconditioning. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 167 prior native IDs/names/aliases. Full-checkout searches in both worktrees included ignored and hidden files; the 15 lines in each were shared Tierney source-title references or an adaptive-rejection discovery lead, not matching records. Existing Gibbs, Metropolis-within-Gibbs, random-walk and independence Metropolis mechanisms were inspected to resolve specialization boundaries.

The target must be proper relative to the Gaussian reference. The explicit density-ratio implementation here is finite-dimensional with symmetric positive-definite C; function-space extensions require the source’s operator, regularity and absolute-continuity assumptions. Target invariance does not imply independent draws, good exploration or finite-run accuracy. Mesh-robust behavior under stated assumptions is not a universal dimension-free performance guarantee. C and the step size are fixed in the stated kernel. Adaptive covariance or step-size policies need separate validity arguments. The reprint’s later Equation (6.2) reverses signs relative to Equation (6.1) and the explicit Section 4 proposals. This record uses Section 4 and does not claim a published erratum or use the inconsistent expression. The gradient and forward/reverse Gaussian densities must be evaluated consistently. In infinite dimensions one must use the source’s measure-based acceptance under its assumptions, not a nonexistent Lebesgue density. No identity with every MALA implementation or guaranteed advantage over CN or pCN is asserted.

### Identity, sampling mechanism, evidence scope and AIO assessment

evidence: supported. Targets: AIMech:PreconditionedCrankNicolsonLangevin.

This is Cotter et al. pCNL. The reference covariance multiplies grad Phi, and the linear denominator is the scalar 2+delta, distinguishing it from the CNL matrix solve. Removing the potential gradient recovers the pCN proposal, but a nonzero gradient changes its acceptance rule. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 167 prior native IDs/names/aliases. Full-checkout searches in both worktrees included ignored and hidden files; the 15 lines in each were shared Tierney source-title references or an adaptive-rejection discovery lead, not matching records. Existing Gibbs, Metropolis-within-Gibbs, random-walk and independence Metropolis mechanisms were inspected to resolve specialization boundaries.

The target must be proper relative to the Gaussian reference. The explicit density-ratio implementation here is finite-dimensional with symmetric positive-definite C; function-space extensions require the source’s operator, regularity and absolute-continuity assumptions. Target invariance does not imply independent draws, good exploration or finite-run accuracy. Mesh-robust behavior under stated assumptions is not a universal dimension-free performance guarantee. C and the step size are fixed in the stated kernel. Adaptive covariance or step-size policies need separate validity arguments. The reprint’s later Equation (6.2) reverses signs relative to Equation (6.1) and the explicit Section 4 proposals. This record uses Section 4 and does not claim a published erratum or use the inconsistent expression. The gradient is of the potential relative to the Gaussian reference. Substituting the full log-target gradient without accounting for the already implicit Gaussian drift defines a different proposal. Function-space validity and efficient discretizations need the source’s extra assumptions; the finite-dimensional density ratio is not a definition of an infinite-dimensional Lebesgue density.

### Independent generation, adaptive hulls and rejection-driven Markov states

scope: supported. Targets: AIMech:RejectionSampling, AIMech:AdaptiveRejectionSampling, AIMech:RejectionDrivenIndependenceMetropolis.

Retain ordinary rejection, derivative-based ARS and the fixed-envelope rejection-driven Metropolis chain as distinct procedures.

Ordinary rejection needs a dominating integrable envelope; ARS obtains one from log-concavity and tangents and updates on every full density/derivative evaluation. Neither requires repetition of a previous output after rejecting an inner trial. The Tierney construction instead corrects proposals proportional to min(pi,c h), retaining an outer rejected state. The 1994 mixed-case and final-case formulas agree with the general independence ratio and resolve the two incompatible 1991 expressions.

### Random angular slice bracket versus a fixed Gaussian-reference Metropolis proposal

scope: supported. Targets: AIMech:EllipticalSliceSampling, AIMech:PreconditionedCrankNicolson.

ESS and pCN share Gaussian-reference geometry but use different candidate selection and acceptance procedures.

ESS keeps one auxiliary Gaussian draw and slice threshold while shrinking a randomly positioned full-circle angular bracket around zero. pCN draws a fixed-coefficient autoregressive proposal and accepts it using the potential difference. A deterministic ESS bracket is not substituted; internal angle rejections are acknowledged. Beta=1 is an independence proposal, not a claim that outer retained states are independent.

### Preconditioning, likelihood-gradient drift and Metropolis acceptance

scope: supported. Targets: AIMech:CrankNicolsonMetropolis, AIMech:PreconditionedCrankNicolson, AIMech:CrankNicolsonLangevin, AIMech:PreconditionedCrankNicolsonLangevin.

The four CN-family records retain distinct matrix/scalar proposal operators and the presence or absence of potential-gradient drift.

The explicit Section 4 equations were visually checked. CN uses a solve involving 2C+delta I, while pCN uses 2+delta. Gradient variants add −2 delta C grad Phi and need the full forward/reverse proposal correction. Their finite-dimensional density-ratio expression is explicitly an algebraic specialization, not an infinite-dimensional Lebesgue formula. The later Equation (6.2) has reversed signs relative to (6.1); it is documented and not used. No universal dimension-independent efficiency theorem is asserted.

### Independent generators and bounded absence of an informative AIO mapping

representation: supported. Targets: AIMech:RejectionSampling, AIMech:AdaptiveRejectionSampling.

The explicit no-match assessments are supported by the searched pin and rejected-target definitions.

Independent generation can be embedded in a Markov process, but that mathematical possibility and an outer Gibbs application do not justify this model/network mapping. Graphical dependence tasks, Bayesian DAG models, generic mathematical functions and sampling-bias categories likewise do not define these generators. The no-match conclusion is limited to the inspected snapshot; it is not a statement about all ontologies.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:RejectionSampling, AIMech:AdaptiveRejectionSampling, AIMech:EllipticalSliceSampling, AIMech:RejectionDrivenIndependenceMetropolis, AIMech:CrankNicolsonMetropolis, AIMech:PreconditionedCrankNicolson, AIMech:CrankNicolsonLangevin, AIMech:PreconditionedCrankNicolsonLangevin. Preserve ordinary rejection and its derivative-based ARS specialization, the rejection-driven independence chain, elliptical angular slice updates, and the four explicitly different CN-family proposals. Shared Gaussian priors or acceptance components do not establish equivalence. The two no-match assessments are bounded local mapping judgments; the other six related mappings do not assert a network subclass.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T071428Z-rejection-gaussian-sampling.json | supports | No normalized identity match across all 442 AIO labels/scoped synonyms and 167 preceding native IDs/names/aliases. Both ignored-inclusive full-checkout searches returned 15 lines, all inspected: shared Tierney paper titles in Gibbs/MWG/random-walk records and the previous discovery ledger, plus the ARS/ARMS lead. These are references/leads rather than duplicates. Existing independence Metropolis and the earlier Gibbs/MWG/random-walk YAML mechanisms were inspected; specialization and proposal-generator differences are retained. |
| mapping | sources/aio/aio.json; Exact MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel, MathematicalFunction and SelectionAndSamplingBias CLASS definitions, synonyms and incident edges | supports | Six Markov samplers receive related_match to AIO:MarkovChain, whose exact definition, synonyms, Network parent and hidden-layer edge were inspected. Ordinary and adaptive rejection generation receive explicit aio_no_match with five inspected rejected targets: MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel, MathematicalFunction and SelectionAndSamplingBias. Independent generation is not forced into a process/model class merely because it can be used inside Gibbs. Semantic search covered sampling, Monte Carlo, Markov, Bayesian, probabilistic and mathematical-function descriptions across the pin. No ontology axiom is changed. |
| existing-samplers | data/curated/IndependenceMetropolisHastings.yaml; Definition, identity and mechanism; also GibbsSampling, MetropolisWithinGibbs and RandomWalkMetropolisHastings YAMLs | supports | Existing records distinguish exact conditional resampling, conditional invariant transitions, additive proposals and fixed state-independent proposals. The rejection-driven chain adds a specific clipped proposal generator; ordinary rejection and ARS yield independent draws for fixed targets, while ESS and the CN family specify different Markov updates. |
| rejectionsampling-0 | https://hedibert.org/wp-content/uploads/2013/12/1992GilksWild.pdf; Section 2.1, Rejection Sampling, printed pp. 338–339 / PDF pp. 3–4 | supports | A random-variate generation algorithm that draws proposals from a normalized envelope dominating an unnormalized target and accepts each with the target-to-envelope ratio, yielding independent target draws with fresh independent random trials. Version: Applied Statistics 41(2), 1992, pp. 337–348; 13-page published scan including JSTOR cover. Attested text pages: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13. Attested visual pages: 4, 5, 6. |
| adaptiverejectionsampling-0 | https://hedibert.org/wp-content/uploads/2013/12/1992GilksWild.pdf; Sections 2.2–2.3, Equations (1)–(4), initialization, sampling step and correctness argument, printed pp. 339–342 / PDF pp. 4–7; conclusion on numerical care, p. 347 / PDF p. 12 | supports | The Gilks–Wild univariate rejection sampler that uses tangents to a concave log density as a piecewise-linear upper hull and chords as a lower hull, updating these bounds from evaluated proposals. Version: Applied Statistics 41(2), 1992, pp. 337–348; 13-page published scan including JSTOR cover. Attested text pages: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13. Attested visual pages: 4, 5, 6. |
| ellipticalslicesampling-0 | https://proceedings.mlr.press/v9/murray10a/murray10a.pdf; Sections 2.1–2.3, Figure 2 and correctness proof, printed pp. 542–545 / PDF pp. 2–5 | supports | A Markov-chain update for a target factored into a Gaussian prior and a likelihood, which performs an angular slice search along the ellipse defined by the current state and an independent prior draw. Version: AISTATS 2010, PMLR 9, pp. 541–548; eight-page proceedings PDF. Attested text pages: 1, 2, 3, 4, 5, 6, 7, 8. Attested visual pages: 3. |
| rejectiondrivenindependencemetropolis-0 | https://www.ma.imperial.ac.uk/~das01/MyWeb/SCBI/Papers/Tierney94.pdf; Sections 2.3.1, 2.3.3–2.3.4, especially Rejection sampling chains, printed pp. 1704–1707 / PDF pp. 5–8 | supports | An independence Metropolis sampler whose proposals are generated by a rejection procedure with a fixed possibly non-dominating envelope, followed by a Metropolis correction for the resulting clipped proposal law. Version: Annals of Statistics 22(4), 1994; 29-page hosted scan including JSTOR cover and main article pp. 1701–1728, excluding discussion. Attested text pages: none; image-only scan. Attested visual pages: 1, 2, 5, 6, 7, 8. |
| rejectiondrivenindependencemetropolis-1 | https://conservancy.umn.edu/server/api/core/bitstreams/f87bc468-91ac-45bc-a1cf-5d4b0f8fbcd6/content; 1991 report Section 2.3, Rejection Sampling Chains, printed p. 6 / PDF p. 8; compare 1994 Section 2.3.4, printed p. 1707 / PDF p. 8 | supports | The inspected 1991 technical report prints pi(x)/(c h(x)) in the mixed acceptance case and an uncapped ratio in the both-outside case. The 1994 published Section 2.3.4 instead gives c h(x)/pi(x) and a minimum with one, matching the independence Metropolis ratio used in this record. Version: University of Minnesota Technical Report No. 560, August 8, 1991; 28 PDF pages; not the 1994 published version. Attested text pages: 7, 8. Attested visual pages: 7, 8. |
| cranknicolsonmetropolis-0 | https://arxiv.org/pdf/1202.0709v3; Sections 3–4.2, Equations (4.5), (4.6) and (4.11), reprint/PDF pp. 7–11 | supports | A Metropolis sampler for a Gaussian-reference target using a Crank–Nicolson discretization of the unpreconditioned reference Ornstein–Uhlenbeck dynamics as its proposal. Version: arXiv:1202.0709v3, 2013-10-10; 23-page electronic reprint of Statistical Science 28(3):424–446; reprint pagination differs from journal. Attested text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 19, 20, 21, 22, 23. Attested visual pages: 10, 11, 20. |
| preconditionedcranknicolson-0 | https://arxiv.org/pdf/1202.0709v3; Introduction Equation (1.1) and algorithm, Section 4.2 Equations (4.7)–(4.11), reprint/PDF pp. 3 and 10–11 | supports | A Metropolis sampler for a Gaussian-reference target whose proposal combines the current state with an independent draw from that reference using a scalar autoregressive coefficient. Version: arXiv:1202.0709v3, 2013-10-10; 23-page electronic reprint of Statistical Science 28(3):424–446; reprint pagination differs from journal. Attested text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 19, 20, 21, 22, 23. Attested visual pages: 10, 11, 20. |
| cranknicolsonlangevin-0 | https://arxiv.org/pdf/1202.0709v3; Sections 4.1 and 4.3, Equation (4.12) and the associated rho/acceptance expression, reprint/PDF pp. 9 and 11 | supports | A Metropolis-corrected Gaussian-reference sampler that combines a Crank–Nicolson treatment of the reference precision with an explicit gradient drift of the remaining target potential. Version: arXiv:1202.0709v3, 2013-10-10; 23-page electronic reprint of Statistical Science 28(3):424–446; reprint pagination differs from journal. Attested text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 19, 20, 21, 22, 23. Attested visual pages: 10, 11, 20. |
| preconditionedcranknicolsonlangevin-0 | https://arxiv.org/pdf/1202.0709v3; Sections 4.1 and 4.3, Equation (4.13) and its rho/acceptance expression, reprint/PDF pp. 9 and 11 | supports | A Metropolis-corrected Gaussian-reference sampler that preconditions the potential-gradient drift by the reference covariance and uses a scalar Crank–Nicolson autoregressive update. Version: arXiv:1202.0709v3, 2013-10-10; 23-page electronic reprint of Statistical Science 28(3):424–446; reprint pagination differs from journal. Attested text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 19, 20, 21, 22, 23. Attested visual pages: 10, 11, 20. |

## Limits And Additional Notes

- Adversarial author self-review only; all eight records remain DRAFT.
- Only declared text and visual pages were inspected. Tierney 1994 is a visually read scan, not a text-extracted full-paper read.
- Version discrepancies are documented with inspected equations; no separate published erratum is asserted.
- ARMS full original/correction access remains incomplete, so no ARMS mechanism is curated.
- The finite-dimensional gradient-proposal ratios are explicit specializations of the source Metropolis construction. Function-space theory has additional assumptions.
- No sampling experiment or benchmark was run and no universal convergence or performance claim is asserted.
- An initial sandboxed vendored-check failed to resolve the public host; the authorized network-enabled retry passed for all 22 immutable artifacts.
- All required checks passed. Repeated use of a paper is not independent evidence, and this review does not retire unrelated findings or establish discovery saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T071702Z-rejection-gaussian-sampling
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of rejection and Gaussian-reference samplers
started_at: '2026-10-11T07:14:45Z'
finished_at: '2026-10-11T07:17:02Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all eight actual
    YAMLs against inspected primary methods, equations, proofs, version discrepancies
    and exact AIO targets. Critical ARS, Tierney and CNL equations were revisited
    visually during review. No independent reviewer or approval is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain all eight distinct sampler identities, six related AIO mappings and
  two bounded no-match assessments. No actionable record defect was found. Independent
  generation, adaptive envelopes, angular slice search and Gaussian-reference proposal
  variants remain distinct; all records stay DRAFT.
source:
  git_revision: 7583609697d5c3b5e8820534fd130dd4e24debae
  state: working_tree
  inputs:
  - path: data/curated/AdaptiveRejectionSampling.yaml
    sha256: a737adf53c8f94b887427a3b56c7da458a11d0d42cd56083d66fcd68023d311b
    role: target
  - path: data/curated/CrankNicolsonLangevin.yaml
    sha256: d0171a10c78d7a9d62b97940c28c759741e50aee796ad1f32d12faa4ad08f6ce
    role: target
  - path: data/curated/CrankNicolsonMetropolis.yaml
    sha256: a0da3eb3b2e3fac5ccf6bfbae1f86f890235385e9bd6c110da4b6aa5fe815d45
    role: target
  - path: data/curated/EllipticalSliceSampling.yaml
    sha256: 6176b40f80f575b805140d402cd370f199c4db2083affd43fad991f1bc07df57
    role: target
  - path: data/curated/GibbsSampling.yaml
    sha256: 8175215986c0507e3664a3aedf8074fc067d85b4a89002091d1bcb9b637a522a
    role: context
  - path: data/curated/IndependenceMetropolisHastings.yaml
    sha256: ca1390f00edca43e94f897e2398b3f7d8edddefadc0a5780e0b470816a7754df
    role: context
  - path: data/curated/MetropolisWithinGibbs.yaml
    sha256: 0e9cfedc93c7e46cc6316809d5a9ec9488b33891a9c9862f914a0adf8f7cb140
    role: context
  - path: data/curated/PreconditionedCrankNicolson.yaml
    sha256: 3473e9f107f7975ce103c0253ba874af94a79ae08a1543f1e2633404f924768b
    role: target
  - path: data/curated/PreconditionedCrankNicolsonLangevin.yaml
    sha256: c756816ef326247f54b75b1c88d6df452742f39235676ef50056f6254ff375dc
    role: target
  - path: data/curated/RandomWalkMetropolisHastings.yaml
    sha256: aeff822517db546b4e3dee3421a54d5887ed178f3b9e6e3df46283eceb39677d
    role: context
  - path: data/curated/RejectionDrivenIndependenceMetropolis.yaml
    sha256: aa609541950d30328fc53a8fe035945d61bcc2d25866c55ed91b0676bb6548e0
    role: target
  - path: data/curated/RejectionSampling.yaml
    sha256: 69e7583098c6dd6cae145d01e3f95ac95424fe1f61436c9ded1b160e58e92d05
    role: target
  - path: research/discovery/20261011T071428Z-rejection-gaussian-sampling.json
    sha256: c0e8a5bdf591b878c26cc699281d0f2f75405bd0de8f071bcaffdbd243c3383e
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
- target_id: AIMech:RejectionSampling
  path: data/curated/RejectionSampling.yaml
  label: Rejection sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RejectionSampling.yaml
    role: maintained_record
- target_id: AIMech:AdaptiveRejectionSampling
  path: data/curated/AdaptiveRejectionSampling.yaml
  label: Adaptive rejection sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AdaptiveRejectionSampling.yaml
    role: maintained_record
- target_id: AIMech:EllipticalSliceSampling
  path: data/curated/EllipticalSliceSampling.yaml
  label: Elliptical slice sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/EllipticalSliceSampling.yaml
    role: maintained_record
- target_id: AIMech:RejectionDrivenIndependenceMetropolis
  path: data/curated/RejectionDrivenIndependenceMetropolis.yaml
  label: Rejection-driven independence Metropolis sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RejectionDrivenIndependenceMetropolis.yaml
    role: maintained_record
- target_id: AIMech:CrankNicolsonMetropolis
  path: data/curated/CrankNicolsonMetropolis.yaml
  label: Crank–Nicolson Metropolis sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CrankNicolsonMetropolis.yaml
    role: maintained_record
- target_id: AIMech:PreconditionedCrankNicolson
  path: data/curated/PreconditionedCrankNicolson.yaml
  label: Preconditioned Crank–Nicolson sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PreconditionedCrankNicolson.yaml
    role: maintained_record
- target_id: AIMech:CrankNicolsonLangevin
  path: data/curated/CrankNicolsonLangevin.yaml
  label: Crank–Nicolson Langevin sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CrankNicolsonLangevin.yaml
    role: maintained_record
- target_id: AIMech:PreconditionedCrankNicolsonLangevin
  path: data/curated/PreconditionedCrankNicolsonLangevin.yaml
  label: Preconditioned Crank–Nicolson Langevin sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PreconditionedCrankNicolsonLangevin.yaml
    role: maintained_record
scope:
  description: Eight maintained rejection and Gaussian-reference sampling algorithms.
  selection: Exactly the eight added IDs in the rejection-gaussian-sampling discovery
    ledger; no sampling.
  coverage: full
  population_size: 8
  reviewed_target_ids:
  - AIMech:RejectionSampling
  - AIMech:AdaptiveRejectionSampling
  - AIMech:EllipticalSliceSampling
  - AIMech:RejectionDrivenIndependenceMetropolis
  - AIMech:CrankNicolsonMetropolis
  - AIMech:PreconditionedCrankNicolson
  - AIMech:CrankNicolsonLangevin
  - AIMech:PreconditionedCrankNicolsonLangevin
  exclusions:
  - target: ARMS, derivative-free ARS, other source variants and uninspected sections
    reason: Their full mechanisms or corrections were not inspected; leads remain
      in the ledger.
  - target: Numerical sampler execution and benchmark reproduction
    reason: No sampler, model fit or numerical experiment was executed.
checks:
- check_id: required-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:RejectionSampling
  - AIMech:AdaptiveRejectionSampling
  - AIMech:EllipticalSliceSampling
  - AIMech:RejectionDrivenIndependenceMetropolis
  - AIMech:CrankNicolsonMetropolis
  - AIMech:PreconditionedCrankNicolson
  - AIMech:CrankNicolsonLangevin
  - AIMech:PreconditionedCrankNicolsonLangevin
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
  - AIMech:RejectionSampling
  - AIMech:AdaptiveRejectionSampling
  - AIMech:EllipticalSliceSampling
  - AIMech:RejectionDrivenIndependenceMetropolis
  - AIMech:CrankNicolsonMetropolis
  - AIMech:PreconditionedCrankNicolson
  - AIMech:CrankNicolsonLangevin
  - AIMech:PreconditionedCrankNicolsonLangevin
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
  - AIMech:RejectionSampling
  - AIMech:AdaptiveRejectionSampling
  - AIMech:EllipticalSliceSampling
  - AIMech:RejectionDrivenIndependenceMetropolis
  - AIMech:CrankNicolsonMetropolis
  - AIMech:PreconditionedCrankNicolson
  - AIMech:CrankNicolsonLangevin
  - AIMech:PreconditionedCrankNicolsonLangevin
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 175 curated concept record(s); 0 error(s).

    '
- check_id: required-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:RejectionSampling
  - AIMech:AdaptiveRejectionSampling
  - AIMech:EllipticalSliceSampling
  - AIMech:RejectionDrivenIndependenceMetropolis
  - AIMech:CrankNicolsonMetropolis
  - AIMech:PreconditionedCrankNicolson
  - AIMech:CrankNicolsonLangevin
  - AIMech:PreconditionedCrankNicolsonLangevin
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
  - AIMech:RejectionSampling
  - AIMech:AdaptiveRejectionSampling
  - AIMech:EllipticalSliceSampling
  - AIMech:RejectionDrivenIndependenceMetropolis
  - AIMech:CrankNicolsonMetropolis
  - AIMech:PreconditionedCrankNicolson
  - AIMech:CrankNicolsonLangevin
  - AIMech:PreconditionedCrankNicolsonLangevin
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 34 history record(s); 0 error(s).

    '
- check_id: required-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:RejectionSampling
  - AIMech:AdaptiveRejectionSampling
  - AIMech:EllipticalSliceSampling
  - AIMech:RejectionDrivenIndependenceMetropolis
  - AIMech:CrankNicolsonMetropolis
  - AIMech:PreconditionedCrankNicolson
  - AIMech:CrankNicolsonLangevin
  - AIMech:PreconditionedCrankNicolsonLangevin
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 34,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\ntopClass is deprecated - use top_class\n"
- check_id: required-6
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:RejectionSampling
  - AIMech:AdaptiveRejectionSampling
  - AIMech:EllipticalSliceSampling
  - AIMech:RejectionDrivenIndependenceMetropolis
  - AIMech:CrankNicolsonMetropolis
  - AIMech:PreconditionedCrankNicolson
  - AIMech:CrankNicolsonLangevin
  - AIMech:PreconditionedCrankNicolsonLangevin
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 71.52s (0:01:11)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 175 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 34 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 34,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-7
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:RejectionSampling
  - AIMech:AdaptiveRejectionSampling
  - AIMech:EllipticalSliceSampling
  - AIMech:RejectionDrivenIndependenceMetropolis
  - AIMech:CrankNicolsonMetropolis
  - AIMech:PreconditionedCrankNicolson
  - AIMech:CrankNicolsonLangevin
  - AIMech:PreconditionedCrankNicolsonLangevin
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T071428Z-rejection-gaussian-sampling.json
  accessed_at: '2026-10-11T07:14:45Z'
  support: supports
  summary: 'No normalized identity match across all 442 AIO labels/scoped synonyms
    and 167 preceding native IDs/names/aliases. Both ignored-inclusive full-checkout
    searches returned 15 lines, all inspected: shared Tierney paper titles in Gibbs/MWG/random-walk
    records and the previous discovery ledger, plus the ARS/ARMS lead. These are references/leads
    rather than duplicates. Existing independence Metropolis and the earlier Gibbs/MWG/random-walk
    YAML mechanisms were inspected; specialization and proposal-generator differences
    are retained.'
  search_scope: All 442 AIO labels/scoped synonyms and 167 preceding native IDs/names/aliases;
    both full checkouts include ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-11T07:14:45Z'
  support: supports
  locator: Exact MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel, MathematicalFunction
    and SelectionAndSamplingBias CLASS definitions, synonyms and incident edges
  summary: 'Six Markov samplers receive related_match to AIO:MarkovChain, whose exact
    definition, synonyms, Network parent and hidden-layer edge were inspected. Ordinary
    and adaptive rejection generation receive explicit aio_no_match with five inspected
    rejected targets: MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel, MathematicalFunction
    and SelectionAndSamplingBias. Independent generation is not forced into a process/model
    class merely because it can be used inside Gibbs. Semantic search covered sampling,
    Monte Carlo, Markov, Bayesian, probabilistic and mathematical-function descriptions
    across the pin. No ontology axiom is changed.'
- evidence_id: existing-samplers
  kind: record_content
  reference: data/curated/IndependenceMetropolisHastings.yaml
  accessed_at: '2026-10-11T07:14:45Z'
  support: supports
  locator: Definition, identity and mechanism; also GibbsSampling, MetropolisWithinGibbs
    and RandomWalkMetropolisHastings YAMLs
  summary: Existing records distinguish exact conditional resampling, conditional
    invariant transitions, additive proposals and fixed state-independent proposals.
    The rejection-driven chain adds a specific clipped proposal generator; ordinary
    rejection and ARS yield independent draws for fixed targets, while ESS and the
    CN family specify different Markov updates.
- evidence_id: rejectionsampling-0
  kind: primary_source
  reference: https://hedibert.org/wp-content/uploads/2013/12/1992GilksWild.pdf
  locator: Section 2.1, Rejection Sampling, printed pp. 338–339 / PDF pp. 3–4
  accessed_at: '2026-10-11T07:04:24Z'
  snapshot_sha256: c88f55b2e19e6e3a7f828ba1dcd84ff65db20924220779a12680f7fe84fc2c55
  support: supports
  summary: 'A random-variate generation algorithm that draws proposals from a normalized
    envelope dominating an unnormalized target and accepts each with the target-to-envelope
    ratio, yielding independent target draws with fresh independent random trials.
    Version: Applied Statistics 41(2), 1992, pp. 337–348; 13-page published scan including
    JSTOR cover. Attested text pages: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13. Attested
    visual pages: 4, 5, 6.'
- evidence_id: adaptiverejectionsampling-0
  kind: primary_source
  reference: https://hedibert.org/wp-content/uploads/2013/12/1992GilksWild.pdf
  locator: Sections 2.2–2.3, Equations (1)–(4), initialization, sampling step and
    correctness argument, printed pp. 339–342 / PDF pp. 4–7; conclusion on numerical
    care, p. 347 / PDF p. 12
  accessed_at: '2026-10-11T07:04:24Z'
  snapshot_sha256: c88f55b2e19e6e3a7f828ba1dcd84ff65db20924220779a12680f7fe84fc2c55
  support: supports
  summary: 'The Gilks–Wild univariate rejection sampler that uses tangents to a concave
    log density as a piecewise-linear upper hull and chords as a lower hull, updating
    these bounds from evaluated proposals. Version: Applied Statistics 41(2), 1992,
    pp. 337–348; 13-page published scan including JSTOR cover. Attested text pages:
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13. Attested visual pages: 4, 5, 6.'
- evidence_id: ellipticalslicesampling-0
  kind: primary_source
  reference: https://proceedings.mlr.press/v9/murray10a/murray10a.pdf
  locator: Sections 2.1–2.3, Figure 2 and correctness proof, printed pp. 542–545 /
    PDF pp. 2–5
  accessed_at: '2026-10-11T07:03:48Z'
  snapshot_sha256: ad6fbbfb8fb7b5899161ab425f0516e81c9c0f3a95ddcd9da04e4745ce232eee
  support: supports
  summary: 'A Markov-chain update for a target factored into a Gaussian prior and
    a likelihood, which performs an angular slice search along the ellipse defined
    by the current state and an independent prior draw. Version: AISTATS 2010, PMLR
    9, pp. 541–548; eight-page proceedings PDF. Attested text pages: 1, 2, 3, 4, 5,
    6, 7, 8. Attested visual pages: 3.'
- evidence_id: rejectiondrivenindependencemetropolis-0
  kind: primary_source
  reference: https://www.ma.imperial.ac.uk/~das01/MyWeb/SCBI/Papers/Tierney94.pdf
  locator: Sections 2.3.1, 2.3.3–2.3.4, especially Rejection sampling chains, printed
    pp. 1704–1707 / PDF pp. 5–8
  accessed_at: '2026-10-11T07:07:24Z'
  snapshot_sha256: 91155ffee0e33211c993e8de23fd8ff7612a84112df318231efee89716aa1053
  support: supports
  summary: 'An independence Metropolis sampler whose proposals are generated by a
    rejection procedure with a fixed possibly non-dominating envelope, followed by
    a Metropolis correction for the resulting clipped proposal law. Version: Annals
    of Statistics 22(4), 1994; 29-page hosted scan including JSTOR cover and main
    article pp. 1701–1728, excluding discussion. Attested text pages: none; image-only
    scan. Attested visual pages: 1, 2, 5, 6, 7, 8.'
- evidence_id: rejectiondrivenindependencemetropolis-1
  kind: primary_source
  reference: https://conservancy.umn.edu/server/api/core/bitstreams/f87bc468-91ac-45bc-a1cf-5d4b0f8fbcd6/content
  locator: 1991 report Section 2.3, Rejection Sampling Chains, printed p. 6 / PDF
    p. 8; compare 1994 Section 2.3.4, printed p. 1707 / PDF p. 8
  accessed_at: '2026-10-11T06:52:00Z'
  snapshot_sha256: cfde8fc2fa3c390da09badda81394a0a334d70f13403031ac9d4c0b5a1e11fde
  support: supports
  summary: 'The inspected 1991 technical report prints pi(x)/(c h(x)) in the mixed
    acceptance case and an uncapped ratio in the both-outside case. The 1994 published
    Section 2.3.4 instead gives c h(x)/pi(x) and a minimum with one, matching the
    independence Metropolis ratio used in this record. Version: University of Minnesota
    Technical Report No. 560, August 8, 1991; 28 PDF pages; not the 1994 published
    version. Attested text pages: 7, 8. Attested visual pages: 7, 8.'
- evidence_id: cranknicolsonmetropolis-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1202.0709v3
  locator: Sections 3–4.2, Equations (4.5), (4.6) and (4.11), reprint/PDF pp. 7–11
  accessed_at: '2026-10-11T07:06:31Z'
  snapshot_sha256: 4be2044ef1d84ae82730a524b3ea2ea3047711138fc9dd8afeefb6a050c786a0
  support: supports
  summary: 'A Metropolis sampler for a Gaussian-reference target using a Crank–Nicolson
    discretization of the unpreconditioned reference Ornstein–Uhlenbeck dynamics as
    its proposal. Version: arXiv:1202.0709v3, 2013-10-10; 23-page electronic reprint
    of Statistical Science 28(3):424–446; reprint pagination differs from journal.
    Attested text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 19, 20, 21, 22,
    23. Attested visual pages: 10, 11, 20.'
- evidence_id: preconditionedcranknicolson-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1202.0709v3
  locator: Introduction Equation (1.1) and algorithm, Section 4.2 Equations (4.7)–(4.11),
    reprint/PDF pp. 3 and 10–11
  accessed_at: '2026-10-11T07:06:31Z'
  snapshot_sha256: 4be2044ef1d84ae82730a524b3ea2ea3047711138fc9dd8afeefb6a050c786a0
  support: supports
  summary: 'A Metropolis sampler for a Gaussian-reference target whose proposal combines
    the current state with an independent draw from that reference using a scalar
    autoregressive coefficient. Version: arXiv:1202.0709v3, 2013-10-10; 23-page electronic
    reprint of Statistical Science 28(3):424–446; reprint pagination differs from
    journal. Attested text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 19, 20,
    21, 22, 23. Attested visual pages: 10, 11, 20.'
- evidence_id: cranknicolsonlangevin-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1202.0709v3
  locator: Sections 4.1 and 4.3, Equation (4.12) and the associated rho/acceptance
    expression, reprint/PDF pp. 9 and 11
  accessed_at: '2026-10-11T07:06:31Z'
  snapshot_sha256: 4be2044ef1d84ae82730a524b3ea2ea3047711138fc9dd8afeefb6a050c786a0
  support: supports
  summary: 'A Metropolis-corrected Gaussian-reference sampler that combines a Crank–Nicolson
    treatment of the reference precision with an explicit gradient drift of the remaining
    target potential. Version: arXiv:1202.0709v3, 2013-10-10; 23-page electronic reprint
    of Statistical Science 28(3):424–446; reprint pagination differs from journal.
    Attested text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 19, 20, 21, 22,
    23. Attested visual pages: 10, 11, 20.'
- evidence_id: preconditionedcranknicolsonlangevin-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1202.0709v3
  locator: Sections 4.1 and 4.3, Equation (4.13) and its rho/acceptance expression,
    reprint/PDF pp. 9 and 11
  accessed_at: '2026-10-11T07:06:31Z'
  snapshot_sha256: 4be2044ef1d84ae82730a524b3ea2ea3047711138fc9dd8afeefb6a050c786a0
  support: supports
  summary: 'A Metropolis-corrected Gaussian-reference sampler that preconditions the
    potential-gradient drift by the reference covariance and uses a scalar Crank–Nicolson
    autoregressive update. Version: arXiv:1202.0709v3, 2013-10-10; 23-page electronic
    reprint of Statistical Science 28(3):424–446; reprint pagination differs from
    journal. Attested text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 19, 20,
    21, 22, 23. Attested visual pages: 10, 11, 20.'
assessments:
- assessment_id: rejectionsampling
  area: evidence
  topic: Identity, sampling mechanism, evidence scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:RejectionSampling
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - rejectionsampling-0
  summary: This is ordinary accept-reject generation with a valid global envelope.
    A rejected candidate is discarded, not recorded as a repeated chain state. The
    method differs from Metropolis acceptance, rejection-driven Metropolis proposals,
    importance weighting and selective filtering of model answers. The inspected primary
    source presents the scalar density case. No normalized identity match was found
    across all 442 pinned AIO labels/scoped synonyms and 167 prior native IDs/names/aliases.
    Full-checkout searches in both worktrees included ignored and hidden files; the
    15 lines in each were shared Tierney source-title references or an adaptive-rejection
    discovery lead, not matching records. Existing Gibbs, Metropolis-within-Gibbs,
    random-walk and independence Metropolis mechanisms were inspected to resolve specialization
    boundaries.
  details: A valid dominating envelope and an exact sampler for its normalized distribution
    are required. Clipping an invalid envelope ratio at one does not preserve the
    intended independent-sample law. An envelope with excessive mass can make acceptance
    rare. No universal efficiency, dimensional scaling or bound on the number of trials
    is claimed. The optional squeezing bound must be valid everywhere it is used;
    it is an evaluation shortcut, not a replacement target. Numerical approximation,
    finite precision and inaccurate envelope sampling can change the output distribution.
    Log concavity is not required by ordinary rejection sampling itself.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A random-variate generation or Markov sampling algorithm, with stated
      target and proposal conditions; not a probability model, numerical benchmark
      or trained instance.
    evidence_ids:
    - rejectionsampling-0
  - name: aio-assessment
    value: explicit aio_no_match
    definition: 'No suitable target for this independent random-variate generator
      was found in the inspected pin. Its possible use inside a Gibbs sampler or Bayesian
      model is insufficient to force a process/model mapping. This is a bounded assessment
      of this AIO snapshot. AIO:MarkovChain: A stochastic sequence/model exported
      beneath Network, rather than an independent random-variate generation procedure.
      Embedding independent draws in a chain or an outer Gibbs algorithm does not
      establish the needed concept relation here. AIO:ProbabilisticGraphicalModel:
      Defines a graphical conditional-dependence task; no graphical factorization
      defines this generator. AIO:BayesianNetwork: A directed acyclic probabilistic
      model, not this sampling algorithm; use for a conditional distribution is incidental.
      AIO:MathematicalFunction: A generic rule assigning dependent-variable values
      is not a suitable identity or informative broader mapping for a randomized accept-reject
      procedure. AIO:SelectionAndSamplingBias: Describes selection-induced representativeness
      error, not exact generation from a specified target; shared sampling terminology
      is insufficient.'
    evidence_ids:
    - identity
    - mapping
- assessment_id: adaptiverejectionsampling
  area: evidence
  topic: Identity, sampling mechanism, evidence scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:AdaptiveRejectionSampling
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - adaptiverejectionsampling-0
  summary: This record scopes ARS to the derivative-based tangent construction in
    Gilks and Wild (1992), for a fixed log-concave scalar target on a connected domain.
    Derivative-free envelope constructions and adaptive rejection Metropolis sampling
    are distinct variants requiring their own evidence. Exact conditional draws do
    not make successive joint Gibbs states independent. No normalized identity match
    was found across all 442 pinned AIO labels/scoped synonyms and 167 prior native
    IDs/names/aliases. Full-checkout searches in both worktrees included ignored and
    hidden files; the 15 lines in each were shared Tierney source-title references
    or an adaptive-rejection discovery lead, not matching records. Existing Gibbs,
    Metropolis-within-Gibbs, random-walk and independence Metropolis mechanisms were
    inspected to resolve specialization boundaries.
  details: Concavity of log g is essential for the tangent and chord bounds. Unimodality
    alone is insufficient, and non-log-concave targets are not covered by this construction.
    The displayed baseline assumes usable derivatives and connected scalar support.
    It does not assert validity for every nonsmooth density or a direct multivariate
    joint draw. Tail slopes and support endpoints must make the proposal integrable.
    Concentrated or skewed densities require numerical care. When a Gibbs conditional
    changes, hull values must be computed for that conditional; reusing stale density
    bounds is not justified. No universal evaluation savings or benchmark result is
    asserted. ARMS and its 1997 correction remain separate uninspected-method leads.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A random-variate generation or Markov sampling algorithm, with stated
      target and proposal conditions; not a probability model, numerical benchmark
      or trained instance.
    evidence_ids:
    - adaptiverejectionsampling-0
  - name: aio-assessment
    value: explicit aio_no_match
    definition: 'No suitable target for this independent random-variate generator
      was found in the inspected pin. Its possible use inside a Gibbs sampler or Bayesian
      model is insufficient to force a process/model mapping. This is a bounded assessment
      of this AIO snapshot. AIO:MarkovChain: A stochastic sequence/model exported
      beneath Network, rather than an independent random-variate generation procedure.
      Embedding independent draws in a chain or an outer Gibbs algorithm does not
      establish the needed concept relation here. AIO:ProbabilisticGraphicalModel:
      Defines a graphical conditional-dependence task; no graphical factorization
      defines this generator. AIO:BayesianNetwork: A directed acyclic probabilistic
      model, not this sampling algorithm; use for a conditional distribution is incidental.
      AIO:MathematicalFunction: A generic rule assigning dependent-variable values
      is not a suitable identity or informative broader mapping for a randomized accept-reject
      procedure. AIO:SelectionAndSamplingBias: Describes selection-induced representativeness
      error, not exact generation from a specified target; shared sampling terminology
      is insufficient.'
    evidence_ids:
    - identity
    - mapping
- assessment_id: ellipticalslicesampling
  area: evidence
  topic: Identity, sampling mechanism, evidence scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:EllipticalSliceSampling
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - ellipticalslicesampling-0
  summary: This is the full-circle default algorithm in Murray et al. Figure 2 for
    a fixed Gaussian prior covariance. It differs from a fixed-angle Gaussian autoregressive
    Metropolis proposal and from scalar interval stepping-out or doubling. ESS here
    denotes this sampler, not the effective-sample-size diagnostic. No normalized
    identity match was found across all 442 pinned AIO labels/scoped synonyms and
    167 prior native IDs/names/aliases. Full-checkout searches in both worktrees included
    ignored and hidden files; the 15 lines in each were shared Tierney source-title
    references or an adaptive-rejection discovery lead, not matching records. Existing
    Gibbs, Metropolis-within-Gibbs, random-walk and independence Metropolis mechanisms
    were inspected to resolve specialization boundaries.
  details: A Gaussian prior draw and likelihood evaluation are required. A nonzero
    prior mean must be handled by centering the ellipse; an arbitrary non-Gaussian
    prior is outside this formula. Fixing the initial bracket deterministically to
    [−pi,pi] is not the proved algorithm; the paper explicitly explains why its random
    placement matters. The algorithm may reject multiple internal angle trials before
    returning an update. Its lack of an outer Metropolis rejection is not a claim
    of one likelihood evaluation or independent retained states. The default full-circle
    algorithm avoids a user-specified proposal scale, but covariance, model hyperparameters
    and optional narrower angular variants still involve choices. Strong offsets,
    covariance structure and likelihood geometry can impede exploration. No universal
    mixing rate, finite-run accuracy or timing advantage is asserted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A random-variate generation or Markov sampling algorithm, with stated
      target and proposal conditions; not a probability model, numerical benchmark
      or trained instance.
    evidence_ids:
    - ellipticalslicesampling-0
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This algorithm constructs target-invariant Markov transitions under
      its stated assumptions. The exact AIO CLASS denotes a stochastic process/model
      and is exported beneath Network. This is a method-to-process related match,
      not equivalence, subclass membership, independence of retained draws or a claim
      that the algorithm is a trained network.
    evidence_ids:
    - identity
    - mapping
- assessment_id: rejectiondrivenindependencemetropolis
  area: evidence
  topic: Identity, sampling mechanism, evidence scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:RejectionDrivenIndependenceMetropolis
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - rejectiondrivenindependencemetropolis-0
  - rejectiondrivenindependencemetropolis-1
  summary: This is Tierney’s rejection sampling chain in Section 2.3.4. It specializes
    independence Metropolis by an inner proposal generator; it is not ordinary rejection
    sampling unless the envelope dominates everywhere. It is distinct from adaptive
    rejection Metropolis sampling, because h and c are fixed here. No normalized identity
    match was found across all 442 pinned AIO labels/scoped synonyms and 167 prior
    native IDs/names/aliases. Full-checkout searches in both worktrees included ignored
    and hidden files; the 15 lines in each were shared Tierney source-title references
    or an adaptive-rejection discovery lead, not matching records. Existing Gibbs,
    Metropolis-within-Gibbs, random-walk and independence Metropolis mechanisms were
    inspected to resolve specialization boundaries.
  details: The inner proposal must have positive acceptance mass and cover the target
    support required for irreducibility. A poor choice of h or c can make either stage
    inefficient. The inner rejected trials are discarded, while rejection by the outer
    Metropolis test repeats the chain state; these two rejection events have different
    roles. A non-dominating envelope without the outer correction generally gives
    the clipped density rather than pi. Correcting it does not guarantee fast mixing.
    The inspected 1991 technical report prints the reciprocal of the mixed-case factor
    and omits the minimum with one in the final case. This record uses the visually
    verified 1994 published expressions, consistent with the general independence
    ratio; no separate erratum is asserted. Adapting h or c from chain history is
    outside the fixed-proposal definition and needs its own validity argument.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A random-variate generation or Markov sampling algorithm, with stated
      target and proposal conditions; not a probability model, numerical benchmark
      or trained instance.
    evidence_ids:
    - rejectiondrivenindependencemetropolis-0
    - rejectiondrivenindependencemetropolis-1
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This algorithm constructs target-invariant Markov transitions under
      its stated assumptions. The exact AIO CLASS denotes a stochastic process/model
      and is exported beneath Network. This is a method-to-process related match,
      not equivalence, subclass membership, independence of retained draws or a claim
      that the algorithm is a trained network.
    evidence_ids:
    - identity
    - mapping
- assessment_id: cranknicolsonmetropolis
  area: evidence
  topic: Identity, sampling mechanism, evidence scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:CrankNicolsonMetropolis
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - cranknicolsonmetropolis-0
  summary: This is the CN proposal of Cotter et al. Section 4.2 paired with its Metropolis
    test, not the generic Crank–Nicolson numerical integration scheme. Unlike pCN,
    its proposal requires an operator or matrix solve involving C and the step size.
    It contains no likelihood-gradient drift. No normalized identity match was found
    across all 442 pinned AIO labels/scoped synonyms and 167 prior native IDs/names/aliases.
    Full-checkout searches in both worktrees included ignored and hidden files; the
    15 lines in each were shared Tierney source-title references or an adaptive-rejection
    discovery lead, not matching records. Existing Gibbs, Metropolis-within-Gibbs,
    random-walk and independence Metropolis mechanisms were inspected to resolve specialization
    boundaries.
  details: The target must be proper relative to the Gaussian reference. The explicit
    density-ratio implementation here is finite-dimensional with symmetric positive-definite
    C; function-space extensions require the source’s operator, regularity and absolute-continuity
    assumptions. Target invariance does not imply independent draws, good exploration
    or finite-run accuracy. Mesh-robust behavior under stated assumptions is not a
    universal dimension-free performance guarantee. C and the step size are fixed
    in the stated kernel. Adaptive covariance or step-size policies need separate
    validity arguments. The reprint’s later Equation (6.2) reverses signs relative
    to Equation (6.1) and the explicit Section 4 proposals. This record uses Section
    4 and does not claim a published erratum or use the inconsistent expression. An
    accurate linear solve and Gaussian draw are required. Replacing the noise by an
    incorrectly scaled standard Gaussian changes the proposal and invalidates the
    stated cancellation.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A random-variate generation or Markov sampling algorithm, with stated
      target and proposal conditions; not a probability model, numerical benchmark
      or trained instance.
    evidence_ids:
    - cranknicolsonmetropolis-0
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This algorithm constructs target-invariant Markov transitions under
      its stated assumptions. The exact AIO CLASS denotes a stochastic process/model
      and is exported beneath Network. This is a method-to-process related match,
      not equivalence, subclass membership, independence of retained draws or a claim
      that the algorithm is a trained network.
    evidence_ids:
    - identity
    - mapping
- assessment_id: preconditionedcranknicolson
  area: evidence
  topic: Identity, sampling mechanism, evidence scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:PreconditionedCrankNicolson
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - preconditionedcranknicolson-0
  summary: This is the pCN proposal and likelihood-ratio test in Cotter et al. Section
    4.2. It preserves the Gaussian reference before correction and differs from an
    additive random walk, the unpreconditioned CN solve and an angular slice search.
    The displayed nonnegative coefficient form uses the source’s delta≤2 parameterization.
    No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 167 prior native IDs/names/aliases. Full-checkout searches in both
    worktrees included ignored and hidden files; the 15 lines in each were shared
    Tierney source-title references or an adaptive-rejection discovery lead, not matching
    records. Existing Gibbs, Metropolis-within-Gibbs, random-walk and independence
    Metropolis mechanisms were inspected to resolve specialization boundaries.
  details: The target must be proper relative to the Gaussian reference. The explicit
    density-ratio implementation here is finite-dimensional with symmetric positive-definite
    C; function-space extensions require the source’s operator, regularity and absolute-continuity
    assumptions. Target invariance does not imply independent draws, good exploration
    or finite-run accuracy. Mesh-robust behavior under stated assumptions is not a
    universal dimension-free performance guarantee. C and the step size are fixed
    in the stated kernel. Adaptive covariance or step-size policies need separate
    validity arguments. The reprint’s later Equation (6.2) reverses signs relative
    to Equation (6.1) and the explicit Section 4 proposals. This record uses Section
    4 and does not claim a published erratum or use the inconsistent expression. Beta=0
    would give no movement and is excluded from this stated sampler. Delta>2 in the
    original linear form gives a negative autoregressive coefficient and is not represented
    by the positive square-root parameterization here.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A random-variate generation or Markov sampling algorithm, with stated
      target and proposal conditions; not a probability model, numerical benchmark
      or trained instance.
    evidence_ids:
    - preconditionedcranknicolson-0
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This algorithm constructs target-invariant Markov transitions under
      its stated assumptions. The exact AIO CLASS denotes a stochastic process/model
      and is exported beneath Network. This is a method-to-process related match,
      not equivalence, subclass membership, independence of retained draws or a claim
      that the algorithm is a trained network.
    evidence_ids:
    - identity
    - mapping
- assessment_id: cranknicolsonlangevin
  area: evidence
  topic: Identity, sampling mechanism, evidence scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:CrankNicolsonLangevin
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - cranknicolsonlangevin-0
  summary: This is Cotter et al. CNL, with unpreconditioned dynamics and a precision-dependent
    linear solve. The potential gradient is of Phi relative to the Gaussian reference,
    not of the entire Lebesgue log density. It differs from CN by its gradient term
    and from pCNL by its preconditioning. No normalized identity match was found across
    all 442 pinned AIO labels/scoped synonyms and 167 prior native IDs/names/aliases.
    Full-checkout searches in both worktrees included ignored and hidden files; the
    15 lines in each were shared Tierney source-title references or an adaptive-rejection
    discovery lead, not matching records. Existing Gibbs, Metropolis-within-Gibbs,
    random-walk and independence Metropolis mechanisms were inspected to resolve specialization
    boundaries.
  details: The target must be proper relative to the Gaussian reference. The explicit
    density-ratio implementation here is finite-dimensional with symmetric positive-definite
    C; function-space extensions require the source’s operator, regularity and absolute-continuity
    assumptions. Target invariance does not imply independent draws, good exploration
    or finite-run accuracy. Mesh-robust behavior under stated assumptions is not a
    universal dimension-free performance guarantee. C and the step size are fixed
    in the stated kernel. Adaptive covariance or step-size policies need separate
    validity arguments. The reprint’s later Equation (6.2) reverses signs relative
    to Equation (6.1) and the explicit Section 4 proposals. This record uses Section
    4 and does not claim a published erratum or use the inconsistent expression. The
    gradient and forward/reverse Gaussian densities must be evaluated consistently.
    In infinite dimensions one must use the source’s measure-based acceptance under
    its assumptions, not a nonexistent Lebesgue density. No identity with every MALA
    implementation or guaranteed advantage over CN or pCN is asserted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A random-variate generation or Markov sampling algorithm, with stated
      target and proposal conditions; not a probability model, numerical benchmark
      or trained instance.
    evidence_ids:
    - cranknicolsonlangevin-0
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This algorithm constructs target-invariant Markov transitions under
      its stated assumptions. The exact AIO CLASS denotes a stochastic process/model
      and is exported beneath Network. This is a method-to-process related match,
      not equivalence, subclass membership, independence of retained draws or a claim
      that the algorithm is a trained network.
    evidence_ids:
    - identity
    - mapping
- assessment_id: preconditionedcranknicolsonlangevin
  area: evidence
  topic: Identity, sampling mechanism, evidence scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:PreconditionedCrankNicolsonLangevin
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - preconditionedcranknicolsonlangevin-0
  summary: This is Cotter et al. pCNL. The reference covariance multiplies grad Phi,
    and the linear denominator is the scalar 2+delta, distinguishing it from the CNL
    matrix solve. Removing the potential gradient recovers the pCN proposal, but a
    nonzero gradient changes its acceptance rule. No normalized identity match was
    found across all 442 pinned AIO labels/scoped synonyms and 167 prior native IDs/names/aliases.
    Full-checkout searches in both worktrees included ignored and hidden files; the
    15 lines in each were shared Tierney source-title references or an adaptive-rejection
    discovery lead, not matching records. Existing Gibbs, Metropolis-within-Gibbs,
    random-walk and independence Metropolis mechanisms were inspected to resolve specialization
    boundaries.
  details: The target must be proper relative to the Gaussian reference. The explicit
    density-ratio implementation here is finite-dimensional with symmetric positive-definite
    C; function-space extensions require the source’s operator, regularity and absolute-continuity
    assumptions. Target invariance does not imply independent draws, good exploration
    or finite-run accuracy. Mesh-robust behavior under stated assumptions is not a
    universal dimension-free performance guarantee. C and the step size are fixed
    in the stated kernel. Adaptive covariance or step-size policies need separate
    validity arguments. The reprint’s later Equation (6.2) reverses signs relative
    to Equation (6.1) and the explicit Section 4 proposals. This record uses Section
    4 and does not claim a published erratum or use the inconsistent expression. The
    gradient is of the potential relative to the Gaussian reference. Substituting
    the full log-target gradient without accounting for the already implicit Gaussian
    drift defines a different proposal. Function-space validity and efficient discretizations
    need the source’s extra assumptions; the finite-dimensional density ratio is not
    a definition of an infinite-dimensional Lebesgue density.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A random-variate generation or Markov sampling algorithm, with stated
      target and proposal conditions; not a probability model, numerical benchmark
      or trained instance.
    evidence_ids:
    - preconditionedcranknicolsonlangevin-0
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This algorithm constructs target-invariant Markov transitions under
      its stated assumptions. The exact AIO CLASS denotes a stochastic process/model
      and is exported beneath Network. This is a method-to-process related match,
      not equivalence, subclass membership, independence of retained draws or a claim
      that the algorithm is a trained network.
    evidence_ids:
    - identity
    - mapping
- assessment_id: rejection-boundaries
  area: scope
  topic: Independent generation, adaptive hulls and rejection-driven Markov states
  outcome: supported
  target_ids:
  - AIMech:RejectionSampling
  - AIMech:AdaptiveRejectionSampling
  - AIMech:RejectionDrivenIndependenceMetropolis
  evidence_ids:
  - rejectionsampling-0
  - adaptiverejectionsampling-0
  - rejectiondrivenindependencemetropolis-0
  - rejectiondrivenindependencemetropolis-1
  - existing-samplers
  summary: Retain ordinary rejection, derivative-based ARS and the fixed-envelope
    rejection-driven Metropolis chain as distinct procedures.
  details: Ordinary rejection needs a dominating integrable envelope; ARS obtains
    one from log-concavity and tangents and updates on every full density/derivative
    evaluation. Neither requires repetition of a previous output after rejecting an
    inner trial. The Tierney construction instead corrects proposals proportional
    to min(pi,c h), retaining an outer rejected state. The 1994 mixed-case and final-case
    formulas agree with the general independence ratio and resolve the two incompatible
    1991 expressions.
- assessment_id: elliptical-versus-autoregressive
  area: scope
  topic: Random angular slice bracket versus a fixed Gaussian-reference Metropolis
    proposal
  outcome: supported
  target_ids:
  - AIMech:EllipticalSliceSampling
  - AIMech:PreconditionedCrankNicolson
  evidence_ids:
  - ellipticalslicesampling-0
  - preconditionedcranknicolson-0
  summary: ESS and pCN share Gaussian-reference geometry but use different candidate
    selection and acceptance procedures.
  details: ESS keeps one auxiliary Gaussian draw and slice threshold while shrinking
    a randomly positioned full-circle angular bracket around zero. pCN draws a fixed-coefficient
    autoregressive proposal and accepts it using the potential difference. A deterministic
    ESS bracket is not substituted; internal angle rejections are acknowledged. Beta=1
    is an independence proposal, not a claim that outer retained states are independent.
- assessment_id: cn-family
  area: scope
  topic: Preconditioning, likelihood-gradient drift and Metropolis acceptance
  outcome: supported
  target_ids:
  - AIMech:CrankNicolsonMetropolis
  - AIMech:PreconditionedCrankNicolson
  - AIMech:CrankNicolsonLangevin
  - AIMech:PreconditionedCrankNicolsonLangevin
  evidence_ids:
  - cranknicolsonmetropolis-0
  - preconditionedcranknicolson-0
  - cranknicolsonlangevin-0
  - preconditionedcranknicolsonlangevin-0
  summary: The four CN-family records retain distinct matrix/scalar proposal operators
    and the presence or absence of potential-gradient drift.
  details: The explicit Section 4 equations were visually checked. CN uses a solve
    involving 2C+delta I, while pCN uses 2+delta. Gradient variants add −2 delta C
    grad Phi and need the full forward/reverse proposal correction. Their finite-dimensional
    density-ratio expression is explicitly an algebraic specialization, not an infinite-dimensional
    Lebesgue formula. The later Equation (6.2) has reversed signs relative to (6.1);
    it is documented and not used. No universal dimension-independent efficiency theorem
    is asserted.
- assessment_id: no-match-boundaries
  area: representation
  topic: Independent generators and bounded absence of an informative AIO mapping
  outcome: supported
  target_ids:
  - AIMech:RejectionSampling
  - AIMech:AdaptiveRejectionSampling
  evidence_ids:
  - identity
  - mapping
  - rejectionsampling-0
  - adaptiverejectionsampling-0
  summary: The explicit no-match assessments are supported by the searched pin and
    rejected-target definitions.
  details: Independent generation can be embedded in a Markov process, but that mathematical
    possibility and an outer Gibbs application do not justify this model/network mapping.
    Graphical dependence tasks, Bayesian DAG models, generic mathematical functions
    and sampling-bias categories likewise do not define these generators. The no-match
    conclusion is limited to the inspected snapshot; it is not a statement about all
    ontologies.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:RejectionSampling
  - AIMech:AdaptiveRejectionSampling
  - AIMech:EllipticalSliceSampling
  - AIMech:RejectionDrivenIndependenceMetropolis
  - AIMech:CrankNicolsonMetropolis
  - AIMech:PreconditionedCrankNicolson
  - AIMech:CrankNicolsonLangevin
  - AIMech:PreconditionedCrankNicolsonLangevin
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - rejectionsampling-0
  - adaptiverejectionsampling-0
  - ellipticalslicesampling-0
  - rejectiondrivenindependencemetropolis-0
  - rejectiondrivenindependencemetropolis-1
  - cranknicolsonmetropolis-0
  - preconditionedcranknicolson-0
  - cranknicolsonlangevin-0
  - preconditionedcranknicolsonlangevin-0
  rationale: Preserve ordinary rejection and its derivative-based ARS specialization,
    the rejection-driven independence chain, elliptical angular slice updates, and
    the four explicitly different CN-family proposals. Shared Gaussian priors or acceptance
    components do not establish equivalence. The two no-match assessments are bounded
    local mapping judgments; the other six related mappings do not assert a network
    subclass.
limitations:
- Adversarial author self-review only; all eight records remain DRAFT.
- Only declared text and visual pages were inspected. Tierney 1994 is a visually read
  scan, not a text-extracted full-paper read.
- Version discrepancies are documented with inspected equations; no separate published
  erratum is asserted.
- ARMS full original/correction access remains incomplete, so no ARMS mechanism is
  curated.
- The finite-dimensional gradient-proposal ratios are explicit specializations of
  the source Metropolis construction. Function-space theory has additional assumptions.
- No sampling experiment or benchmark was run and no universal convergence or performance
  claim is asserted.
- An initial sandboxed vendored-check failed to resolve the public host; the authorized
  network-enabled retry passed for all 22 immutable artifacts.
- All required checks passed. Repeated use of a paper is not independent evidence,
  and this review does not retire unrelated findings or establish discovery saturation.
tags:
- native-concepts
- mcmc
- rejection-sampling
- gaussian-priors
- primary-methods
- self-review
- discovery-ongoing
```
