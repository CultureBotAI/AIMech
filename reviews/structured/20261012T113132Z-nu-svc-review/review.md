# Scientific author self-review of Nu support vector classification: final

- Review: 20261012T113132Z-nu-svc-review
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T11:31:02Z
- Finished UTC: 2026-10-12T11:31:32Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the source-scoped algorithm. No actionable finding remains in the selected final record; mathematical, evaluation and access limits are explicit.

## Scope And Provenance

Every field of one maintained supervised nu-SVM record.

Selection: Exact maintained ID AIMech:NuSupportVectorClassification
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 90c25fb04337c7e24dd5408db7707d196026ed8f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:NuSupportVectorClassification | data/curated/NuSupportVectorClassification.yaml | maintained | Nu support vector classification |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:NuSupportVectorClassification | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 114.96s (0:01:54)<br>Checked 442 record(s); 0 failed.<br>Checked 522 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 169 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 165,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:NuSupportVectorClassification | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:NuSupportVectorClassification | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:NuSupportVectorClassification | Exited0 without output. |
| uv run --locked aimech validate-history --base HEAD | passed | True | AIMech:NuSupportVectorClassification | Checked 170 history record(s); 0 error(s).<br> |
| Exact finite nu-SVM certificates | passed | True | AIMech:NuSupportVectorClassification | {"svr_positive_width": {"primal": "1/2", "dual": "1/2", "w": "0", "b": "0", "epsilon": "1", "error_fraction": "0", "support_fraction": "1", "free_coefficients": 4}, "svr_zero_width": {"primal": "0", "dual": "0", "w": "0", "b": "0", "epsilon": "0", "error_fraction": "0", "support_fraction": "0", "free_coefficients": 0}, "svr_endpoint_ambiguity": [{"primal": "1", "dual": "1", "w": "0", "b": "0", "epsilon": "0", "error_fraction": "1", "support_fraction": "1", "free_coefficients": 0}, {"primal": "1", "dual": "1", "w": "0", "b": "1/2", "epsilon": "0", "error_fraction": "1", "support_fraction": "1", "free_coefficients": 0}, {"primal": "1", "dual": "1", "w": "0", "b": "0", "epsilon": "1", "error_fraction": "0", "support_fraction": "1", "free_coefficients": 0}], "svc_positive_margin": {"primal": "-1/8", "dual": "-1/8", "w": "1/2", "b": "0", "rho": "1/2", "scores": ["-1/2", "-1/2", "1/2", "1/2"], "margin_error_fraction": "0", "support_fraction": "1", "free_coefficients": 4}, "svc_zero_margin": {"primal": "0", "dual": "0", "w": "0", "b": "0", "rho": "0", "scores": ["0", "0", "0", "0"], "margin_error_fraction": "0", "support_fraction": "1", "free_coefficients": 4}, "svc_endpoint_ambiguity": [{"primal": "-1/2", "dual": "-1/2", "w": "1", "b": "0", "rho": "1", "scores": ["-1", "1"], "margin_error_fraction": "0", "support_fraction": "1", "free_coefficients": 0}, {"primal": "-1/2", "dual": "-1/2", "w": "1", "b": "3", "rho": "4", "scores": ["2", "4"], "margin_error_fraction": "1/2", "support_fraction": "1", "free_coefficients": 0}], "svc_infeasible_nu": {"n": 4, "positive_count": 3, "negative_count": 1, "maximum_dual_mass": "1/2", "chosen_nu": "3/4", "primal_coefficient_of_t": "-1/4"}, "parametric_source_discrepancy": "For zeta=1, the positive-width SVR certificate has support fraction1 at nu1/2, contradicting the printed Proposition4(ii) upper-bound wording. This contextual variant remains pending assessment."} |

## Scientific And Domain Assessments

### Original supervised optimization identity

identity: supported. Targets: AIMech:NuSupportVectorClassification.

Retain the source-scoped algorithm identity.

A supervised binary-classification algorithm that jointly fits a regularized kernel hyperplane and a nonnegative margin level, using nu to reward that level relative to linearly penalized margin shortfalls. The original binary nu-SVC formulation in Scholkopf, Smola, Williamson and Bartlett (2000) is the selected identity. It differs from a particular decomposition solver, multiclass reduction, nu-SVR and the one-class estimator; source-specific equivalence to C-SVC requires fitted positive rho and parameter conversion. Compared all442 pinned AIO IDs, labels and scoped synonyms against all520 preceding native IDs, names and aliases, without a normalized collision. Full-text fixed-string whole-word searches in both checkouts included ignored and hidden files, expanded labels, acronyms, DOI and paper identifiers. Read all25 distinct matching text windows across88 locations: these are the existing one-class record context, its review/renderings and the preceding discovery lead, not supervised nu records. All125 semantic AIO rows and115 prior native name/definition rows match the previous reading; the additional one-class row and complete record were read. Thirty-one contextual full-record readings are retained with matching hashes. Absence is bounded to this snapshot and corpus.

