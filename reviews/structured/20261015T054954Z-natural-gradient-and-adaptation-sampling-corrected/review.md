# Scientific author self-review after NaturalGradient citation corrections

- Review: 20261015T054954Z-natural-gradient-and-adaptation-sampling-corrected
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-15T05:40:43.064477Z
- Finished UTC: 2026-10-15T05:49:54.802856Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All 12 scientific claims, two definitions, mappings and 16 limitations were reassessed in the original captured cohort. Root read both full canonical records and all substantive supporting assessments. After correcting only two section locators and the actual NaturalGradient updated_at, root captured and inspected the corrected bytes and verified their exact semantic diff. Both original minor findings are resolved with retained predecessor identities and primary-page evidence. Required publication checks passed. Both records remain DRAFT; mathematical limitations and uninspected evidence boundaries remain explicit.

## Scope And Provenance

Complete two-target,12-claim cohort review after two citation corrections. Both records retain their definitions, scientific statements, mapping assessments and16 limitations.

Selection: Exact maintained IDs AIMech:NaturalGradient and AIMech:AdaptationSampling from the actual cohort332 creation.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base eabf695fb458fd2163bacbdd7c49b74610832920.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:NaturalGradient | data/curated/NaturalGradient.yaml | maintained | Natural gradient |
| AIMech:AdaptationSampling | data/curated/AdaptationSampling.yaml | maintained | Adaptation sampling |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full repository gate | passed | True | AIMech:NaturalGradient, AIMech:AdaptationSampling | Lint;247 tests passed,3 skipped;442 generated and735 native records; exact seed reproduction;408 history records; initial420 saved reviews passed. |
| Pinned AIO source integrity | passed | True | AIMech:NaturalGradient, AIMech:AdaptationSampling | Pinned AIO source fingerprint verified. |
| Vendored CLAW integrity | passed | True | AIMech:NaturalGradient, AIMech:AdaptationSampling | Governed artifacts match pinned public CLAW revision. |
| Generated concept pages | passed | True | AIMech:NaturalGradient, AIMech:AdaptationSampling | Rendered current record pages. |
| Page reproduction | passed | True | AIMech:NaturalGradient, AIMech:AdaptationSampling | Generated pages reproduce from current records. |
| Whitespace check | passed | True | AIMech:NaturalGradient, AIMech:AdaptationSampling | No diff whitespace errors. |

## Scientific And Domain Assessments

### Claim metric-dependent-local-direction

evidence: supported. Targets: AIMech:NaturalGradient.

The source proof on 1998 PDF pp.3–4 minimizes the first-order term g^T a under a metric-length constraint. With symmetric positive-definite G, Cauchy–Schwarz gives the stated normalized negative inverse-metric direction; the sign and square-root denominator are correct. The record explicitly requires g nonzero for that normalization and does not turn the local linearization into an exact finite-radius nonlinear minimizer. Equation2.5 is a later additive use, not an omitted normalization requirement.

### Claim model-fisher-statistical-metric

evidence: supported. Targets: AIMech:NaturalGradient.

Retained scientific assessment from the initial review: The statistical expectation is under the model density, and the conditional example includes a fixed input distribution and model output law. Equation3.5 and the explicit log-score calculation on PDF16 support both log derivatives; the visually retained Equation3.11 mismatch is not silently certified. Finite score moments and nondegenerate coordinates explain why an ordinary inverse needs qualifications. An observed-label outer-product sample is not automatically the model expectation. NIPS9 Equation11 corroborates this, but its section locator must be corrected from3 to4; the claim itself is supported. The identified section locators have now been corrected and verified against the captured current bytes; see both resolved findings.

### Claim sampled-loss-gradient-use

evidence: supported. Targets: AIMech:NaturalGradient.

Retained scientific assessment from the initial review: The source distinguishes expected loss L from one-observation l and permits a separately chosen preconditioning matrix before selecting G inverse. The record therefore correctly describes a sampled metric-gradient use rather than a complete universally specified optimizer. Independence and a fixed data law are part of the stated setup; no finite-step monotonicity follows. For example, even G=1 and a quadratic loss can increase after an excessively large step. Equations3.1–3.2 are correctly identified by page/equation but belong to Section3, not subsection3.1; that locator requires correction. The identified section locators have now been corrected and verified against the captured current bytes; see both resolved findings.

### Claim coordinate-direction-and-finite-step-boundary

evidence: supported. Targets: AIMech:NaturalGradient.

The transformation follows directly from g_theta=J^T g_w and G_theta=J^T G_w J with nonsingular J: the inverse action transforms by J inverse. This is a tangent-vector and corresponding flow statement. Taylor expansion of a twice-differentiable nonlinear coordinate map leaves a generally nonzero second-order term after an additive step; affine maps have no such term. The record identifies this as curator chain-rule/Taylor reasoning and does not misattribute an arbitrary finite-update invariance theorem to the paper.

### Claim specified-right-invariant-matrix-geometry

evidence: supported. Targets: AIMech:NaturalGradient.

The paper explicitly fixes the identity Frobenius metric and transports dW by right multiplication W inverse. That choice, not mere membership in a matrix group, yields (ordinary matrix gradient) W^T W in Theorem6. The nonintegrable-frame paragraph supports the warning that dX need not be global coordinates. The earlier BSS Equation18 displays the same metric adjustment and Equation19 confirms the matrix outer product missing from the1998 display. The record appropriately avoids identifying this chosen geometry with the exact Fisher for every unknown source law, or promising nonsingularity after arbitrary finite updates.

### Claim conditional-reported-asymptotic-efficiency

evidence: supported. Targets: AIMech:NaturalGradient.

The inspected Section4 first fixes a realizable teacher and independent observations, then reports leading inverse-Fisher error second moment for a1/t natural update. The record qualifies invertibility, regularity and convergence instead of promoting the theorem title to a universal optimizer guarantee. The displayed O(1/t) metric perturbation is not implied by consistency alone and is expressly left uncertified. The same page switches to an expected Hessian for misspecification and excludes generic semiparametric separation/deconvolution, matching the maintained boundaries.

### definition assessment

evidence: supported. Targets: AIMech:NaturalGradient.

The definition identifies an inverse-metric differential rule with Fisher as its statistical specialization; it does not conflate the local direction with all algorithms that use it. Section2 PDF2–4 and Section3.1 PDF5 Equation3.5 support this scope. The definition citation locators are correct.

### identity kind assessment

identity: supported. Targets: AIMech:NaturalGradient.

Retain a mathematical_method: fixed differentiable objective plus metric defines a vector rule, while initialization, gradient sampling, step size and domain handling belong to particular optimizers. NES/IGO add distribution objectives and sampling, xNES/SNES add finite Gaussian updates, and BSS is a specialization. Existing owner196 and its1996context are retained; fresh creation-time identity assessment remains root-owned.

### mapping assessment

grounding: supported. Targets: AIMech:NaturalGradient.

The pinned MathematicalFunction definition is a rule relating dependent values to independent inputs, not only a scalar activation. For fixed objective and metric the natural-gradient construction is such a tangent-vector-valued rule, supporting only a qualified related_match. The record explicitly denies equivalence, subclass, neural layer and complete optimizer semantics. No Fisher-uniqueness theorem is inferred from the mapping.

### limitations assessment

scope: supported. Targets: AIMech:NaturalGradient.

Positive-definite/invertible domain, model versus observed-score expectation, sampled finite-step behavior, nonholonomic matrix frame, source formula discrepancies and the conditional reported efficiency theorem are material qualifications, not cosmetic caveats. Missing proof-rate and characterization assumptions remain unresolved rather than certified.

### Claim direct-hyperparameter-comparison

evidence: supported. Targets: AIMech:AdaptationSampling.

The thesis and journal both compare fresh samples under a nearby algorithm-hyperparameter setting and retain or revert that setting according to a quality comparison. This supports a meta-level controller identity; it does not specify the host optimizer’s gradient or make a Mann–Whitney protocol mandatory. The record distinguishes motivation by progress over time from maximizing raw sample fitness and does not promise nominal significance or automatic improvement.

### Claim virtual-density-ratio-reuse

evidence: supported. Targets: AIMech:AdaptationSampling.

The primary prose uses the same quality observations twice, first with unit weights and then with hypothetical-to-current density ratios. The direction of the ratio is correct, and the record keeps the values unchanged rather than multiplying their numeric ranks. Reuse explains avoided fresh quality evaluations but also makes the groups dependent. Observation-wise positive finite denominators alone do not prove global proposal coverage, integrability or stable weights; those limitations are preserved.

### Claim reported-weighted-rank-comparison

evidence: supported. Targets: AIMech:AdaptationSampling.

AppendixB visibly gives weighted greater-than pairs plus half weight for equality and substitutes the two weight masses in the ordinary normal mean/variance formulas. The record accurately labels these as reported formulas. For identical reused groups with all ratios one, h(x,y)+h(y,x)=1, including ties, so diagonal halves and unordered pairs force U=n²/2 for every sample; actual variance is zero, while the substituted variance is positive. This hand derivation justifies the calibration caveat without asserting a general unequal-law distribution, repaired test or universal invalidity of direct independent comparisons.

### Claim nes-counterfactual-scale-learning-rate

evidence: supported. Targets: AIMech:AdaptationSampling.

The2012 method and Algorithm2 identify eta_sigma, not every NES learning rate or the current scale itself. The hypothetical law is recomputed from the previous optimizer state using1.5 times that rate, and the current population is compared through density ratios. This distinguishes a counterfactual optimizer update from multiplying sigma by1.5. The record does not inherit or recertify the separate full-matrix xNES pseudocode or its convention issues.

### Claim empirical-increase-or-return-policy

evidence: supported. Targets: AIMech:AdaptationSampling.

The prose specifies a capped multiplicative increase after a favorable comparison and otherwise an affine return toward the initial rate; c prime=0.1 and the dimension-dependent rho match the thesis and2012 Table1. These are empirical settings, not an optimal rate or calibrated significance level. The record does not equate an unspecified weighted-Mann–Whitney return value with a particular directional p-value, and explicitly retains the rank/tail branch ambiguity in the printed algorithms.

