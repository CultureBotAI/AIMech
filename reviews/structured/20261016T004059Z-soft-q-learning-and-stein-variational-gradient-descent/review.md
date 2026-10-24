# Scientific self-review of Soft Q-learning and Stein variational gradient descent

- Review: 20261016T004059Z-soft-q-learning-and-stein-variational-gradient-descent
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-16T00:26:56.042079Z
- Finished UTC: 2026-10-16T00:40:59.313135Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Separate issue404 accounting preserves six pending source questions and seven inspection-responsibility attachments; no issue closure is requested. Retain the source-defined Soft Q-learning control algorithm and SVGD particle inference algorithm as distinct DRAFT records. Eleven claims and fourteen limitations preserve exact versus approximate theory and source-version boundaries. Owner 909 groups their discovery with explicit non-equivalence and retained source questions. Actual canonical/capture/page evidence and six checks are verified. Inherited 402 triage and restoration provenance remain exact; no issue closure is requested.

## Scope And Provenance

Complete selected two-record cohort in actual captured canonical state, plus source-question and inherited-governance preservation.

Selection: Exact source-defined Soft Q-learning and Stein variational gradient descent drafts.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 008d1eafc23cb19605953fa860475256d1b28895.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SoftQLearning | data/curated/SoftQLearning.yaml | maintained | Soft Q-learning |
| AIMech:SteinVariationalGradientDescent | data/curated/SteinVariationalGradientDescent.yaml | maintained | Stein variational gradient descent |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:SoftQLearning, AIMech:SteinVariationalGradientDescent | Actual successful command; exact output is retained. |
| just vendored-check | passed | True | AIMech:SoftQLearning, AIMech:SteinVariationalGradientDescent | Actual successful command; exact output is retained. |
| uv run --locked aimech check-source | passed | True | AIMech:SoftQLearning, AIMech:SteinVariationalGradientDescent | Actual successful command; exact output is retained. |
| just render | passed | True | AIMech:SoftQLearning, AIMech:SteinVariationalGradientDescent | Actual successful command; exact output is retained. |
| just render-check | passed | True | AIMech:SoftQLearning, AIMech:SteinVariationalGradientDescent | Actual successful command; exact output is retained. |
| git diff --check | passed | True | AIMech:SoftQLearning, AIMech:SteinVariationalGradientDescent | Actual successful command; exact output is retained. |
| Historical attempt: just vendored-check | failed | False | AIMech:SoftQLearning, AIMech:SteinVariationalGradientDescent | Retained failed attempt; actual successful replacement cited separately. |

## Scientific And Domain Assessments

### entropy-objective

evidence: supported. Targets: AIMech:SoftQLearning.

Main Equation 2 adds conditional policy entropy and Section 2.1 distinguishes future entropy from greedy Boltzmann exploration. Appendix A explicitly qualifies discount weighting; the claim does not adopt its inconsistent first display as a corrected executable objective.

### energy-policy

evidence: supported. Targets: AIMech:SoftQLearning.

Main Equations 3–6 identify the target Boltzmann distribution and alpha-scaled log normalizer. The claim requires finite positive normalization and distinguishes the exact target identity from expressivity or sampling guarantees for finite neural networks.

### soft-backup

evidence: supported. Targets: AIMech:SoftQLearning.

Main Theorem 3 and Appendix A.2 concern the exact soft expected backup with bounded values and finite partitions. The statement retains those premises and does not transfer the fixed-point result to replay, neural projection or approximate sampling.

### approximate-value-fit

evidence: supported. Targets: AIMech:SoftQLearning.

Main Equation 10 is an importance-weighted integral representation, and Algorithm 1 uses its empirical estimate with delayed parameters before fitting Equation 11. The claim describes this estimator without asserting log-unbiasedness or a globally valid sampler density.

### amortized-stein-sampler

evidence: supported. Targets: AIMech:SoftQLearning.

Main Equation 13 defines action-gradient attraction plus alpha-scaled kernel repulsion, and Equation 14/C.1 project the finite-particle direction through the sampler. The third citation is context only: pinned later code minimizes a negative surrogate. The positive update direction is not silently relabeled the literal ordinary KL gradient.

### replay-alternation

evidence: supported. Targets: AIMech:SoftQLearning.

Algorithm 1 and Section 3.4 explicitly interleave interaction, replay minibatches, value/sampler updates and periodic target copies. This defines the reusable method without certifying a unique implementation schedule, terminal convention or trained policy result.

### Limitation 1

scope: supported. Targets: AIMech:SoftQLearning.

For alpha&gt;0 and finite positive partitions, Q1&lt;=Q2+epsilon implies V1&lt;=V2+epsilon. Reversing the inequality bounds the soft-value difference by the sup norm of Q1-Q2; the exact expected backup is gamma-Lipschitz for 0&lt;=gamma&lt;1 on an appropriate complete bounded function class. This hand check does not certify all theorem premises, an arbitrary action measure, or convergence after neural projection, finite sampling and nonconvex SGD. Locator: Main Theorem 3, PDF pp. 3–4; supplement Appendix A.2, PDF pp. 12–13.

### Limitation 2

scope: supported. Targets: AIMech:SoftQLearning.

If independent proposal samples have positive weights w=exp(Q/alpha)/q and E[w]=Z, the sample mean estimates Z; applying alpha log generally introduces downward Jensen bias whenever the mean is nonconstant and the required expectations exist. Exact normalized q=exp(Q/alpha)/Z for the same Q makes all weights equal to Z, eliminating this sampling variation. An approximate sampler, especially one targeting a different delayed Q, does not meet that equality automatically. No numerical experiment was run. Locator: Main Section 3.2, Equation 10, PDF p. 4; supplement C.2, PDF p. 14.

### Limitation 3

scope: supported. Targets: AIMech:SoftQLearning.

Equal dimension and a nonsingular Jacobian at a point ensure only a local inverse. A density through a many-to-one smooth map requires summing over regular preimages (with appropriate domain conditions). For f(x)=x^2, standard-normal x and y&gt;0, the two branches give pY(y)=[phi(sqrt(y))+phi(-sqrt(y))]/(2 sqrt(y)); one-branch Equation 33 gives half that density. Switching from uniform samples after training does not establish global injectivity. No failure of a particular trained sampler is claimed. Locator: Supplement Appendix C.2, Equation 33, PDF p. 14.

### Limitation 4

scope: supported. Targets: AIMech:SoftQLearning.