### Task and network abstraction

grounding: supported. Targets: AIMech:NuSupportVectorClassification.

Related mappings preserve the algorithm/task/network distinctions.

AIO BinaryClassification identifies the supervised two-group task, while this native record specifies a particular margin-based fitting algorithm. A related match preserves this abstraction difference. Classification and SupervisedLearning are broader task context, not exact identities for the nu objective. The source derives this supervised kernel optimization from support-vector methods, but the pinned AIO target describes a network with input, hidden and output parts. This native identity is an optimization algorithm, so the network abstraction is related rather than an asserted exact or broader class. KernelLayer names a component, and generic Network or TrainingStrategy also does not identify the objective. Twelve annotated AIO CLASS nodes and their outgoing edges were inspected.

### learned margin objective

evidence: supported. Targets: AIMech:NuSupportVectorClassification.

Supported within the stated source and mathematical scope.

For n observations with both binary labels y_i in{-1,+1} represented and a positive-semidefinite kernel, minimize (1/2)&#124;&#124;w&#124;&#124;^2-nu*rho+sum_i xi_i/n, subject to y_i*(w.Phi(x_i)+b)&gt;=rho-xi_i, xi_i&gt;=0 and rho&gt;=0. A positive feasible nu is at most2*min(n_positive,n_negative)/n, as follows directly from the balanced dual masses and coefficient caps. Values beyond this class-balance limit make the stated dual infeasible and primal unbounded. For three positive and one negative label, nu=3/4 exceeds the limit1/2; w=0,b=rho=t and negative slack2t give objective -t/4. Locator: Section 7, PDF pp17-19 / printed pp1223-1225, Equations 7.3-7.12; feasibility implication and exact example in research/discovery/nu-svm-boundaries.py

### dual and decision

evidence: supported. Targets: AIMech:NuSupportVectorClassification.

Supported within the stated source and mathematical scope.

The dual minimizes (1/2)*alpha^T*Y*K*Y*alpha, with0&lt;=alpha_i&lt;=1/n, sum_i alpha_i*y_i=0 and sum_i alpha_i&gt;=nu. The score is g(x)=sum_i alpha_i*y_i*k(x_i,x)+b and the classifier takes its sign. The source does not specify how an exactly zero score is assigned to one binary label. When free coefficients exist in both classes, KKT equalities give g(x_positive)=rho and g(x_negative)=-rho and permit recovery of b and rho. Such free coefficients need not exist; general recovery must respect the remaining KKT inequalities. Locator: Section 7, PDF pp18-19 / printed pp1224-1225, Equations 7.7-7.15

### margin error counts

evidence: supported. Targets: AIMech:NuSupportVectorClassification.

Supported within the stated source and mathematical scope.

For an exact optimum with rho&gt;0, sum_i alpha_i=nu. Thus nu bounds the fraction of strict margin errors y_i*g(x_i)&lt;rho from above and the positive-coefficient fraction from below. A margin error can still be correctly classified; it is not the same event as misclassification. Finite counts need not equal nu, and capped coefficients can occur on the margin. Four linear-kernel inputs -1,-1,1,1 with matching labels and nu=1/2 admit alpha_i=1/8,w=1/2,b=0,rho=1/2: all points are support vectors and none is a strict margin error. The source states the finite result under an analytic-kernel assumption; its additional asymptotic distribution and boundary-mass arguments are not promoted to unconditional calibration. Locator: Section 7 Proposition 5, PDF pp20-21 / printed pp1226-1227; exact finite certificate in research/discovery/nu-svm-boundaries.py

### c svc correspondence

evidence: supported. Targets: AIMech:NuSupportVectorClassification.

Supported within the stated source and mathematical scope.

If the fitted rho is positive, dividing w,b and slacks by rho yields a C-SVC optimum with C=1/rho in the paper’s C/n slack-penalty convention, preserving the sign decision. The numerical conversion differs when software uses C times the unaveraged slack sum. A global positive multiplier on the nu-SVC loss terms scales the solution without changing its boundary, explaining removal of that separate C parameter. This does not remove kernel selection or make arbitrary C and nu settings equivalent, and the conversion cannot divide by rho=0. Locator: Section 7, PDF p19 / printed p1225, homogeneity discussion; Proposition 6, PDF p21 / printed p1227

### degenerate and nonunique offsets

evidence: supported. Targets: AIMech:NuSupportVectorClassification.

Supported within the stated source and mathematical scope.

Feasibility does not guarantee positive rho or a useful binary separator. Balanced opposite labels at identical zero inputs admit w=b=rho=0. Even at rho&gt;0, b and rho can be nonunique when no coefficient is free: for linear-kernel inputs -1 and1 with matching labels and nu=1, both coefficients are1/2 and w=1, while (b,rho)=(0,1) and(3,4) attain the same objective -1/2 and classify the first training point differently. Strict convexity fixes the optimal normal w, not necessarily the intercept, margin variable or singular-Gram coefficient representation. Locator: Section 7, PDF pp18-21 / printed pp1224-1227, primal/dual constraints, free-coefficient formulas and positive-rho condition; exact certificates in research/discovery/nu-svm-boundaries.py

