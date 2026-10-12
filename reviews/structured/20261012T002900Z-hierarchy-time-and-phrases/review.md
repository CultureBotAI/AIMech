# Scientific self-review of DAG, continuous-time and phrase topic models

- Review: 20261012T002900Z-hierarchy-time-and-phrases
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T00:25:04Z
- Finished UTC: 2026-10-12T00:29:00Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain three DRAFT model families for DAG topic paths, continuous timestamp factors and topic-dependent phrase gates. Explicit qualifications preserve shared-parameter scope, alternate generative laws, approximate fitting and printed-equation boundaries. No actionable curation finding remains in this selected cohort.

## Scope And Provenance

All fields of three maintained probability-model records.

Selection: Exact maintained IDs PachinkoAllocationModel, TopicsOverTimeModel and TopicalNGramModel; complete selected cohort without sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base a43f98de507150660ac211ada935c0d7bdaccfe9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:PachinkoAllocationModel | data/curated/PachinkoAllocationModel.yaml | maintained | Pachinko allocation model |
| AIMech:TopicsOverTimeModel | data/curated/TopicsOverTimeModel.yaml | maintained | Topics over Time model |
| AIMech:TopicalNGramModel | data/curated/TopicalNGramModel.yaml | maintained | Topical n-gram model |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:PachinkoAllocationModel, AIMech:TopicsOverTimeModel, AIMech:TopicalNGramModel | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 141.61s (0:02:21)<br>Checked 442 record(s); 0 failed.<br>Checked 435 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 126 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 123,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:PachinkoAllocationModel, AIMech:TopicsOverTimeModel, AIMech:TopicalNGramModel | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:PachinkoAllocationModel, AIMech:TopicsOverTimeModel, AIMech:TopicalNGramModel | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:PachinkoAllocationModel, AIMech:TopicsOverTimeModel, AIMech:TopicalNGramModel | Command exited 0 with no output. |
| Hierarchy, timestamp and phrase probability boundaries | passed | True | AIMech:PachinkoAllocationModel, AIMech:TopicsOverTimeModel, AIMech:TopicalNGramModel | {"pam_assignment_states": 64, "pam_conditional_checks": 192, "pam_maximum_conditional_error": 4.440892098500626e-16, "positive_shared_parent_covariance": 0.01686507936507957, "tot_single_timestamp_joint": 0.25, "tot_repeated_timestamp_joint": 0.16000000000000003, "tot_inverse_length_tempered_joint": 0.2, "tot_repeated_diagonal_integral": 0.16666666666666666, "tot_single_time_word_mass": 0.25, "beta_consistent_mean": 0.2, "beta_reversed_display_mean": 0.8, "token_topic_given_time": 0.8, "document_mixture_posterior_mean": 0.6, "tng_correct_topic_conditional": [0.6666666666666666, 0.3333333333333334], "tng_without_next_gate": [0.5714285714285715, 0.4285714285714286], "scope": "Finite synthetic checks and counterexamples, not author-code execution or benchmark reproduction."} |

## Scientific And Domain Assessments

### Identity, model definition, inference interpretation, limitations and mappings

evidence: supported. Targets: AIMech:PachinkoAllocationModel.

Scoped to Li and McCallum's PAM construction, with Dirichlet child-distribution priors and the four-level experimental variant in ICML2006. Interior topics can have multiple parents, and paths may skip levels. A new path is selected for each token. This differs from a single topic path assigned to an entire document, a logistic-normal topic mixture, or a causal graph of semantic concepts. PAM is a source acronym within this scope; later hierarchical, nonparametric and scalable variants are not asserted as exact aliases. No normalized candidate identity matched all 442 pinned AIO IDs, labels and scoped synonyms or 432 preceding native IDs, names and aliases. Full-checkout searches included ignored and hidden files in both checkouts; six matching lines per checkout came from three unique file contents containing prior frontier leads, bibliography context and a cached publication-list mention. All candidate-matching excerpts were read; the long cached browser transcript was not reread in full. All 205 semantic label/synonym hits were byte-verified unchanged from prior reading. Eighteen annotated AIO CLASS nodes and outgoing edges comprise 17 verified prior inspections and one fresh reading. Twenty-seven contextual YAMLs comprise 25 unchanged prior readings, one fresh generated AIO reading and one final round102 native record verified against its fully read review inputs. No candidate record is present within this bounded pinned-snapshot and maintained-corpus search.

In the general Dirichlet formulation, each document draws a categorical child vector for each interior node. Each token starts at the root and repeatedly chooses a child until it reaches a word leaf. The finite rooted DAG and reachable word leaves ensure termination. In the demonstrated four-level variant, root-to-supertopic and supertopic-to-subtopic vectors vary per document, while subtopic-to-word vectors are drawn once and shared across the corpus. The latter sharing changes corpus marginalization: shared random emissions must be integrated jointly. The product of separately marginalized documents written for the fully document-local formulation is not automatically the marginal law of this shared-emission variant. For fixed positive hyperparameters in the four-level variant, a token's collapsed supertopic/subtopic weight multiplies three leave-one-out predictive factors: the document root-to-supertopic count, the document supertopic-to-subtopic count, and the corpus subtopic-to-word count, each smoothed and normalized by its Dirichlet prior. The source jointly samples both topic levels. Its experimental fitting also changes supertopic hyperparameters using smoothed empirical moments and a concentration heuristic, rather than exact maximum likelihood or MAP. That changing-parameter procedure is not simply fixed-target posterior Gibbs sampling; neither finite samples nor moment updates establish convergence or optimality. Limitations: The experiments fix a fully connected four-level structure and topic counts. Learning arbitrary DAG structure or a nonparametric number of nodes is prospective in this paper. A DAG can encode nested and overlapping mixtures without establishing a universal representation theorem for every correlation structure. Dirichlet topic proportions are compositionally dependent, with negative off-diagonal covariances; the introductory LDA-independence contrast is not literal independence. Logistic-normal covariance parameters likewise do not mean higher-order dependence vanishes. PAM supplies a different mixing construction, not proof that CTM is exactly equivalent to a two-child DAG. Moment updates require policies for unvisited parent nodes, zero or invalid variances and nonpositive concentration estimates. Smoothing child means alone does not specify all edge cases. LDA reductions require compatible shared or fixed emissions; redrawing every word-emission vector independently per document is a different model. Evidence includes selected topics, a small human-judgment study, approximate held-out likelihood and five-way newsgroup classification. The prose and Table 2 disagree on majority-vote counts. The generated-document likelihood approximation is not exact marginal likelihood, and the reported results do not establish universal superiority. No author code or benchmark was executed.

### Identity, model definition, inference interpretation, limitations and mappings

evidence: supported. Targets: AIMech:TopicsOverTimeModel.

Scoped to Wang and McCallum's KDD2006 Topics over Time model, especially its fitted token-level timestamp construction with Beta densities over normalized time. The paper also proposes a distinct single-document-timestamp view. Fixed topic-word distributions distinguish TOT from dynamic topic models with evolving word probabilities; continuous observed time does not imply a Markov process or point-process intensity. TOT is a source acronym within this scope. No normalized candidate identity matched all 442 pinned AIO IDs, labels and scoped synonyms or 432 preceding native IDs, names and aliases. Full-checkout searches included ignored and hidden files in both checkouts; six matching lines per checkout came from three unique file contents containing prior frontier leads, bibliography context and a cached publication-list mention. All candidate-matching excerpts were read; the long cached browser transcript was not reread in full. All 205 semantic label/synonym hits were byte-verified unchanged from prior reading. Eighteen annotated AIO CLASS nodes and outgoing edges comprise 17 verified prior inspections and one fresh reading. Twenty-seven contextual YAMLs comprise 25 unchanged prior readings, one fresh generated AIO reading and one final round102 native record verified against its fully read review inputs. No candidate record is present within this bounded pinned-snapshot and maintained-corpus search.

