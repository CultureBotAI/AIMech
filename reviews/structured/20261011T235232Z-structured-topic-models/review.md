# Scientific self-review of correlated, dynamic and author-topic model families

- Review: 20261011T235232Z-structured-topic-models
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T23:46:55Z
- Finished UTC: 2026-10-11T23:52:32Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain three DRAFT topic-model families with distinct logistic-normal, temporal and author-conditioned structures. Exact source versions and generative assumptions are separated from approximate inference and empirical claims. No actionable curation finding remains in the selected cohort.

## Scope And Provenance

All fields of three maintained probability-model records.

Selection: Exact maintained IDs CorrelatedTopicModel, DynamicTopicModel and AuthorTopicModel; complete selected cohort without sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base c32fb473aa625d9b2c187c4a53b7ef880c2758d6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CorrelatedTopicModel | data/curated/CorrelatedTopicModel.yaml | maintained | Correlated topic model |
| AIMech:DynamicTopicModel | data/curated/DynamicTopicModel.yaml | maintained | Dynamic topic model |
| AIMech:AuthorTopicModel | data/curated/AuthorTopicModel.yaml | maintained | Author-topic model |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:CorrelatedTopicModel, AIMech:DynamicTopicModel, AIMech:AuthorTopicModel | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 149.27s (0:02:29)<br>Checked 442 record(s); 0 failed.<br>Checked 426 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 123 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 120,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:CorrelatedTopicModel, AIMech:DynamicTopicModel, AIMech:AuthorTopicModel | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:CorrelatedTopicModel, AIMech:DynamicTopicModel, AIMech:AuthorTopicModel | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:CorrelatedTopicModel, AIMech:DynamicTopicModel, AIMech:AuthorTopicModel | Command exited 0 with no output. |
| Compositional, temporal and author-topic probability boundaries | passed | True | AIMech:CorrelatedTopicModel, AIMech:DynamicTopicModel, AIMech:AuthorTopicModel | {"softmax_shift_error": 2.220446049250313e-16, "dirichlet_cov12": -0.007936507936507936, "logistic_normal_quadrature_cov12": 0.00880317941602575, "one_logit_auxiliary_bound_gap": 0.5, "adjacent_difference_variance": 0.5, "omitting_cross_covariance": 2, "joint_entropy": 2.4245377798171113, "sum_marginal_entropy": 2.8378770664093453, "beta_two_word_predictive": 0.3333333333333333, "beta_plugin": 0.25, "author_topic_gibbs_probs": [0.609375, 0.04687499999999999, 0.203125, 0.14062499999999997], "gibbs_joint_comparison_error": 2.220446049250313e-16, "uniform_author_mixture": [0.55, 0.45]} |

## Scientific And Domain Assessments

### Identity, definition, generative law, inference scope, limitations and AIO mapping

evidence: supported. Targets: AIMech:CorrelatedTopicModel.

Scoped to the Blei-Lafferty correlated topic model introduced at NIPS 2005 and developed in the 2007 journal article. The defining change is the logistic-normal document mixture, not a word-interaction MRF, dynamic topic evolution, sparse topic graph or the particular variational solver. Topic graphs are optional analyses of fitted latent coordinates. This is not the Dynamic Conditional Correlation econometric model. No normalized identity match was found across all 442 pinned AIO labels and scoped synonyms and 423 preceding native IDs, names and aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main. Ten matched lines in each checkout reduce to nine unique line contents: prior frontier references, copied discovery context and cached web-result mentions. Every matching concept excerpt was inspected; these are not maintained or imported identities. All 200 semantic label/synonym hits were read. Eighteen exact annotated AIO CLASS nodes and outgoing edges were inspected, including 14 verified unchanged from prior reading and four newly read. Thirty contextual YAMLs comprise those 18 AIO records and 12 native neighbors: six fully read here, 23 byte-verified after prior reading and the updated APM verified against its fully reviewed round100 bytes. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.

For fixed K topics beta_k on a finite vocabulary, draw document logits eta_d from N(mu,Sigma), set theta_d=softmax(eta_d), then independently draw each topic assignment z_dn from theta_d and its word from beta_zdn, conditional on these variables. The logistic-normal prior allows associations that a single Dirichlet proportion prior cannot express, including positive pairwise proportion covariance when at least three components are available. Dirichlet proportions are not literally independent: their sum-to-one constraint gives negative off-diagonal covariance for positive concentration parameters. Common shifts of all logits leave proportions unchanged; unrestricted K-logit mean/covariance parameters are not uniquely identified by the induced composition. Logit covariance, proportion covariance and causal relationships are distinct. The original inference scheme approximates each document posterior by independent univariate Gaussian logits and categorical topic assignments. An auxiliary positive scalar bounds expected log-sum-exp from above, yielding a tractable lower bound no greater than the exact mean-field evidence lower bound. Coordinate updates alternate the auxiliary scalar, assignment probabilities, Gaussian means and positive variances; variational EM fits topics and Gaussian parameters from approximate sufficient statistics. Nonconjugacy and the additional bound make this approximate inference, not exact posterior computation or a guarantee of global marginal-likelihood maximization. The journal correction restores entropy in the originally printed corpus bound; the inspected v2 reprint already includes it, and the corpus objective sums expected log joint plus entropy for each document. Limitations: Fixed topic count, finite vocabulary and conditional bag-of-words assumptions remain. Flexible logistic-normal associations do not remove compositional constraints, identify unique semantic topics or establish that all Dirichlet laws are exact special cases. The source assertion that one observed document leaves no advantage for a nondiagonal variational covariance is not a general theorem. Posterior dependence can remain. Substituting the auxiliary bound into an expected log probability, as displayed with equality in the appendices, must be read as a bound rather than an exact expectation. The journal topic graph regresses standardized fitted logit means using lasso and combines neighborhoods. Gaussian precision statements concern specified Gaussian coordinates; graph estimates do not automatically establish conditional independence of proportions, gauge-invariant structure, causal links or consistency from noisy variational means. Reported Science-corpus comparisons use importance sampling or partially observed-document prediction under particular fits. No universal performance or semantic-interpretability advantage is asserted. No author code or benchmark was executed.

### Identity, definition, generative law, inference scope, limitations and AIO mapping

evidence: supported. Targets: AIMech:DynamicTopicModel.

Scoped to Blei and Lafferty's ICML 2006 dynamic topic models. Topic-word distributions evolve, unlike a static topic model with only changing document proportions. The full formulation also evolves the logistic-normal mean for document-topic proportions; the inference exposition explicitly simplifies that part to a fixed Dirichlet prior. Variational Kalman and wavelet approximations are fitting choices, not synonyms for the model family or neural state-space layers. No normalized identity match was found across all 442 pinned AIO labels and scoped synonyms and 423 preceding native IDs, names and aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main. Ten matched lines in each checkout reduce to nine unique line contents: prior frontier references, copied discovery context and cached web-result mentions. Every matching concept excerpt was inspected; these are not maintained or imported identities. All 200 semantic label/synonym hits were read. Eighteen exact annotated AIO CLASS nodes and outgoing edges were inspected, including 14 verified unchanged from prior reading and four newly read. Thirty contextual YAMLs comprise those 18 AIO records and 12 native neighbors: six fully read here, 23 byte-verified after prior reading and the updated APM verified against its fully reviewed round100 bytes. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.

