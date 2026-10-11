# Scientific self-review of probabilistic inference methods

- Review: 20261011T065053Z-probabilistic-inference
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T06:49:49Z
- Finished UTC: 2026-10-11T06:50:53Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All six identities, supported mechanisms and related AIO mappings are retained in their stated scopes. No actionable record defect was found. Source access and algorithm-version limitations remain explicit; all records stay DRAFT.

## Scope And Provenance

Six maintained concepts covering Metropolis acceptance/proposals, Hamiltonian transitions, original slice NUTS and step-size warmup.

Selection: Exactly the six IDs in the probabilistic-inference discovery ledger; no sampling.
Coverage: full; 6 reviewed / 6 in the declared population.
Source: working_tree at Git base ac930ae96801f5fb2a5767861fccda52fe2e2dad.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:MetropolisHastings | data/curated/MetropolisHastings.yaml | maintained | Metropolis–Hastings sampling |
| AIMech:BarkerAcceptanceRule | data/curated/BarkerAcceptanceRule.yaml | maintained | Barker acceptance rule |
| AIMech:IndependenceMetropolisHastings | data/curated/IndependenceMetropolisHastings.yaml | maintained | Independence Metropolis–Hastings sampling |
| AIMech:HamiltonianMonteCarlo | data/curated/HamiltonianMonteCarlo.yaml | maintained | Hamiltonian Monte Carlo |
| AIMech:OriginalNoUTurnSampler | data/curated/OriginalNoUTurnSampler.yaml | maintained | No-U-Turn sampler (original slice formulation) |
| AIMech:DualAveragingHamiltonianStepSize | data/curated/DualAveragingHamiltonianStepSize.yaml | maintained | Dual-averaging step-size adaptation for Hamiltonian samplers |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:MetropolisHastings, AIMech:BarkerAcceptanceRule, AIMech:IndependenceMetropolisHastings, AIMech:HamiltonianMonteCarlo, AIMech:OriginalNoUTurnSampler, AIMech:DualAveragingHamiltonianStepSize | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate | passed | True | AIMech:MetropolisHastings, AIMech:BarkerAcceptanceRule, AIMech:IndependenceMetropolisHastings, AIMech:HamiltonianMonteCarlo, AIMech:OriginalNoUTurnSampler, AIMech:DualAveragingHamiltonianStepSize | Checked 442 record(s); 0 failed.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-curated | passed | True | AIMech:MetropolisHastings, AIMech:BarkerAcceptanceRule, AIMech:IndependenceMetropolisHastings, AIMech:HamiltonianMonteCarlo, AIMech:OriginalNoUTurnSampler, AIMech:DualAveragingHamiltonianStepSize | Checked 159 curated concept record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli seed --check | passed | True | AIMech:MetropolisHastings, AIMech:BarkerAcceptanceRule, AIMech:IndependenceMetropolisHastings, AIMech:HamiltonianMonteCarlo, AIMech:OriginalNoUTurnSampler, AIMech:DualAveragingHamiltonianStepSize | AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-history --base HEAD | passed | True | AIMech:MetropolisHastings, AIMech:BarkerAcceptanceRule, AIMech:IndependenceMetropolisHastings, AIMech:HamiltonianMonteCarlo, AIMech:OriginalNoUTurnSampler, AIMech:DualAveragingHamiltonianStepSize | Checked 32 history record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python scripts/record_review.py check | passed | True | AIMech:MetropolisHastings, AIMech:BarkerAcceptanceRule, AIMech:IndependenceMetropolisHastings, AIMech:HamiltonianMonteCarlo, AIMech:OriginalNoUTurnSampler, AIMech:DualAveragingHamiltonianStepSize | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 32,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class<br> |
| just check | passed | True | AIMech:MetropolisHastings, AIMech:BarkerAcceptanceRule, AIMech:IndependenceMetropolisHastings, AIMech:HamiltonianMonteCarlo, AIMech:OriginalNoUTurnSampler, AIMech:DualAveragingHamiltonianStepSize | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 42.42s<br>Checked 442 record(s); 0 failed.<br>Checked 159 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 32 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 32,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:MetropolisHastings, AIMech:BarkerAcceptanceRule, AIMech:IndependenceMetropolisHastings, AIMech:HamiltonianMonteCarlo, AIMech:OriginalNoUTurnSampler, AIMech:DualAveragingHamiltonianStepSize | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Method identity, acceptance or tuning mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:MetropolisHastings.

This record denotes the usual Metropolis acceptance choice within Hastings’s more general family of reversible updates. It is not the whole MCMC family, a Markov-chain model, the Barker acceptance rule or an independent-draw generator. Asymmetric proposals require the proposal-ratio correction. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 153 prior native IDs/names/aliases. Both checkout text searches included ignored and hidden files and returned no matches for the selected exact IDs, full labels, aliases and source titles. Existing HMM and Markov random field records describe probability models, not these sampling or tuning procedures.

The target must be proper, and the proposal and acceptance calculation must be defined on the relevant support. A proposed move with no reverse support has zero acceptance; zero-over-zero expressions are not a general operational rule. Target invariance does not ensure irreducibility, aperiodicity, rapid mixing, independent samples or convergence from every start. Those properties depend on the target and proposal. Rejections repeat the current state. Keeping only accepted moves without correcting their weighting changes the sampling process. Poor proposals, isolated modes, finite precision and inadequate run length can yield misleading estimates; acceptance rate alone does not establish adequate exploration. The record does not reproduce an implementation or assert a universal acceptance target, speed improvement or numerical posterior result.

### Method identity, acceptance or tuning mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:BarkerAcceptanceRule.

The record covers Hastings’s s_ij=1 form, which reduces to Barker’s 1965 rule for symmetric proposals. It is a scalar decision rule used inside a sampler, not a complete choice of proposal, a logistic-regression model, or the Metropolis min(1,R) rule. The original 1965 plasma paper was located but its full text has not been inspected for this record. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 153 prior native IDs/names/aliases. Both checkout text searches included ignored and hidden files and returned no matches for the selected exact IDs, full labels, aliases and source titles. Existing HMM and Markov random field records describe probability models, not these sampling or tuning procedures.

The asymmetric-proposal formula is an explicit algebraic restatement of Hastings’s general construction, not a claim that the inspected source is Barker’s original paper. The rule alone supplies neither a proposal distribution nor an ergodic or rapidly mixing chain. Support, boundary cases and numerical evaluation still require specification. The same ratio generally gives different acceptance probabilities under Barker and Metropolis rules. A lower or higher acceptance probability alone does not prove a universal computational-efficiency ordering. No claim is made about newer methods called Barker proposals or gradient-based Barker samplers; those can use different proposal mechanisms and need separate identity review.

### Method identity, acceptance or tuning mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:IndependenceMetropolisHastings.

Independence describes the proposal q(y), not independence of the retained Markov-chain states. This specializes Metropolis–Hastings and differs from estimating an expectation using separately weighted independent importance samples or from a state-centered random-walk proposal. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 153 prior native IDs/names/aliases. Both checkout text searches included ignored and hidden files and returned no matches for the selected exact IDs, full labels, aliases and source titles. Existing HMM and Markov random field records describe probability models, not these sampling or tuning procedures.

