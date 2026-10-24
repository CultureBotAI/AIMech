# Scientific author self-review of Annealed importance sampling

- Review: 20261014T200216Z-annealed-importance-sampling
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T19:57:45Z
- Finished UTC: 2026-10-14T20:02:16Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain AIS as a DRAFT native algorithm with a related Markov-process mapping. All three initial review findings are corrected with same-key predecessor lineage: zero-weight paths, Equation2 locator and the initial-draw indexing exception.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:AnnealedImportanceSampling
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c924f97a3db72c41c068391adbbd8fd3690d5740.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AnnealedImportanceSampling | data/curated/AnnealedImportanceSampling.yaml | maintained | Annealed importance sampling |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:AnnealedImportanceSampling | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 437.22s (0:07:17)<br>Checked 442 record(s); 0 failed.<br>Checked 701 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 392 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 393,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:AnnealedImportanceSampling | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:AnnealedImportanceSampling | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:AnnealedImportanceSampling | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:AnnealedImportanceSampling | {"nonreversible_example": {"target": [1, 2, 7], "bridge": [1, 1, 1], "base": [3, 2, 1], "weighted_endpoint_mass": ["1/6", "1/3", "7/6"], "expected_weight": "5/3", "unweighted_endpoint_probability": ["1/6", "1/2", "1/3"], "target_probability": ["1/10", "1/5", "7/10"], "self_normalized_indicator_expected_value": {"one_run": "1/3", "two_runs": "967/2025", "target": "7/10"}, "expected_log_weight": 0.21485510211104045, "log_expected_weight": 0.5108256237659907}, "identity_kernel_reduces_to_plain_importance_sampling": true, "noninvariant_reset_expected_weight": "1/2", "invariant_family_cases": 192, "violated_support_example": {"expected_weight": "1", "actual_normalizing_ratio": "2"}, "nested_support_zero_path": {"functions": [[1, 0], [1, 0], [1, 1]], "guarded_weights": ["1", "0"], "ratio_evaluations": [2, 1], "expected_weight": "1/2", "actual_normalizing_ratio": "1/2", "zero_path_stops_before_undefined_ratio": true}, "scope": "Finite exact laws and counterexamples only. No continuous-state theorem certification, variance bound, benchmark replication, author implementation, paid provider or training."} |

## Scientific And Domain Assessments

### Annealed importance sampling

identity: supported. Targets: AIMech:AnnealedImportanceSampling.

Retain this distinct DRAFT algorithm.

Retain AIS as a distinct weighted-path estimator. Model-specific uses in PoHMM, SQR, fixed-length Poisson MRF and replicated softmax do not supply a generic AIS identity. It differs from up/down accept/reject transitions, replica exchange and optimization annealing.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:AnnealedImportanceSampling.

The explicit AIO mapping assessment is supported within its stated scope.

Related MarkovChain preserves the algorithm-to-process distinction. Ten complete AIO contexts were assessed, including the Network parent and ProbabilisticHiddenLayer relation, which are not imported into AIS. Partition normalization does not match the data-normalization task; incidental graphical-model uses do not define algorithm equivalence. Seven full native neighbors distinguish existing model-specific applications and sampling/optimization methods.

### path-law-and-weight

evidence: supported. Targets: AIMech:AnnealedImportanceSampling.

Supported within the stated primary-source and mathematical scope.

The prescribed ordering and product agree with Equations4–5. Invariance is sufficient for the intermediate kernels; reversibility and full equilibration are unnecessary. Nested supports require the now-explicit chronological zero-weight stop. Zero runs remain observations of weight0 in the mean, and no endpoint observable or later undefined ratio is evaluated.

### estimand-and-unbiasedness-boundary

evidence: supported. Targets: AIMech:AnnealedImportanceSampling.

Supported within the stated primary-source and mathematical scope.

The extended-space law establishes weighted mass and mean-weight normalizer ratios under the stated assumptions. Ratios of random sums and logarithms do not inherit unbiasedness; all-zero normalized estimates are undefined. Exact finite examples distinguish unweighted endpoint probabilities and finite normalized-estimate bias.

### finite-weight-law-checks

evidence: supported. Targets: AIMech:AnnealedImportanceSampling.

Supported within the stated primary-source and mathematical scope.

The three-state nonreversible cycle reproduces5/3 expected weight and the specified endpoint masses; one/two-run normalized indicator expectations differ from7/10. The192 invariant-kernel cases pass. A valid nested-support case stops before0/0 and yields1/2, while genuinely missing target support or noninvariant kernels fail. These are exact finite examples only.

### bridge-and-bayesian-scope

evidence: supported. Targets: AIMech:AnnealedImportanceSampling.

Supported within the stated primary-source and mathematical scope.

