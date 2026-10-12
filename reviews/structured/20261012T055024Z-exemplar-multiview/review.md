# Scientific self-review of single-view and multiview exemplar clustering

- Review: 20261012T055024Z-exemplar-multiview
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T05:47:55Z
- Finished UTC: 2026-10-12T05:50:24Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain three distinct exemplar clustering procedures with explicit soft-versus-hard, view-objective, normalization and calibration boundaries. Source discrepancies are qualified in the records. No actionable curation finding was identified in the final cohort.

## Scope And Provenance

All fields of three source-defined exemplar fitting and assignment algorithms.

Selection: Exact maintained IDs ExemplarBasedConvexClustering, UnweightedMultiviewConvexMixtureClustering and WeightedMultiviewConvexMixtureClustering; all three, without sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base abfc9acc093a5ce5eedd19571ca059b8086a26d7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ExemplarBasedConvexClustering | data/curated/ExemplarBasedConvexClustering.yaml | maintained | Exemplar-Based Convex Clustering |
| AIMech:UnweightedMultiviewConvexMixtureClustering | data/curated/UnweightedMultiviewConvexMixtureClustering.yaml | maintained | Unweighted Multiview Convex Mixture Clustering |
| AIMech:WeightedMultiviewConvexMixtureClustering | data/curated/WeightedMultiviewConvexMixtureClustering.yaml | maintained | Weighted Multiview Convex Mixture Clustering |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:ExemplarBasedConvexClustering, AIMech:UnweightedMultiviewConvexMixtureClustering, AIMech:WeightedMultiviewConvexMixtureClustering | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 98.06s (0:01:38)<br>Checked 442 record(s); 0 failed.<br>Checked 490 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 145 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 142,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:ExemplarBasedConvexClustering, AIMech:UnweightedMultiviewConvexMixtureClustering, AIMech:WeightedMultiviewConvexMixtureClustering | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:ExemplarBasedConvexClustering, AIMech:UnweightedMultiviewConvexMixtureClustering, AIMech:WeightedMultiviewConvexMixtureClustering | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:ExemplarBasedConvexClustering, AIMech:UnweightedMultiviewConvexMixtureClustering, AIMech:WeightedMultiviewConvexMixtureClustering | Command exited 0 with no output. |
| Exemplar and multiview boundaries | passed | True | AIMech:ExemplarBasedConvexClustering, AIMech:UnweightedMultiviewConvexMixtureClustering, AIMech:WeightedMultiviewConvexMixtureClustering | {"status": "passed", "conditional_row_sums": [1.0, 1.0], "printed_assignment_row_sums": [0.5, 0.5], "pruned_small_weight": 5.0499999955045e-10, "stable_ranking_objective_gap": 0.004431176533266967, "soft_vs_hard": {"points": [0.0, 1.0, 3.0], "beta": 0.25, "weights": [7.903163782101564e-38, 0.9430634470953659, 0.05693655290463398], "iterations": 401, "mutual_information_nats": 0.032280278694272406, "hard_exemplar_indices": [1], "soft_gap_certificate": 9.5479180117763e-15}, "multiview": {"unweighted_objective": 0.38041532790905963, "weighted_uniform_objective": 0.3332282826534504, "unweighted_one_step": [0.6359842351349336, 0.36401576486506637], "weighted_outer_view_update": [0.36896937831653764, 0.6310306216834622], "weighted_inner_solution": [0.5949936032303513, 0.40500639676964867], "weighted_next_objective": 0.2618447739437066}, "view_scale": {"raw_affinity_outer_weight": 0.3793103448275862, "normalized_density_outer_weight": 0.6625122267484607, "coordinate_rescaled_density_outer_weight": 0.16409418793651973}, "unnormalized_product_mass": 2.4, "printed_gaussian_integral": 0.7071067811865475} |

## Scientific And Domain Assessments

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:ExemplarBasedConvexClustering.

This is the Lashkari-Golland procedure, also described as convex mixture model clustering. Its data-derived exemplar dictionary and hard extraction policy specialize fixed-component weight EM and finite rate-distortion Blahut-Arimoto. It is distinct from moving-centroid k-means, neural balanced transport in SeLa, scale-persistence melting, and fusion-penalty methods also called convex clustering. CMM and CCE are searched contextual acronyms, not unqualified identity aliases. No normalized identity collision across all 442 pinned AIO IDs, labels/scoped synonyms and 487 maintained IDs, names and aliases. Full-checkout searches include ignored and hidden files: 8 matched lines in the worktree and 9 in main. All six distinct matched texts were read; they concern the prior exemplar-clustering frontier, its source/query URLs and an unrelated FreeFem lexer token. Seven annotated AIO nodes and seven full native neighbors were inspected. The same pinned bytes retain the previously read 442 class labels and 138 semantic label/synonym rows. Absence is bounded to this snapshot and corpus.

For N indexed observations, fixed finite dissimilarities d_ij and beta&gt;=0, set S_ij=exp(-beta*d_ij). Minimize J(q)=-(1/N)sum_i log(sum_j q_j S_ij) over simplex weights with positive initialization. With z_i=sum_j q_j S_ij, set r_ij=q_j S_ij/z_i and q_j_new=(1/N)sum_i r_ij. Equivalently, the row-conditional channel minimizes I(I;J)+beta*E[d_ij] with a uniform data-index source. A valid common-base component family additionally gives the stated mixture-likelihood interpretation; Gaussian components use squared Euclidean distance. For finite positive kernels and positive initialization, the exact unpruned iteration converges to a global optimum of the restricted soft weight objective. This is not a global fit of freely moving mixture components. Convexity does not imply unique coefficients: at beta=0 every q is fixed and optimal. Zero weights stay zero and can exclude useful exemplars; exact positive-kernel finite iterations preserve positive weights. At an optimum eta_j=(1/N)sum_i S_ij/z_i equals one on positive weights and is at most one on inactive coordinates, rather than necessarily strictly less. The 2007 visualization policy first selects every exemplar index that maximizes r_ij for at least one observation, then assigns each observation to its closest selected exemplar. Tie handling is not specified. This differs from the later multiview top-M policy. Beta controls the soft distortion tradeoff but does not uniquely determine a universally correct hard cluster count. Hardening does not retain the soft optimum guarantee or a general bound I&lt;=log(K_hard): for points (0,1,3), squared distance and beta=1/4, the saved near-optimal soft solution has I about 0.03228 nats while this MAP policy selects only the middle point. The dense exact update uses two matrix-vector operations with O(N^2) work per iteration. The paper separately proposes deleting weights below 10^-3/N and renormalizing, and retaining only a rowwise subset of large similarities. These approximations can change the feasible set or objective and need not preserve the full soft optimum. The saved two-point example shows the stated pruning threshold removing a small but useful positive component. The expression r_ij=q_j S_ij/(N z_i) after Equation 9 is joint data-index/exemplar mass, not the row-conditional r defined in Equation 6; the conditional omits N. Literal KL from an atomic empirical measure to a continuous density is not finite merely by evaluating that density at data points. The finite-index objective and normalized responsibilities above avoid transferring that common-measure ambiguity from Equation 3. Limitations: Sparsity at an asymptotic limit, numerical pruning, and the selected hard exemplars are different notions. Neither every beta change nor every initialization produces a distinct optimum. Natural-log objectives use nats; bit rates require consistent log-base and multiplier conversion. A slope statement for the rate-distortion curve needs differentiability or a supporting-slope interpretation. Synthetic source comparisons tune beta using class labels and do not establish universal performance or a biological application. No historical software or benchmark was reproduced.

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:UnweightedMultiviewConvexMixtureClustering.

