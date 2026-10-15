# Scientific self-review of replacing traces, Watkins hard-cut learning and stochastic local search

- Review: 20261015T145952Z-replacing-traces-watkins-hard-cut-and-stochastic-local-search
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-15T14:47:02.854323Z
- Finished UTC: 2026-10-15T14:59:52.329386Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The explicitly selected heterogeneous cohort is assessed through 16 source-linked claims, 21 individual limitations and four declared source rows. Retain a replacing eligibility component, the original Watkins hard-cut forward/delayed control construction and the stochastic local-search family separately. The first two retain qualified related ReinforcementLearning mappings; SLS retains eight examined no-match targets. All records remain DRAFT. This review binds actual creation, canonical capture, postcapture root assessment and six completed required checks; its conclusions are limited to those bytes and stated reading scopes.

## Scope And Provenance

Complete explicitly selected heterogeneous cohort: a credit-memory component, a source-scoped control procedure and a configurable combinatorial search family. A shared review does not assert a common algorithm identity.

Selection: Exact maintained IDs AIMech:ReplacingEligibilityTraces, AIMech:WatkinsHardCutMultistepQLearning, AIMech:StochasticLocalSearch from actual cohort343 creation.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 73729051e58d582f36c9af9296a92b393be0a679.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ReplacingEligibilityTraces | data/curated/ReplacingEligibilityTraces.yaml | maintained | Replacing eligibility traces |
| AIMech:WatkinsHardCutMultistepQLearning | data/curated/WatkinsHardCutMultistepQLearning.yaml | maintained | Watkins hard-cut multistep Q-learning |
| AIMech:StochasticLocalSearch | data/curated/StochasticLocalSearch.yaml | maintained | Stochastic local search |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:ReplacingEligibilityTraces, AIMech:WatkinsHardCutMultistepQLearning, AIMech:StochasticLocalSearch | Actual command completed with exit0; exact output is retained. |
| just vendored-check | passed | True | AIMech:ReplacingEligibilityTraces, AIMech:WatkinsHardCutMultistepQLearning, AIMech:StochasticLocalSearch | Actual command completed with exit0; exact output is retained. |
| uv run --locked aimech check-source | passed | True | AIMech:ReplacingEligibilityTraces, AIMech:WatkinsHardCutMultistepQLearning, AIMech:StochasticLocalSearch | Actual command completed with exit0; exact output is retained. |
| just render | passed | True | AIMech:ReplacingEligibilityTraces, AIMech:WatkinsHardCutMultistepQLearning, AIMech:StochasticLocalSearch | Actual command completed with exit0; exact output is retained. |
| just render-check | passed | True | AIMech:ReplacingEligibilityTraces, AIMech:WatkinsHardCutMultistepQLearning, AIMech:StochasticLocalSearch | Actual command completed with exit0; exact output is retained. |
| git diff --check | passed | True | AIMech:ReplacingEligibilityTraces, AIMech:WatkinsHardCutMultistepQLearning, AIMech:StochasticLocalSearch | Actual command completed with exit0; exact output is retained. |

## Scientific And Domain Assessments

### Claim state-replacing-recurrence

evidence: supported. Targets: AIMech:ReplacingEligibilityTraces.

Fresh PDF pp. 2–3 text/visual confirms reset-to-one for the current state and q times the old trace for other states. The accumulating comparator and closed gamma/lambda intervals are literal; replacing does not mean add then clip an arbitrary trace.

### Claim trace-as-td-credit-component

evidence: supported. Targets: AIMech:ReplacingEligibilityTraces.

Fresh PDF pp. 3–4 confirms gamma=1, absorbing terminal value 0, and DeltaV using the newly formed e_(t+1) with the same-time value estimates. This is a prediction-credit component, not an action selector or full controller.

### Claim bounded-recency-with-endpoints

evidence: supported. Targets: AIMech:ReplacingEligibilityTraces.

Hand induction: reset to 1 and multiplication by q in [0,1] preserve the stated trace interval. k inactive updates give q^k times the prior value; q=0 clears after one inactive update and q=1 retains it. This says nothing about bounds on TD errors or parameter updates.

### Claim qualified-first-visit-correspondence

evidence: supported. Targets: AIMech:ReplacingEligibilityTraces.

Fresh PDF pp. 7–8 confirms a repeated-batch limit and a different completed-trial offline identity. For N(s)&gt;0 and 0&lt;alpha&lt;1/N, the batch error multiplier 1-alpha*N(s) is strictly between 0 and 1; the limiting estimate is the first-visit mean. Offline schedule 1/i gives V_i=V_(i-1)+(R_i-V_(i-1))/i. No arbitrary online finite-step equality is inferred.

### Claim binary-feature-control-realization

evidence: supported. Targets: AIMech:ReplacingEligibilityTraces.

Fresh Figure 9 and PDF pp. 21–22 confirm decay, then active chosen-action traces to 1 and corresponding active other-action traces to 0, before environment/reward and later scalar TD update. The alternative pair-only replacement is explicitly separate; clearing other actions at active features is not a hard cut of every preceding trace.

### definition assessment

evidence: supported. Targets: AIMech:ReplacingEligibilityTraces.

The recurrence is a mathematical credit-memory component. Source behavior does not supply a complete policy/controller; qualified related RL mapping preserves that boundary.

### mapping assessment

grounding: supported. Targets: AIMech:ReplacingEligibilityTraces.

One qualified related ReinforcementLearning mapping follows root acceptance. The pinned target is a learning task, not the recurrence or a guarantee. MathematicalFunction is a defensible optional relation for the concrete rule and is not rejected as scalar-only; it is omitted as unnecessary. Geometric decay does not force ExponentialFunction, and trace recurrence is not neural architecture.

### source assessment

provenance: supported. Targets: AIMech:ReplacingEligibilityTraces.

Only singh-sutton1996 is declared and cited. Author prepublication layout, published 1996 metadata, raw fractional access, failed acquisition and whole-second native projection remain separate; all local locators use author PDF pages.

### limitations assessment

scope: supported. Targets: AIMech:ReplacingEligibilityTraces.

All seven limitations have individual source or hand-boundary explanations. The source’s algorithm/pseudocode and experiment-environment ambiguities are explicit without an executable repair or author-code defect claim.

### Concept boundary and actual owner

identity: supported. Targets: AIMech:ReplacingEligibilityTraces.

The maintained concept retains its accepted mathematical_method scope with its exact accepted aliases []. Actual root decisions retain owner 264 and distinct residuals. The supporting historical identity scope is: Historical 757 native / 442 AIO identity snapshot only, with complete retained four-root phrase and eligibility passes. Owner 264 is reused; generic/true-online residuals remain. No future merged-base absence is asserted.

### Retained limitation 1

scope: supported. Targets: AIMech:ReplacingEligibilityTraces.

Component-versus-control distinction is supported by the recurrence and its distinct prediction/control uses. Historical priority is not re-established; general trace-family and true-online residuals are retained.

### Retained limitation 2

scope: supported. Targets: AIMech:ReplacingEligibilityTraces.

Trace boundedness requires both initialization and multiplier bounds. It neither bounds rewards/step sizes nor gives return existence at gamma=1 or learning convergence.

### Retained limitation 3

scope: supported. Targets: AIMech:ReplacingEligibilityTraces.

Fresh batch/offline proof passages support the schedule distinctions and positive-alpha qualification. Fresh visual p. 15 confirms non-strict inequalities and equality cases. The appendix proof itself is not certified.

### Retained limitation 4

scope: supported. Targets: AIMech:ReplacingEligibilityTraces.

PDF pp. 21–22 and Note 6 on p. 35 support the selected binary-feature realization, pair-only alternative and nonstationary-policy limitation. No arbitrary neural-network or off-policy convergence claim is added.

### Retained limitation 5

scope: supported. Targets: AIMech:ReplacingEligibilityTraces.

Fresh visual Figure 9 has traces initialized in step 1 and episode-end return to step 2; Note 3 continuing indices do not settle an all-trace reset. The unresolved printed convention remains explicit without asserting author-code failure.

### Retained limitation 6

scope: supported. Targets: AIMech:ReplacingEligibilityTraces.

Fresh Appendix B text/visual pp. 34–35 confirms clipping to 0.5 followed by the printed strict &gt;0.5 condition, and minus-g with negative g. Literal post-clipping testing cannot pass; no experimental implementation or repaired dynamics are inferred.

### Retained limitation 7

scope: supported. Targets: AIMech:ReplacingEligibilityTraces.

Exact accepted author-PDF hash and metadata are preserved. Selective OCR and visuals do not establish full source/proof/software/benchmark reproduction.

### Claim action-values-and-implicit-greedy-policy

evidence: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Fresh PDF pp. 102–103 confirms maximum state values, an implicit maximizing policy and separate unspecified behavior selection. Ties are possible and are retained as a convention gap; an exploration branch label alone does not identify a non-policy action.

### Claim hard-cut-forward-return

evidence: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Fresh PDF pp. 100–102 and visual p. 101 confirm lambda_t from action at t but lambda_(t+1) in R_t recursion, with the displayed bootstrap U_t(s_(t+1)). Visual p. 104 reuses the hard-cut rule for action values and separately introduces the soft alternative. The following U_(t+1) prose is not silently substituted.

### Claim cut-boundary-and-experimental-action-credit

evidence: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Hand substitution lambda_(t+1)=0 leaves r_t+gamma*U_t(s_(t+1)), retaining the bootstrap but removing R_(t+1), including the reward generated by the next non-policy action. By contrast lambda_t affects prior returns, not whether the current experimental action receives its own action-value estimate. This statement concerns propagation through the displayed return recursion, not all indirect future changes in learned values.

### Claim delayed-action-value-update

evidence: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Visual p. 104 has Q_(t+T+1)=(1-alpha)Q_(t+T)+alpha*R_t at the earlier visited pair; current update-time value is correct. The source separately discusses incremental prediction differences and changing-estimate effects. The claim is conditional on an estimate being available, not a promise of exact finite-delay observability of an infinite return.

### Claim one-step-and-unit-continuation-boundaries

evidence: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Fresh PDF p. 95 constant-lambda endpoints combined with PDF pp. 101 and 104 hard cuts supports the scoped limits: lambda_star=0 gives the one-step target; lambda_star=1 still cuts at a subsequent non-policy action. Target equality does not force the same delayed/online trajectory.

### definition assessment

evidence: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

The selected identity is an algorithm for policy-cut action-return estimation with delayed action-value updating; its definition does not replace the original construction with a modern trace-loop alias. Qualified related RL is appropriate.

### mapping assessment

grounding: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Qualified related_match to the ReinforcementLearning task only; neither exact identity nor an algorithm-class hierarchy. Optional soft exponential machinery does not justify an additional required-component relation.

### source assessment

provenance: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Only the original thesis is declared as a native evidence source, and it is cited by every claim and the definition. Rummery/Peng/Watkins–Dayan comparisons remain historical research context; no unsupported native comparative theorem is added.

### limitations assessment

scope: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

All seven limits individually assessed. Source timing/corrigenda and proof boundaries are intrinsic evidence qualifications, not fabricated canonical findings.

### Concept boundary and actual owner

identity: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

