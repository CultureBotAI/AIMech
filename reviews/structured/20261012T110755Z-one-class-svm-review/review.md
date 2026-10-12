# Scientific self-review of the original one-class support vector machine

- Review: 20261012T110755Z-one-class-svm-review
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T11:03:38Z
- Finished UTC: 2026-10-12T11:07:55Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the source-scoped one-class estimator as a distinct native algorithm. No actionable finding remains in the selected record; kernel, offset, count and evidence limits are explicit.

## Scope And Provenance

Every field of one maintained one-class support vector machine record.

Selection: Exact maintained ID AIMech:OneClassSupportVectorMachine.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 466d27ac2a4353d49c8ad16ed5912c8f30e466f8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:OneClassSupportVectorMachine | data/curated/OneClassSupportVectorMachine.yaml | maintained | One-class support vector machine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:OneClassSupportVectorMachine | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 107.20s (0:01:47)<br>Checked 442 record(s); 0 failed.<br>Checked 520 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 167 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 163,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:OneClassSupportVectorMachine | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:OneClassSupportVectorMachine | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:OneClassSupportVectorMachine | Exited0 without output. |
| Exact OCSVM boundary examples | passed | True | AIMech:OneClassSupportVectorMachine | {"scope": "Exact rational mathematical examples; no historical solver or benchmark was run.", "nonconstant_diagonal": {"kernel": "k(x,y)=xy", "points": [1, 2], "nu": "1/4", "C": "2", "ocsvm": {"alpha": ["1", "0"], "w": "1", "rho": "1", "acceptance": "x&gt;=1"}, "svdd": {"alpha": ["1/2", "1/2"], "center": "3/2", "radius_squared": "1/4", "acceptance": "1&lt;=x&lt;=2"}, "interpretation": "Equal sample and penalty do not make the methods identical for arbitrary kernels."}, "nu_one": {"scores": ["3/2", "3"], "thresholds": [3, 4], "objectives": ["-9/8", "-9/8"], "accepted_training_points": [[false, true], [false, false]], "interpretation": "Uniform expansion weights do not uniquely determine the acceptance threshold."}, "finite_boundary_mass": {"kernel": "k(x,y)=1+xy, feature map (1,x)", "points": ["-3/4", "-1/4", "1/4", "3/4"], "nu": "1/2", "rho": "1", "strict_training_outlier_fraction": "0", "support_vector_fraction": "1", "interpretation": "Finite nu bounds need not be equalities, and analyticity alone does not force a nonconstant fitted score. This finite example is not an iid asymptotic counterexample."}} |

## Scientific And Domain Assessments

### Distinct one-class hyperplane estimator

identity: supported. Targets: AIMech:OneClassSupportVectorMachine.

Retain a separate algorithm identity.

A support-estimation algorithm that optimizes a kernel feature-space score relative to the origin using a norm penalty, a learned offset and linearly penalized shortfalls controlled by nu, then accepts a query when its score meets the learned threshold. This record denotes the original origin-relative one-class hyperplane support estimator in Scholkopf, Platt, Shawe-Taylor, Smola and Williamson (2001). It does not denote supervised nu-SVC or nu-SVR, sphere-fitting SVDD, support-vector clustering with component assignment, or later negative-example feature extraction. Compared all442 pinned AIO IDs, labels and scoped synonyms with all519 preceding native IDs, names and aliases, with no normalized collision. Fixed-string whole-word searches in both checkouts included ignored and hidden files, expanded names, acronyms, DOI and paper identifiers. All11 distinct matched-text windows were read; the locations are prior discovery leads and neighboring method context. All125 semantic AIO rows and114 native identity rows exactly match the preceding read capture; the additional RAPID row and full record were read. Thirty complete contextual record readings were retained with matching hashes. Absence is bounded to the inspected pin and corpus.

### Task and supervised-network relations

grounding: supported. Targets: AIMech:OneClassSupportVectorMachine.

Both related mappings preserve the abstraction and supervision distinctions.

The AIO target describes the task of learning patterns from unlabeled observations, whereas this local record specifies one support-estimation algorithm. The relation captures that learning setting without equating an algorithm with a task or asserting a subclass edge. Users may supply a selected target class; the mathematical objective does not require negative training examples. BinaryClassification and Classification inherit supervised task scope and do not identify this objective. KernelLayer is a neural component, and generic Model/Network nodes do not identify the estimator. The origin-relative kernel hyperplane and norm/slack optimization are directly related to support-vector classification. The pinned AIO target specifically describes a supervised category-separating network, so it is not treated as an exact or broader identity for this one-class support estimator. The source explicitly derives the connection and its changed objective. Native SVDD has only a conditional constant-diagonal correspondence; KernelPCA optimizes variance directions and SVC additionally assigns connected components.

### soft origin objective

evidence: supported. Targets: AIMech:OneClassSupportVectorMachine.

Supported within the declared mathematical and source scope.

For a nonempty sample of n observations, a positive-semidefinite kernel with feature map Phi, and 0&lt;nu&lt;=1, minimize (1/2)&#124;&#124;w&#124;&#124;^2 + sum_i xi_i/(nu*n) - rho subject to w.Phi(x_i)&gt;=rho-xi_i and xi_i&gt;=0. The offset rho is unrestricted. The method learns from the supplied observations without requiring a representative negative class. It does not minimize input-space Lebesgue volume, and a degenerate feature configuration need not yield a nonzero separating normal. Locator: Sections 2-3, PDF pp3-5 / printed pp1445-1447, Equations 3.1-3.6

### dual score and threshold