This is the unweighted Tzortzis-Likas 2009 procedure. Shared q couples corresponding exemplar indices across views, while each view retains its own fixed component family and scale. It averages view-specific log objectives and responsibilities; fixing uniform view weights inside the later weighted log-of-sum objective does not recover this procedure. The original sum-of-posteriors hard assignment and top-M ranking stop are retained explicitly. No normalized identity collision across all 442 pinned AIO IDs, labels/scoped synonyms and 487 maintained IDs, names and aliases. Full-checkout searches include ignored and hidden files: 8 matched lines in the worktree and 9 in main. All six distinct matched texts were read; they concern the prior exemplar-clustering frontier, its source/query URLs and an unrelated FreeFem lexer token. Seven annotated AIO nodes and seven full native neighbors were inspected. The same pinned bytes retain the previously read 442 class labels and 138 semantic label/synonym rows. Absence is bounded to this snapshot and corpus.

For N observations with V aligned views, fix view-specific component values f_vij=f_vj(x_vi) and common simplex weights q_j. Minimize -(1/(N V))sum_vi log Q_vi, where Q_vi=sum_j q_j f_vij. Set q_j_new=q_j/(N V)*sum_vi f_vij/Q_vi. Each view contributes its average current responsibilities equally. Common factors depending on the view and observation but not the exemplar cancel in this update. With finite positive component values, positive support and exact unpruned iteration, the soft convex problem attains a global optimum; coefficient uniqueness is not implied. Given a requested M, retain the M largest fitted q values as exemplars, each anchoring its own cluster. Assign every other observation to the selected exemplar maximizing sum_v q_j f_vij/Q_vi. This sums per-view posteriors, rather than multiplying densities or taking the maximum over individual views. The source uses strict comparisons without a tie policy. Its implementation stops when the selected top-M indices and their ranking stay unchanged for several consecutive iterations; this can occur before the soft objective is optimized. View families and beta_v values remain supplied choices. The empirical scale N^2 log(N)/sum_ij d_vij is a search guide and is undefined when its denominator vanishes. The fitting update needs O(N^2 V) dense arithmetic per iteration, apart from distance construction. A fixed-M hard partition has no transferred global-optimum guarantee; stable ranking is not a bound on residual objective error. Equal view contribution also does not guarantee robustness to uninformative or systematically biased views. Limitations: The record uses the finite evaluated-component/log-likelihood objective; the source empirical-versus-continuous KL shorthand requires a compatible measure or lift. Gaussian exponents use squared Euclidean distances. The soft fit is a shared-weight specialization of fixed-component EM. The complete multiview data construction, equal-view objective and sum-of-posteriors/top-M policy define this narrower algorithm. Source experiments remove observations lacking required views and select scale multipliers by label entropy. They do not establish an intrinsic missing-view algorithm, fully label-free model selection, or universal performance. No historical experiment was reproduced.

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:WeightedMultiviewConvexMixtureClustering.

This is the Tzortzis-Likas 2010 weighted multiview CMM procedure. Despite the inherited CMM name, its joint objective is not convex. It uses the log of a view-weighted sum of exemplar scores, whereas the 2009 algorithm sums view log likelihoods. This record distinguishes the general component-value formulation from the distance-only experimental variant that omits density base factors, and does not assert that marginal densities on different view spaces automatically define a joint generative model. No normalized identity collision across all 442 pinned AIO IDs, labels/scoped synonyms and 487 maintained IDs, names and aliases. Full-checkout searches include ignored and hidden files: 8 matched lines in the worktree and 9 in main. All six distinct matched texts were read; they concern the prior exemplar-clustering frontier, its source/query URLs and an unrelated FreeFem lexer token. Seven annotated AIO nodes and seven full native neighbors were inspected. The same pinned bytes retain the previously read 442 class labels and 138 semantic label/synonym rows. Absence is bounded to this snapshot and corpus.

