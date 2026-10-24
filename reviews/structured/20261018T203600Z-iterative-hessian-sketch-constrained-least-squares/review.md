# Scientific author self-review of Iterative Hessian Sketch for constrained least-squares and information-theoretic classical sketching lower bounds

- Review: 20261018T203600Z-iterative-hessian-sketch-constrained-least-squares
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-18T20:35:00Z
- Finished UTC: 2026-10-18T20:36:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Iterative Hessian Sketch for Constrained Least-Squares and Information-Theoretic Classical Sketching Lower Bounds as a distinct DRAFT mathematical_method with narrow LinearRegression and related LassoRegression mappings. All three claims and locators across Pilanci &amp; Wainwright (2016, JMLR 17(53):1-38, arXiv:1411.0347v1) are supported with explicit multi-pass matrix-vector product and restricted-eigenvalue tangent-cone limitations.

## Scope And Provenance

All fields of the exact maintained IterativeHessianSketchForConstrainedLeastSquares record and its primary evidence.

Selection: Exact maintained ID: AIMech:IterativeHessianSketchForConstrainedLeastSquares
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14162a23d4c5c5da529c4ba462cc05fa51e05fdb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:IterativeHessianSketchForConstrainedLeastSquares | data/curated/IterativeHessianSketchForConstrainedLeastSquares.yaml | maintained | Iterative Hessian Sketch for Constrained Least-Squares and Information-Theoretic Classical Sketching Lower Bounds |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:IterativeHessianSketchForConstrainedLeastSquares | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:IterativeHessianSketchForConstrainedLeastSquares | All 621 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:IterativeHessianSketchForConstrainedLeastSquares | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:IterativeHessianSketchForConstrainedLeastSquares | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:IterativeHessianSketchForConstrainedLeastSquares | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:IterativeHessianSketchForConstrainedLeastSquares | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:IterativeHessianSketchForConstrainedLeastSquares | Exited 0 without output. |
| Constructed Pilanci &amp; Wainwright 2016 Iterative Hessian Sketch and classical sketch lower-bound checks | passed | True | AIMech:IterativeHessianSketchForConstrainedLeastSquares | {<br>  "concept_id": "AIMech:IterativeHessianSketchForConstrainedLeastSquares",<br>  "all_passed": true,<br>  "unconstrained_ihs_and_theorem1_2": {<br>    "passed": true,<br>    "ols_stat_err": 0.04088827677040154,<br>    "ihs_stat_err": 0.04109504420070216,<br>    "classical_stat_err": 0.12727772242146404,<br>    "ihs_ols_gap": 0.0003819292885153705,<br>    "classical_ols_gap": 0.11646909834560103,<br>    "theorem2_product_bound": 0.12175253124797426,<br>    "all_step_inequalities_39_passed": true<br>  },<br>  "sparse_l1_constrained_ihs": {<br>    "passed": true,<br>    "initial_gap": 1.4140436263049643,<br>    "round1_gap": 0.28177805056510624,<br>    "final_gap": 0.011687177300639338<br>  }<br>} |

## Scientific And Domain Assessments

### Distinctness of Iterative Hessian Sketch for constrained least-squares and information-theoretic classical sketching lower bounds

identity: supported. Targets: AIMech:IterativeHessianSketchForConstrainedLeastSquares.

Distinct from Newton Sketch for general twice-differentiable and self-concordant barrier optimization, hybrid CountSketch-leverage regression, and accelerated statistically preconditioned unconstrained sketching.

Confirmed via normalized identity check and full-text reading of Pilanci &amp; Wainwright (2016, arXiv:1411.0347v1).

### AIO mappings for AIMech:IterativeHessianSketchForConstrainedLeastSquares

grounding: supported. Targets: AIMech:IterativeHessianSketchForConstrainedLeastSquares.

narrow_match to AIO:LinearRegression and related_match to AIO:LassoRegression are accurate.

Pinned AIO (2026-07-22) contains LinearRegression and LassoRegression broadly without Fano lower bounds for classical sketching or tangent-cone Gaussian-width Iterative Hessian Sketch guarantees.

### Definition and scope

evidence: supported. Targets: AIMech:IterativeHessianSketchForConstrainedLeastSquares.

