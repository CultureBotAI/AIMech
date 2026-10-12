# Scientific author self-review of Semiparametric support vector regression

- Review: 20261012T114833Z-semiparametric-svr-review
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T11:44:37Z
- Finished UTC: 2026-10-12T11:48:33Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the source-scoped algorithm. No actionable finding remains in this reviewed record; formulation, evaluation, version and access limits are explicit.

## Scope And Provenance

Every field of one maintained semiparametric regression record.

Selection: Exact maintained ID AIMech:SemiparametricSupportVectorRegression
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a28e888ad5002299e83caaf113d22ba7c23ba2ad.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SemiparametricSupportVectorRegression | data/curated/SemiparametricSupportVectorRegression.yaml | maintained | Semiparametric support vector regression |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:SemiparametricSupportVectorRegression | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 104.43s (0:01:44)<br>Checked 442 record(s); 0 failed.<br>Checked 524 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 171 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 167,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:SemiparametricSupportVectorRegression | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:SemiparametricSupportVectorRegression | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:SemiparametricSupportVectorRegression | Exited0 without output. |
| Exact semiparametric regression certificates | passed | True | AIMech:SemiparametricSupportVectorRegression | {"joint_fit": {"w": "1", "beta": "0", "raw_primal": "1/4", "normalized_dual": "1/2", "all_kkt_products_zero": true}, "one_pass_fit": {"w": "1/3", "beta": "2", "raw_primal": "49/36", "normalized_dual": "49/18", "all_kkt_products_zero": true}, "quadratic_regularizer": {"w": "2/3", "beta": "0", "raw_primal": "4/3", "normalized_dual": "4/9", "all_kkt_products_zero": true}, "coefficient_l1_regularizer": {"coefficients": ["0", "0"], "predictions": ["0", "0"], "raw_primal": "2", "raw_dual": "2", "primal_dual_equality": true}, "alternative_lp_optima": [{"coefficients": ["-1", "0"], "predictions": ["-1", "1"], "raw_primal": "1/2", "raw_dual": "1/2", "primal_dual_equality": true}, {"coefficients": ["0", "1"], "predictions": ["-1", "1"], "raw_primal": "1/2", "raw_dual": "1/2", "primal_dual_equality": true}, {"coefficients": ["-1/2", "1/2"], "predictions": ["-1", "1"], "raw_primal": "1/2", "raw_dual": "1/2", "primal_dual_equality": true}], "limits": "Finite curator-derived certificates, not performance evidence, a general convergence theorem, or an audit of all backfitting algorithms."} |

## Scientific And Domain Assessments

### Source-specific semiparametric algorithm

identity: supported. Targets: AIMech:SemiparametricSupportVectorRegression.

Retain the distinct, narrowly scoped algorithm identity.

A supervised regression algorithm that jointly fits an unpenalized finite expansion of supplied basis functions and a kernel component, minimizing fixed epsilon-insensitive residual loss plus a squared feature-space norm penalty on the kernel component. Selected source-specific scalar-regression formulation from Smola, Friess and Scholkopf, NIPS 1998. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 522 existing native IDs, names and aliases; no normalized identity collision. Fixed-string whole-word searches across both checkouts included ignored and hidden files, expanded labels, semiparametric spellings, author variants and paper identifiers. All 54 matching locations were accounted for through 23 distinct text windows: the previous source lead, its metadata correction and an unrelated semiparametric factor-analysis reference. The semantic search returned 126 AIO name/definition rows and 121 native name/definition rows. Prior readings were reused only with unchanged contents; new rows were read. Thirty-five full contextual records were hash-verified, including the new nu-SVR/SVC records; twelve complete annotated AIO CLASS nodes and their edges were inspected. This is a bounded snapshot/corpus assessment, not a claim of absence from all literature. This record covers the unpenalized parametric component in Section 2. A constant-only supplied basis recovers the usual intercept special case. It is distinct from nu-SVR learning a tube width, the 2000 supplied-insensitivity basis that changes the tube shape, coefficient-L1 linear-programming regression and the additional penalties on the supplied basis in Section 3. Generic semiparametric statistics and all later semiparametric SVM variants are not aliases.

### Task and network abstraction

grounding: supported. Targets: AIMech:SemiparametricSupportVectorRegression.

Related mappings preserve the algorithm/task/network distinctions.

The pinned target denotes a supervised estimation task. This record specifies a fitting algorithm for real-valued responses, so the relation captures the task without asserting algorithm/task equivalence. LinearRegression, RidgeRegression and LeastsquaresAnalysis do not specify this kernel expansion, fixed epsilon-insensitive loss and differently regularized basis components. The source extends support-vector kernel fitting, but the pinned AIO target describes a network with input, hidden and output parts. The native record denotes an optimization algorithm, making this a related abstraction rather than an exact match or asserted subclass. KernelLayer and RegularizationLayer are neural components, while TrainingStrategy and Network are too general to identify this objective.

