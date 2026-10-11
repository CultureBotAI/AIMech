# Scientific self-review of adaptive and tempered samplers

- Review: 20261011T074346Z-adaptive-and-tempered-sampling
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T07:42:29Z
- Finished UTC: 2026-10-11T07:43:46Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain six distinct adaptive and population-tempering algorithms with qualified AIO related mappings. No actionable defect remains in the assessed records; original-source access limitations and adaptive validity conditions are explicit. All remain DRAFT.

## Scope And Provenance

Six maintained adaptive Metropolis and fixed/adaptive population-tempering algorithms.

Selection: Exactly the six added IDs in the adaptive-and-tempered-sampling ledger; no sampling.
Coverage: full; 6 reviewed / 6 in the declared population.
Source: working_tree at Git base 55426b2f512def647c6bff14f3202ecf9805fe72.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AdaptiveMetropolis | data/curated/AdaptiveMetropolis.yaml | maintained | Adaptive Metropolis |
| AIMech:DelayedRejectionAdaptiveMetropolis | data/curated/DelayedRejectionAdaptiveMetropolis.yaml | maintained | Delayed-rejection adaptive Metropolis |
| AIMech:AdaptiveScalingMetropolis | data/curated/AdaptiveScalingMetropolis.yaml | maintained | Adaptive scaling Metropolis |
| AIMech:AdaptiveScalingWithinAdaptiveMetropolis | data/curated/AdaptiveScalingWithinAdaptiveMetropolis.yaml | maintained | Adaptive scaling within adaptive Metropolis |
| AIMech:ParallelTempering | data/curated/ParallelTempering.yaml | maintained | Parallel tempering |
| AIMech:AdaptiveParallelTempering | data/curated/AdaptiveParallelTempering.yaml | maintained | Adaptive parallel tempering |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:AdaptiveMetropolis, AIMech:DelayedRejectionAdaptiveMetropolis, AIMech:AdaptiveScalingMetropolis, AIMech:AdaptiveScalingWithinAdaptiveMetropolis, AIMech:ParallelTempering, AIMech:AdaptiveParallelTempering | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 51.57s<br>Checked 442 record(s); 0 failed.<br>Checked 187 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 36 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 36,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:AdaptiveMetropolis, AIMech:DelayedRejectionAdaptiveMetropolis, AIMech:AdaptiveScalingMetropolis, AIMech:AdaptiveScalingWithinAdaptiveMetropolis, AIMech:ParallelTempering, AIMech:AdaptiveParallelTempering | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Identity, mechanism, source scope, limitations and mapping

evidence: supported. Targets: AIMech:AdaptiveMetropolis.

This record identifies covariance adaptation from the full retained history, distinguished from a fixed random-walk kernel, finite sliding-window adaptation, scale-only tuning and RAM direction-based adaptation. The original empirical-covariance form and later recursive modifications share this core but differ in update timing and regularization. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 181 prior native IDs/names/aliases. Ignored-inclusive searches of both full checkouts found prior discovery leads, neighboring sampler discussions and unrelated author-name/environment substrings. Existing random-walk Metropolis, delayed-rejection, fixed symmetric delayed-rejection and RAM records were inspected; shared components do not make these procedures equivalent.

Start at a state with positive target density. In the original form, after an initial period with a chosen positive-definite C0, propose Y from N(X_(t−1), C_t), where C_t=s_d[Cov(X_0,...,X_(t−1))+epsilon I], epsilon&gt;0 and s_d&gt;0. The empirical covariance uses every retained state, with denominator t−1 for t available states; choose the adaptation start after at least two states. Accept with min(1,pi(Y)/pi(X_(t−1))) and otherwise repeat the old state. The fixed-covariance Metropolis rule is used at each iteration, but adapting C_t from the sampled history requires a separate validity argument. Limitations: The 2010 source explicitly analyzes a recursive modification, not an exact restatement of the original unbiased sample covariance. Its displayed outline also shifts the covariance index; the original timing is stated explicitly here. The original full-method text was read through a public indexed PDF. Direct download returned 403 and no visible page images were obtained; no original-PDF hash or visual inspection is claimed. The 2010 method pages were read and visually checked. The original bounded-support result and the later regular superexponential-tail results have different hypotheses. Neither licenses arbitrary targets or unrestricted adaptive variants. The usual dimension-based scale is a tuning heuristic under particular target assumptions, not a universal optimum. Empirical covariance estimation can be unsuitable for distributions without finite second moments. The sampled-state sequence alone is history dependent; invariant kernels at frozen settings do not by themselves prove adaptive convergence.

### Identity, mechanism, source scope, limitations and mapping

evidence: supported. Targets: AIMech:DelayedRejectionAdaptiveMetropolis.

DRAM combines two distinct mechanisms: retained-history covariance learning across iterations and reversed-path acceptance corrections for additional attempts after rejection. The inspected author implementation supplies the explicit Gaussian-stage realization; it is not merely repeated ordinary Metropolis tests. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 181 prior native IDs/names/aliases. Ignored-inclusive searches of both full checkouts found prior discovery leads, neighboring sampler discussions and unrelated author-name/environment substrings. Existing random-walk Metropolis, delayed-rejection, fixed symmetric delayed-rejection and RAM records were inspected; shared components do not make these procedures equivalent.

At fixed proposal settings for a transition, first propose y1 from N(x,C1) and use the Metropolis target ratio. After rejection propose y2 from N(x,C2), centered at the original x, with C2=C1/d1² for a positive stage scale d1 (d1&gt;1 narrows the proposal). Let q_i(a,b) denote the Gaussian proposal density at b from a and a1(a,b)=min(1,pi(b)/pi(a)). On a reachable rejection path, accept y2 with min(1, [pi(y2)q1(y2,y1)q2(y2,x)(1−a1(y2,y1))]/[pi(x)q1(x,y1)q2(x,y2)(1−a1(x,y1))]). Higher stages use the recursive forward/reverse rejection products and earlier-stage Gaussian proposal ratios. Retain x after all capped stages reject. At scheduled iterations, update the empirical covariance from stored retained states including repeats, scale its Cholesky factor, and recompute stage factors for later transitions. In the inspected implementation diagonal jitter is attempted only when factorization fails; if that attempt also fails, the previous proposal factor is retained. Limitations: The original 2006 article metadata was located but its complete method PDF was not obtained. This record is supported by the named author’s pinned implementation and its covariance helper, not a claim to have read that article. The Gaussian factors remain fixed within a delayed-rejection transition. Recomputing adaptation from rejected internal candidates or ignoring reverse-path factors would require different justification. The implementation defaults to two attempts and adaptation every 100 iterations; its usage comment about three stages is inconsistent with those executable defaults. These counts are options, not the concept identity. Optional covariance pseudoweights, fixed nonadapted coordinates, early rejection-rate scaling, variance sampling and hierarchical updates are outside the simple fixed-target account here. Jitter only on factorization failure differs from always adding a positive regularizer. Source-code inspection alone establishes neither correctness for arbitrary targets nor adaptive ergodicity; no MATLAB execution or performance comparison was performed. Initialize within positive target support. Zero reverse-path probability gives zero acceptance; numerical evaluation must handle vanishing densities and log ratios without invalid divisions.

### Identity, mechanism, source scope, limitations and mapping

evidence: supported. Targets: AIMech:AdaptiveScalingMetropolis.

The source’s ASM has fixed positive-definite shape and an adaptive scalar scale. This is distinct from covariance-shape adaptation and from RAM’s direction-dependent matrix update. The record uses the exponential-scale specialization of the source’s more general increasing scale map. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 181 prior native IDs/names/aliases. Ignored-inclusive searches of both full checkouts found prior discovery leads, neighboring sampler discussions and unrelated author-name/environment substrings. Existing random-walk Metropolis, delayed-rejection, fixed symmetric delayed-rejection and RAM records were inspected; shared components do not make these procedures equivalent.

Fix shape Sigma positive definite and use a spherical proposal W. From retained x with pi(x)&gt;0 and log scale S, propose Y=x+exp(S)Sigma^(1/2)W. Compute alpha=min(1,pi(Y)/pi(x)), accept Y with that probability or retain x, then update S_new=S+eta_n(alpha−alpha_star). Adapt after either outcome, using the acceptance probability rather than its Bernoulli realization. Choose alpha_star in (0,1) and positive step sizes with divergent sum and convergent sum of squares for the stated stochastic-approximation setting. The shape remains fixed; exp(S) multiplies standard deviation, so the covariance multiplier is exp(2S). Limitations: The stability and strong-law theorems in this version restrict alpha_star to (0,1/2), beyond the broader algorithm definition. Larger targets are discussed as expected extensions, not proved here. Compact-support regularity or the stated unbounded-target tail/contour assumptions and admissible proposal conditions are needed for the corresponding results. Positive step sizes alone are insufficient. The strong-law statements concern sample averages. The source explicitly distinguishes them from convergence in distribution of the adaptive sampled states. A target rate such as 0.234 is not a universal optimum, evidence of convergence or guarantee of good multimodal exploration. The inspected arXiv v3 submission date and later PDF footer differ; no later journal PDF inspection or numerical validation is claimed.

