# Scientific self-review of Regularized Evolution, Shake-Shake and ShakeDrop

- Review: 20261015T083524Z-regularized-evolution-shake-shake-and-shakedrop
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-15T08:20:59.383853Z
- Finished UTC: 2026-10-15T08:35:24.145401Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The explicit three-target batch was assessed through18 source-linked claims, definitions, five declared source rows, three qualified related mappings and20 individual limitations. Retain the aging architecture-search algorithm separately from the two distinct residual-network regularization procedures. Actual capture, root postcapture reading and completed required checks are bound. Records remain DRAFT; no new concrete findings were identified within the declared scope.

## Scope And Provenance

Complete explicit three-target curation batch; architecture search and residual regularization are not asserted to form one scientific category.

Selection: Exact maintained IDs AIMech:RegularizedEvolution, AIMech:ShakeShakeRegularization, AIMech:ShakeDropRegularization from actual cohort336 creation.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base fc27ccaf4668f1bf7468a10c269f5583fa3e640b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:RegularizedEvolution | data/curated/RegularizedEvolution.yaml | maintained | Regularized Evolution |
| AIMech:ShakeShakeRegularization | data/curated/ShakeShakeRegularization.yaml | maintained | Shake-Shake regularization |
| AIMech:ShakeDropRegularization | data/curated/ShakeDropRegularization.yaml | maintained | ShakeDrop regularization |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:RegularizedEvolution, AIMech:ShakeShakeRegularization, AIMech:ShakeDropRegularization | Actual command completed with exit0; exact output is retained. |
| just vendored-check | passed | True | AIMech:RegularizedEvolution, AIMech:ShakeShakeRegularization, AIMech:ShakeDropRegularization | Actual command completed with exit0; exact output is retained. |
| uv run --locked aimech check-source | passed | True | AIMech:RegularizedEvolution, AIMech:ShakeShakeRegularization, AIMech:ShakeDropRegularization | Actual command completed with exit0; exact output is retained. |
| just render | passed | True | AIMech:RegularizedEvolution, AIMech:ShakeShakeRegularization, AIMech:ShakeDropRegularization | Actual command completed with exit0; exact output is retained. |
| just render-check | passed | True | AIMech:RegularizedEvolution, AIMech:ShakeShakeRegularization, AIMech:ShakeDropRegularization | Actual command completed with exit0; exact output is retained. |
| git diff --check | passed | True | AIMech:RegularizedEvolution, AIMech:ShakeShakeRegularization, AIMech:ShakeDropRegularization | Actual command completed with exit0; exact output is retained. |
| Historical attempt: just vendored-check | failed | False | AIMech:RegularizedEvolution, AIMech:ShakeShakeRegularization, AIMech:ShakeDropRegularization | Retained failed attempt; the same required command later passed in the separately cited current log. |

## Scientific And Domain Assessments

### Claim trained-population-and-architecture-search

evidence: supported. Targets: AIMech:RegularizedEvolution.

The main Methods section and Algorithm 1 explicitly initialize a queue with random architectures followed by training/evaluation, while the NASNet section separates cell choices from repeated use of those cells. PDF 6 names AmoebaNet-A as a selected result. The statement correctly treats trained instances, architecture encodings and the outer search algorithm as different objects; it does not introduce a specific model instance.

### Claim with-replacement-fitness-tournament

evidence: supported. Targets: AIMech:RegularizedEvolution.

The prose on PDF 3 explicitly says uniform with-replacement draws and highest validation fitness. The parent criterion is therefore stored accuracy, not age, despite the broad introductory description. PDF 4 independently defines the baseline as independent random architecture generation, supporting the S=1 qualification. Repeated samples and unspecified ties remain explicit, rather than silently treating the sample as a set.

### Claim whole-population-oldest-removal

evidence: supported. Targets: AIMech:RegularizedEvolution.

Algorithm 1 appends the child on the right and removes the leftmost old individual. That is removal from the whole queue, not the tournament, and it yields P members at completed-update boundaries. The short P+1 transient follows directly from the operation order. PDF 2 explicitly contrasts gene-age ALPS. Architecture persistence is a boundary of individual-age semantics, not a claim of a new stochastic theorem.

### Claim architecture-mutation-and-fresh-evaluation

evidence: supported. Targets: AIMech:RegularizedEvolution.

Figure 3 and its surrounding text separately define connection and operation mutations, with a no-cycle constraint on new input connections. Methods Details supplies the optional identity mutation and reported P, S and probability, while PDF 8 discusses retraining inherited architectures. The statement confines constants and NASNet operators to the reported application and distinguishes a new training/evaluation call from PBT weight copying; it does not certify unseen code.

### Claim evaluation-history-and-stopping

evidence: supported. Targets: AIMech:RegularizedEvolution.

The displayed initialization inserts every evaluated individual into history before the while guard. Therefore C-P later updates under the stated integer C&gt;=P&gt;0 assumption and return of the best historical score are exact readings of Algorithm 1. A growing archive of fixed scores has a nondecreasing maximum, but FIFO can remove the best live member and noise can alter future retraining. Those elementary arguments do not establish optimization or statistical convergence.

### Claim training-noise-motivation-and-empirical-boundary

evidence: supported. Targets: AIMech:RegularizedEvolution.

The official discussion repeatedly calls the training-noise mechanism speculative and a conjecture for future verification. Supplement C expressly uses unit-cube bit strings with fraction-zero score plus Gaussian noise and labels the evidence circumstantial. The claim attributes this motivation and toy test without asserting universal regularization, guaranteed extinction, quantitative empirical superiority or a theorem about neural network search.

### definition assessment

evidence: supported. Targets: AIMech:RegularizedEvolution.

Algorithm 1 and the paired prose support every defining operation. The explicit names in the heading support the one Aging Evolution alias. The definition keeps parent selection and removal separate and does not turn this algorithm into the discovered AmoebaNet architecture.

### mapping assessment

grounding: supported. Targets: AIMech:RegularizedEvolution.

The accepted related-only link reflects mandatory model training/evaluation guiding architecture selection. It does not import the pinned preprocessing definition as an is-a statement. Thirteen exact AIO contexts were already inspected; output network classes, RL comparator and RegularizationLayer are not substituted.

### source assessment

provenance: supported. Targets: AIMech:RegularizedEvolution.

Both declared sources are explicitly cited: official AAAI2019 for the six core operational/scope claims and arXivv7 Supplement C in the sixth claim. The supplement is not an uncited metadata-only source. Acquisition hashes, date precision and failed/successful retrievals are retained in exact inputs.

### limitations assessment

scope: supported. Targets: AIMech:RegularizedEvolution.

All seven source and analytical limitations retain the distinction between fixed-score tournaments, sequential FIFO lifetimes and noisy empirical motivation. The C/history mismatch, sample-multiset interpretation and S=1 boundary are explicit; no concurrency, architecture-extinction or convergence guarantee is claimed.

### Concept boundary and actual owner

identity: supported. Targets: AIMech:RegularizedEvolution.

The maintained concept retains its accepted algorithm scope with its exact accepted aliases ['Aging Evolution']. Actual root decisions retain owner 183 and distinct residuals. The supporting historical identity scope is: The historical identity/frontier research supports one named algorithm and optional full-name alias under owner 183, not a new leaf or an architecture instance. Future creation must use its actual fresh context; no historical search is relabeled as current.

### Retained limitation 1

scope: supported. Targets: AIMech:RegularizedEvolution.

The source distinguishes the search procedure, NASNet search space, resulting AmoebaNets and ALPS. The limitation prevents scope expansion from the named original method to later variants or model outputs.

### Retained limitation 2

scope: supported. Targets: AIMech:RegularizedEvolution.

Explicit with-replacement prose takes precedence over the set glyph. The source leaves score ties and invalid inputs open; preserving those details avoids certifying a distinct-set implementation or invented repair.

### Retained limitation 3

scope: supported. Targets: AIMech:RegularizedEvolution.

This is the concrete guard/comment mismatch identified in research. For C&lt;P the initialization guard is independent of history, so initialization still takes P evaluations. Concurrency overshoot is deliberately unverified.

### Retained limitation 4

scope: supported. Targets: AIMech:RegularizedEvolution.

The paper mentions asynchronous workers without defining full concurrency semantics. A FIFO residence argument counts completed sequential updates, not seconds, and does not constrain repeated architectural genotypes.

### Retained limitation 5

scope: supported. Targets: AIMech:RegularizedEvolution.

The supporting rank-selection argument shows nonzero selection probability even for a low-ranked fixed-score member. Independent coexistence and mutation also undermine a literal extinction guarantee; the limitation is consistent with the surrounding conjecture language.

### Retained limitation 6

scope: supported. Targets: AIMech:RegularizedEvolution.

S=1 removes the fitness ranking step but leaves conditional mutation and population history. Replacement at S=P permits repeated individuals. The source does not establish uniformity over quotiented graph classes or trained functions, so the encoding qualifier is necessary.

### Retained limitation 7

scope: supported. Targets: AIMech:RegularizedEvolution.

Source identity, visible and machine dates, and the older author-page context are individually retained. The stated reading scope is exact and does not promote access to complete empirical/implementation validation.

### Claim two-residual-branches-and-skip

evidence: supported. Targets: AIMech:ShakeShakeRegularization.

The source explicitly distinguishes two learned residual units from the skip, and the implementation description qualifies the skip at changes of dimensions. This prevents the three-branch title from being misread as three learned residual paths or an identity operation at every resolution.

### Claim coupled-uniform-forward-mixture

evidence: supported. Targets: AIMech:ShakeShakeRegularization.

Equation2 gives complementary uniform weights on the two residual outputs. The source contrasts the whole-tensor scalar operation with elementwise perturbation and binary drop-path. No independent branch weights or added-loss penalty is inferred.

### Claim redrawn-backward-coefficients

evidence: supported. Targets: AIMech:ShakeShakeRegularization.

The full training paragraph and Figure1 specify overwriting coefficients for both passes. Keep is separately defined as reusing forward coefficients, so ordinary realized-forward chain-rule behavior cannot be silently imported into the fresh-backward configuration. The bounded scalar witness is curator reasoning, not a claimed source erratum.

### Claim image-versus-minibatch-sharing

evidence: supported. Targets: AIMech:ShakeShakeRegularization.

The explicit tensor slicing example holds one scalar over all channels/spatial locations within an image; Batch shares that scalar across images. This evidence supports both named sharing conventions without importing later per-pixel versions.

### Claim shake-even-keep-controls

evidence: supported. Targets: AIMech:ShakeShakeRegularization.

The source supplies exact meanings for Shake, Even and Keep and uses them as controlled settings. Section4 changes coefficient dependence experimentally; that discussion supports retaining configurations without forcing extra concept identities or pretending every setting is the core redrawn/redrawn rule.