### joint function objective

evidence: supported. Targets: AIMech:SemiparametricSupportVectorRegression.

Supported within the stated source and mathematical scope.

For scalar responses y_i, a positive-semidefinite kernel k with feature map psi, fixed epsilon&gt;=0 and lambda&gt;0, use f(x)=w.psi(x)+sum_j beta_j*phi_j(x). The finite functions phi_j are supplied; the real beta_j are unpenalized. Jointly minimize sum_i max(0,abs(y_i-f(x_i))-epsilon)+(lambda/2)*&#124;&#124;w&#124;&#124;^2. Constant phi=1 gives an intercept, but no extra intercept is implicit when it is omitted from the supplied basis. The component changes the fitted function rather than learning an input-dependent tube. Locator: Section 2, Equations 1 and 4–7, PDF pp. 2–3 / printed pp. 586–587

### normalized dual

evidence: supported. Targets: AIMech:SemiparametricSupportVectorRegression.

Supported within the stated source and mathematical scope.

After dividing the primal objective by lambda, write a_i=alpha_i-alpha_star_i. Maximize y.a-(1/2)*a^T*K*a-epsilon*sum_i(alpha_i+alpha_star_i), subject to 0&lt;=alpha_i,alpha_star_i&lt;=1/lambda and sum_i a_i*phi_j(x_i)=0 for every supplied basis function. Recover w=sum_i a_i*psi(x_i) and f(x)=sum_i a_i*k(x_i,x)+sum_j beta_j*phi_j(x). The printed Equation 6 uses this normalized convention: its optimal value equals the raw Equation 5 primal value divided by lambda, not the raw value itself. Locator: Section 2, Equations 1 and 4–7, PDF pp. 2–3 / printed pp. 586–587; curator-derived exact certificates in research/discovery/semiparametric-regression-boundaries.py

### coefficient recovery

evidence: supported. Targets: AIMech:SemiparametricSupportVectorRegression.

Supported within the stated source and mathematical scope.

The supplied-basis coefficients can be recovered through the primal/dual KKT conditions or as equality-constraint multipliers of the normalized dual; the paper uses an interior-point method. For a free alpha_i, y_i-f(x_i)=epsilon; for a free alpha_star_i, f(x_i)-y_i=epsilon. Recovering every beta from such equations needs sufficient independent information. Free coefficients, full basis rank and unique beta are not guaranteed. Locator: Section 2, Equations 1 and 4–7, PDF pp. 2–3 / printed pp. 586–587

### sequential fit boundary

evidence: supported. Targets: AIMech:SemiparametricSupportVectorRegression.

Supported within the stated source and mathematical scope.

Fitting the parametric component once and holding it fixed while fitting residuals need not minimize the joint objective. A curator-derived specialization uses x=y=(1,3), epsilon=0, lambda=1/2 and f(x)=w*x+beta. The joint optimum w=1,beta=0 has raw objective 1/4. A first-stage absolute-loss median beta=2, followed by optimal fitting with beta fixed, gives w=1/3 and objective 49/36. This supports the paper’s one-pass counterexample; it does not establish failure of every iterative backfitting or coordinate-descent procedure. Locator: Section 4, PDF pp. 4–5 / printed pp. 588–589; curator-derived exact certificates in research/discovery/semiparametric-regression-boundaries.py

### supplied basis limits

evidence: supported. Targets: AIMech:SemiparametricSupportVectorRegression.

Supported within the stated source and mathematical scope.

The kernel norm does not penalize the supplied finite component. Appropriate basis choice can encode prior structure, but the paper does not establish automatic recovery of the true basis, globally identifiable coefficients or a universal accuracy benefit. Overlapping or rank-deficient supplied functions can make beta nonunique. Section 3 changes the method when it adds an L1 penalty to beta, replacing zero dual basis moments with bounds; that penalized variant is outside this record. Locator: Sections 1–3, PDF pp. 1–4 / printed pp. 585–588, especially Equations 8 and 11

### evaluation scope

evidence: supported. Targets: AIMech:SemiparametricSupportVectorRegression.

Supported within the stated source and mathematical scope.

