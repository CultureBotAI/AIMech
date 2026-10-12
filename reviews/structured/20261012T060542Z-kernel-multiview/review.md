# Scientific self-review of multiview kernel k-means and weighted spectral clustering

- Review: 20261012T060542Z-kernel-multiview
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T05:58:53Z
- Finished UTC: 2026-10-12T06:05:42Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain source-specific MVKKM and MVSpec as separate algorithms with qualified weight, normalization, convergence and discretization boundaries. No actionable curation finding was identified in the final two records.

## Scope And Provenance

All fields of two source-defined multiview kernel clustering algorithms.

Selection: Exact maintained IDs MultiviewKernelKMeans and WeightedMultiviewSpectralClustering; all selected records without sampling.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base f94447a06ab242944771dbe643c953474a178c0d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:MultiviewKernelKMeans | data/curated/MultiviewKernelKMeans.yaml | maintained | Multiview Kernel K-Means |
| AIMech:WeightedMultiviewSpectralClustering | data/curated/WeightedMultiviewSpectralClustering.yaml | maintained | Weighted Multiview Spectral Clustering |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:MultiviewKernelKMeans, AIMech:WeightedMultiviewSpectralClustering | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 158.58s (0:02:38)<br>Checked 442 record(s); 0 failed.<br>Checked 492 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 146 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 143,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:MultiviewKernelKMeans, AIMech:WeightedMultiviewSpectralClustering | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:MultiviewKernelKMeans, AIMech:WeightedMultiviewSpectralClustering | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:MultiviewKernelKMeans, AIMech:WeightedMultiviewSpectralClustering | Command exited 0 with no output. |
| Kernel multiview boundaries | passed | True | AIMech:MultiviewKernelKMeans, AIMech:WeightedMultiviewSpectralClustering | {"status": "passed", "positive_residual_weights": [0.8, 0.2], "objective": 0.8, "large_p_weights": [0.5000346573589725, 0.4999653426410275], "large_p_normalized_coefficients": [0.8000221797873109, 0.19997782021268906], "spectral_fixed_point": {"initial_objective": 0.25, "perturbed_objective": 0.24990001333262224, "perturbed_weights": [0.4900006666533335, 0.5099993333466665], "eigenvalue_tie": true}, "constant_kernel_mean_squared_distance": 0.0} |

## Scientific And Domain Assessments

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:MultiviewKernelKMeans.

This is the Tzortzis-Likas 2012 MVKKM procedure. It maintains a discrete common partition while learning view weights. It differs from MVSpec, which optimizes an orthonormal relaxation before final discretization, and from exemplar-based multiview mixture methods, which fit log-mixture objectives. Its kernel-k-means component does not make the complete procedure ordinary input-space k-means or kernel PCA. MVKKM is the source-specific alias. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 490 preceding native IDs, names and aliases; no normalized identity collision. Full searches of both checkouts include ignored and hidden files, with 5 matched lines in the worktree and 5 in main. All 3 distinct matched texts were inspected as source-query and frontier references. Nine annotated AIO nodes, nine generated YAMLs and seven native contextual YAMLs were assessed. Seven unchanged annotated nodes and generated records, all 442 class labels and 138 semantic rows reuse byte-verified earlier readings; two additional targets and the KernelLayer semantic row were read, giving 139 semantic rows. Absence is bounded to this snapshot and corpus.

