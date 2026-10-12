# Scientific self-review of kernel k-means and three incremental initialization procedures

- Review: 20261012T062551Z-global-kernel
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T06:21:48Z
- Finished UTC: 2026-10-12T06:25:51Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the local kernel algorithm and three distinct incremental seed policies, with positive observation weighting parameterized within each. Scope and guarantee qualifications are supported; no actionable finding was identified in the four final records.

## Scope And Provenance

All fields of four fixed-kernel clustering procedures.

Selection: Exact maintained IDs KernelKMeans, GlobalKernelKMeans, FastGlobalKernelKMeans and ConvexMixtureInitializedGlobalKernelKMeans; all selected records without sampling.
Coverage: full; 4 reviewed / 4 in the declared population.
Source: working_tree at Git base 3404a83a69353f30a3c9017225d87f6a6becc560.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:KernelKMeans | data/curated/KernelKMeans.yaml | maintained | Kernel K-Means |
| AIMech:GlobalKernelKMeans | data/curated/GlobalKernelKMeans.yaml | maintained | Global Kernel K-Means |
| AIMech:FastGlobalKernelKMeans | data/curated/FastGlobalKernelKMeans.yaml | maintained | Fast Global Kernel K-Means |
| AIMech:ConvexMixtureInitializedGlobalKernelKMeans | data/curated/ConvexMixtureInitializedGlobalKernelKMeans.yaml | maintained | Global Kernel K-Means with Convex Mixture Models |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:KernelKMeans, AIMech:GlobalKernelKMeans, AIMech:FastGlobalKernelKMeans, AIMech:ConvexMixtureInitializedGlobalKernelKMeans | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 118.21s (0:01:58)<br>Checked 442 record(s); 0 failed.<br>Checked 496 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 148 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 144,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:KernelKMeans, AIMech:GlobalKernelKMeans, AIMech:FastGlobalKernelKMeans, AIMech:ConvexMixtureInitializedGlobalKernelKMeans | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:KernelKMeans, AIMech:GlobalKernelKMeans, AIMech:FastGlobalKernelKMeans, AIMech:ConvexMixtureInitializedGlobalKernelKMeans | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:KernelKMeans, AIMech:GlobalKernelKMeans, AIMech:FastGlobalKernelKMeans, AIMech:ConvexMixtureInitializedGlobalKernelKMeans | Command exited 0 with no output. |
| Kernel initialization boundaries | passed | True | AIMech:KernelKMeans, AIMech:GlobalKernelKMeans, AIMech:FastGlobalKernelKMeans, AIMech:ConvexMixtureInitializedGlobalKernelKMeans | {"weighted_gram_objective": 4.75, "fast_bound_checks": [{"kernel": "linear", "seed": 0, "old_objective": 4.75, "comparison_upper_bound": 1.6875, "first_assignment_cost": 0.6666666666666661}, {"kernel": "linear", "seed": 1, "old_objective": 4.75, "comparison_upper_bound": 4.0625, "first_assignment_cost": 3.25}, {"kernel": "linear", "seed": 2, "old_objective": 4.75, "comparison_upper_bound": 3.1875, "first_assignment_cost": 2.666666666666667}, {"kernel": "rbf", "seed": 0, "old_objective": 0.8486462040235963, "comparison_upper_bound": 0.3296646484213036, "first_assignment_cost": 0.15667079655387284}, {"kernel": "rbf", "seed": 1, "old_objective": 0.8486462040235963, "comparison_upper_bound": 0.7539877504331017, "first_assignment_cost": 0.5726799611516342}, {"kernel": "rbf", "seed": 2, "old_objective": 0.8486462040235963, "comparison_upper_bound": 0.6056308912932656, "first_assignment_cost": 0.5246257870498227}], "graph_shift_checks": [{"mode": "ratio_association", "partition": [[0, 1], [2, 3]], "old_objective": -3.0, "shifted_objective": 7.0, "additive_shift": 10.0}, {"mode": "ratio_association", "partition": [[0, 2], [1, 3]], "old_objective": 2.0, "shifted_objective": 12.0, "additive_shift": 10.0}, {"mode": "ratio_association", "partition": [[0], [1, 2, 3]], "old_objective": -0.6666666666666663, "shifted_objective": 9.333333333333332, "additive_shift": 9.999999999999998}, {"mode": "normalized_cut", "partition": [[0, 1], [2, 3]], "old_objective": -0.6499999999999999, "shifted_objective": 9.350000000000001, "additive_shift": 10.000000000000002}, {"mode": "normalized_cut", "partition": [[0, 2], [1, 3]], "old_objective": 0.45555555555555555, "shifted_objective": 10.455555555555556, "additive_shift": 10.0}, {"mode": "normalized_cut", "partition": [[0], [1, 2, 3]], "old_objective": -0.13571428571428562, "shifted_objective": 9.864285714285716, "additive_shift": 10.000000000000002}], "cmm_ranking_last_two": [{"iteration": 4, "q": [0.2949178532920066, 0.39448833367798647, 0.310593813030007], "order": [1, 2, 0], "log_score": -0.6488260487567276}, {"iteration": 5, "q": [0.28331422366284814, 0.4074168739220094, 0.3092689024151423], "order": [1, 2, 0], "log_score": -0.6479466973520568}], "duplicate_zero_distortion": {"two_identical_points_entropy": 0.6931471805599453, "constant_output_mutual_information": 0, "distortion": 0}, "interpretation": "Finite checks only: weighted distances, scale invariance, singleton bounds, fixed-count graph shift constants, and stable rankings before convergence."} |

## Scientific And Domain Assessments

### Definition, identity, mechanism, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:KernelKMeans.

This record covers the fixed-kernel Lloyd procedure and its positive observation-weight parameterization. Linear kernels with unit weights recover input-space k-means; general valid kernels need not give the same partition. It does not specify the incremental global, fast or CMM seed-selection procedures, learn multiview kernel weights, or perform kernel PCA. Weighted and unit-weight cases share the same parameterized update rather than receiving duplicate local IDs. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 492 prior native IDs, names and aliases; no normalized identity collision. Full searches of both checkouts include ignored and hidden files, returning 62 worktree and 62 main matched lines. All 47 distinct matched texts were inspected as neighboring method mentions, query/frontier references or rendered copies. Eleven annotated AIO nodes, eleven generated YAMLs and seven native neighbors were examined. Nine unchanged annotated nodes, their generated YAMLs, all 442 class labels and 139 semantic rows reuse byte-verified earlier readings; two additional annotated targets and eight new semantic rows were read (147 rows total). Absence is bounded to this pin and corpus.

For a fixed PSD Gram matrix K, supplied cluster count M and positive observation weights a_i, represent each center as the weighted mean of its assigned RKHS features. For cluster C with A_C=sum_j_in_C a_j, compute squared distance K_ii - 2*sum_j_in_C a_j*K_ij/A_C + sum_j,l_in_C a_j*a_l*K_jl/A_C^2. Alternate synchronous nearest-center assignments and mean recomputation. Unit observation weights give unweighted kernel k-means. Scaling every a_i by the same positive constant preserves distances and fits while scaling the objective; these weights are not learned view weights. With W=diag(a), the objective is tr(W*K)-tr(Y^T*W^(1/2)*K*W^(1/2)*Y), where the nonzero indicator entries are Y_ij=sqrt(a_i)/sqrt(A_Cj). Replacing that discrete indicator constraint by arbitrary orthonormal columns yields a leading-eigenvector relaxation. Discretizing its solution need not attain the best discrete objective; the resulting partition can instead initialize further kernel k-means. An objective connection is not equality of all spectral and kernel-k-means algorithms. For a symmetric nonnegative graph affinity A, ratio association uses unit observation weights and K=A. Normalized-cut optimization uses positive degrees d_i=sum_j A_ij as observation weights and K=D^(-1) A D^(-1). For fixed M these choices identify partition objective orderings, not all graph algorithms or their outputs. A sufficiently large shift lambda*I for ratio association, or lambda*D^(-1) for normalized cut, can ensure PSD. Either adds the partition-independent lambda*(N-M) to the corresponding weighted kernel objective while potentially changing local update paths. Zero-degree vertices require a convention. The source graph experiments used small shifts not necessarily ensuring PSD, so their observed convergence is not a general guarantee for indefinite similarities. Exact assignment and mean updates do not increase the nonnegative PSD-kernel objective, but initialization can lead to different fixed points and need not yield a global optimum. Unspecified tie and empty-cluster handling prevents an unconditional termination or unique-result claim. With a dense Gram matrix and cached cluster terms, the source describes quadratic work per local pass in addition to kernel construction; spectral initialization and optional triangle-distance pruning are separate choices. Limitations: PSD kernels, positive cluster weight and well-defined nonempty updates are conditions for the RKHS distance and descent arguments. Arbitrary similarities or arbitrary sigmoid-kernel parameters do not automatically satisfy them. Ties, empty clusters and stopping need explicit implementation conventions. Dense Gram storage is quadratic in N. Kernel choice, supplied cluster count and initialization affect results. No global optimum, approximation ratio, universal empirical superiority or biological causal interpretation is asserted. The primary papers use particular synthetic, digit, face, expression or graph settings, chosen kernels and parameters, and supplied cluster counts. Their finite comparisons do not establish universal performance. No historical implementation or benchmark was reproduced.

### Definition, identity, mechanism, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:GlobalKernelKMeans.

This is the Tzortzis-Likas2009 global kernel k-means procedure, including its positive observation-weight extension. It tries all datum candidates at each stage, unlike the fast one-candidate procedure or CMM-selected subset. Adding clusters is not an asserted nested hierarchy because local fitting can reassign all observations. The algorithm name does not certify a globally optimal partition. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 492 prior native IDs, names and aliases; no normalized identity collision. Full searches of both checkouts include ignored and hidden files, returning 62 worktree and 62 main matched lines. All 47 distinct matched texts were inspected as neighboring method mentions, query/frontier references or rendered copies. Eleven annotated AIO nodes, eleven generated YAMLs and seven native neighbors were examined. Nine unchanged annotated nodes, their generated YAMLs, all 442 class labels and 139 semantic rows reuse byte-verified earlier readings; two additional annotated targets and eight new semantic rows were read (147 rows total). Absence is bounded to this pin and corpus.

