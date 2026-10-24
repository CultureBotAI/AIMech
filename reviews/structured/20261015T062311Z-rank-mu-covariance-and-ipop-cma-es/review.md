# Scientific self-review of the rank-mu covariance component and original IPOP-CMA-ES

- Review: 20261015T062311Z-rank-mu-covariance-and-ipop-cma-es
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-15T06:19:45.948191Z
- Finished UTC: 2026-10-15T06:23:11.615879Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete two-target CMA-related cohort was reviewed through all 12 source-linked claims, definitions, source versions/access, qualified mappings and 17 limitations. Retain the original 2003 covariance component separately from the original 2005 whole restart algorithm with its specified 2004 base. No new concrete findings were identified within the declared source scope. Actual capture and required completed checks are bound. Both records remain DRAFT; no benchmark, implementation or global-convergence certification is implied.

## Scope And Provenance

Complete exact two-target coherent CMA component/whole-algorithm cohort; no population sampling or extrapolation to the rest of the repository.

Selection: Exact maintained IDs AIMech:CMARankMuCovarianceUpdate and AIMech:IPOPCMAES from actual cohort333 creation.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base a7303d92795cc371954c527372fce9117342d7b5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CMARankMuCovarianceUpdate | data/curated/CMARankMuCovarianceUpdate.yaml | maintained | CMA rank-mu covariance update |
| AIMech:IPOPCMAES | data/curated/IPOPCMAES.yaml | maintained | IPOP-CMA-ES |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:CMARankMuCovarianceUpdate, AIMech:IPOPCMAES | Actual command completed with exit 0; exact output is retained in its evidence receipt. |
| just vendored-check | passed | True | AIMech:CMARankMuCovarianceUpdate, AIMech:IPOPCMAES | Actual command completed with exit 0; exact output is retained in its evidence receipt. |
| uv run --locked aimech check-source | passed | True | AIMech:CMARankMuCovarianceUpdate, AIMech:IPOPCMAES | Actual command completed with exit 0; exact output is retained in its evidence receipt. |
| just render | passed | True | AIMech:CMARankMuCovarianceUpdate, AIMech:IPOPCMAES | Actual command completed with exit 0; exact output is retained in its evidence receipt. |
| just render-check | passed | True | AIMech:CMARankMuCovarianceUpdate, AIMech:IPOPCMAES | Actual command completed with exit 0; exact output is retained in its evidence receipt. |
| git diff --check | passed | True | AIMech:CMARankMuCovarianceUpdate, AIMech:IPOPCMAES | Actual command completed with exit 0; exact output is retained in its evidence receipt. |

## Scientific And Domain Assessments

### Claim selected-old-mean-second-moment

evidence: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

PDF4 Eq1–4 and PDF6 Eq10 use old-generation mean and scale, with an equal-weight average of individual step outer products. They do not center at the newly selected mean or replace individual moments by the mean-step outer product.

### Claim path-and-population-covariance-blend

evidence: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

PDF4 Eq5 and PDF6 Eq11 give the stated accumulated path and nonnegative blend. The new path is used in the same covariance update. Its component identity does not silently add the complete host optimizer.

### Claim blend-endpoints-and-host-boundary

evidence: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

PDF6 text after Eq11 and PDF8 Section6 identify alpha=1,0,1/mu and the three labels. PDF5 Section3 leaves global step-size adaptation unchanged. Treating the labels as configurations and leaving host exponentiation outside this component is supported.

### Claim rank-and-positive-definite-domain

evidence: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

Eq10 is a sum of positive outer products, giving rank at most min(mu,n), with equality only at the corresponding span. A positive retained coefficient of SPD C guarantees SPD for c_cov&lt;1. At c_cov=1 the vectors with positive weight must span. The claim labels this linear algebra rather than repeating unconditional source rank equality.

### Claim neutral-selection-and-path-initialization-scope

evidence: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

Independent zero-mean neutral steps with covariance C have E[Z]=C. With zero path and fixed C, the covariance of sqrt(mu)*mean(y) is C; the first path covariance is c_c(2-c_c)C. Substitution gives [1-c_cov*alpha*(1-c_c)^2]C. This is explicitly bounded first-step curator algebra, not certification of the source-cited 1998 result or an adaptive martingale theorem.

### Claim empirically-chosen-covariance-rate

evidence: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

PDF6 Eq12 has the stated alpha blend; PDF7 Section4 describes conservative fitting and trial-and-error Eq15. PDF8 gives lambda=4mu in the experiments. The record does not turn the empirical rate into a universal optimum or population ratio requirement.

### definition assessment

evidence: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

A narrow original 2003 equal-weight covariance-valued component, distinct from the complete CMA optimizer and later unequal/negative-weight variants.

### mapping assessment

grounding: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

The explicit covariance-valued input/output rule supports a qualified related_match to the pinned MathematicalFunction definition. It is neither scalar activation equivalence nor an upstream subclass assertion; host exp is outside this component.

### source assessment

provenance: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

The sole source is the19-page author-hosted 2003 article including courtesy cover. Printed page p is PDF p+1. Full-text access is availability; partial empirical/dependency audit remains explicit. Test-function errata are retained context rather than a covariance correction.

### limitations assessment

scope: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

All eight limitations preserve original equal weights/nonnegative blend, rank/SPD/conditioning boundaries, neutral/zero-path versus adaptive claims, old-mean centering, empirical-rate and complexity limits, large-population shrinkage/control issues, page offsets/source errata and historical identity scope.

### Concept boundary and current owner

identity: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

The actual maintained identity retains its accepted mathematical_method scope, no aliases, and original owner 200. Fresh identity notes are bound to actual root decisions. This support reads accepted historical identity notes; it does not replace the separately running current collection/root decision or assert fresh absence. Existing owner is retained.

### Retained limitation 1

scope: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

This record is restricted to the 2003 equal-weight selected-step moment and nonnegative path/moment blend. Arbitrary unequal or negative weights, active covariance updates, later safeguards, restart schemes, limited-memory variants and modern implementations are not established by this source scope. The alpha=1 endpoint recovers the source’s reviewed host rule without making the new component identical to the whole maintained 2001 CMA-ES algorithm.

### Retained limitation 2

scope: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

The source’s rank=min(mu,n) wording requires a generic full-span qualification. Degenerate supplied steps or finite precision can reduce rank. Positive-semidefinite arithmetic and a retained positive old-covariance coefficient do not guarantee good conditioning, stable eigendecompositions or an admissible numerical implementation. The boundary c_cov=1 requires adequate positive span; the ordinary positive-definite domain cannot be assumed there.

### Retained limitation 3

scope: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

The neutral-model expectation argument on PDF pp. 6–7 / printed pp. 5–6 does not establish conditional martingale behavior or stationarity throughout an adaptive optimization run. The zero-path first-step calculation is curator hand algebra under fixed C and independent neutral steps, not an author-issued erratum or a claim to have disproved the separate Hansen 1998 argument cited by the paper. That thesis proof was not acquired or audited here.

### Retained limitation 4

scope: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

The new term uses old-mean normalized individual steps. Replacing it by covariance around the selected mean, by an outer product of the selected mean step or by a generic elite maximum-likelihood covariance changes the rule. Connections to IGO or natural-gradient search require their own distribution, utility and finite-update assumptions; neither a first-order resemblance nor a shared Gaussian family makes these methods exact aliases.

### Retained limitation 5

scope: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

Equation 12 is an empirically selected rate, not a universal optimum. Reported time-complexity results count generations in the stated parallel experiments; they do not establish linear dense-matrix arithmetic, a universal speedup or a convergence guarantee. No numerical performance result or benchmark replication is imported.

### Retained limitation 6

scope: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

Section 7, PDF pp. 18–19 / printed pp. 17–18, reports excessive shrinkage of overall variance and difficulties with global step-size control for large populations and rates. Smaller covariance rates and covariance renormalization are discussed as possible responses, not silently added to this component as mandatory safeguards. Positive-definite covariance alone does not prevent these problems.

### Retained limitation 7

scope: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

The acquired article has 19 PDF pages including a courtesy cover; printed pages 1–18 therefore occur at PDF pages 2–19. Core formulas were inspected visually because native formula extraction is garbled. The author’s separately retained errata correct test-function separability and a summation index, not Equations 10–11. The full empirical table/figure analysis and cited theoretical dependencies were not audited; no general historical-priority claim is made.

### Retained limitation 8

scope: supported. Targets: AIMech:CMARankMuCovarianceUpdate.