Given N aligned observations, V fixed positive-semidefinite view Gram matrices K_v, a supplied cluster count M and exponent p&gt;=1, form Ktilde=sum_v w_v^p K_v with nonnegative w and sum_v w_v=1. The actual kernel coefficients are w_v^p, which need not sum to one. Their feature map concatenates the view features scaled by sqrt(w_v^p). The supplied kernels, M and p are not all learned by this procedure. Maintain M nonempty clusters with normalized indicator matrix Y_ik=1[i in C_k]/sqrt(&#124;C_k&#124;). For fixed view weights, apply kernel k-means to Ktilde, initializing from the preceding partition. For fixed clusters, use D_v=tr(K_v)-tr(Y^T K_v Y), equal to the sum of squared distances to view-specific feature means, and update w by the conditional weight solution. The paper starts view weights uniformly and initializes the partition through the named global kernel k-means procedure; that initialization is a heuristic, not a certificate of global optimality. For fixed positive residuals D_v and p&gt;1, minimize sum_v D_v*w_v^p on the simplex using w_v=D_v^(-1/(p-1))/sum_u D_u^(-1/(p-1)). This gives positive weights for every positive residual. If some residuals are zero, the ratio formula is undefined; any weights supported entirely on zero-residual views minimize the block. At p=1, select a minimum-residual view as in the source, while ties mathematically permit any simplex distribution over minimizers. Neither zero-residual nor tied cases imply a unique weight vector. For fixed positive residuals, increasing p makes the simplex weight ratio (D_u/D_v)^(1/(p-1)) approach one. The ratio of actual kernel coefficients is (D_u/D_v)^(p/(p-1)); as p grows it approaches D_u/D_v, not generally one. Thus nearly uniform w does not imply uniform effective kernel contributions. The source uses sparsity to describe relative concentration; finite p&gt;1 with positive residuals does not select exact zeros. The power-of-simplex constraint is not an asserted equivalence to every conventional lp multiple-kernel regularizer. View residual scales affect the learned weights. The source divides each view kernel by its mean pairwise squared feature distance, N^(-2)*sum_ij(K_vii-2*K_vij+K_vjj), to make scales comparable. This denominator vanishes for a constant feature view and needs an explicit convention. Such normalization does not establish that weights quantify semantic reliability or that a method is immune to uninformative views. Admissible kernel-k-means updates and exact weight minimization do not increase the shared within-cluster objective. Its nonnegativity supports objective-value convergence, while the selected partition remains initialization dependent. Nonempty clusters, tie handling and numerical stopping require explicit conventions. The procedure does not promise a globally best joint partition and weighting or unique parameters, and the source word global in the initialization algorithm name is not such a guarantee. Limitations: The input must provide aligned views and valid PSD kernels. An arbitrary similarity matrix is not automatically an RKHS Gram matrix. Kernel selection, requested cluster count and p remain modeling choices. Dense Gram matrices require storage quadratic in N per view; the source uses repeated clustering or eigensolutions, with additional initialization cost. No general scalability or global-optimum guarantee is curated. Source experiments use known class counts, parameter sweeps, selected digit/image subsets and specific preprocessing; their NMI results do not establish universal superiority or label-free model selection. No historical software or benchmark was reproduced.

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:WeightedMultiviewSpectralClustering.

This is the Tzortzis-Likas 2012 MVSpec procedure; the local descriptive name is qualified by that source-specific identity. It is not every weighted multiview spectral method. Unlike MVKKM, it keeps an orthonormal embedding rather than a discrete partition during weight fitting. It differs from normalized-Laplacian graph clustering, power iteration clustering, kernel PCA and binary spectral hashing; a shared eigenvector operation does not establish equivalence. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 490 preceding native IDs, names and aliases; no normalized identity collision. Full searches of both checkouts include ignored and hidden files, with 5 matched lines in the worktree and 5 in main. All 3 distinct matched texts were inspected as source-query and frontier references. Nine annotated AIO nodes, nine generated YAMLs and seven native contextual YAMLs were assessed. Seven unchanged annotated nodes and generated records, all 442 class labels and 138 semantic rows reuse byte-verified earlier readings; two additional targets and the KernelLayer semantic row were read, giving 139 semantic rows. Absence is bounded to this snapshot and corpus.

Given N aligned observations, V fixed positive-semidefinite view Gram matrices K_v, a supplied cluster count M and exponent p&gt;=1, form Ktilde=sum_v w_v^p K_v with nonnegative w and sum_v w_v=1. The actual kernel coefficients are w_v^p, which need not sum to one. Their feature map concatenates the view features scaled by sqrt(w_v^p). The supplied kernels, M and p are not all learned by this procedure. For fixed w, choose N-by-M Y with Y^T Y=I spanning a leading M-dimensional eigenspace of the raw composite kernel Ktilde. This minimizes tr(Ktilde)-tr(Y^T Ktilde Y) over that relaxed set. Then compute D_v=tr(K_v)-tr(Y^T K_v Y) and update w by the conditional weight solution. Repeat without discretizing Y between weight updates. The paper starts w uniformly and applies k-means-based discretization to the final eigenvector embedding after convergence. That postprocessing is separate from the relaxed optimization and may lose its optimal value. For fixed positive residuals D_v and p&gt;1, minimize sum_v D_v*w_v^p on the simplex using w_v=D_v^(-1/(p-1))/sum_u D_u^(-1/(p-1)). This gives positive weights for every positive residual. If some residuals are zero, the ratio formula is undefined; any weights supported entirely on zero-residual views minimize the block. At p=1, select a minimum-residual view as in the source, while ties mathematically permit any simplex distribution over minimizers. Neither zero-residual nor tied cases imply a unique weight vector. For fixed positive residuals, increasing p makes the simplex weight ratio (D_u/D_v)^(1/(p-1)) approach one. The ratio of actual kernel coefficients is (D_u/D_v)^(p/(p-1)); as p grows it approaches D_u/D_v, not generally one. Thus nearly uniform w does not imply uniform effective kernel contributions. The source uses sparsity to describe relative concentration; finite p&gt;1 with positive residuals does not select exact zeros. The power-of-simplex constraint is not an asserted equivalence to every conventional lp multiple-kernel regularizer. View residual scales affect the learned weights. The source divides each view kernel by its mean pairwise squared feature distance, N^(-2)*sum_ij(K_vii-2*K_vij+K_vjj), to make scales comparable. This denominator vanishes for a constant feature view and needs an explicit convention. Such normalization does not establish that weights quantify semantic reliability or that a method is immune to uninformative views. Exact spectral and weight block updates do not increase the nonnegative relaxed objective, so its values converge. This alone does not prove unique parameter convergence or that every coordinatewise fixed point is a joint local minimum. For K_1=diag(1,0), K_2=diag(0,1), M=1 and p=2, w=(1/2,1/2) gives a tied composite eigenspace. Choosing Y=(1,1)/sqrt(2) is a valid fixed spectral/weight update with objective 1/4, yet an arbitrarily small joint rotation and weight adjustment lowers the objective. This curator example qualifies the source local-minimum claim under allowed eigenvalue ties; it does not reproduce the source experiments. Limitations: The input must provide aligned views and valid PSD kernels. An arbitrary similarity matrix is not automatically an RKHS Gram matrix. Kernel selection, requested cluster count and p remain modeling choices. Dense Gram matrices require storage quadratic in N per view; the source uses repeated clustering or eigensolutions, with additional initialization cost. No general scalability or global-optimum guarantee is curated. Source experiments use known class counts, parameter sweeps, selected digit/image subsets and specific preprocessing; their NMI results do not establish universal superiority or label-free model selection. No historical software or benchmark was reproduced.

### Complete algorithm identities

consistency: supported. Targets: AIMech:MultiviewKernelKMeans, AIMech:WeightedMultiviewSpectralClustering.

Retain MVKKM and MVSpec separately.

Both share fixed PSD kernels, simplex weights and a power-weighted variance objective. MVKKM keeps a normalized indicator of a discrete partition and applies kernel k-means; MVSpec allows any orthonormal embedding and takes leading composite-kernel eigenvectors. Only the latter delays discretization until after fitting. Their final groupings and learned weights need not agree. Neither is equivalent to the exemplar-mixture likelihood algorithms, kernel PCA, spectral hashing or early-stopped power iteration.

### Conditional minimizers and missing ratio cases

consistency: supported. Targets: AIMech:MultiviewKernelKMeans, AIMech:WeightedMultiviewSpectralClustering.

State positive, zero and tied-residual cases explicitly.

The displayed inverse-residual formula is valid for p&gt;1 and strictly positive residuals. Zero residuals permit support entirely on their zero set; multiple zeros can make solutions nonunique. At p=1, any simplex mass over tied minimum residuals is optimal, so not every optimum must be a vertex. Positive residuals and finite p&gt;1 yield positive coefficients; the source sparsity discussion concerns relative concentration.

### Simplex weights versus effective kernel coefficients

consistency: supported. Targets: AIMech:MultiviewKernelKMeans, AIMech:WeightedMultiviewSpectralClustering.

Keep the large-p limits and scale sensitivity distinct.

For fixed D=(1,4), p=2 gives w=(.8,.2). At p=10001 the weights are approximately (.500034657,.499965343) but normalized effective coefficients are approximately (.80002218,.19997782). The coefficient ratio exponent p/(p-1) approaches one, leaving inverse-residual ratios rather than uniform contributions. Kernel rescaling changes D and weights; the mean pairwise squared-distance normalization is undefined for a constant view. None of these facts makes learned weights pure measures of semantic quality.

### Blockwise optimality versus a joint local minimum

consistency: supported. Targets: AIMech:WeightedMultiviewSpectralClustering.

Qualify the source convergence claim under allowed eigenvalue ties.

With K1=diag(1,0), K2=diag(0,1), M=1 and p=2, equal weights give .25 I. The unit vector at angle pi/4 is therefore a valid leading eigenvector; equal weights also minimize its weight block. The point is fixed under permissible tie choices with objective .25. Rotate by epsilon and minimize the weight block: the objective becomes .25*cos(2*epsilon)^2, strictly less for arbitrarily small nonzero epsilon. This is a coordinatewise fixed point that is not a joint local minimum. Exact block descent still ensures convergent objective values; the counterexample does not refute that weaker conclusion.

### Initialization, rounding and benchmark scope

consistency: supported. Targets: AIMech:MultiviewKernelKMeans, AIMech:WeightedMultiviewSpectralClustering.

Preserve the source-specific procedure and avoid transferred guarantees.

MVKKM uses a named deterministic global kernel k-means initialization; its name does not certify a globally optimal fit. MVSpec fits a continuous orthonormal solution then discretizes with k-means, so the relaxed optimum is not guaranteed for the resulting partition. The source uses known class counts, parameter sweeps, representative subsets and preprocessing. Figures and tables do not establish universal superiority or intrinsically label-free selection.

### Bounded identity scope and algorithm-to-task mapping

grounding: supported. Targets: AIMech:MultiviewKernelKMeans, AIMech:WeightedMultiviewSpectralClustering.

Keep native DRAFT status and the related UnsupervisedClustering mapping.

Ignored-inclusive searches returned five matching lines per checkout and three distinct texts, all source-query/frontier references. All 442 AIO and 490 prior native identities were compared. The nine annotated targets and sixteen contextual YAMLs do not identify these complete algorithms with a dot-product layer, PCA projection, neural representation learning or dimensionality-reduction task. 413 pending cohorts remain outside this selected review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:MultiviewKernelKMeans, AIMech:WeightedMultiviewSpectralClustering. MVKKM alternates discrete partitions and kernel weights; MVSpec alternates a leading-eigenspace relaxation and weights before final discretization. The common variance framework does not identify their optimization paths or final partitions. Related AIO task mappings preserve abstraction without upstream subclass assertions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T055803Z-kernel-multiview.json | supports | Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 490 preceding native IDs, names and aliases; no normalized identity collision. Full searches of both checkouts include ignored and hidden files, with 5 matched lines in the worktree and 5 in main. All 3 distinct matched texts were inspected as source-query and frontier references. Nine annotated AIO nodes, nine generated YAMLs and seven native contextual YAMLs were assessed. Seven unchanged annotated nodes and generated records, all 442 class labels and 138 semantic rows reuse byte-verified earlier readings; two additional targets and the KernelLayer semantic row were read, giving 139 semantic rows. Absence is bounded to this snapshot and corpus.<br> |
| mapping | sources/aio/aio.json; Nine annotated CLASS nodes with outgoing edges; 139 semantic rows and all 442 class labels, including byte-verified prior readings | supports | Both source-specific procedures group unlabeled aligned views. UnsupervisedClustering is the closest inspected task association, so related_match avoids algorithm/task equivalence or subclass assertions. Broader Clustering, UnsupervisedLearning and MachineLearningTask are less specific. KernelLayer denotes a dot-product layer, Model a representation, PCA a variance projection and DimensionalityReduction a different task; the pin’s neural RepresentationLearning definition does not identify these kernel procedures. Eigenvectors and dot products alone do not establish those alternative mappings.<br> |
| neighbors | research/discovery/20261012T055803Z-kernel-multiview.json; source_analysis.aio_mapping_inspection: nine generated and seven native contextual YAMLs | supports | K-means, kernel PCA, spectral hashing, power iteration clustering and the three exemplar mixture algorithms distinguish the new source-specific procedures. Seven generated records and annotated targets reuse verified identical bytes; KernelLayer and PCA annotations and YAMLs were additionally read. All seven native records were read in this working session. No contextual record receives renewed scientific approval. |
| finite-boundaries | research/discovery/kernel-multiview-boundaries.py; Positive and zero residuals, tied minima, weight/coefficient limits, normalization and a spectral fixed saddle | supports | Finite examples test positive-residual weight minimization, tied p=1 minima, zero residuals, large-p effective coefficient ratios, kernel scaling, constant-view normalization and a coordinatewise spectral fixed point with a nearby lower joint objective. They are curator mathematical illustrations, not historical benchmark reproduction. |
| multiviewkernelkmeans-source-0 | https://www.cs.uoi.gr/~arly/full/conferences/C78.pdf; Section III-A, PDF p. 2, Equations 1-2; Section IV-B.1/3/5, PDF p. 4; Equation 8; Section IV-A, PDF p. 3, Equations 4-7; Section IV-B, PDF p. 4, Equations 9-10; Appendices A-B, PDF p. 10, Equations 11-18; curator zero-residual and tied-minimum checks; Section IV-B.1/5, PDF p. 4; Section IV-C, PDF p. 5; source discussion of initialization and local optimization; Section IV-C, PDF p. 5, last paragraph; Section V-B, PDF pp. 6-7; curator constant-kernel and rescaling checks; Section IV-C, PDF pp. 4-5; Equation 4 and related norm discussion, PDF p. 3; curator large-p calculation; Sections III-A and IV, PDF pp. 2-5, Equations 1-2 and 4-10; Appendix A, PDF p. 10 | supports | Kernel-based Weighted Multi-view Clustering. Author-hosted ten-page manuscript corresponding to ICDM 2012, pp. 675-684. This PDF has no visible printed page numbering; locators use PDF pages. All ten pages, tables, figures and appendices visually read. Original printed statements and curator qualifications are distinguished; finite calculations are not historical empirical reproduction. |
| weightedmultiviewspectralclustering-source-0 | https://www.cs.uoi.gr/~arly/full/conferences/C78.pdf; Section III-B, PDF p. 3, Equation 3; Section IV-B.2/4/5, PDF p. 4; Section IV-C, PDF p. 5; Appendix B, PDF p. 10; Section IV-A, PDF p. 3, Equations 4-7; Section IV-B, PDF p. 4, Equations 9-10; Appendices A-B, PDF p. 10, Equations 11-18; curator zero-residual and tied-minimum checks; Section IV-C, PDF p. 5, convergence discussion; Appendix B, PDF p. 10; curator two-kernel fixed-point calculation; Section IV-C, PDF p. 5, last paragraph; Section V-B, PDF pp. 6-7; curator constant-kernel and rescaling checks; Section IV-C, PDF pp. 4-5; Equation 4 and related norm discussion, PDF p. 3; curator large-p calculation; Sections III-B and IV, PDF pp. 3-5, Equations 3-4 and 8-10; Appendix B, PDF p. 10 | supports | Kernel-based Weighted Multi-view Clustering. Author-hosted ten-page manuscript corresponding to ICDM 2012, pp. 675-684. This PDF has no visible printed page numbering; locators use PDF pages. All ten pages, tables, figures and appendices visually read. Original printed statements and curator qualifications are distinguished; finite calculations are not historical empirical reproduction. |

## Limits And Additional Notes

- Adversarial author self-review only; both records remain DRAFT.
- The initial history command failed before writing because --actor was ambiguous. The corrected --actor-name invocation succeeded and its sidecar records this recovery.
- All ten pages of the 2012 author manuscript were visually read, including formulas, tables, figures, references and appendices. It is an unnumbered author manuscript corresponding to ICDM pp. 675-684; citations use PDF pages.
- MVKKM maintains a discrete partition while MVSpec optimizes an orthonormal relaxation and discretizes only at the end. The two complete procedures are retained separately.
- The records qualify zero residuals, tied minima, positive finite-p weights, the distinction between w and w^p, scale normalization and the scope of blockwise descent. A finite spectral tied-eigenvalue example refutes a universal fixed-point local-minimum interpretation.
- Synthetic, handwritten-digit and Corel-image comparisons were inspected for scope only. Known cluster counts, parameter sweeps, selected subsets and preprocessing do not establish universal superiority or label-free model selection.
- Coupled-mixture and co-EM full methods remain uninspected because of access/version limitations. Three additional objective/initialization cohorts are provisional. No author code, model training, paid service or full-paper redistribution occurred.
- Two additions bring the native collection to 492; 442 pinned AIO records are unchanged. The frontier contains 413 pending cohorts and other unresolved dispositions, so discovery has not reached saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T060542Z-kernel-multiview
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of multiview kernel k-means and weighted spectral clustering
started_at: '2026-10-12T05:58:53Z'
finished_at: '2026-10-12T06:05:42Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent read all fields of both final records against
    all ten visually inspected primary PDF pages, nine annotated AIO nodes and sixteen
    contextual YAMLs. Finite calculations challenge minimizer uniqueness, effective-weight
    limits, normalization and spectral fixed-point claims. This is author self-review,
    not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain source-specific MVKKM and MVSpec as separate algorithms with qualified
  weight, normalization, convergence and discretization boundaries. No actionable
  curation finding was identified in the final two records.
source:
  git_revision: f94447a06ab242944771dbe643c953474a178c0d
  state: working_tree
  inputs:
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
  - path: data/curated/ExemplarBasedConvexClustering.yaml
    sha256: 5520d800b3c23b513c66837e5f8fc424a7d7d4261f94047b94c8d71fee5973d9
    role: context
  - path: data/curated/KMeans.yaml
    sha256: 50fc1d8d18403a8f314636f68b6812ffd15fec2dfaaf4c32aaad423dfa7ffa03
    role: context
  - path: data/curated/KernelPCA.yaml
    sha256: a93227a6b2d6b2b89b679b8f7f9ddd5054741d1c11f9510490d82a3e691a1cab
    role: context
  - path: data/curated/MultiviewKernelKMeans.yaml
    sha256: fa7e2c11fa5e73ed61188affeee7ac460761880154837228e3724a754885467a
    role: target
  - path: data/curated/PowerIterationClustering.yaml
    sha256: ca81d60eb87c027126a3372950d40f50d0df8391b1075697e0ab5ffabf3dfa0f
    role: context
  - path: data/curated/SpectralHashing.yaml
    sha256: db90a881a13cbebad6083cb7534f8f0719c4a56fd136f5f3dc17e8c1ba8833c8
    role: context
  - path: data/curated/UnweightedMultiviewConvexMixtureClustering.yaml
    sha256: fb1a89caf2c25983cfe6cb0e3f2c25774891c24328e2e9efa6dbd4ef7556b3e0
    role: context
  - path: data/curated/WeightedMultiviewConvexMixtureClustering.yaml
    sha256: 44d41fb1c7de7f62733f6309e3f130c9bafde017118cbf82f2f5f4f147f5934d
    role: context
  - path: data/curated/WeightedMultiviewSpectralClustering.yaml
    sha256: 14031e86b6ad2c67137b7f0806675600ece879a392494f295f23edadf2eee9fe
    role: target
  - path: research/discovery/20261012T055803Z-kernel-multiview.json
    sha256: db2681856cddcd21451ea20af665987b873d242a72aa612b8f577db9535be33c
    role: context
  - path: research/discovery/kernel-multiview-boundaries.py
    sha256: 131c4d35d5a1aaa4de56001e9aad13758e1f209b03af6dddf2d1b8eb93d29315
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
- target_id: AIMech:MultiviewKernelKMeans
  path: data/curated/MultiviewKernelKMeans.yaml
  label: Multiview Kernel K-Means
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MultiviewKernelKMeans.yaml
    role: maintained
- target_id: AIMech:WeightedMultiviewSpectralClustering
  path: data/curated/WeightedMultiviewSpectralClustering.yaml
  label: Weighted Multiview Spectral Clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/WeightedMultiviewSpectralClustering.yaml
    role: maintained
scope:
  description: All fields of two source-defined multiview kernel clustering algorithms.
  selection: Exact maintained IDs MultiviewKernelKMeans and WeightedMultiviewSpectralClustering;
    all selected records without sampling.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - AIMech:MultiviewKernelKMeans
  - AIMech:WeightedMultiviewSpectralClustering
  exclusions:
  - target: Contextual AIO and maintained records
    reason: Context supports identity and mapping without renewed scientific approval
      or mutation.
  - target: Historical implementation and benchmarks
    reason: No author code, model training or source benchmark reproduction was performed.
      Curator finite examples test bounded mathematical claims.
  - target: Remaining discovery frontier
    reason: 413 pending cohorts and other unresolved dispositions remain. Global kernel
      initialization, similarity fusion, maximum-margin kernels, coupled mixtures
      and co-EM require further primary reading.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:MultiviewKernelKMeans
  - AIMech:WeightedMultiviewSpectralClustering
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 158.58s (0:02:38)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 492 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 146 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 143,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:MultiviewKernelKMeans
  - AIMech:WeightedMultiviewSpectralClustering
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
  - AIMech:MultiviewKernelKMeans
  - AIMech:WeightedMultiviewSpectralClustering
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
  - AIMech:MultiviewKernelKMeans
  - AIMech:WeightedMultiviewSpectralClustering
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Kernel multiview boundaries
  command: python3 research/discovery/kernel-multiview-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:MultiviewKernelKMeans
  - AIMech:WeightedMultiviewSpectralClustering
  exit_code: 0
  expected_exit_code: 0
  summary: '{"status": "passed", "positive_residual_weights": [0.8, 0.2], "objective":
    0.8, "large_p_weights": [0.5000346573589725, 0.4999653426410275], "large_p_normalized_coefficients":
    [0.8000221797873109, 0.19997782021268906], "spectral_fixed_point": {"initial_objective":
    0.25, "perturbed_objective": 0.24990001333262224, "perturbed_weights": [0.4900006666533335,
    0.5099993333466665], "eigenvalue_tie": true}, "constant_kernel_mean_squared_distance":
    0.0}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T055803Z-kernel-multiview.json
  accessed_at: '2026-10-12T05:58:53Z'
  support: supports
  summary: 'Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 490
    preceding native IDs, names and aliases; no normalized identity collision. Full
    searches of both checkouts include ignored and hidden files, with 5 matched lines
    in the worktree and 5 in main. All 3 distinct matched texts were inspected as
    source-query and frontier references. Nine annotated AIO nodes, nine generated
    YAMLs and seven native contextual YAMLs were assessed. Seven unchanged annotated
    nodes and generated records, all 442 class labels and 138 semantic rows reuse
    byte-verified earlier readings; two additional targets and the KernelLayer semantic
    row were read, giving 139 semantic rows. Absence is bounded to this snapshot and
    corpus.

    '
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Nine annotated CLASS nodes with outgoing edges; 139 semantic rows and all
    442 class labels, including byte-verified prior readings
  accessed_at: '2026-10-12T05:58:53Z'
  support: supports
  summary: 'Both source-specific procedures group unlabeled aligned views. UnsupervisedClustering
    is the closest inspected task association, so related_match avoids algorithm/task
    equivalence or subclass assertions. Broader Clustering, UnsupervisedLearning and
    MachineLearningTask are less specific. KernelLayer denotes a dot-product layer,
    Model a representation, PCA a variance projection and DimensionalityReduction
    a different task; the pin’s neural RepresentationLearning definition does not
    identify these kernel procedures. Eigenvectors and dot products alone do not establish
    those alternative mappings.

    '
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261012T055803Z-kernel-multiview.json
  locator: 'source_analysis.aio_mapping_inspection: nine generated and seven native
    contextual YAMLs'
  accessed_at: '2026-10-12T05:58:53Z'
  support: supports
  summary: K-means, kernel PCA, spectral hashing, power iteration clustering and the
    three exemplar mixture algorithms distinguish the new source-specific procedures.
    Seven generated records and annotated targets reuse verified identical bytes;
    KernelLayer and PCA annotations and YAMLs were additionally read. All seven native
    records were read in this working session. No contextual record receives renewed
    scientific approval.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/kernel-multiview-boundaries.py
  locator: Positive and zero residuals, tied minima, weight/coefficient limits, normalization
    and a spectral fixed saddle
  accessed_at: '2026-10-12T05:58:53Z'
  snapshot_sha256: 131c4d35d5a1aaa4de56001e9aad13758e1f209b03af6dddf2d1b8eb93d29315
  support: supports
  summary: Finite examples test positive-residual weight minimization, tied p=1 minima,
    zero residuals, large-p effective coefficient ratios, kernel scaling, constant-view
    normalization and a coordinatewise spectral fixed point with a nearby lower joint
    objective. They are curator mathematical illustrations, not historical benchmark
    reproduction.