### Identity, mechanism, source scope, limitations and mapping

evidence: supported. Targets: AIMech:AdaptiveScalingWithinAdaptiveMetropolis.

This record gives the bounded mean-and-shape formulation of Vihola Definition 5. Its log scale is unbounded, while the proposed mean/shape pair is accepted only inside a specified compact constraint set. Unconstrained software variants are not automatically the same validity setting. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 181 prior native IDs/names/aliases. Ignored-inclusive searches of both full checkouts found prior discovery leads, neighboring sampler discussions and unrelated author-name/environment substrings. Existing random-walk Metropolis, delayed-rejection, fixed symmetric delayed-rejection and RAM records were inspected; shared components do not make these procedures equivalent.

Choose alpha_star in (0,1) and initialize x with pi(x)&gt;0, mu=x and feasible positive-definite Sigma. Propose Y=x+exp(S)Sigma^(1/2)W with spherical W, use alpha=min(1,pi(Y)/pi(x)), and retain X_new after the accept/reject test. Update S_new=S+eta_n(alpha−alpha_star). With the old mean mu and shape Sigma, form mu_hat=(1−eta_n)mu+eta_n X_new and Sigma_hat=(1−eta_n)Sigma+eta_n(X_new−mu)(X_new−mu)^T. For fixed zeta≥1, accept the entire proposed mean/shape pair only if &#124;&#124;mu_hat&#124;&#124;≤zeta and every eigenvalue of Sigma_hat lies in [zeta^−1,zeta]; otherwise keep both old mu and old Sigma. Start with a feasible mean/shape pair and keep the scalar update separately. Use eta_n in (0,1), with divergent sum and finite squared sum under the source assumptions. Limitations: The covariance update uses the old mean and the retained new state, including repeated states after rejection. Substituting the new mean or only accepted proposals changes the specified recursion. The mean and shape constraints are part of this source’s proved formulation; only the scalar scale lacks a fixed bound. Omitting constraints in practice does not inherit the same theorem. The source’s strong-law results restrict alpha_star to (0,1/2) and require the corresponding target/proposal regularity conditions. Algorithm definition alone does not prove ergodicity. Shape learning is a recursive stochastic-approximation update, not exactly the original unbiased full-history covariance at every finite iteration. No universal efficiency advantage, marginal-distribution convergence or executed benchmark is asserted.

### Identity, mechanism, source scope, limitations and mapping

evidence: supported. Targets: AIMech:ParallelTempering.

The record identifies fixed-temperature parallel tempering, with the source’s adjacent-swap and random-walk realization as an explicit example. The population state includes all replicas; the beta=1 replica targets the original distribution. It differs from a single-chain simulated-temperature state and from adapting the temperature ladder. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 181 prior native IDs/names/aliases. Ignored-inclusive searches of both full checkouts found prior discovery leads, neighboring sampler discussions and unrelated author-name/environment substrings. Existing random-walk Metropolis, delayed-rejection, fixed symmetric delayed-rejection and RAM records were inspected; shared components do not make these procedures equivalent.

Choose a fixed L≥2 and inverse temperatures 1=beta1&gt;...&gt;betaL&gt;0 for which each integral Z_beta=integral pi(x)^beta dx is finite. Initialize replicas in positive target support. The joint target is the product of pi(x_l)^beta_l/Z_beta_l. In the inspected realization, choose j uniformly from adjacent pairs and propose swapping x_j and x_(j+1), with probability min(1,[pi(x_(j+1))/pi(x_j)]^(beta_j−beta_(j+1))). Then apply a Gaussian random-walk Metropolis update at every level using acceptance min(1,[pi(y_l)/pi(x_l)]^beta_l); rejected moves retain their current replica state. Both steps preserve the joint target, so their composition does also; samples at beta1=1 have the desired stationary marginal. Limitations: All tempered densities must be normalizable; flattening a target by taking a positive power below one need not preserve integrability. Target invariance alone does not establish irreducibility, mixing speed, finite-run convergence or independence of cold-replica samples. The source calls the composed chain reversible. Composition of two reversible kernels need not be reversible without additional conditions; this record asserts only their directly justified invariance. The original distribution is the cold replica’s marginal, not the pooled unweighted population distribution. Other valid local kernels and exchange schedules require their own conditions. The record’s explicit Gaussian and adjacent-swap realization is not a claim that all implementations use it.

### Identity, mechanism, source scope, limitations and mapping

evidence: supported. Targets: AIMech:AdaptiveParallelTempering.

This record is the fixed-replica-count Miasojedow–Moulines–Vihola 2012 construction. Its multiplicative inverse-temperature parameterization and all-pair swap-probability updates differ from later author software using increments of reciprocal temperatures and updates for selected pairs. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 181 prior native IDs/names/aliases. Ignored-inclusive searches of both full checkouts found prior discovery leads, neighboring sampler discussions and unrelated author-name/environment substrings. Existing random-walk Metropolis, delayed-rejection, fixed symmetric delayed-rejection and RAM records were inspected; shared components do not make these procedures equivalent.

With fixed L≥2, alpha_star in (0,1) and epsilon in (0,1), set beta1=1 and beta_(l+1)=beta_l exp(−exp(rho_l)). Initialize within the parameter constraint sets and positive target support. At each iteration use the previous temperatures and proposal covariances for an adjacent exchange followed by local Gaussian Metropolis moves. From the retained post-propagation population X_new, compute every adjacent hypothetical exchange probability h_l=min(1,[pi(X_(l+1))/pi(X_l)]^(beta_l−beta_(l+1))). Update each rho_l by projection of rho_l+gamma1_n(h_l−alpha_star) onto a fixed finite interval. For each replica update mu_l=(1−gamma2_n)mu_l+gamma2_n X_new,l, and project (1−gamma2_n)Gamma_l+gamma2_n(X_new,l−mu_old,l)(X_new,l−mu_old,l)^T onto matrices with eigenvalues in [epsilon,epsilon^−1]. Update T_l by interval projection of T_l+gamma3_n(alpha_local,l−alpha_star), where alpha_local is that iteration’s local proposal acceptance probability. Use Sigma_l=exp(T_l)Gamma_l for later Gaussian proposals. Thus T is log variance, not log standard deviation; all adaptation follows the completed transition. Limitations: The record uses projected covariance and log-scale adaptation with separate step sequences; the mean recursion itself is not projected. Finite rho bounds keep ordered positive inverse temperatures, and the replica count is fixed. Every rho update uses a hypothetical adjacent swap probability at the post-propagation state, not just the pair actually selected or a binary swap outcome. The strong-law and temperature-convergence results have different hypotheses. Temperature convergence additionally needs stronger step conditions and the target solution inside the projection bounds; projection alone does not guarantee the desired rate is attainable. The continuous-target results assume the stated tail/contour, moment and step-size conditions. Experiments omitting projections do not prove unrestricted adaptive validity. The optional RAM proposal variant in Section 2.3 uses a physical increment where the original RAM paper uses a standardized proposal direction. That variant is excluded here; the covariance-based construction is the inspected core. No changing-replica-count method, unrestricted adaptive convergence, universal efficiency claim or benchmark reproduction is asserted.

### Accumulated covariance and within-transition retries

scope: supported. Targets: AIMech:AdaptiveMetropolis, AIMech:DelayedRejectionAdaptiveMetropolis.

Retain AM and its delayed-rejection combination as distinct scopes, preserving source-version limits.

Original AM indexed method text supplies the unbiased covariance over retained states and always-positive jitter; the 2010 visual page makes its different recursive modification explicit. The DRAM author code keeps the Gaussian factors fixed within each transition, centers later candidates on the original state, recursively corrects reverse rejection paths, and stores the original state after complete rejection. covupd receives stored states and computes empirical covariance. Its jitter fallback and stage defaults are implementation-specific and are stated, not silently substituted into original AM. q2 symmetry cancels its ratio in the shown two-stage specialization, while q1 and rejected-path probabilities remain. No original DRAM article reading or general adaptive ergodicity proof is claimed.