### Claim modes-and-composition-boundary

evidence: supported. Targets: AIMech:AdaptationSampling.

Fresh hypothetical-law samples and reweighted old observations are operationally different modes, and the source explicitly permits a mixture with unit-weight new samples. That supports one controller record with stated modes rather than silently identifying them as interchangeable implementations. The2012 xNES-as name is a host optimizer plus this controller. Generic importance sampling, importance mixing and the comparison statistic alone omit the parameter-selection mechanism, so the record properly rejects them as exact aliases.

### definition assessment

evidence: supported. Targets: AIMech:AdaptationSampling.

The direct/virtual comparison controller is supported by thesis Section2.4.4 PDF48–49 and journal Section3.2 PDF11–13. The definition leaves comparison details and host optimizer separate. Both definition evidence locators agree with the inspected sections.

### identity kind assessment

identity: supported. Targets: AIMech:AdaptationSampling.

Retain an algorithm controller with explicit direct/virtual modes. It chooses hyperparameter settings using comparative sample quality, unlike a bare importance-weighting estimator, standalone rank statistic, base NES gradient or population-copying method. xNES-as names the composition and is correctly excluded as an alias. Owner195 is reused; no new family exhaustion is asserted.

### mapping assessment

grounding: supported. Targets: AIMech:AdaptationSampling.

The accepted13 no-match reasons are coherent with the current pinned definitions: metadata-based MetaLearning, model-training TrainingStrategy, labeling ActiveLearning and language-model/layer categories add requirements absent from the general controller. KnowledgeTransfer’s related Adaptation synonym does not establish identity. ExponentialFunction belongs to some hosts, not a mandatory controller operation. MathematicalFunction is broad, but generic computability is not an informative defining-component mapping for this procedure family. The bounded no-match assessment is distinct from a global ontology absence claim.

### limitations assessment

scope: supported. Targets: AIMech:AdaptationSampling.

The equal-law paired witness refutes the substituted positive variance as the actual variance in that case; it does not disprove all independent direct tests. Half-tie pair counts do not supply a tie-adjusted variance, and repeated/data-selected comparisons, support and integrability need separate treatment. Weight-versus-multiplied-rank shorthand and the undefined return/tail convention prevent literal implementation certification. No performance or calibrated significance guarantee follows.

### Source version and access: amari1998

provenance: supported. Targets: AIMech:NaturalGradient.

Core26-page1998 journal copy, hosted by RIKEN; publication date and later PDF build/modification dates remain different fields. Equations2.3/3.5, Sections4/7 and the local proof define the supported geometry. Printed Fisher/BSS displays and proof-rate caveats are retained; neither an author erratum nor a full theorem verification is asserted. The original DNS failure and successful network retry retain separate receipts, and the publisher access limitation is not absence of the paper.

### Source version and access: amari1996-nips9

provenance: supported. Targets: AIMech:NaturalGradient.

Official seven-page NIPS9 general-geometry article, conference1996/printed127–133, cited by the1998 paper as its earlier version. Its Equation11 uses two log-density derivatives and belongs to Section4 on PDF4, while its local metric definition is Section3 on PDF3. This is corroboration from a distinct source version, not interchangeable pagination with the journal.

### Source version and access: amari-cichocki-yang1996-nips8

provenance: supported. Targets: AIMech:NaturalGradient.

Official seven-page NIPS8 blind-separation article, conference1995 and cited as1996 proceedings, printed757–763. PDF5 visually distinguishes the ordinary gradient and its right-metric adjustment; Equations18–19 support the specialized matrix rule and outer-product reconciliation. It does not establish that every ICA procedure is natural gradient or that the specified metric is every unknown-source Fisher. The root visual timing was honestly corrected in a successor receipt rather than backdated.

### Source version and access: schaul2011-thesis

provenance: supported. Targets: AIMech:AdaptationSampling.

The acquired134-page IDSIA author copy supplies the direct/virtual definition and the explicit weightedU construction. Only declared method/context pages were read; full_text denotes access level rather than a full-thesis audit. The body points to AppendixA, but the formula is in AppendixB, PDF121/printed97. Cover submission/acceptance dates are distinct from institutional oral-exam metadata; no byte equivalence to the separately described TUM repository PDF is asserted.

### Source version and access: wierstra2014

provenance: supported. Targets: AIMech:AdaptationSampling.

Official32-page JMLR journal copy restates the controller in Section3.2, PDF11–13/printed959–961, and supplies Algorithm4. Its prose supports unchanged quality values plus weights, while the displayed weight-times-rank shorthand and unspecified test return remain implementation caveats. Selective source reading is distinct from a full32-page review, and host NES conventions are not recertified by this controller claim.

### Source version and access: schaul2012

provenance: supported. Targets: AIMech:AdaptationSampling.

Eight-page GECCO2012 Companion source, printed221–228, supplies the explicit global-scale-rate specialization, counterfactual previous state, xNES-as composition and empirical defaults. The conference date is not invented as an exact publication date or DOI. The known-target restart-policy caveat prevents importing its numerical comparisons as general evidence. The initial sandbox DNS failure and successful retry are both retained; no author implementation or benchmark was run.

### Actual target capture, source correspondence and DRAFT status

consistency: supported. Targets: AIMech:NaturalGradient, AIMech:AdaptationSampling.

The corrected records and report entry payloads agree; exact semantic comparison establishes only the two locator edits and actual updated_at in NaturalGradient, with AdaptationSampling unchanged. Current capture input hashes remain exact. All12 scientific claims,13 no-match rejections and the qualified related mapping are preserved. Source, full gate, vendored and page reproduction checks passed. Both records remain DRAFT.

## Findings

### ng-nips9-section: Fisher corroboration cites the wrong NIPS 9 section

minor / resolved / confirmed; issue key: aimech.natural-gradient.nips9-fisher-section.

Historical defect identified in the predecessor review: The model-fisher-statistical-metric evidence cites Section 3 for NIPS 9 PDF p. 4 / printed p. 130, Equation 11. The actual page heading is Section 4, Natural gradient gives efficient on-line learning. Section 3 is on the preceding page. Replace only Section 3 with Section 4 in this locator and its report mirror; the page, equation and scientific claim remain supported. The correction and its verification are recorded in this successor disposition.

Disposition: Corrected in the maintained NaturalGradient record and matching report entry. Root inspected the changed captured fields against the primary headings: NIPS9 Equation11 is Section4; Amari1998 Equations3.1–3.2 are Section3. Pages, equations, scientific statements and mappings remain unchanged. Publication gates passed; original review and CREATE history are preserved.

### ng-learning-section: Sampled-loss equations cite a subsection that starts later

minor / resolved / confirmed; issue key: aimech.natural-gradient.sampled-loss-section.

Historical defect identified in the predecessor review: The sampled-loss-gradient-use locator attributes Equations 3.1–3.2 to Section 3.1. Both equations are under Section 3, Natural Gradient Learning, on 1998 PDF p. 4 / printed p. 254; subsection 3.1 starts on the next page. Replace only Section 3.1, Equations 3.1–3.2 with Section 3, Equations 3.1–3.2 in this locator and its report mirror. The other subsection, page and equation references remain unchanged; the scientific claim is supported. The correction and its verification are recorded in this successor disposition.