The primary publication year and author-hosted copy are retained without inferring a publication day from file metadata. Initial sandbox DNS failures and separate successful acquisition retries remain in the source provenance. Historical research assessed 733 native and 442 pinned AIO records and associated this component with existing frontier owner 200. That dated scope is not a claim of current frontier absence. No author code, calculator, optimizer or benchmark was executed in that research.

### Claim weighted-gaussian-cma-inner-search

evidence: supported. Targets: AIMech:IPOPCMAES.

IPOP PDF2 Section2 explicitly fixes the cited 2004 weighted rank-mu CMA base. Baseline PDF3 Eq1–3 establishes independent Gaussian offspring, positive weighted selection, and path plus selected-displacement covariance terms. The record distinguishes search density from a predictive objective model.

### Claim inherited-cumulative-step-size-adaptation

evidence: supported. Targets: AIMech:IPOPCMAES.

Baseline PDF4 Eq4 uses delta=(m_new-m_old)/sigma_old whitened by B_old D_old^(-1) B_old^T, with sqrt(c_sigma(2-c_sigma)mu_eff), then Eq5 uses the updated path norm inside scalar exp. The claim accurately describes this recurrence without purporting to print every coefficient. Positive sigma preservation is restricted to finite exact-real exponents.

### Claim independent-population-doubling-restarts

evidence: supported. Targets: AIMech:IPOPCMAES.

IPOP PDF2 specifies independent restarts with population factor 2. Baseline PDF4 Eq6–8 and PDF5 footnote6 establish dependent defaults. Thus mu, weights, mu_eff and dependent rates are recomputed for each actual population; dimension-only c_c need not change. The finite budget prevents interpreting lambda_k as an infinite executed sequence.

### Claim corrected-local-restart-triggers

evidence: supported. Targets: AIMech:IPOPCMAES.

IPOP PDF3 stopping categories are read with its PDF1 and official-text erratum. Current v2 says at least one coordinate remains unchanged, matching the existential corrected condition. Numerical stopping is not global optimality. The retained TolX absolute-value and executable-budget ambiguities remain limitations.

### Claim fresh-initialization-and-overall-stopping

evidence: supported. Targets: AIMech:IPOPCMAES.

IPOP PDF3 Section3 specifies fresh uniform means, sigma0=(B-A)/2, the n*10^4 allowance and known-optimum error target; baseline PDF4 supplies identity covariance and zero paths. The record explicitly identifies these as evaluated configuration and separates local restart from overall termination.

### Claim original-whole-method-and-local-comparator-boundary

evidence: supported. Targets: AIMech:IPOPCMAES.

The original whole named method and its fixed2004 base are distinct from a host-independent controller and all CMA variants. Local PDF3–4 Section3 retains small-population independent attempts; PDF4 Section4 uses scale10^-2(B-A)/2. The 100-times scale difference prevents attributing comparisons solely to population growth. No BIPOP method claim is made.

### definition assessment

evidence: supported. Targets: AIMech:IPOPCMAES.

The original named whole 2005 IPOP algorithm includes the specified 2004 weighted/rank-mu/CSA base, independent doubling restarts and separate overall stopping.

### mapping assessment

grounding: supported. Targets: AIMech:IPOPCMAES.

Mandatory inherited scalar CSA in the fixed original base supports related_match ExponentialFunction. This is not based merely on writing population growth as2^k, and does not assert equivalence, subclass, activation or matrix exponential.

### source assessment

provenance: supported. Targets: AIMech:IPOPCMAES.

Four cited sources separate the 2005 IPOP paper, 2004 base, 2005 local comparison and author errata documentation. Publication years remain distinct from later PDF-build and HTTP dates. Author errata is correctly typed official_documentation/documentation and cited at claim level.

### limitations assessment

scope: supported. Targets: AIMech:IPOPCMAES.

All nine limitations preserve author errata, version-specific fixed base/multipliers, TolX and budget implementation gaps, whole-protocol invariance boundaries, finite-budget/global-performance limits, full-run versus heterogeneous-attempt runtime, baseline errata, unread BIPOP methods and separate historical scopes.

### Concept boundary and current owner

identity: supported. Targets: AIMech:IPOPCMAES.

The actual maintained identity retains its accepted algorithm scope, no aliases, and original owner 202. Fresh identity notes are bound to actual root decisions. This support reads accepted historical identity notes; it does not replace the separately running current collection/root decision or assert fresh absence. Existing owner is retained.

### Retained limitation 1

scope: supported. Targets: AIMech:IPOPCMAES.

The 2005 author-hosted copy includes an explicit no-effect-coordinate erratum, used above. Its separate author-hosted ERRATA text also reports that the F4 initial mean was mistakenly sampled with Xup rather than Xlow in the offset, and that boundary settings were omitted on some functions. The authors suggest limited or favorable effects of correction, but those effects were not reproduced. No numerical superiority or repaired benchmark result is curated.

### Retained limitation 2

scope: supported. Targets: AIMech:IPOPCMAES.

The original inner routine is the 2004 positive-weight rank-mu and evolution-path CMA-ES, not merely the maintained 2001 rank-one CMA description and not later active/negative-weight variants. The 2004 conclusion suggests a restart multiplier of 3; the concrete 2005 procedure chooses 2. The 2005 discussion of factors between 1.5 and 5 is heuristic context, not a proven optimal range or an identification of every such schedule with the original procedure.

### Retained limitation 3

scope: supported. Targets: AIMech:IPOPCMAES.

The literal small-path stopping prose says sigma*p_c is smaller than TolX in all components without explicitly printing absolute-value syntax. The draft retains the stopping category and does not claim a verified executable interpretation. The prose also does not fully specify partial-generation evaluation or budget overshoot behavior. The referenced cmaes.m version 2.35 was not acquired or executed.

### Retained limitation 4

scope: supported. Targets: AIMech:IPOPCMAES.

The fixed objective-value tolerance, known-optimum error target, coordinate no-effect checks, condition-number threshold, initialization box and boundary policy limit claims about the whole protocol. An increasing transformation that preserves rankings can change a numeric function-range stopping test. Corresponding transformations of inner distributions alone do not certify invariance of every configured restart run.

### Retained limitation 5

scope: supported. Targets: AIMech:IPOPCMAES.

Population growth changes the allocation of evaluations across attempts, but numerical stopping and a finite budget do not establish a global optimum, monotonic distribution quality or universal improvement over constant-population restarts. The source empirical comparison also changes initial scale. No optimizer, benchmark or author code was run for this draft.

### Retained limitation 6

scope: supported. Targets: AIMech:IPOPCMAES.

The success-runtime expression in the 2005 Section 3 concerns independent repetition of a complete algorithm with positive success probability. It must not be applied without qualification to heterogeneous internal IPOP attempts with changing populations. Table 2 on PDF p. 5 displays SP2=0 for some zero-success rows, although Equation 4 on PDF p. 3 divides by that estimated success probability; those entries are not evidence of zero expected runtime. No success-rate or expected-runtime result is claimed.

### Retained limitation 7

scope: supported. Targets: AIMech:IPOPCMAES.

The 2004 base-paper errata correct a benchmark penalty and identify the initialized point as the recombination mean. Source build dates and later author errata are distinct from the 2004 and 2005 publication years. The source version and acquisition records are retained; no complete certification of all baseline proofs, numerical safeguards or benchmark tables is asserted.

### Retained limitation 8

scope: supported. Targets: AIMech:IPOPCMAES.

The local-restart companion is cited only for the defining method and initialization comparison. BIPOP is retained solely as a separate unresolved boundary: its full primary methods were not read and no substantive BIPOP construction, equivalence or performance claim is made. Existing rank-mu, active-CMA and other source-family leads are not resolved by this one named algorithm.

### Retained limitation 9

scope: supported. Targets: AIMech:IPOPCMAES.

Supporting research read all nine pages of the IPOP author copy including its erratum, selected defining and discussion pages of the 2004 base, and the first four pages of the local-restart companion. Exact text/visual scopes and the narrower root reading are retained separately. The historical wrapper/no-match proposal is preserved; the current mapping follows the accepted whole-method scope. Identity and frontier checks remain bounded to their recorded snapshot and must be refreshed before curation.

### Captured bytes, report mirror, frontier and DRAFT status

consistency: supported. Targets: AIMech:CMARankMuCovarianceUpdate, AIMech:IPOPCMAES.

