# Scientific self-review of linear-slack and L2-loss support vector data descriptions

- Review: 20261012T074807Z-support-description
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T07:36:53Z
- Finished UTC: 2026-10-12T07:48:07Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain two distinct target-only support-description algorithms with related AIO binary-decision mappings. All selected fields are supported within their stated assumptions; no actionable defect was found in the final records.

## Scope And Provenance

All fields of the two explicitly selected target-only sphere support-description algorithms.

Selection: Exact maintained IDs AIMech:SupportVectorDataDescription and AIMech:L2LossSupportVectorDataDescription, without sampling.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base ab181382ac619413e3572febd2be2e3c9e24ce29.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SupportVectorDataDescription | data/curated/SupportVectorDataDescription.yaml | maintained | Support vector data description |
| AIMech:L2LossSupportVectorDataDescription | data/curated/L2LossSupportVectorDataDescription.yaml | maintained | L2-loss support vector data description |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Initial gate before page regeneration | failed | False | AIMech:SupportVectorDataDescription, AIMech:L2LossSupportVectorDataDescription | 245 tests passed and two page-freshness/count tests failed because seven generated pages had not yet been regenerated. Ran just render and then repeated the full required gate. This superseded initial failure is retained transparently; the required final result follows. |
| just check | passed | True | AIMech:SupportVectorDataDescription, AIMech:L2LossSupportVectorDataDescription | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 191.73s (0:03:11)<br>Checked 442 record(s); 0 failed.<br>Checked 504 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 153 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 149,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:SupportVectorDataDescription, AIMech:L2LossSupportVectorDataDescription | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:SupportVectorDataDescription, AIMech:L2LossSupportVectorDataDescription | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:SupportVectorDataDescription, AIMech:L2LossSupportVectorDataDescription | Exited0 without output. |
| Exact SVDD regime and duplicate-feature calculations | passed | True | AIMech:SupportVectorDataDescription, AIMech:L2LossSupportVectorDataDescription | {"status": "passed", "four_point_kkt": [{"t": "1", "C": "1/2", "loss": 1, "alpha": ["1/2", "0", "0", "1/2"], "slack": ["3", "0", "0", "3"], "beta": "0", "primal": "4", "dual": "4"}, {"t": "5/2", "C": "1/2", "loss": 1, "alpha": ["1/2", "0", "0", "1/2"], "slack": ["3/2", "0", "0", "3/2"], "beta": "0", "primal": "4", "dual": "4"}, {"t": "4", "C": "1/2", "loss": 1, "alpha": ["1/2", "0", "0", "1/2"], "slack": ["0", "0", "0", "0"], "beta": "0", "primal": "4", "dual": "4"}, {"t": "0", "C": "1/10", "loss": 1, "alpha": ["1/10", "1/10", "1/10", "1/10"], "slack": ["4", "1", "1", "4"], "beta": "3/5", "primal": "1", "dual": "1"}, {"t": "0", "C": "1/4", "loss": 1, "alpha": ["1/4", "1/4", "1/4", "1/4"], "slack": ["4", "1", "1", "4"], "beta": "0", "primal": "5/2", "dual": "5/2"}, {"t": "1/2", "C": "1/4", "loss": 1, "alpha": ["1/4", "1/4", "1/4", "1/4"], "slack": ["7/2", "1/2", "1/2", "7/2"], "beta": "0", "primal": "5/2", "dual": "5/2"}, {"t": "1", "C": "1/4", "loss": 1, "alpha": ["1/4", "1/4", "1/4", "1/4"], "slack": ["3", "0", "0", "3"], "beta": "0", "primal": "5/2", "dual": "5/2"}, {"t": "0", "C": "1/40", "loss": 2, "alpha": ["1/5", "1/20", "1/20", "1/5"], "slack": ["4", "1", "1", "4"], "beta": "1/2", "primal": "17/20", "dual": "17/20"}, {"t": "0", "C": "1/20", "loss": 2, "alpha": ["2/5", "1/10", "1/10", "2/5"], "slack": ["4", "1", "1", "4"], "beta": "0", "primal": "17/10", "dual": "17/10"}, {"t": "3/2", "C": "1/10", "loss": 2, "alpha": ["1/2", "0", "0", "1/2"], "slack": ["5/2", "0", "0", "5/2"], "beta": "0", "primal": "11/4", "dual": "11/4"}], "L2_threshold": "1/20", "duplicate_support_fraction": "1", "duplicate_loo_rejection_fraction": "0", "interpretation": "Exact KKT/primal-dual examples for convex target-only problems; no claim about negative-example nonconvex extensions or historical performance."} |

## Scientific And Domain Assessments

### Identity, definition and AIO mapping scope

identity: supported. Targets: AIMech:SupportVectorDataDescription.

Retain the target-only algorithm as a native DRAFT with a related binary-decision task mapping.

This record covers the target-only linear-slack method called support vector domain description in 1999 and support vector data description in 2004, with later qualifications to its optimization. L1 refers to the slack loss, not an L1 norm on the sphere center. The negative-example extension and squared-hinge-loss variant change the optimization and are not exact aliases. Sphere support estimation does not include SVC graph-component labeling or the general origin-separating one-class hyperplane formulation. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 502 preceding native IDs, names and aliases. No normalized candidate identity collision was found. Full fixed-string whole-word searches included ignored and hidden files in both checkouts, expanded names, acronyms and source identifiers. All 15 matches per checkout, eight distinct texts at 30 locations, were inspected as source queries, search terms and pending leads in the preceding discovery ledger, not existing concepts. Ten annotated AIO nodes and outgoing edges, their generated records, and three native neighbors were inspected or checked against unchanged complete readings. Four SAT Novelty-family records were inspected only for names, definitions and identity notes: those flip heuristics are unrelated. Absence is bounded to this pin and inspected corpus. A one-class support-estimation algorithm that learns a sphere in an input or kernel feature space by minimizing squared radius plus linearly penalized nonnegative distance-constraint violations, then accepts a query when its feature lies within or on the learned sphere.

### convex formulation

evidence: supported. Targets: AIMech:SupportVectorDataDescription.

The claim is supported within its stated assumptions and evidence scope.

For N target observations and C&gt;0, use squared radius t&gt;=0, center a and slacks xi_i&gt;=0 to minimize t+C*sum_i xi_i subject to &#124;&#124;Phi(x_i)-a&#124;&#124;²&lt;=t+xi_i. This is a convex reformulation of the radius-variable problem and satisfies a strict-feasibility condition supporting strong duality. The objective penalizes violation magnitudes, not an exact count of rejected examples. The optimal center is unique, but the radius and slacks can have multiple optima. Source locators: tax2004: Section 2.1, printed pp.47-49 / PDF pp.3-5, Equations 1-15; chang-revisit: Sections 2.2-3.1, PDF pp.4-7, Equation 7, Theorem 2 and Corollary 1; Appendix A, pp.15-16

### dual and small penalty

evidence: supported. Targets: AIMech:SupportVectorDataDescription.

The claim is supported within its stated assumptions and evidence scope.

For C&gt;1/N, the usual dual maximizes sum_i alpha_i*K_ii-alpha^T*K*alpha subject to sum_i alpha_i=1 and 0&lt;=alpha_i&lt;=C, and a=sum_i alpha_i*Phi(x_i). For 0&lt;C&lt;1/N this equality-simplex dual is infeasible even though the primal is feasible: its optimum has t=0 and the feature-space sample mean as center. At C=1/N the same zero-radius solution is optimal, but additional positive-radius optima may exist. Dividing the original radius stationarity equation by R silently omits R=0. For C&gt;1 the method reduces to the minimum sphere enclosing all training features. Source locators: chang-revisit: Sections 2.3 and 3.2, PDF pp.5-11, Theorems 4 and 6, Equations 9-26; Appendices B and D, pp.16-17

### radius and prediction

evidence: supported. Targets: AIMech:SupportVectorDataDescription.

The claim is supported within its stated assumptions and evidence scope.