The proposal must cover the target support required for irreducibility, and its probability or density must be evaluable for the ratio. Independent candidates do not imply independent retained draws: rejection leaves the chain at the same state. The ratio shows why a state with very large pi(x)/g(x) can be hard to leave for ordinary candidates. This is an algebraic caution, not a measured mixing rate or a universal convergence theorem. Unweighted retained-chain averages and importance-weighted independent-sample estimates are different procedures. Validity still requires appropriate chain and integrability conditions. Adaptive or learned changing proposals are outside this fixed-proposal definition and require their own validity arguments.

### Method identity, acceptance or tuning mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:HamiltonianMonteCarlo.

The record describes conventional Euclidean HMC with Gaussian momenta, leapfrog integration and an end-of-trajectory Metropolis test. The source’s unit-mass baseline is explicit; fixed positive-definite mass matrices are documented in the author technical chapter. HMC is not deterministic optimization, an uncorrected molecular-dynamics simulation, or NUTS’s adaptive tree-selection kernel. The original 1987 publication’s metadata was verified, but its full text was inaccessible in this session. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 153 prior native IDs/names/aliases. Both checkout text searches included ignored and hidden files and returned no matches for the selected exact IDs, full labels, aliases and source titles. Existing HMM and Markov random field records describe probability models, not these sampling or tuning procedures.

The baseline needs evaluable log density and gradients on continuous coordinates. Discrete variables or constraints require additional handling; the stated algorithm does not directly solve those representation problems. Step size, trajectory length and coordinate scaling materially affect behavior. Too-large steps can cause integration failure or rejection, and too-short or resonant trajectories can explore poorly. Target invariance is not universal ergodicity or finite-sample convergence. Neal explicitly gives periodic trajectories that can cause nonergodicity. The correction does not remove Monte Carlo error or make floating-point dynamics exactly reversible in every implementation. Rejected positions remain part of the chain. No universal dimension-scaling law, tuned parameter value, benchmark superiority or current library default is asserted.

### Method identity, acceptance or tuning mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:OriginalNoUTurnSampler.

This record is restricted to Hoffman and Gelman’s 2014 slice formulation, principally efficient Algorithm 3. Algorithm 2 is its simpler uniform-selection derivation. The paper’s acronym NUTS is context, not an asserted exact alias for every later algorithm with that name. Dual-averaging step-size warmup is separable from the fixed-step-size NUTS transition. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 153 prior native IDs/names/aliases. Both checkout text searches included ignored and hidden files and returned no matches for the selected exact IDs, full labels, aliases and source titles. Existing HMM and Markov random field records describe probability models, not these sampling or tuning procedures.

Stopping one forward trajectory at its first U-turn without the paper’s balanced-tree construction and candidate exclusions is not the defined valid NUTS kernel. The source mechanism uses identity mass and its corresponding Euclidean dot-product criterion. Nonidentity or position-dependent metrics require an appropriate formulation; no generalized metric rule is inferred here. Eliminating a preset leapfrog-step count does not eliminate step size, numerical-divergence handling, model geometry, convergence assessment or implementation resource limits. The efficient top-level candidate transition and uniform selection within a subtree are different operations. Zero valid-candidate counts require guarded implementation; no literal zero-over-zero probability is asserted. This is not a specification of later multinomial NUTS or current Stan defaults. No author implementation was executed or performance result reproduced.

### Method identity, acceptance or tuning mechanism, limitations and AIO mapping

evidence: supported. Targets: AIMech:DualAveragingHamiltonianStepSize.

This is Hoffman and Gelman’s adaptation of dual averaging to HMC/NUTS step-size tuning. It is not the general Nesterov optimization algorithm, trajectory-length adaptation, mass-matrix estimation, or an acceptance test for retaining each NUTS output. The HMC and original NUTS acceptance statistics differ. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 153 prior native IDs/names/aliases. Both checkout text searches included ignored and hidden files and returned no matches for the selected exact IDs, full labels, aliases and source titles. Existing HMM and Markov random field records describe probability models, not these sampling or tuning procedures.

The convergence discussion assumes suitable regularity, including the relevant expected acceptance statistic decreasing with step size. The update formula alone does not prove convergence on every target. The target delta, warmup duration, initialization and shrinkage controls remain choices. The paper’s experimental defaults are not universal optimal values or current-library defaults. For NUTS the statistic averages potential HMC acceptances over explored states in the final doubling; it is not the proportion of returned positions that changed. Adapting throughout retained sampling requires a separate adaptive-MCMC argument. This record follows the paper’s finite-warmup/freeze practice. The procedure tunes epsilon, not a mass matrix or the complete distribution geometry, and does not guarantee independent samples or adequate posterior exploration.

### Invariant target versus independent or converged finite samples

scope: supported. Targets: AIMech:MetropolisHastings, AIMech:BarkerAcceptanceRule, AIMech:IndependenceMetropolisHastings, AIMech:HamiltonianMonteCarlo.

The acceptance ratios retain reverse-proposal factors, rejected states and target-support qualifications. The records do not turn detailed balance into unconditional mixing or convergence.

Barker R/(1+R) and independence min(1,w(y)/w(x)) are explicit algebraic substitutions in Hastings’s general construction. The independence property belongs to candidates, not retained states. HMC uses refreshed momenta and a corrected reversible volume-preserving proposal; the inspected author chapter provides a periodicity counterexample to unconditional ergodicity. Acceptance frequency alone is not treated as an efficiency or accuracy certificate.

### Balanced-tree sampling and acceptance-statistic adaptation are separate procedures

scope: supported. Targets: AIMech:OriginalNoUTurnSampler, AIMech:DualAveragingHamiltonianStepSize.

The original slice NUTS record preserves subtree stopping tests, slice restrictions and the distinction between uniform subtree representatives and the top-level count-ratio transition. Dual averaging tunes log step size from a defined statistic during warmup.