Both captured records equal the actual write payloads and report entries. Exact support hashes cover all 12 claims, mappings and 17 limitations. Only owners 200/202 changed; all 906 other main and 393 nested values remain exact, with no new leaves. Six required project/publication checks passed; saving and checking this new review remain separate.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:CMARankMuCovarianceUpdate, AIMech:IPOPCMAES. The rank-mu record is an original equal-weight covariance-valued component; IPOP is an independent population-doubling restart algorithm with a specified later weighted/rank-mu/CSA base. Component overlap does not establish identity, aliasing or a lump. Preserve both local IDs and their distinct qualified related mappings.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| captured-inputs | /private/tmp/aimech-cma-cohort333-capture.json | context_only | Actual canonical inspect output; every captured input hash rechecked. Inspection alone is not scientific approval. |
| postcapture-reading | /private/tmp/aimech-cma-cohort333-root-reading.json | context_only | Actual root full-target and evidence assessment after capture and completed checks; source scopes are separately stated. |
| scientific-support | /private/tmp/aimech-cma-cohort333-scientific-support-20261015/scientific-support.json | context_only | Same-author supporting assessment of all 12 accepted claims, definitions, mappings and 17 limitations, with exact selective primary readings. This preparation was not itself a canonical capture. |
| actual-write | /private/tmp/aimech-cma-cohort333-write.json | context_only | Actual creation receipt binds two records, report pair and history; no review or gate was claimed at creation. |
| discovery-report | research/discovery/20261015T061345Z-rank-mu-covariance-and-ipop-cma-es.json | context_only | Exact report entry payloads equal maintained YAML. Only owners 200/202 changed; all 906 other main and 393 nested objects are exact. Historical correction and source scopes remain preserved. |
| creation-history | history/reports/rank-mu-covariance-and-ipop-cma-es/2026-10-15T061357Z-codex-34bc26.yaml | context_only | Actual append-only CREATE sidecar; review completion and publication were later tasks. |
| pinned-aio | sources/aio/aio.json; AIO:MathematicalFunction and AIO:ExponentialFunction; retained candidate-specific alternatives and edges are in scientific support. | context_only | Exact pinned CLASS contexts support qualified related mappings, not upstream subclass or equivalence claims. |
| identity-assessment | /private/tmp/aimech-cohort333-current-identity-20261015/root-decisions.json | context_only | Actual root assessment binds the fresh four-checkout ignored/hidden-inclusive identity scans and owner200/202 decisions; this generator does not claim to have manually reread all search hits. |
| record-rank-mu | data/curated/CMARankMuCovarianceUpdate.yaml | supports | Complete maintained DRAFT record read by root after capture; all claim and evidence bytes matched the accepted scientific support. |
| src-hansen2003 | https://www.cmap.polytechnique.fr/~nikolaus.hansen/evco_11_1_1_0.pdf; Supporting fresh selected native PDF pages [4, 5, 6, 7, 8, 18, 19]; visuals [4, 6, 7] | supports | Evolutionary Computation 11(1):1–18, 2003; author-hosted typeset article with MIT courtesy cover, 19 PDF pages; printed page p is PDF p+1. Acquisition timestamp is access metadata, not a full-reading claim. The sole source is the19-page author-hosted 2003 article including courtesy cover. Printed page p is PDF p+1. Full-text access is availability; partial empirical/dependency audit remains explicit. Test-function errata are retained context rather than a covariance correction. |
| record-ipop | data/curated/IPOPCMAES.yaml | supports | Complete maintained DRAFT record read by root after capture; all claim and evidence bytes matched the accepted scientific support. |
| src-auger2005ipop | https://www.cmap.polytechnique.fr/~nikolaus.hansen/cec2005ipopcmaes.pdf; Supporting fresh selected native PDF pages [1, 2, 3]; visuals [3] | supports | 2005 IEEE Congress on Evolutionary Computation, volume 2, pp. 1769–1776. Retained author-hosted copy has one erratum cover and eight paper pages; its 2 May 2006 PDF build is not the publication date. PDF locators include the cover; paper-page locators exclude it. Acquisition timestamp is access metadata, not a full-reading claim. Four cited sources separate the 2005 IPOP paper, 2004 base, 2005 local comparison and author errata documentation. Publication years remain distinct from later PDF-build and HTTP dates. Author errata is correctly typed official_documentation/documentation and cited at claim level. |
| src-hansen2004 | https://www.cmap.polytechnique.fr/~nikolaus.hansen/ppsn2004hansenkern.pdf; Supporting fresh selected native PDF pages [1, 3, 4, 5]; visuals [4] | supports | Parallel Problem Solving from Nature–PPSN VIII, LNCS 3242, pp. 282–291 (2004). Retained author-hosted eleven-page copy has an erratum cover and ten article pages numbered 1–10; PDF build 24 October 2009 is file metadata, not publication year. Acquisition timestamp is access metadata, not a full-reading claim. Four cited sources separate the 2005 IPOP paper, 2004 base, 2005 local comparison and author errata documentation. Publication years remain distinct from later PDF-build and HTTP dates. Author errata is correctly typed official_documentation/documentation and cited at claim level. |
| src-auger2005local | https://www.cmap.polytechnique.fr/~nikolaus.hansen/cec2005localcmaes.pdf; Supporting fresh selected native PDF pages [3, 4]; visuals [4] | supports | 2005 IEEE Congress on Evolutionary Computation, pp. 1777–1784. Retained author-hosted copy has one erratum cover and eight paper pages; PDF build 2 May 2006 is not the publication date. Only the defining and comparison scope in the first four PDF pages is used here. Acquisition timestamp is access metadata, not a full-reading claim. Four cited sources separate the 2005 IPOP paper, 2004 base, 2005 local comparison and author errata documentation. Publication years remain distinct from later PDF-build and HTTP dates. Author errata is correctly typed official_documentation/documentation and cited at claim level. |
| src-ipop-author-errata | https://www.cmap.polytechnique.fr/~nikolaus.hansen/cec2005ipopcmaes.txt; Full official author abstract/ERRATA text; end-of-Section-2 noeffectcoord correction | supports | Undated author-hosted abstract and ERRATA text, retained on 15 October 2026. HTTP Last-Modified is 2 December 2009; it is access metadata, not a claimed publication date for each correction. Acquisition timestamp is access metadata, not a full-reading claim. Four cited sources separate the 2005 IPOP paper, 2004 base, 2005 local comparison and author errata documentation. Publication years remain distinct from later PDF-build and HTTP dates. Author errata is correctly typed official_documentation/documentation and cited at claim level. |
| check-gate | /private/tmp/aimech-cma-cohort333-check-gate.json | context_only | Actual completed command and retained output; this evidence predates saving the new review. |
| check-vendor | /private/tmp/aimech-cma-cohort333-check-vendor.json | context_only | Actual completed command and retained output; this evidence predates saving the new review. |
| check-check-source | /private/tmp/aimech-cma-cohort333-check-check-source.json | context_only | Actual completed command and retained output; this evidence predates saving the new review. |
| check-render | /private/tmp/aimech-cma-cohort333-check-render.json | context_only | Actual completed command and retained output; this evidence predates saving the new review. |
| check-render-check | /private/tmp/aimech-cma-cohort333-check-render-check.json | context_only | Actual completed command and retained output; this evidence predates saving the new review. |
| check-diff | /private/tmp/aimech-cma-cohort333-check-diff.json | context_only | Actual completed command and retained output; this evidence predates saving the new review. |

## Limits And Additional Notes