- evidence_id: multiviewkernelkmeans-source-0
  kind: primary_source
  reference: https://www.cs.uoi.gr/~arly/full/conferences/C78.pdf
  locator: Section III-A, PDF p. 2, Equations 1-2; Section IV-B.1/3/5, PDF p. 4; Equation
    8; Section IV-A, PDF p. 3, Equations 4-7; Section IV-B, PDF p. 4, Equations 9-10;
    Appendices A-B, PDF p. 10, Equations 11-18; curator zero-residual and tied-minimum
    checks; Section IV-B.1/5, PDF p. 4; Section IV-C, PDF p. 5; source discussion
    of initialization and local optimization; Section IV-C, PDF p. 5, last paragraph;
    Section V-B, PDF pp. 6-7; curator constant-kernel and rescaling checks; Section
    IV-C, PDF pp. 4-5; Equation 4 and related norm discussion, PDF p. 3; curator large-p
    calculation; Sections III-A and IV, PDF pp. 2-5, Equations 1-2 and 4-10; Appendix
    A, PDF p. 10
  accessed_at: '2026-10-12T05:49:46Z'
  snapshot_sha256: 96eb9aab2cdb190edfda4f00c211693a15bfa9593368723a833b100bfe96b103
  support: supports
  summary: Kernel-based Weighted Multi-view Clustering. Author-hosted ten-page manuscript
    corresponding to ICDM 2012, pp. 675-684. This PDF has no visible printed page
    numbering; locators use PDF pages. All ten pages, tables, figures and appendices
    visually read. Original printed statements and curator qualifications are distinguished;
    finite calculations are not historical empirical reproduction.