For fixed topic count K and vocabulary, the basic model evolves each topic logit vector as beta_tk&#124;beta_(t-1)k~N(beta_(t-1)k,sigma² I) and maps it through softmax to word probabilities. In the full generative description, alpha_t&#124;alpha_(t-1)~N(alpha_(t-1),delta² I) evolves the document-topic logit mean. Each document draws eta~N(alpha_t,a² I), then topic assignments from softmax(eta) and words from the selected time-specific topic. Initial-state distributions and variance settings must be specified. Documents are grouped into ordered slices; conditional within-document word exchangeability remains. The inference example beginning on p.3 retains evolving topics but fixes a Dirichlet document-proportion prior, a stated simplification rather than an equivalent formula for the entire full model. The published approximation uses Gaussian topic trajectories conditioned on optimized pseudo-observations, retaining time dependence within each topic chain while separating it from document-level latent factors. Gaussian forward filtering and backward smoothing compute the surrogate trajectory moments; a wavelet-regression approach is presented as an alternative. Expected topic-word counts connect document updates to trajectory fitting. Exact Kalman recursions for this Gaussian surrogate do not yield the exact nonconjugate multinomial posterior. The auxiliary expected-log-normalizer bound and numerical optimization introduce approximation; smoothing over a fitted interval can use later observations and must be distinguished from forecasting beyond that interval. Limitations: The basic random-walk model fixes topic count and vocabulary and does not create or remove topics. Richer drift, heteroscedasticity and topic birth/death processes are proposed extensions. Time-slice choice and Gaussian innovation assumptions matter; temporal association is not a causal account of scientific change. Softmax logits are invariant to a common shift. Fixed topic indexing links trajectories, while label permutation and model fitting can still limit semantic identification. The presented isotropic document-logit law does not itself fit the full static CTM covariance or evolving correlations. Appendix A's displayed expected transition quadratic omits adjacent-time posterior covariance terms, and its entropy display does not give the joint correlated Gaussian entropy. A correct Gaussian-chain calculation uses cross-time covariance and the joint covariance determinant. With fixed surrogate variances some omitted terms are constant for mean optimization, but the printed expressions are not certified as exact complete objectives when variances change. The reported next-year Science comparison uses a variational likelihood bound, as stated in Figure 5, rather than computed exact predictive likelihood. The illustrative wavelet approximation and historical results are not a universal accuracy or convergence guarantee. No author implementation or benchmark was executed.

### Identity, definition, generative law, inference scope, limitations and AIO mapping

evidence: supported. Targets: AIMech:AuthorTopicModel.

Scoped to Rosen-Zvi, Griffiths, Steyvers and Smyth's UAI 2004 author-topic model, whose arXiv deposit occurred in 2012. It conditions on a document's authors and pools topic preferences across their documents. It is distinct from document-specific LDA, a pure author-word mixture, author-recipient-topic models and personalized large language models. Latent token-author assignments are model variables, not observed intellectual contributions. No normalized identity match was found across all 442 pinned AIO labels and scoped synonyms and 423 preceding native IDs, names and aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main. Ten matched lines in each checkout reduce to nine unique line contents: prior frontier references, copied discovery context and cached web-result mentions. Every matching concept excerpt was inspected; these are not maintained or imported identities. All 200 semantic label/synonym hits were read. Eighteen exact annotated AIO CLASS nodes and outgoing edges were inspected, including 14 verified unchanged from prior reading and four newly read. Thirty contextual YAMLs comprise those 18 AIO records and 12 native neighbors: six fully read here, 23 byte-verified after prior reading and the updated APM verified against its fully reviewed round100 bytes. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.

For fixed topic count T, draw each author topic vector theta_a from a symmetric Dirichlet(alpha) and each topic word vector phi_t from a symmetric Dirichlet(beta). Given a nonempty observed author set A_d, each token draws x uniformly from A_d, z from theta_x, and w from phi_z. Conditional on theta, the document-topic mixture is the arithmetic mean of its authors' topic vectors. Ordinary smoothed LDA is recovered when every document is assigned its own distinct single author and the priors match; sharing one author across documents instead pools their proportions. The author-word model requires deterministic unique topic assignment per author, a constrained degenerate case rather than a typical positive-Dirichlet draw. The published Gibbs sampler jointly updates each token's author-topic pair after integrating theta and phi. For observed word v, eligible author a in A_d and topic t, the conditional weight is proportional to (n_vt^(-i)+beta)/(n_.t^(-i)+V*beta) times (n_at^(-i)+alpha)/(n_a.^(-i)+T*alpha). Counts exclude the current token; assignments outside A_d have zero weight. The uniform author-selection factor is constant among eligible pairs and cancels in normalization. Dirichlet posterior means conditional on sampled assignments estimate the author-topic and topic-word vectors; averaging across sampled assignments approximates marginal inference. Finite sampling and posterior-mean plug-ins are not exact multiword posterior predictive integration. Limitations: Known author sets, uniform token-level author choice, fixed topic count, bag-of-words observations and stationary author preferences constrain the model. The author set is conditioned on, not generated. Coauthors with indistinguishable participation can be unidentifiable, and inferred assignments do not establish actual authorship contributions or expertise. Topic and author probability vectors are conditionally independent given assignments under the conjugate construction, but their marginal posterior is generally coupled. The product of separate marginal posterior factors displayed in Equation (8) must not be taken as a general exact factorization. Reported prediction averages plug-in conditional means, which need not equal integrated multiword probabilities. The historical held-out NIPS split ensures test authors already occur in training and can incorporate observed words from each test document. It does not demonstrate cold-start prediction for unseen authors. LDA overtakes the author-topic model in reported settings as more document words become available; no blanket superiority is asserted. Symmetric-KL author similarity and topic entropy are descriptive applications. They do not validate reviewer selection, establish causal collaboration or supply calibrated measures of author competence. Finite Gibbs runs and restarts do not prove mixing, and no author software or benchmark was executed.

### Logistic-normal model and approximate inference

consistency: supported. Targets: AIMech:CorrelatedTopicModel.

Retain the CTM family with compositional and variational qualifications.

CTM introduces a document-level logistic-normal mixture; it is neither a within-topic MRF nor a causal topic graph. Dirichlet coordinates are negatively dependent rather than independent. Softmax shift invariance prevents unique unrestricted logit parameters. The auxiliary expected-normalizer bound can be strictly lower than the exact mean-field ELBO; the scalar Gaussian witness has gap 0.5. The source nondiagonal-q claim is not a general theorem. The inspected v2 reprint already includes the entropy addressed by the original-journal correction.

### Temporal model versus Gaussian inference surrogate

consistency: supported. Targets: AIMech:DynamicTopicModel.

Retain the fixed-topic dynamic family and distinguish the simplified inference example.

Topic-word logits evolve through Gaussian transitions; the full document-logit mean also evolves, while the exposition simplifies proportions to a fixed Dirichlet law. Kalman smoothing is exact for the Gaussian surrogate, not the original multinomial posterior. The two-time witness has transition-difference variance 0.5 rather than 2 when cross covariance is omitted; joint entropy 2.4245 differs from summed marginal entropies 2.8379. Printed appendix qualifications do not establish failure of unseen code or invalidate the generative model. Forecasting and smoothing scopes remain distinct.

### Observed authors, collapsed sampling and prediction

consistency: supported. Targets: AIMech:AuthorTopicModel.

Retain the author-topic family with exact special-case conditions.

Uniform token-author choice is restricted to the observed author set. The collapsed joint ratio matches the leave-one-out Gibbs expression to floating-point precision in a finite example. Document-specific LDA requires a distinct single author per document. Marginal topic/author parameter posteriors need not factorize, and posterior-mean plug-ins need not integrate multiword probabilities: the Beta example gives 1/3 versus 1/4. Identical coauthor patterns limit identifiability; latent assignments do not establish actual contributions.

### Primary versions, locators and empirical boundaries

consistency: supported. Targets: AIMech:CorrelatedTopicModel, AIMech:DynamicTopicModel, AIMech:AuthorTopicModel.

Preserve publication/deposit and reprint distinctions.

All 45 primary pages were visually inspected. NIPS 2005 CTM model Figure 1 is on PDF p.3, inference is Section 2.1 on pp.4-5, and Appendix A is p.8; provisional locator errors were corrected before the formal saved review. The CTM journal reprint has its own pagination. Author-topic publication is UAI 2004, not its 2012 arXiv deposit. DTM reports variational predictive bounds, and author-topic evaluation covers authors seen in training. No universal empirical advantage, author-code execution or benchmark reproduction is asserted.

### Model/task direction and neighboring meanings

grounding: supported. Targets: AIMech:CorrelatedTopicModel, AIMech:DynamicTopicModel, AIMech:AuthorTopicModel.

Retain three distinct native model families.