- Review is author self-review with attributed supporting agents, not independent approval. Full_text means source availability; fresh and retained selective reading scopes are explicit in supporting evidence and the root reading receipt.
- Root read the two complete canonical records after actual capture and all12 substantive support narratives, with all17 limitations and exact source metadata. Earlier actual root primary reading was rank-mu nativePDF4–7 and18–19 with visual5–6, IPOP native1–3 with visual3, base2004 native3–4 with visual4, local2005 native3–4 and complete author errata. Those retained scopes are not new per-page readings at this timestamp. The supporting scientific agent separately reread rank-mu4–8,18–19 with visuals4/6/7; IPOP1–3 with visual3; baseline1/3–5 with visual4; local3–4 with visual4 and officialerrata. No full empirical or dependency audit is claimed. Root also read all45 current grouped search contents and owner objects; canonical report comparisons verified only200/202changed,906othermain393nestedexact, with all31capturehashes exact.
- The rank/span and zero-initial-path expectations are bounded curator hand algebra; no original 1998 theory certification, full adaptive-process theorem or empirical replication is asserted. IPOP stopping/initialization/budget choices do not establish global optimality or whole-protocol invariance.
- The original IPOP v1 quantifier ambiguity was corrected and accepted before canonical creation. Its original module, preview, finding and v2 lineage remain context; there is no fabricated resolved formal finding or previous_occurrence for these targets. The rank-mu original no-match proposal and accepted mapping/wording successors likewise remain historical.
- No author code, calculator or benchmark was run by this review generator. The BIPOP full methods and other uninspected dependencies remain outside scope.
- Root owns the actual postcapture scientific judgment and fresh identity assessment. Mechanical hash and frontier equality checks do not themselves prove scientific truth or worldwide absence.
- Required checks reflect the actual completed logs for these bytes. Canonical validation/save and the saved-review collection check for this new review remain separate later actions. A passing review does not promote either DRAFT record or change the ontology.
- Retain two distinct identities: original2003 equal-weight covariance component with qualified MathematicalFunction relation and original2005 whole IPOP with fixed2004 CSA base and qualified ExponentialFunction relation. Claims, source locators and explicit rank/positivity/initialization/default/stopping/comparator limits are supported within these scopes. No new concrete defect found. OriginalTEMP IPOPambiguity and exactv2correction are historical precreation lineage, not a resolved formal finding. Allsix required check logs passed; records remain DRAFT, publication and newly savedreviewcheck remain later actions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T062311Z-rank-mu-covariance-and-ipop-cma-es
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of the rank-mu covariance component and original IPOP-CMA-ES
started_at: '2026-10-15T06:19:45.948191Z'
finished_at: '2026-10-15T06:23:11.615879Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Root author assessment with same-author supporting source and
    mathematical agents. No external or independent scientific approval is asserted.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete two-target CMA-related cohort was reviewed through all 12 source-linked
  claims, definitions, source versions/access, qualified mappings and 17 limitations.
  Retain the original 2003 covariance component separately from the original 2005
  whole restart algorithm with its specified 2004 base. No new concrete findings were
  identified within the declared source scope. Actual capture and required completed
  checks are bound. Both records remain DRAFT; no benchmark, implementation or global-convergence
  certification is implied.
source:
  git_revision: a7303d92795cc371954c527372fce9117342d7b5
  state: working_tree
  inputs:
  - path: .claude/skills/review-category/SKILL.md
    sha256: 553c3870c1dfc127f90f196b7b212b644706d4c26e2a578ab615ccce588070d7
    role: context
  - path: data/aio/ExponentialFunction.yaml
    sha256: a9e6fe9954dee5c61f799631c1892a99a891468e81e725e584d1a3dc06d84239
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/curated/AdaptationSampling.yaml
    sha256: 675a122fec61acc7b625d037a53d784420be2559e0aef6405dac91e50b762b27
    role: context
  - path: data/curated/CMARankMuCovarianceUpdate.yaml
    sha256: 67339de3e4309eac07d9e6e9c0f281b65e0e308e40508affdcd4859f6e1be7d3
    role: target
  - path: data/curated/CovarianceMatrixAdaptationEvolutionStrategy.yaml
    sha256: 7018c9916e78f34ba32a3a9d46e694d2a78c17a6e7222d9050d305eedf96ed06
    role: context
  - path: data/curated/CrossEntropyOptimization.yaml
    sha256: b2d993224f56b48738bbecc23df28fe0bc1e16e54c658979fdd28fc1924ba269
    role: context
  - path: data/curated/ExponentialNaturalEvolutionStrategies.yaml
    sha256: 8230e120126387ffb32405d2072fa5604e8cf39598972afcf5401c53730088b6
    role: context
  - path: data/curated/IPOPCMAES.yaml
    sha256: 7c70b1c160acfeec27d7d1603597c84eaf5db525ce96761512f4f575c9dd8752
    role: target
  - path: data/curated/InformationGeometricOptimization.yaml
    sha256: ef55808962485da0302293b2110ff61ed153c76b6e5da5c570f189dafc66282f
    role: context
  - path: data/curated/NaturalEvolutionStrategies.yaml
    sha256: b11c8d02da55175afcf5d5c11cf91a864418d7396b726f423f865d95cfe76a4c
    role: context
  - path: data/curated/NaturalGradient.yaml
    sha256: d082d3f17e9428d1765b8041ae6abecd604161b9d6d12082ef17b4d45255ce2b
    role: context
  - path: data/curated/PopulationBasedIncrementalLearning.yaml
    sha256: fb2500f70c8a0cf57639b33f7f89acf9f141adf75a238aa248e784afc09866d2
    role: context
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
  - path: history/reports/rank-mu-covariance-and-ipop-cma-es/2026-10-15T061357Z-codex-34bc26.yaml
    sha256: ea4c4d612037fac3283d1693e4fd54b4358d87bab78b88c2beaef175fb412f93
    role: context
  - path: justfile
    sha256: 2d9c1b68c1c80d53aa44a6b8b5e916efe8b493650ff59a3fc7479a42be37f400
    role: context
  - path: research/discovery/20261015T061345Z-rank-mu-covariance-and-ipop-cma-es.json
    sha256: 341f7750acb3cb6a2ca670c08c032529fa353c16587c40dc4a32690deb0dec54
    role: context
  - path: research/discovery/20261015T061345Z-rank-mu-covariance-and-ipop-cma-es.md
    sha256: 29ab1928cd438ed8d67b0d5eec3d5533cf56597459f6c571586685198f3ab4ac
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
  - path: src/aimech/validation.py
    sha256: 274ed5e6bc97440515a1964b9b21927135a2e9a5a4808ae8daebccd3e172ffcc
    role: context
scope:
  description: Complete exact two-target coherent CMA component/whole-algorithm cohort;
    no population sampling or extrapolation to the rest of the repository.
  selection: Exact maintained IDs AIMech:CMARankMuCovarianceUpdate and AIMech:IPOPCMAES
    from actual cohort333 creation.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  - AIMech:IPOPCMAES
  exclusions:
  - target: Other CMA/NES/IGO/active-CMA/BIPOP concepts and carried frontier entries
    reason: Context only; this review does not resolve their distinct method/source
      leads.
  - target: Author implementations, full benchmark analyses, uninspected pages and
      referenced theoretical dependencies
    reason: Outside the declared selective primary-source and bounded hand-algebra
      scope.
targets:
- target_id: AIMech:CMARankMuCovarianceUpdate
  path: data/curated/CMARankMuCovarianceUpdate.yaml
  label: CMA rank-mu covariance update
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CMARankMuCovarianceUpdate.yaml
    role: maintained native concept record
- target_id: AIMech:IPOPCMAES
  path: data/curated/IPOPCMAES.yaml
  label: IPOP-CMA-ES
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IPOPCMAES.yaml
    role: maintained native concept record
checks:
- check_id: check-gate
  name: just check
  status: passed
  required: true
  summary: Actual command completed with exit 0; exact output is retained in its evidence
    receipt.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  - AIMech:IPOPCMAES
  command: just check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-gate
- check_id: check-vendor
  name: just vendored-check
  status: passed
  required: true
  summary: Actual command completed with exit 0; exact output is retained in its evidence
    receipt.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  - AIMech:IPOPCMAES
  command: just vendored-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-vendor
- check_id: check-check-source
  name: uv run --locked aimech check-source
  status: passed
  required: true
  summary: Actual command completed with exit 0; exact output is retained in its evidence
    receipt.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  - AIMech:IPOPCMAES
  command: uv run --locked aimech check-source
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-check-source
- check_id: check-render
  name: just render
  status: passed
  required: true
  summary: Actual command completed with exit 0; exact output is retained in its evidence
    receipt.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  - AIMech:IPOPCMAES
  command: just render
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-render
- check_id: check-render-check
  name: just render-check
  status: passed
  required: true
  summary: Actual command completed with exit 0; exact output is retained in its evidence
    receipt.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  - AIMech:IPOPCMAES
  command: just render-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-render-check
- check_id: check-diff
  name: git diff --check
  status: passed
  required: true
  summary: Actual command completed with exit 0; exact output is retained in its evidence
    receipt.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  - AIMech:IPOPCMAES
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-diff
evidence:
- evidence_id: captured-inputs
  kind: record_content
  reference: /private/tmp/aimech-cma-cohort333-capture.json
  accessed_at: '2026-10-15T06:22:19.308320Z'
  support: context_only
  summary: Actual canonical inspect output; every captured input hash rechecked. Inspection
    alone is not scientific approval.
  snapshot_sha256: aa15738534b1f1fb248a33dfdd4e53281e4221201c7a86b4ccc8b3118d1e8ef9
