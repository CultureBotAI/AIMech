# Scientific author self-review of Fast Dropout Training

- Review: 20261013T133120Z-fast-dropout-training
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T13:24:04Z
- Finished UTC: 2026-10-13T13:31:20Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Fast Dropout Training as a DRAFT native algorithm with related AIO mappings. All five claims are supported within their explicit approximation, independence, local-derivative and version limits. The initial minor sparse-feature page-locator finding is corrected and resolved in this successor review; no unresolved actionable finding remains. No implementation or empirical replication.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:FastDropoutTraining
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 646f2520b634b844eb2a1bdd28ee9576f47fb827.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FastDropoutTraining | data/curated/FastDropoutTraining.yaml | maintained | Fast Dropout Training |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:FastDropoutTraining | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 206.20s (0:03:26)<br>Checked 442 record(s); 0 failed.<br>Checked 620 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 293 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 289,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:FastDropoutTraining | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:FastDropoutTraining | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:FastDropoutTraining | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:FastDropoutTraining | {"bernoulli_fourth": 0.5, "correlated_variance": 4.0, "diagonal_only_variance": 2.0, "expected_sigmoid": 0.6354589138849707, "expected_squared_loss": 14.04, "local_variance_gradient": 289.92319999999995, "matched_gaussian_fourth": 0.625, "mean": 2.1999999999999997, "sigmoid_of_mean": 0.9002495108803148, "variance": 13.399999999999999} |

## Scientific And Domain Assessments

### Fast Dropout Training

identity: supported. Targets: AIMech:FastDropoutTraining.

Retain this distinct DRAFT algorithm.

Retain Gaussian-approximated dropout training as one algorithm, including the inspected recurrent application. Independent identity searches included hidden and ignored files across three checkouts; every distinct hit and matched semantic definition was read. Connection-masked DropConnect training, a Bernoulli dropout layer, Gaussian-noise injection and a recurrent architecture are distinct abstractions.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:FastDropoutTraining.

The declared AIO mapping is supported.

Related mappings to DropoutLayer and GaussianDropoutLayer are justified by masked-computation approximation and Gaussian effects. The algorithm also integrates moments and propagates variance, so no equivalence or subclass mapping is asserted. Generic GaussianNoiseLayer and the penalty-adding RegularizationLayer do not establish broader mappings. All four full annotated AIO contexts and three native neighboring records were inspected.

### masked-sum-moments

evidence: supported. Targets: AIMech:FastDropoutTraining.

Supported within the stated primary-source and mathematical scope.

Independent Bernoulli retention gives the stated exact fixed-input mean and variance. Finite independence alone does not justify Gaussianity; the corrected page6 locator directly supports the sparse-feature caveat. Finite enumeration agrees with the claimed moments.

### sampling-integration-and-loss

evidence: supported. Targets: AIMech:FastDropoutTraining.

Supported within the stated primary-source and mathematical scope.

Sections2.3–2.4 distinguish sampled and integrated approximations and account for mask-gradient dependence. Sigmoid/log-sigmoid integration is approximate; expected squared loss follows the exact variance identity. Constructed nonlinear expectation and fourth-moment examples reject stronger distribution/loss equivalence.

### propagated-variance-and-recurrence

evidence: supported. Targets: AIMech:FastDropoutTraining.

Supported within the stated primary-source and mathematical scope.

Original page5 displays the incoming-variance term before the practical omission. Recurrent Equation2 retains p*sigma squared alongside p*(1-p)*mu squared; hidden state and current input are concatenated. The stated independence assumptions matter, and removing final-layer fast dropout differs from setting only its mask dropout rate to zero.

### local-regularization-boundary

evidence: supported. Targets: AIMech:FastDropoutTraining.

Supported within the stated primary-source and mathematical scope.

Differentiating the variance with incoming moments fixed gives the displayed local chain-rule contribution. Its loss derivative can have either sign or vanish. The record does not infer a global nonnegative quadratic penalty, every stationary-point contribution vanishing, or recurrent stability from this local decomposition.

