# Scientific self-review of PLSA, latent Dirichlet allocation and tempered EM

- Review: 20261011T232435Z-classical-topic-models
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T23:20:39Z
- Finished UTC: 2026-10-11T23:24:35Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain PLSA, latent Dirichlet allocation and tempered EM as DRAFT concepts. Fitted document weights, random Dirichlet mixtures and powered latent responsibilities have distinct roles. Approximate inference and printed-expression limitations remain qualified; no actionable curation finding remains in the selected batch.

## Scope And Provenance

All fields of two classical topic-model records and one tempered fitting algorithm.

Selection: Exact maintained IDs ProbabilisticLatentSemanticAnalysis, LatentDirichletAllocation and TemperedExpectationMaximization; complete selected batch without sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 90838c7d687b598499646824fd12cd3bc83661fe.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ProbabilisticLatentSemanticAnalysis | data/curated/ProbabilisticLatentSemanticAnalysis.yaml | maintained | Probabilistic latent semantic analysis |
| AIMech:LatentDirichletAllocation | data/curated/LatentDirichletAllocation.yaml | maintained | Latent Dirichlet allocation |
| AIMech:TemperedExpectationMaximization | data/curated/TemperedExpectationMaximization.yaml | maintained | Tempered expectation maximization |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:ProbabilisticLatentSemanticAnalysis, AIMech:LatentDirichletAllocation, AIMech:TemperedExpectationMaximization | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 128.39s (0:02:08)<br>Checked 442 record(s); 0 failed.<br>Checked 421 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 121 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 118,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:ProbabilisticLatentSemanticAnalysis, AIMech:LatentDirichletAllocation, AIMech:TemperedExpectationMaximization | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:ProbabilisticLatentSemanticAnalysis, AIMech:LatentDirichletAllocation, AIMech:TemperedExpectationMaximization | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:ProbabilisticLatentSemanticAnalysis, AIMech:LatentDirichletAllocation, AIMech:TemperedExpectationMaximization | Command exited 0 with no output. |
| Topic-mixture normalization, posterior moments, EM updates, tempered free energy and source-expression checks | passed | True | AIMech:ProbabilisticLatentSemanticAnalysis, AIMech:LatentDirichletAllocation, AIMech:TemperedExpectationMaximization | {"status": "passed", "lda_normalization_lengths": [0, 1, 2, 3, 4, 5], "two_word_same_symbol": {"lda": 0.3433333333333334, "fixed_weights": 0.30250000000000005, "document_mixture": 0.42500000000000004}, "count_mass": [0.14625000000000005, 0.29125000000000006, 0.32875000000000004, 0.23375000000000007], "posterior_second_moments": {"exact_mixture": 0.4393939393939394, "expected_count_dirichlet": 0.42699724517906334}, "plsa_em_loglikelihood": [-15.296684988212109, -14.887801605993316], "tempered_responsibilities": {"beta1": [0.8571428571428571, 0.14285714285714285], "beta_half": [0.7101020514433644, 0.2898979485566356]}, "tempered_kl_gap": 0.027686811684659862, "empirical_mixture_total": {"correct": 1.0, "literal_inside_product": 0.3699999999999999}, "alpha_hessian": {"derived": -1.6944444444444446, "finite_difference": -1.6944445917488338, "printed": 2.3584133116557906}} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:ProbabilisticLatentSemanticAnalysis.

PLSA denotes the aspect-model probability construction, also called the probabilistic latent semantic indexing model in the LDA comparison. A document can mix several aspects because each co-occurrence has its own latent class. It differs from an SVD reconstruction, a single class for a whole document, and LDA’s prior over document-specific topic weights. The alias PLSI identifies this underlying model, not every cosine, interpolation or model-averaging choice in a retrieval pipeline. Tempered EM is one fitting procedure rather than part of the model’s defining probability law. Compared all 442 pinned AIO labels and scoped synonyms and 418 preceding native IDs, names and aliases. The initial normalized LDA hit denotes LinearDiscriminantAnalysis, whose full Gaussian-classifier record was read; the bare LDA alias is omitted from the new topic-model record. No normalized identity match remains for the final candidate names/aliases. Final full-checkout fixed-string searches, including ignored and hidden files in both worktree and main, return two lines each; both unique contents are existing frontier references. An additional broad LDA search returned 289 worktree and 237 main lines before the preceding batch merged; all 84 distinct contents were read, covering the existing classifier, topic-context references, unrelated programming mnemonics and namespace abbreviations. All 188 semantic label/synonym hits were read. Nineteen exact annotated AIO CLASS nodes and outgoing edges were inspected (18 verified unchanged from prior reading, Biclustering read here), along with their generated records and 16 native neighbors. The 35 contextual YAMLs were read or byte-verified after documented full reading. Absence is bounded to this snapshot, maintained corpus and inspected semantic neighborhood.