- evidence_id: postcapture-reading
  kind: record_content
  reference: /private/tmp/aimech-cma-cohort333-root-reading.json
  accessed_at: '2026-10-15T06:22:19.308320Z'
  support: context_only
  summary: Actual root full-target and evidence assessment after capture and completed
    checks; source scopes are separately stated.
  snapshot_sha256: c70aec65b8cb56b00c4dbe37a4bb33cdc7bdf2578264987d2559af5573fe530e
- evidence_id: scientific-support
  kind: record_content
  reference: /private/tmp/aimech-cma-cohort333-scientific-support-20261015/scientific-support.json
  accessed_at: '2026-10-15T06:22:19.308320Z'
  support: context_only
  summary: Same-author supporting assessment of all 12 accepted claims, definitions,
    mappings and 17 limitations, with exact selective primary readings. This preparation
    was not itself a canonical capture.
  snapshot_sha256: c1b6f3c993afb7e256b65012320aec357577b231367c4a30e4101416be6b5ab1
- evidence_id: actual-write
  kind: record_content
  reference: /private/tmp/aimech-cma-cohort333-write.json
  accessed_at: '2026-10-15T06:22:19.308320Z'
  support: context_only
  summary: Actual creation receipt binds two records, report pair and history; no
    review or gate was claimed at creation.
  snapshot_sha256: eca16c40dd8b6239645414981578c9dc385eaf09e30738a5716f25fe489cd05c
- evidence_id: discovery-report
  kind: record_content
  reference: research/discovery/20261015T061345Z-rank-mu-covariance-and-ipop-cma-es.json
  accessed_at: '2026-10-15T06:22:19.308320Z'
  support: context_only
  summary: Exact report entry payloads equal maintained YAML. Only owners 200/202
    changed; all 906 other main and 393 nested objects are exact. Historical correction
    and source scopes remain preserved.
  snapshot_sha256: 341f7750acb3cb6a2ca670c08c032529fa353c16587c40dc4a32690deb0dec54
- evidence_id: creation-history
  kind: record_content
  reference: history/reports/rank-mu-covariance-and-ipop-cma-es/2026-10-15T061357Z-codex-34bc26.yaml
  accessed_at: '2026-10-15T06:22:19.308320Z'
  support: context_only
  summary: Actual append-only CREATE sidecar; review completion and publication were
    later tasks.
  snapshot_sha256: ea4c4d612037fac3283d1693e4fd54b4358d87bab78b88c2beaef175fb412f93
- evidence_id: pinned-aio
  kind: database
  reference: sources/aio/aio.json
  accessed_at: '2026-10-15T06:22:19.308320Z'
  support: context_only
  summary: Exact pinned CLASS contexts support qualified related mappings, not upstream
    subclass or equivalence claims.
  locator: AIO:MathematicalFunction and AIO:ExponentialFunction; retained candidate-specific
    alternatives and edges are in scientific support.
  snapshot_sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
- evidence_id: identity-assessment
  kind: search
  reference: /private/tmp/aimech-cohort333-current-identity-20261015/root-decisions.json
  accessed_at: '2026-10-15T06:22:19.308320Z'
  support: context_only
  summary: Actual root assessment binds the fresh four-checkout ignored/hidden-inclusive
    identity scans and owner200/202 decisions; this generator does not claim to have
    manually reread all search hits.
  snapshot_sha256: 47d334432b12106bf845bc41247b4d9570fd93062d67ab8c21d854c30858a957
  search_scope: Bounded four retained checkouts using rg --no-ignore --hidden --fixed-strings
    --word-regexp; exact current inventory and carried frontier. No global absence
    or saturation claim.
- evidence_id: record-rank-mu
  kind: record_content
  reference: data/curated/CMARankMuCovarianceUpdate.yaml
  accessed_at: '2026-10-15T06:22:19.308320Z'
  support: supports
  summary: Complete maintained DRAFT record read by root after capture; all claim
    and evidence bytes matched the accepted scientific support.
  snapshot_sha256: 67339de3e4309eac07d9e6e9c0f281b65e0e308e40508affdcd4859f6e1be7d3
- evidence_id: src-hansen2003
  kind: primary_source
  reference: https://www.cmap.polytechnique.fr/~nikolaus.hansen/evco_11_1_1_0.pdf
  accessed_at: '2026-10-15T05:12:47Z'
  support: supports
  summary: Evolutionary Computation 11(1):1–18, 2003; author-hosted typeset article
    with MIT courtesy cover, 19 PDF pages; printed page p is PDF p+1. Acquisition
    timestamp is access metadata, not a full-reading claim. The sole source is the19-page
    author-hosted 2003 article including courtesy cover. Printed page p is PDF p+1.
    Full-text access is availability; partial empirical/dependency audit remains explicit.
    Test-function errata are retained context rather than a covariance correction.
  locator: Supporting fresh selected native PDF pages [4, 5, 6, 7, 8, 18, 19]; visuals
    [4, 6, 7]
  snapshot_sha256: 1e3e35799fda200ca496998652182cf3da7c95e093b5c637930bca4ac72b60a6
- evidence_id: record-ipop
  kind: record_content
  reference: data/curated/IPOPCMAES.yaml
  accessed_at: '2026-10-15T06:22:19.308320Z'
  support: supports
  summary: Complete maintained DRAFT record read by root after capture; all claim
    and evidence bytes matched the accepted scientific support.
  snapshot_sha256: 7c70b1c160acfeec27d7d1603597c84eaf5db525ce96761512f4f575c9dd8752
- evidence_id: src-auger2005ipop
  kind: primary_source
  reference: https://www.cmap.polytechnique.fr/~nikolaus.hansen/cec2005ipopcmaes.pdf
  accessed_at: '2026-10-15T05:13:13Z'
  support: supports
  summary: 2005 IEEE Congress on Evolutionary Computation, volume 2, pp. 1769–1776.
    Retained author-hosted copy has one erratum cover and eight paper pages; its 2
    May 2006 PDF build is not the publication date. PDF locators include the cover;
    paper-page locators exclude it. Acquisition timestamp is access metadata, not
    a full-reading claim. Four cited sources separate the 2005 IPOP paper, 2004 base,
    2005 local comparison and author errata documentation. Publication years remain
    distinct from later PDF-build and HTTP dates. Author errata is correctly typed
    official_documentation/documentation and cited at claim level.
  locator: Supporting fresh selected native PDF pages [1, 2, 3]; visuals [3]
  snapshot_sha256: 67e91cca499d21c7fbd757f857aca24742788392b77abfa26a3d9c5b61a157b3
- evidence_id: src-hansen2004
  kind: primary_source
  reference: https://www.cmap.polytechnique.fr/~nikolaus.hansen/ppsn2004hansenkern.pdf
  accessed_at: '2026-10-15T05:16:17Z'
  support: supports
  summary: Parallel Problem Solving from Nature–PPSN VIII, LNCS 3242, pp. 282–291
    (2004). Retained author-hosted eleven-page copy has an erratum cover and ten article
    pages numbered 1–10; PDF build 24 October 2009 is file metadata, not publication
    year. Acquisition timestamp is access metadata, not a full-reading claim. Four
    cited sources separate the 2005 IPOP paper, 2004 base, 2005 local comparison and
    author errata documentation. Publication years remain distinct from later PDF-build
    and HTTP dates. Author errata is correctly typed official_documentation/documentation
    and cited at claim level.
  locator: Supporting fresh selected native PDF pages [1, 3, 4, 5]; visuals [4]
  snapshot_sha256: 81fb79a0bc916e9c4ce2440b727aafed85488622ec51eb2adbac4d3a4e5c4f38
- evidence_id: src-auger2005local
  kind: primary_source
  reference: https://www.cmap.polytechnique.fr/~nikolaus.hansen/cec2005localcmaes.pdf
  accessed_at: '2026-10-15T05:16:19Z'
  support: supports
  summary: 2005 IEEE Congress on Evolutionary Computation, pp. 1777–1784. Retained
    author-hosted copy has one erratum cover and eight paper pages; PDF build 2 May
    2006 is not the publication date. Only the defining and comparison scope in the
    first four PDF pages is used here. Acquisition timestamp is access metadata, not
    a full-reading claim. Four cited sources separate the 2005 IPOP paper, 2004 base,
    2005 local comparison and author errata documentation. Publication years remain
    distinct from later PDF-build and HTTP dates. Author errata is correctly typed
    official_documentation/documentation and cited at claim level.
  locator: Supporting fresh selected native PDF pages [3, 4]; visuals [4]
  snapshot_sha256: caefccd2984ed5cdd7d6754e079bf5069e7889f57417e0e46bd8bedda3de08a6