Disposition: Corrected in the maintained NaturalGradient record and matching report entry. Root inspected the changed captured fields against the primary headings: NIPS9 Equation11 is Section4; Amari1998 Equations3.1–3.2 are Section3. Pages, equations, scientific statements and mappings remain unchanged. Publication gates passed; original review and CREATE history are preserved.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:NaturalGradient. Retain the reusable metric-gradient direction separately from AdaptationSampling: a geometric direction neither compares hypothetical hyperparameters nor defines a statistical controller. Retain its distinctions from NES/IGO frameworks and particular Gaussian or ICA algorithms; a component relationship is not exact identity.
- retain: AIMech:AdaptationSampling. Retain one comparative hyperparameter-controller identity with both explicitly distinguished sampling modes. The methods do not equate it with NaturalGradient, a host xNES/SNES/IGO method, generic importance sampling or a weighted test. The record does not split direct/virtual modes into unsupported new identities or treat xNES-as as an exact synonym.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record-naturalgradient | data/curated/NaturalGradient.yaml | supports | Current captured bytes were compared with the original full-field scientific assessment and the exact correction receipt. Only NaturalGradient two section locators and updated_at changed in record content; report mirrors the corrected record and retains explicit correction provenance. |
| record-adaptationsampling | data/curated/AdaptationSampling.yaml | supports | Current captured bytes were compared with the original full-field scientific assessment and the exact correction receipt. Only NaturalGradient two section locators and updated_at changed in record content; report mirrors the corrected record and retains explicit correction provenance. |
| src-amari1998 | https://bsi-ni.brain.riken.jp/database/file/176/181.pdf; Selected native text PDF pp. 2–6, 10–12, 15–16 and 19–21; selected visuals PDF pp. 4 and 21. PDF p. 4 text reread after capture. | supports | Core26-page1998 journal copy, hosted by RIKEN; publication date and later PDF build/modification dates remain different fields. Equations2.3/3.5, Sections4/7 and the local proof define the supported geometry. Printed Fisher/BSS displays and proof-rate caveats are retained; neither an author erratum nor a full theorem verification is asserted. The original DNS failure and successful network retry retain separate receipts, and the publisher access limitation is not absence of the paper. Access timestamp is acquisition metadata, not a claim of full-paper reading. The selected reading scope is stated in the locator; most source assessment preceded capture. |
| src-amari1996-nips9 | https://proceedings.neurips.cc/paper/1996/file/39e4973ba3321b80f37d9b55f63ed8b8-Paper.pdf; Selected native text PDF pp. 3–4 and visual p. 4; p. 4 text reread after capture. Section 4 contains Equation 11. | supports | Official seven-page NIPS9 general-geometry article, conference1996/printed127–133, cited by the1998 paper as its earlier version. Its Equation11 uses two log-density derivatives and belongs to Section4 on PDF4, while its local metric definition is Section3 on PDF3. This is corroboration from a distinct source version, not interchangeable pagination with the journal. Access timestamp is acquisition metadata, not a claim of full-paper reading. The selected reading scope is stated in the locator; most source assessment preceded capture. |
| src-amari-cichocki-yang1996-nips8 | https://proceedings.neurips.cc/paper/1995/file/e19347e1c3ca0c0b97de5fb3b690855a-Paper.pdf; Selected visual PDF p. 5 / printed p. 761, Equations 18–19. Historical root visual timing correction remains separately attributed. | supports | Official seven-page NIPS8 blind-separation article, conference1995 and cited as1996 proceedings, printed757–763. PDF5 visually distinguishes the ordinary gradient and its right-metric adjustment; Equations18–19 support the specialized matrix rule and outer-product reconciliation. It does not establish that every ICA procedure is natural gradient or that the specified metric is every unknown-source Fisher. The root visual timing was honestly corrected in a successor receipt rather than backdated. Access timestamp is acquisition metadata, not a claim of full-paper reading. The selected reading scope is stated in the locator; most source assessment preceded capture. |
| src-schaul2011-thesis | https://people.idsia.ch/~tom/publications/thesis.pdf; Selected native text PDF pp. 48–49 and 121; visual p. 121. Section 2.4.4 and Appendix B. | supports | The acquired134-page IDSIA author copy supplies the direct/virtual definition and the explicit weightedU construction. Only declared method/context pages were read; full_text denotes access level rather than a full-thesis audit. The body points to AppendixA, but the formula is in AppendixB, PDF121/printed97. Cover submission/acceptance dates are distinct from institutional oral-exam metadata; no byte equivalence to the separately described TUM repository PDF is asserted. Access timestamp is acquisition metadata, not a claim of full-paper reading. The selected reading scope is stated in the locator; most source assessment preceded capture. |
| src-wierstra2014 | https://www.jmlr.org/papers/volume15/wierstra14a/wierstra14a.pdf; Selected native text PDF pp. 11–13 / printed pp. 959–961, Section 3.2 and Algorithm 4. | supports | Official32-page JMLR journal copy restates the controller in Section3.2, PDF11–13/printed959–961, and supplies Algorithm4. Its prose supports unchanged quality values plus weights, while the displayed weight-times-rank shorthand and unspecified test return remain implementation caveats. Selective source reading is distinct from a full32-page review, and host NES conventions are not recertified by this controller claim. Access timestamp is acquisition metadata, not a claim of full-paper reading. The selected reading scope is stated in the locator; most source assessment preceded capture. |
| src-schaul2012 | https://www.cmap.polytechnique.fr/~nikolaus.hansen/proceedings/2012/GECCO/companion/p221.pdf; Selected native text PDF pp. 2–3 / printed pp. 222–223, Section 2.2, Algorithm 2 and Table 1. | supports | Eight-page GECCO2012 Companion source, printed221–228, supplies the explicit global-scale-rate specialization, counterfactual previous state, xNES-as composition and empirical defaults. The conference date is not invented as an exact publication date or DOI. The known-target restart-policy caveat prevents importing its numerical comparisons as general evidence. The initial sandbox DNS failure and successful retry are both retained; no author implementation or benchmark was run. Access timestamp is acquisition metadata, not a claim of full-paper reading. The selected reading scope is stated in the locator; most source assessment preceded capture. |
| captured-inputs | /private/tmp/aimech-cohort332-initial-review-20261015/capture.json | context_only | Historical initial-review observation: Actual canonical inspect output captures the working-tree revision, two targets and 31 exact input hashes. Inspection is not a scientific or project-gate pass. |
| postcapture-reading | /private/tmp/aimech-cohort332-initial-review-20261015/postcapture-reading.json | context_only | Historical initial-review observation: Actual postcapture full-target reading and hash comparison; source reading before capture is identified separately. |
| scientific-support | /private/tmp/aimech-cohort332-review-support-20261015/scientific-support.json | context_only | Same-author supporting primary-source and mathematical assessment with all 12 claim narratives and exact selected reading scope; not independent approval. |
| locator-audit | /private/tmp/aimech-cohort332-review-support-20261015/primary-locator-audit.json | supports | Both erroneous section numbers were confirmed against primary pages; claim content, equations and pages remain supported. |
| discovery-report | research/discovery/20261015T052604Z-natural-gradient-and-adaptation-sampling.json | context_only | Current captured bytes were compared with the original full-field scientific assessment and the exact correction receipt. Only NaturalGradient two section locators and updated_at changed in record content; report mirrors the corrected record and retains explicit correction provenance. |
| pinned-aio | sources/aio/aio.json; AIO:MetaLearning, AIO:TrainingStrategy, AIO:MathematicalFunction, AIO:ExponentialFunction, AIO:ReinforcementLearning, AIO:ProbabilisticHiddenLayer, AIO:SelectionAndSamplingBias, AIO:ActiveLearning, AIO:KnowledgeTransfer, AIO:MetaLearningLLM, AIO:EvolutionaryLLM, AIO:RegularizationLayer, AIO:MachineLearningTask | context_only | Pinned AIO mapping context. Thirteen current target definitions, names, scoped synonyms, direct parents and declared relationships were inspected in the preparation projection; this is not a fresh full incident-edge or whole-ontology review. |
| identity-assessment | /private/tmp/aimech-cohort332-current-identity-20261015/root-decisions.json | context_only | Root-owned current identity/frontier assessment: 1175 prior identity/definition/hash rows; four ignored/hidden-inclusive scans, 4491 occurrences in 196 exact contents. Historical supporting reading covers 167 retained contents and root freshly read 29 new contents. Existing owners 195/196 and residual context are retained. This subagent attributes that broader search work rather than claiming its own full fresh manual reassessment. |
| successor-gate | /private/tmp/aimech-natural-gradient-adaptation-cohort332-check-gate.json | context_only | Lint;247 tests passed,3 skipped;442 generated and735 native records; exact seed reproduction;408 history records; initial420 saved reviews passed. |
| successor-check-source | /private/tmp/aimech-natural-gradient-adaptation-cohort332-check-check-source.json | context_only | Pinned AIO source fingerprint verified. |
| successor-vendor | /private/tmp/aimech-natural-gradient-adaptation-cohort332-check-vendor.json | context_only | Governed artifacts match pinned public CLAW revision. |
| successor-render | /private/tmp/aimech-natural-gradient-adaptation-cohort332-check-render.json | context_only | Rendered current record pages. |
| successor-render-check | /private/tmp/aimech-natural-gradient-adaptation-cohort332-check-render-check.json | context_only | Generated pages reproduce from current records. |
| successor-diff | /private/tmp/aimech-natural-gradient-adaptation-cohort332-check-diff.json | context_only | No diff whitespace errors. |
| original-review | reviews/structured/20261015T053856Z-natural-gradient-adaptation-initial-locators/review.yaml | context_only | Original immutable partial scientific review retained both open locator findings before correction; required publication checks were pending. |
| actual-correction | /private/tmp/aimech-cohort332-correction/receipt.json | supports | Actual before/after receipt and retained preimages establish exactly two section-locator edits, actual curation updated_at, corresponding discovery report and an append-only EDIT sidecar. Original CREATE history and all other records remain unchanged. |
| corrected-inputs | /private/tmp/aimech-cohort332-successor-capture.json | context_only | Current canonical capture of corrected targets and maintained inputs; root inspected exact semantic changes after capture. |
| correction-audit | /private/tmp/aimech-cohort332-correction-supporting-audit.json | context_only | Supporting same-author audit passed43 bounded comparisons of exact correction, report mirroring, unchanged frontier/other record/CREATE history/initial review and primary headings. |
| scientific-peer | /private/tmp/aimech-cohort332-scientific-peer-20261015/assessment.json | context_only | Additional same-author scientific reassessment found no defect beyond the two corrected locators; specifically checked paired-U variance and metric-versus-model-Fisher boundaries. |

## Limits And Additional Notes

- Historical initial-review scope: Source access level full_text means the source was acquired, not that this reviewer read every page. Most primary reading preceded capture: Amari1998 native PDF2–6,10–12,15–16,19–21 and visuals4/21; NIPS9 native3–4 and visual4; BSS visual5; thesis native48–49/121 and visual121; JMLR2014 native11–13; proceedings2012 native2–3. Only the two finding pages were text-reread after capture.
- Root and other supporting source scopes, failed downloads and successful retries, the missing-PyYAML preparation failure, and the root BSS visual timing successor are preserved as historical attributed evidence. No earlier receipt is backdated or treated as a fresh independent review.
- The model-Fisher display discrepancy, matrix outer-product discrepancy, unproved proof-rate qualification, invariant-metric characterization limits, paired weighted-test variance counterexample, rank/test-return ambiguity and proposal-support limits remain explicit. Curator chain-rule and paired-count reasoning are not source theorems or empirical replication.
- No author code, numerical calculator, benchmark or statistical calibration experiment was executed. No general efficiency, finite-step invariance, optimizer convergence, source priority, global absence or literature saturation is certified.
- Current identity/search conclusions are attributed to the retained root assessment and historical supporting scopes. This subagent did not freshly manually reread the whole prior frontier or every captured implementation/context file.
- Both maintained review_status values remain DRAFT. Boundary decisions remain recommendations. Both locator corrections were actually performed in the separately recorded EDIT session; this successor observes their disposition and does not mutate records.
- The initial review and its source hashes describe historical uncorrected bytes; this successor captures corrected current bytes. Saved-review validation/check after this successor is a separate post-save action, not claimed by its pre-save full gate. Scientific support remains same-author review, with no author-code, calculator or benchmark execution.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T054954Z-natural-gradient-and-adaptation-sampling-corrected
kind: batch
repository: CultureBotAI/AIMech
title: Scientific author self-review after NaturalGradient citation corrections
started_at: '2026-10-15T05:40:43.064477Z'
finished_at: '2026-10-15T05:49:54.802856Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Root author reassessment and same-author supporting agents;
    no independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All 12 scientific claims, two definitions, mappings and 16 limitations were
  reassessed in the original captured cohort. Root read both full canonical records
  and all substantive supporting assessments. After correcting only two section locators
  and the actual NaturalGradient updated_at, root captured and inspected the corrected
  bytes and verified their exact semantic diff. Both original minor findings are resolved
  with retained predecessor identities and primary-page evidence. Required publication
  checks passed. Both records remain DRAFT; mathematical limitations and uninspected
  evidence boundaries remain explicit.