For C&gt;1/N and an optimal dual solution, squared distances d_i² to the center bound an optimal t by max_{alpha_i&lt;C} d_i² &lt;= t &lt;= min_{alpha_i&gt;0} d_i². A free coefficient 0&lt;alpha_i&lt;C fixes the radius; otherwise choosing the interval midpoint is an implementation convention. Bounded coefficients need not be strictly outside the sphere. Accept a query when K(x,x)-2*sum_i alpha_i*K(x_i,x)+alpha^T*K*alpha&lt;=t. For observations {-2,-1,1,2} with a linear kernel and C=1/2, a=0 and every t in [1,4] achieves objective 4; this illustrates different acceptance regions at the same optimum. Source locators: tax2004: Section 2.1, printed p.49 / PDF p.5, Equations 14-15; chang-revisit: Section 3.2, PDF pp.9-11, Theorem 5 and Equations 20-23; Appendix A, p.16, Equation 41; Appendix C, p.17

### gaussian and boundary scope

evidence: supported. Targets: AIMech:SupportVectorDataDescription.

The claim is supported within its stated assumptions and evidence scope.

A Gaussian kernel exp(-&#124;&#124;x-y&#124;&#124;²/s²) gives a weighted kernel-score acceptance region without explicitly constructing features. It can produce a non-spherical region in input space. The narrow-width equal-weight limit assumes distinct training inputs; the exact constant-kernel limit is degenerate and does not select a unique coefficient vector. Comparisons with one-class hyperplane support estimation require the stated kernel/normalization conditions rather than general method identity. The boundary estimate is not by itself a normalized density model or a component-labeling rule. Source locators: tax1999: Section 3, printed pp.1193-1194 / PDF pp.3-4; tax2004: Sections 2.1 and 2.3, printed pp.50-54 / PDF pp.6-10, Equations 16-21 and 30-35; curator constant-Gram qualification

### support count and error

evidence: supported. Targets: AIMech:SupportVectorDataDescription.

The claim is supported within its stated assumptions and evidence scope.

The papers use support-vector fractions to guide target-error and kernel-width choices. The 2004 account distinguishes essential from nonessential vectors and gives a leave-one-out bound/estimate; the raw support fraction is not universally equal to observed leave-one-out rejection or a calibrated future error rate. With two identical training features and C=2, a valid two-support-vector representation has radius zero, while either leave-one-out fit accepts the omitted duplicate. For the nonnegative equality-simplex coefficients the fraction at the upper bound is at most 1/(N*C); bounded coefficients can be on the boundary, and this count bound cannot be transferred unchanged to signed negative-example coefficients. Source locators: tax1999: Section 4, printed pp.1194-1195 / PDF pp.4-5, Equation 11; tax2004: Section 2.4, printed pp.55-56 / PDF pp.11-12, Equation 36; curator duplicate-feature and coefficient-sum calculations

### empirical and extension boundaries

evidence: supported. Targets: AIMech:SupportVectorDataDescription.

The claim is supported within its stated assumptions and evidence scope.

The published tests depend on target/negative sampling, feature dimension, preprocessing, kernel width and target-rejection settings. The 2004 paper reports failures when a pump training set covers too little operating range and cautions that overlapping negative examples can worsen its separate negative-example extension. Its reverse distance constraints are not the convex target-only formulation above. These studies do not establish universal performance superiority or immunity to distribution changes. Source locators: tax1999: Sections 5-6 and Discussion, printed pp.1195-1199 / PDF pp.5-9; tax2004: Section 2.2, printed pp.51-52 / PDF pp.7-8; Sections 3-5, pp.57-65 / PDF pp.13-21, Tables 1-4 and Figures 4-7

### Identity, definition and AIO mapping scope

identity: supported. Targets: AIMech:L2LossSupportVectorDataDescription.

Retain the target-only algorithm as a native DRAFT with a related binary-decision task mapping.

This is the target-only L2-loss extension in Chang, Lee and Lin Section 4.1. L2 denotes squared slack loss, not merely the Euclidean geometry already used by standard SVDD. It changes the dual penalty and zero-radius threshold and is distinct from linear-slack SVDD, negative-example SVDD, origin-separating one-class SVM and support-vector clustering. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 502 preceding native IDs, names and aliases. No normalized candidate identity collision was found. Full fixed-string whole-word searches included ignored and hidden files in both checkouts, expanded names, acronyms and source identifiers. All 15 matches per checkout, eight distinct texts at 30 locations, were inspected as source queries, search terms and pending leads in the preceding discovery ledger, not existing concepts. Ten annotated AIO nodes and outgoing edges, their generated records, and three native neighbors were inspected or checked against unchanged complete readings. Four SAT Novelty-family records were inspected only for names, definitions and identity notes: those flip heuristics are unrelated. Absence is bounded to this pin and inspected corpus. A support-vector data-description algorithm that learns a feature-space sphere using squared-hinge penalties on squared-distance violations, yielding a unique optimal center, squared radius and slack vector for a fixed positive penalty and feature map.

### squared slack objective

evidence: supported. Targets: AIMech:L2LossSupportVectorDataDescription.

The claim is supported within its stated assumptions and evidence scope.

For C&gt;0, minimize t+C*sum_i xi_i² subject to t&gt;=0 and &#124;&#124;Phi(x_i)-a&#124;&#124;²&lt;=t+xi_i. Explicit nonnegativity constraints on xi are redundant at an optimum: a negative slack can be replaced by zero to improve the objective. This convex formulation has strong duality and a unique optimal center, squared radius and slack vector. Its squared violation penalty changes the method, even though both SVDD variants use squared Euclidean distances. Source locators: chang-revisit: Section 4.1, PDF p.12, Equation 27 and Theorem 7; Appendix E, pp.17-18

### zero radius threshold

evidence: supported. Targets: AIMech:L2LossSupportVectorDataDescription.

The claim is supported within its stated assumptions and evidence scope.

First consider the zero-radius auxiliary problem minimizing sum_i &#124;&#124;Phi(x_i)-a&#124;&#124;^4, with optimal squared distances xi_i*. When their sum is positive, define C*=1/(2*sum_i xi_i*). For 0&lt;C&lt;=C*, the optimal squared radius is zero and the auxiliary center is optimal; for C&gt;C* the radius is positive. This threshold depends on the data and feature map and is not the standard SVDD threshold 1/N. The auxiliary center need not be the sample mean. If all training features coincide, the optimal radius and slacks are zero at their common feature and the denominator formula is inapplicable. Source locators: chang-revisit: Section 4.1, PDF pp.12-14, Theorem 8 and Equations 28-29, 37; Appendix F, pp.18-20

### positive radius dual

evidence: supported. Targets: AIMech:L2LossSupportVectorDataDescription.

The claim is supported within its stated assumptions and evidence scope.

For C&gt;C*, maximize sum_i alpha_i*K_ii-alpha^T*K*alpha-sum_i alpha_i²/(4*C) subject to alpha_i&gt;=0 and sum_i alpha_i=1. The additional quadratic term makes the maximization objective strictly concave; there is no standard SVDD upper bound alpha_i&lt;=C, though the simplex implies alpha_i&lt;=1. Recover a=sum_i alpha_i*Phi(x_i), xi_i=alpha_i/(2*C), and t=&#124;&#124;Phi(x_i)-a&#124;&#124;²-alpha_i/(2*C) using any positive coefficient. This equality-simplex recovery is scoped to the positive-radius regime and must not be applied indiscriminately below C*. Source locators: chang-revisit: Section 4.1, PDF pp.13-14, Equations 30-36 and radius recovery

### prediction and evidence limits

evidence: supported. Targets: AIMech:L2LossSupportVectorDataDescription.

The claim is supported within its stated assumptions and evidence scope.

Prediction compares feature-space squared distance to the learned squared radius, using the kernel expansion when appropriate. A zero-radius fit accepts only queries mapped exactly to the center. The reassessment supplies mathematical derivations rather than a benchmark comparison establishing superiority of squared-hinge SVDD over linear-slack SVDD. Standard SVDD support-count and box-constraint error arguments do not transfer unchanged to this loss. For the symmetric linear-kernel sample {-2,-1,1,2}, C*=1/20; at C=1/10 the solution has center 0, t=3/2 and objective 11/4, as verified by exact KKT and primal-dual calculations. Source locators: chang-revisit: Sections 3.3 and 4.1, PDF pp.11-14; Appendices E-F, pp.17-20; curator exact symmetric four-observation calculation

### Linear versus squared slack loss

consistency: supported. Targets: AIMech:SupportVectorDataDescription, AIMech:L2LossSupportVectorDataDescription.

Retain two algorithms with different losses, dual constraints and solution uniqueness.

The squared geometry is common to both and does not define the L2-loss extension. Standard SVDD uses a box-constrained equality-simplex dual when C&gt;1/N and may have a radius interval; squared slack adds a strictly concave dual penalty in its positive-radius regime and has a data-dependent threshold. At the four symmetric points, C=1/2 gives the standard method every squared radius in[1,4] with objective4. L2-loss has C*=1/20 and at C=1/10 has squared radius3/2 and objective11/4. Exact rational KKT and primal-dual checks support these claims; these are not benchmark comparisons.

### Feasible primal, dual regime and recovery

consistency: supported. Targets: AIMech:SupportVectorDataDescription, AIMech:L2LossSupportVectorDataDescription.

The final records do not silently discard the zero-radius solution.

For standard SVDD below1/N, equality-simplex constraints are infeasible while the primal has the mean-centered zero-radius optimum. At equality, a positive-radius optimum can coexist. L2-loss threshold uses the sum of optimal squared distances in a fourth-power auxiliary problem; it is neither1/N nor necessarily mean-centered. The all-identical-features case makes the threshold denominator zero and is explicitly separated. For L2-loss above its threshold, any positive coefficient recovers t after subtracting alpha/(2C), not a standard free-vector boundary formula.

### Support counts, duplicate observations and kernel limits

consistency: supported. Targets: AIMech:SupportVectorDataDescription.

The record qualifies raw leave-one-out equality and degenerate coefficient claims.

At C=2, two identical features admit two positive free coefficients and radius0. Each leave-one-out model also accepts the duplicate at distance0; support fraction1 therefore differs from observed rejection fraction0. An exact all-ones Gram matrix admits many coefficient optima, and at C=3/4 a coefficient vector(1,0) violates the box. These qualifications avoid promoting simplified source descriptions into unconditional claims. The bounded-coefficient fraction bound uses nonnegative simplex mass and does not transfer unchanged to signed negative-example coefficients or the L2-loss dual.

### Target-only support estimation and adjacent concepts

grounding: supported. Targets: AIMech:SupportVectorDataDescription, AIMech:L2LossSupportVectorDataDescription.

Negative-example extensions and component-labeling algorithms remain distinct.

The2004 negative-example extension imposes reverse distance constraints, so the convex target-only proof does not certify its global optimization. SVC adds a segment graph and component assignment. Origin-separating one-class hyperplanes have only conditional kernel/normalization correspondences with sphere descriptions. The AIO BinaryClassification mapping is related through the two-output task and explicitly preserves that its supervised parent does not describe the training assumptions of these target-only algorithms.

### Inspected source versions and empirical limits

provenance: supported. Targets: AIMech:SupportVectorDataDescription, AIMech:L2LossSupportVectorDataDescription.

The records identify exact inspected bytes and retain mathematical and empirical limits.

All52 pages of the three primary PDFs were visually read, including appendices, figures and tables. Historical performance depends on target/negative sampling, preprocessing, dimensionality and parameter choices; the pump examples include failures from inadequate operating-range coverage. The mathematical reassessment supplies no benchmark basis for universal superiority of squared loss. The differently formatted author copy and implementation archive were not read in full. No model training or historical implementation was run. Mapping contexts receive no renewed scientific approval;431 pending discovery cohorts remain.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:SupportVectorDataDescription, AIMech:L2LossSupportVectorDataDescription. Linear and squared slack penalties define different optimization procedures, with distinct dual penalties, thresholds and uniqueness properties. The shared sphere geometry does not make them aliases. Keep negative-example methods, hyperplane estimators and clustering procedures outside these target-only identities.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T073618Z-support-description.json | supports | Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 502 preceding native IDs, names and aliases. No normalized candidate identity collision was found. Full fixed-string whole-word searches included ignored and hidden files in both checkouts, expanded names, acronyms and source identifiers. All 15 matches per checkout, eight distinct texts at 30 locations, were inspected as source queries, search terms and pending leads in the preceding discovery ledger, not existing concepts. Ten annotated AIO nodes and outgoing edges, their generated records, and three native neighbors were inspected or checked against unchanged complete readings. Four SAT Novelty-family records were inspected only for names, definitions and identity notes: those flip heuristics are unrelated. Absence is bounded to this pin and inspected corpus. |
| mapping | sources/aio/aio.json; Ten annotated class nodes and outgoing edges, ten generated YAMLs and three native neighboring records; SAT Novelty family identity fields only | supports | AIO:BinaryClassification is related through the accept-versus-reject prediction task. Its Classification parent is under SupervisedLearning, whereas this particular algorithm learns a target-class description without requiring representative negative training examples. This is a related task mapping, not algorithm-task equivalence, an is-a assertion or a claim of two-class supervision. Inspected BinaryClassification, Classification, SupervisedLearning, UnsupervisedLearning, MachineLearningTask, SupportVectorMachine, Model, Network, KernelLayer and UnsupervisedClustering, including definitions and outgoing edges. The supervised category-separating network definition of SupportVectorMachine does not identify a sphere support estimator. The clustering task assigns groups, while this method supplies an acceptance region; generic models, networks and kernel layers do not identify the algorithm. All 442 class labels and 153 semantic matches retain byte-verified prior readings; expanded description/hinge/enclosing/classification searches added no rows. SupportVectorClustering adds graph labeling; DBSCAN uses neighborhood density connectivity; KernelPCA extracts variance directions. These contexts do not receive renewed scientific approval. |
| finite-boundaries | research/discovery/support-description-boundaries.py; Exact linear-kernel four-point KKT cases and constant-Gram duplicate-feature cases | supports | Exact four-point KKT and primal-dual calculations verify L1 radius nonuniqueness, feasible small-C primal with infeasible equality-simplex dual, the equality threshold and L2 data-dependent zero-radius threshold. Symmetry and convexity justify the zero auxiliary center. Recomputed duplicate-feature leave-one-out query distances show that a raw positive-support fraction need not equal observed LOO rejection. Constant Gram coefficients expose nonunique optima and box-infeasible vertices. These are curator derivations, not historical experiments. |
| source-versions | https://www.csie.ntu.edu.tw/~cjlin/papers.html; A Revisit to Support Vector Data Description entry, compared with https://leepei.github.io/ publication entry and exact downloaded PDF | context_only | The Lin index says Technical report, 2013; the Lee index says 2015 and links a differently formatted PDF. All21 pages of the exact cited manuscript were visually read, but the other version was not compared in full. The records therefore preserve the inspected URL/hash without inventing a revision date or journal publication. The software index does not establish implementation of the L2-loss SVDD extension. |
| tax1999 | https://rduin.nl/papers/prl_99_svdd.pdf; Section 3, printed pp.1193-1194 / PDF pp.3-4; Section 4, printed pp.1194-1195 / PDF pp.4-5, Equation 11; Sections 2-3, printed pp.1192-1194 / PDF pp.2-4; Sections 5-6 and Discussion, printed pp.1195-1199 / PDF pp.5-9 | supports | Support vector domain description. Pattern Recognition Letters 20 (1999):1191-1199; exact author-hosted 9-page PDF, all pages visually read. Inspected mechanism, assumptions, evidence and limitations; historical benchmark results are not reproduced. |
| tax2004 | https://rduin.nl/papers/ML_SVDD_04.pdf; Section 2.1, printed p.49 / PDF p.5, Equations 14-15; Section 2.1, printed pp.47-49 / PDF pp.3-5, Equations 1-15; Section 2.1, printed pp.47-50 / PDF pp.3-6; Section 2.2, printed pp.51-52 / PDF pp.7-8; Sections 3-5, pp.57-65 / PDF pp.13-21, Tables 1-4 and Figures 4-7; Section 2.4, printed pp.55-56 / PDF pp.11-12, Equation 36; curator duplicate-feature and coefficient-sum calculations; Sections 2.1 and 2.3, printed pp.50-54 / PDF pp.6-10, Equations 16-21 and 30-35; curator constant-Gram qualification | supports | Support Vector Data Description. Machine Learning 54 (2004):45-66; DOI 10.1023/B:MACH.0000008084.60811.49. Exact author-hosted 22-page journal PDF, all pages visually read; final manuscript date June 17, 2002 is distinct from publication year. Inspected mechanism, assumptions, evidence and limitations; historical benchmark results are not reproduced. |
| chang-revisit | https://www.csie.ntu.edu.tw/~cjlin/papers/svdd.pdf; Section 3.2, PDF pp.9-11, Theorem 5 and Equations 20-23; Appendix A, p.16, Equation 41; Appendix C, p.17; Section 4.1, PDF p.12, Equation 27 and Theorem 7; Appendix E, pp.17-18; Section 4.1, PDF pp.11-14, Equations 27-37 and Theorems 7-8; Appendices E-F, pp.17-20; Section 4.1, PDF pp.12-14, Theorem 8 and Equations 28-29, 37; Appendix F, pp.18-20; Section 4.1, PDF pp.13-14, Equations 30-36 and radius recovery; Sections 2.2-3.1, PDF pp.4-7, Equation 7, Theorem 2 and Corollary 1; Appendix A, pp.15-16; Sections 2.2-3.3, PDF pp.4-11; Sections 2.3 and 3.2, PDF pp.5-11, Theorems 4 and 6, Equations 9-26; Appendices B and D, pp.16-17; Sections 3.3 and 4.1, PDF pp.11-14; Appendices E-F, pp.17-20; curator exact symmetric four-observation calculation | supports | A Revisit to Support Vector Data Description. Exact 21-page author-hosted manuscript at the recorded URL, all pages and appendices visually read. Lin author index identifies a Technical report, 2013; Lee author index labels the work 2015 and links a differently formatted PDF. This record identifies the inspected bytes without assigning an unverified revision date or journal publication. The two author-hosted PDF versions were not compared in full. Inspected mechanism, assumptions, evidence and limitations; historical benchmark results are not reproduced. |

## Limits And Additional Notes

- Adversarial author self-review only; both records remain DRAFT.
- All52 cited primary PDF pages were visually read, including equations, seven figures and four tables of Tax2004 and all reassessment appendices. The1999 printed-page offset is1190;2004 offset44; reassessment PDF pages equal displayed pages.
- The reassessment is preserved as the exact21-page author manuscript. Conflicting2013/2015 author-index labels and a different linked PDF prevent asserting an exact revision date or journal publication.
- Negative-example SVDD was read in the2004 paper but is retained as a distinct unresolved candidate with nonconvex optimization and recovery questions. Two-stage SVM-SVDD abstracts alone do not support a mechanism record.
- Follow-up source opens failed internally for the2015 SVM-SVDD DOI, Duin publications.html and subspace PDF. Indexed primary abstracts/first-page excerpts still identify leads; failures are not evidence of conceptual absence.
- No complete paper is redistributed. No historical implementation, training or benchmark was executed; exact rational examples check mathematical qualifications only.
- The two new records bring native DRAFT concepts to504, with442 generated AIO records unchanged. There remain431 pending cohorts and other unresolved dispositions; no saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T074807Z-support-description
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of linear-slack and L2-loss support vector data descriptions
started_at: '2026-10-12T07:36:53Z'
finished_at: '2026-10-12T07:48:07Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent visually read all52 cited PDF pages, inspected
    ignored-inclusive identity matches and mapping context, reread every field of
    both final records, and challenged optimization regimes, recovery, uniqueness,
    duplicate-feature error estimates, kernel degeneracy and evidence versions with
    exact calculations. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain two distinct target-only support-description algorithms with related
  AIO binary-decision mappings. All selected fields are supported within their stated
  assumptions; no actionable defect was found in the final records.
source:
  git_revision: ab181382ac619413e3572febd2be2e3c9e24ce29
  state: working_tree
  inputs:
  - path: data/aio/BinaryClassification.yaml
    sha256: 4c710e70fe7e71227f0c6aa55162a3683f04ebbe6f5a4601bd4c0398329f1481
    role: context
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
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
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
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
  - path: data/curated/KernelPCA.yaml
    sha256: a93227a6b2d6b2b89b679b8f7f9ddd5054741d1c11f9510490d82a3e691a1cab
    role: context
  - path: data/curated/L2LossSupportVectorDataDescription.yaml
    sha256: 42d0072e69d90f8f70b87bec4393787ce23f2b9e494d1efa74aaad270cec1893
    role: target
  - path: data/curated/Novelty.yaml
    sha256: 6a85c443510cb4ecee4dbe2f4a5b43e87c53c8e0f3c11142dc81a6419a6feee5
    role: context
  - path: data/curated/NoveltyPlus.yaml
    sha256: a019ef5bec6faf42ce64e3cbc2f7d3388832c103505e9635f213ccfd1a4f5a75
    role: context
  - path: data/curated/RNovelty.yaml
    sha256: ae6b7c18041ad345bf7db44d26a350e7d64d99164b98ac730262490b5c88ba98
    role: context
  - path: data/curated/RNoveltyPlus.yaml
    sha256: c6130d848787664b24ec75a07270c548a644ec7c9ec77b375bde2b0d269e7c03
    role: context
  - path: data/curated/SupportVectorClustering.yaml
    sha256: f15f79f69443b23faa8247bb4fb67d86caeb2a80a86ae0e8c97dd247e152ad3a
    role: context
  - path: data/curated/SupportVectorDataDescription.yaml
    sha256: 45e181fa0ce8eeeda5c10e6e3fbce658b05bfd650e7c9c6bf77501d7fa315b7b
    role: target
  - path: research/discovery/20261012T073618Z-support-description.json
    sha256: 641021eca5b4c440875934019acbbd46fdca5c084ed5688990fc1fba16e9ebb8
    role: context
  - path: research/discovery/support-description-boundaries.py
    sha256: 7ac1228abf3d4da6cdc77272d1c33482970fe955a8a3ea0a511903baa4e04c6a
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
- target_id: AIMech:SupportVectorDataDescription
  path: data/curated/SupportVectorDataDescription.yaml
  label: Support vector data description
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SupportVectorDataDescription.yaml
    role: maintained
- target_id: AIMech:L2LossSupportVectorDataDescription
  path: data/curated/L2LossSupportVectorDataDescription.yaml
  label: L2-loss support vector data description
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/L2LossSupportVectorDataDescription.yaml
    role: maintained
scope:
  description: All fields of the two explicitly selected target-only sphere support-description
    algorithms.
  selection: Exact maintained IDs AIMech:SupportVectorDataDescription and AIMech:L2LossSupportVectorDataDescription,
    without sampling.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - AIMech:SupportVectorDataDescription
  - AIMech:L2LossSupportVectorDataDescription
  exclusions:
  - target: Seventeen contextual AIO/native YAMLs
    reason: Ten AIO and three neighboring native records inform identity and mappings;
      four SAT Novelty-family records were inspected only in their identity fields.
      None receives renewed scientific approval.
  - target: Historical implementation and benchmark reproduction
    reason: Only exact mathematical boundary calculations were executed.
  - target: Other author-hosted reassessment version
    reason: Differently formatted linked PDF was not compared in full; version equivalence
      is not asserted.
  - target: Generated website
    reason: Freshness and validity are checked without a separate visual-design review.
  - target: Remaining discovery frontier
    reason: 431 pending cohorts and other unresolved dispositions remain.
checks:
- check_id: initial-gate
  name: Initial gate before page regeneration
  command: just check
  status: failed
  required: false
  target_ids:
  - AIMech:SupportVectorDataDescription
  - AIMech:L2LossSupportVectorDataDescription
  exit_code: 1
  expected_exit_code: 0
  summary: 245 tests passed and two page-freshness/count tests failed because seven
    generated pages had not yet been regenerated. Ran just render and then repeated
    the full required gate. This superseded initial failure is retained transparently;
    the required final result follows.
- check_id: required-1
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:SupportVectorDataDescription
  - AIMech:L2LossSupportVectorDataDescription
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 191.73s (0:03:11)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 504 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 153 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 149,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-2
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:SupportVectorDataDescription
  - AIMech:L2LossSupportVectorDataDescription
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: required-3
  name: uv run --locked aimech check-source
  command: uv run --locked aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:SupportVectorDataDescription
  - AIMech:L2LossSupportVectorDataDescription
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
- check_id: required-4
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:SupportVectorDataDescription
  - AIMech:L2LossSupportVectorDataDescription
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: exact-boundaries
  name: Exact SVDD regime and duplicate-feature calculations
  command: python3 research/discovery/support-description-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SupportVectorDataDescription
  - AIMech:L2LossSupportVectorDataDescription
  exit_code: 0
  expected_exit_code: 0
  summary: '{"status": "passed", "four_point_kkt": [{"t": "1", "C": "1/2", "loss":
    1, "alpha": ["1/2", "0", "0", "1/2"], "slack": ["3", "0", "0", "3"], "beta": "0",
    "primal": "4", "dual": "4"}, {"t": "5/2", "C": "1/2", "loss": 1, "alpha": ["1/2",
    "0", "0", "1/2"], "slack": ["3/2", "0", "0", "3/2"], "beta": "0", "primal": "4",
    "dual": "4"}, {"t": "4", "C": "1/2", "loss": 1, "alpha": ["1/2", "0", "0", "1/2"],
    "slack": ["0", "0", "0", "0"], "beta": "0", "primal": "4", "dual": "4"}, {"t":
    "0", "C": "1/10", "loss": 1, "alpha": ["1/10", "1/10", "1/10", "1/10"], "slack":
    ["4", "1", "1", "4"], "beta": "3/5", "primal": "1", "dual": "1"}, {"t": "0", "C":
    "1/4", "loss": 1, "alpha": ["1/4", "1/4", "1/4", "1/4"], "slack": ["4", "1", "1",
    "4"], "beta": "0", "primal": "5/2", "dual": "5/2"}, {"t": "1/2", "C": "1/4", "loss":
    1, "alpha": ["1/4", "1/4", "1/4", "1/4"], "slack": ["7/2", "1/2", "1/2", "7/2"],
    "beta": "0", "primal": "5/2", "dual": "5/2"}, {"t": "1", "C": "1/4", "loss": 1,
    "alpha": ["1/4", "1/4", "1/4", "1/4"], "slack": ["3", "0", "0", "3"], "beta":
    "0", "primal": "5/2", "dual": "5/2"}, {"t": "0", "C": "1/40", "loss": 2, "alpha":
    ["1/5", "1/20", "1/20", "1/5"], "slack": ["4", "1", "1", "4"], "beta": "1/2",
    "primal": "17/20", "dual": "17/20"}, {"t": "0", "C": "1/20", "loss": 2, "alpha":
    ["2/5", "1/10", "1/10", "2/5"], "slack": ["4", "1", "1", "4"], "beta": "0", "primal":
    "17/10", "dual": "17/10"}, {"t": "3/2", "C": "1/10", "loss": 2, "alpha": ["1/2",
    "0", "0", "1/2"], "slack": ["5/2", "0", "0", "5/2"], "beta": "0", "primal": "11/4",
    "dual": "11/4"}], "L2_threshold": "1/20", "duplicate_support_fraction": "1", "duplicate_loo_rejection_fraction":
    "0", "interpretation": "Exact KKT/primal-dual examples for convex target-only
    problems; no claim about negative-example nonconvex extensions or historical performance."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T073618Z-support-description.json
  accessed_at: '2026-10-12T07:36:53Z'
  support: supports
  summary: 'Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 502
    preceding native IDs, names and aliases. No normalized candidate identity collision
    was found. Full fixed-string whole-word searches included ignored and hidden files
    in both checkouts, expanded names, acronyms and source identifiers. All 15 matches
    per checkout, eight distinct texts at 30 locations, were inspected as source queries,
    search terms and pending leads in the preceding discovery ledger, not existing
    concepts. Ten annotated AIO nodes and outgoing edges, their generated records,
    and three native neighbors were inspected or checked against unchanged complete
    readings. Four SAT Novelty-family records were inspected only for names, definitions
    and identity notes: those flip heuristics are unrelated. Absence is bounded to
    this pin and inspected corpus.'
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Ten annotated class nodes and outgoing edges, ten generated YAMLs and three
    native neighboring records; SAT Novelty family identity fields only
  accessed_at: '2026-10-12T07:36:53Z'
  support: supports
  summary: AIO:BinaryClassification is related through the accept-versus-reject prediction
    task. Its Classification parent is under SupervisedLearning, whereas this particular
    algorithm learns a target-class description without requiring representative negative
    training examples. This is a related task mapping, not algorithm-task equivalence,
    an is-a assertion or a claim of two-class supervision. Inspected BinaryClassification,
    Classification, SupervisedLearning, UnsupervisedLearning, MachineLearningTask,
    SupportVectorMachine, Model, Network, KernelLayer and UnsupervisedClustering,
    including definitions and outgoing edges. The supervised category-separating network
    definition of SupportVectorMachine does not identify a sphere support estimator.
    The clustering task assigns groups, while this method supplies an acceptance region;
    generic models, networks and kernel layers do not identify the algorithm. All
    442 class labels and 153 semantic matches retain byte-verified prior readings;
    expanded description/hinge/enclosing/classification searches added no rows. SupportVectorClustering
    adds graph labeling; DBSCAN uses neighborhood density connectivity; KernelPCA
    extracts variance directions. These contexts do not receive renewed scientific
    approval.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/support-description-boundaries.py
  locator: Exact linear-kernel four-point KKT cases and constant-Gram duplicate-feature
    cases
  accessed_at: '2026-10-12T07:36:53Z'
  snapshot_sha256: 7ac1228abf3d4da6cdc77272d1c33482970fe955a8a3ea0a511903baa4e04c6a
  support: supports
  summary: Exact four-point KKT and primal-dual calculations verify L1 radius nonuniqueness,
    feasible small-C primal with infeasible equality-simplex dual, the equality threshold
    and L2 data-dependent zero-radius threshold. Symmetry and convexity justify the
    zero auxiliary center. Recomputed duplicate-feature leave-one-out query distances
    show that a raw positive-support fraction need not equal observed LOO rejection.
    Constant Gram coefficients expose nonunique optima and box-infeasible vertices.
    These are curator derivations, not historical experiments.