All three native probability-model families map broadly to AIO Model and related to task-scoped ProbabilisticTopicModel. DynamicTopicModel additionally maps related to TimeSeriesAnalysis. CorrelatedTopicModel is a logistic-normal document mixture, not the econometric DynamicConditionalCorrelation model. AuthorTopicModel is a finite author-conditioned generative law, not PersonalizedLLM. ExponentialSmoothingStateSpaceModel is a particular forecasting family, not every Gaussian state transition; TimeSeriesForecasting is a task, and smoothing is not automatically forecasting. MarkovChain, SoftmaxFunction, LassoRegression, BayesianNetwork and ProbabilisticGraphicalModel describe components or broader graphical roles rather than these exact identities. CausalGraphicalModel does not follow from statistical topic associations. Native LDA/PLSA, SAGE, Replicated Softmax, APM and fixed-length PMRF topic models have different mixture priors or word laws. HMM and factorial-HMM structured VI use different hidden state laws; LSSL is a neural layer. BBVI and EM are inference/estimation algorithms, not the present model families. BayesianDataAugmentation is specifically a supervised synthetic-data deep-learning method, not general latent-variable augmentation. No contextual record receives renewed scientific approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:CorrelatedTopicModel, AIMech:DynamicTopicModel, AIMech:AuthorTopicModel. Logistic-normal document mixtures, evolving topic trajectories and shared author-specific mixtures define distinct model families. Shared topic vocabulary and approximate-inference tools do not establish equivalence. Preserve broad Model and related task mappings; no upstream AIO identity or empirical approval is inferred.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T234625Z-structured-topic-models.json | supports | No normalized identity match was found across all 442 pinned AIO labels and scoped synonyms and 423 preceding native IDs, names and aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main. Ten matched lines in each checkout reduce to nine unique line contents: prior frontier references, copied discovery context and cached web-result mentions. Every matching concept excerpt was inspected; these are not maintained or imported identities. All 200 semantic label/synonym hits were read. Eighteen exact annotated AIO CLASS nodes and outgoing edges were inspected, including 14 verified unchanged from prior reading and four newly read. Thirty contextual YAMLs comprise those 18 AIO records and 12 native neighbors: six fully read here, 23 byte-verified after prior reading and the updated APM verified against its fully reviewed round100 bytes. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood. |
| mapping | sources/aio/aio.json; 18 exact CLASS nodes and outgoing edges; all 200 semantic label/synonym hits in source_analysis.aio_mapping_inspection | supports | All three native probability-model families map broadly to AIO Model and related to task-scoped ProbabilisticTopicModel. DynamicTopicModel additionally maps related to TimeSeriesAnalysis. CorrelatedTopicModel is a logistic-normal document mixture, not the econometric DynamicConditionalCorrelation model. AuthorTopicModel is a finite author-conditioned generative law, not PersonalizedLLM. ExponentialSmoothingStateSpaceModel is a particular forecasting family, not every Gaussian state transition; TimeSeriesForecasting is a task, and smoothing is not automatically forecasting. MarkovChain, SoftmaxFunction, LassoRegression, BayesianNetwork and ProbabilisticGraphicalModel describe components or broader graphical roles rather than these exact identities. CausalGraphicalModel does not follow from statistical topic associations. Native LDA/PLSA, SAGE, Replicated Softmax, APM and fixed-length PMRF topic models have different mixture priors or word laws. HMM and factorial-HMM structured VI use different hidden state laws; LSSL is a neural layer. BBVI and EM are inference/estimation algorithms, not the present model families. BayesianDataAugmentation is specifically a supervised synthetic-data deep-learning method, not general latent-variable augmentation. No contextual record receives renewed scientific approval. |
| neighbors | research/discovery/20261011T234625Z-structured-topic-models.json; Twelve full native neighbors and 18 generated contextual records in context_reading | supports | LDA, PLSA, SAGE, Replicated Softmax, APM, fixed-length PMRF topic model, HMM, factorial-HMM structured VI, BBVI, LSSL, EM and the specifically scoped Bayesian deep-model augmentation record inform distinctions. Six contextual YAMLs were read here, 23 verified unchanged after prior reading and final APM verified against round100 inspection. This is not renewed scientific approval of contextual records. |
| finite-boundaries | research/discovery/topic-structure-boundaries.py; Softmax and covariance witnesses, Gaussian chain moments, collapsed joint ratios and predictive integration | supports | Synthetic witnesses check softmax common-shift invariance, exact negative Dirichlet covariance, a positive logistic-normal covariance illustration by three-point Gaussian quadrature, and a strict auxiliary-bound gap for one Gaussian logit. A two-time correlated Gaussian demonstrates the missing transition cross-covariance and the difference between joint and marginal entropies. Exact small collapsed-joint ratios reproduce author-topic leave-one-out Gibbs probabilities. A Beta two-word example distinguishes integrated prediction from a posterior-mean plug-in, and author-profile exchange preserves a uniform coauthor mixture. Quadrature is approximate; these calculations are not author-code execution or corpus results. |
| correlatedtopicmodel-source-0 | https://papers.nips.cc/paper/2005/file/9e82757e9a1c12cb710ad680db11f6f1-Paper.pdf; Section 2, PDF pp.2-3, Equations (1)-(3); Section 2, PDF pp.2-3, Figure 1 and Equation (3); Section 2.1, PDF pp.4-5; Appendix A, p.8, Equations (4)-(17) | supports | Correlated Topic Models. NIPS 2005 official eight-page PDF; all pages visually read. Use PDF page numbers. Proceedings volume 18 is also cited with 2006 publication year. Complete primary PDF visually read; the ledger distinguishes source statements, curator qualifications and unexecuted empirical work. |
| correlatedtopicmodel-source-1 | https://arxiv.org/pdf/0708.3601v2; Section 2, PDF/reprint pp.4-6, Figure 1 and softmax nonminimality note; Section 2, PDF/reprint pp.4-6, generative process and Equation (1); Section 3.1-3.2, PDF/reprint pp.7-9; Appendix, pp.16-18, Equations (9)-(20) | supports | A Correlated Topic Model of Science. Annals of Applied Statistics 2007 article; inspected arXiv:0708.3601v2 electronic reprint, 20 pages. Reprint explicitly differs from journal pagination; locators use PDF/reprint pages. All pages visually read. Its p.9 already includes the entropy term addressed by the separate journal correction. Complete primary PDF visually read; the ledger distinguishes source statements, curator qualifications and unexecuted empirical work. |
| correlatedtopicmodel-source-2 | https://arxiv.org/pdf/0712.1486v1; Entire one-page correction, printed p.634, referring to original journal p.24 | supports | Correction: A Correlated Topic Model of Science. One-page Annals of Applied Statistics 2007 correction, inspected arXiv:0712.1486v1; printed p.634. Entire page visually read. Complete primary PDF visually read; the ledger distinguishes source statements, curator qualifications and unexecuted empirical work. |
| dynamictopicmodel-source-0 | https://www.cs.columbia.edu/~blei/papers/BleiLafferty2006a.pdf; Section 2 and opening of Section 3, PDF pp.2-3; Section 2, PDF pp.2-3, Equations (1)-(2), Figure 1 and generative process; Section 3, PDF pp.3-5, Equations (3)-(4); Appendix A, pp.7-8 | supports | Dynamic Topic Models. ICML 2006 author-hosted eight-page manuscript, including Appendix A. All pages visually read; locators use PDF page numbers. Complete primary PDF visually read; the ledger distinguishes source statements, curator qualifications and unexecuted empirical work. |
| authortopicmodel-source-0 | https://arxiv.org/pdf/1207.4169v1; Section 2.3 and Figure 1(c), printed pp.488-489 / PDF pp.2-3; Section 3, printed pp.489-490 / PDF pp.3-4, Equations (4)-(6); Section 4.2, p.492 / PDF p.6, Equation (8); Sections 2.1-2.3, printed pp.488-489 / PDF pp.2-3, including smoothed-LDA footnote and special cases | supports | The Author-Topic Model for Authors and Documents. UAI 2004 proceedings pp.487-494, deposited as arXiv:1207.4169v1 in 2012. All eight pages visually read. Printed page = PDF page +486. Complete primary PDF visually read; the ledger distinguishes source statements, curator qualifications and unexecuted empirical work. |

## Limits And Additional Notes