Equation 13 is a Stein transport/descent direction for KL; Equation 14 labels its positive projection a gradient. Hand witness: alpha=1, Q(a)=-a^2/2, constant positive-semidefinite kernel k=1, and sampler a=xi+phi with xi standard normal give KL(N(phi,1)&#124;&#124;N(0,1))=phi^2/2, ordinary derivative phi, but projected Stein direction -phi. Thus minimizing with the literal positive projected direction as an ordinary gradient would reverse this simple descent direction. The paper calls it an optimal functional direction rather than a strict gradient. The pinned 2019 code forms the projected direction and minimizes the negative surrogate, consistent with following the transport direction. This is a notation/sign-convention limitation, not a demonstrated implementation failure or full exact-gradient equivalence. Locator: Main Equations 12–14, PDF p. 5; supplement C.1, PDF pp. 13–14; pinned later code lines 247–268 (context).

### Limitation 5

scope: supported. Targets: AIMech:SoftQLearning.

The source explicitly distinguishes discounted policy-gradient weighting from a plain globally discounted state-occupancy objective. Its first Appendix A display uses r(s_t,a_t) and H(pi(.&#124;s_t)) inside a future-l sum, whereas nearby prose describes future rewards/entropies and Equation 15 indexes future terms. Retain this displayed-index inconsistency; recommend only a source-qualified reward-plus-entropy description, not a silent repaired objective or a universal trajectory-entropy identity. With residual r=Abar+Vtheta-Qtheta and the fixed target treated constant, the ordinary derivative of 0.5*r^2 is r*(grad V-grad Q). Equation 32 instead displays r*(grad Q-grad V), a descent direction. This reinforces the need to distinguish update direction from literal derivative. Do not import unqualified policy-gradient/soft-Q gradient equivalence from this display; no entire proof-invalidity claim is made. Locator: Supplement Appendix A first display/Equations 15–16, PDF p. 11; Appendix B Equation 32, PDF p. 13.

### Limitation 6

scope: supported. Targets: AIMech:SoftQLearning.

A zero population squared loss with positive sampling density ordinarily gives equality almost everywhere; pointwise equality needs additional regularity. Finite empirical zero does not prove either global statement. On unbounded Lebesgue action domains, bounded Q alone cannot ensure a finite partition; the finite-partition premise and selected domain/function class must be maintained. Differential entropy also depends on the fixed action reference measure and units. These are scope conditions, not experimental counterexamples. Locator: Main Sections 3.1–3.2, PDF pp. 3–4; supplement A.1–A.2 and C.2, PDF pp. 11–14.

### Limitation 7

scope: supported. Targets: AIMech:SoftQLearning.

Finite simulated tasks and pretraining/fine-tuning results do not establish universal multimodal coverage, performance, policy composition or global convergence. The complete later sql.py was read but not executed; its uniform action proposal, reward scaling, squash correction and target-Q implementation are version-specific context. Its code, dependencies, kernels, policies and environments were not fully audited as an executable system. Locator: Main Sections 5–6, PDF pp. 6–8; supplement D, PDF pp. 14–16; official version metadata and later author implementation context.

### Definition and granularity

identity: supported. Targets: AIMech:SoftQLearning.

The selected 2017 procedure couples interactive soft Bellman fitting with an amortized Stein sampler; the target Boltzmann identity does not imply exact neural sampling. Main and supplement define one work.

### Historical identity and version boundaries

identity: supported. Targets: AIMech:SoftQLearning.

The selected 2017 procedure couples interactive soft Bellman fitting with an amortized Stein sampler; the target Boltzmann identity does not imply exact neural sampling. Main and supplement define one work. Keep the compound control algorithm distinct from its SVGD sampling component and maintained SAC/Q-learning neighbors. The actual captured identity notes implement the root current collection decisions; the original preview scope remains historical and is recorded in context_changes. Existing owner 909 has the current bounded disposition partially_addressed, with all prior IDs, discovery pointers and resolution objects retained.

### Explicit bounded AIO mapping

grounding: supported. Targets: AIMech:SoftQLearning.

All nine exact AIO nodes and 71 incident-edge entries were read in research. The chosen RL relation is algorithm-to-task association, not exact or broad-match ontology identity; alternative generic-function/network/LLM classes are not substituted.

### Distinct source roles and reading scopes

evidence: supported. Targets: AIMech:SoftQLearning.

Three rows: official main and supplement are two primary artifacts of one 2017 work; pinned 2019 code is official documentation used only as context. Paper accessed_at explicitly records actual local verification, not invented acquisition seconds. Historical research acceptance reading: {"root_primary_reading": {"path": "/private/tmp/aimech-soft-q-research-20261015/root-primary-reading.json", "sha256": "ec82498475f2ae36600109c34ac3222cbf8806e80b6f03a44f92add738ba1842"}, "scope": "Research accepted for TEMP data-only native draft: one SoftQLearning algorithm, no aliases, qualified related_match to AIO ReinforcementLearning, six claims and seven limitations. Canonical ownership and actual merged-base identity remain future steps.", "root_reading": "Read full dossier, analytic boundaries, all proposed claims/limitations, sources and identity assessment; all seven matching contents and provenance, ten native definition projections, six selected frontier objects, and nine complete AIO nodes with 71 incident edges. Read later sql.py lines 210–280 for the projected positive transport and minimized negative surrogate. Prior source reading remains attributed by root-primary-reading; full five native record and full code reads are agent evidence, not relabeled root reading."}. Exact draft acceptance reading: {"scope": "Root full static module, inputs, sources, identity, six claim and seven limitation support reading; exact metadata-only successor read and accepted. Definition and claims retain 2017 method, finite approximation and source notation boundaries. Source context remains explicit and no exact code-version equivalence claimed.", "root_reading_scope": "Prior primary reading and research acceptance remain separately attributed. No new primary reread or independent approval is implied."}. This preparation did not newly inspect primary pages or execute the methods.

### Algorithm and operational scope

scope: supported. Targets: AIMech:SoftQLearning.

The record denotes the source-defined reusable algorithm, with the exact accepted scope and limitations.

### target-and-particles

evidence: supported. Targets: AIMech:SteinVariationalGradientDescent.

The target-score requirement and supplied initial particles are explicit in Algorithm 1. An x-independent positive normalizer cancels under the log gradient; the transported particle configuration is not a fixed parametric variational family.

### synchronous-kernel-update

evidence: supported. Targets: AIMech:SteinVariationalGradientDescent.

Equation 8 averages over every j including the diagonal and uses old iteration-l particles for both arguments and scores. An in-place sequential mutation would define a different recurrence; no implementation was executed.

### population-variational-direction

evidence: supported. Targets: AIMech:SteinVariationalGradientDescent.

Theorem 3.1 has the negative Stein expectation, Lemma 3.2 uses the radius-D RKHS ball, and Theorem 3.3 identifies the unnormalized representer as negative functional gradient at the identity. Unit-ball normalization and population/empirical measures are not silently interchanged. The supplemental leading sign is explicitly qualified.

### rbf-specialization

evidence: supported. Targets: AIMech:SteinVariationalGradientDescent.

For k(u,x)=exp(-&#124;&#124;u-x&#124;&#124;²/h), its first-argument derivative is (2/h)(x-u)k. At one particle, unit diagonal and zero diagonal first derivative yield the target score. This is an exact recurrence reduction, not a MAP convergence guarantee or general-kernel normalization claim.

### practical-computation

evidence: supported. Targets: AIMech:SteinVariationalGradientDescent.

The operational recurrence uses scores and pair kernels, without transporting-density determinant evaluation or Metropolis rejection. Main prose discusses minibatch scores and pairwise approximations; their sampling/scaling differs from exact-score full sums. Later v3 is cited only to retain the Eq. 9 version/display context, not as independent mechanism evidence.

### Limitation 1

scope: supported. Targets: AIMech:SteinVariationalGradientDescent.

Smooth-density integration and valid global transforms are premises. Local nonsingularity is insufficient. The retained Lipschitz hand bound supplies an illustrative sufficient injectivity condition only, not an implementation safeguard or full domain proof. Locator: Main pp. 2–4; supplement A–B, pp. 1–2.

### Limitation 2

scope: supported. Targets: AIMech:SteinVariationalGradientDescent.

Finite particles assign positive mass to points of zero probability under a continuous target; absolute continuity fails and atomic KL is infinite. The empirical vector field approximates the smooth-population construction. Infinitesimal descent and reported experiments do not establish arbitrary finite-step convergence. Locator: Main p. 5 particle approximation discussion and p. 6 error-rate qualification; supplement D.

### Limitation 3

scope: supported. Targets: AIMech:SteinVariationalGradientDescent.

Identical particle locations give identical scores and zero RBF separation derivatives, so synchronous updates preserve coincidence. The median/log(n) domain caveat concerns the reported experimental heuristic, not every permissible Algorithm 1 kernel. Locator: Main pp. 5–6; explicit hand consequence of Equation 8.

### Limitation 4

scope: supported. Targets: AIMech:SteinVariationalGradientDescent.

A general nonunit diagonal rescales the score contribution at n=1; distinct fixed particles with h→0 leave the self term score/n. Neither limiting direction nor a repulsion label establishes equal numerical steps, independent samples or universal anti-collapse. Locator: Main p. 5 Equation 8 and limiting prose; hand substitutions.

### Limitation 5

scope: supported. Targets: AIMech:SteinVariationalGradientDescent.

Direct all-pair evaluation is quadratic in particle count; score-cost dominance is problem dependent. Minibatch and approximate pair sampling add assumptions and randomness, and no software implementation or benchmark was inspected. These are bounded implementation/evaluation limits rather than an observed failure. Locator: Main pp. 5–8 and supplement D.

### Limitation 6

scope: supported. Targets: AIMech:SteinVariationalGradientDescent.

The retained Gaussian-translation witness distinguishes the supplement leading sign from its proof; Algorithm 1 has explicit gradients whereas Eq. 9 displays scalar log densities. Selected v3 pages retain these displays. Neither is treated as proof that the entire algorithm or every implementation is invalid. Locator: Main p. 5 Equation 9; supplement p. 1; arXiv v3 pp. 5 and 11.

### Limitation 7

scope: supported. Targets: AIMech:SteinVariationalGradientDescent.

The original toy prose/caption discrepancy was visually checked in research and no numerical toy conclusion is adopted. The original scalar-kernel recurrence does not confer coverage of later amortization, policy-gradient, matrix-kernel or convergence literature; prior citation leads remain separate. Locator: Main pp. 6–7, visually verified; original method scope and separately retained later-web/citation context.

### Definition and granularity

identity: supported. Targets: AIMech:SteinVariationalGradientDescent.

The reusable source-defined scalar-kernel particle-inference recurrence is narrower than later amortized control methods and is distinguished from population transport theory.

### Historical identity and version boundaries

identity: supported. Targets: AIMech:SteinVariationalGradientDescent.

The reusable source-defined scalar-kernel particle-inference recurrence is narrower than later amortized control methods and is distinguished from population transport theory. Keep the original particle inference algorithm distinct from its amortized use in Soft Q-learning and other variational or stochastic methods. The actual captured identity notes implement the root current collection decisions; the original preview scope remains historical and is recorded in context_changes. Existing owner 909 has the current bounded disposition partially_addressed, with all prior IDs, discovery pointers and resolution objects retained.

### Explicit bounded AIO mapping

grounding: supported. Targets: AIMech:SteinVariationalGradientDescent.

All eight exact pinned contexts and 32 incident edges were read in research. No scalar-only interpretation of MathematicalFunction is used. No positive mapping field is emitted. The actual no-match search_scope is the separately recorded current root assessment; its accepted rationale and examined-target rejections remain unchanged.

### Distinct source roles and reading scopes

evidence: supported. Targets: AIMech:SteinVariationalGradientDescent.

Three declared rows: official main and downloaded supplement ZIP are defining artifacts of one 2016 work; the sole appendix PDF is separately checksum-bound. Later combined arXiv v3 is context only. Actual original acquisition times are preserved. Historical research acceptance reading: {"reading_scope": "Root previously read all nine original main text pages and main visuals 4–5. Root now read all four official supplement text pages and supplement visual 1, full dossier, source ledger and reading scopes, all proposed five claims/seven limitations and analytic boundaries, identity/mapping/citation assessments, all eight pinned AIO node/edge contexts, and eight maintained identity/definition/mapping projections. Later-v3 selected reading, other declared original visuals, two full native records and sixteen selected frontier bodies remain attributed to the supporting researcher. No whole later-version or software inspection is claimed."}. Exact draft acceptance reading: {"scope": "Root read exact static module and sources before restart; inputs, time projection, identity and complete support after restart, including truncation recovery for limitations2/3. All5claims/7limitations and8explicit AIO rejections agree with accepted original source reading. Defining main/appendix belong to one2016work; appendix row hashes downloaded ZIP and separately binds extractedPDF; later v3 has only inspected context scope. No new visual reading or future-base identity clearance claimed. Mechanical AST/support equality checked separately."}. This preparation did not newly inspect primary pages or execute the methods.

### Algorithm and operational scope

scope: supported. Targets: AIMech:SteinVariationalGradientDescent.

The record denotes the source-defined reusable algorithm, with the exact accepted scope and limitations.

### citation-accounting

ownership: supported. Targets: AIMech:SoftQLearning, AIMech:SteinVariationalGradientDescent.

Owner 909 remains a partial source-discovery group for two distinct concepts. Three original citation entries and five bibliography questions remain fully queryable; fresh semantic assessments retain existing records or responsible owners when found. Seven pending source questions do not assert seven missing concepts. No main or nested row is appended.

### inherited-governance

provenance: supported. Targets: AIMech:SoftQLearning, AIMech:SteinVariationalGradientDescent.

The exact actual 354/353/352 governance snapshots, restoration provenance and separate issue 402 bibliography triage are preserved. No prior repair or closure is repeated. Separate issue404 accounting assigns future inspection responsibility for six pending questions and seven scoped attachments, preserving exact source questions and existing owner objects; no research completion is inferred.

### actual-correspondence

provenance: supported. Targets: AIMech:SoftQLearning, AIMech:SteinVariationalGradientDescent.

Two DRAFT records preserve eleven accepted claims and fourteen limitations. Four defining artifacts belong to two works; later code and later arXiv v3 remain two context artifacts. Only owner 909 changes; all 912 other main and 394 nested objects remain exact. Five exclusive outputs, one CREATE history, 44 capture inputs, actual pages and six completed checks are bound. Original citation questions and separate inherited issue 402 triage remain explicit. No independent approval or exhaustion is implied.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:SoftQLearning. The selected 2017 procedure couples interactive soft Bellman fitting with an amortized Stein sampler; the target Boltzmann identity does not imply exact neural sampling. Main and supplement define one work. Keep the compound control algorithm distinct from its SVGD sampling component and maintained SAC/Q-learning neighbors.
- retain: AIMech:SteinVariationalGradientDescent. The reusable source-defined scalar-kernel particle-inference recurrence is narrower than later amortized control methods and is distinguished from population transport theory. Keep the original particle inference algorithm distinct from its amortized use in Soft Q-learning and other variational or stochastic methods.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| preview-softq | /private/tmp/aimech-soft-q-code-access-successor-20261015/native-preview.json | context_only | Accepted TEMP preview; actual canonical correspondence remains unbound. |
| support-softq | /private/tmp/aimech-soft-q-draft-preparation-20261015/scientific-support.json | context_only | Exact accepted per-claim and per-limitation support; historical scope remains attributed. |
| draft-acceptance-softq | /private/tmp/aimech-soft-q-code-access-successor-20261015/root-draft-acceptance.json | context_only | Exact root draft acceptance precedes retained validation. |
| preview-validation-softq | /private/tmp/aimech-soft-q-code-access-successor-20261015/native-preview-validation.json | context_only | Retained postacceptance TEMP validation; no future gate inferred. |
| root-research-softq | /private/tmp/aimech-soft-q-research-20261015/root-research-acceptance.json | context_only | Historical research acceptance reading: {"root_primary_reading": {"path": "/private/tmp/aimech-soft-q-research-20261015/root-primary-reading.json", "sha256": "ec82498475f2ae36600109c34ac3222cbf8806e80b6f03a44f92add738ba1842"}, "scope": "Research accepted for TEMP data-only native draft: one SoftQLearning algorithm, no aliases, qualified related_match to AIO ReinforcementLearning, six claims and seven limitations. Canonical ownership and actual merged-base identity remain future steps.", "root_reading": "Read full dossier, analytic boundaries, all proposed claims/limitations, sources and identity assessment; all seven matching contents and provenance, ten native definition projections, six selected frontier objects, and nine complete AIO nodes with 71 incident edges. Read later sql.py lines 210–280 for the projected positive transport and minimized negative surrogate. Prior source reading remains attributed by root-primary-reading; full five native record and full code reads are agent evidence, not relabeled root reading."}. Exact draft acceptance reading: {"scope": "Root full static module, inputs, sources, identity, six claim and seven limitation support reading; exact metadata-only successor read and accepted. Definition and claims retain 2017 method, finite approximation and source notation boundaries. Source context remains explicit and no exact code-version equivalence claimed.", "root_reading_scope": "Prior primary reading and research acceptance remain separately attributed. No new primary reread or independent approval is implied."}. This preparation did not newly inspect primary pages or execute the methods. |
| preparation-reading-softq | /private/tmp/aimech-soft-q-draft-preparation-20261015/reading.json | context_only | Historical draft reading scope, separately attributed. |
| historical-identity-softq | /private/tmp/aimech-soft-q-research-20261015/identity-assessment.json | context_only | Dated identity assessment; fresh current collection remains required. |
| src-haarnoja2017-main | /private/tmp/aimech-soft-q-research-20261015/haarnoja2017-main.pdf | supports | primary method support. Official PMLR 70 (ICML 2017), ten-page main article; accessed_at records local artifact verification, not download time. Original acquisition was approximately 2026-10-15 21:31Z; exact download seconds are not asserted. |
| src-haarnoja2017-supp | /private/tmp/aimech-soft-q-research-20261015/haarnoja2017-supp.pdf | supports | primary supplementary derivation/implementation scope. Official PMLR supplementary PDF, sixteen pages; first ten extracted text pages equal main; appendices A–D on PDF pages 11–16; accessed_at records local artifact verification, not download time. Original acquisition was approximately 2026-10-15 21:31Z; exact download seconds are not asserted. |
| src-haarnoja-code-context | /private/tmp/aimech-soft-q-research-20261015/code-context/sql.py | context_only | context_only for later sign convention and version boundary. Author repository commit 6f51eaca77d15b35c6443363c51a5a53ff4e9854, dated 2019-01-05; complete 357-line static read. Later implementation context only, not established as the 2017 experimental version. |
| preview-svgd | /private/tmp/aimech-svgd-draft-preparation-20261015/native-preview.json | context_only | Accepted TEMP preview; actual canonical correspondence remains unbound. |
| support-svgd | /private/tmp/aimech-svgd-draft-preparation-20261015/scientific-support.json | context_only | Exact accepted per-claim and per-limitation support; historical scope remains attributed. |
| draft-acceptance-svgd | /private/tmp/aimech-svgd-draft-preparation-20261015/root-draft-acceptance.json | context_only | Exact root draft acceptance precedes retained validation. |
| preview-validation-svgd | /private/tmp/aimech-svgd-draft-preparation-20261015/native-preview-validation.json | context_only | Retained postacceptance TEMP validation; no future gate inferred. |
| root-research-svgd | /private/tmp/aimech-svgd-research-20261015/root-research-acceptance.json | context_only | Historical research acceptance reading: {"reading_scope": "Root previously read all nine original main text pages and main visuals 4–5. Root now read all four official supplement text pages and supplement visual 1, full dossier, source ledger and reading scopes, all proposed five claims/seven limitations and analytic boundaries, identity/mapping/citation assessments, all eight pinned AIO node/edge contexts, and eight maintained identity/definition/mapping projections. Later-v3 selected reading, other declared original visuals, two full native records and sixteen selected frontier bodies remain attributed to the supporting researcher. No whole later-version or software inspection is claimed."}. Exact draft acceptance reading: {"scope": "Root read exact static module and sources before restart; inputs, time projection, identity and complete support after restart, including truncation recovery for limitations2/3. All5claims/7limitations and8explicit AIO rejections agree with accepted original source reading. Defining main/appendix belong to one2016work; appendix row hashes downloaded ZIP and separately binds extractedPDF; later v3 has only inspected context scope. No new visual reading or future-base identity clearance claimed. Mechanical AST/support equality checked separately."}. This preparation did not newly inspect primary pages or execute the methods. |
| preparation-reading-svgd | /private/tmp/aimech-svgd-draft-preparation-20261015/reading.json | context_only | Historical draft reading scope, separately attributed. |
| historical-identity-svgd | /private/tmp/aimech-svgd-research-20261015/identity-assessment.json | context_only | Dated identity assessment; fresh current collection remains required. |
| src-liu2016-main | /private/tmp/aimech-svgd-research-20261015/liu-wang2016.pdf | supports | primary method support. Official 2016 proceedings PDF, nine pages. |
| src-liu2016-supplement | /private/tmp/aimech-svgd-research-20261015/supplement.zip | supports | same-work primary appendix support with display caveat. Official single-member ZIP; four-page PDF appendix, no software in this archive. The row checksum identifies the downloaded ZIP; its sole inspected member 1239-appendix.pdf has SHA256 112e4b57860af60e81f9f9bd6877bc8c3b190cc6aee6375e3ed9a99f294de337. This is supplementary evidence for the same 2016 work. |
| src-liu2019-v3-context | /private/tmp/aimech-svgd-research-20261015/liu-wang-arxiv-v3.pdf | context_only | context_only selected later-version comparison. arXiv:1608.04471v3, submitted 2019-09-09, 13-page combined paper/appendix. No full-version reading claimed. Context only for selected display/version comparison; the original 2016 method remains defining. |
| actual-write | /private/tmp/aimech-softq-svgd-cohort355-write.json | context_only | Actual exclusive creation receipt: two records, report pair and one CREATE history. |
| captured-inputs | /private/tmp/aimech-cohort355-capture.json | context_only | Actual canonical inspection; every current input hash and maintained target was checked. |
| postcapture-reading | /private/tmp/aimech-cohort355-root-review-reading.json | context_only | Historical root reading receipt, recorded 2026-10-16T00:29:56.490975+00:00: Root read both complete canonical YAML files after writing, complete report Markdown (recovered truncated FLOW07–20 block), complete CREATE history, current report metadata, three identity/no-match context changes and complete changed owner909 including all eight citations/root dispositions. Root previously read the three inherited governance blocks, all six404 questions/seven responsibility attachments and all33 normalized406 questions and exact recoverable source payloads; actual report/write/decision registry equality and 44 capture hashes independently rechecked after capture. This is not full manual reading of 912 unchanged main or394 nested objects nor every repeated raw provenance occurrence. Root read actual scientific correspondence audit with105 checks and independent output audit189checks; no finding remains. Prior full primary reading and mathematical checks remain separately attributed; source-version caveat retained. Any future-event wording belongs to that earlier receipt; the later six check logs establish completion before this review was generated, while canonical save remains subsequent. |
| governance-assessment | /private/tmp/aimech-cohort355-governance-audit-20261015/assessment.json | context_only | Actual byte preservation, owner/frontier, history and parsed-page audit; no independent approval. |
| rendered-pages | /private/tmp/aimech-cohort355-governance-audit-20261015/rendered-pages.json | context_only | Actual generated page paths and bytes, with parsed-content correspondence; no browser/layout inspection. |
| actual-scientific-assessment | /private/tmp/aimech-cohort355-actual-scientific-audit-20261016/assessment.json | context_only | Same-author actual-record adversarial assessment with separately attributed primary reading. |
| current-identity-collection | /private/tmp/aimech-cohort355-identity-20261016/collection.json | context_only | Current four-root ignored- and hidden-inclusive identity collection; mechanical coverage is distinct from attributed semantic reading. |
| current-context-assessment | /private/tmp/aimech-cohort355-identity-20261016/root-current-assessment.json | context_only | Actual supporting interpretation of retained matched contexts; root and supporting scopes remain separate. |
| root-decisions | /private/tmp/aimech-cohort355-identity-20261016/root-decisions.json | context_only | Actual root identity, partial owner 909 and all eight source-question decisions; existing record/owner links remain explicit and all other frontier objects remain exact. |
| scientific-support | /private/tmp/aimech-cohort355-consumer-preparation-20261015/scientific-support.v2.prepared.json | context_only | Exact accepted claim and limitation support; historical and later source/math scopes remain separate. |
| discovery-report | /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T002614Z-soft-q-learning-and-stein-variational-gradient-descent.json | context_only | Current records and owner 909 citation mirrors; three original citation entries and five bibliography questions remain queryable. Exact inherited governance and issue 402 triage remain separate; no rows appended. |
| creation-history | /private/tmp/aimech-discovery-recovery-worktree-20261012/history/reports/soft-q-learning-and-stein-variational-gradient-descent/2026-10-16T002628Z-codex-1f51bf.yaml | context_only | Actual CREATE report history covers two new records and the report; no old report or existing restoration row is edited. |
| record-softq | /private/tmp/aimech-discovery-recovery-worktree-20261012/data/curated/SoftQLearning.yaml | context_only | Complete current DRAFT record equals accepted science and actual root identity decisions. |
| record-svgd | /private/tmp/aimech-discovery-recovery-worktree-20261012/data/curated/SteinVariationalGradientDescent.yaml | context_only | Complete current DRAFT record equals accepted science and actual root identity decisions. |
| check-gate | /private/tmp/aimech-cohort355-check-gate.json | context_only | Actual required command completed successfully before this review generation. |
| check-vendor | /private/tmp/aimech-cohort355-network-resume-check-vendor.json | context_only | Actual required command completed successfully before this review generation. |
| check-check-source | /private/tmp/aimech-cohort355-network-resume-check-check-source.json | context_only | Actual required command completed successfully before this review generation. |
| check-render | /private/tmp/aimech-cohort355-check-render.json | context_only | Actual required command completed successfully before this review generation. |
| check-render-check | /private/tmp/aimech-cohort355-network-resume-check-render-check.json | context_only | Actual required command completed successfully before this review generation. |
| check-diff | /private/tmp/aimech-cohort355-network-resume-check-diff.json | context_only | Actual required command completed successfully before this review generation. |
| historical-check-attempt-1 | /private/tmp/aimech-cohort355-check-vendor.json | context_only | Actual failed attempt, retained with its later successful same-command replacement. |

## Limits And Additional Notes

- Historical research, root and supporting readings remain separately attributed; this review preparation adds no primary-page reading or algorithm execution.
- Soft Q-learning preserves exact-backup versus finite neural learning, action-measure, density, source-display and version limits. SVGD preserves population versus finite-particle, transform, source-display, finite-step and empirical limits.
- Four defining artifacts belong to two primary works. The pinned later SoftQ code and later SVGD arXiv v3 are two context artifacts, not two additional defining works. The downloaded supplement ZIP and its extracted PDF have distinct hashes.
- Both exact draft acceptances preceded their retained one-time TEMP native validations. Later canonical checks remain separately required.
- Owner909 groups two distinct concepts through source discovery; it does not assert equivalence, aliasing or subclass. Three original SoftQ citation entries and five SVGD bibliography questions remain recursively queryable.
- Inherited354 restoration and older352 provenance remain exact. Issue402 triage is separately preserved; no old repair or closure is repeated.
- Historical 783/442 identity evidence remains dated; actual current root decisions supply identity and mapping scope. Owner 909 remains partial; pending source questions retain existing identity/owner links when found and do not imply novel concepts.
- Actual five outputs, one CREATE history, 7 generated pages and 44 capture inputs are bound through separate receipts. Six checks passed; failed attempts remain explicit. Parsed HTML is not browser/layout inspection. Canonical save and publication remain subsequent.
- Historical root reading receipt, recorded 2026-10-16T00:29:56.490975+00:00: Root read both complete canonical YAML files after writing, complete report Markdown (recovered truncated FLOW07–20 block), complete CREATE history, current report metadata, three identity/no-match context changes and complete changed owner909 including all eight citations/root dispositions. Root previously read the three inherited governance blocks, all six404 questions/seven responsibility attachments and all33 normalized406 questions and exact recoverable source payloads; actual report/write/decision registry equality and 44 capture hashes independently rechecked after capture. This is not full manual reading of 912 unchanged main or394 nested objects nor every repeated raw provenance occurrence. Root read actual scientific correspondence audit with105 checks and independent output audit189checks; no finding remains. Prior full primary reading and mathematical checks remain separately attributed; source-version caveat retained. Later logs establish six check completions; save remains subsequent.
- Four ignored/hidden-inclusive scans, all1230prior IDs/names/aliases/scoped synonyms and current913main394nested recursive queries; all665distinctcontents read across team, root440–664 and selected exact node/neighborhood projections. No unbounded novelty or saturation claim.
- The inspected 2017 Soft Q main/supplement and 2016 SVGD main/supplement support two distinct source-scoped methods; later code/arXiv artifacts remain context. Three original SoftQ citation objects and five SVGD bibliography questions remain exactly queryable under owner 909, with one scoped SVGD addition and seven pending questions. Current historical searches also recovered 33 pending source/accounting questions: 20 flow/consistency objects, three RL component objects, Spatial Sensitive Grad-CAM++, eight incidental bibliography/component-source questions, and one generic later-SAC version question. Issue 406 and the additive registry preserve them without declaring 33 novel concepts or appending main/nested rows. Existing TULA owner 42, topic/inference owners and maintained attribution methods remain explicitly distinguished. The normalizing-flow family question links to the specific Rezende–Mohamed citation without merging their scopes. Issue 402 triage and issue 404 research remain unresolved and exactly preserved; discovery is not exhausted.
- Both exact draft acceptances preceded their retained TEMP native validations; whole-second curation timestamps use an explicitly truncated start bound.
- Four defining main/supplement artifacts belong to two original works. The later SoftQ code and later SVGD arXiv v3 remain context only. The SVGD downloaded ZIP and extracted PDF have separate checksum roles.
- Issue 402 bibliography triage remains separately open predecessor governance. Earlier 397/398 and 352 restoration and LPGA corrections remain exact historical provenance; no prior repair or closure is repeated.
- Issue404 pending source responsibility H354-S1: {"candidate":"CRSAT source-defined cautious walk variant","comparison_owners":[{"candidate":"Additional UBCSAT search variants","index":296,"object_sha256_canonical_json":"b3ec47a4ae0681b5cd0cd9d82e16a09152cd4c0d09de14db3dceb8021f07a61f","pointer":"/full_owners/296","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}}],"concept_identity_established":false,"disposition":"pending_primary_source_identity_and_operational_reconciliation","followup_id":"H354-S1","new_record_required":false,"next_check":"Read original CSAT definitions and compare cautious positive/no-decrease/all-variable pools with the1995 probability branch; resolve whether pick is applied uniformly to both branches and retain any ambiguity. Decide represented variant versus separate identity only after that evidence.","original_question":{"blocks_hrsat_or_tsat_science":false,"followup_id":"H354-S1","identity_established":false,"label":"CRSAT source-defined cautious walk variant","new_concept_established":false,"pdf_pages":[3,4,5],"possible_owners":[296,298],"primary_source":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"question":"Reconcile the cautious candidate rule and probability-controlled focused branch with original CSAT and other maintained SAT selectors; preserve select/pick ambiguity rather than assume a new distinct identity.","record_count_implied":false,"source_spelling":"CRSAT","status":"pending_source_identity_and_owner_reconciliation","url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"},"original_question_sha256_canonical_json":"375e19d0eaa52710dfdd2925e964a5f8d9c5f588a849948c474cd8f673f3a03d","other_ownership_assessment":"Owner270 is an umbrella local-search family and does not preserve these selector/source questions precisely. Owner301 has a separate GWSAT sampling-version question and must not be discharged or overwritten.","owner_attachment_state":"responsibility_assigned_for_future_inspection","owner_attachments":[{"owner":{"candidate":"Additional GenSAT selection and initialization variants","index":298,"object_sha256_canonical_json":"ade6ee0e5c875afd4044fd18a2082adc237626b3b36c4935a33f3e8a25b383d3","pointer":"/full_owners/298","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"primary source-family research attachment","status":"responsibility_assigned_research_pending"}],"ownership_rationale":"CRSAT is explicitly introduced as the random-walk composition of cautious CSAT in the1995 continuation of GenSAT. Owner298 already names CSAT and separates candidate selection from picking and initialization. It is the closest existing source-family research owner; owner296 provides the archival-source and HRSAT/HWSAT version comparison. This attachment does not establish CRSAT as a distinct record.","primary_existing_owner_index":298,"primary_scoped_owner_indexes":[{"owner_index":298,"scope":"primary source-family research attachment"}],"research_resolved":false,"responsibility_scope":"future_primary_source_inspection_only_not_method_identity_or_completion","secondary_context_owner_roles":[{"owner_index":296,"role":"secondary_source_family_or_maintained_method_comparison"}],"source":{"artifact":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"passage_bindings":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/origin-source-passages.json","sha256":"e6da50683ebf232d5cad782df05517d4600d6a66701a77b8b42b5d164a1043f3"},"physical_pdf_pages":[3,4,5],"url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"}}
- Issue404 pending source responsibility H354-S2: {"candidate":"TRSAT source-defined timid walk variant","comparison_owners":[{"candidate":"Additional UBCSAT search variants","index":296,"object_sha256_canonical_json":"b3ec47a4ae0681b5cd0cd9d82e16a09152cd4c0d09de14db3dceb8021f07a61f","pointer":"/full_owners/296","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}}],"concept_identity_established":false,"disposition":"pending_primary_source_identity_and_operational_reconciliation","followup_id":"H354-S2","new_record_required":false,"next_check":"Compare the original timid least-positive-gain rule and its no-decrease/all-variable fallbacks with the1995 focused composition. Preserve selector/picker ambiguity and do not transfer1997 tabu tenure, aspiration or implementation conventions.","original_question":{"blocks_hrsat_or_tsat_science":false,"followup_id":"H354-S2","identity_established":false,"label":"TRSAT source-defined timid walk variant","new_concept_established":false,"pdf_pages":[3,4,5],"possible_owners":[296,298],"primary_source":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"question":"Reconcile the timid candidate rule and focused branch with original timid TSAT; do not confuse it with1997 tabu TSAT or assume the abbreviation proves identity.","record_count_implied":false,"source_spelling":"TRSAT","status":"pending_source_identity_and_owner_reconciliation","url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"},"original_question_sha256_canonical_json":"fd52ee53bb5bf701d940c2d8e5f1eb083fefc2439cce5cbd31dbe8b3e82c22a5","other_ownership_assessment":"AIMech:TabuSearchForSAT is a comparison exclusion, not a resolution of this timid-source question; owner270 is broader context only.","owner_attachment_state":"responsibility_assigned_for_future_inspection","owner_attachments":[{"owner":{"candidate":"Additional GenSAT selection and initialization variants","index":298,"object_sha256_canonical_json":"ade6ee0e5c875afd4044fd18a2082adc237626b3b36c4935a33f3e8a25b383d3","pointer":"/full_owners/298","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"primary source-family research attachment","status":"responsibility_assigned_research_pending"}],"ownership_rationale":"TRSAT explicitly composes the earlier timid TSAT hill-climbing choice with the1995 focused branch. Owner298 names timid TSAT and warns against the later tabu acronym. Owner296 now owns the1997 fixed-FIFO record but explicitly delegates timid TSAT to298, supporting a primary298 attachment.","primary_existing_owner_index":298,"primary_scoped_owner_indexes":[{"owner_index":298,"scope":"primary source-family research attachment"}],"research_resolved":false,"responsibility_scope":"future_primary_source_inspection_only_not_method_identity_or_completion","secondary_context_owner_roles":[{"owner_index":296,"role":"secondary_source_family_or_maintained_method_comparison"}],"source":{"artifact":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"passage_bindings":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/origin-source-passages.json","sha256":"e6da50683ebf232d5cad782df05517d4600d6a66701a77b8b42b5d164a1043f3"},"physical_pdf_pages":[3,4,5],"url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"}}
- Issue404 pending source responsibility H354-S3: {"candidate":"DRSAT source-defined deterministic fair-pick walk variant","comparison_owners":[{"candidate":"Additional UBCSAT search variants","index":296,"object_sha256_canonical_json":"b3ec47a4ae0681b5cd0cd9d82e16a09152cd4c0d09de14db3dceb8021f07a61f","pointer":"/full_owners/296","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}}],"concept_identity_established":false,"disposition":"pending_primary_source_identity_and_operational_reconciliation","followup_id":"H354-S3","new_record_required":false,"next_check":"Read the original DSAT deterministic fairness construction, clarify state/tie/restart rules and determine the focused-branch composition from primary evidence. Do not infer an executable merely from the word fair or copy HRSAT behavior.","original_question":{"blocks_hrsat_or_tsat_science":false,"followup_id":"H354-S3","identity_established":false,"label":"DRSAT source-defined deterministic fair-pick walk variant","new_concept_established":false,"pdf_pages":[3,4,5],"possible_owners":[296,298],"primary_source":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"question":"Inspect the deterministic fair picker and its composition with the focused branch against original DSAT; establish operational convention and identity before any addition.","record_count_implied":false,"source_spelling":"DRSAT","status":"pending_source_identity_and_owner_reconciliation","url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"},"original_question_sha256_canonical_json":"0121601b25753fbc759cb5dda9fa317d634d23d7d7e51c40652620597adbc2a0","other_ownership_assessment":"Deterministic fair picking is not automatically HSAT least-recent-flip history, tabu exclusion or a stochastic-uniform picker. Broad owner270 does not settle the operational rule.","owner_attachment_state":"responsibility_assigned_for_future_inspection","owner_attachments":[{"owner":{"candidate":"Additional GenSAT selection and initialization variants","index":298,"object_sha256_canonical_json":"ade6ee0e5c875afd4044fd18a2082adc237626b3b36c4935a33f3e8a25b383d3","pointer":"/full_owners/298","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"primary source-family research attachment","status":"responsibility_assigned_research_pending"}],"ownership_rationale":"DRSAT combines DSAT’s deterministic fair picker with the1995 walk extension. Owner298 already names DSAT and explicitly owns picking/selection variants. Source-catalog owner296 is a secondary provenance/version comparator; no extra frontier row is needed to retain the pending question.","primary_existing_owner_index":298,"primary_scoped_owner_indexes":[{"owner_index":298,"scope":"primary source-family research attachment"}],"research_resolved":false,"responsibility_scope":"future_primary_source_inspection_only_not_method_identity_or_completion","secondary_context_owner_roles":[{"owner_index":296,"role":"secondary_source_family_or_maintained_method_comparison"}],"source":{"artifact":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"passage_bindings":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/origin-source-passages.json","sha256":"e6da50683ebf232d5cad782df05517d4600d6a66701a77b8b42b5d164a1043f3"},"physical_pdf_pages":[3,4,5],"url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"}}
- Issue404 pending source responsibility H354-S4: {"candidate":"CHRSAT cautious history-pick walk variant","comparison_owners":[{"candidate":"Additional UBCSAT search variants","index":296,"object_sha256_canonical_json":"b3ec47a4ae0681b5cd0cd9d82e16a09152cd4c0d09de14db3dceb8021f07a61f","pointer":"/full_owners/296","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}}],"concept_identity_established":false,"disposition":"pending_primary_source_identity_and_operational_reconciliation","followup_id":"H354-S4","new_record_required":false,"next_check":"Compare cautious pools, the1995 history selector, CHSAT no-walk endpoint and unrestricted/restricted triggers. Determine if CHRSAT is a separate concept or an internal supported variant while retaining select/pick versus generic-random-walk ambiguity.","original_question":{"blocks_hrsat_or_tsat_science":false,"followup_id":"H354-S4","identity_established":false,"label":"CHRSAT cautious history-pick walk variant","new_concept_established":false,"pdf_pages":[8],"possible_owners":[296,298],"primary_source":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"question":"Reconcile cautious hill-climbing plus the HRSAT picking method and the CHSAT no-walk comparison. Determine whether this is a separate concept, scoped variant or existing-owner sublead.","record_count_implied":false,"source_spelling":"CHRSAT","status":"pending_source_identity_and_owner_reconciliation","url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"},"original_question_sha256_canonical_json":"59ea0a89b01ff1b8d4b23a1dbf667d4c14691eddc956a37bbda68257822a7c59","other_ownership_assessment":"The CHSAT comparison is retained inside this same question, not counted as a sixth named issue form or an additional established concept. Owner270 is broader context only.","owner_attachment_state":"responsibility_assigned_for_future_inspection","owner_attachments":[{"owner":{"candidate":"Additional GenSAT selection and initialization variants","index":298,"object_sha256_canonical_json":"ade6ee0e5c875afd4044fd18a2082adc237626b3b36c4935a33f3e8a25b383d3","pointer":"/full_owners/298","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"primary source-family research attachment","status":"responsibility_assigned_research_pending"}],"ownership_rationale":"CHRSAT combines CSAT cautious candidate selection with HRSAT history picking and compares a CHSAT no-walk endpoint. Its unresolved source-family dimension belongs with owner298’s CSAT/selector/picker variants. Owner296 and AIMech:HRSAT are essential comparisons for the already represented history-plus-walk construction, not automatic aliases.","primary_existing_owner_index":298,"primary_scoped_owner_indexes":[{"owner_index":298,"scope":"primary source-family research attachment"}],"research_resolved":false,"responsibility_scope":"future_primary_source_inspection_only_not_method_identity_or_completion","secondary_context_owner_roles":[{"owner_index":296,"role":"secondary_source_family_or_maintained_method_comparison"}],"source":{"artifact":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"passage_bindings":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/origin-source-passages.json","sha256":"e6da50683ebf232d5cad782df05517d4600d6a66701a77b8b42b5d164a1043f3"},"physical_pdf_pages":[8],"url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"}}
- Issue404 pending source responsibility H354-S5: {"candidate":"JumpSAT multiple-clause jump variant","comparison_owners":[{"candidate":"Additional GenSAT selection and initialization variants","index":298,"object_sha256_canonical_json":"ade6ee0e5c875afd4044fd18a2082adc237626b3b36c4935a33f3e8a25b383d3","pointer":"/full_owners/298","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},{"candidate":"Local search","index":270,"object_sha256_canonical_json":"03c1f90e4934557856fb2ec201458a4408cd311af19e0b55c5824dfbe1c89059","pointer":"/full_owners/270","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}}],"concept_identity_established":false,"disposition":"pending_primary_source_identity_and_operational_reconciliation","followup_id":"H354-S5","new_record_required":false,"next_check":"Inspect exact multi-clause variable selection, duplicate-variable handling, simultaneous versus sequential updates, and clause-state timing. Assess unrestricted and improvement-gated jump policies separately. The source statement that all previously false clauses become satisfied is not accepted as an unconditional guarantee from the incomplete description.","original_question":{"blocks_hrsat_or_tsat_science":false,"followup_id":"H354-S5","identity_established":false,"label":"JumpSAT multiple-clause jump variant","new_concept_established":false,"pdf_pages":[8,9],"possible_owners":[296,298,270],"primary_source":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"question":"Inspect the one-variable-from-each-unsatisfied-clause jump and its selection/update semantics, including overlapping variables and the unrestricted versus improvement-gated versions; do not infer a full executable or universal success.","record_count_implied":false,"source_spelling":"JumpSAT","status":"pending_source_identity_and_owner_reconciliation","url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"},"original_question_sha256_canonical_json":"fa84c156411ca08f9730ad1de71448bcded4c850d68729eb380de9b9ac9c2787","other_ownership_assessment":"Owner298 is relevant comparison for the single-flip GenSAT/GRSAT lineage but its existing selection-and-initialization scope does not, without expansion, cover an arbitrary multiple-variable transition. Owner270 supplies broader SLS context; it is too general as the primary source-question home.","owner_attachment_state":"responsibility_assigned_for_future_inspection","owner_attachments":[{"owner":{"candidate":"Additional UBCSAT search variants","index":296,"object_sha256_canonical_json":"b3ec47a4ae0681b5cd0cd9d82e16a09152cd4c0d09de14db3dceb8021f07a61f","pointer":"/full_owners/296","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"primary source-family research attachment","status":"responsibility_assigned_research_pending"}],"ownership_rationale":"JumpSAT is described as a GRSAT-related multiple-clause jump rather than one candidate variable selected and flipped by the printed GenSAT driver. Owner296’s additional SAT-source catalogue is a suitable explicit pending-source owner because it already follows the same archived1995 source and method/version discrepancies. This does not assert that JumpSAT is implemented or registered in UBCSAT.","primary_existing_owner_index":296,"primary_scoped_owner_indexes":[{"owner_index":296,"scope":"primary source-family research attachment"}],"research_resolved":false,"responsibility_scope":"future_primary_source_inspection_only_not_method_identity_or_completion","secondary_context_owner_roles":[{"owner_index":298,"role":"secondary_source_family_or_maintained_method_comparison"},{"owner_index":270,"role":"broader_local_search_context_only"}],"source":{"artifact":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"passage_bindings":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/origin-source-passages.json","sha256":"e6da50683ebf232d5cad782df05517d4600d6a66701a77b8b42b5d164a1043f3"},"physical_pdf_pages":[8,9],"url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"}}
- Issue404 pending source responsibility H354-S6: {"candidate":"Restricted-walk trigger policy in CHRSAT and JumpSAT","comparison_owners":[{"candidate":"Local search","index":270,"object_sha256_canonical_json":"03c1f90e4934557856fb2ec201458a4408cd311af19e0b55c5824dfbe1c89059","pointer":"/full_owners/270","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}}],"concept_identity_established":false,"disposition":"pending_primary_source_identity_and_operational_reconciliation","followup_id":"H354-S6","new_record_required":false,"next_check":"For both named procedures, compare a walk/jump permitted at every step with a version allowed only when no strictly improving hill-climbing move is available. Clarify neutral-move treatment, selector/picker composition and whether this is an internal control dimension or warrants separate identity. Do not infer an extra record count.","original_question":{"blocks_hrsat_or_tsat_science":false,"followup_id":"H354-S6","identity_established":false,"label":"Restricted-walk trigger policy in CHRSAT and JumpSAT","new_concept_established":false,"pdf_pages":[8,9],"possible_owners":[296,298],"primary_source":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"question":"Retain the explicit policy difference between allowing focused moves on every step and allowing them only without an improving move. Determine whether this is an internal variant dimension or a separately owned identity; it is not a sixth named algorithm.","record_count_implied":false,"source_spelling":"walk only when hill climbing is not possible","status":"pending_source_identity_and_owner_reconciliation","url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"},"original_question_sha256_canonical_json":"aa4d40e0cfe3364dca424d9b18eb1574771995bb0382efb6660810557320ffd9","other_ownership_assessment":"Owner270 provides the generic improvement/non-improvement context only. Owner301’s independent GWSAT sampling-distribution question remains unchanged and unresolved.","owner_attachment_state":"responsibility_assigned_for_future_inspection","owner_attachments":[{"owner":{"candidate":"Additional GenSAT selection and initialization variants","index":298,"object_sha256_canonical_json":"ade6ee0e5c875afd4044fd18a2082adc237626b3b36c4935a33f3e8a25b383d3","pointer":"/full_owners/298","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"CHRSAT trigger-policy branch","status":"responsibility_assigned_research_pending"},{"owner":{"candidate":"Additional UBCSAT search variants","index":296,"object_sha256_canonical_json":"b3ec47a4ae0681b5cd0cd9d82e16a09152cd4c0d09de14db3dceb8021f07a61f","pointer":"/full_owners/296","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"JumpSAT trigger-policy branch","status":"responsibility_assigned_research_pending"}],"ownership_rationale":"This is one cross-cutting trigger-policy question, not a sixth named algorithm. Attach the CHRSAT branch to298 and the JumpSAT branch to296, using the same followup_id and source question. Distinct scoped attachments avoid forcing the multiple-variable JumpSAT mechanism into owner298 or duplicating a policy question.","primary_existing_owner_index":null,"primary_scoped_owner_indexes":[{"owner_index":298,"scope":"CHRSAT trigger-policy branch"},{"owner_index":296,"scope":"JumpSAT trigger-policy branch"}],"research_resolved":false,"responsibility_scope":"future_primary_source_inspection_only_not_method_identity_or_completion","secondary_context_owner_roles":[{"owner_index":270,"role":"broader_local_search_context_only"}],"source":{"artifact":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"passage_bindings":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/origin-source-passages.json","sha256":"e6da50683ebf232d5cad782df05517d4600d6a66701a77b8b42b5d164a1043f3"},"physical_pdf_pages":[8,9],"url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"}}
- Incidental historical pointers and bibliography/source questions remain pending. Existing record or owner links are context, not equivalence or proof of completed source research. No new concept, frontier row, primary-source reading, or issue closure is asserted by this accounting. Registry SHA256: 859f88842f9e932a6656ac9b9cea2130a29fca38d478c7cfa36d7a9ad48c5de3.
- Incidental source-accounting issue remains open for research: https://github.com/CultureBotAI/AIMech/issues/406. No closure is performed by this cohort.
- H355-FLOW-01: Laplacian multiscale flow matching. Status: pending_inspection. Related record context: AIMech:FlowMatching. Related owner context: . Next check: Resolve primary source identity, inspect the full defining method and compare mechanism/scope with existing records; evidence-only or application-only items need not become new concept records. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/0; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 4a6d39afb18173f978ffe8c00afcc6478c495e14d2283c10579d201777875e2d.
- H355-FLOW-02: Fisher flow matching. Status: pending_inspection. Related record context: AIMech:FlowMatching. Related owner context: . Next check: Resolve primary source identity, inspect the full defining method and compare mechanism/scope with existing records; evidence-only or application-only items need not become new concept records. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/1; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 bd06b0e49d2c960c9e2f2d6470d2807e95ca1e120c12f6813eecf423c8f1b187.
- H355-FLOW-03: Functional rectified flow. Status: pending_inspection. Related record context: AIMech:RectifiedFlow. Related owner context: . Next check: Resolve primary source identity, inspect the full defining method and compare mechanism/scope with existing records; evidence-only or application-only items need not become new concept records. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/2; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 6fa62e21445c1fbe554b669a03e1cacc922bcb5fcc5007c2a051ca7f20c22da1.
- H355-FLOW-04: Consistency-model convergence conditions. Status: pending_inspection. Related record context: AIMech:ConsistencyModel. Related owner context: . Next check: Resolve primary source identity, inspect the full defining method and compare mechanism/scope with existing records; evidence-only or application-only items need not become new concept records. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/3; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 02ad182ac3ab3b9986669b09af9c4c577bb97a499d9e0f72d605a80d2589a92a.
- H355-FLOW-05: Manifold-aligned consistency tangents. Status: pending_inspection. Related record context: AIMech:ConsistencyModel. Related owner context: . Next check: Resolve primary source identity, inspect the full defining method and compare mechanism/scope with existing records; evidence-only or application-only items need not become new concept records. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/4; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 cc6a7aa117e44cb45c018ce8e314748513798845c108ad777a4148127726cc36.
- H355-FLOW-06: Biological flow-matching applications. Status: pending_inspection. Related record context: AIMech:FlowMatching. Related owner context: . Next check: Resolve primary source identity, inspect the full defining method and compare mechanism/scope with existing records; evidence-only or application-only items need not become new concept records. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/5; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 236953ebf1b0c33832a7ec7a27428b7757c484255af74d482ecf241dcd275fc3.
- H355-FLOW-07: Variational rectified flow matching. Status: pending_inspection. Related record context: AIMech:FlowMatching. Related owner context: . Next check: Resolve primary source identity, inspect the full defining method and compare mechanism/scope with existing records; evidence-only or application-only items need not become new concept records. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/6; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 2d6306f1f628db0114c7de2372c1bcdacaf03d4e963aa2e29248d97e8d6b9044.
- H355-FLOW-08: Coreset-induced conditional velocity flow matching. Status: pending_inspection. Related record context: AIMech:FlowMatching. Related owner context: . Next check: Resolve primary source identity, inspect the full defining method and compare mechanism/scope with existing records; evidence-only or application-only items need not become new concept records. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/7; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 efa83a10ba3b1e6d0926fb936ae95ccf14f9cee6cbe5e538f2c562dd82bff8e1.
- H355-FLOW-09: Isokinetic flow matching. Status: pending_inspection. Related record context: AIMech:FlowMatching. Related owner context: . Next check: Resolve primary source identity, inspect the full defining method and compare mechanism/scope with existing records; evidence-only or application-only items need not become new concept records. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/8; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 ab47f7af627dc0cb39aaa4cce38cb8527c9e22ea0a81598333a075bd3aa48950.
- H355-FLOW-10: FLOWALIGN. Status: pending_inspection. Related record context: AIMech:FlowMatching. Related owner context: . Next check: Resolve primary source identity, inspect the full defining method and compare mechanism/scope with existing records; evidence-only or application-only items need not become new concept records. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/9; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 da310d8da81dfd9c8d4cc54934bd6df5c69603d22cc75100bbc1706f2bc491d0.
- H355-FLOW-11: ReQFlow. Status: pending_inspection. Related record context: AIMech:RectifiedFlow. Related owner context: . Next check: Resolve primary source identity, inspect the full defining method and compare mechanism/scope with existing records; evidence-only or application-only items need not become new concept records. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/10; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 3bf821a75e665e361b78cd17a2d49aa2c2716242c71a2115ffa9171d2e46e47b.
- H355-FLOW-12: RF-Physical / RF-FWD. Status: pending_inspection. Related record context: AIMech:RectifiedFlow. Related owner context: . Next check: Resolve primary source identity, inspect the full defining method and compare mechanism/scope with existing records; evidence-only or application-only items need not become new concept records. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/11; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 4aa56509645dcb3fa92d070c9032ba875d8ada427ff9819bad746d2488b9cd7e.
- H355-FLOW-13: Unresolved ICLR 2026 conditional-flow relation source. Status: pending_inspection. Related record context: AIMech:FlowMatching. Related owner context: . Next check: Resolve primary source identity, inspect the full defining method and compare mechanism/scope with existing records; evidence-only or application-only items need not become new concept records. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/12; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 00e3b109d013645c9cd0f69c7fc9e4ac9d79482af887b5aaa1bcdb5c3c396103.
- H355-FLOW-14: Conditional flow matching and OT conditional flow matching. Status: pending_inspection. Related record context: AIMech:FlowMatching, AIMech:RectifiedFlow. Related owner context: . Next check: Determine whether named objectives merit separately scoped methods rather than aliases for the general framework. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/13; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 69a91404238fa8725cd4e374690e0aae5c1d5e1bf98abe5387cf8ffe7c6c053b.
- H355-FLOW-15: Consistency training and consistency distillation. Status: pending_inspection. Related record context: AIMech:ConsistencyModel, AIMech:ImprovedConsistencyTraining. Related owner context: . Next check: Assess standalone procedure identities, preserving the EMA-theory correction for the original CT variant. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/14; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 55dd8c121ec319e972285d31e8878cf30ffc64b68189cba66d0fd03c4e9fcb95.
- H355-FLOW-16: Gradient-constrained rectification. Status: pending_inspection. Related record context: AIMech:RectifiedFlow. Related owner context: . Next check: Inspect the original defining method and retain support/regularity counterexamples, without promoting straightness to optimal transport. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/15; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 b2c9e705f06bab67e3ebc69d0bc977ba88eceb5c270ac9d242af9cbbbae23418.
- H355-FLOW-17: Normalizing flows, continuous normalizing flows and probability-flow ODEs. Status: pending_inspection. Related record context: AIMech:FlowMatching, AIMech:RectifiedFlow, AIMech:ConsistencyModel. Related owner context: planned_owner909/svgd_bibliography_4. Next check: Read original definitions, distinguish model families from differential-equation constructions, and search AIO identities. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/16; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 d62687cddf2304d85467fd317c4c9760b06b749dd7cc822e6dd4b7ae5313175b.
- H355-FLOW-18: Pseudo-Huber discrepancy and LPIPS. Status: pending_inspection. Related record context: AIMech:ImprovedConsistencyTraining. Related owner context: . Next check: Decide on mathematical-method/evaluation-method scope and inspect original definitions rather than import a name from a training paper. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/17; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 d6fe8b871ece43c62d89e21f3459be1c3586c5b1eda9572dbd4ee1b1d6a16bc2.
- H355-FLOW-19: DDIM, DPM-Solver, DEIS, UniPC, TRACT, Diff-Instruct and BOOT. Status: pending_inspection. Related record context: AIMech:ImprovedConsistencyTraining. Related owner context: . Next check: Only names were used as leads; inspect each defining paper before a record, and do not infer performance from the extracted table. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/18; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 841720635ef3f85c37e8469dd82f3f349a0d5c1135cf0ade430d5f839f7ec577.
- H355-FLOW-20: Consistency Flow Matching. Status: pending_inspection. Related record context: AIMech:FlowMatching. Related owner context: . Next check: Re-search the exact primary title/source before identity or method assertions. Access scope: Historical pointer and neighboring record context only; original source identity, narrower ownership and method/application/evidence scope remain pending. No primary reading or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/19; ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b; payload SHA256 52d4ef7359116fc1c7e4a19ca21253a08ec6ee75cb52927ba66aeadc10879360.
- H355-R1: Deterministic policy gradient. Status: pending_inspection. Related record context: AIMech:DeepDeterministicPolicyGradient. Related owner context: . Next check: Resolve exact identity and representation scope against both collections, then inspect the primary defining source; a shared component or related method is not automatically a new record. Access scope: Historical discovery object, saved-review boundary and current record text inspected; no new original-primary-method reading or separate concept assertion. Exact source question: /private/tmp/aimech-cohort355-context220-439-20261016/pending-questions.json#/0; ledger SHA256 b531fd652aad7a8baeca6fa4b747b58ec7a397ac598c1709000bd9bc6040144c; payload SHA256 94cb21f31b9f7ab8b6b9943f5647bcc7663685a4d846b8f0c34850056ce42a56.
- H355-R2: Experience replay. Status: pending_inspection. Related record context: AIMech:DeepDeterministicPolicyGradient, AIMech:DeepQNetwork. Related owner context: . Next check: Resolve exact identity and representation scope against both collections, then inspect the primary defining source; a shared component or related method is not automatically a new record. Access scope: Historical discovery object, saved-review boundary and current record text inspected; no new original-primary-method reading or separate concept assertion. Exact source question: /private/tmp/aimech-cohort355-context220-439-20261016/pending-questions.json#/1; ledger SHA256 b531fd652aad7a8baeca6fa4b747b58ec7a397ac598c1709000bd9bc6040144c; payload SHA256 78deff07777c5d17bb3953885b84f575f90e62dc54e07692fdc6e6347e0d6a5e.
- H355-R3: Target network. Status: pending_inspection. Related record context: AIMech:DeepDeterministicPolicyGradient, AIMech:DeepQNetwork. Related owner context: . Next check: Resolve exact identity and representation scope against both collections, then inspect the primary defining source; a shared component or related method is not automatically a new record. Access scope: Historical discovery object, saved-review boundary and current record text inspected; no new original-primary-method reading or separate concept assertion. Exact source question: /private/tmp/aimech-cohort355-context220-439-20261016/pending-questions.json#/2; ledger SHA256 b531fd652aad7a8baeca6fa4b747b58ec7a397ac598c1709000bd9bc6040144c; payload SHA256 6fbf4a5f6da3720234fab4ff805e596a47f424ebfdbd4a7d3f1f68e87a6adbd6.
- H355-SCI-H1: Spatial Sensitive Grad-CAM++. Status: pending_inspection. Related record context: AIMech:GradCAM, AIMech:GuidedGradCAM. Related owner context: . Next check: Locate the exact CVF2024 workshop source named by the original historical pointer, compare its mechanism and aliases against GradCAM and GuidedGradCAM and other attribution variants, and retain an explicit pending or supported existing-owner disposition. Shared Grad-CAM wording is not an identity decision. Access scope: An explicit historical pending object, visible through a later embedded identity-search result. The original method itself has not been read. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/0; ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527; payload SHA256 36b9bb9e0881a73d4af8bdc12d92f2a7bde5fede9490129ae702dae4457b7bb3.
- H355-SCI-B1: Nonparametric empirical Bayes for the Dirichlet process mixture model. Status: pending_inspection. Related record context: AIMech:LatentDirichletAllocation, AIMech:BlackBoxVariationalInference. Related owner context: /prior_frontier_accounting/425. Next check: The existing topic cohort explicitly retains DP variational inference and HDP/nested-CRP models, but does not explicitly resolve this empirical-Bayes source. Determine whether its estimand/procedure is already represented or belongs within that cohort. Access scope: Previously retained search output only, newly reconciled now. No original method reading, novelty decision or full source validation. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/1; ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527; payload SHA256 0eac3087b2678a4bb91287c6ad8e01733847e29d2a9b4651d39f7d4c9d147397.
- H355-SCI-B2: Probabilistic Models of Text and Images (Blei 2004 thesis). Status: pending_inspection. Related record context: AIMech:LatentDirichletAllocation. Related owner context: /prior_frontier_accounting/425. Next check: This thesis is a discovery source, not one established new method. Compare its chapters with existing LDA and pending annotated/cross-modal sources; retain only distinct, evidenced methods or version questions after reading. Access scope: Previously retained search output only, newly reconciled now. No original method reading, novelty decision or full source validation. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/2; ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527; payload SHA256 a0478d0c711e831a5a3ce42edf3e68ee9991a55d8d419d2ed2c0613464454734.
- H355-SCI-B3: Hierarchical Bayesian models for applications in information retrieval. Status: pending_inspection. Related record context: AIMech:LatentDirichletAllocation. Related owner context: /prior_frontier_accounting/425. Next check: The Blei–Ng–Jordan chapter may overlap existing LDA evidence. Read and compare the actual chapter before deciding source-only duplication, evidence extension or distinct mechanism; broad title similarity is insufficient. Access scope: Previously retained search output only, newly reconciled now. No original method reading, novelty decision or full source validation. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/3; ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527; payload SHA256 a0e2d0b0b3d2c6878118c0a53cde4b0d03eb9bab2e54176870889e8475352feb.
- H355-SCI-B4: Predicting the performance of linearly combined IR systems. Status: pending_inspection. Related record context: . Related owner context: /prior_frontier_accounting/468. Next check: The nearest retrieval cohort concerns query likelihood and document expansion, not an established account of this combination-performance source. Establish the original reference and whether it defines a reusable AI procedure, an evaluation theory or merely contextual evidence. Access scope: Previously retained search output only, newly reconciled now. No original method reading, novelty decision or full source validation. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/4; ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527; payload SHA256 21a68ac7428177b09dbbf93f6bdee48e9df409b7b0ae752e0a738ce30844732d.
- H355-SCI-B5: A Similarity-based Probability Model for Latent Semantic Indexing. Status: pending_inspection. Related record context: AIMech:ProbabilisticLatentSemanticAnalysis. Related owner context: /prior_frontier_accounting/421. Next check: The retained SIGIR listing gives a title only. Resolve its source/authors and compare with PLSA, SVD-LSI and the existing dyadic-clustering owner before assigning an owner or claiming distinctness. Access scope: Previously retained search output only, newly reconciled now. No original method reading, novelty decision or full source validation. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/5; ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527; payload SHA256 39b50214f53e4a89e979f8cafd18234745689a9538656dd4320112bc8dca8161.
- H355-SCI-B6: A Hierarchical Model for Clustering and Categorising Documents. Status: pending_inspection. Related record context: AIMech:LatentDirichletAllocation. Related owner context: /prior_frontier_accounting/425, /prior_frontier_accounting/490, /prior_frontier_accounting/491. Next check: The source is a third-party bibliography snippet. Compare the actual 2002 paper with current annotated/nonparametric topics and distinct owners490/491; those owners name different later sources and do not establish identity. Access scope: Previously retained search output only, newly reconciled now. No original method reading, novelty decision or full source validation. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/6; ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527; payload SHA256 d88b882890c2a6a9d9070165f547a8e8123f328500a4bfb2c6b3cf8973d9a74b.
- H355-SCI-B7: Variational Inference: a review for statisticians. Status: pending_inspection. Related record context: AIMech:BlackBoxVariationalInference, AIMech:FullyFactorizedMeanFieldInference, AIMech:VariationalExpectationMaximization. Related owner context: /prior_frontier_accounting/426. Next check: This secondary biographical snippet identifies a review source. Resolve the actual version and use its cited originals for bounded discovery; do not add a record for the review title or treat generic VI records as an explicit disposition. Access scope: Previously retained search output only, newly reconciled now. No original method reading, novelty decision or full source validation. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/7; ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527; payload SHA256 ce4a9fb1c042cca1f34944c8f6047e7cddbda5c72563dcd4f72d46e52272d362.
- H355-SCI-B8: Foundational TF-IDF term weighting and Salton–McGill1983 source scope. Status: pending_inspection. Related record context: AIMech:UnsupervisedDataAugmentation, AIMech:ExponentialFamilyHarmonium. Related owner context: /prior_frontier_accounting/140. Next check: Owner140 explicitly covers TF-IDF word replacement for augmentation; maintained UDA uses that component and harmonium compares against TF-IDF retrieval. The foundational weighting/source identity is not explicitly resolved by those scoped uses. Inspect the original formulation/version and decide representation/component/owner scope without assuming a new algorithm. Access scope: Previously retained search output only, newly reconciled now. No original method reading, novelty decision or full source validation. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/8; ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527; payload SHA256 607032235a6edf33aea28b219e91b70b0e1243928c26c17f32114adadbbac782.
- H355-SAC-VERSION: Later SAC implementations: unspecified source/version. Status: pending_inspection. Related record context: AIMech:SoftActorCritic. Related owner context: . Next check: Identify the precise later SAC source/version and compare it with the maintained original2018 state-value formulation before deciding source enrichment, variant scope or distinct identity. Do not conflate this generic uncertainty with Soft Q-learning. Access scope: Historical review boundary appearing in groups49 and413 (with further embedded repetition) only; no specific later primary source or additional concept has been established. Exact source question: /private/tmp/aimech-cohort355-context220-439-20261016/selected-original-boundary-decisions.json#/1/boundary_decisions/1; ledger SHA256 5e0dfa47076bdf04d04bc01000d79f21516a7970ad1d64359011b0fb30d58061; payload SHA256 6e8ac4f7db6bec1e4ce6b68d982011edb6ee76ac6b00ba363a92442c0690d338.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T004059Z-soft-q-learning-and-stein-variational-gradient-descent
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of Soft Q-learning and Stein variational gradient descent
started_at: '2026-10-16T00:26:56.042079Z'
finished_at: '2026-10-16T00:40:59.313135Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Author self-review with separately attributed primary research,
    root reading and bounded supporting reasoning. Preparing this scaffold is not
    an independent scientific approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Separate issue404 accounting preserves six pending source questions and seven
  inspection-responsibility attachments; no issue closure is requested. Retain the
  source-defined Soft Q-learning control algorithm and SVGD particle inference algorithm
  as distinct DRAFT records. Eleven claims and fourteen limitations preserve exact
  versus approximate theory and source-version boundaries. Owner 909 groups their
  discovery with explicit non-equivalence and retained source questions. Actual canonical/capture/page
  evidence and six checks are verified. Inherited 402 triage and restoration provenance
  remain exact; no issue closure is requested.
source:
  git_revision: 008d1eafc23cb19605953fa860475256d1b28895
  state: working_tree
  inputs:
  - path: .claude/skills/review-category/SKILL.md
    sha256: 553c3870c1dfc127f90f196b7b212b644706d4c26e2a578ab615ccce588070d7
    role: context
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/KernelLayer.yaml
    sha256: 0723e7f15d57807a1f922cd87b878593fb167757c7429dd06e99bde723290d43
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/curated/BlackBoxVariationalInference.yaml
    sha256: 8237d3233ae06163b8fab5b4fa047ffc938e275bc1e3ede883348e06c2b266a8
    role: context
  - path: data/curated/ContrastiveDivergence.yaml
    sha256: 375d9a8cafc07b831743ac858a20bb33a08677e613cfce59773eeba644adc1c4
    role: context
  - path: data/curated/DeepDeterministicPolicyGradient.yaml
    sha256: 17a2f2205f1928697e5dac816484819fbbe7d23b67d3f5dce09c469790c970ec
    role: context
  - path: data/curated/DeepQNetwork.yaml
    sha256: ea346f5f8650c02e1d8d825c896797e3c022f20525d07b64b96f97ae96a1df2a
    role: context
  - path: data/curated/FlowMatching.yaml
    sha256: 3e7122ee85f438483256afcce7b4621b4701d10a0022b8efa1f0eb86c6a02887
    role: context
  - path: data/curated/FullyFactorizedMeanFieldInference.yaml
    sha256: 102be6f77143b26acb0d482f91e2dfa58ea113f2188b14b92067484cc4f9408d
    role: context
  - path: data/curated/MetropolisAdjustedLangevinAlgorithm.yaml
    sha256: 6e815be8054929061e44ef8ddd5a63c5b1361d8c518fb3ec5fd7f9bba884b6f7
    role: context
  - path: data/curated/QLearning.yaml
    sha256: bcbd0f51f46e91ba6d88c9dc84baa9656aef82282c5c56d887ca81ff5182eb95
    role: context
  - path: data/curated/RectifiedFlow.yaml
    sha256: 10025e94e6142cb77cc95f963afb4c5c70c96a7cdaac208a02420bd30245bd01
    role: context
  - path: data/curated/SoftActorCritic.yaml
    sha256: fd4dd468f1b4a139c0166eab39944608314e42e7cf4dc0f8d750d3cf4802fe85
    role: context
  - path: data/curated/SoftQLearning.yaml
    sha256: 30a9c92eac4e3169d040b64230b7efd6ec8d9685ea58cd5136f4a2d7fa895dca
    role: target
  - path: data/curated/SteinVariationalGradientDescent.yaml
    sha256: 306808b660d4ce0880599e6acc901c5352c8a92d3ed6db58f89bd2b3c107d2b0
    role: target
  - path: data/curated/StructuredMeanFieldInference.yaml
    sha256: 3cd31e539123908291c2a9a394792c52dacf415ce3c19c4d6a42e9be6173c86b
    role: context
  - path: data/curated/UnadjustedLangevinAlgorithm.yaml
    sha256: 4c09ef556111d807d01b68678691453752de613610bb23239c9480b90b8535eb
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
  - path: history/reports/soft-q-learning-and-stein-variational-gradient-descent/2026-10-16T002628Z-codex-1f51bf.yaml
    sha256: 9f4f5367fa502dcb576b57beeed3fe7e799e73a0fd3e9695f8200720355207b7
    role: context
  - path: justfile
    sha256: 2d9c1b68c1c80d53aa44a6b8b5e916efe8b493650ff59a3fc7479a42be37f400
    role: context
  - path: research/discovery/20261011T031353Z-optimization-graphs-rl-explanations.json
    sha256: 3ff14c6070c548dcc3785e8a4ac394c6d50392dd313a6625ba6dad4299a5c0d0
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
  - path: research/discovery/20261016T002614Z-soft-q-learning-and-stein-variational-gradient-descent.json
    sha256: 96f80b5598848c2418b5995938067dd03f4ccf33e8c1d80eedfd3422c3db386b
    role: context
  - path: research/discovery/20261016T002614Z-soft-q-learning-and-stein-variational-gradient-descent.md
    sha256: a2a5afe9e67e52e4786dc38a0ff1a7cc4b4e4e12b8b7df0af79d5e4a6963326b
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
  description: Complete selected two-record cohort in actual captured canonical state,
    plus source-question and inherited-governance preservation.
  selection: Exact source-defined Soft Q-learning and Stein variational gradient descent
    drafts.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - AIMech:SoftQLearning
  - AIMech:SteinVariationalGradientDescent
  exclusions:
  - target: Uninspected original citation methods and bibliography questions
    reason: Pending source questions do not assert missing concepts; fresh decisions
      must link existing records or responsible owners if found.
  - target: Inherited issue402 bibliography triage and earlier restoration repairs
    reason: Exact predecessor governance is preserved; no issue closure or additional
      frontier row is authorized.
checks:
- check_id: check-gate
  name: just check
  status: passed
  required: true
  summary: Actual successful command; exact output is retained.
  target_ids:
  - AIMech:SoftQLearning
  - AIMech:SteinVariationalGradientDescent
  command: just check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-gate
- check_id: check-vendor
  name: just vendored-check
  status: passed
  required: true
  summary: Actual successful command; exact output is retained.
  target_ids:
  - AIMech:SoftQLearning
  - AIMech:SteinVariationalGradientDescent
  command: just vendored-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-vendor
- check_id: check-check-source
  name: uv run --locked aimech check-source
  status: passed
  required: true
  summary: Actual successful command; exact output is retained.
  target_ids:
  - AIMech:SoftQLearning
  - AIMech:SteinVariationalGradientDescent
  command: uv run --locked aimech check-source
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-check-source
- check_id: check-render
  name: just render
  status: passed
  required: true
  summary: Actual successful command; exact output is retained.
  target_ids:
  - AIMech:SoftQLearning
  - AIMech:SteinVariationalGradientDescent
  command: just render
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-render
- check_id: check-render-check
  name: just render-check
  status: passed
  required: true
  summary: Actual successful command; exact output is retained.
  target_ids:
  - AIMech:SoftQLearning
  - AIMech:SteinVariationalGradientDescent
  command: just render-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-render-check
- check_id: check-diff
  name: git diff --check
  status: passed
  required: true
  summary: Actual successful command; exact output is retained.
  target_ids:
  - AIMech:SoftQLearning
  - AIMech:SteinVariationalGradientDescent
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-diff
- check_id: historical-check-attempt-1
  name: 'Historical attempt: just vendored-check'
  status: failed
  required: false
  summary: Retained failed attempt; actual successful replacement cited separately.
  target_ids:
  - AIMech:SoftQLearning
  - AIMech:SteinVariationalGradientDescent
  command: just vendored-check
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - historical-check-attempt-1
findings: []
actions: []
limitations:
- Historical research, root and supporting readings remain separately attributed;
  this review preparation adds no primary-page reading or algorithm execution.
- Soft Q-learning preserves exact-backup versus finite neural learning, action-measure,
  density, source-display and version limits. SVGD preserves population versus finite-particle,
  transform, source-display, finite-step and empirical limits.
- Four defining artifacts belong to two primary works. The pinned later SoftQ code
  and later SVGD arXiv v3 are two context artifacts, not two additional defining works.
  The downloaded supplement ZIP and its extracted PDF have distinct hashes.
- Both exact draft acceptances preceded their retained one-time TEMP native validations.
  Later canonical checks remain separately required.
- Owner909 groups two distinct concepts through source discovery; it does not assert
  equivalence, aliasing or subclass. Three original SoftQ citation entries and five
  SVGD bibliography questions remain recursively queryable.
- Inherited354 restoration and older352 provenance remain exact. Issue402 triage is
  separately preserved; no old repair or closure is repeated.
- Historical 783/442 identity evidence remains dated; actual current root decisions
  supply identity and mapping scope. Owner 909 remains partial; pending source questions
  retain existing identity/owner links when found and do not imply novel concepts.
- Actual five outputs, one CREATE history, 7 generated pages and 44 capture inputs
  are bound through separate receipts. Six checks passed; failed attempts remain explicit.
  Parsed HTML is not browser/layout inspection. Canonical save and publication remain
  subsequent.
tags:
- scientific-review
- self-review
- reinforcement-learning
- variational-inference
- citation-accounting
notes:
- 'Historical root reading receipt, recorded 2026-10-16T00:29:56.490975+00:00: Root
  read both complete canonical YAML files after writing, complete report Markdown
  (recovered truncated FLOW07–20 block), complete CREATE history, current report metadata,
  three identity/no-match context changes and complete changed owner909 including
  all eight citations/root dispositions. Root previously read the three inherited
  governance blocks, all six404 questions/seven responsibility attachments and all33
  normalized406 questions and exact recoverable source payloads; actual report/write/decision
  registry equality and 44 capture hashes independently rechecked after capture. This
  is not full manual reading of 912 unchanged main or394 nested objects nor every
  repeated raw provenance occurrence. Root read actual scientific correspondence audit
  with105 checks and independent output audit189checks; no finding remains. Prior
  full primary reading and mathematical checks remain separately attributed; source-version
  caveat retained. Later logs establish six check completions; save remains subsequent.'
- Four ignored/hidden-inclusive scans, all1230prior IDs/names/aliases/scoped synonyms
  and current913main394nested recursive queries; all665distinctcontents read across
  team, root440–664 and selected exact node/neighborhood projections. No unbounded
  novelty or saturation claim.
- 'The inspected 2017 Soft Q main/supplement and 2016 SVGD main/supplement support
  two distinct source-scoped methods; later code/arXiv artifacts remain context. Three
  original SoftQ citation objects and five SVGD bibliography questions remain exactly
  queryable under owner 909, with one scoped SVGD addition and seven pending questions.
  Current historical searches also recovered 33 pending source/accounting questions:
  20 flow/consistency objects, three RL component objects, Spatial Sensitive Grad-CAM++,
  eight incidental bibliography/component-source questions, and one generic later-SAC
  version question. Issue 406 and the additive registry preserve them without declaring
  33 novel concepts or appending main/nested rows. Existing TULA owner 42, topic/inference
  owners and maintained attribution methods remain explicitly distinguished. The normalizing-flow
  family question links to the specific Rezende–Mohamed citation without merging their
  scopes. Issue 402 triage and issue 404 research remain unresolved and exactly preserved;
  discovery is not exhausted.'
- Both exact draft acceptances preceded their retained TEMP native validations; whole-second
  curation timestamps use an explicitly truncated start bound.
- Four defining main/supplement artifacts belong to two original works. The later
  SoftQ code and later SVGD arXiv v3 remain context only. The SVGD downloaded ZIP
  and extracted PDF have separate checksum roles.
- Issue 402 bibliography triage remains separately open predecessor governance. Earlier
  397/398 and 352 restoration and LPGA corrections remain exact historical provenance;
  no prior repair or closure is repeated.
- 'Issue404 pending source responsibility H354-S1: {"candidate":"CRSAT source-defined
  cautious walk variant","comparison_owners":[{"candidate":"Additional UBCSAT search
  variants","index":296,"object_sha256_canonical_json":"b3ec47a4ae0681b5cd0cd9d82e16a09152cd4c0d09de14db3dceb8021f07a61f","pointer":"/full_owners/296","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}}],"concept_identity_established":false,"disposition":"pending_primary_source_identity_and_operational_reconciliation","followup_id":"H354-S1","new_record_required":false,"next_check":"Read
  original CSAT definitions and compare cautious positive/no-decrease/all-variable
  pools with the1995 probability branch; resolve whether pick is applied uniformly
  to both branches and retain any ambiguity. Decide represented variant versus separate
  identity only after that evidence.","original_question":{"blocks_hrsat_or_tsat_science":false,"followup_id":"H354-S1","identity_established":false,"label":"CRSAT
  source-defined cautious walk variant","new_concept_established":false,"pdf_pages":[3,4,5],"possible_owners":[296,298],"primary_source":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"question":"Reconcile
  the cautious candidate rule and probability-controlled focused branch with original
  CSAT and other maintained SAT selectors; preserve select/pick ambiguity rather than
  assume a new distinct identity.","record_count_implied":false,"source_spelling":"CRSAT","status":"pending_source_identity_and_owner_reconciliation","url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"},"original_question_sha256_canonical_json":"375e19d0eaa52710dfdd2925e964a5f8d9c5f588a849948c474cd8f673f3a03d","other_ownership_assessment":"Owner270
  is an umbrella local-search family and does not preserve these selector/source questions
  precisely. Owner301 has a separate GWSAT sampling-version question and must not
  be discharged or overwritten.","owner_attachment_state":"responsibility_assigned_for_future_inspection","owner_attachments":[{"owner":{"candidate":"Additional
  GenSAT selection and initialization variants","index":298,"object_sha256_canonical_json":"ade6ee0e5c875afd4044fd18a2082adc237626b3b36c4935a33f3e8a25b383d3","pointer":"/full_owners/298","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"primary
  source-family research attachment","status":"responsibility_assigned_research_pending"}],"ownership_rationale":"CRSAT
  is explicitly introduced as the random-walk composition of cautious CSAT in the1995
  continuation of GenSAT. Owner298 already names CSAT and separates candidate selection
  from picking and initialization. It is the closest existing source-family research
  owner; owner296 provides the archival-source and HRSAT/HWSAT version comparison.
  This attachment does not establish CRSAT as a distinct record.","primary_existing_owner_index":298,"primary_scoped_owner_indexes":[{"owner_index":298,"scope":"primary
  source-family research attachment"}],"research_resolved":false,"responsibility_scope":"future_primary_source_inspection_only_not_method_identity_or_completion","secondary_context_owner_roles":[{"owner_index":296,"role":"secondary_source_family_or_maintained_method_comparison"}],"source":{"artifact":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"passage_bindings":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/origin-source-passages.json","sha256":"e6da50683ebf232d5cad782df05517d4600d6a66701a77b8b42b5d164a1043f3"},"physical_pdf_pages":[3,4,5],"url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"}}'
- 'Issue404 pending source responsibility H354-S2: {"candidate":"TRSAT source-defined
  timid walk variant","comparison_owners":[{"candidate":"Additional UBCSAT search
  variants","index":296,"object_sha256_canonical_json":"b3ec47a4ae0681b5cd0cd9d82e16a09152cd4c0d09de14db3dceb8021f07a61f","pointer":"/full_owners/296","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}}],"concept_identity_established":false,"disposition":"pending_primary_source_identity_and_operational_reconciliation","followup_id":"H354-S2","new_record_required":false,"next_check":"Compare
  the original timid least-positive-gain rule and its no-decrease/all-variable fallbacks
  with the1995 focused composition. Preserve selector/picker ambiguity and do not
  transfer1997 tabu tenure, aspiration or implementation conventions.","original_question":{"blocks_hrsat_or_tsat_science":false,"followup_id":"H354-S2","identity_established":false,"label":"TRSAT
  source-defined timid walk variant","new_concept_established":false,"pdf_pages":[3,4,5],"possible_owners":[296,298],"primary_source":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"question":"Reconcile
  the timid candidate rule and focused branch with original timid TSAT; do not confuse
  it with1997 tabu TSAT or assume the abbreviation proves identity.","record_count_implied":false,"source_spelling":"TRSAT","status":"pending_source_identity_and_owner_reconciliation","url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"},"original_question_sha256_canonical_json":"fd52ee53bb5bf701d940c2d8e5f1eb083fefc2439cce5cbd31dbe8b3e82c22a5","other_ownership_assessment":"AIMech:TabuSearchForSAT
  is a comparison exclusion, not a resolution of this timid-source question; owner270
  is broader context only.","owner_attachment_state":"responsibility_assigned_for_future_inspection","owner_attachments":[{"owner":{"candidate":"Additional
  GenSAT selection and initialization variants","index":298,"object_sha256_canonical_json":"ade6ee0e5c875afd4044fd18a2082adc237626b3b36c4935a33f3e8a25b383d3","pointer":"/full_owners/298","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"primary
  source-family research attachment","status":"responsibility_assigned_research_pending"}],"ownership_rationale":"TRSAT
  explicitly composes the earlier timid TSAT hill-climbing choice with the1995 focused
  branch. Owner298 names timid TSAT and warns against the later tabu acronym. Owner296
  now owns the1997 fixed-FIFO record but explicitly delegates timid TSAT to298, supporting
  a primary298 attachment.","primary_existing_owner_index":298,"primary_scoped_owner_indexes":[{"owner_index":298,"scope":"primary
  source-family research attachment"}],"research_resolved":false,"responsibility_scope":"future_primary_source_inspection_only_not_method_identity_or_completion","secondary_context_owner_roles":[{"owner_index":296,"role":"secondary_source_family_or_maintained_method_comparison"}],"source":{"artifact":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"passage_bindings":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/origin-source-passages.json","sha256":"e6da50683ebf232d5cad782df05517d4600d6a66701a77b8b42b5d164a1043f3"},"physical_pdf_pages":[3,4,5],"url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"}}'
- 'Issue404 pending source responsibility H354-S3: {"candidate":"DRSAT source-defined
  deterministic fair-pick walk variant","comparison_owners":[{"candidate":"Additional
  UBCSAT search variants","index":296,"object_sha256_canonical_json":"b3ec47a4ae0681b5cd0cd9d82e16a09152cd4c0d09de14db3dceb8021f07a61f","pointer":"/full_owners/296","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}}],"concept_identity_established":false,"disposition":"pending_primary_source_identity_and_operational_reconciliation","followup_id":"H354-S3","new_record_required":false,"next_check":"Read
  the original DSAT deterministic fairness construction, clarify state/tie/restart
  rules and determine the focused-branch composition from primary evidence. Do not
  infer an executable merely from the word fair or copy HRSAT behavior.","original_question":{"blocks_hrsat_or_tsat_science":false,"followup_id":"H354-S3","identity_established":false,"label":"DRSAT
  source-defined deterministic fair-pick walk variant","new_concept_established":false,"pdf_pages":[3,4,5],"possible_owners":[296,298],"primary_source":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"question":"Inspect
  the deterministic fair picker and its composition with the focused branch against
  original DSAT; establish operational convention and identity before any addition.","record_count_implied":false,"source_spelling":"DRSAT","status":"pending_source_identity_and_owner_reconciliation","url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"},"original_question_sha256_canonical_json":"0121601b25753fbc759cb5dda9fa317d634d23d7d7e51c40652620597adbc2a0","other_ownership_assessment":"Deterministic
  fair picking is not automatically HSAT least-recent-flip history, tabu exclusion
  or a stochastic-uniform picker. Broad owner270 does not settle the operational rule.","owner_attachment_state":"responsibility_assigned_for_future_inspection","owner_attachments":[{"owner":{"candidate":"Additional
  GenSAT selection and initialization variants","index":298,"object_sha256_canonical_json":"ade6ee0e5c875afd4044fd18a2082adc237626b3b36c4935a33f3e8a25b383d3","pointer":"/full_owners/298","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"primary
  source-family research attachment","status":"responsibility_assigned_research_pending"}],"ownership_rationale":"DRSAT
  combines DSAT’s deterministic fair picker with the1995 walk extension. Owner298
  already names DSAT and explicitly owns picking/selection variants. Source-catalog
  owner296 is a secondary provenance/version comparator; no extra frontier row is
  needed to retain the pending question.","primary_existing_owner_index":298,"primary_scoped_owner_indexes":[{"owner_index":298,"scope":"primary
  source-family research attachment"}],"research_resolved":false,"responsibility_scope":"future_primary_source_inspection_only_not_method_identity_or_completion","secondary_context_owner_roles":[{"owner_index":296,"role":"secondary_source_family_or_maintained_method_comparison"}],"source":{"artifact":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"passage_bindings":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/origin-source-passages.json","sha256":"e6da50683ebf232d5cad782df05517d4600d6a66701a77b8b42b5d164a1043f3"},"physical_pdf_pages":[3,4,5],"url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"}}'
