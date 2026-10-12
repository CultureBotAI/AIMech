# Scientific self-review of support-vector sphere clustering

- Review: 20261012T072446Z-support-vector-sphere
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T07:17:12Z
- Finished UTC: 2026-10-12T07:24:46Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete sphere-and-connectivity algorithm, related task mapping and source-qualified limitations are supported. No actionable finding remains in this record; the unavailable revision comparison and wider method frontier remain explicit.

## Scope And Provenance

All fields of AIMech:SupportVectorClustering.

Selection: Exact maintained ID, without sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e691d9dc081ac34ba62fcb8aebd4fb87a29ee9cf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SupportVectorClustering | data/curated/SupportVectorClustering.yaml | maintained | Support Vector Clustering |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:SupportVectorClustering | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 151.90s (0:02:31)<br>Checked 442 record(s); 0 failed.<br>Checked 502 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 152 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 148,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:SupportVectorClustering | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:SupportVectorClustering | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:SupportVectorClustering | Exited0 without output. |
| Exact Gaussian sphere boundary example | passed | True | AIMech:SupportVectorClustering | {"gaussian_kernel_off_diagonal": "1/2", "penalty": "1/2", "beta": ["1/2", "1/2"], "free_support_vectors": 0, "primal_dual_optimum": "1/4", "examples": [{"radius_squared": "0", "slack": ["1/4", "1/4"], "objective": "1/4"}, {"radius_squared": "1/8", "slack": ["1/8", "1/8"], "objective": "1/4"}, {"radius_squared": "1/4", "slack": ["0", "0"], "objective": "1/4"}], "conclusion": "No free support vector determines the radius. At squared radius1/4 both box-bound vectors lie on the boundary, not strictly outside. The displayed constraints alone give a non-strict bounded-vector count bound."} |

## Scientific And Domain Assessments

### Complete algorithm identity and AIO mapping direction

identity: supported. Targets: AIMech:SupportVectorClustering.

Retain the complete sphere-and-component clustering algorithm with a related unsupervised task mapping.

The support-description stage alone does not label components. Supervised hyperplane SVM, kernel variance objectives, label-matrix margin clustering, neighborhood density connectivity and mode updates do not denote this procedure. Parameter regimes are not separate identities. SVC is an explicitly scoped alias, not an assertion that every use of this acronym denotes the same method.

### sphere fit

evidence: supported. Targets: AIMech:SupportVectorClustering.

The stated mechanism or qualification is supported within the recorded source scope.