The maintained concept retains its accepted algorithm scope with its exact accepted aliases []. Actual root decisions retain owner 264 and distinct residuals. The supporting historical identity scope is: This record selects the original 1989 hard-cut forward-return and delayed action-value construction. It is distinct from the maintained one-step Q-learning and Sarsa records, the neural selected-action MCQ-L procedure, Peng–Williams two-error propagation, and replacing eligibility as a component. Shared one-step targets or greedy special cases do not equate complete timing and credit policies. The source’s soft-cut alternative and other eligibility variants remain separate scope. Research on 15 October 2026 at 13:56:54–13:57:06 UTC compared 760 native and 442 pinned AIO records using Watkins-specific identity probes. Four ignored- and hidden-inclusive checkout scans returned 177, 179, 515 and 557 occurrences, reconstructed into 12 exact contents, all read. All string values and keys in 909 main and 393 nested frontier objects were queried, with six relevant objects read in full. Fourteen exact AIO nodes and 59 incident-edge entries were assessed. The native identifier was selected after that historical research; these observations do not assert absence beyond its inspected snapshot and contexts. The broader eligibility-trace context retains other components and control variants; Full-echo Q-routing is a separate method.

### Retained limitation 1

scope: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Hard-cut return/control procedure is distinct from replacing credit memory and the source soft exponential continuation. MCQ-L/Peng comparisons retain the already accepted historical scopes; no fresh complete rereading of those separate sources is claimed.

### Retained limitation 2

scope: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Fresh PDF p. 92 states bounded rewards and gamma&lt;1 for tail control. The draft does not extend this to continuing undiscounted or arbitrary approximation; lambda_star=1 retains hard cuts and supplies no convergence result.

### Retained limitation 3

scope: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Fresh visual p. 101 independently confirms the literal U_t display versus U_(t+1) prose. Keeping both observations is accurate; an executable convention remains unresolved rather than repaired.

### Retained limitation 4

scope: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Fresh initial corrigenda pp. 5–6 and original pp. 97–98 show the changing-value correction terms and C(x,t)/C(x,t+1) discrepancy. Small-alpha prose is not a uniform horizon error bound or exact true-online equivalence; no such claim appears in the draft.

### Retained limitation 5

scope: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Fresh PDF p. 100 assumes a unique policy action while p. 102 defines a maximizing action without a tie rule. The selected passages do not fully specify exploration, terminal/reset and initialization conventions. The caveat is properly local to this construction, not absence from all later literature.

### Retained limitation 6

scope: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Fresh PDF p. 105 explicitly states no general proof for this multistep family and explains possible policy/value instability. The one-step proof claim on p. 103 cannot be promoted to this family; no modern nonexistence claim is made.

### Retained limitation 7

scope: supported. Targets: AIMech:WatkinsHardCutMultistepQLearning.

Exact Cambridge scan hash and accepted publication/access metadata are preserved. Current audit did not redownload the source or freshly verify external catalog dates, and does not certify all 241 pages, appendix proofs, software or performance.

### Claim neighborhood-search-framework

evidence: supported. Targets: AIMech:StochasticLocalSearch.

The thesis lists the five underlying search components. The later author exposition expressly adds memory and stopping. The claim distinguishes these source roles instead of retroactively attributing the seven-component form to the 1998 list. A preparation-only wording correction distinguishes a termination predicate as a framework component from position and memory as the search state.

### Claim randomized-and-deterministic-decisions

evidence: supported. Targets: AIMech:StochasticLocalSearch.

The chapter explicitly models deterministic decisions with degenerate distributions. No uniformity, independence or mandatory random branch is inferred from the word stochastic.

### Claim guidance-memory-and-nonimproving-moves

evidence: supported. Targets: AIMech:StochasticLocalSearch.

The chapter states that evaluation may differ from the objective or change during search, includes memory, and explicitly describes worsening acceptance. Strict iterative improvement is separately identified, so the family is not collapsed into HillClimbing.

### Claim constructive-perturbative-and-population-positions

evidence: supported. Targets: AIMech:StochasticLocalSearch.

The thesis permits positions beyond complete candidates; the chapter explicitly constructs partial-solution neighborhoods and set-valued population positions. The final sentence is an identity boundary, not a claim that the members share identical transitions.

### Claim termination-and-best-encountered-solution

evidence: supported. Targets: AIMech:StochasticLocalSearch.

The working-principle passage supplies the stop and return conventions. The claim adds the explicit existence condition for a feasible incumbent and does not turn the solution-set definition into a global optimality certificate.

### Claim family-and-search-control-boundary

evidence: supported. Targets: AIMech:StochasticLocalSearch.

The chapter directly contrasts SLS with metaheuristic and gives non-equivalence examples. The thesis distinguishes local strategies from higher control and introduces GLSM as a representation; no unread GLSM theorem or universal equivalence is claimed.

### definition assessment

evidence: supported. Targets: AIMech:StochasticLocalSearch.

The thesis establishes the underlying neighborhood-search procedure; the later author exposition supplies memory, stopping and deterministic special cases. The definition identifies a configurable combinatorial family, not a complete fixed transition kernel.

### mapping assessment

grounding: supported. Targets: AIMech:StochasticLocalSearch.

Eight candidate AIO classes were inspected with all incident edges. Training/learning or LLM scope is not mandatory; Markov state augmentation and arbitrary function representation do not supply an informative match for the whole family. MathematicalFunction is not rejected as scalar-only.

### source assessment

provenance: supported. Targets: AIMech:StochasticLocalSearch.

The 1998 author dissertation supplies the underlying formalism; the 2015 author-hosted chapter supplies memory, stopping and deterministic-case exposition. Both native source rows are cited. The later chapter does not establish invention priority. The ILS discovery pointer remains context, not a declared native source. Publication, raw access time, native whole-second projection and selective reading are separately retained.

### limitations assessment

scope: supported. Targets: AIMech:StochasticLocalSearch.

All seven limitations retain configurable-instance requirements, the feasible-incumbent condition, nonmonotone current positions, absence of automatic reachability or termination, augmented-state qualifications, family/member distinctions and selective source-reading limits.

### Concept boundary and actual owner

identity: supported. Targets: AIMech:StochasticLocalSearch.

The maintained concept retains its accepted algorithm scope with its exact accepted aliases []. Actual root decisions retain owner 270 and distinct residuals. The supporting historical identity scope is: This record selects the named combinatorial Stochastic local search family, not every informal use of local search or an exact alias of HillClimbing, IteratedLocalSearch, TabuSearch, SimulatedAnnealing, VariableNeighborhoodSearch or the GLSM control representation. The historical identity snapshot on 15 October 2026 at 13:57:30–13:57:45 UTC contained 760 native records and 442 pinned AIO records. Four ignored- and hidden-inclusive scans produced 14,722 occurrences in 529 exact contents; the supporting research assessed 359 decoded contexts, including 29 exact contexts previously read in a separately retained assessment. Mechanical identity normalization found no candidate collision within that snapshot. Recursive matching covered all 909 main and 393 nested frontier objects, with relevant full rows assessed separately. Existing owner 270 carries the 2001 ILS pointer as historical discovery context; its prior HillClimbing progress remains distinct. The 1998 thesis and 2015 overview supply the present family definition. Guided/Fast Local Search, Gu’s SAT method, continuous or terminological variants and detailed GLSM organization remain separate residual contexts. This dated assessment is not a claim of absence at a later merged base; the subsequently added VNS record is a distinct named method, not an uninspected exact synonym.

### Retained limitation 1

scope: supported. Targets: AIMech:StochasticLocalSearch.

The chapter acknowledges the common perturbative use of the bare term. The historical ILS pointer uses LocalSearch as a flexible embedded routine; that context does not broaden the native definition to every optimizer. Continuous and full GLSM variants remain residual.

### Retained limitation 2

scope: supported. Targets: AIMech:StochasticLocalSearch.

The listed components are parameters of a family, not supplied instance code. An empty feasible-incumbent set has no best feasible member; an implementation needs its own failure convention. No implementation has been inspected or repaired.

### Retained limitation 3

scope: supported. Targets: AIMech:StochasticLocalSearch.

Elementary bookkeeping: for a fixed consistently evaluated minimization objective, the minimum over encountered feasible candidates cannot increase as that set grows. This does not constrain the current point or a changing guidance function.

### Retained limitation 4

scope: supported. Targets: AIMech:StochasticLocalSearch.

The research hand example has states a,b,c, solution c, deterministic moves a→b→a and initialization at a, so the allowed framework need not reach a solution or terminate under success-only stopping. This is a scoped counterexample, not a theorem about every instance.

### Retained limitation 5

scope: supported. Targets: AIMech:StochasticLocalSearch.

Memory-dependent transitions can differ at the same position. Augmenting the state with all relevant memory and time removes that particular omission, without implying homogeneous transitions, stationarity, reversibility or a specified target law.

### Retained limitation 6

scope: supported. Targets: AIMech:StochasticLocalSearch.

Shared formal representability does not make named methods aliases. The chapter’s constructive/population and metaheuristic discussion supports retaining each narrower mechanism and the accepted family identity separately.

### Retained limitation 7

scope: supported. Targets: AIMech:StochasticLocalSearch.

Exact source genres, years, actual file versions and selective reading are retained. The original author thesis and later scholarly exposition serve different roles; neither the unread book nor uninspected empirical/proof/software material is certified.

### Captured bytes, accepted science and frontier accounting

consistency: supported. Targets: AIMech:ReplacingEligibilityTraces, AIMech:WatkinsHardCutMultistepQLearning, AIMech:StochasticLocalSearch.