- 'Issue404 pending source responsibility H354-S4: {"candidate":"CHRSAT cautious history-pick
  walk variant","comparison_owners":[{"candidate":"Additional UBCSAT search variants","index":296,"object_sha256_canonical_json":"b3ec47a4ae0681b5cd0cd9d82e16a09152cd4c0d09de14db3dceb8021f07a61f","pointer":"/full_owners/296","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}}],"concept_identity_established":false,"disposition":"pending_primary_source_identity_and_operational_reconciliation","followup_id":"H354-S4","new_record_required":false,"next_check":"Compare
  cautious pools, the1995 history selector, CHSAT no-walk endpoint and unrestricted/restricted
  triggers. Determine if CHRSAT is a separate concept or an internal supported variant
  while retaining select/pick versus generic-random-walk ambiguity.","original_question":{"blocks_hrsat_or_tsat_science":false,"followup_id":"H354-S4","identity_established":false,"label":"CHRSAT
  cautious history-pick walk variant","new_concept_established":false,"pdf_pages":[8],"possible_owners":[296,298],"primary_source":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"question":"Reconcile
  cautious hill-climbing plus the HRSAT picking method and the CHSAT no-walk comparison.
  Determine whether this is a separate concept, scoped variant or existing-owner sublead.","record_count_implied":false,"source_spelling":"CHRSAT","status":"pending_source_identity_and_owner_reconciliation","url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"},"original_question_sha256_canonical_json":"59ea0a89b01ff1b8d4b23a1dbf667d4c14691eddc956a37bbda68257822a7c59","other_ownership_assessment":"The
  CHSAT comparison is retained inside this same question, not counted as a sixth named
  issue form or an additional established concept. Owner270 is broader context only.","owner_attachment_state":"responsibility_assigned_for_future_inspection","owner_attachments":[{"owner":{"candidate":"Additional
  GenSAT selection and initialization variants","index":298,"object_sha256_canonical_json":"ade6ee0e5c875afd4044fd18a2082adc237626b3b36c4935a33f3e8a25b383d3","pointer":"/full_owners/298","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"primary
  source-family research attachment","status":"responsibility_assigned_research_pending"}],"ownership_rationale":"CHRSAT
  combines CSAT cautious candidate selection with HRSAT history picking and compares
  a CHSAT no-walk endpoint. Its unresolved source-family dimension belongs with owner298’s
  CSAT/selector/picker variants. Owner296 and AIMech:HRSAT are essential comparisons
  for the already represented history-plus-walk construction, not automatic aliases.","primary_existing_owner_index":298,"primary_scoped_owner_indexes":[{"owner_index":298,"scope":"primary
  source-family research attachment"}],"research_resolved":false,"responsibility_scope":"future_primary_source_inspection_only_not_method_identity_or_completion","secondary_context_owner_roles":[{"owner_index":296,"role":"secondary_source_family_or_maintained_method_comparison"}],"source":{"artifact":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"passage_bindings":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/origin-source-passages.json","sha256":"e6da50683ebf232d5cad782df05517d4600d6a66701a77b8b42b5d164a1043f3"},"physical_pdf_pages":[8],"url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"}}'