Geometric interpolation is optional. Proper base/intermediate distributions and likelihood constants matter; a shared prior constant cancels only in the specified ratio. No unsupported general temperature or normalizability guarantee is asserted.

### terminal-and-correlated-extensions

evidence: supported. Targets: AIMech:AnnealedImportanceSampling.

Supported within the stated primary-source and mathematical scope.

A predetermined p0-invariant extension contributes its within-run average with the original weight. Dependence must be reflected in uncertainty. Ergodic correlated base sampling can support consistency, without claiming finite unbiasedness from an arbitrary initialization.

### diagnostic-and-efficiency-limits

evidence: supported. Targets: AIMech:AnnealedImportanceSampling.

Supported within the stated primary-source and mathematical scope.

The source explicitly warns that observed weight variance may miss unsampled important modes. Idealized temperature and dimension analyses are kept conditional; no universal efficiency or contemporary benchmark claim is imported.

### support and zero-weight paths, chronological indexing, weighted versus unweighted outputs, normalizer unbiasedness versus ratio bias, and model-versus-method mappings

consistency: supported. Targets: AIMech:AnnealedImportanceSampling.

Constructed calculations support the stated distinctions.

Exact three-state path enumeration checks weighted endpoint mass and the 5/3 normalizer ratio despite nonreversible, nonmixing transitions; computes one- and two-run self-normalization bias; checks 192 invariant-kernel cases; exhibits failures for noninvariant kernels and missing support. No author implementation or benchmark replication. A valid nested-support zero-weight case terminates before0/0, with exact expected weight1/2.

### All maintained fields

provenance: supported. Targets: AIMech:AnnealedImportanceSampling.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. All six claims, definition evidence, AIS alias, identity notes, source/version/access/hash, AIO pin and related mapping, limitations and curation times assessed. Zero-weight termination, Equation2 page2 and the initial-draw exception were checked against their exact predecessors, source equations, report mirror and finite guard result. The author assessed the separate bounded subagent audit without treating it as independent scientific approval.

### Zero-weight support and source locators

consistency: supported. Targets: AIMech:AnnealedImportanceSampling.

All three initial findings are resolved with explicit lineage.

The zero path is retained with weight0 in the N-run mean; it stops before0/0 or endpoint evaluation. Equation2 is on page2, and only states below the initial base draw follow T_(j+1). The initial bundle and audit remain immutable.

## Findings

### ais-zero-weight-path-convention: AIS: define zero-weight path handling under nested supports

major / resolved / confirmed; issue key: ais-zero-weight-path-convention.

The maintained field and exact report mirror now satisfy this finding’s acceptance criteria; the original observation remains unchanged.

Disposition: Full corrected record and primary passages were reread; zero-weight termination, inclusion in the attempted-run mean, Equation2 page2 and the top-index exception were verified. Exact report/calculation mirrors, actual history, required gates and the same-target predecessor identity agree. Ignored-inclusive review search found only the initial observation before this successor.

### ais-definition-equation-page: AIS: correct Equation 2 definition locator to PDF page 2

minor / resolved / confirmed; issue key: ais-definition-equation-page.

The maintained field and exact report mirror now satisfy this finding’s acceptance criteria; the original observation remains unchanged.

Disposition: Full corrected record and primary passages were reread; zero-weight termination, inclusion in the attempted-run mean, Equation2 page2 and the top-index exception were verified. Exact report/calculation mirrors, actual history, required gates and the same-target predecessor identity agree. Ignored-inclusive review search found only the initial observation before this successor.

### ais-initial-state-index-exception: AIS: qualify the intermediate-state indexing note at the initial draw

minor / resolved / confirmed; issue key: ais-initial-state-index-exception.

The maintained field and exact report mirror now satisfy this finding’s acceptance criteria; the original observation remains unchanged.