- evidence_id: src-ipop-author-errata
  kind: authority
  reference: https://www.cmap.polytechnique.fr/~nikolaus.hansen/cec2005ipopcmaes.txt
  accessed_at: '2026-10-15T05:16:15Z'
  support: supports
  summary: Undated author-hosted abstract and ERRATA text, retained on 15 October
    2026. HTTP Last-Modified is 2 December 2009; it is access metadata, not a claimed
    publication date for each correction. Acquisition timestamp is access metadata,
    not a full-reading claim. Four cited sources separate the 2005 IPOP paper, 2004
    base, 2005 local comparison and author errata documentation. Publication years
    remain distinct from later PDF-build and HTTP dates. Author errata is correctly
    typed official_documentation/documentation and cited at claim level.
  locator: Full official author abstract/ERRATA text; end-of-Section-2 noeffectcoord
    correction
  snapshot_sha256: addac47190bcbdf2a2f1d4c6c45cbc9e5f11ecf1054167bef9a19ac3594fde4a
- evidence_id: check-gate
  kind: validation
  reference: /private/tmp/aimech-cma-cohort333-check-gate.json
  accessed_at: '2026-10-15T06:21:26.416337Z'
  support: context_only
  summary: Actual completed command and retained output; this evidence predates saving
    the new review.
  snapshot_sha256: c2db675c9085f479844fbe8c4b4fdacc9bc9aab5a1af6ce88eed1381e0a9620b
- evidence_id: check-vendor
  kind: validation
  reference: /private/tmp/aimech-cma-cohort333-check-vendor.json
  accessed_at: '2026-10-15T06:14:31.971825Z'
  support: context_only
  summary: Actual completed command and retained output; this evidence predates saving
    the new review.
  snapshot_sha256: e537174afac6c65115290f703ab7fc6fcc814c30f8bde0e0ae2ae72269c82074
- evidence_id: check-check-source
  kind: validation
  reference: /private/tmp/aimech-cma-cohort333-check-check-source.json
  accessed_at: '2026-10-15T06:14:47.179380Z'
  support: context_only
  summary: Actual completed command and retained output; this evidence predates saving
    the new review.
  snapshot_sha256: e52c7608aad8579289dfe88bf7b174728ea49e127ab6408fd6d05c07a517f1f1
- evidence_id: check-render
  kind: validation
  reference: /private/tmp/aimech-cma-cohort333-check-render.json
  accessed_at: '2026-10-15T06:14:49.156918Z'
  support: context_only
  summary: Actual completed command and retained output; this evidence predates saving
    the new review.
  snapshot_sha256: 035fc8976b14d61f2b58ead86fe88a2bcb025133a15dc875a715fef9b9919814
- evidence_id: check-render-check
  kind: validation
  reference: /private/tmp/aimech-cma-cohort333-check-render-check.json
  accessed_at: '2026-10-15T06:16:01.236971Z'
  support: context_only
  summary: Actual completed command and retained output; this evidence predates saving
    the new review.
  snapshot_sha256: d0198a9072b5b80f8aeac451523dcc134898df3da9ec9af004ee5d4ef168ea45
- evidence_id: check-diff
  kind: validation
  reference: /private/tmp/aimech-cma-cohort333-check-diff.json
  accessed_at: '2026-10-15T06:15:46.154828Z'
  support: context_only
  summary: Actual completed command and retained output; this evidence predates saving
    the new review.
  snapshot_sha256: 531f565f8390a57f041f6f087e8a15564868e1c9723122dd58d77937f5217e0c
assessments:
- assessment_id: rank-mu-selected-old-mean-second-moment
  area: evidence
  topic: Claim selected-old-mean-second-moment
  outcome: supported
  summary: PDF4 Eq1–4 and PDF6 Eq10 use old-generation mean and scale, with an equal-weight
    average of individual step outer products. They do not center at the newly selected
    mean or replace individual moments by the mean-step outer product.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-path-and-population-covariance-blend
  area: evidence
  topic: Claim path-and-population-covariance-blend
  outcome: supported
  summary: PDF4 Eq5 and PDF6 Eq11 give the stated accumulated path and nonnegative
    blend. The new path is used in the same covariance update. Its component identity
    does not silently add the complete host optimizer.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-blend-endpoints-and-host-boundary
  area: evidence
  topic: Claim blend-endpoints-and-host-boundary
  outcome: supported
  summary: PDF6 text after Eq11 and PDF8 Section6 identify alpha=1,0,1/mu and the
    three labels. PDF5 Section3 leaves global step-size adaptation unchanged. Treating
    the labels as configurations and leaving host exponentiation outside this component
    is supported.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-rank-and-positive-definite-domain
  area: evidence
  topic: Claim rank-and-positive-definite-domain
  outcome: supported
  summary: Eq10 is a sum of positive outer products, giving rank at most min(mu,n),
    with equality only at the corresponding span. A positive retained coefficient
    of SPD C guarantees SPD for c_cov<1. At c_cov=1 the vectors with positive weight
    must span. The claim labels this linear algebra rather than repeating unconditional
    source rank equality.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-neutral-selection-and-path-initialization-scope
  area: evidence
  topic: Claim neutral-selection-and-path-initialization-scope
  outcome: supported
  summary: Independent zero-mean neutral steps with covariance C have E[Z]=C. With
    zero path and fixed C, the covariance of sqrt(mu)*mean(y) is C; the first path
    covariance is c_c(2-c_c)C. Substitution gives [1-c_cov*alpha*(1-c_c)^2]C. This
    is explicitly bounded first-step curator algebra, not certification of the source-cited
    1998 result or an adaptive martingale theorem.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-empirically-chosen-covariance-rate
  area: evidence
  topic: Claim empirically-chosen-covariance-rate
  outcome: supported
  summary: PDF6 Eq12 has the stated alpha blend; PDF7 Section4 describes conservative
    fitting and trial-and-error Eq15. PDF8 gives lambda=4mu in the experiments. The
    record does not turn the empirical rate into a universal optimum or population
    ratio requirement.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: A narrow original 2003 equal-weight covariance-valued component, distinct
    from the complete CMA optimizer and later unequal/negative-weight variants.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: The explicit covariance-valued input/output rule supports a qualified related_match
    to the pinned MathematicalFunction definition. It is neither scalar activation
    equivalence nor an upstream subclass assertion; host exp is outside this component.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - pinned-aio
- assessment_id: rank-mu-source-assessment
  area: provenance
  topic: source assessment
  outcome: supported
  summary: The sole source is the19-page author-hosted 2003 article including courtesy
    cover. Printed page p is PDF p+1. Full-text access is availability; partial empirical/dependency
    audit remains explicit. Test-function errata are retained context rather than
    a covariance correction.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-limitations-assessment
  area: scope
  topic: limitations assessment
  outcome: supported
  summary: All eight limitations preserve original equal weights/nonnegative blend,
    rank/SPD/conditioning boundaries, neutral/zero-path versus adaptive claims, old-mean
    centering, empirical-rate and complexity limits, large-population shrinkage/control
    issues, page offsets/source errata and historical identity scope.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-identity
  area: identity
  topic: Concept boundary and current owner
  outcome: supported
  summary: The actual maintained identity retains its accepted mathematical_method
    scope, no aliases, and original owner 200. Fresh identity notes are bound to actual
    root decisions. This support reads accepted historical identity notes; it does
    not replace the separately running current collection/root decision or assert
    fresh absence. Existing owner is retained.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - identity-assessment
  - postcapture-reading