### evaluation-and-version-scope

evidence: supported. Targets: AIMech:FastDropoutTraining.

Supported within the stated primary-source and mathematical scope.

The original minibatch and regression exceptions are retained. Four-music-dataset recurrent comparisons use random-search validation and multiple optimization aids. Primary v7 metadata explicitly removes erroneous Penn Treebank experiments; these are not retained as supporting language-model results.

### Gaussian approximation, exact moments versus full distributions, propagated covariance, local variance gradients and version-scoped experiments

consistency: supported. Targets: AIMech:FastDropoutTraining.

Constructed calculations support the stated distinctions.

Finite enumeration verifies independent mask/input moments and expected squared loss, separates nonlinear expectation from evaluation at the mean, demonstrates unequal fourth moments of matched Bernoulli/Gaussian variables and missing covariance under diagonal closure, and checks a local variance-path derivative. No author implementation or model fitting.

### All maintained fields

provenance: supported. Targets: AIMech:FastDropoutTraining.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Reviewed all five claims, definition and identity, mapping rationale, evidence/source versions/hashes/locators and curation metadata. The corrected sparse-feature reference points to the actual Section6.2 prose on PDFpage6; page7 contains results. Exact moment identities are distinguished from Gaussian/nonlinear closure, and the version7 removal of erroneous Penn Treebank experiments is retained. The initial finding is preserved and the report mirror synchronized.

## Findings

### F1: Correct fast-dropout sparse-feature page locator

minor / resolved / confirmed; issue key: fast-dropout-sparse-feature-page-locator.

The masked-sum-moments claim cites the sparse-feature limitation in Section6.2 as PDFpage7. The actual Section6.2 prose, including the MPQA sparse-feature Gaussian-assumption caveat, is on PDFpage6; page7 contains the associated results table. The moment formula and qualified claim remain supported. Correct this precise page locator.

Disposition: The sparse-feature caveat now cites Section6.2 on PDFpage6. The actual heading and MPQA prose were rechecked after corrected capture. Report mirror synchronized and append-only EDIT history saved; corrected-input gates pass.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T131205Z-fast-dropout-training.json | supports | Compared all 442 pinned AIO and 619 native IDs, names, aliases and scoped synonyms; no normalized identity match.  Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 181, 90, 89 lines. All distinct match contents were inspected. Semantic matching covered 34 AIO and 119 native definitions, with every matched definition read. 4 full annotated AIO node/edge/generated contexts and 3 full native records were inspected. Fast dropout denotes Wang and Manning’s Gaussian approximation algorithm, including sampling and moment-integration variants and the inspected recurrent application. It is not the Bernoulli masking layer itself, a fixed Gaussian-noise layer, a recurrent architecture or the original DropConnect layer’s connection-masked training. DropConnect shares a Gaussian moment approximation at inference, which does not identify its full procedure with fast-dropout training. Recurrent use is kept within this method; no duplicate recurrent-method ID is created. |
| mapping | sources/aio/aio.json | supports | Related mappings to DropoutLayer and GaussianDropoutLayer are justified by masked-computation approximation and Gaussian effects. The algorithm also integrates moments and propagates variance, so no equivalence or subclass mapping is asserted. Generic GaussianNoiseLayer and the penalty-adding RegularizationLayer do not establish broader mappings. All four full annotated AIO contexts and three native neighboring records were inspected. |
| wang2013 | https://proceedings.mlr.press/v28/wang13a.pdf; Complete nine-page original and twelve-page arXiv1311.0701v7 recurrent followup, plus primary v7 metadata. Other versions, author code and empirical replication excluded. | supports | ICML2013, PMLR28(2):118–126, nine-page proceedings PDF. All pages visually read. Locators use PDF pages1–9; no author implementation executed. |
| bayer2014 | https://arxiv.org/pdf/1311.0701v7; Complete nine-page original and twelve-page arXiv1311.0701v7 recurrent followup, plus primary v7 metadata. Other versions, author code and empirical replication excluded. | supports | arXiv1311.0701v7,5March2014,12pages; all pages visually read, including appendix. The primary version comments state that erroneous Penn Treebank experiments were removed. Earlier versions and author implementation not inspected. |
| calculation | research/discovery/fast-dropout-boundaries.py | supports | Finite enumeration verifies independent mask/input moments and expected squared loss, separates nonlinear expectation from evaluation at the mean, demonstrates unequal fourth moments of matched Bernoulli/Gaussian variables and missing covariance under diagonal closure, and checks a local variance-path derivative. No author implementation or model fitting. |
| corrected-record | data/curated/FastDropoutTraining.yaml | supports | Complete corrected record read after capture; the sparse-feature locator agrees with the primary-page heading and prose. |
| predecessor | reviews/structured/20261013T131528Z-fast-dropout-evidence-locator/review.yaml | supports | Immutable partial author self-review retains the original minor locator finding. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- 1 new DRAFT concepts and 0 updated existing concepts, yielding 620 native and 442 unchanged generated records. The 804-entry main frontier retains 476 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- Complete visually inspected primary PDFs: 9 pages, 12 pages. Original download and reading times retained. No author code, training or empirical replication.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T133120Z-fast-dropout-training
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Fast Dropout Training
started_at: '2026-10-13T13:24:04Z'
finished_at: '2026-10-13T13:31:20Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged Gaussian approximation, exact moments
    versus full distributions, propagated covariance, local variance gradients and
    version-scoped experiments. This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Fast Dropout Training as a DRAFT native algorithm with related AIO
  mappings. All five claims are supported within their explicit approximation, independence,
  local-derivative and version limits. The initial minor sparse-feature page-locator
  finding is corrected and resolved in this successor review; no unresolved actionable
  finding remains. No implementation or empirical replication.