evidence: supported. Targets: AIMech:OneClassSupportVectorMachine.

Supported within the declared mathematical and source scope.

The dual minimizes (1/2)*alpha^T*K*alpha subject to sum_i alpha_i=1 and 0&lt;=alpha_i&lt;=C, where C=1/(nu*n). The score is g(x)=sum_i alpha_i*k(x_i,x); accept g(x)&gt;=rho, including equality. A coefficient strictly between zero and C fixes rho=g(x_i). Such a coefficient need not exist. KKT conditions instead bound rho below by max_{alpha_i&gt;0} g(x_i) and above by min_{alpha_i&lt;C} g(x_i); an empty upper-bound set gives no finite upper bound. Different optimal offsets can give different acceptance regions. The primal normal is fixed by strict convexity in w, while coefficients can be nonunique for a singular Gram matrix. Locator: Section 3, PDF pp4-6 / printed pp1446-1448, Equations 3.4-3.12 and sign convention; KKT interval derived from these constraints; research/discovery/ocsvm-boundaries.py

### finite nu bounds

evidence: supported. Targets: AIMech:OneClassSupportVectorMachine.

Supported within the declared mathematical and source scope.

At an exact optimum, nu bounds the fraction of strictly rejected training observations from above and the fraction of positive expansion coefficients from below. The paper states these properties under rho!=0. Neither bound requires equality in a finite sample; a coefficient at its upper bound can lie on the accepted boundary. A support-vector count is not a calibrated future rejection probability or a guaranteed sparse fraction. With the analytic nonconstant kernel k(x,y)=1+x*y and four balanced points -3/4,-1/4,1/4,3/4, nu=1/2 admits optimal weights 1/4, rho=1 and a constant score: all four points are support vectors and none is rejected. This is a finite illustration, not an iid asymptotic counterexample. Locator: Section 5 Proposition 3, PDF p11 / printed p1453; Appendix B proof sketch, PDF p23 / printed p1465; curator calculation in research/discovery/ocsvm-boundaries.py

### sphere correspondence

evidence: supported. Targets: AIMech:OneClassSupportVectorMachine.

Supported within the declared mathematical and source scope.

For 0&lt;nu&lt;1, a kernel whose diagonal k(x,x) is constant over both training and query inputs makes the matched-penalty SVDD and hyperplane dual objectives differ only by scale and a constant. Compatible radius and offset choices then give the same acceptance rule. This restricted correspondence does not identify the algorithms for arbitrary kernels. For linear-kernel observations 1 and 2 with nu=1/4, the exact hyperplane rule accepts x&gt;=1, while matched-penalty SVDD accepts only 1&lt;=x&lt;=2. Training-only diagonal equality also does not justify dropping the query diagonal. Locator: Section 3, PDF pp6-7 / printed pp1448-1449, Equations 3.13-3.17 and following comparison; curator calculation in research/discovery/ocsvm-boundaries.py

### pairwise optimization

evidence: supported. Targets: AIMech:OneClassSupportVectorMachine.

Supported within the declared mathematical and source scope.

The proposed SMO adaptation updates two coefficients while preserving their sum and the box constraints. For positive pair curvature k_ii+k_jj-2*k_ij, the unconstrained second-coefficient update adds (g_i-g_j)/(k_ii+k_jj-2*k_ij), then clips to the jointly feasible interval before recovering the first coefficient. Zero curvature cannot be handled by dividing that formula. The paper alternates full and non-bound KKT scans and refers to fallback selection rules; it also discusses tolerance adjustments and a modification for pathological convergence cases. This describes an optimization procedure, not a universal runtime or implementation-convergence guarantee. Locator: Section 4, PDF pp7-9 / printed pp1449-1451, Equations 4.1-4.8 and termination discussion

### density and endpoint

evidence: supported. Targets: AIMech:OneClassSupportVectorMachine.

Supported within the declared mathematical and source scope.

At nu=1 the constraints force every expansion coefficient to 1/n. For appropriately normalized density kernels this recovers a Parzen-type score, but does not by itself determine a useful acceptance threshold. The source explicitly changes the offset in its Parzen comparison. For linear-kernel observations 1 and 2 at nu=1, offsets 3 and 4 share the exact optimal objective -9/8 but respectively accept one and zero training points. For smaller nu, nonuniform learned weights generally differ from an ordinary unweighted kernel-density estimate; an arbitrary kernel score is not a normalized probability density. Locator: Section 3, PDF p6 / printed p1448; Figure 2 caption, PDF p14 / printed p1456; curator endpoint calculation in research/discovery/ocsvm-boundaries.py

### generalization scope

evidence: supported. Targets: AIMech:OneClassSupportVectorMachine.

Supported within the declared mathematical and source scope.

The paper gives a high-probability bound for rejection outside an enlarged region using offset rho-gamma with gamma&gt;0, under iid sampling, a distribution without discrete components and the stated function-class/complexity conditions. It does not set the original region’s future rejection probability exactly to nu or establish unconditional complete-support recovery. The authors describe the bound as loose and unsuitable for direct parameter selection. Their asymptotic nu-equality discussion depends on additional distribution, kernel and vanishing-boundary-fraction arguments; it is not asserted here as a general guarantee for every kernel. Locator: Section 5, PDF pp11-13 / printed pp1453-1455, Proposition 3 and Theorem 1; Appendix B, PDF pp23-26 / printed pp1465-1468

### evaluation boundaries

evidence: supported. Targets: AIMech:OneClassSupportVectorMachine.

Supported within the declared mathematical and source scope.