Given fixed positive component values f_vij, let Q_vi(q)=sum_j q_j f_vij and maximize L(q,pi)=sum_i log(sum_v pi_v Q_vi(q)) with q and pi on their respective simplices. From the current parameters compute gamma_iv=pi_v Q_vi/sum_w pi_w Q_wi. Set pi_v_new=(1/N)sum_i gamma_iv. Hold these outer responsibilities fixed while iterating q_j &lt;- q_j/N*sum_iv gamma_iv f_vij/Q_vi(q), using the current inner q in the denominator. Repeat inner updates to their stated tolerance, then recompute outer responsibilities. The paper starts both weight vectors uniformly and uses inner L1-change and outer objective-change stopping conditions. The objective is separately concave in either weight vector with the other fixed, but not jointly concave in general. The nested surrogate updates support objective ascent for admissible exact arithmetic; a finite inner tolerance is an approximate M-step. Uniform starts, small objective changes or successful source examples do not prove global optimality, a unique limit, or that every stationary outcome is a local maximum. Uniform pi also leaves a log-of-sum objective, not the unweighted sum-of-logs objective. The source writes a sum of marginal densities Q_v(x_v) as a density of the full view tuple. That sum is not automatically normalized on the product observation space without an appropriate common observation model or background factors. For two- and three-state view alphabets, its total mass is 3*pi_1+2*pi_2. The finite positive-score objective still has meaningful normalized responsibilities and surrogate updates, but does not by itself establish the asserted generative interpretation. View-specific density scales affect the learned pi; they are not pure measures of semantic view quality. The general outer gamma calculation retains C_v(x_vi) from f_vij=C_v(x_vi)exp(-beta_v*d_vij). These factors cancel within the inner q update but not generally across views in gamma. The experiments explicitly omit them from the outer update to work from distances alone; this optimizes a modified affinity-score objective unless the factors cancel across views. With exp(-beta*&#124;&#124;x-m&#124;&#124;^2), the normalized Gaussian factor is (beta/pi)^(d/2), rather than the printed (beta/(2*pi))^(d/2). Source benchmark results for omitted factors do not certify the normalized-density formulation. After fitting, select a specified M largest-q exemplars and anchor each to its own cluster. Assign other observations by maximizing q_j sum_v pi_v f_vij among the selected exemplars. The full-component denominator is shared and cancels for this comparison; the selected-subset scores need not sum to one as M-cluster probabilities without renormalization. Ties need an explicit policy. Dense training costs O(N^2 V tau tau_inner), excluding initial distances. Kernel squared distances can supply a feature-space realization, but a generic dissimilarity matrix does not automatically establish a normalized feature-space density. Limitations: All views must be aligned to the same observation and exemplar indices. The source explicitly does not model general dependence between views and notes failures with systematic inter-view bias. The number of final exemplars and each component scale remain supplied choices. Hard assignment is separate from soft fitting and has no global clustering guarantee. Zero weights remain excluded; positivity and nonzero denominators matter. The empirical comparisons use complete-view filtering, specified cluster counts, label-based scale selection and optional kernel-k-means fine-tuning. They do not establish general noise immunity, semantic calibration of view weights, or universal superiority. No author software or historical benchmark was reproduced.

### Shared mathematical components do not establish identity

consistency: supported. Targets: AIMech:ExemplarBasedConvexClustering, AIMech:UnweightedMultiviewConvexMixtureClustering, AIMech:WeightedMultiviewConvexMixtureClustering.

Retain the single-view, unweighted multiview and weighted multiview procedures.

The single-view algorithm fixes every datum as a candidate exemplar, fits simplex weights and uses posterior-MAP selection followed by nearest-exemplar grouping. The 2009 multiview method shares weights across aligned views, averages view log objectives and sums view posteriors for a specified top-M grouping. The 2010 method learns view weights through a log-of-sum objective and nested updates, then uses weighted component scores. Even uniform view weights do not recover the unweighted objective.

### Convex soft fitting versus approximate and hard policies

consistency: supported. Targets: AIMech:ExemplarBasedConvexClustering.

Preserve support, normalization and hardening qualifications.

The source conditional expression after Equation 9 includes an extra factor N relative to its earlier row-conditional definition; it instead normalizes joint index mass. Exact full-support fitting retains the convex soft objective. At beta zero all simplex weights are fixed optima, and inactive optimal coordinates need only eta&lt;=1. The source pruning threshold can delete a useful component. On points (0,1,3), beta=1/4 and squared distances, the saved near-optimal soft solution has positive information 0.03228 nats but only one MAP-selected exemplar; the caption bound involving the hard count is not general. Numerical closeness to the optimum is not an exact symbolic proof.

### Actual 2009 stopping and assignment rules

consistency: supported. Targets: AIMech:UnweightedMultiviewConvexMixtureClustering.

Keep the sum-of-posteriors policy and distinguish ranking stability from optimization.

Section 3.2 and Equation 10 specify anchored top-M exemplars and a sum over view posteriors. The source stops after unchanged selected indices and ordering across several iterations; it does not provide a residual objective certificate. A positive two-point example retains its ranking for five updates with objective error about 0.00443. Strict assignment comparisons leave ties unspecified, and the beta search guide is undefined for zero total dissimilarity.

### Nested update order, objective shape and posterior scope

consistency: supported. Targets: AIMech:WeightedMultiviewConvexMixtureClustering.

Retain the frozen outer responsibilities during inner shared-weight fitting.

The general positive-score objective is separately concave but not jointly concave. The paper computes view responsibilities from current q and pi, updates pi, then iterates q with the outer responsibilities held fixed. The saved calculation distinguishes this from one unweighted update and checks ascent. Finite inner tolerance is an approximate M-step; source convergence prose does not establish a unique global solution or universal local maximum. Selected scores require renormalization to act as an M-component probability distribution.

### Observation space, density units and experimental base-factor omission

consistency: supported. Targets: AIMech:WeightedMultiviewConvexMixtureClustering.

Qualify the source generative and view-quality interpretation.

A weighted sum of densities on separate view domains is not automatically normalized on their product space: two- and three-state alphabets give total mass 3*pi_1+2*pi_2. Component base factors cancel inside the inner q ratio but affect the outer view responsibilities. Section V-A explicitly drops these factors for distance-only experiments. The printed Gaussian factor with exp(-beta*distance_squared) integrates to 2^(-d/2), not one. A coordinate rescaling preserving the kernel changes the normalized-density view update; learned pi is not solely semantic view quality. These are bounded mathematical deductions, not claims that every practical affinity variant is invalid.

### Corpus scope, mappings and incomplete discovery

grounding: supported. Targets: AIMech:ExemplarBasedConvexClustering, AIMech:UnweightedMultiviewConvexMixtureClustering, AIMech:WeightedMultiviewConvexMixtureClustering.

Maintain local DRAFT records and related task mappings.

All 442 pinned AIO identities and 487 prior native identities were compared, with ignored and hidden checkout files included. All six distinct match texts were inspected. Seven annotated AIO targets, seven native neighbors and seven generated YAMLs were read. The unchanged snapshot permits reuse of the previously read class-label and semantic-synonym inventories. Algorithms relate to the UnsupervisedClustering task without equivalence or subclass assertions. The complete selected three-record cohort is reviewed; 411 pending frontier cohorts remain outside this review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:ExemplarBasedConvexClustering, AIMech:UnweightedMultiviewConvexMixtureClustering, AIMech:WeightedMultiviewConvexMixtureClustering. The three complete procedures differ in view construction, soft objective, optimization order and hard extraction. Common fixed-component fitting does not erase these distinctions. Related task mappings preserve abstraction without asserting upstream subclasses.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T054505Z-exemplar-multiview.json | supports | No normalized identity collision across all 442 pinned AIO IDs, labels/scoped synonyms and 487 maintained IDs, names and aliases. Full-checkout searches include ignored and hidden files: 8 matched lines in the worktree and 9 in main. All six distinct matched texts were read; they concern the prior exemplar-clustering frontier, its source/query URLs and an unrelated FreeFem lexer token. Seven annotated AIO nodes and seven full native neighbors were inspected. The same pinned bytes retain the previously read 442 class labels and 138 semantic label/synonym rows. Absence is bounded to this snapshot and corpus.<br> |
| mapping | sources/aio/aio.json; Seven annotated CLASS nodes with outgoing edges; all 442 class labels and 138 semantic rows retained from the prior complete reading of identical pinned bytes | supports | All three records describe fitting and assignment algorithms for unlabeled observations. The inspected UnsupervisedClustering target denotes a task, so related_match preserves that abstraction difference. Clustering, UnsupervisedLearning and MachineLearningTask are less specific task associations; Model denotes a representation rather than the complete fitting procedure. Neither dimensionality reduction nor the pin's deep neural RepresentationLearning definition identifies these procedures. No upstream subclass assertion is made.<br> |
| neighbors | research/discovery/20261012T054505Z-exemplar-multiview.json; source_analysis.aio_mapping_inspection: seven generated and seven native full YAML readings | supports | Fixed-component weight EM, rate-distortion Blahut-Arimoto, EM, k-means, deterministic annealing EM, clustering by melting and SeLa distinguish general fitting components from complete exemplar procedures. Seven generated records provide task/model/representation boundaries. Contextual records receive no renewed scientific approval. |
| finite-boundaries | research/discovery/exemplar-multiview-boundaries.py; Conditional versus joint mass, support/pruning, ranking stop, soft versus hard information, multiview objectives and density normalization | supports | Finite checks distinguish conditional/joint mass, support and pruning, beta-zero nonuniqueness, stable ranking from objective convergence, soft rate from hard cluster count, unweighted and weighted objectives, nested update ascent, density-scale effects and product-space normalization. These are curator illustrations, not historical software or empirical reproduction. |
| exemplarbasedconvexclustering-source-0 | https://papers.neurips.cc/paper/3181-convex-clustering-with-exemplar-based-models.pdf; Section 2, PDF p. 3, Equation 3; Section 3, Equations 6-8; Section 4, PDF p. 4, expression after Equation 9; curator normalization checks; Section 2, PDF p. 3, Equation 4 and positive-support condition; Section 4, PDF p. 4, Equation 9; curator support and beta-zero checks; Section 4, PDF pp. 4-5, Equation 9, pruning and similarity sparsification; curator finite pruning example; Section 5, PDF p. 5, hard assignment and loss of optimality; Figure 1 caption; curator finite soft-channel/MAP calculation; Sections 2-4, PDF pp. 2-4, Equations 2, 4, 6-9; conditional normalization from Equations 6-8; Sections 2-5, PDF pp. 2-5, Equations 2, 4, 8-9 and hard-exemplar extraction | supports | Convex Clustering with Exemplar-Based Models. NIPS 2007 proceedings, volume 20; official eight-page PDF, internally numbered 1-8. All pages, figures, captions and references visually read. Original printed statements and curator qualifications are distinguished; finite calculations are not historical empirical reproduction. |
| unweightedmultiviewconvexmixtureclustering-source-0 | https://www.cs.uoi.gr/~arly/full/conferences/C64.pdf; Section 3, printed pp. 208-210 / PDF pp. 4-6, Equations 5-11; Section 3.2, printed p. 210 / PDF p. 6, Equation 11 and cost; Sections 4-5, printed pp. 210-214 / PDF pp. 6-10; curator stable-ranking example; Section 3.2, printed pp. 209-210 / PDF pp. 5-6, stopping discussion and Equation 10; Sections 3.1-3.2, printed pp. 208-209 / PDF pp. 4-5, Equations 6-9 and support condition | supports | Convex Mixture Models for Multi-view Clustering. ICANN 2009, Part II, LNCS 5769, pp. 205-214; author-hosted ten-page proceedings PDF. All pages visually read; printed page = PDF page + 204. Original printed statements and curator qualifications are distinguished; finite calculations are not historical empirical reproduction. |
| weightedmultiviewconvexmixtureclustering-source-0 | https://www.cs.uoi.gr/~arly/full/journals/J71.pdf; Section IV-A, printed p. 1928 / PDF p. 4, Equation 9; Appendix A, printed p. 1936 / PDF p. 12, Equations 17-21; curator product-mass and coordinate-rescaling examples; Section IV-B, printed p. 1929 / PDF p. 5, Equations 11-13 and Algorithm 1; Appendix A, printed pp. 1936-1937 / PDF pp. 12-13, Equations 22-28; Section IV-B, printed p. 1929 / PDF p. 5, third implementation remark; Section V-A, printed p. 1930 / PDF p. 6, Gaussian factor and explicit removal; curator Gaussian-integral check; Section IV-B, printed pp. 1928-1929 / PDF pp. 4-5; Appendix A, printed pp. 1936-1937 / PDF pp. 12-13; curator two-view objective/update comparison; Section IV-B, printed pp. 1929-1930 / PDF pp. 5-6, Equations 14-15; Section IV-C, PDF p. 6; Appendix B, printed p. 1937 / PDF p. 13, Equations 29-34; Sections IV-A/IV-B, printed pp. 1928-1930 / PDF pp. 4-6, Equations 9-15 and Algorithm 1 | supports | Multiple View Clustering Using a Weighted Combination of Exemplar-Based Mixture Models. IEEE Transactions on Neural Networks 21(12):1925-1938, December 2010. Author-hosted journal PDF; all 14 pages, tables and appendices visually read. Printed page = PDF page + 1924. Original printed statements and curator qualifications are distinguished; finite calculations are not historical empirical reproduction. |

## Limits And Additional Notes

- Adversarial author self-review only; all three records remain DRAFT.
- All 8 pages of the 2007 proceedings,10 pages of the 2009 multiview proceedings and 14 pages of the 2010 journal paper were visually read, including formulas, algorithm boxes, tables, appendices and references.
- The original single-view hard-MAP/nearest-exemplar extraction differs from the 2009 top-M and sum-of-view-posteriors policy. The 2010 weighted scores and nested view/shared-weight updates use a different objective, even at equal view weights.
- Source-prose qualifications preserve conditional versus joint assignment normalization, exact versus pruned support, soft versus hard guarantees, ranking stopping, finite score objectives versus literal atomic/continuous KL, and density factors omitted in the 2010 experiments.
- The weighted sum of view marginal densities is not automatically a normalized joint density on their product space. Positive-score objectives and surrogate updates remain meaningful, but learned view weights depend on relative score or density scales. No unsupported joint generative or pure view-quality interpretation is asserted.
- Synthetic and document/image benchmarks were read for scope, not reproduced or promoted into universal performance. Supplied cluster counts, complete-view filtering, label-guided scale selection and optional postprocessing remain explicit.
- Three new cohorts remain provisional with primary access limitations. No author software, model training, paid service or full-paper redistribution occurred. Three additions bring the native collection to 490;442 pinned AIO records are unchanged. No literature saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T055024Z-exemplar-multiview
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of single-view and multiview exemplar clustering
started_at: '2026-10-12T05:47:55Z'
finished_at: '2026-10-12T05:50:24Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially read all fields of the three
    final records against 32 visually inspected primary PDF pages, seven annotated
    AIO nodes and fourteen contextual YAMLs. Finite calculations challenge support,
    hardening, stopping, nested objectives and density interpretation. This is author
    self-review, not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain three distinct exemplar clustering procedures with explicit soft-versus-hard,
  view-objective, normalization and calibration boundaries. Source discrepancies are
  qualified in the records. No actionable curation finding was identified in the final
  cohort.
source:
  git_revision: abfc9acc093a5ce5eedd19571ca059b8086a26d7
  state: working_tree
  inputs:
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/DimensionalityReduction.yaml
    sha256: 99eb0714b362a98a9e704e5ef2ac370cb7a900fbe97da43de790c3ec67ed812e
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
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
  - path: data/curated/BlahutArimotoRateDistortionAlgorithm.yaml
    sha256: 7e7e05bc224e256cef7fa22d696bca28fa4097563f14980843b145ab2613506a
    role: context
  - path: data/curated/ClusteringDataByMelting.yaml
    sha256: 957e63d61f09c25a547dae5e1ebf535d8cba2c76e927b9ac7c6accb61cbce005
    role: context
  - path: data/curated/DeterministicAnnealingExpectationMaximization.yaml
    sha256: 55b477435b3c27f9061a649effe0be94b71f346127d6ab773f861cec8df5112d
    role: context
  - path: data/curated/ExemplarBasedConvexClustering.yaml
    sha256: 5520d800b3c23b513c66837e5f8fc424a7d7d4261f94047b94c8d71fee5973d9
    role: target
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: context
  - path: data/curated/FixedComponentMixtureWeightEM.yaml
    sha256: 3c1835ab99983d2fe8d5f40f0b7156d124c3140c0d019df7617aff38d2131a08
    role: context
  - path: data/curated/KMeans.yaml
    sha256: 50fc1d8d18403a8f314636f68b6812ffd15fec2dfaaf4c32aaad423dfa7ffa03
    role: context
  - path: data/curated/SeLa.yaml
    sha256: 0b5e4c15b065fcf3fd0958d25d93c2c18a418dedac7e29c8a805cb3fd3a674ea
    role: context
  - path: data/curated/UnweightedMultiviewConvexMixtureClustering.yaml
    sha256: fb1a89caf2c25983cfe6cb0e3f2c25774891c24328e2e9efa6dbd4ef7556b3e0
    role: target
  - path: data/curated/WeightedMultiviewConvexMixtureClustering.yaml
    sha256: 44d41fb1c7de7f62733f6309e3f130c9bafde017118cbf82f2f5f4f147f5934d
    role: target
  - path: research/discovery/20261012T054505Z-exemplar-multiview.json
    sha256: 9cd2b879394317cc80b5b5d51da5b7cca760b4f49245cbbfc55af1130e62d3ec
    role: context
  - path: research/discovery/exemplar-multiview-boundaries.py
    sha256: 9ea9eee10873abe3fb9ef66df527e9b25c0dc6de31d294578b1071da58815c66
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
- target_id: AIMech:ExemplarBasedConvexClustering
  path: data/curated/ExemplarBasedConvexClustering.yaml
  label: Exemplar-Based Convex Clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ExemplarBasedConvexClustering.yaml
    role: maintained
- target_id: AIMech:UnweightedMultiviewConvexMixtureClustering
  path: data/curated/UnweightedMultiviewConvexMixtureClustering.yaml
  label: Unweighted Multiview Convex Mixture Clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/UnweightedMultiviewConvexMixtureClustering.yaml
    role: maintained
- target_id: AIMech:WeightedMultiviewConvexMixtureClustering
  path: data/curated/WeightedMultiviewConvexMixtureClustering.yaml
  label: Weighted Multiview Convex Mixture Clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/WeightedMultiviewConvexMixtureClustering.yaml
    role: maintained
scope:
  description: All fields of three source-defined exemplar fitting and assignment
    algorithms.
  selection: Exact maintained IDs ExemplarBasedConvexClustering, UnweightedMultiviewConvexMixtureClustering
    and WeightedMultiviewConvexMixtureClustering; all three, without sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:ExemplarBasedConvexClustering
  - AIMech:UnweightedMultiviewConvexMixtureClustering
  - AIMech:WeightedMultiviewConvexMixtureClustering
  exclusions:
  - target: Contextual AIO and maintained records
    reason: Context supports identity and mapping without renewed scientific approval
      or mutation.
  - target: Historical software and benchmarks
    reason: No author software, training or benchmark reproduction ran. Finite curator
      examples test bounded mathematical claims.
  - target: Remaining discovery frontier
    reason: 411 pending cohorts and other unresolved dispositions remain, including
      coupled mixtures, kernel weighted multiview methods and co-EM objectives. Failed
      source access is retained as a limitation, not absence.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:ExemplarBasedConvexClustering
  - AIMech:UnweightedMultiviewConvexMixtureClustering
  - AIMech:WeightedMultiviewConvexMixtureClustering
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 98.06s (0:01:38)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 490 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 145 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 142,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:ExemplarBasedConvexClustering
  - AIMech:UnweightedMultiviewConvexMixtureClustering
  - AIMech:WeightedMultiviewConvexMixtureClustering
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
  - AIMech:ExemplarBasedConvexClustering
  - AIMech:UnweightedMultiviewConvexMixtureClustering
  - AIMech:WeightedMultiviewConvexMixtureClustering
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
  - AIMech:ExemplarBasedConvexClustering
  - AIMech:UnweightedMultiviewConvexMixtureClustering
  - AIMech:WeightedMultiviewConvexMixtureClustering
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Exemplar and multiview boundaries
  command: python3 research/discovery/exemplar-multiview-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ExemplarBasedConvexClustering
  - AIMech:UnweightedMultiviewConvexMixtureClustering
  - AIMech:WeightedMultiviewConvexMixtureClustering
  exit_code: 0
  expected_exit_code: 0
  summary: '{"status": "passed", "conditional_row_sums": [1.0, 1.0], "printed_assignment_row_sums":
    [0.5, 0.5], "pruned_small_weight": 5.0499999955045e-10, "stable_ranking_objective_gap":
    0.004431176533266967, "soft_vs_hard": {"points": [0.0, 1.0, 3.0], "beta": 0.25,
    "weights": [7.903163782101564e-38, 0.9430634470953659, 0.05693655290463398], "iterations":
    401, "mutual_information_nats": 0.032280278694272406, "hard_exemplar_indices":
    [1], "soft_gap_certificate": 9.5479180117763e-15}, "multiview": {"unweighted_objective":
    0.38041532790905963, "weighted_uniform_objective": 0.3332282826534504, "unweighted_one_step":
    [0.6359842351349336, 0.36401576486506637], "weighted_outer_view_update": [0.36896937831653764,
    0.6310306216834622], "weighted_inner_solution": [0.5949936032303513, 0.40500639676964867],
    "weighted_next_objective": 0.2618447739437066}, "view_scale": {"raw_affinity_outer_weight":
    0.3793103448275862, "normalized_density_outer_weight": 0.6625122267484607, "coordinate_rescaled_density_outer_weight":
    0.16409418793651973}, "unnormalized_product_mass": 2.4, "printed_gaussian_integral":
    0.7071067811865475}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T054505Z-exemplar-multiview.json
  accessed_at: '2026-10-12T05:47:55Z'
  support: supports
  summary: 'No normalized identity collision across all 442 pinned AIO IDs, labels/scoped
    synonyms and 487 maintained IDs, names and aliases. Full-checkout searches include
    ignored and hidden files: 8 matched lines in the worktree and 9 in main. All six
    distinct matched texts were read; they concern the prior exemplar-clustering frontier,
    its source/query URLs and an unrelated FreeFem lexer token. Seven annotated AIO
    nodes and seven full native neighbors were inspected. The same pinned bytes retain
    the previously read 442 class labels and 138 semantic label/synonym rows. Absence
    is bounded to this snapshot and corpus.

    '
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Seven annotated CLASS nodes with outgoing edges; all 442 class labels and
    138 semantic rows retained from the prior complete reading of identical pinned
    bytes
  accessed_at: '2026-10-12T05:47:55Z'
  support: supports
  summary: 'All three records describe fitting and assignment algorithms for unlabeled
    observations. The inspected UnsupervisedClustering target denotes a task, so related_match
    preserves that abstraction difference. Clustering, UnsupervisedLearning and MachineLearningTask
    are less specific task associations; Model denotes a representation rather than
    the complete fitting procedure. Neither dimensionality reduction nor the pin''s
    deep neural RepresentationLearning definition identifies these procedures. No
    upstream subclass assertion is made.

    '
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261012T054505Z-exemplar-multiview.json
  locator: 'source_analysis.aio_mapping_inspection: seven generated and seven native
    full YAML readings'
  accessed_at: '2026-10-12T05:47:55Z'
  support: supports
  summary: Fixed-component weight EM, rate-distortion Blahut-Arimoto, EM, k-means,
    deterministic annealing EM, clustering by melting and SeLa distinguish general
    fitting components from complete exemplar procedures. Seven generated records
    provide task/model/representation boundaries. Contextual records receive no renewed
    scientific approval.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/exemplar-multiview-boundaries.py
  locator: Conditional versus joint mass, support/pruning, ranking stop, soft versus
    hard information, multiview objectives and density normalization
  accessed_at: '2026-10-12T05:47:55Z'
  snapshot_sha256: 9ea9eee10873abe3fb9ef66df527e9b25c0dc6de31d294578b1071da58815c66
  support: supports
  summary: Finite checks distinguish conditional/joint mass, support and pruning,
    beta-zero nonuniqueness, stable ranking from objective convergence, soft rate
    from hard cluster count, unweighted and weighted objectives, nested update ascent,
    density-scale effects and product-space normalization. These are curator illustrations,
    not historical software or empirical reproduction.