For N input observations, Gaussian kernel K(x,y)=exp(-q*&#124;&#124;x-y&#124;&#124;²), q&gt;0, and slack penalty C&gt;0, fit a center a and radius R by minimizing R²+C*sum_i xi_i subject to &#124;&#124;Phi(x_i)-a&#124;&#124;²&lt;=R²+xi_i and xi_i&gt;=0. The displayed dual maximizes sum_i beta_i*K_ii-beta^T*K*beta with sum_i beta_i=1 and 0&lt;=beta_i&lt;=C. Its feasibility requires N*C&gt;=1. The center is sum_i beta_i*Phi(x_i); kernel evaluation avoids explicitly constructing those features. The convex quadratic dual concerns sphere fitting, not globally optimal clustering or parameter selection. Locator: Section2.1, printed pp.126-127 / PDF pp.2-3, Equations1-11; feasibility follows by summing the box bounds

### radius and bound vectors

evidence: supported. Targets: AIMech:SupportVectorClustering.

The stated mechanism or qualification is supported within the recorded source scope.

The squared distance of a new input is K(x,x)-2*sum_i beta_i*K(x_i,x)+beta^T*K*beta. A free support vector with 0&lt;beta_i&lt;C lies on the sphere and supplies R. If no free support vector exists, the stated radius rule needs an additional convention. A coefficient beta_i=C permits distance equal to R as well as greater than R; bounded coefficients alone do not prove strict exclusion. With N=2, C=1/2 and Gaussian off-diagonal kernel value 1/2, beta=(1/2,1/2), and every squared radius from 0 to 1/4 with equal slacks 1/4-R² attains primal and dual value 1/4. At R²=1/4 both bounded vectors are on the boundary and no free vector exists. Locator: Section2.1, printed pp.127-128 / PDF pp.3-4, Equations3-14; curator exact two-observation KKT and primal-dual calculation

### component assignment

evidence: supported. Targets: AIMech:SupportVectorClustering.

The stated mechanism or qualification is supported within the recorded source scope.

For observations retained inside or on the sphere, form an edge when every point on their straight line segment in input space also maps inside or onto the sphere. Assign clusters as connected components of this observation graph. The reported implementation approximates each continuous segment test with 20 sampled points. Points treated as outliers are initially unassigned; leaving them unassigned or assigning them to a nearest cluster is an additional policy, and the paper uses the latter in its examples. Locator: Section2.2, printed p.128 / PDF p.4, Equation16 and following paragraphs

### finite connectivity

evidence: supported. Targets: AIMech:SupportVectorClustering.

The stated mechanism or qualification is supported within the recorded source scope.

An exact accepted segment gives a path inside the sphere preimage, but a graph on finitely many observations need not capture every path-connected component of that continuous set. Finite segment sampling can miss an excursion outside and introduce a false connection. The 20-sample implementation therefore has no stated exact topological recovery guarantee. Restricting adjacency tests to support vectors is a heuristic described in Section 5 reported to agree on the tried datasets, not a general equivalence proof. Locator: Section2.2, printed p.128 / PDF p.4; Section5, printed p.135 / PDF p.11; curator distinction between continuous paths and finite sampled edges

### scale and outlier control

evidence: supported. Targets: AIMech:SupportVectorClustering.

The stated mechanism or qualification is supported within the recorded source scope.

The parameters q and p=1/(N*C) explore spatial scale and allowable slack. Larger q means a narrower Gaussian; larger p means a smaller penalty C. The box and sum constraints imply that the fraction of coefficients at their upper bound is at most p; the paper’s stricter inequality requires remaining positive coefficient mass. High-p fits can describe cluster cores rather than the envelope of all data. The weighted kernel score sum_i beta_i*K(x_i,x) approaches the equal-weight Parzen score as p approaches 1, up to density normalization; this resemblance does not make the component procedure identical to mode seeking. Locator: Sections3.2-4, printed pp.130-133 / PDF pp.6-9, Equations17-22; bound qualification follows from Equations3,9

### selection and hierarchy

evidence: supported. Targets: AIMech:SupportVectorClustering.

The stated mechanism or qualification is supported within the recorded source scope.

The source proposes increasing q and adjusting p while monitoring support-vector fractions and stability. It explicitly reports counterexamples to a strict hierarchy when bounded support vectors are used. These choices do not provide a universal cluster-count selector or nested partition guarantee. Strong overlap may leave small cluster cores; the finite experiments also show sensitivity to retained PCA dimensions. Locator: Sections4.1-4.2 and 6, printed pp.134-136 / PDF pp.10-12

### computational scope

evidence: supported. Targets: AIMech:SupportVectorClustering.

The stated mechanism or qualification is supported within the recorded source scope.

The source uses an adapted sequential minimal optimization fit and sampled pairwise connectivity checks. With a fixed number of segment samples, straightforward labeling scales with retained-point pairs, nonzero-coefficient kernel evaluations and input dimension. The stated overall quadratic scaling assumes a bounded support-vector count and empirical solver behavior; it is not an unconditional complexity guarantee for all kernels or datasets. Locator: Section5, printed p.135 / PDF p.11

### KKT edge case, topology and global guarantees

consistency: supported. Targets: AIMech:SupportVectorClustering.

The draft preserves material qualifications to simplified source descriptions.

For the exact two-point Gaussian example, beta=(1/2,1/2) is the unique feasible coefficient vector at C=1/2; betaTKbeta=3/4 and each squared distance is1/4. Every R² in[0,1/4] with slacks1/4-R² has objective1/4, attaining the dual and proving optimality. At the upper endpoint both bounded coefficients are on the sphere. The strict count inequality also fails at p1 unless mass remains on free coefficients. Exact accepted segments provide paths but finite observation graphs can miss continuous connections; finitely sampled segments can add false connections. No invented tie, radius or topology repair is attributed to the source. The convex sphere QP does not select an optimal number of clusters.

### Exact evidence version and experimental boundaries

provenance: supported. Targets: AIMech:SupportVectorClustering.

The record preserves unavailable revision comparison and conditional empirical scope.

All13 current PDF pages were visually read. The main and MIT-mirror revision URLs returned404. Printed-to-PDF page offset124 and download hash are explicit. Iris two-PC results require combining returned clusters; higher-dimensional results differ. No numerical benchmark superiority is curated, no historical implementation executed and no claim of scientific approval for contextual records is made. Continued discovery includes428 pending cohorts.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:SupportVectorClustering. Retain one complete algorithm spanning its parameter regimes; distinguish the sphere support description, component assignment and adjacent methods.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://www.jmlr.org/papers/volume2/horn01a/horn01a.pdf; All13 PDF pages / printed pp.125-137, especially Sections2-5, Equations1-23 and Figures1-7 | supports | Read all thirteen rendered primary pages and reread the maintained claims against their locators. The sphere fit and segment graph are supported; categorical bounded-vector, exact-connectivity and global-clustering interpretations are qualified rather than repeated. This exact download is not asserted equivalent to the unavailable separately listed revision. |
| identity | research/discovery/20261012T071653Z-support-vector-sphere.json | supports | Compared all442 pinned AIO IDs, labels and scoped synonyms with all501 prior native IDs, names and aliases; no normalized identity collision for Support Vector Clustering or SVC. Full fixed-string searches of both checkouts included ignored and hidden files, expanded terminology, source identifiers and adjacent support-description names. They returned13 lines per checkout: nine distinct texts at26 locations, all inspected as query, bibliography or provisional frontier references in the preceding discovery ledger, not maintained concepts. Eight annotated AIO nodes and outgoing edges, eight generated records and five native neighbors distinguish the selected procedure. Absence is bounded to the inspected pin and corpus; inaccessible source revisions do not establish absence upstream.<br> |
| mapping | sources/aio/aio.json; Eight annotated class nodes and outgoing edges, eight generated YAMLs and five native contextual records | supports | The procedure performs the inspected unlabeled clustering task, so AIO:UnsupervisedClustering is a related task mapping, not algorithm-task identity or an upstream subclass assertion. Inspected eight annotated AIO nodes and their generated records: UnsupervisedClustering, Clustering, UnsupervisedLearning, MachineLearningTask, SupportVectorMachine, Network, KernelLayer and Model. The supervised classification/regression network definition of SupportVectorMachine does not cover this unsupervised sphere-and-connectivity algorithm; a shared support-vector name is insufficient. Generic networks, kernel layers and model abstractions do not specify it. All442 AIO class labels and153 semantic matches reuse byte-verified prior readings; expanded support/sphere/density/novelty/anomaly searches add no rows. KernelPCA, KernelKMeans and SemidefiniteMaximumMarginClustering were checked against their unchanged complete readings; DBSCAN and MeanShift were fully read as additional context. Their projections, variance objectives, label matrices, neighborhoods and mode updates differ from the selected sphere preimage and segment graph. Context is not renewed scientific approval.<br> |
| versions | https://www.jmlr.org/papers/v2/; Support Vector Clustering entry and separately listed January2002 revision; captured access attempts in discovery ledger | context_only | The index distinguishes a revision. Both official revision PDF links returned404 in direct authorized fetches; the record preserves the current exact PDF URL/hash and does not assert equivalence. This is a provenance limitation, not evidence that the method is absent. |
| finite-example | research/discovery/support-vector-sphere-boundaries.py; Two-observation Gaussian Gram matrix and three representative radii | supports | Gaussian off-diagonal1/2 with N2,C1/2 forces beta=(1/2,1/2). The midpoint has distance²1/4 to each input. Every R² in[0,1/4] with corresponding equal slacks attains primal/dual1/4; at the upper radius both bounded vectors lie on the boundary. This also demonstrates that the strict bounded-count bound needs positive coefficient mass elsewhere. The code checks three representatives; the entire interval follows from the displayed linear objective. |

## Limits And Additional Notes

- Adversarial author self-review only; the record remains DRAFT.
- Temporary review serialization initially used context instead of the required context_only evidence-support value. Validation rejected it before saving; the value was corrected and the complete review revalidated.
- The official13-page PDF was read in full, including all seven figures, equations and bibliography. Printed pp.125-137 correspond to PDF pp.1-13.
- The separately listed January2002 revision URLs on jmlr.org and the MIT mirror returned404. The record names the exact inspected URL and SHA without asserting it equals the inaccessible revision.
- The initial sandbox download failed DNS resolution; the permitted network retry succeeded. No paper was copied into the repository.
- The exact two-point example checks a degenerate but feasible Gaussian sphere problem; it is not historical optimizer or benchmark execution.
- All record claims and scientific qualifications were reread against the paper; no universal performance or exact topology claim is made.
- 502 native DRAFT concepts after this addition;442 pinned AIO records unchanged. There remain428 pending cohorts and other unresolved dispositions; no saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T072446Z-support-vector-sphere
kind: record
repository: CultureBotAI/AIMech
title: Scientific self-review of support-vector sphere clustering
started_at: '2026-10-12T07:17:12Z'
finished_at: '2026-10-12T07:24:46Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent read all13 primary PDF pages, inspected
    ignored-inclusive identity matches and mapping context, reread the final YAML,
    and challenged KKT, recovery, connectivity, scaling and version claims with an
    exact example. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete sphere-and-connectivity algorithm, related task mapping and
  source-qualified limitations are supported. No actionable finding remains in this
  record; the unavailable revision comparison and wider method frontier remain explicit.
source:
  git_revision: e691d9dc081ac34ba62fcb8aebd4fb87a29ee9cf
  state: working_tree
  inputs:
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/KernelLayer.yaml
    sha256: 0723e7f15d57807a1f922cd87b878593fb167757c7429dd06e99bde723290d43
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/Network.yaml
    sha256: ec24eb397241fe903137b2d8c8f4081d0f9d246c296c247864f199e160a3ee30
    role: context
  - path: data/aio/SupportVectorMachine.yaml
    sha256: 0cc2faa913fdafdc539a7d04d08d26c0963f77ad3ca26b833b29ed3ed313e4e0
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/DBSCAN.yaml
    sha256: de7d744d1f7761af64ce963cf5759853d70a586b4188eea757751357e5035f44
    role: context
  - path: data/curated/KernelKMeans.yaml
    sha256: a5fe0bf0d883e32d689c79c232d8a8093b0ab29a56df616a5ef367e931aca84a
    role: context
  - path: data/curated/KernelPCA.yaml
    sha256: a93227a6b2d6b2b89b679b8f7f9ddd5054741d1c11f9510490d82a3e691a1cab
    role: context
  - path: data/curated/MeanShift.yaml
    sha256: 3e6868e9d4786ef56fc10af3e1b9e8fd8a3cd15fa8e63d058ba99a3d9567448a
    role: context
  - path: data/curated/SemidefiniteMaximumMarginClustering.yaml
    sha256: 9cfe6597d65d6a9dae4040f56bade8cba946a4b09c82c8f0b5adbec8b66a59dc
    role: context
  - path: data/curated/SupportVectorClustering.yaml
    sha256: f15f79f69443b23faa8247bb4fb67d86caeb2a80a86ae0e8c97dd247e152ad3a
    role: target
  - path: research/discovery/20261012T071653Z-support-vector-sphere.json
    sha256: 26a5c75316bf7ab14b402cc64e1369c50418cf1e1a8570955fe5cf655bc8c95d
    role: context
  - path: research/discovery/support-vector-sphere-boundaries.py
    sha256: e5882fc151b317e928f7a4e8db38c944b21d6b42a59d788d74f699c0eb38897c
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
- target_id: AIMech:SupportVectorClustering
  path: data/curated/SupportVectorClustering.yaml
  label: Support Vector Clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SupportVectorClustering.yaml
    role: maintained
scope:
  description: All fields of AIMech:SupportVectorClustering.
  selection: Exact maintained ID, without sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SupportVectorClustering
  exclusions:
  - target: Thirteen contextual AIO/native YAMLs
    reason: Identity and mapping context without renewed scientific approval.
  - target: Historical implementation and benchmark reproduction
    reason: An exact finite mathematical example was checked; no historical solver
      or benchmark run.
  - target: Separately listed January2002 revision
    reason: Official revision PDF links returned404; equivalence to current downloaded
      bytes is not asserted.
  - target: Generated website
    reason: Freshness is checked, without a separate visual-design review.
  - target: Remaining discovery frontier
    reason: 428 pending cohorts and other unresolved dispositions remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:SupportVectorClustering
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 151.90s (0:02:31)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 502 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 152 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 148,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:SupportVectorClustering
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
  - AIMech:SupportVectorClustering
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
  - AIMech:SupportVectorClustering
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: finite-boundary
  name: Exact Gaussian sphere boundary example
  command: python3 research/discovery/support-vector-sphere-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SupportVectorClustering
  exit_code: 0
  expected_exit_code: 0
  summary: '{"gaussian_kernel_off_diagonal": "1/2", "penalty": "1/2", "beta": ["1/2",
    "1/2"], "free_support_vectors": 0, "primal_dual_optimum": "1/4", "examples": [{"radius_squared":
    "0", "slack": ["1/4", "1/4"], "objective": "1/4"}, {"radius_squared": "1/8", "slack":
    ["1/8", "1/8"], "objective": "1/4"}, {"radius_squared": "1/4", "slack": ["0",
    "0"], "objective": "1/4"}], "conclusion": "No free support vector determines the
    radius. At squared radius1/4 both box-bound vectors lie on the boundary, not strictly
    outside. The displayed constraints alone give a non-strict bounded-vector count
    bound."}'
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume2/horn01a/horn01a.pdf
  locator: All13 PDF pages / printed pp.125-137, especially Sections2-5, Equations1-23
    and Figures1-7
  accessed_at: '2026-10-12T07:04:07Z'
  snapshot_sha256: 001d2385ad19bc0d71c6bde187ccc8b54acd38bfca615c69e04ae4734fd0ddff
  support: supports
  summary: Read all thirteen rendered primary pages and reread the maintained claims
    against their locators. The sphere fit and segment graph are supported; categorical
    bounded-vector, exact-connectivity and global-clustering interpretations are qualified
    rather than repeated. This exact download is not asserted equivalent to the unavailable
    separately listed revision.
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T071653Z-support-vector-sphere.json
  accessed_at: '2026-10-12T07:17:12Z'
  support: supports
  summary: 'Compared all442 pinned AIO IDs, labels and scoped synonyms with all501
    prior native IDs, names and aliases; no normalized identity collision for Support
    Vector Clustering or SVC. Full fixed-string searches of both checkouts included
    ignored and hidden files, expanded terminology, source identifiers and adjacent
    support-description names. They returned13 lines per checkout: nine distinct texts
    at26 locations, all inspected as query, bibliography or provisional frontier references
    in the preceding discovery ledger, not maintained concepts. Eight annotated AIO
    nodes and outgoing edges, eight generated records and five native neighbors distinguish
    the selected procedure. Absence is bounded to the inspected pin and corpus; inaccessible
    source revisions do not establish absence upstream.

    '
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Eight annotated class nodes and outgoing edges, eight generated YAMLs and
    five native contextual records
  accessed_at: '2026-10-12T07:17:12Z'
  support: supports
  summary: 'The procedure performs the inspected unlabeled clustering task, so AIO:UnsupervisedClustering
    is a related task mapping, not algorithm-task identity or an upstream subclass
    assertion. Inspected eight annotated AIO nodes and their generated records: UnsupervisedClustering,
    Clustering, UnsupervisedLearning, MachineLearningTask, SupportVectorMachine, Network,
    KernelLayer and Model. The supervised classification/regression network definition
    of SupportVectorMachine does not cover this unsupervised sphere-and-connectivity
    algorithm; a shared support-vector name is insufficient. Generic networks, kernel
    layers and model abstractions do not specify it. All442 AIO class labels and153
    semantic matches reuse byte-verified prior readings; expanded support/sphere/density/novelty/anomaly
    searches add no rows. KernelPCA, KernelKMeans and SemidefiniteMaximumMarginClustering
    were checked against their unchanged complete readings; DBSCAN and MeanShift were
    fully read as additional context. Their projections, variance objectives, label
    matrices, neighborhoods and mode updates differ from the selected sphere preimage
    and segment graph. Context is not renewed scientific approval.

    '