- assessment_id: rank-mu-limitation-1
  area: scope
  topic: Retained limitation 1
  outcome: supported
  summary: This record is restricted to the 2003 equal-weight selected-step moment
    and nonnegative path/moment blend. Arbitrary unequal or negative weights, active
    covariance updates, later safeguards, restart schemes, limited-memory variants
    and modern implementations are not established by this source scope. The alpha=1
    endpoint recovers the source’s reviewed host rule without making the new component
    identical to the whole maintained 2001 CMA-ES algorithm.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-limitation-2
  area: scope
  topic: Retained limitation 2
  outcome: supported
  summary: The source’s rank=min(mu,n) wording requires a generic full-span qualification.
    Degenerate supplied steps or finite precision can reduce rank. Positive-semidefinite
    arithmetic and a retained positive old-covariance coefficient do not guarantee
    good conditioning, stable eigendecompositions or an admissible numerical implementation.
    The boundary c_cov=1 requires adequate positive span; the ordinary positive-definite
    domain cannot be assumed there.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-limitation-3
  area: scope
  topic: Retained limitation 3
  outcome: supported
  summary: The neutral-model expectation argument on PDF pp. 6–7 / printed pp. 5–6
    does not establish conditional martingale behavior or stationarity throughout
    an adaptive optimization run. The zero-path first-step calculation is curator
    hand algebra under fixed C and independent neutral steps, not an author-issued
    erratum or a claim to have disproved the separate Hansen 1998 argument cited by
    the paper. That thesis proof was not acquired or audited here.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-limitation-4
  area: scope
  topic: Retained limitation 4
  outcome: supported
  summary: The new term uses old-mean normalized individual steps. Replacing it by
    covariance around the selected mean, by an outer product of the selected mean
    step or by a generic elite maximum-likelihood covariance changes the rule. Connections
    to IGO or natural-gradient search require their own distribution, utility and
    finite-update assumptions; neither a first-order resemblance nor a shared Gaussian
    family makes these methods exact aliases.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-limitation-5
  area: scope
  topic: Retained limitation 5
  outcome: supported
  summary: Equation 12 is an empirically selected rate, not a universal optimum. Reported
    time-complexity results count generations in the stated parallel experiments;
    they do not establish linear dense-matrix arithmetic, a universal speedup or a
    convergence guarantee. No numerical performance result or benchmark replication
    is imported.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-limitation-6
  area: scope
  topic: Retained limitation 6
  outcome: supported
  summary: Section 7, PDF pp. 18–19 / printed pp. 17–18, reports excessive shrinkage
    of overall variance and difficulties with global step-size control for large populations
    and rates. Smaller covariance rates and covariance renormalization are discussed
    as possible responses, not silently added to this component as mandatory safeguards.
    Positive-definite covariance alone does not prevent these problems.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-limitation-7
  area: scope
  topic: Retained limitation 7
  outcome: supported
  summary: The acquired article has 19 PDF pages including a courtesy cover; printed
    pages 1–18 therefore occur at PDF pages 2–19. Core formulas were inspected visually
    because native formula extraction is garbled. The author’s separately retained
    errata correct test-function separability and a summation index, not Equations
    10–11. The full empirical table/figure analysis and cited theoretical dependencies
    were not audited; no general historical-priority claim is made.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: rank-mu-limitation-8
  area: scope
  topic: Retained limitation 8
  outcome: supported
  summary: The primary publication year and author-hosted copy are retained without
    inferring a publication day from file metadata. Initial sandbox DNS failures and
    separate successful acquisition retries remain in the source provenance. Historical
    research assessed 733 native and 442 pinned AIO records and associated this component
    with existing frontier owner 200. That dated scope is not a claim of current frontier
    absence. No author code, calculator, optimizer or benchmark was executed in that
    research.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  evidence_ids:
  - record-rank-mu
  - scientific-support
  - src-hansen2003
- assessment_id: ipop-weighted-gaussian-cma-inner-search
  area: evidence
  topic: Claim weighted-gaussian-cma-inner-search
  outcome: supported
  summary: IPOP PDF2 Section2 explicitly fixes the cited 2004 weighted rank-mu CMA
    base. Baseline PDF3 Eq1–3 establishes independent Gaussian offspring, positive
    weighted selection, and path plus selected-displacement covariance terms. The
    record distinguishes search density from a predictive objective model.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
- assessment_id: ipop-inherited-cumulative-step-size-adaptation
  area: evidence
  topic: Claim inherited-cumulative-step-size-adaptation
  outcome: supported
  summary: Baseline PDF4 Eq4 uses delta=(m_new-m_old)/sigma_old whitened by B_old
    D_old^(-1) B_old^T, with sqrt(c_sigma(2-c_sigma)mu_eff), then Eq5 uses the updated
    path norm inside scalar exp. The claim accurately describes this recurrence without
    purporting to print every coefficient. Positive sigma preservation is restricted
    to finite exact-real exponents.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
- assessment_id: ipop-independent-population-doubling-restarts
  area: evidence
  topic: Claim independent-population-doubling-restarts
  outcome: supported
  summary: IPOP PDF2 specifies independent restarts with population factor 2. Baseline
    PDF4 Eq6–8 and PDF5 footnote6 establish dependent defaults. Thus mu, weights,
    mu_eff and dependent rates are recomputed for each actual population; dimension-only
    c_c need not change. The finite budget prevents interpreting lambda_k as an infinite
    executed sequence.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
- assessment_id: ipop-corrected-local-restart-triggers
  area: evidence
  topic: Claim corrected-local-restart-triggers
  outcome: supported
  summary: IPOP PDF3 stopping categories are read with its PDF1 and official-text
    erratum. Current v2 says at least one coordinate remains unchanged, matching the
    existential corrected condition. Numerical stopping is not global optimality.
    The retained TolX absolute-value and executable-budget ambiguities remain limitations.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-ipop-author-errata
- assessment_id: ipop-fresh-initialization-and-overall-stopping
  area: evidence
  topic: Claim fresh-initialization-and-overall-stopping
  outcome: supported
  summary: IPOP PDF3 Section3 specifies fresh uniform means, sigma0=(B-A)/2, the n*10^4
    allowance and known-optimum error target; baseline PDF4 supplies identity covariance
    and zero paths. The record explicitly identifies these as evaluated configuration
    and separates local restart from overall termination.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
- assessment_id: ipop-original-whole-method-and-local-comparator-boundary
  area: evidence
  topic: Claim original-whole-method-and-local-comparator-boundary
  outcome: supported
  summary: The original whole named method and its fixed2004 base are distinct from
    a host-independent controller and all CMA variants. Local PDF3–4 Section3 retains
    small-population independent attempts; PDF4 Section4 uses scale10^-2(B-A)/2. The
    100-times scale difference prevents attributing comparisons solely to population
    growth. No BIPOP method claim is made.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-auger2005local
- assessment_id: ipop-definition-assessment
  area: evidence
  topic: definition assessment
  outcome: supported
  summary: The original named whole 2005 IPOP algorithm includes the specified 2004
    weighted/rank-mu/CSA base, independent doubling restarts and separate overall
    stopping.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
  - src-auger2005local
  - src-ipop-author-errata
- assessment_id: ipop-mapping-assessment
  area: grounding
  topic: mapping assessment
  outcome: supported
  summary: Mandatory inherited scalar CSA in the fixed original base supports related_match
    ExponentialFunction. This is not based merely on writing population growth as2^k,
    and does not assert equivalence, subclass, activation or matrix exponential.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - pinned-aio
- assessment_id: ipop-source-assessment
  area: provenance
  topic: source assessment
  outcome: supported
  summary: Four cited sources separate the 2005 IPOP paper, 2004 base, 2005 local
    comparison and author errata documentation. Publication years remain distinct
    from later PDF-build and HTTP dates. Author errata is correctly typed official_documentation/documentation
    and cited at claim level.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
  - src-auger2005local
  - src-ipop-author-errata
- assessment_id: ipop-limitations-assessment
  area: scope
  topic: limitations assessment
  outcome: supported
  summary: All nine limitations preserve author errata, version-specific fixed base/multipliers,
    TolX and budget implementation gaps, whole-protocol invariance boundaries, finite-budget/global-performance
    limits, full-run versus heterogeneous-attempt runtime, baseline errata, unread
    BIPOP methods and separate historical scopes.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
  - src-auger2005local
  - src-ipop-author-errata
- assessment_id: ipop-identity
  area: identity
  topic: Concept boundary and current owner
  outcome: supported
  summary: The actual maintained identity retains its accepted algorithm scope, no
    aliases, and original owner 202. Fresh identity notes are bound to actual root
    decisions. This support reads accepted historical identity notes; it does not
    replace the separately running current collection/root decision or assert fresh
    absence. Existing owner is retained.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - identity-assessment
  - postcapture-reading
- assessment_id: ipop-limitation-1
  area: scope
  topic: Retained limitation 1
  outcome: supported
  summary: The 2005 author-hosted copy includes an explicit no-effect-coordinate erratum,
    used above. Its separate author-hosted ERRATA text also reports that the F4 initial
    mean was mistakenly sampled with Xup rather than Xlow in the offset, and that
    boundary settings were omitted on some functions. The authors suggest limited
    or favorable effects of correction, but those effects were not reproduced. No
    numerical superiority or repaired benchmark result is curated.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
  - src-auger2005local
  - src-ipop-author-errata