The empirical study is a synthetic regression proof of concept: sin(x)+sinc(2*pi*(x-5)), x uniform on [0,10], uniform additive noise with standard deviation 0.2, Gaussian RBF width 1/4 and fixed epsilon=0.05. Unless stated otherwise, 100 datasets contain 50 observations each. The paper compares a supplied sin(x),cos(x),1 basis, an incorrect-frequency sin(2x),cos(2x),1 basis and nonparametric SV regression. Regularization is selected separately by 10-fold cross-validation; L1 and L2 errors are evaluated over [0,10] with uniform measure. Table 1 parentheses count trials in which a model was best. Its plus/minus uncertainty is not explicitly identified as standard deviation or standard error. No numerical gain, universal superiority or guarantee that a wrong basis cannot harm is asserted here. Locator: Section 5, Figures 2–5 and Table 1, PDF pp. 5–6 / printed pp. 589–590

### extension and proof limits

evidence: supported. Targets: AIMech:SemiparametricSupportVectorRegression.

Supported within the stated source and mathematical scope.

The discussion connects the model to smoothing splines and representer results and describes polynomial augmentation for conditionally positive-definite kernels. The core record uses the positive-semidefinite feature-space formulation actually specified above. Proposed compound-class risk bounds, hypothesis testing and Gaussian-process extensions are future directions; the cited external kernel and representer proofs were not independently audited. Locator: Section 6 and references, PDF p. 7 / printed p. 591

### Raw objective and normalized dual

consistency: supported. Targets: AIMech:SemiparametricSupportVectorRegression.

The lambda convention and coefficient signs are explicit.

Divide the raw primal by positive lambda before taking the displayed dual. The resulting box is1/lambda, signed coefficients arealpha-alpha_star, and unpenalized beta giveszero basis moments. Thus rawprimal=lambda*normalizeddual. The exact x=y=(1,3) case yields1/4 versus1/2, preventing accidental raw-value equality. The free-alpha residual sign follows the explicitly stated convention. Sufficient independent KKT equations and free coefficients are not assumed.

### One-pass fit versus universal impossibility

consistency: supported. Targets: AIMech:SemiparametricSupportVectorRegression.

The record retains the valid narrow counterexample.

The paper calls parametric-first fitting followed by a fixed residual fit backfitting. The exact example verifies a median2 and conditional w1/3 with objective49/36, whilejointw1,beta0 achieves1/4. It does not show that all iterative coordinate methods fail or that orthogonality is necessary for every individual dataset; those stronger interpretations are excluded.

### Synthetic SV study and future directions

evidence: supported. Targets: AIMech:SemiparametricSupportVectorRegression.

No universal benefit or invented uncertainty is curated.

Reread PDF5–6: the noisy target, Gaussian width, fixed epsilon, sample counts, independently selected regularization, uniform-domain errors and tablewin counts agree. Tableplus/minus is not defined asSEMorSD; no such interpretation or numeric advantage is asserted. LP experiments are absent from this study. Source discussion proposes future compound bounds and Gaussian-process use; external representer proofs remain outside the review.

### Complete record and research handoff

provenance: supported. Targets: AIMech:SemiparametricSupportVectorRegression.

Every selected field was read after canonical capture.