- evidence_id: exemplarbasedconvexclustering-source-0
  kind: primary_source
  reference: https://papers.neurips.cc/paper/3181-convex-clustering-with-exemplar-based-models.pdf
  locator: Section 2, PDF p. 3, Equation 3; Section 3, Equations 6-8; Section 4, PDF
    p. 4, expression after Equation 9; curator normalization checks; Section 2, PDF
    p. 3, Equation 4 and positive-support condition; Section 4, PDF p. 4, Equation
    9; curator support and beta-zero checks; Section 4, PDF pp. 4-5, Equation 9, pruning
    and similarity sparsification; curator finite pruning example; Section 5, PDF
    p. 5, hard assignment and loss of optimality; Figure 1 caption; curator finite
    soft-channel/MAP calculation; Sections 2-4, PDF pp. 2-4, Equations 2, 4, 6-9;
    conditional normalization from Equations 6-8; Sections 2-5, PDF pp. 2-5, Equations
    2, 4, 8-9 and hard-exemplar extraction
  accessed_at: '2026-10-12T05:29:43Z'
  snapshot_sha256: d15f7a33be58a8364e3d27d854da66f0f92b0beba690b7cb2ea687981c75dda9
  support: supports
  summary: Convex Clustering with Exemplar-Based Models. NIPS 2007 proceedings, volume
    20; official eight-page PDF, internally numbered 1-8. All pages, figures, captions
    and references visually read. Original printed statements and curator qualifications
    are distinguished; finite calculations are not historical empirical reproduction.