Definition accurately captures the Theorem 1 Fano lower bound for classical sketching, the Equation (24) IHS update, Theorem 2 tangent-cone contraction, and Corollary 1 minimax risk matching.

All equations and claims verified against Sections 1-5 and Appendices A-E of arXiv:1411.0347v1.

### fano-information-theoretic-lower-bound-for-classical-sketching

evidence: supported. Targets: AIMech:IterativeHessianSketchForConstrainedLeastSquares.

Supported by Section 2.2 (Theorem 1, Examples 1-3), Appendix A (Lemma 2), and boundary script.

Verified classical sketching prediction error inflation (0.127278 vs. 0.040888 for OLS and 0.041095 for IHS).

### hessian-sketch-tangent-cone-contraction-and-iterative-hessian-sketch

evidence: supported. Targets: AIMech:IterativeHessianSketchForConstrainedLeastSquares.

Supported by Sections 2.3-2.4 (Proposition 1, Lemma 1, Theorem 2), Appendices B-D (Lemmas 3-6), and boundary script.

Verified deterministic per-step inequality (Equation 39) across all 12 steps and cumulative product bound (0.000382 &lt;= 0.121753).

### minimax-localized-gaussian-width-statistical-optimality-and-applications

evidence: supported. Targets: AIMech:IterativeHessianSketchForConstrainedLeastSquares.

Supported by Section 2.4.2 (Proposition 2, Corollary 1), Section 3 (Corollaries 2-4), Appendix D.2.2 (Lemma 7), and boundary script.

Verified minimax statistical error matching on OLS and geometric convergence on l_1-constrained sparse least squares (gap reduced from 1.414044 to 0.011687).

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:IterativeHessianSketchForConstrainedLeastSquares.

The full record is consistent; retain DRAFT.

Read every field of IterativeHessianSketchForConstrainedLeastSquares.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, three claims and locators, three primary sources with exact SHA-256 digests, two pinned AIO mappings and rationales, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261018T203500Z-iterative-hessian-sketch-constrained-least-squares.json | supports | No normalized identity match for Iterative Hessian Sketch across 442 pinned AIO records and 620 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected LinearRegression and LassoRegression in the pinned AIO snapshot (2026-07-22). Provide accurate narrow_match and related_match context. |
| calculation | research/discovery/iterative-hessian-sketch-constrained-least-squares-boundaries.py | supports | Executed pure-Python verification in research/discovery/iterative-hessian-sketch-constrained-least-squares-boundaries.py (SHA-256 951b71668675b9b5a1accae2ee73efaf02772c1b7e993a59901ac79827889ee5): verified (1) Theorem 1 and Corollary 2 statistical sub-optimality of single-shot classical sketching (prediction error 0.127278, OLS gap 0.116469) vs. unconstrained Iterative Hessian Sketch over N = 12 rounds (prediction error 0.041095 matching exact OLS error 0.040888, OLS gap 3.819e-4); (2) Proposition 1 and Theorem 2 deterministic per-step inequality &#124;&#124;x^{t+1} - x^{LS}&#124;&#124;_A &lt;= (Z_2(S^{t+1})/Z_1(S^{t+1})) &#124;&#124;x^t - x^{LS}&#124;&#124;_A (Equation 39) across all 12 steps and cumulative product bound (0.000382 &lt;= 0.121753); and (3) Section 3.2 Corollary 3 geometric convergence of constrained IHS on l_1-constrained sparse least squares (reducing prediction-norm gap to x^{LS} from 1.414044 to 0.281778 after 1 round and 0.011687 after 5 rounds). |
| pilanci2016-ihs-pdf | https://arxiv.org/pdf/1411.0347; Pages 1-33, Sections 1-5 and Appendices A-E (Theorems 1-2, Propositions 1-2, Corollaries 1-4, Lemmas 1-7, Equations 1-48) | supports | All 33 pages of the full-text PDF of Pilanci &amp; Wainwright (2014/2016, arXiv:1411.0347v1) read. Checked all definitions, lemmas, propositions, theorems, corollaries, and proofs. |
| pilanci2016-ihs-abs | https://arxiv.org/abs/1411.0347; arXiv:1411.0347v1 abstract | supports | arXiv abstract and submission metadata read and verified. |
| pilanci2016-ihs-jmlr | https://jmlr.org/papers/v17/14-460.html; JMLR 17(53):1-38 (2016) HTML record | supports | JMLR 2016 metadata and abstract record read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Iterative Hessian Sketch record, yielding 621 native and 442 unchanged generated records.
- All 33 PDF pages of arXiv:1411.0347v1 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261018T203600Z-iterative-hessian-sketch-constrained-least-squares
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Iterative Hessian Sketch for constrained least-squares
  and information-theoretic classical sketching lower bounds