- 'Issue404 pending source responsibility H354-S5: {"candidate":"JumpSAT multiple-clause
  jump variant","comparison_owners":[{"candidate":"Additional GenSAT selection and
  initialization variants","index":298,"object_sha256_canonical_json":"ade6ee0e5c875afd4044fd18a2082adc237626b3b36c4935a33f3e8a25b383d3","pointer":"/full_owners/298","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},{"candidate":"Local
  search","index":270,"object_sha256_canonical_json":"03c1f90e4934557856fb2ec201458a4408cd311af19e0b55c5824dfbe1c89059","pointer":"/full_owners/270","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}}],"concept_identity_established":false,"disposition":"pending_primary_source_identity_and_operational_reconciliation","followup_id":"H354-S5","new_record_required":false,"next_check":"Inspect
  exact multi-clause variable selection, duplicate-variable handling, simultaneous
  versus sequential updates, and clause-state timing. Assess unrestricted and improvement-gated
  jump policies separately. The source statement that all previously false clauses
  become satisfied is not accepted as an unconditional guarantee from the incomplete
  description.","original_question":{"blocks_hrsat_or_tsat_science":false,"followup_id":"H354-S5","identity_established":false,"label":"JumpSAT
  multiple-clause jump variant","new_concept_established":false,"pdf_pages":[8,9],"possible_owners":[296,298,270],"primary_source":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"question":"Inspect
  the one-variable-from-each-unsatisfied-clause jump and its selection/update semantics,
  including overlapping variables and the unrestricted versus improvement-gated versions;
  do not infer a full executable or universal success.","record_count_implied":false,"source_spelling":"JumpSAT","status":"pending_source_identity_and_owner_reconciliation","url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"},"original_question_sha256_canonical_json":"fa84c156411ca08f9730ad1de71448bcded4c850d68729eb380de9b9ac9c2787","other_ownership_assessment":"Owner298
  is relevant comparison for the single-flip GenSAT/GRSAT lineage but its existing
  selection-and-initialization scope does not, without expansion, cover an arbitrary
  multiple-variable transition. Owner270 supplies broader SLS context; it is too general
  as the primary source-question home.","owner_attachment_state":"responsibility_assigned_for_future_inspection","owner_attachments":[{"owner":{"candidate":"Additional
  UBCSAT search variants","index":296,"object_sha256_canonical_json":"b3ec47a4ae0681b5cd0cd9d82e16a09152cd4c0d09de14db3dceb8021f07a61f","pointer":"/full_owners/296","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"primary
  source-family research attachment","status":"responsibility_assigned_research_pending"}],"ownership_rationale":"JumpSAT
  is described as a GRSAT-related multiple-clause jump rather than one candidate variable
  selected and flipped by the printed GenSAT driver. Owner296’s additional SAT-source
  catalogue is a suitable explicit pending-source owner because it already follows
  the same archived1995 source and method/version discrepancies. This does not assert
  that JumpSAT is implemented or registered in UBCSAT.","primary_existing_owner_index":296,"primary_scoped_owner_indexes":[{"owner_index":296,"scope":"primary
  source-family research attachment"}],"research_resolved":false,"responsibility_scope":"future_primary_source_inspection_only_not_method_identity_or_completion","secondary_context_owner_roles":[{"owner_index":298,"role":"secondary_source_family_or_maintained_method_comparison"},{"owner_index":270,"role":"broader_local_search_context_only"}],"source":{"artifact":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"passage_bindings":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/origin-source-passages.json","sha256":"e6da50683ebf232d5cad782df05517d4600d6a66701a77b8b42b5d164a1043f3"},"physical_pdf_pages":[8,9],"url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"}}'
