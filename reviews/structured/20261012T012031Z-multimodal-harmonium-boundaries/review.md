# Scientific self-review of RAP and labeled harmonium model families

- Review: 20261012T012031Z-multimodal-harmonium-boundaries
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T01:16:07Z
- Finished UTC: 2026-10-12T01:20:31Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain RAP, FoH and HH with explicit bounded-hidden, class-normalizer, Gaussian-domain and binary-label boundaries. Defer the earlier unbounded-count DWH specialization rather than silently changing its support. No actionable curation finding remains in the three selected maintained records.

## Scope And Provenance

All fields of three maintained model-family records.

Selection: Exact maintained IDs RateAdaptingPoissonModel, FamilyOfHarmonium and HierarchicalHarmonium; complete selected cohort without sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 87cbd196d7a408f8901996a9633666b13630fca5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:RateAdaptingPoissonModel | data/curated/RateAdaptingPoissonModel.yaml | maintained | Rate-adapting Poisson model |
| AIMech:FamilyOfHarmonium | data/curated/FamilyOfHarmonium.yaml | maintained | Family-of-harmonium |
| AIMech:HierarchicalHarmonium | data/curated/HierarchicalHarmonium.yaml | maintained | Hierarchical harmonium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:RateAdaptingPoissonModel, AIMech:FamilyOfHarmonium, AIMech:HierarchicalHarmonium | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 95.43s (0:01:35)<br>Checked 442 record(s); 0 failed.<br>Checked 447 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 130 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 127,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:RateAdaptingPoissonModel, AIMech:FamilyOfHarmonium, AIMech:HierarchicalHarmonium | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:RateAdaptingPoissonModel, AIMech:FamilyOfHarmonium, AIMech:HierarchicalHarmonium | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:RateAdaptingPoissonModel, AIMech:FamilyOfHarmonium, AIMech:HierarchicalHarmonium | Command exited 0 with no output. |
| env PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-curated | passed | True | AIMech:RateAdaptingPoissonModel, AIMech:FamilyOfHarmonium, AIMech:HierarchicalHarmonium | Checked 447 curated concept record(s); 0 error(s).<br> |
| Multimodal harmonium probability boundaries | passed | True | AIMech:RateAdaptingPoissonModel, AIMech:FamilyOfHarmonium, AIMech:HierarchicalHarmonium | {"rap": {"hidden_states": 6, "checked_hidden_probabilities": 96, "conditional_error": 1.5265566588595902e-16, "marginal_error": 2.220446049250313e-16, "exact_log_normalizer": 3.3751013338131903, "gradient": 0.3021105497615496, "finite_difference": 0.3021105497102994, "complement_error": 8.881784197001252e-16, "normalization": "Finite hidden sum after exact Poisson summation, without truncating visible support."}, "family_of_harmonium": {"class_unnormalized_scores": [1.0202013400267558, 1.6487212707001282], "class_normalizers": [5.170490871695183, 9.977009730616732], "class_densities": [0.19731227949973643, 0.1652520459753237], "raw_winner": 1, "proper_winner": 0, "gaussian_precision_condition": "For identity variances, I-U U^T must be positive definite; equivalently every singular value of U is below one."}, "hierarchical_harmonium": {"binary_label_states": [[0, 0], [0, 1], [1, 0], [1, 1]], "joint_label_probabilities": [0.08556882867798671, 0.14107914795029183, 0.14107914795029183, 0.6322728754214296], "label_marginals": [0.7733520233717215, 0.7733520233717215], "onehot_restricted_probabilities": [0.0, 0.5, 0.5, 0.0], "bernoulli_means_given_h_one": [0.7310585786300049, 0.7310585786300049], "onehot_means_given_h_one": [0.5, 0.5], "logistic_at_posterior_mean": 0.8244371838867636, "exact_label_marginal": 0.7733520233717215, "interpretation": "One-hot training observations do not constrain the binary-cube joint; conditional Bernoulli logits differ from categorical softmax. Integrating a missing label layer yields Gaussian mixtures, not a single plug-in Gaussian."}, "dual_wing_boundary": {"counts": [100, 1000, 10000], "log_integrated_terms": [-163.7393755555634, 14087.87182151184, 1917891.0721631858], "negative_coupling_same_divergence": true, "conclusion": "The unbounded count/unit-Gaussian-hidden specialization is not jointly normalizable for a nonzero count coupling. A proper-support revision or clarification is needed before an asserted native probability-model record.", "additional_display_note": "Poisson base measure is 1/Gamma(n+1), not the printed 1/Gamma(n); correcting that factorial does not repair quadratic tail growth."}, "status": "PASS"} |

## Scientific And Domain Assessments

### Identity, model definition, probability boundaries, limitations and mappings

evidence: supported. Targets: AIMech:RateAdaptingPoissonModel.

Scoped to Gehler, Holub and Welling's ICML2006 RAP construction with fixed finite integer binomial trial counts. This differs from a Gaussian-hidden count harmonium, a two-unbounded-Poisson-layer construction, categorical word-bin EFH and replicated-token Softmax. Baseline Poisson rates and hidden logits are conditional parameters, not generally marginal means or independent hidden priors. The latent count model is distinct from its CD fitting algorithm or a trained retrieval system. No normalized identity matched four candidates against all 442 pinned AIO IDs, labels and scoped synonyms or 444 preceding native IDs, names and aliases. Full-checkout searches included ignored and hidden files in both checkouts; five matching lines per checkout came from two unique prior discovery-ledger contents, and all matching excerpts were read. All 205 semantic label/synonym hits were byte-verified against prior readings. Twenty-nine annotated AIO nodes and outgoing edges comprise 28 unchanged prior readings and one newly read multimodal-deep-learning node. Thirty-nine contextual YAMLs comprise 34 unchanged prior readings and five fully read current records. Three candidates are curated; the unbounded-count DWH specialization remains deferred because the inspected joint is not normalizable with nonzero count couplings. Absence is bounded to this pinned snapshot and maintained corpus.

With baseline log rates a_i, hidden thresholds beta_j, interaction weights W_ij and finite integer trial counts M_j, visible counts conditioned on h are independent Poisson with rates exp(a_i+sum_j W_ij h_j). Hidden variables conditioned on x are independent Binomial(M_j,sigmoid(sum_i W_ij x_i-beta_j)). The joint retains visible factorial and hidden binomial base measures. Summing all visible counts first leaves a finite sum over bounded hidden configurations, proving a finite joint normalizer for finite parameters without truncating visible counts. Marginalizing hidden units gives visible log mass sum_i(a_i x_i-log(x_i!))+sum_j M_j softplus(sum_i W_ij x_i-beta_j), up to a global constant. The hard threshold interpretation is an approximation to softplus, not exact zero influence below a threshold. Complementing a hidden count to M_j-h_j, reversing its weight column and threshold, and adding M_j W_ij to each visible log baseline preserves the normalized visible law. This discrete symmetry does not establish arbitrary orthogonal rotation invariance or full parameter identifiability. Likelihood gradients contrast observed and equilibrium sufficient statistics. Conditional hidden expectations M_j sigmoid(W_j^T x-beta_j) replace sampled hidden counts in the displayed gradient statistics. The reported CD1 procedure draws hidden counts from each observed vector, reconstructs visible counts and uses short-chain negative expectations, introducing approximation bias. Retrieval uses cosine similarity of the linear projection W^T x, which is distinct from the nonlinear conditional-binomial mean and from exact joint likelihood scoring. Limitations: The normalizer is finite but its exact finite hidden sum can grow exponentially with the number and ranges of hidden units. CD, minibatches and momentum do not certify exact maximum likelihood or chain convergence. No noninteger binomial trial-count extension is asserted. The document-retrieval topic dimension is selected using test-set one-nearest-neighbor performance, explicitly stated in the Figure 4 caption. Reported curves therefore do not constitute an independently tuned held-out comparison. The split used for class-informed newsgroup vocabulary selection is insufficiently specified to assert a separate leakage mechanism. RAP is compared with LSI and PLSI on selected text corpora and bag-of-visual-words image tasks. LDA is omitted from the reported comparison. Different retrieval measures and dataset configurations yield different rankings; no universal performance advantage is curated. Finite checks verify 96 hidden conditional probabilities, exact visible marginalization, a likelihood gradient and complement symmetry. No author code, coordinate-mode implementation, empirical benchmark, hierarchical extension or negative-binomial replacement was executed or certified.

### Identity, model definition, probability boundaries, limitations and mappings

evidence: supported. Targets: AIMech:FamilyOfHarmonium.

Scoped to the FoH construction in Yang and colleagues' semantic-video manuscript. Each labeled class owns its parameters and latent coordinates; a categorical class selector has a prior distribution. This differs from the shared label-coupled hierarchical harmonium, an unsupervised single harmonium followed by an SVM, and the earlier unbounded Poisson-text dual-wing specialization. The record covers the proper Gaussian parameter domain; published training or normalizer-estimation safeguards are not inferred from the existence of that domain. No normalized identity matched four candidates against all 442 pinned AIO IDs, labels and scoped synonyms or 444 preceding native IDs, names and aliases. Full-checkout searches included ignored and hidden files in both checkouts; five matching lines per checkout came from two unique prior discovery-ledger contents, and all matching excerpts were read. All 205 semantic label/synonym hits were byte-verified against prior readings. Twenty-nine annotated AIO nodes and outgoing edges comprise 28 unchanged prior readings and one newly read multimodal-deep-learning node. Thirty-nine contextual YAMLs comprise 34 unchanged prior readings and five fully read current records. Three candidates are curated; the unbounded-count DWH specialization remains deferred because the inspected joint is not normalizable with nonzero count couplings. Absence is bounded to this pinned snapshot and maintained corpus.