### Claim half-weight-inference

evidence: supported. Targets: AIMech:ShakeShakeRegularization.

The test instruction sets each coefficient to its meanonehalf. Direct linearity of conditional expectation gives the local statement for fixed branch outputs. Equation1 is an unweighted sum, so neither recovery of that baseline nor exact nonlinear whole-network ensemble equivalence follows.

### definition assessment

evidence: supported. Targets: AIMech:ShakeShakeRegularization.

The original core is a training/inference procedure with two learned residual branches, complementary random forward weights, deliberately resampled backward weights and half-weight inference. The definition names sharing explicitly rather than conflating it with architecture or all stochastic regularization.

### mapping assessment

grounding: supported. Targets: AIMech:ShakeShakeRegularization.

Root accepted the single related_match to exact AIO:ResidualNeuralNetwork as procedure-to-original-host relatedness. It is not architecture equivalence or subclassing. TrainingStrategy was inspected but not selected; penalty-based RegularizationLayer and noise/dropout targets do not follow merely from the regularization label. The pinned node and incident context were read, without inferring universal components for every source variant.

### source assessment

provenance: supported. Targets: AIMech:ShakeShakeRegularization.

Fixed v2 primary evidence is declared and used in definition plus all six claims. Workshop equation-number correction is separately bound; workshop/v1 are not extra uncited sources. Source access is the actual successful 2026-10-15 acquisition, with original fractional timestamp and failed first acquisition retained.

### limitations assessment

scope: supported. Targets: AIMech:ShakeShakeRegularization.

All six limitations retain the original two-branch scope, deliberately redrawn backward rule, bounded hand counterexample, conditional local mean only, sharing/version distinctions and empirical limits. The workshop locator correction changes historical supporting provenance, not the accepted nativev2 mechanism.

### Concept boundary and actual owner

identity: supported. Targets: AIMech:ShakeShakeRegularization.

The maintained concept retains its accepted algorithm scope with its exact accepted aliases []. Actual root decisions retain owner 211 and distinct residuals. The supporting historical identity scope is: {"identity_notes": "The original 2017 two-learned-branch forward/backward mixing procedure is retained separately from its residual-network host, Bernoulli stochastic depth and cross-example MixUp or ManifoldMixup. Shake, Even, Keep and image/minibatch sharing are explicit configurations; no aliases are asserted. Historical research at 2026-10-15T07:42:50.033621Z–07:43:08.177461Z compared 742 native and 442 pinned AIO records, mechanically normalizing all 4,742 ID/local-ID/name/alias/scoped-synonym values with no candidate collision. Four ignored/hidden-inclusive checkout searches reconstructed all 1,444 occurrences into seven fully read exact contents: existing owner211, neighboring owner212 distinction text and historical FastAutoAugment code-tree inventory. All 65 selected definitions, 29 query-selected full frontier objects, three full native neighbors and 13 exact AIO contexts were read. This is historical bounded research, not a current creation-time absence assertion. Existing owner211 represents the concept; owners209 DropPath,212 ShakeDrop and227 Swapout remain separate pending source scopes.", "research": {"path": "/private/tmp/aimech-shake-shake-research-20261015/identity/assessment.json", "sha256": "a6543d911a6d052b522296eb599947506eed59ab846d563fc2922866ab612f33"}, "mapping_context": {"path": "/private/tmp/aimech-shake-shake-research-20261015/identity/aio-contexts.json", "sha256": "8dbb7437e890c893444908d10369f41bcd7b3370f20109641ca4e6347f417650"}}

### Retained limitation 1

scope: supported. Targets: AIMech:ShakeShakeRegularization.

The source-defined original residual host and separately reported architectural variants are distinguished. Continuous coupled mixing differs from binary path removal, and the same-example residual construction differs from input/target mixing across examples.

### Retained limitation 2

scope: supported. Targets: AIMech:ShakeShakeRegularization.

The hand calculation uses the same specified scalar forward loss and independent uniform coefficients. E[beta]=1/2, E[alpha]=1/2, E[alpha squared]=1/3 and E[alpha(1-alpha)]=1/6 give the displayed unequal fields. This is an analytical scope boundary, not an executed experiment or failure theorem.

### Retained limitation 3

scope: supported. Targets: AIMech:ShakeShakeRegularization.

The local expectation follows directly from a linear combination at fixed inputs. The record does not commute expectation through nonlinear downstream computation or conflate same-output branches with identical parameter-gradient allocations.

### Retained limitation 4

scope: supported. Targets: AIMech:ShakeShakeRegularization.

Sharing and pass choices are explicit in the method. Implementation-dependent random number generation, endpoint and device behavior remain outside source reading because author code was not inspected.

### Retained limitation 5

scope: supported. Targets: AIMech:ShakeShakeRegularization.

The complete source text contains empirical observations and a conclusion leaving dynamics for further study. No quantitative benchmark, convergence, decorrelation or generalization guarantee is added.

### Retained limitation 6

scope: supported. Targets: AIMech:ShakeShakeRegularization.

Exact v2 acquisition and submission metadata are retained separately from PDF build dates. Earlier workshop and v1 artifacts are provenance context; root and supporting reading scopes remain attributed, without asserting author-code execution or numerical agreement across editions.

### Claim gated-residual-perturbation

evidence: supported. Targets: AIMech:ShakeDropRegularization.

The single learned residual branch plus identity skip is explicit in the displayed construction. Scope separates the regularizer from its host and the compared two-learned-branch mixing method; it does not claim that every residual architecture works equally well.

### Claim distinct-forward-backward-coefficients

evidence: supported. Targets: AIMech:ShakeDropRegularization.

Equation (6) uses one b_l in both lines, with alpha and beta separately specified. Equations (7)–(8) give the two gate cases. Constant-zero alpha is explicitly studied. The statement treats the backward line as a prescribed path derivative rule, avoiding a false ordinary-chain-rule interpretation.

### Claim depth-dependent-switching

evidence: supported. Targets: AIMech:ShakeDropRegularization.

The l/L expression is indexed by block depth. The claim bounds p_L and does not reinterpret it as temporal annealing or claim one globally optimal value. The journal uses different choices for CIFAR, ImageNet and depth experiments.

### Claim sampling-and-host-settings

evidence: supported. Targets: AIMech:ShakeDropRegularization.

The later Section IV and Table 5 caption support the empirical range/sharing choices. The earlier v1 text explicitly chooses Image for memory despite the lower Pixel error in Table 2. Both sources are structurally cited, with no version-equivalence or numerical benefit claim.

### Claim deterministic-test-rule

evidence: supported. Targets: AIMech:ShakeDropRegularization.

The test line is printed in Equation (6). The conditional expectation is direct Bernoulli algebra, stated only for p_l&lt;1 so the zero-probability event at p_l=1 is not used. Independence and zero mean are sufficient for the p_l simplification. This does not average the nonlinear network.

### Claim distinction-and-special-cases

evidence: supported. Targets: AIMech:ShakeDropRegularization.

The special settings agree with the printed RandomDrop relation and Table 2 cases A/B. With alpha zero and beta positive, forward value suppression differs from suppressing both passes; a nonzero derivative is permitted, not guaranteed for every loss/Jacobian. Degenerate equality does not collapse identities.

### definition assessment

evidence: supported. Targets: AIMech:ShakeDropRegularization.

The definition describes the ordinary/perturbed switch, separately specified backward rule and deterministic test coefficient without saying every alpha configuration is sampled or imposing a universal positive perturbation.

### mapping assessment

grounding: supported. Targets: AIMech:ShakeDropRegularization.

The exact pinned residual-network CLASS supplies the host relation. This single related_match is neither equality nor an is_a assertion. The optional TrainingStrategy association remains historical context and is absent from the draft, as root requested.

### source assessment

provenance: supported. Targets: AIMech:ShakeDropRegularization.

The retained2019author proof and original2018v1 are both explicitly cited. They differ in coefficient sharing defaults and TypeA/B names; PDF build and acquisition times are not publication dates. The proof is not silently equated to the final publisher PDF or arXivv3. Historical acquisition failures and exact source hashes remain in the bound inputs.

### limitations assessment

scope: supported. Targets: AIMech:ShakeDropRegularization.

All seven limitations retain prescribed-versus-chain-rule differentiation, the conditional-zero-mean test coefficient, local-versus-network expectation, heuristic stability explanations, version-specific settings, same-gate semantics and bounded empirical/implementation scope. The accepted successor corrects only the independence-alone wording in limitation2; original bytes and root acceptance lineage remain explicit.

### Concept boundary and actual owner

identity: supported. Targets: AIMech:ShakeDropRegularization.

The maintained concept retains its accepted algorithm scope with its exact accepted aliases []. Actual root decisions retain owner 212 and distinct residuals. The supporting historical identity scope is: This record denotes the named ShakeDrop residual-network regularization procedure, not a particular trained network, the two-residual-branch Shake-Shake procedure, stochastic depth, DropBlock, Zoneout or the intermediate single-branch Shake construction. Coefficient and sharing configurations are not separately named native identities here. The accepted historical research snapshot contained 742 native and 442 pinned AIO records; normalized IDs, names, aliases and scoped synonyms had no queried collision. Four whole-checkout searches included ignored and hidden files and returned 714 occurrences reconstructed into one pending-label content. A bounded static check of 196 top-level TEMP content modules found no identity match. Research mechanically traversed all 908 main and 393 nested frontier objects and read 41 selected full objects, 54 semantic definitions, three full native neighbors and 13 exact AIO CLASS contexts with 53 incident-edge rows. Existing owner 212 belongs to this concept; owner 211 remains the distinct Shake-Shake lead. The old owner source pointer is historical discovery context, while the acquired primary evidence is identified explicitly. These historical findings do not assert a fresh future creation-time absence, global completeness or saturation. The optional qualified TrainingStrategy association was inspected but is not needed in addition to the residual-host mapping accepted here.

### Retained limitation 1

scope: supported. Targets: AIMech:ShakeDropRegularization.

The source supplies a prescribed backward multiplier. The scalar hand witness distinguishes it from the derivative of an expected randomized loss, while the ratio qualification avoids confusing a relative ratio with an absolute-gradient bound. Negative-alpha sign comparison is scoped to the same realized forward computation.

### Retained limitation 2

scope: supported. Targets: AIMech:ShakeDropRegularization.

Expectation is local and conditioned correctly. Subsequent nonlinear operations and stateful normalization prevent a generic whole-network average interpretation.

### Retained limitation 3

scope: supported. Targets: AIMech:ShakeDropRegularization.

Conceptual trajectories and empirical settings are not a general theorem. Probability and shape conditions are elementary requirements, not an asserted implementation safeguard.

