# Scientific self-review of MCEM, SAEM and MCMC-SAEM

- Review: 20261012T041121Z-monte-carlo-and-stochastic-approximation-em
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T04:06:05Z
- Finished UTC: 2026-10-12T04:11:21Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain fresh Monte Carlo EM, recursive stochastic approximation EM and its persistent Markov-chain extension. Preserve source formula/proof discrepancies, stability and kernel assumptions, original-paper access limits and the difference between finite-step behavior and asymptotic claims. No actionable curation finding remains in the three final additions.

## Scope And Provenance

All fields of three source-defined stochastic incomplete-data fitting algorithms.

Selection: Exact maintained IDs MonteCarloExpectationMaximization, StochasticApproximationExpectationMaximization and MarkovChainMonteCarloStochasticApproximationExpectationMaximization; full selected cohort without sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 07239e4b2e93e8df6ad13aa88d41bdc26dd96e45.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:MonteCarloExpectationMaximization | data/curated/MonteCarloExpectationMaximization.yaml | maintained | Monte Carlo Expectation Maximization |
| AIMech:StochasticApproximationExpectationMaximization | data/curated/StochasticApproximationExpectationMaximization.yaml | maintained | Stochastic Approximation Expectation Maximization |
| AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization | data/curated/MarkovChainMonteCarloStochasticApproximationExpectationMaximization.yaml | maintained | Markov Chain Monte Carlo Stochastic Approximation Expectation Maximization |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:MonteCarloExpectationMaximization, AIMech:StochasticApproximationExpectationMaximization, AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 133.19s (0:02:13)<br>Checked 442 record(s); 0 failed.<br>Checked 473 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 138 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 135,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:MonteCarloExpectationMaximization, AIMech:StochasticApproximationExpectationMaximization, AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:MonteCarloExpectationMaximization, AIMech:StochasticApproximationExpectationMaximization, AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:MonteCarloExpectationMaximization, AIMech:StochasticApproximationExpectationMaximization, AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization | Command exited 0 with no output. |
| Monte Carlo and stochastic approximation EM boundaries | passed | True | AIMech:MonteCarloExpectationMaximization, AIMech:StochasticApproximationExpectationMaximization, AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization | {"gaussian": {"old": 1.0, "exact_em": 0.5, "mcem": 1.5, "saem": 1.125, "likelihoods": [-0.5, -0.125, -1.125, -0.6328125]}, "nonlinear_averaging": {"maximize_averaged_statistic": 1.6094379124341003, "average_parameter": 1.0986122886681098}, "markov": {"target": ["3/11", "8/11"], "transition": [["3/5", "2/5"], ["3/20", "17/20"]], "first": ["3/5", "2/5"], "second": ["21/50", "29/50"], "conditional_noise": "-18/55", "periodic_flip": [["0", "1"], ["1", "0"]]}, "information": {"complete_hessian": -2, "G": -1, "H": -1, "observed_information": 1}, "proof_boundaries": {"endpoint_logs": [-4.605170185988091, -13.815510557964274, -27.631021115928547, -55.262042231857095], "superlinear_holder_ratio": [100.0, 10000.0, 1000000.0], "weaker_holder_to_lipschitz_ratio": [10.0, 100.0, 1000.0000000000001]}, "scope": "Finite algebraic checks only; no general convergence-proof repair, original software, empirical fit, or calibration experiment."} |

## Scientific And Domain Assessments

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:MonteCarloExpectationMaximization.

MCEM approximates the E-step of a latent-data fitting procedure. It differs from recursive objective averaging in SAEM, conditional expectation of a completed-data estimator in ICE, and Bayesian data-augmentation sampling of the parameter itself. Specialized synthetic-data or image-model applications do not exhaust this general algorithm. All 442 pinned AIO labels/scoped synonyms and 470 preceding native IDs, names and aliases were compared with no normalized identity match. Ignored-inclusive whole-checkout fixed-string searches found 218 matched lines in each checkout; context windows for all 41 distinct matched texts were read. BayesianDataAugmentation, HiddenMarkovTree and IterativeConditionalEstimation mention applications or adjacent estimators, not these identities. All 225 semantic label/synonym rows were recomputed and verified identical to the preceding fully read inventory. Sixteen annotated AIO nodes and outgoing edges comprise fourteen verified prior readings and two new readings. Thirty-four contextual YAMLs comprise twenty-seven byte-verified prior readings and seven full new readings. Absence is bounded to this pin, maintained corpus and inspected neighborhood. No normalized name/alias matches among 442 pinned and 470 maintained records. BayesianDataAugmentation, HiddenMarkovTree and IterativeConditionalEstimation matches are applications or adjacent estimators, not duplicate generic MCEM, SAEM or MCMC-SAEM records. The inspected sufficient-statistic maximization and fixed-data scope distinguish SAEM from averaged parameter gradients, ICE and sequential-task continual learning. Persistent Markovian simulation distinguishes the MCMC extension from the exact-conditional-draw base theorem.