- evidence_id: unweightedmultiviewconvexmixtureclustering-source-0
  kind: primary_source
  reference: https://www.cs.uoi.gr/~arly/full/conferences/C64.pdf
  locator: Section 3, printed pp. 208-210 / PDF pp. 4-6, Equations 5-11; Section 3.2,
    printed p. 210 / PDF p. 6, Equation 11 and cost; Sections 4-5, printed pp. 210-214
    / PDF pp. 6-10; curator stable-ranking example; Section 3.2, printed pp. 209-210
    / PDF pp. 5-6, stopping discussion and Equation 10; Sections 3.1-3.2, printed
    pp. 208-209 / PDF pp. 4-5, Equations 6-9 and support condition
  accessed_at: '2026-10-12T05:37:11Z'
  snapshot_sha256: d0bde397e858b35c43abc00c1be5e3063790ded1da0fd768996c5517085d7766
  support: supports
  summary: Convex Mixture Models for Multi-view Clustering. ICANN 2009, Part II, LNCS
    5769, pp. 205-214; author-hosted ten-page proceedings PDF. All pages visually
    read; printed page = PDF page + 204. Original printed statements and curator qualifications
    are distinguished; finite calculations are not historical empirical reproduction.
- evidence_id: weightedmultiviewconvexmixtureclustering-source-0
  kind: primary_source
  reference: https://www.cs.uoi.gr/~arly/full/journals/J71.pdf
  locator: Section IV-A, printed p. 1928 / PDF p. 4, Equation 9; Appendix A, printed
    p. 1936 / PDF p. 12, Equations 17-21; curator product-mass and coordinate-rescaling
    examples; Section IV-B, printed p. 1929 / PDF p. 5, Equations 11-13 and Algorithm
    1; Appendix A, printed pp. 1936-1937 / PDF pp. 12-13, Equations 22-28; Section
    IV-B, printed p. 1929 / PDF p. 5, third implementation remark; Section V-A, printed
    p. 1930 / PDF p. 6, Gaussian factor and explicit removal; curator Gaussian-integral
    check; Section IV-B, printed pp. 1928-1929 / PDF pp. 4-5; Appendix A, printed
    pp. 1936-1937 / PDF pp. 12-13; curator two-view objective/update comparison; Section
    IV-B, printed pp. 1929-1930 / PDF pp. 5-6, Equations 14-15; Section IV-C, PDF
    p. 6; Appendix B, printed p. 1937 / PDF p. 13, Equations 29-34; Sections IV-A/IV-B,
    printed pp. 1928-1930 / PDF pp. 4-6, Equations 9-15 and Algorithm 1
  accessed_at: '2026-10-12T05:33:45Z'
  snapshot_sha256: 6b6c13d90ee99bdaa09f28d7f065df0bd9bbb6c775eb02bb014c01df47915d3d
  support: supports
  summary: Multiple View Clustering Using a Weighted Combination of Exemplar-Based
    Mixture Models. IEEE Transactions on Neural Networks 21(12):1925-1938, December
    2010. Author-hosted journal PDF; all 14 pages, tables and appendices visually
    read. Printed page = PDF page + 1924. Original printed statements and curator
    qualifications are distinguished; finite calculations are not historical empirical
    reproduction.