### Retained limitation 4

scope: supported. Targets: AIMech:ShakeDropRegularization.

The Image-versus-Pixel choice and reversed A/B letters are directly visible source-version differences. The draft preserves the actual before/after-sum distinction instead of silently unifying letters.

### Retained limitation 5

scope: supported. Targets: AIMech:ShakeDropRegularization.

Same-gate use is literal. Zero local loss-gradient is narrower than unchanged parameters under a full optimizer, and alpha zero does not force the prescribed beta path to vanish. No author implementation was audited.

### Retained limitation 6

scope: supported. Targets: AIMech:ShakeDropRegularization.

Publication, build and acquisition times are distinct. The local-page author proof remains precisely identified; workshop and later full-text versions are not silently substituted.

### Retained limitation 7

scope: supported. Targets: AIMech:ShakeDropRegularization.

The claim set contains no performance-kind claim or new numerical comparison. The stated source/visual scope and absence of code, training and benchmark execution are accurate.

### Captured bytes, accepted science and frontier accounting

consistency: supported. Targets: AIMech:RegularizedEvolution, AIMech:ShakeShakeRegularization, AIMech:ShakeDropRegularization.

All three captured records equal the actual write payloads and report entries. Exact support covers18 claims and20 limitations. Only owners183/211/212 changed; all905 other main and393 nested values remain unchanged. Six required checks passed. No global exhaustion or DRAFT promotion is inferred.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:RegularizedEvolution. Regularized Evolution is fitness-tournament architecture search with oldest-instance replacement. It is distinct from the maintained generic GA, inherited-weight PBT, augmentation-policy search and architecture outputs. Aging Evolution is its explicitly supported alias, not a new record.
- retain: AIMech:ShakeShakeRegularization, AIMech:ShakeDropRegularization. Shake-Shake uses complementary weights on two learned residual branches with prescribed pass-specific sampling. ShakeDrop uses a shared Bernoulli switch and separate forward/backward perturbations on a residual contribution. Parameter special cases and a common residual host do not establish exact identity or a lump; keep owners211 and212 separate from stochastic depth and pending adjacent methods.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| captured-inputs | /private/tmp/aimech-evolution-shake-cohort336-capture.json | context_only | Actual canonical inspect output; all captured input hashes rechecked. Inspection alone is not scientific approval. |
| postcapture-reading | /private/tmp/aimech-evolution-shake-cohort336-root-postcapture-reading.json | context_only | Actual root full-target assessment after capture and completed checks; selective primary scopes are stated separately. |
| scientific-support | /private/tmp/aimech-evolution-shake-cohort336-review-preparation-20261015/scientific-support.prepared.json | context_only | Attributed same-author support of all18 accepted claims and20 individual limitations. This is preparation DATA, not itself an actual canonical capture. |
| actual-write | /private/tmp/aimech-evolution-shake-cohort336-write.json | context_only | Actual creation receipt binds three records, report pair and CREATE history. |
| discovery-report | research/discovery/20261015T081823Z-regularized-evolution-shake-shake-and-shakedrop.json | context_only | Record mirrors are exact. Only owners183/211/212 changed; all905 other main and393 nested objects are unchanged. No new frontier leaves. |
| creation-history | history/reports/regularized-evolution-shake-shake-and-shakedrop/2026-10-15T081837Z-codex-13ab96.yaml | context_only | Actual append-only CREATE sidecar; review and publication are separate later actions. |
| pinned-aio | sources/aio/aio.json; Exact AIO:TrainingStrategy and AIO:ResidualNeuralNetwork with retained inspected alternatives and incident edges. | context_only | Exact snapshot supports three qualified related mappings; no upstream equivalence or subclass assertion. |
| identity-assessment | /private/tmp/aimech-cohort336-root-decisions.json | context_only | Actual root decisions bind fresh ignored/hidden-inclusive scans and owner183/211/212 accounting; no manual rereading of every hit by this generator is claimed. |
| shake-shake-research-locator-correction | /private/tmp/aimech-shake-shake-draft-preparation-20261015/research-locator-correction.json; Historical workshop forward equation: Section1.1, PDFp1, Equation2; Equation3 is half-weight inference. Nativev2 core stays Section1.2,p2,Equation2. | context_only | The original frozen research locator incorrectly cited workshop Equation3 for forward mixing. The separate correction identifies Equation2 and preserves the original handoff. The native record usesv2; no canonical issue or formula correction is invented. |
| shakedrop-precuration-wording-correction | /private/tmp/aimech-shakedrop-expectation-wording-successor-20261015/correction.json; Native limitation2 final sentence; source SectionIII-A, Equation6, localPDFp3. | context_only | The original uninvoked draft said conditional zero-mean or independence assumptions. Its separately accepted successor states the required conditional meanzero and that independence together with zero mean is sufficient. All claims remain unchanged; originals are retained. No canonical finding or public issue is claimed. |
| src-real2019-aaai | https://ojs.aaai.org/index.php/AAAI/article/download/4405/4283; Supporting research read all10 official native-text pages and visuals2,3,4,8; core Algorithm1 p3, mutation pp3–4, discussionp8. Root research separately read method/discussion selectively, recorded in its acceptance; no full-paper root or benchmark/code audit is inferred. | supports | AAAI 2019 proceedings 33(01):4780–4789, official ten-page PDF. Publisher visible publication date is 2019-07-17; DC.Date.issued is 2019-07-23. The earlier 2018 workshop author page is a distinct version context. Acquisition time is access metadata, not a claim of full reading. |
| src-real2019-arxiv-v7 | https://arxiv.org/pdf/1802.01548v7; Separately pinned authorv7 is used for Supplement C p14 only in the native claim. Supporting research selectively read supplement text11,13,14 and visual14; root additionally read Supplement C p14 text+visual. No claim of full16page reading or verification of other supplement results. | supports | arXiv:1802.01548v7, 16 February 2019, sixteen-page author manuscript including supplements. Supplement C on PDF p. 14 supplies the cited toy-noise scope; no all-version or full-manuscript review is asserted. Acquisition time is access metadata, not a claim of full reading. |
| src-gastaldi2017v2 | https://arxiv.org/pdf/1705.07485v2; Supporting research read all10v2 native-text pages and visuals2–3; method Sections1.2–1.3 pp2 and2.1.2 p3, coefficient controls Section4. Root research read text2,3,6,7,8 and visuals2–3. Workshop/v1 remain distinct context, not extra declared native sources; no benchmark/code execution. | supports | Fixed arXiv:1705.07485v2, submitted 23 May 2017 at 13:36:46 UTC; ten-page author manuscript. The PDF build timestamp 24 May 2017 is distinct from submission. The earlier four-page ICLR 2017 workshop manuscript and arXiv v1 are separately retained context; no byte equivalence or cross-version numerical-result merger is asserted. Acquisition time is access metadata, not a claim of full reading. |
| src-yamada2019 | https://publication.imlab.jp/db/publication_data/1708/ACCESS2960566.pdf; Supporting research read all11 native-text pages of the author-hosted accepted-proof-layout copy and visuals2–6; defining Equations6–8 p3, sharingp5, TypeA/B p7, Appendix9–10. Root separately recorded selective reading. No final-publisher byte-equivalence or author implementation audit. | supports | IEEE Access 7 (2019), bibliographic pages 186126–186136; specifically retained 11-page author-hosted accepted-proof-layout copy, local PDF pages 1–11, received 7 October 2019 and accepted 9 December 2019, with placeholder publication-date fields. PDF metadata creation 24 December 2019 is a file-build timestamp. No byte-equivalence claim to the final publisher PDF or arXiv v3. Acquisition time is access metadata, not a claim of full reading. |
| src-yamada2018-v1 | https://arxiv.org/pdf/1802.02375v1; Supporting research read all12v1 native-text pages and visual5, including Image-versus-Pixel choice Section4.1 p5 and before/after-sum variants pp6–7. Root separately inspected relevant version passages. Source dates/builds and later defaults remain distinct; no benchmark reproduction. | supports | arXiv:1802.02375v1, submitted 7 February 2018 at 10:23:54 UTC; retained 12-page PDF returned by the pinned v1 route. Its ICLR 2018 conference-paper header is retained as printed, while the separate four-page workshop version is not treated as byte-equivalent. PDF metadata creation 27 May 2022 is a file-build timestamp, not the publication date. Acquisition time is access metadata, not a claim of full reading. |
| record-regularized-evolution | data/curated/RegularizedEvolution.yaml | supports | Complete maintained DRAFT record assessed by root after capture and matched to accepted scientific support. |
| record-shake-shake | data/curated/ShakeShakeRegularization.yaml | supports | Complete maintained DRAFT record assessed by root after capture and matched to accepted scientific support. |
| record-shakedrop | data/curated/ShakeDropRegularization.yaml | supports | Complete maintained DRAFT record assessed by root after capture and matched to accepted scientific support. |
| check-gate | /private/tmp/aimech-evolution-shake-cohort336-check-gate.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-vendor | /private/tmp/aimech-evolution-shake-cohort336-retry-check-vendor.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-check-source | /private/tmp/aimech-evolution-shake-cohort336-check-check-source.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-render | /private/tmp/aimech-evolution-shake-cohort336-check-render.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-render-check | /private/tmp/aimech-evolution-shake-cohort336-check-render-check.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-diff | /private/tmp/aimech-evolution-shake-cohort336-check-diff.json | context_only | Actual completed command and retained output before this new review was saved. |
| historical-check-attempt-1 | /private/tmp/aimech-evolution-shake-cohort336-check-vendor.json | context_only | Actual failed attempt retained alongside its later successful required-check replacement; failure is not rewritten as a pass. |

## Limits And Additional Notes