### generalization and robustness limits

evidence: supported. Targets: AIMech:NuSupportVectorClassification.

Supported within the stated source and mathematical scope.

The generalization analysis adds sample-size, confidence, margin and function-class complexity terms to empirical margin error; test risk is not bounded by nu alone. Its displayed normalized radial-kernel bound omits the intercept b, and the authors explicitly note that treating b requires a modification. Their resistance statement is conditional on a representation using free support vectors and local movements in feature space parallel to w; it is not arbitrary input-space or label-noise robustness. External proof dependencies were not independently audited. Locator: Section 7 Propositions 7-10, PDF pp21-24 / printed pp1227-1230, including the paragraph following Proposition 10

### classification evaluation scope

evidence: supported. Targets: AIMech:NuSupportVectorClassification.

Supported within the stated source and mathematical scope.

The classification study shows a two-dimensional circles-versus-disks example with a Gaussian kernel and nu values from0.1 to0.8, reporting support-vector and margin-error fractions plus geometric margins. The paper leaves real-world nu-SVC evaluation and efficient chunking methods to future work. It supplies no universal accuracy or runtime advantage over C-SVC, and later decomposition solvers are not identified with this original optimization formulation. Locator: Section 8.2 and Table 4/Figure 11, PDF pp32 and35 / printed pp1238 and1241; Section 9, PDF p36 / printed p1242

### Class balance and bounded optimization

consistency: supported. Targets: AIMech:NuSupportVectorClassification.

The feasible range follows from the displayed dual.

Balanced class coefficient sums are equal and at mostmin(n_positive,n_negative)/n each. Thus positive feasible nu cannot exceed twice that value. Above it, choose w0 and b=rho toward the majority class: average slack grows as2*n_minority*rho/n, while the reward is-nu*rho, proving unboundedness. The exact3:1 example verifies this coefficient. This is an explicitly labeled implication of the primary constraints, not an unseen theorem attribution.

### Positive margin, scaling and endpoint ambiguity

consistency: supported. Targets: AIMech:NuSupportVectorClassification.

Positive rho and free-coefficient assumptions are not dropped.

Rho complementarity forces totalalpha=nu whenrho&gt;0; capped strictmarginerrors and positive coefficient counts give the inequalities. The four-point certificate has no strict errors and full support. Zero features with conflicting labels admitrho0, preventing division by it. Atnu1 two capped coefficients givew1 while b0/rho1 andb3/rho4 have equal exact objectives and different predictions. Dividing the fixed-rho primal by rho² yields C=1/rho under C/n normalization; a different software convention changes that numeric value.

### Intercept and experimental scope

evidence: supported. Targets: AIMech:NuSupportVectorClassification.

The bounds and evaluations retain their stated limits.

Read the missing-b note following Proposition10, conditional feature-space resistance statement and circles/disks toy experiment. No bound risk&lt;=nu, unconditional robustness or real-world runtime advantage is curated. External proofs and later decomposition solvers are excluded from approval.

### Complete record and research handoff

provenance: supported. Targets: AIMech:NuSupportVectorClassification.

Every selected field was read after canonical capture.