The naive Algorithm 2’s uniform final-set draw is not substituted for efficient Algorithm 3’s transition. A bad new half-tree is excluded while a U-turn only at the completed overall boundary can retain the new valid candidates. Zero candidate counts and numerical boundaries require guarded implementation. NUTS’s warmup statistic averages hypothetical HMC acceptance probabilities over the final doubling; it is not binary output acceptance. Finite warmup/freeze, regularity assumptions and version scope are explicit, with no assertion about current Stan defaults.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:MetropolisHastings, AIMech:BarkerAcceptanceRule, AIMech:IndependenceMetropolisHastings, AIMech:HamiltonianMonteCarlo, AIMech:OriginalNoUTurnSampler, AIMech:DualAveragingHamiltonianStepSize. Retain a general Metropolis–Hastings transition, an alternative scalar Barker rule, the fixed independent-proposal specialization, the Euclidean Hamiltonian proposal/correction algorithm, the original slice-based trajectory-tree sampler and its separable warmup adaptation. Specialization and shared components do not make these identities equivalent. The records do not equate methods with the AIO stochastic model.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T064909Z-probabilistic-inference.json | supports | No normalized match across all 442 AIO labels/scoped synonyms and 153 preceding native IDs/names/aliases. Both full-checkout fixed-string searches included ignored and hidden files and returned zero matches for selected exact IDs, full labels, aliases and source titles. Short acronyms were included in normalized identity comparison. The bounded phrase search does not establish absence of every related mention. Existing HiddenMarkovModel and MarkovRandomField YAMLs were inspected: they define probability models, not the new sampler/acceptance/tuning identities. |
| mapping | sources/aio/aio.json; Exact MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction CLASS definitions, synonyms and incident edges | supports | All six have a justified related_match to the exact MarkovChain CLASS, whose model definition, MC/MP/Markov Process synonyms, is_a Network edge and ProbabilisticHiddenLayer part edge were inspected. The relation is to the stochastic process constructed or tuned, not equivalence or subclass membership. Barker is a scalar rule and dual averaging a warmup procedure; their specific rationales avoid calling them Markov-chain models. BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction exact nodes/incident edges were also inspected. Graph-factorization models are not generic posterior samplers, and evaluating formulas does not equate a procedure to a generic mathematical function. The Barker rule could support a separate broad functional assessment, but no exhaustive mapping set is claimed. |
| existing-models | data/curated/HiddenMarkovModel.yaml; Definition and mechanism, alongside data/curated/MarkovRandomField.yaml | supports | The existing HMM and MRF records describe probabilistic models with hidden-state/emission or undirected-factor structures, rather than these posterior-sampling transitions, acceptance rules or tuning procedures. |
| metropolishastings-0 | https://probability.ca/hastings/hastings.pdf; Section 2.2, Equations (4)–(6), Metropolis choice of s_ij and continuous-density discussion, printed pp. 99–101 / PDF pp. 3–5 | supports | A Markov chain Monte Carlo algorithm that proposes a new state from a specified transition distribution and accepts it with the smaller of one and the target-density ratio multiplied by the reverse-to-forward proposal ratio, otherwise retaining the current state. Version: Biometrika 57(1), 1970, printed pp. 97–109; 13-page published scan hosted by probability.ca. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13. Attested visual pages: 2, 3, 4, 5, 7. |
| metropolishastings-1 | https://probability.ca/hastings/hastings.pdf; Sections 2.1 and 2.6, printed pp. 98–99 and 104–105 / PDF pp. 2–3 and 8–9 | supports | Hastings distinguishes invariance from practical error assessment: initial-state effects, correlated samples, incomplete exploration and inaccurate ratio calculations can undermine finite-run estimates. Version: Biometrika 57(1), 1970, printed pp. 97–109; 13-page published scan hosted by probability.ca. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13. Attested visual pages: 2, 3, 4, 5, 7. |
| barkeracceptancerule-0 | https://probability.ca/hastings/hastings.pdf; Section 2.2, Equation (6) and s_ij^(B)=1, with symmetric-proposal alpha_ij^(B), printed pp. 99–100 / PDF pp. 3–4 | supports | An acceptance-probability rule for reversible Monte Carlo proposals that uses R/(1+R), where R is the target-density ratio times the reverse-to-forward proposal ratio. Version: Biometrika 57(1), 1970, printed pp. 97–109; 13-page published scan hosted by probability.ca. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13. Attested visual pages: 2, 3, 4, 5, 7. |
| independencemetropolishastings-0 | https://probability.ca/hastings/hastings.pdf; Sections 2.2 and 2.5, Metropolis choice and final paragraph setting q_ij=pi_prime_j, printed pp. 99–101 and 103 / PDF pp. 3–5 and 7 | supports | A Metropolis–Hastings sampler whose proposal distribution is fixed independently of the current state, with proposal-density ratios still included in acceptance. Version: Biometrika 57(1), 1970, printed pp. 97–109; 13-page published scan hosted by probability.ca. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13. Attested visual pages: 2, 3, 4, 5, 7. |
| hamiltonianmontecarlo-0 | https://www.jmlr.org/papers/volume15/hoffman14a/hoffman14a.pdf; Section 2 and Algorithm 1, printed pp. 1594–1596 / PDF pp. 2–4 | supports | A Markov chain Monte Carlo algorithm for differentiable continuous targets that augments positions with momenta, proposes a state through reversible volume-preserving numerical Hamiltonian dynamics, and applies a Metropolis correction for the Hamiltonian change. Version: JMLR 15(47), 2014, printed pp. 1593–1623; 31-page published PDF. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29. Attested visual pages: 3, 9, 11, 14, 15, 17, 18, 19. |
| hamiltonianmontecarlo-1 | https://arxiv.org/pdf/1206.1901v1; Sections 2.1, 2.3 and 3.1–3.2, Equations (2.5)–(2.8), (2.28)–(2.30), (3.6), Figure 2 and Ergodicity of HMC, PDF/printed pp. 3–4, 8, 10–15 | supports | Neal’s author-posted technical chapter defines fixed Gaussian mass matrices, the full-refresh leapfrog/Metropolis algorithm, its invariant-distribution argument, and periodicity failures of ergodicity. It is a methodological review and implementation description, not the original 1987 invention paper. Version: arXiv:1206.1901v1, submitted 2012-06-09; author-posted version of 2011 Handbook of Markov Chain Monte Carlo chapter 5; 51 pages. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16. Attested visual pages: 12. |
| originalnouturnsampler-0 | https://www.jmlr.org/papers/volume15/hoffman14a/hoffman14a.pdf; Sections 3.1.1–3.1.2, conditions C.1–C.4, Equations (3)–(4), Algorithms 2–3 and transition kernel T, printed pp. 1597–1606 / PDF pp. 5–14 | supports | The original 2014 slice-based NUTS algorithm, which adapts a Hamiltonian trajectory’s length through randomly directed binary-tree doubling and selects a valid next state while enforcing subtree U-turn and reversibility conditions. Version: JMLR 15(47), 2014, printed pp. 1593–1623; 31-page published PDF. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29. Attested visual pages: 3, 9, 11, 14, 15, 17, 18, 19. |
| originalnouturnsampler-1 | https://www.jmlr.org/papers/volume15/hoffman14a/hoffman14a.pdf; Section 5, printed pp. 1619–1620 / PDF pp. 27–28 | supports | The paper limits direct use to differentiable continuous coordinates, discusses transformations and separate treatment of discrete variables, and identifies mass-matrix changes as extensions rather than the unit-mass formulation itself. Version: JMLR 15(47), 2014, printed pp. 1593–1623; 31-page published PDF. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29. Attested visual pages: 3, 9, 11, 14, 15, 17, 18, 19. |
| dualaveraginghamiltonianstepsize-0 | https://www.jmlr.org/papers/volume15/hoffman14a/hoffman14a.pdf; Sections 3.2–3.2.4, Equations (5)–(6) and Algorithms 5–6, printed pp. 1605–1611 / PDF pp. 13–19 | supports | A warmup procedure that tunes the logarithm of a Hamiltonian sampler’s integration step size using cumulative discrepancy from a target acceptance statistic, a shrinkage point and a smoothed sequence of iterates. Version: JMLR 15(47), 2014, printed pp. 1593–1623; 31-page published PDF. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29. Attested visual pages: 3, 9, 11, 14, 15, 17, 18, 19. |

## Limits And Additional Notes