- Author self-review with attributed supporting agents is not independent scientific approval. Full_text is source access; selective root reading and supporting full-text scopes remain separately attributed.
- Regularized Evolution retains with-replacement tournaments, whole-population FIFO, historical budget including initialization, fixed-score archive semantics and unproved noise motivation. Sequential hand consequences are not guarantees about concurrent implementation, architecture extinction, convergence or benchmark superiority.
- Shake-Shake and ShakeDrop have prescribed backward rules, not automatic ordinary derivatives of the realized forward loss or unbiased gradients of one expected objective. Their deterministic local coefficient rules are not exact nonlinear whole-network ensemble predictions. Source-sharing, shape and special-case assumptions remain explicit.
- The official2019AAAI main paper and arXivv7 SupplementC, fixed Shake-Shakev2, and ShakeDrop2019author proof/original2018v1 are distinct source versions. Earlier workshop artifacts and differing build/publication dates remain context; no source-code or numerical-result equivalence is asserted.
- The Shake-Shake workshop-forward locator correction and ShakeDrop pre-curation limitation wording correction preserve original research/draft artifacts. These are truthful preparation lineage, not fabricated canonical findings or issues.
- No calculator, author implementation, model training or benchmark was executed for this review. Bounded curator hand arguments and source observations do not supply universal stability, generalization, efficiency or optimization guarantees.
- The three mappings are qualified related associations to TrainingStrategy or ResidualNeuralNetwork. They are not equivalence, subclass assertions or inherited architecture-component guarantees. Only actual identity notes and curation timestamps may differ from accepted previews.
- Required checks are actual retained completed logs, including explicitly retained failed attempts where applicable. Canonical validation, save and saved-review collection checking for this new review remain separate actions. No DRAFT promotion, upstream ontology change or global exhaustion is inferred.
- Root read complete canonical records, all18 claims/all20 limitations and corresponding attributed support, actual report Markdown/CREATE history/current owners and context projection after capture; all905 unrelated main and393 nested values were mechanically compared. Root primary reading was selective: Regularized Evolution main web text1–5/discussion6–8, local text2/4/6/7/8 and visual2/3/4/8; v7 SupplementC14 text+visual. Shake-Shake v2 text2/3/6/7/8 and visual2/3; workshop text1/2. ShakeDrop journal text3/4/5/6/7/10 and visual3/5, original v1 text2/3/4/5/7/10, workshop text2. Supporting agents read the broader scopes explicitly recorded in their ledgers. Root read selected exact pinned AIO contexts/incident edges and neighboring definitions, mappings, claims and limitations, not all repository bodies. Generated shared-page diffs were read; supporting agent parsed all three new HTML pages. Existing renderer omissions of definition_evidence and source version/access timestamps, and abbreviated hashes, are retained as display scope; canonical fields were verified. No author code, calculator, training or benchmark was executed.
- The accepted science is unchanged apart from explicitly declared current identity notes and timestamps. The three DRAFT algorithm identities and related mappings are supported with bounded claims: oldest-individual regularized evolution, separate Shake-Shake forward/backward draws, and shared-gate ShakeDrop coefficients with conditional-zero-mean qualification. All individual limitation assessments and pre-curation workshop-locator/ShakeDrop wording corrections were read and retained. Actual captured hashes and report mirrors match. Six required checks passed, including247 tests with3 skips; the failed DNS vendor attempt remains alongside its successful retry. No additional required finding was identified. This is author scientific review with supporting agents, not independent approval or global discovery exhaustion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
title: Scientific self-review of Regularized Evolution, Shake-Shake and ShakeDrop
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Root author assessment with attributed same-author supporting
    source and mathematical agents. No external or independent scientific approval
    is asserted.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The explicit three-target batch was assessed through18 source-linked claims,
  definitions, five declared source rows, three qualified related mappings and20 individual
  limitations. Retain the aging architecture-search algorithm separately from the
  two distinct residual-network regularization procedures. Actual capture, root postcapture
  reading and completed required checks are bound. Records remain DRAFT; no new concrete
  findings were identified within the declared scope.
scope:
  description: Complete explicit three-target curation batch; architecture search
    and residual regularization are not asserted to form one scientific category.
  selection: Exact maintained IDs AIMech:RegularizedEvolution, AIMech:ShakeShakeRegularization,
    AIMech:ShakeDropRegularization from actual cohort336 creation.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:RegularizedEvolution
  - AIMech:ShakeShakeRegularization
  - AIMech:ShakeDropRegularization
  exclusions:
  - target: Other age-based/NAS procedures, residual regularizers and coefficient
      variants
    reason: Context only; no resolution of DropPath, Swapout, general architecture
      search or every source configuration.
  - target: Author code, training runs, benchmark reproduction and source-wide guarantees
    reason: Outside the actual retained reading and bounded hand reasoning.
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:RegularizedEvolution
  rationale: Regularized Evolution is fitness-tournament architecture search with
    oldest-instance replacement. It is distinct from the maintained generic GA, inherited-weight
    PBT, augmentation-policy search and architecture outputs. Aging Evolution is its
    explicitly supported alias, not a new record.
  evidence_ids:
  - record-regularized-evolution
  - src-real2019-aaai
  - src-real2019-arxiv-v7
  - identity-assessment
- action: retain
  target_ids:
  - AIMech:ShakeShakeRegularization
  - AIMech:ShakeDropRegularization
  rationale: Shake-Shake uses complementary weights on two learned residual branches
    with prescribed pass-specific sampling. ShakeDrop uses a shared Bernoulli switch
    and separate forward/backward perturbations on a residual contribution. Parameter
    special cases and a common residual host do not establish exact identity or a
    lump; keep owners211 and212 separate from stochastic depth and pending adjacent
    methods.
  evidence_ids:
  - record-shake-shake
  - record-shakedrop
  - src-gastaldi2017v2
  - src-yamada2019
  - src-yamada2018-v1
  - pinned-aio
limitations:
- Author self-review with attributed supporting agents is not independent scientific
  approval. Full_text is source access; selective root reading and supporting full-text
  scopes remain separately attributed.
- Regularized Evolution retains with-replacement tournaments, whole-population FIFO,
  historical budget including initialization, fixed-score archive semantics and unproved
  noise motivation. Sequential hand consequences are not guarantees about concurrent
  implementation, architecture extinction, convergence or benchmark superiority.
- Shake-Shake and ShakeDrop have prescribed backward rules, not automatic ordinary
  derivatives of the realized forward loss or unbiased gradients of one expected objective.
  Their deterministic local coefficient rules are not exact nonlinear whole-network
  ensemble predictions. Source-sharing, shape and special-case assumptions remain
  explicit.
- The official2019AAAI main paper and arXivv7 SupplementC, fixed Shake-Shakev2, and
  ShakeDrop2019author proof/original2018v1 are distinct source versions. Earlier workshop
  artifacts and differing build/publication dates remain context; no source-code or
  numerical-result equivalence is asserted.
- The Shake-Shake workshop-forward locator correction and ShakeDrop pre-curation limitation
  wording correction preserve original research/draft artifacts. These are truthful
  preparation lineage, not fabricated canonical findings or issues.
- No calculator, author implementation, model training or benchmark was executed for
  this review. Bounded curator hand arguments and source observations do not supply
  universal stability, generalization, efficiency or optimization guarantees.
- The three mappings are qualified related associations to TrainingStrategy or ResidualNeuralNetwork.
  They are not equivalence, subclass assertions or inherited architecture-component
  guarantees. Only actual identity notes and curation timestamps may differ from accepted
  previews.
- Required checks are actual retained completed logs, including explicitly retained
  failed attempts where applicable. Canonical validation, save and saved-review collection
  checking for this new review remain separate actions. No DRAFT promotion, upstream
  ontology change or global exhaustion is inferred.
- 'Root read complete canonical records, all18 claims/all20 limitations and corresponding
  attributed support, actual report Markdown/CREATE history/current owners and context
  projection after capture; all905 unrelated main and393 nested values were mechanically
  compared. Root primary reading was selective: Regularized Evolution main web text1–5/discussion6–8,
  local text2/4/6/7/8 and visual2/3/4/8; v7 SupplementC14 text+visual. Shake-Shake
  v2 text2/3/6/7/8 and visual2/3; workshop text1/2. ShakeDrop journal text3/4/5/6/7/10
  and visual3/5, original v1 text2/3/4/5/7/10, workshop text2. Supporting agents read
  the broader scopes explicitly recorded in their ledgers. Root read selected exact
  pinned AIO contexts/incident edges and neighboring definitions, mappings, claims
  and limitations, not all repository bodies. Generated shared-page diffs were read;
  supporting agent parsed all three new HTML pages. Existing renderer omissions of
  definition_evidence and source version/access timestamps, and abbreviated hashes,
  are retained as display scope; canonical fields were verified. No author code, calculator,
  training or benchmark was executed.'
tags:
- scientific-review
- self-review
- heterogeneous-batch
- source-scoped
schema_version: 1.0.0
review_id: 20261015T083524Z-regularized-evolution-shake-shake-and-shakedrop
kind: batch
repository: CultureBotAI/AIMech
started_at: '2026-10-15T08:20:59.383853Z'
finished_at: '2026-10-15T08:35:24.145401Z'
source:
  git_revision: fc27ccaf4668f1bf7468a10c269f5583fa3e640b
  state: working_tree
  inputs:
  - path: .claude/skills/review-category/SKILL.md
    sha256: 553c3870c1dfc127f90f196b7b212b644706d4c26e2a578ab615ccce588070d7
    role: context
  - path: data/aio/RegularizationLayer.yaml
    sha256: d4280bbc058b841655bcfcea7ef1dd1e05ac5e0211a860045f13eaa30933dbae
    role: context
  - path: data/aio/ResidualNeuralNetwork.yaml
    sha256: 46855f48bc672169007ca212c92ee049f8089e649db9cfa272a3df61fa98ab3e
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/AutoAugment.yaml
    sha256: 29dec7588a9f992bb2bdaa71cde95d0bdb4d3a96353337f1149e61fa8099a9c8
    role: context
  - path: data/curated/FastAutoAugment.yaml
    sha256: 5b1f1543059ac7ec769f0cfc8f8c865cc027a2726ad69587d9b463b91f9dc26f
    role: context
  - path: data/curated/GeneticAlgorithm.yaml
    sha256: d40bf1a03e29a3ca6bf88f6553f18c6b1559baf56da6a21d63b54163f4752ceb
    role: context
  - path: data/curated/ManifoldMixup.yaml
    sha256: 0df5cfeb08de7758bd9cee4eba3382681f8183f6c37b2da8265e05bd49ddb915
    role: context
  - path: data/curated/MixUp.yaml
    sha256: 2f7e6cd92b02c2b258d3b1be9f541b6aa1593416032fc55da7250821d179a724
    role: context
  - path: data/curated/PopulationBasedTraining.yaml
    sha256: 4a0fff56bd5ccb2d2b21cea0c533bd0fa83e1601a035b1c0b5dbf796e7e81261
    role: context
  - path: data/curated/RegularizedEvolution.yaml
    sha256: a5a0a419b664a38daee85e821d6e5598583edad61ea7f24f94b3907ee3adb68e
    role: target
  - path: data/curated/ShakeDropRegularization.yaml
    sha256: f5653331df1b4469c49ed4a78b422aeadd16617a16fadea8ca4c42422c1236ff
    role: target
  - path: data/curated/ShakeShakeRegularization.yaml
    sha256: 184f2d3694ce8e98d8a55d3948ef4ffafed0ad345231e88ae27832d792da4883
    role: target
  - path: data/curated/StochasticDepth.yaml
    sha256: 32a0f2baac7ebf1c7f08c81f54710df74e56044bbf36e0df1ac7a05f4d925852
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
  - path: history/reports/regularized-evolution-shake-shake-and-shakedrop/2026-10-15T081837Z-codex-13ab96.yaml
    sha256: afc082db13f50cc35b5bfde9383a4d196b89a1124a8b7b24b7fb6641b5b11be5
    role: context
  - path: justfile
    sha256: 2d9c1b68c1c80d53aa44a6b8b5e916efe8b493650ff59a3fc7479a42be37f400
    role: context
  - path: research/discovery/20261015T081823Z-regularized-evolution-shake-shake-and-shakedrop.json
    sha256: f4dd01db75a7c85abd94e16e572a9f859ba670083d84da064b006774630557bd
    role: context
  - path: research/discovery/20261015T081823Z-regularized-evolution-shake-shake-and-shakedrop.md
    sha256: 5c41c90eb093438c9d9bcab9546d5965a30911c0772d4c4c634a86b1b9a8bcf0
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:RegularizedEvolution
  path: data/curated/RegularizedEvolution.yaml
  label: Regularized Evolution
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RegularizedEvolution.yaml
    role: maintained native concept record