For a selected class y, each word-presence variable is Bernoulli with logit alpha_i^y+sum_k W_ik^y h_k. The demonstrated image-feature conditional is Gaussian with identity covariance and mean beta^y+U^y h. Hidden variables given all text/image features and the class are independent unit-Gaussian variables with mean (W^y)^T x+(U^y)^T z. Separate class parameters produce separate latent coordinates; topic positions across classes are not inherently aligned. For the identity-covariance construction, the Gaussian image/hidden precision must be positive definite; equivalently I-U^y(U^y)^T must be positive definite in every class. Binary word variables add bounded-state linear terms and do not repair an unstable Gaussian coupling. Proper-looking conditional normals alone do not establish a proper joint. The record restricts the probability-model definition to this admissible domain and does not certify that the historical fitting procedure enforced it. Integrating Gaussian hidden variables gives class-specific visible log mass F_y(x,z)=alpha^y dot x+beta^y dot z-&#124;&#124;z&#124;&#124;^2/2+&#124;&#124;(W^y)^T x+(U^y)^T z&#124;&#124;^2/2. Class posterior scores require pi_y exp(F_y)/Z_y. Assuming uniform class priors removes pi_y but not the separate class normalizers Z_y. In a one-word, one-image-feature example, unnormalized scores favor the second class while normalized densities favor the first. Each class can be fitted from its labeled examples; adding a class does not require sharing its latent coordinates with existing classes. Limitations: The manuscript acknowledges hidden partition functions but does not give a complete operational recipe for estimating and comparing every class normalizer. Raw energy comparison is not certified as probability comparison; no omission in uninspected author code is alleged. The Appendix adds quantities as log-partitions but displays integrals without the required logarithms. The compatible main joint and standard exponential-family algebra determine this record, rather than that inconsistent display. Gaussian color features are a modeling approximation to physical histogram observations. Fully factorized mean field and short-chain CD approximate learning statistics. The manuscript's broad CD-to-maximum-likelihood convergence statement is not accepted as a general guarantee. Sampling schedules and stability safeguards remain implementation details not fully specified by the paper. Main model comparisons use the five largest TRECVID categories, 1078 shots, an equal training/test split and selected latent sizes. The broader collection has 15 classes and 2468 shots. Selected topic examples and classification curves do not prove universal semantic accuracy, causality or generalization. No historical implementation or benchmark was run.

### Identity, model definition, probability boundaries, limitations and mappings

evidence: supported. Targets: AIMech:HierarchicalHarmonium.

Scoped to Yang and colleagues' shared hierarchical harmonium for semantic video. The label layer couples to the same hidden topics as text and images, unlike FoH's independently parameterized class models. Although its diagram has three tiers, the graph is bipartite between the latent variables and the combined text/image/label layer. The source uses one-hot labeled training shots and a single-label decision rule, while its Bernoulli label conditionals define a joint over the full binary label cube; the conclusion explicitly permits multiple active categories. This is not an ontology class hierarchy or an asserted one-hot generative model. No normalized identity matched four candidates against all 442 pinned AIO IDs, labels and scoped synonyms or 444 preceding native IDs, names and aliases. Full-checkout searches included ignored and hidden files in both checkouts; five matching lines per checkout came from two unique prior discovery-ledger contents, and all matching excerpts were read. All 205 semantic label/synonym hits were byte-verified against prior readings. Twenty-nine annotated AIO nodes and outgoing edges comprise 28 unchanged prior readings and one newly read multimodal-deep-learning node. Thirty-nine contextual YAMLs comprise 34 unchanged prior readings and five fully read current records. Three candidates are curated; the unbounded-count DWH specialization remains deferred because the inspected joint is not normalizable with nonzero count couplings. Absence is bounded to this pinned snapshot and maintained corpus. Unlike the maintained conditional-RBM record, which conditions on an externally supplied input and curates binary hidden units, HH specifies a joint over text, images and labels with Gaussian hidden variables.