- Adversarial author self-review only; all three records remain DRAFT.
- All 45 PDF pages across five primary documents were visually read, including the CTM correction, journal appendix, DTM appendix and author-topic tables. PDF extraction is a reading aid; only the visual reading is asserted here.
- The CTM v2 electronic reprint differs from journal pagination and already incorporates entropy in its corpus bound. The separate correction refers to the original journal display. NIPS 2005 inference is Section 2.1, not Section 3; precise locators were corrected before formal review.
- The DTM Gaussian-chain appendix and author-topic posterior-factorization displays require the explicit qualifications retained in their records. No author implementation was inspected or executed, and no empirical result was reproduced.
- All sources were accessible. Bibliography and search leads remain provisional until full identity/evidence assessment. All six new cohorts were deduplicated against 432 prior cohort labels and ignored-inclusive checkout searches.
- All maintained records remain DRAFT; review is adversarial author self-review. The 264 pending leads and other unresolved dispositions preclude a saturation claim.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T235232Z-structured-topic-models
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of correlated, dynamic and author-topic model families
started_at: '2026-10-11T23:46:55Z'
finished_at: '2026-10-11T23:52:32Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all fields of three
    final records against 45 complete primary PDF pages, 18 annotated AIO nodes and
    12 native contextual records. Finite calculations tested covariance, Gaussian-chain
    and collapsed-sampling distinctions. This is author self-review, not independent
    approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain three DRAFT topic-model families with distinct logistic-normal, temporal
  and author-conditioned structures. Exact source versions and generative assumptions
  are separated from approximate inference and empirical claims. No actionable curation
  finding remains in the selected cohort.
source:
  git_revision: c32fb473aa625d9b2c187c4a53b7ef880c2758d6
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/DynamicConditionalCorrelation.yaml
    sha256: 5cf6959d2e27d395fdc956473bf305fcaf9f5d99ad0a855477b49c609a7ed43b
    role: context
  - path: data/aio/ExponentialSmoothingStateSpaceModel.yaml
    sha256: e54f9504ddd176b6fc08542cdacb2ab5cdb5a25cec8501ccf071de34881ec79d
    role: context
  - path: data/aio/LanguageModel.yaml
    sha256: 67c8faa6d8ac8fb5194931f662d513d1527cefb92ab1d7c283b2c8d1ddc20c4a
    role: context
  - path: data/aio/LassoRegression.yaml
    sha256: c62e7ffd00a16f5a82d514687b094aee5f6796d19a7d16200bdb10498c024949
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/PersonalizedLLM.yaml
    sha256: c31d8e53b6ef629c9524297350a27e766b6c1e29efbeea9abb0390f311d3f6bd
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ProbabilisticTopicModel.yaml
    sha256: a3ddfd23b511de967f562e99542d8a89109852359d286a4d707d784359ddfe32
    role: context
  - path: data/aio/RepresentationLearning.yaml
    sha256: bc7af756440437f60210019e17ad1e2dd15cd1c7cbfbc96312520934b7a5c7ca
    role: context
  - path: data/aio/SoftmaxFunction.yaml
    sha256: 150cf1f70d0a49c2515fc4569b451c6b835050346797db01b0536751b867e69f
    role: context
  - path: data/aio/TimeSeriesAnalysis.yaml
    sha256: c26b267d0f5fb895e9cb0eb587fe86a115d461dae4d70e0ac6baf1eefb1d4eff
    role: context
  - path: data/aio/TimeSeriesForecasting.yaml
    sha256: 88bbef37663508cc885b40d258cdb6b720c627c0f73af1935c01a372c18b3863
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/AdmixtureOfPoissonMarkovRandomFields.yaml
    sha256: a8541c4ee4241152c68898fbe925661eb68e33119ba19a6fe3e4e1d24c3d3f90
    role: context
  - path: data/curated/AuthorTopicModel.yaml
    sha256: 732dd9bc7f7bfbfb461f4cca668f72b128449e27f4008a0e9a3cd90c15e8a28f
    role: target
  - path: data/curated/BayesianDataAugmentation.yaml
    sha256: 4d95781fa743392ee3bcda4cf5cb3d79a35052750a01e090d2bc54b5693e14b5
    role: context
  - path: data/curated/BlackBoxVariationalInference.yaml
    sha256: 8237d3233ae06163b8fab5b4fa047ffc938e275bc1e3ede883348e06c2b266a8
    role: context
  - path: data/curated/CorrelatedTopicModel.yaml
    sha256: 22654d8ad69cbe6a464faf19d4c0bbd9a8a74b966197cd05443f9d01f851b893
    role: target
  - path: data/curated/DynamicTopicModel.yaml
    sha256: 3ea748baf3dcedb99616573346822cb7d7bd3cb75ed496fcbb0cb152bee76f0e
    role: target
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: context
  - path: data/curated/FixedLengthPoissonMRFTopicModel.yaml
    sha256: bf8bf0556cbeaf48e98700e462a402ce681f3dba33e31a2a256f582672187048
    role: context
  - path: data/curated/HiddenMarkovModel.yaml
    sha256: 062a31bd525cb90e8077d4889c177f55cb7b29dea4e71c33be95bae9e72a5240
    role: context
  - path: data/curated/LatentDirichletAllocation.yaml
    sha256: d8147371973fa1a5d5e9d3487d092e64ab70271ab42c18d199cd868bb8eb5aef
    role: context
  - path: data/curated/LinearStateSpaceLayer.yaml
    sha256: 05d7d834a8c0db4c33613384cde4a250838290cce6960fda10e7209da318c151
    role: context
  - path: data/curated/ProbabilisticLatentSemanticAnalysis.yaml
    sha256: e9cb970e4795b65a17c073a109b4716fc42f2aa0661bf3f7be128568b19ecc71
    role: context
  - path: data/curated/ReplicatedSoftmax.yaml
    sha256: 1a71debad5b7ac38c8e647ffb18c52f712300a7906b44efa5d348fb3488940cf
    role: context
  - path: data/curated/SparseAdditiveGenerativeModel.yaml
    sha256: 446900da4ecc41ccf341a27fe1f51c6a2dd2723e972bbc32a8bdb069cccdabdd
    role: context
  - path: data/curated/StructuredVariationalInferenceForFactorialHMMs.yaml
    sha256: 236f080993e164f5768f1eb1a179ff3589b03344cf133091fea5d35cc3ce4918
    role: context
  - path: research/discovery/20261011T234625Z-structured-topic-models.json
    sha256: b9259a24000ef8d365736f67bffff2e2bb5ae9f632ae5d32d1c77f88960bf169
    role: context
  - path: research/discovery/topic-structure-boundaries.py
    sha256: d1335250d6d507621dce9f79944dd65d964046a13d25d8246f6ea80b9fd33132
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
- target_id: AIMech:CorrelatedTopicModel
  path: data/curated/CorrelatedTopicModel.yaml
  label: Correlated topic model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CorrelatedTopicModel.yaml
    role: maintained
- target_id: AIMech:DynamicTopicModel
  path: data/curated/DynamicTopicModel.yaml
  label: Dynamic topic model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DynamicTopicModel.yaml
    role: maintained
- target_id: AIMech:AuthorTopicModel
  path: data/curated/AuthorTopicModel.yaml
  label: Author-topic model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AuthorTopicModel.yaml
    role: maintained