started_at: '2026-10-18T20:35:00Z'
finished_at: '2026-10-18T20:36:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from NewtonSketchRandomizedHessianProjectedOptimization,
    CountSketchLeveragedHybridRandomizedConstrainedAndRidgeRegression, and StatisticallyPreconditionedAcceleratedIterativeSketchingLeastSquaresAndRidge,
    verified the Theorem 1 Fano lower bound gap between classical sketching and IHS,
    the Proposition 1 and Theorem 2 deterministic per-step tangent-cone contraction
    inequalities (Equation 39), and Corollary 3 l_1-constrained sparse IHS geometric
    convergence, and documented four primary-source typographical notes in Pilanci
    & Wainwright (2016, arXiv:1411.0347v1, pp. 8-11, 20, 24-26). This is adversarial
    author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Iterative Hessian Sketch for Constrained Least-Squares and Information-Theoretic
  Classical Sketching Lower Bounds as a distinct DRAFT mathematical_method with narrow
  LinearRegression and related LassoRegression mappings. All three claims and locators
  across Pilanci & Wainwright (2016, JMLR 17(53):1-38, arXiv:1411.0347v1) are supported
  with explicit multi-pass matrix-vector product and restricted-eigenvalue tangent-cone
  limitations.
source:
  git_revision: 14162a23d4c5c5da529c4ba462cc05fa51e05fdb
  state: working_tree
  inputs:
  - path: data/aio/LassoRegression.yaml
    sha256: c62e7ffd00a16f5a82d514687b094aee5f6796d19a7d16200bdb10498c024949
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/curated/IterativeHessianSketchForConstrainedLeastSquares.yaml
    sha256: 7624f3072ac2ec20f35299908dc147a50cc8ae497303a3d4813fb05fa281558c
    role: target
  - path: data/curated/NewtonSketchRandomizedHessianProjectedOptimization.yaml
    sha256: 7e4b3c72c5a4729fde85b448ad4a4d10c22bf40ebdb309f7abaf509fc0ed010c
    role: context
  - path: research/discovery/20261018T203500Z-iterative-hessian-sketch-constrained-least-squares.json
    sha256: 7ace4cd6b57f6d822a4a3ad1b2aa22bfdcca8d84784ce153a2721dcb4f417d28
    role: context
  - path: research/discovery/iterative-hessian-sketch-constrained-least-squares-boundaries.py
    sha256: 951b71668675b9b5a1accae2ee73efaf02772c1b7e993a59901ac79827889ee5
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
- target_id: AIMech:IterativeHessianSketchForConstrainedLeastSquares
  path: data/curated/IterativeHessianSketchForConstrainedLeastSquares.yaml
  label: Iterative Hessian Sketch for Constrained Least-Squares and Information-Theoretic
    Classical Sketching Lower Bounds
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IterativeHessianSketchForConstrainedLeastSquares.yaml
    role: maintained