source:
  git_revision: eabf695fb458fd2163bacbdd7c49b74610832920
  state: working_tree
  inputs:
  - path: data/aio/ActiveLearning.yaml
    sha256: a4d5b2c82df6f586fedc7290261bc978e7c8d17f1d844c5ee9efc8243e46bbaf
    role: context
  - path: data/aio/EvolutionaryLLM.yaml
    sha256: d3db6adea3d8d58096c9fb5abef67273489ee719ab900b2d4adbb129e4f7362f
    role: context
  - path: data/aio/ExponentialFunction.yaml
    sha256: a9e6fe9954dee5c61f799631c1892a99a891468e81e725e584d1a3dc06d84239
    role: context
  - path: data/aio/KnowledgeTransfer.yaml
    sha256: d9c3efd84c05da8efb7b8eb46e15d64a1ea18fd0816c96cba9bcad85619c57bb
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
  - path: data/aio/MetaLearningLLM.yaml
    sha256: 79bc06e7aaa6c619a158b7ad34d7efa4d01eed506a37ab0afbc6b13274823b23
    role: context
  - path: data/aio/ProbabilisticHiddenLayer.yaml
    sha256: 610c29db815f7348c5bdcdc7e7460dd2dea9ea338f3727ebb1596c51b4af41da
    role: context
  - path: data/aio/RegularizationLayer.yaml
    sha256: d4280bbc058b841655bcfcea7ef1dd1e05ac5e0211a860045f13eaa30933dbae
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/SelectionAndSamplingBias.yaml
    sha256: 72d8ef34949942ddee1fe60d645806a2117b95207f681de923297b64f78cc477
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/AdaptationSampling.yaml
    sha256: 675a122fec61acc7b625d037a53d784420be2559e0aef6405dac91e50b762b27
    role: target
  - path: data/curated/CovarianceMatrixAdaptationEvolutionStrategy.yaml
    sha256: 7018c9916e78f34ba32a3a9d46e694d2a78c17a6e7222d9050d305eedf96ed06
    role: context
  - path: data/curated/ExponentialNaturalEvolutionStrategies.yaml
    sha256: 8230e120126387ffb32405d2072fa5604e8cf39598972afcf5401c53730088b6
    role: context
  - path: data/curated/InformationGeometricOptimization.yaml
    sha256: ef55808962485da0302293b2110ff61ed153c76b6e5da5c570f189dafc66282f
    role: context
  - path: data/curated/NaturalEvolutionStrategies.yaml
    sha256: b11c8d02da55175afcf5d5c11cf91a864418d7396b726f423f865d95cfe76a4c
    role: context
  - path: data/curated/NaturalGradient.yaml
    sha256: d082d3f17e9428d1765b8041ae6abecd604161b9d6d12082ef17b4d45255ce2b
    role: target
  - path: data/curated/SeparableNaturalEvolutionStrategies.yaml
    sha256: f39df297c75087d405a46904176b11e86d23759c95d8d0b5a16535f267983ae4
    role: context
  - path: docs/curated-concepts.md
    sha256: 1a3db0915791b0e90b02cd1f83c35850bfc3c97b18edfd8b946c91030578ccb8
    role: context
  - path: docs/record-review-profile.md
    sha256: 2d3e3a73264523c78930d17b0812e2d22887e25423fe7c38e0ddce922d9cec9d
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/reports/natural-gradient-and-adaptation-sampling/2026-10-15T052614Z-codex-3940fc.yaml
    sha256: 4f7ae1e23127d92674dcaad71b2904dfd33c7c5e16317e5f44d1d7f2acd4b76e
    role: context
  - path: history/reports/natural-gradient-and-adaptation-sampling/2026-10-15T054042Z-codex-7662ce.yaml
    sha256: ce7d78ac3ee4458889be2abcd46b736833512bc9f28aaa81865634adcae718cf
    role: context
  - path: justfile
    sha256: 2d9c1b68c1c80d53aa44a6b8b5e916efe8b493650ff59a3fc7479a42be37f400
    role: context
  - path: research/discovery/20261015T052604Z-natural-gradient-and-adaptation-sampling.json
    sha256: 208a84d2e99a1ec2bbae8bd470d8e9cbeeddb56e379a950ac3b90b381817b895
    role: context
  - path: research/discovery/20261015T052604Z-natural-gradient-and-adaptation-sampling.md
    sha256: bec95a938abbec17746fbf8ce64d72b82d34f111f0d71644362abafdb4c35777
    role: context
  - path: reviews/structured/20261015T053856Z-natural-gradient-adaptation-initial-locators/review.yaml
    sha256: 344742f9c021329062df18502e00ad85fe411b4c0a56e9b6c4b09b646c5597ae
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/check.py
    sha256: ff3a90be3a48a66f380d49c41de04cd8603bc0744feceeb907604b97c81f0629
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
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
  - path: src/aimech/schema/aimech.yaml
    sha256: 5a54dafe2fc17bc027e14bc3a2829b265cbb34427ad58eef63fe99616e17b852
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
scope:
  description: Complete two-target,12-claim cohort review after two citation corrections.
    Both records retain their definitions, scientific statements, mapping assessments
    and16 limitations.
  selection: Exact maintained IDs AIMech:NaturalGradient and AIMech:AdaptationSampling
    from the actual cohort332 creation.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - AIMech:NaturalGradient
  - AIMech:AdaptationSampling
  exclusions:
  - target: Unselected repository concepts and carried frontier entries
    reason: Context only; no fresh full scientific review of all prior records or
      source families.
  - target: Author implementations, benchmarks, complete source proofs and uninspected
      PDF pages
    reason: Outside the declared selective primary-source and analytic assessment.
targets:
- target_id: AIMech:NaturalGradient
  path: data/curated/NaturalGradient.yaml
  label: Natural gradient
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NaturalGradient.yaml
    role: maintained
- target_id: AIMech:AdaptationSampling
  path: data/curated/AdaptationSampling.yaml
  label: Adaptation sampling
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AdaptationSampling.yaml
    role: maintained
checks:
- check_id: successor-gate
  name: Full repository gate
  status: passed
  required: true
  summary: Lint;247 tests passed,3 skipped;442 generated and735 native records; exact
    seed reproduction;408 history records; initial420 saved reviews passed.
  target_ids:
  - AIMech:NaturalGradient
  - AIMech:AdaptationSampling
  command: just check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - successor-gate
- check_id: successor-check-source
  name: Pinned AIO source integrity
  status: passed
  required: true
  summary: Pinned AIO source fingerprint verified.
  target_ids:
  - AIMech:NaturalGradient
  - AIMech:AdaptationSampling
  command: uv run --locked aimech check-source
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - successor-check-source
- check_id: successor-vendor
  name: Vendored CLAW integrity
  status: passed
  required: true
  summary: Governed artifacts match pinned public CLAW revision.
  target_ids:
  - AIMech:NaturalGradient
  - AIMech:AdaptationSampling
  command: just vendored-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - successor-vendor
- check_id: successor-render
  name: Generated concept pages
  status: passed
  required: true
  summary: Rendered current record pages.
  target_ids:
  - AIMech:NaturalGradient
  - AIMech:AdaptationSampling
  command: just render
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - successor-render
- check_id: successor-render-check
  name: Page reproduction
  status: passed
  required: true
  summary: Generated pages reproduce from current records.
  target_ids:
  - AIMech:NaturalGradient
  - AIMech:AdaptationSampling
  command: just render-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - successor-render-check
- check_id: successor-diff
  name: Whitespace check
  status: passed
  required: true
  summary: No diff whitespace errors.
  target_ids:
  - AIMech:NaturalGradient
  - AIMech:AdaptationSampling
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - successor-diff
evidence:
- evidence_id: record-naturalgradient
  kind: record_content
  reference: data/curated/NaturalGradient.yaml
  accessed_at: '2026-10-15T05:49:54.793966Z'
  support: supports
  summary: Current captured bytes were compared with the original full-field scientific
    assessment and the exact correction receipt. Only NaturalGradient two section
    locators and updated_at changed in record content; report mirrors the corrected
    record and retains explicit correction provenance.
  snapshot_sha256: d082d3f17e9428d1765b8041ae6abecd604161b9d6d12082ef17b4d45255ce2b
- evidence_id: record-adaptationsampling
  kind: record_content
  reference: data/curated/AdaptationSampling.yaml
  accessed_at: '2026-10-15T05:49:54.794193Z'
  support: supports
  summary: Current captured bytes were compared with the original full-field scientific
    assessment and the exact correction receipt. Only NaturalGradient two section
    locators and updated_at changed in record content; report mirrors the corrected
    record and retains explicit correction provenance.
  snapshot_sha256: 675a122fec61acc7b625d037a53d784420be2559e0aef6405dac91e50b762b27
- evidence_id: src-amari1998
  kind: primary_source
  reference: https://bsi-ni.brain.riken.jp/database/file/176/181.pdf
  accessed_at: '2026-10-15T04:51:48Z'
  support: supports
  summary: Core26-page1998 journal copy, hosted by RIKEN; publication date and later
    PDF build/modification dates remain different fields. Equations2.3/3.5, Sections4/7
    and the local proof define the supported geometry. Printed Fisher/BSS displays
    and proof-rate caveats are retained; neither an author erratum nor a full theorem
    verification is asserted. The original DNS failure and successful network retry
    retain separate receipts, and the publisher access limitation is not absence of
    the paper. Access timestamp is acquisition metadata, not a claim of full-paper
    reading. The selected reading scope is stated in the locator; most source assessment
    preceded capture.
  locator: Selected native text PDF pp. 2–6, 10–12, 15–16 and 19–21; selected visuals
    PDF pp. 4 and 21. PDF p. 4 text reread after capture.
  snapshot_sha256: fd56b27be7088548daad4e33676c2ec36aa7f8b45d501dada8afb7c41f466b73