- target_id: AIMech:ShakeShakeRegularization
  path: data/curated/ShakeShakeRegularization.yaml
  label: Shake-Shake regularization
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ShakeShakeRegularization.yaml
    role: maintained native concept record
- target_id: AIMech:ShakeDropRegularization
  path: data/curated/ShakeDropRegularization.yaml
  label: ShakeDrop regularization
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ShakeDropRegularization.yaml
    role: maintained native concept record
checks:
- check_id: check-gate
  name: just check
  status: passed
  required: true
  summary: Actual command completed with exit0; exact output is retained.
  target_ids:
  - AIMech:RegularizedEvolution
  - AIMech:ShakeShakeRegularization
  - AIMech:ShakeDropRegularization
  command: just check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-gate
- check_id: check-vendor
  name: just vendored-check
  status: passed
  required: true
  summary: Actual command completed with exit0; exact output is retained.
  target_ids:
  - AIMech:RegularizedEvolution
  - AIMech:ShakeShakeRegularization
  - AIMech:ShakeDropRegularization
  command: just vendored-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-vendor
- check_id: check-check-source
  name: uv run --locked aimech check-source
  status: passed
  required: true
  summary: Actual command completed with exit0; exact output is retained.
  target_ids:
  - AIMech:RegularizedEvolution
  - AIMech:ShakeShakeRegularization
  - AIMech:ShakeDropRegularization
  command: uv run --locked aimech check-source
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-check-source
- check_id: check-render
  name: just render
  status: passed
  required: true
  summary: Actual command completed with exit0; exact output is retained.
  target_ids:
  - AIMech:RegularizedEvolution
  - AIMech:ShakeShakeRegularization
  - AIMech:ShakeDropRegularization
  command: just render
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-render
- check_id: check-render-check
  name: just render-check
  status: passed
  required: true
  summary: Actual command completed with exit0; exact output is retained.
  target_ids:
  - AIMech:RegularizedEvolution
  - AIMech:ShakeShakeRegularization
  - AIMech:ShakeDropRegularization
  command: just render-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-render-check
- check_id: check-diff
  name: git diff --check
  status: passed
  required: true
  summary: Actual command completed with exit0; exact output is retained.
  target_ids:
  - AIMech:RegularizedEvolution
  - AIMech:ShakeShakeRegularization
  - AIMech:ShakeDropRegularization
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-diff
- check_id: historical-check-attempt-1
  name: 'Historical attempt: just vendored-check'
  status: failed
  required: false
  summary: Retained failed attempt; the same required command later passed in the
    separately cited current log.
  target_ids:
  - AIMech:RegularizedEvolution
  - AIMech:ShakeShakeRegularization
  - AIMech:ShakeDropRegularization
  command: just vendored-check
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - historical-check-attempt-1
evidence:
- evidence_id: captured-inputs
  kind: record_content
  reference: /private/tmp/aimech-evolution-shake-cohort336-capture.json
  accessed_at: '2026-10-15T08:35:10.442240Z'
  support: context_only
  summary: Actual canonical inspect output; all captured input hashes rechecked. Inspection
    alone is not scientific approval.
  snapshot_sha256: 3baafd6ed6d09c71c8441440ee1943bc265ef0a13d1ce8d39340123231dbf7fb
- evidence_id: postcapture-reading
  kind: record_content
  reference: /private/tmp/aimech-evolution-shake-cohort336-root-postcapture-reading.json
  accessed_at: '2026-10-15T08:35:10.442240Z'
  support: context_only
  summary: Actual root full-target assessment after capture and completed checks;
    selective primary scopes are stated separately.
  snapshot_sha256: 699b5fc537bcd8b0aa3d63a9635857496fdb115d50c808cc27778d88f3673c29
- evidence_id: scientific-support
  kind: record_content
  reference: /private/tmp/aimech-evolution-shake-cohort336-review-preparation-20261015/scientific-support.prepared.json
  accessed_at: '2026-10-15T08:35:10.442240Z'
  support: context_only
  summary: Attributed same-author support of all18 accepted claims and20 individual
    limitations. This is preparation DATA, not itself an actual canonical capture.
  snapshot_sha256: db160e80122f7b8954bc1f7b08158572cfc0ea7ce152abf0f6048718ae3c3d67
- evidence_id: actual-write
  kind: record_content
  reference: /private/tmp/aimech-evolution-shake-cohort336-write.json
  accessed_at: '2026-10-15T08:35:10.442240Z'
  support: context_only
  summary: Actual creation receipt binds three records, report pair and CREATE history.
  snapshot_sha256: be40182aa3bbda2d6460de6fa780d230554c1f6f5c95cd8405e648567b16f3b3
- evidence_id: discovery-report
  kind: record_content
  reference: research/discovery/20261015T081823Z-regularized-evolution-shake-shake-and-shakedrop.json
  accessed_at: '2026-10-15T08:35:10.442240Z'
  support: context_only
  summary: Record mirrors are exact. Only owners183/211/212 changed; all905 other
    main and393 nested objects are unchanged. No new frontier leaves.
  snapshot_sha256: f4dd01db75a7c85abd94e16e572a9f859ba670083d84da064b006774630557bd
- evidence_id: creation-history
  kind: record_content
  reference: history/reports/regularized-evolution-shake-shake-and-shakedrop/2026-10-15T081837Z-codex-13ab96.yaml
  accessed_at: '2026-10-15T08:35:10.442240Z'
  support: context_only
  summary: Actual append-only CREATE sidecar; review and publication are separate
    later actions.
  snapshot_sha256: afc082db13f50cc35b5bfde9383a4d196b89a1124a8b7b24b7fb6641b5b11be5
- evidence_id: pinned-aio
  kind: database
  reference: sources/aio/aio.json
  accessed_at: '2026-10-15T08:35:10.442240Z'
  support: context_only
  summary: Exact snapshot supports three qualified related mappings; no upstream equivalence
    or subclass assertion.
  locator: Exact AIO:TrainingStrategy and AIO:ResidualNeuralNetwork with retained
    inspected alternatives and incident edges.
  snapshot_sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
- evidence_id: identity-assessment
  kind: search
  reference: /private/tmp/aimech-cohort336-root-decisions.json
  accessed_at: '2026-10-15T08:35:10.442240Z'
  support: context_only
  summary: Actual root decisions bind fresh ignored/hidden-inclusive scans and owner183/211/212
    accounting; no manual rereading of every hit by this generator is claimed.
  snapshot_sha256: 4f3d13193b46e4e1624ba7c4a3cf9ed1aeca015b6b490d56b2a2601a04088cbd
  search_scope: Exact captured inventory, full carried frontier and four retained
    checkouts searched including ignored and hidden files; no worldwide absence or
    exhaustion claim.
- evidence_id: shake-shake-research-locator-correction
  kind: record_content
  reference: /private/tmp/aimech-shake-shake-draft-preparation-20261015/research-locator-correction.json
  accessed_at: '2026-10-15T08:35:10.442240Z'
  support: context_only
  summary: The original frozen research locator incorrectly cited workshop Equation3
    for forward mixing. The separate correction identifies Equation2 and preserves
    the original handoff. The native record usesv2; no canonical issue or formula
    correction is invented.
  locator: 'Historical workshop forward equation: Section1.1, PDFp1, Equation2; Equation3
    is half-weight inference. Nativev2 core stays Section1.2,p2,Equation2.'
  snapshot_sha256: 24ec0b8a44c102f912cdf623e2419750cd0498095c9654f600a9110fcc43d040
- evidence_id: shakedrop-precuration-wording-correction
  kind: record_content
  reference: /private/tmp/aimech-shakedrop-expectation-wording-successor-20261015/correction.json
  accessed_at: '2026-10-15T08:35:10.442240Z'
  support: context_only
  summary: The original uninvoked draft said conditional zero-mean or independence
    assumptions. Its separately accepted successor states the required conditional
    meanzero and that independence together with zero mean is sufficient. All claims
    remain unchanged; originals are retained. No canonical finding or public issue
    is claimed.
  locator: Native limitation2 final sentence; source SectionIII-A, Equation6, localPDFp3.
  snapshot_sha256: ae2ffaba869f8979c70a61ab67417515c28f1146461afc2b7429e9a5baae33b6
- evidence_id: src-real2019-aaai
  kind: primary_source
  reference: https://ojs.aaai.org/index.php/AAAI/article/download/4405/4283
  accessed_at: '2026-10-15T07:35:11Z'
  support: supports
  summary: AAAI 2019 proceedings 33(01):4780–4789, official ten-page PDF. Publisher
    visible publication date is 2019-07-17; DC.Date.issued is 2019-07-23. The earlier
    2018 workshop author page is a distinct version context. Acquisition time is access
    metadata, not a claim of full reading.
  locator: Supporting research read all10 official native-text pages and visuals2,3,4,8;
    core Algorithm1 p3, mutation pp3–4, discussionp8. Root research separately read
    method/discussion selectively, recorded in its acceptance; no full-paper root
    or benchmark/code audit is inferred.
  snapshot_sha256: 39fa5f1d74dd380c050a8d91f7251212b00056f1fc385a262f06ae2366636dee
- evidence_id: src-real2019-arxiv-v7
  kind: primary_source
  reference: https://arxiv.org/pdf/1802.01548v7
  accessed_at: '2026-10-15T07:38:39Z'
  support: supports
  summary: arXiv:1802.01548v7, 16 February 2019, sixteen-page author manuscript including
    supplements. Supplement C on PDF p. 14 supplies the cited toy-noise scope; no
    all-version or full-manuscript review is asserted. Acquisition time is access
    metadata, not a claim of full reading.
  locator: Separately pinned authorv7 is used for Supplement C p14 only in the native
    claim. Supporting research selectively read supplement text11,13,14 and visual14;
    root additionally read Supplement C p14 text+visual. No claim of full16page reading
    or verification of other supplement results.
  snapshot_sha256: bc74c52b4c131de073b6fa9318ef653dc0719aa99d0e5103d3f8d254c2e0cb92