Read stableID,name,allaliases,kind,definition,identity notes,definition citation,all7claims and locators,full primary source authors/version/access/hash,exactAIOpin,both mapping rationales,limitations,DRAFTstatus and actual curation provenance. The mirrored report and append-only history were checked.453pendingcohortsplus43partlyaddressedcohortsremain; no saturation is claimed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:NuSupportVectorClassification. The selected supervised formulation has a distinct target and objective from the other nu variant, one-class estimation and sphere fitting. Conditional parameter conversion does not equate arbitrary fitting settings or identify a solver implementation.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T111940Z-supervised-nu-support-vector-methods.json | supports | Compared all442 pinned AIO IDs, labels and scoped synonyms against all520 preceding native IDs, names and aliases, without a normalized collision. Full-text fixed-string whole-word searches in both checkouts included ignored and hidden files, expanded labels, acronyms, DOI and paper identifiers. Read all25 distinct matching text windows across88 locations: these are the existing one-class record context, its review/renderings and the preceding discovery lead, not supervised nu records. All125 semantic AIO rows and115 prior native name/definition rows match the previous reading; the additional one-class row and complete record were read. Thirty-one contextual full-record readings are retained with matching hashes. Absence is bounded to this snapshot and corpus. |
| mapping | sources/aio/aio.json; Twelve declared annotated CLASS nodes with outgoing edges;31 contextual full-record readings retained by hash. | supports | AIO RegressionAnalysis identifies a supervised estimation task, while this native record specifies one fitting algorithm for real-valued responses. A related match captures its task without asserting algorithm/task equivalence. LinearRegression, RidgeRegression and LeastsquaresAnalysis do not identify the kernel, learned tube or piecewise-linear loss. The source derives this supervised kernel optimization from support-vector methods, but the pinned AIO target describes a network with input, hidden and output parts. This native identity is an optimization algorithm, so the network abstraction is related rather than an asserted exact or broader class. KernelLayer names a component, and generic Network or TrainingStrategy also does not identify the objective. Twelve annotated AIO CLASS nodes and their outgoing edges were inspected. AIO BinaryClassification identifies the supervised two-group task, while this native record specifies a particular margin-based fitting algorithm. A related match preserves this abstraction difference. Classification and SupervisedLearning are broader task context, not exact identities for the nu objective. The source derives this supervised kernel optimization from support-vector methods, but the pinned AIO target describes a network with input, hidden and output parts. This native identity is an optimization algorithm, so the network abstraction is related rather than an asserted exact or broader class. KernelLayer names a component, and generic Network or TrainingStrategy also does not identify the objective. Twelve annotated AIO CLASS nodes and their outgoing edges were inspected. |
| scholkopf2000 | https://www.stat.purdue.edu/~yuzhu/stat598m3/Papers/NewSVM.pdf; Neural Computation12(5):1207-1245, May2000. Exact39-page journal PDF hosted by Purdue; allpages visually read including11figures,4tables and references. Printedpage=PDFpage+1206. The1998 conference precursor and external proof dependencies were not fully audited. | supports | All39 original journal pages visually read, including11figures,4tables, formal objectives/proofs, discussion and references. External proof dependencies and later methods were not fully audited. |
| finite-certificates | research/discovery/nu-svm-boundaries.py | supports | Exact finite certificates show that positive-width/margin counts need not equalnu, zero-width/margin cases need qualifications, endpoint offsets and widths can be nonunique, and class imbalance limits feasible nu. A constant supplied basis also refutes the printed upper-support-bound wording in the pending parametric variant. These are curator calculations, not model training or a universal asymptotic disproof. |

## Limits And Additional Notes

- Adversarial author self-review only; native status remains DRAFT.
- All39 original journal pages were visually read, including11figures,4tables and references. The1998 precursor, external proofs and later decomposition sources were not fully audited.
- The public Purdue PDF was downloaded and rendered successfully. Some adjacent primary-page opens failed or returned browser checks, while their indexed abstracts were available; access failures are not evidence of absence. No access-control bypass was attempted.
- Exact rational examples verify feasibility, KKT conditions and primal/dual equality for selected finite cases. No historical solver, model training or benchmark was executed.
- The printed parametric-insensitivity support-bound discrepancy is preserved in research notes and the pending frontier. Neither that extension nor later learned/twin methods is silently certified by these two records.
- There are522 native DRAFT records and442 unchanged AIO records.453 pending cohorts and43 partly addressed cohorts, plus other unresolved scopes, prevent a saturation claim.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T113132Z-nu-svc-review
kind: record
repository: CultureBotAI/AIMech
title: 'Scientific author self-review of Nu support vector classification: final'
started_at: '2026-10-12T11:31:02Z'
finished_at: '2026-10-12T11:31:32Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent read all39 original journal pages, compared
    identity/mapping context, challenged the objectives and edge cases with exact
    KKT certificates, and reread every selected field after canonical capture. This
    is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the source-scoped algorithm. No actionable finding remains in the
  selected final record; mathematical, evaluation and access limits are explicit.
source:
  git_revision: 90c25fb04337c7e24dd5408db7707d196026ed8f
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
  - path: data/curated/NuSupportVectorClassification.yaml
    sha256: 9d301dc822b5fcc15b1a3b9b9a8636cce7e2fb79b67da09a0e204eb9b97c698d
    role: target
  - path: data/curated/NuSupportVectorRegression.yaml
    sha256: 77b999ae2c8c6d3dcc40dba5731728f3f612ff744063ac1847d9e4527380a989
    role: context
  - path: data/curated/OneClassSupportVectorMachine.yaml
    sha256: c54e30f216ce4205c1d9e0bd84e3cb6dd412e90ee078df8366593c746018765a
    role: context
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
  - path: research/discovery/20261012T111940Z-supervised-nu-support-vector-methods.json
    sha256: a5ff4f2880a8713d1b9d7f2b085d6ca478ce8ad12696659ec0b38b81beb71df6
    role: context
  - path: research/discovery/nu-svm-boundaries.py
    sha256: b65d75700f65680a298d5d30d3cf49de26ad81d82eae69fb89e77125a6bfa917
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
- target_id: AIMech:NuSupportVectorClassification
  path: data/curated/NuSupportVectorClassification.yaml
  label: Nu support vector classification
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NuSupportVectorClassification.yaml
    role: maintained