source:
  git_revision: 646f2520b634b844eb2a1bdd28ee9576f47fb827
  state: working_tree
  inputs:
  - path: data/aio/DropoutLayer.yaml
    sha256: f1d1f2ad44ecf177e8c5d16bf1fb72388712d25f499583feab23e5fb65a71e24
    role: context
  - path: data/aio/GaussianDropoutLayer.yaml
    sha256: d709e2b88e01052b2dbb1a1e3213a79b428c3c1de4acb2e55c875528250d58d2
    role: context
  - path: data/aio/GaussianNoiseLayer.yaml
    sha256: 1d6c203daf9e9a5a450a85a7d7bf6e55bb9bffbeea7ceffcc1a8aefbd9629452
    role: context
  - path: data/aio/RegularizationLayer.yaml
    sha256: d4280bbc058b841655bcfcea7ef1dd1e05ac5e0211a860045f13eaa30933dbae
    role: context
  - path: data/curated/DropConnect.yaml
    sha256: 4785777508a6f24792c7533279a08eb66977144b62a260eb26f1d0fbdad1b356
    role: context
  - path: data/curated/FastDropoutTraining.yaml
    sha256: 88784e3f7730f339b39b09d20cf3aeb0cfc56d8a7c300cd453d9c3cb1cc01b3c
    role: target
  - path: data/curated/NoisyRectifier.yaml
    sha256: fb65c10663835e61629f05d55866248e00aed07a28cc00eb444499d0f4936f28
    role: context
  - path: data/curated/NormStabilizer.yaml
    sha256: 534daa42c9584cefc836a8e5299b1b61e3e57957f153c3f5a0cd9d4c46202ecb
    role: context
  - path: research/discovery/20261013T131205Z-fast-dropout-training.json
    sha256: d92ca2e86cabd2c1921bd6267ab00e14f6b06213f465c520599b1e711e9c989e
    role: context
  - path: research/discovery/fast-dropout-boundaries.py
    sha256: 9c70a1950b6b353e0fa31c472454f9a274eaff149f2b72238c9dae3a9f71dbbd
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
- target_id: AIMech:FastDropoutTraining
  path: data/curated/FastDropoutTraining.yaml
  label: Fast Dropout Training
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FastDropoutTraining.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:FastDropoutTraining'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:FastDropoutTraining
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: Complete nine-page original and twelve-page arXiv1311.0701v7 recurrent
      followup, plus primary v7 metadata. Other versions, author code and empirical
      replication excluded.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:FastDropoutTraining
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 206.20s (0:03:26)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 620 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 293 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 289,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:FastDropoutTraining
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
  - AIMech:FastDropoutTraining
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
  - AIMech:FastDropoutTraining
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/fast-dropout-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:FastDropoutTraining
  exit_code: 0
  expected_exit_code: 0
  summary: '{"bernoulli_fourth": 0.5, "correlated_variance": 4.0, "diagonal_only_variance":
    2.0, "expected_sigmoid": 0.6354589138849707, "expected_squared_loss": 14.04, "local_variance_gradient":
    289.92319999999995, "matched_gaussian_fourth": 0.625, "mean": 2.1999999999999997,
    "sigmoid_of_mean": 0.9002495108803148, "variance": 13.399999999999999}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T131205Z-fast-dropout-training.json
  accessed_at: '2026-10-13T13:24:04Z'
  support: supports
  summary: Compared all 442 pinned AIO and 619 native IDs, names, aliases and scoped
    synonyms; no normalized identity match.  Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    181, 90, 89 lines. All distinct match contents were inspected. Semantic matching
    covered 34 AIO and 119 native definitions, with every matched definition read.
    4 full annotated AIO node/edge/generated contexts and 3 full native records were
    inspected. Fast dropout denotes Wang and Manning’s Gaussian approximation algorithm,
    including sampling and moment-integration variants and the inspected recurrent
    application. It is not the Bernoulli masking layer itself, a fixed Gaussian-noise
    layer, a recurrent architecture or the original DropConnect layer’s connection-masked
    training. DropConnect shares a Gaussian moment approximation at inference, which
    does not identify its full procedure with fast-dropout training. Recurrent use
    is kept within this method; no duplicate recurrent-method ID is created.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T13:24:04Z'
  support: supports
  summary: Related mappings to DropoutLayer and GaussianDropoutLayer are justified
    by masked-computation approximation and Gaussian effects. The algorithm also integrates
    moments and propagates variance, so no equivalence or subclass mapping is asserted.
    Generic GaussianNoiseLayer and the penalty-adding RegularizationLayer do not establish
    broader mappings. All four full annotated AIO contexts and three native neighboring
    records were inspected.