- evidence_id: weightedmultiviewspectralclustering-source-0
  kind: primary_source
  reference: https://www.cs.uoi.gr/~arly/full/conferences/C78.pdf
  locator: Section III-B, PDF p. 3, Equation 3; Section IV-B.2/4/5, PDF p. 4; Section
    IV-C, PDF p. 5; Appendix B, PDF p. 10; Section IV-A, PDF p. 3, Equations 4-7;
    Section IV-B, PDF p. 4, Equations 9-10; Appendices A-B, PDF p. 10, Equations 11-18;
    curator zero-residual and tied-minimum checks; Section IV-C, PDF p. 5, convergence
    discussion; Appendix B, PDF p. 10; curator two-kernel fixed-point calculation;
    Section IV-C, PDF p. 5, last paragraph; Section V-B, PDF pp. 6-7; curator constant-kernel
    and rescaling checks; Section IV-C, PDF pp. 4-5; Equation 4 and related norm discussion,
    PDF p. 3; curator large-p calculation; Sections III-B and IV, PDF pp. 3-5, Equations
    3-4 and 8-10; Appendix B, PDF p. 10
  accessed_at: '2026-10-12T05:49:46Z'
  snapshot_sha256: 96eb9aab2cdb190edfda4f00c211693a15bfa9593368723a833b100bfe96b103
  support: supports
  summary: Kernel-based Weighted Multi-view Clustering. Author-hosted ten-page manuscript
    corresponding to ICDM 2012, pp. 675-684. This PDF has no visible printed page
    numbering; locators use PDF pages. All ten pages, tables, figures and appendices
    visually read. Original printed statements and curator qualifications are distinguished;
    finite calculations are not historical empirical reproduction.