- evidence_id: src-gastaldi2017v2
  kind: primary_source
  reference: https://arxiv.org/pdf/1705.07485v2
  accessed_at: '2026-10-15T07:41:19Z'
  support: supports
  summary: Fixed arXiv:1705.07485v2, submitted 23 May 2017 at 13:36:46 UTC; ten-page
    author manuscript. The PDF build timestamp 24 May 2017 is distinct from submission.
    The earlier four-page ICLR 2017 workshop manuscript and arXiv v1 are separately
    retained context; no byte equivalence or cross-version numerical-result merger
    is asserted. Acquisition time is access metadata, not a claim of full reading.
  locator: Supporting research read all10v2 native-text pages and visuals2–3; method
    Sections1.2–1.3 pp2 and2.1.2 p3, coefficient controls Section4. Root research
    read text2,3,6,7,8 and visuals2–3. Workshop/v1 remain distinct context, not extra
    declared native sources; no benchmark/code execution.
  snapshot_sha256: 5475784fc5c08a7ca6be3cca7214031821c15b8e37383c5a51fc467d75cfa7c5
- evidence_id: src-yamada2019
  kind: primary_source
  reference: https://publication.imlab.jp/db/publication_data/1708/ACCESS2960566.pdf
  accessed_at: '2026-10-15T07:49:07Z'
  support: supports
  summary: IEEE Access 7 (2019), bibliographic pages 186126–186136; specifically retained
    11-page author-hosted accepted-proof-layout copy, local PDF pages 1–11, received
    7 October 2019 and accepted 9 December 2019, with placeholder publication-date
    fields. PDF metadata creation 24 December 2019 is a file-build timestamp. No byte-equivalence
    claim to the final publisher PDF or arXiv v3. Acquisition time is access metadata,
    not a claim of full reading.
  locator: Supporting research read all11 native-text pages of the author-hosted accepted-proof-layout
    copy and visuals2–6; defining Equations6–8 p3, sharingp5, TypeA/B p7, Appendix9–10.
    Root separately recorded selective reading. No final-publisher byte-equivalence
    or author implementation audit.
  snapshot_sha256: 3a9687505f533abac20dc847cda8c3f228974e9c09af672d992f6c798cc6f58b
- evidence_id: src-yamada2018-v1
  kind: primary_source
  reference: https://arxiv.org/pdf/1802.02375v1
  accessed_at: '2026-10-15T07:47:33Z'
  support: supports
  summary: arXiv:1802.02375v1, submitted 7 February 2018 at 10:23:54 UTC; retained
    12-page PDF returned by the pinned v1 route. Its ICLR 2018 conference-paper header
    is retained as printed, while the separate four-page workshop version is not treated
    as byte-equivalent. PDF metadata creation 27 May 2022 is a file-build timestamp,
    not the publication date. Acquisition time is access metadata, not a claim of
    full reading.
  locator: Supporting research read all12v1 native-text pages and visual5, including
    Image-versus-Pixel choice Section4.1 p5 and before/after-sum variants pp6–7. Root
    separately inspected relevant version passages. Source dates/builds and later
    defaults remain distinct; no benchmark reproduction.
  snapshot_sha256: 31e0716fd1c4d4f59fbf7e0d04dad301226cfec1aa4bfb61a18802f189db8d22
- evidence_id: record-regularized-evolution
  kind: record_content
  reference: data/curated/RegularizedEvolution.yaml
  accessed_at: '2026-10-15T08:35:10.442240Z'
  support: supports
  summary: Complete maintained DRAFT record assessed by root after capture and matched
    to accepted scientific support.
  snapshot_sha256: a5a0a419b664a38daee85e821d6e5598583edad61ea7f24f94b3907ee3adb68e
- evidence_id: record-shake-shake
  kind: record_content
  reference: data/curated/ShakeShakeRegularization.yaml
  accessed_at: '2026-10-15T08:35:10.442240Z'
  support: supports
  summary: Complete maintained DRAFT record assessed by root after capture and matched
    to accepted scientific support.
  snapshot_sha256: 184f2d3694ce8e98d8a55d3948ef4ffafed0ad345231e88ae27832d792da4883
- evidence_id: record-shakedrop
  kind: record_content
  reference: data/curated/ShakeDropRegularization.yaml
  accessed_at: '2026-10-15T08:35:10.442240Z'
  support: supports
  summary: Complete maintained DRAFT record assessed by root after capture and matched
    to accepted scientific support.
  snapshot_sha256: f5653331df1b4469c49ed4a78b422aeadd16617a16fadea8ca4c42422c1236ff
- evidence_id: check-gate
  kind: validation
  reference: /private/tmp/aimech-evolution-shake-cohort336-check-gate.json
  accessed_at: '2026-10-15T08:30:28.657372Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: 4903a7817d72856b0d773aa4dec95b9eeeba845021753239b9a11d0ef0c6c77e
- evidence_id: check-vendor
  kind: validation
  reference: /private/tmp/aimech-evolution-shake-cohort336-retry-check-vendor.json
  accessed_at: '2026-10-15T08:33:56.735713Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: 9b250baeefaf841b72e8a7673cf04bdf2d0706c54029f7463ead09180fe9452a
- evidence_id: check-check-source
  kind: validation
  reference: /private/tmp/aimech-evolution-shake-cohort336-check-check-source.json
  accessed_at: '2026-10-15T08:34:18.545801Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: 05d23181ea3164eac5c87d4a232efbb30b00e850f731c8a678b56278f7ec1875
- evidence_id: check-render
  kind: validation
  reference: /private/tmp/aimech-evolution-shake-cohort336-check-render.json
  accessed_at: '2026-10-15T08:19:12.060905Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: a5c684545653ac5e8e7de70788c30ed72e075b96bab35b01440adbc985fe4ad7
- evidence_id: check-render-check
  kind: validation
  reference: /private/tmp/aimech-evolution-shake-cohort336-check-render-check.json
  accessed_at: '2026-10-15T08:34:37.936744Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: 04216d7a0be1002b33c80c6b84ae562039105081fe206990984e83fcf2c22574
- evidence_id: check-diff
  kind: validation
  reference: /private/tmp/aimech-evolution-shake-cohort336-check-diff.json
  accessed_at: '2026-10-15T08:34:39.095080Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: 25d00095e1506e9b18c54481734a6c3fe2456842479be8d5b598083c76b4f607
- evidence_id: historical-check-attempt-1
  kind: validation
  reference: /private/tmp/aimech-evolution-shake-cohort336-check-vendor.json
  accessed_at: '2026-10-15T08:30:29.166551Z'
  support: context_only
  summary: Actual failed attempt retained alongside its later successful required-check
    replacement; failure is not rewritten as a pass.
  snapshot_sha256: 45afa9e62212d0d7cdcb7ee7d21360ab1bd2e8fb5577a3efd0475dbce9abc1b3
assessments:
- assessment_id: regularized-evolution-trained-population-and-architecture-search
  area: evidence
  topic: Claim trained-population-and-architecture-search
  outcome: supported
  summary: The main Methods section and Algorithm 1 explicitly initialize a queue
    with random architectures followed by training/evaluation, while the NASNet section
    separates cell choices from repeated use of those cells. PDF 6 names AmoebaNet-A
    as a selected result. The statement correctly treats trained instances, architecture
    encodings and the outer search algorithm as different objects; it does not introduce
    a specific model instance.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
- assessment_id: regularized-evolution-with-replacement-fitness-tournament
  area: evidence
  topic: Claim with-replacement-fitness-tournament
  outcome: supported
  summary: The prose on PDF 3 explicitly says uniform with-replacement draws and highest
    validation fitness. The parent criterion is therefore stored accuracy, not age,
    despite the broad introductory description. PDF 4 independently defines the baseline
    as independent random architecture generation, supporting the S=1 qualification.
    Repeated samples and unspecified ties remain explicit, rather than silently treating
    the sample as a set.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
- assessment_id: regularized-evolution-whole-population-oldest-removal
  area: evidence
  topic: Claim whole-population-oldest-removal
  outcome: supported
  summary: Algorithm 1 appends the child on the right and removes the leftmost old
    individual. That is removal from the whole queue, not the tournament, and it yields
    P members at completed-update boundaries. The short P+1 transient follows directly
    from the operation order. PDF 2 explicitly contrasts gene-age ALPS. Architecture
    persistence is a boundary of individual-age semantics, not a claim of a new stochastic
    theorem.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
- assessment_id: regularized-evolution-architecture-mutation-and-fresh-evaluation
  area: evidence
  topic: Claim architecture-mutation-and-fresh-evaluation
  outcome: supported
  summary: Figure 3 and its surrounding text separately define connection and operation
    mutations, with a no-cycle constraint on new input connections. Methods Details
    supplies the optional identity mutation and reported P, S and probability, while
    PDF 8 discusses retraining inherited architectures. The statement confines constants
    and NASNet operators to the reported application and distinguishes a new training/evaluation
    call from PBT weight copying; it does not certify unseen code.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
- assessment_id: regularized-evolution-evaluation-history-and-stopping
  area: evidence
  topic: Claim evaluation-history-and-stopping
  outcome: supported
  summary: The displayed initialization inserts every evaluated individual into history
    before the while guard. Therefore C-P later updates under the stated integer C>=P>0
    assumption and return of the best historical score are exact readings of Algorithm
    1. A growing archive of fixed scores has a nondecreasing maximum, but FIFO can
    remove the best live member and noise can alter future retraining. Those elementary
    arguments do not establish optimization or statistical convergence.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
- assessment_id: regularized-evolution-training-noise-motivation-and-empirical-boundary
  area: evidence
  topic: Claim training-noise-motivation-and-empirical-boundary
  outcome: supported
  summary: The official discussion repeatedly calls the training-noise mechanism speculative
    and a conjecture for future verification. Supplement C expressly uses unit-cube
    bit strings with fraction-zero score plus Gaussian noise and labels the evidence
    circumstantial. The claim attributes this motivation and toy test without asserting
    universal regularization, guaranteed extinction, quantitative empirical superiority
    or a theorem about neural network search.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
  - src-real2019-arxiv-v7
- assessment_id: regularized-evolution-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: Algorithm 1 and the paired prose support every defining operation. The
    explicit names in the heading support the one Aging Evolution alias. The definition
    keeps parent selection and removal separate and does not turn this algorithm into
    the discovered AmoebaNet architecture.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
  - src-real2019-arxiv-v7