scope:
  description: All fields of the exact maintained IterativeHessianSketchForConstrainedLeastSquares
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:IterativeHessianSketchForConstrainedLeastSquares'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  exclusions:
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
checks:
- check_id: maintain-1
  name: aimech validate
  command: aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  exit_code: 0
  expected_exit_code: 0
  summary: All 621 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Pilanci & Wainwright 2016 Iterative Hessian Sketch and classical
    sketch lower-bound checks
  command: python3 research/discovery/iterative-hessian-sketch-constrained-least-squares-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:IterativeHessianSketchForConstrainedLeastSquares\"\
    ,\n  \"all_passed\": true,\n  \"unconstrained_ihs_and_theorem1_2\": {\n    \"\
    passed\": true,\n    \"ols_stat_err\": 0.04088827677040154,\n    \"ihs_stat_err\"\
    : 0.04109504420070216,\n    \"classical_stat_err\": 0.12727772242146404,\n   \
    \ \"ihs_ols_gap\": 0.0003819292885153705,\n    \"classical_ols_gap\": 0.11646909834560103,\n\
    \    \"theorem2_product_bound\": 0.12175253124797426,\n    \"all_step_inequalities_39_passed\"\
    : true\n  },\n  \"sparse_l1_constrained_ihs\": {\n    \"passed\": true,\n    \"\
    initial_gap\": 1.4140436263049643,\n    \"round1_gap\": 0.28177805056510624,\n\
    \    \"final_gap\": 0.011687177300639338\n  }\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261018T203500Z-iterative-hessian-sketch-constrained-least-squares.json
  accessed_at: '2026-10-18T20:35:00Z'
  support: supports
  summary: No normalized identity match for Iterative Hessian Sketch across 442 pinned
    AIO records and 620 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-18T20:35:00Z'
  support: supports
  summary: Inspected LinearRegression and LassoRegression in the pinned AIO snapshot
    (2026-07-22). Provide accurate narrow_match and related_match context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/iterative-hessian-sketch-constrained-least-squares-boundaries.py
  accessed_at: '2026-10-18T20:35:00Z'
  snapshot_sha256: 951b71668675b9b5a1accae2ee73efaf02772c1b7e993a59901ac79827889ee5
  support: supports
  summary: 'Executed pure-Python verification in research/discovery/iterative-hessian-sketch-constrained-least-squares-boundaries.py
    (SHA-256 951b71668675b9b5a1accae2ee73efaf02772c1b7e993a59901ac79827889ee5): verified
    (1) Theorem 1 and Corollary 2 statistical sub-optimality of single-shot classical
    sketching (prediction error 0.127278, OLS gap 0.116469) vs. unconstrained Iterative
    Hessian Sketch over N = 12 rounds (prediction error 0.041095 matching exact OLS
    error 0.040888, OLS gap 3.819e-4); (2) Proposition 1 and Theorem 2 deterministic
    per-step inequality ||x^{t+1} - x^{LS}||_A <= (Z_2(S^{t+1})/Z_1(S^{t+1})) ||x^t
    - x^{LS}||_A (Equation 39) across all 12 steps and cumulative product bound (0.000382
    <= 0.121753); and (3) Section 3.2 Corollary 3 geometric convergence of constrained
    IHS on l_1-constrained sparse least squares (reducing prediction-norm gap to x^{LS}
    from 1.414044 to 0.281778 after 1 round and 0.011687 after 5 rounds).'
- evidence_id: pilanci2016-ihs-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1411.0347
  locator: Pages 1-33, Sections 1-5 and Appendices A-E (Theorems 1-2, Propositions
    1-2, Corollaries 1-4, Lemmas 1-7, Equations 1-48)
  accessed_at: '2026-10-18T13:31:00Z'
  snapshot_sha256: dea3c1364a748d6a428dbfd16ba058ab9265c83fb8c11374812bd487c4c4d147
  support: supports
  summary: All 33 pages of the full-text PDF of Pilanci & Wainwright (2014/2016, arXiv:1411.0347v1)
    read. Checked all definitions, lemmas, propositions, theorems, corollaries, and
    proofs.
- evidence_id: pilanci2016-ihs-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1411.0347
  locator: arXiv:1411.0347v1 abstract
  accessed_at: '2026-10-18T13:31:00Z'
  snapshot_sha256: e6cc8cea30c1d6a8c76f9cc0ff30bd1174521c5ca0054a42c36a0078f3745634
  support: supports
  summary: arXiv abstract and submission metadata read and verified.
- evidence_id: pilanci2016-ihs-jmlr
  kind: primary_source
  reference: https://jmlr.org/papers/v17/14-460.html
  locator: JMLR 17(53):1-38 (2016) HTML record
  accessed_at: '2026-10-18T13:31:00Z'
  snapshot_sha256: 19fa92bd87c2ef95c737af6a6b880d52e2afd761eb83825ac636628fe0d41401
  support: supports
  summary: JMLR 2016 metadata and abstract record read and verified.