- evidence_id: source-versions
  kind: primary_source
  reference: https://www.csie.ntu.edu.tw/~cjlin/papers.html
  locator: A Revisit to Support Vector Data Description entry, compared with https://leepei.github.io/
    publication entry and exact downloaded PDF
  accessed_at: '2026-10-12T07:36:53Z'
  support: context_only
  summary: The Lin index says Technical report, 2013; the Lee index says 2015 and
    links a differently formatted PDF. All21 pages of the exact cited manuscript were
    visually read, but the other version was not compared in full. The records therefore
    preserve the inspected URL/hash without inventing a revision date or journal publication.
    The software index does not establish implementation of the L2-loss SVDD extension.
- evidence_id: tax1999
  kind: primary_source
  reference: https://rduin.nl/papers/prl_99_svdd.pdf
  locator: Section 3, printed pp.1193-1194 / PDF pp.3-4; Section 4, printed pp.1194-1195
    / PDF pp.4-5, Equation 11; Sections 2-3, printed pp.1192-1194 / PDF pp.2-4; Sections
    5-6 and Discussion, printed pp.1195-1199 / PDF pp.5-9
  accessed_at: '2026-10-12T07:18:49Z'
  snapshot_sha256: 3a5748fa74d9dcfa36f126f12dc56d55ca41c782189d164a439deabb29bd6d77
  support: supports
  summary: Support vector domain description. Pattern Recognition Letters 20 (1999):1191-1199;
    exact author-hosted 9-page PDF, all pages visually read. Inspected mechanism,
    assumptions, evidence and limitations; historical benchmark results are not reproduced.