The experiments use selected two-dimensional examples and USPS digits with specified Gaussian width and nu. The digit-zero experiment trains on training-set zeros and tests against zeros and other digits. A separate outlier experiment fits the USPS test set itself after adding ten class-label coordinates, so that study is neither a held-out test nor an unlabeled-pixel-only experiment. Reported SMO scaling uses small selected subsets and is explicitly described as noisy. These studies do not establish universal accuracy, kernel choice, robustness or computational scaling. No numerical performance advantage is curated. Locator: Section 6, PDF pp13-18 / printed pp1455-1460, Figures 1-6 and Table 1; discussion PDF pp19-21 / printed pp1461-1463

### No interior coefficient and endpoint ambiguity

consistency: supported. Targets: AIMech:OneClassSupportVectorMachine.

The record does not assume that a free coefficient always exists.

KKT: alpha&gt;0 gives rho&gt;=g_i from active slack constraints; alpha&lt;C gives rho&lt;=g_i from zero slack. Their intersection gives the recorded interval. At nu1 allalpha=1/n are capped, leaving no upper bound. The exact linear example has primal objective -9/8 for rho3 andrho4 and meets the dual value, with different training acceptance. Strict convexity fixes w but not necessarily the offset or singular-Gram coefficient representation.

### Global kernel-diagonal condition

consistency: supported. Targets: AIMech:OneClassSupportVectorMachine.

Sphere equivalence is conditional and does not duplicate SVDD.

For constant diagonal kappa, the sphere dual is twice the hyperplane dual minus kappa under the same simplex/box, and radius²=kappa+&#124;&#124;w&#124;&#124;²-2rho gives the same prediction inequality when the query diagonal is also kappa. Restricting0&lt;nu&lt;1 avoids the endpoint radius/offset degeneracy. The linear two-point example has hyperplane objective(1+t)^2/2 minimized at t0, but sphere objective t²-t minimized at t1/2; query3 is accepted only by the hyperplane.

### Finite support counts and boundary mass

consistency: supported. Targets: AIMech:OneClassSupportVectorMachine.

The nu parameter supplies inequalities rather than exact calibration.

Positive coefficients sum to1 and each is at most1/(nu*n), giving the support-count lower bound. Strictly rejected points have capped coefficients, giving the upper count bound. Capped points may be on the boundary. For feature map(1,x), the balanced four-point example reaches the minimum convex-hull norm at(1,0), with allinterior coefficients and constant score1. Its zero rejection and fullsupport are a finite example; the record does not mislabel it an iid asymptotic disproof.

### Generalization and experimental provenance

consistency: supported. Targets: AIMech:OneClassSupportVectorMachine.

The theorem and experiments retain their actual scope.

Read the enlarged rho-gamma region, iid/nonatomic assumptions, slack and complexity terms, authors’ loose-bound warning, AppendixB proof sketches and references. No complete externalproofaudit is claimed. Figure2 changes the Parzen offset. The digit-zero held-out experiment differs from the separate2007-observation label-augmented in-sample USPS fit. Runtime plots are small/noisy selected cases; no universal performance result is curated.

### Complete record and discovery handoff

provenance: supported. Targets: AIMech:OneClassSupportVectorMachine.

Every selected field was read after canonical inspection.

Read ID,name,allaliases,kind,definition,identitynotes,definitioncitation,all8claimsandlocators,completeauthor/source/version/access/hashmetadata,exactAIOsnapshot,bothmappingrationales,limitations,DRAFTstatusandactualcurationtimes. Report mirror and append-only CREATE history agree. Three new source cohorts were deduplicated with ignored/hidden files included;452pendingcohortspluspartialwork remain.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:OneClassSupportVectorMachine. The original origin-relative hyperplane objective is distinct from general sphere fitting, component-labeling SVC and supervised nu methods. A conditional constant-diagonal equivalence is preserved without erasing these scopes.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T110312Z-one-class-support-vector-machine.json | supports | This record denotes the original origin-relative one-class hyperplane support estimator in Scholkopf, Platt, Shawe-Taylor, Smola and Williamson (2001). It does not denote supervised nu-SVC or nu-SVR, sphere-fitting SVDD, support-vector clustering with component assignment, or later negative-example feature extraction. Compared all442 pinned AIO IDs, labels and scoped synonyms with all519 preceding native IDs, names and aliases, with no normalized collision. Fixed-string whole-word searches in both checkouts included ignored and hidden files, expanded names, acronyms, DOI and paper identifiers. All11 distinct matched-text windows were read; the locations are prior discovery leads and neighboring method context. All125 semantic AIO rows and114 native identity rows exactly match the preceding read capture; the additional RAPID row and full record were read. Thirty complete contextual record readings were retained with matching hashes. Absence is bounded to the inspected pin and corpus. |
| mapping | sources/aio/aio.json; Ten declared annotated CLASS nodes and outgoing edges;30 contextual YAML readings. | supports | The AIO target describes the task of learning patterns from unlabeled observations, whereas this local record specifies one support-estimation algorithm. The relation captures that learning setting without equating an algorithm with a task or asserting a subclass edge. Users may supply a selected target class; the mathematical objective does not require negative training examples. BinaryClassification and Classification inherit supervised task scope and do not identify this objective. KernelLayer is a neural component, and generic Model/Network nodes do not identify the estimator. The origin-relative kernel hyperplane and norm/slack optimization are directly related to support-vector classification. The pinned AIO target specifically describes a supervised category-separating network, so it is not treated as an exact or broader identity for this one-class support estimator. The source explicitly derives the connection and its changed objective. Native SVDD has only a conditional constant-diagonal correspondence; KernelPCA optimizes variance directions and SVC additionally assigns connected components. |
| scholkopf2001 | https://alex.smola.org/papers/2001/SchPlaShaSmoetal01.pdf; Neural Computation13(7):1443-1471, July2001. Exact29-page author-hosted journal PDF, allpages visually read including figures, Table1, appendices and references. Printedpage=PDFpage+1442. Earlier1999 technical report and separately cited proof sources were not fully compared or audited. | supports | All29 final journal pages visually read, including formal method, figures,Table1,appendices and references; external proof dependencies were not independently audited. |
| exact-boundaries | research/discovery/ocsvm-boundaries.py | supports | Exact linear-kernel examples distinguish SVDD geometry and nu1 offset ambiguity; an analytic nonconstant-kernel example shows finite nu inequalities need not be equalities. No asymptotic disproof, historical implementation run or benchmark is asserted. |