scope:
  description: Every field of one maintained supervised nu-SVM record.
  selection: Exact maintained ID AIMech:NuSupportVectorClassification
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:NuSupportVectorClassification
  exclusions:
  - target: Contextual records and other nu variant
    reason: Identity/mapping context only; separate record review required.
  - target: Historical solver and benchmarks
    reason: No optimizer, training or benchmark executed.
  - target: External proofs and later variants
    reason: Original source read in full; later full methods and external proof dependencies
      not audited.
  - target: Discovery frontier
    reason: 453pendingcohortsandpartlyaddressedworkremain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:NuSupportVectorClassification
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 114.96s (0:01:54)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 522 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 169 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 165,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:NuSupportVectorClassification
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
  - AIMech:NuSupportVectorClassification
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
  - AIMech:NuSupportVectorClassification
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: required-4
  name: uv run --locked aimech validate-history --base HEAD
  command: uv run --locked aimech validate-history --base HEAD
  status: passed
  required: true
  target_ids:
  - AIMech:NuSupportVectorClassification
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 170 history record(s); 0 error(s).

    '
- check_id: finite-certificates
  name: Exact finite nu-SVM certificates
  command: python3 research/discovery/nu-svm-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:NuSupportVectorClassification
  exit_code: 0
  expected_exit_code: 0
  summary: '{"svr_positive_width": {"primal": "1/2", "dual": "1/2", "w": "0", "b":
    "0", "epsilon": "1", "error_fraction": "0", "support_fraction": "1", "free_coefficients":
    4}, "svr_zero_width": {"primal": "0", "dual": "0", "w": "0", "b": "0", "epsilon":
    "0", "error_fraction": "0", "support_fraction": "0", "free_coefficients": 0},
    "svr_endpoint_ambiguity": [{"primal": "1", "dual": "1", "w": "0", "b": "0", "epsilon":
    "0", "error_fraction": "1", "support_fraction": "1", "free_coefficients": 0},
    {"primal": "1", "dual": "1", "w": "0", "b": "1/2", "epsilon": "0", "error_fraction":
    "1", "support_fraction": "1", "free_coefficients": 0}, {"primal": "1", "dual":
    "1", "w": "0", "b": "0", "epsilon": "1", "error_fraction": "0", "support_fraction":
    "1", "free_coefficients": 0}], "svc_positive_margin": {"primal": "-1/8", "dual":
    "-1/8", "w": "1/2", "b": "0", "rho": "1/2", "scores": ["-1/2", "-1/2", "1/2",
    "1/2"], "margin_error_fraction": "0", "support_fraction": "1", "free_coefficients":
    4}, "svc_zero_margin": {"primal": "0", "dual": "0", "w": "0", "b": "0", "rho":
    "0", "scores": ["0", "0", "0", "0"], "margin_error_fraction": "0", "support_fraction":
    "1", "free_coefficients": 4}, "svc_endpoint_ambiguity": [{"primal": "-1/2", "dual":
    "-1/2", "w": "1", "b": "0", "rho": "1", "scores": ["-1", "1"], "margin_error_fraction":
    "0", "support_fraction": "1", "free_coefficients": 0}, {"primal": "-1/2", "dual":
    "-1/2", "w": "1", "b": "3", "rho": "4", "scores": ["2", "4"], "margin_error_fraction":
    "1/2", "support_fraction": "1", "free_coefficients": 0}], "svc_infeasible_nu":
    {"n": 4, "positive_count": 3, "negative_count": 1, "maximum_dual_mass": "1/2",
    "chosen_nu": "3/4", "primal_coefficient_of_t": "-1/4"}, "parametric_source_discrepancy":
    "For zeta=1, the positive-width SVR certificate has support fraction1 at nu1/2,
    contradicting the printed Proposition4(ii) upper-bound wording. This contextual
    variant remains pending assessment."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T111940Z-supervised-nu-support-vector-methods.json
  accessed_at: '2026-10-12T11:31:02Z'
  support: supports
  summary: 'Compared all442 pinned AIO IDs, labels and scoped synonyms against all520
    preceding native IDs, names and aliases, without a normalized collision. Full-text
    fixed-string whole-word searches in both checkouts included ignored and hidden
    files, expanded labels, acronyms, DOI and paper identifiers. Read all25 distinct
    matching text windows across88 locations: these are the existing one-class record
    context, its review/renderings and the preceding discovery lead, not supervised
    nu records. All125 semantic AIO rows and115 prior native name/definition rows
    match the previous reading; the additional one-class row and complete record were
    read. Thirty-one contextual full-record readings are retained with matching hashes.
    Absence is bounded to this snapshot and corpus.'
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Twelve declared annotated CLASS nodes with outgoing edges;31 contextual
    full-record readings retained by hash.
  accessed_at: '2026-10-12T11:31:02Z'
  support: supports
  summary: AIO RegressionAnalysis identifies a supervised estimation task, while this
    native record specifies one fitting algorithm for real-valued responses. A related
    match captures its task without asserting algorithm/task equivalence. LinearRegression,
    RidgeRegression and LeastsquaresAnalysis do not identify the kernel, learned tube
    or piecewise-linear loss. The source derives this supervised kernel optimization
    from support-vector methods, but the pinned AIO target describes a network with
    input, hidden and output parts. This native identity is an optimization algorithm,
    so the network abstraction is related rather than an asserted exact or broader
    class. KernelLayer names a component, and generic Network or TrainingStrategy
    also does not identify the objective. Twelve annotated AIO CLASS nodes and their
    outgoing edges were inspected. AIO BinaryClassification identifies the supervised
    two-group task, while this native record specifies a particular margin-based fitting
    algorithm. A related match preserves this abstraction difference. Classification
    and SupervisedLearning are broader task context, not exact identities for the
    nu objective. The source derives this supervised kernel optimization from support-vector
    methods, but the pinned AIO target describes a network with input, hidden and
    output parts. This native identity is an optimization algorithm, so the network
    abstraction is related rather than an asserted exact or broader class. KernelLayer
    names a component, and generic Network or TrainingStrategy also does not identify
    the objective. Twelve annotated AIO CLASS nodes and their outgoing edges were
    inspected.