- evidence_id: tax2004
  kind: primary_source
  reference: https://rduin.nl/papers/ML_SVDD_04.pdf
  locator: Section 2.1, printed p.49 / PDF p.5, Equations 14-15; Section 2.1, printed
    pp.47-49 / PDF pp.3-5, Equations 1-15; Section 2.1, printed pp.47-50 / PDF pp.3-6;
    Section 2.2, printed pp.51-52 / PDF pp.7-8; Sections 3-5, pp.57-65 / PDF pp.13-21,
    Tables 1-4 and Figures 4-7; Section 2.4, printed pp.55-56 / PDF pp.11-12, Equation
    36; curator duplicate-feature and coefficient-sum calculations; Sections 2.1 and
    2.3, printed pp.50-54 / PDF pp.6-10, Equations 16-21 and 30-35; curator constant-Gram
    qualification
  accessed_at: '2026-10-12T07:21:27Z'
  snapshot_sha256: fe7e0705e66bae7237353ec43dbaf23cecc0c527d375d966b35170c1787bef30
  support: supports
  summary: Support Vector Data Description. Machine Learning 54 (2004):45-66; DOI
    10.1023/B:MACH.0000008084.60811.49. Exact author-hosted 22-page journal PDF, all
    pages visually read; final manuscript date June 17, 2002 is distinct from publication
    year. Inspected mechanism, assumptions, evidence and limitations; historical benchmark
    results are not reproduced.
