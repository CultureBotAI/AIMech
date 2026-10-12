# Initial scientific self-review of semidefinite and cutting-plane margin methods

- Review: 20261012T070104Z-margin-relaxation-initial
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T06:55:43Z
- Finished UTC: 2026-10-12T07:01:04Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The three procedure identities, mathematical qualifications and related task mappings are supported. One minor identity-note comparison needs correction because it can mischaracterize other transductive solvers.

## Scope And Provenance

All fields of the three selected margin procedures.

Selection: Exact maintained IDs SemidefiniteMaximumMarginClustering, SemisupervisedSemidefiniteMaximumMarginClustering and CuttingPlaneMulticlassMaximumMarginClustering; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base d738cb15f478a6affbae23e06cf2d0734124b2c9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SemidefiniteMaximumMarginClustering | data/curated/SemidefiniteMaximumMarginClustering.yaml | maintained | Semidefinite Maximum Margin Clustering |
| AIMech:SemisupervisedSemidefiniteMaximumMarginClustering | data/curated/SemisupervisedSemidefiniteMaximumMarginClustering.yaml | maintained | Semisupervised Semidefinite Maximum Margin Clustering |
| AIMech:CuttingPlaneMulticlassMaximumMarginClustering | data/curated/CuttingPlaneMulticlassMaximumMarginClustering.yaml | maintained | Cutting Plane Multiclass Maximum Margin Clustering |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:SemidefiniteMaximumMarginClustering, AIMech:SemisupervisedSemidefiniteMaximumMarginClustering, AIMech:CuttingPlaneMulticlassMaximumMarginClustering | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 162.68s (0:02:42)<br>Checked 442 record(s); 0 failed.<br>Checked 501 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 150 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 146,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:SemidefiniteMaximumMarginClustering, AIMech:SemisupervisedSemidefiniteMaximumMarginClustering, AIMech:CuttingPlaneMulticlassMaximumMarginClustering | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:SemidefiniteMaximumMarginClustering, AIMech:SemisupervisedSemidefiniteMaximumMarginClustering, AIMech:CuttingPlaneMulticlassMaximumMarginClustering | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:SemidefiniteMaximumMarginClustering, AIMech:SemisupervisedSemidefiniteMaximumMarginClustering, AIMech:CuttingPlaneMulticlassMaximumMarginClustering | Command exited0 with no output. |
| Margin-relaxation boundaries | passed | True | AIMech:SemidefiniteMaximumMarginClustering, AIMech:SemisupervisedSemidefiniteMaximumMarginClustering, AIMech:CuttingPlaneMulticlassMaximumMarginClustering | {"winner_convexity": {"left": -0.2, "right": 0.2, "mix": 0.1, "value_at_mix": 1.1, "convex_upper_bound": 0.9}, "balanced_relaxation": {"cuts": [[1, 1, 1, -1, -1, -1], [1, 1, -1, 1, -1, -1], [1, -1, 1, 1, -1, -1]], "matrix": [[1.0, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, -1.0, -1.0], [0.3333333333333333, 1.0, -0.3333333333333333, -0.3333333333333333, -0.3333333333333333, -0.3333333333333333], [0.3333333333333333, -0.3333333333333333, 1.0, -0.3333333333333333, -0.3333333333333333, -0.3333333333333333], [0.3333333333333333, -0.3333333333333333, -0.3333333333333333, 1.0, -0.3333333333333333, -0.3333333333333333], [-1.0, -0.3333333333333333, -0.3333333333333333, -0.3333333333333333, 1.0, 1.0], [-1.0, -0.3333333333333333, -0.3333333333333333, -0.3333333333333333, 1.0, 1.0]], "largest_eigenvalue": 3.3333333333333335, "soft_labels": [1.0, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, -1.0, -1.0], "rounded_labels": [1, 1, 1, 1, -1, -1], "rounded_label_sum": 2}, "semisupervised_decoding": {"cuts": [[1, -1, 1, 1, -1, -1], [1, -1, -1, -1, 1, 1]], "largest_eigenvalue": 4, "soft_labels": [0, 0, 1, 1, -1, -1], "fixed_labeled_relation": -1, "interpretation": "Feasible relaxed constraints, including S1-S2, permit leading-eigenvector zeros on both observed labels. With zero kernel, every feasible M is also optimal for the relaxed dual."}, "slack_normalization": {"displayed_primal_C1": 2, "printed_dual_C1": 4, "interpretation": "For norm-squared primal with slack coefficient C, alpha=2*lambda yields lambda&lt;=C/2. The printed dual bound C corresponds to slack coefficient 2C."}, "interpretation": "Exact finite examples plus PSD Gram and trace arguments; no solver or benchmark reproduction."} |

## Scientific And Domain Assessments

### Definition, mechanism, limitations and mapping direction

evidence: supported. Targets: AIMech:SemidefiniteMaximumMarginClustering.

The scoped mechanism, claim locators, concept kind and related task mapping are supported; the semisupervised identity-note comparison is tracked separately.

For N observations with fixed PSD kernel matrix K, the hard binary label matrix is M=y*y^T with y_i in {-1,+1}. Replace its integer entries by a symmetric PSD matrix with diagonal 1 and entries in [-1,1], retaining m_ik&gt;=m_ij+m_jk-1 and m_jk&gt;=-m_ij-m_ik-1 for every triple, and &#124;sum_i m_ij&#124;&lt;=ell for every column. The first two linear families preserve constraints satisfied by binary equivalence relations; PSD and these constraints do not force rank one after relaxation. In the integer case the column bound equals a bound on the difference in class counts; ell&lt;N excludes assigning everything to one class, subject to feasibility. Minimize over the feasible label matrix M the convex objective max_{0&lt;=lambda_i&lt;=C} [2*sum_i lambda_i-lambda^T*(K elementwise M)*lambda], with C&gt;0. The paper equivalent SDP minimizes delta over M, delta and nonnegative mu,nu, requiring the block matrix with upper-left K elementwise M, off-diagonal 1+mu-nu and bottom-right delta-2*C*sum_i nu_i to be PSD. This optimizes a relaxation for a fixed input kernel; it does not learn a combination of input kernels. The derivation fixes the classifier intercept to zero, which centering does not make identical to freely optimizing an intercept. The stated recovery is the soft vector sqrt(lambda_max(M))*v_max(M), not necessarily a binary partition or probabilities. A global SDP solution need not solve the discrete clustering problem. The source mentions randomized rounding without specifying a complete rounding policy or balance certificate. A feasible convex mixture of three balanced six-point label matrices can have a unique leading eigenvector whose signs split the data 4-to-2 despite zero column sums. These matrix constraints therefore do not alone guarantee count balance after sign rounding. Eigenvector sign, zero entries and repeated top eigenvalues require conventions. The record uses the displayed dual and SDP convention. The printed Equation3 norm-squared primal has slack coefficient C, but its displayed dual bound lambda&lt;=C corresponds to slack coefficient 2*C under alpha=2*lambda. With two zero-feature observations of opposite labels and C=1, the displayed primal optimum is 2 while the printed dual optimum is 4. Thus those displays should not be treated as numerically identical with the same C. A soft-margin regularized objective with nonzero slacks is also not simply the reciprocal squared geometric margin. Limitations: The method targets binary clustering with a supplied PSD kernel, penalty and feasible balance constraints, and fixes the classifier intercept to zero. The continuous matrix problem is convex; its rounded discrete output has no asserted global-optimality or approximation guarantee. The formulation maintains an N-by-N label matrix and constraints indexed by triples, in addition to conic constraints. Kernel construction, solver tolerances and recovery policies affect cost and results. No unconditional linear-time or large-scale efficiency claim is made. All eight source pages, figures and tables were read. The clustering experiments use selected RBF widths, C=100 and majority labels per cluster. The semisupervised experiments are transductive: unlabeled input points participate in fitting while their labels are withheld. The finite comparisons do not establish universal superiority or inductive generalization. No historical code, benchmark or model training was executed.

### Definition, mechanism, limitations and mapping direction

evidence: supported. Targets: AIMech:SemisupervisedSemidefiniteMaximumMarginClustering.

The scoped mechanism, claim locators, concept kind and related task mapping are supported; the semisupervised identity-note comparison is tracked separately.