- evidence_id: wang2013
  kind: primary_source
  reference: https://proceedings.mlr.press/v28/wang13a.pdf
  locator: Complete nine-page original and twelve-page arXiv1311.0701v7 recurrent
    followup, plus primary v7 metadata. Other versions, author code and empirical
    replication excluded.
  accessed_at: '2026-10-13T12:55:49Z'
  snapshot_sha256: a5a8f1efb4381963188ad3bcd5e0525d7f95e7106255c1019445ad16f6bb2c63
  support: supports
  summary: ICML2013, PMLR28(2):118–126, nine-page proceedings PDF. All pages visually
    read. Locators use PDF pages1–9; no author implementation executed.
- evidence_id: bayer2014
  kind: primary_source
  reference: https://arxiv.org/pdf/1311.0701v7
  locator: Complete nine-page original and twelve-page arXiv1311.0701v7 recurrent
    followup, plus primary v7 metadata. Other versions, author code and empirical
    replication excluded.
  accessed_at: '2026-10-13T12:55:49Z'
  snapshot_sha256: d447d6f4ca5c298af5315d2f1bd680d19bb20d52bbe600a9317b7fefd3092992
  support: supports
  summary: arXiv1311.0701v7,5March2014,12pages; all pages visually read, including
    appendix. The primary version comments state that erroneous Penn Treebank experiments
    were removed. Earlier versions and author implementation not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/fast-dropout-boundaries.py
  accessed_at: '2026-10-13T13:25:40Z'
  snapshot_sha256: 9c70a1950b6b353e0fa31c472454f9a274eaff149f2b72238c9dae3a9f71dbbd
  support: supports
  summary: Finite enumeration verifies independent mask/input moments and expected
    squared loss, separates nonlinear expectation from evaluation at the mean, demonstrates
    unequal fourth moments of matched Bernoulli/Gaussian variables and missing covariance
    under diagonal closure, and checks a local variance-path derivative. No author
    implementation or model fitting.