## Limits And Additional Notes

- Adversarial author self-review only; the maintained record remains DRAFT.
- All29 journal PDF pages were visually read, including6 figures,Table1, appendices and references. The earlier1999 technical report and external proof sources were not independently audited.
- The author PDF download initially failed in urllib but succeeded with curl; exact bytes and hash are retained. Alternative source failures and missing screenshot payloads are recorded without claiming absence or visual reading.
- Exact finite arithmetic verifies specific examples, not a historical implementation, benchmark or asymptotic counterexample. No model training or paid service was used.
- Three new primary source cohorts remain pending full-method reading. No numerical performance advantage or unqualified asymptotic nu-equality theorem is curated.
- There are520 native DRAFT records and442 unchanged generated AIO records.452 pending cohorts plus partly addressed work prevent a saturation claim.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T110755Z-one-class-svm-review
kind: record
repository: CultureBotAI/AIMech
title: Scientific self-review of the original one-class support vector machine
started_at: '2026-10-12T11:03:38Z'
finished_at: '2026-10-12T11:07:55Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent read all29 journal pages, challenged geometry,
    threshold and nu claims with exact arithmetic, compared AIO/native neighbors and
    reread every record field after canonical capture. This is adversarial author
    self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the source-scoped one-class estimator as a distinct native algorithm.
  No actionable finding remains in the selected record; kernel, offset, count and
  evidence limits are explicit.
source:
  git_revision: 466d27ac2a4353d49c8ad16ed5912c8f30e466f8
  state: working_tree
  inputs:
  - path: data/aio/BinaryClassification.yaml
    sha256: 4c710e70fe7e71227f0c6aa55162a3683f04ebbe6f5a4601bd4c0398329f1481
    role: context
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/DataPreparation.yaml
    sha256: 99aebfc324b628969407ddc7591312e992db1469e7ef8fb3ad28e4b62d3bb359
    role: context
  - path: data/aio/KernelLayer.yaml
    sha256: 0723e7f15d57807a1f922cd87b878593fb167757c7429dd06e99bde723290d43
    role: context
  - path: data/aio/LeastsquaresAnalysis.yaml
    sha256: 666926bd17035ea825f0f521620b9c5538ff2a8695e7d37f96ab3b0cc8aa1d3c
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/Network.yaml
    sha256: ec24eb397241fe903137b2d8c8f4081d0f9d246c296c247864f199e160a3ee30
    role: context
  - path: data/aio/Preprocessing.yaml
    sha256: 2c4a30f4f829a757be1feabf78d15780eedf93681a62eede3e76b2304f21bb7a
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/RidgeRegression.yaml
    sha256: 7ee3be4552041e1ee2194a78eb0cbefe25283907027a6680395973dbf98636bb
    role: context
  - path: data/aio/SelectionAndSamplingBias.yaml
    sha256: 72d8ef34949942ddee1fe60d645806a2117b95207f681de923297b64f78cc477
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/SupportVectorMachine.yaml
    sha256: 0cc2faa913fdafdc539a7d04d08d26c0963f77ad3ca26b833b29ed3ed313e4e0
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/BallVectorMachine.yaml
    sha256: 08e08546d0f28411efad82a84b2f6a56362f7284804bad569820d42bca548737
    role: context
  - path: data/curated/CondensedNearestNeighborDataDomainDescription.yaml
    sha256: 7a9a70a3bda10bd66dec59c5560471f68af26c9603f707c878c48f69a427a02a
    role: context
  - path: data/curated/CondensedPrototypeBasedDomainDescription.yaml
    sha256: 97c4c87b9023f63170576613b537eb81964d7365ae1600105ac5f911ecca43a8
    role: context
  - path: data/curated/CoreSetSupportVectorDataDescription.yaml
    sha256: f02d6459178882f29b748532bf817d1477721d2f7402fbfe91305ac2eb6076f2
    role: context
  - path: data/curated/CoreVectorMachine.yaml
    sha256: ac41d81c889250fb49a7593cc9dfccbf1fc56f979c4584eb60ea2c5d420619bf
    role: context
  - path: data/curated/CoreVectorRegression.yaml
    sha256: 35ed0d44bad43789851e83ce7bea8ca0303030002d474861dabe8fe276054e97
    role: context
  - path: data/curated/FastCondensedPrototypeBasedDomainDescription.yaml
    sha256: af96a4d9b08517140732b60a7e9e7c2883ea2eb7e008f718fceeafeb42f32cdc
    role: context
  - path: data/curated/GeneralizedCoreVectorMachine.yaml
    sha256: 44551b4922a2d7454570f5862448de86ae266fcdd2433e5fea681c6df6549091
    role: context
  - path: data/curated/KernelPCA.yaml
    sha256: a93227a6b2d6b2b89b679b8f7f9ddd5054741d1c11f9510490d82a3e691a1cab
    role: context
  - path: data/curated/L2LossSupportVectorDataDescription.yaml
    sha256: 42d0072e69d90f8f70b87bec4393787ce23f2b9e494d1efa74aaad270cec1893
    role: context
  - path: data/curated/OneClassSupportVectorMachine.yaml
    sha256: c54e30f216ce4205c1d9e0bd84e3cb6dd412e90ee078df8366593c746018765a
    role: target
  - path: data/curated/RapidSupportVectorDataDescriptionSampling.yaml
    sha256: 681844c15688dbebe254c77723d6913d07003ea34de60c31b18cef59fd181942
    role: context
  - path: data/curated/SemidefiniteMaximumMarginClustering.yaml
    sha256: 9cfe6597d65d6a9dae4040f56bade8cba946a4b09c82c8f0b5adbec8b66a59dc
    role: context
  - path: data/curated/SupportVectorClustering.yaml
    sha256: f15f79f69443b23faa8247bb4fb67d86caeb2a80a86ae0e8c97dd247e152ad3a
    role: context
  - path: data/curated/SupportVectorDataDescription.yaml
    sha256: 45e181fa0ce8eeeda5c10e6e3fbce658b05bfd650e7c9c6bf77501d7fa315b7b
    role: context
  - path: research/discovery/20261012T110312Z-one-class-support-vector-machine.json
    sha256: 3386581e6592318bde7e3349ea4b2d290dcf28c5816f6d51b02f111fcca6ba77
    role: context
  - path: research/discovery/ocsvm-boundaries.py
    sha256: c8c0d49e317e997a881cd9f7dd05d2e323d52f38170a3593e0a90e52996cea57
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
- target_id: AIMech:OneClassSupportVectorMachine
  path: data/curated/OneClassSupportVectorMachine.yaml
  label: One-class support vector machine
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OneClassSupportVectorMachine.yaml
    role: maintained