For a fixed PSD Gram matrix K, supplied cluster count M and positive observation weights a_i, represent each center as the weighted mean of its assigned RKHS features. For cluster C with A_C=sum_j_in_C a_j, compute squared distance K_ii - 2*sum_j_in_C a_j*K_ij/A_C + sum_j,l_in_C a_j*a_l*K_jl/A_C^2. Alternate synchronous nearest-center assignments and mean recomputation. Unit observation weights give unweighted kernel k-means. Scaling every a_i by the same positive constant preserves distances and fits while scaling the objective; these weights are not learned view weights. Begin with all N observations in one cluster. For k=2,...,M, use the retained (k-1)-cluster partition and try each datum x_n as a new singleton, removing it from its previous cluster while retaining the other groups. Run the local kernel-k-means procedure from each candidate and retain the least final weighted error for this stage. Observation weights change means and errors, not the stated all-datum candidate enumeration. For a symmetric nonnegative graph affinity A, ratio association uses unit observation weights and K=A. Normalized-cut optimization uses positive degrees d_i=sum_j A_ij as observation weights and K=D^(-1) A D^(-1). For fixed M these choices identify partition objective orderings, not all graph algorithms or their outputs. A sufficiently large shift lambda*I for ratio association, or lambda*D^(-1) for normalized cut, can ensure PSD. Either adds the partition-independent lambda*(N-M) to the corresponding weighted kernel objective while potentially changing local update paths. Zero-degree vertices require a convention. The source graph experiments used small shifts not necessarily ensuring PSD, so their observed convergence is not a general guarantee for indefinite similarities. This is a greedy sequence of local fits: it explores datum seeds conditional on the previously retained partition, not every partition or feature-space center. The source explicitly leaves near-optimality theory as future work. A reproducible deterministic result requires fixed tie, candidate-order and stopping policies. Removing a seed from an already singleton source cluster makes that cluster empty; the paper pseudocode does not provide its handling. The all-candidate search multiplies local fitting cost across stages. Limitations: PSD kernels, positive cluster weight and well-defined nonempty updates are conditions for the RKHS distance and descent arguments. Arbitrary similarities or arbitrary sigmoid-kernel parameters do not automatically satisfy them. Ties, empty clusters and stopping need explicit implementation conventions. Dense Gram storage is quadratic in N. Kernel choice, supplied cluster count and initialization affect results. No global optimum, approximation ratio, universal empirical superiority or biological causal interpretation is asserted. The primary papers use particular synthetic, digit, face, expression or graph settings, chosen kernels and parameters, and supplied cluster counts. Their finite comparisons do not establish universal performance. No historical implementation or benchmark was reproduced.

### Definition, identity, mechanism, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:FastGlobalKernelKMeans.

This is the Tzortzis-Likas2009 fast variant with its positive observation-weight extension. It maximizes a bound over datum seeds and performs one local fit per stage, rather than evaluating final errors for every seed or fitting a CMM exemplar shortlist. Maximizing the bound need not select the seed with greatest actual final improvement. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 492 prior native IDs, names and aliases; no normalized identity collision. Full searches of both checkouts include ignored and hidden files, returning 62 worktree and 62 main matched lines. All 47 distinct matched texts were inspected as neighboring method mentions, query/frontier references or rendered copies. Eleven annotated AIO nodes, eleven generated YAMLs and seven native neighbors were examined. Nine unchanged annotated nodes, their generated YAMLs, all 442 class labels and 139 semantic rows reuse byte-verified earlier readings; two additional annotated targets and eight new semantic rows were read (147 rows total). Absence is bounded to this pin and corpus.

For a fixed PSD Gram matrix K, supplied cluster count M and positive observation weights a_i, represent each center as the weighted mean of its assigned RKHS features. For cluster C with A_C=sum_j_in_C a_j, compute squared distance K_ii - 2*sum_j_in_C a_j*K_ij/A_C + sum_j,l_in_C a_j*a_l*K_jl/A_C^2. Alternate synchronous nearest-center assignments and mean recomputation. Unit observation weights give unweighted kernel k-means. Scaling every a_i by the same positive constant preserves distances and fits while scaling the objective; these weights are not learned view weights. At each stage after the one-cluster start, let d_i be the squared distance to the retained old feature mean. For each datum n compute b_n=sum_i a_i*max(d_i-(K_ii+K_nn-2*K_in),0). Select a maximizer, create the corresponding singleton initialization, and run one local kernel-k-means fit. Unit weights recover the unweighted criterion. Candidate-scoring work remains even though only one local fit is performed per stage. For converged old assignments, positive residual cluster weights and well-defined exact nonempty local updates, the source bound is E_new&lt;=E_old-b_n. Although removing the seed changes its previous cluster mean, a weighted RKHS comparison shows that this shift does not raise the aggregate comparison cost, so the bound extends to the displayed singleton-removal initialization under those conditions. It is a bound on one stage, not a global approximation guarantee or proof that the selected seed maximizes actual final improvement. Empty-cluster repairs, indefinite similarities or approximate updates need separate justification. For a symmetric nonnegative graph affinity A, ratio association uses unit observation weights and K=A. Normalized-cut optimization uses positive degrees d_i=sum_j A_ij as observation weights and K=D^(-1) A D^(-1). For fixed M these choices identify partition objective orderings, not all graph algorithms or their outputs. A sufficiently large shift lambda*I for ratio association, or lambda*D^(-1) for normalized cut, can ensure PSD. Either adds the partition-independent lambda*(N-M) to the corresponding weighted kernel objective while potentially changing local update paths. Zero-degree vertices require a convention. The source graph experiments used small shifts not necessarily ensuring PSD, so their observed convergence is not a general guarantee for indefinite similarities. Limitations: PSD kernels, positive cluster weight and well-defined nonempty updates are conditions for the RKHS distance and descent arguments. Arbitrary similarities or arbitrary sigmoid-kernel parameters do not automatically satisfy them. Ties, empty clusters and stopping need explicit implementation conventions. Dense Gram storage is quadratic in N. Kernel choice, supplied cluster count and initialization affect results. No global optimum, approximation ratio, universal empirical superiority or biological causal interpretation is asserted. The primary papers use particular synthetic, digit, face, expression or graph settings, chosen kernels and parameters, and supplied cluster counts. Their finite comparisons do not establish universal performance. No historical implementation or benchmark was reproduced.

### Definition, identity, mechanism, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:ConvexMixtureInitializedGlobalKernelKMeans.

This is the Tzortzis-Likas2009 global kernel k-means with CMM procedure, including its positive observation-weight extension. It uses mixture weights to restrict initialization candidates, while final partitions optimize kernel variance over all observations. It is not the original CMM hard-clustering output, all-datum global search, fast bound maximization, or multiview mixture weighting. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 492 prior native IDs, names and aliases; no normalized identity collision. Full searches of both checkouts include ignored and hidden files, returning 62 worktree and 62 main matched lines. All 47 distinct matched texts were inspected as neighboring method mentions, query/frontier references or rendered copies. Eleven annotated AIO nodes, eleven generated YAMLs and seven native neighbors were examined. Nine unchanged annotated nodes, their generated YAMLs, all 442 class labels and 139 semantic rows reuse byte-verified earlier readings; two additional annotated targets and eight new semantic rows were read (147 rows total). Absence is bounded to this pin and corpus.

For a fixed PSD Gram matrix K, supplied cluster count M and positive observation weights a_i, represent each center as the weighted mean of its assigned RKHS features. For cluster C with A_C=sum_j_in_C a_j, compute squared distance K_ii - 2*sum_j_in_C a_j*K_ij/A_C + sum_j,l_in_C a_j*a_l*K_jl/A_C^2. Alternate synchronous nearest-center assignments and mean recomputation. Unit observation weights give unweighted kernel k-means. Scaling every a_i by the same positive constant preserves distances and fits while scaling the objective; these weights are not learned view weights. For a supplied positive beta, set S_ij=exp(-beta*(K_ii+K_jj-2*K_ij)). With empirical p_i=a_i/sum_l a_l and positive simplex q over eligible exemplars, form z_i=sum_j S_ij*q_j and update q_j&lt;-q_j*sum_i p_i*S_ij/z_i. The unweighted case has p_i=1/N. Fit this finite positive-affinity log-mixture criterion once, then select the P highest-weight exemplars. The source stops when their identities and ordering stay unchanged for a number of consecutive iterations, rather than requiring objective convergence; that iteration count and tie policies need specification. Starting from one cluster, for each k=2,...,M try each of the selected P exemplar data as a new singleton removed from its previous group, run local kernel k-means on all N observations, and retain the least-error fit. The source recommends M&lt;P much smaller than N when useful, with P supplied. Restricting seeds reduces local fits but does not guarantee the same trajectory or objective as all-datum global search; singleton-source and later empty clusters still require conventions. The source beta reference is N*H(p)/sum_ij p_i*distance(i,j)^2, reducing to N^2*log(N)/sum_ij distance(i,j)^2 for uniform p; it is an empirical scale guide and is undefined for a zero denominator. Stable top-P ranking does not certify an optimized mixture or globally optimal final partition. The finite log-affinity criterion is meaningful without assuming a normalized Gaussian density on an arbitrary RKHS; atomic-to-continuous KL language needs a common measure. Duplicate zero-distance observations also qualify the appendix identification of zero-distortion rate with H(p). For a symmetric nonnegative graph affinity A, ratio association uses unit observation weights and K=A. Normalized-cut optimization uses positive degrees d_i=sum_j A_ij as observation weights and K=D^(-1) A D^(-1). For fixed M these choices identify partition objective orderings, not all graph algorithms or their outputs. A sufficiently large shift lambda*I for ratio association, or lambda*D^(-1) for normalized cut, can ensure PSD. Either adds the partition-independent lambda*(N-M) to the corresponding weighted kernel objective while potentially changing local update paths. Zero-degree vertices require a convention. The source graph experiments used small shifts not necessarily ensuring PSD, so their observed convergence is not a general guarantee for indefinite similarities. Limitations: PSD kernels, positive cluster weight and well-defined nonempty updates are conditions for the RKHS distance and descent arguments. Arbitrary similarities or arbitrary sigmoid-kernel parameters do not automatically satisfy them. Ties, empty clusters and stopping need explicit implementation conventions. Dense Gram storage is quadratic in N. Kernel choice, supplied cluster count and initialization affect results. No global optimum, approximation ratio, universal empirical superiority or biological causal interpretation is asserted. The primary papers use particular synthetic, digit, face, expression or graph settings, chosen kernels and parameters, and supplied cluster counts. Their finite comparisons do not establish universal performance. No historical implementation or benchmark was reproduced.

### Local updates versus three seed policies

consistency: supported. Targets: AIMech:KernelKMeans, AIMech:GlobalKernelKMeans, AIMech:FastGlobalKernelKMeans, AIMech:ConvexMixtureInitializedGlobalKernelKMeans.

Retain all four complete procedures.

KernelKMeans specifies a local partition/mean update for a supplied kernel. Global tries all datum seeds at every incremental stage; FastGlobal chooses one by a bound; the CMM version fits an exemplar shortlist once and tries its members at each stage. Shared local updates do not erase different searches. Positive observation weighting is an input parameterization within each algorithm, with unit weights as a special case, rather than eight duplicate local identities. Full reassignment does not ensure a nested cluster hierarchy.

### Gram means and spectral objective connection

consistency: supported. Targets: AIMech:KernelKMeans, AIMech:GlobalKernelKMeans, AIMech:FastGlobalKernelKMeans, AIMech:ConvexMixtureInitializedGlobalKernelKMeans.

Preserve positive-weight, PSD and discrete-partition conditions.

The displayed weighted Gram distance equals direct squared distance to a weighted mean in the finite linear example (objective 4.75); uniform weight scaling preserves distances and scales errors. Orthonormal spectral relaxation removes discrete indicator structure, so a leading eigenspace and its rounding do not certify the best discrete partition or identical algorithm outputs. Fixed observation weights differ from learned view weights.

### Greedy search, deterministic policies and unsupported optimality

consistency: supported. Targets: AIMech:GlobalKernelKMeans, AIMech:FastGlobalKernelKMeans, AIMech:ConvexMixtureInitializedGlobalKernelKMeans.

Keep implementation gaps and guarantee limits explicit.