assessments:
- assessment_id: exemplarbasedconvexclustering
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:ExemplarBasedConvexClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - exemplarbasedconvexclustering-source-0
  summary: 'This is the Lashkari-Golland procedure, also described as convex mixture
    model clustering. Its data-derived exemplar dictionary and hard extraction policy
    specialize fixed-component weight EM and finite rate-distortion Blahut-Arimoto.
    It is distinct from moving-centroid k-means, neural balanced transport in SeLa,
    scale-persistence melting, and fusion-penalty methods also called convex clustering.
    CMM and CCE are searched contextual acronyms, not unqualified identity aliases.
    No normalized identity collision across all 442 pinned AIO IDs, labels/scoped
    synonyms and 487 maintained IDs, names and aliases. Full-checkout searches include
    ignored and hidden files: 8 matched lines in the worktree and 9 in main. All six
    distinct matched texts were read; they concern the prior exemplar-clustering frontier,
    its source/query URLs and an unrelated FreeFem lexer token. Seven annotated AIO
    nodes and seven full native neighbors were inspected. The same pinned bytes retain
    the previously read 442 class labels and 138 semantic label/synonym rows. Absence
    is bounded to this snapshot and corpus.'
  details: 'For N indexed observations, fixed finite dissimilarities d_ij and beta>=0,
    set S_ij=exp(-beta*d_ij). Minimize J(q)=-(1/N)sum_i log(sum_j q_j S_ij) over simplex
    weights with positive initialization. With z_i=sum_j q_j S_ij, set r_ij=q_j S_ij/z_i
    and q_j_new=(1/N)sum_i r_ij. Equivalently, the row-conditional channel minimizes
    I(I;J)+beta*E[d_ij] with a uniform data-index source. A valid common-base component
    family additionally gives the stated mixture-likelihood interpretation; Gaussian
    components use squared Euclidean distance. For finite positive kernels and positive
    initialization, the exact unpruned iteration converges to a global optimum of
    the restricted soft weight objective. This is not a global fit of freely moving
    mixture components. Convexity does not imply unique coefficients: at beta=0 every
    q is fixed and optimal. Zero weights stay zero and can exclude useful exemplars;
    exact positive-kernel finite iterations preserve positive weights. At an optimum
    eta_j=(1/N)sum_i S_ij/z_i equals one on positive weights and is at most one on
    inactive coordinates, rather than necessarily strictly less. The 2007 visualization
    policy first selects every exemplar index that maximizes r_ij for at least one
    observation, then assigns each observation to its closest selected exemplar. Tie
    handling is not specified. This differs from the later multiview top-M policy.
    Beta controls the soft distortion tradeoff but does not uniquely determine a universally
    correct hard cluster count. Hardening does not retain the soft optimum guarantee
    or a general bound I<=log(K_hard): for points (0,1,3), squared distance and beta=1/4,
    the saved near-optimal soft solution has I about 0.03228 nats while this MAP policy
    selects only the middle point. The dense exact update uses two matrix-vector operations
    with O(N^2) work per iteration. The paper separately proposes deleting weights
    below 10^-3/N and renormalizing, and retaining only a rowwise subset of large
    similarities. These approximations can change the feasible set or objective and
    need not preserve the full soft optimum. The saved two-point example shows the
    stated pruning threshold removing a small but useful positive component. The expression
    r_ij=q_j S_ij/(N z_i) after Equation 9 is joint data-index/exemplar mass, not
    the row-conditional r defined in Equation 6; the conditional omits N. Literal
    KL from an atomic empirical measure to a continuous density is not finite merely
    by evaluating that density at data points. The finite-index objective and normalized
    responsibilities above avoid transferring that common-measure ambiguity from Equation
    3. Limitations: Sparsity at an asymptotic limit, numerical pruning, and the selected
    hard exemplars are different notions. Neither every beta change nor every initialization
    produces a distinct optimum. Natural-log objectives use nats; bit rates require
    consistent log-base and multiplier conversion. A slope statement for the rate-distortion
    curve needs differentiability or a supporting-slope interpretation. Synthetic
    source comparisons tune beta using class labels and do not establish universal
    performance or a biological application. No historical software or benchmark was
    reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A source-defined exemplar fitting and assignment algorithm, not a
      trained model instance or task class.
    evidence_ids:
    - exemplarbasedconvexclustering-source-0
  - name: aio-assessment
    value: related_match
    definition: 'All three records describe fitting and assignment algorithms for
      unlabeled observations. The inspected UnsupervisedClustering target denotes
      a task, so related_match preserves that abstraction difference. Clustering,
      UnsupervisedLearning and MachineLearningTask are less specific task associations;
      Model denotes a representation rather than the complete fitting procedure. Neither
      dimensionality reduction nor the pin''s deep neural RepresentationLearning definition
      identifies these procedures. No upstream subclass assertion is made.

      '
    evidence_ids:
    - mapping