### ASM and constrained ASWAM update boundaries

scope: supported. Targets: AIMech:AdaptiveScalingMetropolis, AIMech:AdaptiveScalingWithinAdaptiveMetropolis.

Retain scalar-only adaptation and coupled scalar/shape adaptation.

Visually rechecked Definitions 4–5 and the compact mean/shape constraint. Both methods adapt from the proposal acceptance probability after either outcome; exp(S) scales standard deviation. ASWAM covariance uses retained X_new and old mean, and rejects the whole candidate mean/shape pair outside S_zeta while keeping the scalar update. The stated positive steps are a supported specialization of nonnegative steps; the record does not conflate the broad target-rate definition with the theorems restricted to alpha_star below one half. Strong-law averages are not asserted to imply marginal convergence.

### Fixed and projected adaptive temperature ladders

scope: supported. Targets: AIMech:ParallelTempering, AIMech:AdaptiveParallelTempering.

Retain fixed-ladder PT and the specified 2012 adaptive construction.

Visually rechecked swap Equation (9), multiplicative ladder Equation (13), all-pair projected update (14) and shape/mean/log-variance equations (18)–(21). The adjacent-swap ratio has the cold-minus-hot exponent. Fixed swap and local kernels preserve the product target; their composition need not inherit reversibility, so the record makes only the invariant-law claim. APT uses every hypothetical adjacent exchange probability at the retained post-propagation state, old means in covariance updates, finite interval projections and exp(T) as a variance multiplier. The evolving joint target and fixed cold marginal are explicit. Strong-law and temperature-root convergence hypotheses differ; no removal of projections or changing replica count is inferred.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:AdaptiveMetropolis, AIMech:DelayedRejectionAdaptiveMetropolis, AIMech:AdaptiveScalingMetropolis, AIMech:AdaptiveScalingWithinAdaptiveMetropolis, AIMech:ParallelTempering, AIMech:AdaptiveParallelTempering. Retain original retained-history covariance adaptation, its delayed-rejection combination, scalar-only acceptance adaptation, bounded recursive shape/scale adaptation, fixed-temperature population exchange and the specified projected adaptive ladder. These differ in state and update construction. Frozen-kernel related mappings preserve algorithm/process and adaptive-history distinctions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T074108Z-adaptive-and-tempered-sampling.json | supports | No normalized match among 442 AIO labels/all scoped synonyms and 181 native IDs/names/aliases. Both full checkouts were searched including ignored and hidden files. The 112 discovery and 121 main text hits are prior research/review/history references, neighboring RAM/delayed-rejection discussion, the unrelated author name Krishnaswamy, and nine main-environment substrings such as dramatic/drama and a public CA certificate. Existing sampler definitions and mechanism claims were inspected and remain distinct. |
| mapping | sources/aio/aio.json; Exact MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction CLASS nodes and incident edges | supports | Exact MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction CLASS nodes and incident edges were read. The six method-to-process related mappings do not assert network subclasses. Adaptive records explicitly map through frozen kernels and do not assert homogeneous Markov behavior for sampled-state history. PT uses the complete replica population. APT notes that the frozen joint target changes with the ladder while its cold marginal is pi. No AIO pin or generated record changed. |
| neighbor-samplers | data/curated/RobustAdaptiveMetropolis.yaml; Definitions, identity notes, claims and mappings in RAM, RandomWalkMetropolisHastings, DelayedRejectionMetropolis and SymmetricDelayedRejection | supports | The neighboring records separate fixed additive random walks, within-transition rejected paths and direction-dependent RAM shape updates. The new records add accumulated covariance, scalar acceptance-rate adaptation and replica-temperature population constructions; component overlap is not identity. |
| adaptivemetropolis-source | https://arxiv.org/pdf/0806.2933v5; Section 5, Equations (26)–(30), PDF pp. 14–15, and Theorem 10, pp. 15–16; compare original 2001 Section 2, Equations (1)–(2), printed pp. 224–226 | supports | A history-adaptive random-walk Metropolis sampler whose Gaussian proposal covariance is estimated from the accumulated retained states, including repetitions after rejected proposals. Version: arXiv:0806.2933v5, submitted 2010-11-11; electronic reprint of Annals of Applied Probability 20(6), pp. 2178–2203; reprint pagination differs. Text pages read: 1, 2, 3, 4, 5, 14, 15, 16, 23. Actual image pages viewed: 14, 15. For DRAM, inspected pinned mcmcrun code ranges and complete covupd helper instead of the unavailable original article. No executed benchmark. |
| adaptivemetropolis-source-1 | https://scispace.com/pdf/an-adaptive-metropolis-algorithm-4puhyontsn.pdf; Sections 1–2, Equations (1)–(2), printed pp. 223–226 / PDF pp. 1–4; Section 3 Theorem 1, printed p. 229 / PDF p. 7 | supports | Additional inspected method evidence: An adaptive Metropolis algorithm. Bernoulli 7(2), 2001, pp. 223–242; indexed full-method text, no local PDF or visual inspection. Original AM uses web-extracted full-method text with no visible page image or local hash; the covariance helper was read in full. |
| delayedrejectionadaptivemetropolis-source | https://raw.githubusercontent.com/mjlaine/mcmcstat/ca0cbd288f03c7a29050b3d6698a96b45ccfa4b2/mcmcrun.m; mcmcrun.m lines 119–168 (method controls), 339–380 (factors), 497–603 (proposals and retained chain), 661–717 (covariance adaptation), 854–905 (alphafun, qfun, lfun) | supports | An adaptive Metropolis procedure combining history-based Gaussian proposal covariance updates between transitions with corrected delayed-rejection proposal stages within a transition. Version: mjlaine/mcmcstat commit ca0cbd288f03c7a29050b3d6698a96b45ccfa4b2. Text pages read: . Actual image pages viewed: . For DRAM, inspected pinned mcmcrun code ranges and complete covupd helper instead of the unavailable original article. No executed benchmark. |
| delayedrejectionadaptivemetropolis-source-1 | https://raw.githubusercontent.com/mjlaine/mcmcstat/ca0cbd288f03c7a29050b3d6698a96b45ccfa4b2/covupd.m; covupd.m complete function: weighted mean and unbiased empirical covariance updates, including old-state accumulation | supports | Additional inspected method evidence: MCMCSTAT covupd: recursive weighted empirical covariance. mjlaine/mcmcstat commit ca0cbd288f03c7a29050b3d6698a96b45ccfa4b2. Original AM uses web-extracted full-method text with no visible page image or local hash; the covariance helper was read in full. |
| adaptivescalingmetropolis-source | https://arxiv.org/pdf/0903.4061v3; Section 2, Assumptions 1–3 and Definition 4, PDF pp. 3–4; Theorems 7 and 9 and Remarks 11–13, pp. 5–7 | supports | A random-walk Metropolis algorithm that adapts its proposal scale through stochastic approximation driven by the proposal acceptance probability relative to a chosen target rate. Version: arXiv:0903.4061v3, submitted 2011-04-05; 24-page PDF with footer dated 2022-03-01. Text pages read: 1, 2, 3, 4, 5, 6, 7, 19, 20, 21, 22, 23, 24. Actual image pages viewed: 4, 5. For DRAM, inspected pinned mcmcrun code ranges and complete covupd helper instead of the unavailable original article. No executed benchmark. |
| adaptivescalingwithinadaptivemetropolis-source | https://arxiv.org/pdf/0903.4061v3; Section 2, Definitions 4–5 and constraint set S_zeta, PDF pp. 4–5; Theorems 7 and 9, Remarks 11–13, pp. 5–7 | supports | An adaptive Metropolis algorithm that combines acceptance-rate-driven scalar proposal scaling with recursive mean and covariance-shape adaptation from retained samples. Version: arXiv:0903.4061v3, submitted 2011-04-05; 24-page PDF with footer dated 2022-03-01. Text pages read: 1, 2, 3, 4, 5, 6, 7, 19, 20, 21, 22, 23, 24. Actual image pages viewed: 4, 5. For DRAM, inspected pinned mcmcrun code ranges and complete covupd helper instead of the unavailable original article. No executed benchmark. |
| paralleltempering-source | https://arxiv.org/pdf/1205.1076v1; Sections 1–2.1, Equations (1)–(10), PDF pp. 1–4; Section 2.4 implementation remarks, p. 7 | supports | A population Monte Carlo method that combines within-temperature target-preserving updates with corrected exchanges between replicas targeting differently tempered densities. Version: arXiv:1205.1076v1, submitted 2012-05-04; 33-page preprint. Text pages read: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30, 31, 32, 33. Actual image pages viewed: 4, 5, 6. For DRAM, inspected pinned mcmcrun code ranges and complete covupd helper instead of the unavailable original article. No executed benchmark. |
| adaptiveparalleltempering-source | https://arxiv.org/pdf/1205.1076v1; Sections 2.1–2.3, Equations (1)–(24), PDF pp. 3–6; assumptions A1–A3 and Theorems 5 and 10, pp. 8–11 | supports | A parallel-tempering algorithm that adapts temperature gaps and within-replica random-walk proposal parameters through projected stochastic approximation. Version: arXiv:1205.1076v1, submitted 2012-05-04; 33-page preprint. Text pages read: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30, 31, 32, 33. Actual image pages viewed: 4, 5, 6. For DRAM, inspected pinned mcmcrun code ranges and complete covupd helper instead of the unavailable original article. No executed benchmark. |