- evidence_id: scholkopf2000
  kind: primary_source
  reference: https://www.stat.purdue.edu/~yuzhu/stat598m3/Papers/NewSVM.pdf
  locator: Neural Computation12(5):1207-1245, May2000. Exact39-page journal PDF hosted
    by Purdue; allpages visually read including11figures,4tables and references. Printedpage=PDFpage+1206.
    The1998 conference precursor and external proof dependencies were not fully audited.
  accessed_at: '2026-10-12T11:05:38Z'
  snapshot_sha256: 57eb6d4db2e8d90f5a1c34055c91fe36deb34977d54031f9c09acbd9dc3b9bb4
  support: supports
  summary: All39 original journal pages visually read, including11figures,4tables,
    formal objectives/proofs, discussion and references. External proof dependencies
    and later methods were not fully audited.
- evidence_id: finite-certificates
  kind: record_content
  reference: research/discovery/nu-svm-boundaries.py
  accessed_at: '2026-10-12T11:31:02Z'
  snapshot_sha256: b65d75700f65680a298d5d30d3cf49de26ad81d82eae69fb89e77125a6bfa917
  support: supports
  summary: Exact finite certificates show that positive-width/margin counts need not
    equalnu, zero-width/margin cases need qualifications, endpoint offsets and widths
    can be nonunique, and class imbalance limits feasible nu. A constant supplied
    basis also refutes the printed upper-support-bound wording in the pending parametric
    variant. These are curator calculations, not model training or a universal asymptotic
    disproof.
assessments:
- assessment_id: identity-definition
  area: identity
  topic: Original supervised optimization identity
  outcome: supported
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - identity
  - scholkopf2000
  summary: Retain the source-scoped algorithm identity.
  details: 'A supervised binary-classification algorithm that jointly fits a regularized
    kernel hyperplane and a nonnegative margin level, using nu to reward that level
    relative to linearly penalized margin shortfalls. The original binary nu-SVC formulation
    in Scholkopf, Smola, Williamson and Bartlett (2000) is the selected identity.
    It differs from a particular decomposition solver, multiclass reduction, nu-SVR
    and the one-class estimator; source-specific equivalence to C-SVC requires fitted
    positive rho and parameter conversion. Compared all442 pinned AIO IDs, labels
    and scoped synonyms against all520 preceding native IDs, names and aliases, without
    a normalized collision. Full-text fixed-string whole-word searches in both checkouts
    included ignored and hidden files, expanded labels, acronyms, DOI and paper identifiers.
    Read all25 distinct matching text windows across88 locations: these are the existing
    one-class record context, its review/renderings and the preceding discovery lead,
    not supervised nu records. All125 semantic AIO rows and115 prior native name/definition
    rows match the previous reading; the additional one-class row and complete record
    were read. Thirty-one contextual full-record readings are retained with matching
    hashes. Absence is bounded to this snapshot and corpus.'
- assessment_id: related-mappings
  area: grounding
  topic: Task and network abstraction
  outcome: supported
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - mapping
  - scholkopf2000
  summary: Related mappings preserve the algorithm/task/network distinctions.
  details: AIO BinaryClassification identifies the supervised two-group task, while
    this native record specifies a particular margin-based fitting algorithm. A related
    match preserves this abstraction difference. Classification and SupervisedLearning
    are broader task context, not exact identities for the nu objective. The source
    derives this supervised kernel optimization from support-vector methods, but the
    pinned AIO target describes a network with input, hidden and output parts. This
    native identity is an optimization algorithm, so the network abstraction is related
    rather than an asserted exact or broader class. KernelLayer names a component,
    and generic Network or TrainingStrategy also does not identify the objective.
    Twelve annotated AIO CLASS nodes and their outgoing edges were inspected.