- evidence_id: chang-revisit
  kind: primary_source
  reference: https://www.csie.ntu.edu.tw/~cjlin/papers/svdd.pdf
  locator: Section 3.2, PDF pp.9-11, Theorem 5 and Equations 20-23; Appendix A, p.16,
    Equation 41; Appendix C, p.17; Section 4.1, PDF p.12, Equation 27 and Theorem
    7; Appendix E, pp.17-18; Section 4.1, PDF pp.11-14, Equations 27-37 and Theorems
    7-8; Appendices E-F, pp.17-20; Section 4.1, PDF pp.12-14, Theorem 8 and Equations
    28-29, 37; Appendix F, pp.18-20; Section 4.1, PDF pp.13-14, Equations 30-36 and
    radius recovery; Sections 2.2-3.1, PDF pp.4-7, Equation 7, Theorem 2 and Corollary
    1; Appendix A, pp.15-16; Sections 2.2-3.3, PDF pp.4-11; Sections 2.3 and 3.2,
    PDF pp.5-11, Theorems 4 and 6, Equations 9-26; Appendices B and D, pp.16-17; Sections
    3.3 and 4.1, PDF pp.11-14; Appendices E-F, pp.17-20; curator exact symmetric four-observation
    calculation
  accessed_at: '2026-10-12T07:21:32Z'
  snapshot_sha256: 7618a0ff3b9260977e3a9d94231258a7271be76cc4d226fd8b7c21f3fb9f8a44
  support: supports
  summary: A Revisit to Support Vector Data Description. Exact 21-page author-hosted
    manuscript at the recorded URL, all pages and appendices visually read. Lin author
    index identifies a Technical report, 2013; Lee author index labels the work 2015
    and links a differently formatted PDF. This record identifies the inspected bytes
    without assigning an unverified revision date or journal publication. The two
    author-hosted PDF versions were not compared in full. Inspected mechanism, assumptions,
    evidence and limitations; historical benchmark results are not reproduced.