All three captured records equal the actual write payloads and report entries. Exact support covers 16 claims and 21 limitations. Only existing owners 264 and 270 changed; all 907 other prior main and 393 nested values remain unchanged. All three accepted method scopes reuse their existing owners, with no appended leaf. Six required checks passed. No global exhaustion or DRAFT promotion is inferred.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:ReplacingEligibilityTraces. Retain one source-scoped replacing component. Existing accumulating-TD coverage, one-step Sarsa, MCQ-L/Peng whole methods, generic eligibility and true-online variants are not exact aliases or implicitly completed. Actual owner resolution and residuals are bound separately by the current collection and root decisions.
- retain: AIMech:WatkinsHardCutMultistepQLearning. Retain the original hard-cut forward/delayed control method separately from replacing credit memory. Both reuse existing owner 264 with generic, true-online and soft-cut residuals preserved. Owner 267 Full-echo Q-routing remains untouched. Actual owner resolution and residuals are bound by the current collection and root decisions.
- retain: AIMech:StochasticLocalSearch. Retain the stochastic local-search family under existing owner 270, preserving prior HillClimbing progress and separate named methods. No aliases or new frontier leaf are added; continuous, terminological and GLSM residual work remains separate. Actual owner resolution and residuals are bound by the current collection and root decisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| captured-inputs | /private/tmp/aimech-traces-local-search-cohort343-capture.json | context_only | Actual canonical inspect output; all captured input hashes rechecked. Inspection alone is not scientific approval. |
| postcapture-reading | /private/tmp/aimech-cohort343-root-postcapture-reading.json | context_only | Actual root full-target assessment after capture and completed checks; selective primary scopes are stated separately. |
| scientific-support | /private/tmp/aimech-traces-local-search-cohort343-review-preparation-20261015/scientific-support.readable.structure.json | context_only | Attributed same-author support of all 16 accepted claims and 21 individual limitations. This is preparation DATA, not itself an actual canonical capture. |
| actual-write | /private/tmp/aimech-traces-local-search-cohort343-write.json | context_only | Actual creation receipt binds three records, report pair and CREATE history. |
| discovery-report | research/discovery/20261015T144547Z-replacing-traces-watkins-and-stochastic-local-search.json | context_only | Record mirrors are exact. Only existing owners 264 and 270 changed; all 907 other prior main and 393 nested objects are unchanged. The two trace targets share existing owner 264; SLS reuses owner 270 with prior HillClimbing context preserved; no new frontier leaf was appended. |
| creation-history | history/reports/replacing-traces-watkins-and-stochastic-local-search/2026-10-15T144602Z-codex-a9e723.yaml | context_only | Actual append-only CREATE sidecar; review and publication are separate later actions. |
| pinned-aio | sources/aio/aio.json; Exact AIO:ReinforcementLearning plus all eight accepted SLS rejected targets and retained incident-edge contexts. Positive mapping directions and no-match reasons retain their distinct meanings. | context_only | Exact snapshot supports two qualified related ReinforcementLearning mappings and one explicit eight-target SLS no-match assessment; no upstream equivalence or subclass assertion. |
| identity-assessment | /private/tmp/aimech-cohort343-root-decisions-20261015.json | context_only | Actual root decisions bind fresh ignored/hidden-inclusive scans and existing owners 264/270, including any explicitly assessed context-only matches; no manual rereading of every hit by this generator is claimed. |
| replacing-preparation-spacing | /private/tmp/aimech-replacing-traces-draft-preparation-20261015/finalization.json; Finalization and referenced four support-comment spacing changes, retained preimages and exact differences. | context_only | Preparation-only spacing refinement left the native scientific module unchanged. The historical receipt predates the separately retained successful native preview. |
| sls-framework-wording | /private/tmp/aimech-stochastic-local-search-draft-preparation-20261015/preparation-refinement.json; Single claim-1 framework-versus-state wording correction, with exact module/support/input preimages and differences. | context_only | Before invocation and root acceptance, the termination predicate was described as a framework component rather than an element of the search state. Other record fields were unchanged; no canonical defect is asserted. |
| src-singh-sutton1996 | https://web.eecs.umich.edu/~baveja/Papers/Replace.pdf; Source agent read all 36 OCR pages and visual pages 2, 3, 7, 8, 15, 20, 34, 35. Root’s distinct partial and supplemental scopes are in the accepted reading receipts. Appendix OCR reading does not certify all proofs; no author software was inspected. Later separate supporting trace-pair audit refreshed OCR pp. 2–4, 7–8, 15, 20–22, 34–35 and visuals 2, 3, 7, 8, 15, 20, 34, 35. Historical root/source-agent scopes remain separate from the actual runtime root postcapture scope. | supports | 36-page author-hosted prepublication layout associated with Machine Learning 22, 123–158, March 1996. Official publisher metadata verifies the published counterpart; no publication day or byte identity with journal typesetting is inferred. Author cover dates and provisional pagination remain distinct from published metadata. Acquisition time is access metadata, not a claim of full reading. |
| src-watkins1989 | https://www.repository.cam.ac.uk/bitstreams/2ad45009-0e4b-496e-bd52-cd8f98a3f4d0/download; Original supporting researcher: OCR PDF pp. 1–5, 88–109, 119–120; visuals pp. 5–8, 97–98, 101, 104. Root: OCR pp. 5, 96–98, 101–105; visuals pp. 5, 101, 104. These are separately attributed selected scopes, not all 241 pages or complete proofs. The later separate supporting trace-pair audit refreshed OCR pp. 88–105 and visuals pp. 5, 6, 98, 101, 104. It does not certify the whole thesis or original convergence proofs; runtime root postcapture reading is separate. | supports | PhD thesis submitted at King’s College, University of Cambridge, cover dated May 1989. The retained 241-page Cambridge repository scan includes two initial corrigenda pages. The repository separately records 1989-05-10, while the preface is dated May 1; no exact cover publication day is inferred. PDF build metadata is dated 2006-04-06 and the response Last-Modified is 2026-07-10, neither a publication date. Local PDF and printed page locators are both supplied. Acquisition time is access metadata, not a claim of full reading. |
| src-hoos1998 | https://www.cs.ubc.ca/~hoos/ps/phd-thesis.pdf; Original research agent: native PDF pp. 15–17 and 59–65, visuals pp. 59–61. Root: native pp. 59–61 and visual p. 60. Draft preparation: native pp. 59–61 and visuals pp. 59–61. None is a full 224-page reading or GLSM proof certification. | supports | Author-hosted Darmstadt doctoral dissertation, 1998; title page records submission on 30 September 1998 and defense on 11 November 1998. The acquired file has 224 physical PDF pages; the author index describes 218 pages. Locators distinguish physical PDF from printed pages. This is the thesis, not a later book edition. Acquisition time is access metadata, not a claim of full reading. |
| src-hoos-stutzle2015 | https://ada.liacs.nl/papers/HooStu15b.pdf; Original research agent: native PDF pp. 1–6, visuals pp. 3–4. Root: native pp. 2–5 and visual p. 3. Draft preparation: native pp. 2–5 and visuals pp. 3–4. The 21-page overview is used as author exposition, not priority evidence. | supports | Author-hosted scholarly handbook chapter 54, 2015, printed pp. 1085–1105, in a 21-page PDF. Institutional metadata gives January 2015 without a publication day. Used as the authors’ framework exposition, not as an invention-priority claim or evidence of having read the book cited by the chapter. Acquisition time is access metadata, not a claim of full reading. |
| record-replacing | data/curated/ReplacingEligibilityTraces.yaml | supports | Complete maintained DRAFT record assessed by root after capture and matched to accepted scientific support. |
| preview-acceptance-replacing | /private/tmp/aimech-replacing-traces-draft-preparation-20261015/root-preview-acceptance.json | context_only | Root read complete static draft and all support narratives before invocation. Current preview compared field-for-field to the root-read AST literal, identity/source metadata and snapshot; actual curation metadata and successful native validation receipt were separately inspected. This is comparison-based review, not a second verbatim full-preview reading. Fresh creation-base identity reconciliation and adversarial source audit remain separate. Historical TEMP acceptance is separate from the actual postcapture review; no independent approval. |
| supporting-context-replacing | /private/tmp/aimech-trace-pair-supporting-audit-20261015/assessment.json | context_only | Separate same-author supporting audit: all ten trace-pair claims and fourteen limitations assessed. Fresh Watkins OCR PDF pp. 88–105 and visuals 5, 6, 98, 101, 104; fresh Singh–Sutton OCR pp. 2–4, 7–8, 15, 20–22, 34–35 and visuals 2, 3, 7, 8, 15, 20, 34, 35. No source-wide proof certification, code, calculator or native invocation. |
| record-watkins | data/curated/WatkinsHardCutMultistepQLearning.yaml | supports | Complete maintained DRAFT record assessed by root after capture and matched to accepted scientific support. |
| preview-acceptance-watkins | /private/tmp/aimech-watkins-hard-cut-draft-preparation-20261015/root-preview-acceptance.json | context_only | Exact semantic comparison of actual native preview with the complete root-read static module, all inputs and all five claim/seven limitation support rows passed; no second verbatim reading of the same scientific prose is claimed. Native schema returned no errors. Accepted bounded draft, not canonical or fresh-base identity clearance. Historical TEMP acceptance is separate from the actual postcapture review; no independent approval. |
| supporting-context-watkins | /private/tmp/aimech-trace-pair-supporting-audit-20261015/assessment.json | context_only | Separate same-author supporting audit: all ten trace-pair claims and fourteen limitations assessed. Fresh Watkins OCR PDF pp. 88–105 and visuals 5, 6, 98, 101, 104; fresh Singh–Sutton OCR pp. 2–4, 7–8, 15, 20–22, 34–35 and visuals 2, 3, 7, 8, 15, 20, 34, 35. No source-wide proof certification, code, calculator or native invocation. |
| record-sls | data/curated/StochasticLocalSearch.yaml | supports | Complete maintained DRAFT record assessed by root after capture and matched to accepted scientific support. |
| preview-acceptance-sls | /private/tmp/aimech-stochastic-local-search-draft-preparation-20261015/root-preview-acceptance.json | context_only | Actual native preview compared exactly to the fully root-read static science, metadata and six claim/seven limitation support hashes. Native schema passed. This is not a second verbatim reading or current-base identity clearance. Historical TEMP acceptance is separate from the actual postcapture review; no independent approval. |
| supporting-context-sls | /private/tmp/aimech-stochastic-local-search-draft-preparation-20261015/scientific-support.json | context_only | Same-author static draft support, with thesis PDF pp. 59–61 and visuals 59–61, overview pp. 2–5 and visuals 3–4. Root separately read all six claims and seven limitations. This is preparation support, not an independent audit or an actual canonical postcapture reading. |
| check-gate | /private/tmp/aimech-traces-local-search-cohort343-check-gate.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-vendor | /private/tmp/aimech-traces-local-search-cohort343-check-vendor.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-check-source | /private/tmp/aimech-traces-local-search-cohort343-check-check-source.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-render | /private/tmp/aimech-traces-local-search-cohort343-check-render.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-render-check | /private/tmp/aimech-traces-local-search-cohort343-check-render-check.json | context_only | Actual completed command and retained output before this new review was saved. |
| check-diff | /private/tmp/aimech-traces-local-search-cohort343-check-diff.json | context_only | Actual completed command and retained output before this new review was saved. |

## Limits And Additional Notes