Disposition: Full corrected record and primary passages were reread; zero-weight termination, inclusion in the attempted-run mean, Equation2 page2 and the top-index exception were verified. Exact report/calculation mirrors, actual history, required gates and the same-target predecessor identity agree. Ignored-inclusive review search found only the initial observation before this successor.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T082648Z-annealed-importance-sampling.json | supports | Compared AIS and tempered transitions against all 442 pinned AIO and 699 native identities; no normalized match. Ignored- and hidden-inclusive three-checkout searches returned 1133,473,482 lines, collapsed into 132 unique content groups. Groups were classified using short full content and long-line paths/identity excerpts; full canonical model-neighbor records were read. Long generated search attributes and ignored dependency linguistic tables were not claimed as complete raw-code readings. Hits concern model-specific AIS uses, historical discovery/review context, pending methods and acronym noise. Semantic assessment covered 103 AIO and306 native definitions, including47 and22 new rows;56 and284 prior rows were verified unchanged. Ten complete AIO contexts and seven full native neighbors assessed. AIS estimates expectations and normalizing-constant ratios using weighted annealing paths. It is distinct from annealing for optimization, parallel-temperature replica exchange, ordinary Metropolis–Hastings, an up/down tempered Metropolis transition, and model-specific uses of AIS already represented in AIMech. |
| mapping | sources/aio/aio.json | supports | Related MarkovChain preserves the algorithm-to-process distinction. Ten complete AIO contexts were assessed, including the Network parent and ProbabilisticHiddenLayer relation, which are not imported into AIS. Partition normalization does not match the data-normalization task; incidental graphical-model uses do not define algorithm equivalence. Seven full native neighbors distinguish existing model-specific applications and sampling/optimization methods. |
| neal1998ais | https://arxiv.org/pdf/physics/9803008v2; Section 2, PDF pp. 4–6, Equations 3–11; self-normalized estimate, Equation 2, p. 2; Section 2, PDF pp. 4–6, Equations 4–11; support condition and invariance requirement, p. 4; zero-weight convention is a curator interpretation of the extended-space importance law, checked in research/discovery/ais-boundaries.py; Extended-space construction, PDF pp. 5–6, Equations 6–11; ratio estimate, Equation 12, p. 7; curator finite examples in research/discovery/ais-boundaries.py; Equations 4–11, PDF pp. 5–6; exact independently authored finite enumeration in research/discovery/ais-boundaries.py; Section 2, PDF pp. 4 and 6, Equation 3 and marginal-likelihood discussion; Section 2, PDF p. 6; accuracy discussion, p. 8; Section 3, PDF pp. 7–8; Section 4, pp. 8–11; examples, Sections 5–6, pp. 11–18; discussion, pp. 21–24 | supports | arXiv physics/9803008v2, submitted September 4, 1998; printed report first version February 18, revised September 1, 1998. All 25 pages and 18 references inspected, with figure pages 14–15 and core method pages 4–6 visually checked. Author metadata lists Statistics and Computing 11:125–139 (2001); journal-byte equivalence was not established. |
| calculation | research/discovery/ais-boundaries.py | supports | Exact three-state path enumeration checks weighted endpoint mass and the 5/3 normalizer ratio despite nonreversible, nonmixing transitions; computes one- and two-run self-normalization bias; checks 192 invariant-kernel cases; exhibits failures for noninvariant kernels and missing support. No author implementation or benchmark replication. A valid nested-support zero-weight case terminates before0/0, with exact expected weight1/2. |
| supporting-fix-audit | research/discovery/20261014T194929Z-ais-tempered-fix-verification.json | supports | Separate bounded agent verification confirms four original audit dispositions in exact current bytes; it is not independent approval or a complete formal review. |
| predecessor | reviews/structured/20261014T194501Z-ais-path-and-locators/review.yaml | context_only | Immutable partial review with three same-target open findings, all retained in this successor. |
| correction | research/discovery/20261014T194609Z-ais-review-corrections.json | supports | Actual correction report preserves before/after bytes, issue links and exact zero-support guard result. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- The initial review YAML draft was rejected for serializer-generated anchors before saving; alias-free serialization validated and saved the immutable initial bundle.
- The first correction-history invocation rejected unsupported event UPDATE without creating a sidecar; the actual correction was recorded using EDIT.
- A separate supporting subagent mathematical audit and follow-up check supplement the author review; neither is independent scientific approval.
- This round adds one DRAFT concept, reaching 700 native and 442 unchanged AIO records. The main frontier has 885 entries, including 471 pending and 59 partly addressed cohorts; nested leads remain.
- All25pages and18bibliographic entries inspected. Pages1–13 and16–25 read as text; huge scatter-plot extraction artifacts on14–15 replaced by visual figure/caption reading. Core method/proof pages4–6 visually inspected. Other mathematical displays remain text-only.
- The inspected source is arXiv physics/9803008v2, submittedSeptember4,1998, with printed firstversionFebruary18 and revisedSeptember1. The author lists a2001journalpublication; journal-byte equivalence was not established. The author-hosted ais-rev.pdf uses garbled text encoding; the readable arXiv file has different bytes. No byte equivalence is assumed. The p6 intermediate-distribution paragraph says x_j is found after T_(j-1), inconsistent with the main Eq4 ordering, where x_j follows T_(j+1). Do not copy this indexing into a maintained algorithm. Invariance is required; reaching equilibrium at each stage is not. No general variance, mode-discovery or efficiency guarantee follows. More temperatures can leave rare-mode weights problematic. Finite-run normalized expectations and log normalizing-ratio estimates are not generally unbiased. Empirical effective-sample-size diagnostics can miss unobserved heavy tails. No author-code execution, model fitting, benchmark replication or certification of general asymptotic efficiency. S4, thermodynamic integration, regenerative variants and backward tempered-transition estimates are separate evidence/identity leads.
- The generic AIS estimator is added. Tempered transitions, nonreversible MCMC, linked importance sampling, thermodynamic integration and S4 retain separate evidence and identity requirements.
- Original Documents synchronization and old round141 cleanup remain unapproved after automatic-review rejection; only the isolated recovery worktree is modified.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T200216Z-annealed-importance-sampling
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Annealed importance sampling
started_at: '2026-10-14T19:57:45Z'
finished_at: '2026-10-14T20:02:16Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged support and zero-weight paths, chronological
    indexing, weighted versus unweighted outputs, normalizer unbiasedness versus ratio
    bias, and model-versus-method mappings. A separate bounded supporting agent math
    audit was also assessed. This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Retain AIS as a DRAFT native algorithm with a related Markov-process mapping.
  All three initial review findings are corrected with same-key predecessor lineage:
  zero-weight paths, Equation2 locator and the initial-draw indexing exception.'