- evidence_id: corrected-record
  kind: record_content
  reference: data/curated/FastDropoutTraining.yaml
  accessed_at: '2026-10-13T13:25:40Z'
  snapshot_sha256: 88784e3f7730f339b39b09d20cf3aeb0cfc56d8a7c300cd453d9c3cb1cc01b3c
  support: supports
  summary: Complete corrected record read after capture; the sparse-feature locator
    agrees with the primary-page heading and prose.
- evidence_id: predecessor
  kind: record_content
  reference: reviews/structured/20261013T131528Z-fast-dropout-evidence-locator/review.yaml
  accessed_at: '2026-10-13T13:25:40Z'
  support: supports
  summary: Immutable partial author self-review retains the original minor locator
    finding.
assessments:
- assessment_id: identity
  area: identity
  topic: Fast Dropout Training
  outcome: supported
  target_ids:
  - AIMech:FastDropoutTraining
  evidence_ids:
  - identity
  - wang2013
  - bayer2014
  summary: Retain this distinct DRAFT algorithm.
  details: Retain Gaussian-approximated dropout training as one algorithm, including
    the inspected recurrent application. Independent identity searches included hidden
    and ignored files across three checkouts; every distinct hit and matched semantic
    definition was read. Connection-masked DropConnect training, a Bernoulli dropout
    layer, Gaussian-noise injection and a recurrent architecture are distinct abstractions.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:FastDropoutTraining
  evidence_ids:
  - mapping
  - wang2013
  - bayer2014
  summary: The declared AIO mapping is supported.
  details: Related mappings to DropoutLayer and GaussianDropoutLayer are justified
    by masked-computation approximation and Gaussian effects. The algorithm also integrates
    moments and propagates variance, so no equivalence or subclass mapping is asserted.
    Generic GaussianNoiseLayer and the penalty-adding RegularizationLayer do not establish
    broader mappings. All four full annotated AIO contexts and three native neighboring
    records were inspected.
- assessment_id: masked-sum-moments
  area: evidence
  topic: masked-sum-moments
  outcome: supported
  target_ids:
  - AIMech:FastDropoutTraining
  evidence_ids:
  - wang2013
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Independent Bernoulli retention gives the stated exact fixed-input mean
    and variance. Finite independence alone does not justify Gaussianity; the corrected
    page6 locator directly supports the sparse-feature caveat. Finite enumeration
    agrees with the claimed moments.
- assessment_id: sampling-integration-and-loss
  area: evidence
  topic: sampling-integration-and-loss
  outcome: supported
  target_ids:
  - AIMech:FastDropoutTraining
  evidence_ids:
  - wang2013
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Sections2.3–2.4 distinguish sampled and integrated approximations and account
    for mask-gradient dependence. Sigmoid/log-sigmoid integration is approximate;
    expected squared loss follows the exact variance identity. Constructed nonlinear
    expectation and fourth-moment examples reject stronger distribution/loss equivalence.
- assessment_id: propagated-variance-and-recurrence
  area: evidence
  topic: propagated-variance-and-recurrence
  outcome: supported
  target_ids:
  - AIMech:FastDropoutTraining
  evidence_ids:
  - wang2013
  - bayer2014
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Original page5 displays the incoming-variance term before the practical
    omission. Recurrent Equation2 retains p*sigma squared alongside p*(1-p)*mu squared;
    hidden state and current input are concatenated. The stated independence assumptions
    matter, and removing final-layer fast dropout differs from setting only its mask
    dropout rate to zero.