- evidence_id: versions
  kind: primary_source
  reference: https://www.jmlr.org/papers/v2/
  locator: Support Vector Clustering entry and separately listed January2002 revision;
    captured access attempts in discovery ledger
  accessed_at: '2026-10-12T07:17:12Z'
  support: context_only
  summary: The index distinguishes a revision. Both official revision PDF links returned404
    in direct authorized fetches; the record preserves the current exact PDF URL/hash
    and does not assert equivalence. This is a provenance limitation, not evidence
    that the method is absent.
- evidence_id: finite-example
  kind: record_content
  reference: research/discovery/support-vector-sphere-boundaries.py
  locator: Two-observation Gaussian Gram matrix and three representative radii
  accessed_at: '2026-10-12T07:17:12Z'
  snapshot_sha256: e5882fc151b317e928f7a4e8db38c944b21d6b42a59d788d74f699c0eb38897c
  support: supports
  summary: Gaussian off-diagonal1/2 with N2,C1/2 forces beta=(1/2,1/2). The midpoint
    has distance²1/4 to each input. Every R² in[0,1/4] with corresponding equal slacks
    attains primal/dual1/4; at the upper radius both bounded vectors lie on the boundary.
    This also demonstrates that the strict bounded-count bound needs positive coefficient
    mass elsewhere. The code checks three representatives; the entire interval follows
    from the displayed linear objective.