- evidence_id: src-amari1996-nips9
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper/1996/file/39e4973ba3321b80f37d9b55f63ed8b8-Paper.pdf
  accessed_at: '2026-10-15T04:48:23Z'
  support: supports
  summary: Official seven-page NIPS9 general-geometry article, conference1996/printed127–133,
    cited by the1998 paper as its earlier version. Its Equation11 uses two log-density
    derivatives and belongs to Section4 on PDF4, while its local metric definition
    is Section3 on PDF3. This is corroboration from a distinct source version, not
    interchangeable pagination with the journal. Access timestamp is acquisition metadata,
    not a claim of full-paper reading. The selected reading scope is stated in the
    locator; most source assessment preceded capture.
  locator: Selected native text PDF pp. 3–4 and visual p. 4; p. 4 text reread after
    capture. Section 4 contains Equation 11.
  snapshot_sha256: 385ed47e413a0b1622a27eb8d36f730ae3c0a64a72355a479e659241356a98de
- evidence_id: src-amari-cichocki-yang1996-nips8
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper/1995/file/e19347e1c3ca0c0b97de5fb3b690855a-Paper.pdf
  accessed_at: '2026-10-15T04:52:49Z'
  support: supports
  summary: Official seven-page NIPS8 blind-separation article, conference1995 and
    cited as1996 proceedings, printed757–763. PDF5 visually distinguishes the ordinary
    gradient and its right-metric adjustment; Equations18–19 support the specialized
    matrix rule and outer-product reconciliation. It does not establish that every
    ICA procedure is natural gradient or that the specified metric is every unknown-source
    Fisher. The root visual timing was honestly corrected in a successor receipt rather
    than backdated. Access timestamp is acquisition metadata, not a claim of full-paper
    reading. The selected reading scope is stated in the locator; most source assessment
    preceded capture.
  locator: Selected visual PDF p. 5 / printed p. 761, Equations 18–19. Historical
    root visual timing correction remains separately attributed.
  snapshot_sha256: 5b8a207f0f496fb5f075894f0c6434b7456b06e590a5003efdb640f0fa4f3e1d
- evidence_id: src-schaul2011-thesis
  kind: primary_source
  reference: https://people.idsia.ch/~tom/publications/thesis.pdf
  accessed_at: '2026-10-15T04:52:56Z'
  support: supports
  summary: The acquired134-page IDSIA author copy supplies the direct/virtual definition
    and the explicit weightedU construction. Only declared method/context pages were
    read; full_text denotes access level rather than a full-thesis audit. The body
    points to AppendixA, but the formula is in AppendixB, PDF121/printed97. Cover
    submission/acceptance dates are distinct from institutional oral-exam metadata;
    no byte equivalence to the separately described TUM repository PDF is asserted.
    Access timestamp is acquisition metadata, not a claim of full-paper reading. The
    selected reading scope is stated in the locator; most source assessment preceded
    capture.
  locator: Selected native text PDF pp. 48–49 and 121; visual p. 121. Section 2.4.4
    and Appendix B.
  snapshot_sha256: 788a40bc471cdef2ab15b2a48145477aa2a29d0ffbde26917bad9760cb43ea4d
- evidence_id: src-wierstra2014
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume15/wierstra14a/wierstra14a.pdf
  accessed_at: '2026-10-15T04:08:30Z'
  support: supports
  summary: Official32-page JMLR journal copy restates the controller in Section3.2,
    PDF11–13/printed959–961, and supplies Algorithm4. Its prose supports unchanged
    quality values plus weights, while the displayed weight-times-rank shorthand and
    unspecified test return remain implementation caveats. Selective source reading
    is distinct from a full32-page review, and host NES conventions are not recertified
    by this controller claim. Access timestamp is acquisition metadata, not a claim
    of full-paper reading. The selected reading scope is stated in the locator; most
    source assessment preceded capture.
  locator: Selected native text PDF pp. 11–13 / printed pp. 959–961, Section 3.2 and
    Algorithm 4.
  snapshot_sha256: 80ec84951836e76f3db0ce5d245d73ceecf8b233069cca387ed97f157bae08d6
- evidence_id: src-schaul2012
  kind: primary_source
  reference: https://www.cmap.polytechnique.fr/~nikolaus.hansen/proceedings/2012/GECCO/companion/p221.pdf
  accessed_at: '2026-10-15T04:55:41Z'
  support: supports
  summary: Eight-page GECCO2012 Companion source, printed221–228, supplies the explicit
    global-scale-rate specialization, counterfactual previous state, xNES-as composition
    and empirical defaults. The conference date is not invented as an exact publication
    date or DOI. The known-target restart-policy caveat prevents importing its numerical
    comparisons as general evidence. The initial sandbox DNS failure and successful
    retry are both retained; no author implementation or benchmark was run. Access
    timestamp is acquisition metadata, not a claim of full-paper reading. The selected
    reading scope is stated in the locator; most source assessment preceded capture.
  locator: Selected native text PDF pp. 2–3 / printed pp. 222–223, Section 2.2, Algorithm
    2 and Table 1.
  snapshot_sha256: ef2d3e54ebf70c8d4feb6d9d8a89e44734f9fb50c1c3e665ba92a13ef681f0bb
- evidence_id: captured-inputs
  kind: record_content
  reference: /private/tmp/aimech-cohort332-initial-review-20261015/capture.json
  accessed_at: '2026-10-15T05:38:56.603874Z'
  support: context_only
  summary: 'Historical initial-review observation: Actual canonical inspect output
    captures the working-tree revision, two targets and 31 exact input hashes. Inspection
    is not a scientific or project-gate pass.'
  snapshot_sha256: 23e2c8064b071133277c4e305e786fa13390ffa93916e361633b657ccf0ebf07
- evidence_id: postcapture-reading
  kind: record_content
  reference: /private/tmp/aimech-cohort332-initial-review-20261015/postcapture-reading.json
  accessed_at: '2026-10-15T05:38:56.603874Z'
  support: context_only
  summary: 'Historical initial-review observation: Actual postcapture full-target
    reading and hash comparison; source reading before capture is identified separately.'
  snapshot_sha256: b056394beea19a7ee3b07805d119b83bb3c229af90869820d0e1f5191342566d
- evidence_id: scientific-support
  kind: record_content
  reference: /private/tmp/aimech-cohort332-review-support-20261015/scientific-support.json
  accessed_at: '2026-10-15T05:38:56.603874Z'
  support: context_only
  summary: Same-author supporting primary-source and mathematical assessment with
    all 12 claim narratives and exact selected reading scope; not independent approval.
  snapshot_sha256: feee8e4142d2f405ee4f0542d5d52c0fd17caa01eb2b879b65046236a3f71acf
- evidence_id: locator-audit
  kind: record_content
  reference: /private/tmp/aimech-cohort332-review-support-20261015/primary-locator-audit.json
  accessed_at: '2026-10-15T05:38:56.603874Z'
  support: supports
  summary: Both erroneous section numbers were confirmed against primary pages; claim
    content, equations and pages remain supported.
  snapshot_sha256: 71c4b46850b0150bf353a2ded7b3e5257cc59454511d125093064e5f57bde70d
- evidence_id: discovery-report
  kind: record_content
  reference: research/discovery/20261015T052604Z-natural-gradient-and-adaptation-sampling.json
  accessed_at: '2026-10-15T05:49:54.797327Z'
  support: context_only
  summary: Current captured bytes were compared with the original full-field scientific
    assessment and the exact correction receipt. Only NaturalGradient two section
    locators and updated_at changed in record content; report mirrors the corrected
    record and retains explicit correction provenance.
  snapshot_sha256: 208a84d2e99a1ec2bbae8bd470d8e9cbeeddb56e379a950ac3b90b381817b895
- evidence_id: pinned-aio
  kind: database
  reference: sources/aio/aio.json
  accessed_at: '2026-10-15T05:38:56.603874Z'
  support: context_only
  summary: Pinned AIO mapping context. Thirteen current target definitions, names,
    scoped synonyms, direct parents and declared relationships were inspected in the
    preparation projection; this is not a fresh full incident-edge or whole-ontology
    review.
  locator: AIO:MetaLearning, AIO:TrainingStrategy, AIO:MathematicalFunction, AIO:ExponentialFunction,
    AIO:ReinforcementLearning, AIO:ProbabilisticHiddenLayer, AIO:SelectionAndSamplingBias,
    AIO:ActiveLearning, AIO:KnowledgeTransfer, AIO:MetaLearningLLM, AIO:EvolutionaryLLM,
    AIO:RegularizationLayer, AIO:MachineLearningTask
  snapshot_sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
- evidence_id: identity-assessment
  kind: search
  reference: /private/tmp/aimech-cohort332-current-identity-20261015/root-decisions.json
  accessed_at: '2026-10-15T05:38:56.603874Z'
  support: context_only
  summary: 'Root-owned current identity/frontier assessment: 1175 prior identity/definition/hash
    rows; four ignored/hidden-inclusive scans, 4491 occurrences in 196 exact contents.
    Historical supporting reading covers 167 retained contents and root freshly read
    29 new contents. Existing owners 195/196 and residual context are retained. This
    subagent attributes that broader search work rather than claiming its own full
    fresh manual reassessment.'
  snapshot_sha256: e8c50ba2e5f48957e27ff20e1f9231300bd156c5ad87ece57e64947de05e6ddd
  search_scope: Bounded four-checkout rg --no-ignore --hidden combined NaturalGradient/AdaptationSampling
    search; retained actual collection and root decisions. No universal absence or
    saturation claim.