assessments:
- assessment_id: multiviewkernelkmeans
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:MultiviewKernelKMeans
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - multiviewkernelkmeans-source-0
  summary: This is the Tzortzis-Likas 2012 MVKKM procedure. It maintains a discrete
    common partition while learning view weights. It differs from MVSpec, which optimizes
    an orthonormal relaxation before final discretization, and from exemplar-based
    multiview mixture methods, which fit log-mixture objectives. Its kernel-k-means
    component does not make the complete procedure ordinary input-space k-means or
    kernel PCA. MVKKM is the source-specific alias. Compared all 442 pinned AIO IDs,
    labels and scoped synonyms with all 490 preceding native IDs, names and aliases;
    no normalized identity collision. Full searches of both checkouts include ignored
    and hidden files, with 5 matched lines in the worktree and 5 in main. All 3 distinct
    matched texts were inspected as source-query and frontier references. Nine annotated
    AIO nodes, nine generated YAMLs and seven native contextual YAMLs were assessed.
    Seven unchanged annotated nodes and generated records, all 442 class labels and
    138 semantic rows reuse byte-verified earlier readings; two additional targets
    and the KernelLayer semantic row were read, giving 139 semantic rows. Absence
    is bounded to this snapshot and corpus.
  details: 'Given N aligned observations, V fixed positive-semidefinite view Gram
    matrices K_v, a supplied cluster count M and exponent p>=1, form Ktilde=sum_v
    w_v^p K_v with nonnegative w and sum_v w_v=1. The actual kernel coefficients are
    w_v^p, which need not sum to one. Their feature map concatenates the view features
    scaled by sqrt(w_v^p). The supplied kernels, M and p are not all learned by this
    procedure. Maintain M nonempty clusters with normalized indicator matrix Y_ik=1[i
    in C_k]/sqrt(|C_k|). For fixed view weights, apply kernel k-means to Ktilde, initializing
    from the preceding partition. For fixed clusters, use D_v=tr(K_v)-tr(Y^T K_v Y),
    equal to the sum of squared distances to view-specific feature means, and update
    w by the conditional weight solution. The paper starts view weights uniformly
    and initializes the partition through the named global kernel k-means procedure;
    that initialization is a heuristic, not a certificate of global optimality. For
    fixed positive residuals D_v and p>1, minimize sum_v D_v*w_v^p on the simplex
    using w_v=D_v^(-1/(p-1))/sum_u D_u^(-1/(p-1)). This gives positive weights for
    every positive residual. If some residuals are zero, the ratio formula is undefined;
    any weights supported entirely on zero-residual views minimize the block. At p=1,
    select a minimum-residual view as in the source, while ties mathematically permit
    any simplex distribution over minimizers. Neither zero-residual nor tied cases
    imply a unique weight vector. For fixed positive residuals, increasing p makes
    the simplex weight ratio (D_u/D_v)^(1/(p-1)) approach one. The ratio of actual
    kernel coefficients is (D_u/D_v)^(p/(p-1)); as p grows it approaches D_u/D_v,
    not generally one. Thus nearly uniform w does not imply uniform effective kernel
    contributions. The source uses sparsity to describe relative concentration; finite
    p>1 with positive residuals does not select exact zeros. The power-of-simplex
    constraint is not an asserted equivalence to every conventional lp multiple-kernel
    regularizer. View residual scales affect the learned weights. The source divides
    each view kernel by its mean pairwise squared feature distance, N^(-2)*sum_ij(K_vii-2*K_vij+K_vjj),
    to make scales comparable. This denominator vanishes for a constant feature view
    and needs an explicit convention. Such normalization does not establish that weights
    quantify semantic reliability or that a method is immune to uninformative views.
    Admissible kernel-k-means updates and exact weight minimization do not increase
    the shared within-cluster objective. Its nonnegativity supports objective-value
    convergence, while the selected partition remains initialization dependent. Nonempty
    clusters, tie handling and numerical stopping require explicit conventions. The
    procedure does not promise a globally best joint partition and weighting or unique
    parameters, and the source word global in the initialization algorithm name is
    not such a guarantee. Limitations: The input must provide aligned views and valid
    PSD kernels. An arbitrary similarity matrix is not automatically an RKHS Gram
    matrix. Kernel selection, requested cluster count and p remain modeling choices.
    Dense Gram matrices require storage quadratic in N per view; the source uses repeated
    clustering or eigensolutions, with additional initialization cost. No general
    scalability or global-optimum guarantee is curated. Source experiments use known
    class counts, parameter sweeps, selected digit/image subsets and specific preprocessing;
    their NMI results do not establish universal superiority or label-free model selection.
    No historical software or benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A source-specific kernel clustering algorithm, not a trained model
      instance or the whole family of multiview spectral methods.
    evidence_ids:
    - multiviewkernelkmeans-source-0
  - name: aio-assessment
    value: related_match
    definition: 'Both source-specific procedures group unlabeled aligned views. UnsupervisedClustering
      is the closest inspected task association, so related_match avoids algorithm/task
      equivalence or subclass assertions. Broader Clustering, UnsupervisedLearning
      and MachineLearningTask are less specific. KernelLayer denotes a dot-product
      layer, Model a representation, PCA a variance projection and DimensionalityReduction
      a different task; the pin’s neural RepresentationLearning definition does not
      identify these kernel procedures. Eigenvectors and dot products alone do not
      establish those alternative mappings.

      '
    evidence_ids:
    - mapping