The primary paper leaves near-optimality theory open. All-datum initialization searches conditionally on the previously retained partition, not all partitions. The fast criterion maximizes a bound, not measured final improvement. A singleton source cluster becomes empty on removal, and later Lloyd steps can also create empty groups; no unrestricted repair guarantee is asserted. Tie, stopping and candidate conventions are needed for a reproducible deterministic implementation.

### Conditional stage-wise upper error bound

consistency: supported. Targets: AIMech:FastGlobalKernelKMeans.

The singleton-removal concern is resolved, not a source defect.

At a converged old partition, choose the comparison assignment using old means plus the new datum center. In the seed source cluster, every transferred observation has twice its centered inner product with the seed vector at least the seed squared norm. The removed weight B includes the seed weight a. Recomputing the remaining mean changes aggregate comparison cost by at most a*W*(a-B)*norm(z)^2/(W-a)^2&lt;=0. Nearest reassignment and weighted-mean updates cannot increase that cost. Positive residual weight, PSD geometry and defined nonempty exact updates are essential. Six finite linear/RBF examples agree. The 10000-dataset exploratory probe was not itself a proof.

### Objective equivalence versus optimization paths

consistency: supported. Targets: AIMech:KernelKMeans, AIMech:GlobalKernelKMeans, AIMech:FastGlobalKernelKMeans, AIMech:ConvexMixtureInitializedGlobalKernelKMeans.

Preserve fixed-M constants, degree conditions and PSD limits.

For ratio association and normalized cut, the appropriate diagonal shift adds lambda*(N-M); six finite checks give 10 at N=4,M=2,lambda=5. Pre-shift indefinite matrices can have negative algebraic values, not valid nonnegative RKHS errors. A sufficient shift preserves partition objective ordering but can change local trajectories. The papers do not establish convergence for every indefinite similarity. The 2004 averaged normalized-cut convention differs by a fixed factor from its later unaveraged display; the records assert orderings, not incompatible numerical equalities.

### Candidate fitting, ranking stopping and density interpretation

consistency: supported. Targets: AIMech:ConvexMixtureInitializedGlobalKernelKMeans.

Keep CMM as seed selection and qualify its scale heuristic.

The final fit uses all N observations and kernel variance, not the original CMM hard assignments. Finite iterations 4 and 5 preserve exemplar ordering while changing q and improving the log score, so stable ranking does not certify objective convergence. The beta guide requires a nonzero denominator and does not tune all model choices. Gaussian-density and atomic/continuous KL claims need their measure assumptions; duplicate identical observations can attain zero distortion with zero information despite positive empirical entropy.

### Bounded duplicate search and mapping

grounding: supported. Targets: AIMech:KernelKMeans, AIMech:GlobalKernelKMeans, AIMech:FastGlobalKernelKMeans, AIMech:ConvexMixtureInitializedGlobalKernelKMeans.

Keep native DRAFT status and related task mappings.

All 442 AIO and 492 previous native identities were compared. Ignored-inclusive searches found 62 lines in each checkout, 47 distinct texts at 124 locations, all inspected as references or neighboring procedures and generated copies. The eleven annotated targets and eighteen contextual YAMLs support related UnsupervisedClustering mappings without equivalence to tasks, kernel layers, PCA projections, neural graph models or a nested hierarchy. There remain 417 pending cohorts, so this review is not saturation or corpus-wide scientific approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:KernelKMeans, AIMech:GlobalKernelKMeans, AIMech:FastGlobalKernelKMeans, AIMech:ConvexMixtureInitializedGlobalKernelKMeans. The local update and three initialization policies define different complete algorithms. Unit and positive observation-weight cases share each procedure parameterization. Related AIO task mappings preserve abstraction boundaries without upstream subclass assertions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T062054Z-global-kernel.json | supports | Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 492 prior native IDs, names and aliases; no normalized identity collision. Full searches of both checkouts include ignored and hidden files, returning 62 worktree and 62 main matched lines. All 47 distinct matched texts were inspected as neighboring method mentions, query/frontier references or rendered copies. Eleven annotated AIO nodes, eleven generated YAMLs and seven native neighbors were examined. Nine unchanged annotated nodes, their generated YAMLs, all 442 class labels and 139 semantic rows reuse byte-verified earlier readings; two additional annotated targets and eight new semantic rows were read (147 rows total). Absence is bounded to this pin and corpus.<br> |
| mapping | sources/aio/aio.json; Eleven annotated CLASS nodes and outgoing edges; 147 semantic rows and all 442 class labels with byte-verified prior readings | supports | Inspected eleven annotated AIO CLASS nodes and outgoing edges, eleven generated YAMLs and seven native neighbors. Nine annotated nodes, their generated YAMLs, all 442 class labels and 139 semantic rows reuse verified identical bytes from round122. Expanded graph/hierarchy/feature search adds eight inspected rows (147 total); HierarchicalClustering and GraphConvolutionalNetwork annotations and full YAMLs were newly read. Related AIO:UnsupervisedClustering maps algorithms to the task they perform, not equivalent identities or upstream subclasses. Clustering and UnsupervisedLearning are broader task/paradigm contexts; MachineLearningTask is generic. KernelLayer is a layer, PCA and DimensionalityReduction concern projections, Model is too broad, and neural RepresentationLearning/GraphConvolutionalNetwork do not describe the fixed-kernel procedures. Incrementally adding clusters with full reassignment need not form a nested cluster hierarchy, so HierarchicalClustering is not an identity match. Native KMeans is the linear-kernel special case; KernelPCA/SpectralHashing/PowerIterationClustering use different objectives or procedures. ExemplarBasedConvexClustering fits and hardens mixtures; the new CMM variant uses mixture exemplars only as candidate seeds for kernel variance minimization. MVKKM and MVSpec learn view weights rather than fixed observation weights. Mapping and absence are bounded to the pinned snapshot and inspected corpus.<br> |
| neighbors | research/discovery/20261012T062054Z-global-kernel.json; source_analysis.aio_mapping_inspection: eleven generated and seven native contextual YAMLs | supports | KMeans, KernelPCA, SpectralHashing, PowerIterationClustering, ExemplarBasedConvexClustering, MultiviewKernelKMeans and WeightedMultiviewSpectralClustering distinguish the local algorithm, three new seed policies, projections, mixture outputs and learned view weights. Prior readings use verified identical bytes; two additional AIO nodes and YAMLs were read. No context receives renewed scientific approval. |
| finite-boundaries | research/discovery/global-kernel-boundaries.py; Weighted Gram distances, linear/RBF seed bounds, graph shifts, mixture rankings and duplicate zero-distortion example | supports | Finite checks for weighted Gram distances, uniform observation-weight scaling, singleton seed bounds with linear/RBF kernels, fixed-count graph-shift constants and normalized-cut conventions, stable mixture rankings before convergence, and duplicate zero-distortion information. These are mathematical examples, not historical benchmark reproduction. |
| singleton-proof | research/discovery/global-kernel-seed-bound.md; Weighted RKHS comparison for the seed-removal mean shift | supports | The initial concern about Algorithm 2 shifting the previous mean is resolved under explicit positive residual cluster-weight and exact nonempty-update conditions. The comparison cost change is bounded by a*W*(a-B)*norm(z)^2/(W-a)^2&lt;=0 because B&gt;=a. The source bound therefore survives this shift. Empty-cluster repairs and indefinite similarities remain outside the argument. |
| kernelkmeans-source-0 | https://www.cs.utexas.edu/users/inderjit/public_papers/kdd_spectral_kernelkmeans.pdf; Section 2.1, PDF p. 2, Equations 1-2 and Algorithm 1; Section 2.1, PDF p. 2; Sections 4.2 and 5, PDF p. 4; Section 8, PDF p. 6; Sections 3-4, PDF pp. 3-4 | supports | Kernel k-means, Spectral Clustering and Normalized Cuts. Author-hosted six-page KDD2004 manuscript corresponding to pp. 551-556. No visible printed page numbering; locators use PDF pages. All six pages visually read. Original claims and curator qualifications are distinguished; historical experiments were not reproduced. |
| kernelkmeans-source-1 | https://www.cs.uoi.gr/~arly/papers/TNN09b.pdf; Section II-B, PDF pp. 2-3 / printed pp. 1182-1183, Algorithm 1; Section V-A, PDF p. 6 / p. 1186, Equations 12-13; Section VI, PDF pp. 7-8 / printed pp. 1187-1188, Equations 20-21; Section VII-C, PDF p. 11 / p. 1191; curator fixed-count shift calculation | supports | The Global Kernel k-Means Algorithm for Clustering in Feature Space. IEEE Transactions on Neural Networks 20(7):1181-1194, July 2009. All fourteen author-hosted PDF pages visually read; printed page equals PDF page plus 1180. Original claims and curator qualifications are distinguished; historical experiments were not reproduced. |
| globalkernelkmeans-source-0 | https://www.cs.uoi.gr/~arly/papers/TNN09b.pdf; Section II-B, PDF pp. 2-3 / printed pp. 1182-1183, Algorithm 1; Section V-A, PDF p. 6 / p. 1186, Equations 12-13; Section III-A, PDF pp. 3-4 / pp. 1183-1184, Algorithm 2; Section V-B, PDF p. 6 / p. 1186; Section III-A, PDF pp. 3-4 / pp. 1183-1184; Section VIII, PDF p. 13 / p. 1193; Section III-A, PDF pp. 3-4 / printed pp. 1183-1184, Algorithm 2; Section V-B, PDF p. 6 / p. 1186; Section VI, PDF pp. 7-8 / printed pp. 1187-1188, Equations 20-21; Section VII-C, PDF p. 11 / p. 1191; curator fixed-count shift calculation | supports | The Global Kernel k-Means Algorithm for Clustering in Feature Space. IEEE Transactions on Neural Networks 20(7):1181-1194, July 2009. All fourteen author-hosted PDF pages visually read; printed page equals PDF page plus 1180. Original claims and curator qualifications are distinguished; historical experiments were not reproduced. |
| fastglobalkernelkmeans-source-0 | https://www.cs.uoi.gr/~arly/papers/TNN09b.pdf; Section II-B, PDF pp. 2-3 / printed pp. 1182-1183, Algorithm 1; Section V-A, PDF p. 6 / p. 1186, Equations 12-13; Section IV-A, PDF p. 4 / printed p. 1184, Equation 4; Section V-C, PDF pp. 6-7 / pp. 1186-1187, Equation 14; Section IV-A, PDF p. 4 / printed p. 1184; Section V-C, PDF p. 7 / p. 1187; curator singleton-removal derivation and finite checks; Section VI, PDF pp. 7-8 / printed pp. 1187-1188, Equations 20-21; Section VII-C, PDF p. 11 / p. 1191; curator fixed-count shift calculation; Sections IV-A and V-C, PDF pp. 4 and 6-7 / printed pp. 1184 and 1186-1187, Equations 4 and 14 | supports | The Global Kernel k-Means Algorithm for Clustering in Feature Space. IEEE Transactions on Neural Networks 20(7):1181-1194, July 2009. All fourteen author-hosted PDF pages visually read; printed page equals PDF page plus 1180. Original claims and curator qualifications are distinguished; historical experiments were not reproduced. |
| convexmixtureinitializedglobalkernelkmeans-source-0 | https://www.cs.uoi.gr/~arly/papers/TNN09b.pdf; Section II-B, PDF pp. 2-3 / printed pp. 1182-1183, Algorithm 1; Section V-A, PDF p. 6 / p. 1186, Equations 12-13; Section IV-B, PDF p. 5 / p. 1185, Equations 7-10; Section V-D, PDF p. 7 / p. 1187, Equations 15-18; Section IV-B, PDF p. 6 / p. 1186, Equation 11; Section V-D, PDF p. 7 / p. 1187, Equation 19; Appendix, PDF pp. 13-14 / pp. 1193-1194; curator stable-ranking and duplicate checks; Section IV-B, PDF p. 6 / p. 1186; Section V-D, PDF p. 7 / p. 1187; Section IV-B, PDF pp. 5-6 / printed pp. 1185-1186, Equations 5-11; Section V-D, PDF p. 7 / p. 1187, Equations 15-19; Section VI, PDF pp. 7-8 / printed pp. 1187-1188, Equations 20-21; Section VII-C, PDF p. 11 / p. 1191; curator fixed-count shift calculation | supports | The Global Kernel k-Means Algorithm for Clustering in Feature Space. IEEE Transactions on Neural Networks 20(7):1181-1194, July 2009. All fourteen author-hosted PDF pages visually read; printed page equals PDF page plus 1180. Original claims and curator qualifications are distinguished; historical experiments were not reproduced. |