The fitted construction gives each document a Dirichlet topic mixture, each topic a corpus-shared categorical word vector, and each topic a Beta timestamp density on a normalized bounded interval. A token draws a topic, a word and a timestamp; fitting copies the document timestamp to every token. Word distributions remain fixed across time, while topic-specific time densities influence assignment. The alternative description generates one timestamp from a document-mixture-weighted combination of topic densities. These are different generative laws: repeating topic-time factors, even with inverse-length weighting, is not generally identical to one mixture density for a document timestamp. With topic timestamp parameters fixed, the collapsed token assignment weight combines leave-one-out document-topic and topic-word predictive factors with the assigned topic's timestamp density. The paper introduces an exponent to balance time and word contributions and updates Beta parameters from empirical moments. These adaptations change the fitting objective and require positive valid shapes and safeguards for empty topics or zero variance. The printed density uses (1-t)^(psi1-1)*t^(psi2-1), whereas its moment estimates assign psi1=mean*c and psi2=(1-mean)*c. A coherent calculation must use one consistent shape convention; for the conventional Beta(a,b), the density is proportional to t^(a-1)*(1-t)^(b-1). No behavior of uninspected historical software is inferred from this notation conflict. Limitations: A repeated timestamp provides one density factor per token unless explicitly reweighted. Its restriction to one common timestamp is not automatically a normalized single-time document density. The proposed balancing exponent does not prove equivalence between the two generative descriptions. Bayes inversion can produce a token-topic probability given time using an assumed or estimated topic prior. This is not generally the same quantity as the posterior mean of a random document topic vector, despite notation on p.4. Continuous density values are not probabilities; endpoint handling, normalization range and balancing conventions matter. One Beta per topic limits temporal shapes. Extending the bounded time range for prediction is a modeling choice rather than a guarantee of future extrapolation. Fixed word distributions do not directly model changing word meanings, and topic split/merge interpretations are descriptive. Historical evaluations use selected address, email and NIPS collections with heuristic preprocessing and particular finite samples. Topic names, KL distinctness, thresholded co-occurrence and decade prediction do not establish causal trends, universal semantic accuracy or future forecasting. No author code or benchmark was executed.

### Identity, model definition, inference interpretation, limitations and mappings

evidence: supported. Targets: AIMech:TopicalNGramModel.

Scoped to Wang, McCallum and Wei's ICDM2007 TNG model in Figure 1(c). The Bernoulli gate uses the previous token's topic and word; the emission uses the current topic. Consecutive bigram choices form longer phrases, but the local generative law remains first order. This differs from the always-bigram topic model, the topic-independent LDA collocation components and generic tokenization. TNG is the source acronym. Topic assignments need not be identical within an extracted phrase. No normalized candidate identity matched all 442 pinned AIO IDs, labels and scoped synonyms or 432 preceding native IDs, names and aliases. Full-checkout searches included ignored and hidden files in both checkouts; six matching lines per checkout came from three unique file contents containing prior frontier leads, bibliography context and a cached publication-list mention. All candidate-matching excerpts were read; the long cached browser transcript was not reread in full. All 205 semantic label/synonym hits were byte-verified unchanged from prior reading. Eighteen annotated AIO CLASS nodes and outgoing edges comprise 17 verified prior inspections and one fresh reading. Twenty-seven contextual YAMLs comprise 25 unchanged prior readings, one fresh generated AIO reading and one final round102 native record verified against its fully read review inputs. No candidate record is present within this bounded pinned-snapshot and maintained-corpus search.

Each document has a Dirichlet topic vector theta. Each topic has a categorical unigram vector phi, each topic/previous-word pair has a categorical bigram vector sigma, and each previous-topic/previous-word pair has a Bernoulli gate psi with a Beta prior. At position i, x_i is drawn from psi_(z_(i-1),w_(i-1)), z_i from theta, and w_i from phi_z_i if x_i=0 or sigma_(z_i,w_(i-1)) if x_i=1. Initial and other specified boundaries constrain gates to unigrams. Runs of bigram choices induce phrases; the paper labels a phrase by its last word's topic as an output convention. This does not impose a shared latent topic across the phrase. The generative law makes z_i a parent of the next gate x_(i+1). Consequently a topic update conditioned on the other assignments must account for that outgoing gate as well as the current emission and document mixture. The full joint in Appendix A includes those factors, but the printed joint/topic conditional displays on pp.4 and10 omit the next-gate contribution. A collapsed implementation must remove all affected factors and preserve shared-parameter count corrections before evaluating candidates. A finite integrated example yields a topic conditional of (2/3,1/3), whereas dropping that contribution gives (4/7,3/7). This qualifies the printed inference expression, without asserting that uninspected author software used it. Limitations: The model represents long phrases through successive first-order bigrams, not an unrestricted higher-order n-gram table. Fixed topic count, vocabulary, boundary rules and many topic/word parameter rows constrain the model and require smoothing. The optional same-topic phrase modification on p.4 has an if/else inconsistent with its verbal intention. The record follows the main Figure 1(c) construction. Printed minus-one counts must be interpreted as removing the old assignment, not subtracting one from every candidate category. The retrieval section uses a plug-in first-order query score that averages the previous-topic gate under document weights. It is not generally exact filtering or posterior prediction for the full latent sequence. Query-level mixture and term-level interpolation are different scoring rules; the reported study uses term-level interpolation. The NIPS/TREC experiments use selected preparations, fixed hyperparameters and model-specific interpolation weights selected for best performance. Topic/phrase labels and retrieval comparisons do not establish linguistic ground truth or universal superiority. The finite counterexample audits a printed equation, not source implementation or benchmark execution.

### Per-token DAG paths, shared emissions and fitted hyperparameters

consistency: supported. Targets: AIMech:PachinkoAllocationModel.

Retain PAM with distinct general and four-level scopes.

The general formulation redraws child distributions by document, whereas four-level PAM shares subtopic word vectors across the corpus. A 64-state example verifies 192 collapsed path conditionals to 4.5e-16. Shared parent mass can give positive covariance between child topics, but broad correlation rhetoric does not establish universal expressivity or independence in LDA. The source fixes graph structure and uses moment heuristics with unresolved numerical edge policies. Its human-vote table and prose disagree, so no disputed count is adopted.

### Repeated token timestamps, single-time mixtures and Beta convention

consistency: supported. Targets: AIMech:TopicsOverTimeModel.

Retain TOT while distinguishing its two generative descriptions.

A two-topic example gives joint densities0.25 for one mixture timestamp,0.16 for repeated token factors and0.2 after inverse-length tempering. Restricting repeated times to one diagonal integrates to1/6 instead of word mass1/4. The displayed Beta exponent order conflicts with moment-shape assignments: the consistent mean0.2 becomes0.8 if reversed. A token-topic conditional0.8 also differs from document-mixture posterior mean0.6. These counterexamples qualify source equivalence/notation claims without alleging historical implementation failure.

### Previous-topic phrase gates and outgoing conditional dependence

consistency: supported. Targets: AIMech:TopicalNGramModel.

Retain the TNG generative law with a qualified printed update.

The previous topic and word determine the current gate, while the current topic determines emission. Thus a topic update influences the next gate. The full integrated joint gives a three-token conditional(2/3,1/3), whereas omitting that factor gives(4/7,3/7). The printed topic update is incomplete for general conditioned sequences; correct collapsed updates must account for all affected gate counts. The optional same-topic if/else and plug-in first-order query score are separately qualified. Longer extracted phrases do not make the model an unrestricted higher-order n-gram law.

### Exact publication versions and bounded empirical evidence

consistency: supported. Targets: AIMech:PachinkoAllocationModel, AIMech:TopicsOverTimeModel, AIMech:TopicalNGramModel.

Preserve all three fully inspected primary conference versions.