assessments:
- assessment_id: supportvectordatadescription-identity
  area: identity
  topic: Identity, definition and AIO mapping scope
  outcome: supported
  target_ids:
  - AIMech:SupportVectorDataDescription
  evidence_ids:
  - identity
  - mapping
  - tax1999
  - tax2004
  - chang-revisit
  summary: Retain the target-only algorithm as a native DRAFT with a related binary-decision
    task mapping.
  details: 'This record covers the target-only linear-slack method called support
    vector domain description in 1999 and support vector data description in 2004,
    with later qualifications to its optimization. L1 refers to the slack loss, not
    an L1 norm on the sphere center. The negative-example extension and squared-hinge-loss
    variant change the optimization and are not exact aliases. Sphere support estimation
    does not include SVC graph-component labeling or the general origin-separating
    one-class hyperplane formulation. Compared all 442 pinned AIO IDs, labels and
    scoped synonyms with all 502 preceding native IDs, names and aliases. No normalized
    candidate identity collision was found. Full fixed-string whole-word searches
    included ignored and hidden files in both checkouts, expanded names, acronyms
    and source identifiers. All 15 matches per checkout, eight distinct texts at 30
    locations, were inspected as source queries, search terms and pending leads in
    the preceding discovery ledger, not existing concepts. Ten annotated AIO nodes
    and outgoing edges, their generated records, and three native neighbors were inspected
    or checked against unchanged complete readings. Four SAT Novelty-family records
    were inspected only for names, definitions and identity notes: those flip heuristics
    are unrelated. Absence is bounded to this pin and inspected corpus. A one-class
    support-estimation algorithm that learns a sphere in an input or kernel feature
    space by minimizing squared radius plus linearly penalized nonnegative distance-constraint
    violations, then accepts a query when its feature lies within or on the learned
    sphere.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A fitting and prediction procedure, not a trained instance.
    evidence_ids:
    - tax1999
    - tax2004
    - chang-revisit
  - name: aio-mapping
    value: related_match
    definition: Accept-versus-reject prediction relates to the binary classification
      task. This does not assert algorithm/task equivalence or representative two-class
      supervision.
    evidence_ids:
    - mapping
- assessment_id: supportvectordatadescription-convex-formulation
  area: evidence
  topic: convex formulation
  outcome: supported
  target_ids:
  - AIMech:SupportVectorDataDescription
  evidence_ids:
  - tax2004
  - chang-revisit
  - finite-boundaries
  summary: The claim is supported within its stated assumptions and evidence scope.
  details: 'For N target observations and C>0, use squared radius t>=0, center a and
    slacks xi_i>=0 to minimize t+C*sum_i xi_i subject to ||Phi(x_i)-a||²<=t+xi_i.
    This is a convex reformulation of the radius-variable problem and satisfies a
    strict-feasibility condition supporting strong duality. The objective penalizes
    violation magnitudes, not an exact count of rejected examples. The optimal center
    is unique, but the radius and slacks can have multiple optima. Source locators:
    tax2004: Section 2.1, printed pp.47-49 / PDF pp.3-5, Equations 1-15; chang-revisit:
    Sections 2.2-3.1, PDF pp.4-7, Equation 7, Theorem 2 and Corollary 1; Appendix
    A, pp.15-16'
- assessment_id: supportvectordatadescription-dual-and-small-penalty
  area: evidence
  topic: dual and small penalty
  outcome: supported
  target_ids:
  - AIMech:SupportVectorDataDescription
  evidence_ids:
  - chang-revisit
  - finite-boundaries
  summary: The claim is supported within its stated assumptions and evidence scope.
  details: 'For C>1/N, the usual dual maximizes sum_i alpha_i*K_ii-alpha^T*K*alpha
    subject to sum_i alpha_i=1 and 0<=alpha_i<=C, and a=sum_i alpha_i*Phi(x_i). For
    0<C<1/N this equality-simplex dual is infeasible even though the primal is feasible:
    its optimum has t=0 and the feature-space sample mean as center. At C=1/N the
    same zero-radius solution is optimal, but additional positive-radius optima may
    exist. Dividing the original radius stationarity equation by R silently omits
    R=0. For C>1 the method reduces to the minimum sphere enclosing all training features.
    Source locators: chang-revisit: Sections 2.3 and 3.2, PDF pp.5-11, Theorems 4
    and 6, Equations 9-26; Appendices B and D, pp.16-17'
- assessment_id: supportvectordatadescription-radius-and-prediction
  area: evidence
  topic: radius and prediction
  outcome: supported
  target_ids:
  - AIMech:SupportVectorDataDescription
  evidence_ids:
  - tax2004
  - chang-revisit
  - finite-boundaries
  summary: The claim is supported within its stated assumptions and evidence scope.
  details: 'For C>1/N and an optimal dual solution, squared distances d_i² to the
    center bound an optimal t by max_{alpha_i<C} d_i² <= t <= min_{alpha_i>0} d_i².
    A free coefficient 0<alpha_i<C fixes the radius; otherwise choosing the interval
    midpoint is an implementation convention. Bounded coefficients need not be strictly
    outside the sphere. Accept a query when K(x,x)-2*sum_i alpha_i*K(x_i,x)+alpha^T*K*alpha<=t.
    For observations {-2,-1,1,2} with a linear kernel and C=1/2, a=0 and every t in
    [1,4] achieves objective 4; this illustrates different acceptance regions at the
    same optimum. Source locators: tax2004: Section 2.1, printed p.49 / PDF p.5, Equations
    14-15; chang-revisit: Section 3.2, PDF pp.9-11, Theorem 5 and Equations 20-23;
    Appendix A, p.16, Equation 41; Appendix C, p.17'