## Limits And Additional Notes

- Adversarial author self-review only; all four records remain DRAFT.
- All fourteen Tzortzis2009 and six Dhillon2004 pages were visually read, including formulas, tables, figures and references. The 2009 printed-page offset is 1180; the 2004 author manuscript has no visible printed page numbers.
- Positive observation weights, nonempty cluster weights, PSD kernels and exact local updates delimit the descent and seed-bound claims. The named global search is greedy initialization, not a global-optimality or approximation-ratio certificate.
- A concern about the fast bound under singleton-removal initialization was investigated and resolved by a weighted RKHS comparison, not reported as a paper defect. A separate seeded 10000-dataset probe found no counterexample under defined runs; only the derivation supports the general conditional argument.
- Finite graph checks include algebraic pre-shift values for indefinite affinities; negative values there are not asserted RKHS squared errors. Sufficient PSD shifts preserve fixed-count objective ordering while possibly changing update paths.
- CMM exemplar ranking can stabilize before optimization; its beta rule is empirical and needs nonzero denominator. Finite affinity fitting does not by itself define a normalized Gaussian on arbitrary RKHS or an atomic-to-continuous KL.
- No historical code, benchmark, trained model, paid service or complete-paper redistribution. The downloaded twelve-page maximum-margin paper is not yet fully read.
- Four additions bring the native collection to 496; 442 pinned AIO records are unchanged. There are 417 pending frontier cohorts and other unresolved dispositions; no saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T062551Z-global-kernel
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of kernel k-means and three incremental initialization
  procedures
started_at: '2026-10-12T06:21:48Z'
finished_at: '2026-10-12T06:25:51Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent reread every field of all four final records
    against twenty visually read primary PDF pages, eleven annotated AIO nodes and
    eighteen contextual YAMLs, reusing earlier context only after byte verification.
    Seven boundary assessments and finite calculations challenge scope and guarantees;
    a weighted RKHS derivation resolves the seed-removal bound concern. This is author
    self-review, not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the local kernel algorithm and three distinct incremental seed policies,
  with positive observation weighting parameterized within each. Scope and guarantee
  qualifications are supported; no actionable finding was identified in the four final
  records.
source:
  git_revision: 3404a83a69353f30a3c9017225d87f6a6becc560
  state: working_tree
  inputs:
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/DimensionalityReduction.yaml
    sha256: 99eb0714b362a98a9e704e5ef2ac370cb7a900fbe97da43de790c3ec67ed812e
    role: context
  - path: data/aio/GraphConvolutionalNetwork.yaml
    sha256: 644b6187436c10693cb547dbaa809b8c00c97ad198db201342e5bc0780c78d44
    role: context
  - path: data/aio/HierarchicalClustering.yaml
    sha256: 144deaecd150e22de207c11a62f19db5f8409443724bd4be4b5c95c53375b258
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
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
    role: context
  - path: data/aio/RepresentationLearning.yaml
    sha256: bc7af756440437f60210019e17ad1e2dd15cd1c7cbfbc96312520934b7a5c7ca
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/ConvexMixtureInitializedGlobalKernelKMeans.yaml
    sha256: 02f3c182b8aee11b9dba0bba93f182b9acc8e0a789222e609166d810cb867adf
    role: target
  - path: data/curated/ExemplarBasedConvexClustering.yaml
    sha256: 5520d800b3c23b513c66837e5f8fc424a7d7d4261f94047b94c8d71fee5973d9
    role: context
  - path: data/curated/FastGlobalKernelKMeans.yaml
    sha256: 709a8cab5895fbf8f17e0be45a61f4c5dbcdc2245d73d97f21e7f52a446f8659
    role: target
  - path: data/curated/GlobalKernelKMeans.yaml
    sha256: 68b9f7a2a1d1019f360ffd722e07dc46881cb7dd965990eba57203db34db34a4
    role: target
  - path: data/curated/KMeans.yaml
    sha256: 50fc1d8d18403a8f314636f68b6812ffd15fec2dfaaf4c32aaad423dfa7ffa03
    role: context
  - path: data/curated/KernelKMeans.yaml
    sha256: a5fe0bf0d883e32d689c79c232d8a8093b0ab29a56df616a5ef367e931aca84a
    role: target
  - path: data/curated/KernelPCA.yaml
    sha256: a93227a6b2d6b2b89b679b8f7f9ddd5054741d1c11f9510490d82a3e691a1cab
    role: context
  - path: data/curated/MultiviewKernelKMeans.yaml
    sha256: fa7e2c11fa5e73ed61188affeee7ac460761880154837228e3724a754885467a
    role: context
  - path: data/curated/PowerIterationClustering.yaml
    sha256: ca81d60eb87c027126a3372950d40f50d0df8391b1075697e0ab5ffabf3dfa0f
    role: context
  - path: data/curated/SpectralHashing.yaml
    sha256: db90a881a13cbebad6083cb7534f8f0719c4a56fd136f5f3dc17e8c1ba8833c8
    role: context
  - path: data/curated/WeightedMultiviewSpectralClustering.yaml
    sha256: 14031e86b6ad2c67137b7f0806675600ece879a392494f295f23edadf2eee9fe
    role: context
  - path: research/discovery/20261012T062054Z-global-kernel.json
    sha256: a6010021104a8961401936647479e5256910e2491969dd74bba5c3cad28ea86b
    role: context
  - path: research/discovery/global-kernel-boundaries.py
    sha256: b43fe1c6c6dfa79d5bc713e573a8b14cd44681ca8edc526e1cd4344b59c48dd8
    role: context
  - path: research/discovery/global-kernel-seed-bound.md
    sha256: 8ab880d305b488cd4ffa36a75ffba52463c0ebdc200c2d1039c43bfcffa0b50b
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
- target_id: AIMech:KernelKMeans
  path: data/curated/KernelKMeans.yaml
  label: Kernel K-Means
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/KernelKMeans.yaml
    role: maintained
- target_id: AIMech:GlobalKernelKMeans
  path: data/curated/GlobalKernelKMeans.yaml
  label: Global Kernel K-Means
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GlobalKernelKMeans.yaml
    role: maintained
- target_id: AIMech:FastGlobalKernelKMeans
  path: data/curated/FastGlobalKernelKMeans.yaml
  label: Fast Global Kernel K-Means
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FastGlobalKernelKMeans.yaml
    role: maintained
- target_id: AIMech:ConvexMixtureInitializedGlobalKernelKMeans
  path: data/curated/ConvexMixtureInitializedGlobalKernelKMeans.yaml
  label: Global Kernel K-Means with Convex Mixture Models
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ConvexMixtureInitializedGlobalKernelKMeans.yaml
    role: maintained