- 'Issue404 pending source responsibility H354-S6: {"candidate":"Restricted-walk trigger
  policy in CHRSAT and JumpSAT","comparison_owners":[{"candidate":"Local search","index":270,"object_sha256_canonical_json":"03c1f90e4934557856fb2ec201458a4408cd311af19e0b55c5824dfbe1c89059","pointer":"/full_owners/270","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}}],"concept_identity_established":false,"disposition":"pending_primary_source_identity_and_operational_reconciliation","followup_id":"H354-S6","new_record_required":false,"next_check":"For
  both named procedures, compare a walk/jump permitted at every step with a version
  allowed only when no strictly improving hill-climbing move is available. Clarify
  neutral-move treatment, selector/picker composition and whether this is an internal
  control dimension or warrants separate identity. Do not infer an extra record count.","original_question":{"blocks_hrsat_or_tsat_science":false,"followup_id":"H354-S6","identity_established":false,"label":"Restricted-walk
  trigger policy in CHRSAT and JumpSAT","new_concept_established":false,"pdf_pages":[8,9],"possible_owners":[296,298],"primary_source":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"question":"Retain
  the explicit policy difference between allowing focused moves on every step and
  allowing them only without an improving move. Determine whether this is an internal
  variant dimension or a separately owned identity; it is not a sixth named algorithm.","record_count_implied":false,"source_spelling":"walk
  only when hill climbing is not possible","status":"pending_source_identity_and_owner_reconciliation","url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"},"original_question_sha256_canonical_json":"aa4d40e0cfe3364dca424d9b18eb1574771995bb0382efb6660810557320ffd9","other_ownership_assessment":"Owner270
  provides the generic improvement/non-improvement context only. Owner301’s independent
  GWSAT sampling-distribution question remains unchanged and unresolved.","owner_attachment_state":"responsibility_assigned_for_future_inspection","owner_attachments":[{"owner":{"candidate":"Additional
  GenSAT selection and initialization variants","index":298,"object_sha256_canonical_json":"ade6ee0e5c875afd4044fd18a2082adc237626b3b36c4935a33f3e8a25b383d3","pointer":"/full_owners/298","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"CHRSAT
  trigger-policy branch","status":"responsibility_assigned_research_pending"},{"owner":{"candidate":"Additional
  UBCSAT search variants","index":296,"object_sha256_canonical_json":"b3ec47a4ae0681b5cd0cd9d82e16a09152cd4c0d09de14db3dceb8021f07a61f","pointer":"/full_owners/296","snapshot":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/observed-owner-contexts.json","sha256":"e9f62ff1ee0974cb8736ab05e74ab6ba3d8c0a0983f64e61d3badcb7a7c2f95b"}},"role":"JumpSAT
  trigger-policy branch","status":"responsibility_assigned_research_pending"}],"ownership_rationale":"This
  is one cross-cutting trigger-policy question, not a sixth named algorithm. Attach
  the CHRSAT branch to298 and the JumpSAT branch to296, using the same followup_id
  and source question. Distinct scoped attachments avoid forcing the multiple-variable
  JumpSAT mechanism into owner298 or duplicating a policy question.","primary_existing_owner_index":null,"primary_scoped_owner_indexes":[{"owner_index":298,"scope":"CHRSAT
  trigger-policy branch"},{"owner_index":296,"scope":"JumpSAT trigger-policy branch"}],"research_resolved":false,"responsibility_scope":"future_primary_source_inspection_only_not_method_identity_or_completion","secondary_context_owner_roles":[{"owner_index":270,"role":"broader_local_search_context_only"}],"source":{"artifact":{"path":"/private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf","sha256":"eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5"},"passage_bindings":{"path":"/private/tmp/aimech-issue404-owner-reconciliation-20261015/origin-source-passages.json","sha256":"e6da50683ebf232d5cad782df05517d4600d6a66701a77b8b42b5d164a1043f3"},"physical_pdf_pages":[8,9],"url":"https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf"}}'
- 'Incidental historical pointers and bibliography/source questions remain pending.
  Existing record or owner links are context, not equivalence or proof of completed
  source research. No new concept, frontier row, primary-source reading, or issue
  closure is asserted by this accounting. Registry SHA256: 859f88842f9e932a6656ac9b9cea2130a29fca38d478c7cfa36d7a9ad48c5de3.'
- 'Incidental source-accounting issue remains open for research: https://github.com/CultureBotAI/AIMech/issues/406.
  No closure is performed by this cohort.'
- 'H355-FLOW-01: Laplacian multiscale flow matching. Status: pending_inspection. Related
  record context: AIMech:FlowMatching. Related owner context: . Next check: Resolve
  primary source identity, inspect the full defining method and compare mechanism/scope
  with existing records; evidence-only or application-only items need not become new
  concept records. Access scope: Historical pointer and neighboring record context
  only; original source identity, narrower ownership and method/application/evidence
  scope remain pending. No primary reading or missing concept is asserted. Exact source
  question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/0;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 4a6d39afb18173f978ffe8c00afcc6478c495e14d2283c10579d201777875e2d.'
- 'H355-FLOW-02: Fisher flow matching. Status: pending_inspection. Related record
  context: AIMech:FlowMatching. Related owner context: . Next check: Resolve primary
  source identity, inspect the full defining method and compare mechanism/scope with
  existing records; evidence-only or application-only items need not become new concept
  records. Access scope: Historical pointer and neighboring record context only; original
  source identity, narrower ownership and method/application/evidence scope remain
  pending. No primary reading or missing concept is asserted. Exact source question:
  /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/1;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 bd06b0e49d2c960c9e2f2d6470d2807e95ca1e120c12f6813eecf423c8f1b187.'
- 'H355-FLOW-03: Functional rectified flow. Status: pending_inspection. Related record
  context: AIMech:RectifiedFlow. Related owner context: . Next check: Resolve primary
  source identity, inspect the full defining method and compare mechanism/scope with
  existing records; evidence-only or application-only items need not become new concept
  records. Access scope: Historical pointer and neighboring record context only; original
  source identity, narrower ownership and method/application/evidence scope remain
  pending. No primary reading or missing concept is asserted. Exact source question:
  /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/2;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 6fa62e21445c1fbe554b669a03e1cacc922bcb5fcc5007c2a051ca7f20c22da1.'