- assessment_id: unweightedmultiviewconvexmixtureclustering
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:UnweightedMultiviewConvexMixtureClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - unweightedmultiviewconvexmixtureclustering-source-0
  summary: 'This is the unweighted Tzortzis-Likas 2009 procedure. Shared q couples
    corresponding exemplar indices across views, while each view retains its own fixed
    component family and scale. It averages view-specific log objectives and responsibilities;
    fixing uniform view weights inside the later weighted log-of-sum objective does
    not recover this procedure. The original sum-of-posteriors hard assignment and
    top-M ranking stop are retained explicitly. No normalized identity collision across
    all 442 pinned AIO IDs, labels/scoped synonyms and 487 maintained IDs, names and
    aliases. Full-checkout searches include ignored and hidden files: 8 matched lines
    in the worktree and 9 in main. All six distinct matched texts were read; they
    concern the prior exemplar-clustering frontier, its source/query URLs and an unrelated
    FreeFem lexer token. Seven annotated AIO nodes and seven full native neighbors
    were inspected. The same pinned bytes retain the previously read 442 class labels
    and 138 semantic label/synonym rows. Absence is bounded to this snapshot and corpus.'
  details: 'For N observations with V aligned views, fix view-specific component values
    f_vij=f_vj(x_vi) and common simplex weights q_j. Minimize -(1/(N V))sum_vi log
    Q_vi, where Q_vi=sum_j q_j f_vij. Set q_j_new=q_j/(N V)*sum_vi f_vij/Q_vi. Each
    view contributes its average current responsibilities equally. Common factors
    depending on the view and observation but not the exemplar cancel in this update.
    With finite positive component values, positive support and exact unpruned iteration,
    the soft convex problem attains a global optimum; coefficient uniqueness is not
    implied. Given a requested M, retain the M largest fitted q values as exemplars,
    each anchoring its own cluster. Assign every other observation to the selected
    exemplar maximizing sum_v q_j f_vij/Q_vi. This sums per-view posteriors, rather
    than multiplying densities or taking the maximum over individual views. The source
    uses strict comparisons without a tie policy. Its implementation stops when the
    selected top-M indices and their ranking stay unchanged for several consecutive
    iterations; this can occur before the soft objective is optimized. View families
    and beta_v values remain supplied choices. The empirical scale N^2 log(N)/sum_ij
    d_vij is a search guide and is undefined when its denominator vanishes. The fitting
    update needs O(N^2 V) dense arithmetic per iteration, apart from distance construction.
    A fixed-M hard partition has no transferred global-optimum guarantee; stable ranking
    is not a bound on residual objective error. Equal view contribution also does
    not guarantee robustness to uninformative or systematically biased views. Limitations:
    The record uses the finite evaluated-component/log-likelihood objective; the source
    empirical-versus-continuous KL shorthand requires a compatible measure or lift.
    Gaussian exponents use squared Euclidean distances. The soft fit is a shared-weight
    specialization of fixed-component EM. The complete multiview data construction,
    equal-view objective and sum-of-posteriors/top-M policy define this narrower algorithm.
    Source experiments remove observations lacking required views and select scale
    multipliers by label entropy. They do not establish an intrinsic missing-view
    algorithm, fully label-free model selection, or universal performance. No historical
    experiment was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A source-defined exemplar fitting and assignment algorithm, not a
      trained model instance or task class.
    evidence_ids:
    - unweightedmultiviewconvexmixtureclustering-source-0
  - name: aio-assessment
    value: related_match
    definition: 'All three records describe fitting and assignment algorithms for
      unlabeled observations. The inspected UnsupervisedClustering target denotes
      a task, so related_match preserves that abstraction difference. Clustering,
      UnsupervisedLearning and MachineLearningTask are less specific task associations;
      Model denotes a representation rather than the complete fitting procedure. Neither
      dimensionality reduction nor the pin''s deep neural RepresentationLearning definition
      identifies these procedures. No upstream subclass assertion is made.

      '
    evidence_ids:
    - mapping
- assessment_id: weightedmultiviewconvexmixtureclustering
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:WeightedMultiviewConvexMixtureClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - weightedmultiviewconvexmixtureclustering-source-0
  summary: 'This is the Tzortzis-Likas 2010 weighted multiview CMM procedure. Despite
    the inherited CMM name, its joint objective is not convex. It uses the log of
    a view-weighted sum of exemplar scores, whereas the 2009 algorithm sums view log
    likelihoods. This record distinguishes the general component-value formulation
    from the distance-only experimental variant that omits density base factors, and
    does not assert that marginal densities on different view spaces automatically
    define a joint generative model. No normalized identity collision across all 442
    pinned AIO IDs, labels/scoped synonyms and 487 maintained IDs, names and aliases.
    Full-checkout searches include ignored and hidden files: 8 matched lines in the
    worktree and 9 in main. All six distinct matched texts were read; they concern
    the prior exemplar-clustering frontier, its source/query URLs and an unrelated
    FreeFem lexer token. Seven annotated AIO nodes and seven full native neighbors
    were inspected. The same pinned bytes retain the previously read 442 class labels
    and 138 semantic label/synonym rows. Absence is bounded to this snapshot and corpus.'
  details: 'Given fixed positive component values f_vij, let Q_vi(q)=sum_j q_j f_vij
    and maximize L(q,pi)=sum_i log(sum_v pi_v Q_vi(q)) with q and pi on their respective
    simplices. From the current parameters compute gamma_iv=pi_v Q_vi/sum_w pi_w Q_wi.
    Set pi_v_new=(1/N)sum_i gamma_iv. Hold these outer responsibilities fixed while
    iterating q_j <- q_j/N*sum_iv gamma_iv f_vij/Q_vi(q), using the current inner
    q in the denominator. Repeat inner updates to their stated tolerance, then recompute
    outer responsibilities. The paper starts both weight vectors uniformly and uses
    inner L1-change and outer objective-change stopping conditions. The objective
    is separately concave in either weight vector with the other fixed, but not jointly
    concave in general. The nested surrogate updates support objective ascent for
    admissible exact arithmetic; a finite inner tolerance is an approximate M-step.
    Uniform starts, small objective changes or successful source examples do not prove
    global optimality, a unique limit, or that every stationary outcome is a local
    maximum. Uniform pi also leaves a log-of-sum objective, not the unweighted sum-of-logs
    objective. The source writes a sum of marginal densities Q_v(x_v) as a density
    of the full view tuple. That sum is not automatically normalized on the product
    observation space without an appropriate common observation model or background
    factors. For two- and three-state view alphabets, its total mass is 3*pi_1+2*pi_2.
    The finite positive-score objective still has meaningful normalized responsibilities
    and surrogate updates, but does not by itself establish the asserted generative
    interpretation. View-specific density scales affect the learned pi; they are not
    pure measures of semantic view quality. The general outer gamma calculation retains
    C_v(x_vi) from f_vij=C_v(x_vi)exp(-beta_v*d_vij). These factors cancel within
    the inner q update but not generally across views in gamma. The experiments explicitly
    omit them from the outer update to work from distances alone; this optimizes a
    modified affinity-score objective unless the factors cancel across views. With
    exp(-beta*||x-m||^2), the normalized Gaussian factor is (beta/pi)^(d/2), rather
    than the printed (beta/(2*pi))^(d/2). Source benchmark results for omitted factors
    do not certify the normalized-density formulation. After fitting, select a specified
    M largest-q exemplars and anchor each to its own cluster. Assign other observations
    by maximizing q_j sum_v pi_v f_vij among the selected exemplars. The full-component
    denominator is shared and cancels for this comparison; the selected-subset scores
    need not sum to one as M-cluster probabilities without renormalization. Ties need
    an explicit policy. Dense training costs O(N^2 V tau tau_inner), excluding initial
    distances. Kernel squared distances can supply a feature-space realization, but
    a generic dissimilarity matrix does not automatically establish a normalized feature-space
    density. Limitations: All views must be aligned to the same observation and exemplar
    indices. The source explicitly does not model general dependence between views
    and notes failures with systematic inter-view bias. The number of final exemplars
    and each component scale remain supplied choices. Hard assignment is separate
    from soft fitting and has no global clustering guarantee. Zero weights remain
    excluded; positivity and nonzero denominators matter. The empirical comparisons
    use complete-view filtering, specified cluster counts, label-based scale selection
    and optional kernel-k-means fine-tuning. They do not establish general noise immunity,
    semantic calibration of view weights, or universal superiority. No author software
    or historical benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A source-defined exemplar fitting and assignment algorithm, not a
      trained model instance or task class.
    evidence_ids:
    - weightedmultiviewconvexmixtureclustering-source-0
  - name: aio-assessment
    value: related_match
    definition: 'All three records describe fitting and assignment algorithms for
      unlabeled observations. The inspected UnsupervisedClustering target denotes
      a task, so related_match preserves that abstraction difference. Clustering,
      UnsupervisedLearning and MachineLearningTask are less specific task associations;
      Model denotes a representation rather than the complete fitting procedure. Neither
      dimensionality reduction nor the pin''s deep neural RepresentationLearning definition
      identifies these procedures. No upstream subclass assertion is made.

      '
    evidence_ids:
    - mapping