scope:
  description: All fields of four fixed-kernel clustering procedures.
  selection: Exact maintained IDs KernelKMeans, GlobalKernelKMeans, FastGlobalKernelKMeans
    and ConvexMixtureInitializedGlobalKernelKMeans; all selected records without sampling.
  coverage: full
  population_size: 4
  reviewed_target_ids:
  - AIMech:KernelKMeans
  - AIMech:GlobalKernelKMeans
  - AIMech:FastGlobalKernelKMeans
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
  exclusions:
  - target: Contextual generated and maintained records
    reason: Used for identity and mapping without renewed scientific approval or mutation.
  - target: Historical implementation and benchmark reproduction
    reason: No source implementation was executed. Finite examples and the RKHS derivation
      test limited mathematical claims.
  - target: Generated website
    reason: Regenerated from the new records and included in required validation;
      not a separate scientific target or visual-design review.
  - target: Remaining discovery frontier
    reason: 417 pending cohorts and other unresolved dispositions remain; the downloaded
      Zhao2009 PDF is not yet fully read.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:KernelKMeans
  - AIMech:GlobalKernelKMeans
  - AIMech:FastGlobalKernelKMeans
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 118.21s (0:01:58)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 496 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 148 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 144,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:KernelKMeans
  - AIMech:GlobalKernelKMeans
  - AIMech:FastGlobalKernelKMeans
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
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
  - AIMech:KernelKMeans
  - AIMech:GlobalKernelKMeans
  - AIMech:FastGlobalKernelKMeans
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
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
  - AIMech:KernelKMeans
  - AIMech:GlobalKernelKMeans
  - AIMech:FastGlobalKernelKMeans
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Kernel initialization boundaries
  command: python3 research/discovery/global-kernel-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:KernelKMeans
  - AIMech:GlobalKernelKMeans
  - AIMech:FastGlobalKernelKMeans
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
  exit_code: 0
  expected_exit_code: 0
  summary: '{"weighted_gram_objective": 4.75, "fast_bound_checks": [{"kernel": "linear",
    "seed": 0, "old_objective": 4.75, "comparison_upper_bound": 1.6875, "first_assignment_cost":
    0.6666666666666661}, {"kernel": "linear", "seed": 1, "old_objective": 4.75, "comparison_upper_bound":
    4.0625, "first_assignment_cost": 3.25}, {"kernel": "linear", "seed": 2, "old_objective":
    4.75, "comparison_upper_bound": 3.1875, "first_assignment_cost": 2.666666666666667},
    {"kernel": "rbf", "seed": 0, "old_objective": 0.8486462040235963, "comparison_upper_bound":
    0.3296646484213036, "first_assignment_cost": 0.15667079655387284}, {"kernel":
    "rbf", "seed": 1, "old_objective": 0.8486462040235963, "comparison_upper_bound":
    0.7539877504331017, "first_assignment_cost": 0.5726799611516342}, {"kernel": "rbf",
    "seed": 2, "old_objective": 0.8486462040235963, "comparison_upper_bound": 0.6056308912932656,
    "first_assignment_cost": 0.5246257870498227}], "graph_shift_checks": [{"mode":
    "ratio_association", "partition": [[0, 1], [2, 3]], "old_objective": -3.0, "shifted_objective":
    7.0, "additive_shift": 10.0}, {"mode": "ratio_association", "partition": [[0,
    2], [1, 3]], "old_objective": 2.0, "shifted_objective": 12.0, "additive_shift":
    10.0}, {"mode": "ratio_association", "partition": [[0], [1, 2, 3]], "old_objective":
    -0.6666666666666663, "shifted_objective": 9.333333333333332, "additive_shift":
    9.999999999999998}, {"mode": "normalized_cut", "partition": [[0, 1], [2, 3]],
    "old_objective": -0.6499999999999999, "shifted_objective": 9.350000000000001,
    "additive_shift": 10.000000000000002}, {"mode": "normalized_cut", "partition":
    [[0, 2], [1, 3]], "old_objective": 0.45555555555555555, "shifted_objective": 10.455555555555556,
    "additive_shift": 10.0}, {"mode": "normalized_cut", "partition": [[0], [1, 2,
    3]], "old_objective": -0.13571428571428562, "shifted_objective": 9.864285714285716,
    "additive_shift": 10.000000000000002}], "cmm_ranking_last_two": [{"iteration":
    4, "q": [0.2949178532920066, 0.39448833367798647, 0.310593813030007], "order":
    [1, 2, 0], "log_score": -0.6488260487567276}, {"iteration": 5, "q": [0.28331422366284814,
    0.4074168739220094, 0.3092689024151423], "order": [1, 2, 0], "log_score": -0.6479466973520568}],
    "duplicate_zero_distortion": {"two_identical_points_entropy": 0.6931471805599453,
    "constant_output_mutual_information": 0, "distortion": 0}, "interpretation": "Finite
    checks only: weighted distances, scale invariance, singleton bounds, fixed-count
    graph shift constants, and stable rankings before convergence."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T062054Z-global-kernel.json
  accessed_at: '2026-10-12T06:21:48Z'
  support: supports
  summary: 'Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 492
    prior native IDs, names and aliases; no normalized identity collision. Full searches
    of both checkouts include ignored and hidden files, returning 62 worktree and
    62 main matched lines. All 47 distinct matched texts were inspected as neighboring
    method mentions, query/frontier references or rendered copies. Eleven annotated
    AIO nodes, eleven generated YAMLs and seven native neighbors were examined. Nine
    unchanged annotated nodes, their generated YAMLs, all 442 class labels and 139
    semantic rows reuse byte-verified earlier readings; two additional annotated targets
    and eight new semantic rows were read (147 rows total). Absence is bounded to
    this pin and corpus.

    '
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Eleven annotated CLASS nodes and outgoing edges; 147 semantic rows and
    all 442 class labels with byte-verified prior readings
  accessed_at: '2026-10-12T06:21:48Z'
  support: supports
  summary: 'Inspected eleven annotated AIO CLASS nodes and outgoing edges, eleven
    generated YAMLs and seven native neighbors. Nine annotated nodes, their generated
    YAMLs, all 442 class labels and 139 semantic rows reuse verified identical bytes
    from round122. Expanded graph/hierarchy/feature search adds eight inspected rows
    (147 total); HierarchicalClustering and GraphConvolutionalNetwork annotations
    and full YAMLs were newly read. Related AIO:UnsupervisedClustering maps algorithms
    to the task they perform, not equivalent identities or upstream subclasses. Clustering
    and UnsupervisedLearning are broader task/paradigm contexts; MachineLearningTask
    is generic. KernelLayer is a layer, PCA and DimensionalityReduction concern projections,
    Model is too broad, and neural RepresentationLearning/GraphConvolutionalNetwork
    do not describe the fixed-kernel procedures. Incrementally adding clusters with
    full reassignment need not form a nested cluster hierarchy, so HierarchicalClustering
    is not an identity match. Native KMeans is the linear-kernel special case; KernelPCA/SpectralHashing/PowerIterationClustering
    use different objectives or procedures. ExemplarBasedConvexClustering fits and
    hardens mixtures; the new CMM variant uses mixture exemplars only as candidate
    seeds for kernel variance minimization. MVKKM and MVSpec learn view weights rather
    than fixed observation weights. Mapping and absence are bounded to the pinned
    snapshot and inspected corpus.

    '
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261012T062054Z-global-kernel.json
  locator: 'source_analysis.aio_mapping_inspection: eleven generated and seven native
    contextual YAMLs'
  accessed_at: '2026-10-12T06:21:48Z'
  support: supports
  summary: KMeans, KernelPCA, SpectralHashing, PowerIterationClustering, ExemplarBasedConvexClustering,
    MultiviewKernelKMeans and WeightedMultiviewSpectralClustering distinguish the
    local algorithm, three new seed policies, projections, mixture outputs and learned
    view weights. Prior readings use verified identical bytes; two additional AIO
    nodes and YAMLs were read. No context receives renewed scientific approval.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/global-kernel-boundaries.py
  locator: Weighted Gram distances, linear/RBF seed bounds, graph shifts, mixture
    rankings and duplicate zero-distortion example
  accessed_at: '2026-10-12T06:21:48Z'
  snapshot_sha256: b43fe1c6c6dfa79d5bc713e573a8b14cd44681ca8edc526e1cd4344b59c48dd8
  support: supports
  summary: Finite checks for weighted Gram distances, uniform observation-weight scaling,
    singleton seed bounds with linear/RBF kernels, fixed-count graph-shift constants
    and normalized-cut conventions, stable mixture rankings before convergence, and
    duplicate zero-distortion information. These are mathematical examples, not historical
    benchmark reproduction.
- evidence_id: singleton-proof
  kind: record_content
  reference: research/discovery/global-kernel-seed-bound.md
  locator: Weighted RKHS comparison for the seed-removal mean shift
  accessed_at: '2026-10-12T06:21:48Z'
  snapshot_sha256: 8ab880d305b488cd4ffa36a75ffba52463c0ebdc200c2d1039c43bfcffa0b50b
  support: supports
  summary: The initial concern about Algorithm 2 shifting the previous mean is resolved
    under explicit positive residual cluster-weight and exact nonempty-update conditions.
    The comparison cost change is bounded by a*W*(a-B)*norm(z)^2/(W-a)^2<=0 because
    B>=a. The source bound therefore survives this shift. Empty-cluster repairs and
    indefinite similarities remain outside the argument.
- evidence_id: kernelkmeans-source-0
  kind: primary_source
  reference: https://www.cs.utexas.edu/users/inderjit/public_papers/kdd_spectral_kernelkmeans.pdf
  locator: Section 2.1, PDF p. 2, Equations 1-2 and Algorithm 1; Section 2.1, PDF
    p. 2; Sections 4.2 and 5, PDF p. 4; Section 8, PDF p. 6; Sections 3-4, PDF pp.
    3-4
  accessed_at: '2026-10-12T06:10:44Z'
  snapshot_sha256: 48c2db70020eb1ae7885500b083c3b6c2b635e3050ba5c269a1288c96b3720c3
  support: supports
  summary: Kernel k-means, Spectral Clustering and Normalized Cuts. Author-hosted
    six-page KDD2004 manuscript corresponding to pp. 551-556. No visible printed page
    numbering; locators use PDF pages. All six pages visually read. Original claims
    and curator qualifications are distinguished; historical experiments were not
    reproduced.
- evidence_id: kernelkmeans-source-1
  kind: primary_source
  reference: https://www.cs.uoi.gr/~arly/papers/TNN09b.pdf
  locator: Section II-B, PDF pp. 2-3 / printed pp. 1182-1183, Algorithm 1; Section
    V-A, PDF p. 6 / p. 1186, Equations 12-13; Section VI, PDF pp. 7-8 / printed pp.
    1187-1188, Equations 20-21; Section VII-C, PDF p. 11 / p. 1191; curator fixed-count
    shift calculation
  accessed_at: '2026-10-12T06:00:45Z'
  snapshot_sha256: 7a5bbe6bfbb963a47ff3c94f2446941de1a8496f06feca9ad65a3a08a4c650d9
  support: supports
  summary: The Global Kernel k-Means Algorithm for Clustering in Feature Space. IEEE
    Transactions on Neural Networks 20(7):1181-1194, July 2009. All fourteen author-hosted
    PDF pages visually read; printed page equals PDF page plus 1180. Original claims
    and curator qualifications are distinguished; historical experiments were not
    reproduced.
- evidence_id: globalkernelkmeans-source-0
  kind: primary_source
  reference: https://www.cs.uoi.gr/~arly/papers/TNN09b.pdf
  locator: Section II-B, PDF pp. 2-3 / printed pp. 1182-1183, Algorithm 1; Section
    V-A, PDF p. 6 / p. 1186, Equations 12-13; Section III-A, PDF pp. 3-4 / pp. 1183-1184,
    Algorithm 2; Section V-B, PDF p. 6 / p. 1186; Section III-A, PDF pp. 3-4 / pp.
    1183-1184; Section VIII, PDF p. 13 / p. 1193; Section III-A, PDF pp. 3-4 / printed
    pp. 1183-1184, Algorithm 2; Section V-B, PDF p. 6 / p. 1186; Section VI, PDF pp.
    7-8 / printed pp. 1187-1188, Equations 20-21; Section VII-C, PDF p. 11 / p. 1191;
    curator fixed-count shift calculation
  accessed_at: '2026-10-12T06:00:45Z'
  snapshot_sha256: 7a5bbe6bfbb963a47ff3c94f2446941de1a8496f06feca9ad65a3a08a4c650d9
  support: supports
  summary: The Global Kernel k-Means Algorithm for Clustering in Feature Space. IEEE
    Transactions on Neural Networks 20(7):1181-1194, July 2009. All fourteen author-hosted
    PDF pages visually read; printed page equals PDF page plus 1180. Original claims
    and curator qualifications are distinguished; historical experiments were not
    reproduced.
- evidence_id: fastglobalkernelkmeans-source-0
  kind: primary_source
  reference: https://www.cs.uoi.gr/~arly/papers/TNN09b.pdf
  locator: Section II-B, PDF pp. 2-3 / printed pp. 1182-1183, Algorithm 1; Section
    V-A, PDF p. 6 / p. 1186, Equations 12-13; Section IV-A, PDF p. 4 / printed p.
    1184, Equation 4; Section V-C, PDF pp. 6-7 / pp. 1186-1187, Equation 14; Section
    IV-A, PDF p. 4 / printed p. 1184; Section V-C, PDF p. 7 / p. 1187; curator singleton-removal
    derivation and finite checks; Section VI, PDF pp. 7-8 / printed pp. 1187-1188,
    Equations 20-21; Section VII-C, PDF p. 11 / p. 1191; curator fixed-count shift
    calculation; Sections IV-A and V-C, PDF pp. 4 and 6-7 / printed pp. 1184 and 1186-1187,
    Equations 4 and 14
  accessed_at: '2026-10-12T06:00:45Z'
  snapshot_sha256: 7a5bbe6bfbb963a47ff3c94f2446941de1a8496f06feca9ad65a3a08a4c650d9
  support: supports
  summary: The Global Kernel k-Means Algorithm for Clustering in Feature Space. IEEE
    Transactions on Neural Networks 20(7):1181-1194, July 2009. All fourteen author-hosted
    PDF pages visually read; printed page equals PDF page plus 1180. Original claims
    and curator qualifications are distinguished; historical experiments were not
    reproduced.
