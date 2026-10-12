# Scientific self-review of role, label-subset and joint content-link models

- Review: 20261012T001653Z-roles-labels-and-links
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T00:13:34Z
- Finished UTC: 2026-10-12T00:16:53Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain three DRAFT model families for actor roles, observed label subsets and fixed shared content/link mixtures. Explicit qualifications distinguish detailed model laws, variant sketches, approximate fitting and bounded empirical evidence. No actionable curation finding remains in this selected cohort.

## Scope And Provenance

All fields of three maintained probability-model records.

Selection: Exact maintained IDs RoleAuthorRecipientTopicModel, MultiLabelTextMixtureModel and JointTermCitationModel; complete selected cohort without sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 082bd4895143a63badf7fee58cdd27d1fc8eba39.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:RoleAuthorRecipientTopicModel | data/curated/RoleAuthorRecipientTopicModel.yaml | maintained | Role-author-recipient-topic model |
| AIMech:MultiLabelTextMixtureModel | data/curated/MultiLabelTextMixtureModel.yaml | maintained | Multi-label text mixture model |
| AIMech:JointTermCitationModel | data/curated/JointTermCitationModel.yaml | maintained | Joint term-citation model |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:RoleAuthorRecipientTopicModel, AIMech:MultiLabelTextMixtureModel, AIMech:JointTermCitationModel | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 100.33s (0:01:40)<br>Checked 442 record(s); 0 failed.<br>Checked 432 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 125 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 122,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:RoleAuthorRecipientTopicModel, AIMech:MultiLabelTextMixtureModel, AIMech:JointTermCitationModel | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:RoleAuthorRecipientTopicModel, AIMech:MultiLabelTextMixtureModel, AIMech:JointTermCitationModel | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:RoleAuthorRecipientTopicModel, AIMech:MultiLabelTextMixtureModel, AIMech:JointTermCitationModel | Command exited 0 with no output. |
| Role, label-mixture and joint-channel probability boundaries | passed | True | AIMech:RoleAuthorRecipientTopicModel, AIMech:MultiLabelTextMixtureModel, AIMech:JointTermCitationModel | {"rart_assignment_states": 256, "rart_conditional_checks": 512, "maximum_rart_conditional_error": 3.608224830031759e-16, "same_actor_equal_role_probability": 0.6666666666666662, "independent_actors_equal_role_probability": 0.5, "integrated_multilabel_two_word_probability": 0.30000000000000004, "mode_substitution_two_word_probability": 0.25, "additive_smoothing": [0.6666666666666666, 0.3333333333333333], "flat_dirichlet_map": [0.75, 0.25], "joint_channel_objective_before": -1.403863553946856, "joint_channel_objective_after": -1.3010048308859699, "unnormalized_emission_row_sums": [[0.6151384615384615, 0.5848615384615384], [0.49903846153846154, 0.3009615384615385]], "scope": "Finite synthetic probability and ordinary-EM checks, not source code or benchmarks."} |

## Scientific And Domain Assessments

### Identity, model definition, inference interpretation, limitations and mappings

evidence: supported. Targets: AIMech:RoleAuthorRecipientTopicModel.

Scoped to the RART family introduced by McCallum and colleagues, with the 2007 preprint specifying RART1 in detail and sketching RART2 and RART3. RART1 draws both roles per token; RART2 fixes a sender role and individual recipient roles per message; RART3 uses one common recipient role per message. The latter sketches are not asserted to provide complete independent inference algorithms. Explicit actor roles distinguish this family from ART pair-specific topic vectors and author-topic models. RART is a source acronym within this scope. No normalized candidate identity matched all 442 pinned AIO IDs, labels and scoped synonyms or 429 preceding native IDs, names and aliases. Full-checkout searches included ignored and hidden files in both checkouts; 23 matching lines per checkout came from four unique file contents containing prior frontier leads and contextual distinctions. All matching excerpts were inspected. The semantic search returned 205 label/synonym hits, with 204 unchanged from prior reading and one newly read. Eighteen annotated AIO CLASS nodes and outgoing edges were byte-verified against prior inspected versions. Twenty-six contextual YAMLs comprise 24 unchanged prior readings and two final round102 records verified against their fully read scientific-review inputs. No candidate record is present within this bounded pinned-snapshot and maintained-corpus search.

In RART1, each actor has a Dirichlet-distributed role vector psi, each ordered sender-role/recipient-role pair has a Dirichlet topic vector theta, and each topic has a Dirichlet word vector phi. Given observed sender a and a nonempty recipient set R, a token chooses r uniformly from R, sender role g from psi_a, recipient role h from psi_r, topic z from theta_gh, then word w from phi_z. An actor uses the same role vector for sending and receiving, while theta distinguishes the order of the roles. The model conditions on participants and message lengths rather than generating network edges. Shared random vectors must be integrated jointly across their uses; two roles drawn for the same actor need not be independent after psi is integrated out. The reported RART1 experiment first fits ART, fixes topic and recipient assignments from one sample, and then infers the role structure conditionally on those assignments. This staged procedure does not sample the full joint RART posterior or propagate all uncertainty in the frozen assignments. The source states that general Gibbs updates can be derived, but its Appendix A derives ART updates, not a complete RART sampler. Conditional on fixed parameters, token role choices can vary within a message; RART2 and RART3 impose different message-level sharing and cannot be substituted without changing the model. Limitations: Only RART1 has a detailed generative specification in this source. The RART2/3 diagrams and prose leave further implementation and inference choices for exploration; family coverage does not certify fully specified variants. The demonstrated 15-role, 50-topic fit is illustrated by selected email users and manually named roles in Tables 6-7. Some apparently unrelated assignments remain unexplained, and entity-resolution errors are present. These examples do not establish verified occupations, expertise, causal influence or universal predictive superiority. Earlier ART perplexity results are not RART benchmark results. Fixed role/topic counts, bag-of-words observations, uniform recipient selection and corpus-specific participation affect identifiability and interpretation. Latent role labels are exchangeable; semantic names are human interpretations. A single ART sample judged plausible does not establish adequate uncertainty propagation or convergence. Finite synthetic collapsed-probability checks cover the specified RART1 factorization, including a shared actor in sender and recipient positions. They are not a reproduction of historical software, email preprocessing or the reported benchmark.

### Identity, model definition, inference interpretation, limitations and mappings

evidence: supported. Targets: AIMech:MultiLabelTextMixtureModel.

Scoped to McCallum's 1999 mixture model for multi-label text classification, whose training observes document label sets while token labels are latent. The maintained name describes this source construction; no source acronym is invented. It differs from independent binary classifiers, mutually exclusive multiclass classification and unsupervised topic discovery. The uniform author-word comparator cited by later author-topic papers is a simplified case, not an alias for the full learned label-mixture construction. No normalized candidate identity matched all 442 pinned AIO IDs, labels and scoped synonyms or 429 preceding native IDs, names and aliases. Full-checkout searches included ignored and hidden files in both checkouts; 23 matching lines per checkout came from four unique file contents containing prior frontier leads and contextual distinctions. All matching excerpts were inspected. The semantic search returned 205 label/synonym hits, with 204 unchanged from prior reading and one newly read. Eighteen annotated AIO CLASS nodes and outgoing edges were byte-verified against prior inspected versions. Twenty-six contextual YAMLs comprise 24 unchanged prior readings and two final round102 records verified against their fully read scientific-review inputs. No candidate record is present within this bounded pinned-snapshot and maintained-corpus search.