Read ID,name,alias,kind,definition,identity notes,definition citation,all7claims and locators,source authors/title/version/access/hash,pinnedmappingcommit/hash,bothmappingrationales,limitations,DRAFTstatus andactualcurationprovenance. The report mirror,history andrendered output agree.455pending and44partlyaddressed cohorts remain; no saturation is claimed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:SemiparametricSupportVectorRegression. The selected source-defined objective distinguishes the squared-norm and coefficient-L1 algorithms. Shared special cases and related sparse-coding ideas do not establish exact identity with either whole formulation. The supplied component changes the function rather than learning a tube width or shape.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T114419Z-semiparametric-kernel-regression.json | supports | Selected source-specific scalar-regression formulation from Smola, Friess and Scholkopf, NIPS 1998. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 522 existing native IDs, names and aliases; no normalized identity collision. Fixed-string whole-word searches across both checkouts included ignored and hidden files, expanded labels, semiparametric spellings, author variants and paper identifiers. All 54 matching locations were accounted for through 23 distinct text windows: the previous source lead, its metadata correction and an unrelated semiparametric factor-analysis reference. The semantic search returned 126 AIO name/definition rows and 121 native name/definition rows. Prior readings were reused only with unchanged contents; new rows were read. Thirty-five full contextual records were hash-verified, including the new nu-SVR/SVC records; twelve complete annotated AIO CLASS nodes and their edges were inspected. This is a bounded snapshot/corpus assessment, not a claim of absence from all literature. This record covers the unpenalized parametric component in Section 2. A constant-only supplied basis recovers the usual intercept special case. It is distinct from nu-SVR learning a tube width, the 2000 supplied-insensitivity basis that changes the tube shape, coefficient-L1 linear-programming regression and the additional penalties on the supplied basis in Section 3. Generic semiparametric statistics and all later semiparametric SVM variants are not aliases. |
| mapping | sources/aio/aio.json; Twelve declared annotated CLASS nodes and incident edges;35 full-record contextual readings retained by hash. | supports | Related RegressionAnalysis and SupportVectorMachine mappings preserve algorithm versus task/network distinctions. Twelve complete annotated source nodes and edges were inspected. LassoRegression is contextual, not an asserted equivalence; neural KernelLayer/RegularizationLayer and generic TrainingStrategy do not identify the methods. Mapping assertions remain local to the pinned snapshot. |
| smola1998 | https://proceedings.neurips.cc/paper_files/paper/1998/file/70efba66d3d8d53194fb1a8446ae07fa-Paper.pdf; Advances in Neural Information Processing Systems 11, pp. 585–591. Proceedings website and BibTeX label NIPS 1998/year 1998; later bibliographies cite the book as 1999. Exact seven-page proceedings PDF, all pages visually read including five figures, Table 1 and references. Printed page = PDF page + 584. | supports | All seven primary pages visually read, including five figures, Table1, all six sections and references. Formula pages3–4 and evaluation pages5–6 reread during final author review. External representer/kernel proofs were not audited. |
| finite-certificates | research/discovery/semiparametric-regression-boundaries.py | supports | Raw primal values equal lambda times the normalized SV dual. One-pass fitting need not achieve the joint optimum. The two regularizers can produce distinct predictions at the same statedlambda, and LP optima can have different support patterns and sparsity. These finite curator examples do not establish universal behavior or comparative performance. |

## Limits And Additional Notes

- Adversarial author self-review only; native status remains DRAFT.
- All seven primary proceedings pages were visually read, with five figures and one table. External representer/kernel proofs, the precursor report and later methods remain unaudited.
- The proceedings BibTeX was accessible through the public URL after the web reader rejected its MIME type. Some adjacent publisher page bodies failed or were unreadable; indexed primary abstracts remain provisional identity evidence.
- Curator-derived exact rational examples verify finite primal/dual and KKT conditions; no optimization solver, trained model or historical benchmark was executed.
- The original fixed-epsilon LP record does not inherit empirical results from the squared-norm SV experiments. Other penalties in the same section are not silently labeled linear programs.
- 524 maintained DRAFT concepts and442 unchanged AIO records are present.455 pending cohorts,44 partly addressed cohorts and other unresolved scopes preclude observed saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T114833Z-semiparametric-svr-review
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Semiparametric support vector regression
started_at: '2026-10-12T11:44:37Z'
finished_at: '2026-10-12T11:48:33Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent read all seven original primary pages, compared
    identity/mapping context, challenged normalization, one-pass fitting and sparsity
    using exact primal/dual certificates, and reread every selected field after canonical
    capture. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the source-scoped algorithm. No actionable finding remains in this
  reviewed record; formulation, evaluation, version and access limits are explicit.
source:
  git_revision: a28e888ad5002299e83caaf113d22ba7c23ba2ad
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
  - path: data/aio/LassoRegression.yaml
    sha256: c62e7ffd00a16f5a82d514687b094aee5f6796d19a7d16200bdb10498c024949
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
  - path: data/aio/RegularizationLayer.yaml
    sha256: d4280bbc058b841655bcfcea7ef1dd1e05ac5e0211a860045f13eaa30933dbae
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
    role: context
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
  - path: data/curated/SemiparametricLinearProgrammingRegression.yaml
    sha256: e3cdf67f5bad5096075812498e31af4e8cd28c96c7dbe5afbd3931162d9cddba
    role: context
  - path: data/curated/SemiparametricSupportVectorRegression.yaml
    sha256: 80fd2ce3bd4bd0cadc816ba97ea6a83603b4b1cd9834b922440e26f39fe27c12
    role: target
  - path: data/curated/SupportVectorClustering.yaml
    sha256: f15f79f69443b23faa8247bb4fb67d86caeb2a80a86ae0e8c97dd247e152ad3a
    role: context
  - path: data/curated/SupportVectorDataDescription.yaml
    sha256: 45e181fa0ce8eeeda5c10e6e3fbce658b05bfd650e7c9c6bf77501d7fa315b7b
    role: context
  - path: research/discovery/20261012T114419Z-semiparametric-kernel-regression.json
    sha256: 781f247abf63dd68cef9384daf661ae358a1613c8f9ffb66188d1c403aecdc85
    role: context
  - path: research/discovery/semiparametric-regression-boundaries.py
    sha256: 953b1e7fe90606fab54748680719168dac51aa5d4fbbcf539c10e730fb827a0e
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
- target_id: AIMech:SemiparametricSupportVectorRegression
  path: data/curated/SemiparametricSupportVectorRegression.yaml
  label: Semiparametric support vector regression
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SemiparametricSupportVectorRegression.yaml
    role: maintained