- evidence_id: convexmixtureinitializedglobalkernelkmeans-source-0
  kind: primary_source
  reference: https://www.cs.uoi.gr/~arly/papers/TNN09b.pdf
  locator: Section II-B, PDF pp. 2-3 / printed pp. 1182-1183, Algorithm 1; Section
    V-A, PDF p. 6 / p. 1186, Equations 12-13; Section IV-B, PDF p. 5 / p. 1185, Equations
    7-10; Section V-D, PDF p. 7 / p. 1187, Equations 15-18; Section IV-B, PDF p. 6
    / p. 1186, Equation 11; Section V-D, PDF p. 7 / p. 1187, Equation 19; Appendix,
    PDF pp. 13-14 / pp. 1193-1194; curator stable-ranking and duplicate checks; Section
    IV-B, PDF p. 6 / p. 1186; Section V-D, PDF p. 7 / p. 1187; Section IV-B, PDF pp.
    5-6 / printed pp. 1185-1186, Equations 5-11; Section V-D, PDF p. 7 / p. 1187,
    Equations 15-19; Section VI, PDF pp. 7-8 / printed pp. 1187-1188, Equations 20-21;
    Section VII-C, PDF p. 11 / p. 1191; curator fixed-count shift calculation
  accessed_at: '2026-10-12T06:00:45Z'
  snapshot_sha256: 7a5bbe6bfbb963a47ff3c94f2446941de1a8496f06feca9ad65a3a08a4c650d9
  support: supports
  summary: The Global Kernel k-Means Algorithm for Clustering in Feature Space. IEEE
    Transactions on Neural Networks 20(7):1181-1194, July 2009. All fourteen author-hosted
    PDF pages visually read; printed page equals PDF page plus 1180. Original claims
    and curator qualifications are distinguished; historical experiments were not
    reproduced.
assessments:
- assessment_id: kernelkmeans
  area: evidence
  topic: Definition, identity, mechanism, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:KernelKMeans
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - singleton-proof
  - kernelkmeans-source-0
  - kernelkmeans-source-1
  summary: This record covers the fixed-kernel Lloyd procedure and its positive observation-weight
    parameterization. Linear kernels with unit weights recover input-space k-means;
    general valid kernels need not give the same partition. It does not specify the
    incremental global, fast or CMM seed-selection procedures, learn multiview kernel
    weights, or perform kernel PCA. Weighted and unit-weight cases share the same
    parameterized update rather than receiving duplicate local IDs. Compared all 442
    pinned AIO IDs, labels and scoped synonyms with all 492 prior native IDs, names
    and aliases; no normalized identity collision. Full searches of both checkouts
    include ignored and hidden files, returning 62 worktree and 62 main matched lines.
    All 47 distinct matched texts were inspected as neighboring method mentions, query/frontier
    references or rendered copies. Eleven annotated AIO nodes, eleven generated YAMLs
    and seven native neighbors were examined. Nine unchanged annotated nodes, their
    generated YAMLs, all 442 class labels and 139 semantic rows reuse byte-verified
    earlier readings; two additional annotated targets and eight new semantic rows
    were read (147 rows total). Absence is bounded to this pin and corpus.
  details: 'For a fixed PSD Gram matrix K, supplied cluster count M and positive observation
    weights a_i, represent each center as the weighted mean of its assigned RKHS features.
    For cluster C with A_C=sum_j_in_C a_j, compute squared distance K_ii - 2*sum_j_in_C
    a_j*K_ij/A_C + sum_j,l_in_C a_j*a_l*K_jl/A_C^2. Alternate synchronous nearest-center
    assignments and mean recomputation. Unit observation weights give unweighted kernel
    k-means. Scaling every a_i by the same positive constant preserves distances and
    fits while scaling the objective; these weights are not learned view weights.
    With W=diag(a), the objective is tr(W*K)-tr(Y^T*W^(1/2)*K*W^(1/2)*Y), where the
    nonzero indicator entries are Y_ij=sqrt(a_i)/sqrt(A_Cj). Replacing that discrete
    indicator constraint by arbitrary orthonormal columns yields a leading-eigenvector
    relaxation. Discretizing its solution need not attain the best discrete objective;
    the resulting partition can instead initialize further kernel k-means. An objective
    connection is not equality of all spectral and kernel-k-means algorithms. For
    a symmetric nonnegative graph affinity A, ratio association uses unit observation
    weights and K=A. Normalized-cut optimization uses positive degrees d_i=sum_j A_ij
    as observation weights and K=D^(-1) A D^(-1). For fixed M these choices identify
    partition objective orderings, not all graph algorithms or their outputs. A sufficiently
    large shift lambda*I for ratio association, or lambda*D^(-1) for normalized cut,
    can ensure PSD. Either adds the partition-independent lambda*(N-M) to the corresponding
    weighted kernel objective while potentially changing local update paths. Zero-degree
    vertices require a convention. The source graph experiments used small shifts
    not necessarily ensuring PSD, so their observed convergence is not a general guarantee
    for indefinite similarities. Exact assignment and mean updates do not increase
    the nonnegative PSD-kernel objective, but initialization can lead to different
    fixed points and need not yield a global optimum. Unspecified tie and empty-cluster
    handling prevents an unconditional termination or unique-result claim. With a
    dense Gram matrix and cached cluster terms, the source describes quadratic work
    per local pass in addition to kernel construction; spectral initialization and
    optional triangle-distance pruning are separate choices. Limitations: PSD kernels,
    positive cluster weight and well-defined nonempty updates are conditions for the
    RKHS distance and descent arguments. Arbitrary similarities or arbitrary sigmoid-kernel
    parameters do not automatically satisfy them. Ties, empty clusters and stopping
    need explicit implementation conventions. Dense Gram storage is quadratic in N.
    Kernel choice, supplied cluster count and initialization affect results. No global
    optimum, approximation ratio, universal empirical superiority or biological causal
    interpretation is asserted. The primary papers use particular synthetic, digit,
    face, expression or graph settings, chosen kernels and parameters, and supplied
    cluster counts. Their finite comparisons do not establish universal performance.
    No historical implementation or benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A complete fixed-kernel clustering procedure, with its positive observation-weight
      parameterization; not a trained instance.
    evidence_ids:
    - kernelkmeans-source-0
    - kernelkmeans-source-1
  - name: aio-assessment
    value: related_match
    definition: 'Inspected eleven annotated AIO CLASS nodes and outgoing edges, eleven
      generated YAMLs and seven native neighbors. Nine annotated nodes, their generated
      YAMLs, all 442 class labels and 139 semantic rows reuse verified identical bytes
      from round122. Expanded graph/hierarchy/feature search adds eight inspected
      rows (147 total); HierarchicalClustering and GraphConvolutionalNetwork annotations
      and full YAMLs were newly read. Related AIO:UnsupervisedClustering maps algorithms
      to the task they perform, not equivalent identities or upstream subclasses.
      Clustering and UnsupervisedLearning are broader task/paradigm contexts; MachineLearningTask
      is generic. KernelLayer is a layer, PCA and DimensionalityReduction concern
      projections, Model is too broad, and neural RepresentationLearning/GraphConvolutionalNetwork
      do not describe the fixed-kernel procedures. Incrementally adding clusters with
      full reassignment need not form a nested cluster hierarchy, so HierarchicalClustering
      is not an identity match. Native KMeans is the linear-kernel special case; KernelPCA/SpectralHashing/PowerIterationClustering
      use different objectives or procedures. ExemplarBasedConvexClustering fits and
      hardens mixtures; the new CMM variant uses mixture exemplars only as candidate
      seeds for kernel variance minimization. MVKKM and MVSpec learn view weights
      rather than fixed observation weights. Mapping and absence are bounded to the
      pinned snapshot and inspected corpus.

      '
    evidence_ids:
    - mapping
- assessment_id: globalkernelkmeans
  area: evidence
  topic: Definition, identity, mechanism, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:GlobalKernelKMeans
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - singleton-proof
  - globalkernelkmeans-source-0
  summary: This is the Tzortzis-Likas2009 global kernel k-means procedure, including
    its positive observation-weight extension. It tries all datum candidates at each
    stage, unlike the fast one-candidate procedure or CMM-selected subset. Adding
    clusters is not an asserted nested hierarchy because local fitting can reassign
    all observations. The algorithm name does not certify a globally optimal partition.
    Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 492 prior
    native IDs, names and aliases; no normalized identity collision. Full searches
    of both checkouts include ignored and hidden files, returning 62 worktree and
    62 main matched lines. All 47 distinct matched texts were inspected as neighboring
    method mentions, query/frontier references or rendered copies. Eleven annotated
    AIO nodes, eleven generated YAMLs and seven native neighbors were examined. Nine
    unchanged annotated nodes, their generated YAMLs, all 442 class labels and 139
    semantic rows reuse byte-verified earlier readings; two additional annotated targets
    and eight new semantic rows were read (147 rows total). Absence is bounded to
    this pin and corpus.
  details: 'For a fixed PSD Gram matrix K, supplied cluster count M and positive observation
    weights a_i, represent each center as the weighted mean of its assigned RKHS features.
    For cluster C with A_C=sum_j_in_C a_j, compute squared distance K_ii - 2*sum_j_in_C
    a_j*K_ij/A_C + sum_j,l_in_C a_j*a_l*K_jl/A_C^2. Alternate synchronous nearest-center
    assignments and mean recomputation. Unit observation weights give unweighted kernel
    k-means. Scaling every a_i by the same positive constant preserves distances and
    fits while scaling the objective; these weights are not learned view weights.
    Begin with all N observations in one cluster. For k=2,...,M, use the retained
    (k-1)-cluster partition and try each datum x_n as a new singleton, removing it
    from its previous cluster while retaining the other groups. Run the local kernel-k-means
    procedure from each candidate and retain the least final weighted error for this
    stage. Observation weights change means and errors, not the stated all-datum candidate
    enumeration. For a symmetric nonnegative graph affinity A, ratio association uses
    unit observation weights and K=A. Normalized-cut optimization uses positive degrees
    d_i=sum_j A_ij as observation weights and K=D^(-1) A D^(-1). For fixed M these
    choices identify partition objective orderings, not all graph algorithms or their
    outputs. A sufficiently large shift lambda*I for ratio association, or lambda*D^(-1)
    for normalized cut, can ensure PSD. Either adds the partition-independent lambda*(N-M)
    to the corresponding weighted kernel objective while potentially changing local
    update paths. Zero-degree vertices require a convention. The source graph experiments
    used small shifts not necessarily ensuring PSD, so their observed convergence
    is not a general guarantee for indefinite similarities. This is a greedy sequence
    of local fits: it explores datum seeds conditional on the previously retained
    partition, not every partition or feature-space center. The source explicitly
    leaves near-optimality theory as future work. A reproducible deterministic result
    requires fixed tie, candidate-order and stopping policies. Removing a seed from
    an already singleton source cluster makes that cluster empty; the paper pseudocode
    does not provide its handling. The all-candidate search multiplies local fitting
    cost across stages. Limitations: PSD kernels, positive cluster weight and well-defined
    nonempty updates are conditions for the RKHS distance and descent arguments. Arbitrary
    similarities or arbitrary sigmoid-kernel parameters do not automatically satisfy
    them. Ties, empty clusters and stopping need explicit implementation conventions.
    Dense Gram storage is quadratic in N. Kernel choice, supplied cluster count and
    initialization affect results. No global optimum, approximation ratio, universal
    empirical superiority or biological causal interpretation is asserted. The primary
    papers use particular synthetic, digit, face, expression or graph settings, chosen
    kernels and parameters, and supplied cluster counts. Their finite comparisons
    do not establish universal performance. No historical implementation or benchmark
    was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A complete fixed-kernel clustering procedure, with its positive observation-weight
      parameterization; not a trained instance.
    evidence_ids:
    - globalkernelkmeans-source-0
  - name: aio-assessment
    value: related_match
    definition: 'Inspected eleven annotated AIO CLASS nodes and outgoing edges, eleven
      generated YAMLs and seven native neighbors. Nine annotated nodes, their generated
      YAMLs, all 442 class labels and 139 semantic rows reuse verified identical bytes
      from round122. Expanded graph/hierarchy/feature search adds eight inspected
      rows (147 total); HierarchicalClustering and GraphConvolutionalNetwork annotations
      and full YAMLs were newly read. Related AIO:UnsupervisedClustering maps algorithms
      to the task they perform, not equivalent identities or upstream subclasses.
      Clustering and UnsupervisedLearning are broader task/paradigm contexts; MachineLearningTask
      is generic. KernelLayer is a layer, PCA and DimensionalityReduction concern
      projections, Model is too broad, and neural RepresentationLearning/GraphConvolutionalNetwork
      do not describe the fixed-kernel procedures. Incrementally adding clusters with
      full reassignment need not form a nested cluster hierarchy, so HierarchicalClustering
      is not an identity match. Native KMeans is the linear-kernel special case; KernelPCA/SpectralHashing/PowerIterationClustering
      use different objectives or procedures. ExemplarBasedConvexClustering fits and
      hardens mixtures; the new CMM variant uses mixture exemplars only as candidate
      seeds for kernel variance minimization. MVKKM and MVSpec learn view weights
      rather than fixed observation weights. Mapping and absence are bounded to the
      pinned snapshot and inspected corpus.

      '
    evidence_ids:
    - mapping