- assessment_id: regularized-evolution-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: The accepted related-only link reflects mandatory model training/evaluation
    guiding architecture selection. It does not import the pinned preprocessing definition
    as an is-a statement. Thirteen exact AIO contexts were already inspected; output
    network classes, RL comparator and RegularizationLayer are not substituted.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - pinned-aio
- assessment_id: regularized-evolution-source-assessment
  area: provenance
  topic: source assessment
  outcome: supported
  summary: 'Both declared sources are explicitly cited: official AAAI2019 for the
    six core operational/scope claims and arXivv7 Supplement C in the sixth claim.
    The supplement is not an uncited metadata-only source. Acquisition hashes, date
    precision and failed/successful retrievals are retained in exact inputs.'
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
  - src-real2019-arxiv-v7
- assessment_id: regularized-evolution-limitations-assessment
  area: scope
  topic: limitations assessment
  outcome: supported
  summary: All seven source and analytical limitations retain the distinction between
    fixed-score tournaments, sequential FIFO lifetimes and noisy empirical motivation.
    The C/history mismatch, sample-multiset interpretation and S=1 boundary are explicit;
    no concurrency, architecture-extinction or convergence guarantee is claimed.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
  - src-real2019-arxiv-v7
- assessment_id: regularized-evolution-identity
  area: identity
  topic: Concept boundary and actual owner
  outcome: supported
  summary: 'The maintained concept retains its accepted algorithm scope with its exact
    accepted aliases [''Aging Evolution'']. Actual root decisions retain owner 183
    and distinct residuals. The supporting historical identity scope is: The historical
    identity/frontier research supports one named algorithm and optional full-name
    alias under owner 183, not a new leaf or an architecture instance. Future creation
    must use its actual fresh context; no historical search is relabeled as current.'
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - identity-assessment
  - postcapture-reading
- assessment_id: regularized-evolution-limitation-1
  area: scope
  topic: Retained limitation 1
  outcome: supported
  summary: The source distinguishes the search procedure, NASNet search space, resulting
    AmoebaNets and ALPS. The limitation prevents scope expansion from the named original
    method to later variants or model outputs.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
  - src-real2019-arxiv-v7
- assessment_id: regularized-evolution-limitation-2
  area: scope
  topic: Retained limitation 2
  outcome: supported
  summary: Explicit with-replacement prose takes precedence over the set glyph. The
    source leaves score ties and invalid inputs open; preserving those details avoids
    certifying a distinct-set implementation or invented repair.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
  - src-real2019-arxiv-v7
- assessment_id: regularized-evolution-limitation-3
  area: scope
  topic: Retained limitation 3
  outcome: supported
  summary: This is the concrete guard/comment mismatch identified in research. For
    C<P the initialization guard is independent of history, so initialization still
    takes P evaluations. Concurrency overshoot is deliberately unverified.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
  - src-real2019-arxiv-v7
- assessment_id: regularized-evolution-limitation-4
  area: scope
  topic: Retained limitation 4
  outcome: supported
  summary: The paper mentions asynchronous workers without defining full concurrency
    semantics. A FIFO residence argument counts completed sequential updates, not
    seconds, and does not constrain repeated architectural genotypes.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
  - src-real2019-arxiv-v7
- assessment_id: regularized-evolution-limitation-5
  area: scope
  topic: Retained limitation 5
  outcome: supported
  summary: The supporting rank-selection argument shows nonzero selection probability
    even for a low-ranked fixed-score member. Independent coexistence and mutation
    also undermine a literal extinction guarantee; the limitation is consistent with
    the surrounding conjecture language.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
  - src-real2019-arxiv-v7
- assessment_id: regularized-evolution-limitation-6
  area: scope
  topic: Retained limitation 6
  outcome: supported
  summary: S=1 removes the fitness ranking step but leaves conditional mutation and
    population history. Replacement at S=P permits repeated individuals. The source
    does not establish uniformity over quotiented graph classes or trained functions,
    so the encoding qualifier is necessary.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
  - src-real2019-arxiv-v7
- assessment_id: regularized-evolution-limitation-7
  area: scope
  topic: Retained limitation 7
  outcome: supported
  summary: Source identity, visible and machine dates, and the older author-page context
    are individually retained. The stated reading scope is exact and does not promote
    access to complete empirical/implementation validation.
  target_ids:
  - AIMech:RegularizedEvolution
  evidence_ids:
  - record-regularized-evolution
  - scientific-support
  - src-real2019-aaai
  - src-real2019-arxiv-v7
- assessment_id: shake-shake-two-residual-branches-and-skip
  area: evidence
  topic: Claim two-residual-branches-and-skip
  outcome: supported
  summary: The source explicitly distinguishes two learned residual units from the
    skip, and the implementation description qualifies the skip at changes of dimensions.
    This prevents the three-branch title from being misread as three learned residual
    paths or an identity operation at every resolution.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-coupled-uniform-forward-mixture
  area: evidence
  topic: Claim coupled-uniform-forward-mixture
  outcome: supported
  summary: Equation2 gives complementary uniform weights on the two residual outputs.
    The source contrasts the whole-tensor scalar operation with elementwise perturbation
    and binary drop-path. No independent branch weights or added-loss penalty is inferred.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-redrawn-backward-coefficients
  area: evidence
  topic: Claim redrawn-backward-coefficients
  outcome: supported
  summary: The full training paragraph and Figure1 specify overwriting coefficients
    for both passes. Keep is separately defined as reusing forward coefficients, so
    ordinary realized-forward chain-rule behavior cannot be silently imported into
    the fresh-backward configuration. The bounded scalar witness is curator reasoning,
    not a claimed source erratum.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-image-versus-minibatch-sharing
  area: evidence
  topic: Claim image-versus-minibatch-sharing
  outcome: supported
  summary: The explicit tensor slicing example holds one scalar over all channels/spatial
    locations within an image; Batch shares that scalar across images. This evidence
    supports both named sharing conventions without importing later per-pixel versions.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-shake-even-keep-controls
  area: evidence
  topic: Claim shake-even-keep-controls
  outcome: supported
  summary: The source supplies exact meanings for Shake, Even and Keep and uses them
    as controlled settings. Section4 changes coefficient dependence experimentally;
    that discussion supports retaining configurations without forcing extra concept
    identities or pretending every setting is the core redrawn/redrawn rule.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-half-weight-inference
  area: evidence
  topic: Claim half-weight-inference
  outcome: supported
  summary: The test instruction sets each coefficient to its meanonehalf. Direct linearity
    of conditional expectation gives the local statement for fixed branch outputs.
    Equation1 is an unweighted sum, so neither recovery of that baseline nor exact
    nonlinear whole-network ensemble equivalence follows.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: The original core is a training/inference procedure with two learned residual
    branches, complementary random forward weights, deliberately resampled backward
    weights and half-weight inference. The definition names sharing explicitly rather
    than conflating it with architecture or all stochastic regularization.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: Root accepted the single related_match to exact AIO:ResidualNeuralNetwork
    as procedure-to-original-host relatedness. It is not architecture equivalence
    or subclassing. TrainingStrategy was inspected but not selected; penalty-based
    RegularizationLayer and noise/dropout targets do not follow merely from the regularization
    label. The pinned node and incident context were read, without inferring universal
    components for every source variant.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - pinned-aio
- assessment_id: shake-shake-source-assessment
  area: provenance
  topic: source assessment
  outcome: supported
  summary: Fixed v2 primary evidence is declared and used in definition plus all six
    claims. Workshop equation-number correction is separately bound; workshop/v1 are
    not extra uncited sources. Source access is the actual successful 2026-10-15 acquisition,
    with original fractional timestamp and failed first acquisition retained.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-limitations-assessment
  area: scope
  topic: limitations assessment
  outcome: supported
  summary: All six limitations retain the original two-branch scope, deliberately
    redrawn backward rule, bounded hand counterexample, conditional local mean only,
    sharing/version distinctions and empirical limits. The workshop locator correction
    changes historical supporting provenance, not the accepted nativev2 mechanism.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-identity
  area: identity
  topic: Concept boundary and actual owner
  outcome: supported
  summary: 'The maintained concept retains its accepted algorithm scope with its exact
    accepted aliases []. Actual root decisions retain owner 211 and distinct residuals.
    The supporting historical identity scope is: {"identity_notes": "The original
    2017 two-learned-branch forward/backward mixing procedure is retained separately
    from its residual-network host, Bernoulli stochastic depth and cross-example MixUp
    or ManifoldMixup. Shake, Even, Keep and image/minibatch sharing are explicit configurations;
    no aliases are asserted. Historical research at 2026-10-15T07:42:50.033621Z–07:43:08.177461Z
    compared 742 native and 442 pinned AIO records, mechanically normalizing all 4,742
    ID/local-ID/name/alias/scoped-synonym values with no candidate collision. Four
    ignored/hidden-inclusive checkout searches reconstructed all 1,444 occurrences
    into seven fully read exact contents: existing owner211, neighboring owner212
    distinction text and historical FastAutoAugment code-tree inventory. All 65 selected
    definitions, 29 query-selected full frontier objects, three full native neighbors
    and 13 exact AIO contexts were read. This is historical bounded research, not
    a current creation-time absence assertion. Existing owner211 represents the concept;
    owners209 DropPath,212 ShakeDrop and227 Swapout remain separate pending source
    scopes.", "research": {"path": "/private/tmp/aimech-shake-shake-research-20261015/identity/assessment.json",
    "sha256": "a6543d911a6d052b522296eb599947506eed59ab846d563fc2922866ab612f33"},
    "mapping_context": {"path": "/private/tmp/aimech-shake-shake-research-20261015/identity/aio-contexts.json",
    "sha256": "8dbb7437e890c893444908d10369f41bcd7b3370f20109641ca4e6347f417650"}}'
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - identity-assessment
  - postcapture-reading
- assessment_id: shake-shake-limitation-1
  area: scope
  topic: Retained limitation 1
  outcome: supported
  summary: The source-defined original residual host and separately reported architectural
    variants are distinguished. Continuous coupled mixing differs from binary path
    removal, and the same-example residual construction differs from input/target
    mixing across examples.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-limitation-2
  area: scope
  topic: Retained limitation 2
  outcome: supported
  summary: The hand calculation uses the same specified scalar forward loss and independent
    uniform coefficients. E[beta]=1/2, E[alpha]=1/2, E[alpha squared]=1/3 and E[alpha(1-alpha)]=1/6
    give the displayed unequal fields. This is an analytical scope boundary, not an
    executed experiment or failure theorem.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-limitation-3
  area: scope
  topic: Retained limitation 3
  outcome: supported
  summary: The local expectation follows directly from a linear combination at fixed
    inputs. The record does not commute expectation through nonlinear downstream computation
    or conflate same-output branches with identical parameter-gradient allocations.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-limitation-4
  area: scope
  topic: Retained limitation 4
  outcome: supported
  summary: Sharing and pass choices are explicit in the method. Implementation-dependent
    random number generation, endpoint and device behavior remain outside source reading
    because author code was not inspected.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-limitation-5
  area: scope
  topic: Retained limitation 5
  outcome: supported
  summary: The complete source text contains empirical observations and a conclusion
    leaving dynamics for further study. No quantitative benchmark, convergence, decorrelation
    or generalization guarantee is added.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