For N observations with fixed PSD kernel matrix K, the hard binary label matrix is M=y*y^T with y_i in {-1,+1}. Replace its integer entries by a symmetric PSD matrix with diagonal 1 and entries in [-1,1], retaining m_ik&gt;=m_ij+m_jk-1 and m_jk&gt;=-m_ij-m_ik-1 for every triple, and &#124;sum_i m_ij&#124;&lt;=ell for every column. The first two linear families preserve constraints satisfied by binary equivalence relations; PSD and these constraints do not force rank one after relaxation. In the integer case the column bound equals a bound on the difference in class counts; ell&lt;N excludes assigning everything to one class, subject to feasibility. Minimize over the feasible label matrix M the convex objective max_{0&lt;=lambda_i&lt;=C} [2*sum_i lambda_i-lambda^T*(K elementwise M)*lambda], with C&gt;0. The paper equivalent SDP minimizes delta over M, delta and nonnegative mu,nu, requiring the block matrix with upper-left K elementwise M, off-diagonal 1+mu-nu and bottom-right delta-2*C*sum_i nu_i to be PSD. This optimizes a relaxation for a fixed input kernel; it does not learn a combination of input kernels. The derivation fixes the classifier intercept to zero, which centering does not make identical to freely optimizing an intercept. The stated recovery is the soft vector sqrt(lambda_max(M))*v_max(M), not necessarily a binary partition or probabilities. A global SDP solution need not solve the discrete clustering problem. The source mentions randomized rounding without specifying a complete rounding policy or balance certificate. A feasible convex mixture of three balanced six-point label matrices can have a unique leading eigenvector whose signs split the data 4-to-2 despite zero column sums. These matrix constraints therefore do not alone guarantee count balance after sign rounding. Eigenvector sign, zero entries and repeated top eigenvalues require conventions. The record uses the displayed dual and SDP convention. The printed Equation3 norm-squared primal has slack coefficient C, but its displayed dual bound lambda&lt;=C corresponds to slack coefficient 2*C under alpha=2*lambda. With two zero-feature observations of opposite labels and C=1, the displayed primal optimum is 2 while the printed dual optimum is 4. Thus those displays should not be treated as numerically identical with the same C. A soft-margin regularized objective with nonzero slacks is also not simply the reciprocal squared geometric margin. For n_labeled observed binary labels, fix M_ij=y_i*y_j for every pair of labeled observations. For each unlabeled j also require sum_{i labeled} M_ij&gt;=2-n_labeled. In an integer label matrix the latter requires each unlabeled observation to share a class with at least one labeled observation. Add these linear constraints to the same semidefinite relaxation and margin objective. In the relaxed problem they constrain correlations; they do not directly assign a discrete class to each unlabeled datum. Observed label relations fix a labeled block of M, while leading-eigenvector recovery approximates M by rank one. The matrix constraints alone do not guarantee usable labeled signs in that vector: an exact six-point mixture satisfying the balance and observed-label constraints has a unique leading soft vector (0,0,1,1,-1,-1), even though the first two observed labels are opposite. For a zero input kernel this feasible M can also be an SDP optimum. Orientation by observed labels therefore needs nonzero informative recovered scores or a separate decoding policy. Inconsistent labels or balance requirements can make the constrained problem infeasible. Limitations: The method targets binary clustering with a supplied PSD kernel, penalty and feasible balance constraints, and fixes the classifier intercept to zero. The continuous matrix problem is convex; its rounded discrete output has no asserted global-optimality or approximation guarantee. The formulation maintains an N-by-N label matrix and constraints indexed by triples, in addition to conic constraints. Kernel construction, solver tolerances and recovery policies affect cost and results. No unconditional linear-time or large-scale efficiency claim is made. All eight source pages, figures and tables were read. The clustering experiments use selected RBF widths, C=100 and majority labels per cluster. The semisupervised experiments are transductive: unlabeled input points participate in fitting while their labels are withheld. The finite comparisons do not establish universal superiority or inductive generalization. No historical code, benchmark or model training was executed.

### Definition, mechanism, limitations and mapping direction

evidence: supported. Targets: AIMech:CuttingPlaneMulticlassMaximumMarginClustering.

The scoped mechanism, claim locators, concept kind and related task mapping are supported; the semisupervised identity-note comparison is tracked separately.

For supplied k classes and feature vectors x_i, use intercept-free scores g_ip=w_p^T*x_i and regularization beta&gt;0. Fit beta/2*sum_p &#124;&#124;w_p&#124;&#124;^2+mean_i xi_i with latent winner-versus-competitor margins. For a unique winner p_i and runner-up r_i, the optimal slack at fixed scores is max(0,1-(g_i,p_i-g_i,r_i)). Impose &#124;sum_i(g_ip-g_iq)&#124;&lt;=ell for every class pair; these aggregate score bounds do not impose class-count balance or ensure every class is occupied. Kernel-PCA coordinates are one suggested representation of a supplied kernel, not learned multiple-kernel weights. Aggregate slacks into a shared xi using masks c_i in {0,e_1,...,e_k}. Under a unique winner, the most violated constraint selects the runner-up one-hot vector when the top-runner gap is below 1 and the zero vector otherwise. Starting with an empty working set, fit its constraints, add the most violated mask and stop when violation is at most epsilon. Within a restricted fit, freeze previous winning-class indicators and solve the quadratic program with those indicators and the score-balance constraints; repeat under the stopping rule. The source uses a relative objective-change threshold of 0.01 percent in its experiments. The strict winner product makes every indicator zero at a tied maximum, yielding label 0 outside {1,...,k}; tie handling is not fully specified. Moreover, the source claimed convex term includes a winner-dependent indicator and need not be convex: for one observation, mask e_1 and scores (x,0), it is max(x,0)+I[x&gt;0]. At x=-0.2 and 0.2, a 3/4 mixture gives x=0.1 with value 1.1, exceeding the convex interpolation bound 0.9. These points have unique winners. Thus convexity of the frozen-indicator QP does not justify an unconditional global constrained concave-convex convergence or monotonicity claim for the printed nonconvex procedure. With correct constraint separation and a feasible restricted solution, the epsilon test permits feasibility for all masks after increasing the shared slack by epsilon. This does not itself bound misclassification error or the gap to a global optimum. The stated per-iteration scaling assumes a constant working-set size and supplied feature sparsity; the source iteration-count and linear-runtime theorems explicitly concern k=2, while multiclass scaling is empirical. Nonconvex restricted fitting, feature construction and stopping assumptions prevent an unconditional end-to-end linear-time or optimality guarantee. Limitations: This record describes the printed working-set and frozen-winner procedure with explicit tie and nonconvexity limits. No unmentioned tie repair, globally optimal restricted solver, global optimum or universal convergence guarantee is silently supplied. The class count, fixed kernel/features, regularization beta, score-balance bound and epsilon are supplied choices. Pairwise score balance is not class-count balance; the displayed formulation has no intercept. All eight paper pages, tables and figures were read. Experiments supply true class counts, use selected datasets and kernel tuning, and assess majority-label accuracy per cluster and Rand index. The tables include accuracy and runtime cases favoring comparators, so no universal superiority is asserted. No historical implementation or benchmark was reproduced.

### Three algorithm identities

consistency: supported. Targets: AIMech:SemidefiniteMaximumMarginClustering, AIMech:SemisupervisedSemidefiniteMaximumMarginClustering, AIMech:CuttingPlaneMulticlassMaximumMarginClustering.

Retain the unlabeled SDP, observed-label SDP and CPM3C procedures.

The two SDP procedures optimize a relaxed binary label matrix; the observed-label extension adds S1-S2 and changes the supervision regime. CPM3C directly updates multiclass feature-score parameters through working sets and frozen-winner QPs. A shared margin objective or a supplied kernel does not equate these complete algorithms, and the later multiple-kernel procedures learn additional kernel weights.

### Matrix constraints, convex objective and discrete recovery

consistency: supported. Targets: AIMech:SemidefiniteMaximumMarginClustering, AIMech:SemisupervisedSemidefiniteMaximumMarginClustering.

Retain explicit relaxation and rounding limits.

The hard matrix yyT satisfies L1-L2, PSD and diagonal1; L4 bounds class-count difference only in that hard interpretation. The relaxed convex objective is a pointwise maximum of affine functions of M. The three-cut example satisfies every retained inequality and zero column sums; Mv=(10/3)v, PSD and trace6 make10/3 uniquely largest because the remaining trace is8/3. Recovery gives(1,1/3,1/3,1/3,-1,-1), whose signs are4-to-2. The source unspecified randomized rounding is not silently replaced by a balanced decoder. Global continuous optimization does not certify global discrete optimization.

### Observed-label constraints versus recovered scores

consistency: supported. Targets: AIMech:SemisupervisedSemidefiniteMaximumMarginClustering.

Do not infer a usable oriented label vector from fixed matrix entries alone.

The average of two balanced cuts(1,-1,1,1,-1,-1) and(1,-1,-1,-1,1,1) satisfies L1-L2,L4,PSD and S1-S2 for the first two opposite labels. Its unique top eigenvalue4 exceeds remaining trace2 and gives soft labels(0,0,1,1,-1,-1). Thus the observed pair relation survives in M but both observed scores vanish in the leading vector. At zero K, the box-dual objective is2NC for every feasible M, so this can also be an optimum. Nonzero orientation information or a separate decoding policy is needed; infeasible constraints are a separate possibility.

### Displayed primal and dual normalization

consistency: supported. Targets: AIMech:SemidefiniteMaximumMarginClustering, AIMech:SemisupervisedSemidefiniteMaximumMarginClustering.

Use the later dual/SDP convention explicitly.

For primal norm squared plusC times slack, substitution alpha=2lambda gives box upper boundC/2. The printed dual instead has boundC and corresponds to twice the usual half-norm primal or norm squared plus2C times slack. With two zero-feature opposite labels,C1, the displayed primal has minimum2 and printed dual maximum4. This is a normalization mismatch in the source display, not an altered AIMech mechanism. Soft-margin penalized objectives are not literal inverse squared geometric margins in all slack-bearing cases.

### Strict winner indicators and claimed convexity

consistency: supported. Targets: AIMech:CuttingPlaneMulticlassMaximumMarginClustering.

Keep the exact tie and Jensen counterexamples visible.

Strict ties make every z zero and label0 invalid. Even away from ties, the claimed convex term for n1,c=e1,scores(x,0) is max(x,0)+I[x&gt;0]. At-.2,.2 and mixtureweight.75, its value1.1 at.1 exceeds the convex interpolation.9. The frozen-winner QP remains convex, but this does not certify global constrained-CCCP monotonicity or convergence for the printed winner-dependent function. The record describes the actual update without silently supplying a tie repair.