- evidence_id: successor-gate
  kind: validation
  reference: /private/tmp/aimech-natural-gradient-adaptation-cohort332-check-gate.json
  accessed_at: '2026-10-15T05:49:12.006279Z'
  support: context_only
  snapshot_sha256: ea10edf575ce444cd2a555fcf92eb615c1f329bfdd803b9f53f9b174f8e41ef1
  summary: Lint;247 tests passed,3 skipped;442 generated and735 native records; exact
    seed reproduction;408 history records; initial420 saved reviews passed.
- evidence_id: successor-check-source
  kind: validation
  reference: /private/tmp/aimech-natural-gradient-adaptation-cohort332-check-check-source.json
  accessed_at: '2026-10-15T05:41:44.147829Z'
  support: context_only
  snapshot_sha256: 01be3e47fadfd3879a3e86101757d152ee32869dee576005a4f3bf87fe621f0f
  summary: Pinned AIO source fingerprint verified.
- evidence_id: successor-vendor
  kind: validation
  reference: /private/tmp/aimech-natural-gradient-adaptation-cohort332-check-vendor.json
  accessed_at: '2026-10-15T05:42:19.294030Z'
  support: context_only
  snapshot_sha256: 387da146d487624c85e1c6a36372bfe8fde7631b8bc828c88e29d7d3638bee5b
  summary: Governed artifacts match pinned public CLAW revision.
- evidence_id: successor-render
  kind: validation
  reference: /private/tmp/aimech-natural-gradient-adaptation-cohort332-check-render.json
  accessed_at: '2026-10-15T05:41:13.774813Z'
  support: context_only
  snapshot_sha256: a7d9e57a8454efec00d2f883446e3ba7268339b2304b99742f95b003f9401544
  summary: Rendered current record pages.
- evidence_id: successor-render-check
  kind: validation
  reference: /private/tmp/aimech-natural-gradient-adaptation-cohort332-check-render-check.json
  accessed_at: '2026-10-15T05:41:53.701759Z'
  support: context_only
  snapshot_sha256: 5880c0d6a17ac94f09aeed0be234b8165761e202dc5a309894c6b4632f1bd775
  summary: Generated pages reproduce from current records.
- evidence_id: successor-diff
  kind: validation
  reference: /private/tmp/aimech-natural-gradient-adaptation-cohort332-check-diff.json
  accessed_at: '2026-10-15T05:41:42.898583Z'
  support: context_only
  snapshot_sha256: eb559685356e29b617bd78f52f71029e167518f93ad6fd603632d617628185ca
  summary: No diff whitespace errors.
- evidence_id: original-review
  kind: prior_review
  reference: reviews/structured/20261015T053856Z-natural-gradient-adaptation-initial-locators/review.yaml
  accessed_at: '2026-10-15T05:49:54.801289Z'
  support: context_only
  snapshot_sha256: 344742f9c021329062df18502e00ad85fe411b4c0a56e9b6c4b09b646c5597ae
  summary: Original immutable partial scientific review retained both open locator
    findings before correction; required publication checks were pending.
- evidence_id: actual-correction
  kind: record_content
  reference: /private/tmp/aimech-cohort332-correction/receipt.json
  accessed_at: '2026-10-15T05:49:54.801507Z'
  support: supports
  snapshot_sha256: f75754bde774f9248b5898fa23de309bb3fe653884901279c63e8eebf95ee922
  summary: Actual before/after receipt and retained preimages establish exactly two
    section-locator edits, actual curation updated_at, corresponding discovery report
    and an append-only EDIT sidecar. Original CREATE history and all other records
    remain unchanged.
- evidence_id: corrected-inputs
  kind: record_content
  reference: /private/tmp/aimech-cohort332-successor-capture.json
  accessed_at: '2026-10-15T05:49:54.801613Z'
  support: context_only
  snapshot_sha256: c892e188e3b2f0b81239b522809b88ca0b8cc6fea69a686b966774d5d1e26859
  summary: Current canonical capture of corrected targets and maintained inputs; root
    inspected exact semantic changes after capture.
- evidence_id: correction-audit
  kind: record_content
  reference: /private/tmp/aimech-cohort332-correction-supporting-audit.json
  accessed_at: '2026-10-15T05:49:54.801712Z'
  support: context_only
  snapshot_sha256: c4dd1357445b84db911550f4821958ae4710e00cf54dc08c89a0125cb233ecf0
  summary: Supporting same-author audit passed43 bounded comparisons of exact correction,
    report mirroring, unchanged frontier/other record/CREATE history/initial review
    and primary headings.
- evidence_id: scientific-peer
  kind: record_content
  reference: /private/tmp/aimech-cohort332-scientific-peer-20261015/assessment.json
  accessed_at: '2026-10-15T05:49:54.802233Z'
  support: context_only
  snapshot_sha256: f710ab996726436dfc002d6b1a61be63900b2c11961843e25a4859c0cb9e0d2c
  summary: Additional same-author scientific reassessment found no defect beyond the
    two corrected locators; specifically checked paired-U variance and metric-versus-model-Fisher
    boundaries.
assessments:
- assessment_id: ng-metric-dependent-local-direction
  area: evidence
  topic: Claim metric-dependent-local-direction
  outcome: supported
  summary: The source proof on 1998 PDF pp.3–4 minimizes the first-order term g^T
    a under a metric-length constraint. With symmetric positive-definite G, Cauchy–Schwarz
    gives the stated normalized negative inverse-metric direction; the sign and square-root
    denominator are correct. The record explicitly requires g nonzero for that normalization
    and does not turn the local linearization into an exact finite-radius nonlinear
    minimizer. Equation2.5 is a later additive use, not an omitted normalization requirement.
  target_ids:
  - AIMech:NaturalGradient
  evidence_ids:
  - record-naturalgradient
  - src-amari1998
  - src-amari1996-nips9
- assessment_id: ng-model-fisher-statistical-metric
  area: evidence
  topic: Claim model-fisher-statistical-metric
  outcome: supported
  summary: 'Retained scientific assessment from the initial review: The statistical
    expectation is under the model density, and the conditional example includes a
    fixed input distribution and model output law. Equation3.5 and the explicit log-score
    calculation on PDF16 support both log derivatives; the visually retained Equation3.11
    mismatch is not silently certified. Finite score moments and nondegenerate coordinates
    explain why an ordinary inverse needs qualifications. An observed-label outer-product
    sample is not automatically the model expectation. NIPS9 Equation11 corroborates
    this, but its section locator must be corrected from3 to4; the claim itself is
    supported. The identified section locators have now been corrected and verified
    against the captured current bytes; see both resolved findings.'
  target_ids:
  - AIMech:NaturalGradient
  evidence_ids:
  - record-naturalgradient
  - src-amari1998
  - src-amari1996-nips9
  - locator-audit
  - actual-correction
- assessment_id: ng-sampled-loss-gradient-use
  area: evidence
  topic: Claim sampled-loss-gradient-use
  outcome: supported
  summary: 'Retained scientific assessment from the initial review: The source distinguishes
    expected loss L from one-observation l and permits a separately chosen preconditioning
    matrix before selecting G inverse. The record therefore correctly describes a
    sampled metric-gradient use rather than a complete universally specified optimizer.
    Independence and a fixed data law are part of the stated setup; no finite-step
    monotonicity follows. For example, even G=1 and a quadratic loss can increase
    after an excessively large step. Equations3.1–3.2 are correctly identified by
    page/equation but belong to Section3, not subsection3.1; that locator requires
    correction. The identified section locators have now been corrected and verified
    against the captured current bytes; see both resolved findings.'
  target_ids:
  - AIMech:NaturalGradient
  evidence_ids:
  - record-naturalgradient
  - src-amari1998
  - locator-audit
  - actual-correction
- assessment_id: ng-coordinate-direction-and-finite-step-boundary
  area: evidence
  topic: Claim coordinate-direction-and-finite-step-boundary
  outcome: supported
  summary: 'The transformation follows directly from g_theta=J^T g_w and G_theta=J^T
    G_w J with nonsingular J: the inverse action transforms by J inverse. This is
    a tangent-vector and corresponding flow statement. Taylor expansion of a twice-differentiable
    nonlinear coordinate map leaves a generally nonzero second-order term after an
    additive step; affine maps have no such term. The record identifies this as curator
    chain-rule/Taylor reasoning and does not misattribute an arbitrary finite-update
    invariance theorem to the paper.'
  target_ids:
  - AIMech:NaturalGradient
  evidence_ids:
  - record-naturalgradient
  - src-amari1998
- assessment_id: ng-specified-right-invariant-matrix-geometry
  area: evidence
  topic: Claim specified-right-invariant-matrix-geometry
  outcome: supported
  summary: The paper explicitly fixes the identity Frobenius metric and transports
    dW by right multiplication W inverse. That choice, not mere membership in a matrix
    group, yields (ordinary matrix gradient) W^T W in Theorem6. The nonintegrable-frame
    paragraph supports the warning that dX need not be global coordinates. The earlier
    BSS Equation18 displays the same metric adjustment and Equation19 confirms the
    matrix outer product missing from the1998 display. The record appropriately avoids
    identifying this chosen geometry with the exact Fisher for every unknown source
    law, or promising nonsingularity after arbitrary finite updates.
  target_ids:
  - AIMech:NaturalGradient
  evidence_ids:
  - record-naturalgradient
  - src-amari1998
  - src-amari-cichocki-yang1996-nips8
- assessment_id: ng-conditional-reported-asymptotic-efficiency
  area: evidence
  topic: Claim conditional-reported-asymptotic-efficiency
  outcome: supported
  summary: The inspected Section4 first fixes a realizable teacher and independent
    observations, then reports leading inverse-Fisher error second moment for a1/t
    natural update. The record qualifies invertibility, regularity and convergence
    instead of promoting the theorem title to a universal optimizer guarantee. The
    displayed O(1/t) metric perturbation is not implied by consistency alone and is
    expressly left uncertified. The same page switches to an expected Hessian for
    misspecification and excludes generic semiparametric separation/deconvolution,
    matching the maintained boundaries.
  target_ids:
  - AIMech:NaturalGradient
  evidence_ids:
  - record-naturalgradient
  - src-amari1998