- assessment_id: shake-shake-limitation-6
  area: scope
  topic: Retained limitation 6
  outcome: supported
  summary: Exact v2 acquisition and submission metadata are retained separately from
    PDF build dates. Earlier workshop and v1 artifacts are provenance context; root
    and supporting reading scopes remain attributed, without asserting author-code
    execution or numerical agreement across editions.
  target_ids:
  - AIMech:ShakeShakeRegularization
  evidence_ids:
  - record-shake-shake
  - scientific-support
  - src-gastaldi2017v2
  - shake-shake-research-locator-correction
- assessment_id: shakedrop-gated-residual-perturbation
  area: evidence
  topic: Claim gated-residual-perturbation
  outcome: supported
  summary: The single learned residual branch plus identity skip is explicit in the
    displayed construction. Scope separates the regularizer from its host and the
    compared two-learned-branch mixing method; it does not claim that every residual
    architecture works equally well.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
- assessment_id: shakedrop-distinct-forward-backward-coefficients
  area: evidence
  topic: Claim distinct-forward-backward-coefficients
  outcome: supported
  summary: Equation (6) uses one b_l in both lines, with alpha and beta separately
    specified. Equations (7)–(8) give the two gate cases. Constant-zero alpha is explicitly
    studied. The statement treats the backward line as a prescribed path derivative
    rule, avoiding a false ordinary-chain-rule interpretation.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
- assessment_id: shakedrop-depth-dependent-switching
  area: evidence
  topic: Claim depth-dependent-switching
  outcome: supported
  summary: The l/L expression is indexed by block depth. The claim bounds p_L and
    does not reinterpret it as temporal annealing or claim one globally optimal value.
    The journal uses different choices for CIFAR, ImageNet and depth experiments.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
- assessment_id: shakedrop-sampling-and-host-settings
  area: evidence
  topic: Claim sampling-and-host-settings
  outcome: supported
  summary: The later Section IV and Table 5 caption support the empirical range/sharing
    choices. The earlier v1 text explicitly chooses Image for memory despite the lower
    Pixel error in Table 2. Both sources are structurally cited, with no version-equivalence
    or numerical benefit claim.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
  - src-yamada2018-v1
- assessment_id: shakedrop-deterministic-test-rule
  area: evidence
  topic: Claim deterministic-test-rule
  outcome: supported
  summary: The test line is printed in Equation (6). The conditional expectation is
    direct Bernoulli algebra, stated only for p_l<1 so the zero-probability event
    at p_l=1 is not used. Independence and zero mean are sufficient for the p_l simplification.
    This does not average the nonlinear network.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
- assessment_id: shakedrop-distinction-and-special-cases
  area: evidence
  topic: Claim distinction-and-special-cases
  outcome: supported
  summary: The special settings agree with the printed RandomDrop relation and Table
    2 cases A/B. With alpha zero and beta positive, forward value suppression differs
    from suppressing both passes; a nonzero derivative is permitted, not guaranteed
    for every loss/Jacobian. Degenerate equality does not collapse identities.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
- assessment_id: shakedrop-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: The definition describes the ordinary/perturbed switch, separately specified
    backward rule and deterministic test coefficient without saying every alpha configuration
    is sampled or imposing a universal positive perturbation.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
  - src-yamada2018-v1
- assessment_id: shakedrop-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: The exact pinned residual-network CLASS supplies the host relation. This
    single related_match is neither equality nor an is_a assertion. The optional TrainingStrategy
    association remains historical context and is absent from the draft, as root requested.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - pinned-aio
- assessment_id: shakedrop-source-assessment
  area: provenance
  topic: source assessment
  outcome: supported
  summary: The retained2019author proof and original2018v1 are both explicitly cited.
    They differ in coefficient sharing defaults and TypeA/B names; PDF build and acquisition
    times are not publication dates. The proof is not silently equated to the final
    publisher PDF or arXivv3. Historical acquisition failures and exact source hashes
    remain in the bound inputs.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
  - src-yamada2018-v1
- assessment_id: shakedrop-limitations-assessment
  area: scope
  topic: limitations assessment
  outcome: supported
  summary: All seven limitations retain prescribed-versus-chain-rule differentiation,
    the conditional-zero-mean test coefficient, local-versus-network expectation,
    heuristic stability explanations, version-specific settings, same-gate semantics
    and bounded empirical/implementation scope. The accepted successor corrects only
    the independence-alone wording in limitation2; original bytes and root acceptance
    lineage remain explicit.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
  - src-yamada2018-v1
- assessment_id: shakedrop-identity
  area: identity
  topic: Concept boundary and actual owner
  outcome: supported
  summary: 'The maintained concept retains its accepted algorithm scope with its exact
    accepted aliases []. Actual root decisions retain owner 212 and distinct residuals.
    The supporting historical identity scope is: This record denotes the named ShakeDrop
    residual-network regularization procedure, not a particular trained network, the
    two-residual-branch Shake-Shake procedure, stochastic depth, DropBlock, Zoneout
    or the intermediate single-branch Shake construction. Coefficient and sharing
    configurations are not separately named native identities here. The accepted historical
    research snapshot contained 742 native and 442 pinned AIO records; normalized
    IDs, names, aliases and scoped synonyms had no queried collision. Four whole-checkout
    searches included ignored and hidden files and returned 714 occurrences reconstructed
    into one pending-label content. A bounded static check of 196 top-level TEMP content
    modules found no identity match. Research mechanically traversed all 908 main
    and 393 nested frontier objects and read 41 selected full objects, 54 semantic
    definitions, three full native neighbors and 13 exact AIO CLASS contexts with
    53 incident-edge rows. Existing owner 212 belongs to this concept; owner 211 remains
    the distinct Shake-Shake lead. The old owner source pointer is historical discovery
    context, while the acquired primary evidence is identified explicitly. These historical
    findings do not assert a fresh future creation-time absence, global completeness
    or saturation. The optional qualified TrainingStrategy association was inspected
    but is not needed in addition to the residual-host mapping accepted here.'
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - identity-assessment
  - postcapture-reading
- assessment_id: shakedrop-limitation-1
  area: scope
  topic: Retained limitation 1
  outcome: supported
  summary: The source supplies a prescribed backward multiplier. The scalar hand witness
    distinguishes it from the derivative of an expected randomized loss, while the
    ratio qualification avoids confusing a relative ratio with an absolute-gradient
    bound. Negative-alpha sign comparison is scoped to the same realized forward computation.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
  - src-yamada2018-v1
- assessment_id: shakedrop-limitation-2
  area: scope
  topic: Retained limitation 2
  outcome: supported
  summary: Expectation is local and conditioned correctly. Subsequent nonlinear operations
    and stateful normalization prevent a generic whole-network average interpretation.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
  - src-yamada2018-v1
  - shakedrop-precuration-wording-correction
- assessment_id: shakedrop-limitation-3
  area: scope
  topic: Retained limitation 3
  outcome: supported
  summary: Conceptual trajectories and empirical settings are not a general theorem.
    Probability and shape conditions are elementary requirements, not an asserted
    implementation safeguard.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
  - src-yamada2018-v1
- assessment_id: shakedrop-limitation-4
  area: scope
  topic: Retained limitation 4
  outcome: supported
  summary: The Image-versus-Pixel choice and reversed A/B letters are directly visible
    source-version differences. The draft preserves the actual before/after-sum distinction
    instead of silently unifying letters.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
  - src-yamada2018-v1
- assessment_id: shakedrop-limitation-5
  area: scope
  topic: Retained limitation 5
  outcome: supported
  summary: Same-gate use is literal. Zero local loss-gradient is narrower than unchanged
    parameters under a full optimizer, and alpha zero does not force the prescribed
    beta path to vanish. No author implementation was audited.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
  - src-yamada2018-v1
- assessment_id: shakedrop-limitation-6
  area: scope
  topic: Retained limitation 6
  outcome: supported
  summary: Publication, build and acquisition times are distinct. The local-page author
    proof remains precisely identified; workshop and later full-text versions are
    not silently substituted.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
  - src-yamada2018-v1
- assessment_id: shakedrop-limitation-7
  area: scope
  topic: Retained limitation 7
  outcome: supported
  summary: The claim set contains no performance-kind claim or new numerical comparison.
    The stated source/visual scope and absence of code, training and benchmark execution
    are accurate.
  target_ids:
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - record-shakedrop
  - scientific-support
  - src-yamada2019
  - src-yamada2018-v1
- assessment_id: actual-correspondence
  area: consistency
  topic: Captured bytes, accepted science and frontier accounting
  outcome: supported
  summary: All three captured records equal the actual write payloads and report entries.
    Exact support covers18 claims and20 limitations. Only owners183/211/212 changed;
    all905 other main and393 nested values remain unchanged. Six required checks passed.
    No global exhaustion or DRAFT promotion is inferred.
  target_ids:
  - AIMech:RegularizedEvolution
  - AIMech:ShakeShakeRegularization
  - AIMech:ShakeDropRegularization
  evidence_ids:
  - captured-inputs
  - postcapture-reading
  - discovery-report
  - creation-history
  - shake-shake-research-locator-correction
  - shakedrop-precuration-wording-correction
  - check-gate
  - check-vendor
  - check-check-source
  - check-render
  - check-render-check
  - check-diff
findings: []
actions: []
notes:
- 'The accepted science is unchanged apart from explicitly declared current identity
  notes and timestamps. The three DRAFT algorithm identities and related mappings
  are supported with bounded claims: oldest-individual regularized evolution, separate
  Shake-Shake forward/backward draws, and shared-gate ShakeDrop coefficients with
  conditional-zero-mean qualification. All individual limitation assessments and pre-curation
  workshop-locator/ShakeDrop wording corrections were read and retained. Actual captured
  hashes and report mirrors match. Six required checks passed, including247 tests
  with3 skips; the failed DNS vendor attempt remains alongside its successful retry.
  No additional required finding was identified. This is author scientific review
  with supporting agents, not independent approval or global discovery exhaustion.'
```
