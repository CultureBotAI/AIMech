# Scientific self-review of Dutch eligibility traces and true online GTD(lambda)

- Review: 20261015T173405Z-dutch-eligibility-traces-and-true-online-gtd
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-15T17:20:41.334787Z
- Finished UTC: 2026-10-15T17:34:05.947062Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Dutch eligibility traces as the source-qualified mathematical component and true online GTD(lambda) as the specified linear off-policy state-value algorithm. All eleven claims, fourteen individual limitations and four exact primary artifacts are assessed through attributed source/math reading and actual canonical correspondence. The qualified MathematicalFunction and ReinforcementLearning mappings express different abstraction levels. Actual capture, owner preservation, generated pages and six completed required checks are bound; no independent approval or residual exhaustion is implied.

## Scope And Provenance

Complete explicitly selected two-record cohort in the captured current canonical state.

Selection: Exact IDs: AIMech:DutchEligibilityTraces, AIMech:TrueOnlineGTDLambda.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 9799fa6e2cb303d940fcb56249830c333cac7c90.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:DutchEligibilityTraces | data/curated/DutchEligibilityTraces.yaml | maintained | Dutch eligibility traces |
| AIMech:TrueOnlineGTDLambda | data/curated/TrueOnlineGTDLambda.yaml | maintained | True online GTD(lambda) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:DutchEligibilityTraces, AIMech:TrueOnlineGTDLambda | Actual successful command; exact output is retained. |
| just vendored-check | passed | True | AIMech:DutchEligibilityTraces, AIMech:TrueOnlineGTDLambda | Actual successful command; exact output is retained. |
| uv run --locked aimech check-source | passed | True | AIMech:DutchEligibilityTraces, AIMech:TrueOnlineGTDLambda | Actual successful command; exact output is retained. |
| just render | passed | True | AIMech:DutchEligibilityTraces, AIMech:TrueOnlineGTDLambda | Actual successful command; exact output is retained. |
| just render-check | passed | True | AIMech:DutchEligibilityTraces, AIMech:TrueOnlineGTDLambda | Actual successful command; exact output is retained. |
| git diff --check | passed | True | AIMech:DutchEligibilityTraces, AIMech:TrueOnlineGTDLambda | Actual successful command; exact output is retained. |
| Historical attempt: just vendored-check | failed | False | AIMech:DutchEligibilityTraces, AIMech:TrueOnlineGTDLambda | Retained failed attempt; actual successful replacement cited separately. |

## Scientific And Domain Assessments

### Claim named-trace-component

evidence: supported. Targets: AIMech:DutchEligibilityTraces.

UAI names the general recurrence on p. 4 after displaying it on p. 3. JMLR explicitly calls Equation 11 the Dutch trace and Equation 12’s extra weight term the delta-correction. The statement therefore identifies a reusable mathematical component and does not inherit the host’s complete learning behavior.

### Claim scaled-vector-recurrence

evidence: supported. Targets: AIMech:DutchEligibilityTraces.

Initialization and every scalar/vector term match UAI Equation 3, visually checked in the retained research. The trace’s old-state inner product is explicit. Expanding c*(I-eta*phi*phi^T)*E_old yields the same recurrence; no separate matrix implementation is prescribed. The theorem’s target condition is retained in limitations rather than implied by this formula alone.

### Claim td-step-size-conventions

evidence: supported. Targets: AIMech:DutchEligibilityTraces.

PMLR Equation 11 places alpha_t inside the trace, while JMLR Equation 11 is unscaled for constant alpha and Equation 16 restores the weighted convention. Induction from matched zero initialization gives E=alpha*e for constant alpha, with no division needed. The text retains earlier step-size history and does not silently substitute a time-varying alpha into the constant-step convention.

### Claim one-hot-specialization

evidence: supported. Targets: AIMech:DutchEligibilityTraces.

Substituting a one-hot feature into JMLR Equation 11 gives the exact displayed Section 6.3 cases. Combining the accumulating and replacing update maps from the same old vector yields the displayed coefficients. Alpha in [0,1] is required for convexity; alpha=1 concerns the trace map only. Algorithm 6’s delayed decay placement is not copied into a conflicting time index.

### Claim rank-one-memory-cost

evidence: supported. Targets: AIMech:DutchEligibilityTraces.

The inner product and scaled vector operations make the dense recurrence O(n) without explicitly storing its n-by-n algebraic matrix. The source discusses O(n) backward methods; the statement narrows the claim to trace bookkeeping and excludes feature, action and host costs, without asserting sparsity or wall-clock superiority.

### definition assessment

evidence: supported. Targets: AIMech:DutchEligibilityTraces.

UAI provides the named general vector recurrence, and JMLR distinguishes the trace from the complete weight update. The definition selects the mathematical credit component with explicit source-dependent scaling, not an entire learning algorithm or a coordinatewise clipping operator.

### mapping assessment

grounding: supported. Targets: AIMech:DutchEligibilityTraces.

The component defines a deterministic vector-valued update from prior trace, current feature vector and scalar parameters. This supports a qualified mathematical-rule association with the pinned generic function class, without exact identity, an asserted subclass edge, a scalar-output restriction or a neural-activation claim.

### source assessment

provenance: supported. Targets: AIMech:DutchEligibilityTraces.

Three exact primary versions are declared and all are cited. PMLR 2014 supplies the earlier scaled formula, UAI 2014 the explicit name/general recurrence, and JMLR 2016 the separate component, unscaled/time-dependent and tabular conventions. Original access precision and reuse versus new acquisition are retained. UAI paper 324 is an identifier, not claimed pagination; no exact publication day or DOI was inferred. Fresh Dutch research read PMLR 2014 native/visual p. 5; JMLR 2016 native pp. 12, 22–23, 25–27 and 40, and visuals pp. 12, 23 and 25; UAI 2014 native pp. 1–4 and visuals pp. 3–4. Preparation reuses those exact bounded readings, with root source/identity scope separately attributed. No full UAI off-policy algorithm or complete 40-page proof reading is claimed.

### identity assessment

identity: supported. Targets: AIMech:DutchEligibilityTraces.

Retain the named mathematical trace component separately from complete TD, Sarsa and GTD algorithms, generic eligibility and coordinatewise replacing traces. The same old-state one-hot interpolation is not equality of separately evolved histories. The actual captured identity notes implement the root current collection decisions; the original preview scope remains historical and is recorded in context_changes. Existing owner 264 stays partial, with four prior IDs and all three prior resolution objects retained.

### kind-and-status assessment

scope: supported. Targets: AIMech:DutchEligibilityTraces.

The accepted mathematical_method representation selects a vector-valued credit-update component rather than a full host learner. DRAFT status is retained; mapping does not imply an asserted subclass or exact identity.

### Limitation 1

scope: supported. Targets: AIMech:DutchEligibilityTraces.

The UAI theorem requires a specific linear forward update and scalar relation among target changes. Host weight correction is not an optional consequence of storing the trace. This prevents conflation with the complete maintained TD/Sarsa algorithms or generic eligibility mechanisms.

The component is distinct from complete true online TD or Sarsa, the general eligibility family and an entire forward-view learning algorithm. In the UAI theorem, forward/backward weight equality also requires its linear weight updates, companion correction and horizon-independent target-difference relation; inserting only this trace into an arbitrary host does not establish that equality.

### Limitation 2

scope: supported. Targets: AIMech:DutchEligibilityTraces.

The scaling identity is restricted to constant alpha. A current alpha_t=0 yields q*E_old in the scaled formula, which can retain earlier credit; a constant-zero step size with zero initialization keeps the scaled trace zero. This is an algebraic convention boundary, not a learning convergence claim.

The scaled and unscaled conventions must be matched to the host update. Constant-alpha rescaling E=alpha*e does not justify the substitution E_t=alpha_t*e_t for varying step sizes. Division by alpha is undefined at alpha=0. A current zero alpha_t in the scaled recurrence leaves the decayed previous trace when earlier step sizes produced nonzero credit.

### Limitation 3

scope: supported. Targets: AIMech:DutchEligibilityTraces.

The source specialization is explicitly tabular. An affine combination evaluated from the common old state is not the same assertion as mixing separately evolved accumulator and replacer histories. The inner-product coupling for overlapping features prevents a general coordinatewise reset interpretation.

The accumulating/replacing relation is an identity between one-hot update maps evaluated from the same old trace, not a mixture of separately evolved trace histories. It does not extend as a coordinatewise replacing rule to arbitrary overlapping binary or real features. Coincident one-hot trace updates do not make the complete learning algorithms identical.

### Limitation 4

scope: supported. Targets: AIMech:DutchEligibilityTraces.

Multiplying Equation 3 by phi^T gives z+h*(1-z) with h=eta*&#124;&#124;phi&#124;&#124;². The bound h in [0,1] ensures monotone non-overshooting movement for any starting projection; arbitrary norms/eta do not. Hand examples already retained show a one-hot value above one and a negative value with positive scalar features. No trained-model failure is inferred.

Dutch traces are not coordinatewise clipping and need not remain nonnegative or within [0,1]. In the general scaled recurrence, if z=c*phi^T*E_old and h=eta*&#124;&#124;phi&#124;&#124;^2, then phi^T*E_new=z+h*(1-z). For any starting projection, h in [0,1] keeps the new projection between its old value and one; unrestricted feature norms or step sizes can overshoot or amplify the deviation. The source phrase toward one does not imply exact unit attainment.

### Limitation 5

scope: supported. Targets: AIMech:DutchEligibilityTraces.

Theorem 1 constrains horizon dependence, not &#124;c&#124;. The rank-one transition has eigenvalues c*(1-eta*&#124;&#124;phi&#124;&#124;²) in the feature direction and c orthogonally. Its magnitude depends on parameters and features, so no uniform contraction or statistical performance follows from the name or recurrence.