- assessment_id: ng-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: The definition identifies an inverse-metric differential rule with Fisher
    as its statistical specialization; it does not conflate the local direction with
    all algorithms that use it. Section2 PDF2–4 and Section3.1 PDF5 Equation3.5 support
    this scope. The definition citation locators are correct.
  target_ids:
  - AIMech:NaturalGradient
  evidence_ids:
  - record-naturalgradient
  - src-amari1998
  - src-amari1996-nips9
  - src-amari-cichocki-yang1996-nips8
- assessment_id: ng-identity-kind-assessment
  area: identity
  topic: identity kind assessment
  outcome: supported
  summary: 'Retain a mathematical_method: fixed differentiable objective plus metric
    defines a vector rule, while initialization, gradient sampling, step size and
    domain handling belong to particular optimizers. NES/IGO add distribution objectives
    and sampling, xNES/SNES add finite Gaussian updates, and BSS is a specialization.
    Existing owner196 and its1996context are retained; fresh creation-time identity
    assessment remains root-owned.'
  target_ids:
  - AIMech:NaturalGradient
  evidence_ids:
  - record-naturalgradient
  - identity-assessment
- assessment_id: ng-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: The pinned MathematicalFunction definition is a rule relating dependent
    values to independent inputs, not only a scalar activation. For fixed objective
    and metric the natural-gradient construction is such a tangent-vector-valued rule,
    supporting only a qualified related_match. The record explicitly denies equivalence,
    subclass, neural layer and complete optimizer semantics. No Fisher-uniqueness
    theorem is inferred from the mapping.
  target_ids:
  - AIMech:NaturalGradient
  evidence_ids:
  - record-naturalgradient
  - pinned-aio
- assessment_id: ng-limitations-assessment
  area: scope
  topic: limitations assessment
  outcome: supported
  summary: Positive-definite/invertible domain, model versus observed-score expectation,
    sampled finite-step behavior, nonholonomic matrix frame, source formula discrepancies
    and the conditional reported efficiency theorem are material qualifications, not
    cosmetic caveats. Missing proof-rate and characterization assumptions remain unresolved
    rather than certified.
  target_ids:
  - AIMech:NaturalGradient
  evidence_ids:
  - record-naturalgradient
  - src-amari1998
  - src-amari1996-nips9
  - src-amari-cichocki-yang1996-nips8
- assessment_id: as-direct-hyperparameter-comparison
  area: evidence
  topic: Claim direct-hyperparameter-comparison
  outcome: supported
  summary: The thesis and journal both compare fresh samples under a nearby algorithm-hyperparameter
    setting and retain or revert that setting according to a quality comparison. This
    supports a meta-level controller identity; it does not specify the host optimizer’s
    gradient or make a Mann–Whitney protocol mandatory. The record distinguishes motivation
    by progress over time from maximizing raw sample fitness and does not promise
    nominal significance or automatic improvement.
  target_ids:
  - AIMech:AdaptationSampling
  evidence_ids:
  - record-adaptationsampling
  - src-schaul2011-thesis
  - src-wierstra2014
- assessment_id: as-virtual-density-ratio-reuse
  area: evidence
  topic: Claim virtual-density-ratio-reuse
  outcome: supported
  summary: The primary prose uses the same quality observations twice, first with
    unit weights and then with hypothetical-to-current density ratios. The direction
    of the ratio is correct, and the record keeps the values unchanged rather than
    multiplying their numeric ranks. Reuse explains avoided fresh quality evaluations
    but also makes the groups dependent. Observation-wise positive finite denominators
    alone do not prove global proposal coverage, integrability or stable weights;
    those limitations are preserved.
  target_ids:
  - AIMech:AdaptationSampling
  evidence_ids:
  - record-adaptationsampling
  - src-schaul2011-thesis
  - src-wierstra2014
- assessment_id: as-reported-weighted-rank-comparison
  area: evidence
  topic: Claim reported-weighted-rank-comparison
  outcome: supported
  summary: AppendixB visibly gives weighted greater-than pairs plus half weight for
    equality and substitutes the two weight masses in the ordinary normal mean/variance
    formulas. The record accurately labels these as reported formulas. For identical
    reused groups with all ratios one, h(x,y)+h(y,x)=1, including ties, so diagonal
    halves and unordered pairs force U=n²/2 for every sample; actual variance is zero,
    while the substituted variance is positive. This hand derivation justifies the
    calibration caveat without asserting a general unequal-law distribution, repaired
    test or universal invalidity of direct independent comparisons.
  target_ids:
  - AIMech:AdaptationSampling
  evidence_ids:
  - record-adaptationsampling
  - src-schaul2011-thesis
- assessment_id: as-nes-counterfactual-scale-learning-rate
  area: evidence
  topic: Claim nes-counterfactual-scale-learning-rate
  outcome: supported
  summary: The2012 method and Algorithm2 identify eta_sigma, not every NES learning
    rate or the current scale itself. The hypothetical law is recomputed from the
    previous optimizer state using1.5 times that rate, and the current population
    is compared through density ratios. This distinguishes a counterfactual optimizer
    update from multiplying sigma by1.5. The record does not inherit or recertify
    the separate full-matrix xNES pseudocode or its convention issues.
  target_ids:
  - AIMech:AdaptationSampling
  evidence_ids:
  - record-adaptationsampling
  - src-schaul2012
  - src-wierstra2014
- assessment_id: as-empirical-increase-or-return-policy
  area: evidence
  topic: Claim empirical-increase-or-return-policy
  outcome: supported
  summary: The prose specifies a capped multiplicative increase after a favorable
    comparison and otherwise an affine return toward the initial rate; c prime=0.1
    and the dimension-dependent rho match the thesis and2012 Table1. These are empirical
    settings, not an optimal rate or calibrated significance level. The record does
    not equate an unspecified weighted-Mann–Whitney return value with a particular
    directional p-value, and explicitly retains the rank/tail branch ambiguity in
    the printed algorithms.
  target_ids:
  - AIMech:AdaptationSampling
  evidence_ids:
  - record-adaptationsampling
  - src-schaul2011-thesis
  - src-schaul2012
- assessment_id: as-modes-and-composition-boundary
  area: evidence
  topic: Claim modes-and-composition-boundary
  outcome: supported
  summary: Fresh hypothetical-law samples and reweighted old observations are operationally
    different modes, and the source explicitly permits a mixture with unit-weight
    new samples. That supports one controller record with stated modes rather than
    silently identifying them as interchangeable implementations. The2012 xNES-as
    name is a host optimizer plus this controller. Generic importance sampling, importance
    mixing and the comparison statistic alone omit the parameter-selection mechanism,
    so the record properly rejects them as exact aliases.
  target_ids:
  - AIMech:AdaptationSampling
  evidence_ids:
  - record-adaptationsampling
  - src-schaul2011-thesis
  - src-wierstra2014
  - src-schaul2012
- assessment_id: as-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: The direct/virtual comparison controller is supported by thesis Section2.4.4
    PDF48–49 and journal Section3.2 PDF11–13. The definition leaves comparison details
    and host optimizer separate. Both definition evidence locators agree with the
    inspected sections.
  target_ids:
  - AIMech:AdaptationSampling
  evidence_ids:
  - record-adaptationsampling
  - src-schaul2011-thesis
  - src-wierstra2014
  - src-schaul2012
- assessment_id: as-identity-kind-assessment
  area: identity
  topic: identity kind assessment
  outcome: supported
  summary: Retain an algorithm controller with explicit direct/virtual modes. It chooses
    hyperparameter settings using comparative sample quality, unlike a bare importance-weighting
    estimator, standalone rank statistic, base NES gradient or population-copying
    method. xNES-as names the composition and is correctly excluded as an alias. Owner195
    is reused; no new family exhaustion is asserted.
  target_ids:
  - AIMech:AdaptationSampling
  evidence_ids:
  - record-adaptationsampling
  - identity-assessment
- assessment_id: as-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: 'The accepted13 no-match reasons are coherent with the current pinned definitions:
    metadata-based MetaLearning, model-training TrainingStrategy, labeling ActiveLearning
    and language-model/layer categories add requirements absent from the general controller.
    KnowledgeTransfer’s related Adaptation synonym does not establish identity. ExponentialFunction
    belongs to some hosts, not a mandatory controller operation. MathematicalFunction
    is broad, but generic computability is not an informative defining-component mapping
    for this procedure family. The bounded no-match assessment is distinct from a
    global ontology absence claim.'
  target_ids:
  - AIMech:AdaptationSampling
  evidence_ids:
  - record-adaptationsampling
  - pinned-aio
- assessment_id: as-limitations-assessment
  area: scope
  topic: limitations assessment
  outcome: supported
  summary: The equal-law paired witness refutes the substituted positive variance
    as the actual variance in that case; it does not disprove all independent direct
    tests. Half-tie pair counts do not supply a tie-adjusted variance, and repeated/data-selected
    comparisons, support and integrability need separate treatment. Weight-versus-multiplied-rank
    shorthand and the undefined return/tail convention prevent literal implementation
    certification. No performance or calibrated significance guarantee follows.
  target_ids:
  - AIMech:AdaptationSampling
  evidence_ids:
  - record-adaptationsampling
  - src-schaul2011-thesis
  - src-wierstra2014
  - src-schaul2012
- assessment_id: version-amari1998
  area: provenance
  topic: 'Source version and access: amari1998'
  outcome: supported
  summary: Core26-page1998 journal copy, hosted by RIKEN; publication date and later
    PDF build/modification dates remain different fields. Equations2.3/3.5, Sections4/7
    and the local proof define the supported geometry. Printed Fisher/BSS displays
    and proof-rate caveats are retained; neither an author erratum nor a full theorem
    verification is asserted. The original DNS failure and successful network retry
    retain separate receipts, and the publisher access limitation is not absence of
    the paper.
  target_ids:
  - AIMech:NaturalGradient
  evidence_ids:
  - src-amari1998
  - scientific-support