assessments:
- assessment_id: identity-and-scope
  area: identity
  topic: Complete algorithm identity and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:SupportVectorClustering
  evidence_ids:
  - identity
  - mapping
  - primary
  summary: Retain the complete sphere-and-component clustering algorithm with a related
    unsupervised task mapping.
  details: The support-description stage alone does not label components. Supervised
    hyperplane SVM, kernel variance objectives, label-matrix margin clustering, neighborhood
    density connectivity and mode updates do not denote this procedure. Parameter
    regimes are not separate identities. SVC is an explicitly scoped alias, not an
    assertion that every use of this acronym denotes the same method.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A complete fitting and component-assignment procedure, not a trained
      instance.
    evidence_ids:
    - primary
  - name: aio-mapping
    value: related_match
    definition: The AIO target is the related UnsupervisedClustering task; no equivalence
      or upstream subclass is asserted.
    evidence_ids:
    - mapping
- assessment_id: sphere-fit
  area: evidence
  topic: sphere fit
  outcome: supported
  target_ids:
  - AIMech:SupportVectorClustering
  evidence_ids:
  - primary
  summary: The stated mechanism or qualification is supported within the recorded
    source scope.
  details: 'For N input observations, Gaussian kernel K(x,y)=exp(-q*||x-y||²), q>0,
    and slack penalty C>0, fit a center a and radius R by minimizing R²+C*sum_i xi_i
    subject to ||Phi(x_i)-a||²<=R²+xi_i and xi_i>=0. The displayed dual maximizes
    sum_i beta_i*K_ii-beta^T*K*beta with sum_i beta_i=1 and 0<=beta_i<=C. Its feasibility
    requires N*C>=1. The center is sum_i beta_i*Phi(x_i); kernel evaluation avoids
    explicitly constructing those features. The convex quadratic dual concerns sphere
    fitting, not globally optimal clustering or parameter selection. Locator: Section2.1,
    printed pp.126-127 / PDF pp.2-3, Equations1-11; feasibility follows by summing
    the box bounds'