- assessment_id: learned-margin-objective
  area: evidence
  topic: learned margin objective
  outcome: supported
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - scholkopf2000
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'For n observations with both binary labels y_i in{-1,+1} represented and
    a positive-semidefinite kernel, minimize (1/2)||w||^2-nu*rho+sum_i xi_i/n, subject
    to y_i*(w.Phi(x_i)+b)>=rho-xi_i, xi_i>=0 and rho>=0. A positive feasible nu is
    at most2*min(n_positive,n_negative)/n, as follows directly from the balanced dual
    masses and coefficient caps. Values beyond this class-balance limit make the stated
    dual infeasible and primal unbounded. For three positive and one negative label,
    nu=3/4 exceeds the limit1/2; w=0,b=rho=t and negative slack2t give objective -t/4.
    Locator: Section 7, PDF pp17-19 / printed pp1223-1225, Equations 7.3-7.12; feasibility
    implication and exact example in research/discovery/nu-svm-boundaries.py'
- assessment_id: dual-and-decision
  area: evidence
  topic: dual and decision
  outcome: supported
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - scholkopf2000
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'The dual minimizes (1/2)*alpha^T*Y*K*Y*alpha, with0<=alpha_i<=1/n, sum_i
    alpha_i*y_i=0 and sum_i alpha_i>=nu. The score is g(x)=sum_i alpha_i*y_i*k(x_i,x)+b
    and the classifier takes its sign. The source does not specify how an exactly
    zero score is assigned to one binary label. When free coefficients exist in both
    classes, KKT equalities give g(x_positive)=rho and g(x_negative)=-rho and permit
    recovery of b and rho. Such free coefficients need not exist; general recovery
    must respect the remaining KKT inequalities. Locator: Section 7, PDF pp18-19 /
    printed pp1224-1225, Equations 7.7-7.15'
- assessment_id: margin-error-counts
  area: evidence
  topic: margin error counts
  outcome: supported
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - scholkopf2000
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'For an exact optimum with rho>0, sum_i alpha_i=nu. Thus nu bounds the
    fraction of strict margin errors y_i*g(x_i)<rho from above and the positive-coefficient
    fraction from below. A margin error can still be correctly classified; it is not
    the same event as misclassification. Finite counts need not equal nu, and capped
    coefficients can occur on the margin. Four linear-kernel inputs -1,-1,1,1 with
    matching labels and nu=1/2 admit alpha_i=1/8,w=1/2,b=0,rho=1/2: all points are
    support vectors and none is a strict margin error. The source states the finite
    result under an analytic-kernel assumption; its additional asymptotic distribution
    and boundary-mass arguments are not promoted to unconditional calibration. Locator:
    Section 7 Proposition 5, PDF pp20-21 / printed pp1226-1227; exact finite certificate
    in research/discovery/nu-svm-boundaries.py'
- assessment_id: c-svc-correspondence
  area: evidence
  topic: c svc correspondence
  outcome: supported
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - scholkopf2000
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'If the fitted rho is positive, dividing w,b and slacks by rho yields a
    C-SVC optimum with C=1/rho in the paper’s C/n slack-penalty convention, preserving
    the sign decision. The numerical conversion differs when software uses C times
    the unaveraged slack sum. A global positive multiplier on the nu-SVC loss terms
    scales the solution without changing its boundary, explaining removal of that
    separate C parameter. This does not remove kernel selection or make arbitrary
    C and nu settings equivalent, and the conversion cannot divide by rho=0. Locator:
    Section 7, PDF p19 / printed p1225, homogeneity discussion; Proposition 6, PDF
    p21 / printed p1227'
- assessment_id: degenerate-and-nonunique-offsets
  area: evidence
  topic: degenerate and nonunique offsets
  outcome: supported
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - scholkopf2000
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'Feasibility does not guarantee positive rho or a useful binary separator.
    Balanced opposite labels at identical zero inputs admit w=b=rho=0. Even at rho>0,
    b and rho can be nonunique when no coefficient is free: for linear-kernel inputs
    -1 and1 with matching labels and nu=1, both coefficients are1/2 and w=1, while
    (b,rho)=(0,1) and(3,4) attain the same objective -1/2 and classify the first training
    point differently. Strict convexity fixes the optimal normal w, not necessarily
    the intercept, margin variable or singular-Gram coefficient representation. Locator:
    Section 7, PDF pp18-21 / printed pp1224-1227, primal/dual constraints, free-coefficient
    formulas and positive-rho condition; exact certificates in research/discovery/nu-svm-boundaries.py'
- assessment_id: generalization-and-robustness-limits
  area: evidence
  topic: generalization and robustness limits
  outcome: supported
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - scholkopf2000
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'The generalization analysis adds sample-size, confidence, margin and function-class
    complexity terms to empirical margin error; test risk is not bounded by nu alone.
    Its displayed normalized radial-kernel bound omits the intercept b, and the authors
    explicitly note that treating b requires a modification. Their resistance statement
    is conditional on a representation using free support vectors and local movements
    in feature space parallel to w; it is not arbitrary input-space or label-noise
    robustness. External proof dependencies were not independently audited. Locator:
    Section 7 Propositions 7-10, PDF pp21-24 / printed pp1227-1230, including the
    paragraph following Proposition 10'
