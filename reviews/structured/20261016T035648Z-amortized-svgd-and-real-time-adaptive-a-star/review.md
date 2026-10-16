# Scientific self-review of amortized SVGD and Real-Time Adaptive A-star

- Review: 20261016T035648Z-amortized-svgd-and-real-time-adaptive-a-star
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-16T03:56:43.125821Z
- Finished UTC: 2026-10-16T03:56:48.278280Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain amortized SVGD and Real-Time Adaptive A-star as separate source-scoped DRAFT algorithms. Fourteen claims and18 limitations preserve the generic sampler fitting/projection boundaries and the RTAA planning/update/execution controller with its own theorem and later-comparison scope. Exact current and inherited source responsibilities remain pending where appropriate.

## Scope And Provenance

Two exact current native records from accepted cohort359 creation; all selected claims and limitations assessed. Historical source and neighbor reading scopes remain separately attributed.

Selection: Exact AIMech:AmortizedSteinVariationalGradientDescent, AIMech:RealTimeAdaptiveAStar.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 0f7e2c5df224901e9284a883dfd0457fd4c29375.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AmortizedSteinVariationalGradientDescent | data/curated/AmortizedSteinVariationalGradientDescent.yaml | maintained | Amortized Stein variational gradient descent |
| AIMech:RealTimeAdaptiveAStar | data/curated/RealTimeAdaptiveAStar.yaml | maintained | Real-Time Adaptive A* |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:AmortizedSteinVariationalGradientDescent, AIMech:RealTimeAdaptiveAStar | Actual completed command exited0; exact output and timing retained. |
| just vendored-check | passed | True | AIMech:AmortizedSteinVariationalGradientDescent, AIMech:RealTimeAdaptiveAStar | Actual completed command exited0; exact output and timing retained. |
| uv run --locked aimech check-source | passed | True | AIMech:AmortizedSteinVariationalGradientDescent, AIMech:RealTimeAdaptiveAStar | Actual completed command exited0; exact output and timing retained. |
| just render | passed | True | AIMech:AmortizedSteinVariationalGradientDescent, AIMech:RealTimeAdaptiveAStar | Actual completed command exited0; exact output and timing retained. |
| just render-check | passed | True | AIMech:AmortizedSteinVariationalGradientDescent, AIMech:RealTimeAdaptiveAStar | Actual completed command exited0; exact output and timing retained. |
| git diff --check | passed | True | AIMech:AmortizedSteinVariationalGradientDescent, AIMech:RealTimeAdaptiveAStar | Actual completed command exited0; exact output and timing retained. |
| just vendored-check (retained earlier attempt) | failed | False | AIMech:AmortizedSteinVariationalGradientDescent, AIMech:RealTimeAdaptiveAStar | Historical unsuccessful attempt retained; later exact required command passed. |

## Scientific And Domain Assessments

### Amortized Stein variational gradient descent: implicit-sampler

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Problem1 explicitly permits a differentiable simulator queried through outputs and parameter derivatives, with sampled seeds of unknown density. Generic scope is retained; density-based theoretical claims have narrower regularity requirements.

### Amortized Stein variational gradient descent: particle-direction

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

The empirical Stein field uses the target-score attraction term and first-argument kernel derivative from the same pre-update outputs. The formula uses a minibatch mean; no ordinary KL gradient or unbiasedness is inferred.

### Amortized Stein variational gradient descent: output-projection

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Eqs.8/13 specify regression to displaced old outputs. Frozen targets and same seeds are necessary for the stated fitting derivative; this is source interpretation plus explicit mathematical convention, not a source-code audit.

### Amortized Stein variational gradient descent: parameter-step

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Differentiating the frozen-target squared loss gives negative 2*epsilon*sum J^T v; descent is therefore positive. Source2016 Eq.9 and both practical positive steps support this; source2017 Eq.14 contradicts its own delta residual. Exact tangent projection A A^+ v and single fitting-gradient A A^T v differ.

### Amortized Stein variational gradient descent: learned-output-versus-particles

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Fresh-seed outputs are provided by the learned parameterized sampler. Approximation error remains; no invariant-chain or exact posterior claim follows.

### Amortized Stein variational gradient descent: application-boundaries

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Application sections add model learning, VAE entropy/model structure or trainable Langevin schedules. The generic method does not require these components; five separate source questions remain pending.

### Amortized Stein variational gradient descent: limitation 1

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Retained source and mathematical boundary, not an unqualified defect or empirical finding. No relaxation of the selected research limitation. Retained statement: A target score requires a differentiable continuous target on the relevant domain, finite positive normalization and regularity. An unknown multiplicative constant independent of the sampled variable cancels; arbitrary improper energies do not thereby become distributions.

### Amortized Stein variational gradient descent: limitation 2

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Retained source and mathematical boundary, not an unqualified defect or empirical finding. No relaxation of the selected research limitation. Retained statement: The infinitesimal Stein/KL argument concerns suitable population densities, moments, boundary integration and valid perturbations. A finite empirical particle measure is atomic; a finite/discrete-seed simulator can also have singular output. The algorithm can compute directions without an output density, but that alone does not make its population KL finite or justify density-based entropy identities.

### Amortized Stein variational gradient descent: limitation 3

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Retained source and mathematical boundary, not an unqualified defect or empirical finding. The independent audit provides smooth restricted-family stationarity and projected-KL counterexamples, so the restriction is not limited to rank-deficient Jacobians. Retained statement: Finite sampler capacity, restricted tangent directions, rank-deficient Jacobians, nonlinear fitting error, minibatch error and finite step size separate the parameter update from ideal unconstrained SVGD. A least-squares projection may have nonunique minimizers. Even a full-column-rank but restricted parameterization can have a stationary fitting update while the unrestricted Stein field is nonzero. No universal monotone KL descent, exact posterior recovery or global convergence is adopted.

### Amortized Stein variational gradient descent: limitation 4

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Retained source and mathematical boundary, not an unqualified defect or empirical finding. The source-local printed sign is preserved without silently repairing the primary artifact. Retained statement: The 2016 v1/v2 Eq.9 has eta_new=eta+epsilon*Delta_eta. The 2017 proceedings and arXiv:1707.06626v2 Eq.14 print a minus sign while minimizing &#124;&#124;J*delta-phi&#124;&#124;^2 and retaining positive Eq.15. The fitting target and first-order derivation support plus for this delta definition. Retain the printed discrepancy and use positive 2016 Eq.10/2017 Eq.15 for the practical step; no published erratum or inspected author implementation is claimed.

### Amortized Stein variational gradient descent: limitation 5

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Retained source and mathematical boundary, not an unqualified defect or empirical finding. No relaxation of the selected research limitation. Retained statement: Unit diagonal and zero first-argument diagonal derivative give the exact one-particle score-ascent reduction, as with a normalized RBF. Other kernels can change the scale or add a derivative. The 2016 p4 single-particle sentence is visibly missing the condition value; the 2017 p3 prints derivative=0 but unit-diagonal scaling still matters. Kernel richness, boundary conditions and positive nondegenerate bandwidth matter; repulsion does not guarantee all modes or prevent coincident outputs.

### Amortized Stein variational gradient descent: limitation 6

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Retained source and mathematical boundary, not an unqualified defect or empirical finding. No relaxation of the selected research limitation. Retained statement: The projected Stein field is not asserted to be the exact ordinary parameter gradient of KL. The paper relates it to a kernel-smoothed score difference under Stein conditions; this does not remove smoothing, projection or family restrictions. The output target is held fixed in the regression derivative, rather than differentiating through the target as an additional objective.

### Amortized Stein variational gradient descent: limitation 7

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Retained source and mathematical boundary, not an unqualified defect or empirical finding. No relaxation of the selected research limitation. Retained statement: SteinGAN replaces a model expectation with imperfect sampler outputs, so finite alternating updates are not automatically exact or unbiased MLE. Its gamma-weighted stabilization changes the objective; proper prior normalization is not established by calling exp(gamma*logZ) conjugate. Learned finite-step Langevin chains are not certified target-invariant or universally transferable by the reported experiments. Entropy-tempering requires a normalizable tempered target and meaningful entropy.

### Amortized Stein variational gradient descent: limitation 8

evidence: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Retained source and mathematical boundary, not an unqualified defect or empirical finding. No relaxation of the selected research limitation. Retained statement: 2016 v1/v2 differ in reported CIFAR values and caption gamma, not just typography; keep versions separate. UAI proceedings and later arXiv1707.06626v2 differ in bibliography (Snelson removed, Pu added), and only the latter downloaded artifact contains Appendices A–C. Empirical comparisons, image quality and speed claims are source-reported and not independently reproduced. No code or training was run.

### Amortized Stein variational gradient descent: sources and source scope

provenance: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Two primary evidence rows/two artifacts support the definition and claims. The2016v1 and later2017preprint remain fully bound research/version context, not unused support rows added to satisfy a count.

### Amortized Stein variational gradient descent: definition and source scope

identity: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Direct defining-method support from both primary full texts. Neural examples do not narrow Problem1 generic simulator scope.

### Amortized Stein variational gradient descent: identity and source scope

identity: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Retain the generic differentiable-sampler fitting procedure separately from unamortized interacting-particle SVGD, ordinary variational objectives and the composite SteinGAN/VAE/Langevin applications. No universal exact-sampling or stationarity-implies-target claim is adopted. Actual identity notes equal the fresh root decisions; exact historical/current differences remain in context_changes.

### Amortized Stein variational gradient descent: mapping and source scope

grounding: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

Both primary works explicitly train stochastic neural inference networks using this sampler-fitting procedure. This relates the algorithm to a documented neural-sampler implementation class; the generic differentiable-simulator definition also permits other parameterizations. It asserts neither algorithm/model identity nor subclass or broad-match inclusion, and does not make an ANN architecture mandatory. Actual root decisions supply current mapping assessments; the accepted source-scoped related mappings remain exact.

### Amortized Stein variational gradient descent: kind and source scope

identity: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent.

The record is a training algorithm for a parameterized stochastic sampler. A documented neural implementation is context; it is not a standalone trained model or a required neural architecture.

### Real-Time Adaptive A*: bounded-local-search

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

The positive expansion cap, selected next-to-expand node and explicit failure branch follow Figure1. CLOSED contains expanded states. The selected boundary is not an arbitrary OPEN state.

### Real-Time Adaptive A*: uniform-f-minus-g-learning

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

Only CLOSED is updated using one F. The defining text explicitly excludes ordinary OPEN states because their g values can still exceed shortest-path distances. Hand-derived M3 retains the distinction from the later paper’s broader wording.

### Real-Time Adaptive A*: execution-and-retention

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

The movement cap is independently chosen after learning; source lines13–16 allow increasing costs after actions and interrupt the remaining path when affected. Retention is across search episodes, not an assumed stationary environment.

### Real-Time Adaptive A*: consistency-and-completion

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

Theorems1–3 use the complete Section3/4 assumptions. Initial-state solvability alone does not give uniformly bounded goal distances from all states. The finite potential proof is not extended to arbitrary directed dead-end or stochastic domains.

### Real-Time Adaptive A*: repeated-trial-scope

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

Theorem4 additionally uses fixed-start resets, retained learning and a positive lower bound on nonzero increases. Its bounded nonoptimal-trial count is distinct from first-trial optimality or global exact learning.

### Real-Time Adaptive A*: lrta-comparison-boundary

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

Section5 names its 2004 larger-lookahead comparator. The one-lookahead result requires identical ties. The subsequent one-episode comparison starts with identical heuristics and explicitly disclaims dominance along different trajectories.

### Real-Time Adaptive A*: navigation-application

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

The defining study supports the navigation application and experimental setup. The claim does not reproduce numeric performance, absolute timing or universal superiority; reported domain and implementation limits remain.

### Real-Time Adaptive A*: later-comparator

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

The 2018 paper is primary evidence for its own later comparison, not the defining algorithm. Expansion-bounded runs, amortized CPU time and interpolation are explicit; source timing-label discrepancies remain and no absolute crossover value is asserted.

### Real-Time Adaptive A*: limitation 1

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

M2 shows why admissibility alone does not supply the monotone update theorem. The paper proposes inconsistent-heuristic extensions only as future work. Retained statement: The defining proofs assume finite states/actions, action costs bounded below by positive epsilon, and initial consistency with zero goal values; mere admissibility is insufficient for the same no-reopening A* and monotonic-update proof.

### Real-Time Adaptive A*: limitation 2

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

All-state bounded goal distances exclude reachable traps; the explicit failure branch is not a theorem of success from any initially solvable state. Retained statement: Goal reachability from only the initial state does not establish the source’s bounded-goal-distance assumption for all states. Reachable traps/dead ends are outside that completion theorem. OPEN-exhaustion failure is an explicit branch.

### Real-Time Adaptive A*: limitation 3

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

M4 exhibits why arbitrary decreases can invalidate admissibility. No changing-goal or stochastic extension is inferred. Retained statement: Costs may increase; arbitrary decreases, changing goals, stochastic transitions and moving-goal extensions are not covered by the defining theorem.

### Real-Time Adaptive A*: limitation 4

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

Expansion counts and a linear-sized assignment loop do not bound queue operations, successor generation, learned-heuristic storage or worst-case elapsed time. Retained statement: The lookahead cap bounds expansions, and the update takes one assignment per expanded state; it is not an unconditional wall-clock or total-memory guarantee. Successor generation, queue operations and accumulated learned h have implementation costs.

### Real-Time Adaptive A*: limitation 5

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

The repeated-trial hypotheses are retained separately from exploratory first execution. Retained statement: Exploratory trajectories may be suboptimal and repeated. Theorem4 is conditional on fixed-start repeated trials and lower-bounded nonzero cost increases; it does not guarantee optimal first execution.

### Real-Time Adaptive A*: limitation 6

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

The 2004 comparator, original one-state method and Adaptive A* remain distinct version/source questions; equality in a special case is not general identity. Retained statement: The 2006 paper calls a 2004 larger-lookahead LRTA variant LRTA*, not exclusively Korf’s original one-state method. Its equivalence result is lookahead one with identical ties; Adaptive A* complete-search and later RTAA variants are separate source/version questions.

### Real-Time Adaptive A*: limitation 7

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

Reported relative performance remains confined to its domains, heuristics and implementations. No algorithm/benchmark execution occurred. Retained statement: Reported relative advantages depend on domain, heuristic, lookahead, movement choice, tie handling, hardware and implementation. No universal superiority, monotonic lookahead benefit or reproduced benchmark is asserted.

### Real-Time Adaptive A*: limitation 8

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

The corrected literal center-axis label and unresolved aggregation are retained. Figure1 right caption versus time-axis wording is additionally preserved in source discrepancy context. No absolute timing or plotted-data correction is inferred. Retained statement: 2018 PDF2 prose says microseconds and 77.22us crossover, while visible plot axes on PDF3–5 say ms. The Figure1 center axis reads planning time (ms), without the per-episode qualifier used in nearby prose; actual aggregation remains unresolved. Preserve these inconsistencies and avoid absolute timing/crossover claims until clarified.

### Real-Time Adaptive A*: limitation 9

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

The 2018 traffic reset convention is an empirical protocol, not a repair of arbitrary directed dead-end completeness. Retained statement: The 2018 Traffic benchmark resets an agent with no successors to the start and reports collisions/restarts; this experiment does not extend the 2006 completion theorem to arbitrary directed dead-end graphs.

### Real-Time Adaptive A*: limitation 10

evidence: supported. Targets: AIMech:RealTimeAdaptiveAStar.

The unread thesis, implementation-comparison gap and failed publisher-PDF access remain scoped limitations; the author-hosted manuscript supplies inspected evidence. Retained statement: The 2018 authors did not compare original implementation code and defer statistical-anomaly details to an unread 2017 thesis. Neither claim is independently reproduced here. Publisher PDF access failed; author manuscript supplies the inspected evidence.

### Real-Time Adaptive A*: sources and source scope

provenance: supported. Targets: AIMech:RealTimeAdaptiveAStar.

Two primary evidence rows/two artifacts with distinct roles: 2006 defining method; 2018 later original empirical comparison. Two unread retrieval routes remain source questions, not support rows.

### Real-Time Adaptive A*: definition and source scope

identity: supported. Targets: AIMech:RealTimeAdaptiveAStar.

The defining 2006 algorithm and pseudocode directly support the complete controller. The later empirical paper is used in its own claim rather than added as unused definition evidence.

### Real-Time Adaptive A*: identity and source scope

identity: supported. Targets: AIMech:RealTimeAdaptiveAStar.

Retain the bounded forward-search, CLOSED-only F−g learning and capped-execution controller separately from ordinary A*, one-state LRTA, RTA second-best backup and LSS reverse-Dijkstra propagation. Special-case equality with identical ties does not establish general algorithm identity. Actual identity notes equal the fresh root decisions; exact historical/current differences remain in context_changes.

### Real-Time Adaptive A*: mapping and source scope

grounding: supported. Targets: AIMech:RealTimeAdaptiveAStar.

Persistent state-heuristic learning from repeated search experience supplies a weak relation to the pinned task context. The bounded forward-search, CLOSED-only F−g update and movement controller are not identical to a general task class. This proposal asserts neither exact equivalence nor subclass inclusion and does not identify the algorithm with a sampled reinforcement-learning method. Actual root decisions supply current mapping assessments; the accepted source-scoped related mappings remain exact.

### Real-Time Adaptive A*: kind and source scope

identity: supported. Targets: AIMech:RealTimeAdaptiveAStar.

The record is a real-time heuristic search algorithm with persistent learned state heuristics. Its specific planning/update/execution controller is not identical to a general machine-learning task or a sampled reinforcement-learning method.

### Actual canonical creation and separate source responsibilities

provenance: supported. Targets: AIMech:AmortizedSteinVariationalGradientDescent, AIMech:RealTimeAdaptiveAStar.

Actual records retain14 claims and18 limitations, four source rows and four distinct artifacts: three defining method artifacts and one2018 later comparison. Five exclusive creation outputs and one CREATE event are bound. Current dynamic owner changes and additions exactly follow the accepted plan: {"additional_source_question_count": 0, "bibliography_occurrences": 125, "changed_main_indexes": [8, 909], "changed_nested_indexes": [393], "main": 914, "nested": 394, "new_main_rows": 0, "new_nested_rows": 0}. Separate responsibility for125 bibliography occurrences and19 original/dossier/retrieval objects, plus additional current questions, is retained. The complete actual358 predecessor bundle preserves402/404/406,356 local questions,357 Ritter responsibilities and358 memory-search questions with original provenance. 66 unique captured inputs, actual generated pages and six successful required checks are bound. No source exhaustion, independent approval, issue closure or publication result is implied.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:AmortizedSteinVariationalGradientDescent. Retain the generic differentiable-sampler fitting procedure separately from unamortized interacting-particle SVGD, ordinary variational objectives and the composite SteinGAN/VAE/Langevin applications. No universal exact-sampling or stationarity-implies-target claim is adopted. Source residuals remain separately retained; no family exhaustion is inferred.
- retain: AIMech:RealTimeAdaptiveAStar. Retain the bounded forward-search, CLOSED-only F−g learning and capped-execution controller separately from ordinary A*, one-state LRTA, RTA second-best backup and LSS reverse-Dijkstra propagation. Special-case equality with identical ties does not establish general algorithm identity. Source residuals remain separately retained; no family exhaustion is inferred.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| src-wang-liu2016-v2 | /private/tmp/aimech-amortized-svgd-research-20261016/arxiv-v2.pdf | supports | Learning to Draw Samples: With Application to Amortized MLE for Generative Adversarial Learning. Exact arXiv:1611.01722v2, 26 November 2016; under-review preprint, no ICLR acceptance asserted. Declared role: defining_method. Primary reading is attributed to the selected source support and its reading receipts. |
| src-feng-wang-liu2017 | /private/tmp/aimech-amortized-svgd-research-20261016/uai2017.pdf | supports | Learning to Draw Samples with Amortized Stein Variational Gradient Descent. Exact Official UAI 2017 proceedings paper 206, inspected ten-page PDF; distinct work from arXiv:1611.01722. Declared role: defining_method. Primary reading is attributed to the selected source support and its reading receipts. |
| amortized-svgd-accepted-preview | /private/tmp/aimech-amortized-svgd-native-preview-20261016/native-preview.json | context_only | Exact root-accepted historical TEMP native preview; no current canonical creation or semantic clearance is inferred. |
| amortized-svgd-prior-support | /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json | context_only | Exact accepted source-scoped definition, claim and limitation assessment, including source locators and attributed reading. |
| amortized-svgd-root-preview-readback | /private/tmp/aimech-amortized-svgd-native-preview-20261016/root-preview-readback.json | context_only | Root acceptance of the exact historical native preview and native validation, separate from future ownership. |
| amortized-svgd-reading | /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/reading-attribution.json | context_only | Attributed primary/source/neighbor reading; no fresh source-read claim is made by this assembly. |
| amortized-svgd-limitation-1-support | /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json; /limitations/0; arxiv-v2 Section2 pp3–4; curator normalization consequence | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| amortized-svgd-limitation-2-support | /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json; /limitations/1; arxiv-v2 Eq2–6 pp3–4; UAI Problem1 p1 allows discrete seeds; UAI Section4.1/5.2 dropout examples pp5,8–9; curator measure distinction | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| amortized-svgd-limitation-3-support | /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json; /limitations/2; arxiv-v2 Eq8–10 p5; UAI Eq13–15 p4; both conclusions leave theoretical understanding for future work; curator projection analysis | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| amortized-svgd-limitation-4-support | /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json; /limitations/3; arxiv-v2 p5 Eq8–10; UAI2017 and later arXiv p4 Eq13–15, all three visuals inspected | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| amortized-svgd-limitation-5-support | /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json; /limitations/4; arxiv-v2 p4; UAI2017 pp3,7; curator kernel consequences | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| amortized-svgd-limitation-6-support | /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json; /limitations/5; arxiv-v2 Eq11–12 pp5–6; UAI Eq16–17 p5; curator interpretation of Eq8/13 | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| amortized-svgd-limitation-7-support | /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json; /limitations/6; arxiv-v2 Eq13–16 pp6–8; UAI Eq20–23 pp5–6; curator qualifications | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| amortized-svgd-limitation-8-support | /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json; /limitations/7; retained complete text diffs; 2016p9 tables; later2017pp10–12 | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| src-koenig-likhachev2006 | /private/tmp/aimech-rtaa-standalone-research-20261016/koenig-likhachev2006-current.pdf | supports | Real-Time Adaptive A*. Exact Author-hosted eight-page AAMAS 2006 paper, proceedings pp.281–288; defining method. Workshop version not inspected.. Declared role: defining_method. Primary reading is attributed to the selected source support and its reading receipts. |
| src-kochvi-ruml2018 | /private/tmp/aimech-rtaa-standalone-research-20261016/rtaa-star-socs18.pdf | supports | Does Fast Beat Thorough? Comparing RTAA* and LSS-LRTA*. Exact Author-hosted five-page SoCS 2018 manuscript, volume9(1), proceedings pp.163–167; later empirical comparison. Publisher PDF bytes not inspected.. Declared role: later_empirical_comparison_and_limitations. Primary reading is attributed to the selected source support and its reading receipts. |
| rtaa-accepted-preview | /private/tmp/aimech-rtaa-native-preview-20261016/native-preview.json | context_only | Exact root-accepted historical TEMP native preview; no current canonical creation or semantic clearance is inferred. |
| rtaa-prior-support | /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json | context_only | Exact accepted source-scoped definition, claim and limitation assessment, including source locators and attributed reading. |
| rtaa-root-preview-readback | /private/tmp/aimech-rtaa-native-preview-20261016/root-preview-readback.json | context_only | Root acceptance of the exact historical native preview and native validation, separate from future ownership. |
| rtaa-reading | /private/tmp/aimech-rtaa-draft-preparation-20261016/reading-attribution.json | context_only | Attributed primary/source/neighbor reading; no fresh source-read claim is made by this assembly. |
| rtaa-limitation-1-support | /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json; /limitations/0; 2006 PDF2 Sections3–4; PDF3 Theorems1–3; PDF8 future work explicitly mentions inconsistent heuristics. | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| rtaa-limitation-2-support | /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json; /limitations/1; 2006 PDF2 Section3 and Figure1 lines04–05; PDF3 Theorem3. | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| rtaa-limitation-3-support | /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json; /limitations/2; 2006 PDF2 notation, consistency and Figure1; PDF3 Theorem2. | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| rtaa-limitation-4-support | /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json; /limitations/3; 2006 Figure1/Section8;2018 PDF2 Experimental Set-up. | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| rtaa-limitation-5-support | /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json; /limitations/4; 2006 PDF3–4 Theorem4; PDF7 Table1. | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| rtaa-limitation-6-support | /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json; /limitations/5; 2006 PDF4 Section5 and references5/7/9. | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| rtaa-limitation-7-support | /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json; /limitations/6; 2006 PDF4 final paragraph,PDF6–8;2018 full comparison and PDF5 limitations. | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| rtaa-limitation-8-support | /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json; /limitations/7; 2018 PDF2 Unknown Terrain paragraphs; PDF3 Figure1 and PDF4–5 axes; all visually checked. | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| rtaa-limitation-9-support | /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json; /limitations/8; 2018 PDF3–4 Traffic. | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| rtaa-limitation-10-support | /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json; /limitations/9; 2018 PDF2 Unknown Terrain; PDF5 Conclusions; actual web403 receipt. | context_only | Exact limitation statement, source/mathematical attribution and bounded assessment; cited research context retains its own source role. |
| retained-template-validation-failure | /private/tmp/aimech-cohort359-review-save-validate.json | context_only | Earlier TEMP formal review validation rejected +00:00 timestamp serialization; no canonical review was saved. Successor emits equivalent UTC instants with required Z suffix. Scientific records and assessment narratives are unchanged. |
| actual-write | /private/tmp/aimech-cohort359-write.json | context_only | Actual exclusive creation of two native records, report pair and CREATE history. |
| captured-inputs | /private/tmp/aimech-cohort359-postwrite-20261016/actual-capture.json | context_only | Actual canonical input-byte and maintained-target capture. |
| postcapture-reading | /private/tmp/aimech-cohort359-timestamp-recovery-20261016/root-generation-reading.json | context_only | Actual root reading of source-scoped canonical records, metadata and all retained question objects; historical source reading stays separately attributed. |
| governance-assessment | /private/tmp/aimech-cohort359-governance-20261016/assessment.json | context_only | Actual byte preservation, dynamic owner-plan reconstruction, inherited metadata and parsed-page audit. |
| rendered-pages | /private/tmp/aimech-cohort359-governance-20261016/rendered-pages.json | context_only | Actual generated-page bytes and parsed content; no visual/layout inspection. |
| actual-scientific-assessment | /private/tmp/aimech-cohort359-actual-adversarial-review-20261016/assessment.preliminary.json | context_only | Actual record scientific assessment with its own attributed source-reading scope. |
| current-identity-collection | /private/tmp/aimech-cohort359-current-identity-20261016/collection.json | context_only | Actual scoped ignored-inclusive identity collection; mechanical capture is distinct from human semantic reading. |
| current-context-assessment | /private/tmp/aimech-cohort359-final-inputs-20261016/collection-assessment.json | context_only | Actual attributed current identity and source-question assessment. |
| root-decisions | /private/tmp/aimech-cohort359-final-inputs-20261016/root-decisions.json | context_only | Exact current record identity decisions, dynamic accepted ownership and retained source questions. |
| ownership-plan | /private/tmp/aimech-cohort359-source-ownership-proposal-20261016/ownership-plan.proposed.json | context_only | Exact distinct source responsibilities for two records,125 bibliography occurrences,19 original/dossier/retrieval objects and any additional source questions. |
| ownership-plan-acceptance | /private/tmp/aimech-cohort359-final-inputs-20261016/ownership-acceptance.json | context_only | Actual root acceptance of current source responsibility; no whole-issue closure. |
| current-discovery-report | /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T034316Z-amortized-svgd-and-real-time-adaptive-a-star.json | context_only | Canonical durable report containing the exact recursively queryable predecessor_state bundle and separate current pair source responsibilities. |
| creation-history | /private/tmp/aimech-discovery-recovery-worktree-20261012/history/reports/amortized-svgd-and-real-time-adaptive-a-star/2026-10-16T034327Z-codex-1eb03c.yaml | context_only | Actual single CREATE event for the report. |
| review-support | /private/tmp/aimech-cohort359-timestamp-recovery-20261016/review-support.prepared.json | context_only | Exact historical per-claim and per-limitation narrative support. |
| check-gate | /private/tmp/aimech-cohort359-postwrite-20261016/actual-check-gate.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-vendor | /private/tmp/aimech-cohort359-postwrite-20261016/recovery-check-vendor.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-check-source | /private/tmp/aimech-cohort359-postwrite-20261016/recovery-check-check-source.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-render | /private/tmp/aimech-cohort359-postwrite-20261016/actual-check-render.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-render-check | /private/tmp/aimech-cohort359-postwrite-20261016/recovery-check-render-check.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-diff | /private/tmp/aimech-cohort359-postwrite-20261016/recovery-check-diff.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| historical-failed-check-1 | /private/tmp/aimech-cohort359-postwrite-20261016/actual-check-vendor.json | context_only | Retained unsuccessful earlier command attempt; successful later exact command is separately bound. |

## Limits And Additional Notes

- Scientific correspondence uses exact accepted native-preview content and attributed primary-source, mathematical and source-accounting reading. This preparation does not claim a fresh full-paper reading or a new native validation.
- The amortized sampler remains generic and differentiable; its neural implementation relation is not a mandatory ANN architecture. Projection, finite-step, output-density and source-local sign limitations remain exact.
- RTAA retains CLOSED-only F−g, the selected frontier and movement controller, finite positive-cost/consistency assumptions and the separate2018 comparison/timing limitations.
- 125 bibliography occurrences plus19 original/dossier/retrieval objects remain separate source questions. Captured citation counts are not counts of new concepts; five sampler dossier followups are not presumed historically909-owned.
- Four declared artifacts include three defining method sources and one later comparison. Other version artifacts remain attributed research context rather than extra claim-support rows.
- Two related AIO mappings and historical14 AIO/21 native contexts retain their original scoped readings; capture is not renewed semantic clearance.
- Actual five creation outputs, one CREATE history, 66 capture inputs and 8 parsed generated pages are bound. Six required commands passed; earlier failed attempts remain explicit. Canonical review save/check and publication are subsequent operations.
- Supported outcomes here assess correspondence to already accepted source-scoped preview content. They do not certify future canonical records or source ownership.
- The source-local2017 Eq.14 minus discrepancy remains a limitation; the practical positive-gradient claim has its accepted supporting Eqs.13/15 evidence and no broadened claim-level contradiction.
- The2018 RTAA Figure1 center-axis literal is planning time (ms); aggregation and caption/axis discrepancies remain unresolved.
- The first formal-review validation failed on historical evidence timestamps serialized with +00:00. This successor preserves the same UTC instants using required Z syntax; the exact failure log is retained as evidence. No canonical review was saved by that failed attempt, and no scientific record or source claim changed.
- Two distinct source groups retain 125 bibliography occurrences and independent pending questions; these counts do not assert new concepts.
- {"added_record_ids": [], "assessment": "Andrychowicz et al. 2016 concerns learning an optimizer; sharing gradient-based training does not make it the generic Stein sampler.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 0, "kind": "bibliography", "next_check": "Inspect the exact learned-optimizer original and compare optimizer state, training distribution and objective before identity or ownership decisions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "fa671d0914ecafde33a656ec8065614a1539159b80f68f323749311272f494d8", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/0", "responsible_owner": {"family": "main", "index": 909}, "text": "Andrychowicz, Marcin, Denil, Misha, Gomez, Sergio, Hoffman, Matthew W, Pfau, David, Schaul, Tom, and\nde Freitas, Nando. Learning to learn by gradient descent by gradient descent. arXiv preprint arXiv:1606.04474,\n2016."}
- {"added_record_ids": [], "assessment": "Barbour and Chen is a Stein-method introduction, retained as mathematical source context rather than an asserted new AI algorithm.", "disposition": "retained_context", "existing_record_ids": [], "group": "amortized-svgd", "index": 1, "kind": "bibliography", "next_check": "Use the exact chapter/version if a later claim needs a Stein identity or regularity assumption.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "c721ddecd7c1666b42cbd8946f5728a6f6a1771352e5dc487f37ace1ae3d969c", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/1", "responsible_owner": {"family": "main", "index": 909}, "text": "Barbour, Andrew D and Chen, Louis Hsiao Yun. An introduction to Stein’s method, volume 4. World Scientiﬁc,\n2005."}
- {"added_record_ids": [], "assessment": "Briol et al. concerns probabilistic integration; integration and finite-particle sampler fitting are separate responsibilities.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 2, "kind": "bibliography", "next_check": "Inspect the cited integration construction and its relation to control functionals and Bayesian quadrature.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "0f0636e24b5e4deef177376655d31d6ddd87a3936807f8a7ee39d7445ef36204", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/2", "responsible_owner": {"family": "main", "index": 909}, "text": "Briol, Franc¸ois-Xavier, Oates, Chris, Girolami, Mark, Osborne, Michael A, Sejdinovic, Dino, et al. Probabilistic\nintegration: A role for statisticians in numerical analysis? arXiv preprint http://arxiv.org/abs/1512.00933,\n2015."}
- {"added_record_ids": [], "assessment": "Chwialkowski et al. kernel goodness-of-fit testing belongs to the existing pending Stein-test source question; it is not direct amortized-KSD training.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 3, "kind": "bibliography", "next_check": "Read the exact test original and distinguish its statistic and assumptions from Liu–Lee–Jordan and the sampler appendix.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "65f8207f69e775588c8065d86e2b2b6f3d8f7556c2ad8fda39f9696f89488e18", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/3", "responsible_owner": {"family": "main", "index": 909}, "text": "Chwialkowski, Kacper, Strathmann, Heiko, and Gretton, Arthur. A kernel test of goodness of ﬁt. In Proceedings\nof the International Conference on Machine Learning (ICML), 2016."}
- {"added_record_ids": [], "assessment": "Daniel et al. learned step-size controllers are a specific optimizer-controller source, not automatically the Langevin-schedule application.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 4, "kind": "bibliography", "next_check": "Inspect the controller inputs/objective and compare the application-specific learned Langevin schedule.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "82fa125fccdd77f78b126dc6ebe973abbe2a6fd49f727044bda8096dfb915c29", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/4", "responsible_owner": {"family": "main", "index": 909}, "text": "Daniel, Christian, Taylor, Jonathan, and Nowozin, Sebastian. Learning step size controllers for robust neural\nnetwork training. In Thirtieth AAAI Conference on Artiﬁcial Intelligence, 2016."}
- {"added_record_ids": [], "assessment": "Delyon and Portier concern integral approximation using kernel smoothing; no sampler-training equivalence follows from the kernel vocabulary.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 5, "kind": "bibliography", "next_check": "Read the original approximation method and retain its integration-estimator scope.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "fcb7680faf45ab61213b7473a5aa571dee8078b21758328f06a04e01ecc021cc", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/5", "responsible_owner": {"family": "main", "index": 909}, "text": "Delyon, Bernard and Portier, Franc¸ois.\nIntegral approximation by kernel smoothing.\narXiv preprint\narXiv:1409.0733, 2014."}
- {"added_record_ids": [], "assessment": "Dziugaite et al. train generative networks by maximum mean discrepancy; this is distinct source scope from Stein output displacements.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd", "index": 6, "kind": "bibliography", "next_check": "Inspect the original MMD objective, estimator and its relation to the separately cited GMMN work.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "0d9f60b5b98931641727af0f6585e0b9c73f5fe934636bfcae60910942d3d3e6", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/6", "responsible_owner": {"family": "main", "index": 909}, "text": "Dziugaite, Gintare Karolina, Roy, Daniel M., and Ghahramani, Zoubin. Training generative neural networks\nvia maximum mean discrepancy optimization. In Conference on Uncertainty in Artiﬁcial Intelligence (UAI),\n2015."}
- {"added_record_ids": [], "assessment": "Gershman and Goodman 2014 is amortized probabilistic reasoning, not the 2012 nonparametric-VI question already retained under owner909.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 7, "kind": "bibliography", "next_check": "Inspect the 2014 original separately; retain the exact 2012 pointer and do not substitute one for the other.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "e1953ec8a0bdf73a523eb4d83f9fd0d01c3f14096f0836ed03a67ebf2a676ab4", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/7", "responsible_owner": {"family": "main", "index": 909}, "text": "Gershman, Samuel J and Goodman, Noah D. Amortized inference in probabilistic reasoning. In Proceedings of\nthe 36th Annual Conference of the Cognitive Science Society, 2014."}
- {"added_record_ids": [], "assessment": "Geyer concerns MCMC maximum-likelihood calculations; the SteinGAN composite does not discharge this original-source question.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 8, "kind": "bibliography", "next_check": "Inspect the MCMC likelihood estimator and conditions before comparing the approximate model expectation in amortized MLE.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "f5dc1b4db754e2d010f607d94aea45c2f4405a9ab8bc7ec79adab62edd045fc3", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/8", "responsible_owner": {"family": "main", "index": 909}, "text": "Geyer, Charles J. Markov chain Monte Carlo maximum likelihood. In Computing Science and Statistics: Proc.\n23rd Symp. Interface, pp. 156–163, 1991."}
- {"added_record_ids": [], "assessment": "The maintained GAN class supplies generative/adversarial context for Goodfellow et al.; it is not the generic differentiable Stein sampler.", "disposition": "existing_record_context", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd", "index": 9, "kind": "bibliography", "next_check": "Retain original GAN objective/version scope and inspect any claim beyond the current class context.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "d8adbe74dc5df8e1c23b976b6fc48a92e1fa7f5ed7df753dcead190d3dfcfe40", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/9", "responsible_owner": {"family": "main", "index": 909}, "text": "Goodfellow, Ian, Pouget-Abadie, Jean, Mirza, Mehdi, Xu, Bing, Warde-Farley, David, Ozair, Sherjil, Courville,\nAaron, and Bengio, Yoshua. Generative adversarial nets. In Advances in Neural Information Processing\nSystems, pp. 2672–2680, 2014."}
- {"added_record_ids": [], "assessment": "Gorham and Mackey Stein sample-quality assessment is related to the pending discrepancy family, but is not automatically the same kernel test as Chwialkowski or Liu.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 10, "kind": "bibliography", "next_check": "Inspect its exact discrepancy/test construction and preserve separate source identities.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "fe08416d6cd6da10ca9226a02bdcd4e680a77b54d6cbabd8b0c7852e89500479", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/10", "responsible_owner": {"family": "main", "index": 909}, "text": "Gorham, Jack and Mackey, Lester. Measuring sample quality with Stein’s method. In Advances in Neural\nInformation Processing Systems (NIPS), pp. 226–234, 2015."}
- {"added_record_ids": [], "assessment": "Henmi et al. importance sampling with estimated samplers is an estimator source; BBVI or amortization terminology does not establish identity.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 11, "kind": "bibliography", "next_check": "Read the original weighting/estimation construction and assumptions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "aed321e20e42d2bd99585d8236e83674b7573125988f66fba91135107c38dc43", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/11", "responsible_owner": {"family": "main", "index": 909}, "text": "Henmi, Masayuki, Yoshida, Ryo, and Eguchi, Shinto. Importance sampling via the estimated sampler. Biometrika,\n94(4):985–991, 2007."}
- {"added_record_ids": [], "assessment": "The exact Hinton 2002 source is present in maintained ContrastiveDivergence and ProductOfExperts contexts. Those scopes do not make generic Stein fitting the same algorithm.", "disposition": "existing_record_context", "existing_record_ids": ["AIMech:ContrastiveDivergence", "AIMech:ProductOfExperts"], "group": "amortized-svgd", "index": 12, "kind": "bibliography", "next_check": "Retain the cited version and distinguish the CD approximation and energy-model composite; no fresh full-paper completion is claimed.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "a029eb15467135d37bbbab7f449f04ff6ce14f145dd897e468069c92113c1d60", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/12", "responsible_owner": {"family": "main", "index": 909}, "text": "Hinton, Geoffrey E. Training products of experts by minimizing contrastive divergence. Neural computation, 14\n(8):1771–1800, 2002."}
- {"added_record_ids": [], "assessment": "Kim and Bengio concern a directed generative/energy-model composite; it requires its own original-method comparison.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork", "AIMech:ProductOfExperts"], "group": "amortized-svgd", "index": 13, "kind": "bibliography", "next_check": "Inspect the model, learning objective and sampler interaction before any separate-record decision.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "dd492e1f05ff96a2db02417748d904b3d6aefe9c304c54e9b2c66bbd5b963b02", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/13", "responsible_owner": {"family": "main", "index": 909}, "text": "Kim, Taesup and Bengio, Yoshua. Deep directed generative models with energy-based probability estimation.\narXiv preprint arXiv:1606.03439, 2016."}
- {"added_record_ids": [], "assessment": "Adam is an existing maintained optimizer. Its use by the cited work is component context, not a sampler identity.", "disposition": "existing_record_context", "existing_record_ids": ["AIMech:Adam"], "group": "amortized-svgd", "index": 14, "kind": "bibliography", "next_check": "Reconcile the cited unversioned 2014 arXiv entry with the exact maintained Adam source version if version-specific claims are needed.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "f59517604f6eb3610c8bcaade09ca793bdd0212dda5fee45ee1de43960c7c20d", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/14", "responsible_owner": {"family": "main", "index": 909}, "text": "Kingma, Diederik and Ba, Jimmy. Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980,\n2014."}
- {"added_record_ids": [], "assessment": "The maintained VAE class supplies model context for auto-encoding variational Bayes; the estimator/training source has narrower details than the class.", "disposition": "existing_record_context", "existing_record_ids": ["AIO:VariationalAutoEncoder"], "group": "amortized-svgd", "index": 15, "kind": "bibliography", "next_check": "Retain the exact AEVB version and inspect any pathwise-estimator or application claim separately.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "dbf4fe30857a4800f8e4fe6148993cfe5416ec733135a9eaa49093fec5417481", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/15", "responsible_owner": {"family": "main", "index": 909}, "text": "Kingma, Diederik P and Welling, Max. Auto-encoding variational Bayes. In Proceedings of the International\nConference on Learning Representations (ICLR), 2013."}
- {"added_record_ids": [], "assessment": "Li and Malik learning to optimize is an optimizer-learning original, distinct from generic amortized inference.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 16, "kind": "bibliography", "next_check": "Inspect the optimizer parameterization, objective and training task.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "62d9217a2c27dbf1604fa36e440a2047522f7b3aca07e94069795e2434c32171", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/16", "responsible_owner": {"family": "main", "index": 909}, "text": "Li, Ke and Malik, Jitendra. Learning to optimize. arXiv preprint arXiv:1606.01885, 2016."}
- {"added_record_ids": [], "assessment": "Li, Swersky and Zemel GMMN is an MMD generative-training source, not an interchangeable citation for Dziugaite et al. or Stein fitting.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd", "index": 17, "kind": "bibliography", "next_check": "Read the exact GMMN original and reconcile the separate MMD-training sources.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "f211820994976560c8245bcdd778237f36b18f5869a88cee0f073edbd8a29ee9", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/17", "responsible_owner": {"family": "main", "index": 909}, "text": "Li, Yujia, Swersky, Kevin, and Zemel, Rich. Generative moment matching networks. In Proceedings of the\nInternational Conference on Machine Learning (ICML), 2015."}
- {"added_record_ids": [], "assessment": "Liu and Lee black-box importance sampling concerns importance weighting; maintained BBVI has a different estimator/objective.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference", "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 18, "kind": "bibliography", "next_check": "Inspect the exact importance-weight construction and distinguish it from BBVI and particle transport.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "36468fdf29d602123b670459c1b3b952308bfa28708b00bcf4ad3a3c3d3c0e07", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/18", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu, Qiang and Lee, Jason D. Black-box importance sampling. https://arxiv.org/abs/1610.05247, 2016."}
- {"added_record_ids": [], "assessment": "The maintained SVGD record represents direct interacting-particle transport. The proposed record fits shared sampler parameters to Stein-displaced outputs.", "disposition": "existing_record_context", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 19, "kind": "bibliography", "next_check": "Retain the arXiv-versus-official-proceedings version distinction; do not turn component use into an alias.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "000a9bbe6d1361b7360f59484886f5c6243406fbad390343e1c1961b076c2e3e", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/19", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu, Qiang and Wang, Dilin. Stein variational gradient descent: A general purpose bayesian inference algorithm.\narXiv preprint arXiv:1608.04471, 2016."}
- {"added_record_ids": [], "assessment": "Liu–Lee–Jordan KSD goodness-of-fit testing is explicitly retained under the existing owner909 Stein-test question.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 20, "kind": "bibliography", "next_check": "Read the exact test original, distinguish it from Chwialkowski/Gorham and direct KSD minimization.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "5d050ab3f42c985007bdccef102ed82f202f31a1cc1f10cd567fded79913cc63", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/20", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu, Qiang, Lee, Jason D, and Jordan, Michael I. A kernelized Stein discrepancy for goodness-of-ﬁt tests. In\nProceedings of the International Conference on Machine Learning (ICML), 2016."}
- {"added_record_ids": [], "assessment": "Deep Learning Face Attributes is retained for the cited face-data/benchmark context, not automatically an algorithm candidate.", "disposition": "retained_context", "existing_record_ids": [], "group": "amortized-svgd", "index": 21, "kind": "bibliography", "next_check": "Inspect the dataset/annotation and evaluation protocol if later claims use this source.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "29dbd3a02da0b471b03c5da83a8e7a47ff21cc64d6213da66199564b9d2de970", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/21", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu, Ziwei, Luo, Ping, Wang, Xiaogang, and Tang, Xiaoou. Deep learning face attributes in the wild. In\nProceedings of International Conference on Computer Vision (ICCV), 2015."}
- {"added_record_ids": [], "assessment": "Ngiam et al. deep energy models require a model/training-specific comparison; PoE and CD are related maintained contexts only.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:ProductOfExperts", "AIMech:ContrastiveDivergence"], "group": "amortized-svgd", "index": 22, "kind": "bibliography", "next_check": "Read the original energy model and training procedure before taxonomy decisions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "912b09f4960e31fb8605aca62d8b4a498a4087a966d4f24beed6838376886368", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/22", "responsible_owner": {"family": "main", "index": 909}, "text": "Ngiam, Jiquan, Chen, Zhenghao, Koh, Pang W, and Ng, Andrew Y. Learning deep energy models. In Proceedings\nof the International Conference on Machine Learning (ICML), pp. 1105–1112, 2011."}
- {"added_record_ids": [], "assessment": "f-GAN has a divergence-specific training objective; the broad GAN class does not resolve the exact procedure.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd", "index": 23, "kind": "bibliography", "next_check": "Inspect the variational divergence formulation and relation to the SteinGAN objective.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "8462df53077f30e188041f665aa77633f39ae49044d0b927d6ee4ef8c17671e5", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/23", "responsible_owner": {"family": "main", "index": 909}, "text": "Nowozin, Sebastian, Cseke, Botond, and Tomioka, Ryota. f-gan: Training generative neural samplers using\nvariational divergence minimization. arXiv preprint arXiv:1606.00709, 2016."}
- {"added_record_ids": [], "assessment": "Oates et al. control functionals remain a distinct integration source. This 2014 occurrence is preserved separately from the later 2017 citation.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 24, "kind": "bibliography", "next_check": "Resolve the cited versions and exact variance-reduction construction before merging source responsibilities.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "5cb6f6961e6d5fca34f13020a9b5b4091d2b21652cc8c8feb6d18ce2d4e17fac", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/24", "responsible_owner": {"family": "main", "index": 909}, "text": "Oates, Chris J, Girolami, Mark, and Chopin, Nicolas. Control functionals for Monte Carlo integration. Journal\nof the Royal Statistical Society, Series B, 2014."}
- {"added_record_ids": [], "assessment": "O’Hagan’s Monte Carlo critique is retained as methodology context, not an asserted standalone new AI method.", "disposition": "retained_context", "existing_record_ids": [], "group": "amortized-svgd", "index": 25, "kind": "bibliography", "next_check": "Inspect the exact argument if used to support quadrature or Monte Carlo claims.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "8339b404c435c11db59da276d0a657481102d3f9c129ef3f3f392f25145950c8", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/25", "responsible_owner": {"family": "main", "index": 909}, "text": "O’Hagan, Anthony. Monte Carlo is fundamentally unsound. Journal of the Royal Statistical Society. Series D\n(The Statistician), 36(2/3):247–249, 1987."}
- {"added_record_ids": [], "assessment": "Bayes–Hermite quadrature is a numerical-integration source, distinct from generic sampler fitting.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 26, "kind": "bibliography", "next_check": "Inspect the quadrature prior, estimator and applicability assumptions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "b5e765906391dc8dc38dd37bb957d7315a1e011745ce975503b0721e76b45877", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/26", "responsible_owner": {"family": "main", "index": 909}, "text": "O’Hagan, Anthony. Bayes–hermite quadrature. Journal of statistical planning and inference, 29(3):245–260,\n1991."}
- {"added_record_ids": [], "assessment": "Paige and Wood inference networks for SMC in graphical models have a proposal/inference procedure requiring separate analysis.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 27, "kind": "bibliography", "next_check": "Inspect the original SMC proposal training and relation to generic amortization.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "5ab7abeb6949b19eeb2db01c4b7c6f5a97f92c594a2e967bbe6bf8d96c6d394a", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/27", "responsible_owner": {"family": "main", "index": 909}, "text": "Paige, Brooks and Wood, Frank. Inference networks for sequential monte carlo in graphical models. arXiv\npreprint arXiv:1602.06701, 2016."}
- {"added_record_ids": [], "assessment": "The DCGAN citation concerns architecture/training specifics not represented merely by the broad GAN class.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd", "index": 28, "kind": "bibliography", "next_check": "Read the original convolutional architecture and training prescription before deciding method or model scope.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "d558b100be224aba1a1d93107ab511d5e704da4c2092654e2ae8751989ee443e", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/28", "responsible_owner": {"family": "main", "index": 909}, "text": "Radford, Alec, Metz, Luke, and Chintala, Soumith. Unsupervised representation learning with deep convolutional\ngenerative adversarial networks. arXiv preprint arXiv:1511.06434, 2015."}
- {"added_record_ids": [], "assessment": "Operator variational inference is an operator/objective source; neither BBVI nor amortized SVGD is an automatic alias.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference", "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 29, "kind": "bibliography", "next_check": "Inspect its original operator family, test function and objective.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "4a1c40996bc4b22c9425edb69cf1d0d286215509c5773d1ccd647ec52715f39a", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/29", "responsible_owner": {"family": "main", "index": 909}, "text": "Ranganath, R., Altosaar, J., Tran, D., and Blei, D.M. Operator variational inference. 2016."}
- {"added_record_ids": [], "assessment": "Ranganath–Gerrish–Blei BBVI is an existing maintained record and an exact source context under main308; its retained hierarchical/subsampling questions remain separate.", "disposition": "existing_record_context", "existing_record_ids": ["AIMech:BlackBoxVariationalInference"], "group": "amortized-svgd", "index": 30, "kind": "bibliography", "next_check": "Keep owner308’s residual source scope and inspect any unsupported weighting extension separately.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "15edab4a0a467ab96899161fd9209065be1c8e7ae37a61a989b92bf9c1c7e4d6", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/30", "responsible_owner": {"family": "main", "index": 308}, "text": "Ranganath, Rajesh, Gerrish, Sean, and Blei, David M. Black box variational inference. In Proceedings of the\nInternational Conference on Artiﬁcial Intelligence and Statistics (AISTATS), 2014."}
- {"added_record_ids": [], "assessment": "Hierarchical variational inference concerns a specific variational-family construction, not generic variational EM or BBVI by name.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference"], "group": "amortized-svgd", "index": 31, "kind": "bibliography", "next_check": "Read the original hierarchical family and estimator before owner/identity decisions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "672ce438fbda15c56336e4e7eac54f02b7c5175ec4efd9b4c5d9ee60617e8ef6", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/31", "responsible_owner": {"family": "main", "index": 909}, "text": "Ranganath, Rajesh, Tran, Dustin, and Blei, David M.\nHierarchical variational models.\narXiv preprint\narXiv:1511.02386, 2015."}
- {"added_record_ids": [], "assessment": "Rezende–Mohamed normalizing-flow VI is the existing owner909 bibliography question, cross-linked to H355-FLOW-17. FlowMatching/RectifiedFlow are related contexts, not resolutions.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:FlowMatching", "AIMech:RectifiedFlow"], "group": "amortized-svgd", "index": 32, "kind": "bibliography", "next_check": "Inspect the exact original flow transformations/objective and retain separate CNF/probability-flow family scope in issue406.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "a4bdc09c44052f83b01862e9127f75e17f47009edc87f4eda84625190f71d744", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/32", "responsible_owner": {"family": "main", "index": 909}, "text": "Rezende, Danilo Jimenez and Mohamed, Shakir. Variational inference with normalizing ﬂows. In Proceedings\nof the International Conference on Machine Learning (ICML), 2015a."}
- {"added_record_ids": [], "assessment": "This separate arXiv occurrence of Rezende–Mohamed normalizing-flow VI retains its version identity and the existing owner909/H355-FLOW-17 cross-link.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:FlowMatching", "AIMech:RectifiedFlow"], "group": "amortized-svgd", "index": 33, "kind": "bibliography", "next_check": "Resolve the exact arXiv/proceedings versions without dropping either occurrence or closing the wider flow-family question.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "2b5754efae97b58b5bba75518739d6a40ca9e948d9488ec100e0f217ad9be1bb", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/33", "responsible_owner": {"family": "main", "index": 909}, "text": "Rezende, Danilo Jimenez and Mohamed, Shakir. Variational inference with normalizing ﬂows. arXiv preprint\narXiv:1505.05770, 2015b."}
- {"added_record_ids": [], "assessment": "Improved GAN training is a specific collection of training procedures, not discharged by the broad GAN class or a Stein sampler.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd", "index": 34, "kind": "bibliography", "next_check": "Inspect the individual procedures and decide source/method granularity.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "5e424d1382fe5f5bacdcd647c4db6fe88b024761d4ff6190504fa8b44cbf2216", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/34", "responsible_owner": {"family": "main", "index": 909}, "text": "Salimans, Tim, Goodfellow, Ian, Zaremba, Wojciech, Cheung, Vicki, Radford, Alec, and Chen, Xi. Improved\ntechniques for training gans. arXiv preprint arXiv:1606.03498, 2016."}
- {"added_record_ids": [], "assessment": "Stein 1972 is retained mathematical normal-approximation background, not automatically a new AI algorithm.", "disposition": "retained_context", "existing_record_ids": [], "group": "amortized-svgd", "index": 35, "kind": "bibliography", "next_check": "Use the original theorem and conditions only after reading it for a specific future claim.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "e401080006cf2d9278c0e0f56adb157295da28884acf9532310df91ded73af25", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/35", "responsible_owner": {"family": "main", "index": 909}, "text": "Stein, Charles. A bound for the error in the normal approximation to the distribution of a sum of dependent\nrandom variables. In Proceedings of the Sixth Berkeley Symposium on Mathematical Statistics and Probability,\nVolume 2: Probability Theory, pp. 583–602, 1972."}
- {"added_record_ids": [], "assessment": "Tieleman 2008 is represented in maintained PersistentContrastiveDivergence; persistence and generic Stein fitting remain distinct.", "disposition": "existing_record_context", "existing_record_ids": ["AIMech:PersistentContrastiveDivergence", "AIMech:ContrastiveDivergence"], "group": "amortized-svgd", "index": 36, "kind": "bibliography", "next_check": "Retain exact PCD source scope and do not infer unbiased model expectations or sampler equivalence.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "9282f4df20a001c293f376684acaaa30eb76b1244ae64659e5222db49c7a377b", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/36", "responsible_owner": {"family": "main", "index": 909}, "text": "Tieleman, Tijmen. Training restricted boltzmann machines using approximations to the likelihood gradient. In\nProceedings of the 25th international conference on Machine learning, pp. 1064–1071. ACM, 2008."}
- {"added_record_ids": [], "assessment": "Variational Gaussian processes is a specific variational-family source; a generic GP model or another sparse approximation is not enough for identity.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 37, "kind": "bibliography", "next_check": "Inspect the exact method, construction and objective before owner assignment.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "6f49b889d13be8d64bfaa7c7d6f66622603ebd997131b1fe05c4d7a6951e0e7e", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/37", "responsible_owner": {"family": "main", "index": 909}, "text": "Tran, Dustin, Ranganath, Rajesh, and Blei, David M.\nVariational gaussian process.\narXiv preprint\narXiv:1511.06499, 2015."}
- {"added_record_ids": [], "assessment": "Xie et al. generative ConvNet theory is an energy/convolutional model source; it is not automatically adversarial learning.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:ProductOfExperts"], "group": "amortized-svgd", "index": 38, "kind": "bibliography", "next_check": "Read the original model and learning theory before relating it to the SteinGAN composite.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "8f3ed5561f2492c89e131bf766691f21c96debc7399acadc8182b49fd626cdbf", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/38", "responsible_owner": {"family": "main", "index": 909}, "text": "Xie, Jianwen, Lu, Yang, Zhu, Song-Chun, and Wu, Ying Nian. A theory of generative convnet. arXiv preprint\narXiv:1602.03264, 2016."}
- {"added_record_ids": [], "assessment": "LSUN is retained large-scale image-data construction/evaluation context, not a newly asserted AI method.", "disposition": "retained_context", "existing_record_ids": [], "group": "amortized-svgd", "index": 39, "kind": "bibliography", "next_check": "Inspect benchmark construction and task protocol for any later empirical claim.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "aa6c4160ed75a1e243604864eee824eb8f4ea72d3e96a19ea00d20c92011c96c", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/39", "responsible_owner": {"family": "main", "index": 909}, "text": "Yu, Fisher, Seff, Ari, Zhang, Yinda, Song, Shuran, Funkhouser, Thomas, and Xiao, Jianxiong. Lsun: Construction\nof a large-scale image dataset using deep learning with humans in the loop. arXiv preprint arXiv:1506.03365,\n2015."}
- {"added_record_ids": [], "assessment": "Energy-based GAN is a specific generative-training construction; the broad GAN class supplies context only.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd", "index": 40, "kind": "bibliography", "next_check": "Read the energy/discriminator objective and distinguish it from SteinGAN.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "db3ea88896534fe85c4cfc87ab4e8e959fe4714561bd97c1d85f08abae15b421", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer": "/items/40", "responsible_owner": {"family": "main", "index": 909}, "text": "Zhao, Junbo, Mathieu, Michael, and LeCun, Yann. Energy-based generative adversarial network. arXiv preprint\narXiv:1609.03126, 2016."}
- {"added_record_ids": [], "assessment": "Agakov and Barber auxiliary variational methods require a distinct original construction/objective assessment.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 41, "kind": "bibliography", "next_check": "Read the exact auxiliary-variable formulation before comparing implicit-family training.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "62b44c4da1219173d3626bb6460e81f1bef8e70c485bcfdb116ab0db0fd5fdac", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/41", "responsible_owner": {"family": "main", "index": 909}, "text": "Agakov, Felix V and Barber, David. An auxiliary varia-\ntional method. In International Conference on Neural\nInformation Processing, pp. 561–566. Springer, 2004."}
- {"added_record_ids": [], "assessment": "Andrieu and Thoms is an adaptive-MCMC tutorial. Main63 covers different regeneration/evolutionary originals and is contextual, not exact source responsibility for this tutorial.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 42, "kind": "bibliography", "next_check": "Inspect the tutorial and identify concrete algorithms before linking exact existing owners or asserting a new method.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "54a0b5051505958257db726670d13c595b88ad3832bfdf56bc64f1834d9f89c3", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/42", "responsible_owner": {"family": "main", "index": 909}, "text": "Andrieu, Christophe and Thoms, Johannes. A tutorial on\nadaptive mcmc. Statistics and Computing, 18(4):343–\n373, 2008."}
- {"added_record_ids": [], "assessment": "Bayesian dark knowledge is a particular posterior-predictive/distillation procedure. The AIO Distillation class supplies broad context only.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:Distillation"], "group": "amortized-svgd", "index": 43, "kind": "bibliography", "next_check": "Read the original approximation objective and compare with predictive compression; do not equate it with DINO.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "b13879b74ba1f1cdd3820c4f1814cdfc303e67215fb14fb00e3d89db7949dffd", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/43", "responsible_owner": {"family": "main", "index": 909}, "text": "Balan,\nAnoop Korattikara,\nRathod,\nVivek,\nMurphy,\nKevin P, and Welling, Max. Bayesian dark knowledge.\nIn Advances in Neural Information Processing Systems,\npp. 3438–3446, 2015."}
- {"added_record_ids": [], "assessment": "Briol et al. concerns probabilistic integration; integration and finite-particle sampler fitting are separate responsibilities.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 44, "kind": "bibliography", "next_check": "Inspect the cited integration construction and its relation to control functionals and Bayesian quadrature.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "59a9adfc7f6af1babcf6505fd8f0ad06d7b0336c1b69a8c91f1d88b8fffd9d77", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/44", "responsible_owner": {"family": "main", "index": 909}, "text": "Briol, Franc¸ois-Xavier, Oates, Chris, Girolami, Mark, Os-\nborne, Michael A, Sejdinovic, Dino, et al. Probabilistic\nintegration: A role for statisticians in numerical anal-\nysis?\narXiv preprint http://arxiv.org/abs/1512.00933,\n2015."}
- {"added_record_ids": [], "assessment": "IWAE has a specific importance-weighted variational objective. VAE and reweighted wake-sleep are related maintained scopes, not aliases.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:VariationalAutoEncoder", "AIMech:ReweightedWakeSleep"], "group": "amortized-svgd", "index": 45, "kind": "bibliography", "next_check": "Inspect the exact objective/gradient and compare IWAE with reweighted wake-sleep.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "357450bc10808e62d1e9eca3cb30c226321553aa3ccea4c64f3b29edfef5fa51", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/45", "responsible_owner": {"family": "main", "index": 909}, "text": "Burda, Yuri, Grosse, Roger, and Salakhutdinov, Rus-\nlan. Importance weighted autoencoders. arXiv preprint\narXiv:1509.00519, 2015."}
- {"added_record_ids": [], "assessment": "Chwialkowski et al. kernel goodness-of-fit testing belongs to the existing pending Stein-test source question; it is not direct amortized-KSD training.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 46, "kind": "bibliography", "next_check": "Read the exact test original and distinguish its statistic and assumptions from Liu–Lee–Jordan and the sampler appendix.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "119443ebbfe5a802e97fad4ea0a54b97abfbd9b19811d7e3762197b00628b6e9", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/46", "responsible_owner": {"family": "main", "index": 909}, "text": "Chwialkowski, Kacper, Strathmann, Heiko, and Gretton,\nArthur. A kernel test of goodness of ﬁt. In Proceed-\nings of the International Conference on Machine Learn-\ning (ICML), 2016."}
- {"added_record_ids": [], "assessment": "Delyon and Portier concern integral approximation using kernel smoothing; no sampler-training equivalence follows from the kernel vocabulary.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 47, "kind": "bibliography", "next_check": "Read the original approximation method and retain its integration-estimator scope.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "2933fd3376261ee068399f2ffe4dc96bdee658678a235983b755208f07bfc48b", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/47", "responsible_owner": {"family": "main", "index": 909}, "text": "Delyon, Bernard and Portier, Franc¸ois.\nIntegral ap-\nproximation by kernel smoothing.\narXiv preprint\narXiv:1409.0733, 2014."}
- {"added_record_ids": [], "assessment": "Gershman and Goodman 2014 is amortized probabilistic reasoning, not the 2012 nonparametric-VI question already retained under owner909.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 48, "kind": "bibliography", "next_check": "Inspect the 2014 original separately; retain the exact 2012 pointer and do not substitute one for the other.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "b1f2cd2eb884ec8baf0a856e938b9487716e2bd5ee7234b7d5f60d88da1c20e4", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/48", "responsible_owner": {"family": "main", "index": 909}, "text": "Gershman, Samuel J and Goodman, Noah D. Amortized\ninference in probabilistic reasoning. In Proceedings of\nthe 36th Annual Conference of the Cognitive Science So-\nciety, 2014."}
- {"added_record_ids": [], "assessment": "The maintained GAN class supplies generative/adversarial context for Goodfellow et al.; it is not the generic differentiable Stein sampler.", "disposition": "existing_record_context", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd", "index": 49, "kind": "bibliography", "next_check": "Retain original GAN objective/version scope and inspect any claim beyond the current class context.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "817f39003ab1393d51ad58aa1d8a4662db8326e307778e6b6b3201c5be877225", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/49", "responsible_owner": {"family": "main", "index": 909}, "text": "Goodfellow, Ian, Pouget-Abadie, Jean, Mirza, Mehdi, Xu,\nBing, Warde-Farley, David, Ozair, Sherjil, Courville,\nAaron, and Bengio, Yoshua. Generative adversarial nets.\nIn Advances in Neural Information Processing Systems,\npp. 2672–2680, 2014."}
- {"added_record_ids": [], "assessment": "Henmi et al. importance sampling with estimated samplers is an estimator source; BBVI or amortization terminology does not establish identity.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 50, "kind": "bibliography", "next_check": "Read the original weighting/estimation construction and assumptions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "50f52683c3d853b6e1ca9a65792b15c3eb15fde79a2ba12770edb6927711e98f", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/50", "responsible_owner": {"family": "main", "index": 909}, "text": "Henmi, Masayuki, Yoshida, Ryo, and Eguchi, Shinto.\nImportance\nsampling\nvia\nthe\nestimated\nsampler.\nBiometrika, 94(4):985–991, 2007."}
- {"added_record_ids": [], "assessment": "Hoffman–Blei–Wang–Paisley stochastic VI is explicitly retained under main426 with the exact 1206.7051 source. Nested0 concerns a different 2017 sparse-GP source.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:BlackBoxVariationalInference"], "group": "amortized-svgd", "index": 51, "kind": "bibliography", "next_check": "Use main426 for the exact SVI original; distinguish its stochastic natural-gradient scheme from online LDA and other similarly named methods.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "354fbf62e4458c3c938a13c1dbce622a3d55dc29d169e542214779aa6998a74b", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/51", "responsible_owner": {"family": "main", "index": 426}, "text": "Hoffman, Matthew D, Blei, David M, Wang, Chong, and\nPaisley, John. Stochastic variational inference. JMLR,\n2013."}
- {"added_record_ids": [], "assessment": "The maintained VAE class supplies model context for auto-encoding variational Bayes; the estimator/training source has narrower details than the class.", "disposition": "existing_record_context", "existing_record_ids": ["AIO:VariationalAutoEncoder"], "group": "amortized-svgd", "index": 52, "kind": "bibliography", "next_check": "Retain the exact AEVB version and inspect any pathwise-estimator or application claim separately.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "278284d4ef7b4f7fc4b2f6f1e9b5ca97d1403fc1c5656ae67ac17b1071648a19", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/52", "responsible_owner": {"family": "main", "index": 909}, "text": "Kingma, Diederik P and Welling, Max.\nAuto-encoding\nvariational Bayes. In Proceedings of the International\nConference on Learning Representations (ICLR), 2013."}
- {"added_record_ids": [], "assessment": "Inverse autoregressive flow is a distinct flow construction; the Rezende–Mohamed question supplies related family context, not exact equivalence.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:VariationalAutoEncoder", "AIMech:FlowMatching", "AIMech:RectifiedFlow"], "group": "amortized-svgd", "index": 53, "kind": "bibliography", "next_check": "Read the IAF transformation and estimator, then reconcile with the existing pending normalizing-flow family.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "8113c3744db9f360c8b6a15b2589142dbb477404dbac9231de88b5b0b70b08a6", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/53", "responsible_owner": {"family": "main", "index": 909}, "text": "Kingma, Diederik P, Salimans, Tim, and Welling, Max. Im-\nproving variational inference with inverse autoregressive\nﬂow. arXiv preprint arXiv:1606.04934, 2016."}
- {"added_record_ids": [], "assessment": "Li–Turner–Liu amortised MCMC is a specific transition-distillation/implicit-inference procedure, not an alias from shared amortization vocabulary.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 54, "kind": "bibliography", "next_check": "Inspect its original teacher transition, discrepancy and fitting objective.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "067bdc3d069d0d19b4e5d173a4d6b9d4316d314650f902bbe638433f79469c9e", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/54", "responsible_owner": {"family": "main", "index": 909}, "text": "Li, Yingzhen, Turner, Richard E, and Liu, Qiang. Approx-\nimate inference with amortised mcmc. arXiv preprint\narXiv:1702.08343, 2017."}
- {"added_record_ids": [], "assessment": "Liu and Lee black-box importance sampling concerns importance weighting; maintained BBVI has a different estimator/objective.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference", "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 55, "kind": "bibliography", "next_check": "Inspect the exact importance-weight construction and distinguish it from BBVI and particle transport.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "6806c6dc5e289c7730be28375277edfa7d6daf2afde8b257bf0c8aefccb20dce", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/55", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu, Qiang and Lee, Jason D. Black-box importance sam-\npling. https://arxiv.org/abs/1610.05247, 2016."}
- {"added_record_ids": [], "assessment": "The maintained SVGD record represents direct interacting-particle transport. The proposed record fits shared sampler parameters to Stein-displaced outputs.", "disposition": "existing_record_context", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 56, "kind": "bibliography", "next_check": "Retain the arXiv-versus-official-proceedings version distinction; do not turn component use into an alias.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "fa64d842a5e835bfd375347eb9e57f11c8c8b3dd85d76290d8e1d3101a499f8f", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/56", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu, Qiang and Wang, Dilin. Stein variational gradient de-\nscent: A general purpose bayesian inference algorithm.\narXiv preprint arXiv:1608.04471, 2016."}
- {"added_record_ids": [], "assessment": "Liu–Lee–Jordan KSD goodness-of-fit testing is explicitly retained under the existing owner909 Stein-test question.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 57, "kind": "bibliography", "next_check": "Read the exact test original, distinguish it from Chwialkowski/Gorham and direct KSD minimization.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "f39384f1ef39ab27c5aa8b26ad5af65cc8e7992520c35b771f3894edcc3c55a6", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/57", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu, Qiang, Lee, Jason D, and Jordan, Michael I. A ker-\nnelized Stein discrepancy for goodness-of-ﬁt tests. In\nProceedings of the International Conference on Machine\nLearning (ICML), 2016."}
- {"added_record_ids": [], "assessment": "Maclaurin et al. early stopping as nonparametric VI is not Gershman et al. 2012, which remains a separate owner909 question.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 58, "kind": "bibliography", "next_check": "Inspect the early-stopping distribution/objective and retain the original Gershman pointer.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "8b9f64aadf4c89a9d522ad653561c159d8bf0f06b1ae477d2fd9dab3bced2d7e", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/58", "responsible_owner": {"family": "main", "index": 909}, "text": "Maclaurin, Dougal, Duvenaud, David, and Adams, Ryan P.\nEarly stopping is nonparametric variational inference.\narXiv preprint arXiv:1504.01344, 2015."}
- {"added_record_ids": [], "assessment": "Mandt et al. analyze SGD variationally; an analysis of an optimizer does not automatically define a new optimizer or sampler.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 59, "kind": "bibliography", "next_check": "Read assumptions, stationary approximation and the claimed algorithmic contribution before identity decisions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "db6604c93e0ee53951128974583da142cad3ac322302d5ff52594929a3af5742", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/59", "responsible_owner": {"family": "main", "index": 909}, "text": "Mandt, Stephan, Hoffman, Matthew D, and Blei, David M.\nA variational analysis of stochastic gradient algorithms.\narXiv preprint arXiv:1602.02666, 2016."}
- {"added_record_ids": [], "assessment": "Adversarial variational Bayes is a specific inference/training procedure; VAE/GAN classes are related scopes only.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:VariationalAutoEncoder", "AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd", "index": 60, "kind": "bibliography", "next_check": "Inspect the discriminator/variational objective and compare with the generic Stein fitting update.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "215c8bda7beb5b6e77b7de71b2be73d89e79bd078eff7f987cb542122b8c9677", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/60", "responsible_owner": {"family": "main", "index": 909}, "text": "Mescheder, Lars, Nowozin, Sebastian, and Geiger, An-\ndreas.\nAdversarial variational bayes: Unifying varia-\ntional autoencoders and generative adversarial networks.\narXiv preprint arXiv:1701.04722, 2017."}
- {"added_record_ids": [], "assessment": "Mohamed and Lakshminarayanan implicit generative models is retained as a broad family/source question, not a single asserted algorithm.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork", "AIO:VariationalAutoEncoder"], "group": "amortized-svgd", "index": 61, "kind": "bibliography", "next_check": "Read the taxonomy and isolate concrete procedures before proposing records.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "55c3a7eac063b76bf81a1353c55fbb73b048f431d09c4c688fa8b3656a2dbf10", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/61", "responsible_owner": {"family": "main", "index": 909}, "text": "Mohamed, Shakir and Lakshminarayanan, Balaji. Learn-\ning in implicit generative models.\narXiv preprint\narXiv:1610.03483, 2016."}
- {"added_record_ids": [], "assessment": "The 2017 control-functionals citation is preserved separately from the 2014 occurrence; identical-looking titles do not resolve version correspondence.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 62, "kind": "bibliography", "next_check": "Inspect the published original and reconcile the exact 2014/2017 versions and construction.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "1ab7d269b8c8b89363ce6faf9c0495b1229f85a6d3701a169a70df201170a373", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/62", "responsible_owner": {"family": "main", "index": 909}, "text": "Oates, Chris J, Girolami, Mark, and Chopin, Nicolas. Con-\ntrol functionals for Monte Carlo integration. Journal of\nthe Royal Statistical Society, Series B, 2017."}
- {"added_record_ids": [], "assessment": "O’Hagan’s Monte Carlo critique is retained as methodology context, not an asserted standalone new AI method.", "disposition": "retained_context", "existing_record_ids": [], "group": "amortized-svgd", "index": 63, "kind": "bibliography", "next_check": "Inspect the exact argument if used to support quadrature or Monte Carlo claims.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "ca09058ca5b43a8f7915b2103269b7b3f470f94a03fa417dc45d237c7899da03", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/63", "responsible_owner": {"family": "main", "index": 909}, "text": "O’Hagan, Anthony.\nMonte Carlo is fundamentally un-\nsound. Journal of the Royal Statistical Society. Series\nD (The Statistician), 36(2/3):247–249, 1987."}
- {"added_record_ids": [], "assessment": "Bayes–Hermite quadrature is a numerical-integration source, distinct from generic sampler fitting.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 64, "kind": "bibliography", "next_check": "Inspect the quadrature prior, estimator and applicability assumptions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "1a3f25d3f4857679f8e96d24973df4f53adc375061b8c67f05f970ba041ec906", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/64", "responsible_owner": {"family": "main", "index": 909}, "text": "O’Hagan, Anthony. Bayes–hermite quadrature. Journal of\nstatistical planning and inference, 29(3):245–260, 1991."}
- {"added_record_ids": [], "assessment": "Paige and Wood inference networks for SMC in graphical models have a proposal/inference procedure requiring separate analysis.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 65, "kind": "bibliography", "next_check": "Inspect the original SMC proposal training and relation to generic amortization.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "e5aa80532831ae5f3e32c7f833c6b08b449cb107eb576a4c64cec275696fed84", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/65", "responsible_owner": {"family": "main", "index": 909}, "text": "Paige, Brooks and Wood, Frank. Inference networks for se-\nquential monte carlo in graphical models. arXiv preprint\narXiv:1602.06701, 2016."}
- {"added_record_ids": [], "assessment": "Operator variational inference is an operator/objective source; neither BBVI nor amortized SVGD is an automatic alias.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference", "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 66, "kind": "bibliography", "next_check": "Inspect its original operator family, test function and objective.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "f3c0b8ddc37c6514f9047fe3d6b50836df75a98840f03f38ed5fd3a5667884fb", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/66", "responsible_owner": {"family": "main", "index": 909}, "text": "Ranganath, R., Altosaar, J., Tran, D., and Blei, D.M. Oper-\nator variational inference. 2016."}
- {"added_record_ids": [], "assessment": "Rezende–Mohamed normalizing-flow VI is the existing owner909 bibliography question, cross-linked to H355-FLOW-17. FlowMatching/RectifiedFlow are related contexts, not resolutions.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:FlowMatching", "AIMech:RectifiedFlow"], "group": "amortized-svgd", "index": 67, "kind": "bibliography", "next_check": "Inspect the exact original flow transformations/objective and retain separate CNF/probability-flow family scope in issue406.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "19ad5a801f0cd44e199f0aaba54cb2a3e1d3f304dd59617d42b48c86e2c97968", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/67", "responsible_owner": {"family": "main", "index": 909}, "text": "Rezende, Danilo Jimenez and Mohamed, Shakir. Varia-\ntional inference with normalizing ﬂows. In Proceedings\nof the International Conference on Machine Learning\n(ICML), 2015."}
- {"added_record_ids": [], "assessment": "Roberts and Rosenthal adaptive-MCMC examples are an exact original-source question. Main63’s different cited works provide context, not an accepted equivalent owner.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 68, "kind": "bibliography", "next_check": "Inspect the concrete adaptations and conditions; link an existing owner only after source-specific comparison.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "dbb85db7c3486393b5733fa07c5d22932e7d129f01e177f8c75beef219543d23", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/68", "responsible_owner": {"family": "main", "index": 909}, "text": "Roberts, Gareth O and Rosenthal, Jeffrey S. Examples of\nadaptive mcmc. Journal of Computational and Graphi-\ncal Statistics, 18(2):349–367, 2009."}
- {"added_record_ids": [], "assessment": "Salimans et al. bridge MCMC and VI using a specific hybrid construction; generic sampler fitting or ULA is not its identity.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:UnadjustedLangevinAlgorithm"], "group": "amortized-svgd", "index": 69, "kind": "bibliography", "next_check": "Read the original transition/variational construction and objective.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "56ecfa3a18c9f9edd2df281a5c1dc4884c3c2f5f31187a15164fda777d648450", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/69", "responsible_owner": {"family": "main", "index": 909}, "text": "Salimans, Tim et al. Markov chain monte carlo and varia-\ntional inference: Bridging the gap. In International Con-\nference on Machine Learning, 2015."}
- {"added_record_ids": [], "assessment": "Snelson–Ghahramani compact predictive approximations remain retained in the official 2017 bibliography; their absence from the later bibliography does not erase this source responsibility.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:Distillation"], "group": "amortized-svgd", "index": 70, "kind": "bibliography", "next_check": "Read the predictive-compression method and compare exact source scope with Bayesian dark knowledge.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "f9cc135d8e4eb503392c217e178c10d89e5eb1d1f3d66379010937bd40427483", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/70", "responsible_owner": {"family": "main", "index": 909}, "text": "Snelson, Edward and Ghahramani, Zoubin. Compact ap-\nproximations to bayesian predictive distributions.\nIn\nProceedings of the 22nd international conference on\nMachine learning, pp. 840–847. ACM, 2005."}
- {"added_record_ids": [], "assessment": "Welling–Teh SGLD is a stochastic-gradient transition source. Maintained ULA and main42 TULA are related but do not resolve this exact method.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:UnadjustedLangevinAlgorithm"], "group": "amortized-svgd", "index": 71, "kind": "bibliography", "next_check": "Inspect gradient noise, stepsize schedule and target assumptions before identity or owner decisions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "b8f18daf62d83716f272d13247d6b7bc1fccb0cc56519ab84e4711417dec0654", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/71", "responsible_owner": {"family": "main", "index": 909}, "text": "Welling, Max and Teh, Yee W.\nBayesian learning via\nstochastic gradient Langevin dynamics. In Proceedings\nof the International Conference on Machine Learning\n(ICML), 2011."}
- {"added_record_ids": [], "assessment": "Wu et al. quantitative analysis of decoder-based generative models is retained evaluation/methodology scope, not automatically another generative algorithm.", "disposition": "retained_context", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork", "AIO:VariationalAutoEncoder"], "group": "amortized-svgd", "index": 72, "kind": "bibliography", "next_check": "Inspect the original estimator and evaluation protocol before using quantitative comparisons.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "ea1e831d57cfdd7fbd694dc49a704bf1272fba70fe27fdf49b7ca3796318a266", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer": "/items/72", "responsible_owner": {"family": "main", "index": 909}, "text": "Wu, Yuhuai, Burda, Yuri, Salakhutdinov, Ruslan, and\nGrosse,\nRoger.\nOn the quantitative analysis of\ndecoder-based generative models.\narXiv preprint\narXiv:1611.04273, 2016."}
- {"added_record_ids": [], "assessment": "Agakov and Barber auxiliary variational methods require a distinct original construction/objective assessment.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 73, "kind": "bibliography", "next_check": "Read the exact auxiliary-variable formulation before comparing implicit-family training.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "6f201b44a2760d529a787bc6f38617abf755ec437dec409d547df5b3e359167f", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/73", "responsible_owner": {"family": "main", "index": 909}, "text": "Agakov, Felix V and Barber, David. An auxiliary varia-\ntional method. In International Conference on Neural\nInformation Processing, pp. 561–566. Springer, 2004."}
- {"added_record_ids": [], "assessment": "Andrieu and Thoms is an adaptive-MCMC tutorial. Main63 covers different regeneration/evolutionary originals and is contextual, not exact source responsibility for this tutorial.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 74, "kind": "bibliography", "next_check": "Inspect the tutorial and identify concrete algorithms before linking exact existing owners or asserting a new method.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "fce7fae9331a6d951d9ca9f92e51b1af6b162cc071537fc03303c1177413efcf", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/74", "responsible_owner": {"family": "main", "index": 909}, "text": "Andrieu, Christophe and Thoms, Johannes. A tutorial on\nadaptive mcmc. Statistics and Computing, 18(4):343–\n373, 2008."}
- {"added_record_ids": [], "assessment": "Bayesian dark knowledge is a particular posterior-predictive/distillation procedure. The AIO Distillation class supplies broad context only.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:Distillation"], "group": "amortized-svgd", "index": 75, "kind": "bibliography", "next_check": "Read the original approximation objective and compare with predictive compression; do not equate it with DINO.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "61d46554ab4b0cf16f182ffa87eaf3e12e2eb2177fbf1c2e3b034158b2bfa9d8", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/75", "responsible_owner": {"family": "main", "index": 909}, "text": "Balan,\nAnoop Korattikara,\nRathod,\nVivek,\nMurphy,\nKevin P, and Welling, Max. Bayesian dark knowledge.\nIn Advances in Neural Information Processing Systems,\npp. 3438–3446, 2015."}
- {"added_record_ids": [], "assessment": "Briol et al. concerns probabilistic integration; integration and finite-particle sampler fitting are separate responsibilities.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 76, "kind": "bibliography", "next_check": "Inspect the cited integration construction and its relation to control functionals and Bayesian quadrature.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "5712a790c48c39c8090684565e7bd115c623789eaa9e981856da9778a4233c7b", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/76", "responsible_owner": {"family": "main", "index": 909}, "text": "Briol, Franc¸ois-Xavier, Oates, Chris, Girolami, Mark, Os-\nborne, Michael A, Sejdinovic, Dino, et al. Probabilistic\nintegration: A role for statisticians in numerical anal-\nysis?\narXiv preprint http://arxiv.org/abs/1512.00933,\n2015."}
- {"added_record_ids": [], "assessment": "IWAE has a specific importance-weighted variational objective. VAE and reweighted wake-sleep are related maintained scopes, not aliases.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:VariationalAutoEncoder", "AIMech:ReweightedWakeSleep"], "group": "amortized-svgd", "index": 77, "kind": "bibliography", "next_check": "Inspect the exact objective/gradient and compare IWAE with reweighted wake-sleep.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "7be97e146f7b71fe76f2efbb55f98d75c5c4edb64fd5a49167d702191e0d9a3a", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/77", "responsible_owner": {"family": "main", "index": 909}, "text": "Burda, Yuri, Grosse, Roger, and Salakhutdinov, Rus-\nlan. Importance weighted autoencoders. arXiv preprint\narXiv:1509.00519, 2015."}
- {"added_record_ids": [], "assessment": "Chwialkowski et al. kernel goodness-of-fit testing belongs to the existing pending Stein-test source question; it is not direct amortized-KSD training.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 78, "kind": "bibliography", "next_check": "Read the exact test original and distinguish its statistic and assumptions from Liu–Lee–Jordan and the sampler appendix.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "e4103113df8e18f8d1175480da88e713674f46704f477c029b355e36255a16c2", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/78", "responsible_owner": {"family": "main", "index": 909}, "text": "Chwialkowski, Kacper, Strathmann, Heiko, and Gretton,\nArthur. A kernel test of goodness of ﬁt. In Proceed-\nings of the International Conference on Machine Learn-\ning (ICML), 2016."}
- {"added_record_ids": [], "assessment": "Delyon and Portier concern integral approximation using kernel smoothing; no sampler-training equivalence follows from the kernel vocabulary.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 79, "kind": "bibliography", "next_check": "Read the original approximation method and retain its integration-estimator scope.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "a7af1cc238f27d2d1b214110a78d5a5a178fb4366da905f97df0759e2b53954c", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/79", "responsible_owner": {"family": "main", "index": 909}, "text": "Delyon, Bernard and Portier, Franc¸ois.\nIntegral ap-\nproximation by kernel smoothing.\narXiv preprint\narXiv:1409.0733, 2014."}
- {"added_record_ids": [], "assessment": "Gershman and Goodman 2014 is amortized probabilistic reasoning, not the 2012 nonparametric-VI question already retained under owner909.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 80, "kind": "bibliography", "next_check": "Inspect the 2014 original separately; retain the exact 2012 pointer and do not substitute one for the other.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "a4117394a3de24e0b4c7bbc03b3316e6c514e0ae3bcc2f1b050247ce35757af5", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/80", "responsible_owner": {"family": "main", "index": 909}, "text": "Gershman, Samuel J and Goodman, Noah D. Amortized\ninference in probabilistic reasoning. In Proceedings of\nthe 36th Annual Conference of the Cognitive Science So-\nciety, 2014."}
- {"added_record_ids": [], "assessment": "The maintained GAN class supplies generative/adversarial context for Goodfellow et al.; it is not the generic differentiable Stein sampler.", "disposition": "existing_record_context", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd", "index": 81, "kind": "bibliography", "next_check": "Retain original GAN objective/version scope and inspect any claim beyond the current class context.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "727cf2ef521e72567a2ad746dff9c5466cc01f1936a682d1f8057dd58f89c43a", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/81", "responsible_owner": {"family": "main", "index": 909}, "text": "Goodfellow, Ian, Pouget-Abadie, Jean, Mirza, Mehdi, Xu,\nBing, Warde-Farley, David, Ozair, Sherjil, Courville,\nAaron, and Bengio, Yoshua. Generative adversarial nets.\nIn Advances in Neural Information Processing Systems,\npp. 2672–2680, 2014."}
- {"added_record_ids": [], "assessment": "Henmi et al. importance sampling with estimated samplers is an estimator source; BBVI or amortization terminology does not establish identity.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 82, "kind": "bibliography", "next_check": "Read the original weighting/estimation construction and assumptions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "4396cffa55b2cffb94d5d6abb8e8b21609b6eb54b100922809623173e2ff4641", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/82", "responsible_owner": {"family": "main", "index": 909}, "text": "Henmi, Masayuki, Yoshida, Ryo, and Eguchi, Shinto.\nImportance\nsampling\nvia\nthe\nestimated\nsampler.\nBiometrika, 94(4):985–991, 2007."}
- {"added_record_ids": [], "assessment": "Hoffman–Blei–Wang–Paisley stochastic VI is explicitly retained under main426 with the exact 1206.7051 source. Nested0 concerns a different 2017 sparse-GP source.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:BlackBoxVariationalInference"], "group": "amortized-svgd", "index": 83, "kind": "bibliography", "next_check": "Use main426 for the exact SVI original; distinguish its stochastic natural-gradient scheme from online LDA and other similarly named methods.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "4c9c71aad013782bdd7c95f1fdfa7709a8c5e8da0035a7e3099097ca98f4499f", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/83", "responsible_owner": {"family": "main", "index": 426}, "text": "Hoffman, Matthew D, Blei, David M, Wang, Chong, and\nPaisley, John. Stochastic variational inference. JMLR,\n2013."}
- {"added_record_ids": [], "assessment": "The maintained VAE class supplies model context for auto-encoding variational Bayes; the estimator/training source has narrower details than the class.", "disposition": "existing_record_context", "existing_record_ids": ["AIO:VariationalAutoEncoder"], "group": "amortized-svgd", "index": 84, "kind": "bibliography", "next_check": "Retain the exact AEVB version and inspect any pathwise-estimator or application claim separately.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "c94aa2446f1da1851cf5f317e360f5db32d5d84946b4a0f0199e32d833eefedf", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/84", "responsible_owner": {"family": "main", "index": 909}, "text": "Kingma, Diederik P and Welling, Max.\nAuto-encoding\nvariational Bayes. In Proceedings of the International\nConference on Learning Representations (ICLR), 2013."}
- {"added_record_ids": [], "assessment": "Inverse autoregressive flow is a distinct flow construction; the Rezende–Mohamed question supplies related family context, not exact equivalence.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:VariationalAutoEncoder", "AIMech:FlowMatching", "AIMech:RectifiedFlow"], "group": "amortized-svgd", "index": 85, "kind": "bibliography", "next_check": "Read the IAF transformation and estimator, then reconcile with the existing pending normalizing-flow family.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "8e0d0f5a98a7309e95424ccbbeaa288a0c4aa14cc9d0bcda0b8bb96c1d125e36", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/85", "responsible_owner": {"family": "main", "index": 909}, "text": "Kingma, Diederik P, Salimans, Tim, and Welling, Max. Im-\nproving variational inference with inverse autoregressive\nﬂow. arXiv preprint arXiv:1606.04934, 2016."}
- {"added_record_ids": [], "assessment": "Li–Turner–Liu amortised MCMC is a specific transition-distillation/implicit-inference procedure, not an alias from shared amortization vocabulary.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 86, "kind": "bibliography", "next_check": "Inspect its original teacher transition, discrepancy and fitting objective.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "c83c5749316b801eb80bf97bc944e42e23ce6ce29b079e98b4df7baf7fd44b6d", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/86", "responsible_owner": {"family": "main", "index": 909}, "text": "Li, Yingzhen, Turner, Richard E, and Liu, Qiang. Approx-\nimate inference with amortised mcmc. arXiv preprint\narXiv:1702.08343, 2017."}
- {"added_record_ids": [], "assessment": "Liu and Lee black-box importance sampling concerns importance weighting; maintained BBVI has a different estimator/objective.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference", "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 87, "kind": "bibliography", "next_check": "Inspect the exact importance-weight construction and distinguish it from BBVI and particle transport.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "280763c860f10e72456d39a99aff1fd0407363fec894f52906c5c057b7ba3f52", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/87", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu, Qiang and Lee, Jason D. Black-box importance sam-\npling. https://arxiv.org/abs/1610.05247, 2016."}
- {"added_record_ids": [], "assessment": "The maintained SVGD record represents direct interacting-particle transport. The proposed record fits shared sampler parameters to Stein-displaced outputs.", "disposition": "existing_record_context", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 88, "kind": "bibliography", "next_check": "Retain the arXiv-versus-official-proceedings version distinction; do not turn component use into an alias.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "0bf5d7b8514d71109497d1f51c2f11426f7a3812648484c0fb46869bf731c8ef", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/88", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu, Qiang and Wang, Dilin. Stein variational gradient de-\nscent: A general purpose bayesian inference algorithm.\narXiv preprint arXiv:1608.04471, 2016."}
- {"added_record_ids": [], "assessment": "Liu–Lee–Jordan KSD goodness-of-fit testing is explicitly retained under the existing owner909 Stein-test question.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 89, "kind": "bibliography", "next_check": "Read the exact test original, distinguish it from Chwialkowski/Gorham and direct KSD minimization.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "a436b192221da791b9da23e7e6f8f50d3776b6255f81bf13d2838a0a86080402", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/89", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu, Qiang, Lee, Jason D, and Jordan, Michael I. A ker-\nnelized Stein discrepancy for goodness-of-ﬁt tests. In\nProceedings of the International Conference on Machine\nLearning (ICML), 2016."}
- {"added_record_ids": [], "assessment": "Maclaurin et al. early stopping as nonparametric VI is not Gershman et al. 2012, which remains a separate owner909 question.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 90, "kind": "bibliography", "next_check": "Inspect the early-stopping distribution/objective and retain the original Gershman pointer.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "4af785fd3e235c5f7026605282dad7dd3727ec9a44bcf02f055d697021f29d95", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/90", "responsible_owner": {"family": "main", "index": 909}, "text": "Maclaurin, Dougal, Duvenaud, David, and Adams, Ryan P.\nEarly stopping is nonparametric variational inference.\narXiv preprint arXiv:1504.01344, 2015."}
- {"added_record_ids": [], "assessment": "Mandt et al. analyze SGD variationally; an analysis of an optimizer does not automatically define a new optimizer or sampler.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 91, "kind": "bibliography", "next_check": "Read assumptions, stationary approximation and the claimed algorithmic contribution before identity decisions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "a6cfb459d9416441a150ced1214a1fb7b143a04de4ab9b03b6f2027b047eb768", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/91", "responsible_owner": {"family": "main", "index": 909}, "text": "Mandt, Stephan, Hoffman, Matthew D, and Blei, David M.\nA variational analysis of stochastic gradient algorithms.\narXiv preprint arXiv:1602.02666, 2016."}
- {"added_record_ids": [], "assessment": "Adversarial variational Bayes is a specific inference/training procedure; VAE/GAN classes are related scopes only.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:VariationalAutoEncoder", "AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd", "index": 92, "kind": "bibliography", "next_check": "Inspect the discriminator/variational objective and compare with the generic Stein fitting update.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "06e573f49a07db6ae647a68c1674a4531a1b976c2fd39f8e8a96f349eb45a152", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/92", "responsible_owner": {"family": "main", "index": 909}, "text": "Mescheder, Lars, Nowozin, Sebastian, and Geiger, An-\ndreas.\nAdversarial variational bayes: Unifying varia-\ntional autoencoders and generative adversarial networks.\narXiv preprint arXiv:1701.04722, 2017."}
- {"added_record_ids": [], "assessment": "Mohamed and Lakshminarayanan implicit generative models is retained as a broad family/source question, not a single asserted algorithm.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork", "AIO:VariationalAutoEncoder"], "group": "amortized-svgd", "index": 93, "kind": "bibliography", "next_check": "Read the taxonomy and isolate concrete procedures before proposing records.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "d440c5bdb06beb7d4bc1a13637346fab248fac0cc31ed26ab569f3c8a5403a39", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/93", "responsible_owner": {"family": "main", "index": 909}, "text": "Mohamed, Shakir and Lakshminarayanan, Balaji. Learn-\ning in implicit generative models.\narXiv preprint\narXiv:1610.03483, 2016."}
- {"added_record_ids": [], "assessment": "The 2017 control-functionals citation is preserved separately from the 2014 occurrence; identical-looking titles do not resolve version correspondence.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 94, "kind": "bibliography", "next_check": "Inspect the published original and reconcile the exact 2014/2017 versions and construction.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "c890a539f2c5dccfb9f7dd4f17dfb8e5dc9ea9c6e47a0b31d15db85af1e339a4", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/94", "responsible_owner": {"family": "main", "index": 909}, "text": "Oates, Chris J, Girolami, Mark, and Chopin, Nicolas. Con-\ntrol functionals for Monte Carlo integration. Journal of\nthe Royal Statistical Society, Series B, 2017."}
- {"added_record_ids": [], "assessment": "O’Hagan’s Monte Carlo critique is retained as methodology context, not an asserted standalone new AI method.", "disposition": "retained_context", "existing_record_ids": [], "group": "amortized-svgd", "index": 95, "kind": "bibliography", "next_check": "Inspect the exact argument if used to support quadrature or Monte Carlo claims.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "2e1836a466c3f28dbdb2574489aa87c8c5e944e0c1ee539a60014d91e093b35f", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/95", "responsible_owner": {"family": "main", "index": 909}, "text": "O’Hagan, Anthony.\nMonte Carlo is fundamentally un-\nsound. Journal of the Royal Statistical Society. Series\nD (The Statistician), 36(2/3):247–249, 1987."}
- {"added_record_ids": [], "assessment": "Bayes–Hermite quadrature is a numerical-integration source, distinct from generic sampler fitting.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 96, "kind": "bibliography", "next_check": "Inspect the quadrature prior, estimator and applicability assumptions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "dd318b194f69759dfbb5b33d28b0d8e9bd6564f3f668bbef63218142ab4c9a70", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/96", "responsible_owner": {"family": "main", "index": 909}, "text": "O’Hagan, Anthony. Bayes–hermite quadrature. Journal of\nstatistical planning and inference, 29(3):245–260, 1991."}
- {"added_record_ids": [], "assessment": "Paige and Wood inference networks for SMC in graphical models have a proposal/inference procedure requiring separate analysis.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 97, "kind": "bibliography", "next_check": "Inspect the original SMC proposal training and relation to generic amortization.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "9ba0de7e458d4be14186c59ab2b8ea1768ec6c8dec816c68a3224e04426d1953", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/97", "responsible_owner": {"family": "main", "index": 909}, "text": "Paige, Brooks and Wood, Frank. Inference networks for se-\nquential monte carlo in graphical models. arXiv preprint\narXiv:1602.06701, 2016."}
- {"added_record_ids": [], "assessment": "Pu et al. VAE learning via SVGD is a later-version citation addition and remains a distinct unread-original question linked to the Stein-VAE followup.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:VariationalAutoEncoder", "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 98, "kind": "bibliography", "next_check": "Acquire Pu’s exact original and compare its procedure with the Feng application; no equivalence or priority follows from citation addition.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "9a33575e2d5d6f08160637088e2d3e934113f9a0ea4369ac692cce7074b6870f", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/98", "responsible_owner": {"family": "main", "index": 909}, "text": "Pu, Yunchen, Gan, Zhe, Henao, Ricardo, Li, Chunyuan,\nHan, Shaobo, and Carin, Lawrence.\nVae learning via\nstein variational gradient descent. In Advances in Neural\nInformation Processing Systems (NIPS), 2017."}
- {"added_record_ids": [], "assessment": "Operator variational inference is an operator/objective source; neither BBVI nor amortized SVGD is an automatic alias.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference", "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 99, "kind": "bibliography", "next_check": "Inspect its original operator family, test function and objective.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "57656ead0f81f28b5f098834b6e5ca4ce1d91db4a5deab01e660ad88310f128b", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/99", "responsible_owner": {"family": "main", "index": 909}, "text": "Ranganath, R., Altosaar, J., Tran, D., and Blei, D.M. Oper-\nator variational inference. 2016."}
- {"added_record_ids": [], "assessment": "Rezende–Mohamed normalizing-flow VI is the existing owner909 bibliography question, cross-linked to H355-FLOW-17. FlowMatching/RectifiedFlow are related contexts, not resolutions.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:FlowMatching", "AIMech:RectifiedFlow"], "group": "amortized-svgd", "index": 100, "kind": "bibliography", "next_check": "Inspect the exact original flow transformations/objective and retain separate CNF/probability-flow family scope in issue406.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "7cf44304618a7be11db57eeeb686bc6e24b8e819d2c8a581d0a260e19e5d91c1", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/100", "responsible_owner": {"family": "main", "index": 909}, "text": "Rezende, Danilo Jimenez and Mohamed, Shakir. Varia-\ntional inference with normalizing ﬂows. In Proceedings\nof the International Conference on Machine Learning\n(ICML), 2015."}
- {"added_record_ids": [], "assessment": "Roberts and Rosenthal adaptive-MCMC examples are an exact original-source question. Main63’s different cited works provide context, not an accepted equivalent owner.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index": 101, "kind": "bibliography", "next_check": "Inspect the concrete adaptations and conditions; link an existing owner only after source-specific comparison.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "ddd56ba6787f4788e190beafe49197c88c93879c1b1c477c85b0e2c7e28a7d24", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/101", "responsible_owner": {"family": "main", "index": 909}, "text": "Roberts, Gareth O and Rosenthal, Jeffrey S. Examples of\nadaptive mcmc. Journal of Computational and Graphi-\ncal Statistics, 18(2):349–367, 2009."}
- {"added_record_ids": [], "assessment": "Salimans et al. bridge MCMC and VI using a specific hybrid construction; generic sampler fitting or ULA is not its identity.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:UnadjustedLangevinAlgorithm"], "group": "amortized-svgd", "index": 102, "kind": "bibliography", "next_check": "Read the original transition/variational construction and objective.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "a02f88401d9c301ca67931b83bc41ee9effc02f36ae38df3dbbaaa002e1d4270", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/102", "responsible_owner": {"family": "main", "index": 909}, "text": "Salimans, Tim et al. Markov chain monte carlo and varia-\ntional inference: Bridging the gap. In International Con-\nference on Machine Learning, 2015."}
- {"added_record_ids": [], "assessment": "Welling–Teh SGLD is a stochastic-gradient transition source. Maintained ULA and main42 TULA are related but do not resolve this exact method.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:UnadjustedLangevinAlgorithm"], "group": "amortized-svgd", "index": 103, "kind": "bibliography", "next_check": "Inspect gradient noise, stepsize schedule and target assumptions before identity or owner decisions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "4efbed874c5a3ecfae0bd29c5506b1de12576f3009b25949aca8123e7e45e1af", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/103", "responsible_owner": {"family": "main", "index": 909}, "text": "Welling, Max and Teh, Yee W.\nBayesian learning via\nstochastic gradient Langevin dynamics. In Proceedings\nof the International Conference on Machine Learning\n(ICML), 2011."}
- {"added_record_ids": [], "assessment": "Wu et al. quantitative analysis of decoder-based generative models is retained evaluation/methodology scope, not automatically another generative algorithm.", "disposition": "retained_context", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork", "AIO:VariationalAutoEncoder"], "group": "amortized-svgd", "index": 104, "kind": "bibliography", "next_check": "Inspect the original estimator and evaluation protocol before using quantitative comparisons.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256": "9807a5730b4783819894803dd0e9d8da299532aeff9df2089d960d6243fdfb1c", "original_source_details": {"next_check": "Reconcile this exact cited work against maintained definitions and recursive source-owner objects before deciding existing, distinct, contextual, or nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"}, "pointer": "/items/104", "responsible_owner": {"family": "main", "index": 909}, "text": "Wu, Yuhuai, Burda, Yuri, Salakhutdinov, Ruslan, and\nGrosse,\nRoger.\nOn the quantitative analysis of\ndecoder-based generative models.\narXiv preprint\narXiv:1611.04273, 2016."}
- {"added_record_ids": ["AIMech:AmortizedSteinVariationalGradientDescent"], "assessment": "The accepted 2016v2 and distinct 2017 defining sources support the generic differentiable-sampler component. Conditional representation by the proposed record does not resolve SteinGAN, direct KSD, Stein-VAE, learned Langevin or umbrella scopes. Historical citation-only access remains original provenance.", "disposition": "represented_by_added_record", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent", "AIMech:SoftQLearning"], "group": "amortized-svgd", "index": 0, "kind": "original_owner_questions", "next_check": "After authorized creation verify this narrow component; retain all five application/umbrella followups, six other original questions and all source/version limitations.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256": "50fee4fe8b1585b08ab6e9feab21bd6973cd5ad0166e63a3e2dcf027d3382dbc", "original_source_details": {"candidate": "Learning to Draw Samples: With Application to Amortized MLE for Generative Adversarial Learning", "next_check": "Verify source version and original amortized inference method; decide separate component versus closely related source scope after full method reading.", "source": {"citation_ledger": {"path": "/private/tmp/aimech-soft-q-research-20261015/citation-leads.json", "sha256": "ff8ba8586defbf9bfa950127764c5ec12426c9eccf87aa255ace12e46102e107"}, "origin": "Main PDF p. 10 bibliography and Section 3.3", "pointer": "/leads/1"}, "url": "https://arxiv.org/abs/1611.01722"}, "pointer": "/original_questions/0", "responsible_owner": {"family": "main", "index": 909}, "text": "Learning to Draw Samples: With Application to Amortized MLE for Generative Adversarial Learning"}
- {"added_record_ids": [], "assessment": "SVPG remains an independent policy-parameter-particle method. Separate TEMP primary research/native preview now exists, but it is not a maintained record and the historical citation-only statement is preserved as historical.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent", "AIMech:SoftQLearning"], "group": "amortized-svgd", "index": 1, "kind": "original_owner_questions", "next_check": "Reconcile the separately prepared SVPG draft with a fresh future identity/owner decision; do not resolve it through amortized action or generic sampler fitting.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256": "56ce5076ab8064b6fdf8dcff2d5db24629277b09dd32844ab1d8bd09367497de", "original_source_details": {"candidate": "Stein Variational Policy Gradient", "next_check": "Inspect original policy-particle method and compare it with amortized action sampling; no identity decision from the shared Stein name.", "source": {"citation_ledger": {"path": "/private/tmp/aimech-soft-q-research-20261015/citation-leads.json", "sha256": "ff8ba8586defbf9bfa950127764c5ec12426c9eccf87aa255ace12e46102e107"}, "origin": "Main PDF p. 9 bibliography", "pointer": "/leads/2"}, "url": "https://arxiv.org/abs/1704.02399"}, "pointer": "/original_questions/1", "responsible_owner": {"family": "main", "index": 909}, "text": "Stein Variational Policy Gradient"}
- {"added_record_ids": [], "assessment": "Dai et al. particle mirror descent remains the exact pending original-source question under main909. Particle vocabulary does not establish equality.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 2, "kind": "original_owner_questions", "next_check": "Acquire the exact original and compare update geometry, objective and current owners.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256": "e90aab01a761b2fd0f577b9a14eff54284e3872cdf0b28500d235d246f4d337b", "original_source_details": {"candidate": "Particle mirror descent (Dai et al. 2016)", "next_check": "Identify the exact original cited work and reconcile its full method against maintained records and existing owners before deciding distinct concept, overlap or existing-owner linkage. The cited title is not novelty evidence.", "source": {"citation_scope": {"path": "/private/tmp/aimech-svgd-research-20261015/citation-scope.json", "sha256": "6e4fce31c555b25438183ac54c24d71ac09d4b6b65373d5297dc835cb088d28f"}, "origin": {"path": "/private/tmp/aimech-svgd-research-20261015/extraction/page-09.txt", "sha256": "2bfab341a9840bb1f34c345f8e2d2ba3e12b864e1a41cf44b1a666de99da8f63"}, "pointer": "/other_bibliography_next_checks/0"}, "url": "https://proceedings.neurips.cc/paper_files/paper/2016/file/b3ba8f1bee1238a2f37603d90b58898d-Paper.pdf"}, "pointer": "/original_questions/2", "responsible_owner": {"family": "main", "index": 909}, "text": "Particle mirror descent (Dai et al. 2016)"}
- {"added_record_ids": [], "assessment": "The existing Stein discrepancy/test question retains separate Chwialkowski, Liu–Lee–Jordan and Gorham–Mackey responsibilities. Direct amortized-KSD optimization is a further application question.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 3, "kind": "original_owner_questions", "next_check": "Inspect the exact tests/statistics and normalize objective conventions before any merge or separate record.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256": "b26e01f712344c24363ff6aac3914ff0f237923dd4fc86f65c520d1045c987a6", "original_source_details": {"candidate": "Kernelized Stein discrepancy and Stein goodness-of-fit tests", "next_check": "Identify the exact original cited work and reconcile its full method against maintained records and existing owners before deciding distinct concept, overlap or existing-owner linkage. The cited title is not novelty evidence.", "source": {"citation_scope": {"path": "/private/tmp/aimech-svgd-research-20261015/citation-scope.json", "sha256": "6e4fce31c555b25438183ac54c24d71ac09d4b6b65373d5297dc835cb088d28f"}, "origin": {"path": "/private/tmp/aimech-svgd-research-20261015/extraction/page-09.txt", "sha256": "2bfab341a9840bb1f34c345f8e2d2ba3e12b864e1a41cf44b1a666de99da8f63"}, "pointer": "/other_bibliography_next_checks/1"}, "url": "https://proceedings.neurips.cc/paper_files/paper/2016/file/b3ba8f1bee1238a2f37603d90b58898d-Paper.pdf"}, "pointer": "/original_questions/3", "responsible_owner": {"family": "main", "index": 909}, "text": "Kernelized Stein discrepancy and Stein goodness-of-fit tests"}
- {"added_record_ids": [], "assessment": "Gershman et al. 2012 nonparametric VI remains pending. Gershman–Goodman 2014 and Maclaurin 2015 are distinct cited works.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:BlackBoxVariationalInference"], "group": "amortized-svgd", "index": 4, "kind": "original_owner_questions", "next_check": "Acquire the 2012 original and compare variational family/objective with maintained BBVI and score-estimator contexts.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256": "bbb9fb2e40d4d8eb57321e2221b539794d26cfd755e5dde0569ad71805aedaf7", "original_source_details": {"candidate": "Nonparametric variational inference (Gershman et al. 2012)", "next_check": "Identify the exact original cited work and reconcile its full method against maintained records and existing owners before deciding distinct concept, overlap or existing-owner linkage. The cited title is not novelty evidence.", "source": {"citation_scope": {"path": "/private/tmp/aimech-svgd-research-20261015/citation-scope.json", "sha256": "6e4fce31c555b25438183ac54c24d71ac09d4b6b65373d5297dc835cb088d28f"}, "origin": {"path": "/private/tmp/aimech-svgd-research-20261015/extraction/page-09.txt", "sha256": "2bfab341a9840bb1f34c345f8e2d2ba3e12b864e1a41cf44b1a666de99da8f63"}, "pointer": "/other_bibliography_next_checks/2"}, "url": "https://proceedings.neurips.cc/paper_files/paper/2016/file/b3ba8f1bee1238a2f37603d90b58898d-Paper.pdf"}, "pointer": "/original_questions/4", "responsible_owner": {"family": "main", "index": 909}, "text": "Nonparametric variational inference (Gershman et al. 2012)"}
- {"added_record_ids": [], "assessment": "The exact Rezende–Mohamed VI source remains pending under main909 and is cross-linked to inherited H355-FLOW-17; CNF/probability-flow family scope remains separately unresolved.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:FlowMatching", "AIMech:RectifiedFlow"], "group": "amortized-svgd", "index": 5, "kind": "original_owner_questions", "next_check": "Inspect the original flow transform/objective and versions; keep issue406 and its broader family question open.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256": "ce4ab105a20be2eaefe9f20c9e387c973ddffa815f4ce1dd7fb724a0684cd2b3", "original_source_details": {"candidate": "Variational inference with normalizing flows (Rezende and Mohamed 2015)", "next_check": "Identify the exact original cited work and reconcile its full method against maintained records and existing owners before deciding distinct concept, overlap or existing-owner linkage. The cited title is not novelty evidence.", "source": {"citation_scope": {"path": "/private/tmp/aimech-svgd-research-20261015/citation-scope.json", "sha256": "6e4fce31c555b25438183ac54c24d71ac09d4b6b65373d5297dc835cb088d28f"}, "origin": {"path": "/private/tmp/aimech-svgd-research-20261015/extraction/page-09.txt", "sha256": "2bfab341a9840bb1f34c345f8e2d2ba3e12b864e1a41cf44b1a666de99da8f63"}, "pointer": "/other_bibliography_next_checks/3"}, "url": "https://proceedings.neurips.cc/paper_files/paper/2016/file/b3ba8f1bee1238a2f37603d90b58898d-Paper.pdf"}, "pointer": "/original_questions/5", "responsible_owner": {"family": "main", "index": 909}, "text": "Variational inference with normalizing flows (Rezende and Mohamed 2015)"}
- {"added_record_ids": [], "assessment": "Doubly stochastic variational Bayes remains the exact Titsias–Lázaro-Gredilla original-source question. BBVI and main305 estimator contexts do not establish an alias.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:BlackBoxVariationalInference"], "group": "amortized-svgd", "index": 6, "kind": "original_owner_questions", "next_check": "Read the exact original estimators and assumptions before assigning a maintained method or closing the question.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256": "f557f214dc41c1aa4f944e970440bced7f8a0626e8c61fe5d27692d2078adfc3", "original_source_details": {"candidate": "Doubly stochastic variational Bayes (Titsias and Lázaro-Gredilla 2014)", "next_check": "Identify the exact original cited work and reconcile its full method against maintained records and existing owners before deciding distinct concept, overlap or existing-owner linkage. The cited title is not novelty evidence.", "source": {"citation_scope": {"path": "/private/tmp/aimech-svgd-research-20261015/citation-scope.json", "sha256": "6e4fce31c555b25438183ac54c24d71ac09d4b6b65373d5297dc835cb088d28f"}, "origin": {"path": "/private/tmp/aimech-svgd-research-20261015/extraction/page-09.txt", "sha256": "2bfab341a9840bb1f34c345f8e2d2ba3e12b864e1a41cf44b1a666de99da8f63"}, "pointer": "/other_bibliography_next_checks/4"}, "url": "https://proceedings.neurips.cc/paper_files/paper/2016/file/b3ba8f1bee1238a2f37603d90b58898d-Paper.pdf"}, "pointer": "/original_questions/6", "responsible_owner": {"family": "main", "index": 909}, "text": "Doubly stochastic variational Bayes (Titsias and Lázaro-Gredilla 2014)"}
- {"added_record_ids": [], "assessment": "SteinGAN/amortized MLE is a composite energy-model and sampler procedure, not the generic sampler identity. This plan newly proposes source-tracking responsibility at main909; historical ownership of this followup is not asserted.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:ProductOfExperts", "AIMech:ContrastiveDivergence", "AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd", "index": 0, "kind": "dossier_followups", "next_check": "Compare the energy objective, approximate model expectation and sampler coupling with PoE/CD and adversarial scopes before deciding a distinct record.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256": "10346c0e0ef8df53eef646056268c10679136889f8de81c160c0f53b81640f45", "original_source_details": {"name": "SteinGAN / amortized MLE of an energy model", "question": "Reconcile the composite energy-model/sampler training identity against existing energy-based generative and adversarial-learning owners; retain normalizer, approximate model expectation and modified-objective caveats. Do not treat it as an alias of generic amortized SVGD."}, "pointer": "/followups/0", "responsible_owner": {"family": "main", "index": 909}, "text": "SteinGAN / amortized MLE of an energy model"}
- {"added_record_ids": [], "assessment": "Direct amortized KSD is a separate objective with second-order score and D-versus-D-squared normalization questions. Newly proposed main909 tracking does not resolve its existing Stein-test family.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent", "AIMech:BlackBoxVariationalInference"], "group": "amortized-svgd", "index": 1, "kind": "dossier_followups", "next_check": "Inspect the exact direct objective/normalization and compare operator-VI/test scopes before a record decision.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256": "d43ae170275c910e42150dc961aa0ef05f5f47b239113bc3cd107b41be898a33", "original_source_details": {"name": "Amortized KSD / KSD variational inference", "question": "Compare direct stochastic optimization of squared KSD and its second-order score requirements with existing Stein-discrepancy/operator-VI scopes. AppendixA uses D^2 in a unit-ball decrease display where Eq8 defines D as the unsquared unit-ball supremum; analyze normalization before adopting that equivalence. Not a second name for amortized SVGD."}, "pointer": "/followups/1", "responsible_owner": {"family": "main", "index": 909}, "text": "Amortized KSD / KSD variational inference"}
- {"added_record_ids": [], "assessment": "Entropy-regularized Stein VAE and Pu et al. remain an application/original-source comparison. The Feng application was historically read; Pu original remains unacquired. Main909 responsibility is newly proposed here.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:VariationalAutoEncoder", "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 2, "kind": "dossier_followups", "next_check": "Acquire Pu’s original and compare the exact application objectives/updates; citation addition alone is not identity or priority.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256": "a2b2358c7794b994893c8f0e222a88991d324182ccd3daa5d788c252b24bca89", "original_source_details": {"name": "Entropy-regularized Stein VAE and Pu et al.2017 VAE learning via SVGD", "question": "Determine whether the application warrants a separate procedure and compare exact Pu source. The later citation addition is not automatic equivalence or priority evidence."}, "pointer": "/followups/2", "responsible_owner": {"family": "main", "index": 909}, "text": "Entropy-regularized Stein VAE and Pu et al.2017 VAE learning via SVGD"}
- {"added_record_ids": [], "assessment": "Learning Langevin step schedules uses a finite-horizon simulator and remains a method-versus-application question. Main909 source responsibility is proposed, not inherited ownership.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:UnadjustedLangevinAlgorithm"], "group": "amortized-svgd", "index": 3, "kind": "dossier_followups", "next_check": "Compare learned schedule parameterization, positivity, differentiation-through-score and blockwise training with ULA and the generic fitting component.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256": "7140e136ded5e91c2e1c3c9f490371148f92b35c962696c881dde40362ce59da", "original_source_details": {"name": "Amortized-SVGD training of Langevin step schedules", "question": "Resolve distinct learned-sampler variant versus application of generic amortized SVGD with ULA as simulator. Retain finite horizon, positive step, gradient-through-score and blockwise-training limits."}, "pointer": "/followups/3", "responsible_owner": {"family": "main", "index": 909}, "text": "Amortized-SVGD training of Langevin step schedules"}
- {"added_record_ids": [], "assessment": "Wild VI/variational programming is umbrella terminology, not a single algorithm declared by this proposal. Main909 is proposed as a tracking location only.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference", "AIO:VariationalAutoEncoder", "AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd", "index": 4, "kind": "dossier_followups", "next_check": "Read operator VI, amortised MCMC and adversarial variational Bayes originals before taxonomy or record decisions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256": "135503b9a08699a200eb387b0b267b34268534ccdb829b72704568a52b6c5a47", "original_source_details": {"name": "Wild variational inference / variational programming", "question": "Compare generic implicit-family scope, operator variational inference, amortised MCMC and adversarial variational Bayes using original sources before taxonomy or record decisions."}, "pointer": "/followups/4", "responsible_owner": {"family": "main", "index": 909}, "text": "Wild variational inference / variational programming"}
- {"added_record_ids": [], "assessment": "Björnsson et al. map abstraction is a separate pathfinding-source question; A* is component context only.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:AStarSearch"], "group": "rtaa", "index": 0, "kind": "bibliography", "next_check": "Inspect the exact abstraction construction and distinguish it from RTAA local search.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "47f729de411b235b3eca21c7b13e85fc58862a26ebd15b340b47b11a873ad60e", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/0", "responsible_owner": {"family": "nested", "index": 393}, "text": "[1] M. Bjornsson, M. Enzenberger, R. Holte, J. Schaeffer, and\nP. Yap. Comparison of different abstractions for pathﬁnding\non maps. In Proceedings of the International Joint\nConference on Artiﬁcial Intelligence, pages 1511–1512,\n2003."}
- {"added_record_ids": [], "assessment": "The 2005 in-press Bulitko–Lee citation is linked to nested393’s pending 2006 framework source, with version/year correspondence still open.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:LearningRealTimeAStar", "AIMech:RealTimeAStar"], "group": "rtaa", "index": 1, "kind": "bibliography", "next_check": "Read the original framework and reconcile the in-press/published versions and concrete variants.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "abb1e7f31ee6003f90364ef32c93ad1ff025c66df07a6a59a70c02caa9c033a8", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/1", "responsible_owner": {"family": "nested", "index": 393}, "text": "[2] V. Bulitko and G. Lee. Learning in real-time search: A\nunifying framework. Journal of Artiﬁcial Intelligence\nResearch, page (in press), 2005."}
- {"added_record_ids": [], "assessment": "Hart et al. is represented by maintained AStarSearch. The bibliography’s volume rendering differs from maintained source metadata and is retained literally.", "disposition": "existing_record_context", "existing_record_ids": ["AIMech:AStarSearch"], "group": "rtaa", "index": 2, "kind": "bibliography", "next_check": "Resolve the exact bibliographic volume/version if source metadata is revised; preserve ordinary A* versus RTAA scope.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "ed69572e3b79a3996740c2309eb71db728e1603149c78fac5479b089546854bd", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/2", "responsible_owner": {"family": "nested", "index": 393}, "text": "[3] P. Hart, N. Nilsson, and B. Raphael. A formal basis for the\nheuristic determination of minimum cost paths. IEEE\nTransactions on Systems Science and Cybernetics,\n2:100–107, 1968."}
- {"added_record_ids": [], "assessment": "Ishida’s Real-Time Search book is a broad source requiring method-specific reading; it does not resolve main8’s KBFS/multi-state residuals.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:LearningRealTimeAStar", "AIMech:RealTimeAStar"], "group": "rtaa", "index": 3, "kind": "bibliography", "next_check": "Inspect relevant original sections and relate specific methods to nested393/main8 without blanket family closure.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "c22bbe136cf22bc7fbdf2929305f8d4a53523dc7cf990e516867a91ec9eaf73f", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/3", "responsible_owner": {"family": "nested", "index": 393}, "text": "[4] T. Ishida. Real-Time Search for Learning Autonomous\nAgents. Kluwer Academic Publishers, 1997."}
- {"added_record_ids": [], "assessment": "Koenig 2004 is the exact earlier LSS source question already retained under nested393; the current LSS record does not establish version identity.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:LocalSearchSpaceLearningRealTimeAStar"], "group": "rtaa", "index": 4, "kind": "bibliography", "next_check": "Acquire the original and compare name, learning and movement control with the later LSS source.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "11e1e176e92e0b54a9e03c36be628d57cf13aae96e01c0d05e6f67dc851deaab", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/4", "responsible_owner": {"family": "nested", "index": 393}, "text": "[5] S. Koenig. A comparison of fast search methods for real-time\nsituated agents. In Proceedings of the International\nConference on Autonomous Agents and Multi-Agent Systems,\npages 864–871, 2004."}
- {"added_record_ids": [], "assessment": "D* Lite is the exact pending nested393 question, distinct from A*, LSS and RTAA.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:AStarSearch", "AIMech:LocalSearchSpaceLearningRealTimeAStar"], "group": "rtaa", "index": 5, "kind": "bibliography", "next_check": "Read the original incremental g/rhs repair and its relation to Lifelong Planning A*.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "4b979d6327b3008a0d6817ab28fb78f322712daf8121681a0caefa337b561c6b", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/5", "responsible_owner": {"family": "nested", "index": 393}, "text": "[6] S. Koenig and M. Likhachev. D* Lite. In Proceedings of the\nNational Conference on Artiﬁcial Intelligence, pages\n476–483, 2002."}
- {"added_record_ids": [], "assessment": "Adaptive A* is the exact pending nested393 original-source question; repeated complete search is not the same scope as truncated RTAA.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:AStarSearch"], "group": "rtaa", "index": 6, "kind": "bibliography", "next_check": "Inspect the 2005 original and compare complete-search learning with real-time truncation.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "0ef21de09f4ce709a3c362900d9aaf36caf062a484e61a51616bc34c814e319a", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/6", "responsible_owner": {"family": "nested", "index": 393}, "text": "[7] S. Koenig and M. Likhachev. Adaptive A* [poster abstract].\nIn Proceedings of the International Conference on\nAutonomous Agents and Multi-Agent Systems, pages\n1311–1312, 2005."}
- {"added_record_ids": [], "assessment": "Unknown-terrain navigation complexity is a theory/source question; it does not imply unrestricted RTAA guarantees.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:LearningRealTimeAStar", "AIMech:RealTimeAStar"], "group": "rtaa", "index": 7, "kind": "bibliography", "next_check": "Read the original assumptions, bounds and navigation model before transferring any theorem.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "08c09d13bad8ac1d379abce3802f46d2213e119423bd5a7ce1600c4a6dea4dc7", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/7", "responsible_owner": {"family": "nested", "index": 393}, "text": "[8] S. Koenig, C. Tovey, and Y. Smirnov. Performance bounds\nfor planning in unknown terrain. Artiﬁcial Intelligence,\n147:253–279, 2003."}
- {"added_record_ids": [], "assessment": "Korf 1990 has maintained LRTA*, RTA* and minimin-alpha-pruning contexts with distinct update/control scopes.", "disposition": "existing_record_context", "existing_record_ids": ["AIMech:LearningRealTimeAStar", "AIMech:RealTimeAStar", "AIMech:MiniminAlphaPruning"], "group": "rtaa", "index": 8, "kind": "bibliography", "next_check": "Retain those narrow method boundaries and inspect any additional source claim separately.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "70da28ef8e224d6a8cc39aa8d672f4e9a58c1808afcf695da2a5c5e061f7106e", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/8", "responsible_owner": {"family": "nested", "index": 393}, "text": "[9] R. Korf. Real-time heuristic search. Artiﬁcial Intelligence,\n42(2-3):189–211, 1990."}
- {"added_record_ids": [], "assessment": "Pearl’s Heuristics is retained broad background; the year is preserved as printed, not silently corrected or treated as a complete book reading.", "disposition": "retained_context", "existing_record_ids": [], "group": "rtaa", "index": 9, "kind": "bibliography", "next_check": "Resolve the exact edition/year and inspect only the original section needed by a future claim.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "110ae429646c4947920fb3cec5c77f94f6cd9db2f4731a6263d783f07b1251c7", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/9", "responsible_owner": {"family": "nested", "index": 393}, "text": "[10] J. Pearl. Heuristics: Intelligent Search Strategies for\nComputer Problem Solving. Addison-Wesley, 1985."}
- {"added_record_ids": [], "assessment": "Focused D* is a separate incremental-search original and is not automatically identical to D* Lite.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:AStarSearch"], "group": "rtaa", "index": 10, "kind": "bibliography", "next_check": "Inspect Stentz’s original control flow and relation to later D* Lite.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "26365a747f71dca0eb9865553c26a0998e117a7bec208d3823525540f2446a52", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/10", "responsible_owner": {"family": "nested", "index": 393}, "text": "[11] A. Stentz. The focussed D* algorithm for real-time\nreplanning. In Proceedings of the International Joint\nConference on Artiﬁcial Intelligence, pages 1652–1659,\n1995."}
- {"added_record_ids": [], "assessment": "Operational Rationality Through Compilation of Anytime Algorithms is a thesis/source responsibility, not a single assumed algorithm identity.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "rtaa", "index": 11, "kind": "bibliography", "next_check": "Inspect the thesis and identify concrete compilation methods and assumptions.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "44cef92363263d02c9e650e776f0a9eca663f7879fc66517c4ecbe776c4174db", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/11", "responsible_owner": {"family": "nested", "index": 393}, "text": "[12] S. Zilberstein. Operational Rationality through Compilation\nof Anytime Algorithms. PhD thesis, Computer Science\nDepartment, University of California at Berkeley, Berkeley\n(California), 1993."}
- {"added_record_ids": [], "assessment": "Arica et al. is a moving-agent comparison source; source-specific experiments do not create a universal RTAA ranking.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "rtaa", "index": 12, "kind": "bibliography", "next_check": "Inspect the original methods, moving-agent model and experimental protocol.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "47f881a39a3dc18b2f6020f80c7faa8c41a2f94e6b25eaf1c14e031603a12ae7", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/12", "responsible_owner": {"family": "nested", "index": 393}, "text": "Arica, N.; Mut, A.; Yorukcu, A.; and Demir, K. A. 2017.\nAn empirical comparison of search approaches for moving\nagents. Computational Intelligence 33(3):368 – 400."}
- {"added_record_ids": [], "assessment": "Kiesel–Burns–Ruml concerns reaching goals in video games; its concrete real-time procedure remains an original-source question.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:LearningRealTimeAStar", "AIMech:LocalSearchSpaceLearningRealTimeAStar"], "group": "rtaa", "index": 13, "kind": "bibliography", "next_check": "Read the method and experiments before deciding existing context or distinct procedure.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "abb0070fd24784cf9282d9ac93674877731e72487a16a47d295021e934ed2449", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/13", "responsible_owner": {"family": "nested", "index": 393}, "text": "Kiesel, S.; Burns, E.; and Ruml, W. 2015. Achieving goals\nquickly using real-time search: experimental results in video\ngames. Journal of Artiﬁcial Intelligence Research 54:123–\n158."}
- {"added_record_ids": [], "assessment": "Kochvi’s 2017 thesis remains an unread source behind the 2018 comparison; reading the shorter comparison does not complete it.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "rtaa", "index": 14, "kind": "bibliography", "next_check": "Acquire the thesis and resolve timing aggregation, search budget and experiment details.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "5dd177516169f8929528527f4a790e5cd8ffe1307f5765e485b10e3bdd8ff805", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/14", "responsible_owner": {"family": "nested", "index": 393}, "text": "Kochvi, S. 2017. Does fast beat thorough?: Comparing real-\ntime search algorithms LSS-LRTA* and RTAA*. Bachelor’s\nthesis, University of New Hampshire."}
- {"added_record_ids": ["AIMech:RealTimeAdaptiveAStar"], "assessment": "The exact 2006 RTAA defining work supports the proposed RTAA record. This is narrow conditional record representation, not exhaustion of its cited search family or all later variants.", "disposition": "represented_by_added_record", "existing_record_ids": [], "group": "rtaa", "index": 15, "kind": "bibliography", "next_check": "After authorized creation verify the RTAA record; keep workshop/version, Adaptive A*, D* Lite, framework and 2018 timing/thesis residuals open.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "0111426729865368d057732c3711ec5aab1b96726a722e087f25729b514c7258", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/15", "responsible_owner": {"family": "nested", "index": 393}, "text": "Koenig, S., and Likhachev, M. 2006. Real-time adaptive A*.\nIn Proceedings of the Fifth International Joint Conference\non Autonomous Agents and Multiagent Systems, AAMAS\n’06, 281–288."}
- {"added_record_ids": [], "assessment": "Koenig–Sun 2009 is the maintained LSS-LRTA* source context, whose reverse-Dijkstra repair differs from RTAA CLOSED-only F-minus-g learning.", "disposition": "existing_record_context", "existing_record_ids": ["AIMech:LocalSearchSpaceLearningRealTimeAStar"], "group": "rtaa", "index": 16, "kind": "bibliography", "next_check": "Retain source-specific movement/repair assumptions and earlier-version residuals.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "b555e1d111fb33cdf17e0a44360e07c70d0a04b914bfbf4c7681a34b39d52c04", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/16", "responsible_owner": {"family": "nested", "index": 393}, "text": "Koenig, S., and Sun, X. 2009. Comparing real-time and in-\ncremental heuristic search for real-time situated agents. Au-\ntonomous Agents and Multi-Agent Systems 18(3):313–341."}
- {"added_record_ids": [], "assessment": "Korf 1985 is represented in maintained DFID and IDA* scopes; depth-first iterative search is not RTAA.", "disposition": "existing_record_context", "existing_record_ids": ["AIMech:DepthFirstIterativeDeepening", "AIMech:IterativeDeepeningAStar"], "group": "rtaa", "index": 17, "kind": "bibliography", "next_check": "Retain the source/erratum scope and compare any additional claim with its exact original version.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "c4aded8e8f77dae6531166a7129d470fecc53780fb3b56da80b4f08a8c970f3b", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/17", "responsible_owner": {"family": "nested", "index": 393}, "text": "Korf, R. E. 1985. Depth-ﬁrst iterative-deepening: An opti-\nmal admissible tree search. Artiﬁcial Intelligence 27(1):97–\n109."}
- {"added_record_ids": [], "assessment": "Sturtevant grid-based pathfinding benchmarks are retained evaluation/data context, not an asserted separate search algorithm.", "disposition": "retained_context", "existing_record_ids": [], "group": "rtaa", "index": 18, "kind": "bibliography", "next_check": "Inspect benchmark/map/task construction before using performance comparisons.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "7c723f47b8608a86f3dd3da708b0a4742a8dae58e7ec7ac66b2799611ddf8ec5", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/18", "responsible_owner": {"family": "nested", "index": 393}, "text": "Sturtevant, N. 2012. Benchmarks for grid-based pathﬁnd-\ning. Transactions on Computational Intelligence and AI in\nGames 4(2):144 – 148."}
- {"added_record_ids": [], "assessment": "Wilt–Ruml operator-cost-ratio analysis concerns cost representation and best-first search behavior, not a universal RTAA performance claim.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:AStarSearch"], "group": "rtaa", "index": 19, "kind": "bibliography", "next_check": "Read the original analysis and experiment assumptions before comparing algorithms.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json", "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256": "46ce26b84bdcf2f88465efddd56b75dc9c279a19daaae706d8d9deaad3aef3d3", "original_source_details": {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier before further method-specific research or ownership changes; do not append one concept per citation."}, "pointer": "/occurrences/19", "responsible_owner": {"family": "nested", "index": 393}, "text": "Wilt, C., and Ruml, W. 2011. Cost-based heuristic search\nis sensitive to the ratio of operator costs. In Proceedings of\nSoCS."}
- {"added_record_ids": [], "assessment": "The exact AAAI workshop URL remains an unacquired version route. The accepted AAMAS2006 artifact does not prove it identical.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "rtaa", "index": 0, "kind": "retrieval_only", "next_check": "Acquire https://cdn.aaai.org/Workshops/2006/WS-06-11/WS06-11-010.pdf and compare full content/version; retain any failed access.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256": "b4a15bdc388bbb15cfc0101af702665bebff0f2945687984591005186a1b2ef0", "original_source_details": {"scope": "Retrieved in search results; not acquired/read. Potential workshop version must not be assumed identical.", "url": "https://cdn.aaai.org/Workshops/2006/WS-06-11/WS06-11-010.pdf"}, "pointer": "/retrieval_only_leads/0", "responsible_owner": {"family": "nested", "index": 393}, "text": "https://cdn.aaai.org/Workshops/2006/WS-06-11/WS06-11-010.pdf"}
- {"added_record_ids": [], "assessment": "The exact AAMAS2012 search route mentions depression-avoidance/incremental variants but remains unread; no method identity is asserted.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "rtaa", "index": 1, "kind": "retrieval_only", "next_check": "Acquire https://www.ifaamas.org/Proceedings/aamas2012/papers/1F_5.pdf and trace the original 2011 depression-avoidance reference before assessing variants.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256": "ce58720411ded2fc5b936f2f7d28813f36f5e1f1e3e80097b684951e632b0ae0", "original_source_details": {"scope": "Search-result bibliography mentions2011 RTAA depression avoidance and additional incremental variants. Full source unread, not an assessed new concept.", "url": "https://www.ifaamas.org/Proceedings/aamas2012/papers/1F_5.pdf"}, "pointer": "/retrieval_only_leads/1", "responsible_owner": {"family": "nested", "index": 393}, "text": "https://www.ifaamas.org/Proceedings/aamas2012/papers/1F_5.pdf"}
- {"added_record_ids": ["AIMech:RealTimeAdaptiveAStar"], "assessment": "The defining 2006 RTAA source and the exact historical 2018 URL have now been assessed in the accepted RTAA dossier/preview. The 2018 work is a scoped later comparison, with timing/caption/axis and thesis limits retained. Old uninspected statements stay historical provenance.", "disposition": "represented_by_added_record", "existing_record_ids": ["AIMech:LocalSearchSpaceLearningRealTimeAStar", "AIMech:AStarSearch"], "group": "rtaa", "index": 0, "kind": "original_owner_questions", "next_check": "After authorized creation verify the narrow RTAA record. Keep 2018 aggregation/thesis, earlier workshop route and all four other nested393 questions pending.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256": "ea1e4d8de8471d2c58024767ac87b356b4be63a524b0b4a0a44f97306a374a9d", "original_source_details": {"candidate": "RTAA*", "next_check": "Build its own current-state candidate/mapping dossier and check the historical 2018 RTAA URL’s relationship; do not treat either as already curated. Resolve the exact historical route https://www.cs.unh.edu/~ruml/papers/rtaa-star-socs18.pdf without assuming its content from its filename.", "source": "https://idm-lab.org/bib/abstracts/papers/aamas06.pdf"}, "pointer": "/historical_nested393_questions/0", "responsible_owner": {"family": "nested", "index": 393}, "text": "RTAA*"}
- {"added_record_ids": [], "assessment": "D* Lite and its Lifelong Planning A* relation remain independent incremental-search source responsibilities under nested393.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:AStarSearch", "AIMech:LocalSearchSpaceLearningRealTimeAStar"], "group": "rtaa", "index": 1, "kind": "original_owner_questions", "next_check": "Acquire the exact original and compare g/rhs repair, keys, updates and assumptions.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256": "04954b529332376f960c011f588eb8e5b12a43df65c6c12a4b463644f21eb627", "original_source_details": {"candidate": "D* Lite", "next_check": "Acquire original source and analyze incremental g/rhs repair, key/update conditions and relation to Lifelong Planning A*.", "source": "Koenig and Likhachev2002, AAAI,476–483; reference21 in primary manuscript"}, "pointer": "/historical_nested393_questions/1", "responsible_owner": {"family": "nested", "index": 393}, "text": "D* Lite"}
- {"added_record_ids": [], "assessment": "The 2004 LSS predecessor remains an earlier-version/source-continuity question; the later LSS record is context, not proof of exact equality.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:LocalSearchSpaceLearningRealTimeAStar"], "group": "rtaa", "index": 2, "kind": "original_owner_questions", "next_check": "Acquire and compare the original naming, local-space learning and movement control.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256": "bcd4ee6fd17b5b78f1f98af159234164d3c41c7353a504132d2bd41dd2b5f2ff", "original_source_details": {"candidate": "LSS2004 predecessor source", "next_check": "Resolve earlier version and name/method continuity; retain as source follow-up under LSS rather than automatically inventing a separate concept.", "source": "Koenig2004, A comparison of fast search methods for real-time situated agents, AAMAS864–871; reference20"}, "pointer": "/historical_nested393_questions/2", "responsible_owner": {"family": "nested", "index": 393}, "text": "LSS2004 predecessor source"}
- {"added_record_ids": [], "assessment": "Adaptive A* remains the exact complete-search heuristic-learning source question, not resolved by truncated RTAA or ordinary A*.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:AStarSearch"], "group": "rtaa", "index": 3, "kind": "original_owner_questions", "next_check": "Read the 2005 original and compare complete versus truncated search/update assumptions.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256": "4708782da3fb7819c53d72cce242047069114a5e4f4cbac2bdb19948cbe92538", "original_source_details": {"candidate": "Adaptive A*", "next_check": "Assess repeated complete-search heuristic learning separately from real-time truncation and existing A* identity.", "source": "Koenig and Likhachev2005, Adaptive A* poster abstract, AAMAS1311–1312; RTAA reference7"}, "pointer": "/historical_nested393_questions/3", "responsible_owner": {"family": "nested", "index": 393}, "text": "Adaptive A*"}
- {"added_record_ids": [], "assessment": "The Bulitko–Lee framework and concrete variants remain pending under nested393 with main8 as umbrella context. No family exhaustion follows from RTAA or LSS.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:LearningRealTimeAStar", "AIMech:RealTimeAStar", "AIMech:LocalSearchSpaceLearningRealTimeAStar"], "group": "rtaa", "index": 4, "kind": "original_owner_questions", "next_check": "Read the framework, reconcile the 2005/2006 version and concrete variants against main8, LRTA* and RTA*.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json", "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256": "607e681137e0bd1dce92689d508039c2bea19cfb5c7212c31833c671f9a7c2f5", "original_source_details": {"candidate": "Real-time heuristic-search variants and unifying framework", "next_check": "Inspect framework and reconcile its concrete variants with main 8 and maintained LRTA/RTA; no bulk novelty claim.", "source": "Bulitko and Lee2006, Learning in real-time search: A unifying framework, JAIR25:119–157; manuscript reference7"}, "pointer": "/historical_nested393_questions/4", "responsible_owner": {"family": "nested", "index": 393}, "text": "Real-time heuristic-search variants and unifying framework"}
- Exact inherited source scopes are recursively retained under predecessor_state/projection; actual 358 report {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T025054Z-mrec-sma-star-and-iterative-threshold-search.json", "sha256": "24cac330ffb11e5a38b61d5926488b5332040a1b908f2451697a619a4bf4528c"}. No original 402/404/406 closure or family exhaustion is asserted.
- Inherited predecessor_historical_pointer_restorations: exact object SHA256 67987c357ad59ed7c61fbfae19a742f3b2c042ecddf348dd9d1e2aa3cffee62c; original source references remain inside predecessor_state/projection/predecessor_historical_pointer_restorations.
- Inherited earlier_historical_pointer_restorations: exact object SHA256 d1e09f5c15b206b56a5f92cf17640f9e4a2849c090f307de50369e2107f307ed; original source references remain inside predecessor_state/projection/earlier_historical_pointer_restorations.
- Inherited predecessor_deferred_historical_accounting_findings: exact object SHA256 8dac593c15973c74e8173b68efd7f2b20257526aac1b29050f52cbd6b4ee6746; original source references remain inside predecessor_state/projection/predecessor_deferred_historical_accounting_findings.
- Inherited predecessor_governance_provenance: exact object SHA256 c459ffad24e9967ce4eaa41ce66c0d8c882437c7fe4aa17626be5e9b79358bca; original source references remain inside predecessor_state/projection/predecessor_governance_provenance.
- Inherited predecessor_source_followup_accounting: exact object SHA256 e4079c59c57a15a8953d277b346d4c05c96044860fd96f4614e49c38a7bad33d; original source references remain inside predecessor_state/projection/predecessor_source_followup_accounting.
- Inherited predecessor_source_followup_audit: exact object SHA256 a90c635226f1823ab783ab7697d01081e6c8f9e3fd9d5ea98ac4b836494b6008; original source references remain inside predecessor_state/projection/predecessor_source_followup_audit.
- Inherited predecessor_incidental_source_accounting: exact object SHA256 859f88842f9e932a6656ac9b9cea2130a29fca38d478c7cfa36d7a9ad48c5de3; original source references remain inside predecessor_state/projection/predecessor_incidental_source_accounting.
- Inherited predecessor_incidental_source_audit: exact object SHA256 a90c635226f1823ab783ab7697d01081e6c8f9e3fd9d5ea98ac4b836494b6008; original source references remain inside predecessor_state/projection/predecessor_incidental_source_audit.
- Inherited predecessor_search_source_followup_accounting: exact object SHA256 39845183ceba4019e3e05ac21518ca500dbf0ee55d5aa0a1ed4be55e0a905b82; original source references remain inside predecessor_state/projection/predecessor_search_source_followup_accounting.
- Inherited predecessor_search_source_owner_contexts: exact object SHA256 df9f7ddcc44ce809fe00bb7dff4b3caad8847f88362d0a5f0e9906c8429c694c; original source references remain inside predecessor_state/projection/predecessor_search_source_owner_contexts.
- Inherited predecessor_metadata_audit: exact object SHA256 926d11cb738cc4372c0ced24a943ed0dd31eccf7718f3005c565d099f6a7f954; original source references remain inside predecessor_state/projection/predecessor_metadata_audit.
- Inherited original_355_write: exact object SHA256 4c72eb1a738a744162aa78398ebaf7d70cf368580730618004c4adcfc7dfe082; original source references remain inside predecessor_state/projection/original_355_write.
- Inherited predecessor_ritter_source_accounting: exact object SHA256 c125f3d4f63f720af2f5f9f15187eb0714ee1a5833c385802f8e68d5ef06a56b; original source references remain inside predecessor_state/projection/predecessor_ritter_source_accounting.
- Inherited predecessor_ritter_frontier_result: exact object SHA256 93544ff90dab74f51b6a5bcd54f9cbc19e935b89d361c0fcb3b29abbb1d6f81e; original source references remain inside predecessor_state/projection/predecessor_ritter_frontier_result.
- Inherited predecessor_ritter_ownership_plan: exact object SHA256 60971b46989c3d32c8c27e2e2fd78b4cac3ad627909c27fb1e248d43390069fb; original source references remain inside predecessor_state/projection/predecessor_ritter_ownership_plan.
- Inherited predecessor_ritter_ownership_acceptance: exact object SHA256 cc78b22f1671274bbd790aa0d0e1b5c8c51fcf00ef22084f621d3c5f4f1c74c4; original source references remain inside predecessor_state/projection/predecessor_ritter_ownership_acceptance.
- Inherited predecessor_ritter_report: exact object SHA256 37feabf676ee7f0bed44e6709c87a4699096f4cd1c04e992d6891469893cebda; original source references remain inside predecessor_state/projection/predecessor_ritter_report.
- Inherited predecessor_357_metadata_audit: exact object SHA256 b514b69445fa29bbc3b65ec32a3cf601ae57332d7b6b3500b71cea45a7605c89; original source references remain inside predecessor_state/projection/predecessor_357_metadata_audit.
- Inherited memory_search_source_accounting: exact object SHA256 846af9efc9256f36d8862a9bae28f0ca67285803eb74cd13470300e95f5dd8b5; original source references remain inside predecessor_state/projection/memory_search_source_accounting.
- Inherited frontier_result: exact object SHA256 ab60923bf613ba6988b967e82023a909cb3b6c51d9f831155f33886fe4d6732b; original source references remain inside predecessor_state/projection/frontier_result.
- Inherited inherited_issue402_triage: exact object SHA256 4dbf034b0f801e9fdc48abee3eed26c21820384d36af6f5fb15c920ee6de25ed; original source references remain inside predecessor_state/projection/inherited_issue402_triage.
- Actual owner-plan/frontier outcome: {"additional_source_question_count": 0, "bibliography_occurrences": 125, "changed_main_indexes": [8, 909], "changed_nested_indexes": [393], "main": 914, "nested": 394, "new_main_rows": 0, "new_nested_rows": 0}
- Actual source accounting digest (sorted compact JSON UTF-8): 3457194f82c872a14e0fddf1b4f1beacd71593cff596b162a4d4f59ae6714d81
- Actual historical/current identity changes: [{"id": "AIMech:AmortizedSteinVariationalGradientDescent", "field": "identity_notes", "historical": "The proposed scope is the generic differentiable stochastic-sampler training procedure that projects minibatch Stein output directions into shared sampler parameters. Neural samplers are explicitly documented implementations, not a required architecture. It differs from unamortized particle SVGD, Soft Q-learning as a control composite, NVIL/BBVI score estimators, wake-sleep procedures, flow-matching velocity regression and the unchanged ULA transition. Historical research copied 790 native and 442 pinned AIO records while the observed checkout moved from cohort 355 HEAD 5b240a558c8d4c440830183628a348b301d9226f to merged HEAD 917e850123890bd00e671353652fe53101f83bfb. Four ignored/hidden-inclusive roots yielded 31 distinct contents and 38 occurrences, previously read in full; normalization covered 4,888 ID/local-ID/name/alias/scoped-synonym occurrences with no exact candidate match. Eleven selected native scientific contexts, eight pinned AIO CLASS nodes and 66 incident edges were previously inspected. All 913 main and 394 nested objects were recursively queried; selected complete owner bodies were read rather than every unmatched body. These are historical observations, not fresh current or future identity clearance. The source question was retained in historical main 909, whose seven original pending questions remain preserved without closure. Five additional application/umbrella questions are retained in the research dossier with future ownership unset. The 105 bibliography occurrences span three source versions and are not 105 concepts. The proposed ANN related mapping describes the documented neural-sampler implementation relationship; it is not exact equivalence, subclassing or a claim that every differentiable simulator is an ANN.", "current": "Current cohort359 assessment on clean base 0f7e2c5df224901e9284a883dfd0457fd4c29375: ignored-inclusive collection reconciles 1,239 AIO and maintained records and 4,913 identity-field occurrences (3,753 normalized values), with no candidate-name/ID/alias collision. Root read388 ordinary matching contents; an independent reviewer reconciled eight large provenance wrappers and read their relevant source-question leaves. Bounded neighbor definitions distinguish this generic differentiable-sampler fitting component from direct SVGD, Soft Q-learning, ULA and score/ELBO estimators; this is not a global novelty claim. The accepted2016v2 and2017 defining sources, six claims, eight limitations and qualified ANN implementation-related mapping remain unchanged. Main909 is accepted as the exact original citation responsibility, with five application/umbrella followups explicitly assigned for tracking rather than asserted historical ownership. All105 bibliography occurrences and seven original source questions remain exact; the narrow component can be represented while application, version and other-original questions stay open. Earlier citation-only access statements remain historical, including separately prepared but not maintained SVPG.", "root_decision": "records/AIMech:AmortizedSteinVariationalGradientDescent/identity_notes"}, {"id": "AIMech:RealTimeAdaptiveAStar", "field": "identity_notes", "historical": "The proposed identity is the named 2006 Real-Time Adaptive A* algorithm with bounded forward A*, the CLOSED-only F−g heuristic update, and a separately chosen movement cap. It differs from ordinary A* as its embedded search, one-state LRTA*, second-best RTA*, and the reverse-Dijkstra learning phase of LSS-LRTA*. Equality with the paper’s 2004 larger-lookahead LRTA comparator at lookahead one and identical ties is a special case, not general concept equivalence. The historical research snapshot at 2026-10-16T01:14:43Z–01:15:17Z observed cohort356 HEAD 917e850123890bd00e671353652fe53101f83bfb with uncommitted actual356 additions, 792 native and 442 pinned AIO records. Four ignored/hidden-inclusive roots, excluding Git administrative contents, yielded 34 distinct contents and 47 occurrences previously read in full. Mechanical normalization covered 4,896 ID/local-ID/name/alias/scoped-synonym occurrences with no exact candidate match in that snapshot. Eight immediate native algorithm contexts plus DFID/IDA definition contexts, nine exact AIO CLASS nodes and 48 incident edges were assessed. All 913 main and 394 nested objects were recursively queried, with matching nested393 and complete broader main8 read; unrelated record definitions and unmatched frontier bodies were not all semantically reread. These are historical observations, not future identity clearance. The original RTAA source question remains preserved under historical nested393 within main8, alongside D* Lite, the LSS2004 predecessor, Adaptive A* and the Bulitko–Lee framework; main8 also retains KBFS and multi-state commitment residuals. The 2018 route is now evidenced as a later comparison paper, not a second defining identity. Twenty bibliography occurrences and two retrieval-only leads remain source questions with no future owner assignment or novelty count. The weak proposed MachineLearningTask related mapping concerns persistent heuristic learning; it does not assert identity, subclassing or a reinforcement-learning model.", "current": "Current cohort359 assessment on clean base 0f7e2c5df224901e9284a883dfd0457fd4c29375: the same ignored-inclusive collection and attributed root/independent matching-content readings found no candidate identity collision in the1,239-record snapshot. Bounded current comparisons distinguish CLOSED-only F-minus-g heuristic repair and separately controlled movement from ordinary A*, basic LRTA*/RTA*, LSS reverse-Dijkstra learning and memory/threshold search. The accepted2006 defining source,2018 later-comparison artifact, eight claims, ten limitations and weak learning-task related mapping remain unchanged; the task class is not algorithm identity or subclass. Nested393 is the accepted exact source responsibility, with main8 retaining an umbrella cross-reference. All20 bibliography occurrences, five original questions and two retrieval routes remain exact. The current2018 reading advances the historical route question but retains timing aggregation, caption/axis and thesis limits; D* Lite/LPA, Adaptive A*, earlier LSS and framework/variant questions remain pending.", "root_decision": "records/AIMech:RealTimeAdaptiveAStar/identity_notes"}]

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T035648Z-amortized-svgd-and-real-time-adaptive-a-star
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of amortized SVGD and Real-Time Adaptive A-star
started_at: '2026-10-16T03:56:43.125821Z'
finished_at: '2026-10-16T03:56:48.278280Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Author self-review with separately attributed root, research
    and supporting mathematical reading. Preparing this scaffold is not independent
    scientific approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain amortized SVGD and Real-Time Adaptive A-star as separate source-scoped
  DRAFT algorithms. Fourteen claims and18 limitations preserve the generic sampler
  fitting/projection boundaries and the RTAA planning/update/execution controller
  with its own theorem and later-comparison scope. Exact current and inherited source
  responsibilities remain pending where appropriate.
source:
  git_revision: 0f7e2c5df224901e9284a883dfd0457fd4c29375
  state: working_tree
  inputs:
  - path: .claude/skills/review-category/SKILL.md
    sha256: 553c3870c1dfc127f90f196b7b212b644706d4c26e2a578ab615ccce588070d7
    role: context
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/DecisionTree.yaml
    sha256: 4c2a5ed08c585f8912d66e3629aaa20e93c46ab49cfb2d128001fcd019c81bfc
    role: context
  - path: data/aio/DeepNeuralNetwork.yaml
    sha256: f5c4c7764ea05631bb6396200141eb8ba124725d2dc27919c7efe89e5e30b19e
    role: context
  - path: data/aio/GenerativeAdversarialNetwork.yaml
    sha256: 4f5080d92af8eaea513deed39c60679f0eb7a62d03e5be0d0d8d5c966a9a4544
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/MetaLearning.yaml
    sha256: 4a1835675f779c8f924cfe085f1b5def3b5c6a2c111596385c61063056f3b8a6
    role: context
  - path: data/aio/Network.yaml
    sha256: ec24eb397241fe903137b2d8c8f4081d0f9d246c296c247864f199e160a3ee30
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/ReinforcementLearningLLM.yaml
    sha256: e386376b9b1a9c78349d66e8609a655e273620d8bc607978c728ac3b7ce3808a
    role: context
  - path: data/aio/SelfsupervisedLearning.yaml
    sha256: ad9a98dfee5629f6433f13470f56e333316f8f03847df2c5678faf023d979c0e
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/curated/AStarSearch.yaml
    sha256: 685cfd5d6b4eaf0811d597e93e117ad065857d5707f0040420d3e6885f520b8d
    role: context
  - path: data/curated/AmortizedSteinVariationalGradientDescent.yaml
    sha256: 9432b34f9db5c87440ad62e1822882d72999da00b9eb7b9a636acb723e2895d9
    role: target
  - path: data/curated/BestFirstSearch.yaml
    sha256: d43811f831e3a4d2c08e861f5a973c03ec481c1b406d724c042847b7dbb426bf
    role: context
  - path: data/curated/BlackBoxVariationalInference.yaml
    sha256: 8237d3233ae06163b8fab5b4fa047ffc938e275bc1e3ede883348e06c2b266a8
    role: context
  - path: data/curated/DepthFirstIterativeDeepening.yaml
    sha256: 2e01d2da093397d74a7647e624015b8b0f54d14c7420e00d3ded18a576ce605d
    role: context
  - path: data/curated/DijkstraShortestPath.yaml
    sha256: 071e00cd1f866ecf4ac09bb8da375a6bb6c576d6453dd70ad062058b9278e496
    role: context
  - path: data/curated/EnforcedHillClimbing.yaml
    sha256: 897d9d1e6437d068a16e83e1bc6431683ac8de49e6ea82ad8a0b553df812a54c
    role: context
  - path: data/curated/FlowMatching.yaml
    sha256: 3e7122ee85f438483256afcce7b4621b4701d10a0022b8efa1f0eb86c6a02887
    role: context
  - path: data/curated/GreedyBestFirstSearch.yaml
    sha256: ec49328f0c41b8205dfe2816c9a01fdb50fa1e1292eacee71fc2872c7cc54020
    role: context
  - path: data/curated/HelmholtzMachine.yaml
    sha256: 9b582e184b171ae372dca219cd6704318a9287150dcbf540f95a8b4cc6405cac
    role: context
  - path: data/curated/IterativeDeepeningAStar.yaml
    sha256: 0a9b9b571f3e7179658db63ce60f2e4febac10c4470212b5b0270b86b9eeac6c
    role: context
  - path: data/curated/LearningRealTimeAStar.yaml
    sha256: 189cfd138de434f3bf350bcf5a18684712c602fc96b3f4ba0abeed5f80e65ceb
    role: context
  - path: data/curated/LocalSearchSpaceLearningRealTimeAStar.yaml
    sha256: 7ac410b5775e73d529bf5d98c93df6f90d187ee35ded28dcb773d4a2f7c461c2
    role: context
  - path: data/curated/NeuralVariationalInferenceAndLearning.yaml
    sha256: 0d24a286ed64974478f452907c018d9618348ef4900808ea97b80036b1dfb06c
    role: context
  - path: data/curated/RealTimeAStar.yaml
    sha256: 4c3378011e027f000c548f4fc56cd67b139c821cc157efe2f1bcf19d6ee3e7d3
    role: context
  - path: data/curated/RealTimeAdaptiveAStar.yaml
    sha256: fd094b4cbc70d64f22498cffa10b5adf4b84b252f2a49cce8faa66d67f5651bc
    role: target
  - path: data/curated/RectifiedFlow.yaml
    sha256: 10025e94e6142cb77cc95f963afb4c5c70c96a7cdaac208a02420bd30245bd01
    role: context
  - path: data/curated/ReweightedWakeSleep.yaml
    sha256: 49509aa6868bcefabf54790503a9d5b87f0d873ab1589cdb6677b5575b3c8997
    role: context
  - path: data/curated/SoftQLearning.yaml
    sha256: 30a9c92eac4e3169d040b64230b7efd6ec8d9685ea58cd5136f4a2d7fa895dca
    role: context
  - path: data/curated/SteinVariationalGradientDescent.yaml
    sha256: 306808b660d4ce0880599e6acc901c5352c8a92d3ed6db58f89bd2b3c107d2b0
    role: context
  - path: data/curated/UnadjustedLangevinAlgorithm.yaml
    sha256: 4c09ef556111d807d01b68678691453752de613610bb23239c9480b90b8535eb
    role: context
  - path: data/curated/VariationalExpectationMaximization.yaml
    sha256: 5ec118dcfd17dd552866d1f4b883ed273c812c04aca5c3eefc628a5f8035ad5d
    role: context
  - path: data/curated/WakeSleepAlgorithm.yaml
    sha256: 48b795b8f0730fc884c1809d405e125ec09b3a906e9b875f9ff3b1772fb21f48
    role: context
  - path: docs/curated-concepts.md
    sha256: 79c497b615b9ba703d67ccfc1a925f5d5c3c527aff6ab323cd271aec8e5a40dc
    role: context
  - path: docs/record-review-profile.md
    sha256: 2d3e3a73264523c78930d17b0812e2d22887e25423fe7c38e0ddce922d9cec9d
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/reports/amortized-svgd-and-real-time-adaptive-a-star/2026-10-16T034327Z-codex-1eb03c.yaml
    sha256: 2b36a87272003ef6f707070e7584d37a8fea3e600f96c1112ca003181564d196
    role: context
  - path: justfile
    sha256: 2d9c1b68c1c80d53aa44a6b8b5e916efe8b493650ff59a3fc7479a42be37f400
    role: context
  - path: research/discovery/20261011T034528Z-reinforcement-learning-methods.json
    sha256: 77986405a5635886714741dba5154ac6b6b3aa3e73e7db09269a2cf2782e1c68
    role: context
  - path: research/discovery/20261011T035430Z-attribution-methods.json
    sha256: 8d0137e23ddc9f28ed1c1026d6bcf6310b82a5a11ea447477e0165a98c446500
    role: context
  - path: research/discovery/20261011T044233Z-flow-and-consistency-methods.json
    sha256: 1efa09e3896278d035b838cf5ee1152a70ea383c014c93d3763b6482f41b1d0b
    role: context
  - path: research/discovery/20261012T071653Z-support-vector-sphere.json
    sha256: 26a5c75316bf7ab14b402cc64e1369c50418cf1e1a8570955fe5cf655bc8c95d
    role: context
  - path: research/discovery/20261012T073618Z-support-description.json
    sha256: 641021eca5b4c440875934019acbbd46fdca5c084ed5688990fc1fba16e9ebb8
    role: context
  - path: research/discovery/20261015T220733Z-lpga-minimin-and-restored-historical-pointers.json
    sha256: 70390ddcefe988c8db1883ad3c798d430425ca4d9c487ea0944de8bce5b9fa32
    role: context
  - path: research/discovery/20261015T225549Z-autowalksat-fixed-noise-controller.json
    sha256: 7ebc4da1f0029b920b1a71a484cd4bec3af9ac92c34894a06103c3ab247621d4
    role: context
  - path: research/discovery/20261015T233554Z-hrsat-tsat-and-restored-search-pointers.json
    sha256: cfb1da2d42702cf571b4b3594c8f408f33392a02bc7dd8b79c50a9b09adb279f
    role: context
  - path: research/discovery/20261015T233554Z-hrsat-tsat-and-restored-search-pointers.md
    sha256: 220b798255e6e9d71006e704b007bbddd8838693efd1c16dd901253d8640d9e6
    role: context
  - path: research/discovery/20261016T010736Z-enforced-hill-climbing-and-local-search-space-lrta.json
    sha256: 516283d10873d36554792b9cc6aac0352cdb000badd1dda54110a330fbd712b7
    role: context
  - path: research/discovery/20261016T020317Z-ritter-gallegos-two-stage-fitting-and-ieco-classification.json
    sha256: a2bf46b1870ccc44138e7c4a5f7a968bf9257a73beea87cbd9471b1177253a04
    role: context
  - path: research/discovery/20261016T025054Z-mrec-sma-star-and-iterative-threshold-search.json
    sha256: 24cac330ffb11e5a38b61d5926488b5332040a1b908f2451697a619a4bf4528c
    role: context
  - path: research/discovery/20261016T034316Z-amortized-svgd-and-real-time-adaptive-a-star.json
    sha256: 5aaa5f8a608224430161ccddacc1cc2cbd7ecedba79e8cec86b52ee81ec4056d
    role: context
  - path: research/discovery/20261016T034316Z-amortized-svgd-and-real-time-adaptive-a-star.md
    sha256: 4e74f183589d2ebe8167debda831272f2e7db3eff45bb7b1ba8129ae46106d70
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/render_pages.py
    sha256: 81fae327c4670e269e8928b53f0370e2853767ec8e1b495f6206216ac03f304a
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
  - path: src/aimech/importer.py
    sha256: 7c2dd8e12f18b76cfb5ed4acc7e1901ae9a968b3a6c7a9d62cb260bc2f1ad3ab
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: 3826f6a7643d6a0140cf60bb52a1d3ac2fbab4811b4fd8d1d178a13c3341fa3f
    role: context
  - path: src/aimech/validation.py
    sha256: 274ed5e6bc97440515a1964b9b21927135a2e9a5a4808ae8daebccd3e172ffcc
    role: context
scope:
  description: Two exact current native records from accepted cohort359 creation;
    all selected claims and limitations assessed. Historical source and neighbor reading
    scopes remain separately attributed.
  selection: Exact AIMech:AmortizedSteinVariationalGradientDescent, AIMech:RealTimeAdaptiveAStar.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  - AIMech:RealTimeAdaptiveAStar
  exclusions:
  - target: Application-specific SteinGAN, amortized KSD, Stein VAE, learned Langevin
      schedules and Wild VI umbrella procedures
    reason: Separate source questions retained without asserting equivalence or full
      coverage by the generic sampler.
  - target: RTAA retrieval-only routes and other parent search procedures
    reason: Unread versions and distinct search controllers retain their own source
      responsibilities.
  - target: Inherited402/404/406 and356/357/358 source accounting
    reason: Full original scopes and later dispositions remain queryable; whole issues
      and source families are not closed.
checks:
- check_id: check-gate
  name: just check
  status: passed
  required: true
  summary: Actual completed command exited0; exact output and timing retained.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  - AIMech:RealTimeAdaptiveAStar
  command: just check
  exit_code: 0
  evidence_ids:
  - check-gate
- check_id: check-vendor
  name: just vendored-check
  status: passed
  required: true
  summary: Actual completed command exited0; exact output and timing retained.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  - AIMech:RealTimeAdaptiveAStar
  command: just vendored-check
  exit_code: 0
  evidence_ids:
  - check-vendor
- check_id: check-check-source
  name: uv run --locked aimech check-source
  status: passed
  required: true
  summary: Actual completed command exited0; exact output and timing retained.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  - AIMech:RealTimeAdaptiveAStar
  command: uv run --locked aimech check-source
  exit_code: 0
  evidence_ids:
  - check-check-source
- check_id: check-render
  name: just render
  status: passed
  required: true
  summary: Actual completed command exited0; exact output and timing retained.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  - AIMech:RealTimeAdaptiveAStar
  command: just render
  exit_code: 0
  evidence_ids:
  - check-render
- check_id: check-render-check
  name: just render-check
  status: passed
  required: true
  summary: Actual completed command exited0; exact output and timing retained.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  - AIMech:RealTimeAdaptiveAStar
  command: just render-check
  exit_code: 0
  evidence_ids:
  - check-render-check
- check_id: check-diff
  name: git diff --check
  status: passed
  required: true
  summary: Actual completed command exited0; exact output and timing retained.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  - AIMech:RealTimeAdaptiveAStar
  command: git diff --check
  exit_code: 0
  evidence_ids:
  - check-diff
- check_id: historical-failed-check-1
  name: just vendored-check (retained earlier attempt)
  status: failed
  required: false
  summary: Historical unsuccessful attempt retained; later exact required command
    passed.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  - AIMech:RealTimeAdaptiveAStar
  command: just vendored-check
  exit_code: 1
  evidence_ids:
  - historical-failed-check-1
evidence:
- evidence_id: src-wang-liu2016-v2
  kind: primary_source
  reference: /private/tmp/aimech-amortized-svgd-research-20261016/arxiv-v2.pdf
  snapshot_sha256: a6c5cffaedb4aabc1243c22e809d332ce7c00bcd564a6846fe5054bab5239477
  accessed_at: '2026-10-16T00:53:17Z'
  support: supports
  summary: 'Learning to Draw Samples: With Application to Amortized MLE for Generative
    Adversarial Learning. Exact arXiv:1611.01722v2, 26 November 2016; under-review
    preprint, no ICLR acceptance asserted. Declared role: defining_method. Primary
    reading is attributed to the selected source support and its reading receipts.'
- evidence_id: src-feng-wang-liu2017
  kind: primary_source
  reference: /private/tmp/aimech-amortized-svgd-research-20261016/uai2017.pdf
  snapshot_sha256: ad78165b3ed79994071b6ebb375a41cee67d24e962ecc24d15e48812d19a26ef
  accessed_at: '2026-10-16T00:53:24Z'
  support: supports
  summary: 'Learning to Draw Samples with Amortized Stein Variational Gradient Descent.
    Exact Official UAI 2017 proceedings paper 206, inspected ten-page PDF; distinct
    work from arXiv:1611.01722. Declared role: defining_method. Primary reading is
    attributed to the selected source support and its reading receipts.'
- evidence_id: amortized-svgd-accepted-preview
  kind: record_content
  reference: /private/tmp/aimech-amortized-svgd-native-preview-20261016/native-preview.json
  snapshot_sha256: 6081d71066af50e40f1b622a506b83ba19d582767bdf381c599c6cf1c2b234a4
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact root-accepted historical TEMP native preview; no current canonical
    creation or semantic clearance is inferred.
- evidence_id: amortized-svgd-prior-support
  kind: record_content
  reference: /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json
  snapshot_sha256: 14598ff393b6ccf92756eee791803cc8810643f7bd0538f3c0140cbf5245c88c
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact accepted source-scoped definition, claim and limitation assessment,
    including source locators and attributed reading.
- evidence_id: amortized-svgd-root-preview-readback
  kind: record_content
  reference: /private/tmp/aimech-amortized-svgd-native-preview-20261016/root-preview-readback.json
  snapshot_sha256: a22168dd63ee4f88143237e074fcc03da93196c62f6e006c6be783a3838809f8
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Root acceptance of the exact historical native preview and native validation,
    separate from future ownership.
- evidence_id: amortized-svgd-reading
  kind: record_content
  reference: /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/reading-attribution.json
  snapshot_sha256: ec13887a5d7466d04c358f3232d3bbdc900b9edffb2a97249e742f7682a18949
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Attributed primary/source/neighbor reading; no fresh source-read claim
    is made by this assembly.
- evidence_id: amortized-svgd-limitation-1-support
  kind: record_content
  reference: /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json
  snapshot_sha256: 14598ff393b6ccf92756eee791803cc8810643f7bd0538f3c0140cbf5245c88c
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/0; arxiv-v2 Section2 pp3–4; curator normalization consequence
- evidence_id: amortized-svgd-limitation-2-support
  kind: record_content
  reference: /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json
  snapshot_sha256: 14598ff393b6ccf92756eee791803cc8810643f7bd0538f3c0140cbf5245c88c
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/1; arxiv-v2 Eq2–6 pp3–4; UAI Problem1 p1 allows discrete seeds;
    UAI Section4.1/5.2 dropout examples pp5,8–9; curator measure distinction
- evidence_id: amortized-svgd-limitation-3-support
  kind: record_content
  reference: /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json
  snapshot_sha256: 14598ff393b6ccf92756eee791803cc8810643f7bd0538f3c0140cbf5245c88c
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/2; arxiv-v2 Eq8–10 p5; UAI Eq13–15 p4; both conclusions leave
    theoretical understanding for future work; curator projection analysis
- evidence_id: amortized-svgd-limitation-4-support
  kind: record_content
  reference: /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json
  snapshot_sha256: 14598ff393b6ccf92756eee791803cc8810643f7bd0538f3c0140cbf5245c88c
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/3; arxiv-v2 p5 Eq8–10; UAI2017 and later arXiv p4 Eq13–15,
    all three visuals inspected
- evidence_id: amortized-svgd-limitation-5-support
  kind: record_content
  reference: /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json
  snapshot_sha256: 14598ff393b6ccf92756eee791803cc8810643f7bd0538f3c0140cbf5245c88c
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/4; arxiv-v2 p4; UAI2017 pp3,7; curator kernel consequences
- evidence_id: amortized-svgd-limitation-6-support
  kind: record_content
  reference: /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json
  snapshot_sha256: 14598ff393b6ccf92756eee791803cc8810643f7bd0538f3c0140cbf5245c88c
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/5; arxiv-v2 Eq11–12 pp5–6; UAI Eq16–17 p5; curator interpretation
    of Eq8/13
- evidence_id: amortized-svgd-limitation-7-support
  kind: record_content
  reference: /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json
  snapshot_sha256: 14598ff393b6ccf92756eee791803cc8810643f7bd0538f3c0140cbf5245c88c
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/6; arxiv-v2 Eq13–16 pp6–8; UAI Eq20–23 pp5–6; curator qualifications
- evidence_id: amortized-svgd-limitation-8-support
  kind: record_content
  reference: /private/tmp/aimech-amortized-svgd-draft-preparation-20261016/successor-v2/scientific-support.json
  snapshot_sha256: 14598ff393b6ccf92756eee791803cc8810643f7bd0538f3c0140cbf5245c88c
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/7; retained complete text diffs; 2016p9 tables; later2017pp10–12
- evidence_id: src-koenig-likhachev2006
  kind: primary_source
  reference: /private/tmp/aimech-rtaa-standalone-research-20261016/koenig-likhachev2006-current.pdf
  snapshot_sha256: 9ad098fbeaa307b3885f03ca9997618748d3ed1c61928f0404dcb7ac01a77bf3
  accessed_at: '2026-10-16T01:14:01Z'
  support: supports
  summary: 'Real-Time Adaptive A*. Exact Author-hosted eight-page AAMAS 2006 paper,
    proceedings pp.281–288; defining method. Workshop version not inspected.. Declared
    role: defining_method. Primary reading is attributed to the selected source support
    and its reading receipts.'
- evidence_id: src-kochvi-ruml2018
  kind: primary_source
  reference: /private/tmp/aimech-rtaa-standalone-research-20261016/rtaa-star-socs18.pdf
  snapshot_sha256: a30caf4dcfe9b69ee91b2ef5c180d68defa546e83a61f258e607e0132d6e8a0a
  accessed_at: '2026-10-16T01:14:03Z'
  support: supports
  summary: 'Does Fast Beat Thorough? Comparing RTAA* and LSS-LRTA*. Exact Author-hosted
    five-page SoCS 2018 manuscript, volume9(1), proceedings pp.163–167; later empirical
    comparison. Publisher PDF bytes not inspected.. Declared role: later_empirical_comparison_and_limitations.
    Primary reading is attributed to the selected source support and its reading receipts.'
- evidence_id: rtaa-accepted-preview
  kind: record_content
  reference: /private/tmp/aimech-rtaa-native-preview-20261016/native-preview.json
  snapshot_sha256: f2c0bf3a63682026daf953c3777ece4acc0f096248725eb2c9a9ce94f1b8aa82
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact root-accepted historical TEMP native preview; no current canonical
    creation or semantic clearance is inferred.
- evidence_id: rtaa-prior-support
  kind: record_content
  reference: /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json
  snapshot_sha256: 0f672572371e5059b8764e06cdf3ed021a6fb2c579abc688395d0c56c1e38bd5
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact accepted source-scoped definition, claim and limitation assessment,
    including source locators and attributed reading.
- evidence_id: rtaa-root-preview-readback
  kind: record_content
  reference: /private/tmp/aimech-rtaa-native-preview-20261016/root-preview-readback.json
  snapshot_sha256: d55631c2371f1f15320371e213fc4d4f708474fa323812c2b1965d29993412e7
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Root acceptance of the exact historical native preview and native validation,
    separate from future ownership.
- evidence_id: rtaa-reading
  kind: record_content
  reference: /private/tmp/aimech-rtaa-draft-preparation-20261016/reading-attribution.json
  snapshot_sha256: b1b9de253b4c63cbe725368e68178aab453616feb40199898d474d9fc8270d56
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Attributed primary/source/neighbor reading; no fresh source-read claim
    is made by this assembly.
- evidence_id: rtaa-limitation-1-support
  kind: record_content
  reference: /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json
  snapshot_sha256: 0f672572371e5059b8764e06cdf3ed021a6fb2c579abc688395d0c56c1e38bd5
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/0; 2006 PDF2 Sections3–4; PDF3 Theorems1–3; PDF8 future work
    explicitly mentions inconsistent heuristics.
- evidence_id: rtaa-limitation-2-support
  kind: record_content
  reference: /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json
  snapshot_sha256: 0f672572371e5059b8764e06cdf3ed021a6fb2c579abc688395d0c56c1e38bd5
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/1; 2006 PDF2 Section3 and Figure1 lines04–05; PDF3 Theorem3.
- evidence_id: rtaa-limitation-3-support
  kind: record_content
  reference: /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json
  snapshot_sha256: 0f672572371e5059b8764e06cdf3ed021a6fb2c579abc688395d0c56c1e38bd5
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/2; 2006 PDF2 notation, consistency and Figure1; PDF3 Theorem2.
- evidence_id: rtaa-limitation-4-support
  kind: record_content
  reference: /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json
  snapshot_sha256: 0f672572371e5059b8764e06cdf3ed021a6fb2c579abc688395d0c56c1e38bd5
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/3; 2006 Figure1/Section8;2018 PDF2 Experimental Set-up.
- evidence_id: rtaa-limitation-5-support
  kind: record_content
  reference: /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json
  snapshot_sha256: 0f672572371e5059b8764e06cdf3ed021a6fb2c579abc688395d0c56c1e38bd5
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/4; 2006 PDF3–4 Theorem4; PDF7 Table1.
- evidence_id: rtaa-limitation-6-support
  kind: record_content
  reference: /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json
  snapshot_sha256: 0f672572371e5059b8764e06cdf3ed021a6fb2c579abc688395d0c56c1e38bd5
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/5; 2006 PDF4 Section5 and references5/7/9.
- evidence_id: rtaa-limitation-7-support
  kind: record_content
  reference: /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json
  snapshot_sha256: 0f672572371e5059b8764e06cdf3ed021a6fb2c579abc688395d0c56c1e38bd5
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/6; 2006 PDF4 final paragraph,PDF6–8;2018 full comparison and
    PDF5 limitations.
- evidence_id: rtaa-limitation-8-support
  kind: record_content
  reference: /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json
  snapshot_sha256: 0f672572371e5059b8764e06cdf3ed021a6fb2c579abc688395d0c56c1e38bd5
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/7; 2018 PDF2 Unknown Terrain paragraphs; PDF3 Figure1 and
    PDF4–5 axes; all visually checked.
- evidence_id: rtaa-limitation-9-support
  kind: record_content
  reference: /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json
  snapshot_sha256: 0f672572371e5059b8764e06cdf3ed021a6fb2c579abc688395d0c56c1e38bd5
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/8; 2018 PDF3–4 Traffic.
- evidence_id: rtaa-limitation-10-support
  kind: record_content
  reference: /private/tmp/aimech-rtaa-draft-preparation-20261016/scientific-support.json
  snapshot_sha256: 0f672572371e5059b8764e06cdf3ed021a6fb2c579abc688395d0c56c1e38bd5
  accessed_at: '2026-10-16T02:19:21.788499Z'
  support: context_only
  summary: Exact limitation statement, source/mathematical attribution and bounded
    assessment; cited research context retains its own source role.
  locator: /limitations/9; 2018 PDF2 Unknown Terrain; PDF5 Conclusions; actual web403
    receipt.
- evidence_id: retained-template-validation-failure
  kind: validation
  reference: /private/tmp/aimech-cohort359-review-save-validate.json
  snapshot_sha256: 6b3bd99efadac7dc90ebf284e564757d168f2fc6c893e23090e2bb3e14f2a51a
  accessed_at: '2026-10-16T03:55:50.615376Z'
  support: context_only
  summary: Earlier TEMP formal review validation rejected +00:00 timestamp serialization;
    no canonical review was saved. Successor emits equivalent UTC instants with required
    Z suffix. Scientific records and assessment narratives are unchanged.
- evidence_id: actual-write
  kind: record_content
  reference: /private/tmp/aimech-cohort359-write.json
  snapshot_sha256: 5422c3560492917cdfa5114bebc9c20b5e37d3a36b9863f741daa6f221fdbf62
  accessed_at: '2026-10-16T03:56:48.203090Z'
  support: context_only
  summary: Actual exclusive creation of two native records, report pair and CREATE
    history.
- evidence_id: captured-inputs
  kind: record_content
  reference: /private/tmp/aimech-cohort359-postwrite-20261016/actual-capture.json
  snapshot_sha256: e432fcd5eb2cf6a642ab7b3c25f1954e7d642d0e037334d40f8b1f8ca295cd5a
  accessed_at: '2026-10-16T03:56:48.203601Z'
  support: context_only
  summary: Actual canonical input-byte and maintained-target capture.
- evidence_id: postcapture-reading
  kind: record_content
  reference: /private/tmp/aimech-cohort359-timestamp-recovery-20261016/root-generation-reading.json
  snapshot_sha256: 47fcf5fb0e0d51fe2815cc7a922ecc5e2123ea08228d7f9593bcf7b2f089e85b
  accessed_at: '2026-10-16T03:56:48.203881Z'
  support: context_only
  summary: Actual root reading of source-scoped canonical records, metadata and all
    retained question objects; historical source reading stays separately attributed.
- evidence_id: governance-assessment
  kind: record_content
  reference: /private/tmp/aimech-cohort359-governance-20261016/assessment.json
  snapshot_sha256: 4d2e109beee3213430377755ee631a2310197a18a0770b8f16d37ce8de408be9
  accessed_at: '2026-10-16T03:56:48.207547Z'
  support: context_only
  summary: Actual byte preservation, dynamic owner-plan reconstruction, inherited
    metadata and parsed-page audit.
- evidence_id: rendered-pages
  kind: record_content
  reference: /private/tmp/aimech-cohort359-governance-20261016/rendered-pages.json
  snapshot_sha256: a9c0206b8ab4102d1eadb4c13799f8cefe38f65b229ce437e668f91e983be2e0
  accessed_at: '2026-10-16T03:56:48.207834Z'
  support: context_only
  summary: Actual generated-page bytes and parsed content; no visual/layout inspection.
- evidence_id: actual-scientific-assessment
  kind: record_content
  reference: /private/tmp/aimech-cohort359-actual-adversarial-review-20261016/assessment.preliminary.json
  snapshot_sha256: f9fcaa41260050b805b1202db2d3c661072468ae8ad83d53135f6aec070e3fa3
  accessed_at: '2026-10-16T03:56:48.208266Z'
  support: context_only
  summary: Actual record scientific assessment with its own attributed source-reading
    scope.
- evidence_id: current-identity-collection
  kind: search
  reference: /private/tmp/aimech-cohort359-current-identity-20261016/collection.json
  snapshot_sha256: b47e240c696d5ca0ffbf2fa8837ea6bf4fe9e736616708253b359cf81fbd13fa
  accessed_at: '2026-10-16T03:56:48.211014Z'
  support: context_only
  summary: Actual scoped ignored-inclusive identity collection; mechanical capture
    is distinct from human semantic reading.
  search_scope: Current ignored-inclusive fixed-string word-boundary scans across
    the four recorded roots; 4,133 matching occurrences reconciled into396 content
    groups. Root freshly read388 ordinary contents; independent reviewer reconciled
    eight inherited wrappers to previously reviewed canonical358 fields and read16
    relevant leaves. Normalized inventory covers797native+442AIO records,4913identity
    occurrences and3753unique normalized values. Bounded semantic neighbor/source
    assessment is not global novelty or literature exhaustion.
- evidence_id: current-context-assessment
  kind: search
  reference: /private/tmp/aimech-cohort359-final-inputs-20261016/collection-assessment.json
  snapshot_sha256: f63b9c9ab4f237c1e7b5b812f1f5cd574f18e666a10f2b55c9c4b009b18f518c
  accessed_at: '2026-10-16T03:56:48.211384Z'
  support: context_only
  summary: Actual attributed current identity and source-question assessment.
  search_scope: Current ignored-inclusive fixed-string word-boundary scans across
    the four recorded roots; 4,133 matching occurrences reconciled into396 content
    groups. Root freshly read388 ordinary contents; independent reviewer reconciled
    eight inherited wrappers to previously reviewed canonical358 fields and read16
    relevant leaves. Normalized inventory covers797native+442AIO records,4913identity
    occurrences and3753unique normalized values. Bounded semantic neighbor/source
    assessment is not global novelty or literature exhaustion.
- evidence_id: root-decisions
  kind: record_content
  reference: /private/tmp/aimech-cohort359-final-inputs-20261016/root-decisions.json
  snapshot_sha256: 2f89dececcf2e694b956c470f6462cc5679c1e4ebf931da28d4da4dcfed4f411
  accessed_at: '2026-10-16T03:56:48.213225Z'
  support: context_only
  summary: Exact current record identity decisions, dynamic accepted ownership and
    retained source questions.
- evidence_id: ownership-plan
  kind: record_content
  reference: /private/tmp/aimech-cohort359-source-ownership-proposal-20261016/ownership-plan.proposed.json
  snapshot_sha256: eef85e6763545177c5ff00d45a74706c4166f0927d171bb0d05e7d1a48eff0cd
  accessed_at: '2026-10-16T03:56:48.215054Z'
  support: context_only
  summary: Exact distinct source responsibilities for two records,125 bibliography
    occurrences,19 original/dossier/retrieval objects and any additional source questions.
- evidence_id: ownership-plan-acceptance
  kind: record_content
  reference: /private/tmp/aimech-cohort359-final-inputs-20261016/ownership-acceptance.json
  snapshot_sha256: eb94714edfd1167c843ba6d415f1e1a75e876879bd0dc49539c32a0c76681764
  accessed_at: '2026-10-16T03:56:48.215334Z'
  support: context_only
  summary: Actual root acceptance of current source responsibility; no whole-issue
    closure.
- evidence_id: current-discovery-report
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T034316Z-amortized-svgd-and-real-time-adaptive-a-star.json
  snapshot_sha256: 5aaa5f8a608224430161ccddacc1cc2cbd7ecedba79e8cec86b52ee81ec4056d
  accessed_at: '2026-10-16T03:56:48.229848Z'
  support: context_only
  summary: Canonical durable report containing the exact recursively queryable predecessor_state
    bundle and separate current pair source responsibilities.
- evidence_id: creation-history
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/history/reports/amortized-svgd-and-real-time-adaptive-a-star/2026-10-16T034327Z-codex-1eb03c.yaml
  snapshot_sha256: 2b36a87272003ef6f707070e7584d37a8fea3e600f96c1112ca003181564d196
  accessed_at: '2026-10-16T03:56:48.230341Z'
  support: context_only
  summary: Actual single CREATE event for the report.
- evidence_id: review-support
  kind: record_content
  reference: /private/tmp/aimech-cohort359-timestamp-recovery-20261016/review-support.prepared.json
  snapshot_sha256: f094688ba4b6cab4f62f7d4f7c12c285d15ab2e5ca4f38434da6a4f7f39cdfac
  accessed_at: '2026-10-16T03:56:48.231548Z'
  support: context_only
  summary: Exact historical per-claim and per-limitation narrative support.
- evidence_id: check-gate
  kind: validation
  reference: /private/tmp/aimech-cohort359-postwrite-20261016/actual-check-gate.json
  snapshot_sha256: c2f5273e73c58adab6e2400d9b89d165032981b666f298b3c31056176ea2f76f
  accessed_at: '2026-10-16T03:53:12.650259Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-vendor
  kind: validation
  reference: /private/tmp/aimech-cohort359-postwrite-20261016/recovery-check-vendor.json
  snapshot_sha256: 752de3574244cd1c930e5fa73490951d226144f8701422380d35ff6f2acbff82
  accessed_at: '2026-10-16T03:54:03.634996Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-check-source
  kind: validation
  reference: /private/tmp/aimech-cohort359-postwrite-20261016/recovery-check-check-source.json
  snapshot_sha256: 84042c513decc49d04e631f8ae55463e1839a79cbe02beedf12477480393764a
  accessed_at: '2026-10-16T03:54:05.832051Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-render
  kind: validation
  reference: /private/tmp/aimech-cohort359-postwrite-20261016/actual-check-render.json
  snapshot_sha256: a29fc7287c340792ddebfe1db799ab6321f04d1107252f87199da61fb7846f4a
  accessed_at: '2026-10-16T03:45:42.504689Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-render-check
  kind: validation
  reference: /private/tmp/aimech-cohort359-postwrite-20261016/recovery-check-render-check.json
  snapshot_sha256: 38b7977cd0524d487cbf1a070802e735efb79435e4340eaf7655a6dcb8e55d76
  accessed_at: '2026-10-16T03:54:17.303166Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-diff
  kind: validation
  reference: /private/tmp/aimech-cohort359-postwrite-20261016/recovery-check-diff.json
  snapshot_sha256: 20fbf6a13cdfb6b923a1d0e92b72ffa11c9c9174964b91e6d9ef14b75e90c181
  accessed_at: '2026-10-16T03:54:17.543453Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: historical-failed-check-1
  kind: validation
  reference: /private/tmp/aimech-cohort359-postwrite-20261016/actual-check-vendor.json
  snapshot_sha256: a4e501695967be82619295b3c8c46171c25ec22b0af601d21d006756a39dad28
  accessed_at: '2026-10-16T03:53:13.053311Z'
  support: context_only
  summary: Retained unsuccessful earlier command attempt; successful later exact command
    is separately bound.
assessments:
- assessment_id: amortized-svgd-claim-implicit-sampler
  area: evidence
  topic: 'Amortized Stein variational gradient descent: implicit-sampler'
  outcome: supported
  summary: Problem1 explicitly permits a differentiable simulator queried through
    outputs and parameter derivatives, with sampled seeds of unknown density. Generic
    scope is retained; density-based theoretical claims have narrower regularity requirements.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - src-wang-liu2016-v2
  - src-feng-wang-liu2017
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-claim-particle-direction
  area: evidence
  topic: 'Amortized Stein variational gradient descent: particle-direction'
  outcome: supported
  summary: The empirical Stein field uses the target-score attraction term and first-argument
    kernel derivative from the same pre-update outputs. The formula uses a minibatch
    mean; no ordinary KL gradient or unbiasedness is inferred.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - src-wang-liu2016-v2
  - src-feng-wang-liu2017
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-claim-output-projection
  area: evidence
  topic: 'Amortized Stein variational gradient descent: output-projection'
  outcome: supported
  summary: Eqs.8/13 specify regression to displaced old outputs. Frozen targets and
    same seeds are necessary for the stated fitting derivative; this is source interpretation
    plus explicit mathematical convention, not a source-code audit.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - src-wang-liu2016-v2
  - src-feng-wang-liu2017
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-claim-parameter-step
  area: evidence
  topic: 'Amortized Stein variational gradient descent: parameter-step'
  outcome: supported
  summary: Differentiating the frozen-target squared loss gives negative 2*epsilon*sum
    J^T v; descent is therefore positive. Source2016 Eq.9 and both practical positive
    steps support this; source2017 Eq.14 contradicts its own delta residual. Exact
    tangent projection A A^+ v and single fitting-gradient A A^T v differ.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - src-wang-liu2016-v2
  - src-feng-wang-liu2017
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-claim-learned-output-versus-particles
  area: evidence
  topic: 'Amortized Stein variational gradient descent: learned-output-versus-particles'
  outcome: supported
  summary: Fresh-seed outputs are provided by the learned parameterized sampler. Approximation
    error remains; no invariant-chain or exact posterior claim follows.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - src-wang-liu2016-v2
  - src-feng-wang-liu2017
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-claim-application-boundaries
  area: evidence
  topic: 'Amortized Stein variational gradient descent: application-boundaries'
  outcome: supported
  summary: Application sections add model learning, VAE entropy/model structure or
    trainable Langevin schedules. The generic method does not require these components;
    five separate source questions remain pending.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - src-wang-liu2016-v2
  - src-feng-wang-liu2017
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-limitation-1
  area: evidence
  topic: 'Amortized Stein variational gradient descent: limitation 1'
  outcome: supported
  summary: 'Retained source and mathematical boundary, not an unqualified defect or
    empirical finding. No relaxation of the selected research limitation. Retained
    statement: A target score requires a differentiable continuous target on the relevant
    domain, finite positive normalization and regularity. An unknown multiplicative
    constant independent of the sampled variable cancels; arbitrary improper energies
    do not thereby become distributions.'
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - amortized-svgd-limitation-1-support
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-limitation-2
  area: evidence
  topic: 'Amortized Stein variational gradient descent: limitation 2'
  outcome: supported
  summary: 'Retained source and mathematical boundary, not an unqualified defect or
    empirical finding. No relaxation of the selected research limitation. Retained
    statement: The infinitesimal Stein/KL argument concerns suitable population densities,
    moments, boundary integration and valid perturbations. A finite empirical particle
    measure is atomic; a finite/discrete-seed simulator can also have singular output.
    The algorithm can compute directions without an output density, but that alone
    does not make its population KL finite or justify density-based entropy identities.'
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - amortized-svgd-limitation-2-support
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-limitation-3
  area: evidence
  topic: 'Amortized Stein variational gradient descent: limitation 3'
  outcome: supported
  summary: 'Retained source and mathematical boundary, not an unqualified defect or
    empirical finding. The independent audit provides smooth restricted-family stationarity
    and projected-KL counterexamples, so the restriction is not limited to rank-deficient
    Jacobians. Retained statement: Finite sampler capacity, restricted tangent directions,
    rank-deficient Jacobians, nonlinear fitting error, minibatch error and finite
    step size separate the parameter update from ideal unconstrained SVGD. A least-squares
    projection may have nonunique minimizers. Even a full-column-rank but restricted
    parameterization can have a stationary fitting update while the unrestricted Stein
    field is nonzero. No universal monotone KL descent, exact posterior recovery or
    global convergence is adopted.'
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - amortized-svgd-limitation-3-support
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-limitation-4
  area: evidence
  topic: 'Amortized Stein variational gradient descent: limitation 4'
  outcome: supported
  summary: 'Retained source and mathematical boundary, not an unqualified defect or
    empirical finding. The source-local printed sign is preserved without silently
    repairing the primary artifact. Retained statement: The 2016 v1/v2 Eq.9 has eta_new=eta+epsilon*Delta_eta.
    The 2017 proceedings and arXiv:1707.06626v2 Eq.14 print a minus sign while minimizing
    ||J*delta-phi||^2 and retaining positive Eq.15. The fitting target and first-order
    derivation support plus for this delta definition. Retain the printed discrepancy
    and use positive 2016 Eq.10/2017 Eq.15 for the practical step; no published erratum
    or inspected author implementation is claimed.'
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - amortized-svgd-limitation-4-support
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-limitation-5
  area: evidence
  topic: 'Amortized Stein variational gradient descent: limitation 5'
  outcome: supported
  summary: 'Retained source and mathematical boundary, not an unqualified defect or
    empirical finding. No relaxation of the selected research limitation. Retained
    statement: Unit diagonal and zero first-argument diagonal derivative give the
    exact one-particle score-ascent reduction, as with a normalized RBF. Other kernels
    can change the scale or add a derivative. The 2016 p4 single-particle sentence
    is visibly missing the condition value; the 2017 p3 prints derivative=0 but unit-diagonal
    scaling still matters. Kernel richness, boundary conditions and positive nondegenerate
    bandwidth matter; repulsion does not guarantee all modes or prevent coincident
    outputs.'
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - amortized-svgd-limitation-5-support
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-limitation-6
  area: evidence
  topic: 'Amortized Stein variational gradient descent: limitation 6'
  outcome: supported
  summary: 'Retained source and mathematical boundary, not an unqualified defect or
    empirical finding. No relaxation of the selected research limitation. Retained
    statement: The projected Stein field is not asserted to be the exact ordinary
    parameter gradient of KL. The paper relates it to a kernel-smoothed score difference
    under Stein conditions; this does not remove smoothing, projection or family restrictions.
    The output target is held fixed in the regression derivative, rather than differentiating
    through the target as an additional objective.'
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - amortized-svgd-limitation-6-support
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-limitation-7
  area: evidence
  topic: 'Amortized Stein variational gradient descent: limitation 7'
  outcome: supported
  summary: 'Retained source and mathematical boundary, not an unqualified defect or
    empirical finding. No relaxation of the selected research limitation. Retained
    statement: SteinGAN replaces a model expectation with imperfect sampler outputs,
    so finite alternating updates are not automatically exact or unbiased MLE. Its
    gamma-weighted stabilization changes the objective; proper prior normalization
    is not established by calling exp(gamma*logZ) conjugate. Learned finite-step Langevin
    chains are not certified target-invariant or universally transferable by the reported
    experiments. Entropy-tempering requires a normalizable tempered target and meaningful
    entropy.'
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - amortized-svgd-limitation-7-support
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-limitation-8
  area: evidence
  topic: 'Amortized Stein variational gradient descent: limitation 8'
  outcome: supported
  summary: 'Retained source and mathematical boundary, not an unqualified defect or
    empirical finding. No relaxation of the selected research limitation. Retained
    statement: 2016 v1/v2 differ in reported CIFAR values and caption gamma, not just
    typography; keep versions separate. UAI proceedings and later arXiv1707.06626v2
    differ in bibliography (Snelson removed, Pu added), and only the latter downloaded
    artifact contains Appendices A–C. Empirical comparisons, image quality and speed
    claims are source-reported and not independently reproduced. No code or training
    was run.'
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - amortized-svgd-limitation-8-support
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-sources
  area: provenance
  topic: 'Amortized Stein variational gradient descent: sources and source scope'
  outcome: supported
  summary: Two primary evidence rows/two artifacts support the definition and claims.
    The2016v1 and later2017preprint remain fully bound research/version context, not
    unused support rows added to satisfy a count.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - src-wang-liu2016-v2
  - src-feng-wang-liu2017
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-definition
  area: identity
  topic: 'Amortized Stein variational gradient descent: definition and source scope'
  outcome: supported
  summary: Direct defining-method support from both primary full texts. Neural examples
    do not narrow Problem1 generic simulator scope.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - src-wang-liu2016-v2
  - src-feng-wang-liu2017
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-identity
  area: identity
  topic: 'Amortized Stein variational gradient descent: identity and source scope'
  outcome: supported
  summary: Retain the generic differentiable-sampler fitting procedure separately
    from unamortized interacting-particle SVGD, ordinary variational objectives and
    the composite SteinGAN/VAE/Langevin applications. No universal exact-sampling
    or stationarity-implies-target claim is adopted. Actual identity notes equal the
    fresh root decisions; exact historical/current differences remain in context_changes.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - src-wang-liu2016-v2
  - src-feng-wang-liu2017
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-mapping
  area: grounding
  topic: 'Amortized Stein variational gradient descent: mapping and source scope'
  outcome: supported
  summary: Both primary works explicitly train stochastic neural inference networks
    using this sampler-fitting procedure. This relates the algorithm to a documented
    neural-sampler implementation class; the generic differentiable-simulator definition
    also permits other parameterizations. It asserts neither algorithm/model identity
    nor subclass or broad-match inclusion, and does not make an ANN architecture mandatory.
    Actual root decisions supply current mapping assessments; the accepted source-scoped
    related mappings remain exact.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - src-wang-liu2016-v2
  - src-feng-wang-liu2017
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: amortized-svgd-kind
  area: identity
  topic: 'Amortized Stein variational gradient descent: kind and source scope'
  outcome: supported
  summary: The record is a training algorithm for a parameterized stochastic sampler.
    A documented neural implementation is context; it is not a standalone trained
    model or a required neural architecture.
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  evidence_ids:
  - src-wang-liu2016-v2
  - src-feng-wang-liu2017
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-claim-bounded-local-search
  area: evidence
  topic: 'Real-Time Adaptive A*: bounded-local-search'
  outcome: supported
  summary: The positive expansion cap, selected next-to-expand node and explicit failure
    branch follow Figure1. CLOSED contains expanded states. The selected boundary
    is not an arbitrary OPEN state.
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - src-koenig-likhachev2006
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-claim-uniform-f-minus-g-learning
  area: evidence
  topic: 'Real-Time Adaptive A*: uniform-f-minus-g-learning'
  outcome: supported
  summary: Only CLOSED is updated using one F. The defining text explicitly excludes
    ordinary OPEN states because their g values can still exceed shortest-path distances.
    Hand-derived M3 retains the distinction from the later paper’s broader wording.
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - src-koenig-likhachev2006
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-claim-execution-and-retention
  area: evidence
  topic: 'Real-Time Adaptive A*: execution-and-retention'
  outcome: supported
  summary: The movement cap is independently chosen after learning; source lines13–16
    allow increasing costs after actions and interrupt the remaining path when affected.
    Retention is across search episodes, not an assumed stationary environment.
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - src-koenig-likhachev2006
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-claim-consistency-and-completion
  area: evidence
  topic: 'Real-Time Adaptive A*: consistency-and-completion'
  outcome: supported
  summary: Theorems1–3 use the complete Section3/4 assumptions. Initial-state solvability
    alone does not give uniformly bounded goal distances from all states. The finite
    potential proof is not extended to arbitrary directed dead-end or stochastic domains.
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - src-koenig-likhachev2006
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-claim-repeated-trial-scope
  area: evidence
  topic: 'Real-Time Adaptive A*: repeated-trial-scope'
  outcome: supported
  summary: Theorem4 additionally uses fixed-start resets, retained learning and a
    positive lower bound on nonzero increases. Its bounded nonoptimal-trial count
    is distinct from first-trial optimality or global exact learning.
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - src-koenig-likhachev2006
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-claim-lrta-comparison-boundary
  area: evidence
  topic: 'Real-Time Adaptive A*: lrta-comparison-boundary'
  outcome: supported
  summary: Section5 names its 2004 larger-lookahead comparator. The one-lookahead
    result requires identical ties. The subsequent one-episode comparison starts with
    identical heuristics and explicitly disclaims dominance along different trajectories.
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - src-koenig-likhachev2006
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-claim-navigation-application
  area: evidence
  topic: 'Real-Time Adaptive A*: navigation-application'
  outcome: supported
  summary: The defining study supports the navigation application and experimental
    setup. The claim does not reproduce numeric performance, absolute timing or universal
    superiority; reported domain and implementation limits remain.
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - src-koenig-likhachev2006
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-claim-later-comparator
  area: evidence
  topic: 'Real-Time Adaptive A*: later-comparator'
  outcome: supported
  summary: The 2018 paper is primary evidence for its own later comparison, not the
    defining algorithm. Expansion-bounded runs, amortized CPU time and interpolation
    are explicit; source timing-label discrepancies remain and no absolute crossover
    value is asserted.
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - src-kochvi-ruml2018
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-limitation-1
  area: evidence
  topic: 'Real-Time Adaptive A*: limitation 1'
  outcome: supported
  summary: 'M2 shows why admissibility alone does not supply the monotone update theorem.
    The paper proposes inconsistent-heuristic extensions only as future work. Retained
    statement: The defining proofs assume finite states/actions, action costs bounded
    below by positive epsilon, and initial consistency with zero goal values; mere
    admissibility is insufficient for the same no-reopening A* and monotonic-update
    proof.'
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - rtaa-limitation-1-support
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-limitation-2
  area: evidence
  topic: 'Real-Time Adaptive A*: limitation 2'
  outcome: supported
  summary: 'All-state bounded goal distances exclude reachable traps; the explicit
    failure branch is not a theorem of success from any initially solvable state.
    Retained statement: Goal reachability from only the initial state does not establish
    the source’s bounded-goal-distance assumption for all states. Reachable traps/dead
    ends are outside that completion theorem. OPEN-exhaustion failure is an explicit
    branch.'
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - rtaa-limitation-2-support
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-limitation-3
  area: evidence
  topic: 'Real-Time Adaptive A*: limitation 3'
  outcome: supported
  summary: 'M4 exhibits why arbitrary decreases can invalidate admissibility. No changing-goal
    or stochastic extension is inferred. Retained statement: Costs may increase; arbitrary
    decreases, changing goals, stochastic transitions and moving-goal extensions are
    not covered by the defining theorem.'
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - rtaa-limitation-3-support
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-limitation-4
  area: evidence
  topic: 'Real-Time Adaptive A*: limitation 4'
  outcome: supported
  summary: 'Expansion counts and a linear-sized assignment loop do not bound queue
    operations, successor generation, learned-heuristic storage or worst-case elapsed
    time. Retained statement: The lookahead cap bounds expansions, and the update
    takes one assignment per expanded state; it is not an unconditional wall-clock
    or total-memory guarantee. Successor generation, queue operations and accumulated
    learned h have implementation costs.'
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - rtaa-limitation-4-support
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-limitation-5
  area: evidence
  topic: 'Real-Time Adaptive A*: limitation 5'
  outcome: supported
  summary: 'The repeated-trial hypotheses are retained separately from exploratory
    first execution. Retained statement: Exploratory trajectories may be suboptimal
    and repeated. Theorem4 is conditional on fixed-start repeated trials and lower-bounded
    nonzero cost increases; it does not guarantee optimal first execution.'
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - rtaa-limitation-5-support
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-limitation-6
  area: evidence
  topic: 'Real-Time Adaptive A*: limitation 6'
  outcome: supported
  summary: 'The 2004 comparator, original one-state method and Adaptive A* remain
    distinct version/source questions; equality in a special case is not general identity.
    Retained statement: The 2006 paper calls a 2004 larger-lookahead LRTA variant
    LRTA*, not exclusively Korf’s original one-state method. Its equivalence result
    is lookahead one with identical ties; Adaptive A* complete-search and later RTAA
    variants are separate source/version questions.'
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - rtaa-limitation-6-support
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-limitation-7
  area: evidence
  topic: 'Real-Time Adaptive A*: limitation 7'
  outcome: supported
  summary: 'Reported relative performance remains confined to its domains, heuristics
    and implementations. No algorithm/benchmark execution occurred. Retained statement:
    Reported relative advantages depend on domain, heuristic, lookahead, movement
    choice, tie handling, hardware and implementation. No universal superiority, monotonic
    lookahead benefit or reproduced benchmark is asserted.'
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - rtaa-limitation-7-support
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-limitation-8
  area: evidence
  topic: 'Real-Time Adaptive A*: limitation 8'
  outcome: supported
  summary: 'The corrected literal center-axis label and unresolved aggregation are
    retained. Figure1 right caption versus time-axis wording is additionally preserved
    in source discrepancy context. No absolute timing or plotted-data correction is
    inferred. Retained statement: 2018 PDF2 prose says microseconds and 77.22us crossover,
    while visible plot axes on PDF3–5 say ms. The Figure1 center axis reads planning
    time (ms), without the per-episode qualifier used in nearby prose; actual aggregation
    remains unresolved. Preserve these inconsistencies and avoid absolute timing/crossover
    claims until clarified.'
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - rtaa-limitation-8-support
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-limitation-9
  area: evidence
  topic: 'Real-Time Adaptive A*: limitation 9'
  outcome: supported
  summary: 'The 2018 traffic reset convention is an empirical protocol, not a repair
    of arbitrary directed dead-end completeness. Retained statement: The 2018 Traffic
    benchmark resets an agent with no successors to the start and reports collisions/restarts;
    this experiment does not extend the 2006 completion theorem to arbitrary directed
    dead-end graphs.'
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - rtaa-limitation-9-support
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-limitation-10
  area: evidence
  topic: 'Real-Time Adaptive A*: limitation 10'
  outcome: supported
  summary: 'The unread thesis, implementation-comparison gap and failed publisher-PDF
    access remain scoped limitations; the author-hosted manuscript supplies inspected
    evidence. Retained statement: The 2018 authors did not compare original implementation
    code and defer statistical-anomaly details to an unread 2017 thesis. Neither claim
    is independently reproduced here. Publisher PDF access failed; author manuscript
    supplies the inspected evidence.'
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - rtaa-limitation-10-support
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-sources
  area: provenance
  topic: 'Real-Time Adaptive A*: sources and source scope'
  outcome: supported
  summary: 'Two primary evidence rows/two artifacts with distinct roles: 2006 defining
    method; 2018 later original empirical comparison. Two unread retrieval routes
    remain source questions, not support rows.'
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - src-koenig-likhachev2006
  - src-kochvi-ruml2018
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-definition
  area: identity
  topic: 'Real-Time Adaptive A*: definition and source scope'
  outcome: supported
  summary: The defining 2006 algorithm and pseudocode directly support the complete
    controller. The later empirical paper is used in its own claim rather than added
    as unused definition evidence.
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - src-koenig-likhachev2006
  - src-kochvi-ruml2018
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-identity
  area: identity
  topic: 'Real-Time Adaptive A*: identity and source scope'
  outcome: supported
  summary: Retain the bounded forward-search, CLOSED-only F−g learning and capped-execution
    controller separately from ordinary A*, one-state LRTA, RTA second-best backup
    and LSS reverse-Dijkstra propagation. Special-case equality with identical ties
    does not establish general algorithm identity. Actual identity notes equal the
    fresh root decisions; exact historical/current differences remain in context_changes.
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - src-koenig-likhachev2006
  - src-kochvi-ruml2018
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-mapping
  area: grounding
  topic: 'Real-Time Adaptive A*: mapping and source scope'
  outcome: supported
  summary: Persistent state-heuristic learning from repeated search experience supplies
    a weak relation to the pinned task context. The bounded forward-search, CLOSED-only
    F−g update and movement controller are not identical to a general task class.
    This proposal asserts neither exact equivalence nor subclass inclusion and does
    not identify the algorithm with a sampled reinforcement-learning method. Actual
    root decisions supply current mapping assessments; the accepted source-scoped
    related mappings remain exact.
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - src-koenig-likhachev2006
  - src-kochvi-ruml2018
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: rtaa-kind
  area: identity
  topic: 'Real-Time Adaptive A*: kind and source scope'
  outcome: supported
  summary: The record is a real-time heuristic search algorithm with persistent learned
    state heuristics. Its specific planning/update/execution controller is not identical
    to a general machine-learning task or a sampled reinforcement-learning method.
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - src-koenig-likhachev2006
  - src-kochvi-ruml2018
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: actual-canonical-correspondence
  area: provenance
  topic: Actual canonical creation and separate source responsibilities
  outcome: supported
  summary: 'Actual records retain14 claims and18 limitations, four source rows and
    four distinct artifacts: three defining method artifacts and one2018 later comparison.
    Five exclusive creation outputs and one CREATE event are bound. Current dynamic
    owner changes and additions exactly follow the accepted plan: {"additional_source_question_count":
    0, "bibliography_occurrences": 125, "changed_main_indexes": [8, 909], "changed_nested_indexes":
    [393], "main": 914, "nested": 394, "new_main_rows": 0, "new_nested_rows": 0}.
    Separate responsibility for125 bibliography occurrences and19 original/dossier/retrieval
    objects, plus additional current questions, is retained. The complete actual358
    predecessor bundle preserves402/404/406,356 local questions,357 Ritter responsibilities
    and358 memory-search questions with original provenance. 66 unique captured inputs,
    actual generated pages and six successful required checks are bound. No source
    exhaustion, independent approval, issue closure or publication result is implied.'
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  - AIMech:RealTimeAdaptiveAStar
  evidence_ids:
  - actual-write
  - captured-inputs
  - postcapture-reading
  - governance-assessment
  - rendered-pages
  - actual-scientific-assessment
  - creation-history
  - current-discovery-report
  - root-decisions
  - ownership-plan
  - ownership-plan-acceptance
  - check-gate
  - check-vendor
  - check-check-source
  - check-render
  - check-render-check
  - check-diff
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:AmortizedSteinVariationalGradientDescent
  rationale: Retain the generic differentiable-sampler fitting procedure separately
    from unamortized interacting-particle SVGD, ordinary variational objectives and
    the composite SteinGAN/VAE/Langevin applications. No universal exact-sampling
    or stationarity-implies-target claim is adopted. Source residuals remain separately
    retained; no family exhaustion is inferred.
  evidence_ids:
  - src-wang-liu2016-v2
  - src-feng-wang-liu2017
  - amortized-svgd-accepted-preview
  - amortized-svgd-prior-support
  - amortized-svgd-reading
  - actual-write
  - root-decisions
  - postcapture-reading
- action: retain
  target_ids:
  - AIMech:RealTimeAdaptiveAStar
  rationale: Retain the bounded forward-search, CLOSED-only F−g learning and capped-execution
    controller separately from ordinary A*, one-state LRTA, RTA second-best backup
    and LSS reverse-Dijkstra propagation. Special-case equality with identical ties
    does not establish general algorithm identity. Source residuals remain separately
    retained; no family exhaustion is inferred.
  evidence_ids:
  - src-koenig-likhachev2006
  - src-kochvi-ruml2018
  - rtaa-accepted-preview
  - rtaa-prior-support
  - rtaa-reading
  - actual-write
  - root-decisions
  - postcapture-reading
targets:
- target_id: AIMech:AmortizedSteinVariationalGradientDescent
  label: Amortized Stein variational gradient descent
  path: data/curated/AmortizedSteinVariationalGradientDescent.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AmortizedSteinVariationalGradientDescent.yaml
    role: maintained native concept record
- target_id: AIMech:RealTimeAdaptiveAStar
  label: Real-Time Adaptive A*
  path: data/curated/RealTimeAdaptiveAStar.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RealTimeAdaptiveAStar.yaml
    role: maintained native concept record
limitations:
- Scientific correspondence uses exact accepted native-preview content and attributed
  primary-source, mathematical and source-accounting reading. This preparation does
  not claim a fresh full-paper reading or a new native validation.
- The amortized sampler remains generic and differentiable; its neural implementation
  relation is not a mandatory ANN architecture. Projection, finite-step, output-density
  and source-local sign limitations remain exact.
- RTAA retains CLOSED-only F−g, the selected frontier and movement controller, finite
  positive-cost/consistency assumptions and the separate2018 comparison/timing limitations.
- 125 bibliography occurrences plus19 original/dossier/retrieval objects remain separate
  source questions. Captured citation counts are not counts of new concepts; five
  sampler dossier followups are not presumed historically909-owned.
- Four declared artifacts include three defining method sources and one later comparison.
  Other version artifacts remain attributed research context rather than extra claim-support
  rows.
- Two related AIO mappings and historical14 AIO/21 native contexts retain their original
  scoped readings; capture is not renewed semantic clearance.
- Actual five creation outputs, one CREATE history, 66 capture inputs and 8 parsed
  generated pages are bound. Six required commands passed; earlier failed attempts
  remain explicit. Canonical review save/check and publication are subsequent operations.
tags:
- scientific-review
- self-review
- source-scoped
- sampling
- heuristic-search
notes:
- Supported outcomes here assess correspondence to already accepted source-scoped
  preview content. They do not certify future canonical records or source ownership.
- The source-local2017 Eq.14 minus discrepancy remains a limitation; the practical
  positive-gradient claim has its accepted supporting Eqs.13/15 evidence and no broadened
  claim-level contradiction.
- The2018 RTAA Figure1 center-axis literal is planning time (ms); aggregation and
  caption/axis discrepancies remain unresolved.
- The first formal-review validation failed on historical evidence timestamps serialized
  with +00:00. This successor preserves the same UTC instants using required Z syntax;
  the exact failure log is retained as evidence. No canonical review was saved by
  that failed attempt, and no scientific record or source claim changed.
- Two distinct source groups retain 125 bibliography occurrences and independent pending
  questions; these counts do not assert new concepts.
- '{"added_record_ids": [], "assessment": "Andrychowicz et al. 2016 concerns learning
  an optimizer; sharing gradient-based training does not make it the generic Stein
  sampler.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "amortized-svgd", "index": 0, "kind": "bibliography", "next_check": "Inspect the
  exact learned-optimizer original and compare optimizer state, training distribution
  and objective before identity or ownership decisions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "fa671d0914ecafde33a656ec8065614a1539159b80f68f323749311272f494d8", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/0", "responsible_owner": {"family": "main", "index": 909}, "text": "Andrychowicz,
  Marcin, Denil, Misha, Gomez, Sergio, Hoffman, Matthew W, Pfau, David, Schaul, Tom,
  and\nde Freitas, Nando. Learning to learn by gradient descent by gradient descent.
  arXiv preprint arXiv:1606.04474,\n2016."}'
- '{"added_record_ids": [], "assessment": "Barbour and Chen is a Stein-method introduction,
  retained as mathematical source context rather than an asserted new AI algorithm.",
  "disposition": "retained_context", "existing_record_ids": [], "group": "amortized-svgd",
  "index": 1, "kind": "bibliography", "next_check": "Use the exact chapter/version
  if a later claim needs a Stein identity or regularity assumption.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "c721ddecd7c1666b42cbd8946f5728a6f6a1771352e5dc487f37ace1ae3d969c", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/1", "responsible_owner": {"family": "main", "index": 909}, "text": "Barbour,
  Andrew D and Chen, Louis Hsiao Yun. An introduction to Stein’s method, volume 4.
  World Scientiﬁc,\n2005."}'
- '{"added_record_ids": [], "assessment": "Briol et al. concerns probabilistic integration;
  integration and finite-particle sampler fitting are separate responsibilities.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd",
  "index": 2, "kind": "bibliography", "next_check": "Inspect the cited integration
  construction and its relation to control functionals and Bayesian quadrature.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "0f0636e24b5e4deef177376655d31d6ddd87a3936807f8a7ee39d7445ef36204", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/2", "responsible_owner": {"family": "main", "index": 909}, "text": "Briol,
  Franc¸ois-Xavier, Oates, Chris, Girolami, Mark, Osborne, Michael A, Sejdinovic,
  Dino, et al. Probabilistic\nintegration: A role for statisticians in numerical analysis?
  arXiv preprint http://arxiv.org/abs/1512.00933,\n2015."}'
- '{"added_record_ids": [], "assessment": "Chwialkowski et al. kernel goodness-of-fit
  testing belongs to the existing pending Stein-test source question; it is not direct
  amortized-KSD training.", "disposition": "existing_pending_owner", "existing_record_ids":
  ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index":
  3, "kind": "bibliography", "next_check": "Read the exact test original and distinguish
  its statistic and assumptions from Liu–Lee–Jordan and the sampler appendix.", "origin":
  {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "65f8207f69e775588c8065d86e2b2b6f3d8f7556c2ad8fda39f9696f89488e18", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/3", "responsible_owner": {"family": "main", "index": 909}, "text": "Chwialkowski,
  Kacper, Strathmann, Heiko, and Gretton, Arthur. A kernel test of goodness of ﬁt.
  In Proceedings\nof the International Conference on Machine Learning (ICML), 2016."}'
- '{"added_record_ids": [], "assessment": "Daniel et al. learned step-size controllers
  are a specific optimizer-controller source, not automatically the Langevin-schedule
  application.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "amortized-svgd", "index": 4, "kind": "bibliography", "next_check": "Inspect the
  controller inputs/objective and compare the application-specific learned Langevin
  schedule.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "82fa125fccdd77f78b126dc6ebe973abbe2a6fd49f727044bda8096dfb915c29", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/4", "responsible_owner": {"family": "main", "index": 909}, "text": "Daniel,
  Christian, Taylor, Jonathan, and Nowozin, Sebastian. Learning step size controllers
  for robust neural\nnetwork training. In Thirtieth AAAI Conference on Artiﬁcial Intelligence,
  2016."}'
- '{"added_record_ids": [], "assessment": "Delyon and Portier concern integral approximation
  using kernel smoothing; no sampler-training equivalence follows from the kernel
  vocabulary.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "amortized-svgd", "index": 5, "kind": "bibliography", "next_check": "Read the original
  approximation method and retain its integration-estimator scope.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "fcb7680faf45ab61213b7473a5aa571dee8078b21758328f06a04e01ecc021cc", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/5", "responsible_owner": {"family": "main", "index": 909}, "text": "Delyon,
  Bernard and Portier, Franc¸ois.\nIntegral approximation by kernel smoothing.\narXiv
  preprint\narXiv:1409.0733, 2014."}'
- '{"added_record_ids": [], "assessment": "Dziugaite et al. train generative networks
  by maximum mean discrepancy; this is distinct source scope from Stein output displacements.",
  "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"],
  "group": "amortized-svgd", "index": 6, "kind": "bibliography", "next_check": "Inspect
  the original MMD objective, estimator and its relation to the separately cited GMMN
  work.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "0d9f60b5b98931641727af0f6585e0b9c73f5fe934636bfcae60910942d3d3e6", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/6", "responsible_owner": {"family": "main", "index": 909}, "text": "Dziugaite,
  Gintare Karolina, Roy, Daniel M., and Ghahramani, Zoubin. Training generative neural
  networks\nvia maximum mean discrepancy optimization. In Conference on Uncertainty
  in Artiﬁcial Intelligence (UAI),\n2015."}'
- '{"added_record_ids": [], "assessment": "Gershman and Goodman 2014 is amortized
  probabilistic reasoning, not the 2012 nonparametric-VI question already retained
  under owner909.", "disposition": "pending_inspection", "existing_record_ids": [],
  "group": "amortized-svgd", "index": 7, "kind": "bibliography", "next_check": "Inspect
  the 2014 original separately; retain the exact 2012 pointer and do not substitute
  one for the other.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "e1953ec8a0bdf73a523eb4d83f9fd0d01c3f14096f0836ed03a67ebf2a676ab4", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/7", "responsible_owner": {"family": "main", "index": 909}, "text": "Gershman,
  Samuel J and Goodman, Noah D. Amortized inference in probabilistic reasoning. In
  Proceedings of\nthe 36th Annual Conference of the Cognitive Science Society, 2014."}'
- '{"added_record_ids": [], "assessment": "Geyer concerns MCMC maximum-likelihood
  calculations; the SteinGAN composite does not discharge this original-source question.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd",
  "index": 8, "kind": "bibliography", "next_check": "Inspect the MCMC likelihood estimator
  and conditions before comparing the approximate model expectation in amortized MLE.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "f5dc1b4db754e2d010f607d94aea45c2f4405a9ab8bc7ec79adab62edd045fc3", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/8", "responsible_owner": {"family": "main", "index": 909}, "text": "Geyer,
  Charles J. Markov chain Monte Carlo maximum likelihood. In Computing Science and
  Statistics: Proc.\n23rd Symp. Interface, pp. 156–163, 1991."}'
- '{"added_record_ids": [], "assessment": "The maintained GAN class supplies generative/adversarial
  context for Goodfellow et al.; it is not the generic differentiable Stein sampler.",
  "disposition": "existing_record_context", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"],
  "group": "amortized-svgd", "index": 9, "kind": "bibliography", "next_check": "Retain
  original GAN objective/version scope and inspect any claim beyond the current class
  context.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "d8adbe74dc5df8e1c23b976b6fc48a92e1fa7f5ed7df753dcead190d3dfcfe40", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/9", "responsible_owner": {"family": "main", "index": 909}, "text": "Goodfellow,
  Ian, Pouget-Abadie, Jean, Mirza, Mehdi, Xu, Bing, Warde-Farley, David, Ozair, Sherjil,
  Courville,\nAaron, and Bengio, Yoshua. Generative adversarial nets. In Advances
  in Neural Information Processing\nSystems, pp. 2672–2680, 2014."}'
- '{"added_record_ids": [], "assessment": "Gorham and Mackey Stein sample-quality
  assessment is related to the pending discrepancy family, but is not automatically
  the same kernel test as Chwialkowski or Liu.", "disposition": "existing_pending_owner",
  "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd",
  "index": 10, "kind": "bibliography", "next_check": "Inspect its exact discrepancy/test
  construction and preserve separate source identities.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "fe08416d6cd6da10ca9226a02bdcd4e680a77b54d6cbabd8b0c7852e89500479", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/10", "responsible_owner": {"family": "main", "index": 909}, "text": "Gorham,
  Jack and Mackey, Lester. Measuring sample quality with Stein’s method. In Advances
  in Neural\nInformation Processing Systems (NIPS), pp. 226–234, 2015."}'
- '{"added_record_ids": [], "assessment": "Henmi et al. importance sampling with estimated
  samplers is an estimator source; BBVI or amortization terminology does not establish
  identity.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "amortized-svgd", "index": 11, "kind": "bibliography", "next_check": "Read the original
  weighting/estimation construction and assumptions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "aed321e20e42d2bd99585d8236e83674b7573125988f66fba91135107c38dc43", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/11", "responsible_owner": {"family": "main", "index": 909}, "text": "Henmi,
  Masayuki, Yoshida, Ryo, and Eguchi, Shinto. Importance sampling via the estimated
  sampler. Biometrika,\n94(4):985–991, 2007."}'
- '{"added_record_ids": [], "assessment": "The exact Hinton 2002 source is present
  in maintained ContrastiveDivergence and ProductOfExperts contexts. Those scopes
  do not make generic Stein fitting the same algorithm.", "disposition": "existing_record_context",
  "existing_record_ids": ["AIMech:ContrastiveDivergence", "AIMech:ProductOfExperts"],
  "group": "amortized-svgd", "index": 12, "kind": "bibliography", "next_check": "Retain
  the cited version and distinguish the CD approximation and energy-model composite;
  no fresh full-paper completion is claimed.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "a029eb15467135d37bbbab7f449f04ff6ce14f145dd897e468069c92113c1d60", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/12", "responsible_owner": {"family": "main", "index": 909}, "text": "Hinton,
  Geoffrey E. Training products of experts by minimizing contrastive divergence. Neural
  computation, 14\n(8):1771–1800, 2002."}'
- '{"added_record_ids": [], "assessment": "Kim and Bengio concern a directed generative/energy-model
  composite; it requires its own original-method comparison.", "disposition": "pending_inspection",
  "existing_record_ids": ["AIO:GenerativeAdversarialNetwork", "AIMech:ProductOfExperts"],
  "group": "amortized-svgd", "index": 13, "kind": "bibliography", "next_check": "Inspect
  the model, learning objective and sampler interaction before any separate-record
  decision.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "dd492e1f05ff96a2db02417748d904b3d6aefe9c304c54e9b2c66bbd5b963b02", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/13", "responsible_owner": {"family": "main", "index": 909}, "text": "Kim,
  Taesup and Bengio, Yoshua. Deep directed generative models with energy-based probability
  estimation.\narXiv preprint arXiv:1606.03439, 2016."}'
- '{"added_record_ids": [], "assessment": "Adam is an existing maintained optimizer.
  Its use by the cited work is component context, not a sampler identity.", "disposition":
  "existing_record_context", "existing_record_ids": ["AIMech:Adam"], "group": "amortized-svgd",
  "index": 14, "kind": "bibliography", "next_check": "Reconcile the cited unversioned
  2014 arXiv entry with the exact maintained Adam source version if version-specific
  claims are needed.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "f59517604f6eb3610c8bcaade09ca793bdd0212dda5fee45ee1de43960c7c20d", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/14", "responsible_owner": {"family": "main", "index": 909}, "text": "Kingma,
  Diederik and Ba, Jimmy. Adam: A method for stochastic optimization. arXiv preprint
  arXiv:1412.6980,\n2014."}'
- '{"added_record_ids": [], "assessment": "The maintained VAE class supplies model
  context for auto-encoding variational Bayes; the estimator/training source has narrower
  details than the class.", "disposition": "existing_record_context", "existing_record_ids":
  ["AIO:VariationalAutoEncoder"], "group": "amortized-svgd", "index": 15, "kind":
  "bibliography", "next_check": "Retain the exact AEVB version and inspect any pathwise-estimator
  or application claim separately.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "dbf4fe30857a4800f8e4fe6148993cfe5416ec733135a9eaa49093fec5417481", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/15", "responsible_owner": {"family": "main", "index": 909}, "text": "Kingma,
  Diederik P and Welling, Max. Auto-encoding variational Bayes. In Proceedings of
  the International\nConference on Learning Representations (ICLR), 2013."}'
- '{"added_record_ids": [], "assessment": "Li and Malik learning to optimize is an
  optimizer-learning original, distinct from generic amortized inference.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index":
  16, "kind": "bibliography", "next_check": "Inspect the optimizer parameterization,
  objective and training task.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "62d9217a2c27dbf1604fa36e440a2047522f7b3aca07e94069795e2434c32171", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/16", "responsible_owner": {"family": "main", "index": 909}, "text": "Li,
  Ke and Malik, Jitendra. Learning to optimize. arXiv preprint arXiv:1606.01885, 2016."}'
- '{"added_record_ids": [], "assessment": "Li, Swersky and Zemel GMMN is an MMD generative-training
  source, not an interchangeable citation for Dziugaite et al. or Stein fitting.",
  "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"],
  "group": "amortized-svgd", "index": 17, "kind": "bibliography", "next_check": "Read
  the exact GMMN original and reconcile the separate MMD-training sources.", "origin":
  {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "f211820994976560c8245bcdd778237f36b18f5869a88cee0f073edbd8a29ee9", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/17", "responsible_owner": {"family": "main", "index": 909}, "text": "Li,
  Yujia, Swersky, Kevin, and Zemel, Rich. Generative moment matching networks. In
  Proceedings of the\nInternational Conference on Machine Learning (ICML), 2015."}'
- '{"added_record_ids": [], "assessment": "Liu and Lee black-box importance sampling
  concerns importance weighting; maintained BBVI has a different estimator/objective.",
  "disposition": "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference",
  "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 18,
  "kind": "bibliography", "next_check": "Inspect the exact importance-weight construction
  and distinguish it from BBVI and particle transport.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "36468fdf29d602123b670459c1b3b952308bfa28708b00bcf4ad3a3c3d3c0e07", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/18", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu,
  Qiang and Lee, Jason D. Black-box importance sampling. https://arxiv.org/abs/1610.05247,
  2016."}'
- '{"added_record_ids": [], "assessment": "The maintained SVGD record represents direct
  interacting-particle transport. The proposed record fits shared sampler parameters
  to Stein-displaced outputs.", "disposition": "existing_record_context", "existing_record_ids":
  ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index":
  19, "kind": "bibliography", "next_check": "Retain the arXiv-versus-official-proceedings
  version distinction; do not turn component use into an alias.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "000a9bbe6d1361b7360f59484886f5c6243406fbad390343e1c1961b076c2e3e", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/19", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu,
  Qiang and Wang, Dilin. Stein variational gradient descent: A general purpose bayesian
  inference algorithm.\narXiv preprint arXiv:1608.04471, 2016."}'
- '{"added_record_ids": [], "assessment": "Liu–Lee–Jordan KSD goodness-of-fit testing
  is explicitly retained under the existing owner909 Stein-test question.", "disposition":
  "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"],
  "group": "amortized-svgd", "index": 20, "kind": "bibliography", "next_check": "Read
  the exact test original, distinguish it from Chwialkowski/Gorham and direct KSD
  minimization.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "5d050ab3f42c985007bdccef102ed82f202f31a1cc1f10cd567fded79913cc63", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/20", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu,
  Qiang, Lee, Jason D, and Jordan, Michael I. A kernelized Stein discrepancy for goodness-of-ﬁt
  tests. In\nProceedings of the International Conference on Machine Learning (ICML),
  2016."}'
- '{"added_record_ids": [], "assessment": "Deep Learning Face Attributes is retained
  for the cited face-data/benchmark context, not automatically an algorithm candidate.",
  "disposition": "retained_context", "existing_record_ids": [], "group": "amortized-svgd",
  "index": 21, "kind": "bibliography", "next_check": "Inspect the dataset/annotation
  and evaluation protocol if later claims use this source.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "29dbd3a02da0b471b03c5da83a8e7a47ff21cc64d6213da66199564b9d2de970", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/21", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu,
  Ziwei, Luo, Ping, Wang, Xiaogang, and Tang, Xiaoou. Deep learning face attributes
  in the wild. In\nProceedings of International Conference on Computer Vision (ICCV),
  2015."}'
- '{"added_record_ids": [], "assessment": "Ngiam et al. deep energy models require
  a model/training-specific comparison; PoE and CD are related maintained contexts
  only.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:ProductOfExperts",
  "AIMech:ContrastiveDivergence"], "group": "amortized-svgd", "index": 22, "kind":
  "bibliography", "next_check": "Read the original energy model and training procedure
  before taxonomy decisions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "912b09f4960e31fb8605aca62d8b4a498a4087a966d4f24beed6838376886368", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/22", "responsible_owner": {"family": "main", "index": 909}, "text": "Ngiam,
  Jiquan, Chen, Zhenghao, Koh, Pang W, and Ng, Andrew Y. Learning deep energy models.
  In Proceedings\nof the International Conference on Machine Learning (ICML), pp.
  1105–1112, 2011."}'
- '{"added_record_ids": [], "assessment": "f-GAN has a divergence-specific training
  objective; the broad GAN class does not resolve the exact procedure.", "disposition":
  "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"],
  "group": "amortized-svgd", "index": 23, "kind": "bibliography", "next_check": "Inspect
  the variational divergence formulation and relation to the SteinGAN objective.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "8462df53077f30e188041f665aa77633f39ae49044d0b927d6ee4ef8c17671e5", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/23", "responsible_owner": {"family": "main", "index": 909}, "text": "Nowozin,
  Sebastian, Cseke, Botond, and Tomioka, Ryota. f-gan: Training generative neural
  samplers using\nvariational divergence minimization. arXiv preprint arXiv:1606.00709,
  2016."}'
- '{"added_record_ids": [], "assessment": "Oates et al. control functionals remain
  a distinct integration source. This 2014 occurrence is preserved separately from
  the later 2017 citation.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "amortized-svgd", "index": 24, "kind": "bibliography", "next_check":
  "Resolve the cited versions and exact variance-reduction construction before merging
  source responsibilities.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "5cb6f6961e6d5fca34f13020a9b5b4091d2b21652cc8c8feb6d18ce2d4e17fac", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/24", "responsible_owner": {"family": "main", "index": 909}, "text": "Oates,
  Chris J, Girolami, Mark, and Chopin, Nicolas. Control functionals for Monte Carlo
  integration. Journal\nof the Royal Statistical Society, Series B, 2014."}'
- '{"added_record_ids": [], "assessment": "O’Hagan’s Monte Carlo critique is retained
  as methodology context, not an asserted standalone new AI method.", "disposition":
  "retained_context", "existing_record_ids": [], "group": "amortized-svgd", "index":
  25, "kind": "bibliography", "next_check": "Inspect the exact argument if used to
  support quadrature or Monte Carlo claims.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "8339b404c435c11db59da276d0a657481102d3f9c129ef3f3f392f25145950c8", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/25", "responsible_owner": {"family": "main", "index": 909}, "text": "O’Hagan,
  Anthony. Monte Carlo is fundamentally unsound. Journal of the Royal Statistical
  Society. Series D\n(The Statistician), 36(2/3):247–249, 1987."}'
- '{"added_record_ids": [], "assessment": "Bayes–Hermite quadrature is a numerical-integration
  source, distinct from generic sampler fitting.", "disposition": "pending_inspection",
  "existing_record_ids": [], "group": "amortized-svgd", "index": 26, "kind": "bibliography",
  "next_check": "Inspect the quadrature prior, estimator and applicability assumptions.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "b5e765906391dc8dc38dd37bb957d7315a1e011745ce975503b0721e76b45877", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/26", "responsible_owner": {"family": "main", "index": 909}, "text": "O’Hagan,
  Anthony. Bayes–hermite quadrature. Journal of statistical planning and inference,
  29(3):245–260,\n1991."}'
- '{"added_record_ids": [], "assessment": "Paige and Wood inference networks for SMC
  in graphical models have a proposal/inference procedure requiring separate analysis.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd",
  "index": 27, "kind": "bibliography", "next_check": "Inspect the original SMC proposal
  training and relation to generic amortization.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "5ab7abeb6949b19eeb2db01c4b7c6f5a97f92c594a2e967bbe6bf8d96c6d394a", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/27", "responsible_owner": {"family": "main", "index": 909}, "text": "Paige,
  Brooks and Wood, Frank. Inference networks for sequential monte carlo in graphical
  models. arXiv\npreprint arXiv:1602.06701, 2016."}'
- '{"added_record_ids": [], "assessment": "The DCGAN citation concerns architecture/training
  specifics not represented merely by the broad GAN class.", "disposition": "pending_inspection",
  "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd",
  "index": 28, "kind": "bibliography", "next_check": "Read the original convolutional
  architecture and training prescription before deciding method or model scope.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "d558b100be224aba1a1d93107ab511d5e704da4c2092654e2ae8751989ee443e", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/28", "responsible_owner": {"family": "main", "index": 909}, "text": "Radford,
  Alec, Metz, Luke, and Chintala, Soumith. Unsupervised representation learning with
  deep convolutional\ngenerative adversarial networks. arXiv preprint arXiv:1511.06434,
  2015."}'
- '{"added_record_ids": [], "assessment": "Operator variational inference is an operator/objective
  source; neither BBVI nor amortized SVGD is an automatic alias.", "disposition":
  "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference",
  "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 29,
  "kind": "bibliography", "next_check": "Inspect its original operator family, test
  function and objective.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "4a1c40996bc4b22c9425edb69cf1d0d286215509c5773d1ccd647ec52715f39a", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/29", "responsible_owner": {"family": "main", "index": 909}, "text": "Ranganath,
  R., Altosaar, J., Tran, D., and Blei, D.M. Operator variational inference. 2016."}'
- '{"added_record_ids": [], "assessment": "Ranganath–Gerrish–Blei BBVI is an existing
  maintained record and an exact source context under main308; its retained hierarchical/subsampling
  questions remain separate.", "disposition": "existing_record_context", "existing_record_ids":
  ["AIMech:BlackBoxVariationalInference"], "group": "amortized-svgd", "index": 30,
  "kind": "bibliography", "next_check": "Keep owner308’s residual source scope and
  inspect any unsupported weighting extension separately.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "15edab4a0a467ab96899161fd9209065be1c8e7ae37a61a989b92bf9c1c7e4d6", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/30", "responsible_owner": {"family": "main", "index": 308}, "text": "Ranganath,
  Rajesh, Gerrish, Sean, and Blei, David M. Black box variational inference. In Proceedings
  of the\nInternational Conference on Artiﬁcial Intelligence and Statistics (AISTATS),
  2014."}'
- '{"added_record_ids": [], "assessment": "Hierarchical variational inference concerns
  a specific variational-family construction, not generic variational EM or BBVI by
  name.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference"],
  "group": "amortized-svgd", "index": 31, "kind": "bibliography", "next_check": "Read
  the original hierarchical family and estimator before owner/identity decisions.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "672ce438fbda15c56336e4e7eac54f02b7c5175ec4efd9b4c5d9ee60617e8ef6", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/31", "responsible_owner": {"family": "main", "index": 909}, "text": "Ranganath,
  Rajesh, Tran, Dustin, and Blei, David M.\nHierarchical variational models.\narXiv
  preprint\narXiv:1511.02386, 2015."}'
- '{"added_record_ids": [], "assessment": "Rezende–Mohamed normalizing-flow VI is
  the existing owner909 bibliography question, cross-linked to H355-FLOW-17. FlowMatching/RectifiedFlow
  are related contexts, not resolutions.", "disposition": "existing_pending_owner",
  "existing_record_ids": ["AIMech:FlowMatching", "AIMech:RectifiedFlow"], "group":
  "amortized-svgd", "index": 32, "kind": "bibliography", "next_check": "Inspect the
  exact original flow transformations/objective and retain separate CNF/probability-flow
  family scope in issue406.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "a4bdc09c44052f83b01862e9127f75e17f47009edc87f4eda84625190f71d744", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/32", "responsible_owner": {"family": "main", "index": 909}, "text": "Rezende,
  Danilo Jimenez and Mohamed, Shakir. Variational inference with normalizing ﬂows.
  In Proceedings\nof the International Conference on Machine Learning (ICML), 2015a."}'
- '{"added_record_ids": [], "assessment": "This separate arXiv occurrence of Rezende–Mohamed
  normalizing-flow VI retains its version identity and the existing owner909/H355-FLOW-17
  cross-link.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:FlowMatching",
  "AIMech:RectifiedFlow"], "group": "amortized-svgd", "index": 33, "kind": "bibliography",
  "next_check": "Resolve the exact arXiv/proceedings versions without dropping either
  occurrence or closing the wider flow-family question.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "2b5754efae97b58b5bba75518739d6a40ca9e948d9488ec100e0f217ad9be1bb", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/33", "responsible_owner": {"family": "main", "index": 909}, "text": "Rezende,
  Danilo Jimenez and Mohamed, Shakir. Variational inference with normalizing ﬂows.
  arXiv preprint\narXiv:1505.05770, 2015b."}'
- '{"added_record_ids": [], "assessment": "Improved GAN training is a specific collection
  of training procedures, not discharged by the broad GAN class or a Stein sampler.",
  "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"],
  "group": "amortized-svgd", "index": 34, "kind": "bibliography", "next_check": "Inspect
  the individual procedures and decide source/method granularity.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "5e424d1382fe5f5bacdcd647c4db6fe88b024761d4ff6190504fa8b44cbf2216", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/34", "responsible_owner": {"family": "main", "index": 909}, "text": "Salimans,
  Tim, Goodfellow, Ian, Zaremba, Wojciech, Cheung, Vicki, Radford, Alec, and Chen,
  Xi. Improved\ntechniques for training gans. arXiv preprint arXiv:1606.03498, 2016."}'
- '{"added_record_ids": [], "assessment": "Stein 1972 is retained mathematical normal-approximation
  background, not automatically a new AI algorithm.", "disposition": "retained_context",
  "existing_record_ids": [], "group": "amortized-svgd", "index": 35, "kind": "bibliography",
  "next_check": "Use the original theorem and conditions only after reading it for
  a specific future claim.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "e401080006cf2d9278c0e0f56adb157295da28884acf9532310df91ded73af25", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/35", "responsible_owner": {"family": "main", "index": 909}, "text": "Stein,
  Charles. A bound for the error in the normal approximation to the distribution of
  a sum of dependent\nrandom variables. In Proceedings of the Sixth Berkeley Symposium
  on Mathematical Statistics and Probability,\nVolume 2: Probability Theory, pp. 583–602,
  1972."}'
- '{"added_record_ids": [], "assessment": "Tieleman 2008 is represented in maintained
  PersistentContrastiveDivergence; persistence and generic Stein fitting remain distinct.",
  "disposition": "existing_record_context", "existing_record_ids": ["AIMech:PersistentContrastiveDivergence",
  "AIMech:ContrastiveDivergence"], "group": "amortized-svgd", "index": 36, "kind":
  "bibliography", "next_check": "Retain exact PCD source scope and do not infer unbiased
  model expectations or sampler equivalence.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "9282f4df20a001c293f376684acaaa30eb76b1244ae64659e5222db49c7a377b", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/36", "responsible_owner": {"family": "main", "index": 909}, "text": "Tieleman,
  Tijmen. Training restricted boltzmann machines using approximations to the likelihood
  gradient. In\nProceedings of the 25th international conference on Machine learning,
  pp. 1064–1071. ACM, 2008."}'
- '{"added_record_ids": [], "assessment": "Variational Gaussian processes is a specific
  variational-family source; a generic GP model or another sparse approximation is
  not enough for identity.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "amortized-svgd", "index": 37, "kind": "bibliography", "next_check":
  "Inspect the exact method, construction and objective before owner assignment.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "6f49b889d13be8d64bfaa7c7d6f66622603ebd997131b1fe05c4d7a6951e0e7e", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/37", "responsible_owner": {"family": "main", "index": 909}, "text": "Tran,
  Dustin, Ranganath, Rajesh, and Blei, David M.\nVariational gaussian process.\narXiv
  preprint\narXiv:1511.06499, 2015."}'
- '{"added_record_ids": [], "assessment": "Xie et al. generative ConvNet theory is
  an energy/convolutional model source; it is not automatically adversarial learning.",
  "disposition": "pending_inspection", "existing_record_ids": ["AIMech:ProductOfExperts"],
  "group": "amortized-svgd", "index": 38, "kind": "bibliography", "next_check": "Read
  the original model and learning theory before relating it to the SteinGAN composite.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "8f3ed5561f2492c89e131bf766691f21c96debc7399acadc8182b49fd626cdbf", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/38", "responsible_owner": {"family": "main", "index": 909}, "text": "Xie,
  Jianwen, Lu, Yang, Zhu, Song-Chun, and Wu, Ying Nian. A theory of generative convnet.
  arXiv preprint\narXiv:1602.03264, 2016."}'
- '{"added_record_ids": [], "assessment": "LSUN is retained large-scale image-data
  construction/evaluation context, not a newly asserted AI method.", "disposition":
  "retained_context", "existing_record_ids": [], "group": "amortized-svgd", "index":
  39, "kind": "bibliography", "next_check": "Inspect benchmark construction and task
  protocol for any later empirical claim.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "aa6c4160ed75a1e243604864eee824eb8f4ea72d3e96a19ea00d20c92011c96c", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/39", "responsible_owner": {"family": "main", "index": 909}, "text": "Yu,
  Fisher, Seff, Ari, Zhang, Yinda, Song, Shuran, Funkhouser, Thomas, and Xiao, Jianxiong.
  Lsun: Construction\nof a large-scale image dataset using deep learning with humans
  in the loop. arXiv preprint arXiv:1506.03365,\n2015."}'
- '{"added_record_ids": [], "assessment": "Energy-based GAN is a specific generative-training
  construction; the broad GAN class supplies context only.", "disposition": "pending_inspection",
  "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd",
  "index": 40, "kind": "bibliography", "next_check": "Read the energy/discriminator
  objective and distinguish it from SteinGAN.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "db3ea88896534fe85c4cfc87ab4e8e959fe4714561bd97c1d85f08abae15b421", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "arxiv-v2"}, "pointer":
  "/items/40", "responsible_owner": {"family": "main", "index": 909}, "text": "Zhao,
  Junbo, Mathieu, Michael, and LeCun, Yann. Energy-based generative adversarial network.
  arXiv preprint\narXiv:1609.03126, 2016."}'
- '{"added_record_ids": [], "assessment": "Agakov and Barber auxiliary variational
  methods require a distinct original construction/objective assessment.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index":
  41, "kind": "bibliography", "next_check": "Read the exact auxiliary-variable formulation
  before comparing implicit-family training.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "62b44c4da1219173d3626bb6460e81f1bef8e70c485bcfdb116ab0db0fd5fdac", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/41", "responsible_owner": {"family": "main", "index": 909}, "text": "Agakov,
  Felix V and Barber, David. An auxiliary varia-\ntional method. In International
  Conference on Neural\nInformation Processing, pp. 561–566. Springer, 2004."}'
- '{"added_record_ids": [], "assessment": "Andrieu and Thoms is an adaptive-MCMC tutorial.
  Main63 covers different regeneration/evolutionary originals and is contextual, not
  exact source responsibility for this tutorial.", "disposition": "pending_inspection",
  "existing_record_ids": [], "group": "amortized-svgd", "index": 42, "kind": "bibliography",
  "next_check": "Inspect the tutorial and identify concrete algorithms before linking
  exact existing owners or asserting a new method.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "54a0b5051505958257db726670d13c595b88ad3832bfdf56bc64f1834d9f89c3", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/42", "responsible_owner": {"family": "main", "index": 909}, "text": "Andrieu,
  Christophe and Thoms, Johannes. A tutorial on\nadaptive mcmc. Statistics and Computing,
  18(4):343–\n373, 2008."}'
- '{"added_record_ids": [], "assessment": "Bayesian dark knowledge is a particular
  posterior-predictive/distillation procedure. The AIO Distillation class supplies
  broad context only.", "disposition": "pending_inspection", "existing_record_ids":
  ["AIO:Distillation"], "group": "amortized-svgd", "index": 43, "kind": "bibliography",
  "next_check": "Read the original approximation objective and compare with predictive
  compression; do not equate it with DINO.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "b13879b74ba1f1cdd3820c4f1814cdfc303e67215fb14fb00e3d89db7949dffd", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/43", "responsible_owner": {"family": "main", "index": 909}, "text": "Balan,\nAnoop
  Korattikara,\nRathod,\nVivek,\nMurphy,\nKevin P, and Welling, Max. Bayesian dark
  knowledge.\nIn Advances in Neural Information Processing Systems,\npp. 3438–3446,
  2015."}'
- '{"added_record_ids": [], "assessment": "Briol et al. concerns probabilistic integration;
  integration and finite-particle sampler fitting are separate responsibilities.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd",
  "index": 44, "kind": "bibliography", "next_check": "Inspect the cited integration
  construction and its relation to control functionals and Bayesian quadrature.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "59a9adfc7f6af1babcf6505fd8f0ad06d7b0336c1b69a8c91f1d88b8fffd9d77", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/44", "responsible_owner": {"family": "main", "index": 909}, "text": "Briol,
  Franc¸ois-Xavier, Oates, Chris, Girolami, Mark, Os-\nborne, Michael A, Sejdinovic,
  Dino, et al. Probabilistic\nintegration: A role for statisticians in numerical anal-\nysis?\narXiv
  preprint http://arxiv.org/abs/1512.00933,\n2015."}'
- '{"added_record_ids": [], "assessment": "IWAE has a specific importance-weighted
  variational objective. VAE and reweighted wake-sleep are related maintained scopes,
  not aliases.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:VariationalAutoEncoder",
  "AIMech:ReweightedWakeSleep"], "group": "amortized-svgd", "index": 45, "kind": "bibliography",
  "next_check": "Inspect the exact objective/gradient and compare IWAE with reweighted
  wake-sleep.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "357450bc10808e62d1e9eca3cb30c226321553aa3ccea4c64f3b29edfef5fa51", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/45", "responsible_owner": {"family": "main", "index": 909}, "text": "Burda,
  Yuri, Grosse, Roger, and Salakhutdinov, Rus-\nlan. Importance weighted autoencoders.
  arXiv preprint\narXiv:1509.00519, 2015."}'
- '{"added_record_ids": [], "assessment": "Chwialkowski et al. kernel goodness-of-fit
  testing belongs to the existing pending Stein-test source question; it is not direct
  amortized-KSD training.", "disposition": "existing_pending_owner", "existing_record_ids":
  ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index":
  46, "kind": "bibliography", "next_check": "Read the exact test original and distinguish
  its statistic and assumptions from Liu–Lee–Jordan and the sampler appendix.", "origin":
  {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "119443ebbfe5a802e97fad4ea0a54b97abfbd9b19811d7e3762197b00628b6e9", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/46", "responsible_owner": {"family": "main", "index": 909}, "text": "Chwialkowski,
  Kacper, Strathmann, Heiko, and Gretton,\nArthur. A kernel test of goodness of ﬁt.
  In Proceed-\nings of the International Conference on Machine Learn-\ning (ICML),
  2016."}'
- '{"added_record_ids": [], "assessment": "Delyon and Portier concern integral approximation
  using kernel smoothing; no sampler-training equivalence follows from the kernel
  vocabulary.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "amortized-svgd", "index": 47, "kind": "bibliography", "next_check": "Read the original
  approximation method and retain its integration-estimator scope.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "2933fd3376261ee068399f2ffe4dc96bdee658678a235983b755208f07bfc48b", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/47", "responsible_owner": {"family": "main", "index": 909}, "text": "Delyon,
  Bernard and Portier, Franc¸ois.\nIntegral ap-\nproximation by kernel smoothing.\narXiv
  preprint\narXiv:1409.0733, 2014."}'
- '{"added_record_ids": [], "assessment": "Gershman and Goodman 2014 is amortized
  probabilistic reasoning, not the 2012 nonparametric-VI question already retained
  under owner909.", "disposition": "pending_inspection", "existing_record_ids": [],
  "group": "amortized-svgd", "index": 48, "kind": "bibliography", "next_check": "Inspect
  the 2014 original separately; retain the exact 2012 pointer and do not substitute
  one for the other.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "b1f2cd2eb884ec8baf0a856e938b9487716e2bd5ee7234b7d5f60d88da1c20e4", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/48", "responsible_owner": {"family": "main", "index": 909}, "text": "Gershman,
  Samuel J and Goodman, Noah D. Amortized\ninference in probabilistic reasoning. In
  Proceedings of\nthe 36th Annual Conference of the Cognitive Science So-\nciety,
  2014."}'
- '{"added_record_ids": [], "assessment": "The maintained GAN class supplies generative/adversarial
  context for Goodfellow et al.; it is not the generic differentiable Stein sampler.",
  "disposition": "existing_record_context", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"],
  "group": "amortized-svgd", "index": 49, "kind": "bibliography", "next_check": "Retain
  original GAN objective/version scope and inspect any claim beyond the current class
  context.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "817f39003ab1393d51ad58aa1d8a4662db8326e307778e6b6b3201c5be877225", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/49", "responsible_owner": {"family": "main", "index": 909}, "text": "Goodfellow,
  Ian, Pouget-Abadie, Jean, Mirza, Mehdi, Xu,\nBing, Warde-Farley, David, Ozair, Sherjil,
  Courville,\nAaron, and Bengio, Yoshua. Generative adversarial nets.\nIn Advances
  in Neural Information Processing Systems,\npp. 2672–2680, 2014."}'
- '{"added_record_ids": [], "assessment": "Henmi et al. importance sampling with estimated
  samplers is an estimator source; BBVI or amortization terminology does not establish
  identity.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "amortized-svgd", "index": 50, "kind": "bibliography", "next_check": "Read the original
  weighting/estimation construction and assumptions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "50f52683c3d853b6e1ca9a65792b15c3eb15fde79a2ba12770edb6927711e98f", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/50", "responsible_owner": {"family": "main", "index": 909}, "text": "Henmi,
  Masayuki, Yoshida, Ryo, and Eguchi, Shinto.\nImportance\nsampling\nvia\nthe\nestimated\nsampler.\nBiometrika,
  94(4):985–991, 2007."}'
- '{"added_record_ids": [], "assessment": "Hoffman–Blei–Wang–Paisley stochastic VI
  is explicitly retained under main426 with the exact 1206.7051 source. Nested0 concerns
  a different 2017 sparse-GP source.", "disposition": "existing_pending_owner", "existing_record_ids":
  ["AIMech:BlackBoxVariationalInference"], "group": "amortized-svgd", "index": 51,
  "kind": "bibliography", "next_check": "Use main426 for the exact SVI original; distinguish
  its stochastic natural-gradient scheme from online LDA and other similarly named
  methods.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "354fbf62e4458c3c938a13c1dbce622a3d55dc29d169e542214779aa6998a74b", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/51", "responsible_owner": {"family": "main", "index": 426}, "text": "Hoffman,
  Matthew D, Blei, David M, Wang, Chong, and\nPaisley, John. Stochastic variational
  inference. JMLR,\n2013."}'
- '{"added_record_ids": [], "assessment": "The maintained VAE class supplies model
  context for auto-encoding variational Bayes; the estimator/training source has narrower
  details than the class.", "disposition": "existing_record_context", "existing_record_ids":
  ["AIO:VariationalAutoEncoder"], "group": "amortized-svgd", "index": 52, "kind":
  "bibliography", "next_check": "Retain the exact AEVB version and inspect any pathwise-estimator
  or application claim separately.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "278284d4ef7b4f7fc4b2f6f1e9b5ca97d1403fc1c5656ae67ac17b1071648a19", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/52", "responsible_owner": {"family": "main", "index": 909}, "text": "Kingma,
  Diederik P and Welling, Max.\nAuto-encoding\nvariational Bayes. In Proceedings of
  the International\nConference on Learning Representations (ICLR), 2013."}'
- '{"added_record_ids": [], "assessment": "Inverse autoregressive flow is a distinct
  flow construction; the Rezende–Mohamed question supplies related family context,
  not exact equivalence.", "disposition": "pending_inspection", "existing_record_ids":
  ["AIO:VariationalAutoEncoder", "AIMech:FlowMatching", "AIMech:RectifiedFlow"], "group":
  "amortized-svgd", "index": 53, "kind": "bibliography", "next_check": "Read the IAF
  transformation and estimator, then reconcile with the existing pending normalizing-flow
  family.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "8113c3744db9f360c8b6a15b2589142dbb477404dbac9231de88b5b0b70b08a6", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/53", "responsible_owner": {"family": "main", "index": 909}, "text": "Kingma,
  Diederik P, Salimans, Tim, and Welling, Max. Im-\nproving variational inference
  with inverse autoregressive\nﬂow. arXiv preprint arXiv:1606.04934, 2016."}'
- '{"added_record_ids": [], "assessment": "Li–Turner–Liu amortised MCMC is a specific
  transition-distillation/implicit-inference procedure, not an alias from shared amortization
  vocabulary.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "amortized-svgd", "index": 54, "kind": "bibliography", "next_check": "Inspect its
  original teacher transition, discrepancy and fitting objective.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "067bdc3d069d0d19b4e5d173a4d6b9d4316d314650f902bbe638433f79469c9e", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/54", "responsible_owner": {"family": "main", "index": 909}, "text": "Li,
  Yingzhen, Turner, Richard E, and Liu, Qiang. Approx-\nimate inference with amortised
  mcmc. arXiv preprint\narXiv:1702.08343, 2017."}'
- '{"added_record_ids": [], "assessment": "Liu and Lee black-box importance sampling
  concerns importance weighting; maintained BBVI has a different estimator/objective.",
  "disposition": "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference",
  "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 55,
  "kind": "bibliography", "next_check": "Inspect the exact importance-weight construction
  and distinguish it from BBVI and particle transport.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "6806c6dc5e289c7730be28375277edfa7d6daf2afde8b257bf0c8aefccb20dce", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/55", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu,
  Qiang and Lee, Jason D. Black-box importance sam-\npling. https://arxiv.org/abs/1610.05247,
  2016."}'
- '{"added_record_ids": [], "assessment": "The maintained SVGD record represents direct
  interacting-particle transport. The proposed record fits shared sampler parameters
  to Stein-displaced outputs.", "disposition": "existing_record_context", "existing_record_ids":
  ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index":
  56, "kind": "bibliography", "next_check": "Retain the arXiv-versus-official-proceedings
  version distinction; do not turn component use into an alias.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "fa64d842a5e835bfd375347eb9e57f11c8c8b3dd85d76290d8e1d3101a499f8f", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/56", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu,
  Qiang and Wang, Dilin. Stein variational gradient de-\nscent: A general purpose
  bayesian inference algorithm.\narXiv preprint arXiv:1608.04471, 2016."}'
- '{"added_record_ids": [], "assessment": "Liu–Lee–Jordan KSD goodness-of-fit testing
  is explicitly retained under the existing owner909 Stein-test question.", "disposition":
  "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"],
  "group": "amortized-svgd", "index": 57, "kind": "bibliography", "next_check": "Read
  the exact test original, distinguish it from Chwialkowski/Gorham and direct KSD
  minimization.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "f39384f1ef39ab27c5aa8b26ad5af65cc8e7992520c35b771f3894edcc3c55a6", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/57", "responsible_owner": {"family": "main", "index": 909}, "text": "Liu,
  Qiang, Lee, Jason D, and Jordan, Michael I. A ker-\nnelized Stein discrepancy for
  goodness-of-ﬁt tests. In\nProceedings of the International Conference on Machine\nLearning
  (ICML), 2016."}'
- '{"added_record_ids": [], "assessment": "Maclaurin et al. early stopping as nonparametric
  VI is not Gershman et al. 2012, which remains a separate owner909 question.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index":
  58, "kind": "bibliography", "next_check": "Inspect the early-stopping distribution/objective
  and retain the original Gershman pointer.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "8b9f64aadf4c89a9d522ad653561c159d8bf0f06b1ae477d2fd9dab3bced2d7e", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/58", "responsible_owner": {"family": "main", "index": 909}, "text": "Maclaurin,
  Dougal, Duvenaud, David, and Adams, Ryan P.\nEarly stopping is nonparametric variational
  inference.\narXiv preprint arXiv:1504.01344, 2015."}'
- '{"added_record_ids": [], "assessment": "Mandt et al. analyze SGD variationally;
  an analysis of an optimizer does not automatically define a new optimizer or sampler.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd",
  "index": 59, "kind": "bibliography", "next_check": "Read assumptions, stationary
  approximation and the claimed algorithmic contribution before identity decisions.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "db6604c93e0ee53951128974583da142cad3ac322302d5ff52594929a3af5742", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/59", "responsible_owner": {"family": "main", "index": 909}, "text": "Mandt,
  Stephan, Hoffman, Matthew D, and Blei, David M.\nA variational analysis of stochastic
  gradient algorithms.\narXiv preprint arXiv:1602.02666, 2016."}'
- '{"added_record_ids": [], "assessment": "Adversarial variational Bayes is a specific
  inference/training procedure; VAE/GAN classes are related scopes only.", "disposition":
  "pending_inspection", "existing_record_ids": ["AIO:VariationalAutoEncoder", "AIO:GenerativeAdversarialNetwork"],
  "group": "amortized-svgd", "index": 60, "kind": "bibliography", "next_check": "Inspect
  the discriminator/variational objective and compare with the generic Stein fitting
  update.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "215c8bda7beb5b6e77b7de71b2be73d89e79bd078eff7f987cb542122b8c9677", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/60", "responsible_owner": {"family": "main", "index": 909}, "text": "Mescheder,
  Lars, Nowozin, Sebastian, and Geiger, An-\ndreas.\nAdversarial variational bayes:
  Unifying varia-\ntional autoencoders and generative adversarial networks.\narXiv
  preprint arXiv:1701.04722, 2017."}'
- '{"added_record_ids": [], "assessment": "Mohamed and Lakshminarayanan implicit generative
  models is retained as a broad family/source question, not a single asserted algorithm.",
  "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork",
  "AIO:VariationalAutoEncoder"], "group": "amortized-svgd", "index": 61, "kind": "bibliography",
  "next_check": "Read the taxonomy and isolate concrete procedures before proposing
  records.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "55c3a7eac063b76bf81a1353c55fbb73b048f431d09c4c688fa8b3656a2dbf10", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/61", "responsible_owner": {"family": "main", "index": 909}, "text": "Mohamed,
  Shakir and Lakshminarayanan, Balaji. Learn-\ning in implicit generative models.\narXiv
  preprint\narXiv:1610.03483, 2016."}'
- '{"added_record_ids": [], "assessment": "The 2017 control-functionals citation is
  preserved separately from the 2014 occurrence; identical-looking titles do not resolve
  version correspondence.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "amortized-svgd", "index": 62, "kind": "bibliography", "next_check":
  "Inspect the published original and reconcile the exact 2014/2017 versions and construction.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "1ab7d269b8c8b89363ce6faf9c0495b1229f85a6d3701a169a70df201170a373", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/62", "responsible_owner": {"family": "main", "index": 909}, "text": "Oates,
  Chris J, Girolami, Mark, and Chopin, Nicolas. Con-\ntrol functionals for Monte Carlo
  integration. Journal of\nthe Royal Statistical Society, Series B, 2017."}'
- '{"added_record_ids": [], "assessment": "O’Hagan’s Monte Carlo critique is retained
  as methodology context, not an asserted standalone new AI method.", "disposition":
  "retained_context", "existing_record_ids": [], "group": "amortized-svgd", "index":
  63, "kind": "bibliography", "next_check": "Inspect the exact argument if used to
  support quadrature or Monte Carlo claims.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "ca09058ca5b43a8f7915b2103269b7b3f470f94a03fa417dc45d237c7899da03", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/63", "responsible_owner": {"family": "main", "index": 909}, "text": "O’Hagan,
  Anthony.\nMonte Carlo is fundamentally un-\nsound. Journal of the Royal Statistical
  Society. Series\nD (The Statistician), 36(2/3):247–249, 1987."}'
- '{"added_record_ids": [], "assessment": "Bayes–Hermite quadrature is a numerical-integration
  source, distinct from generic sampler fitting.", "disposition": "pending_inspection",
  "existing_record_ids": [], "group": "amortized-svgd", "index": 64, "kind": "bibliography",
  "next_check": "Inspect the quadrature prior, estimator and applicability assumptions.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "1a3f25d3f4857679f8e96d24973df4f53adc375061b8c67f05f970ba041ec906", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/64", "responsible_owner": {"family": "main", "index": 909}, "text": "O’Hagan,
  Anthony. Bayes–hermite quadrature. Journal of\nstatistical planning and inference,
  29(3):245–260, 1991."}'
- '{"added_record_ids": [], "assessment": "Paige and Wood inference networks for SMC
  in graphical models have a proposal/inference procedure requiring separate analysis.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd",
  "index": 65, "kind": "bibliography", "next_check": "Inspect the original SMC proposal
  training and relation to generic amortization.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "e5aa80532831ae5f3e32c7f833c6b08b449cb107eb576a4c64cec275696fed84", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/65", "responsible_owner": {"family": "main", "index": 909}, "text": "Paige,
  Brooks and Wood, Frank. Inference networks for se-\nquential monte carlo in graphical
  models. arXiv preprint\narXiv:1602.06701, 2016."}'
- '{"added_record_ids": [], "assessment": "Operator variational inference is an operator/objective
  source; neither BBVI nor amortized SVGD is an automatic alias.", "disposition":
  "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference",
  "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 66,
  "kind": "bibliography", "next_check": "Inspect its original operator family, test
  function and objective.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "f3c0b8ddc37c6514f9047fe3d6b50836df75a98840f03f38ed5fd3a5667884fb", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/66", "responsible_owner": {"family": "main", "index": 909}, "text": "Ranganath,
  R., Altosaar, J., Tran, D., and Blei, D.M. Oper-\nator variational inference. 2016."}'
- '{"added_record_ids": [], "assessment": "Rezende–Mohamed normalizing-flow VI is
  the existing owner909 bibliography question, cross-linked to H355-FLOW-17. FlowMatching/RectifiedFlow
  are related contexts, not resolutions.", "disposition": "existing_pending_owner",
  "existing_record_ids": ["AIMech:FlowMatching", "AIMech:RectifiedFlow"], "group":
  "amortized-svgd", "index": 67, "kind": "bibliography", "next_check": "Inspect the
  exact original flow transformations/objective and retain separate CNF/probability-flow
  family scope in issue406.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "19ad5a801f0cd44e199f0aaba54cb2a3e1d3f304dd59617d42b48c86e2c97968", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/67", "responsible_owner": {"family": "main", "index": 909}, "text": "Rezende,
  Danilo Jimenez and Mohamed, Shakir. Varia-\ntional inference with normalizing ﬂows.
  In Proceedings\nof the International Conference on Machine Learning\n(ICML), 2015."}'
- '{"added_record_ids": [], "assessment": "Roberts and Rosenthal adaptive-MCMC examples
  are an exact original-source question. Main63’s different cited works provide context,
  not an accepted equivalent owner.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "amortized-svgd", "index": 68, "kind": "bibliography", "next_check":
  "Inspect the concrete adaptations and conditions; link an existing owner only after
  source-specific comparison.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "dbb85db7c3486393b5733fa07c5d22932e7d129f01e177f8c75beef219543d23", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/68", "responsible_owner": {"family": "main", "index": 909}, "text": "Roberts,
  Gareth O and Rosenthal, Jeffrey S. Examples of\nadaptive mcmc. Journal of Computational
  and Graphi-\ncal Statistics, 18(2):349–367, 2009."}'
- '{"added_record_ids": [], "assessment": "Salimans et al. bridge MCMC and VI using
  a specific hybrid construction; generic sampler fitting or ULA is not its identity.",
  "disposition": "pending_inspection", "existing_record_ids": ["AIMech:UnadjustedLangevinAlgorithm"],
  "group": "amortized-svgd", "index": 69, "kind": "bibliography", "next_check": "Read
  the original transition/variational construction and objective.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "56ecfa3a18c9f9edd2df281a5c1dc4884c3c2f5f31187a15164fda777d648450", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/69", "responsible_owner": {"family": "main", "index": 909}, "text": "Salimans,
  Tim et al. Markov chain monte carlo and varia-\ntional inference: Bridging the gap.
  In International Con-\nference on Machine Learning, 2015."}'
- '{"added_record_ids": [], "assessment": "Snelson–Ghahramani compact predictive approximations
  remain retained in the official 2017 bibliography; their absence from the later
  bibliography does not erase this source responsibility.", "disposition": "pending_inspection",
  "existing_record_ids": ["AIO:Distillation"], "group": "amortized-svgd", "index":
  70, "kind": "bibliography", "next_check": "Read the predictive-compression method
  and compare exact source scope with Bayesian dark knowledge.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "f9cc135d8e4eb503392c217e178c10d89e5eb1d1f3d66379010937bd40427483", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/70", "responsible_owner": {"family": "main", "index": 909}, "text": "Snelson,
  Edward and Ghahramani, Zoubin. Compact ap-\nproximations to bayesian predictive
  distributions.\nIn\nProceedings of the 22nd international conference on\nMachine
  learning, pp. 840–847. ACM, 2005."}'
- '{"added_record_ids": [], "assessment": "Welling–Teh SGLD is a stochastic-gradient
  transition source. Maintained ULA and main42 TULA are related but do not resolve
  this exact method.", "disposition": "pending_inspection", "existing_record_ids":
  ["AIMech:UnadjustedLangevinAlgorithm"], "group": "amortized-svgd", "index": 71,
  "kind": "bibliography", "next_check": "Inspect gradient noise, stepsize schedule
  and target assumptions before identity or owner decisions.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "b8f18daf62d83716f272d13247d6b7bc1fccb0cc56519ab84e4711417dec0654", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/71", "responsible_owner": {"family": "main", "index": 909}, "text": "Welling,
  Max and Teh, Yee W.\nBayesian learning via\nstochastic gradient Langevin dynamics.
  In Proceedings\nof the International Conference on Machine Learning\n(ICML), 2011."}'
- '{"added_record_ids": [], "assessment": "Wu et al. quantitative analysis of decoder-based
  generative models is retained evaluation/methodology scope, not automatically another
  generative algorithm.", "disposition": "retained_context", "existing_record_ids":
  ["AIO:GenerativeAdversarialNetwork", "AIO:VariationalAutoEncoder"], "group": "amortized-svgd",
  "index": 72, "kind": "bibliography", "next_check": "Inspect the original estimator
  and evaluation protocol before using quantitative comparisons.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "ea1e831d57cfdd7fbd694dc49a704bf1272fba70fe27fdf49b7ca3796318a266", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai2017"}, "pointer":
  "/items/72", "responsible_owner": {"family": "main", "index": 909}, "text": "Wu,
  Yuhuai, Burda, Yuri, Salakhutdinov, Ruslan, and\nGrosse,\nRoger.\nOn the quantitative
  analysis of\ndecoder-based generative models.\narXiv preprint\narXiv:1611.04273,
  2016."}'
- '{"added_record_ids": [], "assessment": "Agakov and Barber auxiliary variational
  methods require a distinct original construction/objective assessment.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index":
  73, "kind": "bibliography", "next_check": "Read the exact auxiliary-variable formulation
  before comparing implicit-family training.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "6f201b44a2760d529a787bc6f38617abf755ec437dec409d547df5b3e359167f", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/73", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Agakov, Felix V and Barber, David. An auxiliary varia-\ntional method. In International
  Conference on Neural\nInformation Processing, pp. 561–566. Springer, 2004."}'
- '{"added_record_ids": [], "assessment": "Andrieu and Thoms is an adaptive-MCMC tutorial.
  Main63 covers different regeneration/evolutionary originals and is contextual, not
  exact source responsibility for this tutorial.", "disposition": "pending_inspection",
  "existing_record_ids": [], "group": "amortized-svgd", "index": 74, "kind": "bibliography",
  "next_check": "Inspect the tutorial and identify concrete algorithms before linking
  exact existing owners or asserting a new method.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "fce7fae9331a6d951d9ca9f92e51b1af6b162cc071537fc03303c1177413efcf", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/74", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Andrieu, Christophe and Thoms, Johannes. A tutorial on\nadaptive mcmc. Statistics
  and Computing, 18(4):343–\n373, 2008."}'
- '{"added_record_ids": [], "assessment": "Bayesian dark knowledge is a particular
  posterior-predictive/distillation procedure. The AIO Distillation class supplies
  broad context only.", "disposition": "pending_inspection", "existing_record_ids":
  ["AIO:Distillation"], "group": "amortized-svgd", "index": 75, "kind": "bibliography",
  "next_check": "Read the original approximation objective and compare with predictive
  compression; do not equate it with DINO.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "61d46554ab4b0cf16f182ffa87eaf3e12e2eb2177fbf1c2e3b034158b2bfa9d8", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/75", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Balan,\nAnoop Korattikara,\nRathod,\nVivek,\nMurphy,\nKevin P, and Welling, Max.
  Bayesian dark knowledge.\nIn Advances in Neural Information Processing Systems,\npp.
  3438–3446, 2015."}'
- '{"added_record_ids": [], "assessment": "Briol et al. concerns probabilistic integration;
  integration and finite-particle sampler fitting are separate responsibilities.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd",
  "index": 76, "kind": "bibliography", "next_check": "Inspect the cited integration
  construction and its relation to control functionals and Bayesian quadrature.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "5712a790c48c39c8090684565e7bd115c623789eaa9e981856da9778a4233c7b", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/76", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Briol, Franc¸ois-Xavier, Oates, Chris, Girolami, Mark, Os-\nborne, Michael A, Sejdinovic,
  Dino, et al. Probabilistic\nintegration: A role for statisticians in numerical anal-\nysis?\narXiv
  preprint http://arxiv.org/abs/1512.00933,\n2015."}'
- '{"added_record_ids": [], "assessment": "IWAE has a specific importance-weighted
  variational objective. VAE and reweighted wake-sleep are related maintained scopes,
  not aliases.", "disposition": "pending_inspection", "existing_record_ids": ["AIO:VariationalAutoEncoder",
  "AIMech:ReweightedWakeSleep"], "group": "amortized-svgd", "index": 77, "kind": "bibliography",
  "next_check": "Inspect the exact objective/gradient and compare IWAE with reweighted
  wake-sleep.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "7be97e146f7b71fe76f2efbb55f98d75c5c4edb64fd5a49167d702191e0d9a3a", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/77", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Burda, Yuri, Grosse, Roger, and Salakhutdinov, Rus-\nlan. Importance weighted autoencoders.
  arXiv preprint\narXiv:1509.00519, 2015."}'
- '{"added_record_ids": [], "assessment": "Chwialkowski et al. kernel goodness-of-fit
  testing belongs to the existing pending Stein-test source question; it is not direct
  amortized-KSD training.", "disposition": "existing_pending_owner", "existing_record_ids":
  ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index":
  78, "kind": "bibliography", "next_check": "Read the exact test original and distinguish
  its statistic and assumptions from Liu–Lee–Jordan and the sampler appendix.", "origin":
  {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "e4103113df8e18f8d1175480da88e713674f46704f477c029b355e36255a16c2", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/78", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Chwialkowski, Kacper, Strathmann, Heiko, and Gretton,\nArthur. A kernel test of
  goodness of ﬁt. In Proceed-\nings of the International Conference on Machine Learn-\ning
  (ICML), 2016."}'
- '{"added_record_ids": [], "assessment": "Delyon and Portier concern integral approximation
  using kernel smoothing; no sampler-training equivalence follows from the kernel
  vocabulary.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "amortized-svgd", "index": 79, "kind": "bibliography", "next_check": "Read the original
  approximation method and retain its integration-estimator scope.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "a7af1cc238f27d2d1b214110a78d5a5a178fb4366da905f97df0759e2b53954c", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/79", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Delyon, Bernard and Portier, Franc¸ois.\nIntegral ap-\nproximation by kernel smoothing.\narXiv
  preprint\narXiv:1409.0733, 2014."}'
- '{"added_record_ids": [], "assessment": "Gershman and Goodman 2014 is amortized
  probabilistic reasoning, not the 2012 nonparametric-VI question already retained
  under owner909.", "disposition": "pending_inspection", "existing_record_ids": [],
  "group": "amortized-svgd", "index": 80, "kind": "bibliography", "next_check": "Inspect
  the 2014 original separately; retain the exact 2012 pointer and do not substitute
  one for the other.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "a4117394a3de24e0b4c7bbc03b3316e6c514e0ae3bcc2f1b050247ce35757af5", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/80", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Gershman, Samuel J and Goodman, Noah D. Amortized\ninference in probabilistic reasoning.
  In Proceedings of\nthe 36th Annual Conference of the Cognitive Science So-\nciety,
  2014."}'
- '{"added_record_ids": [], "assessment": "The maintained GAN class supplies generative/adversarial
  context for Goodfellow et al.; it is not the generic differentiable Stein sampler.",
  "disposition": "existing_record_context", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork"],
  "group": "amortized-svgd", "index": 81, "kind": "bibliography", "next_check": "Retain
  original GAN objective/version scope and inspect any claim beyond the current class
  context.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "727cf2ef521e72567a2ad746dff9c5466cc01f1936a682d1f8057dd58f89c43a", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/81", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Goodfellow, Ian, Pouget-Abadie, Jean, Mirza, Mehdi, Xu,\nBing, Warde-Farley, David,
  Ozair, Sherjil, Courville,\nAaron, and Bengio, Yoshua. Generative adversarial nets.\nIn
  Advances in Neural Information Processing Systems,\npp. 2672–2680, 2014."}'
- '{"added_record_ids": [], "assessment": "Henmi et al. importance sampling with estimated
  samplers is an estimator source; BBVI or amortization terminology does not establish
  identity.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "amortized-svgd", "index": 82, "kind": "bibliography", "next_check": "Read the original
  weighting/estimation construction and assumptions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "4396cffa55b2cffb94d5d6abb8e8b21609b6eb54b100922809623173e2ff4641", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/82", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Henmi, Masayuki, Yoshida, Ryo, and Eguchi, Shinto.\nImportance\nsampling\nvia\nthe\nestimated\nsampler.\nBiometrika,
  94(4):985–991, 2007."}'
- '{"added_record_ids": [], "assessment": "Hoffman–Blei–Wang–Paisley stochastic VI
  is explicitly retained under main426 with the exact 1206.7051 source. Nested0 concerns
  a different 2017 sparse-GP source.", "disposition": "existing_pending_owner", "existing_record_ids":
  ["AIMech:BlackBoxVariationalInference"], "group": "amortized-svgd", "index": 83,
  "kind": "bibliography", "next_check": "Use main426 for the exact SVI original; distinguish
  its stochastic natural-gradient scheme from online LDA and other similarly named
  methods.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "4c9c71aad013782bdd7c95f1fdfa7709a8c5e8da0035a7e3099097ca98f4499f", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/83", "responsible_owner": {"family": "main", "index": 426}, "text":
  "Hoffman, Matthew D, Blei, David M, Wang, Chong, and\nPaisley, John. Stochastic
  variational inference. JMLR,\n2013."}'
- '{"added_record_ids": [], "assessment": "The maintained VAE class supplies model
  context for auto-encoding variational Bayes; the estimator/training source has narrower
  details than the class.", "disposition": "existing_record_context", "existing_record_ids":
  ["AIO:VariationalAutoEncoder"], "group": "amortized-svgd", "index": 84, "kind":
  "bibliography", "next_check": "Retain the exact AEVB version and inspect any pathwise-estimator
  or application claim separately.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "c94aa2446f1da1851cf5f317e360f5db32d5d84946b4a0f0199e32d833eefedf", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/84", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Kingma, Diederik P and Welling, Max.\nAuto-encoding\nvariational Bayes. In Proceedings
  of the International\nConference on Learning Representations (ICLR), 2013."}'
- '{"added_record_ids": [], "assessment": "Inverse autoregressive flow is a distinct
  flow construction; the Rezende–Mohamed question supplies related family context,
  not exact equivalence.", "disposition": "pending_inspection", "existing_record_ids":
  ["AIO:VariationalAutoEncoder", "AIMech:FlowMatching", "AIMech:RectifiedFlow"], "group":
  "amortized-svgd", "index": 85, "kind": "bibliography", "next_check": "Read the IAF
  transformation and estimator, then reconcile with the existing pending normalizing-flow
  family.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "8e0d0f5a98a7309e95424ccbbeaa288a0c4aa14cc9d0bcda0b8bb96c1d125e36", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/85", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Kingma, Diederik P, Salimans, Tim, and Welling, Max. Im-\nproving variational inference
  with inverse autoregressive\nﬂow. arXiv preprint arXiv:1606.04934, 2016."}'
- '{"added_record_ids": [], "assessment": "Li–Turner–Liu amortised MCMC is a specific
  transition-distillation/implicit-inference procedure, not an alias from shared amortization
  vocabulary.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "amortized-svgd", "index": 86, "kind": "bibliography", "next_check": "Inspect its
  original teacher transition, discrepancy and fitting objective.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "c83c5749316b801eb80bf97bc944e42e23ce6ce29b079e98b4df7baf7fd44b6d", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/86", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Li, Yingzhen, Turner, Richard E, and Liu, Qiang. Approx-\nimate inference with
  amortised mcmc. arXiv preprint\narXiv:1702.08343, 2017."}'
- '{"added_record_ids": [], "assessment": "Liu and Lee black-box importance sampling
  concerns importance weighting; maintained BBVI has a different estimator/objective.",
  "disposition": "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference",
  "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 87,
  "kind": "bibliography", "next_check": "Inspect the exact importance-weight construction
  and distinguish it from BBVI and particle transport.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "280763c860f10e72456d39a99aff1fd0407363fec894f52906c5c057b7ba3f52", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/87", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Liu, Qiang and Lee, Jason D. Black-box importance sam-\npling. https://arxiv.org/abs/1610.05247,
  2016."}'
- '{"added_record_ids": [], "assessment": "The maintained SVGD record represents direct
  interacting-particle transport. The proposed record fits shared sampler parameters
  to Stein-displaced outputs.", "disposition": "existing_record_context", "existing_record_ids":
  ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index":
  88, "kind": "bibliography", "next_check": "Retain the arXiv-versus-official-proceedings
  version distinction; do not turn component use into an alias.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "0bf5d7b8514d71109497d1f51c2f11426f7a3812648484c0fb46869bf731c8ef", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/88", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Liu, Qiang and Wang, Dilin. Stein variational gradient de-\nscent: A general purpose
  bayesian inference algorithm.\narXiv preprint arXiv:1608.04471, 2016."}'
- '{"added_record_ids": [], "assessment": "Liu–Lee–Jordan KSD goodness-of-fit testing
  is explicitly retained under the existing owner909 Stein-test question.", "disposition":
  "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"],
  "group": "amortized-svgd", "index": 89, "kind": "bibliography", "next_check": "Read
  the exact test original, distinguish it from Chwialkowski/Gorham and direct KSD
  minimization.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "a436b192221da791b9da23e7e6f8f50d3776b6255f81bf13d2838a0a86080402", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/89", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Liu, Qiang, Lee, Jason D, and Jordan, Michael I. A ker-\nnelized Stein discrepancy
  for goodness-of-ﬁt tests. In\nProceedings of the International Conference on Machine\nLearning
  (ICML), 2016."}'
- '{"added_record_ids": [], "assessment": "Maclaurin et al. early stopping as nonparametric
  VI is not Gershman et al. 2012, which remains a separate owner909 question.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd", "index":
  90, "kind": "bibliography", "next_check": "Inspect the early-stopping distribution/objective
  and retain the original Gershman pointer.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "4af785fd3e235c5f7026605282dad7dd3727ec9a44bcf02f055d697021f29d95", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/90", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Maclaurin, Dougal, Duvenaud, David, and Adams, Ryan P.\nEarly stopping is nonparametric
  variational inference.\narXiv preprint arXiv:1504.01344, 2015."}'
- '{"added_record_ids": [], "assessment": "Mandt et al. analyze SGD variationally;
  an analysis of an optimizer does not automatically define a new optimizer or sampler.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd",
  "index": 91, "kind": "bibliography", "next_check": "Read assumptions, stationary
  approximation and the claimed algorithmic contribution before identity decisions.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "a6cfb459d9416441a150ced1214a1fb7b143a04de4ab9b03b6f2027b047eb768", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/91", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Mandt, Stephan, Hoffman, Matthew D, and Blei, David M.\nA variational analysis
  of stochastic gradient algorithms.\narXiv preprint arXiv:1602.02666, 2016."}'
- '{"added_record_ids": [], "assessment": "Adversarial variational Bayes is a specific
  inference/training procedure; VAE/GAN classes are related scopes only.", "disposition":
  "pending_inspection", "existing_record_ids": ["AIO:VariationalAutoEncoder", "AIO:GenerativeAdversarialNetwork"],
  "group": "amortized-svgd", "index": 92, "kind": "bibliography", "next_check": "Inspect
  the discriminator/variational objective and compare with the generic Stein fitting
  update.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "06e573f49a07db6ae647a68c1674a4531a1b976c2fd39f8e8a96f349eb45a152", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/92", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Mescheder, Lars, Nowozin, Sebastian, and Geiger, An-\ndreas.\nAdversarial variational
  bayes: Unifying varia-\ntional autoencoders and generative adversarial networks.\narXiv
  preprint arXiv:1701.04722, 2017."}'
- '{"added_record_ids": [], "assessment": "Mohamed and Lakshminarayanan implicit generative
  models is retained as a broad family/source question, not a single asserted algorithm.",
  "disposition": "pending_inspection", "existing_record_ids": ["AIO:GenerativeAdversarialNetwork",
  "AIO:VariationalAutoEncoder"], "group": "amortized-svgd", "index": 93, "kind": "bibliography",
  "next_check": "Read the taxonomy and isolate concrete procedures before proposing
  records.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "d440c5bdb06beb7d4bc1a13637346fab248fac0cc31ed26ab569f3c8a5403a39", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/93", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Mohamed, Shakir and Lakshminarayanan, Balaji. Learn-\ning in implicit generative
  models.\narXiv preprint\narXiv:1610.03483, 2016."}'
- '{"added_record_ids": [], "assessment": "The 2017 control-functionals citation is
  preserved separately from the 2014 occurrence; identical-looking titles do not resolve
  version correspondence.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "amortized-svgd", "index": 94, "kind": "bibliography", "next_check":
  "Inspect the published original and reconcile the exact 2014/2017 versions and construction.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "c890a539f2c5dccfb9f7dd4f17dfb8e5dc9ea9c6e47a0b31d15db85af1e339a4", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/94", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Oates, Chris J, Girolami, Mark, and Chopin, Nicolas. Con-\ntrol functionals for
  Monte Carlo integration. Journal of\nthe Royal Statistical Society, Series B, 2017."}'
- '{"added_record_ids": [], "assessment": "O’Hagan’s Monte Carlo critique is retained
  as methodology context, not an asserted standalone new AI method.", "disposition":
  "retained_context", "existing_record_ids": [], "group": "amortized-svgd", "index":
  95, "kind": "bibliography", "next_check": "Inspect the exact argument if used to
  support quadrature or Monte Carlo claims.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "2e1836a466c3f28dbdb2574489aa87c8c5e944e0c1ee539a60014d91e093b35f", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/95", "responsible_owner": {"family": "main", "index": 909}, "text":
  "O’Hagan, Anthony.\nMonte Carlo is fundamentally un-\nsound. Journal of the Royal
  Statistical Society. Series\nD (The Statistician), 36(2/3):247–249, 1987."}'
- '{"added_record_ids": [], "assessment": "Bayes–Hermite quadrature is a numerical-integration
  source, distinct from generic sampler fitting.", "disposition": "pending_inspection",
  "existing_record_ids": [], "group": "amortized-svgd", "index": 96, "kind": "bibliography",
  "next_check": "Inspect the quadrature prior, estimator and applicability assumptions.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "dd318b194f69759dfbb5b33d28b0d8e9bd6564f3f668bbef63218142ab4c9a70", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/96", "responsible_owner": {"family": "main", "index": 909}, "text":
  "O’Hagan, Anthony. Bayes–hermite quadrature. Journal of\nstatistical planning and
  inference, 29(3):245–260, 1991."}'
- '{"added_record_ids": [], "assessment": "Paige and Wood inference networks for SMC
  in graphical models have a proposal/inference procedure requiring separate analysis.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "amortized-svgd",
  "index": 97, "kind": "bibliography", "next_check": "Inspect the original SMC proposal
  training and relation to generic amortization.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "9ba0de7e458d4be14186c59ab2b8ea1768ec6c8dec816c68a3224e04426d1953", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/97", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Paige, Brooks and Wood, Frank. Inference networks for se-\nquential monte carlo
  in graphical models. arXiv preprint\narXiv:1602.06701, 2016."}'
- '{"added_record_ids": [], "assessment": "Pu et al. VAE learning via SVGD is a later-version
  citation addition and remains a distinct unread-original question linked to the
  Stein-VAE followup.", "disposition": "pending_inspection", "existing_record_ids":
  ["AIO:VariationalAutoEncoder", "AIMech:SteinVariationalGradientDescent"], "group":
  "amortized-svgd", "index": 98, "kind": "bibliography", "next_check": "Acquire Pu’s
  exact original and compare its procedure with the Feng application; no equivalence
  or priority follows from citation addition.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "9a33575e2d5d6f08160637088e2d3e934113f9a0ea4369ac692cce7074b6870f", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/98", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Pu, Yunchen, Gan, Zhe, Henao, Ricardo, Li, Chunyuan,\nHan, Shaobo, and Carin, Lawrence.\nVae
  learning via\nstein variational gradient descent. In Advances in Neural\nInformation
  Processing Systems (NIPS), 2017."}'
- '{"added_record_ids": [], "assessment": "Operator variational inference is an operator/objective
  source; neither BBVI nor amortized SVGD is an automatic alias.", "disposition":
  "pending_inspection", "existing_record_ids": ["AIMech:BlackBoxVariationalInference",
  "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 99,
  "kind": "bibliography", "next_check": "Inspect its original operator family, test
  function and objective.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "57656ead0f81f28b5f098834b6e5ca4ce1d91db4a5deab01e660ad88310f128b", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/99", "responsible_owner": {"family": "main", "index": 909}, "text":
  "Ranganath, R., Altosaar, J., Tran, D., and Blei, D.M. Oper-\nator variational inference.
  2016."}'
- '{"added_record_ids": [], "assessment": "Rezende–Mohamed normalizing-flow VI is
  the existing owner909 bibliography question, cross-linked to H355-FLOW-17. FlowMatching/RectifiedFlow
  are related contexts, not resolutions.", "disposition": "existing_pending_owner",
  "existing_record_ids": ["AIMech:FlowMatching", "AIMech:RectifiedFlow"], "group":
  "amortized-svgd", "index": 100, "kind": "bibliography", "next_check": "Inspect the
  exact original flow transformations/objective and retain separate CNF/probability-flow
  family scope in issue406.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "7cf44304618a7be11db57eeeb686bc6e24b8e819d2c8a581d0a260e19e5d91c1", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/100", "responsible_owner": {"family": "main", "index": 909},
  "text": "Rezende, Danilo Jimenez and Mohamed, Shakir. Varia-\ntional inference with
  normalizing ﬂows. In Proceedings\nof the International Conference on Machine Learning\n(ICML),
  2015."}'
- '{"added_record_ids": [], "assessment": "Roberts and Rosenthal adaptive-MCMC examples
  are an exact original-source question. Main63’s different cited works provide context,
  not an accepted equivalent owner.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "amortized-svgd", "index": 101, "kind": "bibliography", "next_check":
  "Inspect the concrete adaptations and conditions; link an existing owner only after
  source-specific comparison.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "ddd56ba6787f4788e190beafe49197c88c93879c1b1c477c85b0e2c7e28a7d24", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/101", "responsible_owner": {"family": "main", "index": 909},
  "text": "Roberts, Gareth O and Rosenthal, Jeffrey S. Examples of\nadaptive mcmc.
  Journal of Computational and Graphi-\ncal Statistics, 18(2):349–367, 2009."}'
- '{"added_record_ids": [], "assessment": "Salimans et al. bridge MCMC and VI using
  a specific hybrid construction; generic sampler fitting or ULA is not its identity.",
  "disposition": "pending_inspection", "existing_record_ids": ["AIMech:UnadjustedLangevinAlgorithm"],
  "group": "amortized-svgd", "index": 102, "kind": "bibliography", "next_check": "Read
  the original transition/variational construction and objective.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "a02f88401d9c301ca67931b83bc41ee9effc02f36ae38df3dbbaaa002e1d4270", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/102", "responsible_owner": {"family": "main", "index": 909},
  "text": "Salimans, Tim et al. Markov chain monte carlo and varia-\ntional inference:
  Bridging the gap. In International Con-\nference on Machine Learning, 2015."}'
- '{"added_record_ids": [], "assessment": "Welling–Teh SGLD is a stochastic-gradient
  transition source. Maintained ULA and main42 TULA are related but do not resolve
  this exact method.", "disposition": "pending_inspection", "existing_record_ids":
  ["AIMech:UnadjustedLangevinAlgorithm"], "group": "amortized-svgd", "index": 103,
  "kind": "bibliography", "next_check": "Inspect gradient noise, stepsize schedule
  and target assumptions before identity or owner decisions.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "4efbed874c5a3ecfae0bd29c5506b1de12576f3009b25949aca8123e7e45e1af", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/103", "responsible_owner": {"family": "main", "index": 909},
  "text": "Welling, Max and Teh, Yee W.\nBayesian learning via\nstochastic gradient
  Langevin dynamics. In Proceedings\nof the International Conference on Machine Learning\n(ICML),
  2011."}'
- '{"added_record_ids": [], "assessment": "Wu et al. quantitative analysis of decoder-based
  generative models is retained evaluation/methodology scope, not automatically another
  generative algorithm.", "disposition": "retained_context", "existing_record_ids":
  ["AIO:GenerativeAdversarialNetwork", "AIO:VariationalAutoEncoder"], "group": "amortized-svgd",
  "index": 104, "kind": "bibliography", "next_check": "Inspect the original estimator
  and evaluation protocol before using quantitative comparisons.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "335cfb181557b16aaec88978191f92e870a2c3896a79592ea711903f0a1edc21"}, "original_sha256":
  "9807a5730b4783819894803dd0e9d8da299532aeff9df2089d960d6243fdfb1c", "original_source_details":
  {"next_check": "Reconcile this exact cited work against maintained definitions and
  recursive source-owner objects before deciding existing, distinct, contextual, or
  nonconcept scope. No new-concept count is implied.", "source": "uai-arxiv-v2"},
  "pointer": "/items/104", "responsible_owner": {"family": "main", "index": 909},
  "text": "Wu, Yuhuai, Burda, Yuri, Salakhutdinov, Ruslan, and\nGrosse,\nRoger.\nOn
  the quantitative analysis of\ndecoder-based generative models.\narXiv preprint\narXiv:1611.04273,
  2016."}'
- '{"added_record_ids": ["AIMech:AmortizedSteinVariationalGradientDescent"], "assessment":
  "The accepted 2016v2 and distinct 2017 defining sources support the generic differentiable-sampler
  component. Conditional representation by the proposed record does not resolve SteinGAN,
  direct KSD, Stein-VAE, learned Langevin or umbrella scopes. Historical citation-only
  access remains original provenance.", "disposition": "represented_by_added_record",
  "existing_record_ids": ["AIMech:SteinVariationalGradientDescent", "AIMech:SoftQLearning"],
  "group": "amortized-svgd", "index": 0, "kind": "original_owner_questions", "next_check":
  "After authorized creation verify this narrow component; retain all five application/umbrella
  followups, six other original questions and all source/version limitations.", "origin":
  {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256":
  "50fee4fe8b1585b08ab6e9feab21bd6973cd5ad0166e63a3e2dcf027d3382dbc", "original_source_details":
  {"candidate": "Learning to Draw Samples: With Application to Amortized MLE for Generative
  Adversarial Learning", "next_check": "Verify source version and original amortized
  inference method; decide separate component versus closely related source scope
  after full method reading.", "source": {"citation_ledger": {"path": "/private/tmp/aimech-soft-q-research-20261015/citation-leads.json",
  "sha256": "ff8ba8586defbf9bfa950127764c5ec12426c9eccf87aa255ace12e46102e107"}, "origin":
  "Main PDF p. 10 bibliography and Section 3.3", "pointer": "/leads/1"}, "url": "https://arxiv.org/abs/1611.01722"},
  "pointer": "/original_questions/0", "responsible_owner": {"family": "main", "index":
  909}, "text": "Learning to Draw Samples: With Application to Amortized MLE for Generative
  Adversarial Learning"}'
- '{"added_record_ids": [], "assessment": "SVPG remains an independent policy-parameter-particle
  method. Separate TEMP primary research/native preview now exists, but it is not
  a maintained record and the historical citation-only statement is preserved as historical.",
  "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent",
  "AIMech:SoftQLearning"], "group": "amortized-svgd", "index": 1, "kind": "original_owner_questions",
  "next_check": "Reconcile the separately prepared SVPG draft with a fresh future
  identity/owner decision; do not resolve it through amortized action or generic sampler
  fitting.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256":
  "56ce5076ab8064b6fdf8dcff2d5db24629277b09dd32844ab1d8bd09367497de", "original_source_details":
  {"candidate": "Stein Variational Policy Gradient", "next_check": "Inspect original
  policy-particle method and compare it with amortized action sampling; no identity
  decision from the shared Stein name.", "source": {"citation_ledger": {"path": "/private/tmp/aimech-soft-q-research-20261015/citation-leads.json",
  "sha256": "ff8ba8586defbf9bfa950127764c5ec12426c9eccf87aa255ace12e46102e107"}, "origin":
  "Main PDF p. 9 bibliography", "pointer": "/leads/2"}, "url": "https://arxiv.org/abs/1704.02399"},
  "pointer": "/original_questions/1", "responsible_owner": {"family": "main", "index":
  909}, "text": "Stein Variational Policy Gradient"}'
- '{"added_record_ids": [], "assessment": "Dai et al. particle mirror descent remains
  the exact pending original-source question under main909. Particle vocabulary does
  not establish equality.", "disposition": "existing_pending_owner", "existing_record_ids":
  ["AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index":
  2, "kind": "original_owner_questions", "next_check": "Acquire the exact original
  and compare update geometry, objective and current owners.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256":
  "e90aab01a761b2fd0f577b9a14eff54284e3872cdf0b28500d235d246f4d337b", "original_source_details":
  {"candidate": "Particle mirror descent (Dai et al. 2016)", "next_check": "Identify
  the exact original cited work and reconcile its full method against maintained records
  and existing owners before deciding distinct concept, overlap or existing-owner
  linkage. The cited title is not novelty evidence.", "source": {"citation_scope":
  {"path": "/private/tmp/aimech-svgd-research-20261015/citation-scope.json", "sha256":
  "6e4fce31c555b25438183ac54c24d71ac09d4b6b65373d5297dc835cb088d28f"}, "origin": {"path":
  "/private/tmp/aimech-svgd-research-20261015/extraction/page-09.txt", "sha256": "2bfab341a9840bb1f34c345f8e2d2ba3e12b864e1a41cf44b1a666de99da8f63"},
  "pointer": "/other_bibliography_next_checks/0"}, "url": "https://proceedings.neurips.cc/paper_files/paper/2016/file/b3ba8f1bee1238a2f37603d90b58898d-Paper.pdf"},
  "pointer": "/original_questions/2", "responsible_owner": {"family": "main", "index":
  909}, "text": "Particle mirror descent (Dai et al. 2016)"}'
- '{"added_record_ids": [], "assessment": "The existing Stein discrepancy/test question
  retains separate Chwialkowski, Liu–Lee–Jordan and Gorham–Mackey responsibilities.
  Direct amortized-KSD optimization is a further application question.", "disposition":
  "existing_pending_owner", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent"],
  "group": "amortized-svgd", "index": 3, "kind": "original_owner_questions", "next_check":
  "Inspect the exact tests/statistics and normalize objective conventions before any
  merge or separate record.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256":
  "b26e01f712344c24363ff6aac3914ff0f237923dd4fc86f65c520d1045c987a6", "original_source_details":
  {"candidate": "Kernelized Stein discrepancy and Stein goodness-of-fit tests", "next_check":
  "Identify the exact original cited work and reconcile its full method against maintained
  records and existing owners before deciding distinct concept, overlap or existing-owner
  linkage. The cited title is not novelty evidence.", "source": {"citation_scope":
  {"path": "/private/tmp/aimech-svgd-research-20261015/citation-scope.json", "sha256":
  "6e4fce31c555b25438183ac54c24d71ac09d4b6b65373d5297dc835cb088d28f"}, "origin": {"path":
  "/private/tmp/aimech-svgd-research-20261015/extraction/page-09.txt", "sha256": "2bfab341a9840bb1f34c345f8e2d2ba3e12b864e1a41cf44b1a666de99da8f63"},
  "pointer": "/other_bibliography_next_checks/1"}, "url": "https://proceedings.neurips.cc/paper_files/paper/2016/file/b3ba8f1bee1238a2f37603d90b58898d-Paper.pdf"},
  "pointer": "/original_questions/3", "responsible_owner": {"family": "main", "index":
  909}, "text": "Kernelized Stein discrepancy and Stein goodness-of-fit tests"}'
- '{"added_record_ids": [], "assessment": "Gershman et al. 2012 nonparametric VI remains
  pending. Gershman–Goodman 2014 and Maclaurin 2015 are distinct cited works.", "disposition":
  "existing_pending_owner", "existing_record_ids": ["AIMech:BlackBoxVariationalInference"],
  "group": "amortized-svgd", "index": 4, "kind": "original_owner_questions", "next_check":
  "Acquire the 2012 original and compare variational family/objective with maintained
  BBVI and score-estimator contexts.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256":
  "bbb9fb2e40d4d8eb57321e2221b539794d26cfd755e5dde0569ad71805aedaf7", "original_source_details":
  {"candidate": "Nonparametric variational inference (Gershman et al. 2012)", "next_check":
  "Identify the exact original cited work and reconcile its full method against maintained
  records and existing owners before deciding distinct concept, overlap or existing-owner
  linkage. The cited title is not novelty evidence.", "source": {"citation_scope":
  {"path": "/private/tmp/aimech-svgd-research-20261015/citation-scope.json", "sha256":
  "6e4fce31c555b25438183ac54c24d71ac09d4b6b65373d5297dc835cb088d28f"}, "origin": {"path":
  "/private/tmp/aimech-svgd-research-20261015/extraction/page-09.txt", "sha256": "2bfab341a9840bb1f34c345f8e2d2ba3e12b864e1a41cf44b1a666de99da8f63"},
  "pointer": "/other_bibliography_next_checks/2"}, "url": "https://proceedings.neurips.cc/paper_files/paper/2016/file/b3ba8f1bee1238a2f37603d90b58898d-Paper.pdf"},
  "pointer": "/original_questions/4", "responsible_owner": {"family": "main", "index":
  909}, "text": "Nonparametric variational inference (Gershman et al. 2012)"}'
- '{"added_record_ids": [], "assessment": "The exact Rezende–Mohamed VI source remains
  pending under main909 and is cross-linked to inherited H355-FLOW-17; CNF/probability-flow
  family scope remains separately unresolved.", "disposition": "existing_pending_owner",
  "existing_record_ids": ["AIMech:FlowMatching", "AIMech:RectifiedFlow"], "group":
  "amortized-svgd", "index": 5, "kind": "original_owner_questions", "next_check":
  "Inspect the original flow transform/objective and versions; keep issue406 and its
  broader family question open.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256":
  "ce4ab105a20be2eaefe9f20c9e387c973ddffa815f4ce1dd7fb724a0684cd2b3", "original_source_details":
  {"candidate": "Variational inference with normalizing flows (Rezende and Mohamed
  2015)", "next_check": "Identify the exact original cited work and reconcile its
  full method against maintained records and existing owners before deciding distinct
  concept, overlap or existing-owner linkage. The cited title is not novelty evidence.",
  "source": {"citation_scope": {"path": "/private/tmp/aimech-svgd-research-20261015/citation-scope.json",
  "sha256": "6e4fce31c555b25438183ac54c24d71ac09d4b6b65373d5297dc835cb088d28f"}, "origin":
  {"path": "/private/tmp/aimech-svgd-research-20261015/extraction/page-09.txt", "sha256":
  "2bfab341a9840bb1f34c345f8e2d2ba3e12b864e1a41cf44b1a666de99da8f63"}, "pointer":
  "/other_bibliography_next_checks/3"}, "url": "https://proceedings.neurips.cc/paper_files/paper/2016/file/b3ba8f1bee1238a2f37603d90b58898d-Paper.pdf"},
  "pointer": "/original_questions/5", "responsible_owner": {"family": "main", "index":
  909}, "text": "Variational inference with normalizing flows (Rezende and Mohamed
  2015)"}'
- '{"added_record_ids": [], "assessment": "Doubly stochastic variational Bayes remains
  the exact Titsias–Lázaro-Gredilla original-source question. BBVI and main305 estimator
  contexts do not establish an alias.", "disposition": "existing_pending_owner", "existing_record_ids":
  ["AIMech:BlackBoxVariationalInference"], "group": "amortized-svgd", "index": 6,
  "kind": "original_owner_questions", "next_check": "Read the exact original estimators
  and assumptions before assigning a maintained method or closing the question.",
  "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256":
  "f557f214dc41c1aa4f944e970440bced7f8a0626e8c61fe5d27692d2078adfc3", "original_source_details":
  {"candidate": "Doubly stochastic variational Bayes (Titsias and Lázaro-Gredilla
  2014)", "next_check": "Identify the exact original cited work and reconcile its
  full method against maintained records and existing owners before deciding distinct
  concept, overlap or existing-owner linkage. The cited title is not novelty evidence.",
  "source": {"citation_scope": {"path": "/private/tmp/aimech-svgd-research-20261015/citation-scope.json",
  "sha256": "6e4fce31c555b25438183ac54c24d71ac09d4b6b65373d5297dc835cb088d28f"}, "origin":
  {"path": "/private/tmp/aimech-svgd-research-20261015/extraction/page-09.txt", "sha256":
  "2bfab341a9840bb1f34c345f8e2d2ba3e12b864e1a41cf44b1a666de99da8f63"}, "pointer":
  "/other_bibliography_next_checks/4"}, "url": "https://proceedings.neurips.cc/paper_files/paper/2016/file/b3ba8f1bee1238a2f37603d90b58898d-Paper.pdf"},
  "pointer": "/original_questions/6", "responsible_owner": {"family": "main", "index":
  909}, "text": "Doubly stochastic variational Bayes (Titsias and Lázaro-Gredilla
  2014)"}'
- '{"added_record_ids": [], "assessment": "SteinGAN/amortized MLE is a composite energy-model
  and sampler procedure, not the generic sampler identity. This plan newly proposes
  source-tracking responsibility at main909; historical ownership of this followup
  is not asserted.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:ProductOfExperts",
  "AIMech:ContrastiveDivergence", "AIO:GenerativeAdversarialNetwork"], "group": "amortized-svgd",
  "index": 0, "kind": "dossier_followups", "next_check": "Compare the energy objective,
  approximate model expectation and sampler coupling with PoE/CD and adversarial scopes
  before deciding a distinct record.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256":
  "10346c0e0ef8df53eef646056268c10679136889f8de81c160c0f53b81640f45", "original_source_details":
  {"name": "SteinGAN / amortized MLE of an energy model", "question": "Reconcile the
  composite energy-model/sampler training identity against existing energy-based generative
  and adversarial-learning owners; retain normalizer, approximate model expectation
  and modified-objective caveats. Do not treat it as an alias of generic amortized
  SVGD."}, "pointer": "/followups/0", "responsible_owner": {"family": "main", "index":
  909}, "text": "SteinGAN / amortized MLE of an energy model"}'
- '{"added_record_ids": [], "assessment": "Direct amortized KSD is a separate objective
  with second-order score and D-versus-D-squared normalization questions. Newly proposed
  main909 tracking does not resolve its existing Stein-test family.", "disposition":
  "pending_inspection", "existing_record_ids": ["AIMech:SteinVariationalGradientDescent",
  "AIMech:BlackBoxVariationalInference"], "group": "amortized-svgd", "index": 1, "kind":
  "dossier_followups", "next_check": "Inspect the exact direct objective/normalization
  and compare operator-VI/test scopes before a record decision.", "origin": {"path":
  "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256":
  "d43ae170275c910e42150dc961aa0ef05f5f47b239113bc3cd107b41be898a33", "original_source_details":
  {"name": "Amortized KSD / KSD variational inference", "question": "Compare direct
  stochastic optimization of squared KSD and its second-order score requirements with
  existing Stein-discrepancy/operator-VI scopes. AppendixA uses D^2 in a unit-ball
  decrease display where Eq8 defines D as the unsquared unit-ball supremum; analyze
  normalization before adopting that equivalence. Not a second name for amortized
  SVGD."}, "pointer": "/followups/1", "responsible_owner": {"family": "main", "index":
  909}, "text": "Amortized KSD / KSD variational inference"}'
- '{"added_record_ids": [], "assessment": "Entropy-regularized Stein VAE and Pu et
  al. remain an application/original-source comparison. The Feng application was historically
  read; Pu original remains unacquired. Main909 responsibility is newly proposed here.",
  "disposition": "pending_inspection", "existing_record_ids": ["AIO:VariationalAutoEncoder",
  "AIMech:SteinVariationalGradientDescent"], "group": "amortized-svgd", "index": 2,
  "kind": "dossier_followups", "next_check": "Acquire Pu’s original and compare the
  exact application objectives/updates; citation addition alone is not identity or
  priority.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256":
  "a2b2358c7794b994893c8f0e222a88991d324182ccd3daa5d788c252b24bca89", "original_source_details":
  {"name": "Entropy-regularized Stein VAE and Pu et al.2017 VAE learning via SVGD",
  "question": "Determine whether the application warrants a separate procedure and
  compare exact Pu source. The later citation addition is not automatic equivalence
  or priority evidence."}, "pointer": "/followups/2", "responsible_owner": {"family":
  "main", "index": 909}, "text": "Entropy-regularized Stein VAE and Pu et al.2017
  VAE learning via SVGD"}'
- '{"added_record_ids": [], "assessment": "Learning Langevin step schedules uses a
  finite-horizon simulator and remains a method-versus-application question. Main909
  source responsibility is proposed, not inherited ownership.", "disposition": "pending_inspection",
  "existing_record_ids": ["AIMech:UnadjustedLangevinAlgorithm"], "group": "amortized-svgd",
  "index": 3, "kind": "dossier_followups", "next_check": "Compare learned schedule
  parameterization, positivity, differentiation-through-score and blockwise training
  with ULA and the generic fitting component.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256":
  "7140e136ded5e91c2e1c3c9f490371148f92b35c962696c881dde40362ce59da", "original_source_details":
  {"name": "Amortized-SVGD training of Langevin step schedules", "question": "Resolve
  distinct learned-sampler variant versus application of generic amortized SVGD with
  ULA as simulator. Retain finite horizon, positive step, gradient-through-score and
  blockwise-training limits."}, "pointer": "/followups/3", "responsible_owner": {"family":
  "main", "index": 909}, "text": "Amortized-SVGD training of Langevin step schedules"}'
- '{"added_record_ids": [], "assessment": "Wild VI/variational programming is umbrella
  terminology, not a single algorithm declared by this proposal. Main909 is proposed
  as a tracking location only.", "disposition": "pending_inspection", "existing_record_ids":
  ["AIMech:BlackBoxVariationalInference", "AIO:VariationalAutoEncoder", "AIO:GenerativeAdversarialNetwork"],
  "group": "amortized-svgd", "index": 4, "kind": "dossier_followups", "next_check":
  "Read operator VI, amortised MCMC and adversarial variational Bayes originals before
  taxonomy or record decisions.", "origin": {"path": "/private/tmp/aimech-amortized-svgd-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "44c0151aa92291201ea70e111b13e8a81c2c788e9e8d9d6f5ff748b9cb469671"}, "original_sha256":
  "135503b9a08699a200eb387b0b267b34268534ccdb829b72704568a52b6c5a47", "original_source_details":
  {"name": "Wild variational inference / variational programming", "question": "Compare
  generic implicit-family scope, operator variational inference, amortised MCMC and
  adversarial variational Bayes using original sources before taxonomy or record decisions."},
  "pointer": "/followups/4", "responsible_owner": {"family": "main", "index": 909},
  "text": "Wild variational inference / variational programming"}'
- '{"added_record_ids": [], "assessment": "Björnsson et al. map abstraction is a separate
  pathfinding-source question; A* is component context only.", "disposition": "pending_inspection",
  "existing_record_ids": ["AIMech:AStarSearch"], "group": "rtaa", "index": 0, "kind":
  "bibliography", "next_check": "Inspect the exact abstraction construction and distinguish
  it from RTAA local search.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "47f729de411b235b3eca21c7b13e85fc58862a26ebd15b340b47b11a873ad60e", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/0", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "[1] M. Bjornsson, M. Enzenberger, R. Holte, J.
  Schaeffer, and\nP. Yap. Comparison of different abstractions for pathﬁnding\non
  maps. In Proceedings of the International Joint\nConference on Artiﬁcial Intelligence,
  pages 1511–1512,\n2003."}'
- '{"added_record_ids": [], "assessment": "The 2005 in-press Bulitko–Lee citation
  is linked to nested393’s pending 2006 framework source, with version/year correspondence
  still open.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:LearningRealTimeAStar",
  "AIMech:RealTimeAStar"], "group": "rtaa", "index": 1, "kind": "bibliography", "next_check":
  "Read the original framework and reconcile the in-press/published versions and concrete
  variants.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "abb1e7f31ee6003f90364ef32c93ad1ff025c66df07a6a59a70c02caa9c033a8", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/1", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "[2] V. Bulitko and G. Lee. Learning in real-time
  search: A\nunifying framework. Journal of Artiﬁcial Intelligence\nResearch, page
  (in press), 2005."}'
- '{"added_record_ids": [], "assessment": "Hart et al. is represented by maintained
  AStarSearch. The bibliography’s volume rendering differs from maintained source
  metadata and is retained literally.", "disposition": "existing_record_context",
  "existing_record_ids": ["AIMech:AStarSearch"], "group": "rtaa", "index": 2, "kind":
  "bibliography", "next_check": "Resolve the exact bibliographic volume/version if
  source metadata is revised; preserve ordinary A* versus RTAA scope.", "origin":
  {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "ed69572e3b79a3996740c2309eb71db728e1603149c78fac5479b089546854bd", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/2", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "[3] P. Hart, N. Nilsson, and B. Raphael. A formal
  basis for the\nheuristic determination of minimum cost paths. IEEE\nTransactions
  on Systems Science and Cybernetics,\n2:100–107, 1968."}'
- '{"added_record_ids": [], "assessment": "Ishida’s Real-Time Search book is a broad
  source requiring method-specific reading; it does not resolve main8’s KBFS/multi-state
  residuals.", "disposition": "pending_inspection", "existing_record_ids": ["AIMech:LearningRealTimeAStar",
  "AIMech:RealTimeAStar"], "group": "rtaa", "index": 3, "kind": "bibliography", "next_check":
  "Inspect relevant original sections and relate specific methods to nested393/main8
  without blanket family closure.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "c22bbe136cf22bc7fbdf2929305f8d4a53523dc7cf990e516867a91ec9eaf73f", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/3", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "[4] T. Ishida. Real-Time Search for Learning Autonomous\nAgents.
  Kluwer Academic Publishers, 1997."}'
- '{"added_record_ids": [], "assessment": "Koenig 2004 is the exact earlier LSS source
  question already retained under nested393; the current LSS record does not establish
  version identity.", "disposition": "existing_pending_owner", "existing_record_ids":
  ["AIMech:LocalSearchSpaceLearningRealTimeAStar"], "group": "rtaa", "index": 4, "kind":
  "bibliography", "next_check": "Acquire the original and compare name, learning and
  movement control with the later LSS source.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "11e1e176e92e0b54a9e03c36be628d57cf13aae96e01c0d05e6f67dc851deaab", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/4", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "[5] S. Koenig. A comparison of fast search methods
  for real-time\nsituated agents. In Proceedings of the International\nConference
  on Autonomous Agents and Multi-Agent Systems,\npages 864–871, 2004."}'
- '{"added_record_ids": [], "assessment": "D* Lite is the exact pending nested393
  question, distinct from A*, LSS and RTAA.", "disposition": "existing_pending_owner",
  "existing_record_ids": ["AIMech:AStarSearch", "AIMech:LocalSearchSpaceLearningRealTimeAStar"],
  "group": "rtaa", "index": 5, "kind": "bibliography", "next_check": "Read the original
  incremental g/rhs repair and its relation to Lifelong Planning A*.", "origin": {"path":
  "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "4b979d6327b3008a0d6817ab28fb78f322712daf8121681a0caefa337b561c6b", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/5", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "[6] S. Koenig and M. Likhachev. D* Lite. In Proceedings
  of the\nNational Conference on Artiﬁcial Intelligence, pages\n476–483, 2002."}'
- '{"added_record_ids": [], "assessment": "Adaptive A* is the exact pending nested393
  original-source question; repeated complete search is not the same scope as truncated
  RTAA.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:AStarSearch"],
  "group": "rtaa", "index": 6, "kind": "bibliography", "next_check": "Inspect the
  2005 original and compare complete-search learning with real-time truncation.",
  "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "0ef21de09f4ce709a3c362900d9aaf36caf062a484e61a51616bc34c814e319a", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/6", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "[7] S. Koenig and M. Likhachev. Adaptive A* [poster
  abstract].\nIn Proceedings of the International Conference on\nAutonomous Agents
  and Multi-Agent Systems, pages\n1311–1312, 2005."}'
- '{"added_record_ids": [], "assessment": "Unknown-terrain navigation complexity is
  a theory/source question; it does not imply unrestricted RTAA guarantees.", "disposition":
  "pending_inspection", "existing_record_ids": ["AIMech:LearningRealTimeAStar", "AIMech:RealTimeAStar"],
  "group": "rtaa", "index": 7, "kind": "bibliography", "next_check": "Read the original
  assumptions, bounds and navigation model before transferring any theorem.", "origin":
  {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "08c09d13bad8ac1d379abce3802f46d2213e119423bd5a7ce1600c4a6dea4dc7", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/7", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "[8] S. Koenig, C. Tovey, and Y. Smirnov. Performance
  bounds\nfor planning in unknown terrain. Artiﬁcial Intelligence,\n147:253–279, 2003."}'
- '{"added_record_ids": [], "assessment": "Korf 1990 has maintained LRTA*, RTA* and
  minimin-alpha-pruning contexts with distinct update/control scopes.", "disposition":
  "existing_record_context", "existing_record_ids": ["AIMech:LearningRealTimeAStar",
  "AIMech:RealTimeAStar", "AIMech:MiniminAlphaPruning"], "group": "rtaa", "index":
  8, "kind": "bibliography", "next_check": "Retain those narrow method boundaries
  and inspect any additional source claim separately.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "70da28ef8e224d6a8cc39aa8d672f4e9a58c1808afcf695da2a5c5e061f7106e", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/8", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "[9] R. Korf. Real-time heuristic search. Artiﬁcial
  Intelligence,\n42(2-3):189–211, 1990."}'
- '{"added_record_ids": [], "assessment": "Pearl’s Heuristics is retained broad background;
  the year is preserved as printed, not silently corrected or treated as a complete
  book reading.", "disposition": "retained_context", "existing_record_ids": [], "group":
  "rtaa", "index": 9, "kind": "bibliography", "next_check": "Resolve the exact edition/year
  and inspect only the original section needed by a future claim.", "origin": {"path":
  "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "110ae429646c4947920fb3cec5c77f94f6cd9db2f4731a6263d783f07b1251c7", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/9", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "[10] J. Pearl. Heuristics: Intelligent Search
  Strategies for\nComputer Problem Solving. Addison-Wesley, 1985."}'
- '{"added_record_ids": [], "assessment": "Focused D* is a separate incremental-search
  original and is not automatically identical to D* Lite.", "disposition": "pending_inspection",
  "existing_record_ids": ["AIMech:AStarSearch"], "group": "rtaa", "index": 10, "kind":
  "bibliography", "next_check": "Inspect Stentz’s original control flow and relation
  to later D* Lite.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "26365a747f71dca0eb9865553c26a0998e117a7bec208d3823525540f2446a52", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/10", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "[11] A. Stentz. The focussed D* algorithm for
  real-time\nreplanning. In Proceedings of the International Joint\nConference on
  Artiﬁcial Intelligence, pages 1652–1659,\n1995."}'
- '{"added_record_ids": [], "assessment": "Operational Rationality Through Compilation
  of Anytime Algorithms is a thesis/source responsibility, not a single assumed algorithm
  identity.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "rtaa", "index": 11, "kind": "bibliography", "next_check": "Inspect the thesis and
  identify concrete compilation methods and assumptions.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "44cef92363263d02c9e650e776f0a9eca663f7879fc66517c4ecbe776c4174db", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/11", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "[12] S. Zilberstein. Operational Rationality through
  Compilation\nof Anytime Algorithms. PhD thesis, Computer Science\nDepartment, University
  of California at Berkeley, Berkeley\n(California), 1993."}'
- '{"added_record_ids": [], "assessment": "Arica et al. is a moving-agent comparison
  source; source-specific experiments do not create a universal RTAA ranking.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "rtaa", "index": 12, "kind":
  "bibliography", "next_check": "Inspect the original methods, moving-agent model
  and experimental protocol.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "47f881a39a3dc18b2f6020f80c7faa8c41a2f94e6b25eaf1c14e031603a12ae7", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/12", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "Arica, N.; Mut, A.; Yorukcu, A.; and Demir, K.
  A. 2017.\nAn empirical comparison of search approaches for moving\nagents. Computational
  Intelligence 33(3):368 – 400."}'
- '{"added_record_ids": [], "assessment": "Kiesel–Burns–Ruml concerns reaching goals
  in video games; its concrete real-time procedure remains an original-source question.",
  "disposition": "pending_inspection", "existing_record_ids": ["AIMech:LearningRealTimeAStar",
  "AIMech:LocalSearchSpaceLearningRealTimeAStar"], "group": "rtaa", "index": 13, "kind":
  "bibliography", "next_check": "Read the method and experiments before deciding existing
  context or distinct procedure.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "abb0070fd24784cf9282d9ac93674877731e72487a16a47d295021e934ed2449", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/13", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "Kiesel, S.; Burns, E.; and Ruml, W. 2015. Achieving
  goals\nquickly using real-time search: experimental results in video\ngames. Journal
  of Artiﬁcial Intelligence Research 54:123–\n158."}'
- '{"added_record_ids": [], "assessment": "Kochvi’s 2017 thesis remains an unread
  source behind the 2018 comparison; reading the shorter comparison does not complete
  it.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "rtaa",
  "index": 14, "kind": "bibliography", "next_check": "Acquire the thesis and resolve
  timing aggregation, search budget and experiment details.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "5dd177516169f8929528527f4a790e5cd8ffe1307f5765e485b10e3bdd8ff805", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/14", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "Kochvi, S. 2017. Does fast beat thorough?: Comparing
  real-\ntime search algorithms LSS-LRTA* and RTAA*. Bachelor’s\nthesis, University
  of New Hampshire."}'
- '{"added_record_ids": ["AIMech:RealTimeAdaptiveAStar"], "assessment": "The exact
  2006 RTAA defining work supports the proposed RTAA record. This is narrow conditional
  record representation, not exhaustion of its cited search family or all later variants.",
  "disposition": "represented_by_added_record", "existing_record_ids": [], "group":
  "rtaa", "index": 15, "kind": "bibliography", "next_check": "After authorized creation
  verify the RTAA record; keep workshop/version, Adaptive A*, D* Lite, framework and
  2018 timing/thesis residuals open.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "0111426729865368d057732c3711ec5aab1b96726a722e087f25729b514c7258", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/15", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "Koenig, S., and Likhachev, M. 2006. Real-time
  adaptive A*.\nIn Proceedings of the Fifth International Joint Conference\non Autonomous
  Agents and Multiagent Systems, AAMAS\n’06, 281–288."}'
- '{"added_record_ids": [], "assessment": "Koenig–Sun 2009 is the maintained LSS-LRTA*
  source context, whose reverse-Dijkstra repair differs from RTAA CLOSED-only F-minus-g
  learning.", "disposition": "existing_record_context", "existing_record_ids": ["AIMech:LocalSearchSpaceLearningRealTimeAStar"],
  "group": "rtaa", "index": 16, "kind": "bibliography", "next_check": "Retain source-specific
  movement/repair assumptions and earlier-version residuals.", "origin": {"path":
  "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "b555e1d111fb33cdf17e0a44360e07c70d0a04b914bfbf4c7681a34b39d52c04", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/16", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "Koenig, S., and Sun, X. 2009. Comparing real-time
  and in-\ncremental heuristic search for real-time situated agents. Au-\ntonomous
  Agents and Multi-Agent Systems 18(3):313–341."}'
- '{"added_record_ids": [], "assessment": "Korf 1985 is represented in maintained
  DFID and IDA* scopes; depth-first iterative search is not RTAA.", "disposition":
  "existing_record_context", "existing_record_ids": ["AIMech:DepthFirstIterativeDeepening",
  "AIMech:IterativeDeepeningAStar"], "group": "rtaa", "index": 17, "kind": "bibliography",
  "next_check": "Retain the source/erratum scope and compare any additional claim
  with its exact original version.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "c4aded8e8f77dae6531166a7129d470fecc53780fb3b56da80b4f08a8c970f3b", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/17", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "Korf, R. E. 1985. Depth-ﬁrst iterative-deepening:
  An opti-\nmal admissible tree search. Artiﬁcial Intelligence 27(1):97–\n109."}'
- '{"added_record_ids": [], "assessment": "Sturtevant grid-based pathfinding benchmarks
  are retained evaluation/data context, not an asserted separate search algorithm.",
  "disposition": "retained_context", "existing_record_ids": [], "group": "rtaa", "index":
  18, "kind": "bibliography", "next_check": "Inspect benchmark/map/task construction
  before using performance comparisons.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "7c723f47b8608a86f3dd3da708b0a4742a8dae58e7ec7ac66b2799611ddf8ec5", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/18", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "Sturtevant, N. 2012. Benchmarks for grid-based
  pathﬁnd-\ning. Transactions on Computational Intelligence and AI in\nGames 4(2):144
  – 148."}'
- '{"added_record_ids": [], "assessment": "Wilt–Ruml operator-cost-ratio analysis
  concerns cost representation and best-first search behavior, not a universal RTAA
  performance claim.", "disposition": "pending_inspection", "existing_record_ids":
  ["AIMech:AStarSearch"], "group": "rtaa", "index": 19, "kind": "bibliography", "next_check":
  "Read the original analysis and experiment assumptions before comparing algorithms.",
  "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/bibliography-occurrences.json",
  "sha256": "848e7655caa56ace8f6b1a9d7707f4f92e39a70425934c0b5d527d0ef6c8e29b"}, "original_sha256":
  "46ce26b84bdcf2f88465efddd56b75dc9c279a19daaae706d8d9deaad3aef3d3", "original_source_details":
  {"next_check": "Reconcile the exact source and purpose against a fresh inventory/frontier
  before further method-specific research or ownership changes; do not append one
  concept per citation."}, "pointer": "/occurrences/19", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "Wilt, C., and Ruml, W. 2011. Cost-based heuristic
  search\nis sensitive to the ratio of operator costs. In Proceedings of\nSoCS."}'
- '{"added_record_ids": [], "assessment": "The exact AAAI workshop URL remains an
  unacquired version route. The accepted AAMAS2006 artifact does not prove it identical.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "rtaa",
  "index": 0, "kind": "retrieval_only", "next_check": "Acquire https://cdn.aaai.org/Workshops/2006/WS-06-11/WS06-11-010.pdf
  and compare full content/version; retain any failed access.", "origin": {"path":
  "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256":
  "b4a15bdc388bbb15cfc0101af702665bebff0f2945687984591005186a1b2ef0", "original_source_details":
  {"scope": "Retrieved in search results; not acquired/read. Potential workshop version
  must not be assumed identical.", "url": "https://cdn.aaai.org/Workshops/2006/WS-06-11/WS06-11-010.pdf"},
  "pointer": "/retrieval_only_leads/0", "responsible_owner": {"family": "nested",
  "index": 393}, "text": "https://cdn.aaai.org/Workshops/2006/WS-06-11/WS06-11-010.pdf"}'
- '{"added_record_ids": [], "assessment": "The exact AAMAS2012 search route mentions
  depression-avoidance/incremental variants but remains unread; no method identity
  is asserted.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "rtaa", "index": 1, "kind": "retrieval_only", "next_check": "Acquire https://www.ifaamas.org/Proceedings/aamas2012/papers/1F_5.pdf
  and trace the original 2011 depression-avoidance reference before assessing variants.",
  "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256":
  "ce58720411ded2fc5b936f2f7d28813f36f5e1f1e3e80097b684951e632b0ae0", "original_source_details":
  {"scope": "Search-result bibliography mentions2011 RTAA depression avoidance and
  additional incremental variants. Full source unread, not an assessed new concept.",
  "url": "https://www.ifaamas.org/Proceedings/aamas2012/papers/1F_5.pdf"}, "pointer":
  "/retrieval_only_leads/1", "responsible_owner": {"family": "nested", "index": 393},
  "text": "https://www.ifaamas.org/Proceedings/aamas2012/papers/1F_5.pdf"}'
- '{"added_record_ids": ["AIMech:RealTimeAdaptiveAStar"], "assessment": "The defining
  2006 RTAA source and the exact historical 2018 URL have now been assessed in the
  accepted RTAA dossier/preview. The 2018 work is a scoped later comparison, with
  timing/caption/axis and thesis limits retained. Old uninspected statements stay
  historical provenance.", "disposition": "represented_by_added_record", "existing_record_ids":
  ["AIMech:LocalSearchSpaceLearningRealTimeAStar", "AIMech:AStarSearch"], "group":
  "rtaa", "index": 0, "kind": "original_owner_questions", "next_check": "After authorized
  creation verify the narrow RTAA record. Keep 2018 aggregation/thesis, earlier workshop
  route and all four other nested393 questions pending.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256":
  "ea1e4d8de8471d2c58024767ac87b356b4be63a524b0b4a0a44f97306a374a9d", "original_source_details":
  {"candidate": "RTAA*", "next_check": "Build its own current-state candidate/mapping
  dossier and check the historical 2018 RTAA URL’s relationship; do not treat either
  as already curated. Resolve the exact historical route https://www.cs.unh.edu/~ruml/papers/rtaa-star-socs18.pdf
  without assuming its content from its filename.", "source": "https://idm-lab.org/bib/abstracts/papers/aamas06.pdf"},
  "pointer": "/historical_nested393_questions/0", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "RTAA*"}'
- '{"added_record_ids": [], "assessment": "D* Lite and its Lifelong Planning A* relation
  remain independent incremental-search source responsibilities under nested393.",
  "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:AStarSearch",
  "AIMech:LocalSearchSpaceLearningRealTimeAStar"], "group": "rtaa", "index": 1, "kind":
  "original_owner_questions", "next_check": "Acquire the exact original and compare
  g/rhs repair, keys, updates and assumptions.", "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256":
  "04954b529332376f960c011f588eb8e5b12a43df65c6c12a4b463644f21eb627", "original_source_details":
  {"candidate": "D* Lite", "next_check": "Acquire original source and analyze incremental
  g/rhs repair, key/update conditions and relation to Lifelong Planning A*.", "source":
  "Koenig and Likhachev2002, AAAI,476–483; reference21 in primary manuscript"}, "pointer":
  "/historical_nested393_questions/1", "responsible_owner": {"family": "nested", "index":
  393}, "text": "D* Lite"}'
- '{"added_record_ids": [], "assessment": "The 2004 LSS predecessor remains an earlier-version/source-continuity
  question; the later LSS record is context, not proof of exact equality.", "disposition":
  "existing_pending_owner", "existing_record_ids": ["AIMech:LocalSearchSpaceLearningRealTimeAStar"],
  "group": "rtaa", "index": 2, "kind": "original_owner_questions", "next_check": "Acquire
  and compare the original naming, local-space learning and movement control.", "origin":
  {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256":
  "bcd4ee6fd17b5b78f1f98af159234164d3c41c7353a504132d2bd41dd2b5f2ff", "original_source_details":
  {"candidate": "LSS2004 predecessor source", "next_check": "Resolve earlier version
  and name/method continuity; retain as source follow-up under LSS rather than automatically
  inventing a separate concept.", "source": "Koenig2004, A comparison of fast search
  methods for real-time situated agents, AAMAS864–871; reference20"}, "pointer": "/historical_nested393_questions/2",
  "responsible_owner": {"family": "nested", "index": 393}, "text": "LSS2004 predecessor
  source"}'
- '{"added_record_ids": [], "assessment": "Adaptive A* remains the exact complete-search
  heuristic-learning source question, not resolved by truncated RTAA or ordinary A*.",
  "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:AStarSearch"],
  "group": "rtaa", "index": 3, "kind": "original_owner_questions", "next_check": "Read
  the 2005 original and compare complete versus truncated search/update assumptions.",
  "origin": {"path": "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256":
  "4708782da3fb7819c53d72cce242047069114a5e4f4cbac2bdb19948cbe92538", "original_source_details":
  {"candidate": "Adaptive A*", "next_check": "Assess repeated complete-search heuristic
  learning separately from real-time truncation and existing A* identity.", "source":
  "Koenig and Likhachev2005, Adaptive A* poster abstract, AAMAS1311–1312; RTAA reference7"},
  "pointer": "/historical_nested393_questions/3", "responsible_owner": {"family":
  "nested", "index": 393}, "text": "Adaptive A*"}'
- '{"added_record_ids": [], "assessment": "The Bulitko–Lee framework and concrete
  variants remain pending under nested393 with main8 as umbrella context. No family
  exhaustion follows from RTAA or LSS.", "disposition": "existing_pending_owner",
  "existing_record_ids": ["AIMech:LearningRealTimeAStar", "AIMech:RealTimeAStar",
  "AIMech:LocalSearchSpaceLearningRealTimeAStar"], "group": "rtaa", "index": 4, "kind":
  "original_owner_questions", "next_check": "Read the framework, reconcile the 2005/2006
  version and concrete variants against main8, LRTA* and RTA*.", "origin": {"path":
  "/private/tmp/aimech-rtaa-draft-preparation-20261016/source-accounting-continuity.json",
  "sha256": "6cdf9ba0f692c1fc7e183432bc6e9e127c8f7e4fcdaa5ea91665f6f7dd3ba3b6"}, "original_sha256":
  "607e681137e0bd1dce92689d508039c2bea19cfb5c7212c31833c671f9a7c2f5", "original_source_details":
  {"candidate": "Real-time heuristic-search variants and unifying framework", "next_check":
  "Inspect framework and reconcile its concrete variants with main 8 and maintained
  LRTA/RTA; no bulk novelty claim.", "source": "Bulitko and Lee2006, Learning in real-time
  search: A unifying framework, JAIR25:119–157; manuscript reference7"}, "pointer":
  "/historical_nested393_questions/4", "responsible_owner": {"family": "nested", "index":
  393}, "text": "Real-time heuristic-search variants and unifying framework"}'
- 'Exact inherited source scopes are recursively retained under predecessor_state/projection;
  actual 358 report {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T025054Z-mrec-sma-star-and-iterative-threshold-search.json",
  "sha256": "24cac330ffb11e5a38b61d5926488b5332040a1b908f2451697a619a4bf4528c"}. No
  original 402/404/406 closure or family exhaustion is asserted.'
- 'Inherited predecessor_historical_pointer_restorations: exact object SHA256 67987c357ad59ed7c61fbfae19a742f3b2c042ecddf348dd9d1e2aa3cffee62c;
  original source references remain inside predecessor_state/projection/predecessor_historical_pointer_restorations.'
- 'Inherited earlier_historical_pointer_restorations: exact object SHA256 d1e09f5c15b206b56a5f92cf17640f9e4a2849c090f307de50369e2107f307ed;
  original source references remain inside predecessor_state/projection/earlier_historical_pointer_restorations.'
- 'Inherited predecessor_deferred_historical_accounting_findings: exact object SHA256
  8dac593c15973c74e8173b68efd7f2b20257526aac1b29050f52cbd6b4ee6746; original source
  references remain inside predecessor_state/projection/predecessor_deferred_historical_accounting_findings.'
- 'Inherited predecessor_governance_provenance: exact object SHA256 c459ffad24e9967ce4eaa41ce66c0d8c882437c7fe4aa17626be5e9b79358bca;
  original source references remain inside predecessor_state/projection/predecessor_governance_provenance.'
- 'Inherited predecessor_source_followup_accounting: exact object SHA256 e4079c59c57a15a8953d277b346d4c05c96044860fd96f4614e49c38a7bad33d;
  original source references remain inside predecessor_state/projection/predecessor_source_followup_accounting.'
- 'Inherited predecessor_source_followup_audit: exact object SHA256 a90c635226f1823ab783ab7697d01081e6c8f9e3fd9d5ea98ac4b836494b6008;
  original source references remain inside predecessor_state/projection/predecessor_source_followup_audit.'
- 'Inherited predecessor_incidental_source_accounting: exact object SHA256 859f88842f9e932a6656ac9b9cea2130a29fca38d478c7cfa36d7a9ad48c5de3;
  original source references remain inside predecessor_state/projection/predecessor_incidental_source_accounting.'
- 'Inherited predecessor_incidental_source_audit: exact object SHA256 a90c635226f1823ab783ab7697d01081e6c8f9e3fd9d5ea98ac4b836494b6008;
  original source references remain inside predecessor_state/projection/predecessor_incidental_source_audit.'
- 'Inherited predecessor_search_source_followup_accounting: exact object SHA256 39845183ceba4019e3e05ac21518ca500dbf0ee55d5aa0a1ed4be55e0a905b82;
  original source references remain inside predecessor_state/projection/predecessor_search_source_followup_accounting.'
- 'Inherited predecessor_search_source_owner_contexts: exact object SHA256 df9f7ddcc44ce809fe00bb7dff4b3caad8847f88362d0a5f0e9906c8429c694c;
  original source references remain inside predecessor_state/projection/predecessor_search_source_owner_contexts.'
- 'Inherited predecessor_metadata_audit: exact object SHA256 926d11cb738cc4372c0ced24a943ed0dd31eccf7718f3005c565d099f6a7f954;
  original source references remain inside predecessor_state/projection/predecessor_metadata_audit.'
- 'Inherited original_355_write: exact object SHA256 4c72eb1a738a744162aa78398ebaf7d70cf368580730618004c4adcfc7dfe082;
  original source references remain inside predecessor_state/projection/original_355_write.'
- 'Inherited predecessor_ritter_source_accounting: exact object SHA256 c125f3d4f63f720af2f5f9f15187eb0714ee1a5833c385802f8e68d5ef06a56b;
  original source references remain inside predecessor_state/projection/predecessor_ritter_source_accounting.'
- 'Inherited predecessor_ritter_frontier_result: exact object SHA256 93544ff90dab74f51b6a5bcd54f9cbc19e935b89d361c0fcb3b29abbb1d6f81e;
  original source references remain inside predecessor_state/projection/predecessor_ritter_frontier_result.'
- 'Inherited predecessor_ritter_ownership_plan: exact object SHA256 60971b46989c3d32c8c27e2e2fd78b4cac3ad627909c27fb1e248d43390069fb;
  original source references remain inside predecessor_state/projection/predecessor_ritter_ownership_plan.'
- 'Inherited predecessor_ritter_ownership_acceptance: exact object SHA256 cc78b22f1671274bbd790aa0d0e1b5c8c51fcf00ef22084f621d3c5f4f1c74c4;
  original source references remain inside predecessor_state/projection/predecessor_ritter_ownership_acceptance.'
- 'Inherited predecessor_ritter_report: exact object SHA256 37feabf676ee7f0bed44e6709c87a4699096f4cd1c04e992d6891469893cebda;
  original source references remain inside predecessor_state/projection/predecessor_ritter_report.'
- 'Inherited predecessor_357_metadata_audit: exact object SHA256 b514b69445fa29bbc3b65ec32a3cf601ae57332d7b6b3500b71cea45a7605c89;
  original source references remain inside predecessor_state/projection/predecessor_357_metadata_audit.'
- 'Inherited memory_search_source_accounting: exact object SHA256 846af9efc9256f36d8862a9bae28f0ca67285803eb74cd13470300e95f5dd8b5;
  original source references remain inside predecessor_state/projection/memory_search_source_accounting.'
- 'Inherited frontier_result: exact object SHA256 ab60923bf613ba6988b967e82023a909cb3b6c51d9f831155f33886fe4d6732b;
  original source references remain inside predecessor_state/projection/frontier_result.'
- 'Inherited inherited_issue402_triage: exact object SHA256 4dbf034b0f801e9fdc48abee3eed26c21820384d36af6f5fb15c920ee6de25ed;
  original source references remain inside predecessor_state/projection/inherited_issue402_triage.'
- 'Actual owner-plan/frontier outcome: {"additional_source_question_count": 0, "bibliography_occurrences":
  125, "changed_main_indexes": [8, 909], "changed_nested_indexes": [393], "main":
  914, "nested": 394, "new_main_rows": 0, "new_nested_rows": 0}'
- 'Actual source accounting digest (sorted compact JSON UTF-8): 3457194f82c872a14e0fddf1b4f1beacd71593cff596b162a4d4f59ae6714d81'
- 'Actual historical/current identity changes: [{"id": "AIMech:AmortizedSteinVariationalGradientDescent",
  "field": "identity_notes", "historical": "The proposed scope is the generic differentiable
  stochastic-sampler training procedure that projects minibatch Stein output directions
  into shared sampler parameters. Neural samplers are explicitly documented implementations,
  not a required architecture. It differs from unamortized particle SVGD, Soft Q-learning
  as a control composite, NVIL/BBVI score estimators, wake-sleep procedures, flow-matching
  velocity regression and the unchanged ULA transition. Historical research copied
  790 native and 442 pinned AIO records while the observed checkout moved from cohort
  355 HEAD 5b240a558c8d4c440830183628a348b301d9226f to merged HEAD 917e850123890bd00e671353652fe53101f83bfb.
  Four ignored/hidden-inclusive roots yielded 31 distinct contents and 38 occurrences,
  previously read in full; normalization covered 4,888 ID/local-ID/name/alias/scoped-synonym
  occurrences with no exact candidate match. Eleven selected native scientific contexts,
  eight pinned AIO CLASS nodes and 66 incident edges were previously inspected. All
  913 main and 394 nested objects were recursively queried; selected complete owner
  bodies were read rather than every unmatched body. These are historical observations,
  not fresh current or future identity clearance. The source question was retained
  in historical main 909, whose seven original pending questions remain preserved
  without closure. Five additional application/umbrella questions are retained in
  the research dossier with future ownership unset. The 105 bibliography occurrences
  span three source versions and are not 105 concepts. The proposed ANN related mapping
  describes the documented neural-sampler implementation relationship; it is not exact
  equivalence, subclassing or a claim that every differentiable simulator is an ANN.",
  "current": "Current cohort359 assessment on clean base 0f7e2c5df224901e9284a883dfd0457fd4c29375:
  ignored-inclusive collection reconciles 1,239 AIO and maintained records and 4,913
  identity-field occurrences (3,753 normalized values), with no candidate-name/ID/alias
  collision. Root read388 ordinary matching contents; an independent reviewer reconciled
  eight large provenance wrappers and read their relevant source-question leaves.
  Bounded neighbor definitions distinguish this generic differentiable-sampler fitting
  component from direct SVGD, Soft Q-learning, ULA and score/ELBO estimators; this
  is not a global novelty claim. The accepted2016v2 and2017 defining sources, six
  claims, eight limitations and qualified ANN implementation-related mapping remain
  unchanged. Main909 is accepted as the exact original citation responsibility, with
  five application/umbrella followups explicitly assigned for tracking rather than
  asserted historical ownership. All105 bibliography occurrences and seven original
  source questions remain exact; the narrow component can be represented while application,
  version and other-original questions stay open. Earlier citation-only access statements
  remain historical, including separately prepared but not maintained SVPG.", "root_decision":
  "records/AIMech:AmortizedSteinVariationalGradientDescent/identity_notes"}, {"id":
  "AIMech:RealTimeAdaptiveAStar", "field": "identity_notes", "historical": "The proposed
  identity is the named 2006 Real-Time Adaptive A* algorithm with bounded forward
  A*, the CLOSED-only F−g heuristic update, and a separately chosen movement cap.
  It differs from ordinary A* as its embedded search, one-state LRTA*, second-best
  RTA*, and the reverse-Dijkstra learning phase of LSS-LRTA*. Equality with the paper’s
  2004 larger-lookahead LRTA comparator at lookahead one and identical ties is a special
  case, not general concept equivalence. The historical research snapshot at 2026-10-16T01:14:43Z–01:15:17Z
  observed cohort356 HEAD 917e850123890bd00e671353652fe53101f83bfb with uncommitted
  actual356 additions, 792 native and 442 pinned AIO records. Four ignored/hidden-inclusive
  roots, excluding Git administrative contents, yielded 34 distinct contents and 47
  occurrences previously read in full. Mechanical normalization covered 4,896 ID/local-ID/name/alias/scoped-synonym
  occurrences with no exact candidate match in that snapshot. Eight immediate native
  algorithm contexts plus DFID/IDA definition contexts, nine exact AIO CLASS nodes
  and 48 incident edges were assessed. All 913 main and 394 nested objects were recursively
  queried, with matching nested393 and complete broader main8 read; unrelated record
  definitions and unmatched frontier bodies were not all semantically reread. These
  are historical observations, not future identity clearance. The original RTAA source
  question remains preserved under historical nested393 within main8, alongside D*
  Lite, the LSS2004 predecessor, Adaptive A* and the Bulitko–Lee framework; main8
  also retains KBFS and multi-state commitment residuals. The 2018 route is now evidenced
  as a later comparison paper, not a second defining identity. Twenty bibliography
  occurrences and two retrieval-only leads remain source questions with no future
  owner assignment or novelty count. The weak proposed MachineLearningTask related
  mapping concerns persistent heuristic learning; it does not assert identity, subclassing
  or a reinforcement-learning model.", "current": "Current cohort359 assessment on
  clean base 0f7e2c5df224901e9284a883dfd0457fd4c29375: the same ignored-inclusive
  collection and attributed root/independent matching-content readings found no candidate
  identity collision in the1,239-record snapshot. Bounded current comparisons distinguish
  CLOSED-only F-minus-g heuristic repair and separately controlled movement from ordinary
  A*, basic LRTA*/RTA*, LSS reverse-Dijkstra learning and memory/threshold search.
  The accepted2006 defining source,2018 later-comparison artifact, eight claims, ten
  limitations and weak learning-task related mapping remain unchanged; the task class
  is not algorithm identity or subclass. Nested393 is the accepted exact source responsibility,
  with main8 retaining an umbrella cross-reference. All20 bibliography occurrences,
  five original questions and two retrieval routes remain exact. The current2018 reading
  advances the historical route question but retains timing aggregation, caption/axis
  and thesis limits; D* Lite/LPA, Adaptive A*, earlier LSS and framework/variant questions
  remain pending.", "root_decision": "records/AIMech:RealTimeAdaptiveAStar/identity_notes"}]'
```