- assessment_id: radius-and-bound-vectors
  area: evidence
  topic: radius and bound vectors
  outcome: supported
  target_ids:
  - AIMech:SupportVectorClustering
  evidence_ids:
  - primary
  - finite-example
  summary: The stated mechanism or qualification is supported within the recorded
    source scope.
  details: 'The squared distance of a new input is K(x,x)-2*sum_i beta_i*K(x_i,x)+beta^T*K*beta.
    A free support vector with 0<beta_i<C lies on the sphere and supplies R. If no
    free support vector exists, the stated radius rule needs an additional convention.
    A coefficient beta_i=C permits distance equal to R as well as greater than R;
    bounded coefficients alone do not prove strict exclusion. With N=2, C=1/2 and
    Gaussian off-diagonal kernel value 1/2, beta=(1/2,1/2), and every squared radius
    from 0 to 1/4 with equal slacks 1/4-R² attains primal and dual value 1/4. At R²=1/4
    both bounded vectors are on the boundary and no free vector exists. Locator: Section2.1,
    printed pp.127-128 / PDF pp.3-4, Equations3-14; curator exact two-observation
    KKT and primal-dual calculation'
- assessment_id: component-assignment
  area: evidence
  topic: component assignment
  outcome: supported
  target_ids:
  - AIMech:SupportVectorClustering
  evidence_ids:
  - primary
  summary: The stated mechanism or qualification is supported within the recorded
    source scope.
  details: 'For observations retained inside or on the sphere, form an edge when every
    point on their straight line segment in input space also maps inside or onto the
    sphere. Assign clusters as connected components of this observation graph. The
    reported implementation approximates each continuous segment test with 20 sampled
    points. Points treated as outliers are initially unassigned; leaving them unassigned
    or assigning them to a nearest cluster is an additional policy, and the paper
    uses the latter in its examples. Locator: Section2.2, printed p.128 / PDF p.4,
    Equation16 and following paragraphs'