- 'H355-FLOW-04: Consistency-model convergence conditions. Status: pending_inspection.
  Related record context: AIMech:ConsistencyModel. Related owner context: . Next check:
  Resolve primary source identity, inspect the full defining method and compare mechanism/scope
  with existing records; evidence-only or application-only items need not become new
  concept records. Access scope: Historical pointer and neighboring record context
  only; original source identity, narrower ownership and method/application/evidence
  scope remain pending. No primary reading or missing concept is asserted. Exact source
  question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/3;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 02ad182ac3ab3b9986669b09af9c4c577bb97a499d9e0f72d605a80d2589a92a.'
- 'H355-FLOW-05: Manifold-aligned consistency tangents. Status: pending_inspection.
  Related record context: AIMech:ConsistencyModel. Related owner context: . Next check:
  Resolve primary source identity, inspect the full defining method and compare mechanism/scope
  with existing records; evidence-only or application-only items need not become new
  concept records. Access scope: Historical pointer and neighboring record context
  only; original source identity, narrower ownership and method/application/evidence
  scope remain pending. No primary reading or missing concept is asserted. Exact source
  question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/4;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 cc6a7aa117e44cb45c018ce8e314748513798845c108ad777a4148127726cc36.'
- 'H355-FLOW-06: Biological flow-matching applications. Status: pending_inspection.
  Related record context: AIMech:FlowMatching. Related owner context: . Next check:
  Resolve primary source identity, inspect the full defining method and compare mechanism/scope
  with existing records; evidence-only or application-only items need not become new
  concept records. Access scope: Historical pointer and neighboring record context
  only; original source identity, narrower ownership and method/application/evidence
  scope remain pending. No primary reading or missing concept is asserted. Exact source
  question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/5;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 236953ebf1b0c33832a7ec7a27428b7757c484255af74d482ecf241dcd275fc3.'
- 'H355-FLOW-07: Variational rectified flow matching. Status: pending_inspection.
  Related record context: AIMech:FlowMatching. Related owner context: . Next check:
  Resolve primary source identity, inspect the full defining method and compare mechanism/scope
  with existing records; evidence-only or application-only items need not become new
  concept records. Access scope: Historical pointer and neighboring record context
  only; original source identity, narrower ownership and method/application/evidence
  scope remain pending. No primary reading or missing concept is asserted. Exact source
  question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/6;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 2d6306f1f628db0114c7de2372c1bcdacaf03d4e963aa2e29248d97e8d6b9044.'
- 'H355-FLOW-08: Coreset-induced conditional velocity flow matching. Status: pending_inspection.
  Related record context: AIMech:FlowMatching. Related owner context: . Next check:
  Resolve primary source identity, inspect the full defining method and compare mechanism/scope
  with existing records; evidence-only or application-only items need not become new
  concept records. Access scope: Historical pointer and neighboring record context
  only; original source identity, narrower ownership and method/application/evidence
  scope remain pending. No primary reading or missing concept is asserted. Exact source
  question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/7;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 efa83a10ba3b1e6d0926fb936ae95ccf14f9cee6cbe5e538f2c562dd82bff8e1.'
- 'H355-FLOW-09: Isokinetic flow matching. Status: pending_inspection. Related record
  context: AIMech:FlowMatching. Related owner context: . Next check: Resolve primary
  source identity, inspect the full defining method and compare mechanism/scope with
  existing records; evidence-only or application-only items need not become new concept
  records. Access scope: Historical pointer and neighboring record context only; original
  source identity, narrower ownership and method/application/evidence scope remain
  pending. No primary reading or missing concept is asserted. Exact source question:
  /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/8;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 ab47f7af627dc0cb39aaa4cce38cb8527c9e22ea0a81598333a075bd3aa48950.'
- 'H355-FLOW-10: FLOWALIGN. Status: pending_inspection. Related record context: AIMech:FlowMatching.
  Related owner context: . Next check: Resolve primary source identity, inspect the
  full defining method and compare mechanism/scope with existing records; evidence-only
  or application-only items need not become new concept records. Access scope: Historical
  pointer and neighboring record context only; original source identity, narrower
  ownership and method/application/evidence scope remain pending. No primary reading
  or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/9;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 da310d8da81dfd9c8d4cc54934bd6df5c69603d22cc75100bbc1706f2bc491d0.'
- 'H355-FLOW-11: ReQFlow. Status: pending_inspection. Related record context: AIMech:RectifiedFlow.
  Related owner context: . Next check: Resolve primary source identity, inspect the
  full defining method and compare mechanism/scope with existing records; evidence-only
  or application-only items need not become new concept records. Access scope: Historical
  pointer and neighboring record context only; original source identity, narrower
  ownership and method/application/evidence scope remain pending. No primary reading
  or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/10;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 3bf821a75e665e361b78cd17a2d49aa2c2716242c71a2115ffa9171d2e46e47b.'
- 'H355-FLOW-12: RF-Physical / RF-FWD. Status: pending_inspection. Related record
  context: AIMech:RectifiedFlow. Related owner context: . Next check: Resolve primary
  source identity, inspect the full defining method and compare mechanism/scope with
  existing records; evidence-only or application-only items need not become new concept
  records. Access scope: Historical pointer and neighboring record context only; original
  source identity, narrower ownership and method/application/evidence scope remain
  pending. No primary reading or missing concept is asserted. Exact source question:
  /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/11;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 4aa56509645dcb3fa92d070c9032ba875d8ada427ff9819bad746d2488b9cd7e.'
- 'H355-FLOW-13: Unresolved ICLR 2026 conditional-flow relation source. Status: pending_inspection.
  Related record context: AIMech:FlowMatching. Related owner context: . Next check:
  Resolve primary source identity, inspect the full defining method and compare mechanism/scope
  with existing records; evidence-only or application-only items need not become new
  concept records. Access scope: Historical pointer and neighboring record context
  only; original source identity, narrower ownership and method/application/evidence
  scope remain pending. No primary reading or missing concept is asserted. Exact source
  question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/12;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 00e3b109d013645c9cd0f69c7fc9e4ac9d79482af887b5aaa1bcdb5c3c396103.'
- 'H355-FLOW-14: Conditional flow matching and OT conditional flow matching. Status:
  pending_inspection. Related record context: AIMech:FlowMatching, AIMech:RectifiedFlow.
  Related owner context: . Next check: Determine whether named objectives merit separately
  scoped methods rather than aliases for the general framework. Access scope: Historical
  pointer and neighboring record context only; original source identity, narrower
  ownership and method/application/evidence scope remain pending. No primary reading
  or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/13;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 69a91404238fa8725cd4e374690e0aae5c1d5e1bf98abe5387cf8ffe7c6c053b.'
- 'H355-FLOW-15: Consistency training and consistency distillation. Status: pending_inspection.
  Related record context: AIMech:ConsistencyModel, AIMech:ImprovedConsistencyTraining.
  Related owner context: . Next check: Assess standalone procedure identities, preserving
  the EMA-theory correction for the original CT variant. Access scope: Historical
  pointer and neighboring record context only; original source identity, narrower
  ownership and method/application/evidence scope remain pending. No primary reading
  or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/14;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 55dd8c121ec319e972285d31e8878cf30ffc64b68189cba66d0fd03c4e9fcb95.'
- 'H355-FLOW-16: Gradient-constrained rectification. Status: pending_inspection. Related
  record context: AIMech:RectifiedFlow. Related owner context: . Next check: Inspect
  the original defining method and retain support/regularity counterexamples, without
  promoting straightness to optimal transport. Access scope: Historical pointer and
  neighboring record context only; original source identity, narrower ownership and
  method/application/evidence scope remain pending. No primary reading or missing
  concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/15;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 b2c9e705f06bab67e3ebc69d0bc977ba88eceb5c270ac9d242af9cbbbae23418.'
- 'H355-FLOW-17: Normalizing flows, continuous normalizing flows and probability-flow
  ODEs. Status: pending_inspection. Related record context: AIMech:FlowMatching, AIMech:RectifiedFlow,
  AIMech:ConsistencyModel. Related owner context: planned_owner909/svgd_bibliography_4.
  Next check: Read original definitions, distinguish model families from differential-equation
  constructions, and search AIO identities. Access scope: Historical pointer and neighboring
  record context only; original source identity, narrower ownership and method/application/evidence
  scope remain pending. No primary reading or missing concept is asserted. Exact source
  question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/16;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 d62687cddf2304d85467fd317c4c9760b06b749dd7cc822e6dd4b7ae5313175b.'
- 'H355-FLOW-18: Pseudo-Huber discrepancy and LPIPS. Status: pending_inspection. Related
  record context: AIMech:ImprovedConsistencyTraining. Related owner context: . Next
  check: Decide on mathematical-method/evaluation-method scope and inspect original
  definitions rather than import a name from a training paper. Access scope: Historical
  pointer and neighboring record context only; original source identity, narrower
  ownership and method/application/evidence scope remain pending. No primary reading
  or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/17;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 d6fe8b871ece43c62d89e21f3459be1c3586c5b1eda9572dbd4ee1b1d6a16bc2.'
- 'H355-FLOW-19: DDIM, DPM-Solver, DEIS, UniPC, TRACT, Diff-Instruct and BOOT. Status:
  pending_inspection. Related record context: AIMech:ImprovedConsistencyTraining.
  Related owner context: . Next check: Only names were used as leads; inspect each
  defining paper before a record, and do not infer performance from the extracted
  table. Access scope: Historical pointer and neighboring record context only; original
  source identity, narrower ownership and method/application/evidence scope remain
  pending. No primary reading or missing concept is asserted. Exact source question:
  /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/18;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 841720635ef3f85c37e8469dd82f3f349a0d5c1135cf0ade430d5f839f7ec577.'
- 'H355-FLOW-20: Consistency Flow Matching. Status: pending_inspection. Related record
  context: AIMech:FlowMatching. Related owner context: . Next check: Re-search the
  exact primary title/source before identity or method assertions. Access scope: Historical
  pointer and neighboring record context only; original source identity, narrower
  ownership and method/application/evidence scope remain pending. No primary reading
  or missing concept is asserted. Exact source question: /private/tmp/aimech-cohort355-groups000-219-reading-20261016/pending-flow-questions.json#/questions/19;
  ledger SHA256 54797045c0c6f5f17738479e5f1b2113576892ba27682d8983bbcf16bcf1125b;
  payload SHA256 52d4ef7359116fc1c7e4a19ca21253a08ec6ee75cb52927ba66aeadc10879360.'
- 'H355-R1: Deterministic policy gradient. Status: pending_inspection. Related record
  context: AIMech:DeepDeterministicPolicyGradient. Related owner context: . Next check:
  Resolve exact identity and representation scope against both collections, then inspect
  the primary defining source; a shared component or related method is not automatically
  a new record. Access scope: Historical discovery object, saved-review boundary and
  current record text inspected; no new original-primary-method reading or separate
  concept assertion. Exact source question: /private/tmp/aimech-cohort355-context220-439-20261016/pending-questions.json#/0;
  ledger SHA256 b531fd652aad7a8baeca6fa4b747b58ec7a397ac598c1709000bd9bc6040144c;
  payload SHA256 94cb21f31b9f7ab8b6b9943f5647bcc7663685a4d846b8f0c34850056ce42a56.'
- 'H355-R2: Experience replay. Status: pending_inspection. Related record context:
  AIMech:DeepDeterministicPolicyGradient, AIMech:DeepQNetwork. Related owner context:
  . Next check: Resolve exact identity and representation scope against both collections,
  then inspect the primary defining source; a shared component or related method is
  not automatically a new record. Access scope: Historical discovery object, saved-review
  boundary and current record text inspected; no new original-primary-method reading
  or separate concept assertion. Exact source question: /private/tmp/aimech-cohort355-context220-439-20261016/pending-questions.json#/1;
  ledger SHA256 b531fd652aad7a8baeca6fa4b747b58ec7a397ac598c1709000bd9bc6040144c;
  payload SHA256 78deff07777c5d17bb3953885b84f575f90e62dc54e07692fdc6e6347e0d6a5e.'
- 'H355-R3: Target network. Status: pending_inspection. Related record context: AIMech:DeepDeterministicPolicyGradient,
  AIMech:DeepQNetwork. Related owner context: . Next check: Resolve exact identity
  and representation scope against both collections, then inspect the primary defining
  source; a shared component or related method is not automatically a new record.
  Access scope: Historical discovery object, saved-review boundary and current record
  text inspected; no new original-primary-method reading or separate concept assertion.
  Exact source question: /private/tmp/aimech-cohort355-context220-439-20261016/pending-questions.json#/2;
  ledger SHA256 b531fd652aad7a8baeca6fa4b747b58ec7a397ac598c1709000bd9bc6040144c;
  payload SHA256 6fbf4a5f6da3720234fab4ff805e596a47f424ebfdbd4a7d3f1f68e87a6adbd6.'
- 'H355-SCI-H1: Spatial Sensitive Grad-CAM++. Status: pending_inspection. Related
  record context: AIMech:GradCAM, AIMech:GuidedGradCAM. Related owner context: . Next
  check: Locate the exact CVF2024 workshop source named by the original historical
  pointer, compare its mechanism and aliases against GradCAM and GuidedGradCAM and
  other attribution variants, and retain an explicit pending or supported existing-owner
  disposition. Shared Grad-CAM wording is not an identity decision. Access scope:
  An explicit historical pending object, visible through a later embedded identity-search
  result. The original method itself has not been read. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/0;
  ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527;
  payload SHA256 36b9bb9e0881a73d4af8bdc12d92f2a7bde5fede9490129ae702dae4457b7bb3.'
- 'H355-SCI-B1: Nonparametric empirical Bayes for the Dirichlet process mixture model.
  Status: pending_inspection. Related record context: AIMech:LatentDirichletAllocation,
  AIMech:BlackBoxVariationalInference. Related owner context: /prior_frontier_accounting/425.
  Next check: The existing topic cohort explicitly retains DP variational inference
  and HDP/nested-CRP models, but does not explicitly resolve this empirical-Bayes
  source. Determine whether its estimand/procedure is already represented or belongs
  within that cohort. Access scope: Previously retained search output only, newly
  reconciled now. No original method reading, novelty decision or full source validation.
  Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/1;
  ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527;
  payload SHA256 0eac3087b2678a4bb91287c6ad8e01733847e29d2a9b4651d39f7d4c9d147397.'
- 'H355-SCI-B2: Probabilistic Models of Text and Images (Blei 2004 thesis). Status:
  pending_inspection. Related record context: AIMech:LatentDirichletAllocation. Related
  owner context: /prior_frontier_accounting/425. Next check: This thesis is a discovery
  source, not one established new method. Compare its chapters with existing LDA and
  pending annotated/cross-modal sources; retain only distinct, evidenced methods or
  version questions after reading. Access scope: Previously retained search output
  only, newly reconciled now. No original method reading, novelty decision or full
  source validation. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/2;
  ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527;
  payload SHA256 a0478d0c711e831a5a3ce42edf3e68ee9991a55d8d419d2ed2c0613464454734.'
- 'H355-SCI-B3: Hierarchical Bayesian models for applications in information retrieval.
  Status: pending_inspection. Related record context: AIMech:LatentDirichletAllocation.
  Related owner context: /prior_frontier_accounting/425. Next check: The Blei–Ng–Jordan
  chapter may overlap existing LDA evidence. Read and compare the actual chapter before
  deciding source-only duplication, evidence extension or distinct mechanism; broad
  title similarity is insufficient. Access scope: Previously retained search output
  only, newly reconciled now. No original method reading, novelty decision or full
  source validation. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/3;
  ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527;
  payload SHA256 a0e2d0b0b3d2c6878118c0a53cde4b0d03eb9bab2e54176870889e8475352feb.'
- 'H355-SCI-B4: Predicting the performance of linearly combined IR systems. Status:
  pending_inspection. Related record context: . Related owner context: /prior_frontier_accounting/468.
  Next check: The nearest retrieval cohort concerns query likelihood and document
  expansion, not an established account of this combination-performance source. Establish
  the original reference and whether it defines a reusable AI procedure, an evaluation
  theory or merely contextual evidence. Access scope: Previously retained search output
  only, newly reconciled now. No original method reading, novelty decision or full
  source validation. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/4;
  ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527;
  payload SHA256 21a68ac7428177b09dbbf93f6bdee48e9df409b7b0ae752e0a738ce30844732d.'
- 'H355-SCI-B5: A Similarity-based Probability Model for Latent Semantic Indexing.
  Status: pending_inspection. Related record context: AIMech:ProbabilisticLatentSemanticAnalysis.
  Related owner context: /prior_frontier_accounting/421. Next check: The retained
  SIGIR listing gives a title only. Resolve its source/authors and compare with PLSA,
  SVD-LSI and the existing dyadic-clustering owner before assigning an owner or claiming
  distinctness. Access scope: Previously retained search output only, newly reconciled
  now. No original method reading, novelty decision or full source validation. Exact
  source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/5;
  ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527;
  payload SHA256 39b50214f53e4a89e979f8cafd18234745689a9538656dd4320112bc8dca8161.'
- 'H355-SCI-B6: A Hierarchical Model for Clustering and Categorising Documents. Status:
  pending_inspection. Related record context: AIMech:LatentDirichletAllocation. Related
  owner context: /prior_frontier_accounting/425, /prior_frontier_accounting/490, /prior_frontier_accounting/491.
  Next check: The source is a third-party bibliography snippet. Compare the actual
  2002 paper with current annotated/nonparametric topics and distinct owners490/491;
  those owners name different later sources and do not establish identity. Access
  scope: Previously retained search output only, newly reconciled now. No original
  method reading, novelty decision or full source validation. Exact source question:
  /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/6;
  ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527;
  payload SHA256 d88b882890c2a6a9d9070165f547a8e8123f328500a4bfb2c6b3cf8973d9a74b.'
- 'H355-SCI-B7: Variational Inference: a review for statisticians. Status: pending_inspection.
  Related record context: AIMech:BlackBoxVariationalInference, AIMech:FullyFactorizedMeanFieldInference,
  AIMech:VariationalExpectationMaximization. Related owner context: /prior_frontier_accounting/426.
  Next check: This secondary biographical snippet identifies a review source. Resolve
  the actual version and use its cited originals for bounded discovery; do not add
  a record for the review title or treat generic VI records as an explicit disposition.
  Access scope: Previously retained search output only, newly reconciled now. No original
  method reading, novelty decision or full source validation. Exact source question:
  /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/7;
  ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527;
  payload SHA256 ce4a9fb1c042cca1f34944c8f6047e7cddbda5c72563dcd4f72d46e52272d362.'
- 'H355-SCI-B8: Foundational TF-IDF term weighting and Salton–McGill1983 source scope.
  Status: pending_inspection. Related record context: AIMech:UnsupervisedDataAugmentation,
  AIMech:ExponentialFamilyHarmonium. Related owner context: /prior_frontier_accounting/140.
  Next check: Owner140 explicitly covers TF-IDF word replacement for augmentation;
  maintained UDA uses that component and harmonium compares against TF-IDF retrieval.
  The foundational weighting/source identity is not explicitly resolved by those scoped
  uses. Inspect the original formulation/version and decide representation/component/owner
  scope without assuming a new algorithm. Access scope: Previously retained search
  output only, newly reconciled now. No original method reading, novelty decision
  or full source validation. Exact source question: /private/tmp/aimech-cohort355-incidental-source-reconciliation-20261016/pending-source-accounting.json#/questions/8;
  ledger SHA256 6aa994414a498a9879798ff065e03f5d303becf1efc0042a02166e79e41cc527;
  payload SHA256 607032235a6edf33aea28b219e91b70b0e1243928c26c17f32114adadbbac782.'
- 'H355-SAC-VERSION: Later SAC implementations: unspecified source/version. Status:
  pending_inspection. Related record context: AIMech:SoftActorCritic. Related owner
  context: . Next check: Identify the precise later SAC source/version and compare
  it with the maintained original2018 state-value formulation before deciding source
  enrichment, variant scope or distinct identity. Do not conflate this generic uncertainty
  with Soft Q-learning. Access scope: Historical review boundary appearing in groups49
  and413 (with further embedded repetition) only; no specific later primary source
  or additional concept has been established. Exact source question: /private/tmp/aimech-cohort355-context220-439-20261016/selected-original-boundary-decisions.json#/1/boundary_decisions/1;
  ledger SHA256 5e0dfa47076bdf04d04bc01000d79f21516a7970ad1d64359011b0fb30d58061;
  payload SHA256 6e8ac4f7db6bec1e4ce6b68d982011edb6ee76ac6b00ba363a92442c0690d338.'
evidence:
- evidence_id: preview-softq
  kind: record_content
  reference: /private/tmp/aimech-soft-q-code-access-successor-20261015/native-preview.json
  snapshot_sha256: aee3ba19cadcbabb1d42a9751a873369b150fb2faa5c60537baee86b233d3abd
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: Accepted TEMP preview; actual canonical correspondence remains unbound.
- evidence_id: support-softq
  kind: record_content
  reference: /private/tmp/aimech-soft-q-draft-preparation-20261015/scientific-support.json
  snapshot_sha256: acd76859196409efe4276813bc6927ea1b24657b87ff64c25634bc80f90e656d
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: Exact accepted per-claim and per-limitation support; historical scope remains
    attributed.