### Feasibility, cost and evaluation scope

consistency: supported. Targets: AIMech:SemidefiniteMaximumMarginClustering, AIMech:SemisupervisedSemidefiniteMaximumMarginClustering, AIMech:CuttingPlaneMulticlassMaximumMarginClustering.

Keep guarantees and empirical claims within their demonstrated scope.

CPM3C epsilon bounds omitted constraint violation when separation and restricted feasibility hold; it is not a classification-error or global-gap bound. The complexity results explicitly restrict iteration-count/linear-time claims to two classes and assume fixed working-set and feature conditions. The SDP has dense matrix and triple-indexed constraints. Source tables contain comparator-favoring results; majority-label scoring is not asserted one-to-one matching. The semisupervised tests are transductive and no historical implementation was executed.

### Identity absence and supervision-aware mappings

grounding: supported. Targets: AIMech:SemidefiniteMaximumMarginClustering, AIMech:SemisupervisedSemidefiniteMaximumMarginClustering, AIMech:CuttingPlaneMulticlassMaximumMarginClustering.

Use related tasks and preserve the ongoing frontier.

All442 AIO and498 previous native identities were checked; ignored-inclusive searches produced57 lines per checkout,41 distinct texts at114 locations, all inspected as references or multiple-kernel neighbors and rendered copies. Fifteen AIO annotated targets and21 contextual YAMLs support related UnsupervisedClustering for the two unlabeled methods and related Clustering for the partially labeled method. SemiSupervisedLLM is not a generic semisupervised-learning class. There remain425 pending cohorts; the review does not certify corpus-wide completeness.

### Comparison with other transductive solvers

identity: concern. Targets: AIMech:SemisupervisedSemidefiniteMaximumMarginClustering.

The identity-note comparison can imply that other transductive SVM solvers do not jointly use labeled and unlabeled inputs.

Section5 explicitly discusses other approaches that incorporate unlabeled data into SVM training. The wording should state the shared use of labeled and unlabeled data separately, then distinguish this variant by its observed-label matrix constraints. The record definition and mechanisms are otherwise appropriately scoped.

## Findings

### transductive-comparison-wording: Clarify the semisupervised record comparison with other transductive solvers

minor / open / confirmed; issue key: CultureBotAI-AIMech-SemidefiniteMargin-TransductiveComparisonWording.

The sentence beginning It jointly uses labeled and unlabeled training inputs attaches unlike to generic supervised SVM and all other transductive SVM solvers. Other transductive SVM methods also combine labeled and unlabeled inputs, as Section5 explains. Separate the shared supervision property from the distinguishing S1-S2 label-matrix constraints, and synchronize the current discovery entry. The definition, mathematical claims and mappings do not need changing.

## Recommended Actions And Acceptance Checks

### clarify-transductive-comparison

Correct the maintained identity note and current discovery entry, append actual edit history, refresh generated pages, validate and save a successor disposition.

- The text explicitly states that labeled and unlabeled inputs are used jointly without claiming this distinguishes every other transductive SVM.
- The distinguishing observed-label constraints are named; definition, mechanism, sources and mappings remain unchanged.
- The current discovery entry and generated page agree with the corrected YAML; curated/history/review and publication gates pass.

## Category Boundaries

- retain: AIMech:SemidefiniteMaximumMarginClustering, AIMech:SemisupervisedSemidefiniteMaximumMarginClustering, AIMech:CuttingPlaneMulticlassMaximumMarginClustering. The unlabeled SDP, labeled-matrix SDP extension and fixed-kernel multiclass cutting-plane procedure have distinct complete scopes and constraints. Related task mappings retain algorithm/task and supervision distinctions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T065516Z-margin-relaxation.json | supports | Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 498 prior native IDs, names and aliases; no normalized identity collision. Full searches of both checkouts include ignored and hidden files, returning 57 worktree and 57 main matched lines. All 41 distinct matched texts were inspected as multiple-kernel neighbors, bibliographic/query/frontier references or their rendered copies. Fifteen annotated AIO nodes and outgoing edges, fifteen generated YAMLs and six native neighbors were examined. Thirteen annotated targets, their generated records, all 442 class labels and 152 semantic rows reuse byte-verified prior readings; two additional annotated targets and one new semantic row were read (153 rows total). Absence is bounded to this pin and corpus.<br> |
| mapping | sources/aio/aio.json; Fifteen annotated CLASS nodes and outgoing edges;153 semantic rows and442 class labels with byte-verified prior readings | supports | Inspected fifteen annotated AIO CLASS nodes and outgoing edges, fifteen generated YAMLs and six native neighbors. Thirteen annotated targets, their generated records, all 442 class labels and 152 semantic rows reuse byte-verified prior readings; SupervisedClustering and SemiSupervisedLLM were additionally read in full. The additional semantic search yielded one new row (MultimodalFusionLLM through the substring grounding), read as unrelated, for 153 total rows. The unlabeled semidefinite and CPM3C procedures receive related UnsupervisedClustering task mappings. The semisupervised semidefinite procedure combines observed labels with unlabeled observations, so related Clustering represents the task without forcing either purely supervised or purely unsupervised identity. SemiSupervisedLLM denotes an LLM pretraining/fine-tuning model, not generic partial-label clustering. SupportVectorMachine is a supervised network in this pin; classification task, kernel layer, PCA projection and generic model terms do not represent these complete procedures. KernelPCA supplies possible coordinates; fixed-kernel variance methods, learned multiple-kernel margins, observed-label LMNN and PIC use different objectives and updates. No equivalence or upstream subclass assertion is made. Absence and mapping are bounded to the inspected pin and corpus.<br> |
| neighbors | research/discovery/20261012T065516Z-margin-relaxation.json; source_analysis.aio_mapping_inspection: fifteen generated and six native contextual YAMLs | supports | KernelPCA, KernelKMeans, LargeMarginNearestNeighbor, both multiple-kernel margin records and PowerIterationClustering distinguish coordinates, kernel variance, observed-label metric learning, learned kernel weights and iterative spectral clustering from the selected procedures. Context uses byte-verified complete earlier readings and receives no renewed scientific approval. |
| finite-boundaries | research/discovery/margin-relaxation-boundaries.py; Jensen violation, balanced-cut Gram mixtures, observed-label zeros and slack normalization | supports | Exact finite Jensen and Gram-mixture examples qualify the source convexity, balance and recovery claims. PSD follows from the construction; exact eigenvalue equations plus the remaining trace certify unique top eigenvectors. A two-observation zero-feature example checks slack-parameter normalization. These are mathematical examples, not historical solver execution. |
| semidefinitemaximummarginclustering-source | https://papers.neurips.cc/paper_files/paper/2004/file/6403675579f6114559c90de0014cd3d6-Paper.pdf; Section2, PDF pp.2-3, Equations1-3; curator dual-scaling derivation and zero-feature check; Section3, PDF p.5 after Equation7 and footnote2; curator exact Gram-mixture example; Section3, PDF pp.3-5, L1-L4 and Equations4-6; Section3, PDF pp.3-5, L1-L4, Equations4-7 and soft-assignment recovery; Sections2-3, PDF pp.3-5, Equations3-7 | supports | Maximum Margin Clustering. NIPS2004, Advances in Neural Information Processing Systems17, pp.1537-1544. All eight official proceedings PDF pages visually read; no visible printed page numbers, so locators use PDF pages. Original procedure claims and curator mathematical qualifications are distinguished. The semisupervised identity wording has one separately tracked concern. No historical benchmark was reproduced. |
| semisupervisedsemidefinitemaximummarginclustering-source | https://papers.neurips.cc/paper_files/paper/2004/file/6403675579f6114559c90de0014cd3d6-Paper.pdf; Section2, PDF pp.2-3, Equations1-3; curator dual-scaling derivation and zero-feature check; Section3, PDF p.5 after Equation7 and footnote2; curator exact Gram-mixture example; Section3, PDF pp.3-5, L1-L4 and Equations4-6; Section5, PDF p.6, S1-S2; Section5, PDF p.6, S1-S2 and Section3 recovery on PDF p.5; curator labeled-block Gram-mixture example; Section5, PDF p.6, S1-S2, together with the Section3 SDP on PDF pp.4-5; Sections2-3, PDF pp.3-5, Equations3-7 | supports | Maximum Margin Clustering. NIPS2004, Advances in Neural Information Processing Systems17, pp.1537-1544. All eight official proceedings PDF pages visually read; no visible printed page numbers, so locators use PDF pages. Original procedure claims and curator mathematical qualifications are distinguished. The semisupervised identity wording has one separately tracked concern. No historical benchmark was reproduced. |
| cuttingplanemulticlassmaximummarginclustering-source | https://icml.cc/Conferences/2008/papers/168.pdf; Sections2.1-2.3, PDF pp.2-4, Equations1-17; Sections2.1-2.4, PDF pp.2-5, Equations2-20 and Algorithms1-2; Sections2.2 and2.4, PDF pp.2-5, strict indicators and Equations18-20; curator exact Jensen check; Sections2.2-2.4, PDF pp.3-5, Equations11-20 and Algorithms1-2; Sections2.5-3, PDF pp.5-6, Theorems4-7; Section4.4, PDF pp.7-8 | supports | Efficient MultiClass Maximum Margin Clustering. ICML2008 proceedings pp.1248-1255. All eight official proceedings PDF pages visually read; no visible printed page numbers, so locators use PDF pages. Original procedure claims and curator mathematical qualifications are distinguished. The semisupervised identity wording has one separately tracked concern. No historical benchmark was reproduced. |