At current theta_k, obtain m_k latent completions from the conditional law p(z&#124;y;theta_k). For candidate theta form Q_hat_k(theta)=m_k^(-1) sum_j log f(y,z_kj;theta), and maximize over theta to obtain the next fit. The simulated completions remain fixed while this sampled objective is optimized. The baseline MCEM calculation replaces the preceding sampled objective at each iteration; it does not recursively average objectives from earlier parameter values. The Monte Carlo average is taken over complete log objectives or their sufficient statistics before maximization. In general this is different from averaging the complete-data maximizer over imputations. A MAP objective can be represented by an appropriate complete log posterior, but simulating latent completions at a current parameter does not by itself sample a posterior distribution over that parameter. Maximizing a finite sampled Q does not certify improvement of the exact Q or observed likelihood. The saved valid Gaussian example gives an MCEM update with lower observed likelihood than its starting value. Monte Carlo count, dependence and integration error require their own analysis; apparently stable parameters or the exact-EM ascent argument alone do not establish convergence of this stochastic procedure. Limitations: The full mechanism source inspected here is the 1999 primary SAEM paper, which explicitly presents MCEM for comparison. The original Wei-Tanner 1990 paper was identified through publisher metadata/abstract but its university PDF returned 403; no unseen original proofs or poor-man data-augmentation details are claimed. The simple unweighted sample mean requires draws from the intended conditional law. MCMC samples are generally dependent and need appropriate exploration/ergodicity conditions; importance sampling requires its own weighting. A local-observation heuristic is not certified full-posterior sampling. Finite Monte Carlo noise can persist near a stationary point. No generic fixed-sample-size convergence theorem, universal rate, adaptive sample-size rule or global optimum is asserted. The complete objective must be well defined and its maximization admissible. Boundary or unbounded likelihoods, nonidentifiability, poor initialization and numerical errors remain model-specific limitations. All 35 pages of the comparison source were read. Finite algebraic checks are curator examples, not historical software, a reproduced fit or empirical performance evidence.

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:StochasticApproximationExpectationMaximization.

The Delyon-Lavielle-Moulines SAEM construction fits a fixed observed data set while stochastic approximation controls integration noise. It is distinct from fresh-batch MCEM, stochastic-gradient parameter steps, parameter-iterate averaging, and online learning from newly arriving observations. A persistent MCMC simulation step is a separately scoped extension because exact conditional draws and Markovian perturbations require different arguments. All 442 pinned AIO labels/scoped synonyms and 470 preceding native IDs, names and aliases were compared with no normalized identity match. Ignored-inclusive whole-checkout fixed-string searches found 218 matched lines in each checkout; context windows for all 41 distinct matched texts were read. BayesianDataAugmentation, HiddenMarkovTree and IterativeConditionalEstimation mention applications or adjacent estimators, not these identities. All 225 semantic label/synonym rows were recomputed and verified identical to the preceding fully read inventory. Sixteen annotated AIO nodes and outgoing edges comprise fourteen verified prior readings and two new readings. Thirty-four contextual YAMLs comprise twenty-seven byte-verified prior readings and seven full new readings. Absence is bounded to this pin, maintained corpus and inspected neighborhood. No normalized name/alias matches among 442 pinned and 470 maintained records. BayesianDataAugmentation, HiddenMarkovTree and IterativeConditionalEstimation matches are applications or adjacent estimators, not duplicate generic MCEM, SAEM or MCMC-SAEM records. The inspected sufficient-statistic maximization and fixed-data scope distinguish SAEM from averaged parameter gradients, ICE and sequential-task continual learning. Persistent Markovian simulation distinguishes the MCMC extension from the exact-conditional-draw base theorem.

Simulate latent completions under the current conditional law and update Q_k(theta)=(1-gamma_k)Q_(k-1)(theta)+gamma_k times the current sample mean of complete log objectives. Maximize Q_k to obtain the next parameter. For the stated curved exponential family, store sufficient statistics instead: s_k=s_(k-1)+gamma_k(S(z_k)-s_(k-1)), followed by theta_k=theta_hat(s_k). The one-draw construction can therefore retain past information without storing every prior completion. The single-draw stationary-set theorem requires a smooth curved-exponential complete model and maximizer map, exact conditional simulation given the past, finite continuous second moments, step sizes in [0,1] with divergent sum and finite sum of squares, and almost-sure containment of the statistic iterates in a compact subset of their domain. Under those hypotheses the distance to the stated stationary sets tends to zero. Step-size conditions alone do not supply stability, point convergence, a global maximum or observed-likelihood ascent at every iteration. Recursive averaging of the expected objective precedes its maximization. Optional averaging of fitted parameter iterates is a separate operation with additional local stability, moment and step-size conditions. Averaging statistics before a nonlinear maximizer need not equal averaging parameter values. Simulation-iteration uncertainty around a fixed-data solution is distinct from sampling uncertainty of the statistical estimator. In Eq6, gamma=0 freezes the accumulated objective, while gamma=1 replaces it by the current Monte Carlo objective; the paragraph identifying gamma=0 with ordinary stochastic EM is inconsistent with that recursion. The 1999 covariance prose also reverses the Hessian sign: its H=G-Delta Delta^T estimates the observed log Hessian, while observed information is -H, as explicitly used in the 2004 follow-up. These printed statements are not used as implementation rules. Limitations: The core mechanism is supported independently of the source’s stronger local-maximizer and averaging claims. Those results need additional isolated-stationary-point, curvature, excitation and local-rate hypotheses. Their printed exposition contains sign/wording inconsistencies; no blanket theorem repair or global convergence certification is claimed. A finite stochastic update need not increase the observed likelihood. The finite Gaussian example lowers it even with a positive averaging weight; stabilization and convergence need separate arguments. The source’s expanding-compact reset scheme, approximate conditional maximizations and stochastic-gradient extensions introduce additional assumptions. They are not silently covered by the core exact-maximizer theorem. The source’s Eq27 average-noise expression omits a Jacobian factor present in its later proof, and its Section 8 Newton direction and convexity wording conflict with concave maximization. These extension formulas are not implemented or endorsed by this record. Independent exact conditional draws are an assumption of the inspected base theorem, not a property of a short MCMC run. The separately scoped MCMC-SAEM extension handles a different noise structure. All 52 pages of the two primary papers were read. No author software, historical fit, empirical speed comparison or uncertainty-calibration study was reproduced.

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization.

MCMC-SAEM replaces exact conditional latent draws in base SAEM by transitions from a carried state, often a fixed number of Metropolis-Hastings steps per parameter update. This differs from running an independent full equilibrium sampler at every iteration, fresh-batch MCEM and posterior sampling of the parameter itself. The Markov kernel changes with the fitted parameter. All 442 pinned AIO labels/scoped synonyms and 470 preceding native IDs, names and aliases were compared with no normalized identity match. Ignored-inclusive whole-checkout fixed-string searches found 218 matched lines in each checkout; context windows for all 41 distinct matched texts were read. BayesianDataAugmentation, HiddenMarkovTree and IterativeConditionalEstimation mention applications or adjacent estimators, not these identities. All 225 semantic label/synonym rows were recomputed and verified identical to the preceding fully read inventory. Sixteen annotated AIO nodes and outgoing edges comprise fourteen verified prior readings and two new readings. Thirty-four contextual YAMLs comprise twenty-seven byte-verified prior readings and seven full new readings. Absence is bounded to this pin, maintained corpus and inspected neighborhood. No normalized name/alias matches among 442 pinned and 470 maintained records. BayesianDataAugmentation, HiddenMarkovTree and IterativeConditionalEstimation matches are applications or adjacent estimators, not duplicate generic MCEM, SAEM or MCMC-SAEM records. The inspected sufficient-statistic maximization and fixed-data scope distinguish SAEM from averaged parameter gradients, ICE and sequential-task continual learning. Persistent Markovian simulation distinguishes the MCMC extension from the exact-conditional-draw base theorem.

From the retained latent state z_(k-1), apply a transition Pi_(theta_k) with invariant target p(z&#124;y;theta_k), obtaining z_k. Use it in s_k=s_(k-1)+gamma_k(S(y,z_k)-s_(k-1)), then set theta_(k+1)=theta_hat(s_k). The kernel can comprise M Metropolis-Hastings steps. Retain rejected states and accepted updates; restart or discarded-rejection variants define different simulation schemes. Metropolis-Hastings acceptance includes the reverse-to-forward proposal ratio. When an independence proposal is the current latent prior, prior factors cancel and the observed conditional likelihood ratio remains. Invariance of the target does not mean one or finitely many transitions from an arbitrary state produce that target distribution. The finite two-state example preserves its target yet has a different first-step distribution and nonzero conditional sampling error. The published analysis imposes the curved-exponential model and smooth maximizer assumptions, stochastic-approximation step sizes, compact latent states, bounded sufficient statistics, parameter regularity of transitions, uniform ergodicity and compact statistic iterates. Its stationary-set conclusion is conditional on these hypotheses. A fixed number of arbitrary MCMC moves, irreducibility alone or bounded latent support alone does not supply them. The stated Lemma 1 uses exponents 1/alpha for alpha in (0,1), whereas its appendix derives Holder exponents below one. The subsequent lambda=1 conclusion does not directly follow from the displayed weaker estimate. The beta deconvolution example also has log(z) and log(1-z) statistics unbounded near the endpoints, despite bounded latent support. These discrepancies limit what is certified from the printed proof and example; the record does not supply a repaired general convergence proof. Limitations: A target-invariant transition can mix poorly or be periodic. A finite irreducible periodic flip chain demonstrates why irreducibility alone does not imply convergence to equilibrium. Markovian simulation errors are not generally conditionally mean-zero at each iteration. The exact-independent-draw martingale argument cannot be transplanted without the additional Markovian-noise analysis. The theorem’s bounded-statistic condition is separate from compact support. Truncating a latent law may change the statistical model and requires an explicit choice; no automatic equivalence to an unbounded original model is asserted. The deconvolution coordinate pseudocode ambiguously refers to old coordinates within its sweep, and its stated uniform beta initialization is inconsistent with ordinary shape parameters. The record specifies persistent transitions and does not reproduce those ambiguous implementation details. The source’s simulations can reach different local solutions. Its truth-centered empirical squared-error matrix is not generally covariance about the estimator mean when bias is present; no finite-sample interval coverage or universal speed guarantee is asserted. All 52 pages of the two primary papers were read. Finite kernel and algebra checks are curator examples, not source software, a historical model fit or independent validation of the general proof.

### Objective integration versus estimator averaging

consistency: supported. Targets: AIMech:MonteCarloExpectationMaximization, AIMech:StochasticApproximationExpectationMaximization.

Retain MCEM and SAEM as distinct accumulation rules.

MCEM forms a fresh conditional Monte Carlo objective at each fitted parameter. SAEM recursively averages complete objectives or sufficient statistics before maximization. ICE averages completed-data estimators instead, while averaged SGD averages parameter iterates. The finite log-variance example yields log(5) versus log(3), showing that nonlinear maximization and averaging do not commute. Fixed observed data distinguishes these procedures from incoming-observation online learning.

### Stochastic update versus exact likelihood improvement

consistency: supported. Targets: AIMech:MonteCarloExpectationMaximization, AIMech:StochasticApproximationExpectationMaximization.

Do not inherit per-step exact-EM ascent.

For the normalized complete model p(y,z&#124;theta)=N(y;theta,1)N(z;theta,1) at observed y=0, theta=1 and accumulated statistic 2, exact EM gives theta=0.5. A possible Monte Carlo sample mean 3 gives MCEM theta=1.5 and SAEM with gamma=0.25 theta=1.125. Observed log likelihood changes from -0.5 to -1.125 or -0.6328125, respectively. These are finite deterministic sample-summary examples, not claimed random trials, global theorems or performance comparisons.

### Exact conditional simulation, stability and printed discrepancies

consistency: supported. Targets: AIMech:StochasticApproximationExpectationMaximization.

Keep the core recursion and theorem hypotheses separate from problematic extension formulas.

Section 6 requires the curved-exponential model, smooth maximizer, exact conditional law given the past, moments, step sizes and compact statistic iterates. It gives stationary-set approach under those assumptions, not an unconditional global maximum. Local maximizer and averaging conclusions require further curvature/excitation/stability hypotheses. Eq6 with gamma=0 freezes and gamma=1 replaces; source prose reverses the SEM endpoint. The complete-Hessian plus score-outer expression is an observed Hessian, and the 2004 follow-up correctly uses -H for information. The Eq27 omitted Jacobian and Section 8 Newton/convexity wording remain documented limitations, not implemented rules.

### Invariant target, finite transitions and changing parameters

consistency: supported. Targets: AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization.

Retain MCMC-SAEM as a persistent-chain extension.

At current parameter the retained state advances under a conditional-target kernel, then updates statistics and the maximizer. Reverse proposal ratios and retained rejections matter. In the exact rational example, target (3/11,8/11) is invariant for K=((3/5,2/5),(3/20,17/20)), yet a first transition from state zero is (3/5,2/5) and conditional statistic noise is -18/55. A second transition uses the retained distribution. Target invariance is therefore distinct from finite-run equilibration and exact conditional unbiasedness; parameter changes add another noise issue.

### Ergodicity, bounded statistics and Holder estimates

consistency: supported. Targets: AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization.

Preserve the unresolved printed-proof limitations.

The stated analysis imposes compact latent support, bounded statistics, transition regularity, uniform ergodicity and stable statistic iterates as well as model and step-size assumptions. A finite irreducible periodic flip has an invariant target but no approach from a point start. Beta log statistics are unbounded near endpoints despite bounded latent support. Lemma 1 prints exponent 1/alpha with alpha&lt;1 while the appendix derives exponents below one; its immediate lambda=1 step is not established by that weaker estimate. Finite ratio checks expose these distinctions but neither repair the proof nor assert that every convergence conclusion is false.

### Pseudocode ambiguities, covariance and empirical scope

consistency: supported. Targets: AIMech:StochasticApproximationExpectationMaximization, AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization.

Do not promote source examples to certified implementations.

The 2004 coordinate sweep refers ambiguously to old coordinates, and its uniform beta initialization is incompatible with ordinary shape parameters. No author code was inspected to resolve these details. Truth-centered squared errors need not be estimator-mean covariance under bias. Simulation-iteration uncertainty differs from statistical-estimator uncertainty. Tables were visually read with their labels; no historical fit, speed comparison or interval coverage was reproduced.

### Bounded source access, aliases and AIO abstraction

grounding: supported. Targets: AIMech:MonteCarloExpectationMaximization, AIMech:StochasticApproximationExpectationMaximization, AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization.

Retain three native algorithms with related mappings and DRAFT status.

All 52 pages of two primary PDFs were read. The original 1990 MCEM full PDF returned 403, and its uninspected posterior variants are excluded; the 1999 full primary comparison supplies the generic mechanism. Scan annotations are not author errata. No normalized identity matches were found in 442 AIO and 470 preceding native records. Both ignored-inclusive checkout searches and all 41 distinct matching windows were inspected. Three algorithm-to-task related mappings and the MCMC algorithm-to-Markov-process relation do not assert subclasses or upstream acceptance. Three new provisional cohorts leave 404 pending entries; no saturation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:MonteCarloExpectationMaximization, AIMech:StochasticApproximationExpectationMaximization, AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization. Fresh conditional integration, recursive objective/statistic averaging and persistent Markovian simulation have distinct operations and assumptions. A shared EM purpose does not establish identity. Related algorithm-to-task and algorithm-to-process mappings preserve abstraction without asserting subclasses.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T040545Z-monte-carlo-and-stochastic-approximation-em.json | supports | No normalized name/alias matches among 442 pinned and 470 maintained records. BayesianDataAugmentation, HiddenMarkovTree and IterativeConditionalEstimation matches are applications or adjacent estimators, not duplicate generic MCEM, SAEM or MCMC-SAEM records. The inspected sufficient-statistic maximization and fixed-data scope distinguish SAEM from averaged parameter gradients, ICE and sequential-task continual learning. Persistent Markovian simulation distinguishes the MCMC extension from the exact-conditional-draw base theorem.<br> |
| mapping | sources/aio/aio.json; 16 annotated CLASS nodes and outgoing edges; 225 semantic rows recomputed and verified against the prior fully read inventory | supports | Sixteen annotated AIO nodes with outgoing edges and 34 contextual YAMLs were assessed against the pinned source. All three fitting algorithms have related_match to MachineLearningTask: this is algorithm-to-task context, not is-a. MCMC-SAEM additionally has related_match to MarkovChain because a conditional-target process is an explicit component. TrainingStrategy, transformation DataAugmentation, ContinualLearning, generic Model and fixed/random-effect model classes do not identify these fitting procedures. The 225 semantic rows were recomputed and byte-verified against the preceding fully read inventory; 14 nodes and 27 YAMLs reuse hash-verified prior readings, with two new nodes and seven new YAMLs fully read this round.<br> |
| neighbors | research/discovery/20261012T040545Z-monte-carlo-and-stochastic-approximation-em.json; Eighteen native neighbors and 16 generated contextual YAMLs in source_analysis.context_reading | supports | Thirty-four contextual YAMLs comprise 27 byte-verified prior readings and seven new full readings. EM variants, MH/IMH/Gibbs, Bayesian data augmentation, ICE, hidden Markov trees, SGD and parameter-iterate averaging distinguish these identities. Contextual records receive no renewed scientific approval. |
| finite-boundaries | research/discovery/monte-carlo-and-stochastic-approximation-em-boundaries.py; Finite Gaussian likelihood, nonlinear averaging, rational MH transitions, periodicity, information sign and source proof boundaries | supports | Valid finite Gaussian completions show MCEM and SAEM need not ascend at each step; nonlinear maximization does not commute with averaging. Exact rational MH calculations distinguish target invariance from finite-run equilibration and conditional unbiasedness. A periodic chain, beta endpoint sequence, Holder ratios, information sign and Newton step expose assumption/formula boundaries. These examples do not repair a general proof or reproduce published experiments. |
| montecarloexpectationmaximization-source-0 | https://oa.ee.tsinghua.edu.cn/ouzhijian/pgm/pgm-pdf/Delyon99_Convergence%20of%20a%20Stochastic%20Approximation%20Version%20of%20the%20EM%20Algorithm.pdf; Section 2 Eq4-5, pp.96-97 / PDF3-4; Section 3 sampling discussion, p.98 / PDF5; finite Gaussian curator calculation in discovery ledger; Section 2 Eq5 and Section 3 MCEM/SAEM comparison, pp.96-98 / PDF3-5; Section 2, pp.95-97 / PDF2-4, especially Eq5 and its simulation/maximization steps; Sections 1-2, pp.94-97 / PDF1-4; Eq4-5 and fixed-parameter conditional-law definition | supports | Convergence of a stochastic approximation version of the EM algorithm. Annals of Statistics 27(1):94-128 (1999), university-hosted annotated JSTOR scan. All 35 PDF pages visually read, including appendices and references. Printed page equals PDF page plus 93. Existing highlights and handwritten marks are not author errata; the 2015 download stamp is not the publication date. Section 2 explicitly defines MCEM as the comparison method. Curator algebraic deductions are distinguished from historical empirical results or uninspected software. |
| stochasticapproximationexpectationmaximization-source-0 | https://oa.ee.tsinghua.edu.cn/ouzhijian/pgm/pgm-pdf/Delyon99_Convergence%20of%20a%20Stochastic%20Approximation%20Version%20of%20the%20EM%20Algorithm.pdf; Section 3 Eq6 and following paragraph, p.97 / PDF4; Section 3 Eq11 and Hessian prose, p.99 / PDF6; Section 3 Eq6, pp.97-98 / PDF4-5; M1-M5, pp.99-100 / PDF6-7; Section 6 Eq30, p.107 / PDF14; Section 3 Eq6, pp.97-98 / PDF4-5; Section 6 Eq30, p.107 / PDF14; Section 6 SAEM1-SAEM4 and Theorem 5, pp.107-109 / PDF14-16; Sections 5.1 and 7, pp.104-106 and 110-113 / PDF11-13 and 17-20; Eq26 and Eq48-55 | supports | Convergence of a stochastic approximation version of the EM algorithm. Annals of Statistics 27(1):94-128 (1999), university-hosted annotated JSTOR scan. All 35 PDF pages visually read, including appendices and references. Printed page equals PDF page plus 93. Existing highlights and handwritten marks are not author errata; the 2015 download stamp is not the publication date. Section 2 explicitly defines MCEM as the comparison method. Curator algebraic deductions are distinguished from historical empirical results or uninspected software. |
| stochasticapproximationexpectationmaximization-source-1 | https://www.numdam.org/article/PS_2004__8__115_0.pdf; Section 2.3 Eq8-10, p.119 / PDF5; compare 1999 Section 3 Eq6 and Eq11, pp.97,99 / PDF4,6 | supports | Coupling a stochastic approximation version of EM with an MCMC procedure. ESAIM: Probability and Statistics 8:115-131, August 2004, Numdam-hosted full journal PDF. All 17 pages visually read, including three tables, proof, appendix and references. Printed page equals PDF page plus 114. Curator algebraic deductions are distinguished from historical empirical results or uninspected software. |
| markovchainmontecarlostochasticapproximationexpectationmaximization-source-0 | https://www.numdam.org/article/PS_2004__8__115_0.pdf; Lemma 1 and proof conclusion, p.123 / PDF9; deconvolution sufficient statistics, p.124 / PDF10; Appendix Eq25-26, p.130 / PDF16; Section 2.2 Eq5-6, p.119 / PDF5; Section 3 discussion of Markovian noise, p.120 / PDF6; finite kernel calculation in discovery ledger; Section 2.2, p.119 / PDF5, three-step algorithm and Pi_theta=P_theta^M; Section 3 SAEM3-prime and Theorem 1, pp.120-123 / PDF6-9; Appendix pp.129-130 / PDF15-16; Sections 2.1-2.2, Eq4-5, pp.118-119 / PDF4-5 | supports | Coupling a stochastic approximation version of EM with an MCMC procedure. ESAIM: Probability and Statistics 8:115-131, August 2004, Numdam-hosted full journal PDF. All 17 pages visually read, including three tables, proof, appendix and references. Printed page equals PDF page plus 114. Curator algebraic deductions are distinguished from historical empirical results or uninspected software. |
| markovchainmontecarlostochasticapproximationexpectationmaximization-source-1 | https://oa.ee.tsinghua.edu.cn/ouzhijian/pgm/pgm-pdf/Delyon99_Convergence%20of%20a%20Stochastic%20Approximation%20Version%20of%20the%20EM%20Algorithm.pdf; Section 6 Eq30 and exact conditional-draw assumption, pp.107-109 / PDF14-16; baseline statistic recursion and simulation assumption replaced by the 2004 Markovian extension | supports | Convergence of a stochastic approximation version of the EM algorithm. Annals of Statistics 27(1):94-128 (1999), university-hosted annotated JSTOR scan. All 35 PDF pages visually read, including appendices and references. Printed page equals PDF page plus 93. Existing highlights and handwritten marks are not author errata; the 2015 download stamp is not the publication date. Section 2 explicitly defines MCEM as the comparison method. Curator algebraic deductions are distinguished from historical empirical results or uninspected software. |

## Limits And Additional Notes

- Adversarial author self-review only; all three records remain DRAFT.
- The first vendored-check failed because the sandbox could not resolve the public host; the authorized network-enabled rerun verified all 22 pinned artifacts.
- All 35 pages of Delyon-Lavielle-Moulines 1999 and all 17 pages of Kuhn-Lavielle 2004 were visually read, including proofs, appendices, tables and references. Printed pages equal PDF pages plus 93 and 114 respectively.
- The university-hosted 1999 scan contains pre-existing highlights, red boxes and handwritten marks. These are not treated as author errata. The 2015 download stamp is not its publication date.
- The Wei-Tanner 1990 original MCEM PDF returned 403. Its publisher title, authors, DOI and abstract were inspected; source-specific posterior approximation variants and unseen proofs are not asserted. The 1999 full primary paper explicitly defines the generic MCEM algorithm used here.
- Source discrepancies are recorded rather than silently repaired: 1999 zero-step, information/Hessian signs, average-noise Jacobian, local-curvature wording and Newton direction; 2004 Holder exponents/proof step, bounded-support versus bounded-statistic assumption, beta initialization and coordinate-sweep ambiguity.
- Core method definitions, conditional asymptotic conclusions, per-iteration likelihood ascent and finite-sample calibration are different claims. No repaired general convergence proof is supplied.
- Finite Gaussian, nonlinear-averaging, exact rational Markov-kernel and sign/endpoint examples are curator calculations. No source software, historical fit, runtime comparison or coverage experiment was reproduced. Full PDFs are not redistributed.
- Initial validate-curated identified an uncited base-SAEM source in MCMC-SAEM; its precise baseline recursion/conditional-draw locator was added as contextual evidence. The rerun validated all 473 native records with zero errors before formal review.
- Three provisional source cohorts leave 404 pending frontier entries and additional unresolved dispositions. Exact new-label searches included ignored/hidden files, but do not prove all underlying methods are novel. No saturation is claimed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T041121Z-monte-carlo-and-stochastic-approximation-em
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of MCEM, SAEM and MCMC-SAEM
started_at: '2026-10-12T04:06:05Z'
finished_at: '2026-10-12T04:11:21Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially read all fields of three final
    maintained records against 52 primary PDF pages, sixteen annotated AIO nodes and
    eighteen native neighbors. Finite algebra challenges likelihood ascent, averaging
    order, Markov equilibration and source proof/sign assumptions. This is author
    self-review; no independent approval is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain fresh Monte Carlo EM, recursive stochastic approximation EM and its
  persistent Markov-chain extension. Preserve source formula/proof discrepancies,
  stability and kernel assumptions, original-paper access limits and the difference
  between finite-step behavior and asymptotic claims. No actionable curation finding
  remains in the three final additions.
source:
  git_revision: 07239e4b2e93e8df6ad13aa88d41bdc26dd96e45
  state: working_tree
  inputs:
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/ContinualLearning.yaml
    sha256: c55fe9b9214b2f98c463af6c6756d71d7b070e9f35cb1dbba0a1b400073bf9b3
    role: context
  - path: data/aio/DataAugmentation.yaml
    sha256: e99fd76071e8b52cbe8ed53f694b30093d7fb7a8af2e225f2f158f5cab5f11ae
    role: context
  - path: data/aio/FixedEffectsModel.yaml
    sha256: ce9b21b60e99bf7abfd19b9b480d5c73777ba59f38af53c3fa2d6bfc50f71a86
    role: context
  - path: data/aio/GeneralizedLinearModel.yaml
    sha256: 202002ec50c6e6207bc2fefba5baeab233514fd8f9118a623d1917b599ce2c7d
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/Preprocessing.yaml
    sha256: 2c4a30f4f829a757be1feabf78d15780eedf93681a62eede3e76b2304f21bb7a
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/RandomEffectsModel.yaml
    sha256: 4e3f50ef012b217822c2b731cce1b07dff14e66826f26d7717a6dab42d482d4c
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/RepresentationLearning.yaml
    sha256: bc7af756440437f60210019e17ad1e2dd15cd1c7cbfbc96312520934b7a5c7ca
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/AlternatingExpectationConditionalMaximization.yaml
    sha256: 7e0e004ed49a7afc64621a394bd6828c25f6ba551357fd97aa54efd6487d74a4
    role: context
  - path: data/curated/AveragedStochasticGradientDescent.yaml
    sha256: 8a57b2cbee2867e7511f114bf155fbffd632474f0b2c6433f7a28a90bf729d85
    role: context
  - path: data/curated/BayesianDataAugmentation.yaml
    sha256: 4d95781fa743392ee3bcda4cf5cb3d79a35052750a01e090d2bc54b5693e14b5
    role: context
  - path: data/curated/ExpectationConditionalMaximization.yaml
    sha256: 525c100f17166d92874cf2f44d4f622b376f86fca16e6716474d463632c53e44
    role: context
  - path: data/curated/ExpectationConditionalMaximizationEither.yaml
    sha256: e9b94dc648b9453f958558e2d91af4c09bd7663380b1a5dd96d52d44f7d15074
    role: context
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: context
  - path: data/curated/GibbsSampling.yaml
    sha256: 8175215986c0507e3664a3aedf8074fc067d85b4a89002091d1bcb9b637a522a
    role: context
  - path: data/curated/HiddenMarkovTree.yaml
    sha256: ca89c267443e8b806d61b389943bd06a514fb8a95668bd604fae4ecc2d873e1b
    role: context
  - path: data/curated/IndependenceMetropolisHastings.yaml
    sha256: ca1390f00edca43e94f897e2398b3f7d8edddefadc0a5780e0b470816a7754df
    role: context
  - path: data/curated/IterativeConditionalEstimation.yaml
    sha256: 98813e020f43870f725a5c1e4ab0de9197f0dc2bc85f61e66e2044ab8d87e9cc
    role: context
  - path: data/curated/MarkovChainMonteCarloStochasticApproximationExpectationMaximization.yaml
    sha256: 6670aad24842e0f3b32fa97689f34054ac90f10d83f05c3fe2b63de0a1a8a6ba
    role: target
  - path: data/curated/MetropolisHastings.yaml
    sha256: 01cb22a25242e8564e2a7bb839ecb46da1bc49eb09b3c85200f9a596e05b99b4
    role: context
  - path: data/curated/MetropolisWithinGibbs.yaml
    sha256: 0e9cfedc93c7e46cc6316809d5a9ec9488b33891a9c9862f914a0adf8f7cb140
    role: context
  - path: data/curated/MonteCarloExpectationMaximization.yaml
    sha256: 4fe2298310d7e8307af93dbab852485beb0ee210588ff7e8c94e7912b7416ffd
    role: target
  - path: data/curated/ParameterExpandedExpectationMaximization.yaml
    sha256: 5bb3941c8224bb835043bae5e22ecb01225a5060cb5f1ea90c531df0dc1104cd
    role: context
  - path: data/curated/SpaceAlternatingGeneralizedExpectationMaximization.yaml
    sha256: 0a6ea8f561031c7c0adc8bd48aa2903410eaee7603da60bbc02fac240cc71464
    role: context
  - path: data/curated/StochasticApproximationExpectationMaximization.yaml
    sha256: f23a3d7e121b29106dcd2372a16e5af853ebedd6b6efdee9fab7f19284cbdefa
    role: target
  - path: data/curated/StochasticGradientDescent.yaml
    sha256: 5c57fc809ae8667d5be8cda421cc9f0bd1f0c668f64ba3d7b23d788528b46e97
    role: context
  - path: data/curated/SupplementedExpectationConditionalMaximization.yaml
    sha256: a4fdc36221d1069e0a8087e052ba23f4d0cac409da023ed5cda67f77e4fbad26
    role: context
  - path: data/curated/SupplementedExpectationMaximization.yaml
    sha256: f394073c0dbc44225cb0d8c5f27f3833d9af19a8b9a7d303556605e923196381
    role: context
  - path: data/curated/TemperedExpectationMaximization.yaml
    sha256: 792d43ce4f38f485002b9fadbb1e9d9ac32879069cb2ec6e42b3443b57441ca5
    role: context
  - path: research/discovery/20261012T040545Z-monte-carlo-and-stochastic-approximation-em.json
    sha256: 0fe666d12a970da98906bf465f4568a972be6d0435691eb506460182525c9833
    role: context
  - path: research/discovery/monte-carlo-and-stochastic-approximation-em-boundaries.py
    sha256: 8232a720051179aca039cbff7974f2905aabb540b2be0965f15966c4ce59067c
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 67cc03d7def5f62490cc1f5db320a7c18fdfd41cebf43a35ad2bb88c32cd40d5
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:MonteCarloExpectationMaximization
  path: data/curated/MonteCarloExpectationMaximization.yaml
  label: Monte Carlo Expectation Maximization
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MonteCarloExpectationMaximization.yaml
    role: maintained
- target_id: AIMech:StochasticApproximationExpectationMaximization
  path: data/curated/StochasticApproximationExpectationMaximization.yaml
  label: Stochastic Approximation Expectation Maximization
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StochasticApproximationExpectationMaximization.yaml
    role: maintained
- target_id: AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization
  path: data/curated/MarkovChainMonteCarloStochasticApproximationExpectationMaximization.yaml
  label: Markov Chain Monte Carlo Stochastic Approximation Expectation Maximization
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MarkovChainMonteCarloStochasticApproximationExpectationMaximization.yaml
    role: maintained
scope:
  description: All fields of three source-defined stochastic incomplete-data fitting
    algorithms.
  selection: Exact maintained IDs MonteCarloExpectationMaximization, StochasticApproximationExpectationMaximization
    and MarkovChainMonteCarloStochasticApproximationExpectationMaximization; full
    selected cohort without sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:MonteCarloExpectationMaximization
  - AIMech:StochasticApproximationExpectationMaximization
  - AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization
  exclusions:
  - target: Contextual AIO and maintained records
    reason: Context informs identity and abstraction boundaries without renewed scientific
      approval or mutation.
  - target: Historical implementations and empirical reproduction
    reason: No source software, empirical model fitting or coverage experiment ran.
      Curator arithmetic checks bounded mathematical claims only.
  - target: Remaining discovery frontier
    reason: 404 pending entries and other unresolved dispositions remain, including
      original MCEM full text and annealed variants. No broader saturation is claimed.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:MonteCarloExpectationMaximization
  - AIMech:StochasticApproximationExpectationMaximization
  - AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 133.19s (0:02:13)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 473 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 138 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 135,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:MonteCarloExpectationMaximization
  - AIMech:StochasticApproximationExpectationMaximization
  - AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: required-2
  name: uv run --locked aimech check-source
  command: uv run --locked aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:MonteCarloExpectationMaximization
  - AIMech:StochasticApproximationExpectationMaximization
  - AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:MonteCarloExpectationMaximization
  - AIMech:StochasticApproximationExpectationMaximization
  - AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Monte Carlo and stochastic approximation EM boundaries
  command: python3 research/discovery/monte-carlo-and-stochastic-approximation-em-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:MonteCarloExpectationMaximization
  - AIMech:StochasticApproximationExpectationMaximization
  - AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization
  exit_code: 0
  expected_exit_code: 0
  summary: '{"gaussian": {"old": 1.0, "exact_em": 0.5, "mcem": 1.5, "saem": 1.125,
    "likelihoods": [-0.5, -0.125, -1.125, -0.6328125]}, "nonlinear_averaging": {"maximize_averaged_statistic":
    1.6094379124341003, "average_parameter": 1.0986122886681098}, "markov": {"target":
    ["3/11", "8/11"], "transition": [["3/5", "2/5"], ["3/20", "17/20"]], "first":
    ["3/5", "2/5"], "second": ["21/50", "29/50"], "conditional_noise": "-18/55", "periodic_flip":
    [["0", "1"], ["1", "0"]]}, "information": {"complete_hessian": -2, "G": -1, "H":
    -1, "observed_information": 1}, "proof_boundaries": {"endpoint_logs": [-4.605170185988091,
    -13.815510557964274, -27.631021115928547, -55.262042231857095], "superlinear_holder_ratio":
    [100.0, 10000.0, 1000000.0], "weaker_holder_to_lipschitz_ratio": [10.0, 100.0,
    1000.0000000000001]}, "scope": "Finite algebraic checks only; no general convergence-proof
    repair, original software, empirical fit, or calibration experiment."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T040545Z-monte-carlo-and-stochastic-approximation-em.json
  accessed_at: '2026-10-12T04:06:05Z'
  support: supports
  summary: 'No normalized name/alias matches among 442 pinned and 470 maintained records.
    BayesianDataAugmentation, HiddenMarkovTree and IterativeConditionalEstimation
    matches are applications or adjacent estimators, not duplicate generic MCEM, SAEM
    or MCMC-SAEM records. The inspected sufficient-statistic maximization and fixed-data
    scope distinguish SAEM from averaged parameter gradients, ICE and sequential-task
    continual learning. Persistent Markovian simulation distinguishes the MCMC extension
    from the exact-conditional-draw base theorem.

    '
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 16 annotated CLASS nodes and outgoing edges; 225 semantic rows recomputed
    and verified against the prior fully read inventory
  accessed_at: '2026-10-12T04:06:05Z'
  support: supports
  summary: 'Sixteen annotated AIO nodes with outgoing edges and 34 contextual YAMLs
    were assessed against the pinned source. All three fitting algorithms have related_match
    to MachineLearningTask: this is algorithm-to-task context, not is-a. MCMC-SAEM
    additionally has related_match to MarkovChain because a conditional-target process
    is an explicit component. TrainingStrategy, transformation DataAugmentation, ContinualLearning,
    generic Model and fixed/random-effect model classes do not identify these fitting
    procedures. The 225 semantic rows were recomputed and byte-verified against the
    preceding fully read inventory; 14 nodes and 27 YAMLs reuse hash-verified prior
    readings, with two new nodes and seven new YAMLs fully read this round.

    '
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261012T040545Z-monte-carlo-and-stochastic-approximation-em.json
  locator: Eighteen native neighbors and 16 generated contextual YAMLs in source_analysis.context_reading
  accessed_at: '2026-10-12T04:06:05Z'
  support: supports
  summary: Thirty-four contextual YAMLs comprise 27 byte-verified prior readings and
    seven new full readings. EM variants, MH/IMH/Gibbs, Bayesian data augmentation,
    ICE, hidden Markov trees, SGD and parameter-iterate averaging distinguish these
    identities. Contextual records receive no renewed scientific approval.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/monte-carlo-and-stochastic-approximation-em-boundaries.py
  locator: Finite Gaussian likelihood, nonlinear averaging, rational MH transitions,
    periodicity, information sign and source proof boundaries
  accessed_at: '2026-10-12T04:06:05Z'
  snapshot_sha256: 8232a720051179aca039cbff7974f2905aabb540b2be0965f15966c4ce59067c
  support: supports
  summary: Valid finite Gaussian completions show MCEM and SAEM need not ascend at
    each step; nonlinear maximization does not commute with averaging. Exact rational
    MH calculations distinguish target invariance from finite-run equilibration and
    conditional unbiasedness. A periodic chain, beta endpoint sequence, Holder ratios,
    information sign and Newton step expose assumption/formula boundaries. These examples
    do not repair a general proof or reproduce published experiments.
- evidence_id: montecarloexpectationmaximization-source-0
  kind: primary_source
  reference: https://oa.ee.tsinghua.edu.cn/ouzhijian/pgm/pgm-pdf/Delyon99_Convergence%20of%20a%20Stochastic%20Approximation%20Version%20of%20the%20EM%20Algorithm.pdf
  locator: Section 2 Eq4-5, pp.96-97 / PDF3-4; Section 3 sampling discussion, p.98
    / PDF5; finite Gaussian curator calculation in discovery ledger; Section 2 Eq5
    and Section 3 MCEM/SAEM comparison, pp.96-98 / PDF3-5; Section 2, pp.95-97 / PDF2-4,
    especially Eq5 and its simulation/maximization steps; Sections 1-2, pp.94-97 /
    PDF1-4; Eq4-5 and fixed-parameter conditional-law definition
  accessed_at: '2026-10-12T03:50:09Z'
  snapshot_sha256: f2c7a8005a1dee0a14bb243cb0bb2cb135227b1e9bff459eb07b3d0e6cc0b9bf
  support: supports
  summary: Convergence of a stochastic approximation version of the EM algorithm.
    Annals of Statistics 27(1):94-128 (1999), university-hosted annotated JSTOR scan.
    All 35 PDF pages visually read, including appendices and references. Printed page
    equals PDF page plus 93. Existing highlights and handwritten marks are not author
    errata; the 2015 download stamp is not the publication date. Section 2 explicitly
    defines MCEM as the comparison method. Curator algebraic deductions are distinguished
    from historical empirical results or uninspected software.
- evidence_id: stochasticapproximationexpectationmaximization-source-0
  kind: primary_source
  reference: https://oa.ee.tsinghua.edu.cn/ouzhijian/pgm/pgm-pdf/Delyon99_Convergence%20of%20a%20Stochastic%20Approximation%20Version%20of%20the%20EM%20Algorithm.pdf
  locator: Section 3 Eq6 and following paragraph, p.97 / PDF4; Section 3 Eq11 and
    Hessian prose, p.99 / PDF6; Section 3 Eq6, pp.97-98 / PDF4-5; M1-M5, pp.99-100
    / PDF6-7; Section 6 Eq30, p.107 / PDF14; Section 3 Eq6, pp.97-98 / PDF4-5; Section
    6 Eq30, p.107 / PDF14; Section 6 SAEM1-SAEM4 and Theorem 5, pp.107-109 / PDF14-16;
    Sections 5.1 and 7, pp.104-106 and 110-113 / PDF11-13 and 17-20; Eq26 and Eq48-55
  accessed_at: '2026-10-12T03:50:09Z'
  snapshot_sha256: f2c7a8005a1dee0a14bb243cb0bb2cb135227b1e9bff459eb07b3d0e6cc0b9bf
  support: supports
  summary: Convergence of a stochastic approximation version of the EM algorithm.
    Annals of Statistics 27(1):94-128 (1999), university-hosted annotated JSTOR scan.
    All 35 PDF pages visually read, including appendices and references. Printed page
    equals PDF page plus 93. Existing highlights and handwritten marks are not author
    errata; the 2015 download stamp is not the publication date. Section 2 explicitly
    defines MCEM as the comparison method. Curator algebraic deductions are distinguished
    from historical empirical results or uninspected software.
- evidence_id: stochasticapproximationexpectationmaximization-source-1
  kind: primary_source
  reference: https://www.numdam.org/article/PS_2004__8__115_0.pdf
  locator: Section 2.3 Eq8-10, p.119 / PDF5; compare 1999 Section 3 Eq6 and Eq11,
    pp.97,99 / PDF4,6
  accessed_at: '2026-10-12T03:50:08Z'
  snapshot_sha256: 48f3b9861570d00ae772287633202a42b06fcaa2cb44ad528d2fcf437bd1838b
  support: supports
  summary: 'Coupling a stochastic approximation version of EM with an MCMC procedure.
    ESAIM: Probability and Statistics 8:115-131, August 2004, Numdam-hosted full journal
    PDF. All 17 pages visually read, including three tables, proof, appendix and references.
    Printed page equals PDF page plus 114. Curator algebraic deductions are distinguished
    from historical empirical results or uninspected software.'
- evidence_id: markovchainmontecarlostochasticapproximationexpectationmaximization-source-0
  kind: primary_source
  reference: https://www.numdam.org/article/PS_2004__8__115_0.pdf
  locator: Lemma 1 and proof conclusion, p.123 / PDF9; deconvolution sufficient statistics,
    p.124 / PDF10; Appendix Eq25-26, p.130 / PDF16; Section 2.2 Eq5-6, p.119 / PDF5;
    Section 3 discussion of Markovian noise, p.120 / PDF6; finite kernel calculation
    in discovery ledger; Section 2.2, p.119 / PDF5, three-step algorithm and Pi_theta=P_theta^M;
    Section 3 SAEM3-prime and Theorem 1, pp.120-123 / PDF6-9; Appendix pp.129-130
    / PDF15-16; Sections 2.1-2.2, Eq4-5, pp.118-119 / PDF4-5
  accessed_at: '2026-10-12T03:50:08Z'
  snapshot_sha256: 48f3b9861570d00ae772287633202a42b06fcaa2cb44ad528d2fcf437bd1838b
  support: supports
  summary: 'Coupling a stochastic approximation version of EM with an MCMC procedure.
    ESAIM: Probability and Statistics 8:115-131, August 2004, Numdam-hosted full journal
    PDF. All 17 pages visually read, including three tables, proof, appendix and references.
    Printed page equals PDF page plus 114. Curator algebraic deductions are distinguished
    from historical empirical results or uninspected software.'
- evidence_id: markovchainmontecarlostochasticapproximationexpectationmaximization-source-1
  kind: primary_source
  reference: https://oa.ee.tsinghua.edu.cn/ouzhijian/pgm/pgm-pdf/Delyon99_Convergence%20of%20a%20Stochastic%20Approximation%20Version%20of%20the%20EM%20Algorithm.pdf
  locator: Section 6 Eq30 and exact conditional-draw assumption, pp.107-109 / PDF14-16;
    baseline statistic recursion and simulation assumption replaced by the 2004 Markovian
    extension
  accessed_at: '2026-10-12T03:50:09Z'
  snapshot_sha256: f2c7a8005a1dee0a14bb243cb0bb2cb135227b1e9bff459eb07b3d0e6cc0b9bf
  support: supports
  summary: Convergence of a stochastic approximation version of the EM algorithm.
    Annals of Statistics 27(1):94-128 (1999), university-hosted annotated JSTOR scan.
    All 35 PDF pages visually read, including appendices and references. Printed page
    equals PDF page plus 93. Existing highlights and handwritten marks are not author
    errata; the 2015 download stamp is not the publication date. Section 2 explicitly
    defines MCEM as the comparison method. Curator algebraic deductions are distinguished
    from historical empirical results or uninspected software.
assessments:
- assessment_id: montecarloexpectationmaximization
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:MonteCarloExpectationMaximization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - montecarloexpectationmaximization-source-0
  summary: MCEM approximates the E-step of a latent-data fitting procedure. It differs
    from recursive objective averaging in SAEM, conditional expectation of a completed-data
    estimator in ICE, and Bayesian data-augmentation sampling of the parameter itself.
    Specialized synthetic-data or image-model applications do not exhaust this general
    algorithm. All 442 pinned AIO labels/scoped synonyms and 470 preceding native
    IDs, names and aliases were compared with no normalized identity match. Ignored-inclusive
    whole-checkout fixed-string searches found 218 matched lines in each checkout;
    context windows for all 41 distinct matched texts were read. BayesianDataAugmentation,
    HiddenMarkovTree and IterativeConditionalEstimation mention applications or adjacent
    estimators, not these identities. All 225 semantic label/synonym rows were recomputed
    and verified identical to the preceding fully read inventory. Sixteen annotated
    AIO nodes and outgoing edges comprise fourteen verified prior readings and two
    new readings. Thirty-four contextual YAMLs comprise twenty-seven byte-verified
    prior readings and seven full new readings. Absence is bounded to this pin, maintained
    corpus and inspected neighborhood. No normalized name/alias matches among 442
    pinned and 470 maintained records. BayesianDataAugmentation, HiddenMarkovTree
    and IterativeConditionalEstimation matches are applications or adjacent estimators,
    not duplicate generic MCEM, SAEM or MCMC-SAEM records. The inspected sufficient-statistic
    maximization and fixed-data scope distinguish SAEM from averaged parameter gradients,
    ICE and sequential-task continual learning. Persistent Markovian simulation distinguishes
    the MCMC extension from the exact-conditional-draw base theorem.
  details: 'At current theta_k, obtain m_k latent completions from the conditional
    law p(z|y;theta_k). For candidate theta form Q_hat_k(theta)=m_k^(-1) sum_j log
    f(y,z_kj;theta), and maximize over theta to obtain the next fit. The simulated
    completions remain fixed while this sampled objective is optimized. The baseline
    MCEM calculation replaces the preceding sampled objective at each iteration; it
    does not recursively average objectives from earlier parameter values. The Monte
    Carlo average is taken over complete log objectives or their sufficient statistics
    before maximization. In general this is different from averaging the complete-data
    maximizer over imputations. A MAP objective can be represented by an appropriate
    complete log posterior, but simulating latent completions at a current parameter
    does not by itself sample a posterior distribution over that parameter. Maximizing
    a finite sampled Q does not certify improvement of the exact Q or observed likelihood.
    The saved valid Gaussian example gives an MCEM update with lower observed likelihood
    than its starting value. Monte Carlo count, dependence and integration error require
    their own analysis; apparently stable parameters or the exact-EM ascent argument
    alone do not establish convergence of this stochastic procedure. Limitations:
    The full mechanism source inspected here is the 1999 primary SAEM paper, which
    explicitly presents MCEM for comparison. The original Wei-Tanner 1990 paper was
    identified through publisher metadata/abstract but its university PDF returned
    403; no unseen original proofs or poor-man data-augmentation details are claimed.
    The simple unweighted sample mean requires draws from the intended conditional
    law. MCMC samples are generally dependent and need appropriate exploration/ergodicity
    conditions; importance sampling requires its own weighting. A local-observation
    heuristic is not certified full-posterior sampling. Finite Monte Carlo noise can
    persist near a stationary point. No generic fixed-sample-size convergence theorem,
    universal rate, adaptive sample-size rule or global optimum is asserted. The complete
    objective must be well defined and its maximization admissible. Boundary or unbounded
    likelihoods, nonidentifiability, poor initialization and numerical errors remain
    model-specific limitations. All 35 pages of the comparison source were read. Finite
    algebraic checks are curator examples, not historical software, a reproduced fit
    or empirical performance evidence.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A source-defined incomplete-data fitting algorithm, not a trained
      model instance, sampling target or learning task.
    evidence_ids:
    - montecarloexpectationmaximization-source-0
  - name: aio-assessment
    value: related_match
    definition: 'Sixteen annotated AIO nodes with outgoing edges and 34 contextual
      YAMLs were assessed against the pinned source. All three fitting algorithms
      have related_match to MachineLearningTask: this is algorithm-to-task context,
      not is-a. MCMC-SAEM additionally has related_match to MarkovChain because a
      conditional-target process is an explicit component. TrainingStrategy, transformation
      DataAugmentation, ContinualLearning, generic Model and fixed/random-effect model
      classes do not identify these fitting procedures. The 225 semantic rows were
      recomputed and byte-verified against the preceding fully read inventory; 14
      nodes and 27 YAMLs reuse hash-verified prior readings, with two new nodes and
      seven new YAMLs fully read this round.

      '
    evidence_ids:
    - mapping
- assessment_id: stochasticapproximationexpectationmaximization
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:StochasticApproximationExpectationMaximization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - stochasticapproximationexpectationmaximization-source-0
  - stochasticapproximationexpectationmaximization-source-1
  summary: The Delyon-Lavielle-Moulines SAEM construction fits a fixed observed data
    set while stochastic approximation controls integration noise. It is distinct
    from fresh-batch MCEM, stochastic-gradient parameter steps, parameter-iterate
    averaging, and online learning from newly arriving observations. A persistent
    MCMC simulation step is a separately scoped extension because exact conditional
    draws and Markovian perturbations require different arguments. All 442 pinned
    AIO labels/scoped synonyms and 470 preceding native IDs, names and aliases were
    compared with no normalized identity match. Ignored-inclusive whole-checkout fixed-string
    searches found 218 matched lines in each checkout; context windows for all 41
    distinct matched texts were read. BayesianDataAugmentation, HiddenMarkovTree and
    IterativeConditionalEstimation mention applications or adjacent estimators, not
    these identities. All 225 semantic label/synonym rows were recomputed and verified
    identical to the preceding fully read inventory. Sixteen annotated AIO nodes and
    outgoing edges comprise fourteen verified prior readings and two new readings.
    Thirty-four contextual YAMLs comprise twenty-seven byte-verified prior readings
    and seven full new readings. Absence is bounded to this pin, maintained corpus
    and inspected neighborhood. No normalized name/alias matches among 442 pinned
    and 470 maintained records. BayesianDataAugmentation, HiddenMarkovTree and IterativeConditionalEstimation
    matches are applications or adjacent estimators, not duplicate generic MCEM, SAEM
    or MCMC-SAEM records. The inspected sufficient-statistic maximization and fixed-data
    scope distinguish SAEM from averaged parameter gradients, ICE and sequential-task
    continual learning. Persistent Markovian simulation distinguishes the MCMC extension
    from the exact-conditional-draw base theorem.
  details: 'Simulate latent completions under the current conditional law and update
    Q_k(theta)=(1-gamma_k)Q_(k-1)(theta)+gamma_k times the current sample mean of
    complete log objectives. Maximize Q_k to obtain the next parameter. For the stated
    curved exponential family, store sufficient statistics instead: s_k=s_(k-1)+gamma_k(S(z_k)-s_(k-1)),
    followed by theta_k=theta_hat(s_k). The one-draw construction can therefore retain
    past information without storing every prior completion. The single-draw stationary-set
    theorem requires a smooth curved-exponential complete model and maximizer map,
    exact conditional simulation given the past, finite continuous second moments,
    step sizes in [0,1] with divergent sum and finite sum of squares, and almost-sure
    containment of the statistic iterates in a compact subset of their domain. Under
    those hypotheses the distance to the stated stationary sets tends to zero. Step-size
    conditions alone do not supply stability, point convergence, a global maximum
    or observed-likelihood ascent at every iteration. Recursive averaging of the expected
    objective precedes its maximization. Optional averaging of fitted parameter iterates
    is a separate operation with additional local stability, moment and step-size
    conditions. Averaging statistics before a nonlinear maximizer need not equal averaging
    parameter values. Simulation-iteration uncertainty around a fixed-data solution
    is distinct from sampling uncertainty of the statistical estimator. In Eq6, gamma=0
    freezes the accumulated objective, while gamma=1 replaces it by the current Monte
    Carlo objective; the paragraph identifying gamma=0 with ordinary stochastic EM
    is inconsistent with that recursion. The 1999 covariance prose also reverses the
    Hessian sign: its H=G-Delta Delta^T estimates the observed log Hessian, while
    observed information is -H, as explicitly used in the 2004 follow-up. These printed
    statements are not used as implementation rules. Limitations: The core mechanism
    is supported independently of the source’s stronger local-maximizer and averaging
    claims. Those results need additional isolated-stationary-point, curvature, excitation
    and local-rate hypotheses. Their printed exposition contains sign/wording inconsistencies;
    no blanket theorem repair or global convergence certification is claimed. A finite
    stochastic update need not increase the observed likelihood. The finite Gaussian
    example lowers it even with a positive averaging weight; stabilization and convergence
    need separate arguments. The source’s expanding-compact reset scheme, approximate
    conditional maximizations and stochastic-gradient extensions introduce additional
    assumptions. They are not silently covered by the core exact-maximizer theorem.
    The source’s Eq27 average-noise expression omits a Jacobian factor present in
    its later proof, and its Section 8 Newton direction and convexity wording conflict
    with concave maximization. These extension formulas are not implemented or endorsed
    by this record. Independent exact conditional draws are an assumption of the inspected
    base theorem, not a property of a short MCMC run. The separately scoped MCMC-SAEM
    extension handles a different noise structure. All 52 pages of the two primary
    papers were read. No author software, historical fit, empirical speed comparison
    or uncertainty-calibration study was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A source-defined incomplete-data fitting algorithm, not a trained
      model instance, sampling target or learning task.
    evidence_ids:
    - stochasticapproximationexpectationmaximization-source-0
    - stochasticapproximationexpectationmaximization-source-1
  - name: aio-assessment
    value: related_match
    definition: 'Sixteen annotated AIO nodes with outgoing edges and 34 contextual
      YAMLs were assessed against the pinned source. All three fitting algorithms
      have related_match to MachineLearningTask: this is algorithm-to-task context,
      not is-a. MCMC-SAEM additionally has related_match to MarkovChain because a
      conditional-target process is an explicit component. TrainingStrategy, transformation
      DataAugmentation, ContinualLearning, generic Model and fixed/random-effect model
      classes do not identify these fitting procedures. The 225 semantic rows were
      recomputed and byte-verified against the preceding fully read inventory; 14
      nodes and 27 YAMLs reuse hash-verified prior readings, with two new nodes and
      seven new YAMLs fully read this round.

      '
    evidence_ids:
    - mapping
- assessment_id: markovchainmontecarlostochasticapproximationexpectationmaximization
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - markovchainmontecarlostochasticapproximationexpectationmaximization-source-0
  - markovchainmontecarlostochasticapproximationexpectationmaximization-source-1
  summary: MCMC-SAEM replaces exact conditional latent draws in base SAEM by transitions
    from a carried state, often a fixed number of Metropolis-Hastings steps per parameter
    update. This differs from running an independent full equilibrium sampler at every
    iteration, fresh-batch MCEM and posterior sampling of the parameter itself. The
    Markov kernel changes with the fitted parameter. All 442 pinned AIO labels/scoped
    synonyms and 470 preceding native IDs, names and aliases were compared with no
    normalized identity match. Ignored-inclusive whole-checkout fixed-string searches
    found 218 matched lines in each checkout; context windows for all 41 distinct
    matched texts were read. BayesianDataAugmentation, HiddenMarkovTree and IterativeConditionalEstimation
    mention applications or adjacent estimators, not these identities. All 225 semantic
    label/synonym rows were recomputed and verified identical to the preceding fully
    read inventory. Sixteen annotated AIO nodes and outgoing edges comprise fourteen
    verified prior readings and two new readings. Thirty-four contextual YAMLs comprise
    twenty-seven byte-verified prior readings and seven full new readings. Absence
    is bounded to this pin, maintained corpus and inspected neighborhood. No normalized
    name/alias matches among 442 pinned and 470 maintained records. BayesianDataAugmentation,
    HiddenMarkovTree and IterativeConditionalEstimation matches are applications or
    adjacent estimators, not duplicate generic MCEM, SAEM or MCMC-SAEM records. The
    inspected sufficient-statistic maximization and fixed-data scope distinguish SAEM
    from averaged parameter gradients, ICE and sequential-task continual learning.
    Persistent Markovian simulation distinguishes the MCMC extension from the exact-conditional-draw
    base theorem.
  details: 'From the retained latent state z_(k-1), apply a transition Pi_(theta_k)
    with invariant target p(z|y;theta_k), obtaining z_k. Use it in s_k=s_(k-1)+gamma_k(S(y,z_k)-s_(k-1)),
    then set theta_(k+1)=theta_hat(s_k). The kernel can comprise M Metropolis-Hastings
    steps. Retain rejected states and accepted updates; restart or discarded-rejection
    variants define different simulation schemes. Metropolis-Hastings acceptance includes
    the reverse-to-forward proposal ratio. When an independence proposal is the current
    latent prior, prior factors cancel and the observed conditional likelihood ratio
    remains. Invariance of the target does not mean one or finitely many transitions
    from an arbitrary state produce that target distribution. The finite two-state
    example preserves its target yet has a different first-step distribution and nonzero
    conditional sampling error. The published analysis imposes the curved-exponential
    model and smooth maximizer assumptions, stochastic-approximation step sizes, compact
    latent states, bounded sufficient statistics, parameter regularity of transitions,
    uniform ergodicity and compact statistic iterates. Its stationary-set conclusion
    is conditional on these hypotheses. A fixed number of arbitrary MCMC moves, irreducibility
    alone or bounded latent support alone does not supply them. The stated Lemma 1
    uses exponents 1/alpha for alpha in (0,1), whereas its appendix derives Holder
    exponents below one. The subsequent lambda=1 conclusion does not directly follow
    from the displayed weaker estimate. The beta deconvolution example also has log(z)
    and log(1-z) statistics unbounded near the endpoints, despite bounded latent support.
    These discrepancies limit what is certified from the printed proof and example;
    the record does not supply a repaired general convergence proof. Limitations:
    A target-invariant transition can mix poorly or be periodic. A finite irreducible
    periodic flip chain demonstrates why irreducibility alone does not imply convergence
    to equilibrium. Markovian simulation errors are not generally conditionally mean-zero
    at each iteration. The exact-independent-draw martingale argument cannot be transplanted
    without the additional Markovian-noise analysis. The theorem’s bounded-statistic
    condition is separate from compact support. Truncating a latent law may change
    the statistical model and requires an explicit choice; no automatic equivalence
    to an unbounded original model is asserted. The deconvolution coordinate pseudocode
    ambiguously refers to old coordinates within its sweep, and its stated uniform
    beta initialization is inconsistent with ordinary shape parameters. The record
    specifies persistent transitions and does not reproduce those ambiguous implementation
    details. The source’s simulations can reach different local solutions. Its truth-centered
    empirical squared-error matrix is not generally covariance about the estimator
    mean when bias is present; no finite-sample interval coverage or universal speed
    guarantee is asserted. All 52 pages of the two primary papers were read. Finite
    kernel and algebra checks are curator examples, not source software, a historical
    model fit or independent validation of the general proof.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A source-defined incomplete-data fitting algorithm, not a trained
      model instance, sampling target or learning task.
    evidence_ids:
    - markovchainmontecarlostochasticapproximationexpectationmaximization-source-0
    - markovchainmontecarlostochasticapproximationexpectationmaximization-source-1
  - name: aio-assessment
    value: related_match,related_match
    definition: 'Sixteen annotated AIO nodes with outgoing edges and 34 contextual
      YAMLs were assessed against the pinned source. All three fitting algorithms
      have related_match to MachineLearningTask: this is algorithm-to-task context,
      not is-a. MCMC-SAEM additionally has related_match to MarkovChain because a
      conditional-target process is an explicit component. TrainingStrategy, transformation
      DataAugmentation, ContinualLearning, generic Model and fixed/random-effect model
      classes do not identify these fitting procedures. The 225 semantic rows were
      recomputed and byte-verified against the preceding fully read inventory; 14
      nodes and 27 YAMLs reuse hash-verified prior readings, with two new nodes and
      seven new YAMLs fully read this round.

      '
    evidence_ids:
    - mapping
- assessment_id: integration-before-maximization
  area: consistency
  topic: Objective integration versus estimator averaging
  outcome: supported
  target_ids:
  - AIMech:MonteCarloExpectationMaximization
  - AIMech:StochasticApproximationExpectationMaximization
  evidence_ids:
  - montecarloexpectationmaximization-source-0
  - stochasticapproximationexpectationmaximization-source-0
  - neighbors
  - finite-boundaries
  summary: Retain MCEM and SAEM as distinct accumulation rules.
  details: MCEM forms a fresh conditional Monte Carlo objective at each fitted parameter.
    SAEM recursively averages complete objectives or sufficient statistics before
    maximization. ICE averages completed-data estimators instead, while averaged SGD
    averages parameter iterates. The finite log-variance example yields log(5) versus
    log(3), showing that nonlinear maximization and averaging do not commute. Fixed
    observed data distinguishes these procedures from incoming-observation online
    learning.
- assessment_id: finite-ascent
  area: consistency
  topic: Stochastic update versus exact likelihood improvement
  outcome: supported
  target_ids:
  - AIMech:MonteCarloExpectationMaximization
  - AIMech:StochasticApproximationExpectationMaximization
  evidence_ids:
  - montecarloexpectationmaximization-source-0
  - stochasticapproximationexpectationmaximization-source-0
  - finite-boundaries
  summary: Do not inherit per-step exact-EM ascent.
  details: For the normalized complete model p(y,z|theta)=N(y;theta,1)N(z;theta,1)
    at observed y=0, theta=1 and accumulated statistic 2, exact EM gives theta=0.5.
    A possible Monte Carlo sample mean 3 gives MCEM theta=1.5 and SAEM with gamma=0.25
    theta=1.125. Observed log likelihood changes from -0.5 to -1.125 or -0.6328125,
    respectively. These are finite deterministic sample-summary examples, not claimed
    random trials, global theorems or performance comparisons.
- assessment_id: saem-assumptions
  area: consistency
  topic: Exact conditional simulation, stability and printed discrepancies
  outcome: supported
  target_ids:
  - AIMech:StochasticApproximationExpectationMaximization
  evidence_ids:
  - stochasticapproximationexpectationmaximization-source-0
  - stochasticapproximationexpectationmaximization-source-1
  - finite-boundaries
  summary: Keep the core recursion and theorem hypotheses separate from problematic
    extension formulas.
  details: Section 6 requires the curved-exponential model, smooth maximizer, exact
    conditional law given the past, moments, step sizes and compact statistic iterates.
    It gives stationary-set approach under those assumptions, not an unconditional
    global maximum. Local maximizer and averaging conclusions require further curvature/excitation/stability
    hypotheses. Eq6 with gamma=0 freezes and gamma=1 replaces; source prose reverses
    the SEM endpoint. The complete-Hessian plus score-outer expression is an observed
    Hessian, and the 2004 follow-up correctly uses -H for information. The Eq27 omitted
    Jacobian and Section 8 Newton/convexity wording remain documented limitations,
    not implemented rules.
- assessment_id: persistent-kernel
  area: consistency
  topic: Invariant target, finite transitions and changing parameters
  outcome: supported
  target_ids:
  - AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization
  evidence_ids:
  - markovchainmontecarlostochasticapproximationexpectationmaximization-source-0
  - markovchainmontecarlostochasticapproximationexpectationmaximization-source-1
  - neighbors
  - finite-boundaries
  summary: Retain MCMC-SAEM as a persistent-chain extension.
  details: At current parameter the retained state advances under a conditional-target
    kernel, then updates statistics and the maximizer. Reverse proposal ratios and
    retained rejections matter. In the exact rational example, target (3/11,8/11)
    is invariant for K=((3/5,2/5),(3/20,17/20)), yet a first transition from state
    zero is (3/5,2/5) and conditional statistic noise is -18/55. A second transition
    uses the retained distribution. Target invariance is therefore distinct from finite-run
    equilibration and exact conditional unbiasedness; parameter changes add another
    noise issue.
- assessment_id: markov-proof-scope
  area: consistency
  topic: Ergodicity, bounded statistics and Holder estimates
  outcome: supported
  target_ids:
  - AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization
  evidence_ids:
  - markovchainmontecarlostochasticapproximationexpectationmaximization-source-0
  - finite-boundaries
  summary: Preserve the unresolved printed-proof limitations.
  details: The stated analysis imposes compact latent support, bounded statistics,
    transition regularity, uniform ergodicity and stable statistic iterates as well
    as model and step-size assumptions. A finite irreducible periodic flip has an
    invariant target but no approach from a point start. Beta log statistics are unbounded
    near endpoints despite bounded latent support. Lemma 1 prints exponent 1/alpha
    with alpha<1 while the appendix derives exponents below one; its immediate lambda=1
    step is not established by that weaker estimate. Finite ratio checks expose these
    distinctions but neither repair the proof nor assert that every convergence conclusion
    is false.
- assessment_id: implementation-and-evaluation
  area: consistency
  topic: Pseudocode ambiguities, covariance and empirical scope
  outcome: supported
  target_ids:
  - AIMech:StochasticApproximationExpectationMaximization
  - AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization
  evidence_ids:
  - stochasticapproximationexpectationmaximization-source-0
  - markovchainmontecarlostochasticapproximationexpectationmaximization-source-0
  - finite-boundaries
  summary: Do not promote source examples to certified implementations.
  details: The 2004 coordinate sweep refers ambiguously to old coordinates, and its
    uniform beta initialization is incompatible with ordinary shape parameters. No
    author code was inspected to resolve these details. Truth-centered squared errors
    need not be estimator-mean covariance under bias. Simulation-iteration uncertainty
    differs from statistical-estimator uncertainty. Tables were visually read with
    their labels; no historical fit, speed comparison or interval coverage was reproduced.
- assessment_id: source-and-mapping-scope
  area: grounding
  topic: Bounded source access, aliases and AIO abstraction
  outcome: supported
  target_ids:
  - AIMech:MonteCarloExpectationMaximization
  - AIMech:StochasticApproximationExpectationMaximization
  - AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - montecarloexpectationmaximization-source-0
  - markovchainmontecarlostochasticapproximationexpectationmaximization-source-0
  summary: Retain three native algorithms with related mappings and DRAFT status.
  details: All 52 pages of two primary PDFs were read. The original 1990 MCEM full
    PDF returned 403, and its uninspected posterior variants are excluded; the 1999
    full primary comparison supplies the generic mechanism. Scan annotations are not
    author errata. No normalized identity matches were found in 442 AIO and 470 preceding
    native records. Both ignored-inclusive checkout searches and all 41 distinct matching
    windows were inspected. Three algorithm-to-task related mappings and the MCMC
    algorithm-to-Markov-process relation do not assert subclasses or upstream acceptance.
    Three new provisional cohorts leave 404 pending entries; no saturation.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:MonteCarloExpectationMaximization
  - AIMech:StochasticApproximationExpectationMaximization
  - AIMech:MarkovChainMonteCarloStochasticApproximationExpectationMaximization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - montecarloexpectationmaximization-source-0
  - stochasticapproximationexpectationmaximization-source-0
  - stochasticapproximationexpectationmaximization-source-1
  - markovchainmontecarlostochasticapproximationexpectationmaximization-source-0
  - markovchainmontecarlostochasticapproximationexpectationmaximization-source-1
  rationale: Fresh conditional integration, recursive objective/statistic averaging
    and persistent Markovian simulation have distinct operations and assumptions.
    A shared EM purpose does not establish identity. Related algorithm-to-task and
    algorithm-to-process mappings preserve abstraction without asserting subclasses.
limitations:
- Adversarial author self-review only; all three records remain DRAFT.
- The first vendored-check failed because the sandbox could not resolve the public
  host; the authorized network-enabled rerun verified all 22 pinned artifacts.
- All 35 pages of Delyon-Lavielle-Moulines 1999 and all 17 pages of Kuhn-Lavielle
  2004 were visually read, including proofs, appendices, tables and references. Printed
  pages equal PDF pages plus 93 and 114 respectively.
- The university-hosted 1999 scan contains pre-existing highlights, red boxes and
  handwritten marks. These are not treated as author errata. The 2015 download stamp
  is not its publication date.
- The Wei-Tanner 1990 original MCEM PDF returned 403. Its publisher title, authors,
  DOI and abstract were inspected; source-specific posterior approximation variants
  and unseen proofs are not asserted. The 1999 full primary paper explicitly defines
  the generic MCEM algorithm used here.
- 'Source discrepancies are recorded rather than silently repaired: 1999 zero-step,
  information/Hessian signs, average-noise Jacobian, local-curvature wording and Newton
  direction; 2004 Holder exponents/proof step, bounded-support versus bounded-statistic
  assumption, beta initialization and coordinate-sweep ambiguity.'
- Core method definitions, conditional asymptotic conclusions, per-iteration likelihood
  ascent and finite-sample calibration are different claims. No repaired general convergence
  proof is supplied.
- Finite Gaussian, nonlinear-averaging, exact rational Markov-kernel and sign/endpoint
  examples are curator calculations. No source software, historical fit, runtime comparison
  or coverage experiment was reproduced. Full PDFs are not redistributed.
- Initial validate-curated identified an uncited base-SAEM source in MCMC-SAEM; its
  precise baseline recursion/conditional-draw locator was added as contextual evidence.
  The rerun validated all 473 native records with zero errors before formal review.
- Three provisional source cohorts leave 404 pending frontier entries and additional
  unresolved dispositions. Exact new-label searches included ignored/hidden files,
  but do not prove all underlying methods are novel. No saturation is claimed.
links: []
tags:
- native-concepts
- monte-carlo-and-stochastic-approximation-em
- self-review
- discovery-ongoing
```