- assessment_id: version-amari1996-nips9
  area: provenance
  topic: 'Source version and access: amari1996-nips9'
  outcome: supported
  summary: Official seven-page NIPS9 general-geometry article, conference1996/printed127–133,
    cited by the1998 paper as its earlier version. Its Equation11 uses two log-density
    derivatives and belongs to Section4 on PDF4, while its local metric definition
    is Section3 on PDF3. This is corroboration from a distinct source version, not
    interchangeable pagination with the journal.
  target_ids:
  - AIMech:NaturalGradient
  evidence_ids:
  - src-amari1996-nips9
  - scientific-support
- assessment_id: version-amari-cichocki-yang1996-nips8
  area: provenance
  topic: 'Source version and access: amari-cichocki-yang1996-nips8'
  outcome: supported
  summary: Official seven-page NIPS8 blind-separation article, conference1995 and
    cited as1996 proceedings, printed757–763. PDF5 visually distinguishes the ordinary
    gradient and its right-metric adjustment; Equations18–19 support the specialized
    matrix rule and outer-product reconciliation. It does not establish that every
    ICA procedure is natural gradient or that the specified metric is every unknown-source
    Fisher. The root visual timing was honestly corrected in a successor receipt rather
    than backdated.
  target_ids:
  - AIMech:NaturalGradient
  evidence_ids:
  - src-amari-cichocki-yang1996-nips8
  - scientific-support
- assessment_id: version-schaul2011-thesis
  area: provenance
  topic: 'Source version and access: schaul2011-thesis'
  outcome: supported
  summary: The acquired134-page IDSIA author copy supplies the direct/virtual definition
    and the explicit weightedU construction. Only declared method/context pages were
    read; full_text denotes access level rather than a full-thesis audit. The body
    points to AppendixA, but the formula is in AppendixB, PDF121/printed97. Cover
    submission/acceptance dates are distinct from institutional oral-exam metadata;
    no byte equivalence to the separately described TUM repository PDF is asserted.
  target_ids:
  - AIMech:AdaptationSampling
  evidence_ids:
  - src-schaul2011-thesis
  - scientific-support
- assessment_id: version-wierstra2014
  area: provenance
  topic: 'Source version and access: wierstra2014'
  outcome: supported
  summary: Official32-page JMLR journal copy restates the controller in Section3.2,
    PDF11–13/printed959–961, and supplies Algorithm4. Its prose supports unchanged
    quality values plus weights, while the displayed weight-times-rank shorthand and
    unspecified test return remain implementation caveats. Selective source reading
    is distinct from a full32-page review, and host NES conventions are not recertified
    by this controller claim.
  target_ids:
  - AIMech:AdaptationSampling
  evidence_ids:
  - src-wierstra2014
  - scientific-support
- assessment_id: version-schaul2012
  area: provenance
  topic: 'Source version and access: schaul2012'
  outcome: supported
  summary: Eight-page GECCO2012 Companion source, printed221–228, supplies the explicit
    global-scale-rate specialization, counterfactual previous state, xNES-as composition
    and empirical defaults. The conference date is not invented as an exact publication
    date or DOI. The known-target restart-policy caveat prevents importing its numerical
    comparisons as general evidence. The initial sandbox DNS failure and successful
    retry are both retained; no author implementation or benchmark was run.
  target_ids:
  - AIMech:AdaptationSampling
  evidence_ids:
  - src-schaul2012
  - scientific-support
- assessment_id: actual-capture-and-status
  area: consistency
  topic: Actual target capture, source correspondence and DRAFT status
  outcome: supported
  summary: The corrected records and report entry payloads agree; exact semantic comparison
    establishes only the two locator edits and actual updated_at in NaturalGradient,
    with AdaptationSampling unchanged. Current capture input hashes remain exact.
    All12 scientific claims,13 no-match rejections and the qualified related mapping
    are preserved. Source, full gate, vendored and page reproduction checks passed.
    Both records remain DRAFT.
  target_ids:
  - AIMech:NaturalGradient
  - AIMech:AdaptationSampling
  evidence_ids:
  - captured-inputs
  - postcapture-reading
  - discovery-report
  - actual-correction
  - successor-gate
  - successor-check-source
  - corrected-inputs
  - correction-audit
findings:
- finding_id: ng-nips9-section
  issue_key: aimech.natural-gradient.nips9-fisher-section
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Fisher corroboration cites the wrong NIPS 9 section
  description: 'Historical defect identified in the predecessor review: The model-fisher-statistical-metric
    evidence cites Section 3 for NIPS 9 PDF p. 4 / printed p. 130, Equation 11. The
    actual page heading is Section 4, Natural gradient gives efficient on-line learning.
    Section 3 is on the preceding page. Replace only Section 3 with Section 4 in this
    locator and its report mirror; the page, equation and scientific claim remain
    supported. The correction and its verification are recorded in this successor
    disposition.'
  target_ids:
  - AIMech:NaturalGradient
  field_paths:
  - claims/1/evidence/1/locator
  evidence_ids:
  - record-naturalgradient
  - src-amari1996-nips9
  - locator-audit
  - original-review
  - actual-correction
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NaturalGradient.yaml
    role: maintained
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/370
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261015T053856Z-natural-gradient-adaptation-initial-locators
    finding_id: ng-nips9-section
  disposition_reason: 'Corrected in the maintained NaturalGradient record and matching
    report entry. Root inspected the changed captured fields against the primary headings:
    NIPS9 Equation11 is Section4; Amari1998 Equations3.1–3.2 are Section3. Pages,
    equations, scientific statements and mappings remain unchanged. Publication gates
    passed; original review and CREATE history are preserved.'
- finding_id: ng-learning-section
  issue_key: aimech.natural-gradient.sampled-loss-section
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Sampled-loss equations cite a subsection that starts later
  description: 'Historical defect identified in the predecessor review: The sampled-loss-gradient-use
    locator attributes Equations 3.1–3.2 to Section 3.1. Both equations are under
    Section 3, Natural Gradient Learning, on 1998 PDF p. 4 / printed p. 254; subsection
    3.1 starts on the next page. Replace only Section 3.1, Equations 3.1–3.2 with
    Section 3, Equations 3.1–3.2 in this locator and its report mirror. The other
    subsection, page and equation references remain unchanged; the scientific claim
    is supported. The correction and its verification are recorded in this successor
    disposition.'
  target_ids:
  - AIMech:NaturalGradient
  field_paths:
  - claims/2/evidence/0/locator
  evidence_ids:
  - record-naturalgradient
  - src-amari1998
  - locator-audit
  - original-review
  - actual-correction
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NaturalGradient.yaml
    role: maintained
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/370
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261015T053856Z-natural-gradient-adaptation-initial-locators
    finding_id: ng-learning-section
  disposition_reason: 'Corrected in the maintained NaturalGradient record and matching
    report entry. Root inspected the changed captured fields against the primary headings:
    NIPS9 Equation11 is Section4; Amari1998 Equations3.1–3.2 are Section3. Pages,
    equations, scientific statements and mappings remain unchanged. Publication gates
    passed; original review and CREATE history are preserved.'
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:NaturalGradient
  rationale: 'Retain the reusable metric-gradient direction separately from AdaptationSampling:
    a geometric direction neither compares hypothetical hyperparameters nor defines
    a statistical controller. Retain its distinctions from NES/IGO frameworks and
    particular Gaussian or ICA algorithms; a component relationship is not exact identity.'
  evidence_ids:
  - record-naturalgradient
  - scientific-support
- action: retain
  target_ids:
  - AIMech:AdaptationSampling
  rationale: Retain one comparative hyperparameter-controller identity with both explicitly
    distinguished sampling modes. The methods do not equate it with NaturalGradient,
    a host xNES/SNES/IGO method, generic importance sampling or a weighted test. The
    record does not split direct/virtual modes into unsupported new identities or
    treat xNES-as as an exact synonym.
  evidence_ids:
  - record-adaptationsampling
  - scientific-support
limitations:
- 'Historical initial-review scope: Source access level full_text means the source
  was acquired, not that this reviewer read every page. Most primary reading preceded
  capture: Amari1998 native PDF2–6,10–12,15–16,19–21 and visuals4/21; NIPS9 native3–4
  and visual4; BSS visual5; thesis native48–49/121 and visual121; JMLR2014 native11–13;
  proceedings2012 native2–3. Only the two finding pages were text-reread after capture.'
- Root and other supporting source scopes, failed downloads and successful retries,
  the missing-PyYAML preparation failure, and the root BSS visual timing successor
  are preserved as historical attributed evidence. No earlier receipt is backdated
  or treated as a fresh independent review.
- The model-Fisher display discrepancy, matrix outer-product discrepancy, unproved
  proof-rate qualification, invariant-metric characterization limits, paired weighted-test
  variance counterexample, rank/test-return ambiguity and proposal-support limits
  remain explicit. Curator chain-rule and paired-count reasoning are not source theorems
  or empirical replication.
- No author code, numerical calculator, benchmark or statistical calibration experiment
  was executed. No general efficiency, finite-step invariance, optimizer convergence,
  source priority, global absence or literature saturation is certified.
- Current identity/search conclusions are attributed to the retained root assessment
  and historical supporting scopes. This subagent did not freshly manually reread
  the whole prior frontier or every captured implementation/context file.
- Both maintained review_status values remain DRAFT. Boundary decisions remain recommendations.
  Both locator corrections were actually performed in the separately recorded EDIT
  session; this successor observes their disposition and does not mutate records.
- The initial review and its source hashes describe historical uncorrected bytes;
  this successor captures corrected current bytes. Saved-review validation/check after
  this successor is a separate post-save action, not claimed by its pre-save full
  gate. Scientific support remains same-author review, with no author-code, calculator
  or benchmark execution.
links:
- https://github.com/CultureBotAI/AIMech/issues/370
tags:
- scientific-review
- self-review
- corrected-successor
- citation-locators
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261015T053856Z-natural-gradient-adaptation-initial-locators
  relationship: Successor resolving both minor section-locator findings after actual
    correction and publication checks.
```