## Limits And Additional Notes

- Adversarial author self-review only; all three records remain DRAFT.
- One minor wording finding is open and must be resolved in a successor observation before the cohort is reported clean.
- All eight Xu2004 and eight CPM3C2008 primary PDF pages were visually read, including equations, pseudocode, figures, tables and references. Both official PDFs lack visible printed page numbers, so locators use PDF pages.
- The SDP label matrix relaxation preserves constraints satisfied by binary labels but does not impose rank one. A global continuous optimum is not a globally optimal discrete partition. A feasible mixture of balanced cuts has unique top eigenvalue10/3 and soft vector(1,1/3,1/3,1/3,-1,-1), whose signs give4-to-2 despite zero column sums.
- The semisupervised feasible example is the average of cuts(1,-1,1,1,-1,-1) and(1,-1,-1,-1,1,1). It fixes opposite observed labels at indices1,2 and satisfies S1-S2 and zero balance. Its unique top eigenvalue4 yields soft vector(0,0,1,1,-1,-1). PSD follows from the Gram mixture; in both examples the top eigenvalue exceeds the remaining trace, certifying it is uniquely largest. At K=0 every feasible M is optimal, so the decoding concern is not excluded by SDP optimality.
- Xu2004 Equation3 uses inconsistent same-C primal/dual normalization: setting alpha=2lambda gives lambda&lt;=C/2 for the displayed norm-squared plusCslack primal. The record uses the later dual/SDP convention explicitly. Two zero-feature opposite labels atC1 give primal2 versus printeddual4.
- For CPM3C the claimed convex winner term can be max(x,0)+I[x&gt;0]. Unique-winner points-.2,.2 with weight3/4 yield midpoint.1 and value1.1 above interpolation.9. Thus a convex frozen-indicator QP does not certify global CCCP behavior for the displayed nonconvex function. Strict ties also make all winning indicators zero. Epsilon feasibility is not a prediction-error or global-optimality bound.
- An exploratory NumPy probe failed before any calculation because NumPy was unavailable. The final examples use only the Python standard library and exact rational arithmetic. No historical optimizer, benchmark, model training, paid service or complete-paper redistribution occurred.
- Three additions bring the native collection to501;442 pinned AIO records remain unchanged. The frontier contains425 pending cohorts plus other unresolved dispositions. There is no saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T070104Z-margin-relaxation-initial
kind: category
repository: CultureBotAI/AIMech
title: Initial scientific self-review of semidefinite and cutting-plane margin methods
started_at: '2026-10-12T06:55:43Z'
finished_at: '2026-10-12T07:01:04Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent reread every field of all three records
    against sixteen visually read primary PDF pages, fifteen annotated AIO targets
    and21 contextual YAMLs, reusing unchanged context only after byte verification.
    Seven mathematical and mapping boundary assessments plus a wording assessment
    challenge the records. This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The three procedure identities, mathematical qualifications and related task
  mappings are supported. One minor identity-note comparison needs correction because
  it can mischaracterize other transductive solvers.
source:
  git_revision: d738cb15f478a6affbae23e06cf2d0734124b2c9
  state: working_tree
  inputs:
  - path: data/aio/BinaryClassification.yaml
    sha256: 4c710e70fe7e71227f0c6aa55162a3683f04ebbe6f5a4601bd4c0398329f1481
    role: context
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/DimensionalityReduction.yaml
    sha256: 99eb0714b362a98a9e704e5ef2ac370cb7a900fbe97da43de790c3ec67ed812e
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
  - path: data/aio/MulticlassClassification.yaml
    sha256: dcf165047485763fd91782b9a9ba43202d58f00fd33b8545893a5eae327de171
    role: context
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
    role: context
  - path: data/aio/RepresentationLearning.yaml
    sha256: bc7af756440437f60210019e17ad1e2dd15cd1c7cbfbc96312520934b7a5c7ca
    role: context
  - path: data/aio/SemiSupervisedLLM.yaml
    sha256: 4ee601313a6cdaa7134207fa384702f0e92d2b93906e379c2b0ef5cfe6eef9ee
    role: context
  - path: data/aio/SupervisedClustering.yaml
    sha256: d8d9f49b7b975d8217fe675e9c670fd0246af4abcdebce2483fa773a441ee83e
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
  - path: data/curated/BinaryMultipleKernelMaximumMarginClustering.yaml
    sha256: 467a5417491bebff1a14277e7809679e8e97625ee1a4374f499f1b062ce3d3d4
    role: context
  - path: data/curated/CuttingPlaneMulticlassMaximumMarginClustering.yaml
    sha256: 6b6f8483688ed54da637fee2929f06723fc2f846a6f1fbbdda46c3ae8ca1ec98
    role: target
  - path: data/curated/KernelKMeans.yaml
    sha256: a5fe0bf0d883e32d689c79c232d8a8093b0ab29a56df616a5ef367e931aca84a
    role: context
  - path: data/curated/KernelPCA.yaml
    sha256: a93227a6b2d6b2b89b679b8f7f9ddd5054741d1c11f9510490d82a3e691a1cab
    role: context
  - path: data/curated/LargeMarginNearestNeighbor.yaml
    sha256: f17ce62722a0b1aaf9629bbb196e67249c1853edd31d220bfff76019d3e3295e
    role: context
  - path: data/curated/MulticlassMultipleKernelMaximumMarginClustering.yaml
    sha256: bfdea2b3468bc8b9d88d79605d016027ed727d7aac096f2d2130294fc0b09d96
    role: context
  - path: data/curated/PowerIterationClustering.yaml
    sha256: ca81d60eb87c027126a3372950d40f50d0df8391b1075697e0ab5ffabf3dfa0f
    role: context
  - path: data/curated/SemidefiniteMaximumMarginClustering.yaml
    sha256: 9cfe6597d65d6a9dae4040f56bade8cba946a4b09c82c8f0b5adbec8b66a59dc
    role: target
  - path: data/curated/SemisupervisedSemidefiniteMaximumMarginClustering.yaml
    sha256: b8c562e10946007631dd75003f19a7f7c11c0021acf3deaf9a34f6d09b012812
    role: target
  - path: research/discovery/20261012T065516Z-margin-relaxation.json
    sha256: b7194eb7e2c1a4a55664e32f8aae0798f45337284131de14e9aa4ab5f8fb8cbb
    role: context
  - path: research/discovery/margin-relaxation-boundaries.py
    sha256: e11ea2325cc74b26fd704068f90fdd7e2392300a80bce6d63e1f52c81fb65128
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
- target_id: AIMech:SemidefiniteMaximumMarginClustering
  path: data/curated/SemidefiniteMaximumMarginClustering.yaml
  label: Semidefinite Maximum Margin Clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SemidefiniteMaximumMarginClustering.yaml
    role: maintained
- target_id: AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  path: data/curated/SemisupervisedSemidefiniteMaximumMarginClustering.yaml
  label: Semisupervised Semidefinite Maximum Margin Clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SemisupervisedSemidefiniteMaximumMarginClustering.yaml
    role: maintained
- target_id: AIMech:CuttingPlaneMulticlassMaximumMarginClustering
  path: data/curated/CuttingPlaneMulticlassMaximumMarginClustering.yaml
  label: Cutting Plane Multiclass Maximum Margin Clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CuttingPlaneMulticlassMaximumMarginClustering.yaml
    role: maintained