source:
  git_revision: c924f97a3db72c41c068391adbbd8fd3690d5740
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/BoltzmannMachineNetwork.yaml
    sha256: 1152d2d85c5c1c408a0420e13f211ed109b12fb289c706ee7449864e91aece03
    role: context
  - path: data/aio/DataPreparation.yaml
    sha256: 99aebfc324b628969407ddc7591312e992db1469e7ef8fb3ad28e4b62d3bb359
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/Normalization.yaml
    sha256: ecdbd41476b6125c670855f1f00090047acd61f5ee16d71384f6b9ed86bea2bb
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ProbabilisticHiddenLayer.yaml
    sha256: 610c29db815f7348c5bdcdc7e7460dd2dea9ea338f3727ebb1596c51b4af41da
    role: context
  - path: data/aio/SelectionAndSamplingBias.yaml
    sha256: 72d8ef34949942ddee1fe60d645806a2117b95207f681de923297b64f78cc477
    role: context
  - path: data/curated/AnnealedImportanceSampling.yaml
    sha256: 94c7b8e597f3551b2b804778e11385d6ec9137515bc44a9c9d429268869f7e68
    role: target
  - path: data/curated/FixedLengthPoissonMarkovRandomField.yaml
    sha256: bf5c284066cbad094b3982f0b2adf8b8e67d62b697204ac7a584d7029a2e027d
    role: context
  - path: data/curated/MetropolisHastings.yaml
    sha256: 01cb22a25242e8564e2a7bb839ecb46da1bc49eb09b3c85200f9a596e05b99b4
    role: context
  - path: data/curated/ParallelTempering.yaml
    sha256: e2976bcbbe756cf1b943520c6c9d739b862213c2df4ab4f2806957b67db8d0eb
    role: context
  - path: data/curated/ProductOfHiddenMarkovModels.yaml
    sha256: 51fdf99954e91afb1d0ddda78bd60dc98991847715c2f1fe9ef2be4a7f46436e
    role: context
  - path: data/curated/ReplicatedSoftmax.yaml
    sha256: 1a71debad5b7ac38c8e647ffb18c52f712300a7906b44efa5d348fb3488940cf
    role: context
  - path: data/curated/SimulatedAnnealing.yaml
    sha256: 7e77f553c8b2afc4563dc7ef6cba2b53719f22b1fd02ed37d22de9821079d42c
    role: context
  - path: data/curated/SquareRootGraphicalModel.yaml
    sha256: 34125cf7fce0580e388de4cb4805c18712679fcd842c4bce48cae7a29728b89f
    role: context
  - path: research/discovery/20261014T082648Z-annealed-importance-sampling.json
    sha256: 5d99f3efdff0cd941141d080294f85232b65e3f4b60c2a3b1d66a16d46645ab3
    role: context
  - path: research/discovery/20261014T194311Z-ais-tempered-supporting-math-audit.json
    sha256: 4fd496660b8f67fdff5d93ebea24f245e8b4cfc293dec87a283ae9224a4f4c24
    role: context
  - path: research/discovery/20261014T194609Z-ais-review-corrections.json
    sha256: 62628b695dd8dc99c78486538c1b639241d51bbceb7a1a4e11708a45c81518b8
    role: context
  - path: research/discovery/20261014T194929Z-ais-tempered-fix-verification.json
    sha256: 29654c16fae36802d32f135267eaf80664c2d3c4c276a1a7734ca3113c6b7757
    role: context
  - path: research/discovery/ais-boundaries.py
    sha256: d72ed061089be457e8581a53b25a9966202b3ea2a2d0cd5f1118b5468703c59c
    role: context
  - path: reviews/structured/20261014T194501Z-ais-path-and-locators/review.yaml
    sha256: cdaec32a376e922eab9cca5614d42c1523e4b0b0fd67cc4329d9798c86cd304c
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
- target_id: AIMech:AnnealedImportanceSampling
  path: data/curated/AnnealedImportanceSampling.yaml
  label: Annealed importance sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AnnealedImportanceSampling.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:AnnealedImportanceSampling'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:AnnealedImportanceSampling
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Uninspected source versions and implementation components
    reason: No author implementation, journal-byte equivalence, general variance certification,
      continuous-state theorem certification or model benchmark replication. Source
      assumptions and finite-sample uncertainty remain explicit.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:AnnealedImportanceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 437.22s (0:07:17)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 701 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 392 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 393,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:AnnealedImportanceSampling
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
  - AIMech:AnnealedImportanceSampling
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
  - AIMech:AnnealedImportanceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/ais-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:AnnealedImportanceSampling
  exit_code: 0
  expected_exit_code: 0
  summary: '{"nonreversible_example": {"target": [1, 2, 7], "bridge": [1, 1, 1], "base":
    [3, 2, 1], "weighted_endpoint_mass": ["1/6", "1/3", "7/6"], "expected_weight":
    "5/3", "unweighted_endpoint_probability": ["1/6", "1/2", "1/3"], "target_probability":
    ["1/10", "1/5", "7/10"], "self_normalized_indicator_expected_value": {"one_run":
    "1/3", "two_runs": "967/2025", "target": "7/10"}, "expected_log_weight": 0.21485510211104045,
    "log_expected_weight": 0.5108256237659907}, "identity_kernel_reduces_to_plain_importance_sampling":
    true, "noninvariant_reset_expected_weight": "1/2", "invariant_family_cases": 192,
    "violated_support_example": {"expected_weight": "1", "actual_normalizing_ratio":
    "2"}, "nested_support_zero_path": {"functions": [[1, 0], [1, 0], [1, 1]], "guarded_weights":
    ["1", "0"], "ratio_evaluations": [2, 1], "expected_weight": "1/2", "actual_normalizing_ratio":
    "1/2", "zero_path_stops_before_undefined_ratio": true}, "scope": "Finite exact
    laws and counterexamples only. No continuous-state theorem certification, variance
    bound, benchmark replication, author implementation, paid provider or training."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T082648Z-annealed-importance-sampling.json
  accessed_at: '2026-10-14T19:57:45Z'
  support: supports
  summary: Compared AIS and tempered transitions against all 442 pinned AIO and 699
    native identities; no normalized match. Ignored- and hidden-inclusive three-checkout
    searches returned 1133,473,482 lines, collapsed into 132 unique content groups.
    Groups were classified using short full content and long-line paths/identity excerpts;
    full canonical model-neighbor records were read. Long generated search attributes
    and ignored dependency linguistic tables were not claimed as complete raw-code
    readings. Hits concern model-specific AIS uses, historical discovery/review context,
    pending methods and acronym noise. Semantic assessment covered 103 AIO and306
    native definitions, including47 and22 new rows;56 and284 prior rows were verified
    unchanged. Ten complete AIO contexts and seven full native neighbors assessed.
    AIS estimates expectations and normalizing-constant ratios using weighted annealing
    paths. It is distinct from annealing for optimization, parallel-temperature replica
    exchange, ordinary Metropolis–Hastings, an up/down tempered Metropolis transition,
    and model-specific uses of AIS already represented in AIMech.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-14T19:57:45Z'
  support: supports
  summary: Related MarkovChain preserves the algorithm-to-process distinction. Ten
    complete AIO contexts were assessed, including the Network parent and ProbabilisticHiddenLayer
    relation, which are not imported into AIS. Partition normalization does not match
    the data-normalization task; incidental graphical-model uses do not define algorithm
    equivalence. Seven full native neighbors distinguish existing model-specific applications
    and sampling/optimization methods.
