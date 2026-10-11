# Scientific self-review of graph clustering and N-pair objectives

- Review: 20261011T093722Z-graph-clustering-npair
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T09:37:09Z
- Finished UTC: 2026-10-11T09:37:22Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain five source-backed DRAFT concepts with scoped mappings and explicit source contradictions. Issues51–53 have supported current-state fixes. No actionable finding remains within the declared five-record scope.

## Scope And Provenance

All fields of five new maintained graph-clustering/metric-loss concepts.

Selection: Exact five added IDs in the discovery report; no sampling.
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base e39e9064784a03aa4a331e7e1df7960a86275885.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:PowerIterationClustering | data/curated/PowerIterationClustering.yaml | maintained | Power iteration clustering |
| AIMech:ZetaMerging | data/curated/ZetaMerging.yaml | maintained | Zeta merging |
| AIMech:CHAMELEONClustering | data/curated/CHAMELEONClustering.yaml | maintained | CHAMELEON clustering |
| AIMech:MultiClassNPairLoss | data/curated/MultiClassNPairLoss.yaml | maintained | Multi-class N-pair loss |
| AIMech:OneVsOneNPairLoss | data/curated/OneVsOneNPairLoss.yaml | maintained | One-vs-one N-pair loss |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:PowerIterationClustering, AIMech:ZetaMerging, AIMech:CHAMELEONClustering, AIMech:MultiClassNPairLoss, AIMech:OneVsOneNPairLoss | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 56.45s<br>Checked 442 record(s); 0 failed.<br>Checked 223 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 48 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 45,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:PowerIterationClustering, AIMech:ZetaMerging, AIMech:CHAMELEONClustering, AIMech:MultiClassNPairLoss, AIMech:OneVsOneNPairLoss | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| Finite Zeta popularity counterexample | passed | True | AIMech:ZetaMerging | {"P": [[0, 1], [1, 0]], "z": "1/4", "det_I_minus_zP": "15/16", "inverse_diagonal": ["16/15", "16/15"], "epsilon": 0.06453852113757118, "chi_leave_one_out": 0.06453852113757118, "chi_resolvent": 0.06453852113757116, "printed_upper_bound_epsilon_over_n": 0.03226926056878559, "printed_upper_bound_satisfied": false, "algorithm_1_sufficient_z_bound_satisfied": true, "scope": "One counterexample to the printed inequality; no general replacement bound asserted."} |

## Scientific And Domain Assessments

### Identity, mechanism, evidence, limitations and mapping

evidence: supported. Targets: AIMech:PowerIterationClustering.

This is the Lin and Cohen ICML 2010 algorithm. Its qualified PIC alias is distinct from path integral clustering: it truncates a matrix iteration to form coordinates instead of merging clusters by resolvent descriptors. It is not a generic eigensolver or a claim that converging to the dominant eigenvector finds clusters. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 218 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 15 lines each in existing discovery/review context. Five neighboring native records and five exact AIO nodes with scoped synonyms and outgoing edges were inspected.

For a symmetric nonnegative similarity matrix A with zero diagonal and positive row sums, form D_ii=sum_j A_ij and W=D^−1 A. Starting with a nonnegative nonzero vector v, iterate v_next=Wv/&#124;&#124;Wv&#124;&#124;_1. Use an intermediate vector before convergence to the constant dominant right eigenvector. Following Algorithm 1 and the released pic.m, monitor d_next=abs(v_next−v) componentwise and stop when max_i abs(d_next_i−d_i) is sufficiently small, subject to an iteration cap. Apply k-means to the scalar coordinates v_i for the requested k clusters. Degree-proportional initialization is described, and multiple random initial vectors may supply several embedding coordinates. Section 2.4 prose instead writes signed differences; the absolute-change convention here is explicitly the pseudocode/implementation convention. The stopping convention follows the paper pseudocode and released code, which use componentwise absolute first changes. The surrounding prose uses signed first changes. The released driver also uses a tolerance 100 times the paper’s stated experimental tolerance. These source differences are preserved rather than silently reconciled. Limitations: The stopping test is a heuristic for a useful intermediate embedding, not a certificate of cluster recovery. A regular graph with degree-proportional initialization starts at a constant vector and can yield no separating coordinates. Positive row sums are required for the stated row-stochastic normalization. Disconnected graphs, negative eigenmodes and collisions in a one-dimensional embedding limit a blanket spectral or convergence interpretation. The paper reports experimental tolerance 1e−5/n. The released experiment driver sets baseconv=0.001 and uses baseconv/n, with maxit=5000. These are different settings, not an asserted benchmark reproduction or proof that either setting is wrong. Choice of similarity, initialization, stopping rule and k-means solution affects the partition. No code was executed, and no runtime, accuracy or global-optimum claim is made.

### Identity, mechanism, evidence, limitations and mapping

evidence: supported. Targets: AIMech:ZetaMerging.

Zeta merging is the named Algorithm 1 component of Zhao and Tang’s Zell method. Its input is an already constructed weighted graph and initial partition; it does not prescribe the l-links initialization. It differs from path integral clustering, which averages all endpoint-to-endpoint resolvent entries rather than logarithms of diagonal entries. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 218 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 15 lines each in existing discovery/review context. Five neighboring native records and five exact AIO nodes with scoped synonyms and outgoing edges were inspected.