- assessment_id: fastglobalkernelkmeans
  area: evidence
  topic: Definition, identity, mechanism, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:FastGlobalKernelKMeans
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - singleton-proof
  - fastglobalkernelkmeans-source-0
  summary: This is the Tzortzis-Likas2009 fast variant with its positive observation-weight
    extension. It maximizes a bound over datum seeds and performs one local fit per
    stage, rather than evaluating final errors for every seed or fitting a CMM exemplar
    shortlist. Maximizing the bound need not select the seed with greatest actual
    final improvement. Compared all 442 pinned AIO IDs, labels and scoped synonyms
    with all 492 prior native IDs, names and aliases; no normalized identity collision.
    Full searches of both checkouts include ignored and hidden files, returning 62
    worktree and 62 main matched lines. All 47 distinct matched texts were inspected
    as neighboring method mentions, query/frontier references or rendered copies.
    Eleven annotated AIO nodes, eleven generated YAMLs and seven native neighbors
    were examined. Nine unchanged annotated nodes, their generated YAMLs, all 442
    class labels and 139 semantic rows reuse byte-verified earlier readings; two additional
    annotated targets and eight new semantic rows were read (147 rows total). Absence
    is bounded to this pin and corpus.
  details: 'For a fixed PSD Gram matrix K, supplied cluster count M and positive observation
    weights a_i, represent each center as the weighted mean of its assigned RKHS features.
    For cluster C with A_C=sum_j_in_C a_j, compute squared distance K_ii - 2*sum_j_in_C
    a_j*K_ij/A_C + sum_j,l_in_C a_j*a_l*K_jl/A_C^2. Alternate synchronous nearest-center
    assignments and mean recomputation. Unit observation weights give unweighted kernel
    k-means. Scaling every a_i by the same positive constant preserves distances and
    fits while scaling the objective; these weights are not learned view weights.
    At each stage after the one-cluster start, let d_i be the squared distance to
    the retained old feature mean. For each datum n compute b_n=sum_i a_i*max(d_i-(K_ii+K_nn-2*K_in),0).
    Select a maximizer, create the corresponding singleton initialization, and run
    one local kernel-k-means fit. Unit weights recover the unweighted criterion. Candidate-scoring
    work remains even though only one local fit is performed per stage. For converged
    old assignments, positive residual cluster weights and well-defined exact nonempty
    local updates, the source bound is E_new<=E_old-b_n. Although removing the seed
    changes its previous cluster mean, a weighted RKHS comparison shows that this
    shift does not raise the aggregate comparison cost, so the bound extends to the
    displayed singleton-removal initialization under those conditions. It is a bound
    on one stage, not a global approximation guarantee or proof that the selected
    seed maximizes actual final improvement. Empty-cluster repairs, indefinite similarities
    or approximate updates need separate justification. For a symmetric nonnegative
    graph affinity A, ratio association uses unit observation weights and K=A. Normalized-cut
    optimization uses positive degrees d_i=sum_j A_ij as observation weights and K=D^(-1)
    A D^(-1). For fixed M these choices identify partition objective orderings, not
    all graph algorithms or their outputs. A sufficiently large shift lambda*I for
    ratio association, or lambda*D^(-1) for normalized cut, can ensure PSD. Either
    adds the partition-independent lambda*(N-M) to the corresponding weighted kernel
    objective while potentially changing local update paths. Zero-degree vertices
    require a convention. The source graph experiments used small shifts not necessarily
    ensuring PSD, so their observed convergence is not a general guarantee for indefinite
    similarities. Limitations: PSD kernels, positive cluster weight and well-defined
    nonempty updates are conditions for the RKHS distance and descent arguments. Arbitrary
    similarities or arbitrary sigmoid-kernel parameters do not automatically satisfy
    them. Ties, empty clusters and stopping need explicit implementation conventions.
    Dense Gram storage is quadratic in N. Kernel choice, supplied cluster count and
    initialization affect results. No global optimum, approximation ratio, universal
    empirical superiority or biological causal interpretation is asserted. The primary
    papers use particular synthetic, digit, face, expression or graph settings, chosen
    kernels and parameters, and supplied cluster counts. Their finite comparisons
    do not establish universal performance. No historical implementation or benchmark
    was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A complete fixed-kernel clustering procedure, with its positive observation-weight
      parameterization; not a trained instance.
    evidence_ids:
    - fastglobalkernelkmeans-source-0
  - name: aio-assessment
    value: related_match
    definition: 'Inspected eleven annotated AIO CLASS nodes and outgoing edges, eleven
      generated YAMLs and seven native neighbors. Nine annotated nodes, their generated
      YAMLs, all 442 class labels and 139 semantic rows reuse verified identical bytes
      from round122. Expanded graph/hierarchy/feature search adds eight inspected
      rows (147 total); HierarchicalClustering and GraphConvolutionalNetwork annotations
      and full YAMLs were newly read. Related AIO:UnsupervisedClustering maps algorithms
      to the task they perform, not equivalent identities or upstream subclasses.
      Clustering and UnsupervisedLearning are broader task/paradigm contexts; MachineLearningTask
      is generic. KernelLayer is a layer, PCA and DimensionalityReduction concern
      projections, Model is too broad, and neural RepresentationLearning/GraphConvolutionalNetwork
      do not describe the fixed-kernel procedures. Incrementally adding clusters with
      full reassignment need not form a nested cluster hierarchy, so HierarchicalClustering
      is not an identity match. Native KMeans is the linear-kernel special case; KernelPCA/SpectralHashing/PowerIterationClustering
      use different objectives or procedures. ExemplarBasedConvexClustering fits and
      hardens mixtures; the new CMM variant uses mixture exemplars only as candidate
      seeds for kernel variance minimization. MVKKM and MVSpec learn view weights
      rather than fixed observation weights. Mapping and absence are bounded to the
      pinned snapshot and inspected corpus.

      '
    evidence_ids:
    - mapping
- assessment_id: convexmixtureinitializedglobalkernelkmeans
  area: evidence
  topic: Definition, identity, mechanism, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - singleton-proof
  - convexmixtureinitializedglobalkernelkmeans-source-0
  summary: This is the Tzortzis-Likas2009 global kernel k-means with CMM procedure,
    including its positive observation-weight extension. It uses mixture weights to
    restrict initialization candidates, while final partitions optimize kernel variance
    over all observations. It is not the original CMM hard-clustering output, all-datum
    global search, fast bound maximization, or multiview mixture weighting. Compared
    all 442 pinned AIO IDs, labels and scoped synonyms with all 492 prior native IDs,
    names and aliases; no normalized identity collision. Full searches of both checkouts
    include ignored and hidden files, returning 62 worktree and 62 main matched lines.
    All 47 distinct matched texts were inspected as neighboring method mentions, query/frontier
    references or rendered copies. Eleven annotated AIO nodes, eleven generated YAMLs
    and seven native neighbors were examined. Nine unchanged annotated nodes, their
    generated YAMLs, all 442 class labels and 139 semantic rows reuse byte-verified
    earlier readings; two additional annotated targets and eight new semantic rows
    were read (147 rows total). Absence is bounded to this pin and corpus.
  details: 'For a fixed PSD Gram matrix K, supplied cluster count M and positive observation
    weights a_i, represent each center as the weighted mean of its assigned RKHS features.
    For cluster C with A_C=sum_j_in_C a_j, compute squared distance K_ii - 2*sum_j_in_C
    a_j*K_ij/A_C + sum_j,l_in_C a_j*a_l*K_jl/A_C^2. Alternate synchronous nearest-center
    assignments and mean recomputation. Unit observation weights give unweighted kernel
    k-means. Scaling every a_i by the same positive constant preserves distances and
    fits while scaling the objective; these weights are not learned view weights.
    For a supplied positive beta, set S_ij=exp(-beta*(K_ii+K_jj-2*K_ij)). With empirical
    p_i=a_i/sum_l a_l and positive simplex q over eligible exemplars, form z_i=sum_j
    S_ij*q_j and update q_j<-q_j*sum_i p_i*S_ij/z_i. The unweighted case has p_i=1/N.
    Fit this finite positive-affinity log-mixture criterion once, then select the
    P highest-weight exemplars. The source stops when their identities and ordering
    stay unchanged for a number of consecutive iterations, rather than requiring objective
    convergence; that iteration count and tie policies need specification. Starting
    from one cluster, for each k=2,...,M try each of the selected P exemplar data
    as a new singleton removed from its previous group, run local kernel k-means on
    all N observations, and retain the least-error fit. The source recommends M<P
    much smaller than N when useful, with P supplied. Restricting seeds reduces local
    fits but does not guarantee the same trajectory or objective as all-datum global
    search; singleton-source and later empty clusters still require conventions. The
    source beta reference is N*H(p)/sum_ij p_i*distance(i,j)^2, reducing to N^2*log(N)/sum_ij
    distance(i,j)^2 for uniform p; it is an empirical scale guide and is undefined
    for a zero denominator. Stable top-P ranking does not certify an optimized mixture
    or globally optimal final partition. The finite log-affinity criterion is meaningful
    without assuming a normalized Gaussian density on an arbitrary RKHS; atomic-to-continuous
    KL language needs a common measure. Duplicate zero-distance observations also
    qualify the appendix identification of zero-distortion rate with H(p). For a symmetric
    nonnegative graph affinity A, ratio association uses unit observation weights
    and K=A. Normalized-cut optimization uses positive degrees d_i=sum_j A_ij as observation
    weights and K=D^(-1) A D^(-1). For fixed M these choices identify partition objective
    orderings, not all graph algorithms or their outputs. A sufficiently large shift
    lambda*I for ratio association, or lambda*D^(-1) for normalized cut, can ensure
    PSD. Either adds the partition-independent lambda*(N-M) to the corresponding weighted
    kernel objective while potentially changing local update paths. Zero-degree vertices
    require a convention. The source graph experiments used small shifts not necessarily
    ensuring PSD, so their observed convergence is not a general guarantee for indefinite
    similarities. Limitations: PSD kernels, positive cluster weight and well-defined
    nonempty updates are conditions for the RKHS distance and descent arguments. Arbitrary
    similarities or arbitrary sigmoid-kernel parameters do not automatically satisfy
    them. Ties, empty clusters and stopping need explicit implementation conventions.
    Dense Gram storage is quadratic in N. Kernel choice, supplied cluster count and
    initialization affect results. No global optimum, approximation ratio, universal
    empirical superiority or biological causal interpretation is asserted. The primary
    papers use particular synthetic, digit, face, expression or graph settings, chosen
    kernels and parameters, and supplied cluster counts. Their finite comparisons
    do not establish universal performance. No historical implementation or benchmark
    was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A complete fixed-kernel clustering procedure, with its positive observation-weight
      parameterization; not a trained instance.
    evidence_ids:
    - convexmixtureinitializedglobalkernelkmeans-source-0
  - name: aio-assessment
    value: related_match
    definition: 'Inspected eleven annotated AIO CLASS nodes and outgoing edges, eleven
      generated YAMLs and seven native neighbors. Nine annotated nodes, their generated
      YAMLs, all 442 class labels and 139 semantic rows reuse verified identical bytes
      from round122. Expanded graph/hierarchy/feature search adds eight inspected
      rows (147 total); HierarchicalClustering and GraphConvolutionalNetwork annotations
      and full YAMLs were newly read. Related AIO:UnsupervisedClustering maps algorithms
      to the task they perform, not equivalent identities or upstream subclasses.
      Clustering and UnsupervisedLearning are broader task/paradigm contexts; MachineLearningTask
      is generic. KernelLayer is a layer, PCA and DimensionalityReduction concern
      projections, Model is too broad, and neural RepresentationLearning/GraphConvolutionalNetwork
      do not describe the fixed-kernel procedures. Incrementally adding clusters with
      full reassignment need not form a nested cluster hierarchy, so HierarchicalClustering
      is not an identity match. Native KMeans is the linear-kernel special case; KernelPCA/SpectralHashing/PowerIterationClustering
      use different objectives or procedures. ExemplarBasedConvexClustering fits and
      hardens mixtures; the new CMM variant uses mixture exemplars only as candidate
      seeds for kernel variance minimization. MVKKM and MVSpec learn view weights
      rather than fixed observation weights. Mapping and absence are bounded to the
      pinned snapshot and inspected corpus.

      '
    evidence_ids:
    - mapping