- evidence_id: neal1998ais
  kind: primary_source
  reference: https://arxiv.org/pdf/physics/9803008v2
  locator: Section 2, PDF pp. 4–6, Equations 3–11; self-normalized estimate, Equation
    2, p. 2; Section 2, PDF pp. 4–6, Equations 4–11; support condition and invariance
    requirement, p. 4; zero-weight convention is a curator interpretation of the extended-space
    importance law, checked in research/discovery/ais-boundaries.py; Extended-space
    construction, PDF pp. 5–6, Equations 6–11; ratio estimate, Equation 12, p. 7;
    curator finite examples in research/discovery/ais-boundaries.py; Equations 4–11,
    PDF pp. 5–6; exact independently authored finite enumeration in research/discovery/ais-boundaries.py;
    Section 2, PDF pp. 4 and 6, Equation 3 and marginal-likelihood discussion; Section
    2, PDF p. 6; accuracy discussion, p. 8; Section 3, PDF pp. 7–8; Section 4, pp.
    8–11; examples, Sections 5–6, pp. 11–18; discussion, pp. 21–24
  accessed_at: '2026-10-14T07:51:05Z'
  snapshot_sha256: 6ae14b83d623438355c2de17a5e830d67a07fd5331b2eb997b82ed40174745cc
  support: supports
  summary: arXiv physics/9803008v2, submitted September 4, 1998; printed report first
    version February 18, revised September 1, 1998. All 25 pages and 18 references
    inspected, with figure pages 14–15 and core method pages 4–6 visually checked.
    Author metadata lists Statistics and Computing 11:125–139 (2001); journal-byte
    equivalence was not established.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/ais-boundaries.py
  accessed_at: '2026-10-14T19:59:04Z'
  snapshot_sha256: d72ed061089be457e8581a53b25a9966202b3ea2a2d0cd5f1118b5468703c59c
  support: supports
  summary: Exact three-state path enumeration checks weighted endpoint mass and the
    5/3 normalizer ratio despite nonreversible, nonmixing transitions; computes one-
    and two-run self-normalization bias; checks 192 invariant-kernel cases; exhibits
    failures for noninvariant kernels and missing support. No author implementation
    or benchmark replication. A valid nested-support zero-weight case terminates before0/0,
    with exact expected weight1/2.