- evidence_id: draft-acceptance-softq
  kind: record_content
  reference: /private/tmp/aimech-soft-q-code-access-successor-20261015/root-draft-acceptance.json
  snapshot_sha256: 25fc4a8f04587acc75c277cf4afbec032ffb58f419503f6f1ad01868635ada4a
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: Exact root draft acceptance precedes retained validation.
- evidence_id: preview-validation-softq
  kind: record_content
  reference: /private/tmp/aimech-soft-q-code-access-successor-20261015/native-preview-validation.json
  snapshot_sha256: 39763c439c0bf11068eb1b93a21ee9c1aa4809315801f2149d8eb3a51b5b3bc4
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: Retained postacceptance TEMP validation; no future gate inferred.
- evidence_id: root-research-softq
  kind: record_content
  reference: /private/tmp/aimech-soft-q-research-20261015/root-research-acceptance.json
  snapshot_sha256: f777ad1afbcd450041803d340fa775dd1188f9622fc8ed16a7a3b8ffccf77b32
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: 'Historical research acceptance reading: {"root_primary_reading": {"path":
    "/private/tmp/aimech-soft-q-research-20261015/root-primary-reading.json", "sha256":
    "ec82498475f2ae36600109c34ac3222cbf8806e80b6f03a44f92add738ba1842"}, "scope":
    "Research accepted for TEMP data-only native draft: one SoftQLearning algorithm,
    no aliases, qualified related_match to AIO ReinforcementLearning, six claims and
    seven limitations. Canonical ownership and actual merged-base identity remain
    future steps.", "root_reading": "Read full dossier, analytic boundaries, all proposed
    claims/limitations, sources and identity assessment; all seven matching contents
    and provenance, ten native definition projections, six selected frontier objects,
    and nine complete AIO nodes with 71 incident edges. Read later sql.py lines 210–280
    for the projected positive transport and minimized negative surrogate. Prior source
    reading remains attributed by root-primary-reading; full five native record and
    full code reads are agent evidence, not relabeled root reading."}. Exact draft
    acceptance reading: {"scope": "Root full static module, inputs, sources, identity,
    six claim and seven limitation support reading; exact metadata-only successor
    read and accepted. Definition and claims retain 2017 method, finite approximation
    and source notation boundaries. Source context remains explicit and no exact code-version
    equivalence claimed.", "root_reading_scope": "Prior primary reading and research
    acceptance remain separately attributed. No new primary reread or independent
    approval is implied."}. This preparation did not newly inspect primary pages or
    execute the methods.'
- evidence_id: preparation-reading-softq
  kind: record_content
  reference: /private/tmp/aimech-soft-q-draft-preparation-20261015/reading.json
  snapshot_sha256: 0d1b50f82298c069cd4b1d089f825f9894ebfc7f49b7b44a186d15ee67f6d388
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: Historical draft reading scope, separately attributed.
- evidence_id: historical-identity-softq
  kind: record_content
  reference: /private/tmp/aimech-soft-q-research-20261015/identity-assessment.json
  snapshot_sha256: eb1a5049a524c6b4750eddde6a31dac136c4fe66d4d7d5bdeb25a192a5fa4163
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: Dated identity assessment; fresh current collection remains required.
- evidence_id: src-haarnoja2017-main
  kind: primary_source
  reference: /private/tmp/aimech-soft-q-research-20261015/haarnoja2017-main.pdf
  snapshot_sha256: 060b03d843a0f38f399a05f23b22a00d953bcfd60a8aefae86e7a68fcafc31b5
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: supports
  summary: primary method support. Official PMLR 70 (ICML 2017), ten-page main article;
    accessed_at records local artifact verification, not download time. Original acquisition
    was approximately 2026-10-15 21:31Z; exact download seconds are not asserted.
- evidence_id: src-haarnoja2017-supp
  kind: primary_source
  reference: /private/tmp/aimech-soft-q-research-20261015/haarnoja2017-supp.pdf
  snapshot_sha256: bca2563b0d8ac50425d707cda59007a16ae95323467a9ea6134a28f004607aa2
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: supports
  summary: primary supplementary derivation/implementation scope. Official PMLR supplementary
    PDF, sixteen pages; first ten extracted text pages equal main; appendices A–D
    on PDF pages 11–16; accessed_at records local artifact verification, not download
    time. Original acquisition was approximately 2026-10-15 21:31Z; exact download
    seconds are not asserted.
- evidence_id: src-haarnoja-code-context
  kind: primary_source
  reference: /private/tmp/aimech-soft-q-research-20261015/code-context/sql.py
  snapshot_sha256: fb395bab4c715e7f223c03776e8a875cd89d5d3857af736f9ecc9d6832543de1
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: context_only for later sign convention and version boundary. Author repository
    commit 6f51eaca77d15b35c6443363c51a5a53ff4e9854, dated 2019-01-05; complete 357-line
    static read. Later implementation context only, not established as the 2017 experimental
    version.
- evidence_id: preview-svgd
  kind: record_content
  reference: /private/tmp/aimech-svgd-draft-preparation-20261015/native-preview.json
  snapshot_sha256: 27abfcfedc7d94a1f4874444cdf803f685ab9c1d38e9d3009123e7511bd1b660
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: Accepted TEMP preview; actual canonical correspondence remains unbound.
- evidence_id: support-svgd
  kind: record_content
  reference: /private/tmp/aimech-svgd-draft-preparation-20261015/scientific-support.json
  snapshot_sha256: 70a927a779d507c50efb923651bdf775379fce91ae2193b824197a6c21bfd39b
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: Exact accepted per-claim and per-limitation support; historical scope remains
    attributed.
- evidence_id: draft-acceptance-svgd
  kind: record_content
  reference: /private/tmp/aimech-svgd-draft-preparation-20261015/root-draft-acceptance.json
  snapshot_sha256: b67e1cec076c1ec9d1f6c024bebdc5738cc8e0221f8d387d3c01e38591016c6c
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: Exact root draft acceptance precedes retained validation.
- evidence_id: preview-validation-svgd
  kind: record_content
  reference: /private/tmp/aimech-svgd-draft-preparation-20261015/native-preview-validation.json
  snapshot_sha256: fa33b7c2ea3bd402f709fe14674f43fe8555b7eb413ca4e9a2b8c8e0df7c69f3
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: Retained postacceptance TEMP validation; no future gate inferred.
- evidence_id: root-research-svgd
  kind: record_content
  reference: /private/tmp/aimech-svgd-research-20261015/root-research-acceptance.json
  snapshot_sha256: 1dd68ceb7ccf07a75d98badda9c90595a3080cb0bcd492e4e62f39dac733d30b
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: 'Historical research acceptance reading: {"reading_scope": "Root previously
    read all nine original main text pages and main visuals 4–5. Root now read all
    four official supplement text pages and supplement visual 1, full dossier, source
    ledger and reading scopes, all proposed five claims/seven limitations and analytic
    boundaries, identity/mapping/citation assessments, all eight pinned AIO node/edge
    contexts, and eight maintained identity/definition/mapping projections. Later-v3
    selected reading, other declared original visuals, two full native records and
    sixteen selected frontier bodies remain attributed to the supporting researcher.
    No whole later-version or software inspection is claimed."}. Exact draft acceptance
    reading: {"scope": "Root read exact static module and sources before restart;
    inputs, time projection, identity and complete support after restart, including
    truncation recovery for limitations2/3. All5claims/7limitations and8explicit AIO
    rejections agree with accepted original source reading. Defining main/appendix
    belong to one2016work; appendix row hashes downloaded ZIP and separately binds
    extractedPDF; later v3 has only inspected context scope. No new visual reading
    or future-base identity clearance claimed. Mechanical AST/support equality checked
    separately."}. This preparation did not newly inspect primary pages or execute
    the methods.'
- evidence_id: preparation-reading-svgd
  kind: record_content
  reference: /private/tmp/aimech-svgd-draft-preparation-20261015/reading.json
  snapshot_sha256: ac2dc8b1d978e0ec4017fe6304ec1677c5734f00fe4c625769d821369aa1712d
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: Historical draft reading scope, separately attributed.
- evidence_id: historical-identity-svgd
  kind: record_content
  reference: /private/tmp/aimech-svgd-research-20261015/identity-assessment.json
  snapshot_sha256: 18e8702d8f8f57bb85c25261d6621004af1494568ec678bf2bb618e4ee447c73
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: Dated identity assessment; fresh current collection remains required.
- evidence_id: src-liu2016-main
  kind: primary_source
  reference: /private/tmp/aimech-svgd-research-20261015/liu-wang2016.pdf
  snapshot_sha256: 2ea66ee72576fc5651edb6bab3b6da6371e7e943b3f6b5a9057cef20474493d9
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: supports
  summary: primary method support. Official 2016 proceedings PDF, nine pages.
- evidence_id: src-liu2016-supplement
  kind: primary_source
  reference: /private/tmp/aimech-svgd-research-20261015/supplement.zip
  snapshot_sha256: 7c4102d79ac513fa586663158939d9a3f1c1fd893e95988c38e89d4731612b5f
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: supports
  summary: same-work primary appendix support with display caveat. Official single-member
    ZIP; four-page PDF appendix, no software in this archive. The row checksum identifies
    the downloaded ZIP; its sole inspected member 1239-appendix.pdf has SHA256 112e4b57860af60e81f9f9bd6877bc8c3b190cc6aee6375e3ed9a99f294de337.
    This is supplementary evidence for the same 2016 work.
- evidence_id: src-liu2019-v3-context
  kind: primary_source
  reference: /private/tmp/aimech-svgd-research-20261015/liu-wang-arxiv-v3.pdf
  snapshot_sha256: 993eee23e03dd78ed3db4e56c92f6a71291436e0f9d8c5d51c8642fbd690b7dc
  accessed_at: '2026-10-15T23:01:52.604840Z'
  support: context_only
  summary: context_only selected later-version comparison. arXiv:1608.04471v3, submitted
    2019-09-09, 13-page combined paper/appendix. No full-version reading claimed.
    Context only for selected display/version comparison; the original 2016 method
    remains defining.
- evidence_id: actual-write
  kind: record_content
  reference: /private/tmp/aimech-softq-svgd-cohort355-write.json
  snapshot_sha256: 456484f26bb178a696dec30090da23d6c63f934bd56a38ec5feea11c998f3dae
  accessed_at: '2026-10-16T00:40:59.303587Z'
  support: context_only
  summary: 'Actual exclusive creation receipt: two records, report pair and one CREATE
    history.'
- evidence_id: captured-inputs
  kind: record_content
  reference: /private/tmp/aimech-cohort355-capture.json
  snapshot_sha256: 4e6a5497aee1d9152b00a9541a93cd3b6179f0d496e054339cef8d2467c603c6
  accessed_at: '2026-10-16T00:40:59.303635Z'
  support: context_only
  summary: Actual canonical inspection; every current input hash and maintained target
    was checked.
- evidence_id: postcapture-reading
  kind: record_content
  reference: /private/tmp/aimech-cohort355-root-review-reading.json
  snapshot_sha256: e5c29089b105e722ac258a6a006c5a16b58477095a8948579e2520e56cd1ecce
  accessed_at: '2026-10-16T00:40:59.303662Z'
  support: context_only
  summary: 'Historical root reading receipt, recorded 2026-10-16T00:29:56.490975+00:00:
    Root read both complete canonical YAML files after writing, complete report Markdown
    (recovered truncated FLOW07–20 block), complete CREATE history, current report
    metadata, three identity/no-match context changes and complete changed owner909
    including all eight citations/root dispositions. Root previously read the three
    inherited governance blocks, all six404 questions/seven responsibility attachments
    and all33 normalized406 questions and exact recoverable source payloads; actual
    report/write/decision registry equality and 44 capture hashes independently rechecked
    after capture. This is not full manual reading of 912 unchanged main or394 nested
    objects nor every repeated raw provenance occurrence. Root read actual scientific
    correspondence audit with105 checks and independent output audit189checks; no
    finding remains. Prior full primary reading and mathematical checks remain separately
    attributed; source-version caveat retained. Any future-event wording belongs to
    that earlier receipt; the later six check logs establish completion before this
    review was generated, while canonical save remains subsequent.'
- evidence_id: governance-assessment
  kind: record_content
  reference: /private/tmp/aimech-cohort355-governance-audit-20261015/assessment.json
  snapshot_sha256: 97a0660785d4f50f8b935e1a94c80d5b1761a3e3351fa76692f70d37c369be4d
  accessed_at: '2026-10-16T00:40:59.303683Z'
  support: context_only
  summary: Actual byte preservation, owner/frontier, history and parsed-page audit;
    no independent approval.
- evidence_id: rendered-pages
  kind: record_content
  reference: /private/tmp/aimech-cohort355-governance-audit-20261015/rendered-pages.json
  snapshot_sha256: d62ecdd68ee248376cc5cee95316eeefc27f3f33e9e1c1e2e72694e3a4ddaa4f
  accessed_at: '2026-10-16T00:40:59.303703Z'
  support: context_only
  summary: Actual generated page paths and bytes, with parsed-content correspondence;
    no browser/layout inspection.
- evidence_id: actual-scientific-assessment
  kind: record_content
  reference: /private/tmp/aimech-cohort355-actual-scientific-audit-20261016/assessment.json
  snapshot_sha256: ac21a24660a442fc3de976d651a24b74e63e559dd491a75150ab19ba27f9bf81
  accessed_at: '2026-10-16T00:40:59.303724Z'
  support: context_only
  summary: Same-author actual-record adversarial assessment with separately attributed
    primary reading.
- evidence_id: current-identity-collection
  kind: search
  reference: /private/tmp/aimech-cohort355-identity-20261016/collection.json
  snapshot_sha256: b0936fc8f48ee88d6f7b4e20fe7501c43f3d6f3aac888ccd4e55c54c718d6809
  accessed_at: '2026-10-16T00:40:59.303745Z'
  support: context_only
  summary: Current four-root ignored- and hidden-inclusive identity collection; mechanical
    coverage is distinct from attributed semantic reading.
  search_scope: Four ignored/hidden-inclusive scans, all1230prior IDs/names/aliases/scoped
    synonyms and current913main394nested recursive queries; all665distinctcontents
    read across team, root440–664 and selected exact node/neighborhood projections.
    No unbounded novelty or saturation claim.
- evidence_id: current-context-assessment
  kind: search
  reference: /private/tmp/aimech-cohort355-identity-20261016/root-current-assessment.json
  snapshot_sha256: 6303cd4fdc4c182c4a7574be27d40eee6c547a5917462dd4fb03b2ceb07b3459
  accessed_at: '2026-10-16T00:40:59.303769Z'
  support: context_only
  summary: Actual supporting interpretation of retained matched contexts; root and
    supporting scopes remain separate.
  search_scope: Four ignored/hidden-inclusive scans, all1230prior IDs/names/aliases/scoped
    synonyms and current913main394nested recursive queries; all665distinctcontents
    read across team, root440–664 and selected exact node/neighborhood projections.
    No unbounded novelty or saturation claim.
- evidence_id: root-decisions
  kind: record_content
  reference: /private/tmp/aimech-cohort355-identity-20261016/root-decisions.json
  snapshot_sha256: 9ce8558681c023ac68349b52e30bfeb98e1d1aa4d6a2da65c48316ef5865aa26
  accessed_at: '2026-10-16T00:40:59.303793Z'
  support: context_only
  summary: Actual root identity, partial owner 909 and all eight source-question decisions;
    existing record/owner links remain explicit and all other frontier objects remain
    exact.
- evidence_id: scientific-support
  kind: record_content
  reference: /private/tmp/aimech-cohort355-consumer-preparation-20261015/scientific-support.v2.prepared.json
  snapshot_sha256: 84620f80da1e8a4dd929d819b6c9edce8e9fc366b307b43e8afdecda2a4ff60a
  accessed_at: '2026-10-16T00:40:59.303813Z'
  support: context_only
  summary: Exact accepted claim and limitation support; historical and later source/math
    scopes remain separate.
- evidence_id: discovery-report
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T002614Z-soft-q-learning-and-stein-variational-gradient-descent.json
  snapshot_sha256: 96f80b5598848c2418b5995938067dd03f4ccf33e8c1d80eedfd3422c3db386b
  accessed_at: '2026-10-16T00:40:59.311874Z'
  support: context_only
  summary: Current records and owner 909 citation mirrors; three original citation
    entries and five bibliography questions remain queryable. Exact inherited governance
    and issue 402 triage remain separate; no rows appended.
- evidence_id: creation-history
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/history/reports/soft-q-learning-and-stein-variational-gradient-descent/2026-10-16T002628Z-codex-1f51bf.yaml
  snapshot_sha256: 9f4f5367fa502dcb576b57beeed3fe7e799e73a0fd3e9695f8200720355207b7
  accessed_at: '2026-10-16T00:40:59.312234Z'
  support: context_only
  summary: Actual CREATE report history covers two new records and the report; no
    old report or existing restoration row is edited.
- evidence_id: record-softq
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/data/curated/SoftQLearning.yaml
  snapshot_sha256: 30a9c92eac4e3169d040b64230b7efd6ec8d9685ea58cd5136f4a2d7fa895dca
  accessed_at: '2026-10-16T00:40:59.312520Z'
  support: context_only
  summary: Complete current DRAFT record equals accepted science and actual root identity
    decisions.
- evidence_id: record-svgd
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/data/curated/SteinVariationalGradientDescent.yaml
  snapshot_sha256: 306808b660d4ce0880599e6acc901c5352c8a92d3ed6db58f89bd2b3c107d2b0
  accessed_at: '2026-10-16T00:40:59.312873Z'
  support: context_only
  summary: Complete current DRAFT record equals accepted science and actual root identity
    decisions.
- evidence_id: check-gate
  kind: validation
  reference: /private/tmp/aimech-cohort355-check-gate.json
  snapshot_sha256: a797ce00cb1525a52ae2bd13f90ac189e39027f8784093537450e7ca28f218df
  accessed_at: '2026-10-16T00:37:34.693756Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-vendor
  kind: validation
  reference: /private/tmp/aimech-cohort355-network-resume-check-vendor.json
  snapshot_sha256: 7bfd89668ae9991231f5352d7124758523fbefd46f42b6b6d0e27412e66dc364
  accessed_at: '2026-10-16T00:40:30.427416Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-check-source
  kind: validation
  reference: /private/tmp/aimech-cohort355-network-resume-check-check-source.json
  snapshot_sha256: f9306c4fc26e2f3d7c5078aec0e71120c429fa78cc5444c7bf69de36552fff4f
  accessed_at: '2026-10-16T00:40:33.744808Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-render
  kind: validation
  reference: /private/tmp/aimech-cohort355-check-render.json
  snapshot_sha256: 786832e72a72ba426fe860116f5d8ac0a79f6187c9464770355ae35becfba071
  accessed_at: '2026-10-16T00:26:50.883112Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-render-check
  kind: validation
  reference: /private/tmp/aimech-cohort355-network-resume-check-render-check.json
  snapshot_sha256: 01baa2fea58ed2e4ce7eb3d44fc0e9bda14583ab94b2106ac4985518539fae75
  accessed_at: '2026-10-16T00:40:52.138965Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-diff
  kind: validation
  reference: /private/tmp/aimech-cohort355-network-resume-check-diff.json
  snapshot_sha256: d11ac80fe71456651b4fe9ea8d5c16f381edfd7fd7d0b92b44203fa6032124e1
  accessed_at: '2026-10-16T00:40:52.477207Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: historical-check-attempt-1
  kind: validation
  reference: /private/tmp/aimech-cohort355-check-vendor.json
  snapshot_sha256: 52ca55ee5150b7bde249db76e97894186e09ddf201261f37c58f40747d2d8dde
  accessed_at: '2026-10-16T00:37:35.326036Z'
  support: context_only
  summary: Actual failed attempt, retained with its later successful same-command
    replacement.
assessments:
- assessment_id: softq-claim-entropy-objective
  area: evidence
  topic: entropy-objective
  outcome: supported
  summary: Main Equation 2 adds conditional policy entropy and Section 2.1 distinguishes
    future entropy from greedy Boltzmann exploration. Appendix A explicitly qualifies
    discount weighting; the claim does not adopt its inconsistent first display as
    a corrected executable objective.
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-claim-energy-policy
  area: evidence
  topic: energy-policy
  outcome: supported
  summary: Main Equations 3–6 identify the target Boltzmann distribution and alpha-scaled
    log normalizer. The claim requires finite positive normalization and distinguishes
    the exact target identity from expressivity or sampling guarantees for finite
    neural networks.
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-claim-soft-backup
  area: evidence
  topic: soft-backup
  outcome: supported
  summary: Main Theorem 3 and Appendix A.2 concern the exact soft expected backup
    with bounded values and finite partitions. The statement retains those premises
    and does not transfer the fixed-point result to replay, neural projection or approximate
    sampling.
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-claim-approximate-value-fit
  area: evidence
  topic: approximate-value-fit
  outcome: supported
  summary: Main Equation 10 is an importance-weighted integral representation, and
    Algorithm 1 uses its empirical estimate with delayed parameters before fitting
    Equation 11. The claim describes this estimator without asserting log-unbiasedness
    or a globally valid sampler density.
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-claim-amortized-stein-sampler
  area: evidence
  topic: amortized-stein-sampler
  outcome: supported
  summary: 'Main Equation 13 defines action-gradient attraction plus alpha-scaled
    kernel repulsion, and Equation 14/C.1 project the finite-particle direction through
    the sampler. The third citation is context only: pinned later code minimizes a
    negative surrogate. The positive update direction is not silently relabeled the
    literal ordinary KL gradient.'
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-claim-replay-alternation
  area: evidence
  topic: replay-alternation
  outcome: supported
  summary: Algorithm 1 and Section 3.4 explicitly interleave interaction, replay minibatches,
    value/sampler updates and periodic target copies. This defines the reusable method
    without certifying a unique implementation schedule, terminal convention or trained
    policy result.
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-limitation-1
  area: scope
  topic: Limitation 1
  outcome: supported
  summary: 'For alpha>0 and finite positive partitions, Q1<=Q2+epsilon implies V1<=V2+epsilon.
    Reversing the inequality bounds the soft-value difference by the sup norm of Q1-Q2;
    the exact expected backup is gamma-Lipschitz for 0<=gamma<1 on an appropriate
    complete bounded function class. This hand check does not certify all theorem
    premises, an arbitrary action measure, or convergence after neural projection,
    finite sampling and nonconvex SGD. Locator: Main Theorem 3, PDF pp. 3–4; supplement
    Appendix A.2, PDF pp. 12–13.'
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-limitation-2
  area: scope
  topic: Limitation 2
  outcome: supported
  summary: 'If independent proposal samples have positive weights w=exp(Q/alpha)/q
    and E[w]=Z, the sample mean estimates Z; applying alpha log generally introduces
    downward Jensen bias whenever the mean is nonconstant and the required expectations
    exist. Exact normalized q=exp(Q/alpha)/Z for the same Q makes all weights equal
    to Z, eliminating this sampling variation. An approximate sampler, especially
    one targeting a different delayed Q, does not meet that equality automatically.
    No numerical experiment was run. Locator: Main Section 3.2, Equation 10, PDF p.
    4; supplement C.2, PDF p. 14.'
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-limitation-3
  area: scope
  topic: Limitation 3
  outcome: supported
  summary: 'Equal dimension and a nonsingular Jacobian at a point ensure only a local
    inverse. A density through a many-to-one smooth map requires summing over regular
    preimages (with appropriate domain conditions). For f(x)=x^2, standard-normal
    x and y>0, the two branches give pY(y)=[phi(sqrt(y))+phi(-sqrt(y))]/(2 sqrt(y));
    one-branch Equation 33 gives half that density. Switching from uniform samples
    after training does not establish global injectivity. No failure of a particular
    trained sampler is claimed. Locator: Supplement Appendix C.2, Equation 33, PDF
    p. 14.'
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-limitation-4
  area: scope
  topic: Limitation 4
  outcome: supported
  summary: 'Equation 13 is a Stein transport/descent direction for KL; Equation 14
    labels its positive projection a gradient. Hand witness: alpha=1, Q(a)=-a^2/2,
    constant positive-semidefinite kernel k=1, and sampler a=xi+phi with xi standard
    normal give KL(N(phi,1)||N(0,1))=phi^2/2, ordinary derivative phi, but projected
    Stein direction -phi. Thus minimizing with the literal positive projected direction
    as an ordinary gradient would reverse this simple descent direction. The paper
    calls it an optimal functional direction rather than a strict gradient. The pinned
    2019 code forms the projected direction and minimizes the negative surrogate,
    consistent with following the transport direction. This is a notation/sign-convention
    limitation, not a demonstrated implementation failure or full exact-gradient equivalence.
    Locator: Main Equations 12–14, PDF p. 5; supplement C.1, PDF pp. 13–14; pinned
    later code lines 247–268 (context).'
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-limitation-5
  area: scope
  topic: Limitation 5
  outcome: supported
  summary: 'The source explicitly distinguishes discounted policy-gradient weighting
    from a plain globally discounted state-occupancy objective. Its first Appendix
    A display uses r(s_t,a_t) and H(pi(.|s_t)) inside a future-l sum, whereas nearby
    prose describes future rewards/entropies and Equation 15 indexes future terms.
    Retain this displayed-index inconsistency; recommend only a source-qualified reward-plus-entropy
    description, not a silent repaired objective or a universal trajectory-entropy
    identity. With residual r=Abar+Vtheta-Qtheta and the fixed target treated constant,
    the ordinary derivative of 0.5*r^2 is r*(grad V-grad Q). Equation 32 instead displays
    r*(grad Q-grad V), a descent direction. This reinforces the need to distinguish
    update direction from literal derivative. Do not import unqualified policy-gradient/soft-Q
    gradient equivalence from this display; no entire proof-invalidity claim is made.
    Locator: Supplement Appendix A first display/Equations 15–16, PDF p. 11; Appendix
    B Equation 32, PDF p. 13.'
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-limitation-6
  area: scope
  topic: Limitation 6
  outcome: supported
  summary: 'A zero population squared loss with positive sampling density ordinarily
    gives equality almost everywhere; pointwise equality needs additional regularity.
    Finite empirical zero does not prove either global statement. On unbounded Lebesgue
    action domains, bounded Q alone cannot ensure a finite partition; the finite-partition
    premise and selected domain/function class must be maintained. Differential entropy
    also depends on the fixed action reference measure and units. These are scope
    conditions, not experimental counterexamples. Locator: Main Sections 3.1–3.2,
    PDF pp. 3–4; supplement A.1–A.2 and C.2, PDF pp. 11–14.'
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-limitation-7
  area: scope
  topic: Limitation 7
  outcome: supported
  summary: 'Finite simulated tasks and pretraining/fine-tuning results do not establish
    universal multimodal coverage, performance, policy composition or global convergence.
    The complete later sql.py was read but not executed; its uniform action proposal,
    reward scaling, squash correction and target-Q implementation are version-specific
    context. Its code, dependencies, kernels, policies and environments were not fully
    audited as an executable system. Locator: Main Sections 5–6, PDF pp. 6–8; supplement
    D, PDF pp. 14–16; official version metadata and later author implementation context.'
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-definition-assessment
  area: identity
  topic: Definition and granularity
  outcome: supported
  summary: The selected 2017 procedure couples interactive soft Bellman fitting with
    an amortized Stein sampler; the target Boltzmann identity does not imply exact
    neural sampling. Main and supplement define one work.
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-identity-assessment
  area: identity
  topic: Historical identity and version boundaries
  outcome: supported
  summary: The selected 2017 procedure couples interactive soft Bellman fitting with
    an amortized Stein sampler; the target Boltzmann identity does not imply exact
    neural sampling. Main and supplement define one work. Keep the compound control
    algorithm distinct from its SVGD sampling component and maintained SAC/Q-learning
    neighbors. The actual captured identity notes implement the root current collection
    decisions; the original preview scope remains historical and is recorded in context_changes.
    Existing owner 909 has the current bounded disposition partially_addressed, with
    all prior IDs, discovery pointers and resolution objects retained.
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
  - current-identity-collection
  - current-context-assessment
  - root-decisions
- assessment_id: softq-mapping-assessment
  area: grounding
  topic: Explicit bounded AIO mapping
  outcome: supported
  summary: All nine exact AIO nodes and 71 incident-edge entries were read in research.
    The chosen RL relation is algorithm-to-task association, not exact or broad-match
    ontology identity; alternative generic-function/network/LLM classes are not substituted.
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-source-assessment
  area: evidence
  topic: Distinct source roles and reading scopes
  outcome: supported
  summary: 'Three rows: official main and supplement are two primary artifacts of
    one 2017 work; pinned 2019 code is official documentation used only as context.
    Paper accessed_at explicitly records actual local verification, not invented acquisition
    seconds. Historical research acceptance reading: {"root_primary_reading": {"path":
    "/private/tmp/aimech-soft-q-research-20261015/root-primary-reading.json", "sha256":
    "ec82498475f2ae36600109c34ac3222cbf8806e80b6f03a44f92add738ba1842"}, "scope":
    "Research accepted for TEMP data-only native draft: one SoftQLearning algorithm,
    no aliases, qualified related_match to AIO ReinforcementLearning, six claims and
    seven limitations. Canonical ownership and actual merged-base identity remain
    future steps.", "root_reading": "Read full dossier, analytic boundaries, all proposed
    claims/limitations, sources and identity assessment; all seven matching contents
    and provenance, ten native definition projections, six selected frontier objects,
    and nine complete AIO nodes with 71 incident edges. Read later sql.py lines 210–280
    for the projected positive transport and minimized negative surrogate. Prior source
    reading remains attributed by root-primary-reading; full five native record and
    full code reads are agent evidence, not relabeled root reading."}. Exact draft
    acceptance reading: {"scope": "Root full static module, inputs, sources, identity,
    six claim and seven limitation support reading; exact metadata-only successor
    read and accepted. Definition and claims retain 2017 method, finite approximation
    and source notation boundaries. Source context remains explicit and no exact code-version
    equivalence claimed.", "root_reading_scope": "Prior primary reading and research
    acceptance remain separately attributed. No new primary reread or independent
    approval is implied."}. This preparation did not newly inspect primary pages or
    execute the methods.'
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: softq-kind-assessment
  area: scope
  topic: Algorithm and operational scope
  outcome: supported
  summary: The record denotes the source-defined reusable algorithm, with the exact
    accepted scope and limitations.
  target_ids:
  - AIMech:SoftQLearning
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - record-softq
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-claim-target-and-particles
  area: evidence
  topic: target-and-particles
  outcome: supported
  summary: The target-score requirement and supplied initial particles are explicit
    in Algorithm 1. An x-independent positive normalizer cancels under the log gradient;
    the transported particle configuration is not a fixed parametric variational family.
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-claim-synchronous-kernel-update
  area: evidence
  topic: synchronous-kernel-update
  outcome: supported
  summary: Equation 8 averages over every j including the diagonal and uses old iteration-l
    particles for both arguments and scores. An in-place sequential mutation would
    define a different recurrence; no implementation was executed.
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-claim-population-variational-direction
  area: evidence
  topic: population-variational-direction
  outcome: supported
  summary: Theorem 3.1 has the negative Stein expectation, Lemma 3.2 uses the radius-D
    RKHS ball, and Theorem 3.3 identifies the unnormalized representer as negative
    functional gradient at the identity. Unit-ball normalization and population/empirical
    measures are not silently interchanged. The supplemental leading sign is explicitly
    qualified.
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-claim-rbf-specialization
  area: evidence
  topic: rbf-specialization
  outcome: supported
  summary: For k(u,x)=exp(-||u-x||²/h), its first-argument derivative is (2/h)(x-u)k.
    At one particle, unit diagonal and zero diagonal first derivative yield the target
    score. This is an exact recurrence reduction, not a MAP convergence guarantee
    or general-kernel normalization claim.
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-claim-practical-computation
  area: evidence
  topic: practical-computation
  outcome: supported
  summary: The operational recurrence uses scores and pair kernels, without transporting-density
    determinant evaluation or Metropolis rejection. Main prose discusses minibatch
    scores and pairwise approximations; their sampling/scaling differs from exact-score
    full sums. Later v3 is cited only to retain the Eq. 9 version/display context,
    not as independent mechanism evidence.
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2019-v3-context
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-limitation-1
  area: scope
  topic: Limitation 1
  outcome: supported
  summary: 'Smooth-density integration and valid global transforms are premises. Local
    nonsingularity is insufficient. The retained Lipschitz hand bound supplies an
    illustrative sufficient injectivity condition only, not an implementation safeguard
    or full domain proof. Locator: Main pp. 2–4; supplement A–B, pp. 1–2.'
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - src-liu2019-v3-context
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-limitation-2
  area: scope
  topic: Limitation 2
  outcome: supported
  summary: 'Finite particles assign positive mass to points of zero probability under
    a continuous target; absolute continuity fails and atomic KL is infinite. The
    empirical vector field approximates the smooth-population construction. Infinitesimal
    descent and reported experiments do not establish arbitrary finite-step convergence.
    Locator: Main p. 5 particle approximation discussion and p. 6 error-rate qualification;
    supplement D.'
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - src-liu2019-v3-context
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-limitation-3
  area: scope
  topic: Limitation 3
  outcome: supported
  summary: 'Identical particle locations give identical scores and zero RBF separation
    derivatives, so synchronous updates preserve coincidence. The median/log(n) domain
    caveat concerns the reported experimental heuristic, not every permissible Algorithm
    1 kernel. Locator: Main pp. 5–6; explicit hand consequence of Equation 8.'
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - src-liu2019-v3-context
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-limitation-4
  area: scope
  topic: Limitation 4
  outcome: supported
  summary: 'A general nonunit diagonal rescales the score contribution at n=1; distinct
    fixed particles with h→0 leave the self term score/n. Neither limiting direction
    nor a repulsion label establishes equal numerical steps, independent samples or
    universal anti-collapse. Locator: Main p. 5 Equation 8 and limiting prose; hand
    substitutions.'
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - src-liu2019-v3-context
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-limitation-5
  area: scope
  topic: Limitation 5
  outcome: supported
  summary: 'Direct all-pair evaluation is quadratic in particle count; score-cost
    dominance is problem dependent. Minibatch and approximate pair sampling add assumptions
    and randomness, and no software implementation or benchmark was inspected. These
    are bounded implementation/evaluation limits rather than an observed failure.
    Locator: Main pp. 5–8 and supplement D.'
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - src-liu2019-v3-context
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-limitation-6
  area: scope
  topic: Limitation 6
  outcome: supported
  summary: 'The retained Gaussian-translation witness distinguishes the supplement
    leading sign from its proof; Algorithm 1 has explicit gradients whereas Eq. 9
    displays scalar log densities. Selected v3 pages retain these displays. Neither
    is treated as proof that the entire algorithm or every implementation is invalid.
    Locator: Main p. 5 Equation 9; supplement p. 1; arXiv v3 pp. 5 and 11.'
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - src-liu2019-v3-context
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-limitation-7
  area: scope
  topic: Limitation 7
  outcome: supported
  summary: 'The original toy prose/caption discrepancy was visually checked in research
    and no numerical toy conclusion is adopted. The original scalar-kernel recurrence
    does not confer coverage of later amortization, policy-gradient, matrix-kernel
    or convergence literature; prior citation leads remain separate. Locator: Main
    pp. 6–7, visually verified; original method scope and separately retained later-web/citation
    context.'
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - src-liu2019-v3-context
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-definition-assessment
  area: identity
  topic: Definition and granularity
  outcome: supported
  summary: The reusable source-defined scalar-kernel particle-inference recurrence
    is narrower than later amortized control methods and is distinguished from population
    transport theory.
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - src-liu2019-v3-context
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-identity-assessment
  area: identity
  topic: Historical identity and version boundaries
  outcome: supported
  summary: The reusable source-defined scalar-kernel particle-inference recurrence
    is narrower than later amortized control methods and is distinguished from population
    transport theory. Keep the original particle inference algorithm distinct from
    its amortized use in Soft Q-learning and other variational or stochastic methods.
    The actual captured identity notes implement the root current collection decisions;
    the original preview scope remains historical and is recorded in context_changes.
    Existing owner 909 has the current bounded disposition partially_addressed, with
    all prior IDs, discovery pointers and resolution objects retained.
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - src-liu2019-v3-context
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
  - current-identity-collection
  - current-context-assessment
  - root-decisions
- assessment_id: svgd-mapping-assessment
  area: grounding
  topic: Explicit bounded AIO mapping
  outcome: supported
  summary: All eight exact pinned contexts and 32 incident edges were read in research.
    No scalar-only interpretation of MathematicalFunction is used. No positive mapping
    field is emitted. The actual no-match search_scope is the separately recorded
    current root assessment; its accepted rationale and examined-target rejections
    remain unchanged.
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - src-liu2019-v3-context
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
  - current-identity-collection
  - current-context-assessment
  - root-decisions
- assessment_id: svgd-source-assessment
  area: evidence
  topic: Distinct source roles and reading scopes
  outcome: supported
  summary: 'Three declared rows: official main and downloaded supplement ZIP are defining
    artifacts of one 2016 work; the sole appendix PDF is separately checksum-bound.
    Later combined arXiv v3 is context only. Actual original acquisition times are
    preserved. Historical research acceptance reading: {"reading_scope": "Root previously
    read all nine original main text pages and main visuals 4–5. Root now read all
    four official supplement text pages and supplement visual 1, full dossier, source
    ledger and reading scopes, all proposed five claims/seven limitations and analytic
    boundaries, identity/mapping/citation assessments, all eight pinned AIO node/edge
    contexts, and eight maintained identity/definition/mapping projections. Later-v3
    selected reading, other declared original visuals, two full native records and
    sixteen selected frontier bodies remain attributed to the supporting researcher.
    No whole later-version or software inspection is claimed."}. Exact draft acceptance
    reading: {"scope": "Root read exact static module and sources before restart;
    inputs, time projection, identity and complete support after restart, including
    truncation recovery for limitations2/3. All5claims/7limitations and8explicit AIO
    rejections agree with accepted original source reading. Defining main/appendix
    belong to one2016work; appendix row hashes downloaded ZIP and separately binds
    extractedPDF; later v3 has only inspected context scope. No new visual reading
    or future-base identity clearance claimed. Mechanical AST/support equality checked
    separately."}. This preparation did not newly inspect primary pages or execute
    the methods.'
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - src-liu2019-v3-context
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: svgd-kind-assessment
  area: scope
  topic: Algorithm and operational scope
  outcome: supported
  summary: The record denotes the source-defined reusable algorithm, with the exact
    accepted scope and limitations.
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - src-liu2019-v3-context
  - record-svgd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: citation-accounting
  area: ownership
  topic: citation-accounting
  outcome: supported
  summary: Owner 909 remains a partial source-discovery group for two distinct concepts.
    Three original citation entries and five bibliography questions remain fully queryable;
    fresh semantic assessments retain existing records or responsible owners when
    found. Seven pending source questions do not assert seven missing concepts. No
    main or nested row is appended.
  target_ids:
  - AIMech:SoftQLearning
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - root-decisions
  - discovery-report
  - governance-assessment
  - actual-scientific-assessment
- assessment_id: inherited-governance
  area: provenance
  topic: inherited-governance
  outcome: supported
  summary: The exact actual 354/353/352 governance snapshots, restoration provenance
    and separate issue 402 bibliography triage are preserved. No prior repair or closure
    is repeated. Separate issue404 accounting assigns future inspection responsibility
    for six pending questions and seven scoped attachments, preserving exact source
    questions and existing owner objects; no research completion is inferred.
  target_ids:
  - AIMech:SoftQLearning
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - root-decisions
  - discovery-report
  - governance-assessment
  - actual-scientific-assessment
- assessment_id: actual-correspondence
  area: provenance
  topic: actual-correspondence
  outcome: supported
  summary: Two DRAFT records preserve eleven accepted claims and fourteen limitations.
    Four defining artifacts belong to two works; later code and later arXiv v3 remain
    two context artifacts. Only owner 909 changes; all 912 other main and 394 nested
    objects remain exact. Five exclusive outputs, one CREATE history, 44 capture inputs,
    actual pages and six completed checks are bound. Original citation questions and
    separate inherited issue 402 triage remain explicit. No independent approval or
    exhaustion is implied.
  target_ids:
  - AIMech:SoftQLearning
  - AIMech:SteinVariationalGradientDescent
  evidence_ids:
  - actual-write
  - captured-inputs
  - postcapture-reading
  - governance-assessment
  - rendered-pages
  - actual-scientific-assessment
  - creation-history
  - root-decisions
  - check-gate
  - check-vendor
  - check-check-source
  - check-render
  - check-render-check
  - check-diff
targets:
- target_id: AIMech:SoftQLearning
  label: Soft Q-learning
  path: data/curated/SoftQLearning.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SoftQLearning.yaml
    role: maintained native concept record
- target_id: AIMech:SteinVariationalGradientDescent
  label: Stein variational gradient descent
  path: data/curated/SteinVariationalGradientDescent.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SteinVariationalGradientDescent.yaml
    role: maintained native concept record
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:SoftQLearning
  rationale: The selected 2017 procedure couples interactive soft Bellman fitting
    with an amortized Stein sampler; the target Boltzmann identity does not imply
    exact neural sampling. Main and supplement define one work. Keep the compound
    control algorithm distinct from its SVGD sampling component and maintained SAC/Q-learning
    neighbors.
  evidence_ids:
  - preview-softq
  - support-softq
  - draft-acceptance-softq
  - preview-validation-softq
  - root-research-softq
  - preparation-reading-softq
  - historical-identity-softq
  - src-haarnoja2017-main
  - src-haarnoja2017-supp
  - src-haarnoja-code-context
  - root-decisions
  - current-identity-collection
- action: retain
  target_ids:
  - AIMech:SteinVariationalGradientDescent
  rationale: The reusable source-defined scalar-kernel particle-inference recurrence
    is narrower than later amortized control methods and is distinguished from population
    transport theory. Keep the original particle inference algorithm distinct from
    its amortized use in Soft Q-learning and other variational or stochastic methods.
  evidence_ids:
  - preview-svgd
  - support-svgd
  - draft-acceptance-svgd
  - preview-validation-svgd
  - root-research-svgd
  - preparation-reading-svgd
  - historical-identity-svgd
  - src-liu2016-main
  - src-liu2016-supplement
  - src-liu2019-v3-context
  - root-decisions
  - current-identity-collection
```