- Author self-review with attributed supporting agents is not independent approval. Accepted previews and full-text access do not imply every source page, cited proof or implementation was read.
- Replacing traces reset current credit memory to one and attenuate other entries. Bounded traces do not establish bounded TD changes or convergence. First-visit correspondence keeps the absorbing setting, positive batch step size, limit versus finite offline equality, completed trials and reciprocal first-visit schedule. The chosen binary-feature action-clearing convention is not universal.
- The replacing source’s Figure 9 trial branch omits an explicit all-trace reset. Its Appendix B clipping/terminal and force-sign ambiguities remain source-qualified; neither author-code behavior nor a repaired experiment is asserted. Conditional MSE comparisons are non-strict and permit equality.
- Watkins hard-cut continuation is indexed by the subsequent action. Cutting removes later return propagation but keeps the bootstrap; an experimental current action still receives its own action-value estimate. Lambda-star endpoints constrain targets, not arbitrary timing-equivalent algorithms. The displayed U timing, C index and thesis corrigenda remain visible; no general multistep convergence theorem or executable backward loop is supplied.
- Replacing memory and Watkins return selection are distinct and potentially composable mechanisms. Shared owner 264 does not make them aliases, prove disjointness or certify a particular combination. Generic eligibility, true-online and soft-cut residuals remain open; owner 267 Full-echo is not resolved here.
- SLS is a configurable combinatorial family. Degenerate deterministic choices are permitted, current positions may worsen, and a best-feasible incumbent requires existence. Memory/time may need state augmentation; randomization alone proves neither reachability nor termination. Formal inclusion of partial or population-valued positions does not equate named member methods.
- The Singh–Sutton author prepublication layout and Watkins thesis have distinct source-version and page conventions. The Hoos dissertation supplies the underlying SLS formalism; the later author chapter is exposition, not invention-priority evidence. Raw access times and whole-second native projections are retained separately from publication and reading dates.
- Root draft acceptances follow complete static draft readings with separately scoped source reading. Actual TEMP preview acceptances compare those drafts and metadata exactly; they are not additional verbatim source or scientific readings. Replacing support spacing and the SLS framework/state wording refinement retain their preimages; they are preparation lineage, not canonical scientific findings.
- The two related ReinforcementLearning mappings are component/procedure-to-task curator relations, not exact identity or subclass assertions. All eight SLS rejection reasons remain exact, including the general mathematical-function and augmented-state distinctions. Actual dated identity notes and the SLS no-match search scope are refreshed from current root decisions; the other accepted fields are unchanged.
- The actual merged-base collection and full frontier accounting are bound to the captured records and root decisions. Only owners 264 and 270 change, preserving prior HillClimbing context and all 907 other main and 393 nested objects. Six required checks passed; any prior failed attempts are separately retained. No global absence, saturation or DRAFT promotion follows.
- Root fully read all three actual record YAMLs, all 16 claims and 21 limitations, actual report Markdown, CREATE history and changed owners before capture, and continued scientific assessment after capture using exact accepted support and newly rechecked 35 captured hashes. Root primary scopes remain selective: Singh–Sutton OCR2–4,7–9,19–26 and visuals1–4,7,8,20; Watkins OCR5,96–98,101–105 and visuals5,101,104; Hoos thesis native59–61/visual60, overview native2–5/visual3. Supporting agent scopes are separately attributed. This postcapture assessment and correspondence check is not a second full verbatim primary-source reading or source-wide proof certification.
- All accepted science is unchanged except declared current identity wording and SLS no-match search scope, plus actual curation times. Assessed all substantive review support rows, source boundaries, individual limits and exact mapping direction. Current identity context distinguishes eight native neighbors; all 20 matching frontier objects and39 candidate-bearing decoded contexts were root-read, with remaining contexts supported by attributed complete assessments. Only owners264/270 change, preserving907othermain and393nested; prior HillClimbing context retained. Governance/render audit reports no discrepancy and preliminary fresh primary audit reports no scientific defect. All six actual check logs passed before this assessment. Records stay DRAFT; no saturation or independent approval inferred.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
title: Scientific self-review of replacing traces, Watkins hard-cut learning and stochastic
  local search
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
summary: The explicitly selected heterogeneous cohort is assessed through 16 source-linked
  claims, 21 individual limitations and four declared source rows. Retain a replacing
  eligibility component, the original Watkins hard-cut forward/delayed control construction
  and the stochastic local-search family separately. The first two retain qualified
  related ReinforcementLearning mappings; SLS retains eight examined no-match targets.
  All records remain DRAFT. This review binds actual creation, canonical capture,
  postcapture root assessment and six completed required checks; its conclusions are
  limited to those bytes and stated reading scopes.
scope:
  description: 'Complete explicitly selected heterogeneous cohort: a credit-memory
    component, a source-scoped control procedure and a configurable combinatorial
    search family. A shared review does not assert a common algorithm identity.'
  selection: Exact maintained IDs AIMech:ReplacingEligibilityTraces, AIMech:WatkinsHardCutMultistepQLearning,
    AIMech:StochasticLocalSearch from actual cohort343 creation.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:ReplacingEligibilityTraces
  - AIMech:WatkinsHardCutMultistepQLearning
  - AIMech:StochasticLocalSearch
  exclusions:
  - target: Generic eligibility traces, true-online methods, soft-cut continuation
      and modern backward-loop reconstructions
    reason: The two source-scoped trace records do not complete or identify these
      residual variants, and no combined implementation is certified.
  - target: One-step Q-learning/Sarsa, MCQ-L, Peng–Williams, Full-echo Q-routing and
      other control procedures
    reason: Overlapping targets or use of eligibility memory does not establish whole-algorithm
      equivalence.
  - target: Continuous search, full GLSM organization and every named local-search
      controller
    reason: The selected SLS family retains representation and configuration boundaries;
      existing HillClimbing progress and other owners remain distinct.
  - target: Uninspected implementation, complete proofs and benchmark replications
    reason: Outside the explicitly attributed primary/exposition and reading scopes.
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  rationale: Retain one source-scoped replacing component. Existing accumulating-TD
    coverage, one-step Sarsa, MCQ-L/Peng whole methods, generic eligibility and true-online
    variants are not exact aliases or implicitly completed. Actual owner resolution
    and residuals are bound separately by the current collection and root decisions.
  evidence_ids:
  - record-replacing
  - src-singh-sutton1996
  - identity-assessment
  - pinned-aio
- action: retain
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  rationale: Retain the original hard-cut forward/delayed control method separately
    from replacing credit memory. Both reuse existing owner 264 with generic, true-online
    and soft-cut residuals preserved. Owner 267 Full-echo Q-routing remains untouched.
    Actual owner resolution and residuals are bound by the current collection and
    root decisions.
  evidence_ids:
  - record-watkins
  - src-watkins1989
  - identity-assessment
  - pinned-aio
- action: retain
  target_ids:
  - AIMech:StochasticLocalSearch
  rationale: Retain the stochastic local-search family under existing owner 270, preserving
    prior HillClimbing progress and separate named methods. No aliases or new frontier
    leaf are added; continuous, terminological and GLSM residual work remains separate.
    Actual owner resolution and residuals are bound by the current collection and
    root decisions.
  evidence_ids:
  - record-sls
  - src-hoos1998
  - identity-assessment
  - pinned-aio
limitations:
- Author self-review with attributed supporting agents is not independent approval.
  Accepted previews and full-text access do not imply every source page, cited proof
  or implementation was read.
- Replacing traces reset current credit memory to one and attenuate other entries.
  Bounded traces do not establish bounded TD changes or convergence. First-visit correspondence
  keeps the absorbing setting, positive batch step size, limit versus finite offline
  equality, completed trials and reciprocal first-visit schedule. The chosen binary-feature
  action-clearing convention is not universal.
- The replacing source’s Figure 9 trial branch omits an explicit all-trace reset.
  Its Appendix B clipping/terminal and force-sign ambiguities remain source-qualified;
  neither author-code behavior nor a repaired experiment is asserted. Conditional
  MSE comparisons are non-strict and permit equality.
- Watkins hard-cut continuation is indexed by the subsequent action. Cutting removes
  later return propagation but keeps the bootstrap; an experimental current action
  still receives its own action-value estimate. Lambda-star endpoints constrain targets,
  not arbitrary timing-equivalent algorithms. The displayed U timing, C index and
  thesis corrigenda remain visible; no general multistep convergence theorem or executable
  backward loop is supplied.
- Replacing memory and Watkins return selection are distinct and potentially composable
  mechanisms. Shared owner 264 does not make them aliases, prove disjointness or certify
  a particular combination. Generic eligibility, true-online and soft-cut residuals
  remain open; owner 267 Full-echo is not resolved here.
- SLS is a configurable combinatorial family. Degenerate deterministic choices are
  permitted, current positions may worsen, and a best-feasible incumbent requires
  existence. Memory/time may need state augmentation; randomization alone proves neither
  reachability nor termination. Formal inclusion of partial or population-valued positions
  does not equate named member methods.
- The Singh–Sutton author prepublication layout and Watkins thesis have distinct source-version
  and page conventions. The Hoos dissertation supplies the underlying SLS formalism;
  the later author chapter is exposition, not invention-priority evidence. Raw access
  times and whole-second native projections are retained separately from publication
  and reading dates.
- Root draft acceptances follow complete static draft readings with separately scoped
  source reading. Actual TEMP preview acceptances compare those drafts and metadata
  exactly; they are not additional verbatim source or scientific readings. Replacing
  support spacing and the SLS framework/state wording refinement retain their preimages;
  they are preparation lineage, not canonical scientific findings.
- The two related ReinforcementLearning mappings are component/procedure-to-task curator
  relations, not exact identity or subclass assertions. All eight SLS rejection reasons
  remain exact, including the general mathematical-function and augmented-state distinctions.
  Actual dated identity notes and the SLS no-match search scope are refreshed from
  current root decisions; the other accepted fields are unchanged.
- The actual merged-base collection and full frontier accounting are bound to the
  captured records and root decisions. Only owners 264 and 270 change, preserving
  prior HillClimbing context and all 907 other main and 393 nested objects. Six required
  checks passed; any prior failed attempts are separately retained. No global absence,
  saturation or DRAFT promotion follows.
- 'Root fully read all three actual record YAMLs, all 16 claims and 21 limitations,
  actual report Markdown, CREATE history and changed owners before capture, and continued
  scientific assessment after capture using exact accepted support and newly rechecked
  35 captured hashes. Root primary scopes remain selective: Singh–Sutton OCR2–4,7–9,19–26
  and visuals1–4,7,8,20; Watkins OCR5,96–98,101–105 and visuals5,101,104; Hoos thesis
  native59–61/visual60, overview native2–5/visual3. Supporting agent scopes are separately
  attributed. This postcapture assessment and correspondence check is not a second
  full verbatim primary-source reading or source-wide proof certification.'
