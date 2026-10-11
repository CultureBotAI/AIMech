# Scientific self-review of graph linkage and NT-Xent, with JULE rationale correction

- Review: 20261011T092103Z-graph-linkage-contrastive-loss
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T09:19:10Z
- Finished UTC: 2026-10-11T09:21:03Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain four source-backed DRAFT concepts, including the exact/approximate GDL distinction and NT-Xent specialization. Issues48 and49 have supported current-state corrections. JULE coverage is limited to its corrected mapping rationale. No actionable finding remains in this declared scope.

## Scope And Provenance

All fields of four new concepts plus the changed UnsupervisedClustering mapping rationale and curation provenance of JULE.

Selection: Exact four added IDs and one corrected maintained owner from the discovery report; no sampling.
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base df875592b387d423caa6f064b88a5a72e10e5271.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GraphDegreeLinkage | data/curated/GraphDegreeLinkage.yaml | maintained | Graph degree linkage |
| AIMech:AcceleratedGraphDegreeLinkage | data/curated/AcceleratedGraphDegreeLinkage.yaml | maintained | Accelerated graph degree linkage |
| AIMech:PathIntegralClustering | data/curated/PathIntegralClustering.yaml | maintained | Path integral clustering |
| AIMech:NTXentLoss | data/curated/NTXentLoss.yaml | maintained | Normalized temperature-scaled cross entropy loss |
| AIMech:JointUnsupervisedLearning | data/curated/JointUnsupervisedLearning.yaml | maintained | Joint unsupervised learning of deep representations and image clusters |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:GraphDegreeLinkage, AIMech:AcceleratedGraphDegreeLinkage, AIMech:PathIntegralClustering, AIMech:NTXentLoss, AIMech:JointUnsupervisedLearning | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 50.82s<br>Checked 442 record(s); 0 failed.<br>Checked 218 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 46 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 44,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:GraphDegreeLinkage, AIMech:AcceleratedGraphDegreeLinkage, AIMech:PathIntegralClustering, AIMech:NTXentLoss, AIMech:JointUnsupervisedLearning | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Identity, mechanism, limitations and mapping

evidence: supported. Targets: AIMech:GraphDegreeLinkage.

GDL is the graph-degree clustering procedure of Zhang et al. Its affinity uses a product of directed degree averages, not average pairwise distance or a symmetrized graph. GDL-U is the paper’s exact update implementation of this same merge criterion; AGDL restricts candidate search and is represented separately. JULE incorporates graph-degree affinity while also learning representations and changing merge selection, so it is not the same algorithm. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 214 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 31 lines each: existing SimCLR/InfoNCE component discussion, shared primary-source references and discovery/review context. Five native neighbors and seven exact AIO nodes with scoped synonyms and outgoing relations were inspected.

Construct a directed K-nearest-neighbor graph with w_ij=exp(−dist(i,j)^2/sigma^2) for retained edges and zero otherwise. Keep W fixed during clustering. Initialize clusters as weakly connected components of a smaller K0-nearest-neighbor graph. For vertex i and cluster C, define d_in(i,C)=sum_(j in C) w_ji/&#124;C&#124; and d_out(i,C)=sum_(j in C) w_ij/&#124;C&#124;. The directed affinity A(B→C)=sum_(i in B) d_in(i,C)d_out(i,C); the symmetric merge affinity is A(B,C)=A(B→C)+A(C→B). Repeatedly choose a pair with maximum affinity over all current pairs, merge it, and stop at the requested cluster count. The exact update implementation uses A((A union B)→C)=A(A→C)+A(B→C), while the opposite direction must be computed from the original degree expression; both directions are not generally additive. Limitations: The distance, K, K0, bandwidth and requested cluster count determine the construction. Weak-component initialization can already join observations irreversibly; the merge-only procedure cannot recover a requested count larger than the initial number of components. Degree products encode two-way connectivity but do not prove recovery of true semantic clusters or universal robustness to noise. The graph is directed even though the final pair affinity is symmetric. GDL-U preserves the exact criterion when updates and tie handling agree. The paper’s AGDL approximation can choose different merges and is not an exact synonym. The published complexity analysis distinguishes naive GDL from its update and approximate implementations, and assumes fixed neighborhood parameters and sparsity. This record asserts no universal runtime or benchmark advantage. No implementation or benchmark was executed.

### Identity, mechanism, limitations and mapping

evidence: supported. Targets: AIMech:AcceleratedGraphDegreeLinkage.

AGDL is Zhang et al.’s named candidate-restricted approximation to GDL, not merely the exact additive-update implementation GDL-U. It retains the GDL affinity but can omit the globally best pair after approximate neighbor-set updates. It is distinct from JULE’s representation-learning procedure. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 214 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 31 lines each: existing SimCLR/InfoNCE component discussion, shared primary-source references and discovery/review context. Five native neighbors and seven exact AIO nodes with scoped synonyms and outgoing relations were inspected.

Use the same fixed directed neighbor graph, weak-component initialization and symmetric product-of-degree affinity as GDL. Initialize a Kc-nearest cluster set for each cluster. Search only pairs for which at least one cluster belongs to the other’s maintained neighbor set, and merge the highest-affinity eligible pair A,B. For any existing cluster whose set contains A or B, add A union B and compute the new pair affinity. Build the merged cluster’s set by choosing Kc nearest clusters from the union of the two old neighbor sets. Remove A and B from remaining neighbor sets and delete their sets. Repeat until the target cluster count. These local updates rely on heuristic persistence of cluster-neighbor relationships, rather than recomputing every nearest-cluster set exactly. Limitations: The method approximates global merge selection, not the defining degree-product formula. It has no asserted guarantee of reproducing exact GDL merges or recovering a globally optimal partition. Kc and the initial neighbor sets affect which pairs remain eligible. The source’s local-update assumptions can fail; an omitted pair need not re-enter through an exhaustive search. The supplement’s quadratic complexity argument assumes small initial clusters, fixed K/K0/Kc and a bound on how many other clusters include a merged cluster in their neighbor sets. A universal worst-case quadratic guarantee is not inferred from that argument. Graph construction, initialization, irreversibility and prescribed cluster count have the same scope limitations as GDL. No implementation, speedup measurement or clustering benchmark was reproduced.

### Identity, mechanism, limitations and mapping

evidence: supported. Targets: AIMech:PathIntegralClustering.

This is Zhang, Zhao and Wang’s 2013 maximum-incremental-path-integral clustering procedure. The qualified PIC alias denotes path integral clustering, not unrelated power-iteration clustering or generic physical path integration. Its affinity uses conditional path descriptors, not simply the merged cluster’s descriptor minus the two original descriptors. GDL instead uses products of degree averages; JULE is a joint neural-learning procedure. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 214 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 31 lines each: existing SimCLR/InfoNCE component discussion, shared primary-source references and discovery/review context. Five native neighbors and seven exact AIO nodes with scoped synonyms and outgoing relations were inspected.