scope:
  description: All fields of three maintained probability-model records.
  selection: Exact maintained IDs CorrelatedTopicModel, DynamicTopicModel and AuthorTopicModel;
    complete selected cohort without sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:CorrelatedTopicModel
  - AIMech:DynamicTopicModel
  - AIMech:AuthorTopicModel
  exclusions:
  - target: Author software, trained instances and empirical reproduction
    reason: No author implementation or benchmark was executed. Synthetic arithmetic
      does not replicate the published experiments or certify unseen source code.
  - target: Contextual records and remaining discovery frontier
    reason: Twelve native neighbors inform identities without renewed scientific approval.
      Six new provisional reference cohorts and 264 pending leads plus other unresolved
      dispositions remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:CorrelatedTopicModel
  - AIMech:DynamicTopicModel
  - AIMech:AuthorTopicModel
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 149.27s (0:02:29)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 426 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 123 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 120,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:CorrelatedTopicModel
  - AIMech:DynamicTopicModel
  - AIMech:AuthorTopicModel
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
  - AIMech:CorrelatedTopicModel
  - AIMech:DynamicTopicModel
  - AIMech:AuthorTopicModel
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
  - AIMech:CorrelatedTopicModel
  - AIMech:DynamicTopicModel
  - AIMech:AuthorTopicModel
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Compositional, temporal and author-topic probability boundaries
  command: python3 research/discovery/topic-structure-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CorrelatedTopicModel
  - AIMech:DynamicTopicModel
  - AIMech:AuthorTopicModel
  exit_code: 0
  expected_exit_code: 0
  summary: '{"softmax_shift_error": 2.220446049250313e-16, "dirichlet_cov12": -0.007936507936507936,
    "logistic_normal_quadrature_cov12": 0.00880317941602575, "one_logit_auxiliary_bound_gap":
    0.5, "adjacent_difference_variance": 0.5, "omitting_cross_covariance": 2, "joint_entropy":
    2.4245377798171113, "sum_marginal_entropy": 2.8378770664093453, "beta_two_word_predictive":
    0.3333333333333333, "beta_plugin": 0.25, "author_topic_gibbs_probs": [0.609375,
    0.04687499999999999, 0.203125, 0.14062499999999997], "gibbs_joint_comparison_error":
    2.220446049250313e-16, "uniform_author_mixture": [0.55, 0.45]}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T234625Z-structured-topic-models.json
  accessed_at: '2026-10-11T23:46:55Z'
  support: supports
  summary: 'No normalized identity match was found across all 442 pinned AIO labels
    and scoped synonyms and 423 preceding native IDs, names and aliases. Full-checkout
    fixed-string searches included ignored and hidden files in worktree and main.
    Ten matched lines in each checkout reduce to nine unique line contents: prior
    frontier references, copied discovery context and cached web-result mentions.
    Every matching concept excerpt was inspected; these are not maintained or imported
    identities. All 200 semantic label/synonym hits were read. Eighteen exact annotated
    AIO CLASS nodes and outgoing edges were inspected, including 14 verified unchanged
    from prior reading and four newly read. Thirty contextual YAMLs comprise those
    18 AIO records and 12 native neighbors: six fully read here, 23 byte-verified
    after prior reading and the updated APM verified against its fully reviewed round100
    bytes. Absence is bounded to the pinned snapshot, maintained corpus and inspected
    semantic neighborhood.'
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison; short acronyms were omitted
    from broad substring searches to avoid irrelevant matches. All nine unique matched-line
    contexts were inspected; long cached web transcripts were examined at every matching
    concept mention, not treated as full primary-method evidence.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 18 exact CLASS nodes and outgoing edges; all 200 semantic label/synonym
    hits in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T23:46:55Z'
  support: supports
  summary: All three native probability-model families map broadly to AIO Model and
    related to task-scoped ProbabilisticTopicModel. DynamicTopicModel additionally
    maps related to TimeSeriesAnalysis. CorrelatedTopicModel is a logistic-normal
    document mixture, not the econometric DynamicConditionalCorrelation model. AuthorTopicModel
    is a finite author-conditioned generative law, not PersonalizedLLM. ExponentialSmoothingStateSpaceModel
    is a particular forecasting family, not every Gaussian state transition; TimeSeriesForecasting
    is a task, and smoothing is not automatically forecasting. MarkovChain, SoftmaxFunction,
    LassoRegression, BayesianNetwork and ProbabilisticGraphicalModel describe components
    or broader graphical roles rather than these exact identities. CausalGraphicalModel
    does not follow from statistical topic associations. Native LDA/PLSA, SAGE, Replicated
    Softmax, APM and fixed-length PMRF topic models have different mixture priors
    or word laws. HMM and factorial-HMM structured VI use different hidden state laws;
    LSSL is a neural layer. BBVI and EM are inference/estimation algorithms, not the
    present model families. BayesianDataAugmentation is specifically a supervised
    synthetic-data deep-learning method, not general latent-variable augmentation.
    No contextual record receives renewed scientific approval.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T234625Z-structured-topic-models.json
  locator: Twelve full native neighbors and 18 generated contextual records in context_reading
  accessed_at: '2026-10-11T23:46:55Z'
  support: supports
  summary: LDA, PLSA, SAGE, Replicated Softmax, APM, fixed-length PMRF topic model,
    HMM, factorial-HMM structured VI, BBVI, LSSL, EM and the specifically scoped Bayesian
    deep-model augmentation record inform distinctions. Six contextual YAMLs were
    read here, 23 verified unchanged after prior reading and final APM verified against
    round100 inspection. This is not renewed scientific approval of contextual records.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/topic-structure-boundaries.py
  locator: Softmax and covariance witnesses, Gaussian chain moments, collapsed joint
    ratios and predictive integration
  accessed_at: '2026-10-11T23:46:55Z'
  snapshot_sha256: d1335250d6d507621dce9f79944dd65d964046a13d25d8246f6ea80b9fd33132
  support: supports
  summary: Synthetic witnesses check softmax common-shift invariance, exact negative
    Dirichlet covariance, a positive logistic-normal covariance illustration by three-point
    Gaussian quadrature, and a strict auxiliary-bound gap for one Gaussian logit.
    A two-time correlated Gaussian demonstrates the missing transition cross-covariance
    and the difference between joint and marginal entropies. Exact small collapsed-joint
    ratios reproduce author-topic leave-one-out Gibbs probabilities. A Beta two-word
    example distinguishes integrated prediction from a posterior-mean plug-in, and
    author-profile exchange preserves a uniform coauthor mixture. Quadrature is approximate;
    these calculations are not author-code execution or corpus results.
- evidence_id: correlatedtopicmodel-source-0
  kind: primary_source
  reference: https://papers.nips.cc/paper/2005/file/9e82757e9a1c12cb710ad680db11f6f1-Paper.pdf
  locator: Section 2, PDF pp.2-3, Equations (1)-(3); Section 2, PDF pp.2-3, Figure
    1 and Equation (3); Section 2.1, PDF pp.4-5; Appendix A, p.8, Equations (4)-(17)
  accessed_at: '2026-10-11T23:35:15Z'
  snapshot_sha256: 0430674307aa8d0c8a2c3425f890ade080fe932059187c37402dfd1be4a658c6
  support: supports
  summary: Correlated Topic Models. NIPS 2005 official eight-page PDF; all pages visually
    read. Use PDF page numbers. Proceedings volume 18 is also cited with 2006 publication
    year. Complete primary PDF visually read; the ledger distinguishes source statements,
    curator qualifications and unexecuted empirical work.
- evidence_id: correlatedtopicmodel-source-1
  kind: primary_source
  reference: https://arxiv.org/pdf/0708.3601v2
  locator: Section 2, PDF/reprint pp.4-6, Figure 1 and softmax nonminimality note;
    Section 2, PDF/reprint pp.4-6, generative process and Equation (1); Section 3.1-3.2,
    PDF/reprint pp.7-9; Appendix, pp.16-18, Equations (9)-(20)
  accessed_at: '2026-10-11T23:35:17Z'
  snapshot_sha256: e6ec936eeb5c4090d5cce54c189cb464d28810efc00460bca65b8c897939503c
  support: supports
  summary: A Correlated Topic Model of Science. Annals of Applied Statistics 2007
    article; inspected arXiv:0708.3601v2 electronic reprint, 20 pages. Reprint explicitly
    differs from journal pagination; locators use PDF/reprint pages. All pages visually
    read. Its p.9 already includes the entropy term addressed by the separate journal
    correction. Complete primary PDF visually read; the ledger distinguishes source
    statements, curator qualifications and unexecuted empirical work.
- evidence_id: correlatedtopicmodel-source-2
  kind: primary_source
  reference: https://arxiv.org/pdf/0712.1486v1
  locator: Entire one-page correction, printed p.634, referring to original journal
    p.24
  accessed_at: '2026-10-11T23:35:20Z'
  snapshot_sha256: 14231c48512223ca5cd00f5c4148d2247a5de86f0623baaaa0afaa51a4798cf0
  support: supports
  summary: 'Correction: A Correlated Topic Model of Science. One-page Annals of Applied
    Statistics 2007 correction, inspected arXiv:0712.1486v1; printed p.634. Entire
    page visually read. Complete primary PDF visually read; the ledger distinguishes
    source statements, curator qualifications and unexecuted empirical work.'
- evidence_id: dynamictopicmodel-source-0
  kind: primary_source
  reference: https://www.cs.columbia.edu/~blei/papers/BleiLafferty2006a.pdf
  locator: Section 2 and opening of Section 3, PDF pp.2-3; Section 2, PDF pp.2-3,
    Equations (1)-(2), Figure 1 and generative process; Section 3, PDF pp.3-5, Equations
    (3)-(4); Appendix A, pp.7-8
  accessed_at: '2026-10-11T23:35:20Z'
  snapshot_sha256: 0af8ce7a05e1f24964473fd99e90a5ed6f6631e5ac091e8acb73779feacbc4d4
  support: supports
  summary: Dynamic Topic Models. ICML 2006 author-hosted eight-page manuscript, including
    Appendix A. All pages visually read; locators use PDF page numbers. Complete primary
    PDF visually read; the ledger distinguishes source statements, curator qualifications
    and unexecuted empirical work.