tags:
- scientific-review
- self-review
- heterogeneous-batch
- source-scoped
schema_version: 1.0.0
review_id: 20261015T145952Z-replacing-traces-watkins-hard-cut-and-stochastic-local-search
kind: batch
repository: CultureBotAI/AIMech
started_at: '2026-10-15T14:47:02.854323Z'
finished_at: '2026-10-15T14:59:52.329386Z'
source:
  git_revision: 73729051e58d582f36c9af9296a92b393be0a679
  state: working_tree
  inputs:
  - path: .claude/skills/review-category/SKILL.md
    sha256: 553c3870c1dfc127f90f196b7b212b644706d4c26e2a578ab615ccce588070d7
    role: context
  - path: data/aio/EvolutionaryLLM.yaml
    sha256: d3db6adea3d8d58096c9fb5abef67273489ee719ab900b2d4adbb129e4f7362f
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
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
  - path: data/curated/HillClimbing.yaml
    sha256: 1f63c3e6341fecd3c78e00ae3ced9898c070ba9565dccc5511f3c67e6ea29476
    role: context
  - path: data/curated/IteratedLocalSearch.yaml
    sha256: 15a6a25711dabac3dff72b612cf7daa7a2ae5f9660a9a677c2d21163335f2ef0
    role: context
  - path: data/curated/ModifiedConnectionistQLearning.yaml
    sha256: 8986696e751e7ab7206755f5cfc32b125b6216feac3043f105b354b2b49f4428
    role: context
  - path: data/curated/PengWilliamsQLambda.yaml
    sha256: 58dd0266b45fd8602081d1b468d55a2456de3dd7488c3a9891c080bb587b0bd5
    role: context
  - path: data/curated/QLearning.yaml
    sha256: bcbd0f51f46e91ba6d88c9dc84baa9656aef82282c5c56d887ca81ff5182eb95
    role: context
  - path: data/curated/ReplacingEligibilityTraces.yaml
    sha256: 81300bc3c4616459fa62d21c03c575bbba8fc5a207edbb78d0a7e46c7724b00c
    role: target
  - path: data/curated/Sarsa.yaml
    sha256: 8ac6efbbcfeda82ce462fbc7f6d641a9eab36b8749c6bdb0b7713ba43496e041
    role: context
  - path: data/curated/SimulatedAnnealing.yaml
    sha256: 7e77f553c8b2afc4563dc7ef6cba2b53719f22b1fd02ed37d22de9821079d42c
    role: context
  - path: data/curated/StochasticLocalSearch.yaml
    sha256: f4ae6fc7e1599ac08d77a99b2adcb54498cc41f9c184b13bf0e8c9a0297a789e
    role: target
  - path: data/curated/TabuSearch.yaml
    sha256: 6dae782f4d0c0b2a7195f471b7f73acb38fa036fb43ec15bacfa8f9a0264b844
    role: context
  - path: data/curated/TemporalDifferenceLearning.yaml
    sha256: edd02cd7a9f2b8b916ba684f7aa8cb4c8d49b81a1896912dc5297370d24f348a
    role: context
  - path: data/curated/VariableNeighborhoodSearch.yaml
    sha256: 103c2e6fadc4e2a74740e3da3e6b19c87654be54533fb8c230876149f15a1306
    role: context
  - path: data/curated/WatkinsHardCutMultistepQLearning.yaml
    sha256: 29b2c3331660910f574b5ed8ba7c1153070f187588cd8360e96ec03e3bd9cee1
    role: target
  - path: docs/curated-concepts.md
    sha256: 1a3db0915791b0e90b02cd1f83c35850bfc3c97b18edfd8b946c91030578ccb8
    role: context
  - path: docs/record-review-profile.md
    sha256: 2d3e3a73264523c78930d17b0812e2d22887e25423fe7c38e0ddce922d9cec9d
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/reports/replacing-traces-watkins-and-stochastic-local-search/2026-10-15T144602Z-codex-a9e723.yaml
    sha256: c119a876b95752acb66c6844e992ce19d0683ffe9852f08a92b86d3e0038d53f
    role: context
  - path: justfile
    sha256: 2d9c1b68c1c80d53aa44a6b8b5e916efe8b493650ff59a3fc7479a42be37f400
    role: context
  - path: research/discovery/20261015T144547Z-replacing-traces-watkins-and-stochastic-local-search.json
    sha256: 2716dfc06855f16180b0e5558da4754c8792cebc8f23b1d583f26183f959edd7
    role: context
  - path: research/discovery/20261015T144547Z-replacing-traces-watkins-and-stochastic-local-search.md
    sha256: 6136a86d2ff793a8893851f94f70d1d8d2851a148375eda25de80d2ba1c2bdc7
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
- target_id: AIMech:ReplacingEligibilityTraces
  label: Replacing eligibility traces
  path: data/curated/ReplacingEligibilityTraces.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ReplacingEligibilityTraces.yaml
    role: maintained native concept record
- target_id: AIMech:WatkinsHardCutMultistepQLearning
  label: Watkins hard-cut multistep Q-learning
  path: data/curated/WatkinsHardCutMultistepQLearning.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/WatkinsHardCutMultistepQLearning.yaml
    role: maintained native concept record
- target_id: AIMech:StochasticLocalSearch
  label: Stochastic local search
  path: data/curated/StochasticLocalSearch.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StochasticLocalSearch.yaml
    role: maintained native concept record
checks:
- check_id: check-gate
  name: just check
  status: passed
  required: true
  summary: Actual command completed with exit0; exact output is retained.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  - AIMech:WatkinsHardCutMultistepQLearning
  - AIMech:StochasticLocalSearch
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
  - AIMech:ReplacingEligibilityTraces
  - AIMech:WatkinsHardCutMultistepQLearning
  - AIMech:StochasticLocalSearch
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
  - AIMech:ReplacingEligibilityTraces
  - AIMech:WatkinsHardCutMultistepQLearning
  - AIMech:StochasticLocalSearch
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
  - AIMech:ReplacingEligibilityTraces
  - AIMech:WatkinsHardCutMultistepQLearning
  - AIMech:StochasticLocalSearch
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
  - AIMech:ReplacingEligibilityTraces
  - AIMech:WatkinsHardCutMultistepQLearning
  - AIMech:StochasticLocalSearch
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
  - AIMech:ReplacingEligibilityTraces
  - AIMech:WatkinsHardCutMultistepQLearning
  - AIMech:StochasticLocalSearch
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-diff
evidence:
- evidence_id: captured-inputs
  kind: record_content
  reference: /private/tmp/aimech-traces-local-search-cohort343-capture.json
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: context_only
  summary: Actual canonical inspect output; all captured input hashes rechecked. Inspection
    alone is not scientific approval.
  snapshot_sha256: 3360237ac6060755839c90747f1e9ecb6e98feb04117b01213063e7236e222f8
- evidence_id: postcapture-reading
  kind: record_content
  reference: /private/tmp/aimech-cohort343-root-postcapture-reading.json
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: context_only
  summary: Actual root full-target assessment after capture and completed checks;
    selective primary scopes are stated separately.
  snapshot_sha256: 6de8847998e044ae0cc46a064a9bec0041b2e8cdee72e014f3eb95bf72d5bd8b
- evidence_id: scientific-support
  kind: record_content
  reference: /private/tmp/aimech-traces-local-search-cohort343-review-preparation-20261015/scientific-support.readable.structure.json
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: context_only
  summary: Attributed same-author support of all 16 accepted claims and 21 individual
    limitations. This is preparation DATA, not itself an actual canonical capture.
  snapshot_sha256: a1c8287d823850c141b1c084505fecbefc3dcbc3af7c69f49212aa0e81d240e2
- evidence_id: actual-write
  kind: record_content
  reference: /private/tmp/aimech-traces-local-search-cohort343-write.json
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: context_only
  summary: Actual creation receipt binds three records, report pair and CREATE history.
  snapshot_sha256: 1f94d7fcce16f16f4f947805e4c9c1a7dce044659791955322c25571e6e5f346
- evidence_id: discovery-report
  kind: record_content
  reference: research/discovery/20261015T144547Z-replacing-traces-watkins-and-stochastic-local-search.json
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: context_only
  summary: Record mirrors are exact. Only existing owners 264 and 270 changed; all
    907 other prior main and 393 nested objects are unchanged. The two trace targets
    share existing owner 264; SLS reuses owner 270 with prior HillClimbing context
    preserved; no new frontier leaf was appended.
  snapshot_sha256: 2716dfc06855f16180b0e5558da4754c8792cebc8f23b1d583f26183f959edd7
- evidence_id: creation-history
  kind: record_content
  reference: history/reports/replacing-traces-watkins-and-stochastic-local-search/2026-10-15T144602Z-codex-a9e723.yaml
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: context_only
  summary: Actual append-only CREATE sidecar; review and publication are separate
    later actions.
  snapshot_sha256: c119a876b95752acb66c6844e992ce19d0683ffe9852f08a92b86d3e0038d53f
- evidence_id: pinned-aio
  kind: database
  reference: sources/aio/aio.json
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: context_only
  summary: Exact snapshot supports two qualified related ReinforcementLearning mappings
    and one explicit eight-target SLS no-match assessment; no upstream equivalence
    or subclass assertion.
  locator: Exact AIO:ReinforcementLearning plus all eight accepted SLS rejected targets
    and retained incident-edge contexts. Positive mapping directions and no-match
    reasons retain their distinct meanings.
  snapshot_sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
- evidence_id: identity-assessment
  kind: search
  reference: /private/tmp/aimech-cohort343-root-decisions-20261015.json
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: context_only
  summary: Actual root decisions bind fresh ignored/hidden-inclusive scans and existing
    owners 264/270, including any explicitly assessed context-only matches; no manual
    rereading of every hit by this generator is claimed.
  snapshot_sha256: 1cca24120a61f18affe84157827c7b9a56d5773c6b511c5fbf7102ba02008c73
  search_scope: Exact captured inventory, full carried frontier and four retained
    checkouts searched including ignored and hidden files; no worldwide absence or
    exhaustion claim.
- evidence_id: replacing-preparation-spacing
  kind: record_content
  reference: /private/tmp/aimech-replacing-traces-draft-preparation-20261015/finalization.json
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: context_only
  summary: Preparation-only spacing refinement left the native scientific module unchanged.
    The historical receipt predates the separately retained successful native preview.
  locator: Finalization and referenced four support-comment spacing changes, retained
    preimages and exact differences.
  snapshot_sha256: a9fa3dae72fa77cff936a934f3642ebc3e943efbdd595ee763a284548e90a927
- evidence_id: sls-framework-wording
  kind: record_content
  reference: /private/tmp/aimech-stochastic-local-search-draft-preparation-20261015/preparation-refinement.json
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: context_only
  summary: Before invocation and root acceptance, the termination predicate was described
    as a framework component rather than an element of the search state. Other record
    fields were unchanged; no canonical defect is asserted.
  locator: Single claim-1 framework-versus-state wording correction, with exact module/support/input
    preimages and differences.
  snapshot_sha256: 15ace340513dcf582c5092738d31cf67b9f58e69d314284ead2d473dee513e15
- evidence_id: src-singh-sutton1996
  kind: primary_source
  reference: https://web.eecs.umich.edu/~baveja/Papers/Replace.pdf
  accessed_at: '2026-10-15T13:10:11Z'
  support: supports
  summary: 36-page author-hosted prepublication layout associated with Machine Learning
    22, 123–158, March 1996. Official publisher metadata verifies the published counterpart;
    no publication day or byte identity with journal typesetting is inferred. Author
    cover dates and provisional pagination remain distinct from published metadata.
    Acquisition time is access metadata, not a claim of full reading.
  locator: Source agent read all 36 OCR pages and visual pages 2, 3, 7, 8, 15, 20,
    34, 35. Root’s distinct partial and supplemental scopes are in the accepted reading
    receipts. Appendix OCR reading does not certify all proofs; no author software
    was inspected. Later separate supporting trace-pair audit refreshed OCR pp. 2–4,
    7–8, 15, 20–22, 34–35 and visuals 2, 3, 7, 8, 15, 20, 34, 35. Historical root/source-agent
    scopes remain separate from the actual runtime root postcapture scope.
  snapshot_sha256: 93193ac196bc90c1e30b800ad0a7d4c6082c3525fcb9037f5cc55b3ffeec4364
- evidence_id: src-watkins1989
  kind: primary_source
  reference: https://www.repository.cam.ac.uk/bitstreams/2ad45009-0e4b-496e-bd52-cd8f98a3f4d0/download
  accessed_at: '2026-10-15T13:55:54Z'
  support: supports
  summary: PhD thesis submitted at King’s College, University of Cambridge, cover
    dated May 1989. The retained 241-page Cambridge repository scan includes two initial
    corrigenda pages. The repository separately records 1989-05-10, while the preface
    is dated May 1; no exact cover publication day is inferred. PDF build metadata
    is dated 2006-04-06 and the response Last-Modified is 2026-07-10, neither a publication
    date. Local PDF and printed page locators are both supplied. Acquisition time
    is access metadata, not a claim of full reading.
  locator: 'Original supporting researcher: OCR PDF pp. 1–5, 88–109, 119–120; visuals
    pp. 5–8, 97–98, 101, 104. Root: OCR pp. 5, 96–98, 101–105; visuals pp. 5, 101,
    104. These are separately attributed selected scopes, not all 241 pages or complete
    proofs. The later separate supporting trace-pair audit refreshed OCR pp. 88–105
    and visuals pp. 5, 6, 98, 101, 104. It does not certify the whole thesis or original
    convergence proofs; runtime root postcapture reading is separate.'
  snapshot_sha256: 676a401aa8d18204de5f4f05f7ce329846325b59f20ae71b2de1d6056a679412