## Limits And Additional Notes

- Adversarial author self-review only; all six records remain DRAFT.
- AM original full-method text was available but page images and local bytes were not; the later primary treatment was visually checked.
- DRAM is supported by pinned author source code and covariance helper, not the unavailable original full article; no MATLAB execution occurred.
- Only declared source text, image pages and code ranges were read.
- Later author documentation differences are recorded as version boundaries; its code was not executed or treated as identical to the 2012 APT method.
- No generic adaptive convergence, universal performance or finite-run sampling accuracy is certified.
- Required local and vendor checks passed; positive discoveries and remaining broad-AI leads mean the discovery goal remains active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T074346Z-adaptive-and-tempered-sampling
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of adaptive and tempered samplers
started_at: '2026-10-11T07:42:29Z'
finished_at: '2026-10-11T07:43:46Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all six actual YAMLs
    against primary method text, visible equations, pinned author implementation,
    neighboring native records and exact AIO mapping targets. No independent reviewer
    or approval is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain six distinct adaptive and population-tempering algorithms with qualified
  AIO related mappings. No actionable defect remains in the assessed records; original-source
  access limitations and adaptive validity conditions are explicit. All remain DRAFT.
source:
  git_revision: 55426b2f512def647c6bff14f3202ecf9805fe72
  state: working_tree
  inputs:
  - path: data/curated/AdaptiveMetropolis.yaml
    sha256: 16ffdea654024fefa0315e7f7982bda369f62d494e15a9d34b1a038d28e766d1
    role: target
  - path: data/curated/AdaptiveParallelTempering.yaml
    sha256: 8a48fc4748f3d3ae3ee1a488986db3ac1f016215ed28b78d44346a841154a919
    role: target
  - path: data/curated/AdaptiveScalingMetropolis.yaml
    sha256: e5afb420108326b017fba1a97e0131ce81e4ff2981aecd2742cfe39194c41e00
    role: target
  - path: data/curated/AdaptiveScalingWithinAdaptiveMetropolis.yaml
    sha256: 47db2a7de64b4128b16b74d02c57bc22347a90d01cf63c0ad7f05549af1f4a6e
    role: target
  - path: data/curated/DelayedRejectionAdaptiveMetropolis.yaml
    sha256: aac75fff730e2c2b6c35c348dc5a20607cb78812dcf011be6f7575e1992cb2b4
    role: target
  - path: data/curated/DelayedRejectionMetropolis.yaml
    sha256: c6a2c94f7bde235ed1a79ff91fbf615920ff3d5710c1e6f90769648ad403c8cd
    role: context
  - path: data/curated/ParallelTempering.yaml
    sha256: e2976bcbbe756cf1b943520c6c9d739b862213c2df4ab4f2806957b67db8d0eb
    role: target
  - path: data/curated/RandomWalkMetropolisHastings.yaml
    sha256: aeff822517db546b4e3dee3421a54d5887ed178f3b9e6e3df46283eceb39677d
    role: context
  - path: data/curated/RobustAdaptiveMetropolis.yaml
    sha256: 5f0feccd0c8d7eda90fabacbc27e1a98cf2582e865081190bb1c3955d4db04f4
    role: context
  - path: data/curated/SymmetricDelayedRejection.yaml
    sha256: e4cb88db36220fe96e697d8b3d42bbdb34e27f8a9a5886a901d299686e389281
    role: context
  - path: research/discovery/20261011T074108Z-adaptive-and-tempered-sampling.json
    sha256: d259f716e6e97deb0eb15c4889eab5c3356d835bef88e61c57c7952d195c5f14
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
- target_id: AIMech:AdaptiveMetropolis
  path: data/curated/AdaptiveMetropolis.yaml
  label: Adaptive Metropolis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AdaptiveMetropolis.yaml
    role: maintained
- target_id: AIMech:DelayedRejectionAdaptiveMetropolis
  path: data/curated/DelayedRejectionAdaptiveMetropolis.yaml
  label: Delayed-rejection adaptive Metropolis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DelayedRejectionAdaptiveMetropolis.yaml
    role: maintained
- target_id: AIMech:AdaptiveScalingMetropolis
  path: data/curated/AdaptiveScalingMetropolis.yaml
  label: Adaptive scaling Metropolis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AdaptiveScalingMetropolis.yaml
    role: maintained
- target_id: AIMech:AdaptiveScalingWithinAdaptiveMetropolis
  path: data/curated/AdaptiveScalingWithinAdaptiveMetropolis.yaml
  label: Adaptive scaling within adaptive Metropolis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AdaptiveScalingWithinAdaptiveMetropolis.yaml
    role: maintained
- target_id: AIMech:ParallelTempering
  path: data/curated/ParallelTempering.yaml
  label: Parallel tempering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ParallelTempering.yaml
    role: maintained
- target_id: AIMech:AdaptiveParallelTempering
  path: data/curated/AdaptiveParallelTempering.yaml
  label: Adaptive parallel tempering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AdaptiveParallelTempering.yaml
    role: maintained