scope:
  description: Every field of one maintained semiparametric regression record.
  selection: Exact maintained ID AIMech:SemiparametricSupportVectorRegression
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  exclusions:
  - target: Contextual records and companion algorithm
    reason: Identity/mapping context only; each target requires its separate saved
      review.
  - target: Historical solver and benchmarks
    reason: No optimizer,training or benchmark executed.
  - target: External proofs and later variants
    reason: Original proceedings fully read; external proofs,precursor andlaterfullmethods
      notaudited.
  - target: Discovery frontier
    reason: 455pending and44partlyaddressed cohorts remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 104.43s (0:01:44)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 524 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 171 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 167,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
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
  - AIMech:SemiparametricSupportVectorRegression
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
  - AIMech:SemiparametricSupportVectorRegression
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: finite-certificates
  name: Exact semiparametric regression certificates
  command: python3 research/discovery/semiparametric-regression-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  exit_code: 0
  expected_exit_code: 0
  summary: '{"joint_fit": {"w": "1", "beta": "0", "raw_primal": "1/4", "normalized_dual":
    "1/2", "all_kkt_products_zero": true}, "one_pass_fit": {"w": "1/3", "beta": "2",
    "raw_primal": "49/36", "normalized_dual": "49/18", "all_kkt_products_zero": true},
    "quadratic_regularizer": {"w": "2/3", "beta": "0", "raw_primal": "4/3", "normalized_dual":
    "4/9", "all_kkt_products_zero": true}, "coefficient_l1_regularizer": {"coefficients":
    ["0", "0"], "predictions": ["0", "0"], "raw_primal": "2", "raw_dual": "2", "primal_dual_equality":
    true}, "alternative_lp_optima": [{"coefficients": ["-1", "0"], "predictions":
    ["-1", "1"], "raw_primal": "1/2", "raw_dual": "1/2", "primal_dual_equality": true},
    {"coefficients": ["0", "1"], "predictions": ["-1", "1"], "raw_primal": "1/2",
    "raw_dual": "1/2", "primal_dual_equality": true}, {"coefficients": ["-1/2", "1/2"],
    "predictions": ["-1", "1"], "raw_primal": "1/2", "raw_dual": "1/2", "primal_dual_equality":
    true}], "limits": "Finite curator-derived certificates, not performance evidence,
    a general convergence theorem, or an audit of all backfitting algorithms."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T114419Z-semiparametric-kernel-regression.json
  accessed_at: '2026-10-12T11:44:37Z'
  support: supports
  summary: 'Selected source-specific scalar-regression formulation from Smola, Friess
    and Scholkopf, NIPS 1998. Compared all 442 pinned AIO IDs, labels and scoped synonyms
    with all 522 existing native IDs, names and aliases; no normalized identity collision.
    Fixed-string whole-word searches across both checkouts included ignored and hidden
    files, expanded labels, semiparametric spellings, author variants and paper identifiers.
    All 54 matching locations were accounted for through 23 distinct text windows:
    the previous source lead, its metadata correction and an unrelated semiparametric
    factor-analysis reference. The semantic search returned 126 AIO name/definition
    rows and 121 native name/definition rows. Prior readings were reused only with
    unchanged contents; new rows were read. Thirty-five full contextual records were
    hash-verified, including the new nu-SVR/SVC records; twelve complete annotated
    AIO CLASS nodes and their edges were inspected. This is a bounded snapshot/corpus
    assessment, not a claim of absence from all literature. This record covers the
    unpenalized parametric component in Section 2. A constant-only supplied basis
    recovers the usual intercept special case. It is distinct from nu-SVR learning
    a tube width, the 2000 supplied-insensitivity basis that changes the tube shape,
    coefficient-L1 linear-programming regression and the additional penalties on the
    supplied basis in Section 3. Generic semiparametric statistics and all later semiparametric
    SVM variants are not aliases.'
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Twelve declared annotated CLASS nodes and incident edges;35 full-record
    contextual readings retained by hash.
  accessed_at: '2026-10-12T11:44:37Z'
  support: supports
  summary: Related RegressionAnalysis and SupportVectorMachine mappings preserve algorithm
    versus task/network distinctions. Twelve complete annotated source nodes and edges
    were inspected. LassoRegression is contextual, not an asserted equivalence; neural
    KernelLayer/RegularizationLayer and generic TrainingStrategy do not identify the
    methods. Mapping assertions remain local to the pinned snapshot.