- assessment_id: finite-connectivity
  area: evidence
  topic: finite connectivity
  outcome: supported
  target_ids:
  - AIMech:SupportVectorClustering
  evidence_ids:
  - primary
  summary: The stated mechanism or qualification is supported within the recorded
    source scope.
  details: 'An exact accepted segment gives a path inside the sphere preimage, but
    a graph on finitely many observations need not capture every path-connected component
    of that continuous set. Finite segment sampling can miss an excursion outside
    and introduce a false connection. The 20-sample implementation therefore has no
    stated exact topological recovery guarantee. Restricting adjacency tests to support
    vectors is a heuristic described in Section 5 reported to agree on the tried datasets,
    not a general equivalence proof. Locator: Section2.2, printed p.128 / PDF p.4;
    Section5, printed p.135 / PDF p.11; curator distinction between continuous paths
    and finite sampled edges'
- assessment_id: scale-and-outlier-control
  area: evidence
  topic: scale and outlier control
  outcome: supported
  target_ids:
  - AIMech:SupportVectorClustering
  evidence_ids:
  - primary
  - finite-example
  summary: The stated mechanism or qualification is supported within the recorded
    source scope.
  details: 'The parameters q and p=1/(N*C) explore spatial scale and allowable slack.
    Larger q means a narrower Gaussian; larger p means a smaller penalty C. The box
    and sum constraints imply that the fraction of coefficients at their upper bound
    is at most p; the paper’s stricter inequality requires remaining positive coefficient
    mass. High-p fits can describe cluster cores rather than the envelope of all data.
    The weighted kernel score sum_i beta_i*K(x_i,x) approaches the equal-weight Parzen
    score as p approaches 1, up to density normalization; this resemblance does not
    make the component procedure identical to mode seeking. Locator: Sections3.2-4,
    printed pp.130-133 / PDF pp.6-9, Equations17-22; bound qualification follows from
    Equations3,9'