Given a fixed nonnegative weighted adjacency P, a nonempty initial partition and target count m_c smaller than its initial count, choose damping 0&lt;z&lt;1/(2&#124;&#124;P&#124;&#124;_1), the sufficient range stated in Section 3.1 for nonzero P. For a cluster C use the principal submatrix P_C without local renormalization and R_C=(I−zP_C)^−1. Its popularity is chi_C=(1/&#124;C&#124;) sum_(i in C) log (R_C)_ii. Equivalently it is the average leave-one-vertex-out reduction of epsilon_C=−log det(I−zP_C). For U=A union B, chi_(A&#124;U) averages log (R_U)_ii over i in A with divisor &#124;A&#124;. Merge the current pair maximizing (chi_(A&#124;U)−chi_A)+(chi_(B&#124;U)−chi_B); recompute affected affinities and repeat to m_c. The conditional increment is not chi_U−chi_A−chi_B. Curator calculation: for P=[[0,1],[1,0]], z=1/4 and C both vertices, det(I−zP)=15/16 and both diagonal entries of (I−zP)^−1 are 16/15. Thus epsilon_C=chi_C=log(16/15)&gt;epsilon_C/2. The z choice satisfies Section 3.1’s sufficient norm bound. The printed upper bound after Theorem 2 is not adopted. The reproducible finite calculation is saved as research/discovery/zeta-popularity-bound.py; it is not a benchmark of the clustering procedure. Limitations: Initialization, graph weights, damping and requested count determine the result; greedy merges cannot undo an initial grouping or certify a global partition optimum. The paper prints z&lt;rho(W) in Theorem 1, whereas the cycle power series requires &#124;z&#124;rho(W)&lt;1. This record uses the stricter positive norm bound actually stated for Algorithm 1, rather than importing the printed general condition. The printed bound 0&lt;chi_C&lt;=epsilon_C/&#124;C&#124; is not used. A two-vertex mutual-edge graph with z=1/4 gives chi_C=epsilon_C=log(16/15)&gt;epsilon_C/2 under the paper’s own definitions; this is a curator counterexample, not an author erratum. Zell’s full l-links and bandwidth conventions require separate clarification and are not specified by this component. No generic sparse-inverse runtime guarantee, automatic correct cluster count, or benchmark reproduction is asserted.

### Identity, mechanism, evidence, limitations and mapping

evidence: supported. Targets: AIMech:CHAMELEONClustering.

This record covers the two-phase CHAMELEON procedure in Technical Report 99-007, including the two merge-selection alternatives described there. Dynamic modeling means recomputing cluster-relative graph statistics, not learning a neural representation. The inspected source is the 22-page report, not the eight-page final Computer article. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 218 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 15 lines each in existing discovery/review context. Five neighboring native records and five exact AIO nodes with scoped synonyms and outgoing edges were inspected.

Construct a weighted undirected k-nearest-neighbor graph by retaining an edge when either endpoint lists the other among its k most similar points. Obtain small initial subclusters by repeated balanced graph bisection, selecting the largest current subcluster; the report uses hMETIS with each child holding at least 25 percent of its parent and stops when the largest subcluster is below MINSIZE. For clusters A,B, relative interconnectivity RI is the total cross-edge weight divided by the mean of the two internal bisection-cut weights. Relative closeness RC is the mean cross-edge weight divided by the size-weighted mean of the two mean internal bisection-edge weights. One merge scheme maximizes RI(A,B)*RC(A,B)^alpha over pairs; this is the scheme used for the report’s dendrogram experiments. An alternative visits clusters and selects their most strongly connected eligible neighbor subject to separate RI and RC thresholds, permitting multiple merges per iteration and either stopping or relaxing thresholds when no pair qualifies. Limitations: Meaningful nonzero internal cut statistics and nonempty cross-edge sets are needed to evaluate the ratios. Very small or disconnected subclusters can make the estimates unstable or undefined; a zero-denominator policy is not supplied by this record. Neighbor size, similarity, initial granularity, bisection balance and merge parameters influence results. The initial partition and later merges may cross desired cluster boundaries; the procedure does not establish semantic recovery. The product-score and threshold-based schemes have different selection and stopping behavior; they are documented alternatives within the original named procedure, not assumed identical algorithms. Internal cuts are computed by graph-partitioning software; describing the min-cut objective does not certify a global exact cut solver. Runtime depends in part on neighbor search and data dimension. No implementation or reported benchmark was reproduced.

### Identity, mechanism, evidence, limitations and mapping

evidence: supported. Targets: AIMech:MultiClassNPairLoss.

This is Sohn’s N-pair-mc objective, Equation (7), together with its distinct-class positive-pair batching. The source also uses unqualified N-pair loss for a family including N-pair-ovo, so that family name is not an exact alias of this member. Its per-anchor categorical form is shared with generic InfoNCE at dot-product scores, but the named supervised batching configuration is retained explicitly. It is not the full SimCLR procedure or NT-Xent’s cosine-temperature two-view construction. N-pair-ovo instead sums individual pairwise softplus terms. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 218 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 15 lines each in existing discovery/review context. Five neighboring native records and five exact AIO nodes with scoped synonyms and outgoing edges were inspected.

Take N&gt;=2 classes and two examples (x_i,x_i+) from each class. Encode 2N examples to f_i and f_i+. The Equation (7) objective is L_mc=(1/N) sum_i log[1+sum_(j!=i) exp(f_i^T f_j+−f_i^T f_i+)]. Each anchor has its paired positive and N−1 negative candidates from the positive side of other classes. Sharing these candidates across anchors forms N tuplets using 2N forward embeddings. Equation (7) specifies one orientation; footnote 2 also mentions a symmetric loss that swaps the anchor/positive roles, without specifying its aggregation in that footnote. No explicit temperature or cosine normalization appears in this expression. Limitations: Use N positive pairs from N distinct classes; other positive-side examples must represent different classes for the stated objective. Pair sampling and class selection are part of this configuration, not interchangeable with arbitrary augmented-view negatives. The main paper uses embedding-norm regularization instead of a hard unit-length constraint. This record specifies the loss term; it does not prescribe a regularization coefficient, encoder, optimizer or full training schedule. No unconditional equivalence to a margin triplet hinge or an information lower bound is asserted. Objective shape and label-based batching do not establish downstream accuracy. No training or benchmark was reproduced. The proceedings Supplemental.zip inspected during retrieval contains a different paper by Steinhardt and Liang. It is not supporting evidence; this record relies on the inspected nine-page N-pair main paper.

### Identity, mechanism, evidence, limitations and mapping

evidence: supported. Targets: AIMech:OneVsOneNPairLoss.

This is the named N-pair-ovo objective in Sohn’s Equation (8). It shares the N-pair batch construction with N-pair-mc but uses a sum of binary softplus comparisons, not one joint log-sum-exp over negatives. They coincide for one negative per anchor (N=2), but generally differ for N&gt;2. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 218 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 15 lines each in existing discovery/review context. Five neighboring native records and five exact AIO nodes with scoped synonyms and outgoing edges were inspected.

Given N&gt;=2 positive pairs (x_i,x_i+) from N distinct classes and embeddings f_i,f_i+, define L_ovo=(1/N) sum_i sum_(j!=i) log[1+exp(f_i^T f_j+−f_i^T f_i+)]. Other positive-side examples supply N−1 different-class negatives to each anchor. The printed divisor is N, not N(N−1), so it averages across anchors while summing each anchor’s pairwise comparisons. In contrast, N-pair-mc places the sum over negatives inside a single logarithm. The expression uses dot products without an explicit temperature or cosine normalization. Limitations: Use N positive pairs from N distinct classes; other positive-side examples must represent different classes for the stated objective. Pair sampling and class selection are part of this configuration, not interchangeable with arbitrary augmented-view negatives. The main paper uses embedding-norm regularization instead of a hard unit-length constraint. This record specifies the loss term; it does not prescribe a regularization coefficient, encoder, optimizer or full training schedule. No unconditional equivalence to a margin triplet hinge or an information lower bound is asserted. Objective shape and label-based batching do not establish downstream accuracy. No training or benchmark was reproduced. The proceedings Supplemental.zip inspected during retrieval contains a different paper by Steinhardt and Liang. It is not supporting evidence; this record relies on the inspected nine-page N-pair main paper.

### Power iteration initialization, stopping and source conventions

consistency: supported. Targets: AIMech:PowerIterationClustering.

Retain the pseudocode/implementation absolute-change convention with paper/code discrepancies explicit.

The iteration is on W=D^−1A with symmetric nonnegative A, not a path-integral agglomeration. Stopping is heuristic; degree initialization on regular graphs can be constant, and one-dimensional coordinates can collide. The prose signed-change expression and100fold experimental-tolerance difference are recorded without an invented reconciliation. The final locator correctly names Sections2.1–2.4.

### Conditional log-diagonal popularity and challenged printed bound

consistency: supported. Targets: AIMech:ZetaMerging.

Retain Algorithm1 as a component independent of unresolved fullZell initialization details.

Principal submatrices preserve global weights. The score averages log diagonal resolvent entries, with conditional union popularity normalized by each original cluster. This differs from all-entry path sums and from chi_union−chi_A−chi_B. The source’s positive norm bound ensures an admissible convergent regime. The printed spectral-radius condition and popularity inequality are not copied as guarantees; the finite counterexample is explicitly curator analysis.

### CHAMELEON relative measures and two merge schemes

consistency: supported. Targets: AIMech:CHAMELEONClustering.

Retain the original two-phase procedure with distinct cut-sum and cut-mean normalizations.

Graph edges use the union of directed nearest-neighbor membership. RI divides cross-weight sum by the average internal cut sum; RC divides average cross weight by a size-weighted mean of internal cut means. The initial largest-subcluster bisection and25percent balance are source-specific. Product RI*RC^alpha and threshold eligibility with maximum absolute cross-weight selection are separate documented alternatives; exact min-cut optimality and denominator handling are not invented.

### Multi-class versus one-vs-one N-pair objective boundaries

scope: supported. Targets: AIMech:MultiClassNPairLoss, AIMech:OneVsOneNPairLoss.

Retain two named loss members; do not make the whole N-pair family an alias of the multi-class member.

Both use N positive pairs from distinct classes and2N embeddings. Equation7 has one logarithm over the negative exponential sum; Equation8 sums separate softplus terms and divides byN only. They coincide forN2 but generally differ beyond one negative. Generic InfoNCE categorical form is acknowledged; no unconditional information bound, margin-hinge equivalence or NT-Xent identity asserted. Footnote2 mentions swapped roles but does not specify the averaging originally claimed. The unrelated supplemental archive is excluded.

### Task, objective and supervision scope

grounding: supported. Targets: AIMech:PowerIterationClustering, AIMech:ZetaMerging, AIMech:CHAMELEONClustering, AIMech:MultiClassNPairLoss, AIMech:OneVsOneNPairLoss.

Mappings remain related associations with abstraction and supervision differences explicit.

Three clustering algorithms have related task mappings; Zeta merging and CHAMELEON also relate to HierarchicalClustering. The N-pair losses have related-only ContrastiveLearning associations with the source’s supervised versus AIO’s self-supervised distinction explicit. No equivalence, subclass or upstream acceptance is asserted.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:PowerIterationClustering, AIMech:ZetaMerging, AIMech:CHAMELEONClustering, AIMech:MultiClassNPairLoss, AIMech:OneVsOneNPairLoss. Power-iteration coordinates, Zeta conditional log-diagonal linkage, CHAMELEON dynamic graph-cut procedure and two differently aggregated supervised N-pair losses have supported distinct scopes. Zeta merging is retained as a component without asserting fullZell conventions. Generic N-pair family identity is not assigned to the multi-class member. The multi-class loss shares categorical form with InfoNCE but specifies supervised batching. No AIO mutation or status promotion follows.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T093440Z-graph-clustering-npair.json | supports | No normalized identity match across442 AIO labels/scoped synonyms and218 preceding native IDs/names/aliases. Both full checkouts were searched including ignored/hidden files;15 lines each were existing discovery/review context. Five native neighbors and five exact AIO nodes were semantically compared. PIC alias is qualified. The genericN-pair family label was removed as an exact alias of the multi-class member after source review. |
| mapping | sources/aio/aio.json; Five exact CLASS nodes listed in source_analysis.aio_mapping_inspection: definitions, scoped synonyms and outgoing edges | supports | Three clustering algorithms have related task mappings; Zeta merging and CHAMELEON also relate to HierarchicalClustering. The N-pair losses have related-only ContrastiveLearning associations with the source’s supervised versus AIO’s self-supervised distinction explicit. No equivalence, subclass or upstream acceptance is asserted. |
| neighbors | research/discovery/20261011T093440Z-graph-clustering-npair.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | InfoNCE, NTXentLoss, PathIntegralClustering, GraphDegreeLinkage and KMeans were compared. The new records distinguish named supervised objectives, power-iteration embedding, log-diagonal popularity and dynamic graph cuts from these existing mechanisms. |
| corrections | research/discovery/20261011T093440Z-graph-clustering-npair.json; review_refinements: before/after hashes, actual edit times, issues51–53 | supports | Issue51 repairs Zeta calculation traceability; issue52 removes the generic N-pair family alias and an unsupported footnote aggregation; issue53 fixes a nonexistent section locator. Final records and changed citations were reread and re-inspected. These are current-state assessments, not invented predecessors to structured findings. |
| poweriterationclustering-source | https://icml.cc/Conferences/2010/papers/387.pdf; Sections 2.1–2.4, PDF pp. 1–4; Algorithm 1 and experimental stopping threshold on p. 4 | supports | Power Iteration Clustering. ICML 2010 proceedings paper, 8 PDF pages. Text pages read: [1]; actual image pages read: [2, 3, 4]. A clustering algorithm that uses an early-stopped power iteration of a normalized similarity matrix to embed observations and then applies k-means to their embedding coordinates. |
| zetamerging-source | https://papers.neurips.cc/paper/3412-cyclizing-clusters-via-zeta-function-of-a-graph.pdf; Sections 2.2–3.2, PDF pp. 3–4, Equations (2)–(5), Theorem 2 and Algorithm 1; Section 4.3, pp. 5–6, component boundary | supports | Cyclizing Clusters via Zeta Function of a Graph. Advances in Neural Information Processing Systems 21, NIPS 2008; 8-page proceedings PDF. Text pages read: [1]; actual image pages read: [2, 3, 4, 5, 6]. An agglomerative graph-clustering algorithm that selects the pair with the largest sum of conditional increases in average log-diagonal resolvent popularity. |
| chameleonclustering-source | https://www-users.cse.umn.edu/~kumar001/papers/chameleon.ps; Technical Report 99-007, Sections 4.1–4.4, printed pp. 5–11 (PDF pp. 6–12), Equations (1)–(4) | supports | CHAMELEON: A Hierarchical Clustering Algorithm Using Dynamic Modeling. University of Minnesota Technical Report 99-007, 1999, to appear in IEEE Computer; 22-page author PostScript, read via a local PDF conversion. Text pages read: []; actual image pages read: [1, 6, 7, 8, 9, 10, 11, 12]. A graph-clustering procedure that first partitions a sparse neighbor graph into small subclusters and then agglomerates them using interconnectivity and closeness normalized by their internal bisection statistics. |
| multiclassnpairloss-source | https://papers.nips.cc/paper_files/paper/2016/file/6b180037abbebea991d8b1232f8a8ca9-Paper.pdf; Sections 3.1–3.2.2, PDF pp. 3–5; Equations (3) and (7), footnotes 1–2, embedding regularization discussion | supports | Improved Deep Metric Learning with Multi-class N-pair Loss Objective. NIPS 2016 proceedings, 9-page main paper; the mislinked Supplemental.zip is not evidence for this method. Text pages read: [1]; actual image pages read: [2, 3, 4, 5]. A supervised metric-learning objective that averages a joint positive-versus-multiple-negative log-softmax loss across a batch of positive pairs drawn from distinct classes. |
| onevsonenpairloss-source | https://papers.nips.cc/paper_files/paper/2016/file/6b180037abbebea991d8b1232f8a8ca9-Paper.pdf; Section 3.2, PDF p. 4, Equations (7)–(8); Section 3.2.2, p. 5, regularization discussion | supports | Improved Deep Metric Learning with Multi-class N-pair Loss Objective. NIPS 2016 proceedings, 9-page main paper; the mislinked Supplemental.zip is not evidence for this method. Text pages read: [1]; actual image pages read: [2, 3, 4, 5]. A supervised metric-learning objective that sums separate positive-versus-negative softplus comparisons for each anchor in a batch of positive pairs from distinct classes. |
| author-code | https://www.cs.cmu.edu/~frank/code/icml2010-code.zip; pic.m, x_clusterembed_icml2010.m and readme.txt; eight actually read files and their hashes recorded in discovery report | supports | Original author-linked MATLAB archive. pic.m uses absolute component changes and an iteration cap; the driver passes baseconv/n with baseconv=.001 and5000 maximum iterations. These files were read, not executed. Archive checksum pins bytes; no release tag or commit is invented. |
| zeta-calculation | research/discovery/zeta-popularity-bound.py; calculate(): exact Fraction determinant/inverse entries and two independent evaluations of popularity | supports | Original curator arithmetic executed successfully: det15/16, inverse diagonal16/15, chi≈0.06453852 and printed upper bound≈0.03226926. The example satisfies the algorithm’s stated norm bound and refutes the displayed inequality without asserting a general replacement theorem or author erratum. |
| conversion | research/discovery/20261011T093440Z-graph-clustering-npair.json; CHAMELEON entry conversion and extraction_manifest | supports | Original author PostScript SHAda03091e656bf4b49f56c2c06a052949f6e91f761d1e5252d39392a8c99c1b69 was converted with gs-noX11 9.07 and -dSAFER; derived22page PDF SHA05de0220cf8e08fb5d67ddff44aa42cd2ab2fe3bd3b07c6430bdfd07442ea5a2. Title/abstract and full methodsPDF6–12 were visually inspected. The final8page journal version is not substituted. |

## Limits And Additional Notes

- Adversarial author self-review only; all five records remain DRAFT.
- Only declared source pages/code were inspected. CHAMELEON evidence is the22page technical report converted from author PostScript; the N-pair supplemental archive is unrelated and excluded.
- Source contradictions are qualified, not silently corrected as author-issued errata. The Zeta counterexample is original finite arithmetic, not a benchmark or general replacement theorem.
- Initial curated validation failed for a context-only asserted Zeta claim; the citation was repaired. An incorrect N-pair alias/aggregation and power-method locator were corrected and re-inspected before this final assessment.
- The first vendored check could not resolve its network hostname inside the sandbox; the authorized network retry passed. Final required checks are recorded, and no auto-review denial occurred.
- Prior immutable reviews are unchanged. Issue fixes are traced in the discovery ledger; no earlier structured finding is fabricated.
- Five positive additions and the retained frontier leave discovery active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T093722Z-graph-clustering-npair
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of graph clustering and N-pair objectives
started_at: '2026-10-11T09:37:09Z'
finished_at: '2026-10-11T09:37:22Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially compared all five current
    records against original equations/algorithms, inspected author code and exact
    AIO nodes, and reread/re-inspected corrected citations and identities. No independent
    approval is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain five source-backed DRAFT concepts with scoped mappings and explicit
  source contradictions. Issues51–53 have supported current-state fixes. No actionable
  finding remains within the declared five-record scope.
source:
  git_revision: e39e9064784a03aa4a331e7e1df7960a86275885
  state: working_tree
  inputs:
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/ContrastiveLearning.yaml
    sha256: f8100e15621b6dd3335dc0bc8253da0197719faf6ac00f1369ebbc455a6fa645
    role: context
  - path: data/aio/HierarchicalClustering.yaml
    sha256: 144deaecd150e22de207c11a62f19db5f8409443724bd4be4b5c95c53375b258
    role: context
  - path: data/aio/RepresentationLearning.yaml
    sha256: bc7af756440437f60210019e17ad1e2dd15cd1c7cbfbc96312520934b7a5c7ca
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/curated/CHAMELEONClustering.yaml
    sha256: 4e3440079afa10c2b7280c6c2c5073509039014a67a3a6fa71ca59a0117886e6
    role: target
  - path: data/curated/GraphDegreeLinkage.yaml
    sha256: 0bd60481926261ff2fb8d69f0404a5d0132f3de4f0c915758bfaffa77fd62f8f
    role: context
  - path: data/curated/InfoNCE.yaml
    sha256: b202ebcafc444df533d78ae82c3618d821ce4c5081a99ffe744deb644a6957da
    role: context
  - path: data/curated/KMeans.yaml
    sha256: 50fc1d8d18403a8f314636f68b6812ffd15fec2dfaaf4c32aaad423dfa7ffa03
    role: context
  - path: data/curated/MultiClassNPairLoss.yaml
    sha256: 530dc708100618d552ac603c69bdb3fe49c6acc1f1763a188556fb9dd316f828
    role: target
  - path: data/curated/NTXentLoss.yaml
    sha256: 523d119e71f1c16672b42300e2a180495f3a09c53a55385f546f02850fed3255
    role: context
  - path: data/curated/OneVsOneNPairLoss.yaml
    sha256: d16207c0d4fc9a43b3a95d1e0094849f4fe4269522406cdf9b0bf0727be58bb4
    role: target
  - path: data/curated/PathIntegralClustering.yaml
    sha256: 62630cc862cc363cc34037447fd70d0b1e793d8ccf0b3339e0777faaefd1172f
    role: context
  - path: data/curated/PowerIterationClustering.yaml
    sha256: ca81d60eb87c027126a3372950d40f50d0df8391b1075697e0ab5ffabf3dfa0f
    role: target
  - path: data/curated/ZetaMerging.yaml
    sha256: 0469af593ef72ac1d28ef38901a7871de1696e1aab05a6d0c409b6134784fb3e
    role: target
  - path: research/discovery/20261011T093440Z-graph-clustering-npair.json
    sha256: 102bc8000e1992c8606a26603e5f9c85562d8cd305e03aad9f9fc5801117f0d1
    role: context
  - path: research/discovery/zeta-popularity-bound.py
    sha256: ae305e805509e700e6ccca15b27c313df2edd30c938885bf7b7d0f6b29f47dfe
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 0600ec8ca628d2dac611f2a068074ebcd4b83b6b5f31832a32dbc4f4bfa35b06
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:PowerIterationClustering
  path: data/curated/PowerIterationClustering.yaml
  label: Power iteration clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PowerIterationClustering.yaml
    role: maintained
- target_id: AIMech:ZetaMerging
  path: data/curated/ZetaMerging.yaml
  label: Zeta merging
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ZetaMerging.yaml
    role: maintained
- target_id: AIMech:CHAMELEONClustering
  path: data/curated/CHAMELEONClustering.yaml
  label: CHAMELEON clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CHAMELEONClustering.yaml
    role: maintained
- target_id: AIMech:MultiClassNPairLoss
  path: data/curated/MultiClassNPairLoss.yaml
  label: Multi-class N-pair loss
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MultiClassNPairLoss.yaml
    role: maintained
- target_id: AIMech:OneVsOneNPairLoss
  path: data/curated/OneVsOneNPairLoss.yaml
  label: One-vs-one N-pair loss
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OneVsOneNPairLoss.yaml
    role: maintained
scope:
  description: All fields of five new maintained graph-clustering/metric-loss concepts.
  selection: Exact five added IDs in the discovery report; no sampling.
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - AIMech:PowerIterationClustering
  - AIMech:ZetaMerging
  - AIMech:CHAMELEONClustering
  - AIMech:MultiClassNPairLoss
  - AIMech:OneVsOneNPairLoss
  exclusions:
  - target: FullZell, generic N-pair batching family and remaining discovery frontier
    reason: FullZell has unresolved source conventions; other candidates need their
      own primary identity/method checks.
  - target: Other paper pages, uninspected code and benchmark outcomes
    reason: Only declared source passages/files were read; no model, clustering implementation
      or benchmark executed.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:PowerIterationClustering
  - AIMech:ZetaMerging
  - AIMech:CHAMELEONClustering
  - AIMech:MultiClassNPairLoss
  - AIMech:OneVsOneNPairLoss
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 56.45s\nChecked 442 record(s); 0 failed.\n\
    Checked 223 curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing,\
    \ 0 changed, 0 unexpected.\nChecked 48 history record(s); 0 error(s).\n{\n  \"\
    repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 45,\n  \"coverage\"\
    : \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:PowerIterationClustering
  - AIMech:ZetaMerging
  - AIMech:CHAMELEONClustering
  - AIMech:MultiClassNPairLoss
  - AIMech:OneVsOneNPairLoss
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: zeta-arithmetic
  name: Finite Zeta popularity counterexample
  command: python3 research/discovery/zeta-popularity-bound.py
  status: passed
  required: true
  target_ids:
  - AIMech:ZetaMerging
  exit_code: 0
  expected_exit_code: 0
  summary: '{"P": [[0, 1], [1, 0]], "z": "1/4", "det_I_minus_zP": "15/16", "inverse_diagonal":
    ["16/15", "16/15"], "epsilon": 0.06453852113757118, "chi_leave_one_out": 0.06453852113757118,
    "chi_resolvent": 0.06453852113757116, "printed_upper_bound_epsilon_over_n": 0.03226926056878559,
    "printed_upper_bound_satisfied": false, "algorithm_1_sufficient_z_bound_satisfied":
    true, "scope": "One counterexample to the printed inequality; no general replacement
    bound asserted."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T093440Z-graph-clustering-npair.json
  accessed_at: '2026-10-11T09:37:09Z'
  support: supports
  summary: No normalized identity match across442 AIO labels/scoped synonyms and218
    preceding native IDs/names/aliases. Both full checkouts were searched including
    ignored/hidden files;15 lines each were existing discovery/review context. Five
    native neighbors and five exact AIO nodes were semantically compared. PIC alias
    is qualified. The genericN-pair family label was removed as an exact alias of
    the multi-class member after source review.
  search_scope: All442 AIO labels/scoped synonyms and218 preceding native IDs/names/aliases,
    plus both complete ignored/hidden-inclusive checkouts.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-11T09:37:09Z'
  support: supports
  locator: 'Five exact CLASS nodes listed in source_analysis.aio_mapping_inspection:
    definitions, scoped synonyms and outgoing edges'
  summary: Three clustering algorithms have related task mappings; Zeta merging and
    CHAMELEON also relate to HierarchicalClustering. The N-pair losses have related-only
    ContrastiveLearning associations with the source’s supervised versus AIO’s self-supervised
    distinction explicit. No equivalence, subclass or upstream acceptance is asserted.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T093440Z-graph-clustering-npair.json
  accessed_at: '2026-10-11T09:37:09Z'
  support: supports
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  summary: InfoNCE, NTXentLoss, PathIntegralClustering, GraphDegreeLinkage and KMeans
    were compared. The new records distinguish named supervised objectives, power-iteration
    embedding, log-diagonal popularity and dynamic graph cuts from these existing
    mechanisms.
- evidence_id: corrections
  kind: record_content
  reference: research/discovery/20261011T093440Z-graph-clustering-npair.json
  accessed_at: '2026-10-11T09:37:09Z'
  support: supports
  locator: 'review_refinements: before/after hashes, actual edit times, issues51–53'
  summary: Issue51 repairs Zeta calculation traceability; issue52 removes the generic
    N-pair family alias and an unsupported footnote aggregation; issue53 fixes a nonexistent
    section locator. Final records and changed citations were reread and re-inspected.
    These are current-state assessments, not invented predecessors to structured findings.
- evidence_id: poweriterationclustering-source
  kind: primary_source
  reference: https://icml.cc/Conferences/2010/papers/387.pdf
  locator: Sections 2.1–2.4, PDF pp. 1–4; Algorithm 1 and experimental stopping threshold
    on p. 4
  accessed_at: '2026-10-11T09:21:27Z'
  snapshot_sha256: 92619e1e526d23d8177a94b44c82f38db6ab41d7f226b76377d9c994d6edb51b
  support: supports
  summary: 'Power Iteration Clustering. ICML 2010 proceedings paper, 8 PDF pages.
    Text pages read: [1]; actual image pages read: [2, 3, 4]. A clustering algorithm
    that uses an early-stopped power iteration of a normalized similarity matrix to
    embed observations and then applies k-means to their embedding coordinates.'
- evidence_id: zetamerging-source
  kind: primary_source
  reference: https://papers.neurips.cc/paper/3412-cyclizing-clusters-via-zeta-function-of-a-graph.pdf
  locator: Sections 2.2–3.2, PDF pp. 3–4, Equations (2)–(5), Theorem 2 and Algorithm
    1; Section 4.3, pp. 5–6, component boundary
  accessed_at: '2026-10-11T09:21:27Z'
  snapshot_sha256: a07c0e034a507cbd97472729b06e8c77a19cc3be2b9bc75f23579aa4441bbeb8
  support: supports
  summary: 'Cyclizing Clusters via Zeta Function of a Graph. Advances in Neural Information
    Processing Systems 21, NIPS 2008; 8-page proceedings PDF. Text pages read: [1];
    actual image pages read: [2, 3, 4, 5, 6]. An agglomerative graph-clustering algorithm
    that selects the pair with the largest sum of conditional increases in average
    log-diagonal resolvent popularity.'
- evidence_id: chameleonclustering-source
  kind: primary_source
  reference: https://www-users.cse.umn.edu/~kumar001/papers/chameleon.ps
  locator: Technical Report 99-007, Sections 4.1–4.4, printed pp. 5–11 (PDF pp. 6–12),
    Equations (1)–(4)
  accessed_at: '2026-10-11T09:23:57Z'
  snapshot_sha256: da03091e656bf4b49f56c2c06a052949f6e91f761d1e5252d39392a8c99c1b69
  support: supports
  summary: 'CHAMELEON: A Hierarchical Clustering Algorithm Using Dynamic Modeling.
    University of Minnesota Technical Report 99-007, 1999, to appear in IEEE Computer;
    22-page author PostScript, read via a local PDF conversion. Text pages read: [];
    actual image pages read: [1, 6, 7, 8, 9, 10, 11, 12]. A graph-clustering procedure
    that first partitions a sparse neighbor graph into small subclusters and then
    agglomerates them using interconnectivity and closeness normalized by their internal
    bisection statistics.'
- evidence_id: multiclassnpairloss-source
  kind: primary_source
  reference: https://papers.nips.cc/paper_files/paper/2016/file/6b180037abbebea991d8b1232f8a8ca9-Paper.pdf
  locator: Sections 3.1–3.2.2, PDF pp. 3–5; Equations (3) and (7), footnotes 1–2,
    embedding regularization discussion
  accessed_at: '2026-10-11T09:21:27Z'
  snapshot_sha256: 83bee5d1a7edf86136dce8944c7db44144c2830e4d1ca62a422e212376a87a46
  support: supports
  summary: 'Improved Deep Metric Learning with Multi-class N-pair Loss Objective.
    NIPS 2016 proceedings, 9-page main paper; the mislinked Supplemental.zip is not
    evidence for this method. Text pages read: [1]; actual image pages read: [2, 3,
    4, 5]. A supervised metric-learning objective that averages a joint positive-versus-multiple-negative
    log-softmax loss across a batch of positive pairs drawn from distinct classes.'
- evidence_id: onevsonenpairloss-source
  kind: primary_source
  reference: https://papers.nips.cc/paper_files/paper/2016/file/6b180037abbebea991d8b1232f8a8ca9-Paper.pdf
  locator: Section 3.2, PDF p. 4, Equations (7)–(8); Section 3.2.2, p. 5, regularization
    discussion
  accessed_at: '2026-10-11T09:21:27Z'
  snapshot_sha256: 83bee5d1a7edf86136dce8944c7db44144c2830e4d1ca62a422e212376a87a46
  support: supports
  summary: 'Improved Deep Metric Learning with Multi-class N-pair Loss Objective.
    NIPS 2016 proceedings, 9-page main paper; the mislinked Supplemental.zip is not
    evidence for this method. Text pages read: [1]; actual image pages read: [2, 3,
    4, 5]. A supervised metric-learning objective that sums separate positive-versus-negative
    softplus comparisons for each anchor in a batch of positive pairs from distinct
    classes.'
- evidence_id: author-code
  kind: primary_source
  reference: https://www.cs.cmu.edu/~frank/code/icml2010-code.zip
  locator: pic.m, x_clusterembed_icml2010.m and readme.txt; eight actually read files
    and their hashes recorded in discovery report
  accessed_at: '2026-10-11T09:23:34Z'
  snapshot_sha256: 95b4275d8ecf9c8544deb5034a4e2d4d58501b9a1c0e41851360db8401c42ca6
  support: supports
  summary: Original author-linked MATLAB archive. pic.m uses absolute component changes
    and an iteration cap; the driver passes baseconv/n with baseconv=.001 and5000
    maximum iterations. These files were read, not executed. Archive checksum pins
    bytes; no release tag or commit is invented.
- evidence_id: zeta-calculation
  kind: record_content
  reference: research/discovery/zeta-popularity-bound.py
  locator: 'calculate(): exact Fraction determinant/inverse entries and two independent
    evaluations of popularity'
  accessed_at: '2026-10-11T09:37:09Z'
  snapshot_sha256: ae305e805509e700e6ccca15b27c313df2edd30c938885bf7b7d0f6b29f47dfe
  support: supports
  summary: 'Original curator arithmetic executed successfully: det15/16, inverse diagonal16/15,
    chi≈0.06453852 and printed upper bound≈0.03226926. The example satisfies the algorithm’s
    stated norm bound and refutes the displayed inequality without asserting a general
    replacement theorem or author erratum.'
- evidence_id: conversion
  kind: record_content
  reference: research/discovery/20261011T093440Z-graph-clustering-npair.json
  locator: CHAMELEON entry conversion and extraction_manifest
  accessed_at: '2026-10-11T09:26:03Z'
  support: supports
  summary: Original author PostScript SHAda03091e656bf4b49f56c2c06a052949f6e91f761d1e5252d39392a8c99c1b69
    was converted with gs-noX11 9.07 and -dSAFER; derived22page PDF SHA05de0220cf8e08fb5d67ddff44aa42cd2ab2fe3bd3b07c6430bdfd07442ea5a2.
    Title/abstract and full methodsPDF6–12 were visually inspected. The final8page
    journal version is not substituted.
assessments:
- assessment_id: poweriterationclustering
  area: evidence
  topic: Identity, mechanism, evidence, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:PowerIterationClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - poweriterationclustering-source
  - corrections
  - author-code
  summary: 'This is the Lin and Cohen ICML 2010 algorithm. Its qualified PIC alias
    is distinct from path integral clustering: it truncates a matrix iteration to
    form coordinates instead of merging clusters by resolvent descriptors. It is not
    a generic eigensolver or a claim that converging to the dominant eigenvector finds
    clusters. No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 218 preceding native IDs/names/aliases. Word-delimited fixed-string
    searches of both full checkouts, including ignored and hidden files, returned
    15 lines each in existing discovery/review context. Five neighboring native records
    and five exact AIO nodes with scoped synonyms and outgoing edges were inspected.'
  details: 'For a symmetric nonnegative similarity matrix A with zero diagonal and
    positive row sums, form D_ii=sum_j A_ij and W=D^−1 A. Starting with a nonnegative
    nonzero vector v, iterate v_next=Wv/||Wv||_1. Use an intermediate vector before
    convergence to the constant dominant right eigenvector. Following Algorithm 1
    and the released pic.m, monitor d_next=abs(v_next−v) componentwise and stop when
    max_i abs(d_next_i−d_i) is sufficiently small, subject to an iteration cap. Apply
    k-means to the scalar coordinates v_i for the requested k clusters. Degree-proportional
    initialization is described, and multiple random initial vectors may supply several
    embedding coordinates. Section 2.4 prose instead writes signed differences; the
    absolute-change convention here is explicitly the pseudocode/implementation convention.
    The stopping convention follows the paper pseudocode and released code, which
    use componentwise absolute first changes. The surrounding prose uses signed first
    changes. The released driver also uses a tolerance 100 times the paper’s stated
    experimental tolerance. These source differences are preserved rather than silently
    reconciled. Limitations: The stopping test is a heuristic for a useful intermediate
    embedding, not a certificate of cluster recovery. A regular graph with degree-proportional
    initialization starts at a constant vector and can yield no separating coordinates.
    Positive row sums are required for the stated row-stochastic normalization. Disconnected
    graphs, negative eigenmodes and collisions in a one-dimensional embedding limit
    a blanket spectral or convergence interpretation. The paper reports experimental
    tolerance 1e−5/n. The released experiment driver sets baseconv=0.001 and uses
    baseconv/n, with maxit=5000. These are different settings, not an asserted benchmark
    reproduction or proof that either setting is wrong. Choice of similarity, initialization,
    stopping rule and k-means solution affects the partition. No code was executed,
    and no runtime, accuracy or global-optimum claim is made.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: Named procedure or mathematical objective, not a trained model or
      benchmark result.
    evidence_ids:
    - poweriterationclustering-source
  - name: aio-relations
    value: 'related_match: AIO:UnsupervisedClustering'
    definition: Power iteration clustering supplies a procedure for grouping unlabeled
      observations. The AIO target denotes a clustering task; this algorithm-to-task
      association does not assert equivalence or subclass membership.
    evidence_ids:
    - mapping
- assessment_id: zetamerging
  area: evidence
  topic: Identity, mechanism, evidence, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:ZetaMerging
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - zetamerging-source
  - corrections
  - zeta-calculation
  summary: Zeta merging is the named Algorithm 1 component of Zhao and Tang’s Zell
    method. Its input is an already constructed weighted graph and initial partition;
    it does not prescribe the l-links initialization. It differs from path integral
    clustering, which averages all endpoint-to-endpoint resolvent entries rather than
    logarithms of diagonal entries. No normalized identity match was found across
    all 442 pinned AIO labels/scoped synonyms and 218 preceding native IDs/names/aliases.
    Word-delimited fixed-string searches of both full checkouts, including ignored
    and hidden files, returned 15 lines each in existing discovery/review context.
    Five neighboring native records and five exact AIO nodes with scoped synonyms
    and outgoing edges were inspected.
  details: 'Given a fixed nonnegative weighted adjacency P, a nonempty initial partition
    and target count m_c smaller than its initial count, choose damping 0<z<1/(2||P||_1),
    the sufficient range stated in Section 3.1 for nonzero P. For a cluster C use
    the principal submatrix P_C without local renormalization and R_C=(I−zP_C)^−1.
    Its popularity is chi_C=(1/|C|) sum_(i in C) log (R_C)_ii. Equivalently it is
    the average leave-one-vertex-out reduction of epsilon_C=−log det(I−zP_C). For
    U=A union B, chi_(A|U) averages log (R_U)_ii over i in A with divisor |A|. Merge
    the current pair maximizing (chi_(A|U)−chi_A)+(chi_(B|U)−chi_B); recompute affected
    affinities and repeat to m_c. The conditional increment is not chi_U−chi_A−chi_B.
    Curator calculation: for P=[[0,1],[1,0]], z=1/4 and C both vertices, det(I−zP)=15/16
    and both diagonal entries of (I−zP)^−1 are 16/15. Thus epsilon_C=chi_C=log(16/15)>epsilon_C/2.
    The z choice satisfies Section 3.1’s sufficient norm bound. The printed upper
    bound after Theorem 2 is not adopted. The reproducible finite calculation is saved
    as research/discovery/zeta-popularity-bound.py; it is not a benchmark of the clustering
    procedure. Limitations: Initialization, graph weights, damping and requested count
    determine the result; greedy merges cannot undo an initial grouping or certify
    a global partition optimum. The paper prints z<rho(W) in Theorem 1, whereas the
    cycle power series requires |z|rho(W)<1. This record uses the stricter positive
    norm bound actually stated for Algorithm 1, rather than importing the printed
    general condition. The printed bound 0<chi_C<=epsilon_C/|C| is not used. A two-vertex
    mutual-edge graph with z=1/4 gives chi_C=epsilon_C=log(16/15)>epsilon_C/2 under
    the paper’s own definitions; this is a curator counterexample, not an author erratum.
    Zell’s full l-links and bandwidth conventions require separate clarification and
    are not specified by this component. No generic sparse-inverse runtime guarantee,
    automatic correct cluster count, or benchmark reproduction is asserted.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: Named procedure or mathematical objective, not a trained model or
      benchmark result.
    evidence_ids:
    - zetamerging-source
  - name: aio-relations
    value: 'related_match: AIO:UnsupervisedClustering; related_match: AIO:HierarchicalClustering'
    definition: Zeta merging supplies a procedure for grouping unlabeled observations.
      The AIO target denotes a clustering task; this algorithm-to-task association
      does not assert equivalence or subclass membership. Zeta merging builds a hierarchy
      through agglomeration. The target describes hierarchy construction without prescribing
      this merge criterion or initialization.
    evidence_ids:
    - mapping
- assessment_id: chameleonclustering
  area: evidence
  topic: Identity, mechanism, evidence, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:CHAMELEONClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - chameleonclustering-source
  - corrections
  - conversion
  summary: This record covers the two-phase CHAMELEON procedure in Technical Report
    99-007, including the two merge-selection alternatives described there. Dynamic
    modeling means recomputing cluster-relative graph statistics, not learning a neural
    representation. The inspected source is the 22-page report, not the eight-page
    final Computer article. No normalized identity match was found across all 442
    pinned AIO labels/scoped synonyms and 218 preceding native IDs/names/aliases.
    Word-delimited fixed-string searches of both full checkouts, including ignored
    and hidden files, returned 15 lines each in existing discovery/review context.
    Five neighboring native records and five exact AIO nodes with scoped synonyms
    and outgoing edges were inspected.
  details: 'Construct a weighted undirected k-nearest-neighbor graph by retaining
    an edge when either endpoint lists the other among its k most similar points.
    Obtain small initial subclusters by repeated balanced graph bisection, selecting
    the largest current subcluster; the report uses hMETIS with each child holding
    at least 25 percent of its parent and stops when the largest subcluster is below
    MINSIZE. For clusters A,B, relative interconnectivity RI is the total cross-edge
    weight divided by the mean of the two internal bisection-cut weights. Relative
    closeness RC is the mean cross-edge weight divided by the size-weighted mean of
    the two mean internal bisection-edge weights. One merge scheme maximizes RI(A,B)*RC(A,B)^alpha
    over pairs; this is the scheme used for the report’s dendrogram experiments. An
    alternative visits clusters and selects their most strongly connected eligible
    neighbor subject to separate RI and RC thresholds, permitting multiple merges
    per iteration and either stopping or relaxing thresholds when no pair qualifies.
    Limitations: Meaningful nonzero internal cut statistics and nonempty cross-edge
    sets are needed to evaluate the ratios. Very small or disconnected subclusters
    can make the estimates unstable or undefined; a zero-denominator policy is not
    supplied by this record. Neighbor size, similarity, initial granularity, bisection
    balance and merge parameters influence results. The initial partition and later
    merges may cross desired cluster boundaries; the procedure does not establish
    semantic recovery. The product-score and threshold-based schemes have different
    selection and stopping behavior; they are documented alternatives within the original
    named procedure, not assumed identical algorithms. Internal cuts are computed
    by graph-partitioning software; describing the min-cut objective does not certify
    a global exact cut solver. Runtime depends in part on neighbor search and data
    dimension. No implementation or reported benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: Named procedure or mathematical objective, not a trained model or
      benchmark result.
    evidence_ids:
    - chameleonclustering-source
  - name: aio-relations
    value: 'related_match: AIO:UnsupervisedClustering; related_match: AIO:HierarchicalClustering'
    definition: CHAMELEON supplies a procedure for grouping unlabeled observations.
      The AIO target denotes a clustering task; this algorithm-to-task association
      does not assert equivalence or subclass membership. CHAMELEON builds a hierarchy
      through agglomeration. The target describes hierarchy construction without prescribing
      this merge criterion or initialization.
    evidence_ids:
    - mapping
- assessment_id: multiclassnpairloss
  area: evidence
  topic: Identity, mechanism, evidence, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:MultiClassNPairLoss
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - multiclassnpairloss-source
  - corrections
  summary: This is Sohn’s N-pair-mc objective, Equation (7), together with its distinct-class
    positive-pair batching. The source also uses unqualified N-pair loss for a family
    including N-pair-ovo, so that family name is not an exact alias of this member.
    Its per-anchor categorical form is shared with generic InfoNCE at dot-product
    scores, but the named supervised batching configuration is retained explicitly.
    It is not the full SimCLR procedure or NT-Xent’s cosine-temperature two-view construction.
    N-pair-ovo instead sums individual pairwise softplus terms. No normalized identity
    match was found across all 442 pinned AIO labels/scoped synonyms and 218 preceding
    native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts,
    including ignored and hidden files, returned 15 lines each in existing discovery/review
    context. Five neighboring native records and five exact AIO nodes with scoped
    synonyms and outgoing edges were inspected.
  details: 'Take N>=2 classes and two examples (x_i,x_i+) from each class. Encode
    2N examples to f_i and f_i+. The Equation (7) objective is L_mc=(1/N) sum_i log[1+sum_(j!=i)
    exp(f_i^T f_j+−f_i^T f_i+)]. Each anchor has its paired positive and N−1 negative
    candidates from the positive side of other classes. Sharing these candidates across
    anchors forms N tuplets using 2N forward embeddings. Equation (7) specifies one
    orientation; footnote 2 also mentions a symmetric loss that swaps the anchor/positive
    roles, without specifying its aggregation in that footnote. No explicit temperature
    or cosine normalization appears in this expression. Limitations: Use N positive
    pairs from N distinct classes; other positive-side examples must represent different
    classes for the stated objective. Pair sampling and class selection are part of
    this configuration, not interchangeable with arbitrary augmented-view negatives.
    The main paper uses embedding-norm regularization instead of a hard unit-length
    constraint. This record specifies the loss term; it does not prescribe a regularization
    coefficient, encoder, optimizer or full training schedule. No unconditional equivalence
    to a margin triplet hinge or an information lower bound is asserted. Objective
    shape and label-based batching do not establish downstream accuracy. No training
    or benchmark was reproduced. The proceedings Supplemental.zip inspected during
    retrieval contains a different paper by Steinhardt and Liang. It is not supporting
    evidence; this record relies on the inspected nine-page N-pair main paper.'
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: Named procedure or mathematical objective, not a trained model or
      benchmark result.
    evidence_ids:
    - multiclassnpairloss-source
  - name: aio-relations
    value: 'related_match: AIO:ContrastiveLearning'
    definition: The objective contrasts same-class positives with different-class
      negatives. The inspected AIO target explicitly describes a self-supervised deep-network
      approach, whereas this objective is supervised and mathematical. Their shared
      positive-versus-negative representation-learning mechanism supports a related
      association only, not an equivalence or subclass assertion.
    evidence_ids:
    - mapping
- assessment_id: onevsonenpairloss
  area: evidence
  topic: Identity, mechanism, evidence, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:OneVsOneNPairLoss
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - onevsonenpairloss-source
  - corrections
  summary: This is the named N-pair-ovo objective in Sohn’s Equation (8). It shares
    the N-pair batch construction with N-pair-mc but uses a sum of binary softplus
    comparisons, not one joint log-sum-exp over negatives. They coincide for one negative
    per anchor (N=2), but generally differ for N>2. No normalized identity match was
    found across all 442 pinned AIO labels/scoped synonyms and 218 preceding native
    IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts,
    including ignored and hidden files, returned 15 lines each in existing discovery/review
    context. Five neighboring native records and five exact AIO nodes with scoped
    synonyms and outgoing edges were inspected.
  details: 'Given N>=2 positive pairs (x_i,x_i+) from N distinct classes and embeddings
    f_i,f_i+, define L_ovo=(1/N) sum_i sum_(j!=i) log[1+exp(f_i^T f_j+−f_i^T f_i+)].
    Other positive-side examples supply N−1 different-class negatives to each anchor.
    The printed divisor is N, not N(N−1), so it averages across anchors while summing
    each anchor’s pairwise comparisons. In contrast, N-pair-mc places the sum over
    negatives inside a single logarithm. The expression uses dot products without
    an explicit temperature or cosine normalization. Limitations: Use N positive pairs
    from N distinct classes; other positive-side examples must represent different
    classes for the stated objective. Pair sampling and class selection are part of
    this configuration, not interchangeable with arbitrary augmented-view negatives.
    The main paper uses embedding-norm regularization instead of a hard unit-length
    constraint. This record specifies the loss term; it does not prescribe a regularization
    coefficient, encoder, optimizer or full training schedule. No unconditional equivalence
    to a margin triplet hinge or an information lower bound is asserted. Objective
    shape and label-based batching do not establish downstream accuracy. No training
    or benchmark was reproduced. The proceedings Supplemental.zip inspected during
    retrieval contains a different paper by Steinhardt and Liang. It is not supporting
    evidence; this record relies on the inspected nine-page N-pair main paper.'
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: Named procedure or mathematical objective, not a trained model or
      benchmark result.
    evidence_ids:
    - onevsonenpairloss-source
  - name: aio-relations
    value: 'related_match: AIO:ContrastiveLearning'
    definition: The objective contrasts same-class positives with different-class
      negatives. The inspected AIO target explicitly describes a self-supervised deep-network
      approach, whereas this objective is supervised and mathematical. Their shared
      positive-versus-negative representation-learning mechanism supports a related
      association only, not an equivalence or subclass assertion.
    evidence_ids:
    - mapping
- assessment_id: power-stopping
  area: consistency
  topic: Power iteration initialization, stopping and source conventions
  outcome: supported
  target_ids:
  - AIMech:PowerIterationClustering
  evidence_ids:
  - poweriterationclustering-source
  - author-code
  - corrections
  summary: Retain the pseudocode/implementation absolute-change convention with paper/code
    discrepancies explicit.
  details: The iteration is on W=D^−1A with symmetric nonnegative A, not a path-integral
    agglomeration. Stopping is heuristic; degree initialization on regular graphs
    can be constant, and one-dimensional coordinates can collide. The prose signed-change
    expression and100fold experimental-tolerance difference are recorded without an
    invented reconciliation. The final locator correctly names Sections2.1–2.4.
- assessment_id: zeta-descriptor
  area: consistency
  topic: Conditional log-diagonal popularity and challenged printed bound
  outcome: supported
  target_ids:
  - AIMech:ZetaMerging
  evidence_ids:
  - zetamerging-source
  - zeta-calculation
  - neighbors
  - corrections
  summary: Retain Algorithm1 as a component independent of unresolved fullZell initialization
    details.
  details: Principal submatrices preserve global weights. The score averages log diagonal
    resolvent entries, with conditional union popularity normalized by each original
    cluster. This differs from all-entry path sums and from chi_union−chi_A−chi_B.
    The source’s positive norm bound ensures an admissible convergent regime. The
    printed spectral-radius condition and popularity inequality are not copied as
    guarantees; the finite counterexample is explicitly curator analysis.
- assessment_id: chameleon-mechanism
  area: consistency
  topic: CHAMELEON relative measures and two merge schemes
  outcome: supported
  target_ids:
  - AIMech:CHAMELEONClustering
  evidence_ids:
  - chameleonclustering-source
  - conversion
  summary: Retain the original two-phase procedure with distinct cut-sum and cut-mean
    normalizations.
  details: Graph edges use the union of directed nearest-neighbor membership. RI divides
    cross-weight sum by the average internal cut sum; RC divides average cross weight
    by a size-weighted mean of internal cut means. The initial largest-subcluster
    bisection and25percent balance are source-specific. Product RI*RC^alpha and threshold
    eligibility with maximum absolute cross-weight selection are separate documented
    alternatives; exact min-cut optimality and denominator handling are not invented.
- assessment_id: npair-objectives
  area: scope
  topic: Multi-class versus one-vs-one N-pair objective boundaries
  outcome: supported
  target_ids:
  - AIMech:MultiClassNPairLoss
  - AIMech:OneVsOneNPairLoss
  evidence_ids:
  - multiclassnpairloss-source
  - onevsonenpairloss-source
  - neighbors
  - corrections
  summary: Retain two named loss members; do not make the whole N-pair family an alias
    of the multi-class member.
  details: Both use N positive pairs from distinct classes and2N embeddings. Equation7
    has one logarithm over the negative exponential sum; Equation8 sums separate softplus
    terms and divides byN only. They coincide forN2 but generally differ beyond one
    negative. Generic InfoNCE categorical form is acknowledged; no unconditional information
    bound, margin-hinge equivalence or NT-Xent identity asserted. Footnote2 mentions
    swapped roles but does not specify the averaging originally claimed. The unrelated
    supplemental archive is excluded.
- assessment_id: mapping-scope
  area: grounding
  topic: Task, objective and supervision scope
  outcome: supported
  target_ids:
  - AIMech:PowerIterationClustering
  - AIMech:ZetaMerging
  - AIMech:CHAMELEONClustering
  - AIMech:MultiClassNPairLoss
  - AIMech:OneVsOneNPairLoss
  evidence_ids:
  - mapping
  - identity
  - neighbors
  summary: Mappings remain related associations with abstraction and supervision differences
    explicit.
  details: Three clustering algorithms have related task mappings; Zeta merging and
    CHAMELEON also relate to HierarchicalClustering. The N-pair losses have related-only
    ContrastiveLearning associations with the source’s supervised versus AIO’s self-supervised
    distinction explicit. No equivalence, subclass or upstream acceptance is asserted.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:PowerIterationClustering
  - AIMech:ZetaMerging
  - AIMech:CHAMELEONClustering
  - AIMech:MultiClassNPairLoss
  - AIMech:OneVsOneNPairLoss
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - corrections
  - poweriterationclustering-source
  - zetamerging-source
  - chameleonclustering-source
  - multiclassnpairloss-source
  - onevsonenpairloss-source
  - author-code
  - zeta-calculation
  - conversion
  rationale: Power-iteration coordinates, Zeta conditional log-diagonal linkage, CHAMELEON
    dynamic graph-cut procedure and two differently aggregated supervised N-pair losses
    have supported distinct scopes. Zeta merging is retained as a component without
    asserting fullZell conventions. Generic N-pair family identity is not assigned
    to the multi-class member. The multi-class loss shares categorical form with InfoNCE
    but specifies supervised batching. No AIO mutation or status promotion follows.
limitations:
- Adversarial author self-review only; all five records remain DRAFT.
- Only declared source pages/code were inspected. CHAMELEON evidence is the22page
  technical report converted from author PostScript; the N-pair supplemental archive
  is unrelated and excluded.
- Source contradictions are qualified, not silently corrected as author-issued errata.
  The Zeta counterexample is original finite arithmetic, not a benchmark or general
  replacement theorem.
- Initial curated validation failed for a context-only asserted Zeta claim; the citation
  was repaired. An incorrect N-pair alias/aggregation and power-method locator were
  corrected and re-inspected before this final assessment.
- The first vendored check could not resolve its network hostname inside the sandbox;
  the authorized network retry passed. Final required checks are recorded, and no
  auto-review denial occurred.
- Prior immutable reviews are unchanged. Issue fixes are traced in the discovery ledger;
  no earlier structured finding is fabricated.
- Five positive additions and the retained frontier leave discovery active.
tags:
- native-concepts
- graph-clustering
- metric-learning
- self-review
- discovery-ongoing
```