- assessment_id: weightedmultiviewspectralclustering
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:WeightedMultiviewSpectralClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - weightedmultiviewspectralclustering-source-0
  summary: This is the Tzortzis-Likas 2012 MVSpec procedure; the local descriptive
    name is qualified by that source-specific identity. It is not every weighted multiview
    spectral method. Unlike MVKKM, it keeps an orthonormal embedding rather than a
    discrete partition during weight fitting. It differs from normalized-Laplacian
    graph clustering, power iteration clustering, kernel PCA and binary spectral hashing;
    a shared eigenvector operation does not establish equivalence. Compared all 442
    pinned AIO IDs, labels and scoped synonyms with all 490 preceding native IDs,
    names and aliases; no normalized identity collision. Full searches of both checkouts
    include ignored and hidden files, with 5 matched lines in the worktree and 5 in
    main. All 3 distinct matched texts were inspected as source-query and frontier
    references. Nine annotated AIO nodes, nine generated YAMLs and seven native contextual
    YAMLs were assessed. Seven unchanged annotated nodes and generated records, all
    442 class labels and 138 semantic rows reuse byte-verified earlier readings; two
    additional targets and the KernelLayer semantic row were read, giving 139 semantic
    rows. Absence is bounded to this snapshot and corpus.
  details: 'Given N aligned observations, V fixed positive-semidefinite view Gram
    matrices K_v, a supplied cluster count M and exponent p>=1, form Ktilde=sum_v
    w_v^p K_v with nonnegative w and sum_v w_v=1. The actual kernel coefficients are
    w_v^p, which need not sum to one. Their feature map concatenates the view features
    scaled by sqrt(w_v^p). The supplied kernels, M and p are not all learned by this
    procedure. For fixed w, choose N-by-M Y with Y^T Y=I spanning a leading M-dimensional
    eigenspace of the raw composite kernel Ktilde. This minimizes tr(Ktilde)-tr(Y^T
    Ktilde Y) over that relaxed set. Then compute D_v=tr(K_v)-tr(Y^T K_v Y) and update
    w by the conditional weight solution. Repeat without discretizing Y between weight
    updates. The paper starts w uniformly and applies k-means-based discretization
    to the final eigenvector embedding after convergence. That postprocessing is separate
    from the relaxed optimization and may lose its optimal value. For fixed positive
    residuals D_v and p>1, minimize sum_v D_v*w_v^p on the simplex using w_v=D_v^(-1/(p-1))/sum_u
    D_u^(-1/(p-1)). This gives positive weights for every positive residual. If some
    residuals are zero, the ratio formula is undefined; any weights supported entirely
    on zero-residual views minimize the block. At p=1, select a minimum-residual view
    as in the source, while ties mathematically permit any simplex distribution over
    minimizers. Neither zero-residual nor tied cases imply a unique weight vector.
    For fixed positive residuals, increasing p makes the simplex weight ratio (D_u/D_v)^(1/(p-1))
    approach one. The ratio of actual kernel coefficients is (D_u/D_v)^(p/(p-1));
    as p grows it approaches D_u/D_v, not generally one. Thus nearly uniform w does
    not imply uniform effective kernel contributions. The source uses sparsity to
    describe relative concentration; finite p>1 with positive residuals does not select
    exact zeros. The power-of-simplex constraint is not an asserted equivalence to
    every conventional lp multiple-kernel regularizer. View residual scales affect
    the learned weights. The source divides each view kernel by its mean pairwise
    squared feature distance, N^(-2)*sum_ij(K_vii-2*K_vij+K_vjj), to make scales comparable.
    This denominator vanishes for a constant feature view and needs an explicit convention.
    Such normalization does not establish that weights quantify semantic reliability
    or that a method is immune to uninformative views. Exact spectral and weight block
    updates do not increase the nonnegative relaxed objective, so its values converge.
    This alone does not prove unique parameter convergence or that every coordinatewise
    fixed point is a joint local minimum. For K_1=diag(1,0), K_2=diag(0,1), M=1 and
    p=2, w=(1/2,1/2) gives a tied composite eigenspace. Choosing Y=(1,1)/sqrt(2) is
    a valid fixed spectral/weight update with objective 1/4, yet an arbitrarily small
    joint rotation and weight adjustment lowers the objective. This curator example
    qualifies the source local-minimum claim under allowed eigenvalue ties; it does
    not reproduce the source experiments. Limitations: The input must provide aligned
    views and valid PSD kernels. An arbitrary similarity matrix is not automatically
    an RKHS Gram matrix. Kernel selection, requested cluster count and p remain modeling
    choices. Dense Gram matrices require storage quadratic in N per view; the source
    uses repeated clustering or eigensolutions, with additional initialization cost.
    No general scalability or global-optimum guarantee is curated. Source experiments
    use known class counts, parameter sweeps, selected digit/image subsets and specific
    preprocessing; their NMI results do not establish universal superiority or label-free
    model selection. No historical software or benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A source-specific kernel clustering algorithm, not a trained model
      instance or the whole family of multiview spectral methods.
    evidence_ids:
    - weightedmultiviewspectralclustering-source-0
  - name: aio-assessment
    value: related_match
    definition: 'Both source-specific procedures group unlabeled aligned views. UnsupervisedClustering
      is the closest inspected task association, so related_match avoids algorithm/task
      equivalence or subclass assertions. Broader Clustering, UnsupervisedLearning
      and MachineLearningTask are less specific. KernelLayer denotes a dot-product
      layer, Model a representation, PCA a variance projection and DimensionalityReduction
      a different task; the pin’s neural RepresentationLearning definition does not
      identify these kernel procedures. Eigenvectors and dot products alone do not
      establish those alternative mappings.

      '
    evidence_ids:
    - mapping