assessments:
- assessment_id: identity-boundary
  area: identity
  topic: Distinctness of Iterative Hessian Sketch for constrained least-squares and
    information-theoretic classical sketching lower bounds
  outcome: supported
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  evidence_ids:
  - identity
  - pilanci2016-ihs-pdf
  - pilanci2016-ihs-abs
  - pilanci2016-ihs-jmlr
  summary: Distinct from Newton Sketch for general twice-differentiable and self-concordant
    barrier optimization, hybrid CountSketch-leverage regression, and accelerated
    statistically preconditioned unconstrained sketching.
  details: Confirmed via normalized identity check and full-text reading of Pilanci
    & Wainwright (2016, arXiv:1411.0347v1).
- assessment_id: aio-mappings
  area: grounding
  topic: AIO mappings for AIMech:IterativeHessianSketchForConstrainedLeastSquares
  outcome: supported
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  evidence_ids:
  - mapping
  - pilanci2016-ihs-pdf
  summary: narrow_match to AIO:LinearRegression and related_match to AIO:LassoRegression
    are accurate.
  details: Pinned AIO (2026-07-22) contains LinearRegression and LassoRegression broadly
    without Fano lower bounds for classical sketching or tangent-cone Gaussian-width
    Iterative Hessian Sketch guarantees.
- assessment_id: definition
  area: evidence
  topic: Definition and scope
  outcome: supported
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  evidence_ids:
  - pilanci2016-ihs-pdf
  - pilanci2016-ihs-abs
  - pilanci2016-ihs-jmlr
  summary: Definition accurately captures the Theorem 1 Fano lower bound for classical
    sketching, the Equation (24) IHS update, Theorem 2 tangent-cone contraction, and
    Corollary 1 minimax risk matching.
  details: All equations and claims verified against Sections 1-5 and Appendices A-E
    of arXiv:1411.0347v1.
- assessment_id: fano-information-theoretic-lower-bound-for-classical-sketching
  area: evidence
  topic: fano-information-theoretic-lower-bound-for-classical-sketching
  outcome: supported
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  evidence_ids:
  - pilanci2016-ihs-pdf
  - calculation
  summary: Supported by Section 2.2 (Theorem 1, Examples 1-3), Appendix A (Lemma 2),
    and boundary script.
  details: Verified classical sketching prediction error inflation (0.127278 vs. 0.040888
    for OLS and 0.041095 for IHS).
- assessment_id: hessian-sketch-tangent-cone-contraction-and-iterative-hessian-sketch
  area: evidence
  topic: hessian-sketch-tangent-cone-contraction-and-iterative-hessian-sketch
  outcome: supported
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  evidence_ids:
  - pilanci2016-ihs-pdf
  - calculation
  summary: Supported by Sections 2.3-2.4 (Proposition 1, Lemma 1, Theorem 2), Appendices
    B-D (Lemmas 3-6), and boundary script.
  details: Verified deterministic per-step inequality (Equation 39) across all 12
    steps and cumulative product bound (0.000382 <= 0.121753).
- assessment_id: minimax-localized-gaussian-width-statistical-optimality-and-applications
  area: evidence
  topic: minimax-localized-gaussian-width-statistical-optimality-and-applications
  outcome: supported
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  evidence_ids:
  - pilanci2016-ihs-pdf
  - calculation
  summary: Supported by Section 2.4.2 (Proposition 2, Corollary 1), Section 3 (Corollaries
    2-4), Appendix D.2.2 (Lemma 7), and boundary script.
  details: Verified minimax statistical error matching on OLS and geometric convergence
    on l_1-constrained sparse least squares (gap reduced from 1.414044 to 0.011687).
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:IterativeHessianSketchForConstrainedLeastSquares
  evidence_ids:
  - identity
  - mapping
  - pilanci2016-ihs-pdf
  - pilanci2016-ihs-abs
  - pilanci2016-ihs-jmlr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of IterativeHessianSketchForConstrainedLeastSquares.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, three claims and locators, three primary sources with exact SHA-256
    digests, two pinned AIO mappings and rationales, four scoped limitations, and
    UTC curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Iterative Hessian Sketch record, yielding 621 native and 442 unchanged
  generated records.
- All 33 PDF pages of arXiv:1411.0347v1 were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- iterative-hessian-sketch
- randomized-numerical-linear-algebra
- constrained-least-squares
- gaussian-width
- self-review
- discovery-ongoing
```