- evidence_id: authortopicmodel-source-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1207.4169v1
  locator: Section 2.3 and Figure 1(c), printed pp.488-489 / PDF pp.2-3; Section 3,
    printed pp.489-490 / PDF pp.3-4, Equations (4)-(6); Section 4.2, p.492 / PDF p.6,
    Equation (8); Sections 2.1-2.3, printed pp.488-489 / PDF pp.2-3, including smoothed-LDA
    footnote and special cases
  accessed_at: '2026-10-11T23:35:23Z'
  snapshot_sha256: d6a920e2b903fbfe855fee7b5a50eb68b3c336c2c7279aa3028a2105fd081430
  support: supports
  summary: The Author-Topic Model for Authors and Documents. UAI 2004 proceedings
    pp.487-494, deposited as arXiv:1207.4169v1 in 2012. All eight pages visually read.
    Printed page = PDF page +486. Complete primary PDF visually read; the ledger distinguishes
    source statements, curator qualifications and unexecuted empirical work.
assessments:
- assessment_id: correlatedtopicmodel
  area: evidence
  topic: Identity, definition, generative law, inference scope, limitations and AIO
    mapping
  outcome: supported
  target_ids:
  - AIMech:CorrelatedTopicModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - correlatedtopicmodel-source-0
  - correlatedtopicmodel-source-1
  - correlatedtopicmodel-source-2
  summary: 'Scoped to the Blei-Lafferty correlated topic model introduced at NIPS
    2005 and developed in the 2007 journal article. The defining change is the logistic-normal
    document mixture, not a word-interaction MRF, dynamic topic evolution, sparse
    topic graph or the particular variational solver. Topic graphs are optional analyses
    of fitted latent coordinates. This is not the Dynamic Conditional Correlation
    econometric model. No normalized identity match was found across all 442 pinned
    AIO labels and scoped synonyms and 423 preceding native IDs, names and aliases.
    Full-checkout fixed-string searches included ignored and hidden files in worktree
    and main. Ten matched lines in each checkout reduce to nine unique line contents:
    prior frontier references, copied discovery context and cached web-result mentions.
    Every matching concept excerpt was inspected; these are not maintained or imported
    identities. All 200 semantic label/synonym hits were read. Eighteen exact annotated
    AIO CLASS nodes and outgoing edges were inspected, including 14 verified unchanged
    from prior reading and four newly read. Thirty contextual YAMLs comprise those
    18 AIO records and 12 native neighbors: six fully read here, 23 byte-verified
    after prior reading and the updated APM verified against its fully reviewed round100
    bytes. Absence is bounded to the pinned snapshot, maintained corpus and inspected
    semantic neighborhood.'
  details: 'For fixed K topics beta_k on a finite vocabulary, draw document logits
    eta_d from N(mu,Sigma), set theta_d=softmax(eta_d), then independently draw each
    topic assignment z_dn from theta_d and its word from beta_zdn, conditional on
    these variables. The logistic-normal prior allows associations that a single Dirichlet
    proportion prior cannot express, including positive pairwise proportion covariance
    when at least three components are available. Dirichlet proportions are not literally
    independent: their sum-to-one constraint gives negative off-diagonal covariance
    for positive concentration parameters. Common shifts of all logits leave proportions
    unchanged; unrestricted K-logit mean/covariance parameters are not uniquely identified
    by the induced composition. Logit covariance, proportion covariance and causal
    relationships are distinct. The original inference scheme approximates each document
    posterior by independent univariate Gaussian logits and categorical topic assignments.
    An auxiliary positive scalar bounds expected log-sum-exp from above, yielding
    a tractable lower bound no greater than the exact mean-field evidence lower bound.
    Coordinate updates alternate the auxiliary scalar, assignment probabilities, Gaussian
    means and positive variances; variational EM fits topics and Gaussian parameters
    from approximate sufficient statistics. Nonconjugacy and the additional bound
    make this approximate inference, not exact posterior computation or a guarantee
    of global marginal-likelihood maximization. The journal correction restores entropy
    in the originally printed corpus bound; the inspected v2 reprint already includes
    it, and the corpus objective sums expected log joint plus entropy for each document.
    Limitations: Fixed topic count, finite vocabulary and conditional bag-of-words
    assumptions remain. Flexible logistic-normal associations do not remove compositional
    constraints, identify unique semantic topics or establish that all Dirichlet laws
    are exact special cases. The source assertion that one observed document leaves
    no advantage for a nondiagonal variational covariance is not a general theorem.
    Posterior dependence can remain. Substituting the auxiliary bound into an expected
    log probability, as displayed with equality in the appendices, must be read as
    a bound rather than an exact expectation. The journal topic graph regresses standardized
    fitted logit means using lasso and combines neighborhoods. Gaussian precision
    statements concern specified Gaussian coordinates; graph estimates do not automatically
    establish conditional independence of proportions, gauge-invariant structure,
    causal links or consistency from noisy variational means. Reported Science-corpus
    comparisons use importance sampling or partially observed-document prediction
    under particular fits. No universal performance or semantic-interpretability advantage
    is asserted. No author code or benchmark was executed.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A probability-model family with specified latent structure, distinct
      from its approximate fitting algorithm or a trained instance.
    evidence_ids:
    - correlatedtopicmodel-source-0
    - correlatedtopicmodel-source-1
    - correlatedtopicmodel-source-2
  - name: aio-assessment
    value: broad_match,related_match
    definition: All three native probability-model families map broadly to AIO Model
      and related to task-scoped ProbabilisticTopicModel. DynamicTopicModel additionally
      maps related to TimeSeriesAnalysis. CorrelatedTopicModel is a logistic-normal
      document mixture, not the econometric DynamicConditionalCorrelation model. AuthorTopicModel
      is a finite author-conditioned generative law, not PersonalizedLLM. ExponentialSmoothingStateSpaceModel
      is a particular forecasting family, not every Gaussian state transition; TimeSeriesForecasting
      is a task, and smoothing is not automatically forecasting. MarkovChain, SoftmaxFunction,
      LassoRegression, BayesianNetwork and ProbabilisticGraphicalModel describe components
      or broader graphical roles rather than these exact identities. CausalGraphicalModel
      does not follow from statistical topic associations. Native LDA/PLSA, SAGE,
      Replicated Softmax, APM and fixed-length PMRF topic models have different mixture
      priors or word laws. HMM and factorial-HMM structured VI use different hidden
      state laws; LSSL is a neural layer. BBVI and EM are inference/estimation algorithms,
      not the present model families. BayesianDataAugmentation is specifically a supervised
      synthetic-data deep-learning method, not general latent-variable augmentation.
      No contextual record receives renewed scientific approval.
    evidence_ids:
    - mapping