- evidence_id: smola1998
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/1998/file/70efba66d3d8d53194fb1a8446ae07fa-Paper.pdf
  locator: Advances in Neural Information Processing Systems 11, pp. 585–591. Proceedings
    website and BibTeX label NIPS 1998/year 1998; later bibliographies cite the book
    as 1999. Exact seven-page proceedings PDF, all pages visually read including five
    figures, Table 1 and references. Printed page = PDF page + 584.
  accessed_at: '2026-10-12T11:27:03Z'
  snapshot_sha256: 9ff4bcbf38105cd1aa1a06e009fb559d3dc91dd895ef832860a29416776e31fb
  support: supports
  summary: All seven primary pages visually read, including five figures, Table1,
    all six sections and references. Formula pages3–4 and evaluation pages5–6 reread
    during final author review. External representer/kernel proofs were not audited.
- evidence_id: finite-certificates
  kind: record_content
  reference: research/discovery/semiparametric-regression-boundaries.py
  accessed_at: '2026-10-12T11:44:37Z'
  snapshot_sha256: 953b1e7fe90606fab54748680719168dac51aa5d4fbbcf539c10e730fb827a0e
  support: supports
  summary: Raw primal values equal lambda times the normalized SV dual. One-pass fitting
    need not achieve the joint optimum. The two regularizers can produce distinct
    predictions at the same statedlambda, and LP optima can have different support
    patterns and sparsity. These finite curator examples do not establish universal
    behavior or comparative performance.
assessments:
- assessment_id: identity-definition
  area: identity
  topic: Source-specific semiparametric algorithm
  outcome: supported
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - identity
  - smola1998
  summary: Retain the distinct, narrowly scoped algorithm identity.
  details: 'A supervised regression algorithm that jointly fits an unpenalized finite
    expansion of supplied basis functions and a kernel component, minimizing fixed
    epsilon-insensitive residual loss plus a squared feature-space norm penalty on
    the kernel component. Selected source-specific scalar-regression formulation from
    Smola, Friess and Scholkopf, NIPS 1998. Compared all 442 pinned AIO IDs, labels
    and scoped synonyms with all 522 existing native IDs, names and aliases; no normalized
    identity collision. Fixed-string whole-word searches across both checkouts included
    ignored and hidden files, expanded labels, semiparametric spellings, author variants
    and paper identifiers. All 54 matching locations were accounted for through 23
    distinct text windows: the previous source lead, its metadata correction and an
    unrelated semiparametric factor-analysis reference. The semantic search returned
    126 AIO name/definition rows and 121 native name/definition rows. Prior readings
    were reused only with unchanged contents; new rows were read. Thirty-five full
    contextual records were hash-verified, including the new nu-SVR/SVC records; twelve
    complete annotated AIO CLASS nodes and their edges were inspected. This is a bounded
    snapshot/corpus assessment, not a claim of absence from all literature. This record
    covers the unpenalized parametric component in Section 2. A constant-only supplied
    basis recovers the usual intercept special case. It is distinct from nu-SVR learning
    a tube width, the 2000 supplied-insensitivity basis that changes the tube shape,
    coefficient-L1 linear-programming regression and the additional penalties on the
    supplied basis in Section 3. Generic semiparametric statistics and all later semiparametric
    SVM variants are not aliases.'
- assessment_id: related-mappings
  area: grounding
  topic: Task and network abstraction
  outcome: supported
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - mapping
  - smola1998
  summary: Related mappings preserve the algorithm/task/network distinctions.
  details: The pinned target denotes a supervised estimation task. This record specifies
    a fitting algorithm for real-valued responses, so the relation captures the task
    without asserting algorithm/task equivalence. LinearRegression, RidgeRegression
    and LeastsquaresAnalysis do not specify this kernel expansion, fixed epsilon-insensitive
    loss and differently regularized basis components. The source extends support-vector
    kernel fitting, but the pinned AIO target describes a network with input, hidden
    and output parts. The native record denotes an optimization algorithm, making
    this a related abstraction rather than an exact match or asserted subclass. KernelLayer
    and RegularizationLayer are neural components, while TrainingStrategy and Network
    are too general to identify this objective.