- assessment_id: selection-and-hierarchy
  area: evidence
  topic: selection and hierarchy
  outcome: supported
  target_ids:
  - AIMech:SupportVectorClustering
  evidence_ids:
  - primary
  summary: The stated mechanism or qualification is supported within the recorded
    source scope.
  details: 'The source proposes increasing q and adjusting p while monitoring support-vector
    fractions and stability. It explicitly reports counterexamples to a strict hierarchy
    when bounded support vectors are used. These choices do not provide a universal
    cluster-count selector or nested partition guarantee. Strong overlap may leave
    small cluster cores; the finite experiments also show sensitivity to retained
    PCA dimensions. Locator: Sections4.1-4.2 and 6, printed pp.134-136 / PDF pp.10-12'
- assessment_id: computational-scope
  area: evidence
  topic: computational scope
  outcome: supported
  target_ids:
  - AIMech:SupportVectorClustering
  evidence_ids:
  - primary
  summary: The stated mechanism or qualification is supported within the recorded
    source scope.
  details: 'The source uses an adapted sequential minimal optimization fit and sampled
    pairwise connectivity checks. With a fixed number of segment samples, straightforward
    labeling scales with retained-point pairs, nonzero-coefficient kernel evaluations
    and input dimension. The stated overall quadratic scaling assumes a bounded support-vector
    count and empirical solver behavior; it is not an unconditional complexity guarantee
    for all kernels or datasets. Locator: Section5, printed p.135 / PDF p.11'