A document first chooses a label subset c with prior P(c), then a mixing vector lambda from P(lambda&#124;c) with zero mass outside that subset. For each word, a label is sampled from lambda and the word from that label's categorical distribution. Training supplies document label subsets and leaves token-label assignments unobserved. Classifying a new document compares subset scores containing P(c) and the word likelihood integrated over lambda. The presented implementation approximates that integral by evaluating one prior-mode mixture for each subset, rather than fitting or integrating an arbitrary full mixing distribution. The source's first displayed document probability omits P(c); Equation (1) includes it consistently with the generative description. The fitting procedure assigns posterior label responsibilities to words, pools class-word counts across documents, and pools mixture weights over documents with the same observed label subset. Unseen subsets use an overlap-weighted backoff from observed subset mixtures. The reported modifications include leave-one-document-out responsibility estimation, a shared learned background component and a uniform word component. Prediction combines two greedy searches over label subsets; annealing is suggested as another search approach. These approximations and modifications do not establish exact marginalization, globally optimal subset selection, or ordinary full-data EM monotonicity. Limitations: The prior-mode substitution is not generally the integrated likelihood or the posterior mode of lambda given the document. Per-subset parameters and label-subset search become difficult with many labels; the source uses backoff and heuristic search. The reported additive estimate (count+m)/(D+m*number_of_subsets) is a posterior mean under symmetric Dirichlet(m), or an interior MAP estimate under Dirichlet(m+1). With positive m it is not generally MAP under a flat Dirichlet(1), despite the source wording. The m=1 Laplace estimator can be retained without adopting that prior interpretation. Experiments use Reuters-21578 ModApte and particular preprocessing; the ten-class binary naive-Bayes baseline vocabulary was selected on test data, explicitly noted by the author. Preliminary 90-label results report improved macro F1 with unchanged micro F1 and precision/recall tradeoffs. No universal advantage or modern comparative claim follows. Background and uniform components are smoothing/modeling devices, not evidence that every document belongs to a real semantic background class. The original PostScript and converted PDF are separately hashed. No author code or benchmark was executed.

### Identity, model definition, inference interpretation, limitations and mappings

evidence: supported. Targets: AIMech:JointTermCitationModel.

Scoped to Cohn and Hofmann's joint content/connectivity model in The Missing Link. The maintained name describes its term/citation construction; PHITS names a link-only predecessor and is not used as an alias. Fixed document memberships distinguish this PLSA-style model from the integrated Dirichlet word/reference model of Erosheva and colleagues. Link orientation must be specified from the supplied incidence matrix rather than silently treating cited targets and citing sources as interchangeable. No normalized candidate identity matched all 442 pinned AIO IDs, labels and scoped synonyms or 429 preceding native IDs, names and aliases. Full-checkout searches included ignored and hidden files in both checkouts; 23 matching lines per checkout came from four unique file contents containing prior frontier leads and contextual distinctions. All matching excerpts were inspected. The semantic search returned 205 label/synonym hits, with 204 unchanged from prior reading and one newly read. Eighteen annotated AIO CLASS nodes and outgoing edges were byte-verified against prior inspected versions. Twenty-six contextual YAMLs comprise 24 unchanged prior readings and two final round102 records verified against their fully read scientific-review inputs. No candidate record is present within this bounded pinned-snapshot and maintained-corpus search.

Each document d has one fixed topic probability vector theta_d. Topic z has a categorical term distribution phi_z and a separate categorical citation-incidence distribution psi_z. The channel mixtures are P(t&#124;d)=sum_z theta_dz*phi_zt and P(c&#124;d)=sum_z theta_dz*psi_zc. Topic choices are made per observation and share the document weights; the construction is not one latent topic for a whole document and does not integrate a Dirichlet membership prior. The source optimizes alpha times the term log score plus 1-alpha times the link log score, separately normalizing each document's counts in each channel. This weighted criterion gives equal document mass per nonempty channel and differs from the raw-count corpus likelihood. An EM-style fit computes topic responsibilities separately for observed terms and citation incidences, then pools their document-normalized expected counts with channel weights alpha and 1-alpha. Document mixtures combine the two channel responsibility averages, and each topic's emission counts must be normalized over its own channel categories. Equation (3) has an inconsistent document subscript in its first numerator, and the displayed emission updates in Equation (4) omit the final categorical normalization; use the conditioning document and normalized vectors for a coherent probability model. Experiments use tempered responsibilities, so ordinary beta=1 EM monotonicity does not certify the whole temperature schedule. Limitations: The exposition alternates between citing-source and cited-target language: Section 2 defines an incidence matrix as document i cited by j, while PHITS and Section 3 use differing verbal descriptions. The factor equations apply to the chosen orientation, but transposing the matrix changes the modeling task. No unique historical implementation orientation is inferred. The displayed channel normalization is undefined for a document with an empty channel; a complete implementation needs an explicit missing-channel policy. Alpha endpoints discard one channel. Fixed topic count, categorical incidence modeling and fixed document weights constrain generalization; unseen documents require inference of new mixtures. The reported factor-space nearest-neighbor classification, topic counts tied to known category counts, and source-page ranking among random distractors are specific evaluation setups. They do not establish recovery of true classes, universal advantage, or a demonstrated end-to-end web crawler. Reference-flow scores sum over observed link support and use reverse document-given-topic probabilities requiring prior and normalization choices. They are not automatically a calibrated Markov transition or causal information flow. The proposed continuous-state MDP extension is prospective. No author code or benchmark was executed.

### Detailed token-role law versus variant sketches and staged fitting

consistency: supported. Targets: AIMech:RoleAuthorRecipientTopicModel.

Retain the RART family with explicit RART1 and variant boundaries.

Each actor has one role vector used for sending and receiving, while ordered role-pair vectors select topics. A 256-state two-token enumeration verifies 512 collapsed conditionals to 3.7e-16, including repeated use of one actor vector. Integrating shared uniform role proportions gives equal roles with probability 2/3, compared with 1/2 for independent actors. The reported frozen-ART-assignment fit is conditional, not full joint posterior inference. RART2/3 are sketches requiring further specification. Selected role examples and earlier ART perplexity results are not independent RART validation.

### Observed label subsets, latent token labels and approximation

consistency: supported. Targets: AIMech:MultiLabelTextMixtureModel.

Retain the source-defined multi-label mixture.

Classification includes the subset prior and in principle integrates a supported mixing vector. The source instead substitutes a prior-mode mixture, pools parameters over repeated subsets and uses greedy search/backoff. A Beta(2,2) example yields integrated two-word probability 0.3 versus mode substitution 0.25. The Laplace count estimate differs from a flat-Dirichlet MAP estimate. Leave-one-document-out updates and background components do not inherit all exact full-data EM guarantees. Test-selected baseline vocabulary and macro/micro tradeoffs bound empirical interpretation.

### Fixed document mixtures, weighted channels and normalized fitting

consistency: supported. Targets: AIMech:JointTermCitationModel.

Retain the joint term/citation model separately from PHITS and random-membership models.

The criterion normalizes each document channel and combines them with alpha, so it differs from raw-count likelihood. Its displayed emission sums require categorical normalization and its first posterior numerator requires a consistent document index. One finite ordinary-EM step improves the weighted objective from -1.403863553946856 to -1.3010048308859699 after normalized updates. This does not validate the tempered schedule. Incoming-source and outgoing-target interpretations depend on incidence orientation. Reference-flow scores and prospective MDP crawling are not a calibrated transition or causal law.

### Exact source bytes, conversions and empirical limits

consistency: supported. Targets: AIMech:RoleAuthorRecipientTopicModel, AIMech:MultiLabelTextMixtureModel, AIMech:JointTermCitationModel.

Preserve all three inspected primary versions.

The RART source is a 24-page author preprint with placeholder journal metadata; final journal pages must not replace its locators. It was read after the immutable round102 review cutoff. The multi-label source is an author-hosted revised AAAI workshop PostScript, with source and derived PDF hashes kept separate after successful conversion using installed gs-noX11. The joint paper is NIPS 2000, also cited as 2001 proceedings. All 38 pages were visually read. No source code, email corpus or benchmark was executed.

### Model/task mapping direction and neighboring constructions

grounding: supported. Targets: AIMech:RoleAuthorRecipientTopicModel, AIMech:MultiLabelTextMixtureModel, AIMech:JointTermCitationModel.

Retain three distinct native model families.

All three source-defined families map broadly to AIO Model. RART and the joint term/citation model map related to task-scoped ProbabilisticTopicModel; the multi-label text mixture maps related to Classification. The latter predicts subsets rather than mutually exclusive BinaryClassification or MulticlassClassification outcomes. SupervisedLearning describes the label-observed task, not the full probability law. RART introduces actor-role vectors absent from ART and author-topic models; PersonalizedLLM is not an exact target. Joint fixed document memberships differ from integrated Dirichlet scientific-publication memberships and from an end-to-end MultimodalLanguageModel. BayesianNetwork and task-scoped ProbabilisticGraphicalModel are broader graphical descriptions. The pinned RepresentationLearning class is a deep-neural-network subclass, so its label alone does not justify mapping these classical models there. Observational role or link associations do not imply CausalGraphicalModel. Gibbs, EM and hierarchical mixtures of experts are contextual distinctions, not aliases or renewed review targets.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:RoleAuthorRecipientTopicModel, AIMech:MultiLabelTextMixtureModel, AIMech:JointTermCitationModel. Actor-role topic mixtures, observed-label token mixtures and fixed document content/link mixtures are distinct generative constructions. Broad Model and related topic/classification task mappings preserve AIO abstraction without forcing exact matches.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T001312Z-roles-labels-and-links.json | supports | No normalized candidate identity matched all 442 pinned AIO IDs, labels and scoped synonyms or 429 preceding native IDs, names and aliases. Full-checkout searches included ignored and hidden files in both checkouts; 23 matching lines per checkout came from four unique file contents containing prior frontier leads and contextual distinctions. All matching excerpts were inspected. The semantic search returned 205 label/synonym hits, with 204 unchanged from prior reading and one newly read. Eighteen annotated AIO CLASS nodes and outgoing edges were byte-verified against prior inspected versions. Twenty-six contextual YAMLs comprise 24 unchanged prior readings and two final round102 records verified against their fully read scientific-review inputs. No candidate record is present within this bounded pinned-snapshot and maintained-corpus search. |
| mapping | sources/aio/aio.json; 18 exact annotated CLASS nodes and outgoing edges, all unchanged from prior inspection; 205 label/synonym hits with 204 unchanged and one fresh hit | supports | All three source-defined families map broadly to AIO Model. RART and the joint term/citation model map related to task-scoped ProbabilisticTopicModel; the multi-label text mixture maps related to Classification. The latter predicts subsets rather than mutually exclusive BinaryClassification or MulticlassClassification outcomes. SupervisedLearning describes the label-observed task, not the full probability law. RART introduces actor-role vectors absent from ART and author-topic models; PersonalizedLLM is not an exact target. Joint fixed document memberships differ from integrated Dirichlet scientific-publication memberships and from an end-to-end MultimodalLanguageModel. BayesianNetwork and task-scoped ProbabilisticGraphicalModel are broader graphical descriptions. The pinned RepresentationLearning class is a deep-neural-network subclass, so its label alone does not justify mapping these classical models there. Observational role or link associations do not imply CausalGraphicalModel. Gibbs, EM and hierarchical mixtures of experts are contextual distinctions, not aliases or renewed review targets. |
| neighbors | research/discovery/20261012T001312Z-roles-labels-and-links.json; Eight native neighbors and 18 generated contextual YAMLs in source_analysis.context_reading | supports | Native LDA, PLSA, author-topic, ART, scientific-publication mixed-membership, Gibbs, EM and hierarchical mixture-of-experts records inform identity distinctions. Twenty-four contextual files are unchanged from prior readings; two round102 records match fully read final review inputs. No contextual record receives renewed scientific approval. |
| finite-boundaries | research/discovery/role-and-document-boundaries.py; RART collapsed probabilities, shared actor-role integration, prior-mode substitution, smoothing and normalized weighted-channel EM | supports | A two-token RART1 enumeration compares 512 local conditional distributions with exact integrated assignment weights over 256 states, including the same actor as sender and recipient. Shared uniform actor-role draws agree with probability 2/3, versus 1/2 for independent actors. A Beta(2,2) label mixture gives an integrated two-word probability 0.3 versus prior-mode substitution 0.25. Additive pseudocount estimates differ from flat-Dirichlet MAP. One ordinary beta=1 weighted-channel EM step increases its normalized objective only after categorical emission normalization; this finite witness does not certify the tempered experimental schedule. No source implementation or benchmark was executed. |
| roleauthorrecipienttopicmodel-source-0 | https://people.cs.umass.edu/~mccallum/papers/art-jair07.pdf; Section 5, preprint pp.18-19, RART1 generative description and joint distribution; Section 5, preprint pp.18-19; Section 6, pp.19-20; Appendix A, pp.21-22; Section 5, preprint printed/PDF pp.17-19 and Figure 6 p.18 | supports | Topic and Role Discovery in Social Networks with Experiments on Enron and Academic Email. Author-hosted 24-page 2007 preprint; all pages visually read. Its header has volume 29 and placeholder pages, whereas final JAIR metadata gives volume 30, pages 249-272, October 13, 2007. Locators refer to the inspected preprint printed/PDF pages, not final journal pagination. All pages of the primary PDF were visually read. Curator qualifications and synthetic calculations are distinguished from historical empirical claims and uninspected implementations. |
| multilabeltextmixturemodel-source-0 | https://people.cs.umass.edu/~mccallum/papers/multilabel-nips99s.ps; Section 2 Parameter Estimation and Additional Features, converted PDF pp.3-4; Section 2, converted PDF pp.2-3, first document-probability display and Equation (1); Section 2, converted PDF pp.2-3, generative process and Equation (1) | supports | Multi-Label Text Classification with a Mixture Model Trained by EM. Author-hosted revised AAAI 1999 Workshop on Text Learning paper, identified by the primary author index. The nips99s filename does not establish NIPS publication. Original PostScript SHA256 is recorded here; seven converted PDF pages were visually read. Conversion used installed gs-noX11 9.07 after gs-X11 failed to load an X11 library. Derived PDF SHA256: d9dde9f407912c56f6cf70c60209ced4eded0efb4e531cbd3327f02c329dc864. Locators use converted PDF pages; no numeric printed labels are visible. All seven derived PDF pages were visually read; the original PostScript and converted PDF are separately hashed. Curator qualifications and synthetic calculations are distinguished from historical empirical claims and uninspected implementations. |
| jointtermcitationmodel-source-0 | https://papers.nips.cc/paper_files/paper/2000/file/f45a1078feb35de77d26b3f7a52ef502-Paper.pdf; Section 3, PDF p.4, Equations (3)-(5); Section 4.1, PDF p.5, tempering settings; Section 3, PDF pp.3-4, channel mixtures and Equation (2); Sections 2-3, PDF pp.2-4, mixture equations and joint criterion (2) | supports | The Missing Link - A Probabilistic Model of Document Content and Hypertext Connectivity. Official NIPS 2000 volume 13 seven-page PDF, also cited with 2001 proceedings publication year. All pages visually read; locators use PDF page numbers, with no numeric printed labels visible. All pages of the primary PDF were visually read. Curator qualifications and synthetic calculations are distinguished from historical empirical claims and uninspected implementations. |

## Limits And Additional Notes

- Adversarial author self-review only; all three records remain DRAFT.
- All 38 pages of the three primary documents were visually read, including equations, tables and bibliography. No extracted-text reading or source-code execution is asserted.
- The 24-page ART journal preprint was read after the immutable round102 review cutoff. Its header has placeholder metadata; official final JAIR metadata differs. Current locators refer to the inspected preprint, not final journal pages.
- The multi-label source is original author-hosted PostScript, identified as a revised AAAI 1999 workshop paper by the author index. Filename alone does not establish NIPS publication. Source and derived PDF have separate SHA256 hashes.
- The default gs-X11 conversion failed because an X11 library was missing. The already installed gs-noX11 9.07 converted the same source successfully with SAFER; no package installation or source alteration was needed. Its access timestamp is the completed source-file modification time retained after the failed first conversion.
- The official joint model PDF is NIPS 2000, also cited with 2001 publication year. Its notation and normalization issues are qualified without assuming unseen implementation defects. Link orientation remains an explicit modeling choice.
- Two selected frontier constructions are represented; RART1 is detailed but RART2/3 sketches remain unresolved. Nine new provisional reference cohorts leave 277 pending leads and other unresolved dispositions. All three records remain DRAFT.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T001653Z-roles-labels-and-links
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of role, label-subset and joint content-link models
started_at: '2026-10-12T00:13:34Z'
finished_at: '2026-10-12T00:16:53Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially read all fields of three final
    records against 38 complete primary pages, 18 annotated AIO nodes and eight native
    contextual records. Finite calculations tested collapsed role conditionals, shared
    latent integration, mode substitution, smoothing and normalized weighted-channel
    EM. This is author self-review, not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain three DRAFT model families for actor roles, observed label subsets
  and fixed shared content/link mixtures. Explicit qualifications distinguish detailed
  model laws, variant sketches, approximate fitting and bounded empirical evidence.
  No actionable curation finding remains in this selected cohort.
source:
  git_revision: 082bd4895143a63badf7fee58cdd27d1fc8eba39
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/BinaryClassification.yaml
    sha256: 4c710e70fe7e71227f0c6aa55162a3683f04ebbe6f5a4601bd4c0398329f1481
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
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
  - path: data/aio/MulticlassClassification.yaml
    sha256: dcf165047485763fd91782b9a9ba43202d58f00fd33b8545893a5eae327de171
    role: context
  - path: data/aio/MultimodalLanguageModel.yaml
    sha256: da9972da8d9ca9552bfe9fd98b11d2e5dc9a43c52c7acdd169d1f548096cfb7a
    role: context
  - path: data/aio/MultimodalLearning.yaml
    sha256: 9e8bd52f242bf2d17bb0d9f5f795327a2067c17a855d47eb1e45630917ead603
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
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/AuthorRecipientTopicModel.yaml
    sha256: e906455576ea983190e281e60361efd6a1dd11d1c5f37531b467bcdf926f7fdd
    role: context
  - path: data/curated/AuthorTopicModel.yaml
    sha256: 732dd9bc7f7bfbfb461f4cca668f72b128449e27f4008a0e9a3cd90c15e8a28f
    role: context
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: context
  - path: data/curated/GibbsSampling.yaml
    sha256: 8175215986c0507e3664a3aedf8074fc067d85b4a89002091d1bcb9b637a522a
    role: context
  - path: data/curated/HierarchicalMixtureOfExperts.yaml
    sha256: 726b98de332b75f77dc51f3028687650e2077216f26100a16c6fc4e8328c4e18
    role: context
  - path: data/curated/JointTermCitationModel.yaml
    sha256: 535130ed54cd0bf2349b6a9b01722f2fc0c208f0babbb191bfcd79a192fb46aa
    role: target
  - path: data/curated/LatentDirichletAllocation.yaml
    sha256: d8147371973fa1a5d5e9d3487d092e64ab70271ab42c18d199cd868bb8eb5aef
    role: context
  - path: data/curated/MixedMembershipModelForScientificPublications.yaml
    sha256: 8bbada318bcfe72091e5502a71f915865cf52aea741a6d969994c7ed82c05c38
    role: context
  - path: data/curated/MultiLabelTextMixtureModel.yaml
    sha256: baf8834cebe5f37264230a16428c7b7541681e3ef35dccddf19149aa46003ed0
    role: target
  - path: data/curated/ProbabilisticLatentSemanticAnalysis.yaml
    sha256: e9cb970e4795b65a17c073a109b4716fc42f2aa0661bf3f7be128568b19ecc71
    role: context
  - path: data/curated/RoleAuthorRecipientTopicModel.yaml
    sha256: 1f22184307bfa7532dbb73665fcc914eff9d31072c5f2acaa0701e3e587ae7ce
    role: target
  - path: research/discovery/20261012T001312Z-roles-labels-and-links.json
    sha256: 7b1f87c7893beb4e699e6d01e0840e01487905f23bbf632b4fbce994b5de47e6
    role: context
  - path: research/discovery/role-and-document-boundaries.py
    sha256: 7dac1e73046ff8f6b41650e52975052cedc51dbb17450cd4bb1a68cd850299a3
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
- target_id: AIMech:RoleAuthorRecipientTopicModel
  path: data/curated/RoleAuthorRecipientTopicModel.yaml
  label: Role-author-recipient-topic model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RoleAuthorRecipientTopicModel.yaml
    role: maintained
- target_id: AIMech:MultiLabelTextMixtureModel
  path: data/curated/MultiLabelTextMixtureModel.yaml
  label: Multi-label text mixture model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MultiLabelTextMixtureModel.yaml
    role: maintained
- target_id: AIMech:JointTermCitationModel
  path: data/curated/JointTermCitationModel.yaml
  label: Joint term-citation model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/JointTermCitationModel.yaml
    role: maintained
scope:
  description: All fields of three maintained probability-model records.
  selection: Exact maintained IDs RoleAuthorRecipientTopicModel, MultiLabelTextMixtureModel
    and JointTermCitationModel; complete selected cohort without sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:RoleAuthorRecipientTopicModel
  - AIMech:MultiLabelTextMixtureModel
  - AIMech:JointTermCitationModel
  exclusions:
  - target: Author software, trained instances and empirical reproduction
    reason: No author implementation or benchmark was executed. Finite curator calculations
      do not certify historical software, chain mixing or empirical findings.
  - target: Contextual records, variant sketches and remaining frontier
    reason: Context informs identity without renewed scientific approval. Nine new
      reference cohorts, 277 pending leads and other unresolved dispositions remain.
      RART2/3 sketches require additional primary specification before independent
      algorithm curation.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:RoleAuthorRecipientTopicModel
  - AIMech:MultiLabelTextMixtureModel
  - AIMech:JointTermCitationModel
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 100.33s (0:01:40)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 432 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 125 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 122,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:RoleAuthorRecipientTopicModel
  - AIMech:MultiLabelTextMixtureModel
  - AIMech:JointTermCitationModel
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
  - AIMech:RoleAuthorRecipientTopicModel
  - AIMech:MultiLabelTextMixtureModel
  - AIMech:JointTermCitationModel
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
  - AIMech:RoleAuthorRecipientTopicModel
  - AIMech:MultiLabelTextMixtureModel
  - AIMech:JointTermCitationModel
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Role, label-mixture and joint-channel probability boundaries
  command: python3 research/discovery/role-and-document-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:RoleAuthorRecipientTopicModel
  - AIMech:MultiLabelTextMixtureModel
  - AIMech:JointTermCitationModel
  exit_code: 0
  expected_exit_code: 0
  summary: '{"rart_assignment_states": 256, "rart_conditional_checks": 512, "maximum_rart_conditional_error":
    3.608224830031759e-16, "same_actor_equal_role_probability": 0.6666666666666662,
    "independent_actors_equal_role_probability": 0.5, "integrated_multilabel_two_word_probability":
    0.30000000000000004, "mode_substitution_two_word_probability": 0.25, "additive_smoothing":
    [0.6666666666666666, 0.3333333333333333], "flat_dirichlet_map": [0.75, 0.25],
    "joint_channel_objective_before": -1.403863553946856, "joint_channel_objective_after":
    -1.3010048308859699, "unnormalized_emission_row_sums": [[0.6151384615384615, 0.5848615384615384],
    [0.49903846153846154, 0.3009615384615385]], "scope": "Finite synthetic probability
    and ordinary-EM checks, not source code or benchmarks."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T001312Z-roles-labels-and-links.json
  accessed_at: '2026-10-12T00:13:34Z'
  support: supports
  summary: No normalized candidate identity matched all 442 pinned AIO IDs, labels
    and scoped synonyms or 429 preceding native IDs, names and aliases. Full-checkout
    searches included ignored and hidden files in both checkouts; 23 matching lines
    per checkout came from four unique file contents containing prior frontier leads
    and contextual distinctions. All matching excerpts were inspected. The semantic
    search returned 205 label/synonym hits, with 204 unchanged from prior reading
    and one newly read. Eighteen annotated AIO CLASS nodes and outgoing edges were
    byte-verified against prior inspected versions. Twenty-six contextual YAMLs comprise
    24 unchanged prior readings and two final round102 records verified against their
    fully read scientific-review inputs. No candidate record is present within this
    bounded pinned-snapshot and maintained-corpus search.
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison; short acronyms were omitted
    from broad substring searches to avoid irrelevant matches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 18 exact annotated CLASS nodes and outgoing edges, all unchanged from prior
    inspection; 205 label/synonym hits with 204 unchanged and one fresh hit
  accessed_at: '2026-10-12T00:13:34Z'
  support: supports
  summary: All three source-defined families map broadly to AIO Model. RART and the
    joint term/citation model map related to task-scoped ProbabilisticTopicModel;
    the multi-label text mixture maps related to Classification. The latter predicts
    subsets rather than mutually exclusive BinaryClassification or MulticlassClassification
    outcomes. SupervisedLearning describes the label-observed task, not the full probability
    law. RART introduces actor-role vectors absent from ART and author-topic models;
    PersonalizedLLM is not an exact target. Joint fixed document memberships differ
    from integrated Dirichlet scientific-publication memberships and from an end-to-end
    MultimodalLanguageModel. BayesianNetwork and task-scoped ProbabilisticGraphicalModel
    are broader graphical descriptions. The pinned RepresentationLearning class is
    a deep-neural-network subclass, so its label alone does not justify mapping these
    classical models there. Observational role or link associations do not imply CausalGraphicalModel.
    Gibbs, EM and hierarchical mixtures of experts are contextual distinctions, not
    aliases or renewed review targets.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261012T001312Z-roles-labels-and-links.json
  locator: Eight native neighbors and 18 generated contextual YAMLs in source_analysis.context_reading
  accessed_at: '2026-10-12T00:13:34Z'
  support: supports
  summary: Native LDA, PLSA, author-topic, ART, scientific-publication mixed-membership,
    Gibbs, EM and hierarchical mixture-of-experts records inform identity distinctions.
    Twenty-four contextual files are unchanged from prior readings; two round102 records
    match fully read final review inputs. No contextual record receives renewed scientific
    approval.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/role-and-document-boundaries.py
  locator: RART collapsed probabilities, shared actor-role integration, prior-mode
    substitution, smoothing and normalized weighted-channel EM
  accessed_at: '2026-10-12T00:13:34Z'
  snapshot_sha256: 7dac1e73046ff8f6b41650e52975052cedc51dbb17450cd4bb1a68cd850299a3
  support: supports
  summary: A two-token RART1 enumeration compares 512 local conditional distributions
    with exact integrated assignment weights over 256 states, including the same actor
    as sender and recipient. Shared uniform actor-role draws agree with probability
    2/3, versus 1/2 for independent actors. A Beta(2,2) label mixture gives an integrated
    two-word probability 0.3 versus prior-mode substitution 0.25. Additive pseudocount
    estimates differ from flat-Dirichlet MAP. One ordinary beta=1 weighted-channel
    EM step increases its normalized objective only after categorical emission normalization;
    this finite witness does not certify the tempered experimental schedule. No source
    implementation or benchmark was executed.
- evidence_id: roleauthorrecipienttopicmodel-source-0
  kind: primary_source
  reference: https://people.cs.umass.edu/~mccallum/papers/art-jair07.pdf
  locator: Section 5, preprint pp.18-19, RART1 generative description and joint distribution;
    Section 5, preprint pp.18-19; Section 6, pp.19-20; Appendix A, pp.21-22; Section
    5, preprint printed/PDF pp.17-19 and Figure 6 p.18
  accessed_at: '2026-10-12T00:01:18Z'
  snapshot_sha256: 40e7acc75fcad244773926272f97c835f0eb3ad56dfd5d15a64413c6765acbfc
  support: supports
  summary: Topic and Role Discovery in Social Networks with Experiments on Enron and
    Academic Email. Author-hosted 24-page 2007 preprint; all pages visually read.
    Its header has volume 29 and placeholder pages, whereas final JAIR metadata gives
    volume 30, pages 249-272, October 13, 2007. Locators refer to the inspected preprint
    printed/PDF pages, not final journal pagination. All pages of the primary PDF
    were visually read. Curator qualifications and synthetic calculations are distinguished
    from historical empirical claims and uninspected implementations.
- evidence_id: multilabeltextmixturemodel-source-0
  kind: primary_source
  reference: https://people.cs.umass.edu/~mccallum/papers/multilabel-nips99s.ps
  locator: Section 2 Parameter Estimation and Additional Features, converted PDF pp.3-4;
    Section 2, converted PDF pp.2-3, first document-probability display and Equation
    (1); Section 2, converted PDF pp.2-3, generative process and Equation (1)
  accessed_at: '2026-10-12T00:01:49Z'
  snapshot_sha256: 165bb4792e919794f752e30c50747e60aa7411542aeaa79e31d2ff97fa5ec6ba
  support: supports
  summary: 'Multi-Label Text Classification with a Mixture Model Trained by EM. Author-hosted
    revised AAAI 1999 Workshop on Text Learning paper, identified by the primary author
    index. The nips99s filename does not establish NIPS publication. Original PostScript
    SHA256 is recorded here; seven converted PDF pages were visually read. Conversion
    used installed gs-noX11 9.07 after gs-X11 failed to load an X11 library. Derived
    PDF SHA256: d9dde9f407912c56f6cf70c60209ced4eded0efb4e531cbd3327f02c329dc864.
    Locators use converted PDF pages; no numeric printed labels are visible. All seven
    derived PDF pages were visually read; the original PostScript and converted PDF
    are separately hashed. Curator qualifications and synthetic calculations are distinguished
    from historical empirical claims and uninspected implementations.'
- evidence_id: jointtermcitationmodel-source-0
  kind: primary_source
  reference: https://papers.nips.cc/paper_files/paper/2000/file/f45a1078feb35de77d26b3f7a52ef502-Paper.pdf
  locator: Section 3, PDF p.4, Equations (3)-(5); Section 4.1, PDF p.5, tempering
    settings; Section 3, PDF pp.3-4, channel mixtures and Equation (2); Sections 2-3,
    PDF pp.2-4, mixture equations and joint criterion (2)
  accessed_at: '2026-10-12T00:01:25Z'
  snapshot_sha256: d0deb7b9c084c7bcd3f2a341dd699d6bf4a5a73c80f575ee59acb41bc28a28c7
  support: supports
  summary: The Missing Link - A Probabilistic Model of Document Content and Hypertext
    Connectivity. Official NIPS 2000 volume 13 seven-page PDF, also cited with 2001
    proceedings publication year. All pages visually read; locators use PDF page numbers,
    with no numeric printed labels visible. All pages of the primary PDF were visually
    read. Curator qualifications and synthetic calculations are distinguished from
    historical empirical claims and uninspected implementations.
assessments:
- assessment_id: roleauthorrecipienttopicmodel
  area: evidence
  topic: Identity, model definition, inference interpretation, limitations and mappings
  outcome: supported
  target_ids:
  - AIMech:RoleAuthorRecipientTopicModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - roleauthorrecipienttopicmodel-source-0
  summary: Scoped to the RART family introduced by McCallum and colleagues, with the
    2007 preprint specifying RART1 in detail and sketching RART2 and RART3. RART1
    draws both roles per token; RART2 fixes a sender role and individual recipient
    roles per message; RART3 uses one common recipient role per message. The latter
    sketches are not asserted to provide complete independent inference algorithms.
    Explicit actor roles distinguish this family from ART pair-specific topic vectors
    and author-topic models. RART is a source acronym within this scope. No normalized
    candidate identity matched all 442 pinned AIO IDs, labels and scoped synonyms
    or 429 preceding native IDs, names and aliases. Full-checkout searches included
    ignored and hidden files in both checkouts; 23 matching lines per checkout came
    from four unique file contents containing prior frontier leads and contextual
    distinctions. All matching excerpts were inspected. The semantic search returned
    205 label/synonym hits, with 204 unchanged from prior reading and one newly read.
    Eighteen annotated AIO CLASS nodes and outgoing edges were byte-verified against
    prior inspected versions. Twenty-six contextual YAMLs comprise 24 unchanged prior
    readings and two final round102 records verified against their fully read scientific-review
    inputs. No candidate record is present within this bounded pinned-snapshot and
    maintained-corpus search.
  details: 'In RART1, each actor has a Dirichlet-distributed role vector psi, each
    ordered sender-role/recipient-role pair has a Dirichlet topic vector theta, and
    each topic has a Dirichlet word vector phi. Given observed sender a and a nonempty
    recipient set R, a token chooses r uniformly from R, sender role g from psi_a,
    recipient role h from psi_r, topic z from theta_gh, then word w from phi_z. An
    actor uses the same role vector for sending and receiving, while theta distinguishes
    the order of the roles. The model conditions on participants and message lengths
    rather than generating network edges. Shared random vectors must be integrated
    jointly across their uses; two roles drawn for the same actor need not be independent
    after psi is integrated out. The reported RART1 experiment first fits ART, fixes
    topic and recipient assignments from one sample, and then infers the role structure
    conditionally on those assignments. This staged procedure does not sample the
    full joint RART posterior or propagate all uncertainty in the frozen assignments.
    The source states that general Gibbs updates can be derived, but its Appendix
    A derives ART updates, not a complete RART sampler. Conditional on fixed parameters,
    token role choices can vary within a message; RART2 and RART3 impose different
    message-level sharing and cannot be substituted without changing the model. Limitations:
    Only RART1 has a detailed generative specification in this source. The RART2/3
    diagrams and prose leave further implementation and inference choices for exploration;
    family coverage does not certify fully specified variants. The demonstrated 15-role,
    50-topic fit is illustrated by selected email users and manually named roles in
    Tables 6-7. Some apparently unrelated assignments remain unexplained, and entity-resolution
    errors are present. These examples do not establish verified occupations, expertise,
    causal influence or universal predictive superiority. Earlier ART perplexity results
    are not RART benchmark results. Fixed role/topic counts, bag-of-words observations,
    uniform recipient selection and corpus-specific participation affect identifiability
    and interpretation. Latent role labels are exchangeable; semantic names are human
    interpretations. A single ART sample judged plausible does not establish adequate
    uncertainty propagation or convergence. Finite synthetic collapsed-probability
    checks cover the specified RART1 factorization, including a shared actor in sender
    and recipient positions. They are not a reproduction of historical software, email
    preprocessing or the reported benchmark.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A specified latent-variable probability-model family, not a trained
      instance or merely its fitting algorithm.
    evidence_ids:
    - roleauthorrecipienttopicmodel-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: All three source-defined families map broadly to AIO Model. RART and
      the joint term/citation model map related to task-scoped ProbabilisticTopicModel;
      the multi-label text mixture maps related to Classification. The latter predicts
      subsets rather than mutually exclusive BinaryClassification or MulticlassClassification
      outcomes. SupervisedLearning describes the label-observed task, not the full
      probability law. RART introduces actor-role vectors absent from ART and author-topic
      models; PersonalizedLLM is not an exact target. Joint fixed document memberships
      differ from integrated Dirichlet scientific-publication memberships and from
      an end-to-end MultimodalLanguageModel. BayesianNetwork and task-scoped ProbabilisticGraphicalModel
      are broader graphical descriptions. The pinned RepresentationLearning class
      is a deep-neural-network subclass, so its label alone does not justify mapping
      these classical models there. Observational role or link associations do not
      imply CausalGraphicalModel. Gibbs, EM and hierarchical mixtures of experts are
      contextual distinctions, not aliases or renewed review targets.
    evidence_ids:
    - mapping
- assessment_id: multilabeltextmixturemodel
  area: evidence
  topic: Identity, model definition, inference interpretation, limitations and mappings
  outcome: supported
  target_ids:
  - AIMech:MultiLabelTextMixtureModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - multilabeltextmixturemodel-source-0
  summary: Scoped to McCallum's 1999 mixture model for multi-label text classification,
    whose training observes document label sets while token labels are latent. The
    maintained name describes this source construction; no source acronym is invented.
    It differs from independent binary classifiers, mutually exclusive multiclass
    classification and unsupervised topic discovery. The uniform author-word comparator
    cited by later author-topic papers is a simplified case, not an alias for the
    full learned label-mixture construction. No normalized candidate identity matched
    all 442 pinned AIO IDs, labels and scoped synonyms or 429 preceding native IDs,
    names and aliases. Full-checkout searches included ignored and hidden files in
    both checkouts; 23 matching lines per checkout came from four unique file contents
    containing prior frontier leads and contextual distinctions. All matching excerpts
    were inspected. The semantic search returned 205 label/synonym hits, with 204
    unchanged from prior reading and one newly read. Eighteen annotated AIO CLASS
    nodes and outgoing edges were byte-verified against prior inspected versions.
    Twenty-six contextual YAMLs comprise 24 unchanged prior readings and two final
    round102 records verified against their fully read scientific-review inputs. No
    candidate record is present within this bounded pinned-snapshot and maintained-corpus
    search.
  details: 'A document first chooses a label subset c with prior P(c), then a mixing
    vector lambda from P(lambda|c) with zero mass outside that subset. For each word,
    a label is sampled from lambda and the word from that label''s categorical distribution.
    Training supplies document label subsets and leaves token-label assignments unobserved.
    Classifying a new document compares subset scores containing P(c) and the word
    likelihood integrated over lambda. The presented implementation approximates that
    integral by evaluating one prior-mode mixture for each subset, rather than fitting
    or integrating an arbitrary full mixing distribution. The source''s first displayed
    document probability omits P(c); Equation (1) includes it consistently with the
    generative description. The fitting procedure assigns posterior label responsibilities
    to words, pools class-word counts across documents, and pools mixture weights
    over documents with the same observed label subset. Unseen subsets use an overlap-weighted
    backoff from observed subset mixtures. The reported modifications include leave-one-document-out
    responsibility estimation, a shared learned background component and a uniform
    word component. Prediction combines two greedy searches over label subsets; annealing
    is suggested as another search approach. These approximations and modifications
    do not establish exact marginalization, globally optimal subset selection, or
    ordinary full-data EM monotonicity. Limitations: The prior-mode substitution is
    not generally the integrated likelihood or the posterior mode of lambda given
    the document. Per-subset parameters and label-subset search become difficult with
    many labels; the source uses backoff and heuristic search. The reported additive
    estimate (count+m)/(D+m*number_of_subsets) is a posterior mean under symmetric
    Dirichlet(m), or an interior MAP estimate under Dirichlet(m+1). With positive
    m it is not generally MAP under a flat Dirichlet(1), despite the source wording.
    The m=1 Laplace estimator can be retained without adopting that prior interpretation.
    Experiments use Reuters-21578 ModApte and particular preprocessing; the ten-class
    binary naive-Bayes baseline vocabulary was selected on test data, explicitly noted
    by the author. Preliminary 90-label results report improved macro F1 with unchanged
    micro F1 and precision/recall tradeoffs. No universal advantage or modern comparative
    claim follows. Background and uniform components are smoothing/modeling devices,
    not evidence that every document belongs to a real semantic background class.
    The original PostScript and converted PDF are separately hashed. No author code
    or benchmark was executed.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A specified latent-variable probability-model family, not a trained
      instance or merely its fitting algorithm.
    evidence_ids:
    - multilabeltextmixturemodel-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: All three source-defined families map broadly to AIO Model. RART and
      the joint term/citation model map related to task-scoped ProbabilisticTopicModel;
      the multi-label text mixture maps related to Classification. The latter predicts
      subsets rather than mutually exclusive BinaryClassification or MulticlassClassification
      outcomes. SupervisedLearning describes the label-observed task, not the full
      probability law. RART introduces actor-role vectors absent from ART and author-topic
      models; PersonalizedLLM is not an exact target. Joint fixed document memberships
      differ from integrated Dirichlet scientific-publication memberships and from
      an end-to-end MultimodalLanguageModel. BayesianNetwork and task-scoped ProbabilisticGraphicalModel
      are broader graphical descriptions. The pinned RepresentationLearning class
      is a deep-neural-network subclass, so its label alone does not justify mapping
      these classical models there. Observational role or link associations do not
      imply CausalGraphicalModel. Gibbs, EM and hierarchical mixtures of experts are
      contextual distinctions, not aliases or renewed review targets.
    evidence_ids:
    - mapping
- assessment_id: jointtermcitationmodel
  area: evidence
  topic: Identity, model definition, inference interpretation, limitations and mappings
  outcome: supported
  target_ids:
  - AIMech:JointTermCitationModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - jointtermcitationmodel-source-0
  summary: Scoped to Cohn and Hofmann's joint content/connectivity model in The Missing
    Link. The maintained name describes its term/citation construction; PHITS names
    a link-only predecessor and is not used as an alias. Fixed document memberships
    distinguish this PLSA-style model from the integrated Dirichlet word/reference
    model of Erosheva and colleagues. Link orientation must be specified from the
    supplied incidence matrix rather than silently treating cited targets and citing
    sources as interchangeable. No normalized candidate identity matched all 442 pinned
    AIO IDs, labels and scoped synonyms or 429 preceding native IDs, names and aliases.
    Full-checkout searches included ignored and hidden files in both checkouts; 23
    matching lines per checkout came from four unique file contents containing prior
    frontier leads and contextual distinctions. All matching excerpts were inspected.
    The semantic search returned 205 label/synonym hits, with 204 unchanged from prior
    reading and one newly read. Eighteen annotated AIO CLASS nodes and outgoing edges
    were byte-verified against prior inspected versions. Twenty-six contextual YAMLs
    comprise 24 unchanged prior readings and two final round102 records verified against
    their fully read scientific-review inputs. No candidate record is present within
    this bounded pinned-snapshot and maintained-corpus search.
  details: 'Each document d has one fixed topic probability vector theta_d. Topic
    z has a categorical term distribution phi_z and a separate categorical citation-incidence
    distribution psi_z. The channel mixtures are P(t|d)=sum_z theta_dz*phi_zt and
    P(c|d)=sum_z theta_dz*psi_zc. Topic choices are made per observation and share
    the document weights; the construction is not one latent topic for a whole document
    and does not integrate a Dirichlet membership prior. The source optimizes alpha
    times the term log score plus 1-alpha times the link log score, separately normalizing
    each document''s counts in each channel. This weighted criterion gives equal document
    mass per nonempty channel and differs from the raw-count corpus likelihood. An
    EM-style fit computes topic responsibilities separately for observed terms and
    citation incidences, then pools their document-normalized expected counts with
    channel weights alpha and 1-alpha. Document mixtures combine the two channel responsibility
    averages, and each topic''s emission counts must be normalized over its own channel
    categories. Equation (3) has an inconsistent document subscript in its first numerator,
    and the displayed emission updates in Equation (4) omit the final categorical
    normalization; use the conditioning document and normalized vectors for a coherent
    probability model. Experiments use tempered responsibilities, so ordinary beta=1
    EM monotonicity does not certify the whole temperature schedule. Limitations:
    The exposition alternates between citing-source and cited-target language: Section
    2 defines an incidence matrix as document i cited by j, while PHITS and Section
    3 use differing verbal descriptions. The factor equations apply to the chosen
    orientation, but transposing the matrix changes the modeling task. No unique historical
    implementation orientation is inferred. The displayed channel normalization is
    undefined for a document with an empty channel; a complete implementation needs
    an explicit missing-channel policy. Alpha endpoints discard one channel. Fixed
    topic count, categorical incidence modeling and fixed document weights constrain
    generalization; unseen documents require inference of new mixtures. The reported
    factor-space nearest-neighbor classification, topic counts tied to known category
    counts, and source-page ranking among random distractors are specific evaluation
    setups. They do not establish recovery of true classes, universal advantage, or
    a demonstrated end-to-end web crawler. Reference-flow scores sum over observed
    link support and use reverse document-given-topic probabilities requiring prior
    and normalization choices. They are not automatically a calibrated Markov transition
    or causal information flow. The proposed continuous-state MDP extension is prospective.
    No author code or benchmark was executed.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A specified latent-variable probability-model family, not a trained
      instance or merely its fitting algorithm.
    evidence_ids:
    - jointtermcitationmodel-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: All three source-defined families map broadly to AIO Model. RART and
      the joint term/citation model map related to task-scoped ProbabilisticTopicModel;
      the multi-label text mixture maps related to Classification. The latter predicts
      subsets rather than mutually exclusive BinaryClassification or MulticlassClassification
      outcomes. SupervisedLearning describes the label-observed task, not the full
      probability law. RART introduces actor-role vectors absent from ART and author-topic
      models; PersonalizedLLM is not an exact target. Joint fixed document memberships
      differ from integrated Dirichlet scientific-publication memberships and from
      an end-to-end MultimodalLanguageModel. BayesianNetwork and task-scoped ProbabilisticGraphicalModel
      are broader graphical descriptions. The pinned RepresentationLearning class
      is a deep-neural-network subclass, so its label alone does not justify mapping
      these classical models there. Observational role or link associations do not
      imply CausalGraphicalModel. Gibbs, EM and hierarchical mixtures of experts are
      contextual distinctions, not aliases or renewed review targets.
    evidence_ids:
    - mapping
- assessment_id: rart-roles
  area: consistency
  topic: Detailed token-role law versus variant sketches and staged fitting
  outcome: supported
  target_ids:
  - AIMech:RoleAuthorRecipientTopicModel
  evidence_ids:
  - roleauthorrecipienttopicmodel-source-0
  - finite-boundaries
  - neighbors
  summary: Retain the RART family with explicit RART1 and variant boundaries.
  details: Each actor has one role vector used for sending and receiving, while ordered
    role-pair vectors select topics. A 256-state two-token enumeration verifies 512
    collapsed conditionals to 3.7e-16, including repeated use of one actor vector.
    Integrating shared uniform role proportions gives equal roles with probability
    2/3, compared with 1/2 for independent actors. The reported frozen-ART-assignment
    fit is conditional, not full joint posterior inference. RART2/3 are sketches requiring
    further specification. Selected role examples and earlier ART perplexity results
    are not independent RART validation.
- assessment_id: label-mixture
  area: consistency
  topic: Observed label subsets, latent token labels and approximation
  outcome: supported
  target_ids:
  - AIMech:MultiLabelTextMixtureModel
  evidence_ids:
  - multilabeltextmixturemodel-source-0
  - finite-boundaries
  - neighbors
  summary: Retain the source-defined multi-label mixture.
  details: Classification includes the subset prior and in principle integrates a
    supported mixing vector. The source instead substitutes a prior-mode mixture,
    pools parameters over repeated subsets and uses greedy search/backoff. A Beta(2,2)
    example yields integrated two-word probability 0.3 versus mode substitution 0.25.
    The Laplace count estimate differs from a flat-Dirichlet MAP estimate. Leave-one-document-out
    updates and background components do not inherit all exact full-data EM guarantees.
    Test-selected baseline vocabulary and macro/micro tradeoffs bound empirical interpretation.
- assessment_id: joint-channels
  area: consistency
  topic: Fixed document mixtures, weighted channels and normalized fitting
  outcome: supported
  target_ids:
  - AIMech:JointTermCitationModel
  evidence_ids:
  - jointtermcitationmodel-source-0
  - finite-boundaries
  - neighbors
  summary: Retain the joint term/citation model separately from PHITS and random-membership
    models.
  details: The criterion normalizes each document channel and combines them with alpha,
    so it differs from raw-count likelihood. Its displayed emission sums require categorical
    normalization and its first posterior numerator requires a consistent document
    index. One finite ordinary-EM step improves the weighted objective from -1.403863553946856
    to -1.3010048308859699 after normalized updates. This does not validate the tempered
    schedule. Incoming-source and outgoing-target interpretations depend on incidence
    orientation. Reference-flow scores and prospective MDP crawling are not a calibrated
    transition or causal law.
- assessment_id: versions-and-empirics
  area: consistency
  topic: Exact source bytes, conversions and empirical limits
  outcome: supported
  target_ids:
  - AIMech:RoleAuthorRecipientTopicModel
  - AIMech:MultiLabelTextMixtureModel
  - AIMech:JointTermCitationModel
  evidence_ids:
  - roleauthorrecipienttopicmodel-source-0
  - multilabeltextmixturemodel-source-0
  - jointtermcitationmodel-source-0
  summary: Preserve all three inspected primary versions.
  details: The RART source is a 24-page author preprint with placeholder journal metadata;
    final journal pages must not replace its locators. It was read after the immutable
    round102 review cutoff. The multi-label source is an author-hosted revised AAAI
    workshop PostScript, with source and derived PDF hashes kept separate after successful
    conversion using installed gs-noX11. The joint paper is NIPS 2000, also cited
    as 2001 proceedings. All 38 pages were visually read. No source code, email corpus
    or benchmark was executed.
- assessment_id: mapping-boundary
  area: grounding
  topic: Model/task mapping direction and neighboring constructions
  outcome: supported
  target_ids:
  - AIMech:RoleAuthorRecipientTopicModel
  - AIMech:MultiLabelTextMixtureModel
  - AIMech:JointTermCitationModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain three distinct native model families.
  details: All three source-defined families map broadly to AIO Model. RART and the
    joint term/citation model map related to task-scoped ProbabilisticTopicModel;
    the multi-label text mixture maps related to Classification. The latter predicts
    subsets rather than mutually exclusive BinaryClassification or MulticlassClassification
    outcomes. SupervisedLearning describes the label-observed task, not the full probability
    law. RART introduces actor-role vectors absent from ART and author-topic models;
    PersonalizedLLM is not an exact target. Joint fixed document memberships differ
    from integrated Dirichlet scientific-publication memberships and from an end-to-end
    MultimodalLanguageModel. BayesianNetwork and task-scoped ProbabilisticGraphicalModel
    are broader graphical descriptions. The pinned RepresentationLearning class is
    a deep-neural-network subclass, so its label alone does not justify mapping these
    classical models there. Observational role or link associations do not imply CausalGraphicalModel.
    Gibbs, EM and hierarchical mixtures of experts are contextual distinctions, not
    aliases or renewed review targets.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:RoleAuthorRecipientTopicModel
  - AIMech:MultiLabelTextMixtureModel
  - AIMech:JointTermCitationModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - roleauthorrecipienttopicmodel-source-0
  - multilabeltextmixturemodel-source-0
  - jointtermcitationmodel-source-0
  rationale: Actor-role topic mixtures, observed-label token mixtures and fixed document
    content/link mixtures are distinct generative constructions. Broad Model and related
    topic/classification task mappings preserve AIO abstraction without forcing exact
    matches.
limitations:
- Adversarial author self-review only; all three records remain DRAFT.
- All 38 pages of the three primary documents were visually read, including equations,
  tables and bibliography. No extracted-text reading or source-code execution is asserted.
- The 24-page ART journal preprint was read after the immutable round102 review cutoff.
  Its header has placeholder metadata; official final JAIR metadata differs. Current
  locators refer to the inspected preprint, not final journal pages.
- The multi-label source is original author-hosted PostScript, identified as a revised
  AAAI 1999 workshop paper by the author index. Filename alone does not establish
  NIPS publication. Source and derived PDF have separate SHA256 hashes.
- The default gs-X11 conversion failed because an X11 library was missing. The already
  installed gs-noX11 9.07 converted the same source successfully with SAFER; no package
  installation or source alteration was needed. Its access timestamp is the completed
  source-file modification time retained after the failed first conversion.
- The official joint model PDF is NIPS 2000, also cited with 2001 publication year.
  Its notation and normalization issues are qualified without assuming unseen implementation
  defects. Link orientation remains an explicit modeling choice.
- Two selected frontier constructions are represented; RART1 is detailed but RART2/3
  sketches remain unresolved. Nine new provisional reference cohorts leave 277 pending
  leads and other unresolved dispositions. All three records remain DRAFT.
links: []
tags:
- native-concepts
- roles-labels-links
- self-review
- discovery-ongoing
```