- evidence_id: src-hoos1998
  kind: primary_source
  reference: https://www.cs.ubc.ca/~hoos/ps/phd-thesis.pdf
  accessed_at: '2026-10-15T13:55:29Z'
  support: supports
  summary: Author-hosted Darmstadt doctoral dissertation, 1998; title page records
    submission on 30 September 1998 and defense on 11 November 1998. The acquired
    file has 224 physical PDF pages; the author index describes 218 pages. Locators
    distinguish physical PDF from printed pages. This is the thesis, not a later book
    edition. Acquisition time is access metadata, not a claim of full reading.
  locator: 'Original research agent: native PDF pp. 15–17 and 59–65, visuals pp. 59–61.
    Root: native pp. 59–61 and visual p. 60. Draft preparation: native pp. 59–61 and
    visuals pp. 59–61. None is a full 224-page reading or GLSM proof certification.'
  snapshot_sha256: a338da187d332f533a288d0e49e56606ae4a47b2366df1ebf6a23e62aae3183e
- evidence_id: src-hoos-stutzle2015
  kind: primary_source
  reference: https://ada.liacs.nl/papers/HooStu15b.pdf
  accessed_at: '2026-10-15T13:55:33Z'
  support: supports
  summary: Author-hosted scholarly handbook chapter 54, 2015, printed pp. 1085–1105,
    in a 21-page PDF. Institutional metadata gives January 2015 without a publication
    day. Used as the authors’ framework exposition, not as an invention-priority claim
    or evidence of having read the book cited by the chapter. Acquisition time is
    access metadata, not a claim of full reading.
  locator: 'Original research agent: native PDF pp. 1–6, visuals pp. 3–4. Root: native
    pp. 2–5 and visual p. 3. Draft preparation: native pp. 2–5 and visuals pp. 3–4.
    The 21-page overview is used as author exposition, not priority evidence.'
  snapshot_sha256: 2203b7888ea15b17f145a5401b4767057c155d0d7d5f44d6a4cb9e68d59f08ee
- evidence_id: record-replacing
  kind: record_content
  reference: data/curated/ReplacingEligibilityTraces.yaml
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: supports
  summary: Complete maintained DRAFT record assessed by root after capture and matched
    to accepted scientific support.
  snapshot_sha256: 81300bc3c4616459fa62d21c03c575bbba8fc5a207edbb78d0a7e46c7724b00c
- evidence_id: preview-acceptance-replacing
  kind: record_content
  reference: /private/tmp/aimech-replacing-traces-draft-preparation-20261015/root-preview-acceptance.json
  accessed_at: '2026-10-15T13:45:02.034921Z'
  support: context_only
  summary: Root read complete static draft and all support narratives before invocation.
    Current preview compared field-for-field to the root-read AST literal, identity/source
    metadata and snapshot; actual curation metadata and successful native validation
    receipt were separately inspected. This is comparison-based review, not a second
    verbatim full-preview reading. Fresh creation-base identity reconciliation and
    adversarial source audit remain separate. Historical TEMP acceptance is separate
    from the actual postcapture review; no independent approval.
  snapshot_sha256: beed1174fe40175d7c668aac26923b61d79141742372a3191eb6f17d2ebb7a22
- evidence_id: supporting-context-replacing
  kind: record_content
  reference: /private/tmp/aimech-trace-pair-supporting-audit-20261015/assessment.json
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: context_only
  summary: 'Separate same-author supporting audit: all ten trace-pair claims and fourteen
    limitations assessed. Fresh Watkins OCR PDF pp. 88–105 and visuals 5, 6, 98, 101,
    104; fresh Singh–Sutton OCR pp. 2–4, 7–8, 15, 20–22, 34–35 and visuals 2, 3, 7,
    8, 15, 20, 34, 35. No source-wide proof certification, code, calculator or native
    invocation.'
  snapshot_sha256: b8f15e2b6140ccc9f6de36412f8427546fab6fc4faf7b6fcaec34f33d396e4b4
- evidence_id: record-watkins
  kind: record_content
  reference: data/curated/WatkinsHardCutMultistepQLearning.yaml
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: supports
  summary: Complete maintained DRAFT record assessed by root after capture and matched
    to accepted scientific support.
  snapshot_sha256: 29b2c3331660910f574b5ed8ba7c1153070f187588cd8360e96ec03e3bd9cee1
- evidence_id: preview-acceptance-watkins
  kind: record_content
  reference: /private/tmp/aimech-watkins-hard-cut-draft-preparation-20261015/root-preview-acceptance.json
  accessed_at: '2026-10-15T14:16:50.624589Z'
  support: context_only
  summary: Exact semantic comparison of actual native preview with the complete root-read
    static module, all inputs and all five claim/seven limitation support rows passed;
    no second verbatim reading of the same scientific prose is claimed. Native schema
    returned no errors. Accepted bounded draft, not canonical or fresh-base identity
    clearance. Historical TEMP acceptance is separate from the actual postcapture
    review; no independent approval.
  snapshot_sha256: ff5cbac3666e961d4e84b0acd8480925f379bf2234e09251d3bf3fd527be9f6f
- evidence_id: supporting-context-watkins
  kind: record_content
  reference: /private/tmp/aimech-trace-pair-supporting-audit-20261015/assessment.json
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: context_only
  summary: 'Separate same-author supporting audit: all ten trace-pair claims and fourteen
    limitations assessed. Fresh Watkins OCR PDF pp. 88–105 and visuals 5, 6, 98, 101,
    104; fresh Singh–Sutton OCR pp. 2–4, 7–8, 15, 20–22, 34–35 and visuals 2, 3, 7,
    8, 15, 20, 34, 35. No source-wide proof certification, code, calculator or native
    invocation.'
  snapshot_sha256: b8f15e2b6140ccc9f6de36412f8427546fab6fc4faf7b6fcaec34f33d396e4b4
- evidence_id: record-sls
  kind: record_content
  reference: data/curated/StochasticLocalSearch.yaml
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: supports
  summary: Complete maintained DRAFT record assessed by root after capture and matched
    to accepted scientific support.
  snapshot_sha256: f4ae6fc7e1599ac08d77a99b2adcb54498cc41f9c184b13bf0e8c9a0297a789e
- evidence_id: preview-acceptance-sls
  kind: record_content
  reference: /private/tmp/aimech-stochastic-local-search-draft-preparation-20261015/root-preview-acceptance.json
  accessed_at: '2026-10-15T14:34:10.723057Z'
  support: context_only
  summary: Actual native preview compared exactly to the fully root-read static science,
    metadata and six claim/seven limitation support hashes. Native schema passed.
    This is not a second verbatim reading or current-base identity clearance. Historical
    TEMP acceptance is separate from the actual postcapture review; no independent
    approval.
  snapshot_sha256: c9195fdfde9a6de0a529e2f27fb22ad5f30abf86806aa0491196ee223d23e711
- evidence_id: supporting-context-sls
  kind: record_content
  reference: /private/tmp/aimech-stochastic-local-search-draft-preparation-20261015/scientific-support.json
  accessed_at: '2026-10-15T14:59:49.719222Z'
  support: context_only
  summary: Same-author static draft support, with thesis PDF pp. 59–61 and visuals
    59–61, overview pp. 2–5 and visuals 3–4. Root separately read all six claims and
    seven limitations. This is preparation support, not an independent audit or an
    actual canonical postcapture reading.
  snapshot_sha256: 61909a6b1fe5899b6c50f0e2d0c15bcba8d17ce4fcc85442be5a58733aecec17
- evidence_id: check-gate
  kind: validation
  reference: /private/tmp/aimech-traces-local-search-cohort343-check-gate.json
  accessed_at: '2026-10-15T14:58:12.131535Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: 238798fface7dd56dda59ab2c3e67b859d4d0e19437001f64bffc80a20b44716
- evidence_id: check-vendor
  kind: validation
  reference: /private/tmp/aimech-traces-local-search-cohort343-check-vendor.json
  accessed_at: '2026-10-15T14:58:16.364993Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: ab46dfdc2636f28b8c3ccc80362adf9a388657ed8d58d5d54f1e6a41ec81dee1
- evidence_id: check-check-source
  kind: validation
  reference: /private/tmp/aimech-traces-local-search-cohort343-check-check-source.json
  accessed_at: '2026-10-15T14:58:19.046555Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: 818672f92929b9e3c8cea2594263b24114472459f7967521087ea715d41a4530
- evidence_id: check-render
  kind: validation
  reference: /private/tmp/aimech-traces-local-search-cohort343-check-render.json
  accessed_at: '2026-10-15T14:46:50.415441Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: a0625328d6bd7731be9c9ca05c696a6f2234022920f7cda55bd8215eca6c2aee
- evidence_id: check-render-check
  kind: validation
  reference: /private/tmp/aimech-traces-local-search-cohort343-check-render-check.json
  accessed_at: '2026-10-15T14:58:36.726364Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: 6e94dc2c74619e73c7863f3c6f5bf1991e85624132a2f3cf47198b7ea27d0a9a
- evidence_id: check-diff
  kind: validation
  reference: /private/tmp/aimech-traces-local-search-cohort343-check-diff.json
  accessed_at: '2026-10-15T14:58:36.982050Z'
  support: context_only
  summary: Actual completed command and retained output before this new review was
    saved.
  snapshot_sha256: 81452cbbf10ead66472a07d672addba97d3dfd234ae191b849dfbefcebe6dd19
assessments:
- assessment_id: replacing-state-replacing-recurrence
  area: evidence
  topic: Claim state-replacing-recurrence
  outcome: supported
  summary: Fresh PDF pp. 2–3 text/visual confirms reset-to-one for the current state
    and q times the old trace for other states. The accumulating comparator and closed
    gamma/lambda intervals are literal; replacing does not mean add then clip an arbitrary
    trace.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - preview-acceptance-replacing
  - src-singh-sutton1996
- assessment_id: replacing-trace-as-td-credit-component
  area: evidence
  topic: Claim trace-as-td-credit-component
  outcome: supported
  summary: Fresh PDF pp. 3–4 confirms gamma=1, absorbing terminal value 0, and DeltaV
    using the newly formed e_(t+1) with the same-time value estimates. This is a prediction-credit
    component, not an action selector or full controller.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - preview-acceptance-replacing
  - src-singh-sutton1996
- assessment_id: replacing-bounded-recency-with-endpoints
  area: evidence
  topic: Claim bounded-recency-with-endpoints
  outcome: supported
  summary: 'Hand induction: reset to 1 and multiplication by q in [0,1] preserve the
    stated trace interval. k inactive updates give q^k times the prior value; q=0
    clears after one inactive update and q=1 retains it. This says nothing about bounds
    on TD errors or parameter updates.'
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - preview-acceptance-replacing
  - src-singh-sutton1996
- assessment_id: replacing-qualified-first-visit-correspondence
  area: evidence
  topic: Claim qualified-first-visit-correspondence
  outcome: supported
  summary: Fresh PDF pp. 7–8 confirms a repeated-batch limit and a different completed-trial
    offline identity. For N(s)>0 and 0<alpha<1/N, the batch error multiplier 1-alpha*N(s)
    is strictly between 0 and 1; the limiting estimate is the first-visit mean. Offline
    schedule 1/i gives V_i=V_(i-1)+(R_i-V_(i-1))/i. No arbitrary online finite-step
    equality is inferred.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - preview-acceptance-replacing
  - src-singh-sutton1996