All28 pages of ICML2006 PAM, KDD2006 TOT and ICDM2007 TNG were visually read. Locators use PDF pages; later PAM variants and the earlier TNG technical report are not current mechanism evidence. Selected topic examples, approximate likelihoods, timestamp prediction and tuned retrieval comparisons do not establish universal superiority, causal interpretation or code reproduction. Native composite HMM-topic coverage is recognized when the TNG source calls it HMMLDA, without a duplicate addition or modification of its immutable prior review.

### Model/task mapping direction and neighboring constructions

grounding: supported. Targets: AIMech:PachinkoAllocationModel, AIMech:TopicsOverTimeModel, AIMech:TopicalNGramModel.

Retain three distinct native model families.

PAM and TOT map broadly to AIO Model; TNG maps broadly to LanguageModel because it defines a word-sequence law. All map related to task-scoped ProbabilisticTopicModel, and TOT additionally maps related to TimeSeriesAnalysis. HierarchicalLanguageModel and FactoredLanguageModel are broader neighboring descriptions, not exact PAM/TNG identities. PAM routing DAGs do not establish CausalGraphicalModel; general graphical and Bayesian-network categories do not replace source-specific mechanisms. TOT uses observed continuous timestamps, not a Markov state trajectory or guaranteed TimeSeriesForecasting method. TNG phrase gates differ from Tokenization, SubwordSegmentation and TextVectorizationLayer. The pinned RepresentationLearning class is a deep-neural-network subclass and is not justified merely by classical latent features. LDA, PLSA, CTM, DTM, author-topic and composite HMM-topic records, together with Gibbs/EM/tempered EM, provide contextual boundaries without renewed scientific approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:PachinkoAllocationModel, AIMech:TopicsOverTimeModel, AIMech:TopicalNGramModel. DAG path mixing, continuous timestamp factors and topic-dependent sequence gates are distinct model structures. Broad Model or LanguageModel and related topic/time-analysis mappings preserve AIO abstraction without forcing exact matches.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T002440Z-hierarchy-time-and-phrases.json | supports | No normalized candidate identity matched all 442 pinned AIO IDs, labels and scoped synonyms or 432 preceding native IDs, names and aliases. Full-checkout searches included ignored and hidden files in both checkouts; six matching lines per checkout came from three unique file contents containing prior frontier leads, bibliography context and a cached publication-list mention. All candidate-matching excerpts were read; the long cached browser transcript was not reread in full. All 205 semantic label/synonym hits were byte-verified unchanged from prior reading. Eighteen annotated AIO CLASS nodes and outgoing edges comprise 17 verified prior inspections and one fresh reading. Twenty-seven contextual YAMLs comprise 25 unchanged prior readings, one fresh generated AIO reading and one final round102 native record verified against its fully read review inputs. No candidate record is present within this bounded pinned-snapshot and maintained-corpus search. |
| mapping | sources/aio/aio.json; 18 exact annotated CLASS nodes and outgoing edges, 17 unchanged and one freshly read; all 205 label/synonym hits verified unchanged | supports | PAM and TOT map broadly to AIO Model; TNG maps broadly to LanguageModel because it defines a word-sequence law. All map related to task-scoped ProbabilisticTopicModel, and TOT additionally maps related to TimeSeriesAnalysis. HierarchicalLanguageModel and FactoredLanguageModel are broader neighboring descriptions, not exact PAM/TNG identities. PAM routing DAGs do not establish CausalGraphicalModel; general graphical and Bayesian-network categories do not replace source-specific mechanisms. TOT uses observed continuous timestamps, not a Markov state trajectory or guaranteed TimeSeriesForecasting method. TNG phrase gates differ from Tokenization, SubwordSegmentation and TextVectorizationLayer. The pinned RepresentationLearning class is a deep-neural-network subclass and is not justified merely by classical latent features. LDA, PLSA, CTM, DTM, author-topic and composite HMM-topic records, together with Gibbs/EM/tempered EM, provide contextual boundaries without renewed scientific approval. |
| neighbors | research/discovery/20261012T002440Z-hierarchy-time-and-phrases.json; Nine native neighbors and 18 generated contextual YAMLs in source_analysis.context_reading | supports | Native LDA, PLSA, CTM, DTM, author-topic, composite HMM-topic, Gibbs, EM and tempered EM records inform identity distinctions. Twenty-five contextual files are unchanged from prior readings; one generated AIO record was freshly read and one round102 native record matches fully read final review inputs. No contextual record receives renewed scientific approval. |
| finite-boundaries | research/discovery/hierarchy-time-phrase-boundaries.py; PAM collapsed path probabilities, timestamp model/shape distinctions and TNG next-gate dependence | supports | A 64-state four-level PAM example verifies 192 collapsed path conditionals against integrated joint ratios and exhibits positive child-topic covariance from shared parent mass. A two-topic TOT example distinguishes a single timestamp mixture (joint density0.25) from repeated token timestamp factors (0.16) and inverse-length tempering (0.2); its repeated diagonal integrates to1/6 rather than word mass1/4. Consistent Beta moment shapes have mean0.2 while the reversed printed convention gives0.8. Token-topic Bayes inversion0.8 differs from document-mixture posterior mean0.6. A three-token TNG integrated joint gives topic conditional(2/3,1/3), while omitting the next-gate factor gives(4/7,3/7). These are finite curator checks/counterexamples, not author-code or empirical reproduction. |
| pachinkoallocationmodel-source-0 | https://people.cs.umass.edu/~mccallum/papers/pam-icml06.pdf; Section 2, PDF p.3, document/corpus probability displays; Section 2.1 pp.3-4 and Figure 2; Section 2.2, PDF p.4, collapsed update and moment-based parameter estimates; Sections 1-2, PDF pp.2-3, Figure 1 and generative process | supports | Pachinko Allocation: DAG-Structured Mixture Models of Topic Correlations. Author-hosted eight-page ICML2006 paper; all pages visually read. No numeric printed page labels are visible, so locators use PDF pages. Later hierarchical, nonparametric and scalable PAM papers are separate versions/extensions. All pages of the primary PDF were visually read. Curator qualifications and synthetic calculations are distinguished from historical empirical claims and uninspected implementations. |
| topicsovertimemodel-source-0 | https://people.cs.umass.edu/~mccallum/papers/tot-kdd06.pdf; Section 2, PDF pp.2-4, Figure 1(b,c), generative steps and alternative description; Section 2, PDF pp.3-4, conditional and Algorithm 1; Appendix A p.10, density and moment estimates; Sections 1-2, PDF pp.1-4, Figure 1 and token-level generative process | supports | Topics over Time: A Non-Markov Continuous-Time Model of Topical Trends. Author-hosted ten-page KDD2006 paper, including Appendix A on p.10; all pages visually read. No numeric printed page labels visible; locators use PDF pages. All pages of the primary PDF were visually read. Curator qualifications and synthetic calculations are distinguished from historical empirical claims and uninspected implementations. |
| topicalngrammodel-source-0 | https://people.cs.umass.edu/~mccallum/papers/tng-icdm07.pdf; Figure 1(c), PDF p.3; Section 2.3 p.4; Appendix A joint p.9 and conditionals p.10; Section 2.3, PDF pp.3-4, Figure 1(c) and generative steps; Sections 2.2-2.3, PDF pp.2-4, boundary handling, Figure 1(c) and topic-consistency discussion | supports | Topical N-grams: Phrase and Topic Discovery, with an Application to Information Retrieval. Author-hosted ten-page ICDM2007 paper, including Appendix A pp.9-10; all pages visually read. No numeric printed page labels visible; locators use PDF pages. The earlier 2005 technical report was located but not read or substituted for this version. All pages of the primary PDF were visually read. Curator qualifications and synthetic calculations are distinguished from historical empirical claims and uninspected implementations. |