- evidence_id: supporting-fix-audit
  kind: record_content
  reference: research/discovery/20261014T194929Z-ais-tempered-fix-verification.json
  accessed_at: '2026-10-14T19:49:29Z'
  snapshot_sha256: 29654c16fae36802d32f135267eaf80664c2d3c4c276a1a7734ca3113c6b7757
  support: supports
  summary: Separate bounded agent verification confirms four original audit dispositions
    in exact current bytes; it is not independent approval or a complete formal review.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261014T194501Z-ais-path-and-locators/review.yaml
  accessed_at: '2026-10-14T20:02:15Z'
  snapshot_sha256: cdaec32a376e922eab9cca5614d42c1523e4b0b0fd67cc4329d9798c86cd304c
  support: context_only
  summary: Immutable partial review with three same-target open findings, all retained
    in this successor.
- evidence_id: correction
  kind: record_content
  reference: research/discovery/20261014T194609Z-ais-review-corrections.json
  accessed_at: '2026-10-14T20:02:15Z'
  snapshot_sha256: 62628b695dd8dc99c78486538c1b639241d51bbceb7a1a4e11708a45c81518b8
  support: supports
  summary: Actual correction report preserves before/after bytes, issue links and
    exact zero-support guard result.
assessments:
- assessment_id: identity
  area: identity
  topic: Annealed importance sampling
  outcome: supported
  target_ids:
  - AIMech:AnnealedImportanceSampling
  evidence_ids:
  - identity
  - neal1998ais
  summary: Retain this distinct DRAFT algorithm.
  details: Retain AIS as a distinct weighted-path estimator. Model-specific uses in
    PoHMM, SQR, fixed-length Poisson MRF and replicated softmax do not supply a generic
    AIS identity. It differs from up/down accept/reject transitions, replica exchange
    and optimization annealing.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:AnnealedImportanceSampling
  evidence_ids:
  - mapping
  - neal1998ais
  summary: The explicit AIO mapping assessment is supported within its stated scope.
  details: Related MarkovChain preserves the algorithm-to-process distinction. Ten
    complete AIO contexts were assessed, including the Network parent and ProbabilisticHiddenLayer
    relation, which are not imported into AIS. Partition normalization does not match
    the data-normalization task; incidental graphical-model uses do not define algorithm
    equivalence. Seven full native neighbors distinguish existing model-specific applications
    and sampling/optimization methods.
- assessment_id: path-law-and-weight
  area: evidence
  topic: path-law-and-weight
  outcome: supported
  target_ids:
  - AIMech:AnnealedImportanceSampling
  evidence_ids:
  - neal1998ais
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The prescribed ordering and product agree with Equations4–5. Invariance
    is sufficient for the intermediate kernels; reversibility and full equilibration
    are unnecessary. Nested supports require the now-explicit chronological zero-weight
    stop. Zero runs remain observations of weight0 in the mean, and no endpoint observable
    or later undefined ratio is evaluated.
- assessment_id: estimand-and-unbiasedness-boundary
  area: evidence
  topic: estimand-and-unbiasedness-boundary
  outcome: supported
  target_ids:
  - AIMech:AnnealedImportanceSampling
  evidence_ids:
  - neal1998ais
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The extended-space law establishes weighted mass and mean-weight normalizer
    ratios under the stated assumptions. Ratios of random sums and logarithms do not
    inherit unbiasedness; all-zero normalized estimates are undefined. Exact finite
    examples distinguish unweighted endpoint probabilities and finite normalized-estimate
    bias.