- assessment_id: complete-procedures
  area: consistency
  topic: Shared mathematical components do not establish identity
  outcome: supported
  target_ids:
  - AIMech:ExemplarBasedConvexClustering
  - AIMech:UnweightedMultiviewConvexMixtureClustering
  - AIMech:WeightedMultiviewConvexMixtureClustering
  evidence_ids:
  - neighbors
  - finite-boundaries
  summary: Retain the single-view, unweighted multiview and weighted multiview procedures.
  details: The single-view algorithm fixes every datum as a candidate exemplar, fits
    simplex weights and uses posterior-MAP selection followed by nearest-exemplar
    grouping. The 2009 multiview method shares weights across aligned views, averages
    view log objectives and sums view posteriors for a specified top-M grouping. The
    2010 method learns view weights through a log-of-sum objective and nested updates,
    then uses weighted component scores. Even uniform view weights do not recover
    the unweighted objective.
- assessment_id: soft-support-and-hardening
  area: consistency
  topic: Convex soft fitting versus approximate and hard policies
  outcome: supported
  target_ids:
  - AIMech:ExemplarBasedConvexClustering
  evidence_ids:
  - exemplarbasedconvexclustering-source-0
  - finite-boundaries
  summary: Preserve support, normalization and hardening qualifications.
  details: The source conditional expression after Equation 9 includes an extra factor
    N relative to its earlier row-conditional definition; it instead normalizes joint
    index mass. Exact full-support fitting retains the convex soft objective. At beta
    zero all simplex weights are fixed optima, and inactive optimal coordinates need
    only eta<=1. The source pruning threshold can delete a useful component. On points
    (0,1,3), beta=1/4 and squared distances, the saved near-optimal soft solution
    has positive information 0.03228 nats but only one MAP-selected exemplar; the
    caption bound involving the hard count is not general. Numerical closeness to
    the optimum is not an exact symbolic proof.
- assessment_id: unweighted-ranking-and-assignment
  area: consistency
  topic: Actual 2009 stopping and assignment rules
  outcome: supported
  target_ids:
  - AIMech:UnweightedMultiviewConvexMixtureClustering
  evidence_ids:
  - unweightedmultiviewconvexmixtureclustering-source-0
  - finite-boundaries
  summary: Keep the sum-of-posteriors policy and distinguish ranking stability from
    optimization.
  details: Section 3.2 and Equation 10 specify anchored top-M exemplars and a sum
    over view posteriors. The source stops after unchanged selected indices and ordering
    across several iterations; it does not provide a residual objective certificate.
    A positive two-point example retains its ranking for five updates with objective
    error about 0.00443. Strict assignment comparisons leave ties unspecified, and
    the beta search guide is undefined for zero total dissimilarity.
- assessment_id: weighted-nested-objective
  area: consistency
  topic: Nested update order, objective shape and posterior scope
  outcome: supported
  target_ids:
  - AIMech:WeightedMultiviewConvexMixtureClustering
  evidence_ids:
  - weightedmultiviewconvexmixtureclustering-source-0
  - finite-boundaries
  summary: Retain the frozen outer responsibilities during inner shared-weight fitting.
  details: The general positive-score objective is separately concave but not jointly
    concave. The paper computes view responsibilities from current q and pi, updates
    pi, then iterates q with the outer responsibilities held fixed. The saved calculation
    distinguishes this from one unweighted update and checks ascent. Finite inner
    tolerance is an approximate M-step; source convergence prose does not establish
    a unique global solution or universal local maximum. Selected scores require renormalization
    to act as an M-component probability distribution.
- assessment_id: weighted-density-calibration
  area: consistency
  topic: Observation space, density units and experimental base-factor omission
  outcome: supported
  target_ids:
  - AIMech:WeightedMultiviewConvexMixtureClustering
  evidence_ids:
  - weightedmultiviewconvexmixtureclustering-source-0
  - finite-boundaries
  summary: Qualify the source generative and view-quality interpretation.
  details: 'A weighted sum of densities on separate view domains is not automatically
    normalized on their product space: two- and three-state alphabets give total mass
    3*pi_1+2*pi_2. Component base factors cancel inside the inner q ratio but affect
    the outer view responsibilities. Section V-A explicitly drops these factors for
    distance-only experiments. The printed Gaussian factor with exp(-beta*distance_squared)
    integrates to 2^(-d/2), not one. A coordinate rescaling preserving the kernel
    changes the normalized-density view update; learned pi is not solely semantic
    view quality. These are bounded mathematical deductions, not claims that every
    practical affinity variant is invalid.'
- assessment_id: identity-and-aio
  area: grounding
  topic: Corpus scope, mappings and incomplete discovery
  outcome: supported
  target_ids:
  - AIMech:ExemplarBasedConvexClustering
  - AIMech:UnweightedMultiviewConvexMixtureClustering
  - AIMech:WeightedMultiviewConvexMixtureClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Maintain local DRAFT records and related task mappings.
  details: All 442 pinned AIO identities and 487 prior native identities were compared,
    with ignored and hidden checkout files included. All six distinct match texts
    were inspected. Seven annotated AIO targets, seven native neighbors and seven
    generated YAMLs were read. The unchanged snapshot permits reuse of the previously
    read class-label and semantic-synonym inventories. Algorithms relate to the UnsupervisedClustering
    task without equivalence or subclass assertions. The complete selected three-record
    cohort is reviewed; 411 pending frontier cohorts remain outside this review.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:ExemplarBasedConvexClustering
  - AIMech:UnweightedMultiviewConvexMixtureClustering
  - AIMech:WeightedMultiviewConvexMixtureClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - exemplarbasedconvexclustering-source-0
  - unweightedmultiviewconvexmixtureclustering-source-0
  - weightedmultiviewconvexmixtureclustering-source-0
  rationale: The three complete procedures differ in view construction, soft objective,
    optimization order and hard extraction. Common fixed-component fitting does not
    erase these distinctions. Related task mappings preserve abstraction without asserting
    upstream subclasses.
limitations:
- Adversarial author self-review only; all three records remain DRAFT.
- All 8 pages of the 2007 proceedings,10 pages of the 2009 multiview proceedings and
  14 pages of the 2010 journal paper were visually read, including formulas, algorithm
  boxes, tables, appendices and references.
- The original single-view hard-MAP/nearest-exemplar extraction differs from the 2009
  top-M and sum-of-view-posteriors policy. The 2010 weighted scores and nested view/shared-weight
  updates use a different objective, even at equal view weights.
- Source-prose qualifications preserve conditional versus joint assignment normalization,
  exact versus pruned support, soft versus hard guarantees, ranking stopping, finite
  score objectives versus literal atomic/continuous KL, and density factors omitted
  in the 2010 experiments.
- The weighted sum of view marginal densities is not automatically a normalized joint
  density on their product space. Positive-score objectives and surrogate updates
  remain meaningful, but learned view weights depend on relative score or density
  scales. No unsupported joint generative or pure view-quality interpretation is asserted.
- Synthetic and document/image benchmarks were read for scope, not reproduced or promoted
  into universal performance. Supplied cluster counts, complete-view filtering, label-guided
  scale selection and optional postprocessing remain explicit.
- Three new cohorts remain provisional with primary access limitations. No author
  software, model training, paid service or full-paper redistribution occurred. Three
  additions bring the native collection to 490;442 pinned AIO records are unchanged.
  No literature saturation.
links: []
tags:
- native-concepts
- exemplar-multiview
- self-review
- discovery-ongoing
```