- Adversarial author self-review only; all six records remain DRAFT.
- The original 1987 HMC full text was not inspected. Neal is honestly identified as an author-posted methodological chapter/review, with its own complete algorithm and implementation description, rather than the original invention paper.
- The record mechanisms use the inspected Hastings and NUTS primary method passages. Related original or later sources found only through search remain uninspected leads.
- The curated NUTS definition covers the original 2014 slice formulation, not all later algorithms called NUTS.
- No universal ergodicity, finite-sample convergence, independent retained-draw or performance claim is asserted.
- No sampler or model was run. Algebraic ratio restatements were checked against the visually inspected equations without claiming an empirical replication.
- Repeated passages from one publication are not independent studies. Only declared text/visual pages were inspected.
- All required checks passed; the assessment covers these six targets and does not retire unrelated findings or establish discovery saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T065053Z-probabilistic-inference
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of probabilistic inference methods
started_at: '2026-10-11T06:49:49Z'
finished_at: '2026-10-11T06:50:53Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all six records against
    the inspected source equations, pseudocode and mapping definitions. No independent
    reviewer or approval is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All six identities, supported mechanisms and related AIO mappings are retained
  in their stated scopes. No actionable record defect was found. Source access and
  algorithm-version limitations remain explicit; all records stay DRAFT.
source:
  git_revision: ac930ae96801f5fb2a5767861fccda52fe2e2dad
  state: working_tree
  inputs:
  - path: data/curated/BarkerAcceptanceRule.yaml
    sha256: e81a763ba4f2eb2c7e51f3e520311bd111d269f45cdf2417055d72a4ddd4d08c
    role: target
  - path: data/curated/DualAveragingHamiltonianStepSize.yaml
    sha256: f140c7da7a288509d8c6afe961ad0d5f2913c52afad65452fe40cd7adedfb319
    role: target
  - path: data/curated/HamiltonianMonteCarlo.yaml
    sha256: 28367594dbc36a8357c33a4e639aeb0fefdd47adc8c46e2b3d5feb96b67e84ca
    role: target
  - path: data/curated/HiddenMarkovModel.yaml
    sha256: 062a31bd525cb90e8077d4889c177f55cb7b29dea4e71c33be95bae9e72a5240
    role: context
  - path: data/curated/IndependenceMetropolisHastings.yaml
    sha256: ca1390f00edca43e94f897e2398b3f7d8edddefadc0a5780e0b470816a7754df
    role: target
  - path: data/curated/MarkovRandomField.yaml
    sha256: 03b1f2a66b2183a5bf5943bee7ec0619b9e07947d6c9187263e279ee475f9149
    role: context
  - path: data/curated/MetropolisHastings.yaml
    sha256: 01cb22a25242e8564e2a7bb839ecb46da1bc49eb09b3c85200f9a596e05b99b4
    role: target
  - path: data/curated/OriginalNoUTurnSampler.yaml
    sha256: e5a5c064ad5ee6b2ff8c75a9e8422e82cd8f9a396302e333018853d8c15599a1
    role: target
  - path: research/discovery/20261011T064909Z-probabilistic-inference.json
    sha256: 0853cb97396f886c38743c19681745ada369a6b864865d04cc5ba088d8e6568e
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
- target_id: AIMech:MetropolisHastings
  path: data/curated/MetropolisHastings.yaml
  label: Metropolis–Hastings sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MetropolisHastings.yaml
    role: maintained_record
- target_id: AIMech:BarkerAcceptanceRule
  path: data/curated/BarkerAcceptanceRule.yaml
  label: Barker acceptance rule
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BarkerAcceptanceRule.yaml
    role: maintained_record
- target_id: AIMech:IndependenceMetropolisHastings
  path: data/curated/IndependenceMetropolisHastings.yaml
  label: Independence Metropolis–Hastings sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IndependenceMetropolisHastings.yaml
    role: maintained_record
- target_id: AIMech:HamiltonianMonteCarlo
  path: data/curated/HamiltonianMonteCarlo.yaml
  label: Hamiltonian Monte Carlo
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HamiltonianMonteCarlo.yaml
    role: maintained_record
- target_id: AIMech:OriginalNoUTurnSampler
  path: data/curated/OriginalNoUTurnSampler.yaml
  label: No-U-Turn sampler (original slice formulation)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OriginalNoUTurnSampler.yaml
    role: maintained_record
- target_id: AIMech:DualAveragingHamiltonianStepSize
  path: data/curated/DualAveragingHamiltonianStepSize.yaml
  label: Dual-averaging step-size adaptation for Hamiltonian samplers
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DualAveragingHamiltonianStepSize.yaml
    role: maintained_record
scope:
  description: Six maintained concepts covering Metropolis acceptance/proposals, Hamiltonian
    transitions, original slice NUTS and step-size warmup.
  selection: Exactly the six IDs in the probabilistic-inference discovery ledger;
    no sampling.
  coverage: full
  population_size: 6
  reviewed_target_ids:
  - AIMech:MetropolisHastings
  - AIMech:BarkerAcceptanceRule
  - AIMech:IndependenceMetropolisHastings
  - AIMech:HamiltonianMonteCarlo
  - AIMech:OriginalNoUTurnSampler
  - AIMech:DualAveragingHamiltonianStepSize
  exclusions:
  - target: Original Duane et al. 1987 HMC full text
    reason: Attempted hosts returned an access challenge or 403. Historical metadata
      was verified; the maintained HMC mechanism relies on other explicitly inspected
      sources.
  - target: Original Barker 1965 paper, Tierney manuscript, later multinomial NUTS
      and other newly discovered variants
    reason: These remain source or concept leads pending full-method inspection, not
      evidence silently imported into the present mechanisms.
  - target: Sampler execution and numerical benchmark reproduction
    reason: No author implementation, model fit or simulation was executed.
checks:
- check_id: required-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:MetropolisHastings
  - AIMech:BarkerAcceptanceRule
  - AIMech:IndependenceMetropolisHastings
  - AIMech:HamiltonianMonteCarlo
  - AIMech:OriginalNoUTurnSampler
  - AIMech:DualAveragingHamiltonianStepSize
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
  - AIMech:MetropolisHastings
  - AIMech:BarkerAcceptanceRule
  - AIMech:IndependenceMetropolisHastings
  - AIMech:HamiltonianMonteCarlo
  - AIMech:OriginalNoUTurnSampler
  - AIMech:DualAveragingHamiltonianStepSize
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
  - AIMech:MetropolisHastings
  - AIMech:BarkerAcceptanceRule
  - AIMech:IndependenceMetropolisHastings
  - AIMech:HamiltonianMonteCarlo
  - AIMech:OriginalNoUTurnSampler
  - AIMech:DualAveragingHamiltonianStepSize
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 159 curated concept record(s); 0 error(s).

    '
- check_id: required-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:MetropolisHastings
  - AIMech:BarkerAcceptanceRule
  - AIMech:IndependenceMetropolisHastings
  - AIMech:HamiltonianMonteCarlo
  - AIMech:OriginalNoUTurnSampler
  - AIMech:DualAveragingHamiltonianStepSize
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
  - AIMech:MetropolisHastings
  - AIMech:BarkerAcceptanceRule
  - AIMech:IndependenceMetropolisHastings
  - AIMech:HamiltonianMonteCarlo
  - AIMech:OriginalNoUTurnSampler
  - AIMech:DualAveragingHamiltonianStepSize
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 32 history record(s); 0 error(s).

    '