- assessment_id: replacing-binary-feature-control-realization
  area: evidence
  topic: Claim binary-feature-control-realization
  outcome: supported
  summary: Fresh Figure 9 and PDF pp. 21–22 confirm decay, then active chosen-action
    traces to 1 and corresponding active other-action traces to 0, before environment/reward
    and later scalar TD update. The alternative pair-only replacement is explicitly
    separate; clearing other actions at active features is not a hard cut of every
    preceding trace.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - preview-acceptance-replacing
  - src-singh-sutton1996
- assessment_id: replacing-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: The recurrence is a mathematical credit-memory component. Source behavior
    does not supply a complete policy/controller; qualified related RL mapping preserves
    that boundary.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - src-singh-sutton1996
- assessment_id: replacing-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: One qualified related ReinforcementLearning mapping follows root acceptance.
    The pinned target is a learning task, not the recurrence or a guarantee. MathematicalFunction
    is a defensible optional relation for the concrete rule and is not rejected as
    scalar-only; it is omitted as unnecessary. Geometric decay does not force ExponentialFunction,
    and trace recurrence is not neural architecture.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - pinned-aio
- assessment_id: replacing-source-assessment
  area: provenance
  topic: source assessment
  outcome: supported
  summary: Only singh-sutton1996 is declared and cited. Author prepublication layout,
    published 1996 metadata, raw fractional access, failed acquisition and whole-second
    native projection remain separate; all local locators use author PDF pages.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - src-singh-sutton1996
- assessment_id: replacing-limitations-assessment
  area: scope
  topic: limitations assessment
  outcome: supported
  summary: All seven limitations have individual source or hand-boundary explanations.
    The source’s algorithm/pseudocode and experiment-environment ambiguities are explicit
    without an executable repair or author-code defect claim.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - src-singh-sutton1996
- assessment_id: replacing-identity
  area: identity
  topic: Concept boundary and actual owner
  outcome: supported
  summary: 'The maintained concept retains its accepted mathematical_method scope
    with its exact accepted aliases []. Actual root decisions retain owner 264 and
    distinct residuals. The supporting historical identity scope is: Historical 757
    native / 442 AIO identity snapshot only, with complete retained four-root phrase
    and eligibility passes. Owner 264 is reused; generic/true-online residuals remain.
    No future merged-base absence is asserted.'
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - identity-assessment
  - postcapture-reading
- assessment_id: replacing-limitation-1
  area: scope
  topic: Retained limitation 1
  outcome: supported
  summary: Component-versus-control distinction is supported by the recurrence and
    its distinct prediction/control uses. Historical priority is not re-established;
    general trace-family and true-online residuals are retained.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - src-singh-sutton1996
- assessment_id: replacing-limitation-2
  area: scope
  topic: Retained limitation 2
  outcome: supported
  summary: Trace boundedness requires both initialization and multiplier bounds. It
    neither bounds rewards/step sizes nor gives return existence at gamma=1 or learning
    convergence.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - src-singh-sutton1996
- assessment_id: replacing-limitation-3
  area: scope
  topic: Retained limitation 3
  outcome: supported
  summary: Fresh batch/offline proof passages support the schedule distinctions and
    positive-alpha qualification. Fresh visual p. 15 confirms non-strict inequalities
    and equality cases. The appendix proof itself is not certified.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - src-singh-sutton1996
- assessment_id: replacing-limitation-4
  area: scope
  topic: Retained limitation 4
  outcome: supported
  summary: PDF pp. 21–22 and Note 6 on p. 35 support the selected binary-feature realization,
    pair-only alternative and nonstationary-policy limitation. No arbitrary neural-network
    or off-policy convergence claim is added.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - src-singh-sutton1996
- assessment_id: replacing-limitation-5
  area: scope
  topic: Retained limitation 5
  outcome: supported
  summary: Fresh visual Figure 9 has traces initialized in step 1 and episode-end
    return to step 2; Note 3 continuing indices do not settle an all-trace reset.
    The unresolved printed convention remains explicit without asserting author-code
    failure.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - src-singh-sutton1996
- assessment_id: replacing-limitation-6
  area: scope
  topic: Retained limitation 6
  outcome: supported
  summary: Fresh Appendix B text/visual pp. 34–35 confirms clipping to 0.5 followed
    by the printed strict >0.5 condition, and minus-g with negative g. Literal post-clipping
    testing cannot pass; no experimental implementation or repaired dynamics are inferred.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - src-singh-sutton1996
- assessment_id: replacing-limitation-7
  area: scope
  topic: Retained limitation 7
  outcome: supported
  summary: Exact accepted author-PDF hash and metadata are preserved. Selective OCR
    and visuals do not establish full source/proof/software/benchmark reproduction.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  evidence_ids:
  - record-replacing
  - scientific-support
  - src-singh-sutton1996
- assessment_id: watkins-action-values-and-implicit-greedy-policy
  area: evidence
  topic: Claim action-values-and-implicit-greedy-policy
  outcome: supported
  summary: Fresh PDF pp. 102–103 confirms maximum state values, an implicit maximizing
    policy and separate unspecified behavior selection. Ties are possible and are
    retained as a convention gap; an exploration branch label alone does not identify
    a non-policy action.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - preview-acceptance-watkins
  - src-watkins1989
- assessment_id: watkins-hard-cut-forward-return
  area: evidence
  topic: Claim hard-cut-forward-return
  outcome: supported
  summary: Fresh PDF pp. 100–102 and visual p. 101 confirm lambda_t from action at
    t but lambda_(t+1) in R_t recursion, with the displayed bootstrap U_t(s_(t+1)).
    Visual p. 104 reuses the hard-cut rule for action values and separately introduces
    the soft alternative. The following U_(t+1) prose is not silently substituted.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - preview-acceptance-watkins
  - src-watkins1989
- assessment_id: watkins-cut-boundary-and-experimental-action-credit
  area: evidence
  topic: Claim cut-boundary-and-experimental-action-credit
  outcome: supported
  summary: Hand substitution lambda_(t+1)=0 leaves r_t+gamma*U_t(s_(t+1)), retaining
    the bootstrap but removing R_(t+1), including the reward generated by the next
    non-policy action. By contrast lambda_t affects prior returns, not whether the
    current experimental action receives its own action-value estimate. This statement
    concerns propagation through the displayed return recursion, not all indirect
    future changes in learned values.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - preview-acceptance-watkins
  - src-watkins1989
- assessment_id: watkins-delayed-action-value-update
  area: evidence
  topic: Claim delayed-action-value-update
  outcome: supported
  summary: Visual p. 104 has Q_(t+T+1)=(1-alpha)Q_(t+T)+alpha*R_t at the earlier visited
    pair; current update-time value is correct. The source separately discusses incremental
    prediction differences and changing-estimate effects. The claim is conditional
    on an estimate being available, not a promise of exact finite-delay observability
    of an infinite return.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - preview-acceptance-watkins
  - src-watkins1989
- assessment_id: watkins-one-step-and-unit-continuation-boundaries
  area: evidence
  topic: Claim one-step-and-unit-continuation-boundaries
  outcome: supported
  summary: 'Fresh PDF p. 95 constant-lambda endpoints combined with PDF pp. 101 and
    104 hard cuts supports the scoped limits: lambda_star=0 gives the one-step target;
    lambda_star=1 still cuts at a subsequent non-policy action. Target equality does
    not force the same delayed/online trajectory.'
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - preview-acceptance-watkins
  - src-watkins1989
- assessment_id: watkins-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: The selected identity is an algorithm for policy-cut action-return estimation
    with delayed action-value updating; its definition does not replace the original
    construction with a modern trace-loop alias. Qualified related RL is appropriate.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - src-watkins1989
- assessment_id: watkins-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: Qualified related_match to the ReinforcementLearning task only; neither
    exact identity nor an algorithm-class hierarchy. Optional soft exponential machinery
    does not justify an additional required-component relation.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - pinned-aio
- assessment_id: watkins-source-assessment
  area: provenance
  topic: source assessment
  outcome: supported
  summary: Only the original thesis is declared as a native evidence source, and it
    is cited by every claim and the definition. Rummery/Peng/Watkins–Dayan comparisons
    remain historical research context; no unsupported native comparative theorem
    is added.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - src-watkins1989
- assessment_id: watkins-limitations-assessment
  area: scope
  topic: limitations assessment
  outcome: supported
  summary: All seven limits individually assessed. Source timing/corrigenda and proof
    boundaries are intrinsic evidence qualifications, not fabricated canonical findings.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - src-watkins1989
- assessment_id: watkins-identity
  area: identity
  topic: Concept boundary and actual owner
  outcome: supported
  summary: 'The maintained concept retains its accepted algorithm scope with its exact
    accepted aliases []. Actual root decisions retain owner 264 and distinct residuals.
    The supporting historical identity scope is: This record selects the original
    1989 hard-cut forward-return and delayed action-value construction. It is distinct
    from the maintained one-step Q-learning and Sarsa records, the neural selected-action
    MCQ-L procedure, Peng–Williams two-error propagation, and replacing eligibility
    as a component. Shared one-step targets or greedy special cases do not equate
    complete timing and credit policies. The source’s soft-cut alternative and other
    eligibility variants remain separate scope. Research on 15 October 2026 at 13:56:54–13:57:06
    UTC compared 760 native and 442 pinned AIO records using Watkins-specific identity
    probes. Four ignored- and hidden-inclusive checkout scans returned 177, 179, 515
    and 557 occurrences, reconstructed into 12 exact contents, all read. All string
    values and keys in 909 main and 393 nested frontier objects were queried, with
    six relevant objects read in full. Fourteen exact AIO nodes and 59 incident-edge
    entries were assessed. The native identifier was selected after that historical
    research; these observations do not assert absence beyond its inspected snapshot
    and contexts. The broader eligibility-trace context retains other components and
    control variants; Full-echo Q-routing is a separate method.'
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - identity-assessment
  - postcapture-reading
- assessment_id: watkins-limitation-1
  area: scope
  topic: Retained limitation 1
  outcome: supported
  summary: Hard-cut return/control procedure is distinct from replacing credit memory
    and the source soft exponential continuation. MCQ-L/Peng comparisons retain the
    already accepted historical scopes; no fresh complete rereading of those separate
    sources is claimed.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - src-watkins1989
- assessment_id: watkins-limitation-2
  area: scope
  topic: Retained limitation 2
  outcome: supported
  summary: Fresh PDF p. 92 states bounded rewards and gamma<1 for tail control. The
    draft does not extend this to continuing undiscounted or arbitrary approximation;
    lambda_star=1 retains hard cuts and supplies no convergence result.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - src-watkins1989
- assessment_id: watkins-limitation-3
  area: scope
  topic: Retained limitation 3
  outcome: supported
  summary: Fresh visual p. 101 independently confirms the literal U_t display versus
    U_(t+1) prose. Keeping both observations is accurate; an executable convention
    remains unresolved rather than repaired.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - src-watkins1989
- assessment_id: watkins-limitation-4
  area: scope
  topic: Retained limitation 4
  outcome: supported
  summary: Fresh initial corrigenda pp. 5–6 and original pp. 97–98 show the changing-value
    correction terms and C(x,t)/C(x,t+1) discrepancy. Small-alpha prose is not a uniform
    horizon error bound or exact true-online equivalence; no such claim appears in
    the draft.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - src-watkins1989