Build a weighted directed nearest-neighbor graph and row-normalize its adjacency W to obtain transition matrix P=D^−1 W. Keep that global P fixed. Initialize small clusters by linking each sample to its nearest neighbor and repeatedly merging overlapping groups. For nonempty C and 0&lt;z&lt;1, let P_C be the principal submatrix of P, without renormalizing its rows inside C, and define S_C=1_C^T(I−z P_C)^−1 1_C/&#124;C&#124;^2. This sums geometrically discounted within-C transition paths, including the length-zero identity contribution. For U=A union B, define S_(A&#124;U)=e_A^T(I−z P_U)^−1 e_A/&#124;A&#124;^2, where e_A is the indicator of A among the vertices of U; its paths stay in U and start and end in A. Merge the pair maximizing (S_(A&#124;U)−S_A)+(S_(B&#124;U)−S_B), then repeat to the requested count. Linear systems can evaluate the descriptors without explicitly forming a dense inverse. Limitations: The distance/similarity, neighborhood size, bandwidth, discount z and target count are inputs or choices. Row normalization needs positive row sums; 0&lt;z&lt;1 and a substochastic principal submatrix make the geometric series converge. Initial nearest-neighbor components and later greedy merges are irreversible. The algorithm cannot split an initial component to reach a larger requested cluster count. No semantic recovery or global partition optimum is certified. Conditional path descriptors retain each original cluster’s &#124;C&#124;^2 normalization and endpoint indicator. Replacing the affinity by S_(A union B)−S_A−S_B changes the method. Principal submatrices are not independently renormalized transition matrices. The paper’s efficient-computation discussion relies on sparse graphs, iterative solves and chosen conditioning/discount. An exact resolvent formula is not a claim of exact finite-iteration numerical solves or an unconditional linear bound for the whole clustering algorithm. No runtime or benchmark reproduction was performed.

### Identity, mechanism, limitations and mapping

evidence: supported. Targets: AIMech:NTXentLoss.

NT-Xent is the named normalized temperature-scaled configuration of the contrastive categorical objective in the SimCLR paper. It specializes the generic InfoNCE score and candidate construction rather than defining a mathematically unrelated loss family. The loss is not the full SimCLR augmentation/encoder/projection/training procedure, and its symmetric two-view minibatch aggregation is stated explicitly. The paper credits prior uses; no claim of first invention by SimCLR is made. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 214 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 31 lines each: existing SimCLR/InfoNCE component discussion, shared primary-source references and discovery/review context. Five native neighbors and seven exact AIO nodes with scoped synonyms and outgoing relations were inspected.