## Limits And Additional Notes

- Adversarial author self-review only; all three records remain DRAFT.
- All 28 pages of three author-hosted conference PDFs were visually read, including equations, figures, tables and bibliographies. Locators use PDF pages because no numeric printed page labels were visible. No extracted-text reading or author-code execution is asserted.
- PAM is the ICML2006 version, TOT is KDD2006 and TNG is ICDM2007. Later PAM extensions and the earlier TNG technical report were located but not read as current mechanism evidence.
- PAM separates the general document-local formulation from corpus-shared emissions in its four-level variant. Moment heuristics and fixed structures are not exact parameter inference or automatic structure learning. Source human-vote totals are inconsistent; no disputed count is adopted.
- TOT has distinct token-time and single-document-time constructions. Source weighting-equivalence and Beta-shape notation are qualified by finite counterexamples. TNG printed topic updates omit an outgoing gate factor present in the full joint; the record preserves the model and qualifies the printed formula. Unseen source-code behavior is not inferred.
- The author-index topic-extension cohort is partially addressed by three records. Thirteen provisional new reference cohorts leave 289 pending leads and other unresolved dispositions. All three records remain DRAFT.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T002900Z-hierarchy-time-and-phrases
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of DAG, continuous-time and phrase topic models
started_at: '2026-10-12T00:25:04Z'
finished_at: '2026-10-12T00:29:00Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially read all fields of three final
    records against 28 complete primary PDF pages, 18 annotated AIO nodes and nine
    native contextual records. Finite calculations tested collapsed path conditionals
    and counterexamples for timestamp constructions, shape conventions and omitted
    phrase-gate dependence. This is author self-review, not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain three DRAFT model families for DAG topic paths, continuous timestamp
  factors and topic-dependent phrase gates. Explicit qualifications preserve shared-parameter
  scope, alternate generative laws, approximate fitting and printed-equation boundaries.
  No actionable curation finding remains in this selected cohort.
source:
  git_revision: a43f98de507150660ac211ada935c0d7bdaccfe9
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/FactoredLanguageModel.yaml
    sha256: d5e425f3c7cc5b57fdab859cdc777b62398077a6ac9312aef6a89af42c6eb421
    role: context
  - path: data/aio/HierarchicalLanguageModel.yaml
    sha256: d37f9eda55372f4e261249cdefc3b88b036e214884ef612ced2bb40076d29622
    role: context
  - path: data/aio/LanguageModel.yaml
    sha256: 67c8faa6d8ac8fb5194931f662d513d1527cefb92ab1d7c283b2c8d1ddc20c4a
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
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ProbabilisticTopicModel.yaml
    sha256: a3ddfd23b511de967f562e99542d8a89109852359d286a4d707d784359ddfe32
    role: context
  - path: data/aio/RepresentationLearning.yaml
    sha256: bc7af756440437f60210019e17ad1e2dd15cd1c7cbfbc96312520934b7a5c7ca
    role: context
  - path: data/aio/SubwordSegmentation.yaml
    sha256: d1841cd8a888cbb54840f58b6edd8bfad7b2bf4dd46e459f06010b89ad3d194a
    role: context
  - path: data/aio/TextVectorizationLayer.yaml
    sha256: d1f98ff810cf2407c1a6783fd62e68054e7446db089573f017c918b109f8a1f6
    role: context
  - path: data/aio/TimeSeriesAnalysis.yaml
    sha256: c26b267d0f5fb895e9cb0eb587fe86a115d461dae4d70e0ac6baf1eefb1d4eff
    role: context
  - path: data/aio/TimeSeriesForecasting.yaml
    sha256: 88bbef37663508cc885b40d258cdb6b720c627c0f73af1935c01a372c18b3863
    role: context
  - path: data/aio/Tokenization.yaml
    sha256: 723d21fd60d200e6eea998a88ebeed5e33fd47d32d5a3fc5c459c8b93847f5ff
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/AuthorTopicModel.yaml
    sha256: 732dd9bc7f7bfbfb461f4cca668f72b128449e27f4008a0e9a3cd90c15e8a28f
    role: context
  - path: data/curated/CompositeHMMTopicModel.yaml
    sha256: d2275fcb6595370e2999156c0d48055a854a627c4cf9443a48f0a892240281da
    role: context
  - path: data/curated/CorrelatedTopicModel.yaml
    sha256: 22654d8ad69cbe6a464faf19d4c0bbd9a8a74b966197cd05443f9d01f851b893
    role: context
  - path: data/curated/DynamicTopicModel.yaml
    sha256: 3ea748baf3dcedb99616573346822cb7d7bd3cb75ed496fcbb0cb152bee76f0e
    role: context
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: context
  - path: data/curated/GibbsSampling.yaml
    sha256: 8175215986c0507e3664a3aedf8074fc067d85b4a89002091d1bcb9b637a522a
    role: context
  - path: data/curated/LatentDirichletAllocation.yaml
    sha256: d8147371973fa1a5d5e9d3487d092e64ab70271ab42c18d199cd868bb8eb5aef
    role: context
  - path: data/curated/PachinkoAllocationModel.yaml
    sha256: 9b1121412afd6a0eaaa1f0aa0cfb757c27220f354f6b2b6bd22770eabf59be23
    role: target
  - path: data/curated/ProbabilisticLatentSemanticAnalysis.yaml
    sha256: e9cb970e4795b65a17c073a109b4716fc42f2aa0661bf3f7be128568b19ecc71
    role: context
  - path: data/curated/TemperedExpectationMaximization.yaml
    sha256: 792d43ce4f38f485002b9fadbb1e9d9ac32879069cb2ec6e42b3443b57441ca5
    role: context
  - path: data/curated/TopicalNGramModel.yaml
    sha256: 60a05ed007a770020343cf97d384cba3ecca40c0d7f5ecd917ab2eedd24837cc
    role: target
  - path: data/curated/TopicsOverTimeModel.yaml
    sha256: 502679a2878af64111a8e70f974632aa99c5e2e05ccd06fa44fdccd1a4147ca8
    role: target
  - path: research/discovery/20261012T002440Z-hierarchy-time-and-phrases.json
    sha256: eb26466ceb6d971fe816bfedc70e5b9828c0d861c5aaa50c0d54b5bcd2c348b2
    role: context
  - path: research/discovery/hierarchy-time-phrase-boundaries.py
    sha256: af8eac0e5116ae94572a5de0f29c86bfbb116ad30e23499f066524eedcb511ec
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
- target_id: AIMech:PachinkoAllocationModel
  path: data/curated/PachinkoAllocationModel.yaml
  label: Pachinko allocation model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PachinkoAllocationModel.yaml
    role: maintained
- target_id: AIMech:TopicsOverTimeModel
  path: data/curated/TopicsOverTimeModel.yaml
  label: Topics over Time model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TopicsOverTimeModel.yaml
    role: maintained
- target_id: AIMech:TopicalNGramModel
  path: data/curated/TopicalNGramModel.yaml
  label: Topical n-gram model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TopicalNGramModel.yaml
    role: maintained