- assessment_id: finite-weight-law-checks
  area: evidence
  topic: finite-weight-law-checks
  outcome: supported
  target_ids:
  - AIMech:AnnealedImportanceSampling
  evidence_ids:
  - neal1998ais
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The three-state nonreversible cycle reproduces5/3 expected weight and the
    specified endpoint masses; one/two-run normalized indicator expectations differ
    from7/10. The192 invariant-kernel cases pass. A valid nested-support case stops
    before0/0 and yields1/2, while genuinely missing target support or noninvariant
    kernels fail. These are exact finite examples only.
- assessment_id: bridge-and-bayesian-scope
  area: evidence
  topic: bridge-and-bayesian-scope
  outcome: supported
  target_ids:
  - AIMech:AnnealedImportanceSampling
  evidence_ids:
  - neal1998ais
  summary: Supported within the stated primary-source and mathematical scope.
  details: Geometric interpolation is optional. Proper base/intermediate distributions
    and likelihood constants matter; a shared prior constant cancels only in the specified
    ratio. No unsupported general temperature or normalizability guarantee is asserted.
- assessment_id: terminal-and-correlated-extensions
  area: evidence
  topic: terminal-and-correlated-extensions
  outcome: supported
  target_ids:
  - AIMech:AnnealedImportanceSampling
  evidence_ids:
  - neal1998ais
  summary: Supported within the stated primary-source and mathematical scope.
  details: A predetermined p0-invariant extension contributes its within-run average
    with the original weight. Dependence must be reflected in uncertainty. Ergodic
    correlated base sampling can support consistency, without claiming finite unbiasedness
    from an arbitrary initialization.
- assessment_id: diagnostic-and-efficiency-limits
  area: evidence
  topic: diagnostic-and-efficiency-limits
  outcome: supported
  target_ids:
  - AIMech:AnnealedImportanceSampling
  evidence_ids:
  - neal1998ais
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source explicitly warns that observed weight variance may miss unsampled
    important modes. Idealized temperature and dimension analyses are kept conditional;
    no universal efficiency or contemporary benchmark claim is imported.
- assessment_id: constructed-boundaries
  area: consistency
  topic: support and zero-weight paths, chronological indexing, weighted versus unweighted
    outputs, normalizer unbiasedness versus ratio bias, and model-versus-method mappings
  outcome: supported
  target_ids:
  - AIMech:AnnealedImportanceSampling
  evidence_ids:
  - neal1998ais
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact three-state path enumeration checks weighted endpoint mass and the
    5/3 normalizer ratio despite nonreversible, nonmixing transitions; computes one-
    and two-run self-normalization bias; checks 192 invariant-kernel cases; exhibits
    failures for noninvariant kernels and missing support. No author implementation
    or benchmark replication. A valid nested-support zero-weight case terminates before0/0,
    with exact expected weight1/2.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:AnnealedImportanceSampling
  evidence_ids:
  - identity
  - mapping
  - neal1998ais
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. All six claims, definition evidence, AIS alias, identity
    notes, source/version/access/hash, AIO pin and related mapping, limitations and
    curation times assessed. Zero-weight termination, Equation2 page2 and the initial-draw
    exception were checked against their exact predecessors, source equations, report
    mirror and finite guard result. The author assessed the separate bounded subagent
    audit without treating it as independent scientific approval.
- assessment_id: resolved-ais-findings
  area: consistency
  topic: Zero-weight support and source locators
  outcome: supported
  target_ids:
  - AIMech:AnnealedImportanceSampling
  evidence_ids:
  - predecessor
  - correction
  - neal1998ais
  - calculation
  - supporting-fix-audit
  summary: All three initial findings are resolved with explicit lineage.
  details: The zero path is retained with weight0 in the N-run mean; it stops before0/0
    or endpoint evaluation. Equation2 is on page2, and only states below the initial
    base draw follow T_(j+1). The initial bundle and audit remain immutable.
findings:
- finding_id: ais-zero-weight-path-convention
  issue_key: ais-zero-weight-path-convention
  category: representation
  severity: major
  status: resolved
  certainty: confirmed
  title: 'AIS: define zero-weight path handling under nested supports'
  description: The maintained field and exact report mirror now satisfy this finding’s
    acceptance criteria; the original observation remains unchanged.
  target_ids:
  - AIMech:AnnealedImportanceSampling
  field_paths:
  - claims[path-law-and-weight]
  evidence_ids:
  - predecessor
  - correction
  - neal1998ais
  - calculation
  - supporting-fix-audit
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AnnealedImportanceSampling.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261014T082648Z-annealed-importance-sampling.json
    role: report mirror
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/352
  disposition_reason: Full corrected record and primary passages were reread; zero-weight
    termination, inclusion in the attempted-run mean, Equation2 page2 and the top-index
    exception were verified. Exact report/calculation mirrors, actual history, required
    gates and the same-target predecessor identity agree. Ignored-inclusive review
    search found only the initial observation before this successor.
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261014T194501Z-ais-path-and-locators
    finding_id: ais-zero-weight-path-convention