scope:
  description: Every field of one maintained one-class support vector machine record.
  selection: Exact maintained ID AIMech:OneClassSupportVectorMachine.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:OneClassSupportVectorMachine
  exclusions:
  - target: Contextual AIO/native records
    reason: Identity/mapping context only, not renewed scientific approval.
  - target: Historical implementation and benchmarks
    reason: No solver implementation or benchmark was executed.
  - target: External proof dependencies and earlier manuscript
    reason: Journal read in full; external proofs and1999versionnotfullyaudited.
  - target: Discovery frontier
    reason: 452pendingcohortsandpartlyaddressedworkremain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 107.20s (0:01:47)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 520 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 167 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 163,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:OneClassSupportVectorMachine
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
  - AIMech:OneClassSupportVectorMachine
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
  - AIMech:OneClassSupportVectorMachine
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: exact-boundaries
  name: Exact OCSVM boundary examples
  command: python3 research/discovery/ocsvm-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  exit_code: 0
  expected_exit_code: 0
  summary: '{"scope": "Exact rational mathematical examples; no historical solver
    or benchmark was run.", "nonconstant_diagonal": {"kernel": "k(x,y)=xy", "points":
    [1, 2], "nu": "1/4", "C": "2", "ocsvm": {"alpha": ["1", "0"], "w": "1", "rho":
    "1", "acceptance": "x>=1"}, "svdd": {"alpha": ["1/2", "1/2"], "center": "3/2",
    "radius_squared": "1/4", "acceptance": "1<=x<=2"}, "interpretation": "Equal sample
    and penalty do not make the methods identical for arbitrary kernels."}, "nu_one":
    {"scores": ["3/2", "3"], "thresholds": [3, 4], "objectives": ["-9/8", "-9/8"],
    "accepted_training_points": [[false, true], [false, false]], "interpretation":
    "Uniform expansion weights do not uniquely determine the acceptance threshold."},
    "finite_boundary_mass": {"kernel": "k(x,y)=1+xy, feature map (1,x)", "points":
    ["-3/4", "-1/4", "1/4", "3/4"], "nu": "1/2", "rho": "1", "strict_training_outlier_fraction":
    "0", "support_vector_fraction": "1", "interpretation": "Finite nu bounds need
    not be equalities, and analyticity alone does not force a nonconstant fitted score.
    This finite example is not an iid asymptotic counterexample."}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T110312Z-one-class-support-vector-machine.json
  accessed_at: '2026-10-12T11:03:38Z'
  support: supports
  summary: This record denotes the original origin-relative one-class hyperplane support
    estimator in Scholkopf, Platt, Shawe-Taylor, Smola and Williamson (2001). It does
    not denote supervised nu-SVC or nu-SVR, sphere-fitting SVDD, support-vector clustering
    with component assignment, or later negative-example feature extraction. Compared
    all442 pinned AIO IDs, labels and scoped synonyms with all519 preceding native
    IDs, names and aliases, with no normalized collision. Fixed-string whole-word
    searches in both checkouts included ignored and hidden files, expanded names,
    acronyms, DOI and paper identifiers. All11 distinct matched-text windows were
    read; the locations are prior discovery leads and neighboring method context.
    All125 semantic AIO rows and114 native identity rows exactly match the preceding
    read capture; the additional RAPID row and full record were read. Thirty complete
    contextual record readings were retained with matching hashes. Absence is bounded
    to the inspected pin and corpus.
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Ten declared annotated CLASS nodes and outgoing edges;30 contextual YAML
    readings.
  accessed_at: '2026-10-12T11:03:38Z'
  support: supports
  summary: The AIO target describes the task of learning patterns from unlabeled observations,
    whereas this local record specifies one support-estimation algorithm. The relation
    captures that learning setting without equating an algorithm with a task or asserting
    a subclass edge. Users may supply a selected target class; the mathematical objective
    does not require negative training examples. BinaryClassification and Classification
    inherit supervised task scope and do not identify this objective. KernelLayer
    is a neural component, and generic Model/Network nodes do not identify the estimator.
    The origin-relative kernel hyperplane and norm/slack optimization are directly
    related to support-vector classification. The pinned AIO target specifically describes
    a supervised category-separating network, so it is not treated as an exact or
    broader identity for this one-class support estimator. The source explicitly derives
    the connection and its changed objective. Native SVDD has only a conditional constant-diagonal
    correspondence; KernelPCA optimizes variance directions and SVC additionally assigns
    connected components.
- evidence_id: scholkopf2001
  kind: primary_source
  reference: https://alex.smola.org/papers/2001/SchPlaShaSmoetal01.pdf
  locator: Neural Computation13(7):1443-1471, July2001. Exact29-page author-hosted
    journal PDF, allpages visually read including figures, Table1, appendices and
    references. Printedpage=PDFpage+1442. Earlier1999 technical report and separately
    cited proof sources were not fully compared or audited.
  accessed_at: '2026-10-12T10:52:38Z'
  snapshot_sha256: 65e412e8d167a675bab0df27ea3516ab942960b23c01bc369df372dc9b126aaf
  support: supports
  summary: All29 final journal pages visually read, including formal method, figures,Table1,appendices
    and references; external proof dependencies were not independently audited.
- evidence_id: exact-boundaries
  kind: record_content
  reference: research/discovery/ocsvm-boundaries.py
  accessed_at: '2026-10-12T11:03:38Z'
  snapshot_sha256: c8c0d49e317e997a881cd9f7dd05d2e323d52f38170a3593e0a90e52996cea57
  support: supports
  summary: Exact linear-kernel examples distinguish SVDD geometry and nu1 offset ambiguity;
    an analytic nonconstant-kernel example shows finite nu inequalities need not be
    equalities. No asymptotic disproof, historical implementation run or benchmark
    is asserted.
assessments:
- assessment_id: identity-definition
  area: identity
  topic: Distinct one-class hyperplane estimator
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - identity
  - scholkopf2001
  summary: Retain a separate algorithm identity.
  details: A support-estimation algorithm that optimizes a kernel feature-space score
    relative to the origin using a norm penalty, a learned offset and linearly penalized
    shortfalls controlled by nu, then accepts a query when its score meets the learned
    threshold. This record denotes the original origin-relative one-class hyperplane
    support estimator in Scholkopf, Platt, Shawe-Taylor, Smola and Williamson (2001).
    It does not denote supervised nu-SVC or nu-SVR, sphere-fitting SVDD, support-vector
    clustering with component assignment, or later negative-example feature extraction.
    Compared all442 pinned AIO IDs, labels and scoped synonyms with all519 preceding
    native IDs, names and aliases, with no normalized collision. Fixed-string whole-word
    searches in both checkouts included ignored and hidden files, expanded names,
    acronyms, DOI and paper identifiers. All11 distinct matched-text windows were
    read; the locations are prior discovery leads and neighboring method context.
    All125 semantic AIO rows and114 native identity rows exactly match the preceding
    read capture; the additional RAPID row and full record were read. Thirty complete
    contextual record readings were retained with matching hashes. Absence is bounded
    to the inspected pin and corpus.
- assessment_id: related-mappings
  area: grounding
  topic: Task and supervised-network relations
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - mapping
  - scholkopf2001
  summary: Both related mappings preserve the abstraction and supervision distinctions.
  details: The AIO target describes the task of learning patterns from unlabeled observations,
    whereas this local record specifies one support-estimation algorithm. The relation
    captures that learning setting without equating an algorithm with a task or asserting
    a subclass edge. Users may supply a selected target class; the mathematical objective
    does not require negative training examples. BinaryClassification and Classification
    inherit supervised task scope and do not identify this objective. KernelLayer
    is a neural component, and generic Model/Network nodes do not identify the estimator.
    The origin-relative kernel hyperplane and norm/slack optimization are directly
    related to support-vector classification. The pinned AIO target specifically describes
    a supervised category-separating network, so it is not treated as an exact or
    broader identity for this one-class support estimator. The source explicitly derives
    the connection and its changed objective. Native SVDD has only a conditional constant-diagonal
    correspondence; KernelPCA optimizes variance directions and SVC additionally assigns
    connected components.
- assessment_id: soft-origin-objective
  area: evidence
  topic: soft origin objective
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - scholkopf2001
  summary: Supported within the declared mathematical and source scope.
  details: 'For a nonempty sample of n observations, a positive-semidefinite kernel
    with feature map Phi, and 0<nu<=1, minimize (1/2)||w||^2 + sum_i xi_i/(nu*n) -
    rho subject to w.Phi(x_i)>=rho-xi_i and xi_i>=0. The offset rho is unrestricted.
    The method learns from the supplied observations without requiring a representative
    negative class. It does not minimize input-space Lebesgue volume, and a degenerate
    feature configuration need not yield a nonzero separating normal. Locator: Sections
    2-3, PDF pp3-5 / printed pp1445-1447, Equations 3.1-3.6'
- assessment_id: dual-score-and-threshold
  area: evidence
  topic: dual score and threshold
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - scholkopf2001
  - exact-boundaries
  summary: Supported within the declared mathematical and source scope.
  details: 'The dual minimizes (1/2)*alpha^T*K*alpha subject to sum_i alpha_i=1 and
    0<=alpha_i<=C, where C=1/(nu*n). The score is g(x)=sum_i alpha_i*k(x_i,x); accept
    g(x)>=rho, including equality. A coefficient strictly between zero and C fixes
    rho=g(x_i). Such a coefficient need not exist. KKT conditions instead bound rho
    below by max_{alpha_i>0} g(x_i) and above by min_{alpha_i<C} g(x_i); an empty
    upper-bound set gives no finite upper bound. Different optimal offsets can give
    different acceptance regions. The primal normal is fixed by strict convexity in
    w, while coefficients can be nonunique for a singular Gram matrix. Locator: Section
    3, PDF pp4-6 / printed pp1446-1448, Equations 3.4-3.12 and sign convention; KKT
    interval derived from these constraints; research/discovery/ocsvm-boundaries.py'
- assessment_id: finite-nu-bounds
  area: evidence
  topic: finite nu bounds
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - scholkopf2001
  - exact-boundaries
  summary: Supported within the declared mathematical and source scope.
  details: 'At an exact optimum, nu bounds the fraction of strictly rejected training
    observations from above and the fraction of positive expansion coefficients from
    below. The paper states these properties under rho!=0. Neither bound requires
    equality in a finite sample; a coefficient at its upper bound can lie on the accepted
    boundary. A support-vector count is not a calibrated future rejection probability
    or a guaranteed sparse fraction. With the analytic nonconstant kernel k(x,y)=1+x*y
    and four balanced points -3/4,-1/4,1/4,3/4, nu=1/2 admits optimal weights 1/4,
    rho=1 and a constant score: all four points are support vectors and none is rejected.
    This is a finite illustration, not an iid asymptotic counterexample. Locator:
    Section 5 Proposition 3, PDF p11 / printed p1453; Appendix B proof sketch, PDF
    p23 / printed p1465; curator calculation in research/discovery/ocsvm-boundaries.py'
- assessment_id: sphere-correspondence
  area: evidence
  topic: sphere correspondence
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - scholkopf2001
  - exact-boundaries
  summary: Supported within the declared mathematical and source scope.
  details: 'For 0<nu<1, a kernel whose diagonal k(x,x) is constant over both training
    and query inputs makes the matched-penalty SVDD and hyperplane dual objectives
    differ only by scale and a constant. Compatible radius and offset choices then
    give the same acceptance rule. This restricted correspondence does not identify
    the algorithms for arbitrary kernels. For linear-kernel observations 1 and 2 with
    nu=1/4, the exact hyperplane rule accepts x>=1, while matched-penalty SVDD accepts
    only 1<=x<=2. Training-only diagonal equality also does not justify dropping the
    query diagonal. Locator: Section 3, PDF pp6-7 / printed pp1448-1449, Equations
    3.13-3.17 and following comparison; curator calculation in research/discovery/ocsvm-boundaries.py'
- assessment_id: pairwise-optimization
  area: evidence
  topic: pairwise optimization
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - scholkopf2001
  summary: Supported within the declared mathematical and source scope.
  details: 'The proposed SMO adaptation updates two coefficients while preserving
    their sum and the box constraints. For positive pair curvature k_ii+k_jj-2*k_ij,
    the unconstrained second-coefficient update adds (g_i-g_j)/(k_ii+k_jj-2*k_ij),
    then clips to the jointly feasible interval before recovering the first coefficient.
    Zero curvature cannot be handled by dividing that formula. The paper alternates
    full and non-bound KKT scans and refers to fallback selection rules; it also discusses
    tolerance adjustments and a modification for pathological convergence cases. This
    describes an optimization procedure, not a universal runtime or implementation-convergence
    guarantee. Locator: Section 4, PDF pp7-9 / printed pp1449-1451, Equations 4.1-4.8
    and termination discussion'
- assessment_id: density-and-endpoint
  area: evidence
  topic: density and endpoint
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - scholkopf2001
  - exact-boundaries
  summary: Supported within the declared mathematical and source scope.
  details: 'At nu=1 the constraints force every expansion coefficient to 1/n. For
    appropriately normalized density kernels this recovers a Parzen-type score, but
    does not by itself determine a useful acceptance threshold. The source explicitly
    changes the offset in its Parzen comparison. For linear-kernel observations 1
    and 2 at nu=1, offsets 3 and 4 share the exact optimal objective -9/8 but respectively
    accept one and zero training points. For smaller nu, nonuniform learned weights
    generally differ from an ordinary unweighted kernel-density estimate; an arbitrary
    kernel score is not a normalized probability density. Locator: Section 3, PDF
    p6 / printed p1448; Figure 2 caption, PDF p14 / printed p1456; curator endpoint
    calculation in research/discovery/ocsvm-boundaries.py'
- assessment_id: generalization-scope
  area: evidence
  topic: generalization scope
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - scholkopf2001
  summary: Supported within the declared mathematical and source scope.
  details: 'The paper gives a high-probability bound for rejection outside an enlarged
    region using offset rho-gamma with gamma>0, under iid sampling, a distribution
    without discrete components and the stated function-class/complexity conditions.
    It does not set the original region’s future rejection probability exactly to
    nu or establish unconditional complete-support recovery. The authors describe
    the bound as loose and unsuitable for direct parameter selection. Their asymptotic
    nu-equality discussion depends on additional distribution, kernel and vanishing-boundary-fraction
    arguments; it is not asserted here as a general guarantee for every kernel. Locator:
    Section 5, PDF pp11-13 / printed pp1453-1455, Proposition 3 and Theorem 1; Appendix
    B, PDF pp23-26 / printed pp1465-1468'
- assessment_id: evaluation-boundaries
  area: evidence
  topic: evaluation boundaries
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - scholkopf2001
  summary: Supported within the declared mathematical and source scope.
  details: 'The experiments use selected two-dimensional examples and USPS digits
    with specified Gaussian width and nu. The digit-zero experiment trains on training-set
    zeros and tests against zeros and other digits. A separate outlier experiment
    fits the USPS test set itself after adding ten class-label coordinates, so that
    study is neither a held-out test nor an unlabeled-pixel-only experiment. Reported
    SMO scaling uses small selected subsets and is explicitly described as noisy.
    These studies do not establish universal accuracy, kernel choice, robustness or
    computational scaling. No numerical performance advantage is curated. Locator:
    Section 6, PDF pp13-18 / printed pp1455-1460, Figures 1-6 and Table 1; discussion
    PDF pp19-21 / printed pp1461-1463'
- assessment_id: adversarial-threshold
  area: consistency
  topic: No interior coefficient and endpoint ambiguity
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - scholkopf2001
  - exact-boundaries
  summary: The record does not assume that a free coefficient always exists.
  details: 'KKT: alpha>0 gives rho>=g_i from active slack constraints; alpha<C gives
    rho<=g_i from zero slack. Their intersection gives the recorded interval. At nu1
    allalpha=1/n are capped, leaving no upper bound. The exact linear example has
    primal objective -9/8 for rho3 andrho4 and meets the dual value, with different
    training acceptance. Strict convexity fixes w but not necessarily the offset or
    singular-Gram coefficient representation.'
- assessment_id: adversarial-correspondence
  area: consistency
  topic: Global kernel-diagonal condition
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - scholkopf2001
  - exact-boundaries
  summary: Sphere equivalence is conditional and does not duplicate SVDD.
  details: For constant diagonal kappa, the sphere dual is twice the hyperplane dual
    minus kappa under the same simplex/box, and radius²=kappa+||w||²-2rho gives the
    same prediction inequality when the query diagonal is also kappa. Restricting0<nu<1
    avoids the endpoint radius/offset degeneracy. The linear two-point example has
    hyperplane objective(1+t)^2/2 minimized at t0, but sphere objective t²-t minimized
    at t1/2; query3 is accepted only by the hyperplane.
- assessment_id: adversarial-counts
  area: consistency
  topic: Finite support counts and boundary mass
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - scholkopf2001
  - exact-boundaries
  summary: The nu parameter supplies inequalities rather than exact calibration.
  details: Positive coefficients sum to1 and each is at most1/(nu*n), giving the support-count
    lower bound. Strictly rejected points have capped coefficients, giving the upper
    count bound. Capped points may be on the boundary. For feature map(1,x), the balanced
    four-point example reaches the minimum convex-hull norm at(1,0), with allinterior
    coefficients and constant score1. Its zero rejection and fullsupport are a finite
    example; the record does not mislabel it an iid asymptotic disproof.
- assessment_id: adversarial-theory-evaluation
  area: consistency
  topic: Generalization and experimental provenance
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - scholkopf2001
  summary: The theorem and experiments retain their actual scope.
  details: Read the enlarged rho-gamma region, iid/nonatomic assumptions, slack and
    complexity terms, authors’ loose-bound warning, AppendixB proof sketches and references.
    No complete externalproofaudit is claimed. Figure2 changes the Parzen offset.
    The digit-zero held-out experiment differs from the separate2007-observation label-augmented
    in-sample USPS fit. Runtime plots are small/noisy selected cases; no universal
    performance result is curated.
- assessment_id: all-fields
  area: provenance
  topic: Complete record and discovery handoff
  outcome: supported
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - identity
  - mapping
  - scholkopf2001
  - exact-boundaries
  summary: Every selected field was read after canonical inspection.
  details: Read ID,name,allaliases,kind,definition,identitynotes,definitioncitation,all8claimsandlocators,completeauthor/source/version/access/hashmetadata,exactAIOsnapshot,bothmappingrationales,limitations,DRAFTstatusandactualcurationtimes.
    Report mirror and append-only CREATE history agree. Three new source cohorts were
    deduplicated with ignored/hidden files included;452pendingcohortspluspartialwork
    remain.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:OneClassSupportVectorMachine
  evidence_ids:
  - identity
  - mapping
  - scholkopf2001
  - exact-boundaries
  rationale: The original origin-relative hyperplane objective is distinct from general
    sphere fitting, component-labeling SVC and supervised nu methods. A conditional
    constant-diagonal equivalence is preserved without erasing these scopes.
limitations:
- Adversarial author self-review only; the maintained record remains DRAFT.
- All29 journal PDF pages were visually read, including6 figures,Table1, appendices
  and references. The earlier1999 technical report and external proof sources were
  not independently audited.
- The author PDF download initially failed in urllib but succeeded with curl; exact
  bytes and hash are retained. Alternative source failures and missing screenshot
  payloads are recorded without claiming absence or visual reading.
- Exact finite arithmetic verifies specific examples, not a historical implementation,
  benchmark or asymptotic counterexample. No model training or paid service was used.
- Three new primary source cohorts remain pending full-method reading. No numerical
  performance advantage or unqualified asymptotic nu-equality theorem is curated.
- There are520 native DRAFT records and442 unchanged generated AIO records.452 pending
  cohorts plus partly addressed work prevent a saturation claim.
related_reviews: []
links: []
tags:
- native-concepts
- one-class-learning
- self-review
- discovery-ongoing
```