- assessment_id: ipop-limitation-2
  area: scope
  topic: Retained limitation 2
  outcome: supported
  summary: The original inner routine is the 2004 positive-weight rank-mu and evolution-path
    CMA-ES, not merely the maintained 2001 rank-one CMA description and not later
    active/negative-weight variants. The 2004 conclusion suggests a restart multiplier
    of 3; the concrete 2005 procedure chooses 2. The 2005 discussion of factors between
    1.5 and 5 is heuristic context, not a proven optimal range or an identification
    of every such schedule with the original procedure.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
  - src-auger2005local
  - src-ipop-author-errata
- assessment_id: ipop-limitation-3
  area: scope
  topic: Retained limitation 3
  outcome: supported
  summary: The literal small-path stopping prose says sigma*p_c is smaller than TolX
    in all components without explicitly printing absolute-value syntax. The draft
    retains the stopping category and does not claim a verified executable interpretation.
    The prose also does not fully specify partial-generation evaluation or budget
    overshoot behavior. The referenced cmaes.m version 2.35 was not acquired or executed.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
  - src-auger2005local
  - src-ipop-author-errata
- assessment_id: ipop-limitation-4
  area: scope
  topic: Retained limitation 4
  outcome: supported
  summary: The fixed objective-value tolerance, known-optimum error target, coordinate
    no-effect checks, condition-number threshold, initialization box and boundary
    policy limit claims about the whole protocol. An increasing transformation that
    preserves rankings can change a numeric function-range stopping test. Corresponding
    transformations of inner distributions alone do not certify invariance of every
    configured restart run.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
  - src-auger2005local
  - src-ipop-author-errata
- assessment_id: ipop-limitation-5
  area: scope
  topic: Retained limitation 5
  outcome: supported
  summary: Population growth changes the allocation of evaluations across attempts,
    but numerical stopping and a finite budget do not establish a global optimum,
    monotonic distribution quality or universal improvement over constant-population
    restarts. The source empirical comparison also changes initial scale. No optimizer,
    benchmark or author code was run for this draft.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
  - src-auger2005local
  - src-ipop-author-errata
- assessment_id: ipop-limitation-6
  area: scope
  topic: Retained limitation 6
  outcome: supported
  summary: The success-runtime expression in the 2005 Section 3 concerns independent
    repetition of a complete algorithm with positive success probability. It must
    not be applied without qualification to heterogeneous internal IPOP attempts with
    changing populations. Table 2 on PDF p. 5 displays SP2=0 for some zero-success
    rows, although Equation 4 on PDF p. 3 divides by that estimated success probability;
    those entries are not evidence of zero expected runtime. No success-rate or expected-runtime
    result is claimed.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
  - src-auger2005local
  - src-ipop-author-errata
- assessment_id: ipop-limitation-7
  area: scope
  topic: Retained limitation 7
  outcome: supported
  summary: The 2004 base-paper errata correct a benchmark penalty and identify the
    initialized point as the recombination mean. Source build dates and later author
    errata are distinct from the 2004 and 2005 publication years. The source version
    and acquisition records are retained; no complete certification of all baseline
    proofs, numerical safeguards or benchmark tables is asserted.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
  - src-auger2005local
  - src-ipop-author-errata
- assessment_id: ipop-limitation-8
  area: scope
  topic: Retained limitation 8
  outcome: supported
  summary: 'The local-restart companion is cited only for the defining method and
    initialization comparison. BIPOP is retained solely as a separate unresolved boundary:
    its full primary methods were not read and no substantive BIPOP construction,
    equivalence or performance claim is made. Existing rank-mu, active-CMA and other
    source-family leads are not resolved by this one named algorithm.'
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
  - src-auger2005local
  - src-ipop-author-errata
- assessment_id: ipop-limitation-9
  area: scope
  topic: Retained limitation 9
  outcome: supported
  summary: Supporting research read all nine pages of the IPOP author copy including
    its erratum, selected defining and discussion pages of the 2004 base, and the
    first four pages of the local-restart companion. Exact text/visual scopes and
    the narrower root reading are retained separately. The historical wrapper/no-match
    proposal is preserved; the current mapping follows the accepted whole-method scope.
    Identity and frontier checks remain bounded to their recorded snapshot and must
    be refreshed before curation.
  target_ids:
  - AIMech:IPOPCMAES
  evidence_ids:
  - record-ipop
  - scientific-support
  - src-auger2005ipop
  - src-hansen2004
  - src-auger2005local
  - src-ipop-author-errata
- assessment_id: actual-correspondence
  area: consistency
  topic: Captured bytes, report mirror, frontier and DRAFT status
  outcome: supported
  summary: Both captured records equal the actual write payloads and report entries.
    Exact support hashes cover all 12 claims, mappings and 17 limitations. Only owners
    200/202 changed; all 906 other main and 393 nested values remain exact, with no
    new leaves. Six required project/publication checks passed; saving and checking
    this new review remain separate.
  target_ids:
  - AIMech:CMARankMuCovarianceUpdate
  - AIMech:IPOPCMAES
  evidence_ids:
  - captured-inputs
  - postcapture-reading
  - discovery-report
  - creation-history
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
  - AIMech:CMARankMuCovarianceUpdate
  - AIMech:IPOPCMAES
  rationale: The rank-mu record is an original equal-weight covariance-valued component;
    IPOP is an independent population-doubling restart algorithm with a specified
    later weighted/rank-mu/CSA base. Component overlap does not establish identity,
    aliasing or a lump. Preserve both local IDs and their distinct qualified related
    mappings.
  evidence_ids:
  - record-rank-mu
  - record-ipop
  - src-hansen2003
  - src-auger2005ipop
  - src-hansen2004
  - pinned-aio
limitations:
- Review is author self-review with attributed supporting agents, not independent
  approval. Full_text means source availability; fresh and retained selective reading
  scopes are explicit in supporting evidence and the root reading receipt.
- Root read the two complete canonical records after actual capture and all12 substantive
  support narratives, with all17 limitations and exact source metadata. Earlier actual
  root primary reading was rank-mu nativePDF4–7 and18–19 with visual5–6, IPOP native1–3
  with visual3, base2004 native3–4 with visual4, local2005 native3–4 and complete
  author errata. Those retained scopes are not new per-page readings at this timestamp.
  The supporting scientific agent separately reread rank-mu4–8,18–19 with visuals4/6/7;
  IPOP1–3 with visual3; baseline1/3–5 with visual4; local3–4 with visual4 and officialerrata.
  No full empirical or dependency audit is claimed. Root also read all45 current grouped
  search contents and owner objects; canonical report comparisons verified only200/202changed,906othermain393nestedexact,
  with all31capturehashes exact.
- The rank/span and zero-initial-path expectations are bounded curator hand algebra;
  no original 1998 theory certification, full adaptive-process theorem or empirical
  replication is asserted. IPOP stopping/initialization/budget choices do not establish
  global optimality or whole-protocol invariance.
- The original IPOP v1 quantifier ambiguity was corrected and accepted before canonical
  creation. Its original module, preview, finding and v2 lineage remain context; there
  is no fabricated resolved formal finding or previous_occurrence for these targets.
  The rank-mu original no-match proposal and accepted mapping/wording successors likewise
  remain historical.
- No author code, calculator or benchmark was run by this review generator. The BIPOP
  full methods and other uninspected dependencies remain outside scope.
- Root owns the actual postcapture scientific judgment and fresh identity assessment.
  Mechanical hash and frontier equality checks do not themselves prove scientific
  truth or worldwide absence.
- Required checks reflect the actual completed logs for these bytes. Canonical validation/save
  and the saved-review collection check for this new review remain separate later
  actions. A passing review does not promote either DRAFT record or change the ontology.
notes:
- 'Retain two distinct identities: original2003 equal-weight covariance component
  with qualified MathematicalFunction relation and original2005 whole IPOP with fixed2004
  CSA base and qualified ExponentialFunction relation. Claims, source locators and
  explicit rank/positivity/initialization/default/stopping/comparator limits are supported
  within these scopes. No new concrete defect found. OriginalTEMP IPOPambiguity and
  exactv2correction are historical precreation lineage, not a resolved formal finding.
  Allsix required check logs passed; records remain DRAFT, publication and newly savedreviewcheck
  remain later actions.'
tags:
- scientific-review
- self-review
- cma
- source-scoped
```