For nonzero representations z_i,z_k and temperature tau&gt;0, use s_ik=z_i^T z_k/(&#124;&#124;z_i&#124;&#124; &#124;&#124;z_k&#124;&#124;). In the SimCLR two-view configuration, N&gt;=2 source examples produce 2N views; j is the other view of the same source as anchor i. Define ell(i,j)=−log[exp(s_ij/tau)/sum_(k=1..2N,k≠i) exp(s_ik/tau)]. The denominator contains 2N−1 terms: the paired positive and 2N−2 other-source views; only the anchor itself is excluded. Average ell over both directions of every positive pair, giving 2N anchor losses. Temperature changes the softmax weighting of candidate similarities. The paper applies this objective to projected representations, but the mathematical loss does not itself prescribe an encoder, augmentation family or optimizer. Curator qualification from comparing the two sampling constructions: SimCLR uses both augmented views of every other source as negative candidates, whereas Poole et al.’s Equation (10) states its InfoNCE expectation over independent joint pairs. The latter proof is not automatically a proof for the full SimCLR candidate construction. This comparison does not assert that no alternative dependent-candidate bound can hold. Limitations: Cosine similarity requires nonzero representations and the specified temperature is positive. The positive is included in the normalization; dropping it or retaining the self-comparison yields a different expression. The two views of each other source are dependent candidates. The standard independent-negative InfoNCE mutual-information argument is not automatically established for this minibatch construction; this record asserts a loss, not an unconditional information certificate. Other-source views are treated as negatives without guaranteeing semantic dissimilarity. Learned usefulness depends on positive construction, candidate sampling and representation choices; minimizing the objective alone does not certify downstream quality. The named configuration shares the categorical form of InfoNCE. Its record preserves the explicit normalization, temperature and batching convention rather than claiming a new unrestricted variational bound. No model training or benchmark was reproduced.

### JULE corrected task-mapping rationale only

grounding: supported. Targets: AIMech:JointUnsupervisedLearning.

The corrected UnsupervisedClustering rationale now describes JULE’s unlabeled-image clustering and representation learning.

The relation and target remain unchanged. Removing the IMSAT-only qualifier repairs local scope/provenance wording without changing JULE’s algorithm or upstream AIO. This is a current-state assessment of the corrected rationale, not a new whole-record review or a fabricated successor to a prior structured finding.

### GDL, GDL-U and AGDL boundaries

consistency: supported. Targets: AIMech:GraphDegreeLinkage, AIMech:AcceleratedGraphDegreeLinkage.

Retain exact GDL separately from AGDL’s approximate candidate search; treat GDL-U as an exact implementation of GDL.

Average in/out degrees divide by the target cluster’s size before their product, while the source-cluster vertices are summed. The graph is directed, but pair affinity is symmetric. The one-way additive update is not applied to both directions. AGDL searches the union of directed neighbor eligibility and updates sets locally; global-pair equivalence and universal quadratic runtime are not asserted.

### Conditional path-integral affinity and numerical assumptions

consistency: supported. Targets: AIMech:PathIntegralClustering.

Retain the conditional-increment construction with global transition normalization and original cluster denominators.

P_C is a principal submatrix of the fixed global row-normalized P. The resolvent includes the identity and geometrically discounted paths for0&lt;z&lt;1. Union paths retain original-cluster endpoint indicators and &#124;C&#124;² factors. The stated affinity is not S_union−S_A−S_B. Sparse numerical solves and empirical robustness are not promoted to universal exact-runtime or recovery guarantees.

### NT-Xent specialization, SimCLR composition and information assumptions

scope: supported. Targets: AIMech:NTXentLoss.

Retain the named cosine/temperature objective with its relationship to InfoNCE explicit.

The denominator contains the positive and excludes self; two-view SimCLR has2N−1 candidates and2N directed anchor losses. Loss identity does not impose the complete encoder/augmentation/optimizer procedure. The independent-joint-pair proof is cited as context for a curator sampling qualification. No universal impossibility claim about correlated negatives is made. Issue49 makes this comparison directly traceable.

### Task and learning-approach relations

grounding: supported. Targets: AIMech:GraphDegreeLinkage, AIMech:AcceleratedGraphDegreeLinkage, AIMech:PathIntegralClustering, AIMech:NTXentLoss, AIMech:JointUnsupervisedLearning.

Keep algorithm-to-task and objective-to-approach associations as related matches.

Seven exact pinned AIO nodes were inspected. Three graph algorithms have related matches to UnsupervisedClustering and HierarchicalClustering; these are algorithm-to-task associations, not broad/subclass assertions. NT-Xent has a related match to ContrastiveLearning, whose AIO node is modeled as a network approach. The corrected JULE rationale refers to its own image-clustering procedure and preserves its existing task relation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:GraphDegreeLinkage, AIMech:AcceleratedGraphDegreeLinkage, AIMech:PathIntegralClustering, AIMech:NTXentLoss, AIMech:JointUnsupervisedLearning. Exact degree-product linkage, its candidate-search approximation, conditional discounted-path clustering and a named normalized contrastive objective have distinct declared scopes. GDL-U stays an implementation of exact GDL. NT-Xent is explicitly a specialization of generic InfoNCE rather than an unrelated loss family. JULE remains a separate jointly learned representation/clustering algorithm; only its corrected task rationale is assessed here. No AIO mutation or status promotion follows.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T091717Z-graph-linkage-contrastive-loss.json | supports | No normalized match among all442 AIO labels/scoped synonyms and214 preceding native IDs/names/aliases. Both full checkouts were searched including ignored/hidden files;31 lines each were existing SimCLR/InfoNCE component descriptions, source citations and discovery/review references. Five neighboring maintained mechanisms were compared. PIC is deliberately qualified because power iteration clustering is a different primary-paper identity. The initial NT-Xent redundant punctuation-only alias failed local validation and was removed before final validation. |
| mapping | sources/aio/aio.json; Seven exact CLASS nodes with definitions, scoped synonyms and outgoing relations listed in source_analysis.aio_mapping_inspection | supports | Seven exact pinned AIO nodes were inspected. Three graph algorithms have related matches to UnsupervisedClustering and HierarchicalClustering; these are algorithm-to-task associations, not broad/subclass assertions. NT-Xent has a related match to ContrastiveLearning, whose AIO node is modeled as a network approach. The corrected JULE rationale refers to its own image-clustering procedure and preserves its existing task relation. |
| neighbors | research/discovery/20261011T091717Z-graph-linkage-contrastive-loss.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | SimCLR, InfoNCE, JULE, DBSCAN and KMeans definitions and mechanisms were compared. Full neural training, generic contrastive loss, jointly learned linkage, density connectivity and centroid assignment are not equivalent to all four selected concepts. |
| graphdegreelinkage-source | https://arxiv.org/pdf/1208.5092v1; Sections 3.1–3.4, PDF pp. 5–8, Definitions 1–2, Equations (1)–(9), Algorithm 1; supplement Section 6, p. 15, Algorithm 2 | supports | Graph Degree Linkage: Agglomerative Clustering on a Directed Graph. arXiv:1208.5092v1, 2012-08-25; ECCV 2012 manuscript with supplement, 17 PDF pages. Local text pages read: [1]; actual image pages read: [3, 4, 5, 6, 7, 8, 15, 16]. An agglomerative clustering algorithm that merges the pair with greatest symmetric graph-degree affinity, formed by summing products of cluster-normalized incoming and outgoing edge weights on a fixed directed nearest-neighbor graph. |
| acceleratedgraphdegreelinkage-source | https://arxiv.org/pdf/1208.5092v1; Section 3.4, PDF p. 8, Accelerated GDL; supplement Section 6, p. 15, Algorithm 3; Section 7, p. 16, AGDL complexity assumptions | supports | Graph Degree Linkage: Agglomerative Clustering on a Directed Graph. arXiv:1208.5092v1, 2012-08-25; ECCV 2012 manuscript with supplement, 17 PDF pages. Local text pages read: [1]; actual image pages read: [3, 4, 5, 6, 7, 8, 15, 16]. An approximate graph degree linkage algorithm that selects merges from maintained cluster-neighbor sets and updates those sets locally instead of searching every current cluster pair. |
| pathintegralclustering-source | https://waynezhanghk.github.io/papers/pr2013_path_clustering.pdf; Section 2, PDF pp. 2–3 (printed 3057–3058), Equations (1)–(3), Algorithm 1; Sections 3.1–3.4, pp. 3–4, Equations (4)–(12); Section 4, p. 5, Equation (14) | supports | Agglomerative clustering via maximum incremental path integral. Pattern Recognition 46(11):3056–3065, 2013; author-hosted published article, 10 PDF pages. Local text pages read: [1]; actual image pages read: [2, 3, 4, 5]. An agglomerative clustering algorithm that merges clusters with the greatest increase in their size-normalized sums of discounted random-walk paths when paths are allowed through the proposed union. |
| ntxentloss-source | https://proceedings.mlr.press/v119/chen20j/chen20j.pdf; Section 2.1, PDF p. 2, Equation (1); Algorithm 1, p. 3; Section 5.1 and Table 2, p. 6 | supports | A Simple Framework for Contrastive Learning of Visual Representations. ICML 2020, PMLR 119:1597–1607; eleven-page proceedings PDF. Local text pages read: [1]; actual image pages read: [2, 3, 5, 6]. A contrastive cross-entropy objective that uses cosine-normalized, temperature-scaled similarities to identify a paired positive representation among nonself candidates, including that positive in the denominator. |
| bound-context | https://proceedings.mlr.press/v97/poole19a/poole19a.pdf; Section2.3, PDF p.4, Equations(8)–(10), independent-joint-pair expectation and footnote2 | context_only | Poole et al.’s expected InfoNCE derivation states independent joint-pair sampling. The rendered page was reread for the explicitly qualified comparison with SimCLR’s paired-view negative set. It is not evidence that every possible dependent-negative bound fails. |
| jule-source | https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Yang_Joint_Unsupervised_Learning_CVPR_2016_paper.pdf; PDF p.4, printed p.5150, Equation7–10 and Sections3.5.1–3.5.2; current maintained definition and mechanism | supports | The reread page describes image-cluster label updates alternating with representation-learning updates. It supports JULE’s own clustering-task association; IMSAT’s categorical/hashing distinction is unrelated. Only this mapping-rationale correction is assessed for JULE this round. |
| corrections | research/discovery/20261011T091717Z-graph-linkage-contrastive-loss.json; review_refinements changes with before/after hashes, actual correction times and source/claim additions | supports | Issue48 removed an unrelated IMSAT qualifier from JULE’s mapping rationale. Issue49 added primary context and a claim-level citation for the NT-Xent sampling caveat. A redundant normalized NT-Xent spelling alias was also removed after the initial validator reported it. Final changed fields were reread and re-inspected. |

## Limits And Additional Notes

- Adversarial author self-review only; all additions remain DRAFT.
- JULE assessment is limited to its corrected mapping rationale, not whole-record revalidation of scientific claims.
- Initial validation found a redundant NT-Xent alias; it was corrected. The final full gate passed after the later source-citation edit.
- Prior immutable reviews are unchanged. Issues48/49 are traced in the discovery ledger; no earlier structured finding is fabricated.
- Only declared source pages were inspected; source complexity and empirical claims are qualified, and no runtime or benchmark was reproduced.
- Four positive discoveries and the remaining frontier mean the goal remains active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T092103Z-graph-linkage-contrastive-loss
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of graph linkage and NT-Xent, with JULE rationale correction
started_at: '2026-10-11T09:19:10Z'
finished_at: '2026-10-11T09:21:03Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially compared all four new records
    with primary formulas/algorithms and seven exact AIO nodes, and checked the narrow
    JULE correction against its current mechanism and reread primary page. Evidence
    additions and changed inputs were reread and re-inspected. No independent approval
    is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain four source-backed DRAFT concepts, including the exact/approximate
  GDL distinction and NT-Xent specialization. Issues48 and49 have supported current-state
  corrections. JULE coverage is limited to its corrected mapping rationale. No actionable
  finding remains in this declared scope.
source:
  git_revision: df875592b387d423caa6f064b88a5a72e10e5271
  state: working_tree
  inputs:
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/ContrastiveLearning.yaml
    sha256: f8100e15621b6dd3335dc0bc8253da0197719faf6ac00f1369ebbc455a6fa645
    role: context
  - path: data/aio/GraphConvolutionalNetwork.yaml
    sha256: 644b6187436c10693cb547dbaa809b8c00c97ad198db201342e5bc0780c78d44
    role: context
  - path: data/aio/HierarchicalClustering.yaml
    sha256: 144deaecd150e22de207c11a62f19db5f8409443724bd4be4b5c95c53375b258
    role: context
  - path: data/aio/RepresentationLearning.yaml
    sha256: bc7af756440437f60210019e17ad1e2dd15cd1c7cbfbc96312520934b7a5c7ca
    role: context
  - path: data/aio/SelfsupervisedLearning.yaml
    sha256: ad9a98dfee5629f6433f13470f56e333316f8f03847df2c5678faf023d979c0e
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/curated/AcceleratedGraphDegreeLinkage.yaml
    sha256: ecba4d4d92e90d742be03decd10465dedcaf38f33a35430e7e265a2e2179ae17
    role: target
  - path: data/curated/DBSCAN.yaml
    sha256: de7d744d1f7761af64ce963cf5759853d70a586b4188eea757751357e5035f44
    role: context
  - path: data/curated/GraphDegreeLinkage.yaml
    sha256: 0bd60481926261ff2fb8d69f0404a5d0132f3de4f0c915758bfaffa77fd62f8f
    role: target
  - path: data/curated/InfoNCE.yaml
    sha256: b202ebcafc444df533d78ae82c3618d821ce4c5081a99ffe744deb644a6957da
    role: context
  - path: data/curated/JointUnsupervisedLearning.yaml
    sha256: ace629ccfd1294005aa74bc1ad065953d09e534e8c2a93a3495b740f61792f4d
    role: target
  - path: data/curated/KMeans.yaml
    sha256: 50fc1d8d18403a8f314636f68b6812ffd15fec2dfaaf4c32aaad423dfa7ffa03
    role: context
  - path: data/curated/NTXentLoss.yaml
    sha256: 523d119e71f1c16672b42300e2a180495f3a09c53a55385f546f02850fed3255
    role: target
  - path: data/curated/PathIntegralClustering.yaml
    sha256: 62630cc862cc363cc34037447fd70d0b1e793d8ccf0b3339e0777faaefd1172f
    role: target
  - path: data/curated/SimCLR.yaml
    sha256: e00dbf707a274e02df684ad09ae679b9dda832ba42e4aea7db5a157e25385e3d
    role: context
  - path: research/discovery/20261011T091717Z-graph-linkage-contrastive-loss.json
    sha256: 64d7bac778277b91428c1f784c5a921001ab7c8feb95b72fc236c19500e1b463
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
- target_id: AIMech:GraphDegreeLinkage
  path: data/curated/GraphDegreeLinkage.yaml
  label: Graph degree linkage
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GraphDegreeLinkage.yaml
    role: maintained
- target_id: AIMech:AcceleratedGraphDegreeLinkage
  path: data/curated/AcceleratedGraphDegreeLinkage.yaml
  label: Accelerated graph degree linkage
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AcceleratedGraphDegreeLinkage.yaml
    role: maintained
- target_id: AIMech:PathIntegralClustering
  path: data/curated/PathIntegralClustering.yaml
  label: Path integral clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PathIntegralClustering.yaml
    role: maintained
- target_id: AIMech:NTXentLoss
  path: data/curated/NTXentLoss.yaml
  label: Normalized temperature-scaled cross entropy loss
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NTXentLoss.yaml
    role: maintained
- target_id: AIMech:JointUnsupervisedLearning
  path: data/curated/JointUnsupervisedLearning.yaml
  label: Joint unsupervised learning of deep representations and image clusters
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/JointUnsupervisedLearning.yaml
    role: maintained
scope:
  description: All fields of four new concepts plus the changed UnsupervisedClustering
    mapping rationale and curation provenance of JULE.
  selection: Exact four added IDs and one corrected maintained owner from the discovery
    report; no sampling.
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - AIMech:GraphDegreeLinkage
  - AIMech:AcceleratedGraphDegreeLinkage
  - AIMech:PathIntegralClustering
  - AIMech:NTXentLoss
  - AIMech:JointUnsupervisedLearning
  exclusions:
  - target: JULE fields outside the corrected mapping rationale and corresponding
      updated provenance
    reason: The whole pre-existing algorithm was not re-reviewed; older immutable
      whole-record reviews remain historical.
  - target: Uninspected paper pages, source implementation behavior and benchmark
      outcomes
    reason: Only declared text/image pages were read; no model, algorithm implementation
      or benchmark was executed.
  - target: Power iteration clustering, Zell, CHAMELEON, loss variants and older frontier
    reason: Provisional or uninspected primary leads remain future discovery work.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:GraphDegreeLinkage
  - AIMech:AcceleratedGraphDegreeLinkage
  - AIMech:PathIntegralClustering
  - AIMech:NTXentLoss
  - AIMech:JointUnsupervisedLearning
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 50.82s\nChecked 442 record(s); 0 failed.\n\
    Checked 218 curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing,\
    \ 0 changed, 0 unexpected.\nChecked 46 history record(s); 0 error(s).\n{\n  \"\
    repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 44,\n  \"coverage\"\
    : \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:GraphDegreeLinkage
  - AIMech:AcceleratedGraphDegreeLinkage
  - AIMech:PathIntegralClustering
  - AIMech:NTXentLoss
  - AIMech:JointUnsupervisedLearning
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T091717Z-graph-linkage-contrastive-loss.json
  accessed_at: '2026-10-11T09:19:10Z'
  support: supports
  summary: No normalized match among all442 AIO labels/scoped synonyms and214 preceding
    native IDs/names/aliases. Both full checkouts were searched including ignored/hidden
    files;31 lines each were existing SimCLR/InfoNCE component descriptions, source
    citations and discovery/review references. Five neighboring maintained mechanisms
    were compared. PIC is deliberately qualified because power iteration clustering
    is a different primary-paper identity. The initial NT-Xent redundant punctuation-only
    alias failed local validation and was removed before final validation.
  search_scope: All442 AIO labels/scoped synonyms and214 preceding native IDs/names/aliases,
    plus both complete ignored/hidden-inclusive checkouts.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-11T09:19:10Z'
  support: supports
  locator: Seven exact CLASS nodes with definitions, scoped synonyms and outgoing
    relations listed in source_analysis.aio_mapping_inspection
  summary: Seven exact pinned AIO nodes were inspected. Three graph algorithms have
    related matches to UnsupervisedClustering and HierarchicalClustering; these are
    algorithm-to-task associations, not broad/subclass assertions. NT-Xent has a related
    match to ContrastiveLearning, whose AIO node is modeled as a network approach.
    The corrected JULE rationale refers to its own image-clustering procedure and
    preserves its existing task relation.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T091717Z-graph-linkage-contrastive-loss.json
  accessed_at: '2026-10-11T09:19:10Z'
  support: supports
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  summary: SimCLR, InfoNCE, JULE, DBSCAN and KMeans definitions and mechanisms were
    compared. Full neural training, generic contrastive loss, jointly learned linkage,
    density connectivity and centroid assignment are not equivalent to all four selected
    concepts.
- evidence_id: graphdegreelinkage-source
  kind: primary_source
  reference: https://arxiv.org/pdf/1208.5092v1
  locator: Sections 3.1–3.4, PDF pp. 5–8, Definitions 1–2, Equations (1)–(9), Algorithm
    1; supplement Section 6, p. 15, Algorithm 2
  accessed_at: '2026-10-11T09:12:14Z'
  snapshot_sha256: eea827c754d6c59226d10b771ffefb882a60c9787cb6d85c088f8efb595ef31c
  support: supports
  summary: 'Graph Degree Linkage: Agglomerative Clustering on a Directed Graph. arXiv:1208.5092v1,
    2012-08-25; ECCV 2012 manuscript with supplement, 17 PDF pages. Local text pages
    read: [1]; actual image pages read: [3, 4, 5, 6, 7, 8, 15, 16]. An agglomerative
    clustering algorithm that merges the pair with greatest symmetric graph-degree
    affinity, formed by summing products of cluster-normalized incoming and outgoing
    edge weights on a fixed directed nearest-neighbor graph.'
- evidence_id: acceleratedgraphdegreelinkage-source
  kind: primary_source
  reference: https://arxiv.org/pdf/1208.5092v1
  locator: Section 3.4, PDF p. 8, Accelerated GDL; supplement Section 6, p. 15, Algorithm
    3; Section 7, p. 16, AGDL complexity assumptions
  accessed_at: '2026-10-11T09:12:14Z'
  snapshot_sha256: eea827c754d6c59226d10b771ffefb882a60c9787cb6d85c088f8efb595ef31c
  support: supports
  summary: 'Graph Degree Linkage: Agglomerative Clustering on a Directed Graph. arXiv:1208.5092v1,
    2012-08-25; ECCV 2012 manuscript with supplement, 17 PDF pages. Local text pages
    read: [1]; actual image pages read: [3, 4, 5, 6, 7, 8, 15, 16]. An approximate
    graph degree linkage algorithm that selects merges from maintained cluster-neighbor
    sets and updates those sets locally instead of searching every current cluster
    pair.'
- evidence_id: pathintegralclustering-source
  kind: primary_source
  reference: https://waynezhanghk.github.io/papers/pr2013_path_clustering.pdf
  locator: Section 2, PDF pp. 2–3 (printed 3057–3058), Equations (1)–(3), Algorithm
    1; Sections 3.1–3.4, pp. 3–4, Equations (4)–(12); Section 4, p. 5, Equation (14)
  accessed_at: '2026-10-11T09:11:11Z'
  snapshot_sha256: 2fde6e306611f80dca850ddeb5ef4be40a087d7edf5a4020240d3b6559ff914c
  support: supports
  summary: 'Agglomerative clustering via maximum incremental path integral. Pattern
    Recognition 46(11):3056–3065, 2013; author-hosted published article, 10 PDF pages.
    Local text pages read: [1]; actual image pages read: [2, 3, 4, 5]. An agglomerative
    clustering algorithm that merges clusters with the greatest increase in their
    size-normalized sums of discounted random-walk paths when paths are allowed through
    the proposed union.'
- evidence_id: ntxentloss-source
  kind: primary_source
  reference: https://proceedings.mlr.press/v119/chen20j/chen20j.pdf
  locator: Section 2.1, PDF p. 2, Equation (1); Algorithm 1, p. 3; Section 5.1 and
    Table 2, p. 6
  accessed_at: '2026-10-11T07:45:10Z'
  snapshot_sha256: cc620e511bafe8b4b11ca3415f6d7bcf127a05818087bfa49905de3a2e50bc2d
  support: supports
  summary: 'A Simple Framework for Contrastive Learning of Visual Representations.
    ICML 2020, PMLR 119:1597–1607; eleven-page proceedings PDF. Local text pages read:
    [1]; actual image pages read: [2, 3, 5, 6]. A contrastive cross-entropy objective
    that uses cosine-normalized, temperature-scaled similarities to identify a paired
    positive representation among nonself candidates, including that positive in the
    denominator.'
- evidence_id: bound-context
  kind: primary_source
  reference: https://proceedings.mlr.press/v97/poole19a/poole19a.pdf
  locator: Section2.3, PDF p.4, Equations(8)–(10), independent-joint-pair expectation
    and footnote2
  accessed_at: '2026-10-11T08:36:10Z'
  snapshot_sha256: 38da74b0bae67ce3e565808b7bf81ce3efbcb2e2477f436d9afe7d114d1198cc
  support: context_only
  summary: Poole et al.’s expected InfoNCE derivation states independent joint-pair
    sampling. The rendered page was reread for the explicitly qualified comparison
    with SimCLR’s paired-view negative set. It is not evidence that every possible
    dependent-negative bound fails.
- evidence_id: jule-source
  kind: primary_source
  reference: https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Yang_Joint_Unsupervised_Learning_CVPR_2016_paper.pdf
  locator: PDF p.4, printed p.5150, Equation7–10 and Sections3.5.1–3.5.2; current
    maintained definition and mechanism
  accessed_at: '2026-10-11T08:19:18Z'
  snapshot_sha256: dbddc50b2f798c0061bccf29f05577bc15e985dd00c77fa1d42f1615df936f8f
  support: supports
  summary: The reread page describes image-cluster label updates alternating with
    representation-learning updates. It supports JULE’s own clustering-task association;
    IMSAT’s categorical/hashing distinction is unrelated. Only this mapping-rationale
    correction is assessed for JULE this round.
- evidence_id: corrections
  kind: record_content
  reference: research/discovery/20261011T091717Z-graph-linkage-contrastive-loss.json
  locator: review_refinements changes with before/after hashes, actual correction
    times and source/claim additions
  accessed_at: '2026-10-11T09:19:10Z'
  support: supports
  summary: Issue48 removed an unrelated IMSAT qualifier from JULE’s mapping rationale.
    Issue49 added primary context and a claim-level citation for the NT-Xent sampling
    caveat. A redundant normalized NT-Xent spelling alias was also removed after the
    initial validator reported it. Final changed fields were reread and re-inspected.
assessments:
- assessment_id: graphdegreelinkage
  area: evidence
  topic: Identity, mechanism, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:GraphDegreeLinkage
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - graphdegreelinkage-source
  summary: 'GDL is the graph-degree clustering procedure of Zhang et al. Its affinity
    uses a product of directed degree averages, not average pairwise distance or a
    symmetrized graph. GDL-U is the paper’s exact update implementation of this same
    merge criterion; AGDL restricts candidate search and is represented separately.
    JULE incorporates graph-degree affinity while also learning representations and
    changing merge selection, so it is not the same algorithm. No normalized identity
    match was found across all 442 pinned AIO labels/scoped synonyms and 214 preceding
    native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts,
    including ignored and hidden files, returned 31 lines each: existing SimCLR/InfoNCE
    component discussion, shared primary-source references and discovery/review context.
    Five native neighbors and seven exact AIO nodes with scoped synonyms and outgoing
    relations were inspected.'
  details: 'Construct a directed K-nearest-neighbor graph with w_ij=exp(−dist(i,j)^2/sigma^2)
    for retained edges and zero otherwise. Keep W fixed during clustering. Initialize
    clusters as weakly connected components of a smaller K0-nearest-neighbor graph.
    For vertex i and cluster C, define d_in(i,C)=sum_(j in C) w_ji/|C| and d_out(i,C)=sum_(j
    in C) w_ij/|C|. The directed affinity A(B→C)=sum_(i in B) d_in(i,C)d_out(i,C);
    the symmetric merge affinity is A(B,C)=A(B→C)+A(C→B). Repeatedly choose a pair
    with maximum affinity over all current pairs, merge it, and stop at the requested
    cluster count. The exact update implementation uses A((A union B)→C)=A(A→C)+A(B→C),
    while the opposite direction must be computed from the original degree expression;
    both directions are not generally additive. Limitations: The distance, K, K0,
    bandwidth and requested cluster count determine the construction. Weak-component
    initialization can already join observations irreversibly; the merge-only procedure
    cannot recover a requested count larger than the initial number of components.
    Degree products encode two-way connectivity but do not prove recovery of true
    semantic clusters or universal robustness to noise. The graph is directed even
    though the final pair affinity is symmetric. GDL-U preserves the exact criterion
    when updates and tie handling agree. The paper’s AGDL approximation can choose
    different merges and is not an exact synonym. The published complexity analysis
    distinguishes naive GDL from its update and approximate implementations, and assumes
    fixed neighborhood parameters and sparsity. This record asserts no universal runtime
    or benchmark advantage. No implementation or benchmark was executed.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified clustering procedure or named mathematical objective,
      not a model checkpoint or benchmark result.
    evidence_ids:
    - graphdegreelinkage-source
  - name: aio-relations
    value: 'related_match: AIO:UnsupervisedClustering; related_match: AIO:HierarchicalClustering'
    definition: GDL groups unlabeled observations using a specified graph-based merge
      procedure. The AIO target is a clustering task, so this algorithm-to-task association
      does not assert equivalence or an is-a relation. GDL repeatedly merges clusters
      to build an agglomerative hierarchy. The target describes hierarchy construction
      without prescribing this linkage or candidate-search procedure.
    evidence_ids:
    - mapping
- assessment_id: acceleratedgraphdegreelinkage
  area: evidence
  topic: Identity, mechanism, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:AcceleratedGraphDegreeLinkage
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - acceleratedgraphdegreelinkage-source
  summary: 'AGDL is Zhang et al.’s named candidate-restricted approximation to GDL,
    not merely the exact additive-update implementation GDL-U. It retains the GDL
    affinity but can omit the globally best pair after approximate neighbor-set updates.
    It is distinct from JULE’s representation-learning procedure. No normalized identity
    match was found across all 442 pinned AIO labels/scoped synonyms and 214 preceding
    native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts,
    including ignored and hidden files, returned 31 lines each: existing SimCLR/InfoNCE
    component discussion, shared primary-source references and discovery/review context.
    Five native neighbors and seven exact AIO nodes with scoped synonyms and outgoing
    relations were inspected.'
  details: 'Use the same fixed directed neighbor graph, weak-component initialization
    and symmetric product-of-degree affinity as GDL. Initialize a Kc-nearest cluster
    set for each cluster. Search only pairs for which at least one cluster belongs
    to the other’s maintained neighbor set, and merge the highest-affinity eligible
    pair A,B. For any existing cluster whose set contains A or B, add A union B and
    compute the new pair affinity. Build the merged cluster’s set by choosing Kc nearest
    clusters from the union of the two old neighbor sets. Remove A and B from remaining
    neighbor sets and delete their sets. Repeat until the target cluster count. These
    local updates rely on heuristic persistence of cluster-neighbor relationships,
    rather than recomputing every nearest-cluster set exactly. Limitations: The method
    approximates global merge selection, not the defining degree-product formula.
    It has no asserted guarantee of reproducing exact GDL merges or recovering a globally
    optimal partition. Kc and the initial neighbor sets affect which pairs remain
    eligible. The source’s local-update assumptions can fail; an omitted pair need
    not re-enter through an exhaustive search. The supplement’s quadratic complexity
    argument assumes small initial clusters, fixed K/K0/Kc and a bound on how many
    other clusters include a merged cluster in their neighbor sets. A universal worst-case
    quadratic guarantee is not inferred from that argument. Graph construction, initialization,
    irreversibility and prescribed cluster count have the same scope limitations as
    GDL. No implementation, speedup measurement or clustering benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified clustering procedure or named mathematical objective,
      not a model checkpoint or benchmark result.
    evidence_ids:
    - acceleratedgraphdegreelinkage-source
  - name: aio-relations
    value: 'related_match: AIO:UnsupervisedClustering; related_match: AIO:HierarchicalClustering'
    definition: AGDL groups unlabeled observations using a specified graph-based merge
      procedure. The AIO target is a clustering task, so this algorithm-to-task association
      does not assert equivalence or an is-a relation. AGDL repeatedly merges clusters
      to build an agglomerative hierarchy. The target describes hierarchy construction
      without prescribing this linkage or candidate-search procedure.
    evidence_ids:
    - mapping
- assessment_id: pathintegralclustering
  area: evidence
  topic: Identity, mechanism, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:PathIntegralClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - pathintegralclustering-source
  summary: 'This is Zhang, Zhao and Wang’s 2013 maximum-incremental-path-integral
    clustering procedure. The qualified PIC alias denotes path integral clustering,
    not unrelated power-iteration clustering or generic physical path integration.
    Its affinity uses conditional path descriptors, not simply the merged cluster’s
    descriptor minus the two original descriptors. GDL instead uses products of degree
    averages; JULE is a joint neural-learning procedure. No normalized identity match
    was found across all 442 pinned AIO labels/scoped synonyms and 214 preceding native
    IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts,
    including ignored and hidden files, returned 31 lines each: existing SimCLR/InfoNCE
    component discussion, shared primary-source references and discovery/review context.
    Five native neighbors and seven exact AIO nodes with scoped synonyms and outgoing
    relations were inspected.'
  details: 'Build a weighted directed nearest-neighbor graph and row-normalize its
    adjacency W to obtain transition matrix P=D^−1 W. Keep that global P fixed. Initialize
    small clusters by linking each sample to its nearest neighbor and repeatedly merging
    overlapping groups. For nonempty C and 0<z<1, let P_C be the principal submatrix
    of P, without renormalizing its rows inside C, and define S_C=1_C^T(I−z P_C)^−1
    1_C/|C|^2. This sums geometrically discounted within-C transition paths, including
    the length-zero identity contribution. For U=A union B, define S_(A|U)=e_A^T(I−z
    P_U)^−1 e_A/|A|^2, where e_A is the indicator of A among the vertices of U; its
    paths stay in U and start and end in A. Merge the pair maximizing (S_(A|U)−S_A)+(S_(B|U)−S_B),
    then repeat to the requested count. Linear systems can evaluate the descriptors
    without explicitly forming a dense inverse. Limitations: The distance/similarity,
    neighborhood size, bandwidth, discount z and target count are inputs or choices.
    Row normalization needs positive row sums; 0<z<1 and a substochastic principal
    submatrix make the geometric series converge. Initial nearest-neighbor components
    and later greedy merges are irreversible. The algorithm cannot split an initial
    component to reach a larger requested cluster count. No semantic recovery or global
    partition optimum is certified. Conditional path descriptors retain each original
    cluster’s |C|^2 normalization and endpoint indicator. Replacing the affinity by
    S_(A union B)−S_A−S_B changes the method. Principal submatrices are not independently
    renormalized transition matrices. The paper’s efficient-computation discussion
    relies on sparse graphs, iterative solves and chosen conditioning/discount. An
    exact resolvent formula is not a claim of exact finite-iteration numerical solves
    or an unconditional linear bound for the whole clustering algorithm. No runtime
    or benchmark reproduction was performed.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified clustering procedure or named mathematical objective,
      not a model checkpoint or benchmark result.
    evidence_ids:
    - pathintegralclustering-source
  - name: aio-relations
    value: 'related_match: AIO:UnsupervisedClustering; related_match: AIO:HierarchicalClustering'
    definition: Path integral clustering groups unlabeled observations using a specified
      graph-based merge procedure. The AIO target is a clustering task, so this algorithm-to-task
      association does not assert equivalence or an is-a relation. Path integral clustering
      repeatedly merges clusters to build an agglomerative hierarchy. The target describes
      hierarchy construction without prescribing this linkage or candidate-search
      procedure.
    evidence_ids:
    - mapping
- assessment_id: ntxentloss
  area: evidence
  topic: Identity, mechanism, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:NTXentLoss
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - ntxentloss-source
  - bound-context
  summary: 'NT-Xent is the named normalized temperature-scaled configuration of the
    contrastive categorical objective in the SimCLR paper. It specializes the generic
    InfoNCE score and candidate construction rather than defining a mathematically
    unrelated loss family. The loss is not the full SimCLR augmentation/encoder/projection/training
    procedure, and its symmetric two-view minibatch aggregation is stated explicitly.
    The paper credits prior uses; no claim of first invention by SimCLR is made. No
    normalized identity match was found across all 442 pinned AIO labels/scoped synonyms
    and 214 preceding native IDs/names/aliases. Word-delimited fixed-string searches
    of both full checkouts, including ignored and hidden files, returned 31 lines
    each: existing SimCLR/InfoNCE component discussion, shared primary-source references
    and discovery/review context. Five native neighbors and seven exact AIO nodes
    with scoped synonyms and outgoing relations were inspected.'
  details: 'For nonzero representations z_i,z_k and temperature tau>0, use s_ik=z_i^T
    z_k/(||z_i|| ||z_k||). In the SimCLR two-view configuration, N>=2 source examples
    produce 2N views; j is the other view of the same source as anchor i. Define ell(i,j)=−log[exp(s_ij/tau)/sum_(k=1..2N,k≠i)
    exp(s_ik/tau)]. The denominator contains 2N−1 terms: the paired positive and 2N−2
    other-source views; only the anchor itself is excluded. Average ell over both
    directions of every positive pair, giving 2N anchor losses. Temperature changes
    the softmax weighting of candidate similarities. The paper applies this objective
    to projected representations, but the mathematical loss does not itself prescribe
    an encoder, augmentation family or optimizer. Curator qualification from comparing
    the two sampling constructions: SimCLR uses both augmented views of every other
    source as negative candidates, whereas Poole et al.’s Equation (10) states its
    InfoNCE expectation over independent joint pairs. The latter proof is not automatically
    a proof for the full SimCLR candidate construction. This comparison does not assert
    that no alternative dependent-candidate bound can hold. Limitations: Cosine similarity
    requires nonzero representations and the specified temperature is positive. The
    positive is included in the normalization; dropping it or retaining the self-comparison
    yields a different expression. The two views of each other source are dependent
    candidates. The standard independent-negative InfoNCE mutual-information argument
    is not automatically established for this minibatch construction; this record
    asserts a loss, not an unconditional information certificate. Other-source views
    are treated as negatives without guaranteeing semantic dissimilarity. Learned
    usefulness depends on positive construction, candidate sampling and representation
    choices; minimizing the objective alone does not certify downstream quality. The
    named configuration shares the categorical form of InfoNCE. Its record preserves
    the explicit normalization, temperature and batching convention rather than claiming
    a new unrestricted variational bound. No model training or benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: A specified clustering procedure or named mathematical objective,
      not a model checkpoint or benchmark result.
    evidence_ids:
    - ntxentloss-source
  - name: aio-relations
    value: 'related_match: AIO:ContrastiveLearning'
    definition: NT-Xent supplies the positive-versus-negative objective used in contrastive
      representation learning. The AIO target is represented as a neural-network learning
      approach, so this mathematical-method-to-approach association does not assert
      equivalence or subclass membership.
    evidence_ids:
    - mapping
- assessment_id: jule-mapping-correction
  area: grounding
  topic: JULE corrected task-mapping rationale only
  outcome: supported
  target_ids:
  - AIMech:JointUnsupervisedLearning
  evidence_ids:
  - mapping
  - jule-source
  - corrections
  summary: The corrected UnsupervisedClustering rationale now describes JULE’s unlabeled-image
    clustering and representation learning.
  details: The relation and target remain unchanged. Removing the IMSAT-only qualifier
    repairs local scope/provenance wording without changing JULE’s algorithm or upstream
    AIO. This is a current-state assessment of the corrected rationale, not a new
    whole-record review or a fabricated successor to a prior structured finding.
- assessment_id: exact-versus-approximate-linkage
  area: consistency
  topic: GDL, GDL-U and AGDL boundaries
  outcome: supported
  target_ids:
  - AIMech:GraphDegreeLinkage
  - AIMech:AcceleratedGraphDegreeLinkage
  evidence_ids:
  - graphdegreelinkage-source
  - acceleratedgraphdegreelinkage-source
  - neighbors
  summary: Retain exact GDL separately from AGDL’s approximate candidate search; treat
    GDL-U as an exact implementation of GDL.
  details: Average in/out degrees divide by the target cluster’s size before their
    product, while the source-cluster vertices are summed. The graph is directed,
    but pair affinity is symmetric. The one-way additive update is not applied to
    both directions. AGDL searches the union of directed neighbor eligibility and
    updates sets locally; global-pair equivalence and universal quadratic runtime
    are not asserted.
- assessment_id: path-descriptor-normalization
  area: consistency
  topic: Conditional path-integral affinity and numerical assumptions
  outcome: supported
  target_ids:
  - AIMech:PathIntegralClustering
  evidence_ids:
  - pathintegralclustering-source
  summary: Retain the conditional-increment construction with global transition normalization
    and original cluster denominators.
  details: P_C is a principal submatrix of the fixed global row-normalized P. The
    resolvent includes the identity and geometrically discounted paths for0<z<1. Union
    paths retain original-cluster endpoint indicators and |C|² factors. The stated
    affinity is not S_union−S_A−S_B. Sparse numerical solves and empirical robustness
    are not promoted to universal exact-runtime or recovery guarantees.
- assessment_id: loss-family-boundary
  area: scope
  topic: NT-Xent specialization, SimCLR composition and information assumptions
  outcome: supported
  target_ids:
  - AIMech:NTXentLoss
  evidence_ids:
  - ntxentloss-source
  - bound-context
  - neighbors
  - corrections
  summary: Retain the named cosine/temperature objective with its relationship to
    InfoNCE explicit.
  details: The denominator contains the positive and excludes self; two-view SimCLR
    has2N−1 candidates and2N directed anchor losses. Loss identity does not impose
    the complete encoder/augmentation/optimizer procedure. The independent-joint-pair
    proof is cited as context for a curator sampling qualification. No universal impossibility
    claim about correlated negatives is made. Issue49 makes this comparison directly
    traceable.
- assessment_id: mapping-scope
  area: grounding
  topic: Task and learning-approach relations
  outcome: supported
  target_ids:
  - AIMech:GraphDegreeLinkage
  - AIMech:AcceleratedGraphDegreeLinkage
  - AIMech:PathIntegralClustering
  - AIMech:NTXentLoss
  - AIMech:JointUnsupervisedLearning
  evidence_ids:
  - mapping
  - identity
  - neighbors
  - jule-source
  summary: Keep algorithm-to-task and objective-to-approach associations as related
    matches.
  details: Seven exact pinned AIO nodes were inspected. Three graph algorithms have
    related matches to UnsupervisedClustering and HierarchicalClustering; these are
    algorithm-to-task associations, not broad/subclass assertions. NT-Xent has a related
    match to ContrastiveLearning, whose AIO node is modeled as a network approach.
    The corrected JULE rationale refers to its own image-clustering procedure and
    preserves its existing task relation.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:GraphDegreeLinkage
  - AIMech:AcceleratedGraphDegreeLinkage
  - AIMech:PathIntegralClustering
  - AIMech:NTXentLoss
  - AIMech:JointUnsupervisedLearning
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - graphdegreelinkage-source
  - acceleratedgraphdegreelinkage-source
  - pathintegralclustering-source
  - ntxentloss-source
  - bound-context
  - jule-source
  - corrections
  rationale: Exact degree-product linkage, its candidate-search approximation, conditional
    discounted-path clustering and a named normalized contrastive objective have distinct
    declared scopes. GDL-U stays an implementation of exact GDL. NT-Xent is explicitly
    a specialization of generic InfoNCE rather than an unrelated loss family. JULE
    remains a separate jointly learned representation/clustering algorithm; only its
    corrected task rationale is assessed here. No AIO mutation or status promotion
    follows.
limitations:
- Adversarial author self-review only; all additions remain DRAFT.
- JULE assessment is limited to its corrected mapping rationale, not whole-record
  revalidation of scientific claims.
- Initial validation found a redundant NT-Xent alias; it was corrected. The final
  full gate passed after the later source-citation edit.
- Prior immutable reviews are unchanged. Issues48/49 are traced in the discovery ledger;
  no earlier structured finding is fabricated.
- Only declared source pages were inspected; source complexity and empirical claims
  are qualified, and no runtime or benchmark was reproduced.
- Four positive discoveries and the remaining frontier mean the goal remains active.
tags:
- native-concepts
- graph-clustering
- contrastive-learning
- self-review
- discovery-ongoing
```