- assessment_id: supportvectordatadescription-gaussian-and-boundary-scope
  area: evidence
  topic: gaussian and boundary scope
  outcome: supported
  target_ids:
  - AIMech:SupportVectorDataDescription
  evidence_ids:
  - tax1999
  - tax2004
  - finite-boundaries
  summary: The claim is supported within its stated assumptions and evidence scope.
  details: 'A Gaussian kernel exp(-||x-y||²/s²) gives a weighted kernel-score acceptance
    region without explicitly constructing features. It can produce a non-spherical
    region in input space. The narrow-width equal-weight limit assumes distinct training
    inputs; the exact constant-kernel limit is degenerate and does not select a unique
    coefficient vector. Comparisons with one-class hyperplane support estimation require
    the stated kernel/normalization conditions rather than general method identity.
    The boundary estimate is not by itself a normalized density model or a component-labeling
    rule. Source locators: tax1999: Section 3, printed pp.1193-1194 / PDF pp.3-4;
    tax2004: Sections 2.1 and 2.3, printed pp.50-54 / PDF pp.6-10, Equations 16-21
    and 30-35; curator constant-Gram qualification'
- assessment_id: supportvectordatadescription-support-count-and-error
  area: evidence
  topic: support count and error
  outcome: supported
  target_ids:
  - AIMech:SupportVectorDataDescription
  evidence_ids:
  - tax1999
  - tax2004
  - finite-boundaries
  summary: The claim is supported within its stated assumptions and evidence scope.
  details: 'The papers use support-vector fractions to guide target-error and kernel-width
    choices. The 2004 account distinguishes essential from nonessential vectors and
    gives a leave-one-out bound/estimate; the raw support fraction is not universally
    equal to observed leave-one-out rejection or a calibrated future error rate. With
    two identical training features and C=2, a valid two-support-vector representation
    has radius zero, while either leave-one-out fit accepts the omitted duplicate.
    For the nonnegative equality-simplex coefficients the fraction at the upper bound
    is at most 1/(N*C); bounded coefficients can be on the boundary, and this count
    bound cannot be transferred unchanged to signed negative-example coefficients.
    Source locators: tax1999: Section 4, printed pp.1194-1195 / PDF pp.4-5, Equation
    11; tax2004: Section 2.4, printed pp.55-56 / PDF pp.11-12, Equation 36; curator
    duplicate-feature and coefficient-sum calculations'
- assessment_id: supportvectordatadescription-empirical-and-extension-boundaries
  area: evidence
  topic: empirical and extension boundaries
  outcome: supported
  target_ids:
  - AIMech:SupportVectorDataDescription
  evidence_ids:
  - tax1999
  - tax2004
  - finite-boundaries
  summary: The claim is supported within its stated assumptions and evidence scope.
  details: 'The published tests depend on target/negative sampling, feature dimension,
    preprocessing, kernel width and target-rejection settings. The 2004 paper reports
    failures when a pump training set covers too little operating range and cautions
    that overlapping negative examples can worsen its separate negative-example extension.
    Its reverse distance constraints are not the convex target-only formulation above.
    These studies do not establish universal performance superiority or immunity to
    distribution changes. Source locators: tax1999: Sections 5-6 and Discussion, printed
    pp.1195-1199 / PDF pp.5-9; tax2004: Section 2.2, printed pp.51-52 / PDF pp.7-8;
    Sections 3-5, pp.57-65 / PDF pp.13-21, Tables 1-4 and Figures 4-7'
- assessment_id: l2losssupportvectordatadescription-identity
  area: identity
  topic: Identity, definition and AIO mapping scope
  outcome: supported
  target_ids:
  - AIMech:L2LossSupportVectorDataDescription
  evidence_ids:
  - identity
  - mapping
  - chang-revisit
  summary: Retain the target-only algorithm as a native DRAFT with a related binary-decision
    task mapping.
  details: 'This is the target-only L2-loss extension in Chang, Lee and Lin Section
    4.1. L2 denotes squared slack loss, not merely the Euclidean geometry already
    used by standard SVDD. It changes the dual penalty and zero-radius threshold and
    is distinct from linear-slack SVDD, negative-example SVDD, origin-separating one-class
    SVM and support-vector clustering. Compared all 442 pinned AIO IDs, labels and
    scoped synonyms with all 502 preceding native IDs, names and aliases. No normalized
    candidate identity collision was found. Full fixed-string whole-word searches
    included ignored and hidden files in both checkouts, expanded names, acronyms
    and source identifiers. All 15 matches per checkout, eight distinct texts at 30
    locations, were inspected as source queries, search terms and pending leads in
    the preceding discovery ledger, not existing concepts. Ten annotated AIO nodes
    and outgoing edges, their generated records, and three native neighbors were inspected
    or checked against unchanged complete readings. Four SAT Novelty-family records
    were inspected only for names, definitions and identity notes: those flip heuristics
    are unrelated. Absence is bounded to this pin and inspected corpus. A support-vector
    data-description algorithm that learns a feature-space sphere using squared-hinge
    penalties on squared-distance violations, yielding a unique optimal center, squared
    radius and slack vector for a fixed positive penalty and feature map.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A fitting and prediction procedure, not a trained instance.
    evidence_ids:
    - chang-revisit
  - name: aio-mapping
    value: related_match
    definition: Accept-versus-reject prediction relates to the binary classification
      task. This does not assert algorithm/task equivalence or representative two-class
      supervision.
    evidence_ids:
    - mapping
- assessment_id: l2losssupportvectordatadescription-squared-slack-objective
  area: evidence
  topic: squared slack objective
  outcome: supported
  target_ids:
  - AIMech:L2LossSupportVectorDataDescription
  evidence_ids:
  - chang-revisit
  - finite-boundaries
  summary: The claim is supported within its stated assumptions and evidence scope.
  details: 'For C>0, minimize t+C*sum_i xi_i² subject to t>=0 and ||Phi(x_i)-a||²<=t+xi_i.
    Explicit nonnegativity constraints on xi are redundant at an optimum: a negative
    slack can be replaced by zero to improve the objective. This convex formulation
    has strong duality and a unique optimal center, squared radius and slack vector.
    Its squared violation penalty changes the method, even though both SVDD variants
    use squared Euclidean distances. Source locators: chang-revisit: Section 4.1,
    PDF p.12, Equation 27 and Theorem 7; Appendix E, pp.17-18'
- assessment_id: l2losssupportvectordatadescription-zero-radius-threshold
  area: evidence
  topic: zero radius threshold
  outcome: supported
  target_ids:
  - AIMech:L2LossSupportVectorDataDescription
  evidence_ids:
  - chang-revisit
  - finite-boundaries
  summary: The claim is supported within its stated assumptions and evidence scope.
  details: 'First consider the zero-radius auxiliary problem minimizing sum_i ||Phi(x_i)-a||^4,
    with optimal squared distances xi_i*. When their sum is positive, define C*=1/(2*sum_i
    xi_i*). For 0<C<=C*, the optimal squared radius is zero and the auxiliary center
    is optimal; for C>C* the radius is positive. This threshold depends on the data
    and feature map and is not the standard SVDD threshold 1/N. The auxiliary center
    need not be the sample mean. If all training features coincide, the optimal radius
    and slacks are zero at their common feature and the denominator formula is inapplicable.
    Source locators: chang-revisit: Section 4.1, PDF pp.12-14, Theorem 8 and Equations
    28-29, 37; Appendix F, pp.18-20'