The general UAI coefficient c is a scalar independent of the data horizon, not necessarily a number in [0,1]. Its description as shrinking requires additional magnitude conditions. The transition c*(I-eta*phi*phi^T) has feature-direction factor c*(1-eta*&#124;&#124;phi&#124;&#124;^2), so the recurrence supplies no unconditional numerical stability, contraction, convergence, variance reduction or performance guarantee.

### Limitation 6

scope: supported. Targets: AIMech:DutchEligibilityTraces.

The trace can be numerically formed for supplied vectors, but the exact forward-view argument uses linear learned weights and the specified sequence. Distinguishing recurrence evaluation from theorem applicability prevents an unsupported nonlinear-learning transfer. Dense complexity is a scoped arithmetic count.

The source forward-view derivations concern linear prediction in the learned weights with the specified feature/target sequence and matching initialization. The vector trace formula can be evaluated on supplied features, but generic nonlinear or parameter-dependent feature learning does not automatically inherit those derivations. Dense O(n) bookkeeping does not imply cost proportional only to the current number of nonzero features or a universal wall-clock advantage.

### Limitation 7

scope: supported. Targets: AIMech:DutchEligibilityTraces.

Each version’s role and the JMLR naming attribution were read. The specific local display omissions/cross-reference are recorded from visuals/text without claiming an official erratum, invalidity of Equation 3 or a complete proof certification. Earlier source access failures and the lack of author-code inspection remain explicit provenance.

The 2014 PMLR paper supplies the earlier scaled recurrence; the 2014 UAI paper explicitly names the general form Dutch traces; the 2016 journal article presents unscaled, time-dependent and tabular conventions and attributes the name to van Hasselt and colleagues. This is inspected source lineage, not an exhaustive priority claim. The UAI proof locally omits +x_k in its first F_k restatement although the theorem and later expansion retain those terms, and the 2016 prose after Equation 17 points to Algorithm 2 although the local time-dependent box is Algorithm 4. These bounded display observations are not a certified defect of the trace recurrence, an official erratum or a full proof audit. No author implementation or benchmark reproduction is certified.

### Claim linear-off-policy-state-value

evidence: supported. Targets: AIMech:TrueOnlineGTDLambda.

Sections 1–2 explicitly define pi/b sampling and linear state-value prediction; Section 8 excludes an action-value extension from the selected method. Coverage is a condition, not an assumed property of arbitrary behavior data.

### Claim error-weighted-interim-forward-views

evidence: supported. Targets: AIMech:TrueOnlineGTDLambda.

Equations 14–18 separate the two replay targets and use w_k=w_k^k in the theta correction. This states a particular sampled construction and deliberately avoids calling an evolving online update an exact MSPBE gradient. Equation 13’s dimension problem is retained separately.

### Claim three-distinct-eligibility-traces

evidence: supported. Targets: AIMech:TrueOnlineGTDLambda.

Every factor was checked against the first-author visual p. 7. Prediction trace e has rho_t outside and inside its Dutch correction; auxiliary e^w uses rho_(t−1) in decay/correction and beta_t in injection; g is the separate accumulating e-nabla trace. The old-state inner products and step-size scaling remain literal.

### Claim coupled-prediction-and-auxiliary-update

evidence: supported. Targets: AIMech:TrueOnlineGTDLambda.

The first-author version resolves the original unindexed gamma in delta. The theta correction uses the previous-weight current prediction, and both coupled right sides use old w/theta with new traces. In-place recomputation is not implicitly authorized.

### Claim finite-horizon-linear-correspondence

evidence: supported. Targets: AIMech:TrueOnlineGTDLambda.

Theorem 1’s horizon-independent relation and the distinct c/eta substitutions in Theorems 3–4 are explicit. This is correspondence on fixed realized data and matching replay initialization, not a universal objective/convergence assertion. Constant numbers of vector operations justify dense linear arithmetic/storage.

### Claim gtd-zero-and-forward-view-boundary

evidence: supported. Targets: AIMech:TrueOnlineGTDLambda.

Direct substitution of all lambda=0 values yields the displayed GTD(0) pair and zero prediction-change correction. The source discussion on p. 9 leaves full off-policy Monte Carlo equivalence to a different weighting choice. No endpoint claim collapses the full method into ordinary TD or control.

### definition assessment

evidence: supported. Targets: AIMech:TrueOnlineGTDLambda.

The source explicitly names the complete off-policy state-value algorithm and gives the coupled updates. The definition identifies its three-trace and auxiliary-weight mechanism without asserting complete convergence or exact identity with a broad RL task.

### mapping assessment

grounding: supported. Targets: AIMech:TrueOnlineGTDLambda.

The algorithm estimates a specified policy’s state values from reward transitions generated by a potentially different behavior policy. This supplies prediction machinery used in reinforcement learning. The pinned class is a broader learning task involving exploration/performance optimization; the relation does not claim exact identity, an algorithm-to-task subclass edge, action selection, policy improvement or convergence.

### source assessment

provenance: supported. Targets: AIMech:TrueOnlineGTDLambda.

The exact first-author-hosted 2014 paper supplies the indexed method. Conference, reissue and coauthor versions remain separately retained; directory naming is not a verified revision date. Local display discrepancies and the projection-residual qualification are explicit, without complete proof or implementation certification. Source-agent scope: original UAI native pages 1–10 and visuals 2, 5–7; coauthor changed page 2 visual and whole-text comparison; first-author complete normalized differences plus native pages 6–7 and visuals 5–8. Later same-author adversarial scope: first-author native pages 1–9, visuals 3, 5–8, and version differences 2, 6–7. These are distinct readings; neither certifies the whole proof, all plots or author software.

### identity assessment

identity: supported. Targets: AIMech:TrueOnlineGTDLambda.

Retain the specified linear off-policy state-value algorithm separately from the Dutch component, on-policy TD/Sarsa, GTD/GQ in general, control and WIS variants. Shared traces do not establish identical complete updates. The actual captured identity notes implement the root current collection decisions; the original preview scope remains historical and is recorded in context_changes. Existing owner 264 stays partial, with four prior IDs and all three prior resolution objects retained.

### kind-and-status assessment

scope: supported. Targets: AIMech:TrueOnlineGTDLambda.

The accepted algorithm representation selects the coupled linear off-policy state-value algorithm rather than the general reinforcement-learning task. DRAFT status is retained; mapping does not imply an asserted subclass or exact identity.

### Limitation 1

scope: supported. Targets: AIMech:TrueOnlineGTDLambda.

The final correction retains w whenever rho=1 and lambda_next&lt;1 in general. The source’s state-value-only and alternative-forward-view discussion distinguish the nearest algorithms and components without assuming disjoint mathematical endpoints.

This is the original linear state-value off-policy algorithm, not GTD/GQ in general, an action-value controller, true online TD/Sarsa, WIS variants or Dutch/replacing traces alone. Setting every importance ratio to one does not generally eliminate the auxiliary gradient correction for lambda&lt;1. A zero (1−lambda_(t+1)) factor removes that explicit correction, but does not by itself establish identity with every Monte Carlo algorithm.

### Limitation 2

scope: supported. Targets: AIMech:TrueOnlineGTDLambda.

Equation 8 uses a behavior distribution and inverse covariance. Finite sequence algebra does not prove statistical coverage, finite moments, convergence or policy optimization; these distinct requirements remain stated rather than silently certified.

Finite-horizon equality to the specified sampled forward views is an algebraic statement, not a proof that each online step is an unbiased MSPBE gradient or that the coupled iterates converge, are stable, improve monotonically or reach an optimal policy. The expected objective uses a behavior-state distribution and an invertible feature second-moment matrix; existence of relevant returns/expectations, sufficient target-action support under behavior, and other convergence assumptions cannot be inferred merely from the update display.

### Limitation 3

scope: supported. Targets: AIMech:TrueOnlineGTDLambda.

The displayed initial e and e^w values and zero-history g give the first-step cancellation. Stored prior prediction, current/prior ratio indices and old coupled weights were checked directly. Replacing the accumulating correction trace is only a proposed alternative in the source, not the defined method.

The derivation uses linear, fixed features and matched replay sequences. The source initializes e_0=alpha_0 rho_0 phi_0 and e^w_0=beta_0 phi_0; a zero pre-initial accumulating trace gives g_0=rho_0 phi_0. The first theta correction cancels, so no arbitrary theta_(−1) affects that first update. Later theta_(t−1)^T phi_t is a stored preceding-weight prediction, not a recomputation under theta_t. Replacing w_t by w_(t+1), swapping current and previous importance ratios, or simply replacing g with a Dutch trace changes the specified construction. Nonlinear or parameter-dependent features need separate justification.

### Limitation 4

scope: supported. Targets: AIMech:TrueOnlineGTDLambda.

Step sizes are embedded in distinct Dutch histories. Setting a current alpha or beta to zero leaves a decayed old trace in general. General scalar ratios/features do not supply a unit-coordinate bound, and dense arithmetic does not assert sparse-current-feature or wall-clock complexity.

Alpha_t and beta_t are inside two different scaled traces; a constant-alpha unscaled TD/Sarsa convention cannot be substituted without a matched derivation. A zero current step size does not in general erase trace contributions from earlier nonzero steps. Importance ratios need not be at most one, and these Dutch or accumulating traces are not generally nonnegative or coordinatewise bounded by one. Linear dense cost excludes feature construction and does not imply cost only in current nonzero features.

### Limitation 5

scope: supported. Targets: AIMech:TrueOnlineGTDLambda.

Fresh original visuals2/5–7 and first-author visuals5–7 support the precise local display observations. The explicit Equation 18/theorem/final recurrence remains identifiable. No blanket invalidity or complete proof certification is inferred.

The inspected source retains mixed t/k indexing and the recursive superscript in Equation 6, and a scalar/vector mismatch in Equation 13 and nearby expectation prose. Its first proof restatement on PDF p. 3 also omits x_k despite its presence in the theorem and later algebra. These are bounded source-display observations; the explicit forward and backward updates remain separately identifiable. This record neither certifies nor invalidates the entire proof or author implementation.

### Limitation 6

scope: supported. Targets: AIMech:TrueOnlineGTDLambda.

The retained analytic projection decomposition gives the nonnegative irreducible term under well-defined full-return and orthogonality conditions. The p. 8 literal equality is therefore qualified, while minimizer agreement in that setting remains possible.

The statement on PDF p. 8 that MSPBE equals MSE at lambda=1 needs qualification. When the full-return operator yields v_pi and Pi is the stated d-orthogonal projection, MSE=J+&#124;&#124;Pi*v_pi-v_pi&#124;&#124;_d^2. The objectives then have the same minimizers, but their values are equal only when the projection residual vanishes. This direct projection identity does not establish convergence of the online algorithm.

### Limitation 7

scope: supported. Targets: AIMech:TrueOnlineGTDLambda.

The declared source is the first-author acquired byte version and actual access time. Original/reissue/coauthor comparisons and genuine DNS failures/retries are bound in the preparation records, not misrepresented as a dated published erratum. No native empirical superiority claim is added.

The evidence source is the exact acquired first-author-hosted version of the 2014 paper, with indexed discount/bootstrap expressions in Equation 16 and the final update. The retained conference, reissue and coauthor copies differ in the discount-product endpoint or some time indices; no verified revision date or comprehensive erratum notice is asserted. Experimental comparisons remain tied to the reported random-walk settings, representations and parameter searches, not universal superiority. No author software or benchmark reproduction is certified.

### Actual canonical, capture, frontier, history, rendered-page and check correspondence

provenance: supported. Targets: AIMech:DutchEligibilityTraces, AIMech:TrueOnlineGTDLambda.

Both current records equal the actual write/report entries and accepted science: eleven claims, fourteen individual limitations and four exact primary artifacts. Five files were created and one CREATE history records the session. Only owner 264 changed; four prior IDs and cohort 343/344/345 resolutions remain, with 908 other main and 393 nested objects unchanged. Every captured input and actual rendered page hash was checked. Six required checks passed; DRAFT and partial residual scope remain.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:DutchEligibilityTraces. Retain the named mathematical trace component separately from complete TD, Sarsa and GTD algorithms, generic eligibility and coordinatewise replacing traces. The same old-state one-hot interpolation is not equality of separately evolved histories. Both outcomes belong to existing partially addressed owner 264; four prior IDs and cohort 343/344/345 resolutions must be retained. Residuals and unrelated owners are not exhausted.
- retain: AIMech:TrueOnlineGTDLambda. Retain the specified linear off-policy state-value algorithm separately from the Dutch component, on-policy TD/Sarsa, GTD/GQ in general, control and WIS variants. Shared traces do not establish identical complete updates. Both outcomes belong to existing partially addressed owner 264; four prior IDs and cohort 343/344/345 resolutions must be retained. Residuals and unrelated owners are not exhausted.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| preview-dutch | /private/tmp/aimech-dutch-traces-draft-preparation-20261015/native-preview.json | context_only | Actual accepted TEMP native payload, not a canonical creation. |
| support-dutch | /private/tmp/aimech-dutch-traces-draft-preparation-20261015/scientific-support.json | context_only | Original claim and limitation narratives with separately attributed bounded primary reading; historical preparation tense remains historical. |
| draft-acceptance-dutch | /private/tmp/aimech-dutch-traces-draft-preparation-20261015/root-draft-acceptance.json | context_only | Root read complete data-only module, inputs and all3 source rows; full5 claim and7 limitation support narratives, recovering initially truncated limit2/3. Research acceptance retains primary text/visual and7AIO43edge scope. Component, scaling, projection, one-hot, cost and source-display qualifications are accepted; no implementation, full proof or benchmark execution inferred. |
| preview-validation-dutch | /private/tmp/aimech-dutch-traces-draft-preparation-20261015/native-preview-validation.json | context_only | Actual TEMP native validation only; no canonical addition, current identity clearance, gate or independent scientific approval. |
| source-reading-dutch | /private/tmp/aimech-dutch-traces-research-20261015/reading.json | context_only | Fresh Dutch research read PMLR 2014 native/visual p. 5; JMLR 2016 native pp. 12, 22–23, 25–27 and 40, and visuals pp. 12, 23 and 25; UAI 2014 native pp. 1–4 and visuals pp. 3–4. Preparation reuses those exact bounded readings, with root source/identity scope separately attributed. No full UAI off-policy algorithm or complete 40-page proof reading is claimed. |
| source-times-dutch | /private/tmp/aimech-dutch-traces-draft-preparation-20261015/source-time-projection.json | context_only | Original access precision and source-version lineage, distinct from this review preparation. |
| historical-identity-dutch | /private/tmp/aimech-dutch-traces-research-20261015/identity/assessment.json | context_only | Historical bounded identity interpretation; current merged-base assessment remains a separate future input. |
| src-vanseijen2014 | https://proceedings.mlr.press/v32/seijen14.pdf; Section 4.1, Equations 10–12 and Algorithm 2; scaled trace/host separation and initial zero trace. This task does not repeat the full nine-page or proof audit. | supports | Official PMLR nine-page ICML 2014 paper, Proceedings of Machine Learning Research 32(1):692–700. PDF heading prints lambda as a Greek symbol; the publisher metadata uses the text lambda. Access to complete bytes is not a claim that every page was read. |
| src-vanseijen2016 | https://www.jmlr.org/papers/volume17/15-599/15-599.pdf; Equation 11 versus correction Equation 12, time-varying scaled Equation 16/Algorithm 4, tabular specialization, historical naming and linear-scope discussion/bibliography. Page 22 experimental context is not promoted to a benchmark claim. The complete 40-page source and proof are not freshly audited. | supports | Official JMLR 17(145):1–40 (2016), 40-page article. Cover states Submitted 11/15; Revised 7/16; Published 8/16. Access to complete bytes is not a claim that every page was read. |
| src-vanhasselt2014 | https://auai.org/uai2014/proceedings/individuals/324.pdf; Abstract, setup, complete general theorem/trace recurrence and naming, and beginning of off-policy context. All ten pages were extracted, but only native pages 1–4 and visuals 3–4 were read. No full off-policy method/experiments certification. | supports | Official UAI 2014 proceedings individual paper 324, ten PDF pages. 324 is the conference paper identifier, not a page number. Exact publication day and DOI are not established by the inspected official pages. Access to complete bytes is not a claim that every page was read. |
| preview-gtd | /private/tmp/aimech-true-online-gtd-draft-preparation-20261015/native-preview.json | context_only | Actual accepted TEMP native payload, not a canonical creation. |
| support-gtd | /private/tmp/aimech-true-online-gtd-draft-preparation-20261015/scientific-support.json | context_only | Original claim and limitation narratives with separately attributed bounded primary reading; historical preparation tense remains historical. |
| draft-acceptance-gtd | /private/tmp/aimech-true-online-gtd-draft-preparation-20261015/root-draft-acceptance.json | context_only | Root read full data-only module, inputs, exact source/access projection, six claim and seven limitation assessments, definition/mapping/identity notes and cited locators. Source reading and paper-version qualifications are separately retained. Accepted for actual TEMP invocation/validation; no merged-base identity clearance or canonical creation asserted. |
| preview-validation-gtd | /private/tmp/aimech-true-online-gtd-draft-preparation-20261015/native-preview-validation.json | context_only | Actual TEMP native validation only; no canonical addition, current identity clearance, gate or independent scientific approval. |
| source-reading-gtd | /private/tmp/aimech-true-online-gtd-research-20261015/reading.json | context_only | Source-agent scope: original UAI native pages 1–10 and visuals 2, 5–7; coauthor changed page 2 visual and whole-text comparison; first-author complete normalized differences plus native pages 6–7 and visuals 5–8. Later same-author adversarial scope: first-author native pages 1–9, visuals 3, 5–8, and version differences 2, 6–7. These are distinct readings; neither certifies the whole proof, all plots or author software. |
| source-times-gtd | /private/tmp/aimech-true-online-gtd-draft-preparation-20261015/source-time-projection.json | context_only | Original access precision and source-version lineage, distinct from this review preparation. |
| historical-identity-gtd | /private/tmp/aimech-true-online-gtd-research-20261015/identity/assessment.json | context_only | Historical bounded identity interpretation; current merged-base assessment remains a separate future input. |
| src-vanhasselt2014-author | https://hadovanhasselt.com/wp-content/uploads/2015/12/off_policy_td.pdf; Source-agent scope: original UAI native pages 1–10 and visuals 2, 5–7; coauthor changed page 2 visual and whole-text comparison; first-author complete normalized differences plus native pages 6–7 and visuals 5–8. Later same-author adversarial scope: first-author native pages 1–9, visuals 3, 5–8, and version differences 2, 6–7. These are distinct readings; neither certifies the whole proof, all plots or author software. | supports | First-author-hosted ten-page version of the UAI 2014 paper. This acquired copy has a reward-discount product through t−1 and explicitly indexed discount/bootstrap expressions in Equation 16 and PDF p. 7. Its revision date is unspecified; the URL directory is not treated as a verified revision date. Access to complete bytes is not a claim that every page was read. |
| gtd-fresh-adversarial | /private/tmp/aimech-true-online-gtd-adversarial-20261015/assessment.json | context_only | Later same-author mathematical/source assessment: all six claims and seven limits, six hand analyses, exact source-version and reading limits; no numerical experiment or independent approval. |
| gtd-fresh-reading | /private/tmp/aimech-true-online-gtd-adversarial-20261015/reading.json | context_only | Later actual first-author text/visual scope, separate from the source-agent and root scopes. |
| gtd-input-successor | /private/tmp/aimech-true-online-gtd-draft-preparation-20261015/acceptance-binding.json | context_only | Metadata-only inputs.final.json successor retains original validated inputs.json; it does not retroactively alter the native validation. |
| dutch-fresh-adversarial | /private/tmp/aimech-dutch-traces-supporting-math-audit-20261015/assessment.json | context_only | Later attributed Dutch same-author source/math audit: UAI text/visual 3–4, PMLR text/visual 5, JMLR text 12, 22–23, 25–26 and visuals 12, 23, 25. Five claims/seven limits; original module read and preview compared, not a second verbatim preview read or independent approval. |
| dutch-fresh-reading | /private/tmp/aimech-dutch-traces-supporting-math-audit-20261015/reading.json | context_only | Later attributed Dutch same-author source/math audit: UAI text/visual 3–4, PMLR text/visual 5, JMLR text 12, 22–23, 25–26 and visuals 12, 23, 25. Five claims/seven limits; original module read and preview compared, not a second verbatim preview read or independent approval. |
| actual-write | /private/tmp/aimech-dutch-gtd-cohort346-write.json | context_only | Actual exclusive creation receipt: two records, report pair and one CREATE history. |
| captured-inputs | /private/tmp/aimech-dutch-gtd-cohort346-capture.json | context_only | Actual canonical inspection; every current input hash and maintained target was checked. |
| postcapture-reading | /private/tmp/aimech-dutch-gtd-cohort346-root-postcapture-reading.json | context_only | Root read both complete canonical YAML records after actual write, including eleven claims, fourteen limitations, four source rows, definitions, mappings, identity notes and curation metadata. After actual canonical capture, rechecked all30 captured bytes and allfivewriteoutputs unchanged. Read full actual scientific-audit narratives for11claims/14limits, definitions/mappings and attributed source-reading scope; scientific payload equals accepted previews except authorized identity/timestamps. Earlier root primary/visual and supporting mathematical readings remain separately attributed; no complete proof, code, benchmark or independent approval is implied. Current gate completion, page audit and saved-review state are separate evidence. |
| governance-assessment | /private/tmp/aimech-cohort346-governance-audit-20261015/assessment.json | context_only | Actual byte preservation, owner/frontier, history and parsed-page audit; no independent approval. |
| rendered-pages | /private/tmp/aimech-cohort346-governance-audit-20261015/rendered-pages.json | context_only | Actual generated page paths and bytes, with parsed-content correspondence; no browser/layout inspection. |
| actual-scientific-assessment | /private/tmp/aimech-cohort346-actual-scientific-audit-20261015/assessment.json | context_only | Same-author actual-record adversarial assessment with separately attributed primary reading. |
| current-identity-collection | /private/tmp/aimech-cohort346-identity-20261015/collection.json | context_only | Current four-root ignored- and hidden-inclusive identity collection; mechanical coverage is distinct from attributed semantic reading. |
| current-context-assessment | /private/tmp/aimech-cohort346-supporting-context-assessment-20261015/assessment.json | context_only | Actual supporting interpretation of retained matched contexts; root and supporting scopes remain separate. |
| root-decisions | /private/tmp/aimech-cohort346-identity-20261015/root-decisions.json | context_only | Actual root identity/owner/source-lead decisions, retaining owner 264 partial residuals. |
| scientific-support | /private/tmp/aimech-dutch-gtd-cohort346-review-preparation-20261015/scientific-support.prepared.json | context_only | Exact accepted claim and limitation support; historical and later source/math scopes remain separate. |
| discovery-report | /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261015T171620Z-dutch-eligibility-traces-and-true-online-gtd.json | context_only | Current record/context/owner mirrors; no added frontier leaf. |
| creation-history | /private/tmp/aimech-discovery-recovery-worktree-20261012/history/reports/dutch-eligibility-traces-and-true-online-gtd/2026-10-15T171633Z-codex-ccdfbb.yaml | context_only | Actual CREATE report history; predecessor schema extension is committed baseline, not a new application. |
| record-dutch | /private/tmp/aimech-discovery-recovery-worktree-20261012/data/curated/DutchEligibilityTraces.yaml | context_only | Complete current DRAFT record equals accepted science and actual root identity decisions. |
| record-gtd | /private/tmp/aimech-discovery-recovery-worktree-20261012/data/curated/TrueOnlineGTDLambda.yaml | context_only | Complete current DRAFT record equals accepted science and actual root identity decisions. |
| check-gate | /private/tmp/aimech-dutch-gtd-cohort346-check-gate.json | context_only | Actual required command completed successfully before this review generation. |
| check-vendor | /private/tmp/aimech-dutch-gtd-cohort346-check-vendor-network-retry.json | context_only | Actual required command completed successfully before this review generation. |
| check-check-source | /private/tmp/aimech-dutch-gtd-cohort346-check-check-source.json | context_only | Actual required command completed successfully before this review generation. |
| check-render | /private/tmp/aimech-dutch-gtd-cohort346-check-render.json | context_only | Actual required command completed successfully before this review generation. |
| check-render-check | /private/tmp/aimech-dutch-gtd-cohort346-check-render-check.json | context_only | Actual required command completed successfully before this review generation. |
| check-diff | /private/tmp/aimech-dutch-gtd-cohort346-check-diff.json | context_only | Actual required command completed successfully before this review generation. |
| historical-check-attempt-1 | /private/tmp/aimech-dutch-gtd-cohort346-check-vendor.json | context_only | Actual failed attempt, retained with its later successful same-command replacement. |

## Limits And Additional Notes

- Same-author team support and root review are not independent scientific approval. Native validation, source acquisition, selective reading and mathematical reasoning are distinct events.
- Dutch traces selects the specified component and scaling convention. One-hot update-map interpolation, general feature projections, non-contraction, zero/current step sizes and host-forward-view requirements remain qualified.
- The 2014 conference UAI source used for Dutch traces and the indexed first-author-hosted version used for GTD are distinct exact artifacts. No verified revision date, exhaustive priority claim or comprehensive erratum audit is inferred.
- GTD retains current versus previous importance ratios, two scaled Dutch traces, separate accumulating correction history, old coupled weights and stored prior predictions. Fixed-sequence finite-horizon correspondence is not convergence, unbiased exact objective gradients, nonlinear exactness or control performance.
- The conditional orthogonal-projection residual distinguishes MSPBE and MSE values even where minimizers agree. Lambda endpoints and rho=1 do not erase every algorithmic distinction.
- Historical ignored-inclusive searches and reading scopes remain historical. The later actual collection and root search interpretation must supply current bounded scope; no global absence or family exhaustion follows.
- Original GTD inputs and validation are preserved. The later metadata-only binding successor is separately cited and does not claim revalidation.
- Actual five creation outputs, one CREATE history, 9 generated pages and 30 capture inputs are assessed through separate receipts. Six required checks passed; any failed attempts remain explicit. Parsed HTML is not browser/layout inspection. Canonical review save/check and publication remain separate actions.
- Root read both complete canonical YAML records after actual write, including eleven claims, fourteen limitations, four source rows, definitions, mappings, identity notes and curation metadata. After actual canonical capture, rechecked all30 captured bytes and allfivewriteoutputs unchanged. Read full actual scientific-audit narratives for11claims/14limits, definitions/mappings and attributed source-reading scope; scientific payload equals accepted previews except authorized identity/timestamps. Earlier root primary/visual and supporting mathematical readings remain separately attributed; no complete proof, code, benchmark or independent approval is implied. Current gate completion, page audit and saved-review state are separate evidence.
- Fresh merged-base identity assessment on 15 October 2026, 17:07:16–17:08:53 UTC, at 9799fa6e2cb303d940fcb56249830c333cac7c90. All 772 native and 442 pinned AIO records supplied 4,834 identity fields and 3,693 normalized values, including local IDs and explicit candidate source spellings. No candidate collision was found. Four checkout scans included ignored and hidden files and retained 2,597 occurrences in 437 exact contents, including 250 new contents. Root read all 250 new contents, all 15 context-only normalized fields with nine definitions, all matching frontier fields and all four complete matching owners. Historical semantic source and mapping readings retain their prior scope; this does not claim a new manual reading of all historical context groups or every record mechanism. All 909 main and 393 nested frontier objects were mechanically queried. Absence is bounded to these snapshots and probes; no saturation is inferred.
- The retained root GTD/correction searches surfaced Mahmood et al. 2015 weighted importance sampling as a further source lead. Prior metadata identifies WIS-TD, WIS-GTD, WIS-TO-GTD and usage-based variants; their methods are not adopted as evidence for the two current records. Fresh bounded normalized, whole-frontier and ignored-inclusive source/name scans reveal no dedicated competing candidate record or separate matching frontier owner for those names. Preserve that unresolved source-family work explicitly under existing eligibility owner 264 alongside generic organization, soft-cut and other off-policy/control variants. Later full-paper research is a separate task and will require its own identity and evidence decisions.
- Source access, historical identity, source-agent reading, later GTD hand analysis, native validation and actual root postcapture assessment retain separate scopes and timestamps. The root science reading may precede some gates; actual logs independently establish completed checks.
- The original GTD inputs remain the validated input; the metadata-only later binding is preserved separately. No original receipt is rewritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T173405Z-dutch-eligibility-traces-and-true-online-gtd
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of Dutch eligibility traces and true online GTD(lambda)
started_at: '2026-10-15T17:20:41.334787Z'
finished_at: '2026-10-15T17:34:05.947062Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Root author assessment with attributed same-author source and
    mathematical supporting agents; no independent scientific approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Dutch eligibility traces as the source-qualified mathematical component
  and true online GTD(lambda) as the specified linear off-policy state-value algorithm.
  All eleven claims, fourteen individual limitations and four exact primary artifacts
  are assessed through attributed source/math reading and actual canonical correspondence.
  The qualified MathematicalFunction and ReinforcementLearning mappings express different
  abstraction levels. Actual capture, owner preservation, generated pages and six
  completed required checks are bound; no independent approval or residual exhaustion
  is implied.
source:
  git_revision: 9799fa6e2cb303d940fcb56249830c333cac7c90
  state: working_tree
  inputs:
  - path: .claude/skills/review-category/SKILL.md
    sha256: 553c3870c1dfc127f90f196b7b212b644706d4c26e2a578ab615ccce588070d7
    role: context
  - path: data/aio/Layer.yaml
    sha256: 46b533d2f0afcbdeadb7c35f8c382d66e51e0f5edf90b0c3552767687d34fa87
    role: context
  - path: data/aio/LinearFunction.yaml
    sha256: 773be0c041b8b1f0f386ec64c794388eff2b482c81f8f828bca0ae27a173811c
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/DutchEligibilityTraces.yaml
    sha256: fd2401fee93665799a7e71c268caac3609dc5fcdb5a542ef9606fd61d272e5ba
    role: target
  - path: data/curated/ModifiedConnectionistQLearning.yaml
    sha256: 8986696e751e7ab7206755f5cfc32b125b6216feac3043f105b354b2b49f4428
    role: context
  - path: data/curated/PengWilliamsQLambda.yaml
    sha256: 58dd0266b45fd8602081d1b468d55a2456de3dd7488c3a9891c080bb587b0bd5
    role: context
  - path: data/curated/ReplacingEligibilityTraces.yaml
    sha256: 81300bc3c4616459fa62d21c03c575bbba8fc5a207edbb78d0a7e46c7724b00c
    role: context
  - path: data/curated/Sarsa.yaml
    sha256: 8ac6efbbcfeda82ce462fbc7f6d641a9eab36b8749c6bdb0b7713ba43496e041
    role: context
  - path: data/curated/TemporalDifferenceLearning.yaml
    sha256: edd02cd7a9f2b8b916ba684f7aa8cb4c8d49b81a1896912dc5297370d24f348a
    role: context
  - path: data/curated/TrueOnlineGTDLambda.yaml
    sha256: fa6e70693e933196af56de2688d5c57d8e9da2fa48af27a64c44e8e45c7a29d2
    role: target
  - path: data/curated/TrueOnlineSarsaLambda.yaml
    sha256: a7101fe8024215197f6ebb008b334d0c7098ca1eccf8bb0fe181cb746c840206
    role: context
  - path: data/curated/TrueOnlineTDLambda.yaml
    sha256: 1841e5ccc400f0fb82633bc768a2ad5531ddf5c53fcd603dddb562899d8a1346
    role: context
  - path: data/curated/WatkinsHardCutMultistepQLearning.yaml
    sha256: 29b2c3331660910f574b5ed8ba7c1153070f187588cd8360e96ec03e3bd9cee1
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
  - path: history/reports/dutch-eligibility-traces-and-true-online-gtd/2026-10-15T171633Z-codex-ccdfbb.yaml
    sha256: 2869a2d1f90d05ea432b62ece31e653152a93703f0530830d873ad5763ae1a0d
    role: context
  - path: justfile
    sha256: 2d9c1b68c1c80d53aa44a6b8b5e916efe8b493650ff59a3fc7479a42be37f400
    role: context
  - path: research/discovery/20261015T171620Z-dutch-eligibility-traces-and-true-online-gtd.json
    sha256: e9e4aa038389bcef5fc41f016869ee0b895f5b038e14d1824b702f9aea089009
    role: context
  - path: research/discovery/20261015T171620Z-dutch-eligibility-traces-and-true-online-gtd.md
    sha256: 7fd536755879cd42d176baa8adf0573e75b7977ed13b6e9cd4facf026e1d7a9a
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
  - path: src/aimech/schema/curated_concept.yaml
    sha256: 3826f6a7643d6a0140cf60bb52a1d3ac2fbab4811b4fd8d1d178a13c3341fa3f
    role: context
targets:
- target_id: AIMech:DutchEligibilityTraces
  label: Dutch eligibility traces
  path: data/curated/DutchEligibilityTraces.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DutchEligibilityTraces.yaml
    role: maintained native concept record
- target_id: AIMech:TrueOnlineGTDLambda
  label: True online GTD(lambda)
  path: data/curated/TrueOnlineGTDLambda.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TrueOnlineGTDLambda.yaml
    role: maintained native concept record
scope:
  description: Complete explicitly selected two-record cohort in the captured current
    canonical state.
  selection: 'Exact IDs: AIMech:DutchEligibilityTraces, AIMech:TrueOnlineGTDLambda.'
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - AIMech:DutchEligibilityTraces
  - AIMech:TrueOnlineGTDLambda
  exclusions:
  - target: Generic eligibility, complete TD/Sarsa/GTD families, control, WIS and
      soft-cut variants
    reason: Distinct residual scopes; shared formulas are not complete identity.
  - target: Complete proof certification, author software and benchmark reproduction
    reason: No such execution or comprehensive certification was performed.
checks:
- check_id: check-gate
  name: just check
  status: passed
  required: true
  summary: Actual successful command; exact output is retained.
  target_ids:
  - AIMech:DutchEligibilityTraces
  - AIMech:TrueOnlineGTDLambda
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
  - AIMech:DutchEligibilityTraces
  - AIMech:TrueOnlineGTDLambda
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
  - AIMech:DutchEligibilityTraces
  - AIMech:TrueOnlineGTDLambda
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
  - AIMech:DutchEligibilityTraces
  - AIMech:TrueOnlineGTDLambda
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
  - AIMech:DutchEligibilityTraces
  - AIMech:TrueOnlineGTDLambda
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
  - AIMech:DutchEligibilityTraces
  - AIMech:TrueOnlineGTDLambda
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
  - AIMech:DutchEligibilityTraces
  - AIMech:TrueOnlineGTDLambda
  command: just vendored-check
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - historical-check-attempt-1
evidence:
- evidence_id: preview-dutch
  kind: record_content
  reference: /private/tmp/aimech-dutch-traces-draft-preparation-20261015/native-preview.json
  snapshot_sha256: 3745f1a6b1e54f01481d0b93aa68977c5ccd81ada41b7fb480d5be246b6181b5
  accessed_at: '2026-10-15T16:39:40Z'
  support: context_only
  summary: Actual accepted TEMP native payload, not a canonical creation.
- evidence_id: support-dutch
  kind: record_content
  reference: /private/tmp/aimech-dutch-traces-draft-preparation-20261015/scientific-support.json
  snapshot_sha256: 8743bb7f21d9606f62dc92ce0e3e10ebeb30f7456356688666315413d181ccda
  accessed_at: '2026-10-15T16:34:44.075148Z'
  support: context_only
  summary: Original claim and limitation narratives with separately attributed bounded
    primary reading; historical preparation tense remains historical.
- evidence_id: draft-acceptance-dutch
  kind: record_content
  reference: /private/tmp/aimech-dutch-traces-draft-preparation-20261015/root-draft-acceptance.json
  snapshot_sha256: 8506873c698ce06c8258790dadc4e4265e32119a6b355de9f4b609cf08d16860
  accessed_at: '2026-10-15T16:39:40.921739Z'
  support: context_only
  summary: Root read complete data-only module, inputs and all3 source rows; full5
    claim and7 limitation support narratives, recovering initially truncated limit2/3.
    Research acceptance retains primary text/visual and7AIO43edge scope. Component,
    scaling, projection, one-hot, cost and source-display qualifications are accepted;
    no implementation, full proof or benchmark execution inferred.
- evidence_id: preview-validation-dutch
  kind: record_content
  reference: /private/tmp/aimech-dutch-traces-draft-preparation-20261015/native-preview-validation.json
  snapshot_sha256: 050e3115d5517ab72ff9fc133837203d4c2835ab3084eb85ac9f0e01ae41f495
  accessed_at: '2026-10-15T16:39:40Z'
  support: context_only
  summary: Actual TEMP native validation only; no canonical addition, current identity
    clearance, gate or independent scientific approval.
- evidence_id: source-reading-dutch
  kind: record_content
  reference: /private/tmp/aimech-dutch-traces-research-20261015/reading.json
  snapshot_sha256: 21ebef36608e32aeab04591d68c458b1f2b4b3e77bf4772b969d6969afe023f7
  accessed_at: '2026-10-15T17:08:47.197162Z'
  support: context_only
  summary: Fresh Dutch research read PMLR 2014 native/visual p. 5; JMLR 2016 native
    pp. 12, 22–23, 25–27 and 40, and visuals pp. 12, 23 and 25; UAI 2014 native pp.
    1–4 and visuals pp. 3–4. Preparation reuses those exact bounded readings, with
    root source/identity scope separately attributed. No full UAI off-policy algorithm
    or complete 40-page proof reading is claimed.
- evidence_id: source-times-dutch
  kind: record_content
  reference: /private/tmp/aimech-dutch-traces-draft-preparation-20261015/source-time-projection.json
  snapshot_sha256: 46f7a1f187dd484a733748976a57df14932f7c22979d55dd90aabecff3ee3a03
  accessed_at: '2026-10-15T17:08:47.197162Z'
  support: context_only
  summary: Original access precision and source-version lineage, distinct from this
    review preparation.
- evidence_id: historical-identity-dutch
  kind: search
  reference: /private/tmp/aimech-dutch-traces-research-20261015/identity/assessment.json
  snapshot_sha256: 885a0994f311dc423fe53aecda310e77c5be7597cfee46ff4306e6d1e80f4217
  accessed_at: '2026-10-15T17:08:47.197162Z'
  support: context_only
  summary: Historical bounded identity interpretation; current merged-base assessment
    remains a separate future input.
  search_scope: This source-named mathematical component selects the Dutch vector
    trace recurrence, not a complete true online TD or Sarsa learning algorithm. The
    separate host methods also specify targets, weight corrections and prediction
    or action timing. ReplacingEligibilityTraces remains distinct outside the stated
    one-hot special case. Historical research on 15 October 2026 at 16:15:04–16:15:17
    UTC inspected 769 native and 442 pinned AIO records in the working cohort 345
    snapshot. Four fixed-string, word-boundary searches included ignored and hidden
    paths, retaining 328 occurrences in 154 exact contents; all complete decoded matching
    contents were read and reconstructed. Normalized candidate ID, label and Dutch-trace
    source spellings had no candidate match; two matched identities were maintained
    neighbors. Mechanical recursive queries covered 909 main and 393 nested frontier
    objects; semantic reading covered all nine matching full objects, 20 selected
    identity/definition rows, both full nearest maintained trace/TD records and seven
    exact AIO nodes with 43 incident edges. This is a dated bounded assessment, not
    a manual reading of every unrelated record or absence beyond that snapshot. At
    that snapshot owner 264 already carried ReplacingEligibilityTraces, WatkinsHardCutMultistepQLearning
    and TrueOnlineTDLambda plus cohort 343 and 344 resolutions; TrueOnlineSarsaLambda
    was a separately accepted TEMP compound-method draft. Those historical owner outcomes
    and the Sutton 1988 discovery pointer are context, while the acquired 2014/2016
    primaries support this component. Generic eligibility organization, soft-cut and
    other extensions remain residuals; no new frontier leaf or family exhaustion follows.
    Later maintained outcomes and current identity decisions are separate from this
    historical research scope.
- evidence_id: src-vanseijen2014
  kind: primary_source
  reference: https://proceedings.mlr.press/v32/seijen14.pdf
  snapshot_sha256: c8f93a80ad4231c9e4ee6c3a0bcbfa60470784e4b1de7eba8c9835402fce0d51
  accessed_at: '2026-10-15T14:43:24Z'
  support: supports
  locator: Section 4.1, Equations 10–12 and Algorithm 2; scaled trace/host separation
    and initial zero trace. This task does not repeat the full nine-page or proof
    audit.
  summary: Official PMLR nine-page ICML 2014 paper, Proceedings of Machine Learning
    Research 32(1):692–700. PDF heading prints lambda as a Greek symbol; the publisher
    metadata uses the text lambda. Access to complete bytes is not a claim that every
    page was read.
- evidence_id: src-vanseijen2016
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume17/15-599/15-599.pdf
  snapshot_sha256: 905d228fcd5e7de3eace656665b6adcba322496f037c94130e14a44084c713fd
  accessed_at: '2026-10-15T14:43:25Z'
  support: supports
  locator: Equation 11 versus correction Equation 12, time-varying scaled Equation
    16/Algorithm 4, tabular specialization, historical naming and linear-scope discussion/bibliography.
    Page 22 experimental context is not promoted to a benchmark claim. The complete
    40-page source and proof are not freshly audited.
  summary: Official JMLR 17(145):1–40 (2016), 40-page article. Cover states Submitted
    11/15; Revised 7/16; Published 8/16. Access to complete bytes is not a claim that
    every page was read.
- evidence_id: src-vanhasselt2014
  kind: primary_source
  reference: https://auai.org/uai2014/proceedings/individuals/324.pdf
  snapshot_sha256: d7bdba51b77d3ee002ec2e3a98997d9ee766f5111195402235504f18f9f06b56
  accessed_at: '2026-10-15T16:15:47Z'
  support: supports
  locator: Abstract, setup, complete general theorem/trace recurrence and naming,
    and beginning of off-policy context. All ten pages were extracted, but only native
    pages 1–4 and visuals 3–4 were read. No full off-policy method/experiments certification.
  summary: Official UAI 2014 proceedings individual paper 324, ten PDF pages. 324
    is the conference paper identifier, not a page number. Exact publication day and
    DOI are not established by the inspected official pages. Access to complete bytes
    is not a claim that every page was read.
- evidence_id: preview-gtd
  kind: record_content
  reference: /private/tmp/aimech-true-online-gtd-draft-preparation-20261015/native-preview.json
  snapshot_sha256: 5720a43ee1c609399c6a437f3ee3de4379b98346d117aec7fa79753e84ca596f
  accessed_at: '2026-10-15T16:58:34Z'
  support: context_only
  summary: Actual accepted TEMP native payload, not a canonical creation.
- evidence_id: support-gtd
  kind: record_content
  reference: /private/tmp/aimech-true-online-gtd-draft-preparation-20261015/scientific-support.json
  snapshot_sha256: 6cc0ae4a5bc25971fa22ac77faa6effacabf78050def258096dd3437c45788e5
  accessed_at: '2026-10-15T16:56:32.425860Z'
  support: context_only
  summary: Original claim and limitation narratives with separately attributed bounded
    primary reading; historical preparation tense remains historical.
- evidence_id: draft-acceptance-gtd
  kind: record_content
  reference: /private/tmp/aimech-true-online-gtd-draft-preparation-20261015/root-draft-acceptance.json
  snapshot_sha256: 16b77ca10d4a6fda5aeb3d99bf58c8c56da997e81fd3b5d0eba24e56b97989a8
  accessed_at: '2026-10-15T16:58:34Z'
  support: context_only
  summary: Root read full data-only module, inputs, exact source/access projection,
    six claim and seven limitation assessments, definition/mapping/identity notes
    and cited locators. Source reading and paper-version qualifications are separately
    retained. Accepted for actual TEMP invocation/validation; no merged-base identity
    clearance or canonical creation asserted.
- evidence_id: preview-validation-gtd
  kind: record_content
  reference: /private/tmp/aimech-true-online-gtd-draft-preparation-20261015/native-preview-validation.json
  snapshot_sha256: e3ee9743271a8f8e0ffd80a79587b211582ed68a5cecd807220d8a3e9eb5f940
  accessed_at: '2026-10-15T16:58:34Z'
  support: context_only
  summary: Actual TEMP native validation only; no canonical addition, current identity
    clearance, gate or independent scientific approval.
- evidence_id: source-reading-gtd
  kind: record_content
  reference: /private/tmp/aimech-true-online-gtd-research-20261015/reading.json
  snapshot_sha256: 89e9cafb1c24ba98d36f9c1aa8e620c2f1751d875aa392fe1a2f188810c650b1
  accessed_at: '2026-10-15T17:08:47.197162Z'
  support: context_only
  summary: 'Source-agent scope: original UAI native pages 1–10 and visuals 2, 5–7;
    coauthor changed page 2 visual and whole-text comparison; first-author complete
    normalized differences plus native pages 6–7 and visuals 5–8. Later same-author
    adversarial scope: first-author native pages 1–9, visuals 3, 5–8, and version
    differences 2, 6–7. These are distinct readings; neither certifies the whole proof,
    all plots or author software.'
- evidence_id: source-times-gtd
  kind: record_content
  reference: /private/tmp/aimech-true-online-gtd-draft-preparation-20261015/source-time-projection.json
  snapshot_sha256: 7849b517702eb00553e0d786335d7eeacda28d09286651c60babf097d0a4a4c6
  accessed_at: '2026-10-15T17:08:47.197162Z'
  support: context_only
  summary: Original access precision and source-version lineage, distinct from this
    review preparation.
- evidence_id: historical-identity-gtd
  kind: search
  reference: /private/tmp/aimech-true-online-gtd-research-20261015/identity/assessment.json
  snapshot_sha256: 06ce02c0965c56173e3e1b2526a5dba662b98d227d5486c0dd115cfcb910f591
  accessed_at: '2026-10-15T17:08:47.197162Z'
  support: context_only
  summary: Historical bounded identity interpretation; current merged-base assessment
    remains a separate future input.
  search_scope: Selects the named linear off-policy state-value algorithm with its
    coupled theta/w updates and three distinct traces. It is not an exact alias of
    on-policy true online TD or Sarsa, original GTD/GQ, a Dutch component or an importance-weighted
    Monte Carlo family. The historical working-cohort-345 research snapshot on 15
    October 2026 contains 772 native and 442 pinned AIO records. Four ignored- and
    hidden-inclusive exact candidate/source searches retained no matches; supplemental
    GTD/GQ/neighbor searches retained 169 occurrences in 83 groups, all meaningful
    matched contexts read. Complete identity fields including local IDs and explicit
    Greek/spelled lambda equivalents were mechanically compared without a candidate
    collision. All 909 main and 393 nested frontier objects were queried, five relevant
    owners read in full, 17 definitions read and three nearest records’ scientific
    fields assessed. Existing owner 264 holds four current record IDs and cohort 343/344/345
    resolutions; the historical Sutton 1988 URL remains a discovery pointer rather
    than evidence for this later algorithm. This is a dated bounded research assessment,
    not absence beyond the inspected snapshot or a future merged-base decision.
- evidence_id: src-vanhasselt2014-author
  kind: primary_source
  reference: https://hadovanhasselt.com/wp-content/uploads/2015/12/off_policy_td.pdf
  snapshot_sha256: b2d5ecc4acea5980a3b6871e86d067471730d3f858a70f5a9d8b04b960ba557c
  accessed_at: '2026-10-15T16:46:33Z'
  support: supports
  locator: 'Source-agent scope: original UAI native pages 1–10 and visuals 2, 5–7;
    coauthor changed page 2 visual and whole-text comparison; first-author complete
    normalized differences plus native pages 6–7 and visuals 5–8. Later same-author
    adversarial scope: first-author native pages 1–9, visuals 3, 5–8, and version
    differences 2, 6–7. These are distinct readings; neither certifies the whole proof,
    all plots or author software.'
  summary: First-author-hosted ten-page version of the UAI 2014 paper. This acquired
    copy has a reward-discount product through t−1 and explicitly indexed discount/bootstrap
    expressions in Equation 16 and PDF p. 7. Its revision date is unspecified; the
    URL directory is not treated as a verified revision date. Access to complete bytes
    is not a claim that every page was read.
- evidence_id: gtd-fresh-adversarial
  kind: record_content
  reference: /private/tmp/aimech-true-online-gtd-adversarial-20261015/assessment.json
  snapshot_sha256: 980fb3bef3ff070e376af09b11d3b96c32c6b5ca346002681e16b97ad012641e
  accessed_at: '2026-10-15T17:08:47.197162Z'
  support: context_only
  summary: 'Later same-author mathematical/source assessment: all six claims and seven
    limits, six hand analyses, exact source-version and reading limits; no numerical
    experiment or independent approval.'
- evidence_id: gtd-fresh-reading
  kind: record_content
  reference: /private/tmp/aimech-true-online-gtd-adversarial-20261015/reading.json
  snapshot_sha256: 00ea0501ef75a6336d3f1a68ce3deb7bab72942dbe284489c55ca3bfbd983e32
  accessed_at: '2026-10-15T17:08:47.197162Z'
  support: context_only
  summary: Later actual first-author text/visual scope, separate from the source-agent
    and root scopes.
- evidence_id: gtd-input-successor
  kind: record_content
  reference: /private/tmp/aimech-true-online-gtd-draft-preparation-20261015/acceptance-binding.json
  snapshot_sha256: 4317d714d01cd6ab2d70b0f7fc64702ac38bef0849b3ab5351776908c5128584
  accessed_at: '2026-10-15T17:08:47.197162Z'
  support: context_only
  summary: Metadata-only inputs.final.json successor retains original validated inputs.json;
    it does not retroactively alter the native validation.
- evidence_id: dutch-fresh-adversarial
  kind: record_content
  reference: /private/tmp/aimech-dutch-traces-supporting-math-audit-20261015/assessment.json
  snapshot_sha256: 3b3036d62e42dc0b76f8acce69d2fc2059ff2c04815bde17571c6bbc34434b6f
  accessed_at: '2026-10-15T17:12:30.680936Z'
  support: context_only
  summary: 'Later attributed Dutch same-author source/math audit: UAI text/visual
    3–4, PMLR text/visual 5, JMLR text 12, 22–23, 25–26 and visuals 12, 23, 25. Five
    claims/seven limits; original module read and preview compared, not a second verbatim
    preview read or independent approval.'
- evidence_id: dutch-fresh-reading
  kind: record_content
  reference: /private/tmp/aimech-dutch-traces-supporting-math-audit-20261015/reading.json
  snapshot_sha256: a4c08cd07f85ed43357d2d89bbe8a70a233a61dd4daa8ed8b2d9cec05a276f52
  accessed_at: '2026-10-15T17:12:30.680936Z'
  support: context_only
  summary: 'Later attributed Dutch same-author source/math audit: UAI text/visual
    3–4, PMLR text/visual 5, JMLR text 12, 22–23, 25–26 and visuals 12, 23, 25. Five
    claims/seven limits; original module read and preview compared, not a second verbatim
    preview read or independent approval.'
- evidence_id: actual-write
  kind: record_content
  reference: /private/tmp/aimech-dutch-gtd-cohort346-write.json
  snapshot_sha256: aa0f760af2e03c580f477c758c3cd9e9463b5b550bcddf592f734ec3870093f2
  accessed_at: '2026-10-15T17:34:05.942497Z'
  support: context_only
  summary: 'Actual exclusive creation receipt: two records, report pair and one CREATE
    history.'
- evidence_id: captured-inputs
  kind: record_content
  reference: /private/tmp/aimech-dutch-gtd-cohort346-capture.json
  snapshot_sha256: 40cf3e13dfbed73fffa8f23470101c257a2560a30ca83ea6a39187bd8d49472e
  accessed_at: '2026-10-15T17:34:05.942534Z'
  support: context_only
  summary: Actual canonical inspection; every current input hash and maintained target
    was checked.
- evidence_id: postcapture-reading
  kind: record_content
  reference: /private/tmp/aimech-dutch-gtd-cohort346-root-postcapture-reading.json
  snapshot_sha256: ddd4076373e169cea68ab5fd8a553889a8ed961c7ad237f1395ba3f5e7c6356c
  accessed_at: '2026-10-15T17:34:05.942556Z'
  support: context_only
  summary: Root read both complete canonical YAML records after actual write, including
    eleven claims, fourteen limitations, four source rows, definitions, mappings,
    identity notes and curation metadata. After actual canonical capture, rechecked
    all30 captured bytes and allfivewriteoutputs unchanged. Read full actual scientific-audit
    narratives for11claims/14limits, definitions/mappings and attributed source-reading
    scope; scientific payload equals accepted previews except authorized identity/timestamps.
    Earlier root primary/visual and supporting mathematical readings remain separately
    attributed; no complete proof, code, benchmark or independent approval is implied.
    Current gate completion, page audit and saved-review state are separate evidence.
- evidence_id: governance-assessment
  kind: record_content
  reference: /private/tmp/aimech-cohort346-governance-audit-20261015/assessment.json
  snapshot_sha256: 0aa9b92f59f3ee8286761777b1e9ca09ca4c1839c7536723d6e496310b70b98b
  accessed_at: '2026-10-15T17:34:05.942573Z'
  support: context_only
  summary: Actual byte preservation, owner/frontier, history and parsed-page audit;
    no independent approval.
- evidence_id: rendered-pages
  kind: record_content
  reference: /private/tmp/aimech-cohort346-governance-audit-20261015/rendered-pages.json
  snapshot_sha256: 5c17a6a065a3a6654b762201c01befed055eb3067e47da026f77df56b7dc947b
  accessed_at: '2026-10-15T17:34:05.942589Z'
  support: context_only
  summary: Actual generated page paths and bytes, with parsed-content correspondence;
    no browser/layout inspection.
- evidence_id: actual-scientific-assessment
  kind: record_content
  reference: /private/tmp/aimech-cohort346-actual-scientific-audit-20261015/assessment.json
  snapshot_sha256: 6786d4094c28ddff071b16d43c67dc7100b9cac785fc800e7b17bfb2093f39cb
  accessed_at: '2026-10-15T17:34:05.942603Z'
  support: context_only
  summary: Same-author actual-record adversarial assessment with separately attributed
    primary reading.
- evidence_id: current-identity-collection
  kind: search
  reference: /private/tmp/aimech-cohort346-identity-20261015/collection.json
  snapshot_sha256: 3bcfdfe694bd57f290a318935b52068c062f2f547a6982e14fb537a238f58a7e
  accessed_at: '2026-10-15T17:34:05.942620Z'
  support: context_only
  summary: Current four-root ignored- and hidden-inclusive identity collection; mechanical
    coverage is distinct from attributed semantic reading.
  search_scope: Fresh merged-base identity assessment on 15 October 2026, 17:07:16–17:08:53
    UTC, at 9799fa6e2cb303d940fcb56249830c333cac7c90. All 772 native and 442 pinned
    AIO records supplied 4,834 identity fields and 3,693 normalized values, including
    local IDs and explicit candidate source spellings. No candidate collision was
    found. Four checkout scans included ignored and hidden files and retained 2,597
    occurrences in 437 exact contents, including 250 new contents. Root read all 250
    new contents, all 15 context-only normalized fields with nine definitions, all
    matching frontier fields and all four complete matching owners. Historical semantic
    source and mapping readings retain their prior scope; this does not claim a new
    manual reading of all historical context groups or every record mechanism. All
    909 main and 393 nested frontier objects were mechanically queried. Absence is
    bounded to these snapshots and probes; no saturation is inferred.
- evidence_id: current-context-assessment
  kind: search
  reference: /private/tmp/aimech-cohort346-supporting-context-assessment-20261015/assessment.json
  snapshot_sha256: 2e468732f432732c39a55fb5b010f4e62e99fc0d7facc40c2657cba8fb75dd3c
  accessed_at: '2026-10-15T17:34:05.942647Z'
  support: context_only
  summary: Actual supporting interpretation of retained matched contexts; root and
    supporting scopes remain separate.
  search_scope: Fresh merged-base identity assessment on 15 October 2026, 17:07:16–17:08:53
    UTC, at 9799fa6e2cb303d940fcb56249830c333cac7c90. All 772 native and 442 pinned
    AIO records supplied 4,834 identity fields and 3,693 normalized values, including
    local IDs and explicit candidate source spellings. No candidate collision was
    found. Four checkout scans included ignored and hidden files and retained 2,597
    occurrences in 437 exact contents, including 250 new contents. Root read all 250
    new contents, all 15 context-only normalized fields with nine definitions, all
    matching frontier fields and all four complete matching owners. Historical semantic
    source and mapping readings retain their prior scope; this does not claim a new
    manual reading of all historical context groups or every record mechanism. All
    909 main and 393 nested frontier objects were mechanically queried. Absence is
    bounded to these snapshots and probes; no saturation is inferred.
- evidence_id: root-decisions
  kind: record_content
  reference: /private/tmp/aimech-cohort346-identity-20261015/root-decisions.json
  snapshot_sha256: 213cc8bb1d17a68df98459a519db4a159a43ed8057218e1e7792b8e2676ce7fd
  accessed_at: '2026-10-15T17:34:05.942666Z'
  support: context_only
  summary: Actual root identity/owner/source-lead decisions, retaining owner 264 partial
    residuals.
- evidence_id: scientific-support
  kind: record_content
  reference: /private/tmp/aimech-dutch-gtd-cohort346-review-preparation-20261015/scientific-support.prepared.json
  snapshot_sha256: cb4795536ff134a1223aac2097427730ac07faf28bb3b2661b07558ddf348a3f
  accessed_at: '2026-10-15T17:34:05.942680Z'
  support: context_only
  summary: Exact accepted claim and limitation support; historical and later source/math
    scopes remain separate.
- evidence_id: discovery-report
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261015T171620Z-dutch-eligibility-traces-and-true-online-gtd.json
  snapshot_sha256: e9e4aa038389bcef5fc41f016869ee0b895f5b038e14d1824b702f9aea089009
  accessed_at: '2026-10-15T17:34:05.946111Z'
  support: context_only
  summary: Current record/context/owner mirrors; no added frontier leaf.
- evidence_id: creation-history
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/history/reports/dutch-eligibility-traces-and-true-online-gtd/2026-10-15T171633Z-codex-ccdfbb.yaml
  snapshot_sha256: 2869a2d1f90d05ea432b62ece31e653152a93703f0530830d873ad5763ae1a0d
  accessed_at: '2026-10-15T17:34:05.946360Z'
  support: context_only
  summary: Actual CREATE report history; predecessor schema extension is committed
    baseline, not a new application.
- evidence_id: record-dutch
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/data/curated/DutchEligibilityTraces.yaml
  snapshot_sha256: fd2401fee93665799a7e71c268caac3609dc5fcdb5a542ef9606fd61d272e5ba
  accessed_at: '2026-10-15T17:34:05.946639Z'
  support: context_only
  summary: Complete current DRAFT record equals accepted science and actual root identity
    decisions.
- evidence_id: record-gtd
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/data/curated/TrueOnlineGTDLambda.yaml
  snapshot_sha256: fa6e70693e933196af56de2688d5c57d8e9da2fa48af27a64c44e8e45c7a29d2
  accessed_at: '2026-10-15T17:34:05.946902Z'
  support: context_only
  summary: Complete current DRAFT record equals accepted science and actual root identity
    decisions.
- evidence_id: check-gate
  kind: validation
  reference: /private/tmp/aimech-dutch-gtd-cohort346-check-gate.json
  snapshot_sha256: d23b644b7ffae62b4f953f2561620a850a6d8c78bbb49f16de070b57607da9dc
  accessed_at: '2026-10-15T17:31:10.840677Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-vendor
  kind: validation
  reference: /private/tmp/aimech-dutch-gtd-cohort346-check-vendor-network-retry.json
  snapshot_sha256: 38cc740ad167e1b33ca9be85175652562e1ca5cb52bbeeddaccafb318ff3b389
  accessed_at: '2026-10-15T17:33:30.406408Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-check-source
  kind: validation
  reference: /private/tmp/aimech-dutch-gtd-cohort346-check-check-source.json
  snapshot_sha256: 067a8a40ec947c812152ff2372ba678455787be28e0e65bb404b176c8d6fe424
  accessed_at: '2026-10-15T17:33:33.018874Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-render
  kind: validation
  reference: /private/tmp/aimech-dutch-gtd-cohort346-check-render.json
  snapshot_sha256: d48b70c745503a336c64b8832fc5c33cd02e301ae20095fbb17ce521ee78d5af
  accessed_at: '2026-10-15T17:20:40.812644Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-render-check
  kind: validation
  reference: /private/tmp/aimech-dutch-gtd-cohort346-check-render-check.json
  snapshot_sha256: 2e34a45c29e48e88e84d9963cab56d5de1566e69d86fefe591cafb71a31c3fb3
  accessed_at: '2026-10-15T17:33:47.340277Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-diff
  kind: validation
  reference: /private/tmp/aimech-dutch-gtd-cohort346-check-diff.json
  snapshot_sha256: da114aefc7079d7066f0c4a8ae9a573efbe0692cf3b0ec6895bdbd4c1f7310c9
  accessed_at: '2026-10-15T17:33:47.599831Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: historical-check-attempt-1
  kind: validation
  reference: /private/tmp/aimech-dutch-gtd-cohort346-check-vendor.json
  snapshot_sha256: b4fbea24335e06a53ffd4a9f956aab5c2efb0344f9bb564acf8e46b82f9cbded
  accessed_at: '2026-10-15T17:31:11.308746Z'
  support: context_only
  summary: Actual failed attempt, retained with its later successful same-command
    replacement.
assessments:
- assessment_id: dutch-named-trace-component
  area: evidence
  topic: Claim named-trace-component
  outcome: supported
  summary: UAI names the general recurrence on p. 4 after displaying it on p. 3. JMLR
    explicitly calls Equation 11 the Dutch trace and Equation 12’s extra weight term
    the delta-correction. The statement therefore identifies a reusable mathematical
    component and does not inherit the host’s complete learning behavior.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanhasselt2014
  - src-vanseijen2016
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-scaled-vector-recurrence
  area: evidence
  topic: Claim scaled-vector-recurrence
  outcome: supported
  summary: Initialization and every scalar/vector term match UAI Equation 3, visually
    checked in the retained research. The trace’s old-state inner product is explicit.
    Expanding c*(I-eta*phi*phi^T)*E_old yields the same recurrence; no separate matrix
    implementation is prescribed. The theorem’s target condition is retained in limitations
    rather than implied by this formula alone.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanhasselt2014
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-td-step-size-conventions
  area: evidence
  topic: Claim td-step-size-conventions
  outcome: supported
  summary: PMLR Equation 11 places alpha_t inside the trace, while JMLR Equation 11
    is unscaled for constant alpha and Equation 16 restores the weighted convention.
    Induction from matched zero initialization gives E=alpha*e for constant alpha,
    with no division needed. The text retains earlier step-size history and does not
    silently substitute a time-varying alpha into the constant-step convention.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanseijen2014
  - src-vanseijen2016
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-one-hot-specialization
  area: evidence
  topic: Claim one-hot-specialization
  outcome: supported
  summary: Substituting a one-hot feature into JMLR Equation 11 gives the exact displayed
    Section 6.3 cases. Combining the accumulating and replacing update maps from the
    same old vector yields the displayed coefficients. Alpha in [0,1] is required
    for convexity; alpha=1 concerns the trace map only. Algorithm 6’s delayed decay
    placement is not copied into a conflicting time index.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanseijen2016
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-rank-one-memory-cost
  area: evidence
  topic: Claim rank-one-memory-cost
  outcome: supported
  summary: The inner product and scaled vector operations make the dense recurrence
    O(n) without explicitly storing its n-by-n algebraic matrix. The source discusses
    O(n) backward methods; the statement narrows the claim to trace bookkeeping and
    excludes feature, action and host costs, without asserting sparsity or wall-clock
    superiority.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanhasselt2014
  - src-vanseijen2016
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: UAI provides the named general vector recurrence, and JMLR distinguishes
    the trace from the complete weight update. The definition selects the mathematical
    credit component with explicit source-dependent scaling, not an entire learning
    algorithm or a coordinatewise clipping operator.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanseijen2014
  - src-vanseijen2016
  - src-vanhasselt2014
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: The component defines a deterministic vector-valued update from prior trace,
    current feature vector and scalar parameters. This supports a qualified mathematical-rule
    association with the pinned generic function class, without exact identity, an
    asserted subclass edge, a scalar-output restriction or a neural-activation claim.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanseijen2014
  - src-vanseijen2016
  - src-vanhasselt2014
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-source-assessment
  area: provenance
  topic: source assessment
  outcome: supported
  summary: Three exact primary versions are declared and all are cited. PMLR 2014
    supplies the earlier scaled formula, UAI 2014 the explicit name/general recurrence,
    and JMLR 2016 the separate component, unscaled/time-dependent and tabular conventions.
    Original access precision and reuse versus new acquisition are retained. UAI paper
    324 is an identifier, not claimed pagination; no exact publication day or DOI
    was inferred. Fresh Dutch research read PMLR 2014 native/visual p. 5; JMLR 2016
    native pp. 12, 22–23, 25–27 and 40, and visuals pp. 12, 23 and 25; UAI 2014 native
    pp. 1–4 and visuals pp. 3–4. Preparation reuses those exact bounded readings,
    with root source/identity scope separately attributed. No full UAI off-policy
    algorithm or complete 40-page proof reading is claimed.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanseijen2014
  - src-vanseijen2016
  - src-vanhasselt2014
  - source-times-dutch
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-identity-assessment
  area: identity
  topic: identity assessment
  outcome: supported
  summary: Retain the named mathematical trace component separately from complete
    TD, Sarsa and GTD algorithms, generic eligibility and coordinatewise replacing
    traces. The same old-state one-hot interpolation is not equality of separately
    evolved histories. The actual captured identity notes implement the root current
    collection decisions; the original preview scope remains historical and is recorded
    in context_changes. Existing owner 264 stays partial, with four prior IDs and
    all three prior resolution objects retained.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - historical-identity-dutch
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
  - current-identity-collection
  - current-context-assessment
  - root-decisions
- assessment_id: dutch-kind-and-status-assessment
  area: scope
  topic: kind-and-status assessment
  outcome: supported
  summary: The accepted mathematical_method representation selects a vector-valued
    credit-update component rather than a full host learner. DRAFT status is retained;
    mapping does not imply an asserted subclass or exact identity.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-limitation-1
  area: scope
  topic: Limitation 1
  outcome: supported
  summary: The UAI theorem requires a specific linear forward update and scalar relation
    among target changes. Host weight correction is not an optional consequence of
    storing the trace. This prevents conflation with the complete maintained TD/Sarsa
    algorithms or generic eligibility mechanisms.
  details: The component is distinct from complete true online TD or Sarsa, the general
    eligibility family and an entire forward-view learning algorithm. In the UAI theorem,
    forward/backward weight equality also requires its linear weight updates, companion
    correction and horizon-independent target-difference relation; inserting only
    this trace into an arbitrary host does not establish that equality.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanseijen2014
  - src-vanseijen2016
  - src-vanhasselt2014
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-limitation-2
  area: scope
  topic: Limitation 2
  outcome: supported
  summary: The scaling identity is restricted to constant alpha. A current alpha_t=0
    yields q*E_old in the scaled formula, which can retain earlier credit; a constant-zero
    step size with zero initialization keeps the scaled trace zero. This is an algebraic
    convention boundary, not a learning convergence claim.
  details: The scaled and unscaled conventions must be matched to the host update.
    Constant-alpha rescaling E=alpha*e does not justify the substitution E_t=alpha_t*e_t
    for varying step sizes. Division by alpha is undefined at alpha=0. A current zero
    alpha_t in the scaled recurrence leaves the decayed previous trace when earlier
    step sizes produced nonzero credit.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanseijen2014
  - src-vanseijen2016
  - src-vanhasselt2014
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-limitation-3
  area: scope
  topic: Limitation 3
  outcome: supported
  summary: The source specialization is explicitly tabular. An affine combination
    evaluated from the common old state is not the same assertion as mixing separately
    evolved accumulator and replacer histories. The inner-product coupling for overlapping
    features prevents a general coordinatewise reset interpretation.
  details: The accumulating/replacing relation is an identity between one-hot update
    maps evaluated from the same old trace, not a mixture of separately evolved trace
    histories. It does not extend as a coordinatewise replacing rule to arbitrary
    overlapping binary or real features. Coincident one-hot trace updates do not make
    the complete learning algorithms identical.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanseijen2014
  - src-vanseijen2016
  - src-vanhasselt2014
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-limitation-4
  area: scope
  topic: Limitation 4
  outcome: supported
  summary: Multiplying Equation 3 by phi^T gives z+h*(1-z) with h=eta*||phi||². The
    bound h in [0,1] ensures monotone non-overshooting movement for any starting projection;
    arbitrary norms/eta do not. Hand examples already retained show a one-hot value
    above one and a negative value with positive scalar features. No trained-model
    failure is inferred.
  details: Dutch traces are not coordinatewise clipping and need not remain nonnegative
    or within [0,1]. In the general scaled recurrence, if z=c*phi^T*E_old and h=eta*||phi||^2,
    then phi^T*E_new=z+h*(1-z). For any starting projection, h in [0,1] keeps the
    new projection between its old value and one; unrestricted feature norms or step
    sizes can overshoot or amplify the deviation. The source phrase toward one does
    not imply exact unit attainment.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanseijen2014
  - src-vanseijen2016
  - src-vanhasselt2014
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-limitation-5
  area: scope
  topic: Limitation 5
  outcome: supported
  summary: Theorem 1 constrains horizon dependence, not |c|. The rank-one transition
    has eigenvalues c*(1-eta*||phi||²) in the feature direction and c orthogonally.
    Its magnitude depends on parameters and features, so no uniform contraction or
    statistical performance follows from the name or recurrence.
  details: The general UAI coefficient c is a scalar independent of the data horizon,
    not necessarily a number in [0,1]. Its description as shrinking requires additional
    magnitude conditions. The transition c*(I-eta*phi*phi^T) has feature-direction
    factor c*(1-eta*||phi||^2), so the recurrence supplies no unconditional numerical
    stability, contraction, convergence, variance reduction or performance guarantee.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanseijen2014
  - src-vanseijen2016
  - src-vanhasselt2014
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-limitation-6
  area: scope
  topic: Limitation 6
  outcome: supported
  summary: The trace can be numerically formed for supplied vectors, but the exact
    forward-view argument uses linear learned weights and the specified sequence.
    Distinguishing recurrence evaluation from theorem applicability prevents an unsupported
    nonlinear-learning transfer. Dense complexity is a scoped arithmetic count.
  details: The source forward-view derivations concern linear prediction in the learned
    weights with the specified feature/target sequence and matching initialization.
    The vector trace formula can be evaluated on supplied features, but generic nonlinear
    or parameter-dependent feature learning does not automatically inherit those derivations.
    Dense O(n) bookkeeping does not imply cost proportional only to the current number
    of nonzero features or a universal wall-clock advantage.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanseijen2014
  - src-vanseijen2016
  - src-vanhasselt2014
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: dutch-limitation-7
  area: scope
  topic: Limitation 7
  outcome: supported
  summary: Each version’s role and the JMLR naming attribution were read. The specific
    local display omissions/cross-reference are recorded from visuals/text without
    claiming an official erratum, invalidity of Equation 3 or a complete proof certification.
    Earlier source access failures and the lack of author-code inspection remain explicit
    provenance.
  details: The 2014 PMLR paper supplies the earlier scaled recurrence; the 2014 UAI
    paper explicitly names the general form Dutch traces; the 2016 journal article
    presents unscaled, time-dependent and tabular conventions and attributes the name
    to van Hasselt and colleagues. This is inspected source lineage, not an exhaustive
    priority claim. The UAI proof locally omits +x_k in its first F_k restatement
    although the theorem and later expansion retain those terms, and the 2016 prose
    after Equation 17 points to Algorithm 2 although the local time-dependent box
    is Algorithm 4. These bounded display observations are not a certified defect
    of the trace recurrence, an official erratum or a full proof audit. No author
    implementation or benchmark reproduction is certified.
  target_ids:
  - AIMech:DutchEligibilityTraces
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanseijen2014
  - src-vanseijen2016
  - src-vanhasselt2014
  - dutch-fresh-adversarial
  - dutch-fresh-reading
  - record-dutch
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-linear-off-policy-state-value
  area: evidence
  topic: Claim linear-off-policy-state-value
  outcome: supported
  summary: Sections 1–2 explicitly define pi/b sampling and linear state-value prediction;
    Section 8 excludes an action-value extension from the selected method. Coverage
    is a condition, not an assumed property of arbitrary behavior data.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-error-weighted-interim-forward-views
  area: evidence
  topic: Claim error-weighted-interim-forward-views
  outcome: supported
  summary: Equations 14–18 separate the two replay targets and use w_k=w_k^k in the
    theta correction. This states a particular sampled construction and deliberately
    avoids calling an evolving online update an exact MSPBE gradient. Equation 13’s
    dimension problem is retained separately.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-three-distinct-eligibility-traces
  area: evidence
  topic: Claim three-distinct-eligibility-traces
  outcome: supported
  summary: Every factor was checked against the first-author visual p. 7. Prediction
    trace e has rho_t outside and inside its Dutch correction; auxiliary e^w uses
    rho_(t−1) in decay/correction and beta_t in injection; g is the separate accumulating
    e-nabla trace. The old-state inner products and step-size scaling remain literal.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-coupled-prediction-and-auxiliary-update
  area: evidence
  topic: Claim coupled-prediction-and-auxiliary-update
  outcome: supported
  summary: The first-author version resolves the original unindexed gamma in delta.
    The theta correction uses the previous-weight current prediction, and both coupled
    right sides use old w/theta with new traces. In-place recomputation is not implicitly
    authorized.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-finite-horizon-linear-correspondence
  area: evidence
  topic: Claim finite-horizon-linear-correspondence
  outcome: supported
  summary: Theorem 1’s horizon-independent relation and the distinct c/eta substitutions
    in Theorems 3–4 are explicit. This is correspondence on fixed realized data and
    matching replay initialization, not a universal objective/convergence assertion.
    Constant numbers of vector operations justify dense linear arithmetic/storage.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-gtd-zero-and-forward-view-boundary
  area: evidence
  topic: Claim gtd-zero-and-forward-view-boundary
  outcome: supported
  summary: Direct substitution of all lambda=0 values yields the displayed GTD(0)
    pair and zero prediction-change correction. The source discussion on p. 9 leaves
    full off-policy Monte Carlo equivalence to a different weighting choice. No endpoint
    claim collapses the full method into ordinary TD or control.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: The source explicitly names the complete off-policy state-value algorithm
    and gives the coupled updates. The definition identifies its three-trace and auxiliary-weight
    mechanism without asserting complete convergence or exact identity with a broad
    RL task.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: The algorithm estimates a specified policy’s state values from reward transitions
    generated by a potentially different behavior policy. This supplies prediction
    machinery used in reinforcement learning. The pinned class is a broader learning
    task involving exploration/performance optimization; the relation does not claim
    exact identity, an algorithm-to-task subclass edge, action selection, policy improvement
    or convergence.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-source-assessment
  area: provenance
  topic: source assessment
  outcome: supported
  summary: 'The exact first-author-hosted 2014 paper supplies the indexed method.
    Conference, reissue and coauthor versions remain separately retained; directory
    naming is not a verified revision date. Local display discrepancies and the projection-residual
    qualification are explicit, without complete proof or implementation certification.
    Source-agent scope: original UAI native pages 1–10 and visuals 2, 5–7; coauthor
    changed page 2 visual and whole-text comparison; first-author complete normalized
    differences plus native pages 6–7 and visuals 5–8. Later same-author adversarial
    scope: first-author native pages 1–9, visuals 3, 5–8, and version differences
    2, 6–7. These are distinct readings; neither certifies the whole proof, all plots
    or author software.'
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - source-times-gtd
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-identity-assessment
  area: identity
  topic: identity assessment
  outcome: supported
  summary: Retain the specified linear off-policy state-value algorithm separately
    from the Dutch component, on-policy TD/Sarsa, GTD/GQ in general, control and WIS
    variants. Shared traces do not establish identical complete updates. The actual
    captured identity notes implement the root current collection decisions; the original
    preview scope remains historical and is recorded in context_changes. Existing
    owner 264 stays partial, with four prior IDs and all three prior resolution objects
    retained.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - historical-identity-gtd
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
  - current-identity-collection
  - current-context-assessment
  - root-decisions
- assessment_id: gtd-kind-and-status-assessment
  area: scope
  topic: kind-and-status assessment
  outcome: supported
  summary: The accepted algorithm representation selects the coupled linear off-policy
    state-value algorithm rather than the general reinforcement-learning task. DRAFT
    status is retained; mapping does not imply an asserted subclass or exact identity.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-limitation-1
  area: scope
  topic: Limitation 1
  outcome: supported
  summary: The final correction retains w whenever rho=1 and lambda_next<1 in general.
    The source’s state-value-only and alternative-forward-view discussion distinguish
    the nearest algorithms and components without assuming disjoint mathematical endpoints.
  details: This is the original linear state-value off-policy algorithm, not GTD/GQ
    in general, an action-value controller, true online TD/Sarsa, WIS variants or
    Dutch/replacing traces alone. Setting every importance ratio to one does not generally
    eliminate the auxiliary gradient correction for lambda<1. A zero (1−lambda_(t+1))
    factor removes that explicit correction, but does not by itself establish identity
    with every Monte Carlo algorithm.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-limitation-2
  area: scope
  topic: Limitation 2
  outcome: supported
  summary: Equation 8 uses a behavior distribution and inverse covariance. Finite
    sequence algebra does not prove statistical coverage, finite moments, convergence
    or policy optimization; these distinct requirements remain stated rather than
    silently certified.
  details: Finite-horizon equality to the specified sampled forward views is an algebraic
    statement, not a proof that each online step is an unbiased MSPBE gradient or
    that the coupled iterates converge, are stable, improve monotonically or reach
    an optimal policy. The expected objective uses a behavior-state distribution and
    an invertible feature second-moment matrix; existence of relevant returns/expectations,
    sufficient target-action support under behavior, and other convergence assumptions
    cannot be inferred merely from the update display.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-limitation-3
  area: scope
  topic: Limitation 3
  outcome: supported
  summary: The displayed initial e and e^w values and zero-history g give the first-step
    cancellation. Stored prior prediction, current/prior ratio indices and old coupled
    weights were checked directly. Replacing the accumulating correction trace is
    only a proposed alternative in the source, not the defined method.
  details: The derivation uses linear, fixed features and matched replay sequences.
    The source initializes e_0=alpha_0 rho_0 phi_0 and e^w_0=beta_0 phi_0; a zero
    pre-initial accumulating trace gives g_0=rho_0 phi_0. The first theta correction
    cancels, so no arbitrary theta_(−1) affects that first update. Later theta_(t−1)^T
    phi_t is a stored preceding-weight prediction, not a recomputation under theta_t.
    Replacing w_t by w_(t+1), swapping current and previous importance ratios, or
    simply replacing g with a Dutch trace changes the specified construction. Nonlinear
    or parameter-dependent features need separate justification.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-limitation-4
  area: scope
  topic: Limitation 4
  outcome: supported
  summary: Step sizes are embedded in distinct Dutch histories. Setting a current
    alpha or beta to zero leaves a decayed old trace in general. General scalar ratios/features
    do not supply a unit-coordinate bound, and dense arithmetic does not assert sparse-current-feature
    or wall-clock complexity.
  details: Alpha_t and beta_t are inside two different scaled traces; a constant-alpha
    unscaled TD/Sarsa convention cannot be substituted without a matched derivation.
    A zero current step size does not in general erase trace contributions from earlier
    nonzero steps. Importance ratios need not be at most one, and these Dutch or accumulating
    traces are not generally nonnegative or coordinatewise bounded by one. Linear
    dense cost excludes feature construction and does not imply cost only in current
    nonzero features.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-limitation-5
  area: scope
  topic: Limitation 5
  outcome: supported
  summary: Fresh original visuals2/5–7 and first-author visuals5–7 support the precise
    local display observations. The explicit Equation 18/theorem/final recurrence
    remains identifiable. No blanket invalidity or complete proof certification is
    inferred.
  details: The inspected source retains mixed t/k indexing and the recursive superscript
    in Equation 6, and a scalar/vector mismatch in Equation 13 and nearby expectation
    prose. Its first proof restatement on PDF p. 3 also omits x_k despite its presence
    in the theorem and later algebra. These are bounded source-display observations;
    the explicit forward and backward updates remain separately identifiable. This
    record neither certifies nor invalidates the entire proof or author implementation.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-limitation-6
  area: scope
  topic: Limitation 6
  outcome: supported
  summary: The retained analytic projection decomposition gives the nonnegative irreducible
    term under well-defined full-return and orthogonality conditions. The p. 8 literal
    equality is therefore qualified, while minimizer agreement in that setting remains
    possible.
  details: The statement on PDF p. 8 that MSPBE equals MSE at lambda=1 needs qualification.
    When the full-return operator yields v_pi and Pi is the stated d-orthogonal projection,
    MSE=J+||Pi*v_pi-v_pi||_d^2. The objectives then have the same minimizers, but
    their values are equal only when the projection residual vanishes. This direct
    projection identity does not establish convergence of the online algorithm.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: gtd-limitation-7
  area: scope
  topic: Limitation 7
  outcome: supported
  summary: The declared source is the first-author acquired byte version and actual
    access time. Original/reissue/coauthor comparisons and genuine DNS failures/retries
    are bound in the preparation records, not misrepresented as a dated published
    erratum. No native empirical superiority claim is added.
  details: The evidence source is the exact acquired first-author-hosted version of
    the 2014 paper, with indexed discount/bootstrap expressions in Equation 16 and
    the final update. The retained conference, reissue and coauthor copies differ
    in the discount-product endpoint or some time indices; no verified revision date
    or comprehensive erratum notice is asserted. Experimental comparisons remain tied
    to the reported random-walk settings, representations and parameter searches,
    not universal superiority. No author software or benchmark reproduction is certified.
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - gtd-fresh-adversarial
  - gtd-fresh-reading
  - record-gtd
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: actual-correspondence
  area: provenance
  topic: Actual canonical, capture, frontier, history, rendered-page and check correspondence
  outcome: supported
  summary: 'Both current records equal the actual write/report entries and accepted
    science: eleven claims, fourteen individual limitations and four exact primary
    artifacts. Five files were created and one CREATE history records the session.
    Only owner 264 changed; four prior IDs and cohort 343/344/345 resolutions remain,
    with 908 other main and 393 nested objects unchanged. Every captured input and
    actual rendered page hash was checked. Six required checks passed; DRAFT and partial
    residual scope remain.'
  target_ids:
  - AIMech:DutchEligibilityTraces
  - AIMech:TrueOnlineGTDLambda
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
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:DutchEligibilityTraces
  rationale: Retain the named mathematical trace component separately from complete
    TD, Sarsa and GTD algorithms, generic eligibility and coordinatewise replacing
    traces. The same old-state one-hot interpolation is not equality of separately
    evolved histories. Both outcomes belong to existing partially addressed owner
    264; four prior IDs and cohort 343/344/345 resolutions must be retained. Residuals
    and unrelated owners are not exhausted.
  evidence_ids:
  - preview-dutch
  - support-dutch
  - draft-acceptance-dutch
  - preview-validation-dutch
  - source-reading-dutch
  - src-vanseijen2014
  - src-vanseijen2016
  - src-vanhasselt2014
  - root-decisions
  - current-identity-collection
- action: retain
  target_ids:
  - AIMech:TrueOnlineGTDLambda
  rationale: Retain the specified linear off-policy state-value algorithm separately
    from the Dutch component, on-policy TD/Sarsa, GTD/GQ in general, control and WIS
    variants. Shared traces do not establish identical complete updates. Both outcomes
    belong to existing partially addressed owner 264; four prior IDs and cohort 343/344/345
    resolutions must be retained. Residuals and unrelated owners are not exhausted.
  evidence_ids:
  - preview-gtd
  - support-gtd
  - draft-acceptance-gtd
  - preview-validation-gtd
  - source-reading-gtd
  - src-vanhasselt2014-author
  - root-decisions
  - current-identity-collection
limitations:
- Same-author team support and root review are not independent scientific approval.
  Native validation, source acquisition, selective reading and mathematical reasoning
  are distinct events.
- Dutch traces selects the specified component and scaling convention. One-hot update-map
  interpolation, general feature projections, non-contraction, zero/current step sizes
  and host-forward-view requirements remain qualified.
- The 2014 conference UAI source used for Dutch traces and the indexed first-author-hosted
  version used for GTD are distinct exact artifacts. No verified revision date, exhaustive
  priority claim or comprehensive erratum audit is inferred.
- GTD retains current versus previous importance ratios, two scaled Dutch traces,
  separate accumulating correction history, old coupled weights and stored prior predictions.
  Fixed-sequence finite-horizon correspondence is not convergence, unbiased exact
  objective gradients, nonlinear exactness or control performance.
- The conditional orthogonal-projection residual distinguishes MSPBE and MSE values
  even where minimizers agree. Lambda endpoints and rho=1 do not erase every algorithmic
  distinction.
- Historical ignored-inclusive searches and reading scopes remain historical. The
  later actual collection and root search interpretation must supply current bounded
  scope; no global absence or family exhaustion follows.
- Original GTD inputs and validation are preserved. The later metadata-only binding
  successor is separately cited and does not claim revalidation.
- Actual five creation outputs, one CREATE history, 9 generated pages and 30 capture
  inputs are assessed through separate receipts. Six required checks passed; any failed
  attempts remain explicit. Parsed HTML is not browser/layout inspection. Canonical
  review save/check and publication remain separate actions.
tags:
- scientific-review
- self-review
- source-scoped
- trace-component-and-algorithm
notes:
- Root read both complete canonical YAML records after actual write, including eleven
  claims, fourteen limitations, four source rows, definitions, mappings, identity
  notes and curation metadata. After actual canonical capture, rechecked all30 captured
  bytes and allfivewriteoutputs unchanged. Read full actual scientific-audit narratives
  for11claims/14limits, definitions/mappings and attributed source-reading scope;
  scientific payload equals accepted previews except authorized identity/timestamps.
  Earlier root primary/visual and supporting mathematical readings remain separately
  attributed; no complete proof, code, benchmark or independent approval is implied.
  Current gate completion, page audit and saved-review state are separate evidence.
- Fresh merged-base identity assessment on 15 October 2026, 17:07:16–17:08:53 UTC,
  at 9799fa6e2cb303d940fcb56249830c333cac7c90. All 772 native and 442 pinned AIO records
  supplied 4,834 identity fields and 3,693 normalized values, including local IDs
  and explicit candidate source spellings. No candidate collision was found. Four
  checkout scans included ignored and hidden files and retained 2,597 occurrences
  in 437 exact contents, including 250 new contents. Root read all 250 new contents,
  all 15 context-only normalized fields with nine definitions, all matching frontier
  fields and all four complete matching owners. Historical semantic source and mapping
  readings retain their prior scope; this does not claim a new manual reading of all
  historical context groups or every record mechanism. All 909 main and 393 nested
  frontier objects were mechanically queried. Absence is bounded to these snapshots
  and probes; no saturation is inferred.
- The retained root GTD/correction searches surfaced Mahmood et al. 2015 weighted
  importance sampling as a further source lead. Prior metadata identifies WIS-TD,
  WIS-GTD, WIS-TO-GTD and usage-based variants; their methods are not adopted as evidence
  for the two current records. Fresh bounded normalized, whole-frontier and ignored-inclusive
  source/name scans reveal no dedicated competing candidate record or separate matching
  frontier owner for those names. Preserve that unresolved source-family work explicitly
  under existing eligibility owner 264 alongside generic organization, soft-cut and
  other off-policy/control variants. Later full-paper research is a separate task
  and will require its own identity and evidence decisions.
- Source access, historical identity, source-agent reading, later GTD hand analysis,
  native validation and actual root postcapture assessment retain separate scopes
  and timestamps. The root science reading may precede some gates; actual logs independently
  establish completed checks.
- The original GTD inputs remain the validated input; the metadata-only later binding
  is preserved separately. No original receipt is rewritten.
```