- check_id: required-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:MetropolisHastings
  - AIMech:BarkerAcceptanceRule
  - AIMech:IndependenceMetropolisHastings
  - AIMech:HamiltonianMonteCarlo
  - AIMech:OriginalNoUTurnSampler
  - AIMech:DualAveragingHamiltonianStepSize
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 32,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\ntopClass is deprecated - use top_class\n"
- check_id: required-6
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:MetropolisHastings
  - AIMech:BarkerAcceptanceRule
  - AIMech:IndependenceMetropolisHastings
  - AIMech:HamiltonianMonteCarlo
  - AIMech:OriginalNoUTurnSampler
  - AIMech:DualAveragingHamiltonianStepSize
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 42.42s\nChecked 442 record(s); 0 failed.\n\
    Checked 159 curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing,\
    \ 0 changed, 0 unexpected.\nChecked 32 history record(s); 0 error(s).\n{\n  \"\
    repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 32,\n  \"coverage\"\
    : \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-7
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:MetropolisHastings
  - AIMech:BarkerAcceptanceRule
  - AIMech:IndependenceMetropolisHastings
  - AIMech:HamiltonianMonteCarlo
  - AIMech:OriginalNoUTurnSampler
  - AIMech:DualAveragingHamiltonianStepSize
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T064909Z-probabilistic-inference.json
  accessed_at: '2026-10-11T06:49:49Z'
  support: supports
  summary: 'No normalized match across all 442 AIO labels/scoped synonyms and 153
    preceding native IDs/names/aliases. Both full-checkout fixed-string searches included
    ignored and hidden files and returned zero matches for selected exact IDs, full
    labels, aliases and source titles. Short acronyms were included in normalized
    identity comparison. The bounded phrase search does not establish absence of every
    related mention. Existing HiddenMarkovModel and MarkovRandomField YAMLs were inspected:
    they define probability models, not the new sampler/acceptance/tuning identities.'
  search_scope: All 442 pinned AIO labels/scoped synonyms and 153 preceding native
    IDs/names/aliases; both updated checkouts with ignored and hidden files included.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Exact MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction
    CLASS definitions, synonyms and incident edges
  accessed_at: '2026-10-11T06:49:49Z'
  support: supports
  summary: All six have a justified related_match to the exact MarkovChain CLASS,
    whose model definition, MC/MP/Markov Process synonyms, is_a Network edge and ProbabilisticHiddenLayer
    part edge were inspected. The relation is to the stochastic process constructed
    or tuned, not equivalence or subclass membership. Barker is a scalar rule and
    dual averaging a warmup procedure; their specific rationales avoid calling them
    Markov-chain models. BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction
    exact nodes/incident edges were also inspected. Graph-factorization models are
    not generic posterior samplers, and evaluating formulas does not equate a procedure
    to a generic mathematical function. The Barker rule could support a separate broad
    functional assessment, but no exhaustive mapping set is claimed.
- evidence_id: existing-models
  kind: record_content
  reference: data/curated/HiddenMarkovModel.yaml
  locator: Definition and mechanism, alongside data/curated/MarkovRandomField.yaml
  accessed_at: '2026-10-11T06:49:49Z'
  support: supports
  summary: The existing HMM and MRF records describe probabilistic models with hidden-state/emission
    or undirected-factor structures, rather than these posterior-sampling transitions,
    acceptance rules or tuning procedures.
- evidence_id: metropolishastings-0
  kind: primary_source
  reference: https://probability.ca/hastings/hastings.pdf
  locator: Section 2.2, Equations (4)–(6), Metropolis choice of s_ij and continuous-density
    discussion, printed pp. 99–101 / PDF pp. 3–5
  accessed_at: '2026-10-11T06:40:06Z'
  snapshot_sha256: dc620d3651d30029729646649e9a26780f1a415d7fd251433b6a270a143de47c
  support: supports
  summary: 'A Markov chain Monte Carlo algorithm that proposes a new state from a
    specified transition distribution and accepts it with the smaller of one and the
    target-density ratio multiplied by the reverse-to-forward proposal ratio, otherwise
    retaining the current state. Version: Biometrika 57(1), 1970, printed pp. 97–109;
    13-page published scan hosted by probability.ca. Attested PDF text pages: 1, 2,
    3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13. Attested visual pages: 2, 3, 4, 5, 7.'
- evidence_id: metropolishastings-1
  kind: primary_source
  reference: https://probability.ca/hastings/hastings.pdf
  locator: Sections 2.1 and 2.6, printed pp. 98–99 and 104–105 / PDF pp. 2–3 and 8–9
  accessed_at: '2026-10-11T06:40:06Z'
  snapshot_sha256: dc620d3651d30029729646649e9a26780f1a415d7fd251433b6a270a143de47c
  support: supports
  summary: 'Hastings distinguishes invariance from practical error assessment: initial-state
    effects, correlated samples, incomplete exploration and inaccurate ratio calculations
    can undermine finite-run estimates. Version: Biometrika 57(1), 1970, printed pp.
    97–109; 13-page published scan hosted by probability.ca. Attested PDF text pages:
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13. Attested visual pages: 2, 3, 4, 5,
    7.'
- evidence_id: barkeracceptancerule-0
  kind: primary_source
  reference: https://probability.ca/hastings/hastings.pdf
  locator: Section 2.2, Equation (6) and s_ij^(B)=1, with symmetric-proposal alpha_ij^(B),
    printed pp. 99–100 / PDF pp. 3–4
  accessed_at: '2026-10-11T06:40:06Z'
  snapshot_sha256: dc620d3651d30029729646649e9a26780f1a415d7fd251433b6a270a143de47c
  support: supports
  summary: 'An acceptance-probability rule for reversible Monte Carlo proposals that
    uses R/(1+R), where R is the target-density ratio times the reverse-to-forward
    proposal ratio. Version: Biometrika 57(1), 1970, printed pp. 97–109; 13-page published
    scan hosted by probability.ca. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8,
    9, 10, 11, 12, 13. Attested visual pages: 2, 3, 4, 5, 7.'
- evidence_id: independencemetropolishastings-0
  kind: primary_source
  reference: https://probability.ca/hastings/hastings.pdf
  locator: Sections 2.2 and 2.5, Metropolis choice and final paragraph setting q_ij=pi_prime_j,
    printed pp. 99–101 and 103 / PDF pp. 3–5 and 7
  accessed_at: '2026-10-11T06:40:06Z'
  snapshot_sha256: dc620d3651d30029729646649e9a26780f1a415d7fd251433b6a270a143de47c
  support: supports
  summary: 'A Metropolis–Hastings sampler whose proposal distribution is fixed independently
    of the current state, with proposal-density ratios still included in acceptance.
    Version: Biometrika 57(1), 1970, printed pp. 97–109; 13-page published scan hosted
    by probability.ca. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    12, 13. Attested visual pages: 2, 3, 4, 5, 7.'
- evidence_id: hamiltonianmontecarlo-0
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume15/hoffman14a/hoffman14a.pdf
  locator: Section 2 and Algorithm 1, printed pp. 1594–1596 / PDF pp. 2–4
  accessed_at: '2026-10-11T06:40:05Z'
  snapshot_sha256: bf2a5592015b6637fe5adaa26d3c8a11871d96c3cb7f41da0aa7d96b9ec1e086
  support: supports
  summary: 'A Markov chain Monte Carlo algorithm for differentiable continuous targets
    that augments positions with momenta, proposes a state through reversible volume-preserving
    numerical Hamiltonian dynamics, and applies a Metropolis correction for the Hamiltonian
    change. Version: JMLR 15(47), 2014, printed pp. 1593–1623; 31-page published PDF.
    Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    17, 18, 19, 20, 27, 28, 29. Attested visual pages: 3, 9, 11, 14, 15, 17, 18, 19.'
- evidence_id: hamiltonianmontecarlo-1
  kind: primary_source
  reference: https://arxiv.org/pdf/1206.1901v1
  locator: Sections 2.1, 2.3 and 3.1–3.2, Equations (2.5)–(2.8), (2.28)–(2.30), (3.6),
    Figure 2 and Ergodicity of HMC, PDF/printed pp. 3–4, 8, 10–15
  accessed_at: '2026-10-11T06:40:05Z'
  snapshot_sha256: 0582743db6913dd05ef7204a76fcd041fffdd86a7ca6c9580fb0fd5fdbf19f13
  support: supports
  summary: 'Neal’s author-posted technical chapter defines fixed Gaussian mass matrices,
    the full-refresh leapfrog/Metropolis algorithm, its invariant-distribution argument,
    and periodicity failures of ergodicity. It is a methodological review and implementation
    description, not the original 1987 invention paper. Version: arXiv:1206.1901v1,
    submitted 2012-06-09; author-posted version of 2011 Handbook of Markov Chain Monte
    Carlo chapter 5; 51 pages. Attested PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9,
    10, 11, 12, 13, 14, 15, 16. Attested visual pages: 12.'
- evidence_id: originalnouturnsampler-0
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume15/hoffman14a/hoffman14a.pdf
  locator: Sections 3.1.1–3.1.2, conditions C.1–C.4, Equations (3)–(4), Algorithms
    2–3 and transition kernel T, printed pp. 1597–1606 / PDF pp. 5–14
  accessed_at: '2026-10-11T06:40:05Z'
  snapshot_sha256: bf2a5592015b6637fe5adaa26d3c8a11871d96c3cb7f41da0aa7d96b9ec1e086
  support: supports
  summary: 'The original 2014 slice-based NUTS algorithm, which adapts a Hamiltonian
    trajectory’s length through randomly directed binary-tree doubling and selects
    a valid next state while enforcing subtree U-turn and reversibility conditions.
    Version: JMLR 15(47), 2014, printed pp. 1593–1623; 31-page published PDF. Attested
    PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 27, 28, 29. Attested visual pages: 3, 9, 11, 14, 15, 17, 18, 19.'
- evidence_id: originalnouturnsampler-1
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume15/hoffman14a/hoffman14a.pdf
  locator: Section 5, printed pp. 1619–1620 / PDF pp. 27–28
  accessed_at: '2026-10-11T06:40:05Z'
  snapshot_sha256: bf2a5592015b6637fe5adaa26d3c8a11871d96c3cb7f41da0aa7d96b9ec1e086
  support: supports
  summary: 'The paper limits direct use to differentiable continuous coordinates,
    discusses transformations and separate treatment of discrete variables, and identifies
    mass-matrix changes as extensions rather than the unit-mass formulation itself.
    Version: JMLR 15(47), 2014, printed pp. 1593–1623; 31-page published PDF. Attested
    PDF text pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 27, 28, 29. Attested visual pages: 3, 9, 11, 14, 15, 17, 18, 19.'
- evidence_id: dualaveraginghamiltonianstepsize-0
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume15/hoffman14a/hoffman14a.pdf
  locator: Sections 3.2–3.2.4, Equations (5)–(6) and Algorithms 5–6, printed pp. 1605–1611
    / PDF pp. 13–19
  accessed_at: '2026-10-11T06:40:05Z'
  snapshot_sha256: bf2a5592015b6637fe5adaa26d3c8a11871d96c3cb7f41da0aa7d96b9ec1e086
  support: supports
  summary: 'A warmup procedure that tunes the logarithm of a Hamiltonian sampler’s
    integration step size using cumulative discrepancy from a target acceptance statistic,
    a shrinkage point and a smoothed sequence of iterates. Version: JMLR 15(47), 2014,
    printed pp. 1593–1623; 31-page published PDF. Attested PDF text pages: 1, 2, 3,
    4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29. Attested
    visual pages: 3, 9, 11, 14, 15, 17, 18, 19.'
assessments:
- assessment_id: metropolishastings
  area: evidence
  topic: Method identity, acceptance or tuning mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:MetropolisHastings
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - metropolishastings-0
  - metropolishastings-1
  summary: This record denotes the usual Metropolis acceptance choice within Hastings’s
    more general family of reversible updates. It is not the whole MCMC family, a
    Markov-chain model, the Barker acceptance rule or an independent-draw generator.
    Asymmetric proposals require the proposal-ratio correction. No normalized identity
    match was found across all 442 pinned AIO labels/scoped synonyms and 153 prior
    native IDs/names/aliases. Both checkout text searches included ignored and hidden
    files and returned no matches for the selected exact IDs, full labels, aliases
    and source titles. Existing HMM and Markov random field records describe probability
    models, not these sampling or tuning procedures.
  details: The target must be proper, and the proposal and acceptance calculation
    must be defined on the relevant support. A proposed move with no reverse support
    has zero acceptance; zero-over-zero expressions are not a general operational
    rule. Target invariance does not ensure irreducibility, aperiodicity, rapid mixing,
    independent samples or convergence from every start. Those properties depend on
    the target and proposal. Rejections repeat the current state. Keeping only accepted
    moves without correcting their weighting changes the sampling process. Poor proposals,
    isolated modes, finite precision and inadequate run length can yield misleading
    estimates; acceptance rate alone does not establish adequate exploration. The
    record does not reproduce an implementation or assert a universal acceptance target,
    speed improvement or numerical posterior result.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: Five procedures are algorithms; Barker acceptance is a mathematical
      decision rule within a sampler. None is a trained model instance or a finite-run
      empirical result.
    evidence_ids:
    - metropolishastings-0
    - metropolishastings-1
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This procedure constructs transitions of a Markov chain to sample
      a specified target distribution. The exact AIO CLASS describes a stochastic
      process/model with dependence on the preceding state and is exported beneath
      Network. The method-to-process relationship is related_match, not equivalence,
      subclass membership or a claim that the sampler is a trained network.
    evidence_ids:
    - mapping
    - identity
- assessment_id: barkeracceptancerule
  area: evidence
  topic: Method identity, acceptance or tuning mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:BarkerAcceptanceRule
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - barkeracceptancerule-0
  summary: The record covers Hastings’s s_ij=1 form, which reduces to Barker’s 1965
    rule for symmetric proposals. It is a scalar decision rule used inside a sampler,
    not a complete choice of proposal, a logistic-regression model, or the Metropolis
    min(1,R) rule. The original 1965 plasma paper was located but its full text has
    not been inspected for this record. No normalized identity match was found across
    all 442 pinned AIO labels/scoped synonyms and 153 prior native IDs/names/aliases.
    Both checkout text searches included ignored and hidden files and returned no
    matches for the selected exact IDs, full labels, aliases and source titles. Existing
    HMM and Markov random field records describe probability models, not these sampling
    or tuning procedures.
  details: The asymmetric-proposal formula is an explicit algebraic restatement of
    Hastings’s general construction, not a claim that the inspected source is Barker’s
    original paper. The rule alone supplies neither a proposal distribution nor an
    ergodic or rapidly mixing chain. Support, boundary cases and numerical evaluation
    still require specification. The same ratio generally gives different acceptance
    probabilities under Barker and Metropolis rules. A lower or higher acceptance
    probability alone does not prove a universal computational-efficiency ordering.
    No claim is made about newer methods called Barker proposals or gradient-based
    Barker samplers; those can use different proposal mechanisms and need separate
    identity review.
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: Five procedures are algorithms; Barker acceptance is a mathematical
      decision rule within a sampler. None is a trained model instance or a finite-run
      empirical result.
    evidence_ids:
    - barkeracceptancerule-0
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The acceptance rule constructs target-invariant Markov transitions
      when paired with a proposal and rejection self-transition. AIO MarkovChain describes
      the stochastic process/model, not this scalar acceptance function. This is a
      rule-to-process related match, not equivalence or an is-a assertion.
    evidence_ids:
    - mapping
    - identity
- assessment_id: independencemetropolishastings
  area: evidence
  topic: Method identity, acceptance or tuning mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:IndependenceMetropolisHastings
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - independencemetropolishastings-0
  summary: Independence describes the proposal q(y), not independence of the retained
    Markov-chain states. This specializes Metropolis–Hastings and differs from estimating
    an expectation using separately weighted independent importance samples or from
    a state-centered random-walk proposal. No normalized identity match was found
    across all 442 pinned AIO labels/scoped synonyms and 153 prior native IDs/names/aliases.
    Both checkout text searches included ignored and hidden files and returned no
    matches for the selected exact IDs, full labels, aliases and source titles. Existing
    HMM and Markov random field records describe probability models, not these sampling
    or tuning procedures.
  details: 'The proposal must cover the target support required for irreducibility,
    and its probability or density must be evaluable for the ratio. Independent candidates
    do not imply independent retained draws: rejection leaves the chain at the same
    state. The ratio shows why a state with very large pi(x)/g(x) can be hard to leave
    for ordinary candidates. This is an algebraic caution, not a measured mixing rate
    or a universal convergence theorem. Unweighted retained-chain averages and importance-weighted
    independent-sample estimates are different procedures. Validity still requires
    appropriate chain and integrability conditions. Adaptive or learned changing proposals
    are outside this fixed-proposal definition and require their own validity arguments.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: Five procedures are algorithms; Barker acceptance is a mathematical
      decision rule within a sampler. None is a trained model instance or a finite-run
      empirical result.
    evidence_ids:
    - independencemetropolishastings-0
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This procedure constructs transitions of a Markov chain to sample
      a specified target distribution. The exact AIO CLASS describes a stochastic
      process/model with dependence on the preceding state and is exported beneath
      Network. The method-to-process relationship is related_match, not equivalence,
      subclass membership or a claim that the sampler is a trained network.
    evidence_ids:
    - mapping
    - identity
- assessment_id: hamiltonianmontecarlo
  area: evidence
  topic: Method identity, acceptance or tuning mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:HamiltonianMonteCarlo
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - hamiltonianmontecarlo-0
  - hamiltonianmontecarlo-1
  summary: The record describes conventional Euclidean HMC with Gaussian momenta,
    leapfrog integration and an end-of-trajectory Metropolis test. The source’s unit-mass
    baseline is explicit; fixed positive-definite mass matrices are documented in
    the author technical chapter. HMC is not deterministic optimization, an uncorrected
    molecular-dynamics simulation, or NUTS’s adaptive tree-selection kernel. The original
    1987 publication’s metadata was verified, but its full text was inaccessible in
    this session. No normalized identity match was found across all 442 pinned AIO
    labels/scoped synonyms and 153 prior native IDs/names/aliases. Both checkout text
    searches included ignored and hidden files and returned no matches for the selected
    exact IDs, full labels, aliases and source titles. Existing HMM and Markov random
    field records describe probability models, not these sampling or tuning procedures.
  details: The baseline needs evaluable log density and gradients on continuous coordinates.
    Discrete variables or constraints require additional handling; the stated algorithm
    does not directly solve those representation problems. Step size, trajectory length
    and coordinate scaling materially affect behavior. Too-large steps can cause integration
    failure or rejection, and too-short or resonant trajectories can explore poorly.
    Target invariance is not universal ergodicity or finite-sample convergence. Neal
    explicitly gives periodic trajectories that can cause nonergodicity. The correction
    does not remove Monte Carlo error or make floating-point dynamics exactly reversible
    in every implementation. Rejected positions remain part of the chain. No universal
    dimension-scaling law, tuned parameter value, benchmark superiority or current
    library default is asserted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: Five procedures are algorithms; Barker acceptance is a mathematical
      decision rule within a sampler. None is a trained model instance or a finite-run
      empirical result.
    evidence_ids:
    - hamiltonianmontecarlo-0
    - hamiltonianmontecarlo-1
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This procedure constructs transitions of a Markov chain to sample
      a specified target distribution. The exact AIO CLASS describes a stochastic
      process/model with dependence on the preceding state and is exported beneath
      Network. The method-to-process relationship is related_match, not equivalence,
      subclass membership or a claim that the sampler is a trained network.
    evidence_ids:
    - mapping
    - identity
- assessment_id: originalnouturnsampler
  area: evidence
  topic: Method identity, acceptance or tuning mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:OriginalNoUTurnSampler
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - originalnouturnsampler-0
  - originalnouturnsampler-1
  summary: This record is restricted to Hoffman and Gelman’s 2014 slice formulation,
    principally efficient Algorithm 3. Algorithm 2 is its simpler uniform-selection
    derivation. The paper’s acronym NUTS is context, not an asserted exact alias for
    every later algorithm with that name. Dual-averaging step-size warmup is separable
    from the fixed-step-size NUTS transition. No normalized identity match was found
    across all 442 pinned AIO labels/scoped synonyms and 153 prior native IDs/names/aliases.
    Both checkout text searches included ignored and hidden files and returned no
    matches for the selected exact IDs, full labels, aliases and source titles. Existing
    HMM and Markov random field records describe probability models, not these sampling
    or tuning procedures.
  details: Stopping one forward trajectory at its first U-turn without the paper’s
    balanced-tree construction and candidate exclusions is not the defined valid NUTS
    kernel. The source mechanism uses identity mass and its corresponding Euclidean
    dot-product criterion. Nonidentity or position-dependent metrics require an appropriate
    formulation; no generalized metric rule is inferred here. Eliminating a preset
    leapfrog-step count does not eliminate step size, numerical-divergence handling,
    model geometry, convergence assessment or implementation resource limits. The
    efficient top-level candidate transition and uniform selection within a subtree
    are different operations. Zero valid-candidate counts require guarded implementation;
    no literal zero-over-zero probability is asserted. This is not a specification
    of later multinomial NUTS or current Stan defaults. No author implementation was
    executed or performance result reproduced.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: Five procedures are algorithms; Barker acceptance is a mathematical
      decision rule within a sampler. None is a trained model instance or a finite-run
      empirical result.
    evidence_ids:
    - originalnouturnsampler-0
    - originalnouturnsampler-1
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This procedure constructs transitions of a Markov chain to sample
      a specified target distribution. The exact AIO CLASS describes a stochastic
      process/model with dependence on the preceding state and is exported beneath
      Network. The method-to-process relationship is related_match, not equivalence,
      subclass membership or a claim that the sampler is a trained network.
    evidence_ids:
    - mapping
    - identity
- assessment_id: dualaveraginghamiltonianstepsize
  area: evidence
  topic: Method identity, acceptance or tuning mechanism, limitations and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:DualAveragingHamiltonianStepSize
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - dualaveraginghamiltonianstepsize-0
  summary: This is Hoffman and Gelman’s adaptation of dual averaging to HMC/NUTS step-size
    tuning. It is not the general Nesterov optimization algorithm, trajectory-length
    adaptation, mass-matrix estimation, or an acceptance test for retaining each NUTS
    output. The HMC and original NUTS acceptance statistics differ. No normalized
    identity match was found across all 442 pinned AIO labels/scoped synonyms and
    153 prior native IDs/names/aliases. Both checkout text searches included ignored
    and hidden files and returned no matches for the selected exact IDs, full labels,
    aliases and source titles. Existing HMM and Markov random field records describe
    probability models, not these sampling or tuning procedures.
  details: The convergence discussion assumes suitable regularity, including the relevant
    expected acceptance statistic decreasing with step size. The update formula alone
    does not prove convergence on every target. The target delta, warmup duration,
    initialization and shrinkage controls remain choices. The paper’s experimental
    defaults are not universal optimal values or current-library defaults. For NUTS
    the statistic averages potential HMC acceptances over explored states in the final
    doubling; it is not the proportion of returned positions that changed. Adapting
    throughout retained sampling requires a separate adaptive-MCMC argument. This
    record follows the paper’s finite-warmup/freeze practice. The procedure tunes
    epsilon, not a mass matrix or the complete distribution geometry, and does not
    guarantee independent samples or adequate posterior exploration.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: Five procedures are algorithms; Barker acceptance is a mathematical
      decision rule within a sampler. None is a trained model instance or a finite-run
      empirical result.
    evidence_ids:
    - dualaveraginghamiltonianstepsize-0
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The procedure tunes the integration step size used by a Markov-chain
      sampler during warmup, after which the fixed sampling transition is used. AIO
      MarkovChain describes the stochastic process/model, not its tuning procedure.
      The relation does not assert that a history-adaptive warmup sequence itself
      is a homogeneous Markov chain on positions alone.
    evidence_ids:
    - mapping
    - identity
- assessment_id: invariance-and-sampling
  area: scope
  topic: Invariant target versus independent or converged finite samples
  outcome: supported
  target_ids:
  - AIMech:MetropolisHastings
  - AIMech:BarkerAcceptanceRule
  - AIMech:IndependenceMetropolisHastings
  - AIMech:HamiltonianMonteCarlo
  evidence_ids:
  - metropolishastings-0
  - metropolishastings-1
  - barkeracceptancerule-0
  - independencemetropolishastings-0
  - hamiltonianmontecarlo-0
  - hamiltonianmontecarlo-1
  summary: The acceptance ratios retain reverse-proposal factors, rejected states
    and target-support qualifications. The records do not turn detailed balance into
    unconditional mixing or convergence.
  details: Barker R/(1+R) and independence min(1,w(y)/w(x)) are explicit algebraic
    substitutions in Hastings’s general construction. The independence property belongs
    to candidates, not retained states. HMC uses refreshed momenta and a corrected
    reversible volume-preserving proposal; the inspected author chapter provides a
    periodicity counterexample to unconditional ergodicity. Acceptance frequency alone
    is not treated as an efficiency or accuracy certificate.
- assessment_id: nuts-and-warmup
  area: scope
  topic: Balanced-tree sampling and acceptance-statistic adaptation are separate procedures
  outcome: supported
  target_ids:
  - AIMech:OriginalNoUTurnSampler
  - AIMech:DualAveragingHamiltonianStepSize
  evidence_ids:
  - originalnouturnsampler-0
  - originalnouturnsampler-1
  - dualaveraginghamiltonianstepsize-0
  summary: The original slice NUTS record preserves subtree stopping tests, slice
    restrictions and the distinction between uniform subtree representatives and the
    top-level count-ratio transition. Dual averaging tunes log step size from a defined
    statistic during warmup.
  details: The naive Algorithm 2’s uniform final-set draw is not substituted for efficient
    Algorithm 3’s transition. A bad new half-tree is excluded while a U-turn only
    at the completed overall boundary can retain the new valid candidates. Zero candidate
    counts and numerical boundaries require guarded implementation. NUTS’s warmup
    statistic averages hypothetical HMC acceptance probabilities over the final doubling;
    it is not binary output acceptance. Finite warmup/freeze, regularity assumptions
    and version scope are explicit, with no assertion about current Stan defaults.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:MetropolisHastings
  - AIMech:BarkerAcceptanceRule
  - AIMech:IndependenceMetropolisHastings
  - AIMech:HamiltonianMonteCarlo
  - AIMech:OriginalNoUTurnSampler
  - AIMech:DualAveragingHamiltonianStepSize
  evidence_ids:
  - identity
  - mapping
  - existing-models
  - metropolishastings-0
  - metropolishastings-1
  - barkeracceptancerule-0
  - independencemetropolishastings-0
  - hamiltonianmontecarlo-0
  - hamiltonianmontecarlo-1
  - originalnouturnsampler-0
  - originalnouturnsampler-1
  - dualaveraginghamiltonianstepsize-0
  rationale: Retain a general Metropolis–Hastings transition, an alternative scalar
    Barker rule, the fixed independent-proposal specialization, the Euclidean Hamiltonian
    proposal/correction algorithm, the original slice-based trajectory-tree sampler
    and its separable warmup adaptation. Specialization and shared components do not
    make these identities equivalent. The records do not equate methods with the AIO
    stochastic model.
limitations:
- Adversarial author self-review only; all six records remain DRAFT.
- The original 1987 HMC full text was not inspected. Neal is honestly identified as
  an author-posted methodological chapter/review, with its own complete algorithm
  and implementation description, rather than the original invention paper.
- The record mechanisms use the inspected Hastings and NUTS primary method passages.
  Related original or later sources found only through search remain uninspected leads.
- The curated NUTS definition covers the original 2014 slice formulation, not all
  later algorithms called NUTS.
- No universal ergodicity, finite-sample convergence, independent retained-draw or
  performance claim is asserted.
- No sampler or model was run. Algebraic ratio restatements were checked against the
  visually inspected equations without claiming an empirical replication.
- Repeated passages from one publication are not independent studies. Only declared
  text/visual pages were inspected.
- All required checks passed; the assessment covers these six targets and does not
  retire unrelated findings or establish discovery saturation.
tags:
- native-concepts
- probabilistic-inference
- mcmc
- hamiltonian
- primary-methods
- self-review
- discovery-ongoing
```