- assessment_id: l2losssupportvectordatadescription-positive-radius-dual
  area: evidence
  topic: positive radius dual
  outcome: supported
  target_ids:
  - AIMech:L2LossSupportVectorDataDescription
  evidence_ids:
  - chang-revisit
  - finite-boundaries
  summary: The claim is supported within its stated assumptions and evidence scope.
  details: 'For C>C*, maximize sum_i alpha_i*K_ii-alpha^T*K*alpha-sum_i alpha_i²/(4*C)
    subject to alpha_i>=0 and sum_i alpha_i=1. The additional quadratic term makes
    the maximization objective strictly concave; there is no standard SVDD upper bound
    alpha_i<=C, though the simplex implies alpha_i<=1. Recover a=sum_i alpha_i*Phi(x_i),
    xi_i=alpha_i/(2*C), and t=||Phi(x_i)-a||²-alpha_i/(2*C) using any positive coefficient.
    This equality-simplex recovery is scoped to the positive-radius regime and must
    not be applied indiscriminately below C*. Source locators: chang-revisit: Section
    4.1, PDF pp.13-14, Equations 30-36 and radius recovery'
- assessment_id: l2losssupportvectordatadescription-prediction-and-evidence-limits
  area: evidence
  topic: prediction and evidence limits
  outcome: supported
  target_ids:
  - AIMech:L2LossSupportVectorDataDescription
  evidence_ids:
  - chang-revisit
  - finite-boundaries
  summary: The claim is supported within its stated assumptions and evidence scope.
  details: 'Prediction compares feature-space squared distance to the learned squared
    radius, using the kernel expansion when appropriate. A zero-radius fit accepts
    only queries mapped exactly to the center. The reassessment supplies mathematical
    derivations rather than a benchmark comparison establishing superiority of squared-hinge
    SVDD over linear-slack SVDD. Standard SVDD support-count and box-constraint error
    arguments do not transfer unchanged to this loss. For the symmetric linear-kernel
    sample {-2,-1,1,2}, C*=1/20; at C=1/10 the solution has center 0, t=3/2 and objective
    11/4, as verified by exact KKT and primal-dual calculations. Source locators:
    chang-revisit: Sections 3.3 and 4.1, PDF pp.11-14; Appendices E-F, pp.17-20; curator
    exact symmetric four-observation calculation'
- assessment_id: loss-boundary
  area: consistency
  topic: Linear versus squared slack loss
  outcome: supported
  target_ids:
  - AIMech:SupportVectorDataDescription
  - AIMech:L2LossSupportVectorDataDescription
  evidence_ids:
  - tax1999
  - tax2004
  - chang-revisit
  - finite-boundaries
  summary: Retain two algorithms with different losses, dual constraints and solution
    uniqueness.
  details: The squared geometry is common to both and does not define the L2-loss
    extension. Standard SVDD uses a box-constrained equality-simplex dual when C>1/N
    and may have a radius interval; squared slack adds a strictly concave dual penalty
    in its positive-radius regime and has a data-dependent threshold. At the four
    symmetric points, C=1/2 gives the standard method every squared radius in[1,4]
    with objective4. L2-loss has C*=1/20 and at C=1/10 has squared radius3/2 and objective11/4.
    Exact rational KKT and primal-dual checks support these claims; these are not
    benchmark comparisons.
- assessment_id: zero-radius-and-recovery
  area: consistency
  topic: Feasible primal, dual regime and recovery
  outcome: supported
  target_ids:
  - AIMech:SupportVectorDataDescription
  - AIMech:L2LossSupportVectorDataDescription
  evidence_ids:
  - chang-revisit
  - finite-boundaries
  summary: The final records do not silently discard the zero-radius solution.
  details: For standard SVDD below1/N, equality-simplex constraints are infeasible
    while the primal has the mean-centered zero-radius optimum. At equality, a positive-radius
    optimum can coexist. L2-loss threshold uses the sum of optimal squared distances
    in a fourth-power auxiliary problem; it is neither1/N nor necessarily mean-centered.
    The all-identical-features case makes the threshold denominator zero and is explicitly
    separated. For L2-loss above its threshold, any positive coefficient recovers
    t after subtracting alpha/(2C), not a standard free-vector boundary formula.
- assessment_id: support-count-and-degeneracy
  area: consistency
  topic: Support counts, duplicate observations and kernel limits
  outcome: supported
  target_ids:
  - AIMech:SupportVectorDataDescription
  evidence_ids:
  - tax1999
  - tax2004
  - finite-boundaries
  summary: The record qualifies raw leave-one-out equality and degenerate coefficient
    claims.
  details: At C=2, two identical features admit two positive free coefficients and
    radius0. Each leave-one-out model also accepts the duplicate at distance0; support
    fraction1 therefore differs from observed rejection fraction0. An exact all-ones
    Gram matrix admits many coefficient optima, and at C=3/4 a coefficient vector(1,0)
    violates the box. These qualifications avoid promoting simplified source descriptions
    into unconditional claims. The bounded-coefficient fraction bound uses nonnegative
    simplex mass and does not transfer unchanged to signed negative-example coefficients
    or the L2-loss dual.
- assessment_id: negative-examples-and-neighbors
  area: grounding
  topic: Target-only support estimation and adjacent concepts
  outcome: supported
  target_ids:
  - AIMech:SupportVectorDataDescription
  - AIMech:L2LossSupportVectorDataDescription
  evidence_ids:
  - identity
  - mapping
  - tax2004
  - chang-revisit
  summary: Negative-example extensions and component-labeling algorithms remain distinct.
  details: The2004 negative-example extension imposes reverse distance constraints,
    so the convex target-only proof does not certify its global optimization. SVC
    adds a segment graph and component assignment. Origin-separating one-class hyperplanes
    have only conditional kernel/normalization correspondences with sphere descriptions.
    The AIO BinaryClassification mapping is related through the two-output task and
    explicitly preserves that its supervised parent does not describe the training
    assumptions of these target-only algorithms.
- assessment_id: provenance-and-evaluation
  area: provenance
  topic: Inspected source versions and empirical limits
  outcome: supported
  target_ids:
  - AIMech:SupportVectorDataDescription
  - AIMech:L2LossSupportVectorDataDescription
  evidence_ids:
  - tax1999
  - tax2004
  - chang-revisit
  - source-versions
  summary: The records identify exact inspected bytes and retain mathematical and
    empirical limits.
  details: All52 pages of the three primary PDFs were visually read, including appendices,
    figures and tables. Historical performance depends on target/negative sampling,
    preprocessing, dimensionality and parameter choices; the pump examples include
    failures from inadequate operating-range coverage. The mathematical reassessment
    supplies no benchmark basis for universal superiority of squared loss. The differently
    formatted author copy and implementation archive were not read in full. No model
    training or historical implementation was run. Mapping contexts receive no renewed
    scientific approval;431 pending discovery cohorts remain.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:SupportVectorDataDescription
  - AIMech:L2LossSupportVectorDataDescription
  evidence_ids:
  - identity
  - mapping
  - tax1999
  - tax2004
  - chang-revisit
  - finite-boundaries
  rationale: Linear and squared slack penalties define different optimization procedures,
    with distinct dual penalties, thresholds and uniqueness properties. The shared
    sphere geometry does not make them aliases. Keep negative-example methods, hyperplane
    estimators and clustering procedures outside these target-only identities.
limitations:
- Adversarial author self-review only; both records remain DRAFT.
- All52 cited primary PDF pages were visually read, including equations, seven figures
  and four tables of Tax2004 and all reassessment appendices. The1999 printed-page
  offset is1190;2004 offset44; reassessment PDF pages equal displayed pages.
- The reassessment is preserved as the exact21-page author manuscript. Conflicting2013/2015
  author-index labels and a different linked PDF prevent asserting an exact revision
  date or journal publication.
- Negative-example SVDD was read in the2004 paper but is retained as a distinct unresolved
  candidate with nonconvex optimization and recovery questions. Two-stage SVM-SVDD
  abstracts alone do not support a mechanism record.
- Follow-up source opens failed internally for the2015 SVM-SVDD DOI, Duin publications.html
  and subspace PDF. Indexed primary abstracts/first-page excerpts still identify leads;
  failures are not evidence of conceptual absence.
- No complete paper is redistributed. No historical implementation, training or benchmark
  was executed; exact rational examples check mathematical qualifications only.
- The two new records bring native DRAFT concepts to504, with442 generated AIO records
  unchanged. There remain431 pending cohorts and other unresolved dispositions; no
  saturation.
links: []
tags:
- native-concepts
- support-description
- self-review
- discovery-ongoing
```