scope:
  description: All fields of three maintained probability-model records.
  selection: Exact maintained IDs PachinkoAllocationModel, TopicsOverTimeModel and
    TopicalNGramModel; complete selected cohort without sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:PachinkoAllocationModel
  - AIMech:TopicsOverTimeModel
  - AIMech:TopicalNGramModel
  exclusions:
  - target: Author software, trained instances and empirical reproduction
    reason: No author implementation or benchmark was executed. Finite curator calculations
      do not certify historical software, chain mixing or empirical findings.
  - target: Contextual records, other topic extensions and remaining frontier
    reason: Context informs identity without renewed scientific approval. Thirteen
      new reference cohorts, 289 pending leads and other unresolved dispositions remain.
      Later PAM variants, earlier TNG versions and other author-index extensions require
      separate primary inspection.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:PachinkoAllocationModel
  - AIMech:TopicsOverTimeModel
  - AIMech:TopicalNGramModel
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 141.61s (0:02:21)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 435 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 126 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 123,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:PachinkoAllocationModel
  - AIMech:TopicsOverTimeModel
  - AIMech:TopicalNGramModel
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
  - AIMech:PachinkoAllocationModel
  - AIMech:TopicsOverTimeModel
  - AIMech:TopicalNGramModel
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
  - AIMech:PachinkoAllocationModel
  - AIMech:TopicsOverTimeModel
  - AIMech:TopicalNGramModel
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Hierarchy, timestamp and phrase probability boundaries
  command: python3 research/discovery/hierarchy-time-phrase-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:PachinkoAllocationModel
  - AIMech:TopicsOverTimeModel
  - AIMech:TopicalNGramModel
  exit_code: 0
  expected_exit_code: 0
  summary: '{"pam_assignment_states": 64, "pam_conditional_checks": 192, "pam_maximum_conditional_error":
    4.440892098500626e-16, "positive_shared_parent_covariance": 0.01686507936507957,
    "tot_single_timestamp_joint": 0.25, "tot_repeated_timestamp_joint": 0.16000000000000003,
    "tot_inverse_length_tempered_joint": 0.2, "tot_repeated_diagonal_integral": 0.16666666666666666,
    "tot_single_time_word_mass": 0.25, "beta_consistent_mean": 0.2, "beta_reversed_display_mean":
    0.8, "token_topic_given_time": 0.8, "document_mixture_posterior_mean": 0.6, "tng_correct_topic_conditional":
    [0.6666666666666666, 0.3333333333333334], "tng_without_next_gate": [0.5714285714285715,
    0.4285714285714286], "scope": "Finite synthetic checks and counterexamples, not
    author-code execution or benchmark reproduction."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T002440Z-hierarchy-time-and-phrases.json
  accessed_at: '2026-10-12T00:25:04Z'
  support: supports
  summary: No normalized candidate identity matched all 442 pinned AIO IDs, labels
    and scoped synonyms or 432 preceding native IDs, names and aliases. Full-checkout
    searches included ignored and hidden files in both checkouts; six matching lines
    per checkout came from three unique file contents containing prior frontier leads,
    bibliography context and a cached publication-list mention. All candidate-matching
    excerpts were read; the long cached browser transcript was not reread in full.
    All 205 semantic label/synonym hits were byte-verified unchanged from prior reading.
    Eighteen annotated AIO CLASS nodes and outgoing edges comprise 17 verified prior
    inspections and one fresh reading. Twenty-seven contextual YAMLs comprise 25 unchanged
    prior readings, one fresh generated AIO reading and one final round102 native
    record verified against its fully read review inputs. No candidate record is present
    within this bounded pinned-snapshot and maintained-corpus search.
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison; short acronyms were omitted
    from broad substring searches to avoid irrelevant matches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 18 exact annotated CLASS nodes and outgoing edges, 17 unchanged and one
    freshly read; all 205 label/synonym hits verified unchanged
  accessed_at: '2026-10-12T00:25:04Z'
  support: supports
  summary: PAM and TOT map broadly to AIO Model; TNG maps broadly to LanguageModel
    because it defines a word-sequence law. All map related to task-scoped ProbabilisticTopicModel,
    and TOT additionally maps related to TimeSeriesAnalysis. HierarchicalLanguageModel
    and FactoredLanguageModel are broader neighboring descriptions, not exact PAM/TNG
    identities. PAM routing DAGs do not establish CausalGraphicalModel; general graphical
    and Bayesian-network categories do not replace source-specific mechanisms. TOT
    uses observed continuous timestamps, not a Markov state trajectory or guaranteed
    TimeSeriesForecasting method. TNG phrase gates differ from Tokenization, SubwordSegmentation
    and TextVectorizationLayer. The pinned RepresentationLearning class is a deep-neural-network
    subclass and is not justified merely by classical latent features. LDA, PLSA,
    CTM, DTM, author-topic and composite HMM-topic records, together with Gibbs/EM/tempered
    EM, provide contextual boundaries without renewed scientific approval.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261012T002440Z-hierarchy-time-and-phrases.json
  locator: Nine native neighbors and 18 generated contextual YAMLs in source_analysis.context_reading
  accessed_at: '2026-10-12T00:25:04Z'
  support: supports
  summary: Native LDA, PLSA, CTM, DTM, author-topic, composite HMM-topic, Gibbs, EM
    and tempered EM records inform identity distinctions. Twenty-five contextual files
    are unchanged from prior readings; one generated AIO record was freshly read and
    one round102 native record matches fully read final review inputs. No contextual
    record receives renewed scientific approval.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/hierarchy-time-phrase-boundaries.py
  locator: PAM collapsed path probabilities, timestamp model/shape distinctions and
    TNG next-gate dependence
  accessed_at: '2026-10-12T00:25:04Z'
  snapshot_sha256: af8eac0e5116ae94572a5de0f29c86bfbb116ad30e23499f066524eedcb511ec
  support: supports
  summary: A 64-state four-level PAM example verifies 192 collapsed path conditionals
    against integrated joint ratios and exhibits positive child-topic covariance from
    shared parent mass. A two-topic TOT example distinguishes a single timestamp mixture
    (joint density0.25) from repeated token timestamp factors (0.16) and inverse-length
    tempering (0.2); its repeated diagonal integrates to1/6 rather than word mass1/4.
    Consistent Beta moment shapes have mean0.2 while the reversed printed convention
    gives0.8. Token-topic Bayes inversion0.8 differs from document-mixture posterior
    mean0.6. A three-token TNG integrated joint gives topic conditional(2/3,1/3),
    while omitting the next-gate factor gives(4/7,3/7). These are finite curator checks/counterexamples,
    not author-code or empirical reproduction.
- evidence_id: pachinkoallocationmodel-source-0
  kind: primary_source
  reference: https://people.cs.umass.edu/~mccallum/papers/pam-icml06.pdf
  locator: Section 2, PDF p.3, document/corpus probability displays; Section 2.1 pp.3-4
    and Figure 2; Section 2.2, PDF p.4, collapsed update and moment-based parameter
    estimates; Sections 1-2, PDF pp.2-3, Figure 1 and generative process
  accessed_at: '2026-10-12T00:14:11Z'
  snapshot_sha256: 645882dd892aa9e308625fd2227dccaa1c91e6ece9bf81cee2e6f857320d9255
  support: supports
  summary: 'Pachinko Allocation: DAG-Structured Mixture Models of Topic Correlations.
    Author-hosted eight-page ICML2006 paper; all pages visually read. No numeric printed
    page labels are visible, so locators use PDF pages. Later hierarchical, nonparametric
    and scalable PAM papers are separate versions/extensions. All pages of the primary
    PDF were visually read. Curator qualifications and synthetic calculations are
    distinguished from historical empirical claims and uninspected implementations.'
- evidence_id: topicsovertimemodel-source-0
  kind: primary_source
  reference: https://people.cs.umass.edu/~mccallum/papers/tot-kdd06.pdf
  locator: Section 2, PDF pp.2-4, Figure 1(b,c), generative steps and alternative
    description; Section 2, PDF pp.3-4, conditional and Algorithm 1; Appendix A p.10,
    density and moment estimates; Sections 1-2, PDF pp.1-4, Figure 1 and token-level
    generative process
  accessed_at: '2026-10-12T00:14:13Z'
  snapshot_sha256: 96102cc116a8f5b01ad4ec82a841a4684bb63d4b6ecd6cc3a5e67d4890d3bf04
  support: supports
  summary: 'Topics over Time: A Non-Markov Continuous-Time Model of Topical Trends.
    Author-hosted ten-page KDD2006 paper, including Appendix A on p.10; all pages
    visually read. No numeric printed page labels visible; locators use PDF pages.
    All pages of the primary PDF were visually read. Curator qualifications and synthetic
    calculations are distinguished from historical empirical claims and uninspected
    implementations.'