The model shares word/image parameters across classes and adds label biases tau_t and label-topic couplings V_tk. Given h, words and labels have independent Bernoulli logits alpha+Wh and tau+Vh, while image features have Gaussian mean beta+Uh and identity covariance. Given all x,z,y, hidden variables are independent unit Gaussians with mean W^T x+U^T z+V^T y. As in FoH, the unbounded image/hidden joint requires I-UU^T positive definite; finite binary words and labels do not remove this requirement. For observed x,z, write a=W^T x+U^T z. Integrating hidden variables gives p(y&#124;x,z) proportional to exp(tau dot y+&#124;&#124;a+V^T y&#124;&#124;^2/2) over all binary label vectors. Labels generally become dependent after hidden marginalization; exact summation over 2^T configurations is possible in principle. Restricting support to exactly one active label would define a different model with categorical, rather than independent Bernoulli, h-conditioned labels. The reported single-label classifier chooses the largest posterior marginal P(Y_t=1&#124;x,z); this decision does not enforce one-hot support in the joint. When labels are unknown, the simple all-observed hidden Gaussian is replaced by a mixture over label configurations. Substituting the posterior mean hidden vector into a logistic label conditional is not generally the exact label marginal. The source explores fully factorized mean field and finite-chain approximations for prediction and learning, and compares CD with a noisy parameter-gradient procedure. These approximations are distinguished from exact finite label enumeration and from an independently verified posterior sampler over model parameters. Limitations: One-hot training observations, independent Bernoulli label conditionals and a single-label argmax decision are different statements. The binary-cube law can assign positive probability to zero or multiple labels; posterior marginals need not sum to one. The graph's tiers do not establish hierarchical class subsumption. Normalizability requires constraints on Gaussian couplings, which the inspected manuscript does not describe enforcing. The Appendix log-partition display is qualified as for FoH. The source's claimed general convergence of CD to maximum likelihood is not adopted. The Gibbs description lists label and hidden updates appropriate to clamped-feature prediction, without fully specifying every free-phase update used during learning. The Langevin display perturbs parameters with likelihood-gradient information and short-chain approximations; its target, prior and discretization controls are not sufficient to certify exact Bayesian parameter inference. The selected TRECVID experiments, latent-topic visualizations and class-similarity heatmap do not establish causal relationships, uniquely identified topics or universal classification gains. Finite calculations check binary versus one-hot support and a plug-in inference discrepancy; no author code or benchmark was run.

### Bounded hidden support and exact joint law

consistency: supported. Targets: AIMech:RateAdaptingPoissonModel.

Retain RAP as a distinct proper count-model family.

Finite binomial hidden states make the normalizer a finite sum after exact infinite Poisson summation. This differs from two unbounded Poisson layers and Gaussian-hidden count models. The softplus marginal, 96 hidden conditional probabilities, likelihood gradient and complement symmetry are verified. Conditional baseline rates and logits are not asserted marginal parameters. CD1 is an approximation, and linear cosine features differ from conditional hidden means.

### Class-specific Gaussian domains and likelihood comparison

consistency: supported. Targets: AIMech:FamilyOfHarmonium.

Retain separately normalized FoH models.

Each class has its own binary/Gaussian harmonium, requiring I-UU^T positive definite for the identity-covariance Gaussian block. Each class has its own partition; uniform priors do not cancel these partitions. The finite example reverses raw-energy and normalized-density rankings. The manuscript does not give a complete operational recipe for class-normalizer estimation, and no behavior of uninspected author code is asserted.

### Binary cube, one-hot observations and missing-label inference

consistency: supported. Targets: AIMech:HierarchicalHarmonium.

Retain HH with its binary-label joint and reported decision rule.

The joint couples binary labels to shared Gaussian topics and remains bipartite. One-hot observations do not constrain the generative label support; the conclusion explicitly allows multiple categories. Finite enumeration yields marginals 0.77335 each, unlike one-hot probabilities 0.5 each. A logistic-at-posterior-mean approximation gives 0.82444 rather than the exact 0.77335. Conditional labels given h are independent, whereas marginal labels generally interact. Hierarchical naming does not establish an ordered class taxonomy or deep hidden stack.

### Distinguish proper parameter domains from an unrepaired count formulation

consistency: supported. Targets: AIMech:RateAdaptingPoissonModel, AIMech:FamilyOfHarmonium, AIMech:HierarchicalHarmonium.

Keep the earlier DWH specialization outside the asserted record set.

FoH/HH use binary words and admit a proper Gaussian domain; RAP uses bounded hidden counts. In the earlier DWH specialization, integrating Gaussian hidden variables gives a positive quadratic term in any count with nonzero coupling. This dominates the factorial tail for either sign of coupling, even after correcting Gamma(n) to Gamma(n+1). Binary observations do not alter Poisson model support. A bounded-support or different-hidden-law revision requires separate primary evidence; no silent repair is attributed to the authors.

### Version identity, approximate fitting and empirical limits

consistency: supported. Targets: AIMech:RateAdaptingPoissonModel, AIMech:FamilyOfHarmonium, AIMech:HierarchicalHarmonium.

Preserve all inspected source and evaluation scopes.

All 29pages were visually read. RAP uses the accessible UCI ICML2006 file; the MPI route returned HTML. The semantic-video author manuscript has an author-name typo relative to proceedings metadata and is not certified as the final typeset file. Its Appendix log-partition display and CD convergence rhetoric are qualified. RAP tunes topic count using test-set 1NN performance; DWH fits representation before its SVM split; labeled harmonium comparisons mainly use a five-class subset. No historical code or benchmark was executed.

### Model/task mappings and neighboring conditional architectures

grounding: supported. Targets: AIMech:RateAdaptingPoissonModel, AIMech:FamilyOfHarmonium, AIMech:HierarchicalHarmonium.

Retain three native model identities with conservative mappings.

All three additions map broadly to AIO Model and related to the underspecified RestrictedBoltzmannMachine family. RAP also maps related to task-scoped ProbabilisticTopicModel. FoH and HH map related to Classification and MultimodalLearning, preserving model-versus-task boundaries. The latter target has a task definition and a deep-learning comment; that comment does not prove a deep neural architecture. MultimodalDeepLearning explicitly requires a deep neural network and is not mapped. HH has a bipartite graph and binary labels, not a class-subsumption hierarchy; HierarchicalClassification is therefore not inferred from its name. Conditional logits do not make the whole latent model identical to LogisticRegression. Ten native neighbors distinguish EFH, GCA, Replicated Softmax, auto-Poisson, auto-normal, CD, Gibbs, mean-field Boltzmann learning ULA and conditional RBM without renewed scientific approval. The conditional-RBM record models outputs given an external input and explicitly curates a binary-hidden specialization; HH instead specifies the joint text/image/label law with Gaussian hidden variables.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:RateAdaptingPoissonModel, AIMech:FamilyOfHarmonium, AIMech:HierarchicalHarmonium. Bounded-binomial count harmoniums, class-specific normalized harmoniums and shared binary-label harmoniums have distinct supported scopes. Broad Model and related RBM/task mappings preserve ontology abstraction. The incompatible unbounded-count specialization is retained only as an unresolved discovery candidate.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T011439Z-multimodal-harmonium-boundaries.json | supports | No normalized identity matched four candidates against all 442 pinned AIO IDs, labels and scoped synonyms or 444 preceding native IDs, names and aliases. Full-checkout searches included ignored and hidden files in both checkouts; five matching lines per checkout came from two unique prior discovery-ledger contents, and all matching excerpts were read. All 205 semantic label/synonym hits were byte-verified against prior readings. Twenty-nine annotated AIO nodes and outgoing edges comprise 28 unchanged prior readings and one newly read multimodal-deep-learning node. Thirty-nine contextual YAMLs comprise 34 unchanged prior readings and five fully read current records. Three candidates are curated; the unbounded-count DWH specialization remains deferred because the inspected joint is not normalizable with nonzero count couplings. Absence is bounded to this pinned snapshot and maintained corpus. |
| mapping | sources/aio/aio.json; 29 annotated CLASS nodes and outgoing edges; 205 unchanged label/synonym hits; MultimodalDeepLearning newly read | supports | All three additions map broadly to AIO Model and related to the underspecified RestrictedBoltzmannMachine family. RAP also maps related to task-scoped ProbabilisticTopicModel. FoH and HH map related to Classification and MultimodalLearning, preserving model-versus-task boundaries. The latter target has a task definition and a deep-learning comment; that comment does not prove a deep neural architecture. MultimodalDeepLearning explicitly requires a deep neural network and is not mapped. HH has a bipartite graph and binary labels, not a class-subsumption hierarchy; HierarchicalClassification is therefore not inferred from its name. Conditional logits do not make the whole latent model identical to LogisticRegression. Ten native neighbors distinguish EFH, GCA, Replicated Softmax, auto-Poisson, auto-normal, CD, Gibbs, mean-field Boltzmann learning ULA and conditional RBM without renewed scientific approval. The conditional-RBM record models outputs given an external input and explicitly curates a binary-hidden specialization; HH instead specifies the joint text/image/label law with Gaussian hidden variables. |
| neighbors | research/discovery/20261012T011439Z-multimodal-harmonium-boundaries.json; Ten native neighbors and 29 generated contextual YAMLs in source_analysis.context_reading | supports | EFH, GCA, Replicated Softmax, auto-Poisson, auto-normal, CD, Gibbs, mean-field Boltzmann learning, ULA and conditional RBM inform identity distinctions. Thirty-four contextual files are unchanged from prior readings and five current files were fully read. Conditional RBM uses an externally supplied input and explicitly curates binary hidden units, unlike the HH joint over words, images and labels. No contextual record receives renewed scientific approval. |
| finite-boundaries | research/discovery/multimodal-harmonium-boundaries.py; RAP conditionals, finite normalizer, gradient and complement; FoH class-normalizer reversal; HH label support and plug-in discrepancy; DWH divergent count tails | supports | RAP enumeration checks 96 hidden conditional probabilities over 16 count vectors and 6 hidden states, the exact visible softplus marginal, an exact finite hidden normalizer after infinite Poisson summation, a likelihood gradient and hidden-complement invariance. A proper one-word/one-image/one-hidden FoH example has raw class scores 1.0202/1.6487 but normalized densities 0.19731/0.16525, reversing the winning class. HH binary label probabilities are (0.08557,0.14108,0.14108,0.63227); each label marginal is 0.77335, whereas conditioning to one-hot support gives (0,0.5,0.5,0). Logistic evaluation at mean hidden value gives 0.82444 rather than the exact 0.77335. For DWH, integrated log count terms at n=1000 and 10000 are 14087.87 and 1917891.07 with coupling 0.2; the analytic quadratic-versus-factorial tail proves divergence for either sign of any nonzero count row. Curator derivations are not historical code or benchmark reproduction. |
| rateadaptingpoissonmodel-source-0 | https://vision.ics.uci.edu/papers/GehlerHW_ICML_2006/GehlerHW_ICML_2006.pdf; Section 2.1, PDF pp.2-3, Equations 1-3; Section 2.1, PDF pp.2-3, Equations 1-3 and 6; Section 2.3, PDF p.4, Equation 10 and Algorithm 1; Sections 3.1-3.2, pp.5-6; Sections 2.1-2.2, PDF pp.3-4, Equations 6-9 | supports | The Rate Adapting Poisson Model for Information Retrieval and Object Recognition. Author-affiliated UCI-hosted eight-page ICML2006 paper; all pages visually read. Numeric printed page labels are absent, so locators use PDF pages. The MPI download returned an HTML challenge; it is not the inspected PDF. All primary PDF pages were visually read. Curator deductions and finite calculations are distinguished from empirical claims and uninspected implementations. |
| familyofharmonium-source-0 | https://www.cs.cmu.edu/~epxing/papers/sdm07jyang.pdf; Section 3.2, PDF p.5, Equations 3.3-3.6; Appendix, p.12; Section 3.2, PDF pp.4-5, Equations 3.2-3.5; Section 3.4, pp.6-7; Sections 3.1-3.2, PDF pp.3-5, Figure 2 and Equations 3.1-3.7; Sections 3.2 and 3.4, PDF pp.5-7, Equations 3.6-3.7 and scalability discussion | supports | Harmonium Models for Semantic Video Representation and Classification. Author-hosted twelve-page manuscript associated with SDM2007 by primary proceedings and author-lab metadata. The title page prints Eric X. Ping, while proceedings metadata names Eric P. Xing. All pages including the Appendix visually read. Numeric printed labels are absent; locators use PDF pages. Not asserted byte-identical to a final publisher file. All primary PDF pages were visually read. Curator deductions and finite calculations are distinguished from empirical claims and uninspected implementations. |
| hierarchicalharmonium-source-0 | https://www.cs.cmu.edu/~epxing/papers/sdm07jyang.pdf; Section 3.3, PDF p.6, Equations 3.8-3.12; Section 6, p.11; Section 3.3, PDF pp.5-6, Equations 3.8-3.11; inherited Gaussian specification in Section 3.2, p.5; Section 3.3, PDF pp.5-6, Figure 3 and Equations 3.8-3.12; Section 6, p.11; Sections 4.1-4.4, PDF pp.7-8; Section 5.2, pp.9-11 | supports | Harmonium Models for Semantic Video Representation and Classification. Author-hosted twelve-page manuscript associated with SDM2007 by primary proceedings and author-lab metadata. The title page prints Eric X. Ping, while proceedings metadata names Eric P. Xing. All pages including the Appendix visually read. Numeric printed labels are absent; locators use PDF pages. Not asserted byte-identical to a final publisher file. All primary PDF pages were visually read. Curator deductions and finite calculations are distinguished from empirical claims and uninspected implementations. |
| deferred-dwh-source | https://arxiv.org/pdf/1207.1423v1; Section2.3, PDF p.4, Equations6-9; Section4, p.5; generic MWH footnote1, p.3 | context_only | All nine pages of arXiv1207.1423v1, archived in 2012 as UAI2005, were visually read. This is context for the deferred unbounded-Poisson/Gaussian specialization, not an added target. The divergent-tail conclusion is a curator derivation from its printed law, not an author-reported correction. Generic multi-wing grouping is explicitly described as mathematically the canonical harmonium with modality partitions. |

## Limits And Additional Notes

- Adversarial author self-review only; all three records remain DRAFT.
- All 29pages of three primary PDFs were visually read, including formulas, plots, algorithm boxes, references and the semantic-video Appendix. Locators use PDF page numbers because numeric printed page labels are absent. No author software ran.
- DWH is the 2012 archived v1 of the UAI2005 paper. The semantic-video file is a twelve-page author manuscript associated with SDM2007 and prints Eric X. Ping where proceedings metadata names Eric P. Xing. RAP is the UCI-hosted ICML2006 file; the MPI route returned HTML. Copies and final publisher versions are not certified equivalent.
- RAP finite hidden support guarantees a finite normalizer for finite parameters. FoH/HH require positive-definite Gaussian precision, separate class normalizers for FoH and binary-cube label semantics for HH. Historical training safeguards and exact partition-estimation implementations are not certified.
- The earlier unbounded-count DWH specialization remains deferred. Correcting its printed factorial does not fix divergent quadratic tails, and replacing it by a bounded law would change the model. No allegation about uninspected author code is made.
- The RAP topic dimension is selected using test-set 1NN performance; DWH fits representations before its classification split; semantic-video comparisons use a restricted five-class subset. These protocols are preserved without asserting universal gains or unverified leakage.
- Ten new provisional cohorts leave329 pending leads and other unresolved dispositions. All three additions remain DRAFT; no global saturation is claimed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T012031Z-multimodal-harmonium-boundaries
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of RAP and labeled harmonium model families
started_at: '2026-10-12T01:16:07Z'
finished_at: '2026-10-12T01:20:31Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially read all fields of three final
    records against29complete primaryPDFpages,29annotated AIO nodes and ten native
    contextual records. Finite calculations tested RAP normalization, conditionals
    and gradients, class-specific normalizers, label support and the deferred DWH
    tail failure. This is author self-review, not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain RAP, FoH and HH with explicit bounded-hidden, class-normalizer, Gaussian-domain
  and binary-label boundaries. Defer the earlier unbounded-count DWH specialization
  rather than silently changing its support. No actionable curation finding remains
  in the three selected maintained records.
source:
  git_revision: 87cbd196d7a408f8901996a9633666b13630fca5
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/BinaryClassification.yaml
    sha256: 4c710e70fe7e71227f0c6aa55162a3683f04ebbe6f5a4601bd4c0398329f1481
    role: context
  - path: data/aio/BoltzmannMachineNetwork.yaml
    sha256: 1152d2d85c5c1c408a0420e13f211ed109b12fb289c706ee7449864e91aece03
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/FactoredLanguageModel.yaml
    sha256: d5e425f3c7cc5b57fdab859cdc777b62398077a6ac9312aef6a89af42c6eb421
    role: context
  - path: data/aio/HierarchicalClassification.yaml
    sha256: 5e1f65090a3a9e7842b57c12410a7279d02c60baef05844fa1dd73545f1cbfc7
    role: context
  - path: data/aio/HierarchicalLanguageModel.yaml
    sha256: d37f9eda55372f4e261249cdefc3b88b036e214884ef612ced2bb40076d29622
    role: context
  - path: data/aio/LanguageModel.yaml
    sha256: 67c8faa6d8ac8fb5194931f662d513d1527cefb92ab1d7c283b2c8d1ddc20c4a
    role: context
  - path: data/aio/LogisticRegression.yaml
    sha256: 67dd6e8ae1bb6bfc48598b41adccbf7d48d925db8b0ee3a71f59569913b8c968
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
  - path: data/aio/MulticlassClassification.yaml
    sha256: dcf165047485763fd91782b9a9ba43202d58f00fd33b8545893a5eae327de171
    role: context
  - path: data/aio/MultimodalDeepLearning.yaml
    sha256: 635a5ce2fa376bd44aba26b8a29778727bf926607e9c0b1f5316b23949ec018e
    role: context
  - path: data/aio/MultimodalLearning.yaml
    sha256: 9e8bd52f242bf2d17bb0d9f5f795327a2067c17a855d47eb1e45630917ead603
    role: context
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
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
  - path: data/aio/RestrictedBoltzmannMachine.yaml
    sha256: 322fcb3b1f6064d944379ed79ffdcb7360fc2c3edd300c0a5a3f46be1f48df43
    role: context
  - path: data/aio/SubwordSegmentation.yaml
    sha256: d1841cd8a888cbb54840f58b6edd8bfad7b2bf4dd46e459f06010b89ad3d194a
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
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
  - path: data/curated/AutoNormalMarkovRandomField.yaml
    sha256: da7cfa897744f9b67bf75a4a8f0ea7748c1a052ed6ef063f0fbceec094e0ec90
    role: context
  - path: data/curated/AutoPoissonMarkovRandomField.yaml
    sha256: c54d99b85a9618652e078124ef40ae66e4744e61dbda5993ac4ffb5d9418f715
    role: context
  - path: data/curated/ConditionalRestrictedBoltzmannMachine.yaml
    sha256: b9e246890f7706a7e65be9f1d9611f06c462b36ab675e9441ca1f7702337aa80
    role: context
  - path: data/curated/ContrastiveDivergence.yaml
    sha256: 375d9a8cafc07b831743ac858a20bb33a08677e613cfce59773eeba644adc1c4
    role: context
  - path: data/curated/ExponentialFamilyHarmonium.yaml
    sha256: 5911a2b5a064e4320869eebf19637798b598f3aa6d741c84fc9f61e79457ffac
    role: context
  - path: data/curated/FamilyOfHarmonium.yaml
    sha256: eaf6b2cd757686e9c1b4e39232af093194e15c79cc06fc678f3b93db2adae728
    role: target
  - path: data/curated/GeneralizedComponentAnalysis.yaml
    sha256: 79ab7923284423c0f542c77deff5f0ce3de898c795d16e930340380b9046a8ff
    role: context
  - path: data/curated/GibbsSampling.yaml
    sha256: 8175215986c0507e3664a3aedf8074fc067d85b4a89002091d1bcb9b637a522a
    role: context
  - path: data/curated/HierarchicalHarmonium.yaml
    sha256: e8d3bc3476659b325ea4795ec22d50132d855b7f537ffabc88cf35071441eca2
    role: target
  - path: data/curated/MeanFieldBoltzmannLearning.yaml
    sha256: d9235021de282002b7b7f78c85382511ee0638f1dcc434fd5e11f85f3439d327
    role: context
  - path: data/curated/RateAdaptingPoissonModel.yaml
    sha256: e5b99fab57f429ef40736f2556b56395df127e99e35bef6553560979d57a3eb7
    role: target
  - path: data/curated/ReplicatedSoftmax.yaml
    sha256: 1a71debad5b7ac38c8e647ffb18c52f712300a7906b44efa5d348fb3488940cf
    role: context
  - path: data/curated/UnadjustedLangevinAlgorithm.yaml
    sha256: 4c09ef556111d807d01b68678691453752de613610bb23239c9480b90b8535eb
    role: context
  - path: research/discovery/20261012T011439Z-multimodal-harmonium-boundaries.json
    sha256: 3f8f87a56ed1cbe3755846316d2b9ba9b32eec40841e17d79be31b5e5d7f8cee
    role: context
  - path: research/discovery/multimodal-harmonium-boundaries.py
    sha256: 2b9b677d829ddee136887ab37766212c9447b6f2bde56518f5a44fbb03ba2454
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
- target_id: AIMech:RateAdaptingPoissonModel
  path: data/curated/RateAdaptingPoissonModel.yaml
  label: Rate-adapting Poisson model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RateAdaptingPoissonModel.yaml
    role: maintained
- target_id: AIMech:FamilyOfHarmonium
  path: data/curated/FamilyOfHarmonium.yaml
  label: Family-of-harmonium
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FamilyOfHarmonium.yaml
    role: maintained
- target_id: AIMech:HierarchicalHarmonium
  path: data/curated/HierarchicalHarmonium.yaml
  label: Hierarchical harmonium
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HierarchicalHarmonium.yaml
    role: maintained
scope:
  description: All fields of three maintained model-family records.
  selection: Exact maintained IDs RateAdaptingPoissonModel, FamilyOfHarmonium and
    HierarchicalHarmonium; complete selected cohort without sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:RateAdaptingPoissonModel
  - AIMech:FamilyOfHarmonium
  - AIMech:HierarchicalHarmonium
  exclusions:
  - target: Unbounded-count dual-wing harmonium specialization
    reason: Candidate remains in the discovery ledger pending a primary proper-support/model
      revision. Its divergent count tail is calculated and documented; it is not an
      asserted record or a fourth review target.
  - target: Author software, trained instances and empirical reproduction
    reason: No implementation or benchmark was executed. Finite curator calculations
      do not certify historical safeguards, convergence or empirical outcomes.
  - target: Contextual records and remaining frontier
    reason: Context informs identity without renewed scientific approval. Ten new
      reference cohorts, 329 pending leads and other unresolved dispositions remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:RateAdaptingPoissonModel
  - AIMech:FamilyOfHarmonium
  - AIMech:HierarchicalHarmonium
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 95.43s (0:01:35)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 447 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 130 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 127,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:RateAdaptingPoissonModel
  - AIMech:FamilyOfHarmonium
  - AIMech:HierarchicalHarmonium
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
  - AIMech:RateAdaptingPoissonModel
  - AIMech:FamilyOfHarmonium
  - AIMech:HierarchicalHarmonium
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
  - AIMech:RateAdaptingPoissonModel
  - AIMech:FamilyOfHarmonium
  - AIMech:HierarchicalHarmonium
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: required-4
  name: env PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated
  command: env PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:RateAdaptingPoissonModel
  - AIMech:FamilyOfHarmonium
  - AIMech:HierarchicalHarmonium
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 447 curated concept record(s); 0 error(s).

    '
- check_id: finite-arithmetic
  name: Multimodal harmonium probability boundaries
  command: python3 research/discovery/multimodal-harmonium-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:RateAdaptingPoissonModel
  - AIMech:FamilyOfHarmonium
  - AIMech:HierarchicalHarmonium
  exit_code: 0
  expected_exit_code: 0
  summary: '{"rap": {"hidden_states": 6, "checked_hidden_probabilities": 96, "conditional_error":
    1.5265566588595902e-16, "marginal_error": 2.220446049250313e-16, "exact_log_normalizer":
    3.3751013338131903, "gradient": 0.3021105497615496, "finite_difference": 0.3021105497102994,
    "complement_error": 8.881784197001252e-16, "normalization": "Finite hidden sum
    after exact Poisson summation, without truncating visible support."}, "family_of_harmonium":
    {"class_unnormalized_scores": [1.0202013400267558, 1.6487212707001282], "class_normalizers":
    [5.170490871695183, 9.977009730616732], "class_densities": [0.19731227949973643,
    0.1652520459753237], "raw_winner": 1, "proper_winner": 0, "gaussian_precision_condition":
    "For identity variances, I-U U^T must be positive definite; equivalently every
    singular value of U is below one."}, "hierarchical_harmonium": {"binary_label_states":
    [[0, 0], [0, 1], [1, 0], [1, 1]], "joint_label_probabilities": [0.08556882867798671,
    0.14107914795029183, 0.14107914795029183, 0.6322728754214296], "label_marginals":
    [0.7733520233717215, 0.7733520233717215], "onehot_restricted_probabilities": [0.0,
    0.5, 0.5, 0.0], "bernoulli_means_given_h_one": [0.7310585786300049, 0.7310585786300049],
    "onehot_means_given_h_one": [0.5, 0.5], "logistic_at_posterior_mean": 0.8244371838867636,
    "exact_label_marginal": 0.7733520233717215, "interpretation": "One-hot training
    observations do not constrain the binary-cube joint; conditional Bernoulli logits
    differ from categorical softmax. Integrating a missing label layer yields Gaussian
    mixtures, not a single plug-in Gaussian."}, "dual_wing_boundary": {"counts": [100,
    1000, 10000], "log_integrated_terms": [-163.7393755555634, 14087.87182151184,
    1917891.0721631858], "negative_coupling_same_divergence": true, "conclusion":
    "The unbounded count/unit-Gaussian-hidden specialization is not jointly normalizable
    for a nonzero count coupling. A proper-support revision or clarification is needed
    before an asserted native probability-model record.", "additional_display_note":
    "Poisson base measure is 1/Gamma(n+1), not the printed 1/Gamma(n); correcting
    that factorial does not repair quadratic tail growth."}, "status": "PASS"}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T011439Z-multimodal-harmonium-boundaries.json
  accessed_at: '2026-10-12T01:16:07Z'
  support: supports
  summary: No normalized identity matched four candidates against all 442 pinned AIO
    IDs, labels and scoped synonyms or 444 preceding native IDs, names and aliases.
    Full-checkout searches included ignored and hidden files in both checkouts; five
    matching lines per checkout came from two unique prior discovery-ledger contents,
    and all matching excerpts were read. All 205 semantic label/synonym hits were
    byte-verified against prior readings. Twenty-nine annotated AIO nodes and outgoing
    edges comprise 28 unchanged prior readings and one newly read multimodal-deep-learning
    node. Thirty-nine contextual YAMLs comprise 34 unchanged prior readings and five
    fully read current records. Three candidates are curated; the unbounded-count
    DWH specialization remains deferred because the inspected joint is not normalizable
    with nonzero count couplings. Absence is bounded to this pinned snapshot and maintained
    corpus.
  search_scope: All matching excerpts from two unique prior discovery-ledger contents
    were read. Both complete checkouts were searched including ignored and hidden
    files. Four candidate identities were evaluated, of which three are additions
    and the unbounded-count DWH specialization remains deferred. Absence is bounded
    to the pinned and maintained corpus.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 29 annotated CLASS nodes and outgoing edges; 205 unchanged label/synonym
    hits; MultimodalDeepLearning newly read
  accessed_at: '2026-10-12T01:16:07Z'
  support: supports
  summary: All three additions map broadly to AIO Model and related to the underspecified
    RestrictedBoltzmannMachine family. RAP also maps related to task-scoped ProbabilisticTopicModel.
    FoH and HH map related to Classification and MultimodalLearning, preserving model-versus-task
    boundaries. The latter target has a task definition and a deep-learning comment;
    that comment does not prove a deep neural architecture. MultimodalDeepLearning
    explicitly requires a deep neural network and is not mapped. HH has a bipartite
    graph and binary labels, not a class-subsumption hierarchy; HierarchicalClassification
    is therefore not inferred from its name. Conditional logits do not make the whole
    latent model identical to LogisticRegression. Ten native neighbors distinguish
    EFH, GCA, Replicated Softmax, auto-Poisson, auto-normal, CD, Gibbs, mean-field
    Boltzmann learning ULA and conditional RBM without renewed scientific approval.
    The conditional-RBM record models outputs given an external input and explicitly
    curates a binary-hidden specialization; HH instead specifies the joint text/image/label
    law with Gaussian hidden variables.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261012T011439Z-multimodal-harmonium-boundaries.json
  locator: Ten native neighbors and 29 generated contextual YAMLs in source_analysis.context_reading
  accessed_at: '2026-10-12T01:16:07Z'
  support: supports
  summary: EFH, GCA, Replicated Softmax, auto-Poisson, auto-normal, CD, Gibbs, mean-field
    Boltzmann learning, ULA and conditional RBM inform identity distinctions. Thirty-four
    contextual files are unchanged from prior readings and five current files were
    fully read. Conditional RBM uses an externally supplied input and explicitly curates
    binary hidden units, unlike the HH joint over words, images and labels. No contextual
    record receives renewed scientific approval.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/multimodal-harmonium-boundaries.py
  locator: RAP conditionals, finite normalizer, gradient and complement; FoH class-normalizer
    reversal; HH label support and plug-in discrepancy; DWH divergent count tails
  accessed_at: '2026-10-12T01:16:07Z'
  snapshot_sha256: 2b9b677d829ddee136887ab37766212c9447b6f2bde56518f5a44fbb03ba2454
  support: supports
  summary: RAP enumeration checks 96 hidden conditional probabilities over 16 count
    vectors and 6 hidden states, the exact visible softplus marginal, an exact finite
    hidden normalizer after infinite Poisson summation, a likelihood gradient and
    hidden-complement invariance. A proper one-word/one-image/one-hidden FoH example
    has raw class scores 1.0202/1.6487 but normalized densities 0.19731/0.16525, reversing
    the winning class. HH binary label probabilities are (0.08557,0.14108,0.14108,0.63227);
    each label marginal is 0.77335, whereas conditioning to one-hot support gives
    (0,0.5,0.5,0). Logistic evaluation at mean hidden value gives 0.82444 rather than
    the exact 0.77335. For DWH, integrated log count terms at n=1000 and 10000 are
    14087.87 and 1917891.07 with coupling 0.2; the analytic quadratic-versus-factorial
    tail proves divergence for either sign of any nonzero count row. Curator derivations
    are not historical code or benchmark reproduction.
- evidence_id: rateadaptingpoissonmodel-source-0
  kind: primary_source
  reference: https://vision.ics.uci.edu/papers/GehlerHW_ICML_2006/GehlerHW_ICML_2006.pdf
  locator: Section 2.1, PDF pp.2-3, Equations 1-3; Section 2.1, PDF pp.2-3, Equations
    1-3 and 6; Section 2.3, PDF p.4, Equation 10 and Algorithm 1; Sections 3.1-3.2,
    pp.5-6; Sections 2.1-2.2, PDF pp.3-4, Equations 6-9
  accessed_at: '2026-10-12T01:06:08Z'
  snapshot_sha256: 413a1ce4396add087e3bd0fc2304415621296f749a3996517e37932d2905ba0f
  support: supports
  summary: The Rate Adapting Poisson Model for Information Retrieval and Object Recognition.
    Author-affiliated UCI-hosted eight-page ICML2006 paper; all pages visually read.
    Numeric printed page labels are absent, so locators use PDF pages. The MPI download
    returned an HTML challenge; it is not the inspected PDF. All primary PDF pages
    were visually read. Curator deductions and finite calculations are distinguished
    from empirical claims and uninspected implementations.
- evidence_id: familyofharmonium-source-0
  kind: primary_source
  reference: https://www.cs.cmu.edu/~epxing/papers/sdm07jyang.pdf
  locator: Section 3.2, PDF p.5, Equations 3.3-3.6; Appendix, p.12; Section 3.2, PDF
    pp.4-5, Equations 3.2-3.5; Section 3.4, pp.6-7; Sections 3.1-3.2, PDF pp.3-5,
    Figure 2 and Equations 3.1-3.7; Sections 3.2 and 3.4, PDF pp.5-7, Equations 3.6-3.7
    and scalability discussion
  accessed_at: '2026-10-12T01:04:31Z'
  snapshot_sha256: 23177fca49a459f341ea4654825537c14f417330de069cfa20b29e8a235938b1
  support: supports
  summary: Harmonium Models for Semantic Video Representation and Classification.
    Author-hosted twelve-page manuscript associated with SDM2007 by primary proceedings
    and author-lab metadata. The title page prints Eric X. Ping, while proceedings
    metadata names Eric P. Xing. All pages including the Appendix visually read. Numeric
    printed labels are absent; locators use PDF pages. Not asserted byte-identical
    to a final publisher file. All primary PDF pages were visually read. Curator deductions
    and finite calculations are distinguished from empirical claims and uninspected
    implementations.
- evidence_id: hierarchicalharmonium-source-0
  kind: primary_source
  reference: https://www.cs.cmu.edu/~epxing/papers/sdm07jyang.pdf
  locator: Section 3.3, PDF p.6, Equations 3.8-3.12; Section 6, p.11; Section 3.3,
    PDF pp.5-6, Equations 3.8-3.11; inherited Gaussian specification in Section 3.2,
    p.5; Section 3.3, PDF pp.5-6, Figure 3 and Equations 3.8-3.12; Section 6, p.11;
    Sections 4.1-4.4, PDF pp.7-8; Section 5.2, pp.9-11
  accessed_at: '2026-10-12T01:04:31Z'
  snapshot_sha256: 23177fca49a459f341ea4654825537c14f417330de069cfa20b29e8a235938b1
  support: supports
  summary: Harmonium Models for Semantic Video Representation and Classification.
    Author-hosted twelve-page manuscript associated with SDM2007 by primary proceedings
    and author-lab metadata. The title page prints Eric X. Ping, while proceedings
    metadata names Eric P. Xing. All pages including the Appendix visually read. Numeric
    printed labels are absent; locators use PDF pages. Not asserted byte-identical
    to a final publisher file. All primary PDF pages were visually read. Curator deductions
    and finite calculations are distinguished from empirical claims and uninspected
    implementations.
- evidence_id: deferred-dwh-source
  kind: primary_source
  reference: https://arxiv.org/pdf/1207.1423v1
  locator: Section2.3, PDF p.4, Equations6-9; Section4, p.5; generic MWH footnote1,
    p.3
  accessed_at: '2026-10-12T01:04:30Z'
  snapshot_sha256: bb17aa787dded68e953f7f41ad2c9ff4fbb4dd7aab02da64d4c0502111caa816
  support: context_only
  summary: All nine pages of arXiv1207.1423v1, archived in 2012 as UAI2005, were visually
    read. This is context for the deferred unbounded-Poisson/Gaussian specialization,
    not an added target. The divergent-tail conclusion is a curator derivation from
    its printed law, not an author-reported correction. Generic multi-wing grouping
    is explicitly described as mathematically the canonical harmonium with modality
    partitions.
assessments:
- assessment_id: rateadaptingpoissonmodel
  area: evidence
  topic: Identity, model definition, probability boundaries, limitations and mappings
  outcome: supported
  target_ids:
  - AIMech:RateAdaptingPoissonModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - rateadaptingpoissonmodel-source-0
  summary: Scoped to Gehler, Holub and Welling's ICML2006 RAP construction with fixed
    finite integer binomial trial counts. This differs from a Gaussian-hidden count
    harmonium, a two-unbounded-Poisson-layer construction, categorical word-bin EFH
    and replicated-token Softmax. Baseline Poisson rates and hidden logits are conditional
    parameters, not generally marginal means or independent hidden priors. The latent
    count model is distinct from its CD fitting algorithm or a trained retrieval system.
    No normalized identity matched four candidates against all 442 pinned AIO IDs,
    labels and scoped synonyms or 444 preceding native IDs, names and aliases. Full-checkout
    searches included ignored and hidden files in both checkouts; five matching lines
    per checkout came from two unique prior discovery-ledger contents, and all matching
    excerpts were read. All 205 semantic label/synonym hits were byte-verified against
    prior readings. Twenty-nine annotated AIO nodes and outgoing edges comprise 28
    unchanged prior readings and one newly read multimodal-deep-learning node. Thirty-nine
    contextual YAMLs comprise 34 unchanged prior readings and five fully read current
    records. Three candidates are curated; the unbounded-count DWH specialization
    remains deferred because the inspected joint is not normalizable with nonzero
    count couplings. Absence is bounded to this pinned snapshot and maintained corpus.
  details: 'With baseline log rates a_i, hidden thresholds beta_j, interaction weights
    W_ij and finite integer trial counts M_j, visible counts conditioned on h are
    independent Poisson with rates exp(a_i+sum_j W_ij h_j). Hidden variables conditioned
    on x are independent Binomial(M_j,sigmoid(sum_i W_ij x_i-beta_j)). The joint retains
    visible factorial and hidden binomial base measures. Summing all visible counts
    first leaves a finite sum over bounded hidden configurations, proving a finite
    joint normalizer for finite parameters without truncating visible counts. Marginalizing
    hidden units gives visible log mass sum_i(a_i x_i-log(x_i!))+sum_j M_j softplus(sum_i
    W_ij x_i-beta_j), up to a global constant. The hard threshold interpretation is
    an approximation to softplus, not exact zero influence below a threshold. Complementing
    a hidden count to M_j-h_j, reversing its weight column and threshold, and adding
    M_j W_ij to each visible log baseline preserves the normalized visible law. This
    discrete symmetry does not establish arbitrary orthogonal rotation invariance
    or full parameter identifiability. Likelihood gradients contrast observed and
    equilibrium sufficient statistics. Conditional hidden expectations M_j sigmoid(W_j^T
    x-beta_j) replace sampled hidden counts in the displayed gradient statistics.
    The reported CD1 procedure draws hidden counts from each observed vector, reconstructs
    visible counts and uses short-chain negative expectations, introducing approximation
    bias. Retrieval uses cosine similarity of the linear projection W^T x, which is
    distinct from the nonlinear conditional-binomial mean and from exact joint likelihood
    scoring. Limitations: The normalizer is finite but its exact finite hidden sum
    can grow exponentially with the number and ranges of hidden units. CD, minibatches
    and momentum do not certify exact maximum likelihood or chain convergence. No
    noninteger binomial trial-count extension is asserted. The document-retrieval
    topic dimension is selected using test-set one-nearest-neighbor performance, explicitly
    stated in the Figure 4 caption. Reported curves therefore do not constitute an
    independently tuned held-out comparison. The split used for class-informed newsgroup
    vocabulary selection is insufficiently specified to assert a separate leakage
    mechanism. RAP is compared with LSI and PLSI on selected text corpora and bag-of-visual-words
    image tasks. LDA is omitted from the reported comparison. Different retrieval
    measures and dataset configurations yield different rankings; no universal performance
    advantage is curated. Finite checks verify 96 hidden conditional probabilities,
    exact visible marginalization, a likelihood gradient and complement symmetry.
    No author code, coordinate-mode implementation, empirical benchmark, hierarchical
    extension or negative-binomial replacement was executed or certified.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A specified probability-model family, distinct from a trained instance,
      a generic task or its fitting algorithm.
    evidence_ids:
    - rateadaptingpoissonmodel-source-0
  - name: aio-assessment
    value: broad_match,related_match,related_match
    definition: All three additions map broadly to AIO Model and related to the underspecified
      RestrictedBoltzmannMachine family. RAP also maps related to task-scoped ProbabilisticTopicModel.
      FoH and HH map related to Classification and MultimodalLearning, preserving
      model-versus-task boundaries. The latter target has a task definition and a
      deep-learning comment; that comment does not prove a deep neural architecture.
      MultimodalDeepLearning explicitly requires a deep neural network and is not
      mapped. HH has a bipartite graph and binary labels, not a class-subsumption
      hierarchy; HierarchicalClassification is therefore not inferred from its name.
      Conditional logits do not make the whole latent model identical to LogisticRegression.
      Ten native neighbors distinguish EFH, GCA, Replicated Softmax, auto-Poisson,
      auto-normal, CD, Gibbs, mean-field Boltzmann learning ULA and conditional RBM
      without renewed scientific approval. The conditional-RBM record models outputs
      given an external input and explicitly curates a binary-hidden specialization;
      HH instead specifies the joint text/image/label law with Gaussian hidden variables.
    evidence_ids:
    - mapping
- assessment_id: familyofharmonium
  area: evidence
  topic: Identity, model definition, probability boundaries, limitations and mappings
  outcome: supported
  target_ids:
  - AIMech:FamilyOfHarmonium
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - familyofharmonium-source-0
  summary: Scoped to the FoH construction in Yang and colleagues' semantic-video manuscript.
    Each labeled class owns its parameters and latent coordinates; a categorical class
    selector has a prior distribution. This differs from the shared label-coupled
    hierarchical harmonium, an unsupervised single harmonium followed by an SVM, and
    the earlier unbounded Poisson-text dual-wing specialization. The record covers
    the proper Gaussian parameter domain; published training or normalizer-estimation
    safeguards are not inferred from the existence of that domain. No normalized identity
    matched four candidates against all 442 pinned AIO IDs, labels and scoped synonyms
    or 444 preceding native IDs, names and aliases. Full-checkout searches included
    ignored and hidden files in both checkouts; five matching lines per checkout came
    from two unique prior discovery-ledger contents, and all matching excerpts were
    read. All 205 semantic label/synonym hits were byte-verified against prior readings.
    Twenty-nine annotated AIO nodes and outgoing edges comprise 28 unchanged prior
    readings and one newly read multimodal-deep-learning node. Thirty-nine contextual
    YAMLs comprise 34 unchanged prior readings and five fully read current records.
    Three candidates are curated; the unbounded-count DWH specialization remains deferred
    because the inspected joint is not normalizable with nonzero count couplings.
    Absence is bounded to this pinned snapshot and maintained corpus.
  details: 'For a selected class y, each word-presence variable is Bernoulli with
    logit alpha_i^y+sum_k W_ik^y h_k. The demonstrated image-feature conditional is
    Gaussian with identity covariance and mean beta^y+U^y h. Hidden variables given
    all text/image features and the class are independent unit-Gaussian variables
    with mean (W^y)^T x+(U^y)^T z. Separate class parameters produce separate latent
    coordinates; topic positions across classes are not inherently aligned. For the
    identity-covariance construction, the Gaussian image/hidden precision must be
    positive definite; equivalently I-U^y(U^y)^T must be positive definite in every
    class. Binary word variables add bounded-state linear terms and do not repair
    an unstable Gaussian coupling. Proper-looking conditional normals alone do not
    establish a proper joint. The record restricts the probability-model definition
    to this admissible domain and does not certify that the historical fitting procedure
    enforced it. Integrating Gaussian hidden variables gives class-specific visible
    log mass F_y(x,z)=alpha^y dot x+beta^y dot z-||z||^2/2+||(W^y)^T x+(U^y)^T z||^2/2.
    Class posterior scores require pi_y exp(F_y)/Z_y. Assuming uniform class priors
    removes pi_y but not the separate class normalizers Z_y. In a one-word, one-image-feature
    example, unnormalized scores favor the second class while normalized densities
    favor the first. Each class can be fitted from its labeled examples; adding a
    class does not require sharing its latent coordinates with existing classes. Limitations:
    The manuscript acknowledges hidden partition functions but does not give a complete
    operational recipe for estimating and comparing every class normalizer. Raw energy
    comparison is not certified as probability comparison; no omission in uninspected
    author code is alleged. The Appendix adds quantities as log-partitions but displays
    integrals without the required logarithms. The compatible main joint and standard
    exponential-family algebra determine this record, rather than that inconsistent
    display. Gaussian color features are a modeling approximation to physical histogram
    observations. Fully factorized mean field and short-chain CD approximate learning
    statistics. The manuscript''s broad CD-to-maximum-likelihood convergence statement
    is not accepted as a general guarantee. Sampling schedules and stability safeguards
    remain implementation details not fully specified by the paper. Main model comparisons
    use the five largest TRECVID categories, 1078 shots, an equal training/test split
    and selected latent sizes. The broader collection has 15 classes and 2468 shots.
    Selected topic examples and classification curves do not prove universal semantic
    accuracy, causality or generalization. No historical implementation or benchmark
    was run.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A specified probability-model family, distinct from a trained instance,
      a generic task or its fitting algorithm.
    evidence_ids:
    - familyofharmonium-source-0
  - name: aio-assessment
    value: broad_match,related_match,related_match,related_match
    definition: All three additions map broadly to AIO Model and related to the underspecified
      RestrictedBoltzmannMachine family. RAP also maps related to task-scoped ProbabilisticTopicModel.
      FoH and HH map related to Classification and MultimodalLearning, preserving
      model-versus-task boundaries. The latter target has a task definition and a
      deep-learning comment; that comment does not prove a deep neural architecture.
      MultimodalDeepLearning explicitly requires a deep neural network and is not
      mapped. HH has a bipartite graph and binary labels, not a class-subsumption
      hierarchy; HierarchicalClassification is therefore not inferred from its name.
      Conditional logits do not make the whole latent model identical to LogisticRegression.
      Ten native neighbors distinguish EFH, GCA, Replicated Softmax, auto-Poisson,
      auto-normal, CD, Gibbs, mean-field Boltzmann learning ULA and conditional RBM
      without renewed scientific approval. The conditional-RBM record models outputs
      given an external input and explicitly curates a binary-hidden specialization;
      HH instead specifies the joint text/image/label law with Gaussian hidden variables.
    evidence_ids:
    - mapping
- assessment_id: hierarchicalharmonium
  area: evidence
  topic: Identity, model definition, probability boundaries, limitations and mappings
  outcome: supported
  target_ids:
  - AIMech:HierarchicalHarmonium
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - hierarchicalharmonium-source-0
  summary: Scoped to Yang and colleagues' shared hierarchical harmonium for semantic
    video. The label layer couples to the same hidden topics as text and images, unlike
    FoH's independently parameterized class models. Although its diagram has three
    tiers, the graph is bipartite between the latent variables and the combined text/image/label
    layer. The source uses one-hot labeled training shots and a single-label decision
    rule, while its Bernoulli label conditionals define a joint over the full binary
    label cube; the conclusion explicitly permits multiple active categories. This
    is not an ontology class hierarchy or an asserted one-hot generative model. No
    normalized identity matched four candidates against all 442 pinned AIO IDs, labels
    and scoped synonyms or 444 preceding native IDs, names and aliases. Full-checkout
    searches included ignored and hidden files in both checkouts; five matching lines
    per checkout came from two unique prior discovery-ledger contents, and all matching
    excerpts were read. All 205 semantic label/synonym hits were byte-verified against
    prior readings. Twenty-nine annotated AIO nodes and outgoing edges comprise 28
    unchanged prior readings and one newly read multimodal-deep-learning node. Thirty-nine
    contextual YAMLs comprise 34 unchanged prior readings and five fully read current
    records. Three candidates are curated; the unbounded-count DWH specialization
    remains deferred because the inspected joint is not normalizable with nonzero
    count couplings. Absence is bounded to this pinned snapshot and maintained corpus.
    Unlike the maintained conditional-RBM record, which conditions on an externally
    supplied input and curates binary hidden units, HH specifies a joint over text,
    images and labels with Gaussian hidden variables.
  details: 'The model shares word/image parameters across classes and adds label biases
    tau_t and label-topic couplings V_tk. Given h, words and labels have independent
    Bernoulli logits alpha+Wh and tau+Vh, while image features have Gaussian mean
    beta+Uh and identity covariance. Given all x,z,y, hidden variables are independent
    unit Gaussians with mean W^T x+U^T z+V^T y. As in FoH, the unbounded image/hidden
    joint requires I-UU^T positive definite; finite binary words and labels do not
    remove this requirement. For observed x,z, write a=W^T x+U^T z. Integrating hidden
    variables gives p(y|x,z) proportional to exp(tau dot y+||a+V^T y||^2/2) over all
    binary label vectors. Labels generally become dependent after hidden marginalization;
    exact summation over 2^T configurations is possible in principle. Restricting
    support to exactly one active label would define a different model with categorical,
    rather than independent Bernoulli, h-conditioned labels. The reported single-label
    classifier chooses the largest posterior marginal P(Y_t=1|x,z); this decision
    does not enforce one-hot support in the joint. When labels are unknown, the simple
    all-observed hidden Gaussian is replaced by a mixture over label configurations.
    Substituting the posterior mean hidden vector into a logistic label conditional
    is not generally the exact label marginal. The source explores fully factorized
    mean field and finite-chain approximations for prediction and learning, and compares
    CD with a noisy parameter-gradient procedure. These approximations are distinguished
    from exact finite label enumeration and from an independently verified posterior
    sampler over model parameters. Limitations: One-hot training observations, independent
    Bernoulli label conditionals and a single-label argmax decision are different
    statements. The binary-cube law can assign positive probability to zero or multiple
    labels; posterior marginals need not sum to one. The graph''s tiers do not establish
    hierarchical class subsumption. Normalizability requires constraints on Gaussian
    couplings, which the inspected manuscript does not describe enforcing. The Appendix
    log-partition display is qualified as for FoH. The source''s claimed general convergence
    of CD to maximum likelihood is not adopted. The Gibbs description lists label
    and hidden updates appropriate to clamped-feature prediction, without fully specifying
    every free-phase update used during learning. The Langevin display perturbs parameters
    with likelihood-gradient information and short-chain approximations; its target,
    prior and discretization controls are not sufficient to certify exact Bayesian
    parameter inference. The selected TRECVID experiments, latent-topic visualizations
    and class-similarity heatmap do not establish causal relationships, uniquely identified
    topics or universal classification gains. Finite calculations check binary versus
    one-hot support and a plug-in inference discrepancy; no author code or benchmark
    was run.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A specified probability-model family, distinct from a trained instance,
      a generic task or its fitting algorithm.
    evidence_ids:
    - hierarchicalharmonium-source-0
  - name: aio-assessment
    value: broad_match,related_match,related_match,related_match
    definition: All three additions map broadly to AIO Model and related to the underspecified
      RestrictedBoltzmannMachine family. RAP also maps related to task-scoped ProbabilisticTopicModel.
      FoH and HH map related to Classification and MultimodalLearning, preserving
      model-versus-task boundaries. The latter target has a task definition and a
      deep-learning comment; that comment does not prove a deep neural architecture.
      MultimodalDeepLearning explicitly requires a deep neural network and is not
      mapped. HH has a bipartite graph and binary labels, not a class-subsumption
      hierarchy; HierarchicalClassification is therefore not inferred from its name.
      Conditional logits do not make the whole latent model identical to LogisticRegression.
      Ten native neighbors distinguish EFH, GCA, Replicated Softmax, auto-Poisson,
      auto-normal, CD, Gibbs, mean-field Boltzmann learning ULA and conditional RBM
      without renewed scientific approval. The conditional-RBM record models outputs
      given an external input and explicitly curates a binary-hidden specialization;
      HH instead specifies the joint text/image/label law with Gaussian hidden variables.
    evidence_ids:
    - mapping
- assessment_id: rap-bounded-hidden-law
  area: consistency
  topic: Bounded hidden support and exact joint law
  outcome: supported
  target_ids:
  - AIMech:RateAdaptingPoissonModel
  evidence_ids:
  - rateadaptingpoissonmodel-source-0
  - finite-boundaries
  - neighbors
  summary: Retain RAP as a distinct proper count-model family.
  details: Finite binomial hidden states make the normalizer a finite sum after exact
    infinite Poisson summation. This differs from two unbounded Poisson layers and
    Gaussian-hidden count models. The softplus marginal, 96 hidden conditional probabilities,
    likelihood gradient and complement symmetry are verified. Conditional baseline
    rates and logits are not asserted marginal parameters. CD1 is an approximation,
    and linear cosine features differ from conditional hidden means.
- assessment_id: foh-class-normalizers
  area: consistency
  topic: Class-specific Gaussian domains and likelihood comparison
  outcome: supported
  target_ids:
  - AIMech:FamilyOfHarmonium
  evidence_ids:
  - familyofharmonium-source-0
  - finite-boundaries
  - neighbors
  summary: Retain separately normalized FoH models.
  details: Each class has its own binary/Gaussian harmonium, requiring I-UU^T positive
    definite for the identity-covariance Gaussian block. Each class has its own partition;
    uniform priors do not cancel these partitions. The finite example reverses raw-energy
    and normalized-density rankings. The manuscript does not give a complete operational
    recipe for class-normalizer estimation, and no behavior of uninspected author
    code is asserted.
- assessment_id: hh-binary-label-semantics
  area: consistency
  topic: Binary cube, one-hot observations and missing-label inference
  outcome: supported
  target_ids:
  - AIMech:HierarchicalHarmonium
  evidence_ids:
  - hierarchicalharmonium-source-0
  - finite-boundaries
  - neighbors
  summary: Retain HH with its binary-label joint and reported decision rule.
  details: The joint couples binary labels to shared Gaussian topics and remains bipartite.
    One-hot observations do not constrain the generative label support; the conclusion
    explicitly allows multiple categories. Finite enumeration yields marginals 0.77335
    each, unlike one-hot probabilities 0.5 each. A logistic-at-posterior-mean approximation
    gives 0.82444 rather than the exact 0.77335. Conditional labels given h are independent,
    whereas marginal labels generally interact. Hierarchical naming does not establish
    an ordered class taxonomy or deep hidden stack.
- assessment_id: properness-and-deferred-dwh
  area: consistency
  topic: Distinguish proper parameter domains from an unrepaired count formulation
  outcome: supported
  target_ids:
  - AIMech:RateAdaptingPoissonModel
  - AIMech:FamilyOfHarmonium
  - AIMech:HierarchicalHarmonium
  evidence_ids:
  - deferred-dwh-source
  - finite-boundaries
  - rateadaptingpoissonmodel-source-0
  - familyofharmonium-source-0
  - hierarchicalharmonium-source-0
  summary: Keep the earlier DWH specialization outside the asserted record set.
  details: FoH/HH use binary words and admit a proper Gaussian domain; RAP uses bounded
    hidden counts. In the earlier DWH specialization, integrating Gaussian hidden
    variables gives a positive quadratic term in any count with nonzero coupling.
    This dominates the factorial tail for either sign of coupling, even after correcting
    Gamma(n) to Gamma(n+1). Binary observations do not alter Poisson model support.
    A bounded-support or different-hidden-law revision requires separate primary evidence;
    no silent repair is attributed to the authors.
- assessment_id: versions-and-evaluation
  area: consistency
  topic: Version identity, approximate fitting and empirical limits
  outcome: supported
  target_ids:
  - AIMech:RateAdaptingPoissonModel
  - AIMech:FamilyOfHarmonium
  - AIMech:HierarchicalHarmonium
  evidence_ids:
  - rateadaptingpoissonmodel-source-0
  - familyofharmonium-source-0
  - hierarchicalharmonium-source-0
  - deferred-dwh-source
  summary: Preserve all inspected source and evaluation scopes.
  details: All 29pages were visually read. RAP uses the accessible UCI ICML2006 file;
    the MPI route returned HTML. The semantic-video author manuscript has an author-name
    typo relative to proceedings metadata and is not certified as the final typeset
    file. Its Appendix log-partition display and CD convergence rhetoric are qualified.
    RAP tunes topic count using test-set 1NN performance; DWH fits representation
    before its SVM split; labeled harmonium comparisons mainly use a five-class subset.
    No historical code or benchmark was executed.
- assessment_id: mapping-boundary
  area: grounding
  topic: Model/task mappings and neighboring conditional architectures
  outcome: supported
  target_ids:
  - AIMech:RateAdaptingPoissonModel
  - AIMech:FamilyOfHarmonium
  - AIMech:HierarchicalHarmonium
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain three native model identities with conservative mappings.
  details: All three additions map broadly to AIO Model and related to the underspecified
    RestrictedBoltzmannMachine family. RAP also maps related to task-scoped ProbabilisticTopicModel.
    FoH and HH map related to Classification and MultimodalLearning, preserving model-versus-task
    boundaries. The latter target has a task definition and a deep-learning comment;
    that comment does not prove a deep neural architecture. MultimodalDeepLearning
    explicitly requires a deep neural network and is not mapped. HH has a bipartite
    graph and binary labels, not a class-subsumption hierarchy; HierarchicalClassification
    is therefore not inferred from its name. Conditional logits do not make the whole
    latent model identical to LogisticRegression. Ten native neighbors distinguish
    EFH, GCA, Replicated Softmax, auto-Poisson, auto-normal, CD, Gibbs, mean-field
    Boltzmann learning ULA and conditional RBM without renewed scientific approval.
    The conditional-RBM record models outputs given an external input and explicitly
    curates a binary-hidden specialization; HH instead specifies the joint text/image/label
    law with Gaussian hidden variables.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:RateAdaptingPoissonModel
  - AIMech:FamilyOfHarmonium
  - AIMech:HierarchicalHarmonium
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - rateadaptingpoissonmodel-source-0
  - familyofharmonium-source-0
  - hierarchicalharmonium-source-0
  - deferred-dwh-source
  rationale: Bounded-binomial count harmoniums, class-specific normalized harmoniums
    and shared binary-label harmoniums have distinct supported scopes. Broad Model
    and related RBM/task mappings preserve ontology abstraction. The incompatible
    unbounded-count specialization is retained only as an unresolved discovery candidate.
limitations:
- Adversarial author self-review only; all three records remain DRAFT.
- All 29pages of three primary PDFs were visually read, including formulas, plots,
  algorithm boxes, references and the semantic-video Appendix. Locators use PDF page
  numbers because numeric printed page labels are absent. No author software ran.
- DWH is the 2012 archived v1 of the UAI2005 paper. The semantic-video file is a twelve-page
  author manuscript associated with SDM2007 and prints Eric X. Ping where proceedings
  metadata names Eric P. Xing. RAP is the UCI-hosted ICML2006 file; the MPI route
  returned HTML. Copies and final publisher versions are not certified equivalent.
- RAP finite hidden support guarantees a finite normalizer for finite parameters.
  FoH/HH require positive-definite Gaussian precision, separate class normalizers
  for FoH and binary-cube label semantics for HH. Historical training safeguards and
  exact partition-estimation implementations are not certified.
- The earlier unbounded-count DWH specialization remains deferred. Correcting its
  printed factorial does not fix divergent quadratic tails, and replacing it by a
  bounded law would change the model. No allegation about uninspected author code
  is made.
- The RAP topic dimension is selected using test-set 1NN performance; DWH fits representations
  before its classification split; semantic-video comparisons use a restricted five-class
  subset. These protocols are preserved without asserting universal gains or unverified
  leakage.
- Ten new provisional cohorts leave329 pending leads and other unresolved dispositions.
  All three additions remain DRAFT; no global saturation is claimed.
links: []
tags:
- native-concepts
- multimodal-harmonium-boundaries
- self-review
- discovery-ongoing
```