- assessment_id: discrete-versus-relaxed
  area: consistency
  topic: Complete algorithm identities
  outcome: supported
  target_ids:
  - AIMech:MultiviewKernelKMeans
  - AIMech:WeightedMultiviewSpectralClustering
  evidence_ids:
  - neighbors
  - finite-boundaries
  summary: Retain MVKKM and MVSpec separately.
  details: Both share fixed PSD kernels, simplex weights and a power-weighted variance
    objective. MVKKM keeps a normalized indicator of a discrete partition and applies
    kernel k-means; MVSpec allows any orthonormal embedding and takes leading composite-kernel
    eigenvectors. Only the latter delays discretization until after fitting. Their
    final groupings and learned weights need not agree. Neither is equivalent to the
    exemplar-mixture likelihood algorithms, kernel PCA, spectral hashing or early-stopped
    power iteration.
- assessment_id: weight-boundaries
  area: consistency
  topic: Conditional minimizers and missing ratio cases
  outcome: supported
  target_ids:
  - AIMech:MultiviewKernelKMeans
  - AIMech:WeightedMultiviewSpectralClustering
  evidence_ids:
  - multiviewkernelkmeans-source-0
  - weightedmultiviewspectralclustering-source-0
  - finite-boundaries
  summary: State positive, zero and tied-residual cases explicitly.
  details: The displayed inverse-residual formula is valid for p>1 and strictly positive
    residuals. Zero residuals permit support entirely on their zero set; multiple
    zeros can make solutions nonunique. At p=1, any simplex mass over tied minimum
    residuals is optimal, so not every optimum must be a vertex. Positive residuals
    and finite p>1 yield positive coefficients; the source sparsity discussion concerns
    relative concentration.