- assessment_id: joint-function-objective
  area: evidence
  topic: joint function objective
  outcome: supported
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - smola1998
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'For scalar responses y_i, a positive-semidefinite kernel k with feature
    map psi, fixed epsilon>=0 and lambda>0, use f(x)=w.psi(x)+sum_j beta_j*phi_j(x).
    The finite functions phi_j are supplied; the real beta_j are unpenalized. Jointly
    minimize sum_i max(0,abs(y_i-f(x_i))-epsilon)+(lambda/2)*||w||^2. Constant phi=1
    gives an intercept, but no extra intercept is implicit when it is omitted from
    the supplied basis. The component changes the fitted function rather than learning
    an input-dependent tube. Locator: Section 2, Equations 1 and 4–7, PDF pp. 2–3
    / printed pp. 586–587'
- assessment_id: normalized-dual
  area: evidence
  topic: normalized dual
  outcome: supported
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - smola1998
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'After dividing the primal objective by lambda, write a_i=alpha_i-alpha_star_i.
    Maximize y.a-(1/2)*a^T*K*a-epsilon*sum_i(alpha_i+alpha_star_i), subject to 0<=alpha_i,alpha_star_i<=1/lambda
    and sum_i a_i*phi_j(x_i)=0 for every supplied basis function. Recover w=sum_i
    a_i*psi(x_i) and f(x)=sum_i a_i*k(x_i,x)+sum_j beta_j*phi_j(x). The printed Equation
    6 uses this normalized convention: its optimal value equals the raw Equation 5
    primal value divided by lambda, not the raw value itself. Locator: Section 2,
    Equations 1 and 4–7, PDF pp. 2–3 / printed pp. 586–587; curator-derived exact
    certificates in research/discovery/semiparametric-regression-boundaries.py'
- assessment_id: coefficient-recovery
  area: evidence
  topic: coefficient recovery
  outcome: supported
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - smola1998
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'The supplied-basis coefficients can be recovered through the primal/dual
    KKT conditions or as equality-constraint multipliers of the normalized dual; the
    paper uses an interior-point method. For a free alpha_i, y_i-f(x_i)=epsilon; for
    a free alpha_star_i, f(x_i)-y_i=epsilon. Recovering every beta from such equations
    needs sufficient independent information. Free coefficients, full basis rank and
    unique beta are not guaranteed. Locator: Section 2, Equations 1 and 4–7, PDF pp.
    2–3 / printed pp. 586–587'
- assessment_id: sequential-fit-boundary
  area: evidence
  topic: sequential fit boundary
  outcome: supported
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - smola1998
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'Fitting the parametric component once and holding it fixed while fitting
    residuals need not minimize the joint objective. A curator-derived specialization
    uses x=y=(1,3), epsilon=0, lambda=1/2 and f(x)=w*x+beta. The joint optimum w=1,beta=0
    has raw objective 1/4. A first-stage absolute-loss median beta=2, followed by
    optimal fitting with beta fixed, gives w=1/3 and objective 49/36. This supports
    the paper’s one-pass counterexample; it does not establish failure of every iterative
    backfitting or coordinate-descent procedure. Locator: Section 4, PDF pp. 4–5 /
    printed pp. 588–589; curator-derived exact certificates in research/discovery/semiparametric-regression-boundaries.py'
- assessment_id: supplied-basis-limits
  area: evidence
  topic: supplied basis limits
  outcome: supported
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - smola1998
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'The kernel norm does not penalize the supplied finite component. Appropriate
    basis choice can encode prior structure, but the paper does not establish automatic
    recovery of the true basis, globally identifiable coefficients or a universal
    accuracy benefit. Overlapping or rank-deficient supplied functions can make beta
    nonunique. Section 3 changes the method when it adds an L1 penalty to beta, replacing
    zero dual basis moments with bounds; that penalized variant is outside this record.
    Locator: Sections 1–3, PDF pp. 1–4 / printed pp. 585–588, especially Equations
    8 and 11'
- assessment_id: evaluation-scope
  area: evidence
  topic: evaluation scope
  outcome: supported
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - smola1998
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'The empirical study is a synthetic regression proof of concept: sin(x)+sinc(2*pi*(x-5)),
    x uniform on [0,10], uniform additive noise with standard deviation 0.2, Gaussian
    RBF width 1/4 and fixed epsilon=0.05. Unless stated otherwise, 100 datasets contain
    50 observations each. The paper compares a supplied sin(x),cos(x),1 basis, an
    incorrect-frequency sin(2x),cos(2x),1 basis and nonparametric SV regression. Regularization
    is selected separately by 10-fold cross-validation; L1 and L2 errors are evaluated
    over [0,10] with uniform measure. Table 1 parentheses count trials in which a
    model was best. Its plus/minus uncertainty is not explicitly identified as standard
    deviation or standard error. No numerical gain, universal superiority or guarantee
    that a wrong basis cannot harm is asserted here. Locator: Section 5, Figures 2–5
    and Table 1, PDF pp. 5–6 / printed pp. 589–590'