- evidence_id: topicalngrammodel-source-0
  kind: primary_source
  reference: https://people.cs.umass.edu/~mccallum/papers/tng-icdm07.pdf
  locator: Figure 1(c), PDF p.3; Section 2.3 p.4; Appendix A joint p.9 and conditionals
    p.10; Section 2.3, PDF pp.3-4, Figure 1(c) and generative steps; Sections 2.2-2.3,
    PDF pp.2-4, boundary handling, Figure 1(c) and topic-consistency discussion
  accessed_at: '2026-10-12T00:14:16Z'
  snapshot_sha256: 3ed0ce0b6b73a932d08af8dc81fdd06148c20c6cea7ee7e284091064059e1a3c
  support: supports
  summary: 'Topical N-grams: Phrase and Topic Discovery, with an Application to Information
    Retrieval. Author-hosted ten-page ICDM2007 paper, including Appendix A pp.9-10;
    all pages visually read. No numeric printed page labels visible; locators use
    PDF pages. The earlier 2005 technical report was located but not read or substituted
    for this version. All pages of the primary PDF were visually read. Curator qualifications
    and synthetic calculations are distinguished from historical empirical claims
    and uninspected implementations.'
assessments:
- assessment_id: pachinkoallocationmodel
  area: evidence
  topic: Identity, model definition, inference interpretation, limitations and mappings
  outcome: supported
  target_ids:
  - AIMech:PachinkoAllocationModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - pachinkoallocationmodel-source-0
  summary: Scoped to Li and McCallum's PAM construction, with Dirichlet child-distribution
    priors and the four-level experimental variant in ICML2006. Interior topics can
    have multiple parents, and paths may skip levels. A new path is selected for each
    token. This differs from a single topic path assigned to an entire document, a
    logistic-normal topic mixture, or a causal graph of semantic concepts. PAM is
    a source acronym within this scope; later hierarchical, nonparametric and scalable
    variants are not asserted as exact aliases. No normalized candidate identity matched
    all 442 pinned AIO IDs, labels and scoped synonyms or 432 preceding native IDs,
    names and aliases. Full-checkout searches included ignored and hidden files in
    both checkouts; six matching lines per checkout came from three unique file contents
    containing prior frontier leads, bibliography context and a cached publication-list
    mention. All candidate-matching excerpts were read; the long cached browser transcript
    was not reread in full. All 205 semantic label/synonym hits were byte-verified
    unchanged from prior reading. Eighteen annotated AIO CLASS nodes and outgoing
    edges comprise 17 verified prior inspections and one fresh reading. Twenty-seven
    contextual YAMLs comprise 25 unchanged prior readings, one fresh generated AIO
    reading and one final round102 native record verified against its fully read review
    inputs. No candidate record is present within this bounded pinned-snapshot and
    maintained-corpus search.
  details: 'In the general Dirichlet formulation, each document draws a categorical
    child vector for each interior node. Each token starts at the root and repeatedly
    chooses a child until it reaches a word leaf. The finite rooted DAG and reachable
    word leaves ensure termination. In the demonstrated four-level variant, root-to-supertopic
    and supertopic-to-subtopic vectors vary per document, while subtopic-to-word vectors
    are drawn once and shared across the corpus. The latter sharing changes corpus
    marginalization: shared random emissions must be integrated jointly. The product
    of separately marginalized documents written for the fully document-local formulation
    is not automatically the marginal law of this shared-emission variant. For fixed
    positive hyperparameters in the four-level variant, a token''s collapsed supertopic/subtopic
    weight multiplies three leave-one-out predictive factors: the document root-to-supertopic
    count, the document supertopic-to-subtopic count, and the corpus subtopic-to-word
    count, each smoothed and normalized by its Dirichlet prior. The source jointly
    samples both topic levels. Its experimental fitting also changes supertopic hyperparameters
    using smoothed empirical moments and a concentration heuristic, rather than exact
    maximum likelihood or MAP. That changing-parameter procedure is not simply fixed-target
    posterior Gibbs sampling; neither finite samples nor moment updates establish
    convergence or optimality. Limitations: The experiments fix a fully connected
    four-level structure and topic counts. Learning arbitrary DAG structure or a nonparametric
    number of nodes is prospective in this paper. A DAG can encode nested and overlapping
    mixtures without establishing a universal representation theorem for every correlation
    structure. Dirichlet topic proportions are compositionally dependent, with negative
    off-diagonal covariances; the introductory LDA-independence contrast is not literal
    independence. Logistic-normal covariance parameters likewise do not mean higher-order
    dependence vanishes. PAM supplies a different mixing construction, not proof that
    CTM is exactly equivalent to a two-child DAG. Moment updates require policies
    for unvisited parent nodes, zero or invalid variances and nonpositive concentration
    estimates. Smoothing child means alone does not specify all edge cases. LDA reductions
    require compatible shared or fixed emissions; redrawing every word-emission vector
    independently per document is a different model. Evidence includes selected topics,
    a small human-judgment study, approximate held-out likelihood and five-way newsgroup
    classification. The prose and Table 2 disagree on majority-vote counts. The generated-document
    likelihood approximation is not exact marginal likelihood, and the reported results
    do not establish universal superiority. No author code or benchmark was executed.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A specified latent-variable probability-model family, not a trained
      instance or merely its fitting algorithm.
    evidence_ids:
    - pachinkoallocationmodel-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: PAM and TOT map broadly to AIO Model; TNG maps broadly to LanguageModel
      because it defines a word-sequence law. All map related to task-scoped ProbabilisticTopicModel,
      and TOT additionally maps related to TimeSeriesAnalysis. HierarchicalLanguageModel
      and FactoredLanguageModel are broader neighboring descriptions, not exact PAM/TNG
      identities. PAM routing DAGs do not establish CausalGraphicalModel; general
      graphical and Bayesian-network categories do not replace source-specific mechanisms.
      TOT uses observed continuous timestamps, not a Markov state trajectory or guaranteed
      TimeSeriesForecasting method. TNG phrase gates differ from Tokenization, SubwordSegmentation
      and TextVectorizationLayer. The pinned RepresentationLearning class is a deep-neural-network
      subclass and is not justified merely by classical latent features. LDA, PLSA,
      CTM, DTM, author-topic and composite HMM-topic records, together with Gibbs/EM/tempered
      EM, provide contextual boundaries without renewed scientific approval.
    evidence_ids:
    - mapping