- assessment_id: dynamictopicmodel
  area: evidence
  topic: Identity, definition, generative law, inference scope, limitations and AIO
    mapping
  outcome: supported
  target_ids:
  - AIMech:DynamicTopicModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - dynamictopicmodel-source-0
  summary: 'Scoped to Blei and Lafferty''s ICML 2006 dynamic topic models. Topic-word
    distributions evolve, unlike a static topic model with only changing document
    proportions. The full formulation also evolves the logistic-normal mean for document-topic
    proportions; the inference exposition explicitly simplifies that part to a fixed
    Dirichlet prior. Variational Kalman and wavelet approximations are fitting choices,
    not synonyms for the model family or neural state-space layers. No normalized
    identity match was found across all 442 pinned AIO labels and scoped synonyms
    and 423 preceding native IDs, names and aliases. Full-checkout fixed-string searches
    included ignored and hidden files in worktree and main. Ten matched lines in each
    checkout reduce to nine unique line contents: prior frontier references, copied
    discovery context and cached web-result mentions. Every matching concept excerpt
    was inspected; these are not maintained or imported identities. All 200 semantic
    label/synonym hits were read. Eighteen exact annotated AIO CLASS nodes and outgoing
    edges were inspected, including 14 verified unchanged from prior reading and four
    newly read. Thirty contextual YAMLs comprise those 18 AIO records and 12 native
    neighbors: six fully read here, 23 byte-verified after prior reading and the updated
    APM verified against its fully reviewed round100 bytes. Absence is bounded to
    the pinned snapshot, maintained corpus and inspected semantic neighborhood.'
  details: 'For fixed topic count K and vocabulary, the basic model evolves each topic
    logit vector as beta_tk|beta_(t-1)k~N(beta_(t-1)k,sigma² I) and maps it through
    softmax to word probabilities. In the full generative description, alpha_t|alpha_(t-1)~N(alpha_(t-1),delta²
    I) evolves the document-topic logit mean. Each document draws eta~N(alpha_t,a²
    I), then topic assignments from softmax(eta) and words from the selected time-specific
    topic. Initial-state distributions and variance settings must be specified. Documents
    are grouped into ordered slices; conditional within-document word exchangeability
    remains. The inference example beginning on p.3 retains evolving topics but fixes
    a Dirichlet document-proportion prior, a stated simplification rather than an
    equivalent formula for the entire full model. The published approximation uses
    Gaussian topic trajectories conditioned on optimized pseudo-observations, retaining
    time dependence within each topic chain while separating it from document-level
    latent factors. Gaussian forward filtering and backward smoothing compute the
    surrogate trajectory moments; a wavelet-regression approach is presented as an
    alternative. Expected topic-word counts connect document updates to trajectory
    fitting. Exact Kalman recursions for this Gaussian surrogate do not yield the
    exact nonconjugate multinomial posterior. The auxiliary expected-log-normalizer
    bound and numerical optimization introduce approximation; smoothing over a fitted
    interval can use later observations and must be distinguished from forecasting
    beyond that interval. Limitations: The basic random-walk model fixes topic count
    and vocabulary and does not create or remove topics. Richer drift, heteroscedasticity
    and topic birth/death processes are proposed extensions. Time-slice choice and
    Gaussian innovation assumptions matter; temporal association is not a causal account
    of scientific change. Softmax logits are invariant to a common shift. Fixed topic
    indexing links trajectories, while label permutation and model fitting can still
    limit semantic identification. The presented isotropic document-logit law does
    not itself fit the full static CTM covariance or evolving correlations. Appendix
    A''s displayed expected transition quadratic omits adjacent-time posterior covariance
    terms, and its entropy display does not give the joint correlated Gaussian entropy.
    A correct Gaussian-chain calculation uses cross-time covariance and the joint
    covariance determinant. With fixed surrogate variances some omitted terms are
    constant for mean optimization, but the printed expressions are not certified
    as exact complete objectives when variances change. The reported next-year Science
    comparison uses a variational likelihood bound, as stated in Figure 5, rather
    than computed exact predictive likelihood. The illustrative wavelet approximation
    and historical results are not a universal accuracy or convergence guarantee.
    No author implementation or benchmark was executed.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A probability-model family with specified latent structure, distinct
      from its approximate fitting algorithm or a trained instance.
    evidence_ids:
    - dynamictopicmodel-source-0
  - name: aio-assessment
    value: broad_match,related_match,related_match
    definition: All three native probability-model families map broadly to AIO Model
      and related to task-scoped ProbabilisticTopicModel. DynamicTopicModel additionally
      maps related to TimeSeriesAnalysis. CorrelatedTopicModel is a logistic-normal
      document mixture, not the econometric DynamicConditionalCorrelation model. AuthorTopicModel
      is a finite author-conditioned generative law, not PersonalizedLLM. ExponentialSmoothingStateSpaceModel
      is a particular forecasting family, not every Gaussian state transition; TimeSeriesForecasting
      is a task, and smoothing is not automatically forecasting. MarkovChain, SoftmaxFunction,
      LassoRegression, BayesianNetwork and ProbabilisticGraphicalModel describe components
      or broader graphical roles rather than these exact identities. CausalGraphicalModel
      does not follow from statistical topic associations. Native LDA/PLSA, SAGE,
      Replicated Softmax, APM and fixed-length PMRF topic models have different mixture
      priors or word laws. HMM and factorial-HMM structured VI use different hidden
      state laws; LSSL is a neural layer. BBVI and EM are inference/estimation algorithms,
      not the present model families. BayesianDataAugmentation is specifically a supervised
      synthetic-data deep-learning method, not general latent-variable augmentation.
      No contextual record receives renewed scientific approval.
    evidence_ids:
    - mapping
- assessment_id: authortopicmodel
  area: evidence
  topic: Identity, definition, generative law, inference scope, limitations and AIO
    mapping
  outcome: supported
  target_ids:
  - AIMech:AuthorTopicModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - authortopicmodel-source-0
  summary: 'Scoped to Rosen-Zvi, Griffiths, Steyvers and Smyth''s UAI 2004 author-topic
    model, whose arXiv deposit occurred in 2012. It conditions on a document''s authors
    and pools topic preferences across their documents. It is distinct from document-specific
    LDA, a pure author-word mixture, author-recipient-topic models and personalized
    large language models. Latent token-author assignments are model variables, not
    observed intellectual contributions. No normalized identity match was found across
    all 442 pinned AIO labels and scoped synonyms and 423 preceding native IDs, names
    and aliases. Full-checkout fixed-string searches included ignored and hidden files
    in worktree and main. Ten matched lines in each checkout reduce to nine unique
    line contents: prior frontier references, copied discovery context and cached
    web-result mentions. Every matching concept excerpt was inspected; these are not
    maintained or imported identities. All 200 semantic label/synonym hits were read.
    Eighteen exact annotated AIO CLASS nodes and outgoing edges were inspected, including
    14 verified unchanged from prior reading and four newly read. Thirty contextual
    YAMLs comprise those 18 AIO records and 12 native neighbors: six fully read here,
    23 byte-verified after prior reading and the updated APM verified against its
    fully reviewed round100 bytes. Absence is bounded to the pinned snapshot, maintained
    corpus and inspected semantic neighborhood.'
  details: 'For fixed topic count T, draw each author topic vector theta_a from a
    symmetric Dirichlet(alpha) and each topic word vector phi_t from a symmetric Dirichlet(beta).
    Given a nonempty observed author set A_d, each token draws x uniformly from A_d,
    z from theta_x, and w from phi_z. Conditional on theta, the document-topic mixture
    is the arithmetic mean of its authors'' topic vectors. Ordinary smoothed LDA is
    recovered when every document is assigned its own distinct single author and the
    priors match; sharing one author across documents instead pools their proportions.
    The author-word model requires deterministic unique topic assignment per author,
    a constrained degenerate case rather than a typical positive-Dirichlet draw. The
    published Gibbs sampler jointly updates each token''s author-topic pair after
    integrating theta and phi. For observed word v, eligible author a in A_d and topic
    t, the conditional weight is proportional to (n_vt^(-i)+beta)/(n_.t^(-i)+V*beta)
    times (n_at^(-i)+alpha)/(n_a.^(-i)+T*alpha). Counts exclude the current token;
    assignments outside A_d have zero weight. The uniform author-selection factor
    is constant among eligible pairs and cancels in normalization. Dirichlet posterior
    means conditional on sampled assignments estimate the author-topic and topic-word
    vectors; averaging across sampled assignments approximates marginal inference.
    Finite sampling and posterior-mean plug-ins are not exact multiword posterior
    predictive integration. Limitations: Known author sets, uniform token-level author
    choice, fixed topic count, bag-of-words observations and stationary author preferences
    constrain the model. The author set is conditioned on, not generated. Coauthors
    with indistinguishable participation can be unidentifiable, and inferred assignments
    do not establish actual authorship contributions or expertise. Topic and author
    probability vectors are conditionally independent given assignments under the
    conjugate construction, but their marginal posterior is generally coupled. The
    product of separate marginal posterior factors displayed in Equation (8) must
    not be taken as a general exact factorization. Reported prediction averages plug-in
    conditional means, which need not equal integrated multiword probabilities. The
    historical held-out NIPS split ensures test authors already occur in training
    and can incorporate observed words from each test document. It does not demonstrate
    cold-start prediction for unseen authors. LDA overtakes the author-topic model
    in reported settings as more document words become available; no blanket superiority
    is asserted. Symmetric-KL author similarity and topic entropy are descriptive
    applications. They do not validate reviewer selection, establish causal collaboration
    or supply calibrated measures of author competence. Finite Gibbs runs and restarts
    do not prove mixing, and no author software or benchmark was executed.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A probability-model family with specified latent structure, distinct
      from its approximate fitting algorithm or a trained instance.
    evidence_ids:
    - authortopicmodel-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: All three native probability-model families map broadly to AIO Model
      and related to task-scoped ProbabilisticTopicModel. DynamicTopicModel additionally
      maps related to TimeSeriesAnalysis. CorrelatedTopicModel is a logistic-normal
      document mixture, not the econometric DynamicConditionalCorrelation model. AuthorTopicModel
      is a finite author-conditioned generative law, not PersonalizedLLM. ExponentialSmoothingStateSpaceModel
      is a particular forecasting family, not every Gaussian state transition; TimeSeriesForecasting
      is a task, and smoothing is not automatically forecasting. MarkovChain, SoftmaxFunction,
      LassoRegression, BayesianNetwork and ProbabilisticGraphicalModel describe components
      or broader graphical roles rather than these exact identities. CausalGraphicalModel
      does not follow from statistical topic associations. Native LDA/PLSA, SAGE,
      Replicated Softmax, APM and fixed-length PMRF topic models have different mixture
      priors or word laws. HMM and factorial-HMM structured VI use different hidden
      state laws; LSSL is a neural layer. BBVI and EM are inference/estimation algorithms,
      not the present model families. BayesianDataAugmentation is specifically a supervised
      synthetic-data deep-learning method, not general latent-variable augmentation.
      No contextual record receives renewed scientific approval.
    evidence_ids:
    - mapping