- assessment_id: local-regularization-boundary
  area: evidence
  topic: local-regularization-boundary
  outcome: supported
  target_ids:
  - AIMech:FastDropoutTraining
  evidence_ids:
  - bayer2014
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Differentiating the variance with incoming moments fixed gives the displayed
    local chain-rule contribution. Its loss derivative can have either sign or vanish.
    The record does not infer a global nonnegative quadratic penalty, every stationary-point
    contribution vanishing, or recurrent stability from this local decomposition.
- assessment_id: evaluation-and-version-scope
  area: evidence
  topic: evaluation-and-version-scope
  outcome: supported
  target_ids:
  - AIMech:FastDropoutTraining
  evidence_ids:
  - wang2013
  - bayer2014
  summary: Supported within the stated primary-source and mathematical scope.
  details: The original minibatch and regression exceptions are retained. Four-music-dataset
    recurrent comparisons use random-search validation and multiple optimization aids.
    Primary v7 metadata explicitly removes erroneous Penn Treebank experiments; these
    are not retained as supporting language-model results.
- assessment_id: constructed-boundaries
  area: consistency
  topic: Gaussian approximation, exact moments versus full distributions, propagated
    covariance, local variance gradients and version-scoped experiments
  outcome: supported
  target_ids:
  - AIMech:FastDropoutTraining
  evidence_ids:
  - wang2013
  - bayer2014
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Finite enumeration verifies independent mask/input moments and expected
    squared loss, separates nonlinear expectation from evaluation at the mean, demonstrates
    unequal fourth moments of matched Bernoulli/Gaussian variables and missing covariance
    under diagonal closure, and checks a local variance-path derivative. No author
    implementation or model fitting.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:FastDropoutTraining
  evidence_ids:
  - identity
  - mapping
  - wang2013
  - bayer2014
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Reviewed all five claims, definition and identity,
    mapping rationale, evidence/source versions/hashes/locators and curation metadata.
    The corrected sparse-feature reference points to the actual Section6.2 prose on
    PDFpage6; page7 contains results. Exact moment identities are distinguished from
    Gaussian/nonlinear closure, and the version7 removal of erroneous Penn Treebank
    experiments is retained. The initial finding is preserved and the report mirror
    synchronized.
findings:
- finding_id: F1
  issue_key: fast-dropout-sparse-feature-page-locator
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Correct fast-dropout sparse-feature page locator
  description: The masked-sum-moments claim cites the sparse-feature limitation in
    Section6.2 as PDFpage7. The actual Section6.2 prose, including the MPQA sparse-feature
    Gaussian-assumption caveat, is on PDFpage6; page7 contains the associated results
    table. The moment formula and qualified claim remain supported. Correct this precise
    page locator.
  target_ids:
  - AIMech:FastDropoutTraining
  field_paths:
  - claims[claim_id=masked-sum-moments].evidence[0].locator
  evidence_ids:
  - wang2013
  - corrected-record
  - predecessor
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FastDropoutTraining.yaml
    role: maintained
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/277
  disposition_reason: The sparse-feature caveat now cites Section6.2 on PDFpage6.
    The actual heading and MPQA prose were rechecked after corrected capture. Report
    mirror synchronized and append-only EDIT history saved; corrected-input gates
    pass.
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261013T131528Z-fast-dropout-evidence-locator
    finding_id: F1
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- 1 new DRAFT concepts and 0 updated existing concepts, yielding 620 native and 442
  unchanged generated records. The 804-entry main frontier retains 476 pending and
  57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- 'Complete visually inspected primary PDFs: 9 pages, 12 pages. Original download
  and reading times retained. No author code, training or empirical replication.'
- No author code, training, paid service, hardware measurement or empirical replication.
  Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261013T131528Z-fast-dropout-evidence-locator
  relationship: Resolves the explicitly linked sparse-feature page-locator finding.
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