- assessment_id: watkins-limitation-5
  area: scope
  topic: Retained limitation 5
  outcome: supported
  summary: Fresh PDF p. 100 assumes a unique policy action while p. 102 defines a
    maximizing action without a tie rule. The selected passages do not fully specify
    exploration, terminal/reset and initialization conventions. The caveat is properly
    local to this construction, not absence from all later literature.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - src-watkins1989
- assessment_id: watkins-limitation-6
  area: scope
  topic: Retained limitation 6
  outcome: supported
  summary: Fresh PDF p. 105 explicitly states no general proof for this multistep
    family and explains possible policy/value instability. The one-step proof claim
    on p. 103 cannot be promoted to this family; no modern nonexistence claim is made.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - src-watkins1989
- assessment_id: watkins-limitation-7
  area: scope
  topic: Retained limitation 7
  outcome: supported
  summary: Exact Cambridge scan hash and accepted publication/access metadata are
    preserved. Current audit did not redownload the source or freshly verify external
    catalog dates, and does not certify all 241 pages, appendix proofs, software or
    performance.
  target_ids:
  - AIMech:WatkinsHardCutMultistepQLearning
  evidence_ids:
  - record-watkins
  - scientific-support
  - src-watkins1989
- assessment_id: sls-neighborhood-search-framework
  area: evidence
  topic: Claim neighborhood-search-framework
  outcome: supported
  summary: The thesis lists the five underlying search components. The later author
    exposition expressly adds memory and stopping. The claim distinguishes these source
    roles instead of retroactively attributing the seven-component form to the 1998
    list. A preparation-only wording correction distinguishes a termination predicate
    as a framework component from position and memory as the search state.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - preview-acceptance-sls
  - src-hoos-stutzle2015
  - src-hoos1998
- assessment_id: sls-randomized-and-deterministic-decisions
  area: evidence
  topic: Claim randomized-and-deterministic-decisions
  outcome: supported
  summary: The chapter explicitly models deterministic decisions with degenerate distributions.
    No uniformity, independence or mandatory random branch is inferred from the word
    stochastic.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - preview-acceptance-sls
  - src-hoos-stutzle2015
- assessment_id: sls-guidance-memory-and-nonimproving-moves
  area: evidence
  topic: Claim guidance-memory-and-nonimproving-moves
  outcome: supported
  summary: The chapter states that evaluation may differ from the objective or change
    during search, includes memory, and explicitly describes worsening acceptance.
    Strict iterative improvement is separately identified, so the family is not collapsed
    into HillClimbing.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - preview-acceptance-sls
  - src-hoos-stutzle2015
- assessment_id: sls-constructive-perturbative-and-population-positions
  area: evidence
  topic: Claim constructive-perturbative-and-population-positions
  outcome: supported
  summary: The thesis permits positions beyond complete candidates; the chapter explicitly
    constructs partial-solution neighborhoods and set-valued population positions.
    The final sentence is an identity boundary, not a claim that the members share
    identical transitions.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - preview-acceptance-sls
  - src-hoos-stutzle2015
  - src-hoos1998
- assessment_id: sls-termination-and-best-encountered-solution
  area: evidence
  topic: Claim termination-and-best-encountered-solution
  outcome: supported
  summary: The working-principle passage supplies the stop and return conventions.
    The claim adds the explicit existence condition for a feasible incumbent and does
    not turn the solution-set definition into a global optimality certificate.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - preview-acceptance-sls
  - src-hoos-stutzle2015
- assessment_id: sls-family-and-search-control-boundary
  area: evidence
  topic: Claim family-and-search-control-boundary
  outcome: supported
  summary: The chapter directly contrasts SLS with metaheuristic and gives non-equivalence
    examples. The thesis distinguishes local strategies from higher control and introduces
    GLSM as a representation; no unread GLSM theorem or universal equivalence is claimed.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - preview-acceptance-sls
  - src-hoos-stutzle2015
  - src-hoos1998
- assessment_id: sls-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: The thesis establishes the underlying neighborhood-search procedure; the
    later author exposition supplies memory, stopping and deterministic special cases.
    The definition identifies a configurable combinatorial family, not a complete
    fixed transition kernel.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - src-hoos1998
  - src-hoos-stutzle2015
- assessment_id: sls-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: Eight candidate AIO classes were inspected with all incident edges. Training/learning
    or LLM scope is not mandatory; Markov state augmentation and arbitrary function
    representation do not supply an informative match for the whole family. MathematicalFunction
    is not rejected as scalar-only.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - pinned-aio
- assessment_id: sls-source-assessment
  area: provenance
  topic: source assessment
  outcome: supported
  summary: The 1998 author dissertation supplies the underlying formalism; the 2015
    author-hosted chapter supplies memory, stopping and deterministic-case exposition.
    Both native source rows are cited. The later chapter does not establish invention
    priority. The ILS discovery pointer remains context, not a declared native source.
    Publication, raw access time, native whole-second projection and selective reading
    are separately retained.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - src-hoos1998
  - src-hoos-stutzle2015
- assessment_id: sls-limitations-assessment
  area: scope
  topic: limitations assessment
  outcome: supported
  summary: All seven limitations retain configurable-instance requirements, the feasible-incumbent
    condition, nonmonotone current positions, absence of automatic reachability or
    termination, augmented-state qualifications, family/member distinctions and selective
    source-reading limits.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - src-hoos1998
  - src-hoos-stutzle2015
- assessment_id: sls-identity
  area: identity
  topic: Concept boundary and actual owner
  outcome: supported
  summary: 'The maintained concept retains its accepted algorithm scope with its exact
    accepted aliases []. Actual root decisions retain owner 270 and distinct residuals.
    The supporting historical identity scope is: This record selects the named combinatorial
    Stochastic local search family, not every informal use of local search or an exact
    alias of HillClimbing, IteratedLocalSearch, TabuSearch, SimulatedAnnealing, VariableNeighborhoodSearch
    or the GLSM control representation. The historical identity snapshot on 15 October
    2026 at 13:57:30–13:57:45 UTC contained 760 native records and 442 pinned AIO
    records. Four ignored- and hidden-inclusive scans produced 14,722 occurrences
    in 529 exact contents; the supporting research assessed 359 decoded contexts,
    including 29 exact contexts previously read in a separately retained assessment.
    Mechanical identity normalization found no candidate collision within that snapshot.
    Recursive matching covered all 909 main and 393 nested frontier objects, with
    relevant full rows assessed separately. Existing owner 270 carries the 2001 ILS
    pointer as historical discovery context; its prior HillClimbing progress remains
    distinct. The 1998 thesis and 2015 overview supply the present family definition.
    Guided/Fast Local Search, Gu’s SAT method, continuous or terminological variants
    and detailed GLSM organization remain separate residual contexts. This dated assessment
    is not a claim of absence at a later merged base; the subsequently added VNS record
    is a distinct named method, not an uninspected exact synonym.'
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - identity-assessment
  - postcapture-reading
- assessment_id: sls-limitation-1
  area: scope
  topic: Retained limitation 1
  outcome: supported
  summary: The chapter acknowledges the common perturbative use of the bare term.
    The historical ILS pointer uses LocalSearch as a flexible embedded routine; that
    context does not broaden the native definition to every optimizer. Continuous
    and full GLSM variants remain residual.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - src-hoos1998
  - src-hoos-stutzle2015
- assessment_id: sls-limitation-2
  area: scope
  topic: Retained limitation 2
  outcome: supported
  summary: The listed components are parameters of a family, not supplied instance
    code. An empty feasible-incumbent set has no best feasible member; an implementation
    needs its own failure convention. No implementation has been inspected or repaired.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - src-hoos1998
  - src-hoos-stutzle2015
- assessment_id: sls-limitation-3
  area: scope
  topic: Retained limitation 3
  outcome: supported
  summary: 'Elementary bookkeeping: for a fixed consistently evaluated minimization
    objective, the minimum over encountered feasible candidates cannot increase as
    that set grows. This does not constrain the current point or a changing guidance
    function.'
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - src-hoos1998
  - src-hoos-stutzle2015
- assessment_id: sls-limitation-4
  area: scope
  topic: Retained limitation 4
  outcome: supported
  summary: The research hand example has states a,b,c, solution c, deterministic moves
    a→b→a and initialization at a, so the allowed framework need not reach a solution
    or terminate under success-only stopping. This is a scoped counterexample, not
    a theorem about every instance.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - src-hoos1998
  - src-hoos-stutzle2015
- assessment_id: sls-limitation-5
  area: scope
  topic: Retained limitation 5
  outcome: supported
  summary: Memory-dependent transitions can differ at the same position. Augmenting
    the state with all relevant memory and time removes that particular omission,
    without implying homogeneous transitions, stationarity, reversibility or a specified
    target law.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - src-hoos1998
  - src-hoos-stutzle2015
- assessment_id: sls-limitation-6
  area: scope
  topic: Retained limitation 6
  outcome: supported
  summary: Shared formal representability does not make named methods aliases. The
    chapter’s constructive/population and metaheuristic discussion supports retaining
    each narrower mechanism and the accepted family identity separately.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - src-hoos1998
  - src-hoos-stutzle2015
- assessment_id: sls-limitation-7
  area: scope
  topic: Retained limitation 7
  outcome: supported
  summary: Exact source genres, years, actual file versions and selective reading
    are retained. The original author thesis and later scholarly exposition serve
    different roles; neither the unread book nor uninspected empirical/proof/software
    material is certified.
  target_ids:
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - record-sls
  - scientific-support
  - src-hoos1998
  - src-hoos-stutzle2015
- assessment_id: actual-correspondence
  area: consistency
  topic: Captured bytes, accepted science and frontier accounting
  outcome: supported
  summary: All three captured records equal the actual write payloads and report entries.
    Exact support covers 16 claims and 21 limitations. Only existing owners 264 and
    270 changed; all 907 other prior main and 393 nested values remain unchanged.
    All three accepted method scopes reuse their existing owners, with no appended
    leaf. Six required checks passed. No global exhaustion or DRAFT promotion is inferred.
  target_ids:
  - AIMech:ReplacingEligibilityTraces
  - AIMech:WatkinsHardCutMultistepQLearning
  - AIMech:StochasticLocalSearch
  evidence_ids:
  - captured-inputs
  - postcapture-reading
  - discovery-report
  - creation-history
  - replacing-preparation-spacing
  - sls-framework-wording
  - check-gate
  - check-vendor
  - check-check-source
  - check-render
  - check-render-check
  - check-diff
findings: []
actions: []
notes:
- All accepted science is unchanged except declared current identity wording and SLS
  no-match search scope, plus actual curation times. Assessed all substantive review
  support rows, source boundaries, individual limits and exact mapping direction.
  Current identity context distinguishes eight native neighbors; all 20 matching frontier
  objects and39 candidate-bearing decoded contexts were root-read, with remaining
  contexts supported by attributed complete assessments. Only owners264/270 change,
  preserving907othermain and393nested; prior HillClimbing context retained. Governance/render
  audit reports no discrepancy and preliminary fresh primary audit reports no scientific
  defect. All six actual check logs passed before this assessment. Records stay DRAFT;
  no saturation or independent approval inferred.
```