scope:
  description: Six maintained adaptive Metropolis and fixed/adaptive population-tempering
    algorithms.
  selection: Exactly the six added IDs in the adaptive-and-tempered-sampling ledger;
    no sampling.
  coverage: full
  population_size: 6
  reviewed_target_ids:
  - AIMech:AdaptiveMetropolis
  - AIMech:DelayedRejectionAdaptiveMetropolis
  - AIMech:AdaptiveScalingMetropolis
  - AIMech:AdaptiveScalingWithinAdaptiveMetropolis
  - AIMech:ParallelTempering
  - AIMech:AdaptiveParallelTempering
  exclusions:
  - target: Original DRAM article and original AM page images
    reason: Direct source access remained incomplete; record evidence and scope state
      the available full-method text/implementation instead.
  - target: Rao-Blackwellized AM, alternate APT parameterizations, simulated tempering
      and Wang–Landau
    reason: These methods require separate source inspection and identity assessment.
  - target: Sampler execution and benchmark reproduction
    reason: No implementation or numerical experiment was run.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:AdaptiveMetropolis
  - AIMech:DelayedRejectionAdaptiveMetropolis
  - AIMech:AdaptiveScalingMetropolis
  - AIMech:AdaptiveScalingWithinAdaptiveMetropolis
  - AIMech:ParallelTempering
  - AIMech:AdaptiveParallelTempering
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 51.57s\nChecked 442 record(s); 0 failed.\n\
    Checked 187 curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing,\
    \ 0 changed, 0 unexpected.\nChecked 36 history record(s); 0 error(s).\n{\n  \"\
    repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 36,\n  \"coverage\"\
    : \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:AdaptiveMetropolis
  - AIMech:DelayedRejectionAdaptiveMetropolis
  - AIMech:AdaptiveScalingMetropolis
  - AIMech:AdaptiveScalingWithinAdaptiveMetropolis
  - AIMech:ParallelTempering
  - AIMech:AdaptiveParallelTempering
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T074108Z-adaptive-and-tempered-sampling.json
  accessed_at: '2026-10-11T07:42:29Z'
  support: supports
  summary: No normalized match among 442 AIO labels/all scoped synonyms and 181 native
    IDs/names/aliases. Both full checkouts were searched including ignored and hidden
    files. The 112 discovery and 121 main text hits are prior research/review/history
    references, neighboring RAM/delayed-rejection discussion, the unrelated author
    name Krishnaswamy, and nine main-environment substrings such as dramatic/drama
    and a public CA certificate. Existing sampler definitions and mechanism claims
    were inspected and remain distinct.
  search_scope: All 442 AIO labels/all scoped synonyms and 181 preceding native IDs/names/aliases;
    full searches of both checkouts included ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-11T07:42:29Z'
  support: supports
  locator: Exact MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction
    CLASS nodes and incident edges
  summary: Exact MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction
    CLASS nodes and incident edges were read. The six method-to-process related mappings
    do not assert network subclasses. Adaptive records explicitly map through frozen
    kernels and do not assert homogeneous Markov behavior for sampled-state history.
    PT uses the complete replica population. APT notes that the frozen joint target
    changes with the ladder while its cold marginal is pi. No AIO pin or generated
    record changed.
- evidence_id: neighbor-samplers
  kind: record_content
  reference: data/curated/RobustAdaptiveMetropolis.yaml
  accessed_at: '2026-10-11T07:42:29Z'
  support: supports
  locator: Definitions, identity notes, claims and mappings in RAM, RandomWalkMetropolisHastings,
    DelayedRejectionMetropolis and SymmetricDelayedRejection
  summary: The neighboring records separate fixed additive random walks, within-transition
    rejected paths and direction-dependent RAM shape updates. The new records add
    accumulated covariance, scalar acceptance-rate adaptation and replica-temperature
    population constructions; component overlap is not identity.
- evidence_id: adaptivemetropolis-source
  kind: primary_source
  reference: https://arxiv.org/pdf/0806.2933v5
  locator: Section 5, Equations (26)–(30), PDF pp. 14–15, and Theorem 10, pp. 15–16;
    compare original 2001 Section 2, Equations (1)–(2), printed pp. 224–226
  accessed_at: '2026-10-11T07:30:43Z'
  snapshot_sha256: 87ccd3ec1113574209f86d03781984bff2defb347a44c653b69a3f53f11dc46d
  support: supports
  summary: 'A history-adaptive random-walk Metropolis sampler whose Gaussian proposal
    covariance is estimated from the accumulated retained states, including repetitions
    after rejected proposals. Version: arXiv:0806.2933v5, submitted 2010-11-11; electronic
    reprint of Annals of Applied Probability 20(6), pp. 2178–2203; reprint pagination
    differs. Text pages read: 1, 2, 3, 4, 5, 14, 15, 16, 23. Actual image pages viewed:
    14, 15. For DRAM, inspected pinned mcmcrun code ranges and complete covupd helper
    instead of the unavailable original article. No executed benchmark.'
- evidence_id: adaptivemetropolis-source-1
  kind: primary_source
  reference: https://scispace.com/pdf/an-adaptive-metropolis-algorithm-4puhyontsn.pdf
  locator: Sections 1–2, Equations (1)–(2), printed pp. 223–226 / PDF pp. 1–4; Section
    3 Theorem 1, printed p. 229 / PDF p. 7
  accessed_at: '2026-10-11T07:33:36Z'
  support: supports
  summary: 'Additional inspected method evidence: An adaptive Metropolis algorithm.
    Bernoulli 7(2), 2001, pp. 223–242; indexed full-method text, no local PDF or visual
    inspection. Original AM uses web-extracted full-method text with no visible page
    image or local hash; the covariance helper was read in full.'
- evidence_id: delayedrejectionadaptivemetropolis-source
  kind: primary_source
  reference: https://raw.githubusercontent.com/mjlaine/mcmcstat/ca0cbd288f03c7a29050b3d6698a96b45ccfa4b2/mcmcrun.m
  locator: mcmcrun.m lines 119–168 (method controls), 339–380 (factors), 497–603 (proposals
    and retained chain), 661–717 (covariance adaptation), 854–905 (alphafun, qfun,
    lfun)
  accessed_at: '2026-10-11T07:35:25Z'
  snapshot_sha256: d665a2f3bd6df31ae576472f0ea18b48f65f2b08393f1cdeda5d1b8b6ad037e6
  support: supports
  summary: 'An adaptive Metropolis procedure combining history-based Gaussian proposal
    covariance updates between transitions with corrected delayed-rejection proposal
    stages within a transition. Version: mjlaine/mcmcstat commit ca0cbd288f03c7a29050b3d6698a96b45ccfa4b2.
    Text pages read: . Actual image pages viewed: . For DRAM, inspected pinned mcmcrun
    code ranges and complete covupd helper instead of the unavailable original article.
    No executed benchmark.'
- evidence_id: delayedrejectionadaptivemetropolis-source-1
  kind: primary_source
  reference: https://raw.githubusercontent.com/mjlaine/mcmcstat/ca0cbd288f03c7a29050b3d6698a96b45ccfa4b2/covupd.m
  locator: 'covupd.m complete function: weighted mean and unbiased empirical covariance
    updates, including old-state accumulation'
  accessed_at: '2026-10-11T07:35:25Z'
  support: supports
  summary: 'Additional inspected method evidence: MCMCSTAT covupd: recursive weighted
    empirical covariance. mjlaine/mcmcstat commit ca0cbd288f03c7a29050b3d6698a96b45ccfa4b2.
    Original AM uses web-extracted full-method text with no visible page image or
    local hash; the covariance helper was read in full.'
  snapshot_sha256: 7663509eccba2f93a0a667d056ff8e4745829343996244aeac35cc8aa0f597ab
- evidence_id: adaptivescalingmetropolis-source
  kind: primary_source
  reference: https://arxiv.org/pdf/0903.4061v3
  locator: Section 2, Assumptions 1–3 and Definition 4, PDF pp. 3–4; Theorems 7 and
    9 and Remarks 11–13, pp. 5–7
  accessed_at: '2026-10-11T07:30:43Z'
  snapshot_sha256: 2de1293c2ed1d1bff38cd97b3a03c5013a420dc92f418a0230edced2a4fbc1f9
  support: supports
  summary: 'A random-walk Metropolis algorithm that adapts its proposal scale through
    stochastic approximation driven by the proposal acceptance probability relative
    to a chosen target rate. Version: arXiv:0903.4061v3, submitted 2011-04-05; 24-page
    PDF with footer dated 2022-03-01. Text pages read: 1, 2, 3, 4, 5, 6, 7, 19, 20,
    21, 22, 23, 24. Actual image pages viewed: 4, 5. For DRAM, inspected pinned mcmcrun
    code ranges and complete covupd helper instead of the unavailable original article.
    No executed benchmark.'
- evidence_id: adaptivescalingwithinadaptivemetropolis-source
  kind: primary_source
  reference: https://arxiv.org/pdf/0903.4061v3
  locator: Section 2, Definitions 4–5 and constraint set S_zeta, PDF pp. 4–5; Theorems
    7 and 9, Remarks 11–13, pp. 5–7
  accessed_at: '2026-10-11T07:30:43Z'
  snapshot_sha256: 2de1293c2ed1d1bff38cd97b3a03c5013a420dc92f418a0230edced2a4fbc1f9
  support: supports
  summary: 'An adaptive Metropolis algorithm that combines acceptance-rate-driven
    scalar proposal scaling with recursive mean and covariance-shape adaptation from
    retained samples. Version: arXiv:0903.4061v3, submitted 2011-04-05; 24-page PDF
    with footer dated 2022-03-01. Text pages read: 1, 2, 3, 4, 5, 6, 7, 19, 20, 21,
    22, 23, 24. Actual image pages viewed: 4, 5. For DRAM, inspected pinned mcmcrun
    code ranges and complete covupd helper instead of the unavailable original article.
    No executed benchmark.'
- evidence_id: paralleltempering-source
  kind: primary_source
  reference: https://arxiv.org/pdf/1205.1076v1
  locator: Sections 1–2.1, Equations (1)–(10), PDF pp. 1–4; Section 2.4 implementation
    remarks, p. 7
  accessed_at: '2026-10-11T07:31:49Z'
  snapshot_sha256: 4c0f3ba8a5a8dcf5001e1c95954638ab43790ba6eeb2abf72db367c0495d3af8
  support: supports
  summary: 'A population Monte Carlo method that combines within-temperature target-preserving
    updates with corrected exchanges between replicas targeting differently tempered
    densities. Version: arXiv:1205.1076v1, submitted 2012-05-04; 33-page preprint.
    Text pages read: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30, 31, 32,
    33. Actual image pages viewed: 4, 5, 6. For DRAM, inspected pinned mcmcrun code
    ranges and complete covupd helper instead of the unavailable original article.
    No executed benchmark.'
- evidence_id: adaptiveparalleltempering-source
  kind: primary_source
  reference: https://arxiv.org/pdf/1205.1076v1
  locator: Sections 2.1–2.3, Equations (1)–(24), PDF pp. 3–6; assumptions A1–A3 and
    Theorems 5 and 10, pp. 8–11
  accessed_at: '2026-10-11T07:31:49Z'
  snapshot_sha256: 4c0f3ba8a5a8dcf5001e1c95954638ab43790ba6eeb2abf72db367c0495d3af8
  support: supports
  summary: 'A parallel-tempering algorithm that adapts temperature gaps and within-replica
    random-walk proposal parameters through projected stochastic approximation. Version:
    arXiv:1205.1076v1, submitted 2012-05-04; 33-page preprint. Text pages read: 1,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30, 31, 32, 33. Actual image pages
    viewed: 4, 5, 6. For DRAM, inspected pinned mcmcrun code ranges and complete covupd
    helper instead of the unavailable original article. No executed benchmark.'
assessments:
- assessment_id: adaptivemetropolis
  area: evidence
  topic: Identity, mechanism, source scope, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:AdaptiveMetropolis
  evidence_ids:
  - identity
  - mapping
  - neighbor-samplers
  - adaptivemetropolis-source
  - adaptivemetropolis-source-1
  summary: This record identifies covariance adaptation from the full retained history,
    distinguished from a fixed random-walk kernel, finite sliding-window adaptation,
    scale-only tuning and RAM direction-based adaptation. The original empirical-covariance
    form and later recursive modifications share this core but differ in update timing
    and regularization. No normalized identity match was found across all 442 pinned
    AIO labels/scoped synonyms and 181 prior native IDs/names/aliases. Ignored-inclusive
    searches of both full checkouts found prior discovery leads, neighboring sampler
    discussions and unrelated author-name/environment substrings. Existing random-walk
    Metropolis, delayed-rejection, fixed symmetric delayed-rejection and RAM records
    were inspected; shared components do not make these procedures equivalent.
  details: 'Start at a state with positive target density. In the original form, after
    an initial period with a chosen positive-definite C0, propose Y from N(X_(t−1),
    C_t), where C_t=s_d[Cov(X_0,...,X_(t−1))+epsilon I], epsilon>0 and s_d>0. The
    empirical covariance uses every retained state, with denominator t−1 for t available
    states; choose the adaptation start after at least two states. Accept with min(1,pi(Y)/pi(X_(t−1)))
    and otherwise repeat the old state. The fixed-covariance Metropolis rule is used
    at each iteration, but adapting C_t from the sampled history requires a separate
    validity argument. Limitations: The 2010 source explicitly analyzes a recursive
    modification, not an exact restatement of the original unbiased sample covariance.
    Its displayed outline also shifts the covariance index; the original timing is
    stated explicitly here. The original full-method text was read through a public
    indexed PDF. Direct download returned 403 and no visible page images were obtained;
    no original-PDF hash or visual inspection is claimed. The 2010 method pages were
    read and visually checked. The original bounded-support result and the later regular
    superexponential-tail results have different hypotheses. Neither licenses arbitrary
    targets or unrestricted adaptive variants. The usual dimension-based scale is
    a tuning heuristic under particular target assumptions, not a universal optimum.
    Empirical covariance estimation can be unsuitable for distributions without finite
    second moments. The sampled-state sequence alone is history dependent; invariant
    kernels at frozen settings do not by themselves prove adaptive convergence.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified sampling or adaptive transition procedure, not a trained
      instance or benchmark outcome.
    evidence_ids:
    - adaptivemetropolis-source
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This procedure adapts a family of Markov transition kernels that are
      target-invariant at frozen settings. Its sampled-state history is not assumed
      to be a homogeneous Markov chain, and adaptive validity requires separate assumptions.
      AIO MarkovChain is a process/model beneath Network; this is a related method-to-process
      mapping, not equivalence, an is-a assertion or a convergence guarantee.
    evidence_ids:
    - identity
    - mapping
- assessment_id: delayedrejectionadaptivemetropolis
  area: evidence
  topic: Identity, mechanism, source scope, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:DelayedRejectionAdaptiveMetropolis
  evidence_ids:
  - identity
  - mapping
  - neighbor-samplers
  - delayedrejectionadaptivemetropolis-source
  - delayedrejectionadaptivemetropolis-source-1
  summary: 'DRAM combines two distinct mechanisms: retained-history covariance learning
    across iterations and reversed-path acceptance corrections for additional attempts
    after rejection. The inspected author implementation supplies the explicit Gaussian-stage
    realization; it is not merely repeated ordinary Metropolis tests. No normalized
    identity match was found across all 442 pinned AIO labels/scoped synonyms and
    181 prior native IDs/names/aliases. Ignored-inclusive searches of both full checkouts
    found prior discovery leads, neighboring sampler discussions and unrelated author-name/environment
    substrings. Existing random-walk Metropolis, delayed-rejection, fixed symmetric
    delayed-rejection and RAM records were inspected; shared components do not make
    these procedures equivalent.'
  details: 'At fixed proposal settings for a transition, first propose y1 from N(x,C1)
    and use the Metropolis target ratio. After rejection propose y2 from N(x,C2),
    centered at the original x, with C2=C1/d1² for a positive stage scale d1 (d1>1
    narrows the proposal). Let q_i(a,b) denote the Gaussian proposal density at b
    from a and a1(a,b)=min(1,pi(b)/pi(a)). On a reachable rejection path, accept y2
    with min(1, [pi(y2)q1(y2,y1)q2(y2,x)(1−a1(y2,y1))]/[pi(x)q1(x,y1)q2(x,y2)(1−a1(x,y1))]).
    Higher stages use the recursive forward/reverse rejection products and earlier-stage
    Gaussian proposal ratios. Retain x after all capped stages reject. At scheduled
    iterations, update the empirical covariance from stored retained states including
    repeats, scale its Cholesky factor, and recompute stage factors for later transitions.
    In the inspected implementation diagonal jitter is attempted only when factorization
    fails; if that attempt also fails, the previous proposal factor is retained. Limitations:
    The original 2006 article metadata was located but its complete method PDF was
    not obtained. This record is supported by the named author’s pinned implementation
    and its covariance helper, not a claim to have read that article. The Gaussian
    factors remain fixed within a delayed-rejection transition. Recomputing adaptation
    from rejected internal candidates or ignoring reverse-path factors would require
    different justification. The implementation defaults to two attempts and adaptation
    every 100 iterations; its usage comment about three stages is inconsistent with
    those executable defaults. These counts are options, not the concept identity.
    Optional covariance pseudoweights, fixed nonadapted coordinates, early rejection-rate
    scaling, variance sampling and hierarchical updates are outside the simple fixed-target
    account here. Jitter only on factorization failure differs from always adding
    a positive regularizer. Source-code inspection alone establishes neither correctness
    for arbitrary targets nor adaptive ergodicity; no MATLAB execution or performance
    comparison was performed. Initialize within positive target support. Zero reverse-path
    probability gives zero acceptance; numerical evaluation must handle vanishing
    densities and log ratios without invalid divisions.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified sampling or adaptive transition procedure, not a trained
      instance or benchmark outcome.
    evidence_ids:
    - delayedrejectionadaptivemetropolis-source
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This procedure adapts a family of Markov transition kernels that are
      target-invariant at frozen settings. Its sampled-state history is not assumed
      to be a homogeneous Markov chain, and adaptive validity requires separate assumptions.
      AIO MarkovChain is a process/model beneath Network; this is a related method-to-process
      mapping, not equivalence, an is-a assertion or a convergence guarantee.
    evidence_ids:
    - identity
    - mapping
- assessment_id: adaptivescalingmetropolis
  area: evidence
  topic: Identity, mechanism, source scope, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:AdaptiveScalingMetropolis
  evidence_ids:
  - identity
  - mapping
  - neighbor-samplers
  - adaptivescalingmetropolis-source
  summary: The source’s ASM has fixed positive-definite shape and an adaptive scalar
    scale. This is distinct from covariance-shape adaptation and from RAM’s direction-dependent
    matrix update. The record uses the exponential-scale specialization of the source’s
    more general increasing scale map. No normalized identity match was found across
    all 442 pinned AIO labels/scoped synonyms and 181 prior native IDs/names/aliases.
    Ignored-inclusive searches of both full checkouts found prior discovery leads,
    neighboring sampler discussions and unrelated author-name/environment substrings.
    Existing random-walk Metropolis, delayed-rejection, fixed symmetric delayed-rejection
    and RAM records were inspected; shared components do not make these procedures
    equivalent.
  details: 'Fix shape Sigma positive definite and use a spherical proposal W. From
    retained x with pi(x)>0 and log scale S, propose Y=x+exp(S)Sigma^(1/2)W. Compute
    alpha=min(1,pi(Y)/pi(x)), accept Y with that probability or retain x, then update
    S_new=S+eta_n(alpha−alpha_star). Adapt after either outcome, using the acceptance
    probability rather than its Bernoulli realization. Choose alpha_star in (0,1)
    and positive step sizes with divergent sum and convergent sum of squares for the
    stated stochastic-approximation setting. The shape remains fixed; exp(S) multiplies
    standard deviation, so the covariance multiplier is exp(2S). Limitations: The
    stability and strong-law theorems in this version restrict alpha_star to (0,1/2),
    beyond the broader algorithm definition. Larger targets are discussed as expected
    extensions, not proved here. Compact-support regularity or the stated unbounded-target
    tail/contour assumptions and admissible proposal conditions are needed for the
    corresponding results. Positive step sizes alone are insufficient. The strong-law
    statements concern sample averages. The source explicitly distinguishes them from
    convergence in distribution of the adaptive sampled states. A target rate such
    as 0.234 is not a universal optimum, evidence of convergence or guarantee of good
    multimodal exploration. The inspected arXiv v3 submission date and later PDF footer
    differ; no later journal PDF inspection or numerical validation is claimed.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified sampling or adaptive transition procedure, not a trained
      instance or benchmark outcome.
    evidence_ids:
    - adaptivescalingmetropolis-source
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This procedure adapts a family of Markov transition kernels that are
      target-invariant at frozen settings. Its sampled-state history is not assumed
      to be a homogeneous Markov chain, and adaptive validity requires separate assumptions.
      AIO MarkovChain is a process/model beneath Network; this is a related method-to-process
      mapping, not equivalence, an is-a assertion or a convergence guarantee.
    evidence_ids:
    - identity
    - mapping
- assessment_id: adaptivescalingwithinadaptivemetropolis
  area: evidence
  topic: Identity, mechanism, source scope, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:AdaptiveScalingWithinAdaptiveMetropolis
  evidence_ids:
  - identity
  - mapping
  - neighbor-samplers
  - adaptivescalingwithinadaptivemetropolis-source
  summary: This record gives the bounded mean-and-shape formulation of Vihola Definition
    5. Its log scale is unbounded, while the proposed mean/shape pair is accepted
    only inside a specified compact constraint set. Unconstrained software variants
    are not automatically the same validity setting. No normalized identity match
    was found across all 442 pinned AIO labels/scoped synonyms and 181 prior native
    IDs/names/aliases. Ignored-inclusive searches of both full checkouts found prior
    discovery leads, neighboring sampler discussions and unrelated author-name/environment
    substrings. Existing random-walk Metropolis, delayed-rejection, fixed symmetric
    delayed-rejection and RAM records were inspected; shared components do not make
    these procedures equivalent.
  details: 'Choose alpha_star in (0,1) and initialize x with pi(x)>0, mu=x and feasible
    positive-definite Sigma. Propose Y=x+exp(S)Sigma^(1/2)W with spherical W, use
    alpha=min(1,pi(Y)/pi(x)), and retain X_new after the accept/reject test. Update
    S_new=S+eta_n(alpha−alpha_star). With the old mean mu and shape Sigma, form mu_hat=(1−eta_n)mu+eta_n
    X_new and Sigma_hat=(1−eta_n)Sigma+eta_n(X_new−mu)(X_new−mu)^T. For fixed zeta≥1,
    accept the entire proposed mean/shape pair only if ||mu_hat||≤zeta and every eigenvalue
    of Sigma_hat lies in [zeta^−1,zeta]; otherwise keep both old mu and old Sigma.
    Start with a feasible mean/shape pair and keep the scalar update separately. Use
    eta_n in (0,1), with divergent sum and finite squared sum under the source assumptions.
    Limitations: The covariance update uses the old mean and the retained new state,
    including repeated states after rejection. Substituting the new mean or only accepted
    proposals changes the specified recursion. The mean and shape constraints are
    part of this source’s proved formulation; only the scalar scale lacks a fixed
    bound. Omitting constraints in practice does not inherit the same theorem. The
    source’s strong-law results restrict alpha_star to (0,1/2) and require the corresponding
    target/proposal regularity conditions. Algorithm definition alone does not prove
    ergodicity. Shape learning is a recursive stochastic-approximation update, not
    exactly the original unbiased full-history covariance at every finite iteration.
    No universal efficiency advantage, marginal-distribution convergence or executed
    benchmark is asserted.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified sampling or adaptive transition procedure, not a trained
      instance or benchmark outcome.
    evidence_ids:
    - adaptivescalingwithinadaptivemetropolis-source
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This procedure adapts a family of Markov transition kernels that are
      target-invariant at frozen settings. Its sampled-state history is not assumed
      to be a homogeneous Markov chain, and adaptive validity requires separate assumptions.
      AIO MarkovChain is a process/model beneath Network; this is a related method-to-process
      mapping, not equivalence, an is-a assertion or a convergence guarantee.
    evidence_ids:
    - identity
    - mapping
- assessment_id: paralleltempering
  area: evidence
  topic: Identity, mechanism, source scope, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:ParallelTempering
  evidence_ids:
  - identity
  - mapping
  - neighbor-samplers
  - paralleltempering-source
  summary: The record identifies fixed-temperature parallel tempering, with the source’s
    adjacent-swap and random-walk realization as an explicit example. The population
    state includes all replicas; the beta=1 replica targets the original distribution.
    It differs from a single-chain simulated-temperature state and from adapting the
    temperature ladder. No normalized identity match was found across all 442 pinned
    AIO labels/scoped synonyms and 181 prior native IDs/names/aliases. Ignored-inclusive
    searches of both full checkouts found prior discovery leads, neighboring sampler
    discussions and unrelated author-name/environment substrings. Existing random-walk
    Metropolis, delayed-rejection, fixed symmetric delayed-rejection and RAM records
    were inspected; shared components do not make these procedures equivalent.
  details: 'Choose a fixed L≥2 and inverse temperatures 1=beta1>...>betaL>0 for which
    each integral Z_beta=integral pi(x)^beta dx is finite. Initialize replicas in
    positive target support. The joint target is the product of pi(x_l)^beta_l/Z_beta_l.
    In the inspected realization, choose j uniformly from adjacent pairs and propose
    swapping x_j and x_(j+1), with probability min(1,[pi(x_(j+1))/pi(x_j)]^(beta_j−beta_(j+1))).
    Then apply a Gaussian random-walk Metropolis update at every level using acceptance
    min(1,[pi(y_l)/pi(x_l)]^beta_l); rejected moves retain their current replica state.
    Both steps preserve the joint target, so their composition does also; samples
    at beta1=1 have the desired stationary marginal. Limitations: All tempered densities
    must be normalizable; flattening a target by taking a positive power below one
    need not preserve integrability. Target invariance alone does not establish irreducibility,
    mixing speed, finite-run convergence or independence of cold-replica samples.
    The source calls the composed chain reversible. Composition of two reversible
    kernels need not be reversible without additional conditions; this record asserts
    only their directly justified invariance. The original distribution is the cold
    replica’s marginal, not the pooled unweighted population distribution. Other valid
    local kernels and exchange schedules require their own conditions. The record’s
    explicit Gaussian and adjacent-swap realization is not a claim that all implementations
    use it.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified sampling or adaptive transition procedure, not a trained
      instance or benchmark outcome.
    evidence_ids:
    - paralleltempering-source
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: At fixed temperatures and proposal settings, the complete replica
      population follows a Markov transition preserving a product of tempered targets.
      AIO MarkovChain denotes the stochastic process/model beneath Network. This is
      a related algorithm-to-process mapping, not equivalence, subclass membership
      or an assertion of independent cold-replica samples.
    evidence_ids:
    - identity
    - mapping
- assessment_id: adaptiveparalleltempering
  area: evidence
  topic: Identity, mechanism, source scope, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:AdaptiveParallelTempering
  evidence_ids:
  - identity
  - mapping
  - neighbor-samplers
  - adaptiveparalleltempering-source
  summary: This record is the fixed-replica-count Miasojedow–Moulines–Vihola 2012
    construction. Its multiplicative inverse-temperature parameterization and all-pair
    swap-probability updates differ from later author software using increments of
    reciprocal temperatures and updates for selected pairs. No normalized identity
    match was found across all 442 pinned AIO labels/scoped synonyms and 181 prior
    native IDs/names/aliases. Ignored-inclusive searches of both full checkouts found
    prior discovery leads, neighboring sampler discussions and unrelated author-name/environment
    substrings. Existing random-walk Metropolis, delayed-rejection, fixed symmetric
    delayed-rejection and RAM records were inspected; shared components do not make
    these procedures equivalent.
  details: 'With fixed L≥2, alpha_star in (0,1) and epsilon in (0,1), set beta1=1
    and beta_(l+1)=beta_l exp(−exp(rho_l)). Initialize within the parameter constraint
    sets and positive target support. At each iteration use the previous temperatures
    and proposal covariances for an adjacent exchange followed by local Gaussian Metropolis
    moves. From the retained post-propagation population X_new, compute every adjacent
    hypothetical exchange probability h_l=min(1,[pi(X_(l+1))/pi(X_l)]^(beta_l−beta_(l+1))).
    Update each rho_l by projection of rho_l+gamma1_n(h_l−alpha_star) onto a fixed
    finite interval. For each replica update mu_l=(1−gamma2_n)mu_l+gamma2_n X_new,l,
    and project (1−gamma2_n)Gamma_l+gamma2_n(X_new,l−mu_old,l)(X_new,l−mu_old,l)^T
    onto matrices with eigenvalues in [epsilon,epsilon^−1]. Update T_l by interval
    projection of T_l+gamma3_n(alpha_local,l−alpha_star), where alpha_local is that
    iteration’s local proposal acceptance probability. Use Sigma_l=exp(T_l)Gamma_l
    for later Gaussian proposals. Thus T is log variance, not log standard deviation;
    all adaptation follows the completed transition. Limitations: The record uses
    projected covariance and log-scale adaptation with separate step sequences; the
    mean recursion itself is not projected. Finite rho bounds keep ordered positive
    inverse temperatures, and the replica count is fixed. Every rho update uses a
    hypothetical adjacent swap probability at the post-propagation state, not just
    the pair actually selected or a binary swap outcome. The strong-law and temperature-convergence
    results have different hypotheses. Temperature convergence additionally needs
    stronger step conditions and the target solution inside the projection bounds;
    projection alone does not guarantee the desired rate is attainable. The continuous-target
    results assume the stated tail/contour, moment and step-size conditions. Experiments
    omitting projections do not prove unrestricted adaptive validity. The optional
    RAM proposal variant in Section 2.3 uses a physical increment where the original
    RAM paper uses a standardized proposal direction. That variant is excluded here;
    the covariance-based construction is the inspected core. No changing-replica-count
    method, unrestricted adaptive convergence, universal efficiency claim or benchmark
    reproduction is asserted.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified sampling or adaptive transition procedure, not a trained
      instance or benchmark outcome.
    evidence_ids:
    - adaptiveparalleltempering-source
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: This procedure adapts a family of Markov transition kernels that are
      target-invariant at frozen settings. Its sampled-state history is not assumed
      to be a homogeneous Markov chain, and adaptive validity requires separate assumptions.
      AIO MarkovChain is a process/model beneath Network; this is a related method-to-process
      mapping, not equivalence, an is-a assertion or a convergence guarantee. The
      frozen joint population target depends on the ladder; the cold marginal remains
      pi. This does not assert one invariant joint law throughout adaptation.
    evidence_ids:
    - identity
    - mapping
- assessment_id: covariance-and-delayed-rejection
  area: scope
  topic: Accumulated covariance and within-transition retries
  outcome: supported
  target_ids:
  - AIMech:AdaptiveMetropolis
  - AIMech:DelayedRejectionAdaptiveMetropolis
  evidence_ids:
  - adaptivemetropolis-source
  - adaptivemetropolis-source-1
  - delayedrejectionadaptivemetropolis-source
  - delayedrejectionadaptivemetropolis-source-1
  - neighbor-samplers
  summary: Retain AM and its delayed-rejection combination as distinct scopes, preserving
    source-version limits.
  details: Original AM indexed method text supplies the unbiased covariance over retained
    states and always-positive jitter; the 2010 visual page makes its different recursive
    modification explicit. The DRAM author code keeps the Gaussian factors fixed within
    each transition, centers later candidates on the original state, recursively corrects
    reverse rejection paths, and stores the original state after complete rejection.
    covupd receives stored states and computes empirical covariance. Its jitter fallback
    and stage defaults are implementation-specific and are stated, not silently substituted
    into original AM. q2 symmetry cancels its ratio in the shown two-stage specialization,
    while q1 and rejected-path probabilities remain. No original DRAM article reading
    or general adaptive ergodicity proof is claimed.
- assessment_id: probability-scale-and-shape
  area: scope
  topic: ASM and constrained ASWAM update boundaries
  outcome: supported
  target_ids:
  - AIMech:AdaptiveScalingMetropolis
  - AIMech:AdaptiveScalingWithinAdaptiveMetropolis
  evidence_ids:
  - adaptivescalingmetropolis-source
  - adaptivescalingwithinadaptivemetropolis-source
  summary: Retain scalar-only adaptation and coupled scalar/shape adaptation.
  details: Visually rechecked Definitions 4–5 and the compact mean/shape constraint.
    Both methods adapt from the proposal acceptance probability after either outcome;
    exp(S) scales standard deviation. ASWAM covariance uses retained X_new and old
    mean, and rejects the whole candidate mean/shape pair outside S_zeta while keeping
    the scalar update. The stated positive steps are a supported specialization of
    nonnegative steps; the record does not conflate the broad target-rate definition
    with the theorems restricted to alpha_star below one half. Strong-law averages
    are not asserted to imply marginal convergence.
- assessment_id: replicas-and-temperature-adaptation
  area: scope
  topic: Fixed and projected adaptive temperature ladders
  outcome: supported
  target_ids:
  - AIMech:ParallelTempering
  - AIMech:AdaptiveParallelTempering
  evidence_ids:
  - paralleltempering-source
  - adaptiveparalleltempering-source
  - mapping
  summary: Retain fixed-ladder PT and the specified 2012 adaptive construction.
  details: Visually rechecked swap Equation (9), multiplicative ladder Equation (13),
    all-pair projected update (14) and shape/mean/log-variance equations (18)–(21).
    The adjacent-swap ratio has the cold-minus-hot exponent. Fixed swap and local
    kernels preserve the product target; their composition need not inherit reversibility,
    so the record makes only the invariant-law claim. APT uses every hypothetical
    adjacent exchange probability at the retained post-propagation state, old means
    in covariance updates, finite interval projections and exp(T) as a variance multiplier.
    The evolving joint target and fixed cold marginal are explicit. Strong-law and
    temperature-root convergence hypotheses differ; no removal of projections or changing
    replica count is inferred.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:AdaptiveMetropolis
  - AIMech:DelayedRejectionAdaptiveMetropolis
  - AIMech:AdaptiveScalingMetropolis
  - AIMech:AdaptiveScalingWithinAdaptiveMetropolis
  - AIMech:ParallelTempering
  - AIMech:AdaptiveParallelTempering
  evidence_ids:
  - identity
  - mapping
  - neighbor-samplers
  - adaptivemetropolis-source
  - adaptivemetropolis-source-1
  - delayedrejectionadaptivemetropolis-source
  - delayedrejectionadaptivemetropolis-source-1
  - adaptivescalingmetropolis-source
  - adaptivescalingwithinadaptivemetropolis-source
  - paralleltempering-source
  - adaptiveparalleltempering-source
  rationale: Retain original retained-history covariance adaptation, its delayed-rejection
    combination, scalar-only acceptance adaptation, bounded recursive shape/scale
    adaptation, fixed-temperature population exchange and the specified projected
    adaptive ladder. These differ in state and update construction. Frozen-kernel
    related mappings preserve algorithm/process and adaptive-history distinctions.
limitations:
- Adversarial author self-review only; all six records remain DRAFT.
- AM original full-method text was available but page images and local bytes were
  not; the later primary treatment was visually checked.
- DRAM is supported by pinned author source code and covariance helper, not the unavailable
  original full article; no MATLAB execution occurred.
- Only declared source text, image pages and code ranges were read.
- Later author documentation differences are recorded as version boundaries; its code
  was not executed or treated as identical to the 2012 APT method.
- No generic adaptive convergence, universal performance or finite-run sampling accuracy
  is certified.
- Required local and vendor checks passed; positive discoveries and remaining broad-AI
  leads mean the discovery goal remains active.
tags:
- native-concepts
- mcmc
- adaptive-mcmc
- parallel-tempering
- self-review
- discovery-ongoing
```