- assessment_id: extension-and-proof-limits
  area: evidence
  topic: extension and proof limits
  outcome: supported
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - smola1998
  - finite-certificates
  summary: Supported within the stated source and mathematical scope.
  details: 'The discussion connects the model to smoothing splines and representer
    results and describes polynomial augmentation for conditionally positive-definite
    kernels. The core record uses the positive-semidefinite feature-space formulation
    actually specified above. Proposed compound-class risk bounds, hypothesis testing
    and Gaussian-process extensions are future directions; the cited external kernel
    and representer proofs were not independently audited. Locator: Section 6 and
    references, PDF p. 7 / printed p. 591'
- assessment_id: adversarial-scaling
  area: consistency
  topic: Raw objective and normalized dual
  outcome: supported
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - smola1998
  - finite-certificates
  summary: The lambda convention and coefficient signs are explicit.
  details: Divide the raw primal by positive lambda before taking the displayed dual.
    The resulting box is1/lambda, signed coefficients arealpha-alpha_star, and unpenalized
    beta giveszero basis moments. Thus rawprimal=lambda*normalizeddual. The exact
    x=y=(1,3) case yields1/4 versus1/2, preventing accidental raw-value equality.
    The free-alpha residual sign follows the explicitly stated convention. Sufficient
    independent KKT equations and free coefficients are not assumed.
- assessment_id: adversarial-backfitting
  area: consistency
  topic: One-pass fit versus universal impossibility
  outcome: supported
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - smola1998
  - finite-certificates
  summary: The record retains the valid narrow counterexample.
  details: The paper calls parametric-first fitting followed by a fixed residual fit
    backfitting. The exact example verifies a median2 and conditional w1/3 with objective49/36,
    whilejointw1,beta0 achieves1/4. It does not show that all iterative coordinate
    methods fail or that orthogonality is necessary for every individual dataset;
    those stronger interpretations are excluded.
- assessment_id: adversarial-evaluation
  area: evidence
  topic: Synthetic SV study and future directions
  outcome: supported
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - smola1998
  summary: No universal benefit or invented uncertainty is curated.
  details: 'Reread PDF5–6: the noisy target, Gaussian width, fixed epsilon, sample
    counts, independently selected regularization, uniform-domain errors and tablewin
    counts agree. Tableplus/minus is not defined asSEMorSD; no such interpretation
    or numeric advantage is asserted. LP experiments are absent from this study. Source
    discussion proposes future compound bounds and Gaussian-process use; external
    representer proofs remain outside the review.'
- assessment_id: all-fields
  area: provenance
  topic: Complete record and research handoff
  outcome: supported
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - identity
  - mapping
  - smola1998
  - finite-certificates
  summary: Every selected field was read after canonical capture.
  details: Read ID,name,alias,kind,definition,identity notes,definition citation,all7claims
    and locators,source authors/title/version/access/hash,pinnedmappingcommit/hash,bothmappingrationales,limitations,DRAFTstatus
    andactualcurationprovenance. The report mirror,history andrendered output agree.455pending
    and44partlyaddressed cohorts remain; no saturation is claimed.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:SemiparametricSupportVectorRegression
  evidence_ids:
  - identity
  - mapping
  - smola1998
  - finite-certificates
  rationale: The selected source-defined objective distinguishes the squared-norm
    and coefficient-L1 algorithms. Shared special cases and related sparse-coding
    ideas do not establish exact identity with either whole formulation. The supplied
    component changes the function rather than learning a tube width or shape.
limitations:
- Adversarial author self-review only; native status remains DRAFT.
- All seven primary proceedings pages were visually read, with five figures and one
  table. External representer/kernel proofs, the precursor report and later methods
  remain unaudited.
- The proceedings BibTeX was accessible through the public URL after the web reader
  rejected its MIME type. Some adjacent publisher page bodies failed or were unreadable;
  indexed primary abstracts remain provisional identity evidence.
- Curator-derived exact rational examples verify finite primal/dual and KKT conditions;
  no optimization solver, trained model or historical benchmark was executed.
- The original fixed-epsilon LP record does not inherit empirical results from the
  squared-norm SV experiments. Other penalties in the same section are not silently
  labeled linear programs.
- 524 maintained DRAFT concepts and442 unchanged AIO records are present.455 pending
  cohorts,44 partly addressed cohorts and other unresolved scopes preclude observed
  saturation.
related_reviews: []
links: []
tags:
- native-concepts
- semiparametric-regression
- self-review
- discovery-ongoing
```