- assessment_id: topicsovertimemodel
  area: evidence
  topic: Identity, model definition, inference interpretation, limitations and mappings
  outcome: supported
  target_ids:
  - AIMech:TopicsOverTimeModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - topicsovertimemodel-source-0
  summary: Scoped to Wang and McCallum's KDD2006 Topics over Time model, especially
    its fitted token-level timestamp construction with Beta densities over normalized
    time. The paper also proposes a distinct single-document-timestamp view. Fixed
    topic-word distributions distinguish TOT from dynamic topic models with evolving
    word probabilities; continuous observed time does not imply a Markov process or
    point-process intensity. TOT is a source acronym within this scope. No normalized
    candidate identity matched all 442 pinned AIO IDs, labels and scoped synonyms
    or 432 preceding native IDs, names and aliases. Full-checkout searches included
    ignored and hidden files in both checkouts; six matching lines per checkout came
    from three unique file contents containing prior frontier leads, bibliography
    context and a cached publication-list mention. All candidate-matching excerpts
    were read; the long cached browser transcript was not reread in full. All 205
    semantic label/synonym hits were byte-verified unchanged from prior reading. Eighteen
    annotated AIO CLASS nodes and outgoing edges comprise 17 verified prior inspections
    and one fresh reading. Twenty-seven contextual YAMLs comprise 25 unchanged prior
    readings, one fresh generated AIO reading and one final round102 native record
    verified against its fully read review inputs. No candidate record is present
    within this bounded pinned-snapshot and maintained-corpus search.
  details: 'The fitted construction gives each document a Dirichlet topic mixture,
    each topic a corpus-shared categorical word vector, and each topic a Beta timestamp
    density on a normalized bounded interval. A token draws a topic, a word and a
    timestamp; fitting copies the document timestamp to every token. Word distributions
    remain fixed across time, while topic-specific time densities influence assignment.
    The alternative description generates one timestamp from a document-mixture-weighted
    combination of topic densities. These are different generative laws: repeating
    topic-time factors, even with inverse-length weighting, is not generally identical
    to one mixture density for a document timestamp. With topic timestamp parameters
    fixed, the collapsed token assignment weight combines leave-one-out document-topic
    and topic-word predictive factors with the assigned topic''s timestamp density.
    The paper introduces an exponent to balance time and word contributions and updates
    Beta parameters from empirical moments. These adaptations change the fitting objective
    and require positive valid shapes and safeguards for empty topics or zero variance.
    The printed density uses (1-t)^(psi1-1)*t^(psi2-1), whereas its moment estimates
    assign psi1=mean*c and psi2=(1-mean)*c. A coherent calculation must use one consistent
    shape convention; for the conventional Beta(a,b), the density is proportional
    to t^(a-1)*(1-t)^(b-1). No behavior of uninspected historical software is inferred
    from this notation conflict. Limitations: A repeated timestamp provides one density
    factor per token unless explicitly reweighted. Its restriction to one common timestamp
    is not automatically a normalized single-time document density. The proposed balancing
    exponent does not prove equivalence between the two generative descriptions. Bayes
    inversion can produce a token-topic probability given time using an assumed or
    estimated topic prior. This is not generally the same quantity as the posterior
    mean of a random document topic vector, despite notation on p.4. Continuous density
    values are not probabilities; endpoint handling, normalization range and balancing
    conventions matter. One Beta per topic limits temporal shapes. Extending the bounded
    time range for prediction is a modeling choice rather than a guarantee of future
    extrapolation. Fixed word distributions do not directly model changing word meanings,
    and topic split/merge interpretations are descriptive. Historical evaluations
    use selected address, email and NIPS collections with heuristic preprocessing
    and particular finite samples. Topic names, KL distinctness, thresholded co-occurrence
    and decade prediction do not establish causal trends, universal semantic accuracy
    or future forecasting. No author code or benchmark was executed.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A specified latent-variable probability-model family, not a trained
      instance or merely its fitting algorithm.
    evidence_ids:
    - topicsovertimemodel-source-0
  - name: aio-assessment
    value: broad_match,related_match,related_match
    definition: PAM and TOT map broadly to AIO Model; TNG maps broadly to LanguageModel
      because it defines a word-sequence law. All map related to task-scoped ProbabilisticTopicModel,
      and TOT additionally maps related to TimeSeriesAnalysis. HierarchicalLanguageModel
      and FactoredLanguageModel are broader neighboring descriptions, not exact PAM/TNG
      identities. PAM routing DAGs do not establish CausalGraphicalModel; general
      graphical and Bayesian-network categories do not replace source-specific mechanisms.
      TOT uses observed continuous timestamps, not a Markov state trajectory or guaranteed
      TimeSeriesForecasting method. TNG phrase gates differ from Tokenization, SubwordSegmentation
      and TextVectorizationLayer. The pinned RepresentationLearning class is a deep-neural-network
      subclass and is not justified merely by classical latent features. LDA, PLSA,
      CTM, DTM, author-topic and composite HMM-topic records, together with Gibbs/EM/tempered
      EM, provide contextual boundaries without renewed scientific approval.
    evidence_ids:
    - mapping
- assessment_id: topicalngrammodel
  area: evidence
  topic: Identity, model definition, inference interpretation, limitations and mappings
  outcome: supported
  target_ids:
  - AIMech:TopicalNGramModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - topicalngrammodel-source-0
  summary: Scoped to Wang, McCallum and Wei's ICDM2007 TNG model in Figure 1(c). The
    Bernoulli gate uses the previous token's topic and word; the emission uses the
    current topic. Consecutive bigram choices form longer phrases, but the local generative
    law remains first order. This differs from the always-bigram topic model, the
    topic-independent LDA collocation components and generic tokenization. TNG is
    the source acronym. Topic assignments need not be identical within an extracted
    phrase. No normalized candidate identity matched all 442 pinned AIO IDs, labels
    and scoped synonyms or 432 preceding native IDs, names and aliases. Full-checkout
    searches included ignored and hidden files in both checkouts; six matching lines
    per checkout came from three unique file contents containing prior frontier leads,
    bibliography context and a cached publication-list mention. All candidate-matching
    excerpts were read; the long cached browser transcript was not reread in full.
    All 205 semantic label/synonym hits were byte-verified unchanged from prior reading.
    Eighteen annotated AIO CLASS nodes and outgoing edges comprise 17 verified prior
    inspections and one fresh reading. Twenty-seven contextual YAMLs comprise 25 unchanged
    prior readings, one fresh generated AIO reading and one final round102 native
    record verified against its fully read review inputs. No candidate record is present
    within this bounded pinned-snapshot and maintained-corpus search.
  details: 'Each document has a Dirichlet topic vector theta. Each topic has a categorical
    unigram vector phi, each topic/previous-word pair has a categorical bigram vector
    sigma, and each previous-topic/previous-word pair has a Bernoulli gate psi with
    a Beta prior. At position i, x_i is drawn from psi_(z_(i-1),w_(i-1)), z_i from
    theta, and w_i from phi_z_i if x_i=0 or sigma_(z_i,w_(i-1)) if x_i=1. Initial
    and other specified boundaries constrain gates to unigrams. Runs of bigram choices
    induce phrases; the paper labels a phrase by its last word''s topic as an output
    convention. This does not impose a shared latent topic across the phrase. The
    generative law makes z_i a parent of the next gate x_(i+1). Consequently a topic
    update conditioned on the other assignments must account for that outgoing gate
    as well as the current emission and document mixture. The full joint in Appendix
    A includes those factors, but the printed joint/topic conditional displays on
    pp.4 and10 omit the next-gate contribution. A collapsed implementation must remove
    all affected factors and preserve shared-parameter count corrections before evaluating
    candidates. A finite integrated example yields a topic conditional of (2/3,1/3),
    whereas dropping that contribution gives (4/7,3/7). This qualifies the printed
    inference expression, without asserting that uninspected author software used
    it. Limitations: The model represents long phrases through successive first-order
    bigrams, not an unrestricted higher-order n-gram table. Fixed topic count, vocabulary,
    boundary rules and many topic/word parameter rows constrain the model and require
    smoothing. The optional same-topic phrase modification on p.4 has an if/else inconsistent
    with its verbal intention. The record follows the main Figure 1(c) construction.
    Printed minus-one counts must be interpreted as removing the old assignment, not
    subtracting one from every candidate category. The retrieval section uses a plug-in
    first-order query score that averages the previous-topic gate under document weights.
    It is not generally exact filtering or posterior prediction for the full latent
    sequence. Query-level mixture and term-level interpolation are different scoring
    rules; the reported study uses term-level interpolation. The NIPS/TREC experiments
    use selected preparations, fixed hyperparameters and model-specific interpolation
    weights selected for best performance. Topic/phrase labels and retrieval comparisons
    do not establish linguistic ground truth or universal superiority. The finite
    counterexample audits a printed equation, not source implementation or benchmark
    execution.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A specified latent-variable probability-model family, not a trained
      instance or merely its fitting algorithm.
    evidence_ids:
    - topicalngrammodel-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: PAM and TOT map broadly to AIO Model; TNG maps broadly to LanguageModel
      because it defines a word-sequence law. All map related to task-scoped ProbabilisticTopicModel,
      and TOT additionally maps related to TimeSeriesAnalysis. HierarchicalLanguageModel
      and FactoredLanguageModel are broader neighboring descriptions, not exact PAM/TNG
      identities. PAM routing DAGs do not establish CausalGraphicalModel; general
      graphical and Bayesian-network categories do not replace source-specific mechanisms.
      TOT uses observed continuous timestamps, not a Markov state trajectory or guaranteed
      TimeSeriesForecasting method. TNG phrase gates differ from Tokenization, SubwordSegmentation
      and TextVectorizationLayer. The pinned RepresentationLearning class is a deep-neural-network
      subclass and is not justified merely by classical latent features. LDA, PLSA,
      CTM, DTM, author-topic and composite HMM-topic records, together with Gibbs/EM/tempered
      EM, provide contextual boundaries without renewed scientific approval.
    evidence_ids:
    - mapping