scope:
  description: All fields of the three selected margin procedures.
  selection: Exact maintained IDs SemidefiniteMaximumMarginClustering, SemisupervisedSemidefiniteMaximumMarginClustering
    and CuttingPlaneMulticlassMaximumMarginClustering; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:SemidefiniteMaximumMarginClustering
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  - AIMech:CuttingPlaneMulticlassMaximumMarginClustering
  exclusions:
  - target: Contextual generated and maintained records
    reason: Identity/mapping context without renewed scientific approval or mutation.
  - target: Historical implementation and benchmark reproduction
    reason: Exact finite mathematical examples were checked; no historical solver
      or benchmark was executed.
  - target: Generated website
    reason: Regenerated and checked for freshness, not a separate scientific or visual-design
      target.
  - target: Remaining discovery frontier
    reason: 425 pending cohorts and other unresolved dispositions remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:SemidefiniteMaximumMarginClustering
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  - AIMech:CuttingPlaneMulticlassMaximumMarginClustering
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 162.68s (0:02:42)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 501 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 150 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 146,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:SemidefiniteMaximumMarginClustering
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  - AIMech:CuttingPlaneMulticlassMaximumMarginClustering
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
  - AIMech:SemidefiniteMaximumMarginClustering
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  - AIMech:CuttingPlaneMulticlassMaximumMarginClustering
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
  - AIMech:SemidefiniteMaximumMarginClustering
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  - AIMech:CuttingPlaneMulticlassMaximumMarginClustering
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited0 with no output.
- check_id: finite-arithmetic
  name: Margin-relaxation boundaries
  command: python3 research/discovery/margin-relaxation-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SemidefiniteMaximumMarginClustering
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  - AIMech:CuttingPlaneMulticlassMaximumMarginClustering
  exit_code: 0
  expected_exit_code: 0
  summary: '{"winner_convexity": {"left": -0.2, "right": 0.2, "mix": 0.1, "value_at_mix":
    1.1, "convex_upper_bound": 0.9}, "balanced_relaxation": {"cuts": [[1, 1, 1, -1,
    -1, -1], [1, 1, -1, 1, -1, -1], [1, -1, 1, 1, -1, -1]], "matrix": [[1.0, 0.3333333333333333,
    0.3333333333333333, 0.3333333333333333, -1.0, -1.0], [0.3333333333333333, 1.0,
    -0.3333333333333333, -0.3333333333333333, -0.3333333333333333, -0.3333333333333333],
    [0.3333333333333333, -0.3333333333333333, 1.0, -0.3333333333333333, -0.3333333333333333,
    -0.3333333333333333], [0.3333333333333333, -0.3333333333333333, -0.3333333333333333,
    1.0, -0.3333333333333333, -0.3333333333333333], [-1.0, -0.3333333333333333, -0.3333333333333333,
    -0.3333333333333333, 1.0, 1.0], [-1.0, -0.3333333333333333, -0.3333333333333333,
    -0.3333333333333333, 1.0, 1.0]], "largest_eigenvalue": 3.3333333333333335, "soft_labels":
    [1.0, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, -1.0, -1.0],
    "rounded_labels": [1, 1, 1, 1, -1, -1], "rounded_label_sum": 2}, "semisupervised_decoding":
    {"cuts": [[1, -1, 1, 1, -1, -1], [1, -1, -1, -1, 1, 1]], "largest_eigenvalue":
    4, "soft_labels": [0, 0, 1, 1, -1, -1], "fixed_labeled_relation": -1, "interpretation":
    "Feasible relaxed constraints, including S1-S2, permit leading-eigenvector zeros
    on both observed labels. With zero kernel, every feasible M is also optimal for
    the relaxed dual."}, "slack_normalization": {"displayed_primal_C1": 2, "printed_dual_C1":
    4, "interpretation": "For norm-squared primal with slack coefficient C, alpha=2*lambda
    yields lambda<=C/2. The printed dual bound C corresponds to slack coefficient
    2C."}, "interpretation": "Exact finite examples plus PSD Gram and trace arguments;
    no solver or benchmark reproduction."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T065516Z-margin-relaxation.json
  accessed_at: '2026-10-12T06:55:43Z'
  support: supports
  summary: 'Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 498
    prior native IDs, names and aliases; no normalized identity collision. Full searches
    of both checkouts include ignored and hidden files, returning 57 worktree and
    57 main matched lines. All 41 distinct matched texts were inspected as multiple-kernel
    neighbors, bibliographic/query/frontier references or their rendered copies. Fifteen
    annotated AIO nodes and outgoing edges, fifteen generated YAMLs and six native
    neighbors were examined. Thirteen annotated targets, their generated records,
    all 442 class labels and 152 semantic rows reuse byte-verified prior readings;
    two additional annotated targets and one new semantic row were read (153 rows
    total). Absence is bounded to this pin and corpus.

    '
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Fifteen annotated CLASS nodes and outgoing edges;153 semantic rows and442
    class labels with byte-verified prior readings
  accessed_at: '2026-10-12T06:55:43Z'
  support: supports
  summary: 'Inspected fifteen annotated AIO CLASS nodes and outgoing edges, fifteen
    generated YAMLs and six native neighbors. Thirteen annotated targets, their generated
    records, all 442 class labels and 152 semantic rows reuse byte-verified prior
    readings; SupervisedClustering and SemiSupervisedLLM were additionally read in
    full. The additional semantic search yielded one new row (MultimodalFusionLLM
    through the substring grounding), read as unrelated, for 153 total rows. The unlabeled
    semidefinite and CPM3C procedures receive related UnsupervisedClustering task
    mappings. The semisupervised semidefinite procedure combines observed labels with
    unlabeled observations, so related Clustering represents the task without forcing
    either purely supervised or purely unsupervised identity. SemiSupervisedLLM denotes
    an LLM pretraining/fine-tuning model, not generic partial-label clustering. SupportVectorMachine
    is a supervised network in this pin; classification task, kernel layer, PCA projection
    and generic model terms do not represent these complete procedures. KernelPCA
    supplies possible coordinates; fixed-kernel variance methods, learned multiple-kernel
    margins, observed-label LMNN and PIC use different objectives and updates. No
    equivalence or upstream subclass assertion is made. Absence and mapping are bounded
    to the inspected pin and corpus.

    '
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261012T065516Z-margin-relaxation.json
  locator: 'source_analysis.aio_mapping_inspection: fifteen generated and six native
    contextual YAMLs'
  accessed_at: '2026-10-12T06:55:43Z'
  support: supports
  summary: KernelPCA, KernelKMeans, LargeMarginNearestNeighbor, both multiple-kernel
    margin records and PowerIterationClustering distinguish coordinates, kernel variance,
    observed-label metric learning, learned kernel weights and iterative spectral
    clustering from the selected procedures. Context uses byte-verified complete earlier
    readings and receives no renewed scientific approval.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/margin-relaxation-boundaries.py
  locator: Jensen violation, balanced-cut Gram mixtures, observed-label zeros and
    slack normalization
  accessed_at: '2026-10-12T06:55:43Z'
  snapshot_sha256: e11ea2325cc74b26fd704068f90fdd7e2392300a80bce6d63e1f52c81fb65128
  support: supports
  summary: Exact finite Jensen and Gram-mixture examples qualify the source convexity,
    balance and recovery claims. PSD follows from the construction; exact eigenvalue
    equations plus the remaining trace certify unique top eigenvectors. A two-observation
    zero-feature example checks slack-parameter normalization. These are mathematical
    examples, not historical solver execution.
- evidence_id: semidefinitemaximummarginclustering-source
  kind: primary_source
  reference: https://papers.neurips.cc/paper_files/paper/2004/file/6403675579f6114559c90de0014cd3d6-Paper.pdf
  locator: Section2, PDF pp.2-3, Equations1-3; curator dual-scaling derivation and
    zero-feature check; Section3, PDF p.5 after Equation7 and footnote2; curator exact
    Gram-mixture example; Section3, PDF pp.3-5, L1-L4 and Equations4-6; Section3,
    PDF pp.3-5, L1-L4, Equations4-7 and soft-assignment recovery; Sections2-3, PDF
    pp.3-5, Equations3-7
  accessed_at: '2026-10-12T06:41:58Z'
  snapshot_sha256: 015d9811484d2ef0c28be5840c68084d45771cbdaafe4043079014ff1f8cfbac
  support: supports
  summary: Maximum Margin Clustering. NIPS2004, Advances in Neural Information Processing
    Systems17, pp.1537-1544. All eight official proceedings PDF pages visually read;
    no visible printed page numbers, so locators use PDF pages. Original procedure
    claims and curator mathematical qualifications are distinguished. The semisupervised
    identity wording has one separately tracked concern. No historical benchmark was
    reproduced.
- evidence_id: semisupervisedsemidefinitemaximummarginclustering-source
  kind: primary_source
  reference: https://papers.neurips.cc/paper_files/paper/2004/file/6403675579f6114559c90de0014cd3d6-Paper.pdf
  locator: Section2, PDF pp.2-3, Equations1-3; curator dual-scaling derivation and
    zero-feature check; Section3, PDF p.5 after Equation7 and footnote2; curator exact
    Gram-mixture example; Section3, PDF pp.3-5, L1-L4 and Equations4-6; Section5,
    PDF p.6, S1-S2; Section5, PDF p.6, S1-S2 and Section3 recovery on PDF p.5; curator
    labeled-block Gram-mixture example; Section5, PDF p.6, S1-S2, together with the
    Section3 SDP on PDF pp.4-5; Sections2-3, PDF pp.3-5, Equations3-7
  accessed_at: '2026-10-12T06:41:58Z'
  snapshot_sha256: 015d9811484d2ef0c28be5840c68084d45771cbdaafe4043079014ff1f8cfbac
  support: supports
  summary: Maximum Margin Clustering. NIPS2004, Advances in Neural Information Processing
    Systems17, pp.1537-1544. All eight official proceedings PDF pages visually read;
    no visible printed page numbers, so locators use PDF pages. Original procedure
    claims and curator mathematical qualifications are distinguished. The semisupervised
    identity wording has one separately tracked concern. No historical benchmark was
    reproduced.
- evidence_id: cuttingplanemulticlassmaximummarginclustering-source
  kind: primary_source
  reference: https://icml.cc/Conferences/2008/papers/168.pdf
  locator: Sections2.1-2.3, PDF pp.2-4, Equations1-17; Sections2.1-2.4, PDF pp.2-5,
    Equations2-20 and Algorithms1-2; Sections2.2 and2.4, PDF pp.2-5, strict indicators
    and Equations18-20; curator exact Jensen check; Sections2.2-2.4, PDF pp.3-5, Equations11-20
    and Algorithms1-2; Sections2.5-3, PDF pp.5-6, Theorems4-7; Section4.4, PDF pp.7-8
  accessed_at: '2026-10-12T06:41:55Z'
  snapshot_sha256: db9db473e6a00cb0a68c651ac7c9f074c41ef4f16f26d564e3839a2ba9cb2b7a
  support: supports
  summary: Efficient MultiClass Maximum Margin Clustering. ICML2008 proceedings pp.1248-1255.
    All eight official proceedings PDF pages visually read; no visible printed page
    numbers, so locators use PDF pages. Original procedure claims and curator mathematical
    qualifications are distinguished. The semisupervised identity wording has one
    separately tracked concern. No historical benchmark was reproduced.
assessments:
- assessment_id: semidefinitemaximummarginclustering
  area: evidence
  topic: Definition, mechanism, limitations and mapping direction
  outcome: supported
  target_ids:
  - AIMech:SemidefiniteMaximumMarginClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - semidefinitemaximummarginclustering-source
  summary: The scoped mechanism, claim locators, concept kind and related task mapping
    are supported; the semisupervised identity-note comparison is tracked separately.
  details: 'For N observations with fixed PSD kernel matrix K, the hard binary label
    matrix is M=y*y^T with y_i in {-1,+1}. Replace its integer entries by a symmetric
    PSD matrix with diagonal 1 and entries in [-1,1], retaining m_ik>=m_ij+m_jk-1
    and m_jk>=-m_ij-m_ik-1 for every triple, and |sum_i m_ij|<=ell for every column.
    The first two linear families preserve constraints satisfied by binary equivalence
    relations; PSD and these constraints do not force rank one after relaxation. In
    the integer case the column bound equals a bound on the difference in class counts;
    ell<N excludes assigning everything to one class, subject to feasibility. Minimize
    over the feasible label matrix M the convex objective max_{0<=lambda_i<=C} [2*sum_i
    lambda_i-lambda^T*(K elementwise M)*lambda], with C>0. The paper equivalent SDP
    minimizes delta over M, delta and nonnegative mu,nu, requiring the block matrix
    with upper-left K elementwise M, off-diagonal 1+mu-nu and bottom-right delta-2*C*sum_i
    nu_i to be PSD. This optimizes a relaxation for a fixed input kernel; it does
    not learn a combination of input kernels. The derivation fixes the classifier
    intercept to zero, which centering does not make identical to freely optimizing
    an intercept. The stated recovery is the soft vector sqrt(lambda_max(M))*v_max(M),
    not necessarily a binary partition or probabilities. A global SDP solution need
    not solve the discrete clustering problem. The source mentions randomized rounding
    without specifying a complete rounding policy or balance certificate. A feasible
    convex mixture of three balanced six-point label matrices can have a unique leading
    eigenvector whose signs split the data 4-to-2 despite zero column sums. These
    matrix constraints therefore do not alone guarantee count balance after sign rounding.
    Eigenvector sign, zero entries and repeated top eigenvalues require conventions.
    The record uses the displayed dual and SDP convention. The printed Equation3 norm-squared
    primal has slack coefficient C, but its displayed dual bound lambda<=C corresponds
    to slack coefficient 2*C under alpha=2*lambda. With two zero-feature observations
    of opposite labels and C=1, the displayed primal optimum is 2 while the printed
    dual optimum is 4. Thus those displays should not be treated as numerically identical
    with the same C. A soft-margin regularized objective with nonzero slacks is also
    not simply the reciprocal squared geometric margin. Limitations: The method targets
    binary clustering with a supplied PSD kernel, penalty and feasible balance constraints,
    and fixes the classifier intercept to zero. The continuous matrix problem is convex;
    its rounded discrete output has no asserted global-optimality or approximation
    guarantee. The formulation maintains an N-by-N label matrix and constraints indexed
    by triples, in addition to conic constraints. Kernel construction, solver tolerances
    and recovery policies affect cost and results. No unconditional linear-time or
    large-scale efficiency claim is made. All eight source pages, figures and tables
    were read. The clustering experiments use selected RBF widths, C=100 and majority
    labels per cluster. The semisupervised experiments are transductive: unlabeled
    input points participate in fitting while their labels are withheld. The finite
    comparisons do not establish universal superiority or inductive generalization.
    No historical code, benchmark or model training was executed.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A complete clustering or partially labeled learning procedure, not
      a trained instance.
    evidence_ids:
    - semidefinitemaximummarginclustering-source
  - name: aio-assessment
    value: related_match
    definition: 'Inspected fifteen annotated AIO CLASS nodes and outgoing edges, fifteen
      generated YAMLs and six native neighbors. Thirteen annotated targets, their
      generated records, all 442 class labels and 152 semantic rows reuse byte-verified
      prior readings; SupervisedClustering and SemiSupervisedLLM were additionally
      read in full. The additional semantic search yielded one new row (MultimodalFusionLLM
      through the substring grounding), read as unrelated, for 153 total rows. The
      unlabeled semidefinite and CPM3C procedures receive related UnsupervisedClustering
      task mappings. The semisupervised semidefinite procedure combines observed labels
      with unlabeled observations, so related Clustering represents the task without
      forcing either purely supervised or purely unsupervised identity. SemiSupervisedLLM
      denotes an LLM pretraining/fine-tuning model, not generic partial-label clustering.
      SupportVectorMachine is a supervised network in this pin; classification task,
      kernel layer, PCA projection and generic model terms do not represent these
      complete procedures. KernelPCA supplies possible coordinates; fixed-kernel variance
      methods, learned multiple-kernel margins, observed-label LMNN and PIC use different
      objectives and updates. No equivalence or upstream subclass assertion is made.
      Absence and mapping are bounded to the inspected pin and corpus.

      '
    evidence_ids:
    - mapping
- assessment_id: semisupervisedsemidefinitemaximummarginclustering
  area: evidence
  topic: Definition, mechanism, limitations and mapping direction
  outcome: supported
  target_ids:
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - semisupervisedsemidefinitemaximummarginclustering-source
  summary: The scoped mechanism, claim locators, concept kind and related task mapping
    are supported; the semisupervised identity-note comparison is tracked separately.
  details: 'For N observations with fixed PSD kernel matrix K, the hard binary label
    matrix is M=y*y^T with y_i in {-1,+1}. Replace its integer entries by a symmetric
    PSD matrix with diagonal 1 and entries in [-1,1], retaining m_ik>=m_ij+m_jk-1
    and m_jk>=-m_ij-m_ik-1 for every triple, and |sum_i m_ij|<=ell for every column.
    The first two linear families preserve constraints satisfied by binary equivalence
    relations; PSD and these constraints do not force rank one after relaxation. In
    the integer case the column bound equals a bound on the difference in class counts;
    ell<N excludes assigning everything to one class, subject to feasibility. Minimize
    over the feasible label matrix M the convex objective max_{0<=lambda_i<=C} [2*sum_i
    lambda_i-lambda^T*(K elementwise M)*lambda], with C>0. The paper equivalent SDP
    minimizes delta over M, delta and nonnegative mu,nu, requiring the block matrix
    with upper-left K elementwise M, off-diagonal 1+mu-nu and bottom-right delta-2*C*sum_i
    nu_i to be PSD. This optimizes a relaxation for a fixed input kernel; it does
    not learn a combination of input kernels. The derivation fixes the classifier
    intercept to zero, which centering does not make identical to freely optimizing
    an intercept. The stated recovery is the soft vector sqrt(lambda_max(M))*v_max(M),
    not necessarily a binary partition or probabilities. A global SDP solution need
    not solve the discrete clustering problem. The source mentions randomized rounding
    without specifying a complete rounding policy or balance certificate. A feasible
    convex mixture of three balanced six-point label matrices can have a unique leading
    eigenvector whose signs split the data 4-to-2 despite zero column sums. These
    matrix constraints therefore do not alone guarantee count balance after sign rounding.
    Eigenvector sign, zero entries and repeated top eigenvalues require conventions.
    The record uses the displayed dual and SDP convention. The printed Equation3 norm-squared
    primal has slack coefficient C, but its displayed dual bound lambda<=C corresponds
    to slack coefficient 2*C under alpha=2*lambda. With two zero-feature observations
    of opposite labels and C=1, the displayed primal optimum is 2 while the printed
    dual optimum is 4. Thus those displays should not be treated as numerically identical
    with the same C. A soft-margin regularized objective with nonzero slacks is also
    not simply the reciprocal squared geometric margin. For n_labeled observed binary
    labels, fix M_ij=y_i*y_j for every pair of labeled observations. For each unlabeled
    j also require sum_{i labeled} M_ij>=2-n_labeled. In an integer label matrix the
    latter requires each unlabeled observation to share a class with at least one
    labeled observation. Add these linear constraints to the same semidefinite relaxation
    and margin objective. In the relaxed problem they constrain correlations; they
    do not directly assign a discrete class to each unlabeled datum. Observed label
    relations fix a labeled block of M, while leading-eigenvector recovery approximates
    M by rank one. The matrix constraints alone do not guarantee usable labeled signs
    in that vector: an exact six-point mixture satisfying the balance and observed-label
    constraints has a unique leading soft vector (0,0,1,1,-1,-1), even though the
    first two observed labels are opposite. For a zero input kernel this feasible
    M can also be an SDP optimum. Orientation by observed labels therefore needs nonzero
    informative recovered scores or a separate decoding policy. Inconsistent labels
    or balance requirements can make the constrained problem infeasible. Limitations:
    The method targets binary clustering with a supplied PSD kernel, penalty and feasible
    balance constraints, and fixes the classifier intercept to zero. The continuous
    matrix problem is convex; its rounded discrete output has no asserted global-optimality
    or approximation guarantee. The formulation maintains an N-by-N label matrix and
    constraints indexed by triples, in addition to conic constraints. Kernel construction,
    solver tolerances and recovery policies affect cost and results. No unconditional
    linear-time or large-scale efficiency claim is made. All eight source pages, figures
    and tables were read. The clustering experiments use selected RBF widths, C=100
    and majority labels per cluster. The semisupervised experiments are transductive:
    unlabeled input points participate in fitting while their labels are withheld.
    The finite comparisons do not establish universal superiority or inductive generalization.
    No historical code, benchmark or model training was executed.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A complete clustering or partially labeled learning procedure, not
      a trained instance.
    evidence_ids:
    - semisupervisedsemidefinitemaximummarginclustering-source
  - name: aio-assessment
    value: related_match
    definition: 'Inspected fifteen annotated AIO CLASS nodes and outgoing edges, fifteen
      generated YAMLs and six native neighbors. Thirteen annotated targets, their
      generated records, all 442 class labels and 152 semantic rows reuse byte-verified
      prior readings; SupervisedClustering and SemiSupervisedLLM were additionally
      read in full. The additional semantic search yielded one new row (MultimodalFusionLLM
      through the substring grounding), read as unrelated, for 153 total rows. The
      unlabeled semidefinite and CPM3C procedures receive related UnsupervisedClustering
      task mappings. The semisupervised semidefinite procedure combines observed labels
      with unlabeled observations, so related Clustering represents the task without
      forcing either purely supervised or purely unsupervised identity. SemiSupervisedLLM
      denotes an LLM pretraining/fine-tuning model, not generic partial-label clustering.
      SupportVectorMachine is a supervised network in this pin; classification task,
      kernel layer, PCA projection and generic model terms do not represent these
      complete procedures. KernelPCA supplies possible coordinates; fixed-kernel variance
      methods, learned multiple-kernel margins, observed-label LMNN and PIC use different
      objectives and updates. No equivalence or upstream subclass assertion is made.
      Absence and mapping are bounded to the inspected pin and corpus.

      '
    evidence_ids:
    - mapping
- assessment_id: cuttingplanemulticlassmaximummarginclustering
  area: evidence
  topic: Definition, mechanism, limitations and mapping direction
  outcome: supported
  target_ids:
  - AIMech:CuttingPlaneMulticlassMaximumMarginClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - cuttingplanemulticlassmaximummarginclustering-source
  summary: The scoped mechanism, claim locators, concept kind and related task mapping
    are supported; the semisupervised identity-note comparison is tracked separately.
  details: 'For supplied k classes and feature vectors x_i, use intercept-free scores
    g_ip=w_p^T*x_i and regularization beta>0. Fit beta/2*sum_p ||w_p||^2+mean_i xi_i
    with latent winner-versus-competitor margins. For a unique winner p_i and runner-up
    r_i, the optimal slack at fixed scores is max(0,1-(g_i,p_i-g_i,r_i)). Impose |sum_i(g_ip-g_iq)|<=ell
    for every class pair; these aggregate score bounds do not impose class-count balance
    or ensure every class is occupied. Kernel-PCA coordinates are one suggested representation
    of a supplied kernel, not learned multiple-kernel weights. Aggregate slacks into
    a shared xi using masks c_i in {0,e_1,...,e_k}. Under a unique winner, the most
    violated constraint selects the runner-up one-hot vector when the top-runner gap
    is below 1 and the zero vector otherwise. Starting with an empty working set,
    fit its constraints, add the most violated mask and stop when violation is at
    most epsilon. Within a restricted fit, freeze previous winning-class indicators
    and solve the quadratic program with those indicators and the score-balance constraints;
    repeat under the stopping rule. The source uses a relative objective-change threshold
    of 0.01 percent in its experiments. The strict winner product makes every indicator
    zero at a tied maximum, yielding label 0 outside {1,...,k}; tie handling is not
    fully specified. Moreover, the source claimed convex term includes a winner-dependent
    indicator and need not be convex: for one observation, mask e_1 and scores (x,0),
    it is max(x,0)+I[x>0]. At x=-0.2 and 0.2, a 3/4 mixture gives x=0.1 with value
    1.1, exceeding the convex interpolation bound 0.9. These points have unique winners.
    Thus convexity of the frozen-indicator QP does not justify an unconditional global
    constrained concave-convex convergence or monotonicity claim for the printed nonconvex
    procedure. With correct constraint separation and a feasible restricted solution,
    the epsilon test permits feasibility for all masks after increasing the shared
    slack by epsilon. This does not itself bound misclassification error or the gap
    to a global optimum. The stated per-iteration scaling assumes a constant working-set
    size and supplied feature sparsity; the source iteration-count and linear-runtime
    theorems explicitly concern k=2, while multiclass scaling is empirical. Nonconvex
    restricted fitting, feature construction and stopping assumptions prevent an unconditional
    end-to-end linear-time or optimality guarantee. Limitations: This record describes
    the printed working-set and frozen-winner procedure with explicit tie and nonconvexity
    limits. No unmentioned tie repair, globally optimal restricted solver, global
    optimum or universal convergence guarantee is silently supplied. The class count,
    fixed kernel/features, regularization beta, score-balance bound and epsilon are
    supplied choices. Pairwise score balance is not class-count balance; the displayed
    formulation has no intercept. All eight paper pages, tables and figures were read.
    Experiments supply true class counts, use selected datasets and kernel tuning,
    and assess majority-label accuracy per cluster and Rand index. The tables include
    accuracy and runtime cases favoring comparators, so no universal superiority is
    asserted. No historical implementation or benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A complete clustering or partially labeled learning procedure, not
      a trained instance.
    evidence_ids:
    - cuttingplanemulticlassmaximummarginclustering-source
  - name: aio-assessment
    value: related_match
    definition: 'Inspected fifteen annotated AIO CLASS nodes and outgoing edges, fifteen
      generated YAMLs and six native neighbors. Thirteen annotated targets, their
      generated records, all 442 class labels and 152 semantic rows reuse byte-verified
      prior readings; SupervisedClustering and SemiSupervisedLLM were additionally
      read in full. The additional semantic search yielded one new row (MultimodalFusionLLM
      through the substring grounding), read as unrelated, for 153 total rows. The
      unlabeled semidefinite and CPM3C procedures receive related UnsupervisedClustering
      task mappings. The semisupervised semidefinite procedure combines observed labels
      with unlabeled observations, so related Clustering represents the task without
      forcing either purely supervised or purely unsupervised identity. SemiSupervisedLLM
      denotes an LLM pretraining/fine-tuning model, not generic partial-label clustering.
      SupportVectorMachine is a supervised network in this pin; classification task,
      kernel layer, PCA projection and generic model terms do not represent these
      complete procedures. KernelPCA supplies possible coordinates; fixed-kernel variance
      methods, learned multiple-kernel margins, observed-label LMNN and PIC use different
      objectives and updates. No equivalence or upstream subclass assertion is made.
      Absence and mapping are bounded to the inspected pin and corpus.

      '
    evidence_ids:
    - mapping
- assessment_id: three-procedures
  area: consistency
  topic: Three algorithm identities
  outcome: supported
  target_ids:
  - AIMech:SemidefiniteMaximumMarginClustering
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  - AIMech:CuttingPlaneMulticlassMaximumMarginClustering
  evidence_ids:
  - identity
  - neighbors
  - semidefinitemaximummarginclustering-source
  - semisupervisedsemidefinitemaximummarginclustering-source
  - cuttingplanemulticlassmaximummarginclustering-source
  summary: Retain the unlabeled SDP, observed-label SDP and CPM3C procedures.
  details: The two SDP procedures optimize a relaxed binary label matrix; the observed-label
    extension adds S1-S2 and changes the supervision regime. CPM3C directly updates
    multiclass feature-score parameters through working sets and frozen-winner QPs.
    A shared margin objective or a supplied kernel does not equate these complete
    algorithms, and the later multiple-kernel procedures learn additional kernel weights.
- assessment_id: relaxation-and-recovery
  area: consistency
  topic: Matrix constraints, convex objective and discrete recovery
  outcome: supported
  target_ids:
  - AIMech:SemidefiniteMaximumMarginClustering
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  evidence_ids:
  - semidefinitemaximummarginclustering-source
  - semisupervisedsemidefinitemaximummarginclustering-source
  - finite-boundaries
  summary: Retain explicit relaxation and rounding limits.
  details: The hard matrix yyT satisfies L1-L2, PSD and diagonal1; L4 bounds class-count
    difference only in that hard interpretation. The relaxed convex objective is a
    pointwise maximum of affine functions of M. The three-cut example satisfies every
    retained inequality and zero column sums; Mv=(10/3)v, PSD and trace6 make10/3
    uniquely largest because the remaining trace is8/3. Recovery gives(1,1/3,1/3,1/3,-1,-1),
    whose signs are4-to-2. The source unspecified randomized rounding is not silently
    replaced by a balanced decoder. Global continuous optimization does not certify
    global discrete optimization.
- assessment_id: known-label-recovery
  area: consistency
  topic: Observed-label constraints versus recovered scores
  outcome: supported
  target_ids:
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  evidence_ids:
  - semisupervisedsemidefinitemaximummarginclustering-source
  - finite-boundaries
  summary: Do not infer a usable oriented label vector from fixed matrix entries alone.
  details: The average of two balanced cuts(1,-1,1,1,-1,-1) and(1,-1,-1,-1,1,1) satisfies
    L1-L2,L4,PSD and S1-S2 for the first two opposite labels. Its unique top eigenvalue4
    exceeds remaining trace2 and gives soft labels(0,0,1,1,-1,-1). Thus the observed
    pair relation survives in M but both observed scores vanish in the leading vector.
    At zero K, the box-dual objective is2NC for every feasible M, so this can also
    be an optimum. Nonzero orientation information or a separate decoding policy is
    needed; infeasible constraints are a separate possibility.
- assessment_id: penalty-convention
  area: consistency
  topic: Displayed primal and dual normalization
  outcome: supported
  target_ids:
  - AIMech:SemidefiniteMaximumMarginClustering
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  evidence_ids:
  - semidefinitemaximummarginclustering-source
  - semisupervisedsemidefinitemaximummarginclustering-source
  - finite-boundaries
  summary: Use the later dual/SDP convention explicitly.
  details: For primal norm squared plusC times slack, substitution alpha=2lambda gives
    box upper boundC/2. The printed dual instead has boundC and corresponds to twice
    the usual half-norm primal or norm squared plus2C times slack. With two zero-feature
    opposite labels,C1, the displayed primal has minimum2 and printed dual maximum4.
    This is a normalization mismatch in the source display, not an altered AIMech
    mechanism. Soft-margin penalized objectives are not literal inverse squared geometric
    margins in all slack-bearing cases.
- assessment_id: winner-nonconvexity
  area: consistency
  topic: Strict winner indicators and claimed convexity
  outcome: supported
  target_ids:
  - AIMech:CuttingPlaneMulticlassMaximumMarginClustering
  evidence_ids:
  - cuttingplanemulticlassmaximummarginclustering-source
  - finite-boundaries
  summary: Keep the exact tie and Jensen counterexamples visible.
  details: Strict ties make every z zero and label0 invalid. Even away from ties,
    the claimed convex term for n1,c=e1,scores(x,0) is max(x,0)+I[x>0]. At-.2,.2 and
    mixtureweight.75, its value1.1 at.1 exceeds the convex interpolation.9. The frozen-winner
    QP remains convex, but this does not certify global constrained-CCCP monotonicity
    or convergence for the printed winner-dependent function. The record describes
    the actual update without silently supplying a tie repair.
- assessment_id: tolerance-cost-and-experiments
  area: consistency
  topic: Feasibility, cost and evaluation scope
  outcome: supported
  target_ids:
  - AIMech:SemidefiniteMaximumMarginClustering
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  - AIMech:CuttingPlaneMulticlassMaximumMarginClustering
  evidence_ids:
  - semidefinitemaximummarginclustering-source
  - semisupervisedsemidefinitemaximummarginclustering-source
  - cuttingplanemulticlassmaximummarginclustering-source
  summary: Keep guarantees and empirical claims within their demonstrated scope.
  details: CPM3C epsilon bounds omitted constraint violation when separation and restricted
    feasibility hold; it is not a classification-error or global-gap bound. The complexity
    results explicitly restrict iteration-count/linear-time claims to two classes
    and assume fixed working-set and feature conditions. The SDP has dense matrix
    and triple-indexed constraints. Source tables contain comparator-favoring results;
    majority-label scoring is not asserted one-to-one matching. The semisupervised
    tests are transductive and no historical implementation was executed.
- assessment_id: mapping-and-frontier
  area: grounding
  topic: Identity absence and supervision-aware mappings
  outcome: supported
  target_ids:
  - AIMech:SemidefiniteMaximumMarginClustering
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  - AIMech:CuttingPlaneMulticlassMaximumMarginClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Use related tasks and preserve the ongoing frontier.
  details: All442 AIO and498 previous native identities were checked; ignored-inclusive
    searches produced57 lines per checkout,41 distinct texts at114 locations, all
    inspected as references or multiple-kernel neighbors and rendered copies. Fifteen
    AIO annotated targets and21 contextual YAMLs support related UnsupervisedClustering
    for the two unlabeled methods and related Clustering for the partially labeled
    method. SemiSupervisedLLM is not a generic semisupervised-learning class. There
    remain425 pending cohorts; the review does not certify corpus-wide completeness.
- assessment_id: semisupervised-comparison-wording
  area: identity
  topic: Comparison with other transductive solvers
  outcome: concern
  target_ids:
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  evidence_ids:
  - semisupervisedsemidefinitemaximummarginclustering-source
  summary: The identity-note comparison can imply that other transductive SVM solvers
    do not jointly use labeled and unlabeled inputs.
  details: Section5 explicitly discusses other approaches that incorporate unlabeled
    data into SVM training. The wording should state the shared use of labeled and
    unlabeled data separately, then distinguish this variant by its observed-label
    matrix constraints. The record definition and mechanisms are otherwise appropriately
    scoped.
findings:
- finding_id: transductive-comparison-wording
  issue_key: CultureBotAI-AIMech-SemidefiniteMargin-TransductiveComparisonWording
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Clarify the semisupervised record comparison with other transductive solvers
  description: The sentence beginning It jointly uses labeled and unlabeled training
    inputs attaches unlike to generic supervised SVM and all other transductive SVM
    solvers. Other transductive SVM methods also combine labeled and unlabeled inputs,
    as Section5 explains. Separate the shared supervision property from the distinguishing
    S1-S2 label-matrix constraints, and synchronize the current discovery entry. The
    definition, mathematical claims and mappings do not need changing.
  target_ids:
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  field_paths:
  - identity_notes
  - entries
  evidence_ids:
  - semisupervisedsemidefinitemaximummarginclustering-source
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SemisupervisedSemidefiniteMaximumMarginClustering.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261012T065516Z-margin-relaxation.json
    role: maintained
actions:
- action_id: clarify-transductive-comparison
  description: Correct the maintained identity note and current discovery entry, append
    actual edit history, refresh generated pages, validate and save a successor disposition.
  finding_ids:
  - transductive-comparison-wording
  target_ids:
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SemisupervisedSemidefiniteMaximumMarginClustering.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261012T065516Z-margin-relaxation.json
    role: maintained
  acceptance_checks:
  - The text explicitly states that labeled and unlabeled inputs are used jointly
    without claiming this distinguishes every other transductive SVM.
  - The distinguishing observed-label constraints are named; definition, mechanism,
    sources and mappings remain unchanged.
  - The current discovery entry and generated page agree with the corrected YAML;
    curated/history/review and publication gates pass.
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:SemidefiniteMaximumMarginClustering
  - AIMech:SemisupervisedSemidefiniteMaximumMarginClustering
  - AIMech:CuttingPlaneMulticlassMaximumMarginClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - semidefinitemaximummarginclustering-source
  - semisupervisedsemidefinitemaximummarginclustering-source
  - cuttingplanemulticlassmaximummarginclustering-source
  rationale: The unlabeled SDP, labeled-matrix SDP extension and fixed-kernel multiclass
    cutting-plane procedure have distinct complete scopes and constraints. Related
    task mappings retain algorithm/task and supervision distinctions.
limitations:
- Adversarial author self-review only; all three records remain DRAFT.
- One minor wording finding is open and must be resolved in a successor observation
  before the cohort is reported clean.
- All eight Xu2004 and eight CPM3C2008 primary PDF pages were visually read, including
  equations, pseudocode, figures, tables and references. Both official PDFs lack visible
  printed page numbers, so locators use PDF pages.
- The SDP label matrix relaxation preserves constraints satisfied by binary labels
  but does not impose rank one. A global continuous optimum is not a globally optimal
  discrete partition. A feasible mixture of balanced cuts has unique top eigenvalue10/3
  and soft vector(1,1/3,1/3,1/3,-1,-1), whose signs give4-to-2 despite zero column
  sums.
- The semisupervised feasible example is the average of cuts(1,-1,1,1,-1,-1) and(1,-1,-1,-1,1,1).
  It fixes opposite observed labels at indices1,2 and satisfies S1-S2 and zero balance.
  Its unique top eigenvalue4 yields soft vector(0,0,1,1,-1,-1). PSD follows from the
  Gram mixture; in both examples the top eigenvalue exceeds the remaining trace, certifying
  it is uniquely largest. At K=0 every feasible M is optimal, so the decoding concern
  is not excluded by SDP optimality.
- 'Xu2004 Equation3 uses inconsistent same-C primal/dual normalization: setting alpha=2lambda
  gives lambda<=C/2 for the displayed norm-squared plusCslack primal. The record uses
  the later dual/SDP convention explicitly. Two zero-feature opposite labels atC1
  give primal2 versus printeddual4.'
- For CPM3C the claimed convex winner term can be max(x,0)+I[x>0]. Unique-winner points-.2,.2
  with weight3/4 yield midpoint.1 and value1.1 above interpolation.9. Thus a convex
  frozen-indicator QP does not certify global CCCP behavior for the displayed nonconvex
  function. Strict ties also make all winning indicators zero. Epsilon feasibility
  is not a prediction-error or global-optimality bound.
- An exploratory NumPy probe failed before any calculation because NumPy was unavailable.
  The final examples use only the Python standard library and exact rational arithmetic.
  No historical optimizer, benchmark, model training, paid service or complete-paper
  redistribution occurred.
- Three additions bring the native collection to501;442 pinned AIO records remain
  unchanged. The frontier contains425 pending cohorts plus other unresolved dispositions.
  There is no saturation.
links: []
tags:
- native-concepts
- margin-relaxation
- self-review
- discovery-ongoing
```