- assessment_id: classification-evaluation-scope
  area: evidence
  topic: classification evaluation scope
  outcome: supported
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - scholkopf2000
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'The classification study shows a two-dimensional circles-versus-disks
    example with a Gaussian kernel and nu values from0.1 to0.8, reporting support-vector
    and margin-error fractions plus geometric margins. The paper leaves real-world
    nu-SVC evaluation and efficient chunking methods to future work. It supplies no
    universal accuracy or runtime advantage over C-SVC, and later decomposition solvers
    are not identified with this original optimization formulation. Locator: Section
    8.2 and Table 4/Figure 11, PDF pp32 and35 / printed pp1238 and1241; Section 9,
    PDF p36 / printed p1242'
- assessment_id: adversarial-feasibility
  area: consistency
  topic: Class balance and bounded optimization
  outcome: supported
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - scholkopf2000
  - finite-certificates
  summary: The feasible range follows from the displayed dual.
  details: 'Balanced class coefficient sums are equal and at mostmin(n_positive,n_negative)/n
    each. Thus positive feasible nu cannot exceed twice that value. Above it, choose
    w0 and b=rho toward the majority class: average slack grows as2*n_minority*rho/n,
    while the reward is-nu*rho, proving unboundedness. The exact3:1 example verifies
    this coefficient. This is an explicitly labeled implication of the primary constraints,
    not an unseen theorem attribution.'
- assessment_id: adversarial-margin-offset
  area: consistency
  topic: Positive margin, scaling and endpoint ambiguity
  outcome: supported
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - scholkopf2000
  - finite-certificates
  summary: Positive rho and free-coefficient assumptions are not dropped.
  details: Rho complementarity forces totalalpha=nu whenrho>0; capped strictmarginerrors
    and positive coefficient counts give the inequalities. The four-point certificate
    has no strict errors and full support. Zero features with conflicting labels admitrho0,
    preventing division by it. Atnu1 two capped coefficients givew1 while b0/rho1
    andb3/rho4 have equal exact objectives and different predictions. Dividing the
    fixed-rho primal by rho² yields C=1/rho under C/n normalization; a different software
    convention changes that numeric value.
- assessment_id: adversarial-theory
  area: evidence
  topic: Intercept and experimental scope
  outcome: supported
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - scholkopf2000
  summary: The bounds and evaluations retain their stated limits.
  details: Read the missing-b note following Proposition10, conditional feature-space
    resistance statement and circles/disks toy experiment. No bound risk<=nu, unconditional
    robustness or real-world runtime advantage is curated. External proofs and later
    decomposition solvers are excluded from approval.
- assessment_id: all-fields
  area: provenance
  topic: Complete record and research handoff
  outcome: supported
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - identity
  - mapping
  - scholkopf2000
  - finite-certificates
  summary: Every selected field was read after canonical capture.
  details: Read stableID,name,allaliases,kind,definition,identity notes,definition
    citation,all7claims and locators,full primary source authors/version/access/hash,exactAIOpin,both
    mapping rationales,limitations,DRAFTstatus and actual curation provenance. The
    mirrored report and append-only history were checked.453pendingcohortsplus43partlyaddressedcohortsremain;
    no saturation is claimed.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:NuSupportVectorClassification
  evidence_ids:
  - identity
  - mapping
  - scholkopf2000
  - finite-certificates
  rationale: The selected supervised formulation has a distinct target and objective
    from the other nu variant, one-class estimation and sphere fitting. Conditional
    parameter conversion does not equate arbitrary fitting settings or identify a
    solver implementation.
limitations:
- Adversarial author self-review only; native status remains DRAFT.
- All39 original journal pages were visually read, including11figures,4tables and
  references. The1998 precursor, external proofs and later decomposition sources were
  not fully audited.
- The public Purdue PDF was downloaded and rendered successfully. Some adjacent primary-page
  opens failed or returned browser checks, while their indexed abstracts were available;
  access failures are not evidence of absence. No access-control bypass was attempted.
- Exact rational examples verify feasibility, KKT conditions and primal/dual equality
  for selected finite cases. No historical solver, model training or benchmark was
  executed.
- The printed parametric-insensitivity support-bound discrepancy is preserved in research
  notes and the pending frontier. Neither that extension nor later learned/twin methods
  is silently certified by these two records.
- There are522 native DRAFT records and442 unchanged AIO records.453 pending cohorts
  and43 partly addressed cohorts, plus other unresolved scopes, prevent a saturation
  claim.
related_reviews: []
links: []
tags:
- native-concepts
- support-vector-methods
- self-review
- discovery-ongoing
```