- finding_id: ais-definition-equation-page
  issue_key: ais-definition-equation-page
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: 'AIS: correct Equation 2 definition locator to PDF page 2'
  description: The maintained field and exact report mirror now satisfy this finding’s
    acceptance criteria; the original observation remains unchanged.
  target_ids:
  - AIMech:AnnealedImportanceSampling
  field_paths:
  - definition_evidence[0].locator
  evidence_ids:
  - predecessor
  - correction
  - neal1998ais
  - calculation
  - supporting-fix-audit
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AnnealedImportanceSampling.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261014T082648Z-annealed-importance-sampling.json
    role: report mirror
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/353
  disposition_reason: Full corrected record and primary passages were reread; zero-weight
    termination, inclusion in the attempted-run mean, Equation2 page2 and the top-index
    exception were verified. Exact report/calculation mirrors, actual history, required
    gates and the same-target predecessor identity agree. Ignored-inclusive review
    search found only the initial observation before this successor.
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261014T194501Z-ais-path-and-locators
    finding_id: ais-definition-equation-page
- finding_id: ais-initial-state-index-exception
  issue_key: ais-initial-state-index-exception
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: 'AIS: qualify the intermediate-state indexing note at the initial draw'
  description: The maintained field and exact report mirror now satisfy this finding’s
    acceptance criteria; the original observation remains unchanged.
  target_ids:
  - AIMech:AnnealedImportanceSampling
  field_paths:
  - limitations[1]
  evidence_ids:
  - predecessor
  - correction
  - neal1998ais
  - calculation
  - supporting-fix-audit
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AnnealedImportanceSampling.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261014T082648Z-annealed-importance-sampling.json
    role: report mirror
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/354
  disposition_reason: Full corrected record and primary passages were reread; zero-weight
    termination, inclusion in the attempted-run mean, Equation2 page2 and the top-index
    exception were verified. Exact report/calculation mirrors, actual history, required
    gates and the same-target predecessor identity agree. Ignored-inclusive review
    search found only the initial observation before this successor.
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261014T194501Z-ais-path-and-locators
    finding_id: ais-initial-state-index-exception
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- The initial review YAML draft was rejected for serializer-generated anchors before
  saving; alias-free serialization validated and saved the immutable initial bundle.
- The first correction-history invocation rejected unsupported event UPDATE without
  creating a sidecar; the actual correction was recorded using EDIT.
- A separate supporting subagent mathematical audit and follow-up check supplement
  the author review; neither is independent scientific approval.
- This round adds one DRAFT concept, reaching 700 native and 442 unchanged AIO records.
  The main frontier has 885 entries, including 471 pending and 59 partly addressed
  cohorts; nested leads remain.
- All25pages and18bibliographic entries inspected. Pages1–13 and16–25 read as text;
  huge scatter-plot extraction artifacts on14–15 replaced by visual figure/caption
  reading. Core method/proof pages4–6 visually inspected. Other mathematical displays
  remain text-only.
- The inspected source is arXiv physics/9803008v2, submittedSeptember4,1998, with
  printed firstversionFebruary18 and revisedSeptember1. The author lists a2001journalpublication;
  journal-byte equivalence was not established. The author-hosted ais-rev.pdf uses
  garbled text encoding; the readable arXiv file has different bytes. No byte equivalence
  is assumed. The p6 intermediate-distribution paragraph says x_j is found after T_(j-1),
  inconsistent with the main Eq4 ordering, where x_j follows T_(j+1). Do not copy
  this indexing into a maintained algorithm. Invariance is required; reaching equilibrium
  at each stage is not. No general variance, mode-discovery or efficiency guarantee
  follows. More temperatures can leave rare-mode weights problematic. Finite-run normalized
  expectations and log normalizing-ratio estimates are not generally unbiased. Empirical
  effective-sample-size diagnostics can miss unobserved heavy tails. No author-code
  execution, model fitting, benchmark replication or certification of general asymptotic
  efficiency. S4, thermodynamic integration, regenerative variants and backward tempered-transition
  estimates are separate evidence/identity leads.
- The generic AIS estimator is added. Tempered transitions, nonreversible MCMC, linked
  importance sampling, thermodynamic integration and S4 retain separate evidence and
  identity requirements.
- Original Documents synchronization and old round141 cleanup remain unapproved after
  automatic-review rejection; only the isolated recovery worktree is modified.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261014T194501Z-ais-path-and-locators
  relationship: Resolves all three same-key AIS findings while completing the full
    author review.
links:
- https://github.com/CultureBotAI/AIMech/issues/352
- https://github.com/CultureBotAI/AIMech/issues/353
- https://github.com/CultureBotAI/AIMech/issues/354
tags:
- native-concepts
- self-review
- discovery-ongoing
```