- assessment_id: pam-paths
  area: consistency
  topic: Per-token DAG paths, shared emissions and fitted hyperparameters
  outcome: supported
  target_ids:
  - AIMech:PachinkoAllocationModel
  evidence_ids:
  - pachinkoallocationmodel-source-0
  - finite-boundaries
  - neighbors
  summary: Retain PAM with distinct general and four-level scopes.
  details: The general formulation redraws child distributions by document, whereas
    four-level PAM shares subtopic word vectors across the corpus. A 64-state example
    verifies 192 collapsed path conditionals to 4.5e-16. Shared parent mass can give
    positive covariance between child topics, but broad correlation rhetoric does
    not establish universal expressivity or independence in LDA. The source fixes
    graph structure and uses moment heuristics with unresolved numerical edge policies.
    Its human-vote table and prose disagree, so no disputed count is adopted.
- assessment_id: tot-time-laws
  area: consistency
  topic: Repeated token timestamps, single-time mixtures and Beta convention
  outcome: supported
  target_ids:
  - AIMech:TopicsOverTimeModel
  evidence_ids:
  - topicsovertimemodel-source-0
  - finite-boundaries
  - neighbors
  summary: Retain TOT while distinguishing its two generative descriptions.
  details: 'A two-topic example gives joint densities0.25 for one mixture timestamp,0.16
    for repeated token factors and0.2 after inverse-length tempering. Restricting
    repeated times to one diagonal integrates to1/6 instead of word mass1/4. The displayed
    Beta exponent order conflicts with moment-shape assignments: the consistent mean0.2
    becomes0.8 if reversed. A token-topic conditional0.8 also differs from document-mixture
    posterior mean0.6. These counterexamples qualify source equivalence/notation claims
    without alleging historical implementation failure.'
- assessment_id: tng-next-gate
  area: consistency
  topic: Previous-topic phrase gates and outgoing conditional dependence
  outcome: supported
  target_ids:
  - AIMech:TopicalNGramModel
  evidence_ids:
  - topicalngrammodel-source-0
  - finite-boundaries
  - neighbors
  summary: Retain the TNG generative law with a qualified printed update.
  details: The previous topic and word determine the current gate, while the current
    topic determines emission. Thus a topic update influences the next gate. The full
    integrated joint gives a three-token conditional(2/3,1/3), whereas omitting that
    factor gives(4/7,3/7). The printed topic update is incomplete for general conditioned
    sequences; correct collapsed updates must account for all affected gate counts.
    The optional same-topic if/else and plug-in first-order query score are separately
    qualified. Longer extracted phrases do not make the model an unrestricted higher-order
    n-gram law.
- assessment_id: versions-and-empirics
  area: consistency
  topic: Exact publication versions and bounded empirical evidence
  outcome: supported
  target_ids:
  - AIMech:PachinkoAllocationModel
  - AIMech:TopicsOverTimeModel
  - AIMech:TopicalNGramModel
  evidence_ids:
  - pachinkoallocationmodel-source-0
  - topicsovertimemodel-source-0
  - topicalngrammodel-source-0
  summary: Preserve all three fully inspected primary conference versions.
  details: All28 pages of ICML2006 PAM, KDD2006 TOT and ICDM2007 TNG were visually
    read. Locators use PDF pages; later PAM variants and the earlier TNG technical
    report are not current mechanism evidence. Selected topic examples, approximate
    likelihoods, timestamp prediction and tuned retrieval comparisons do not establish
    universal superiority, causal interpretation or code reproduction. Native composite
    HMM-topic coverage is recognized when the TNG source calls it HMMLDA, without
    a duplicate addition or modification of its immutable prior review.
- assessment_id: mapping-boundary
  area: grounding
  topic: Model/task mapping direction and neighboring constructions
  outcome: supported
  target_ids:
  - AIMech:PachinkoAllocationModel
  - AIMech:TopicsOverTimeModel
  - AIMech:TopicalNGramModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain three distinct native model families.
  details: PAM and TOT map broadly to AIO Model; TNG maps broadly to LanguageModel
    because it defines a word-sequence law. All map related to task-scoped ProbabilisticTopicModel,
    and TOT additionally maps related to TimeSeriesAnalysis. HierarchicalLanguageModel
    and FactoredLanguageModel are broader neighboring descriptions, not exact PAM/TNG
    identities. PAM routing DAGs do not establish CausalGraphicalModel; general graphical
    and Bayesian-network categories do not replace source-specific mechanisms. TOT
    uses observed continuous timestamps, not a Markov state trajectory or guaranteed
    TimeSeriesForecasting method. TNG phrase gates differ from Tokenization, SubwordSegmentation
    and TextVectorizationLayer. The pinned RepresentationLearning class is a deep-neural-network
    subclass and is not justified merely by classical latent features. LDA, PLSA,
    CTM, DTM, author-topic and composite HMM-topic records, together with Gibbs/EM/tempered
    EM, provide contextual boundaries without renewed scientific approval.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:PachinkoAllocationModel
  - AIMech:TopicsOverTimeModel
  - AIMech:TopicalNGramModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - pachinkoallocationmodel-source-0
  - topicsovertimemodel-source-0
  - topicalngrammodel-source-0
  rationale: DAG path mixing, continuous timestamp factors and topic-dependent sequence
    gates are distinct model structures. Broad Model or LanguageModel and related
    topic/time-analysis mappings preserve AIO abstraction without forcing exact matches.
limitations:
- Adversarial author self-review only; all three records remain DRAFT.
- All 28 pages of three author-hosted conference PDFs were visually read, including
  equations, figures, tables and bibliographies. Locators use PDF pages because no
  numeric printed page labels were visible. No extracted-text reading or author-code
  execution is asserted.
- PAM is the ICML2006 version, TOT is KDD2006 and TNG is ICDM2007. Later PAM extensions
  and the earlier TNG technical report were located but not read as current mechanism
  evidence.
- PAM separates the general document-local formulation from corpus-shared emissions
  in its four-level variant. Moment heuristics and fixed structures are not exact
  parameter inference or automatic structure learning. Source human-vote totals are
  inconsistent; no disputed count is adopted.
- TOT has distinct token-time and single-document-time constructions. Source weighting-equivalence
  and Beta-shape notation are qualified by finite counterexamples. TNG printed topic
  updates omit an outgoing gate factor present in the full joint; the record preserves
  the model and qualifies the printed formula. Unseen source-code behavior is not
  inferred.
- The author-index topic-extension cohort is partially addressed by three records.
  Thirteen provisional new reference cohorts leave 289 pending leads and other unresolved
  dispositions. All three records remain DRAFT.
links: []
tags:
- native-concepts
- hierarchy-time-phrases
- self-review
- discovery-ongoing
```