- assessment_id: ctm-composition
  area: consistency
  topic: Logistic-normal model and approximate inference
  outcome: supported
  target_ids:
  - AIMech:CorrelatedTopicModel
  evidence_ids:
  - correlatedtopicmodel-source-0
  - correlatedtopicmodel-source-1
  - correlatedtopicmodel-source-2
  - finite-boundaries
  - neighbors
  summary: Retain the CTM family with compositional and variational qualifications.
  details: CTM introduces a document-level logistic-normal mixture; it is neither
    a within-topic MRF nor a causal topic graph. Dirichlet coordinates are negatively
    dependent rather than independent. Softmax shift invariance prevents unique unrestricted
    logit parameters. The auxiliary expected-normalizer bound can be strictly lower
    than the exact mean-field ELBO; the scalar Gaussian witness has gap 0.5. The source
    nondiagonal-q claim is not a general theorem. The inspected v2 reprint already
    includes the entropy addressed by the original-journal correction.
- assessment_id: dtm-trajectories
  area: consistency
  topic: Temporal model versus Gaussian inference surrogate
  outcome: supported
  target_ids:
  - AIMech:DynamicTopicModel
  evidence_ids:
  - dynamictopicmodel-source-0
  - finite-boundaries
  - neighbors
  summary: Retain the fixed-topic dynamic family and distinguish the simplified inference
    example.
  details: Topic-word logits evolve through Gaussian transitions; the full document-logit
    mean also evolves, while the exposition simplifies proportions to a fixed Dirichlet
    law. Kalman smoothing is exact for the Gaussian surrogate, not the original multinomial
    posterior. The two-time witness has transition-difference variance 0.5 rather
    than 2 when cross covariance is omitted; joint entropy 2.4245 differs from summed
    marginal entropies 2.8379. Printed appendix qualifications do not establish failure
    of unseen code or invalidate the generative model. Forecasting and smoothing scopes
    remain distinct.
- assessment_id: author-conditioned-mixtures
  area: consistency
  topic: Observed authors, collapsed sampling and prediction
  outcome: supported
  target_ids:
  - AIMech:AuthorTopicModel
  evidence_ids:
  - authortopicmodel-source-0
  - finite-boundaries
  - neighbors
  summary: Retain the author-topic family with exact special-case conditions.
  details: 'Uniform token-author choice is restricted to the observed author set.
    The collapsed joint ratio matches the leave-one-out Gibbs expression to floating-point
    precision in a finite example. Document-specific LDA requires a distinct single
    author per document. Marginal topic/author parameter posteriors need not factorize,
    and posterior-mean plug-ins need not integrate multiword probabilities: the Beta
    example gives 1/3 versus 1/4. Identical coauthor patterns limit identifiability;
    latent assignments do not establish actual contributions.'
- assessment_id: source-version-scope
  area: consistency
  topic: Primary versions, locators and empirical boundaries
  outcome: supported
  target_ids:
  - AIMech:CorrelatedTopicModel
  - AIMech:DynamicTopicModel
  - AIMech:AuthorTopicModel
  evidence_ids:
  - correlatedtopicmodel-source-0
  - correlatedtopicmodel-source-1
  - correlatedtopicmodel-source-2
  - dynamictopicmodel-source-0
  - authortopicmodel-source-0
  summary: Preserve publication/deposit and reprint distinctions.
  details: All 45 primary pages were visually inspected. NIPS 2005 CTM model Figure
    1 is on PDF p.3, inference is Section 2.1 on pp.4-5, and Appendix A is p.8; provisional
    locator errors were corrected before the formal saved review. The CTM journal
    reprint has its own pagination. Author-topic publication is UAI 2004, not its
    2012 arXiv deposit. DTM reports variational predictive bounds, and author-topic
    evaluation covers authors seen in training. No universal empirical advantage,
    author-code execution or benchmark reproduction is asserted.
- assessment_id: mapping-boundary
  area: grounding
  topic: Model/task direction and neighboring meanings
  outcome: supported
  target_ids:
  - AIMech:CorrelatedTopicModel
  - AIMech:DynamicTopicModel
  - AIMech:AuthorTopicModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain three distinct native model families.
  details: All three native probability-model families map broadly to AIO Model and
    related to task-scoped ProbabilisticTopicModel. DynamicTopicModel additionally
    maps related to TimeSeriesAnalysis. CorrelatedTopicModel is a logistic-normal
    document mixture, not the econometric DynamicConditionalCorrelation model. AuthorTopicModel
    is a finite author-conditioned generative law, not PersonalizedLLM. ExponentialSmoothingStateSpaceModel
    is a particular forecasting family, not every Gaussian state transition; TimeSeriesForecasting
    is a task, and smoothing is not automatically forecasting. MarkovChain, SoftmaxFunction,
    LassoRegression, BayesianNetwork and ProbabilisticGraphicalModel describe components
    or broader graphical roles rather than these exact identities. CausalGraphicalModel
    does not follow from statistical topic associations. Native LDA/PLSA, SAGE, Replicated
    Softmax, APM and fixed-length PMRF topic models have different mixture priors
    or word laws. HMM and factorial-HMM structured VI use different hidden state laws;
    LSSL is a neural layer. BBVI and EM are inference/estimation algorithms, not the
    present model families. BayesianDataAugmentation is specifically a supervised
    synthetic-data deep-learning method, not general latent-variable augmentation.
    No contextual record receives renewed scientific approval.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:CorrelatedTopicModel
  - AIMech:DynamicTopicModel
  - AIMech:AuthorTopicModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - correlatedtopicmodel-source-0
  - correlatedtopicmodel-source-1
  - correlatedtopicmodel-source-2
  - dynamictopicmodel-source-0
  - authortopicmodel-source-0
  rationale: Logistic-normal document mixtures, evolving topic trajectories and shared
    author-specific mixtures define distinct model families. Shared topic vocabulary
    and approximate-inference tools do not establish equivalence. Preserve broad Model
    and related task mappings; no upstream AIO identity or empirical approval is inferred.
limitations:
- Adversarial author self-review only; all three records remain DRAFT.
- All 45 PDF pages across five primary documents were visually read, including the
  CTM correction, journal appendix, DTM appendix and author-topic tables. PDF extraction
  is a reading aid; only the visual reading is asserted here.
- The CTM v2 electronic reprint differs from journal pagination and already incorporates
  entropy in its corpus bound. The separate correction refers to the original journal
  display. NIPS 2005 inference is Section 2.1, not Section 3; precise locators were
  corrected before formal review.
- The DTM Gaussian-chain appendix and author-topic posterior-factorization displays
  require the explicit qualifications retained in their records. No author implementation
  was inspected or executed, and no empirical result was reproduced.
- All sources were accessible. Bibliography and search leads remain provisional until
  full identity/evidence assessment. All six new cohorts were deduplicated against
  432 prior cohort labels and ignored-inclusive checkout searches.
- All maintained records remain DRAFT; review is adversarial author self-review. The
  264 pending leads and other unresolved dispositions preclude a saturation claim.
links: []
tags:
- native-concepts
- structured-topic-models
- self-review
- discovery-ongoing
```