- assessment_id: algorithm-identities
  area: consistency
  topic: Local updates versus three seed policies
  outcome: supported
  target_ids:
  - AIMech:KernelKMeans
  - AIMech:GlobalKernelKMeans
  - AIMech:FastGlobalKernelKMeans
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
  evidence_ids:
  - neighbors
  - identity
  summary: Retain all four complete procedures.
  details: KernelKMeans specifies a local partition/mean update for a supplied kernel.
    Global tries all datum seeds at every incremental stage; FastGlobal chooses one
    by a bound; the CMM version fits an exemplar shortlist once and tries its members
    at each stage. Shared local updates do not erase different searches. Positive
    observation weighting is an input parameterization within each algorithm, with
    unit weights as a special case, rather than eight duplicate local identities.
    Full reassignment does not ensure a nested cluster hierarchy.
- assessment_id: weighted-distances-and-relaxation
  area: consistency
  topic: Gram means and spectral objective connection
  outcome: supported
  target_ids:
  - AIMech:KernelKMeans
  - AIMech:GlobalKernelKMeans
  - AIMech:FastGlobalKernelKMeans
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
  evidence_ids:
  - kernelkmeans-source-0
  - kernelkmeans-source-1
  - finite-boundaries
  summary: Preserve positive-weight, PSD and discrete-partition conditions.
  details: The displayed weighted Gram distance equals direct squared distance to
    a weighted mean in the finite linear example (objective 4.75); uniform weight
    scaling preserves distances and scales errors. Orthonormal spectral relaxation
    removes discrete indicator structure, so a leading eigenspace and its rounding
    do not certify the best discrete partition or identical algorithm outputs. Fixed
    observation weights differ from learned view weights.
- assessment_id: global-and-empty-clusters
  area: consistency
  topic: Greedy search, deterministic policies and unsupported optimality
  outcome: supported
  target_ids:
  - AIMech:GlobalKernelKMeans
  - AIMech:FastGlobalKernelKMeans
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
  evidence_ids:
  - globalkernelkmeans-source-0
  - fastglobalkernelkmeans-source-0
  - convexmixtureinitializedglobalkernelkmeans-source-0
  summary: Keep implementation gaps and guarantee limits explicit.
  details: The primary paper leaves near-optimality theory open. All-datum initialization
    searches conditionally on the previously retained partition, not all partitions.
    The fast criterion maximizes a bound, not measured final improvement. A singleton
    source cluster becomes empty on removal, and later Lloyd steps can also create
    empty groups; no unrestricted repair guarantee is asserted. Tie, stopping and
    candidate conventions are needed for a reproducible deterministic implementation.
- assessment_id: fast-singleton-bound
  area: consistency
  topic: Conditional stage-wise upper error bound
  outcome: supported
  target_ids:
  - AIMech:FastGlobalKernelKMeans
  evidence_ids:
  - fastglobalkernelkmeans-source-0
  - singleton-proof
  - finite-boundaries
  summary: The singleton-removal concern is resolved, not a source defect.
  details: At a converged old partition, choose the comparison assignment using old
    means plus the new datum center. In the seed source cluster, every transferred
    observation has twice its centered inner product with the seed vector at least
    the seed squared norm. The removed weight B includes the seed weight a. Recomputing
    the remaining mean changes aggregate comparison cost by at most a*W*(a-B)*norm(z)^2/(W-a)^2<=0.
    Nearest reassignment and weighted-mean updates cannot increase that cost. Positive
    residual weight, PSD geometry and defined nonempty exact updates are essential.
    Six finite linear/RBF examples agree. The 10000-dataset exploratory probe was
    not itself a proof.
- assessment_id: graph-shift-scope
  area: consistency
  topic: Objective equivalence versus optimization paths
  outcome: supported
  target_ids:
  - AIMech:KernelKMeans
  - AIMech:GlobalKernelKMeans
  - AIMech:FastGlobalKernelKMeans
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
  evidence_ids:
  - kernelkmeans-source-0
  - globalkernelkmeans-source-0
  - finite-boundaries
  summary: Preserve fixed-M constants, degree conditions and PSD limits.
  details: For ratio association and normalized cut, the appropriate diagonal shift
    adds lambda*(N-M); six finite checks give 10 at N=4,M=2,lambda=5. Pre-shift indefinite
    matrices can have negative algebraic values, not valid nonnegative RKHS errors.
    A sufficient shift preserves partition objective ordering but can change local
    trajectories. The papers do not establish convergence for every indefinite similarity.
    The 2004 averaged normalized-cut convention differs by a fixed factor from its
    later unaveraged display; the records assert orderings, not incompatible numerical
    equalities.
- assessment_id: cmm-selection-and-scale
  area: consistency
  topic: Candidate fitting, ranking stopping and density interpretation
  outcome: supported
  target_ids:
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
  evidence_ids:
  - convexmixtureinitializedglobalkernelkmeans-source-0
  - neighbors
  - finite-boundaries
  summary: Keep CMM as seed selection and qualify its scale heuristic.
  details: The final fit uses all N observations and kernel variance, not the original
    CMM hard assignments. Finite iterations 4 and 5 preserve exemplar ordering while
    changing q and improving the log score, so stable ranking does not certify objective
    convergence. The beta guide requires a nonzero denominator and does not tune all
    model choices. Gaussian-density and atomic/continuous KL claims need their measure
    assumptions; duplicate identical observations can attain zero distortion with
    zero information despite positive empirical entropy.
- assessment_id: identity-mapping-and-frontier
  area: grounding
  topic: Bounded duplicate search and mapping
  outcome: supported
  target_ids:
  - AIMech:KernelKMeans
  - AIMech:GlobalKernelKMeans
  - AIMech:FastGlobalKernelKMeans
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Keep native DRAFT status and related task mappings.
  details: All 442 AIO and 492 previous native identities were compared. Ignored-inclusive
    searches found 62 lines in each checkout, 47 distinct texts at 124 locations,
    all inspected as references or neighboring procedures and generated copies. The
    eleven annotated targets and eighteen contextual YAMLs support related UnsupervisedClustering
    mappings without equivalence to tasks, kernel layers, PCA projections, neural
    graph models or a nested hierarchy. There remain 417 pending cohorts, so this
    review is not saturation or corpus-wide scientific approval.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:KernelKMeans
  - AIMech:GlobalKernelKMeans
  - AIMech:FastGlobalKernelKMeans
  - AIMech:ConvexMixtureInitializedGlobalKernelKMeans
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - singleton-proof
  - kernelkmeans-source-0
  - kernelkmeans-source-1
  - globalkernelkmeans-source-0
  - fastglobalkernelkmeans-source-0
  - convexmixtureinitializedglobalkernelkmeans-source-0
  rationale: The local update and three initialization policies define different complete
    algorithms. Unit and positive observation-weight cases share each procedure parameterization.
    Related AIO task mappings preserve abstraction boundaries without upstream subclass
    assertions.
limitations:
- Adversarial author self-review only; all four records remain DRAFT.
- All fourteen Tzortzis2009 and six Dhillon2004 pages were visually read, including
  formulas, tables, figures and references. The 2009 printed-page offset is 1180;
  the 2004 author manuscript has no visible printed page numbers.
- Positive observation weights, nonempty cluster weights, PSD kernels and exact local
  updates delimit the descent and seed-bound claims. The named global search is greedy
  initialization, not a global-optimality or approximation-ratio certificate.
- A concern about the fast bound under singleton-removal initialization was investigated
  and resolved by a weighted RKHS comparison, not reported as a paper defect. A separate
  seeded 10000-dataset probe found no counterexample under defined runs; only the
  derivation supports the general conditional argument.
- Finite graph checks include algebraic pre-shift values for indefinite affinities;
  negative values there are not asserted RKHS squared errors. Sufficient PSD shifts
  preserve fixed-count objective ordering while possibly changing update paths.
- CMM exemplar ranking can stabilize before optimization; its beta rule is empirical
  and needs nonzero denominator. Finite affinity fitting does not by itself define
  a normalized Gaussian on arbitrary RKHS or an atomic-to-continuous KL.
- No historical code, benchmark, trained model, paid service or complete-paper redistribution.
  The downloaded twelve-page maximum-margin paper is not yet fully read.
- Four additions bring the native collection to 496; 442 pinned AIO records are unchanged.
  There are 417 pending frontier cohorts and other unresolved dispositions; no saturation.
links: []
tags:
- native-concepts
- global-kernel
- self-review
- discovery-ongoing
```