For finite document indices d, vocabulary items w and K latent classes z, choose normalized nonnegative distributions pi_z, a_z(d) and b_z(w), and define p(d,w)=sum_z pi_z*a_z(d)*b_z(w). Given z, d and w are independent. Equivalently, for p(d)&gt;0, p(w&#124;d)=sum_z theta_dz*b_z(w), where theta_dz=pi_z*a_z(d)/p(d). Fit observed counts n(d,w) with sum_dw n(d,w)*log p(d,w). An exact EM E-step computes r_dwz=pi_z*a_z(d)*b_z(w)/p(d,w); M-steps normalize the corresponding count-weighted responsibilities over words, documents and classes. Each conditional document word distribution is an arithmetic convex combination of topic probabilities. In the original fold-in procedure, keep b_z(w) fixed and fit a new query or document’s mixture weights. This introduces new fitted weights rather than integrating over a population prior as in LDA. Limitations: The base construction is a normalized distribution of indexed co-occurrences. It has no LDA-style population prior on new document mixtures; fold-in estimation is possible, so this is not a claim that unseen documents cannot be represented at all. Training-document mixture parameters grow with the corpus. Maximum-likelihood or tempered fitting can overfit; local EM optimization, initialization and rank selection do not guarantee global optimality or unique factors. Permuting topic labels preserves the law, and linearly dependent topic distributions can yield nonunique mixture weights. The bag-of-words representation omits token order and explicit within-topic word interactions. It is not a raw-count Poisson MRF, a canonical-parameter admixture, or a neural density estimator. Topic labels and selected high-probability words are interpretations, not verified semantic or causal categories. Positive-count cells require positive modeled mass. Responsibility updates need nonzero denominators; unused components require a specified handling convention. Zero-count terms use the standard zero-contribution convention. Historical retrieval experiments use particular corpora, ranks, held-out tempering and cosine interpolation. No universal retrieval advantage, exact new-document marginal likelihood or author implementation is certified.

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:LatentDirichletAllocation.

The defining feature is a shared prior over document-specific topic proportions together with repeated per-token topic selection. This differs from PLSA’s fitted document-index weights and a mixture selecting one topic for a whole document. The model is distinct from its variational EM, sampling or other inference algorithms. The bare LDA alias is omitted because AIMech already uses it for the unrelated Gaussian classifier LinearDiscriminantAnalysis. The base fixed-topic-probability presentation and its Bayesian topic-prior extension are distinguished explicitly. Compared all 442 pinned AIO labels and scoped synonyms and 418 preceding native IDs, names and aliases. The initial normalized LDA hit denotes LinearDiscriminantAnalysis, whose full Gaussian-classifier record was read; the bare LDA alias is omitted from the new topic-model record. No normalized identity match remains for the final candidate names/aliases. Final full-checkout fixed-string searches, including ignored and hidden files in both worktree and main, return two lines each; both unique contents are existing frontier references. An additional broad LDA search returned 289 worktree and 237 main lines before the preceding batch merged; all 84 distinct contents were read, covering the existing classifier, topic-context references, unrelated programming mnemonics and namespace abbreviations. All 188 semantic label/synonym hits were read. Nineteen exact annotated AIO CLASS nodes and outgoing edges were inspected (18 verified unchanged from prior reading, Biclustering read here), along with their generated records and 16 native neighbors. The 35 contextual YAMLs were read or byte-verified after documented full reading. Absence is bounded to this snapshot, maintained corpus and inspected semantic neighborhood.

For a fixed K, positive alpha_i and normalized topic-word probability rows B_i, draw theta_d~Dirichlet(alpha) independently for each document. Given a document length N_d, draw z_dn~Categorical(theta_d) and w_dn~Categorical(B_zdn) for each token. Conditional on theta_d and B, token probabilities are sum_i theta_di*B_iw and tokens are independent; integrating theta_d gives p(w_d&#124;alpha,B)=integral Dir(theta_d;alpha)*product_n(sum_i theta_di*B_i,w_dn)dtheta_d. This is an exchangeable document distribution, generally with dependent tokens after integration. An unordered count vector additionally includes its multinomial multiplicity. The paper’s Poisson length law is optional to this conditional construction. For fixed B, its mean-field approximation is q(theta,z)=Dir(theta;gamma)*product_n Cat(z_n;phi_n), with phi_ni proportional B_i,w_n*exp[digamma(gamma_i)-digamma(sum_j gamma_j)] and gamma_i=alpha_i+sum_n phi_ni. Variational EM optimizes the evidence lower bound, updating B from expected topic-word counts and alpha numerically. Section 5.4 separately places Dirichlet priors on B; then the assignment update uses expected log topic probabilities, not fixed B values. Limitations: The number of topics is finite and fixed in this construction. Integrating a continuous Dirichlet mixture does not introduce infinitely many topic classes. Infinite exchangeability supports the representation discussed in Section 3.1; arbitrary finite exchangeability alone is not the asserted theorem. Given observed topic assignments, Dirichlet conjugacy is exact. With topics unobserved, the marginal posterior over proportions is generally not a single Dirichlet; gamma=alpha+expected counts is a variational update, not exact marginal conjugacy. Exact inference is generally difficult, and bound optimization need not monotonically improve the true likelihood or attain its global maximum. The basic model ignores word order and explicit within-topic dependencies, though integrating document proportions induces dependence between tokens. Zero word probabilities require smoothing or other support handling for novel documents. A prior over document mixtures does not guarantee freedom from overfitting, identifiable topics or meaningful semantic labels. The Bayesian topic-prior extension requires expected log topic probabilities in its assignment update. The appendix’s printed alpha Hessian has a sign/factor mismatch with the preceding gradient; the consistent Hessian is M*(trigamma(sum alpha)-delta_ij*trigamma(alpha_i)). This record does not adopt that printed Hessian as verified code. Equation (13) correctly uses the normalized posterior. The comparison’s empirical mixture over training-document indices must weight an entire document once; the printed p(d) inside its token product is not adopted. These mathematical qualifications do not establish an error in unseen author software or experiments. The source’s document, classification and recommendation experiments have distinct protocols. No exact likelihood replication, generic performance advantage or biological-mechanism conclusion is claimed. All source material concerns the specified 2003 model, not every later topic-model extension.

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:TemperedExpectationMaximization.

This record denotes the deterministic free-energy fitting procedure described by Hofmann, with his held-out inverse-annealing schedule as an explicit realization. Ordinary EM is its beta=1 case. The procedure changes responsibilities and parameter fitting; it is neither replica-exchange MCMC nor a supervised confidence-mask schedule, and it does not introduce a new topic-model probability family. The short TEM acronym is not asserted as a globally unambiguous alias. Compared all 442 pinned AIO labels and scoped synonyms and 418 preceding native IDs, names and aliases. The initial normalized LDA hit denotes LinearDiscriminantAnalysis, whose full Gaussian-classifier record was read; the bare LDA alias is omitted from the new topic-model record. No normalized identity match remains for the final candidate names/aliases. Final full-checkout fixed-string searches, including ignored and hidden files in both worktree and main, return two lines each; both unique contents are existing frontier references. An additional broad LDA search returned 289 worktree and 237 main lines before the preceding batch merged; all 84 distinct contents were read, covering the existing classifier, topic-context references, unrelated programming mnemonics and namespace abbreviations. All 188 semantic label/synonym hits were read. Nineteen exact annotated AIO CLASS nodes and outgoing edges were inspected (18 verified unchanged from prior reading, Biclustering read here), along with their generated records and 16 native neighbors. The 35 contextual YAMLs were read or byte-verified after documented full reading. Absence is bounded to this snapshot, maintained corpus and inspected semantic neighborhood.

For observations x with multiplicities n_x, finite latent states z, model parameters eta and a positive inverse temperature beta, minimize F_beta(q,eta)=sum_x n_x*sum_z q_xz*[log q_xz-beta*log p_eta(x,z)]. For fixed eta, on positive joint support use q_xz=p_eta(x,z)^beta/sum_j p_eta(x,j)^beta. For fixed q and beta&gt;0, minimizing F_beta over eta is equivalent to maximizing the expected complete log likelihood; in PLSA this gives the usual normalized expected-count M-step with the tempered responsibilities. At beta=1 the E-step is the ordinary posterior. With 0&lt;beta&lt;1 it is flatter on its positive support. Hofmann’s inverse-annealing schedule first runs early-stopped EM at beta=1, then reduces beta multiplicatively, continues iterations while held-out performance improves, and stops decreasing beta when further improvements cease. At fixed beta, exact block updates optimize that temperature’s free energy; changing beta changes the objective. Limitations: Responsibilities require a positive finite normalizer for each observed x. At positive beta, zero latent-joint entries remain zero; the beta-to-zero limit is uniform only over the positive support. beta=0 makes the displayed parameter objective independent of eta and is not included as an ordinary M-step. This record concerns finite latent-state sums. Raising a continuous latent density to a power below one need not preserve integrability; that extension requires its own conditions. Exact block updates concern fixed-beta free energy. They do not guarantee monotonic ordinary likelihood for beta different from one, global optimality, posterior calibration or held-out improvement. Changing beta does not optimize one unchanged objective. The inverse-annealing schedule decreases beta after an ordinary-EM start and uses held-out decisions. It is not the same schedule as conventional deterministic-annealing cooling, and it is not a stochastic sampling transition with an invariant target. Schedule thresholds and multiplicative factors require an implementation choice. The source’s perplexity and retrieval comparisons concern selected historical corpora and settings. No automatic prevention of overfitting, speedup, universal benefit or author-code reproduction is claimed.

### Co-occurrence model versus document cluster and retrieval pipeline

consistency: supported. Targets: AIMech:ProbabilisticLatentSemanticAnalysis.

Retain the PLSA probability model.

A latent aspect is assigned per co-occurrence, with conditional independence of its two observed entities. Symmetric and asymmetric parameterizations agree. Document distributions are convex combinations of topic probabilities; dependent topics need not give unique mixture weights. Fold-in can estimate new-document weights, but does not supply a population prior. Optional cosine interpolation and model averaging in PLSI retrieval do not define the probability law. The finite calculation verifies normalization and one synthetic exact EM likelihood increase, without proving global optimization.

### Random document proportions and approximate posterior inference

consistency: supported. Targets: AIMech:LatentDirichletAllocation.

Retain finite-topic LDA with explicit inference qualifications.

A finite K-dimensional Dirichlet document mixture and token-specific topic assignments differ from one topic per document and fixed fitted document mixtures. Ordered-token and count masses differ by multinomial multiplicity. Tokens are exchangeable and generally dependent after integrating proportions. Conditioning on assignments gives a Dirichlet posterior; marginalizing assignments generally gives a mixture, not a Dirichlet with expected counts. Mean-field updates optimize an ELBO rather than performing exact E-steps. Infinite exchangeability and infinitely many topics are distinct. The empirical-Bayes fixed topic matrix and its separately described Bayesian extension are not conflated.

### Powered latent-joint responsibilities and temperature schedule

consistency: supported. Targets: AIMech:TemperedExpectationMaximization.

Retain tempered EM as an optimization algorithm.

For finite latent states and positive beta, powered joint probabilities minimize the stated entropy-tempered free energy, including the latent prior. The weighted complete-log-likelihood M-step agrees with ordinary EM for fixed responsibilities. Beta one recovers posterior responsibilities; beta below one flattens positive support but does not revive zero entries. Beta zero is excluded from the parameter-update claim. Fixed-beta block improvement does not imply ordinary-likelihood monotonicity at other temperatures, and changing beta changes the objective. The held-out inverse-annealing schedule is distinguished from conventional cooling, MCMC replica exchange and training-loss masks.

### Source versions, printed formulas and empirical limits

consistency: supported. Targets: AIMech:ProbabilisticLatentSemanticAnalysis, AIMech:LatentDirichletAllocation, AIMech:TemperedExpectationMaximization.

Keep source qualifications and historical evaluation limits explicit.

All 38 source pages and five specified extracted LDA pages were read. The PLSA proceedings publication is 1999, distinct from its 2013 arXiv deposit. The LDA alpha Hessian requires the corrected sign and document factor; a document-mixture prior belongs outside the token product. Fully Bayesian assignment updates use expected log topic probabilities. Finite witnesses support these qualifications without asserting unseen implementation defects. Equation (13) has the correct normalized posterior: an initial visual suspicion was withdrawn. Corpus settings and qualitative examples do not establish universal performance, exact variational inference or semantic truth.

### Directional AIO mappings and adjacent concepts

grounding: supported. Targets: AIMech:ProbabilisticLatentSemanticAnalysis, AIMech:LatentDirichletAllocation, AIMech:TemperedExpectationMaximization.

Retain all three native identities with scoped AIO mappings.

PLSA and latent Dirichlet allocation map broad to Model and related to task-scoped ProbabilisticTopicModel. TEM maps related to TrainingStrategy and MachineLearningTask because it is a specified optimization algorithm rather than a task or preprocessing stage. None is an upstream class assertion. PLSA fitted document weights, LDA random Dirichlet mixtures and TEM responsibilities/parameter updates have different mathematical roles. Biclustering, Clustering, UnsupervisedClustering and RepresentationLearning describe tasks, not these probability laws; no equivalence follows from dyadic input or dimension reduction. EnsembleLearning does not specify a within-document latent topic model. BayesianNetwork and CausalGraphicalModel do not justify causal claims. LanguageModel and factored/factorized language-model classes do not identify exchangeable count models; neural layers, autoencoders and softmax components also differ. Native SAGE combines log-frequency deviations; PoE/logarithmic pooling multiply factors rather than arithmetic topic probabilities; Replicated Softmax and DocNADE have different latent/autoregressive mechanisms. The fixed-length topic model has an explicit zero-interaction conditional reduction but a broader count-potential family, while APM averages canonical parameters. Generic/full/structured EM and mean-field records do not identify TEM’s temperature-modified objective. Simulated annealing, parallel tempering and adaptive parallel tempering use different search/sampling transitions; training signal annealing masks supervised loss instead of tempering latent responsibilities. Existing LinearDiscriminantAnalysis is a classifier despite the shared acronym. Contextual reading does not renew approval of older records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:ProbabilisticLatentSemanticAnalysis, AIMech:LatentDirichletAllocation, AIMech:TemperedExpectationMaximization. PLSA fitted document mixtures and LDA random Dirichlet mixtures define distinct probability constructions; tempered EM is an optimization procedure. Shared topic-model context does not make these equivalent. Keep model-to-task mapping direction and the classifier acronym collision explicit; no upstream AIO identity or empirical approval is inferred.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T231930Z-classical-topic-models.json | supports | Compared all 442 pinned AIO labels and scoped synonyms and 418 preceding native IDs, names and aliases. The initial normalized LDA hit denotes LinearDiscriminantAnalysis, whose full Gaussian-classifier record was read; the bare LDA alias is omitted from the new topic-model record. No normalized identity match remains for the final candidate names/aliases. Final full-checkout fixed-string searches, including ignored and hidden files in both worktree and main, return two lines each; both unique contents are existing frontier references. An additional broad LDA search returned 289 worktree and 237 main lines before the preceding batch merged; all 84 distinct contents were read, covering the existing classifier, topic-context references, unrelated programming mnemonics and namespace abbreviations. All 188 semantic label/synonym hits were read. Nineteen exact annotated AIO CLASS nodes and outgoing edges were inspected (18 verified unchanged from prior reading, Biclustering read here), along with their generated records and 16 native neighbors. The 35 contextual YAMLs were read or byte-verified after documented full reading. Absence is bounded to this snapshot, maintained corpus and inspected semantic neighborhood. |
| mapping | sources/aio/aio.json; 19 exact CLASS nodes and outgoing edges, and 188 semantic label/synonym hits in source_analysis.aio_mapping_inspection | supports | PLSA and latent Dirichlet allocation map broad to Model and related to task-scoped ProbabilisticTopicModel. TEM maps related to TrainingStrategy and MachineLearningTask because it is a specified optimization algorithm rather than a task or preprocessing stage. None is an upstream class assertion. PLSA fitted document weights, LDA random Dirichlet mixtures and TEM responsibilities/parameter updates have different mathematical roles. Biclustering, Clustering, UnsupervisedClustering and RepresentationLearning describe tasks, not these probability laws; no equivalence follows from dyadic input or dimension reduction. EnsembleLearning does not specify a within-document latent topic model. BayesianNetwork and CausalGraphicalModel do not justify causal claims. LanguageModel and factored/factorized language-model classes do not identify exchangeable count models; neural layers, autoencoders and softmax components also differ. Native SAGE combines log-frequency deviations; PoE/logarithmic pooling multiply factors rather than arithmetic topic probabilities; Replicated Softmax and DocNADE have different latent/autoregressive mechanisms. The fixed-length topic model has an explicit zero-interaction conditional reduction but a broader count-potential family, while APM averages canonical parameters. Generic/full/structured EM and mean-field records do not identify TEM’s temperature-modified objective. Simulated annealing, parallel tempering and adaptive parallel tempering use different search/sampling transitions; training signal annealing masks supervised loss instead of tempering latent responsibilities. Existing LinearDiscriminantAnalysis is a classifier despite the shared acronym. Contextual reading does not renew approval of older records. |
| neighbors | research/discovery/20261011T231930Z-classical-topic-models.json; source_analysis.aio_mapping_inspection.native_neighbors and context_reading | supports | Sixteen complete native contextual records read or byte-verified after prior full reading: EM and mean-field methods, Poisson topic models, SAGE, Replicated Softmax, DocNADE, product/logarithmic pooling, classifier LDA and annealing/tempering procedures. These distinguish model families, task names and optimization or sampling procedures. Context reading does not renew scientific approval of these earlier records. |
| finite-boundaries | research/discovery/topic-mixture-boundaries.py; Topic-mixture normalization, sequence/count multiplicity, posterior moments, PLSA EM, tempered free energy and source-expression witnesses | supports | Original finite enumeration checks normalization for document lengths 0–5, exchangeability and count multiplicity. For the same two topics, a two-token event has probability 0.343333 under Dirichlet mixing, 0.3025 under fixed weights and 0.425 under a whole-document mixture. An exact one-token posterior mixture has a different second moment from a Dirichlet with expected counts, so that substitution is not exact marginal conjugacy. Symmetric/asymmetric PLSA parameterizations agree and one synthetic exact EM update increases its likelihood. Fixed-beta TEM responsibilities minimize the stated free energy with an exact KL gap. A document-label prior placed inside every token factor sums to 0.37 instead of 1 in a witness, and finite differences confirm the corrected alpha Hessian rather than the printed sign/factor. These are curator probability calculations, not corpus experiments, global convergence proofs or author-code reproduction. |
| probabilisticlatentsemanticanalysis-source-0 | https://arxiv.org/pdf/1301.6705v1; Sections 3.1–3.3, printed pp.290–291 / PDF pp.2–3, Equations (1)–(6) and Figures 1–2; Section 3.5, pp.292–293 / PDF pp.4–5; Section 4.2, pp.294–296 / PDF pp.6–8, fold-in and retrieval distinctions | supports | Probabilistic Latent Semantic Analysis. UAI 1999, pp.289–296; arXiv:1301.6705v1 deposited 2013-01-23 via AUAI. Eight-page proceedings scan, all pages visually read. Printed page = PDF page +288. The 2013 deposit date is not the original publication date. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| probabilisticlatentsemanticanalysis-source-1 | https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf; Sections 1 and 4.3–4.4, printed pp.994,1000–1002 / PDF pp.2,8–10; Section 7.1, pp.1011–1012 / PDF pp.19–20, empirical-mixture and fold-in discussion | context_only | Latent Dirichlet Allocation. Journal of Machine Learning Research 3 (January 2003), pp.993–1022, official 30-page journal PDF. All pages visually read; extracted PDF pp.15,19,27,29,30 also inspected. Printed page = PDF page +992. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| latentdirichletallocation-source-0 | https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf; Sections 3–3.2, printed pp.996–998 / PDF pp.4–6, Equations (1)–(3); Sections 4.2–4.4, pp.1000–1002 / PDF pp.8–10; Sections 5.1–5.4, pp.1003–1007 / PDF pp.11–15, Equations (4)–(9); Appendix A.3–A.4, pp.1019–1022 / PDF pp.27–30 | supports | Latent Dirichlet Allocation. Journal of Machine Learning Research 3 (January 2003), pp.993–1022, official 30-page journal PDF. All pages visually read; extracted PDF pp.15,19,27,29,30 also inspected. Printed page = PDF page +992. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| temperedexpectationmaximization-source-0 | https://arxiv.org/pdf/1301.6705v1; Section 3.6, printed p.293 / PDF p.5, Equations (8)–(9) and four-step inverse-annealing schedule; Section 3.2, p.290 / PDF p.2, PLSA M-steps; Sections 4.1–4.2, pp.294–296 / PDF pp.6–8, held-out experiments | supports | Probabilistic Latent Semantic Analysis. UAI 1999, pp.289–296; arXiv:1301.6705v1 deposited 2013-01-23 via AUAI. Eight-page proceedings scan, all pages visually read. Printed page = PDF page +288. The 2013 deposit date is not the original publication date. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |

## Limits And Additional Notes

- Adversarial author self-review only; all records remain DRAFT.
- All 38 pages of the UAI PLSA paper and JMLR LDA paper were visually read, including figures, tables, references and appendices. Extracted LDA PDF pages 15,19,27,29,30 were also read; no full extracted-text reading is claimed.
- The UAI proceedings scan was deposited as arXiv v1 in 2013; publication remains 1999. JMLR is the 2003 journal version. Exact downloaded bytes, access times and page offsets are retained.
- The NIPS 2014 APM follow-up PDF was downloaded and extracted but remains unread; its abstract is discovery context only. Supplement access through the web tool returned an internal error. No mechanism, implementation or evaluation from that uninspected follow-up is certified.
- The LDA printed alpha Hessian and empirical-document-mixture weight position need mathematical qualification. The fully Bayesian assignment update needs expected log topic probabilities. Equation (13) correctly uses the normalized posterior; the initial visual suspicion was withdrawn after text inspection. No unseen software defect is asserted.
- Original finite enumeration checks probability normalization, token/count multiplicities, posterior moments, PLSA parameterizations, one synthetic EM update and fixed-temperature TEM free energy. These calculations are not empirical corpus fitting, author-code reproduction or universal convergence proofs.
- The two model definitions are distinct from fitting/inference algorithms. PLSA can fold in new documents; its limitation is the missing population prior for their weights, not an inability to represent them. Native LDA acronym collision was resolved by omitting that alias.
- All new records remain DRAFT, with adversarial author self-review required. Abstract-only and bibliography-derived leads remain provisional. Known in-scope leads remain; discovery is active.
- Before formal review, omitted the ambiguous LDA alias and corrected the PLSA responsibility index; final updated record bytes were inspected.
- 254 pending leads plus other unresolved dispositions remain; discovery continues.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T232435Z-classical-topic-models
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of PLSA, latent Dirichlet allocation and tempered EM
started_at: '2026-10-11T23:20:39Z'
finished_at: '2026-10-11T23:24:35Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed every field of three
    final records against all 38 PDF pages from two primary papers, plus five specified
    extracted pages. Nineteen annotated AIO nodes and 16 native neighbors inform identity
    and mapping boundaries. Original finite calculations check mixtures, posterior
    moments, EM updates, fixed-temperature free energy and displayed source expressions.
    This is author self-review, not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain PLSA, latent Dirichlet allocation and tempered EM as DRAFT concepts.
  Fitted document weights, random Dirichlet mixtures and powered latent responsibilities
  have distinct roles. Approximate inference and printed-expression limitations remain
  qualified; no actionable curation finding remains in the selected batch.
source:
  git_revision: 90838c7d687b598499646824fd12cd3bc83661fe
  state: working_tree
  inputs:
  - path: data/aio/AutoEncoderNetwork.yaml
    sha256: 7a5eb5c54dab03959ca7a19c03a4c4ece161b05618255294e61df174bcaa4521
    role: context
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/Biclustering.yaml
    sha256: 77a0695d177f5aa8f86a18d3c49010ce9c0201a93f1d95f178618fd37072353a
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/EnsembleLearning.yaml
    sha256: cf9435e5a799d84072222190c2d681c53b22bf9e7094891405008ebe398a39ed
    role: context
  - path: data/aio/FactoredLanguageModel.yaml
    sha256: d5e425f3c7cc5b57fdab859cdc777b62398077a6ac9312aef6a89af42c6eb421
    role: context
  - path: data/aio/FactorizedLLM.yaml
    sha256: f73a5e4d591e4d832f94bfa044d77c5645f585b042f07485f99920527d67b6d5
    role: context
  - path: data/aio/LanguageModel.yaml
    sha256: 67c8faa6d8ac8fb5194931f662d513d1527cefb92ab1d7c283b2c8d1ddc20c4a
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
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
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/curated/AdaptiveParallelTempering.yaml
    sha256: 8a48fc4748f3d3ae3ee1a488986db3ac1f016215ed28b78d44346a841154a919
    role: context
  - path: data/curated/AdmixtureOfPoissonMarkovRandomFields.yaml
    sha256: 1823d508528d9714392fa750a640d6c26440c82224962ac2e0e88b7d1a2e0c5c
    role: context
  - path: data/curated/DocumentNADE.yaml
    sha256: fd0969626c9aa10b8d5d876c3d537cbef1b317090c49944334e00131060b9d27
    role: context
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: context
  - path: data/curated/FixedLengthPoissonMRFTopicModel.yaml
    sha256: bf8bf0556cbeaf48e98700e462a402ce681f3dba33e31a2a256f582672187048
    role: context
  - path: data/curated/FixedLengthPoissonMarkovRandomField.yaml
    sha256: bf5c284066cbad094b3982f0b2adf8b8e67d62b697204ac7a584d7029a2e027d
    role: context
  - path: data/curated/FullyFactorizedMeanFieldInference.yaml
    sha256: 102be6f77143b26acb0d482f91e2dfa58ea113f2188b14b92067484cc4f9408d
    role: context
  - path: data/curated/LatentDirichletAllocation.yaml
    sha256: d8147371973fa1a5d5e9d3487d092e64ab70271ab42c18d199cd868bb8eb5aef
    role: target
  - path: data/curated/LinearDiscriminantAnalysis.yaml
    sha256: cb194468de3c200a57f1d6338e13b604775ce8a10b5517966459242410752b6a
    role: context
  - path: data/curated/LogarithmicOpinionPool.yaml
    sha256: bdff4b82fa80ae38dd1a1295afdf9f5c0d877632818ea25841ca7a4adce2f430
    role: context
  - path: data/curated/ParallelTempering.yaml
    sha256: e2976bcbbe756cf1b943520c6c9d739b862213c2df4ab4f2806957b67db8d0eb
    role: context
  - path: data/curated/ProbabilisticLatentSemanticAnalysis.yaml
    sha256: e9cb970e4795b65a17c073a109b4716fc42f2aa0661bf3f7be128568b19ecc71
    role: target
  - path: data/curated/ProductOfExperts.yaml
    sha256: f08d34564c86a3531094451fb045ee5d1bd20b89d3111bb68d0c19de0cf373a8
    role: context
  - path: data/curated/ReplicatedSoftmax.yaml
    sha256: 1a71debad5b7ac38c8e647ffb18c52f712300a7906b44efa5d348fb3488940cf
    role: context
  - path: data/curated/SimulatedAnnealing.yaml
    sha256: 7e77f553c8b2afc4563dc7ef6cba2b53719f22b1fd02ed37d22de9821079d42c
    role: context
  - path: data/curated/SparseAdditiveGenerativeModel.yaml
    sha256: 446900da4ecc41ccf341a27fe1f51c6a2dd2723e972bbc32a8bdb069cccdabdd
    role: context
  - path: data/curated/StructuredMeanFieldInference.yaml
    sha256: 3cd31e539123908291c2a9a394792c52dacf415ce3c19c4d6a42e9be6173c86b
    role: context
  - path: data/curated/TemperedExpectationMaximization.yaml
    sha256: 792d43ce4f38f485002b9fadbb1e9d9ac32879069cb2ec6e42b3443b57441ca5
    role: target
  - path: data/curated/TrainingSignalAnnealing.yaml
    sha256: d4450649d1cbe8afa01e72e9dddee4fe14893497a820d7a3e8089d594a9d095a
    role: context
  - path: research/discovery/20261011T231930Z-classical-topic-models.json
    sha256: b692a06cc3aab6ae9515f1c792b53e381d9ca0d8bbc1dbed70aca1736067da46
    role: context
  - path: research/discovery/topic-mixture-boundaries.py
    sha256: 27d16772d58853395f4400a67dd3e0b7c1f826ab84e11f2d1a57087e9d2113a7
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
- target_id: AIMech:ProbabilisticLatentSemanticAnalysis
  path: data/curated/ProbabilisticLatentSemanticAnalysis.yaml
  label: Probabilistic latent semantic analysis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ProbabilisticLatentSemanticAnalysis.yaml
    role: maintained
- target_id: AIMech:LatentDirichletAllocation
  path: data/curated/LatentDirichletAllocation.yaml
  label: Latent Dirichlet allocation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LatentDirichletAllocation.yaml
    role: maintained
- target_id: AIMech:TemperedExpectationMaximization
  path: data/curated/TemperedExpectationMaximization.yaml
  label: Tempered expectation maximization
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TemperedExpectationMaximization.yaml
    role: maintained
scope:
  description: All fields of two classical topic-model records and one tempered fitting
    algorithm.
  selection: Exact maintained IDs ProbabilisticLatentSemanticAnalysis, LatentDirichletAllocation
    and TemperedExpectationMaximization; complete selected batch without sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:ProbabilisticLatentSemanticAnalysis
  - AIMech:LatentDirichletAllocation
  - AIMech:TemperedExpectationMaximization
  exclusions:
  - target: Author implementations, empirical performance and exact inference
    reason: No author code, corpus fitting or benchmark ran. One finite synthetic
      EM update was calculated. The NIPS 2014 follow-up was uninspected at the discovery
      ledger cutoff and is excluded from this batch. Mathematical display checks do
      not certify unseen software or exact posterior inference.
  - target: Earlier records and reference frontier
    reason: Sixteen native contextual records inform boundaries without renewed scientific
      approval. Six additional provisional reference cohorts are explicitly enqueued;
      254 pending leads plus other unresolved dispositions remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:ProbabilisticLatentSemanticAnalysis
  - AIMech:LatentDirichletAllocation
  - AIMech:TemperedExpectationMaximization
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 128.39s (0:02:08)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 421 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 121 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 118,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:ProbabilisticLatentSemanticAnalysis
  - AIMech:LatentDirichletAllocation
  - AIMech:TemperedExpectationMaximization
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
  - AIMech:ProbabilisticLatentSemanticAnalysis
  - AIMech:LatentDirichletAllocation
  - AIMech:TemperedExpectationMaximization
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
  - AIMech:ProbabilisticLatentSemanticAnalysis
  - AIMech:LatentDirichletAllocation
  - AIMech:TemperedExpectationMaximization
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Topic-mixture normalization, posterior moments, EM updates, tempered free
    energy and source-expression checks
  command: python3 research/discovery/topic-mixture-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ProbabilisticLatentSemanticAnalysis
  - AIMech:LatentDirichletAllocation
  - AIMech:TemperedExpectationMaximization
  exit_code: 0
  expected_exit_code: 0
  summary: '{"status": "passed", "lda_normalization_lengths": [0, 1, 2, 3, 4, 5],
    "two_word_same_symbol": {"lda": 0.3433333333333334, "fixed_weights": 0.30250000000000005,
    "document_mixture": 0.42500000000000004}, "count_mass": [0.14625000000000005,
    0.29125000000000006, 0.32875000000000004, 0.23375000000000007], "posterior_second_moments":
    {"exact_mixture": 0.4393939393939394, "expected_count_dirichlet": 0.42699724517906334},
    "plsa_em_loglikelihood": [-15.296684988212109, -14.887801605993316], "tempered_responsibilities":
    {"beta1": [0.8571428571428571, 0.14285714285714285], "beta_half": [0.7101020514433644,
    0.2898979485566356]}, "tempered_kl_gap": 0.027686811684659862, "empirical_mixture_total":
    {"correct": 1.0, "literal_inside_product": 0.3699999999999999}, "alpha_hessian":
    {"derived": -1.6944444444444446, "finite_difference": -1.6944445917488338, "printed":
    2.3584133116557906}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T231930Z-classical-topic-models.json
  accessed_at: '2026-10-11T23:20:39Z'
  support: supports
  summary: Compared all 442 pinned AIO labels and scoped synonyms and 418 preceding
    native IDs, names and aliases. The initial normalized LDA hit denotes LinearDiscriminantAnalysis,
    whose full Gaussian-classifier record was read; the bare LDA alias is omitted
    from the new topic-model record. No normalized identity match remains for the
    final candidate names/aliases. Final full-checkout fixed-string searches, including
    ignored and hidden files in both worktree and main, return two lines each; both
    unique contents are existing frontier references. An additional broad LDA search
    returned 289 worktree and 237 main lines before the preceding batch merged; all
    84 distinct contents were read, covering the existing classifier, topic-context
    references, unrelated programming mnemonics and namespace abbreviations. All 188
    semantic label/synonym hits were read. Nineteen exact annotated AIO CLASS nodes
    and outgoing edges were inspected (18 verified unchanged from prior reading, Biclustering
    read here), along with their generated records and 16 native neighbors. The 35
    contextual YAMLs were read or byte-verified after documented full reading. Absence
    is bounded to this snapshot, maintained corpus and inspected semantic neighborhood.
  search_scope: Compared all 442 pinned AIO labels and scoped synonyms and 418 preceding
    native IDs, names and aliases. The initial normalized LDA hit denotes LinearDiscriminantAnalysis,
    whose full Gaussian-classifier record was read; the bare LDA alias is omitted
    from the new topic-model record. No normalized identity match remains for the
    final candidate names/aliases. Final full-checkout fixed-string searches, including
    ignored and hidden files in both worktree and main, return two lines each; both
    unique contents are existing frontier references. An additional broad LDA search
    returned 289 worktree and 237 main lines before the preceding batch merged; all
    84 distinct contents were read, covering the existing classifier, topic-context
    references, unrelated programming mnemonics and namespace abbreviations. All 188
    semantic label/synonym hits were read. Nineteen exact annotated AIO CLASS nodes
    and outgoing edges were inspected (18 verified unchanged from prior reading, Biclustering
    read here), along with their generated records and 16 native neighbors. The 35
    contextual YAMLs were read or byte-verified after documented full reading. Absence
    is bounded to this snapshot, maintained corpus and inspected semantic neighborhood.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 19 exact CLASS nodes and outgoing edges, and 188 semantic label/synonym
    hits in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T23:20:39Z'
  support: supports
  summary: PLSA and latent Dirichlet allocation map broad to Model and related to
    task-scoped ProbabilisticTopicModel. TEM maps related to TrainingStrategy and
    MachineLearningTask because it is a specified optimization algorithm rather than
    a task or preprocessing stage. None is an upstream class assertion. PLSA fitted
    document weights, LDA random Dirichlet mixtures and TEM responsibilities/parameter
    updates have different mathematical roles. Biclustering, Clustering, UnsupervisedClustering
    and RepresentationLearning describe tasks, not these probability laws; no equivalence
    follows from dyadic input or dimension reduction. EnsembleLearning does not specify
    a within-document latent topic model. BayesianNetwork and CausalGraphicalModel
    do not justify causal claims. LanguageModel and factored/factorized language-model
    classes do not identify exchangeable count models; neural layers, autoencoders
    and softmax components also differ. Native SAGE combines log-frequency deviations;
    PoE/logarithmic pooling multiply factors rather than arithmetic topic probabilities;
    Replicated Softmax and DocNADE have different latent/autoregressive mechanisms.
    The fixed-length topic model has an explicit zero-interaction conditional reduction
    but a broader count-potential family, while APM averages canonical parameters.
    Generic/full/structured EM and mean-field records do not identify TEM’s temperature-modified
    objective. Simulated annealing, parallel tempering and adaptive parallel tempering
    use different search/sampling transitions; training signal annealing masks supervised
    loss instead of tempering latent responsibilities. Existing LinearDiscriminantAnalysis
    is a classifier despite the shared acronym. Contextual reading does not renew
    approval of older records.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T231930Z-classical-topic-models.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors and context_reading
  accessed_at: '2026-10-11T23:20:39Z'
  support: supports
  summary: 'Sixteen complete native contextual records read or byte-verified after
    prior full reading: EM and mean-field methods, Poisson topic models, SAGE, Replicated
    Softmax, DocNADE, product/logarithmic pooling, classifier LDA and annealing/tempering
    procedures. These distinguish model families, task names and optimization or sampling
    procedures. Context reading does not renew scientific approval of these earlier
    records.'
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/topic-mixture-boundaries.py
  locator: Topic-mixture normalization, sequence/count multiplicity, posterior moments,
    PLSA EM, tempered free energy and source-expression witnesses
  accessed_at: '2026-10-11T23:20:39Z'
  snapshot_sha256: 27d16772d58853395f4400a67dd3e0b7c1f826ab84e11f2d1a57087e9d2113a7
  support: supports
  summary: Original finite enumeration checks normalization for document lengths 0–5,
    exchangeability and count multiplicity. For the same two topics, a two-token event
    has probability 0.343333 under Dirichlet mixing, 0.3025 under fixed weights and
    0.425 under a whole-document mixture. An exact one-token posterior mixture has
    a different second moment from a Dirichlet with expected counts, so that substitution
    is not exact marginal conjugacy. Symmetric/asymmetric PLSA parameterizations agree
    and one synthetic exact EM update increases its likelihood. Fixed-beta TEM responsibilities
    minimize the stated free energy with an exact KL gap. A document-label prior placed
    inside every token factor sums to 0.37 instead of 1 in a witness, and finite differences
    confirm the corrected alpha Hessian rather than the printed sign/factor. These
    are curator probability calculations, not corpus experiments, global convergence
    proofs or author-code reproduction.
- evidence_id: probabilisticlatentsemanticanalysis-source-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1301.6705v1
  locator: Sections 3.1–3.3, printed pp.290–291 / PDF pp.2–3, Equations (1)–(6) and
    Figures 1–2; Section 3.5, pp.292–293 / PDF pp.4–5; Section 4.2, pp.294–296 / PDF
    pp.6–8, fold-in and retrieval distinctions
  accessed_at: '2026-10-11T23:10:08Z'
  snapshot_sha256: 798ce8b95d01d76534bb4993c79f81f769b129d1493c67cac7bbc9429639c33d
  support: supports
  summary: Probabilistic Latent Semantic Analysis. UAI 1999, pp.289–296; arXiv:1301.6705v1
    deposited 2013-01-23 via AUAI. Eight-page proceedings scan, all pages visually
    read. Printed page = PDF page +288. The 2013 deposit date is not the original
    publication date. All cited method pages were visually read. The source-analysis
    notes distinguish main-paper support, discussion context, source restrictions
    and access/extraction limitations.
- evidence_id: probabilisticlatentsemanticanalysis-source-1
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf
  locator: Sections 1 and 4.3–4.4, printed pp.994,1000–1002 / PDF pp.2,8–10; Section
    7.1, pp.1011–1012 / PDF pp.19–20, empirical-mixture and fold-in discussion
  accessed_at: '2026-10-11T23:10:10Z'
  snapshot_sha256: 4667de63545b57d55d6c43e5af6f3429edfaac9472ed9eff68fdf43572735dd9
  support: context_only
  summary: Latent Dirichlet Allocation. Journal of Machine Learning Research 3 (January
    2003), pp.993–1022, official 30-page journal PDF. All pages visually read; extracted
    PDF pp.15,19,27,29,30 also inspected. Printed page = PDF page +992. All cited
    method pages were visually read. The source-analysis notes distinguish main-paper
    support, discussion context, source restrictions and access/extraction limitations.
- evidence_id: latentdirichletallocation-source-0
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf
  locator: Sections 3–3.2, printed pp.996–998 / PDF pp.4–6, Equations (1)–(3); Sections
    4.2–4.4, pp.1000–1002 / PDF pp.8–10; Sections 5.1–5.4, pp.1003–1007 / PDF pp.11–15,
    Equations (4)–(9); Appendix A.3–A.4, pp.1019–1022 / PDF pp.27–30
  accessed_at: '2026-10-11T23:10:10Z'
  snapshot_sha256: 4667de63545b57d55d6c43e5af6f3429edfaac9472ed9eff68fdf43572735dd9
  support: supports
  summary: Latent Dirichlet Allocation. Journal of Machine Learning Research 3 (January
    2003), pp.993–1022, official 30-page journal PDF. All pages visually read; extracted
    PDF pp.15,19,27,29,30 also inspected. Printed page = PDF page +992. All cited
    method pages were visually read. The source-analysis notes distinguish main-paper
    support, discussion context, source restrictions and access/extraction limitations.
- evidence_id: temperedexpectationmaximization-source-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1301.6705v1
  locator: Section 3.6, printed p.293 / PDF p.5, Equations (8)–(9) and four-step inverse-annealing
    schedule; Section 3.2, p.290 / PDF p.2, PLSA M-steps; Sections 4.1–4.2, pp.294–296
    / PDF pp.6–8, held-out experiments
  accessed_at: '2026-10-11T23:10:08Z'
  snapshot_sha256: 798ce8b95d01d76534bb4993c79f81f769b129d1493c67cac7bbc9429639c33d
  support: supports
  summary: Probabilistic Latent Semantic Analysis. UAI 1999, pp.289–296; arXiv:1301.6705v1
    deposited 2013-01-23 via AUAI. Eight-page proceedings scan, all pages visually
    read. Printed page = PDF page +288. The 2013 deposit date is not the original
    publication date. All cited method pages were visually read. The source-analysis
    notes distinguish main-paper support, discussion context, source restrictions
    and access/extraction limitations.
assessments:
- assessment_id: probabilisticlatentsemanticanalysis
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:ProbabilisticLatentSemanticAnalysis
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - probabilisticlatentsemanticanalysis-source-0
  - probabilisticlatentsemanticanalysis-source-1
  summary: PLSA denotes the aspect-model probability construction, also called the
    probabilistic latent semantic indexing model in the LDA comparison. A document
    can mix several aspects because each co-occurrence has its own latent class. It
    differs from an SVD reconstruction, a single class for a whole document, and LDA’s
    prior over document-specific topic weights. The alias PLSI identifies this underlying
    model, not every cosine, interpolation or model-averaging choice in a retrieval
    pipeline. Tempered EM is one fitting procedure rather than part of the model’s
    defining probability law. Compared all 442 pinned AIO labels and scoped synonyms
    and 418 preceding native IDs, names and aliases. The initial normalized LDA hit
    denotes LinearDiscriminantAnalysis, whose full Gaussian-classifier record was
    read; the bare LDA alias is omitted from the new topic-model record. No normalized
    identity match remains for the final candidate names/aliases. Final full-checkout
    fixed-string searches, including ignored and hidden files in both worktree and
    main, return two lines each; both unique contents are existing frontier references.
    An additional broad LDA search returned 289 worktree and 237 main lines before
    the preceding batch merged; all 84 distinct contents were read, covering the existing
    classifier, topic-context references, unrelated programming mnemonics and namespace
    abbreviations. All 188 semantic label/synonym hits were read. Nineteen exact annotated
    AIO CLASS nodes and outgoing edges were inspected (18 verified unchanged from
    prior reading, Biclustering read here), along with their generated records and
    16 native neighbors. The 35 contextual YAMLs were read or byte-verified after
    documented full reading. Absence is bounded to this snapshot, maintained corpus
    and inspected semantic neighborhood.
  details: 'For finite document indices d, vocabulary items w and K latent classes
    z, choose normalized nonnegative distributions pi_z, a_z(d) and b_z(w), and define
    p(d,w)=sum_z pi_z*a_z(d)*b_z(w). Given z, d and w are independent. Equivalently,
    for p(d)>0, p(w|d)=sum_z theta_dz*b_z(w), where theta_dz=pi_z*a_z(d)/p(d). Fit
    observed counts n(d,w) with sum_dw n(d,w)*log p(d,w). An exact EM E-step computes
    r_dwz=pi_z*a_z(d)*b_z(w)/p(d,w); M-steps normalize the corresponding count-weighted
    responsibilities over words, documents and classes. Each conditional document
    word distribution is an arithmetic convex combination of topic probabilities.
    In the original fold-in procedure, keep b_z(w) fixed and fit a new query or document’s
    mixture weights. This introduces new fitted weights rather than integrating over
    a population prior as in LDA. Limitations: The base construction is a normalized
    distribution of indexed co-occurrences. It has no LDA-style population prior on
    new document mixtures; fold-in estimation is possible, so this is not a claim
    that unseen documents cannot be represented at all. Training-document mixture
    parameters grow with the corpus. Maximum-likelihood or tempered fitting can overfit;
    local EM optimization, initialization and rank selection do not guarantee global
    optimality or unique factors. Permuting topic labels preserves the law, and linearly
    dependent topic distributions can yield nonunique mixture weights. The bag-of-words
    representation omits token order and explicit within-topic word interactions.
    It is not a raw-count Poisson MRF, a canonical-parameter admixture, or a neural
    density estimator. Topic labels and selected high-probability words are interpretations,
    not verified semantic or causal categories. Positive-count cells require positive
    modeled mass. Responsibility updates need nonzero denominators; unused components
    require a specified handling convention. Zero-count terms use the standard zero-contribution
    convention. Historical retrieval experiments use particular corpora, ranks, held-out
    tempering and cosine interpolation. No universal retrieval advantage, exact new-document
    marginal likelihood or author implementation is certified.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: Two distinct document-topic probability models and an entropy-tempered
      latent-variable fitting algorithm, with model and inference roles explicit.
    evidence_ids:
    - probabilisticlatentsemanticanalysis-source-0
    - probabilisticlatentsemanticanalysis-source-1
  - name: aio-assessment
    value: broad_match,related_match
    definition: PLSA and latent Dirichlet allocation map broad to Model and related
      to task-scoped ProbabilisticTopicModel. TEM maps related to TrainingStrategy
      and MachineLearningTask because it is a specified optimization algorithm rather
      than a task or preprocessing stage. None is an upstream class assertion. PLSA
      fitted document weights, LDA random Dirichlet mixtures and TEM responsibilities/parameter
      updates have different mathematical roles. Biclustering, Clustering, UnsupervisedClustering
      and RepresentationLearning describe tasks, not these probability laws; no equivalence
      follows from dyadic input or dimension reduction. EnsembleLearning does not
      specify a within-document latent topic model. BayesianNetwork and CausalGraphicalModel
      do not justify causal claims. LanguageModel and factored/factorized language-model
      classes do not identify exchangeable count models; neural layers, autoencoders
      and softmax components also differ. Native SAGE combines log-frequency deviations;
      PoE/logarithmic pooling multiply factors rather than arithmetic topic probabilities;
      Replicated Softmax and DocNADE have different latent/autoregressive mechanisms.
      The fixed-length topic model has an explicit zero-interaction conditional reduction
      but a broader count-potential family, while APM averages canonical parameters.
      Generic/full/structured EM and mean-field records do not identify TEM’s temperature-modified
      objective. Simulated annealing, parallel tempering and adaptive parallel tempering
      use different search/sampling transitions; training signal annealing masks supervised
      loss instead of tempering latent responsibilities. Existing LinearDiscriminantAnalysis
      is a classifier despite the shared acronym. Contextual reading does not renew
      approval of older records.
    evidence_ids:
    - mapping
- assessment_id: latentdirichletallocation
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:LatentDirichletAllocation
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - latentdirichletallocation-source-0
  summary: The defining feature is a shared prior over document-specific topic proportions
    together with repeated per-token topic selection. This differs from PLSA’s fitted
    document-index weights and a mixture selecting one topic for a whole document.
    The model is distinct from its variational EM, sampling or other inference algorithms.
    The bare LDA alias is omitted because AIMech already uses it for the unrelated
    Gaussian classifier LinearDiscriminantAnalysis. The base fixed-topic-probability
    presentation and its Bayesian topic-prior extension are distinguished explicitly.
    Compared all 442 pinned AIO labels and scoped synonyms and 418 preceding native
    IDs, names and aliases. The initial normalized LDA hit denotes LinearDiscriminantAnalysis,
    whose full Gaussian-classifier record was read; the bare LDA alias is omitted
    from the new topic-model record. No normalized identity match remains for the
    final candidate names/aliases. Final full-checkout fixed-string searches, including
    ignored and hidden files in both worktree and main, return two lines each; both
    unique contents are existing frontier references. An additional broad LDA search
    returned 289 worktree and 237 main lines before the preceding batch merged; all
    84 distinct contents were read, covering the existing classifier, topic-context
    references, unrelated programming mnemonics and namespace abbreviations. All 188
    semantic label/synonym hits were read. Nineteen exact annotated AIO CLASS nodes
    and outgoing edges were inspected (18 verified unchanged from prior reading, Biclustering
    read here), along with their generated records and 16 native neighbors. The 35
    contextual YAMLs were read or byte-verified after documented full reading. Absence
    is bounded to this snapshot, maintained corpus and inspected semantic neighborhood.
  details: 'For a fixed K, positive alpha_i and normalized topic-word probability
    rows B_i, draw theta_d~Dirichlet(alpha) independently for each document. Given
    a document length N_d, draw z_dn~Categorical(theta_d) and w_dn~Categorical(B_zdn)
    for each token. Conditional on theta_d and B, token probabilities are sum_i theta_di*B_iw
    and tokens are independent; integrating theta_d gives p(w_d|alpha,B)=integral
    Dir(theta_d;alpha)*product_n(sum_i theta_di*B_i,w_dn)dtheta_d. This is an exchangeable
    document distribution, generally with dependent tokens after integration. An unordered
    count vector additionally includes its multinomial multiplicity. The paper’s Poisson
    length law is optional to this conditional construction. For fixed B, its mean-field
    approximation is q(theta,z)=Dir(theta;gamma)*product_n Cat(z_n;phi_n), with phi_ni
    proportional B_i,w_n*exp[digamma(gamma_i)-digamma(sum_j gamma_j)] and gamma_i=alpha_i+sum_n
    phi_ni. Variational EM optimizes the evidence lower bound, updating B from expected
    topic-word counts and alpha numerically. Section 5.4 separately places Dirichlet
    priors on B; then the assignment update uses expected log topic probabilities,
    not fixed B values. Limitations: The number of topics is finite and fixed in this
    construction. Integrating a continuous Dirichlet mixture does not introduce infinitely
    many topic classes. Infinite exchangeability supports the representation discussed
    in Section 3.1; arbitrary finite exchangeability alone is not the asserted theorem.
    Given observed topic assignments, Dirichlet conjugacy is exact. With topics unobserved,
    the marginal posterior over proportions is generally not a single Dirichlet; gamma=alpha+expected
    counts is a variational update, not exact marginal conjugacy. Exact inference
    is generally difficult, and bound optimization need not monotonically improve
    the true likelihood or attain its global maximum. The basic model ignores word
    order and explicit within-topic dependencies, though integrating document proportions
    induces dependence between tokens. Zero word probabilities require smoothing or
    other support handling for novel documents. A prior over document mixtures does
    not guarantee freedom from overfitting, identifiable topics or meaningful semantic
    labels. The Bayesian topic-prior extension requires expected log topic probabilities
    in its assignment update. The appendix’s printed alpha Hessian has a sign/factor
    mismatch with the preceding gradient; the consistent Hessian is M*(trigamma(sum
    alpha)-delta_ij*trigamma(alpha_i)). This record does not adopt that printed Hessian
    as verified code. Equation (13) correctly uses the normalized posterior. The comparison’s
    empirical mixture over training-document indices must weight an entire document
    once; the printed p(d) inside its token product is not adopted. These mathematical
    qualifications do not establish an error in unseen author software or experiments.
    The source’s document, classification and recommendation experiments have distinct
    protocols. No exact likelihood replication, generic performance advantage or biological-mechanism
    conclusion is claimed. All source material concerns the specified 2003 model,
    not every later topic-model extension.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: Two distinct document-topic probability models and an entropy-tempered
      latent-variable fitting algorithm, with model and inference roles explicit.
    evidence_ids:
    - latentdirichletallocation-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: PLSA and latent Dirichlet allocation map broad to Model and related
      to task-scoped ProbabilisticTopicModel. TEM maps related to TrainingStrategy
      and MachineLearningTask because it is a specified optimization algorithm rather
      than a task or preprocessing stage. None is an upstream class assertion. PLSA
      fitted document weights, LDA random Dirichlet mixtures and TEM responsibilities/parameter
      updates have different mathematical roles. Biclustering, Clustering, UnsupervisedClustering
      and RepresentationLearning describe tasks, not these probability laws; no equivalence
      follows from dyadic input or dimension reduction. EnsembleLearning does not
      specify a within-document latent topic model. BayesianNetwork and CausalGraphicalModel
      do not justify causal claims. LanguageModel and factored/factorized language-model
      classes do not identify exchangeable count models; neural layers, autoencoders
      and softmax components also differ. Native SAGE combines log-frequency deviations;
      PoE/logarithmic pooling multiply factors rather than arithmetic topic probabilities;
      Replicated Softmax and DocNADE have different latent/autoregressive mechanisms.
      The fixed-length topic model has an explicit zero-interaction conditional reduction
      but a broader count-potential family, while APM averages canonical parameters.
      Generic/full/structured EM and mean-field records do not identify TEM’s temperature-modified
      objective. Simulated annealing, parallel tempering and adaptive parallel tempering
      use different search/sampling transitions; training signal annealing masks supervised
      loss instead of tempering latent responsibilities. Existing LinearDiscriminantAnalysis
      is a classifier despite the shared acronym. Contextual reading does not renew
      approval of older records.
    evidence_ids:
    - mapping
- assessment_id: temperedexpectationmaximization
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:TemperedExpectationMaximization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - temperedexpectationmaximization-source-0
  summary: This record denotes the deterministic free-energy fitting procedure described
    by Hofmann, with his held-out inverse-annealing schedule as an explicit realization.
    Ordinary EM is its beta=1 case. The procedure changes responsibilities and parameter
    fitting; it is neither replica-exchange MCMC nor a supervised confidence-mask
    schedule, and it does not introduce a new topic-model probability family. The
    short TEM acronym is not asserted as a globally unambiguous alias. Compared all
    442 pinned AIO labels and scoped synonyms and 418 preceding native IDs, names
    and aliases. The initial normalized LDA hit denotes LinearDiscriminantAnalysis,
    whose full Gaussian-classifier record was read; the bare LDA alias is omitted
    from the new topic-model record. No normalized identity match remains for the
    final candidate names/aliases. Final full-checkout fixed-string searches, including
    ignored and hidden files in both worktree and main, return two lines each; both
    unique contents are existing frontier references. An additional broad LDA search
    returned 289 worktree and 237 main lines before the preceding batch merged; all
    84 distinct contents were read, covering the existing classifier, topic-context
    references, unrelated programming mnemonics and namespace abbreviations. All 188
    semantic label/synonym hits were read. Nineteen exact annotated AIO CLASS nodes
    and outgoing edges were inspected (18 verified unchanged from prior reading, Biclustering
    read here), along with their generated records and 16 native neighbors. The 35
    contextual YAMLs were read or byte-verified after documented full reading. Absence
    is bounded to this snapshot, maintained corpus and inspected semantic neighborhood.
  details: 'For observations x with multiplicities n_x, finite latent states z, model
    parameters eta and a positive inverse temperature beta, minimize F_beta(q,eta)=sum_x
    n_x*sum_z q_xz*[log q_xz-beta*log p_eta(x,z)]. For fixed eta, on positive joint
    support use q_xz=p_eta(x,z)^beta/sum_j p_eta(x,j)^beta. For fixed q and beta>0,
    minimizing F_beta over eta is equivalent to maximizing the expected complete log
    likelihood; in PLSA this gives the usual normalized expected-count M-step with
    the tempered responsibilities. At beta=1 the E-step is the ordinary posterior.
    With 0<beta<1 it is flatter on its positive support. Hofmann’s inverse-annealing
    schedule first runs early-stopped EM at beta=1, then reduces beta multiplicatively,
    continues iterations while held-out performance improves, and stops decreasing
    beta when further improvements cease. At fixed beta, exact block updates optimize
    that temperature’s free energy; changing beta changes the objective. Limitations:
    Responsibilities require a positive finite normalizer for each observed x. At
    positive beta, zero latent-joint entries remain zero; the beta-to-zero limit is
    uniform only over the positive support. beta=0 makes the displayed parameter objective
    independent of eta and is not included as an ordinary M-step. This record concerns
    finite latent-state sums. Raising a continuous latent density to a power below
    one need not preserve integrability; that extension requires its own conditions.
    Exact block updates concern fixed-beta free energy. They do not guarantee monotonic
    ordinary likelihood for beta different from one, global optimality, posterior
    calibration or held-out improvement. Changing beta does not optimize one unchanged
    objective. The inverse-annealing schedule decreases beta after an ordinary-EM
    start and uses held-out decisions. It is not the same schedule as conventional
    deterministic-annealing cooling, and it is not a stochastic sampling transition
    with an invariant target. Schedule thresholds and multiplicative factors require
    an implementation choice. The source’s perplexity and retrieval comparisons concern
    selected historical corpora and settings. No automatic prevention of overfitting,
    speedup, universal benefit or author-code reproduction is claimed.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: Two distinct document-topic probability models and an entropy-tempered
      latent-variable fitting algorithm, with model and inference roles explicit.
    evidence_ids:
    - temperedexpectationmaximization-source-0
  - name: aio-assessment
    value: related_match,related_match
    definition: PLSA and latent Dirichlet allocation map broad to Model and related
      to task-scoped ProbabilisticTopicModel. TEM maps related to TrainingStrategy
      and MachineLearningTask because it is a specified optimization algorithm rather
      than a task or preprocessing stage. None is an upstream class assertion. PLSA
      fitted document weights, LDA random Dirichlet mixtures and TEM responsibilities/parameter
      updates have different mathematical roles. Biclustering, Clustering, UnsupervisedClustering
      and RepresentationLearning describe tasks, not these probability laws; no equivalence
      follows from dyadic input or dimension reduction. EnsembleLearning does not
      specify a within-document latent topic model. BayesianNetwork and CausalGraphicalModel
      do not justify causal claims. LanguageModel and factored/factorized language-model
      classes do not identify exchangeable count models; neural layers, autoencoders
      and softmax components also differ. Native SAGE combines log-frequency deviations;
      PoE/logarithmic pooling multiply factors rather than arithmetic topic probabilities;
      Replicated Softmax and DocNADE have different latent/autoregressive mechanisms.
      The fixed-length topic model has an explicit zero-interaction conditional reduction
      but a broader count-potential family, while APM averages canonical parameters.
      Generic/full/structured EM and mean-field records do not identify TEM’s temperature-modified
      objective. Simulated annealing, parallel tempering and adaptive parallel tempering
      use different search/sampling transitions; training signal annealing masks supervised
      loss instead of tempering latent responsibilities. Existing LinearDiscriminantAnalysis
      is a classifier despite the shared acronym. Contextual reading does not renew
      approval of older records.
    evidence_ids:
    - mapping
- assessment_id: plsa-boundary
  area: consistency
  topic: Co-occurrence model versus document cluster and retrieval pipeline
  outcome: supported
  target_ids:
  - AIMech:ProbabilisticLatentSemanticAnalysis
  evidence_ids:
  - probabilisticlatentsemanticanalysis-source-0
  - probabilisticlatentsemanticanalysis-source-1
  - finite-boundaries
  - neighbors
  summary: Retain the PLSA probability model.
  details: A latent aspect is assigned per co-occurrence, with conditional independence
    of its two observed entities. Symmetric and asymmetric parameterizations agree.
    Document distributions are convex combinations of topic probabilities; dependent
    topics need not give unique mixture weights. Fold-in can estimate new-document
    weights, but does not supply a population prior. Optional cosine interpolation
    and model averaging in PLSI retrieval do not define the probability law. The finite
    calculation verifies normalization and one synthetic exact EM likelihood increase,
    without proving global optimization.
- assessment_id: lda-boundary
  area: consistency
  topic: Random document proportions and approximate posterior inference
  outcome: supported
  target_ids:
  - AIMech:LatentDirichletAllocation
  evidence_ids:
  - latentdirichletallocation-source-0
  - finite-boundaries
  - neighbors
  summary: Retain finite-topic LDA with explicit inference qualifications.
  details: A finite K-dimensional Dirichlet document mixture and token-specific topic
    assignments differ from one topic per document and fixed fitted document mixtures.
    Ordered-token and count masses differ by multinomial multiplicity. Tokens are
    exchangeable and generally dependent after integrating proportions. Conditioning
    on assignments gives a Dirichlet posterior; marginalizing assignments generally
    gives a mixture, not a Dirichlet with expected counts. Mean-field updates optimize
    an ELBO rather than performing exact E-steps. Infinite exchangeability and infinitely
    many topics are distinct. The empirical-Bayes fixed topic matrix and its separately
    described Bayesian extension are not conflated.
- assessment_id: tempered-em-boundary
  area: consistency
  topic: Powered latent-joint responsibilities and temperature schedule
  outcome: supported
  target_ids:
  - AIMech:TemperedExpectationMaximization
  evidence_ids:
  - temperedexpectationmaximization-source-0
  - finite-boundaries
  - neighbors
  summary: Retain tempered EM as an optimization algorithm.
  details: For finite latent states and positive beta, powered joint probabilities
    minimize the stated entropy-tempered free energy, including the latent prior.
    The weighted complete-log-likelihood M-step agrees with ordinary EM for fixed
    responsibilities. Beta one recovers posterior responsibilities; beta below one
    flattens positive support but does not revive zero entries. Beta zero is excluded
    from the parameter-update claim. Fixed-beta block improvement does not imply ordinary-likelihood
    monotonicity at other temperatures, and changing beta changes the objective. The
    held-out inverse-annealing schedule is distinguished from conventional cooling,
    MCMC replica exchange and training-loss masks.
- assessment_id: evidence-and-estimation
  area: consistency
  topic: Source versions, printed formulas and empirical limits
  outcome: supported
  target_ids:
  - AIMech:ProbabilisticLatentSemanticAnalysis
  - AIMech:LatentDirichletAllocation
  - AIMech:TemperedExpectationMaximization
  evidence_ids:
  - finite-boundaries
  - latentdirichletallocation-source-0
  - probabilisticlatentsemanticanalysis-source-0
  summary: Keep source qualifications and historical evaluation limits explicit.
  details: 'All 38 source pages and five specified extracted LDA pages were read.
    The PLSA proceedings publication is 1999, distinct from its 2013 arXiv deposit.
    The LDA alpha Hessian requires the corrected sign and document factor; a document-mixture
    prior belongs outside the token product. Fully Bayesian assignment updates use
    expected log topic probabilities. Finite witnesses support these qualifications
    without asserting unseen implementation defects. Equation (13) has the correct
    normalized posterior: an initial visual suspicion was withdrawn. Corpus settings
    and qualitative examples do not establish universal performance, exact variational
    inference or semantic truth.'
- assessment_id: mapping-boundary
  area: grounding
  topic: Directional AIO mappings and adjacent concepts
  outcome: supported
  target_ids:
  - AIMech:ProbabilisticLatentSemanticAnalysis
  - AIMech:LatentDirichletAllocation
  - AIMech:TemperedExpectationMaximization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain all three native identities with scoped AIO mappings.
  details: PLSA and latent Dirichlet allocation map broad to Model and related to
    task-scoped ProbabilisticTopicModel. TEM maps related to TrainingStrategy and
    MachineLearningTask because it is a specified optimization algorithm rather than
    a task or preprocessing stage. None is an upstream class assertion. PLSA fitted
    document weights, LDA random Dirichlet mixtures and TEM responsibilities/parameter
    updates have different mathematical roles. Biclustering, Clustering, UnsupervisedClustering
    and RepresentationLearning describe tasks, not these probability laws; no equivalence
    follows from dyadic input or dimension reduction. EnsembleLearning does not specify
    a within-document latent topic model. BayesianNetwork and CausalGraphicalModel
    do not justify causal claims. LanguageModel and factored/factorized language-model
    classes do not identify exchangeable count models; neural layers, autoencoders
    and softmax components also differ. Native SAGE combines log-frequency deviations;
    PoE/logarithmic pooling multiply factors rather than arithmetic topic probabilities;
    Replicated Softmax and DocNADE have different latent/autoregressive mechanisms.
    The fixed-length topic model has an explicit zero-interaction conditional reduction
    but a broader count-potential family, while APM averages canonical parameters.
    Generic/full/structured EM and mean-field records do not identify TEM’s temperature-modified
    objective. Simulated annealing, parallel tempering and adaptive parallel tempering
    use different search/sampling transitions; training signal annealing masks supervised
    loss instead of tempering latent responsibilities. Existing LinearDiscriminantAnalysis
    is a classifier despite the shared acronym. Contextual reading does not renew
    approval of older records.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:ProbabilisticLatentSemanticAnalysis
  - AIMech:LatentDirichletAllocation
  - AIMech:TemperedExpectationMaximization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - probabilisticlatentsemanticanalysis-source-0
  - probabilisticlatentsemanticanalysis-source-1
  - latentdirichletallocation-source-0
  - temperedexpectationmaximization-source-0
  rationale: PLSA fitted document mixtures and LDA random Dirichlet mixtures define
    distinct probability constructions; tempered EM is an optimization procedure.
    Shared topic-model context does not make these equivalent. Keep model-to-task
    mapping direction and the classifier acronym collision explicit; no upstream AIO
    identity or empirical approval is inferred.
limitations:
- Adversarial author self-review only; all records remain DRAFT.
- All 38 pages of the UAI PLSA paper and JMLR LDA paper were visually read, including
  figures, tables, references and appendices. Extracted LDA PDF pages 15,19,27,29,30
  were also read; no full extracted-text reading is claimed.
- The UAI proceedings scan was deposited as arXiv v1 in 2013; publication remains
  1999. JMLR is the 2003 journal version. Exact downloaded bytes, access times and
  page offsets are retained.
- The NIPS 2014 APM follow-up PDF was downloaded and extracted but remains unread;
  its abstract is discovery context only. Supplement access through the web tool returned
  an internal error. No mechanism, implementation or evaluation from that uninspected
  follow-up is certified.
- The LDA printed alpha Hessian and empirical-document-mixture weight position need
  mathematical qualification. The fully Bayesian assignment update needs expected
  log topic probabilities. Equation (13) correctly uses the normalized posterior;
  the initial visual suspicion was withdrawn after text inspection. No unseen software
  defect is asserted.
- Original finite enumeration checks probability normalization, token/count multiplicities,
  posterior moments, PLSA parameterizations, one synthetic EM update and fixed-temperature
  TEM free energy. These calculations are not empirical corpus fitting, author-code
  reproduction or universal convergence proofs.
- The two model definitions are distinct from fitting/inference algorithms. PLSA can
  fold in new documents; its limitation is the missing population prior for their
  weights, not an inability to represent them. Native LDA acronym collision was resolved
  by omitting that alias.
- All new records remain DRAFT, with adversarial author self-review required. Abstract-only
  and bibliography-derived leads remain provisional. Known in-scope leads remain;
  discovery is active.
- Before formal review, omitted the ambiguous LDA alias and corrected the PLSA responsibility
  index; final updated record bytes were inspected.
- 254 pending leads plus other unresolved dispositions remain; discovery continues.
links: []
tags:
- native-concepts
- classical-topic-models
- self-review
- discovery-ongoing
```