- assessment_id: power-and-scale
  area: consistency
  topic: Simplex weights versus effective kernel coefficients
  outcome: supported
  target_ids:
  - AIMech:MultiviewKernelKMeans
  - AIMech:WeightedMultiviewSpectralClustering
  evidence_ids:
  - multiviewkernelkmeans-source-0
  - weightedmultiviewspectralclustering-source-0
  - finite-boundaries
  summary: Keep the large-p limits and scale sensitivity distinct.
  details: For fixed D=(1,4), p=2 gives w=(.8,.2). At p=10001 the weights are approximately
    (.500034657,.499965343) but normalized effective coefficients are approximately
    (.80002218,.19997782). The coefficient ratio exponent p/(p-1) approaches one,
    leaving inverse-residual ratios rather than uniform contributions. Kernel rescaling
    changes D and weights; the mean pairwise squared-distance normalization is undefined
    for a constant view. None of these facts makes learned weights pure measures of
    semantic quality.
- assessment_id: spectral-fixed-point
  area: consistency
  topic: Blockwise optimality versus a joint local minimum
  outcome: supported
  target_ids:
  - AIMech:WeightedMultiviewSpectralClustering
  evidence_ids:
  - weightedmultiviewspectralclustering-source-0
  - finite-boundaries
  summary: Qualify the source convergence claim under allowed eigenvalue ties.
  details: 'With K1=diag(1,0), K2=diag(0,1), M=1 and p=2, equal weights give .25 I.
    The unit vector at angle pi/4 is therefore a valid leading eigenvector; equal
    weights also minimize its weight block. The point is fixed under permissible tie
    choices with objective .25. Rotate by epsilon and minimize the weight block: the
    objective becomes .25*cos(2*epsilon)^2, strictly less for arbitrarily small nonzero
    epsilon. This is a coordinatewise fixed point that is not a joint local minimum.
    Exact block descent still ensures convergent objective values; the counterexample
    does not refute that weaker conclusion.'
- assessment_id: initialization-and-discretization
  area: consistency
  topic: Initialization, rounding and benchmark scope
  outcome: supported
  target_ids:
  - AIMech:MultiviewKernelKMeans
  - AIMech:WeightedMultiviewSpectralClustering
  evidence_ids:
  - multiviewkernelkmeans-source-0
  - weightedmultiviewspectralclustering-source-0
  summary: Preserve the source-specific procedure and avoid transferred guarantees.
  details: MVKKM uses a named deterministic global kernel k-means initialization;
    its name does not certify a globally optimal fit. MVSpec fits a continuous orthonormal
    solution then discretizes with k-means, so the relaxed optimum is not guaranteed
    for the resulting partition. The source uses known class counts, parameter sweeps,
    representative subsets and preprocessing. Figures and tables do not establish
    universal superiority or intrinsically label-free selection.
- assessment_id: identity-and-mapping
  area: grounding
  topic: Bounded identity scope and algorithm-to-task mapping
  outcome: supported
  target_ids:
  - AIMech:MultiviewKernelKMeans
  - AIMech:WeightedMultiviewSpectralClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Keep native DRAFT status and the related UnsupervisedClustering mapping.
  details: Ignored-inclusive searches returned five matching lines per checkout and
    three distinct texts, all source-query/frontier references. All 442 AIO and 490
    prior native identities were compared. The nine annotated targets and sixteen
    contextual YAMLs do not identify these complete algorithms with a dot-product
    layer, PCA projection, neural representation learning or dimensionality-reduction
    task. 413 pending cohorts remain outside this selected review.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:MultiviewKernelKMeans
  - AIMech:WeightedMultiviewSpectralClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - multiviewkernelkmeans-source-0
  - weightedmultiviewspectralclustering-source-0
  rationale: MVKKM alternates discrete partitions and kernel weights; MVSpec alternates
    a leading-eigenspace relaxation and weights before final discretization. The common
    variance framework does not identify their optimization paths or final partitions.
    Related AIO task mappings preserve abstraction without upstream subclass assertions.
limitations:
- Adversarial author self-review only; both records remain DRAFT.
- The initial history command failed before writing because --actor was ambiguous.
  The corrected --actor-name invocation succeeded and its sidecar records this recovery.
- All ten pages of the 2012 author manuscript were visually read, including formulas,
  tables, figures, references and appendices. It is an unnumbered author manuscript
  corresponding to ICDM pp. 675-684; citations use PDF pages.
- MVKKM maintains a discrete partition while MVSpec optimizes an orthonormal relaxation
  and discretizes only at the end. The two complete procedures are retained separately.
- The records qualify zero residuals, tied minima, positive finite-p weights, the
  distinction between w and w^p, scale normalization and the scope of blockwise descent.
  A finite spectral tied-eigenvalue example refutes a universal fixed-point local-minimum
  interpretation.
- Synthetic, handwritten-digit and Corel-image comparisons were inspected for scope
  only. Known cluster counts, parameter sweeps, selected subsets and preprocessing
  do not establish universal superiority or label-free model selection.
- Coupled-mixture and co-EM full methods remain uninspected because of access/version
  limitations. Three additional objective/initialization cohorts are provisional.
  No author code, model training, paid service or full-paper redistribution occurred.
- Two additions bring the native collection to 492; 442 pinned AIO records are unchanged.
  The frontier contains 413 pending cohorts and other unresolved dispositions, so
  discovery has not reached saturation.
links: []
tags:
- native-concepts
- kernel-multiview
- self-review
- discovery-ongoing
```