- assessment_id: mathematical-challenge
  area: consistency
  topic: KKT edge case, topology and global guarantees
  outcome: supported
  target_ids:
  - AIMech:SupportVectorClustering
  evidence_ids:
  - primary
  - finite-example
  summary: The draft preserves material qualifications to simplified source descriptions.
  details: For the exact two-point Gaussian example, beta=(1/2,1/2) is the unique
    feasible coefficient vector at C=1/2; betaTKbeta=3/4 and each squared distance
    is1/4. Every R² in[0,1/4] with slacks1/4-R² has objective1/4, attaining the dual
    and proving optimality. At the upper endpoint both bounded coefficients are on
    the sphere. The strict count inequality also fails at p1 unless mass remains on
    free coefficients. Exact accepted segments provide paths but finite observation
    graphs can miss continuous connections; finitely sampled segments can add false
    connections. No invented tie, radius or topology repair is attributed to the source.
    The convex sphere QP does not select an optimal number of clusters.
- assessment_id: versions-and-evaluation
  area: provenance
  topic: Exact evidence version and experimental boundaries
  outcome: supported
  target_ids:
  - AIMech:SupportVectorClustering
  evidence_ids:
  - primary
  - versions
  summary: The record preserves unavailable revision comparison and conditional empirical
    scope.
  details: All13 current PDF pages were visually read. The main and MIT-mirror revision
    URLs returned404. Printed-to-PDF page offset124 and download hash are explicit.
    Iris two-PC results require combining returned clusters; higher-dimensional results
    differ. No numerical benchmark superiority is curated, no historical implementation
    executed and no claim of scientific approval for contextual records is made. Continued
    discovery includes428 pending cohorts.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:SupportVectorClustering
  evidence_ids:
  - identity
  - mapping
  - primary
  rationale: Retain one complete algorithm spanning its parameter regimes; distinguish
    the sphere support description, component assignment and adjacent methods.
limitations:
- Adversarial author self-review only; the record remains DRAFT.
- Temporary review serialization initially used context instead of the required context_only
  evidence-support value. Validation rejected it before saving; the value was corrected
  and the complete review revalidated.
- The official13-page PDF was read in full, including all seven figures, equations
  and bibliography. Printed pp.125-137 correspond to PDF pp.1-13.
- The separately listed January2002 revision URLs on jmlr.org and the MIT mirror returned404.
  The record names the exact inspected URL and SHA without asserting it equals the
  inaccessible revision.
- The initial sandbox download failed DNS resolution; the permitted network retry
  succeeded. No paper was copied into the repository.
- The exact two-point example checks a degenerate but feasible Gaussian sphere problem;
  it is not historical optimizer or benchmark execution.
- All record claims and scientific qualifications were reread against the paper; no
  universal performance or exact topology claim is made.
- 502 native DRAFT concepts after this addition;442 pinned AIO records unchanged.
  There remain428 pending cohorts and other unresolved dispositions; no saturation.
links: []
tags:
- native-concepts
- support-vector-clustering
- self-review
- discovery-ongoing
```
