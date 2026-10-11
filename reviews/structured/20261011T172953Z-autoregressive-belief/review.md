# Scientific self-review of sigmoid belief and neural autoregressive models

- Review: 20261011T172953Z-autoregressive-belief
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T17:28:04Z
- Finished UTC: 2026-10-11T17:29:53Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain SBN, original binary NADE and DARN as distinct DRAFT architecture records. Their variable roles, factorization, sampling and inference limits, source versions and AIO mapping directions are explicit. No actionable curation finding remains in this declared scope.

## Scope And Provenance

All fields of the exact three-member directed probabilistic architecture cohort.

Selection: The three exact IDs in the saved discovery ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base b57fd0540db90cef0b87b5e08b6a18de1be1debf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SigmoidBeliefNetwork | data/curated/SigmoidBeliefNetwork.yaml | maintained | Sigmoid belief network |
| AIMech:NeuralAutoregressiveDistributionEstimator | data/curated/NeuralAutoregressiveDistributionEstimator.yaml | maintained | Neural autoregressive distribution estimator |
| AIMech:DeepAutoregressiveNetwork | data/curated/DeepAutoregressiveNetwork.yaml | maintained | Deep autoregressive network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:SigmoidBeliefNetwork, AIMech:NeuralAutoregressiveDistributionEstimator, AIMech:DeepAutoregressiveNetwork | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 78.12s (0:01:18)<br>Checked 442 record(s); 0 failed.<br>Checked 346 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 96 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 93,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:SigmoidBeliefNetwork, AIMech:NeuralAutoregressiveDistributionEstimator, AIMech:DeepAutoregressiveNetwork | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:SigmoidBeliefNetwork, AIMech:NeuralAutoregressiveDistributionEstimator, AIMech:DeepAutoregressiveNetwork | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:SigmoidBeliefNetwork, AIMech:NeuralAutoregressiveDistributionEstimator, AIMech:DeepAutoregressiveNetwork | Command exited0 with no output. |
| Sigmoid, NADE and DARN model and gradient boundary calculations | passed | True | AIMech:SigmoidBeliefNetwork, AIMech:NeuralAutoregressiveDistributionEstimator, AIMech:DeepAutoregressiveNetwork | {"sigmoid_belief": {"prior_h1": "1/2", "posterior_h1_given_x1": "3/4", "binary_encoding_transform": "verified"}, "nade": {"joint": {"(0, 0)": 0.375, "(0, 1)": 0.12500000000000003, "(1, 0)": 0.25, "(1, 1)": 0.25}, "total_mass": 1.0, "zero_initialized_total": 0.0, "plus_factor_total": 9.0, "prefix_recurrence_index": "i, not i+1"}, "darn": {"marginal_x1": "1/2", "recognition_to_posterior_kl_nats": 0.2876820724517809, "free_energy_nats": 0.9808292530117262, "negative_log_marginal": 0.6931471805599453, "quadratic_expected_gradient": "3/16", "cubic_expected_gradient": "9/32", "cubic_true_gradient": "3/16"}, "scope": "Finite curator examples and algebra; not author implementation, training, benchmark or general convergence proof."} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:SigmoidBeliefNetwork.

This is the sigmoid conditional family defined by Neal, including equivalent zero/one and minus-one/plus-one encodings. It is not a symmetric Boltzmann machine, a sigmoid activation function alone, or an arbitrary neural network containing sigmoid units. Hidden variables are permitted but not required; the fully visible autoregressive specialization is not treated as an alias for the whole family. Wake-sleep and other inference or learning procedures do not define the model identity. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 343 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 7 and 7 lines respectively. All 6 unique matched line contents were inspected in full: RWS component-model distinctions, its saved review and the carried sigmoid/autoregressive discovery lead, not existing candidate records. Exact checkout counts and differences are retained in the ledger. Thirteen exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and six full native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Choose a topological ordering of binary nodes and directed connections from earlier parents to later nodes. In zero/one encoding let a_i=b_i+sum_j w_ij s_j over parents; then P(s_i=1&#124;parents)=sigmoid(a_i) and P(s_i=0&#124;parents)=1-sigmoid(a_i). Multiplying these locally normalized factors gives the joint distribution without an undirected global partition function. Ancestral sampling visits nodes in topological order. For the equivalent minus-one/plus-one encoding, divide each non-bias weight by two and add half the original incoming-weight sum to the original bias. Marginalizing hidden variables still requires a sum over their configurations, and a Gibbs full conditional uses both the node factor and factors of its children, rather than merely its forward conditional. In the inspected maximum-likelihood learning derivation, gradients of a visible-data log likelihood are posterior expectations of joint log-probability scores; Gibbs sampling is one approximation for those expectations, not a mandatory part of the architecture. Limits: Local normalization and exact ancestral draws do not make arbitrary posterior inference or hidden-variable marginal likelihood tractable. Clamping later observed nodes and using only forward conditionals does not generally sample the desired posterior. The two binary encodings require the stated weight and bias transformation; copying identical numerical parameters between them changes the distribution. The gradient identity requires appropriate posterior expectations. A finite Gibbs run need not provide exact equilibrium samples, rapid mixing or an unbiased implemented learning update. Acyclic probabilistic dependence is not by itself evidence for intervention-level causal interpretation, and the learned units need not represent human-interpretable propositions. No global training optimum, biological implementation or benchmark ranking is asserted. Only the declared portions of the 43-page source were inspected.

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:NeuralAutoregressiveDistributionEstimator.

This record covers the original binary NADE construction of Larochelle and Murray. Its neural hidden activations are deterministic functions of the visible prefix, not stochastic latent variables to be summed out. Mean-field RBM calculations motivate the parameterization; NADE is a separately normalized directed model and does not require a pretrained RBM. Later order-agnostic, real-valued, document and conditional variants need their own scope assessments. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 343 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 7 and 7 lines respectively. All 6 unique matched line contents were inspected in full: RWS component-model distinctions, its saved review and the carried sigmoid/autoregressive discovery lead, not existing candidate records. Exact checkout counts and differences are retained in the ledger. Thirteen exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and six full native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Fix an ordering of D binary observations. For each position i compute h_i=sigmoid(c+W[:,&lt;i] x_&lt;i) and r_i=P(x_i=1&#124;x_&lt;i)=sigmoid(b_i+V[i,:] h_i). The original motivation ties V to the transpose of W, while the paper explicitly also learns separate output weights V; sharing W and c across positions is retained. The joint probability is the product over i of r_i raised to x_i times (1-r_i) raised to (1-x_i). Initialize the hidden preactivation accumulator a_1=c and update a_(i+1)=a_i+W[:,i] x_i after evaluating position i. This reuses prefix work and supports O(DH) evaluation for the original one-hidden-layer construction with H hidden units. Train by differentiating the exact average negative log joint probability. Generate by sampling each visible bit from its prefix conditional in order; no stochastic hidden-state inference or RBM partition function is needed for these operations. Limits: Exact joint evaluation and ancestral generation are properties of the specified NADE distribution, not evidence that it equals an RBM distribution or the data-generating distribution. Arbitrary missing-variable conditionals are not all directly available as forward prefix conditionals. The variable ordering, hidden capacity and optimization affect the fitted model. Original single-hidden-layer complexity does not automatically apply to deeper or order-agnostic variants. The inspected publisher PDF contains inconsistent executable-looking notation: Algorithm 1 initializes a multiplicatively updated probability to zero and places a plus between the two Bernoulli factors; the displayed accumulator-difference equation on printed p.31 uses i+1 where the prefix difference requires i. The curated formulas follow the chain-rule definition, Equations (9)–(11), and the accumulator update in Algorithm 1. These are disclosed mathematical interpretations, not an audit of author software. The nonlinear hidden computation distinguishes NADE from a fully visible sigmoid belief network with only a logistic-linear conditional. Sigmoid hidden activations are the original choice, not a necessity for every valid neural conditional family. No universal density-estimation advantage, fitted-model accuracy or training convergence guarantee is asserted.

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:DeepAutoregressiveNetwork.

This is the DARN family introduced by Gregor and colleagues, not every deep autoregressive model or a time-series forecasting method with a similar name. Its defining latent architecture differs from the fully visible original NADE model and extends paired encoder/decoder modeling with within-layer autoregression. The paper also permits deterministic layers, different conditional parameterizations, non-autoregressive recognition conditionals and an autoregression-free visible layer. Its zero-stochastic-hidden-layer limiting example is the fully visible sigmoid belief network. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 343 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 7 and 7 lines respectively. All 6 unique matched line contents were inspected in full: RWS component-model distinctions, its saved review and the carried sigmoid/autoregressive discovery lead, not existing candidate records. Exact checkout counts and differences are retained in the ledger. Thirteen exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and six full native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood.

In the decoder, factor the top hidden prior along a fixed within-layer order. Each lower stochastic layer conditions each unit on the preceding units in that layer and the complete driving layer above, ending with the visible variables. The basic binary factors are logistic regressions; additional deterministic transformations or more expressive neural conditionals are optional. The recognition model proceeds bottom-up and can likewise be autoregressive within a layer, although the paper usually omits those recognition dependencies. Decoder ancestral sampling follows the top-down layer and within-layer orders and draws exact samples from the specified model; recognition sampling is exact for q but generally only approximate for the model posterior. Jointly train encoder and decoder toward the free-energy cost E_q[log q(h&#124;x)-log p(x,h)], using the paper’s approximate gradient procedure through stochastic units. In Appendix A’s isolated Bernoulli calculation, with probability p depending on parameter theta and downstream f otherwise independent of theta, its final estimator is grad_theta(p) f-prime(h)/(2 q(h)), with h sampled from q. Its expectation equals grad_theta(p) times the average of the endpoint derivatives. This matches the finite-difference gradient for linear or quadratic f but need not for higher-order functions. The record distinguishes this approximation from the exact variational identity. Limits: Efficient ancestral sampling of the joint model does not imply tractable exact marginal likelihood or posterior inference. The source uses explicit latent enumeration for small models and importance estimates for larger ones. The practical estimator can be biased for non-quadratic downstream functions; a curator cubic example checks that boundary. The isolated-unit calculation does not certify all gradient paths of the complete multilayer implementation, variance reduction or convergence. A restricted recognition family may not contain the true posterior. Minimizing the variational objective within that family does not remove its approximation gap automatically. Within-layer autoregression is directed and ordered, not an undirected recurrent connection. Exact model samples do not establish causal semantics or fidelity to observed data. Equation (4) in the publisher PDF prints the visible dimension as the upper product index for recognition hidden variables; this record interprets the product over the declared hidden units, consistent with the surrounding definition and multilayer Equation (8). No author-code behavior is inferred. The supplement contains generated sample images, not the gradient derivation; Appendix A of the main paper supplies that derivation. No benchmark ranking, universal runtime advantage or trained-model result is curated.

### Locally normalized directed factors, binary encodings and conditional inference

consistency: supported. Targets: AIMech:SigmoidBeliefNetwork.

Retain the binary logistic conditional model family.

The inspected Neal definitions specify ordered directed factors. Zero/one to signed encoding halves non-bias weights and shifts biases by half the original weight sum; the finite example checks this equality. A parent-to-child forward factor is not a Gibbs full conditional or posterior: the binary example has prior1/2 and posterior3/4 after observing the child. Exact joint ancestral generation and local normalization do not eliminate the hidden-state sum or guarantee Gibbs mixing. The native family is narrower than AIO BayesianNetwork, so broad_match direction is justified.

### Deterministic prefix features, normalized density and printed pseudocode

consistency: supported. Targets: AIMech:NeuralAutoregressiveDistributionEstimator.

Retain original binary NADE separately from sigmoid-linear and latent models.

The source’s neural hidden activations parameterize visible-prefix conditionals deterministically. The probability product is normalized independently of its RBM inspiration. Shared input weights and hidden biases permit prefix reuse, while output weights may be untied. The printed zero initialization and plus between Bernoulli factors in Algorithm1 conflict with the chain-rule density, and the preceding accumulator difference has an index conflict. These are disclosed and not transcribed as executable mechanism: the curator two-bit model has total mass1, zero-initialized accumulation yields0, and a plus-factor interpretation starting at1 yields mass9. The correct prefix update uses the just-observed variable i. No author-code defect or empirical failure is inferred.

### Autoregressive stochastic layers, recognition inference and approximate gradients

consistency: supported. Targets: AIMech:DeepAutoregressiveNetwork.

Retain DARN as a distinct paired architecture.

Ordered within-layer generative dependencies preserve acyclicity and permit exact model draws. The separately parameterized recognition model does not automatically equal the posterior. Optional deterministic layers and factorized recognition or visible variants are within the paper’s family; its zero-latent limiting case is explicitly identified without equating the main family to NADE. The variational free-energy identity remains exact under normalized distributions, while AppendixA’s isolated-unit endpoint-derivative estimator can be biased. At Bernoulli probability1/4 a quadratic has expected and exact logit gradient3/16; a cubic has expected9/32 versus exact3/16. The printed recognition-product dimension is interpreted over hidden units consistently with Eq8. The supplemental image page supplies no gradient proof.

### Broad directed-model mappings and a paired-architecture component relation

grounding: supported. Targets: AIMech:SigmoidBeliefNetwork, AIMech:NeuralAutoregressiveDistributionEstimator, AIMech:DeepAutoregressiveNetwork.

Retain SBN and NADE broad mappings and DARN related mapping.

All 32 semantic label/scoped-synonym hits, thirteen exact AIO CLASS nodes including full annotations and outgoing edges, and six complete native neighboring records were read. SBN and original NADE each receive broad_match to BayesianNetwork, with the AIO target broader than their binary logistic or shared-neural-factor families. DARN receives related_match to BayesianNetwork for its directed generative component, since the whole identity includes a separate recognition network. BoltzmannMachineNetwork and RestrictedBoltzmannMachine are undirected model boundaries, not equivalent identities. DeepBeliefNetwork, AutoEncoderNetwork and VariationalAutoEncoder do not establish the particular identities, and their pretrained/latent conventions are not forced onto NADE. ProbabilisticGraphicalModel is task-level context; ProbabilisticHiddenLayer has a category-probability definition; SigmoidFunction is a component. AutoregressiveLanguageModel and AutoregressiveMovingAverage have language and time-series scope, respectively. DeepFeedForwardNetwork does not identify the factorization and latent distinctions. CausalGraphicalModel is not inferred from a DAG alone. Neighboring records provide boundaries, not fresh whole-record approvals.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:SigmoidBeliefNetwork, AIMech:NeuralAutoregressiveDistributionEstimator, AIMech:DeepAutoregressiveNetwork. SBN is the binary logistic directed factor family. Original NADE uses deterministic shared neural prefix features to parameterize a fully visible distribution. DARN combines stochastic autoregressive hidden layers and a distinct recognition network. Shared directed factors or sigmoid components do not establish identity equivalence.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T172717Z-autoregressive-belief.json | supports | All 442 pinned AIO labels/scoped synonyms and 343 preceding native IDs/names/aliases were compared, with no normalized identity match. Both ignored- and hidden-inclusive full-checkout scans returned seven lines, identical after sorting. All six unique matched line contents were read in full: RWS component-model contrasts, its saved review and the prior component-model discovery lead. Thirteen exact AIO CLASS nodes with complete annotations and outgoing edges, and six full maintained neighbors, were inspected. Absence is bounded to this snapshot and semantic neighborhood. |
| mapping | sources/aio/aio.json; Thirteen exact CLASS nodes with complete annotations and outgoing edges in source_analysis.aio_mapping_inspection | supports | All 32 semantic label/scoped-synonym hits, thirteen exact AIO CLASS nodes including full annotations and outgoing edges, and six complete native neighboring records were read. SBN and original NADE each receive broad_match to BayesianNetwork, with the AIO target broader than their binary logistic or shared-neural-factor families. DARN receives related_match to BayesianNetwork for its directed generative component, since the whole identity includes a separate recognition network. BoltzmannMachineNetwork and RestrictedBoltzmannMachine are undirected model boundaries, not equivalent identities. DeepBeliefNetwork, AutoEncoderNetwork and VariationalAutoEncoder do not establish the particular identities, and their pretrained/latent conventions are not forced onto NADE. ProbabilisticGraphicalModel is task-level context; ProbabilisticHiddenLayer has a category-probability definition; SigmoidFunction is a component. AutoregressiveLanguageModel and AutoregressiveMovingAverage have language and time-series scope, respectively. DeepFeedForwardNetwork does not identify the factorization and latent distinctions. CausalGraphicalModel is not inferred from a DAG alone. Neighboring records provide boundaries, not fresh whole-record approvals. |
| neighbors | research/discovery/20261011T172717Z-autoregressive-belief.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Complete HelmholtzMachine, WakeSleepAlgorithm, ReweightedWakeSleep, NeuralVariationalInferenceAndLearning, StraightThroughEstimator and GibbsSampling records were read. They distinguish paired architectures, training objectives, importance updates, approximate inference, surrogate derivatives and full conditional resampling. Prior records and mappings are boundary context, not newly approved. |
| source-host | https://www.cs.toronto.edu/~bonner/ | supports | The university homepage identifies Anthony Bonner and lists CSC321 spring2016 among his courses. This supports the third-party course-host attribution for the Neal scan. The specific course-index opening failed, and publisher byte equivalence is not asserted. |
| finite-conventions | research/discovery/autoregressive-belief-boundaries.py; Binary encoding and posterior calculation; two-bit NADE product and recurrence; latent DARN free energy and quadratic/cubic estimator expectations | supports | Finite sigmoid-network enumeration separates a forward prior from a posterior; binary-encoding transformations are checked. An original two-bit NADE instance normalizes, while the printed zero initialization and plus-factor interpretations do not. A small DARN model separates marginal likelihood from variational free energy, and its isolated-unit gradient estimator is checked on quadratic and cubic functions. These are curator calculations, not author-code tests or benchmarks. |
| sigmoidbeliefnetwork-source-0 | https://www.cs.toronto.edu/~bonner/courses/2016s/csc321/readings/Connectionist%20learning%20of%20belief%20networks.pdf; Sections 3.1–3.2, Equations (8)–(9), printed pp.77–78 / PDF pp.7–8; Section 4.1, Equations (11)–(17), pp.79–81 / PDF pp.9–11; Section 5.1, Equations (21)–(27), pp.82–84 / PDF pp.12–14 | supports | Connectionist learning of belief networks. 43-page published scan, Artificial Intelligence 56 (1992):71–113, hosted in a University of Toronto course directory maintained by Anthony Bonner. This is a third-party course copy, not an author-hosted or byte-verified publisher download. Printed page = PDF page + 70. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| neuralautoregressivedistributionestimator-source-0 | https://proceedings.mlr.press/v15/larochelle11a/larochelle11a.pdf; Sections 3–5, Equations (3), (9)–(11), Figure 1 and Algorithm 1, printed pp.30–33 / PDF pp.2–5 | supports | The Neural Autoregressive Distribution Estimator. AISTATS 2011, PMLR 15:29–37; nine-page publisher PDF. Printed page = PDF page + 28. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| deepautoregressivenetwork-source-0 | https://proceedings.mlr.press/v32/gregor14.pdf; Sections 2–4, Equations (1)–(15), PDF pp.2–5; marginal-likelihood scope, Section 5, p.5; Appendix A, Equations (17)–(24), pp.7–8 | supports | Deep AutoRegressive Networks. ICML 2014, PMLR 32(2):1242–1250; nine-page publisher PDF with Appendix A on PDF pp.7–8. Printed proceedings page numbers are absent. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |

## Limits And Additional Notes

- Author self-review only; all records remain DRAFT.
- The Neal file is a third-party university course scan; publisher-file byte equivalence was not established. NADE and DARN use the declared publisher PDFs.
- Only declared pages were read; full implementations, general convergence proofs and empirical comparisons were not audited.
- Printed formula discrepancies are qualified explicitly. Finite calculations illustrate boundaries and do not prove general performance or implementation behavior.
- There are 190 pending inspection leads plus unresolved dispositions; discovery remains active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T172953Z-autoregressive-belief
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of sigmoid belief and neural autoregressive models
started_at: '2026-10-11T17:28:04Z'
finished_at: '2026-10-11T17:29:53Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially checked every field of the
    three directed-probabilistic architecture records against the declared primary
    PDF sections/images, thirteen exact AIO nodes, six complete maintained neighbors
    and original finite calculations. Stochastic versus deterministic hidden roles,
    exact generation versus inference, binary encoding, printed formula conflicts,
    isolated-unit gradient bias and mapping direction were examined. This is author
    self-review.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain SBN, original binary NADE and DARN as distinct DRAFT architecture
  records. Their variable roles, factorization, sampling and inference limits, source
  versions and AIO mapping directions are explicit. No actionable curation finding
  remains in this declared scope.
source:
  git_revision: b57fd0540db90cef0b87b5e08b6a18de1be1debf
  state: working_tree
  inputs:
  - path: data/aio/AutoEncoderNetwork.yaml
    sha256: 7a5eb5c54dab03959ca7a19c03a4c4ece161b05618255294e61df174bcaa4521
    role: context
  - path: data/aio/AutoregressiveLanguageModel.yaml
    sha256: 1ee5824569635aab5df1b1f23eaabca463bd7ef87d1b22e9d9c42375a49ec800
    role: context
  - path: data/aio/AutoregressiveMovingAverage.yaml
    sha256: eb69aaedb34d8c9e620ef4f0d20111feaf9c3dd09236f57536561e9a6cccdf53
    role: context
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/BoltzmannMachineNetwork.yaml
    sha256: 1152d2d85c5c1c408a0420e13f211ed109b12fb289c706ee7449864e91aece03
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/DeepBeliefNetwork.yaml
    sha256: e6912732493adbfea3b48e01184d33682ad262dd73801757c094a2b160046a58
    role: context
  - path: data/aio/DeepFeedForwardNetwork.yaml
    sha256: d66c246318687598cf762fae4b54586a312b70d143735aba5c12b2606c45c8c9
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ProbabilisticHiddenLayer.yaml
    sha256: 610c29db815f7348c5bdcdc7e7460dd2dea9ea338f3727ebb1596c51b4af41da
    role: context
  - path: data/aio/RestrictedBoltzmannMachine.yaml
    sha256: 322fcb3b1f6064d944379ed79ffdcb7360fc2c3edd300c0a5a3f46be1f48df43
    role: context
  - path: data/aio/SigmoidFunction.yaml
    sha256: e112ec27a5b6fc9de17cc2d3354b836968b6693c6902cf004b71f05a0aedb193
    role: context
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/curated/DeepAutoregressiveNetwork.yaml
    sha256: 424d6296a8f402fb443308c3222a835af2f9fddfd5f253773645276dd53b017e
    role: target
  - path: data/curated/GibbsSampling.yaml
    sha256: 8175215986c0507e3664a3aedf8074fc067d85b4a89002091d1bcb9b637a522a
    role: context
  - path: data/curated/HelmholtzMachine.yaml
    sha256: 9b582e184b171ae372dca219cd6704318a9287150dcbf540f95a8b4cc6405cac
    role: context
  - path: data/curated/NeuralAutoregressiveDistributionEstimator.yaml
    sha256: 13578d60229a30803baa9444bda45c5ec3b561520b0bdaaba261eaa022ed1e41
    role: target
  - path: data/curated/NeuralVariationalInferenceAndLearning.yaml
    sha256: 0d24a286ed64974478f452907c018d9618348ef4900808ea97b80036b1dfb06c
    role: context
  - path: data/curated/ReweightedWakeSleep.yaml
    sha256: 49509aa6868bcefabf54790503a9d5b87f0d873ab1589cdb6677b5575b3c8997
    role: context
  - path: data/curated/SigmoidBeliefNetwork.yaml
    sha256: 5fa2d037504b10f0d11db0ebdfef5b7d0f8175d4739d45a3abea789d00164c6a
    role: target
  - path: data/curated/StraightThroughEstimator.yaml
    sha256: 9476ce3dca57298172b11bd84d6132d00c9e5f8bd084d3202d10f159024dfe7a
    role: context
  - path: data/curated/WakeSleepAlgorithm.yaml
    sha256: 48b795b8f0730fc884c1809d405e125ec09b3a906e9b875f9ff3b1772fb21f48
    role: context
  - path: research/discovery/20261011T172717Z-autoregressive-belief.json
    sha256: 0a65645b5b127c852508d97de3772ccf8d95238c43dffb31a2dc9137efed5e47
    role: context
  - path: research/discovery/autoregressive-belief-boundaries.py
    sha256: 23cdcb2ae4a3c4b9f541009381cc0b5be636ee50f4493f68a04955e0ac73c736
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
- target_id: AIMech:SigmoidBeliefNetwork
  path: data/curated/SigmoidBeliefNetwork.yaml
  label: Sigmoid belief network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SigmoidBeliefNetwork.yaml
    role: maintained
- target_id: AIMech:NeuralAutoregressiveDistributionEstimator
  path: data/curated/NeuralAutoregressiveDistributionEstimator.yaml
  label: Neural autoregressive distribution estimator
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NeuralAutoregressiveDistributionEstimator.yaml
    role: maintained
- target_id: AIMech:DeepAutoregressiveNetwork
  path: data/curated/DeepAutoregressiveNetwork.yaml
  label: Deep autoregressive network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DeepAutoregressiveNetwork.yaml
    role: maintained
scope:
  description: All fields of the exact three-member directed probabilistic architecture
    cohort.
  selection: The three exact IDs in the saved discovery ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:SigmoidBeliefNetwork
  - AIMech:NeuralAutoregressiveDistributionEstimator
  - AIMech:DeepAutoregressiveNetwork
  exclusions:
  - target: Uninspected frontier concepts and full executable implementations
    reason: Fully visible and conditional specializations, noisy-OR models, later
      NADE variants, coding methods and other frontier cohorts remain open; author
      software was not inspected or run.
  - target: Prior corpus, unread pages and empirical ranking
    reason: Prior records provide boundary context. Only the declared source reading
      and finite curator calculations support this review.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:SigmoidBeliefNetwork
  - AIMech:NeuralAutoregressiveDistributionEstimator
  - AIMech:DeepAutoregressiveNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 78.12s (0:01:18)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 346 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 96 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 93,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:SigmoidBeliefNetwork
  - AIMech:NeuralAutoregressiveDistributionEstimator
  - AIMech:DeepAutoregressiveNetwork
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
  - AIMech:SigmoidBeliefNetwork
  - AIMech:NeuralAutoregressiveDistributionEstimator
  - AIMech:DeepAutoregressiveNetwork
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
  - AIMech:SigmoidBeliefNetwork
  - AIMech:NeuralAutoregressiveDistributionEstimator
  - AIMech:DeepAutoregressiveNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited0 with no output.
- check_id: finite-arithmetic
  name: Sigmoid, NADE and DARN model and gradient boundary calculations
  command: python3 research/discovery/autoregressive-belief-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SigmoidBeliefNetwork
  - AIMech:NeuralAutoregressiveDistributionEstimator
  - AIMech:DeepAutoregressiveNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: '{"sigmoid_belief": {"prior_h1": "1/2", "posterior_h1_given_x1": "3/4",
    "binary_encoding_transform": "verified"}, "nade": {"joint": {"(0, 0)": 0.375,
    "(0, 1)": 0.12500000000000003, "(1, 0)": 0.25, "(1, 1)": 0.25}, "total_mass":
    1.0, "zero_initialized_total": 0.0, "plus_factor_total": 9.0, "prefix_recurrence_index":
    "i, not i+1"}, "darn": {"marginal_x1": "1/2", "recognition_to_posterior_kl_nats":
    0.2876820724517809, "free_energy_nats": 0.9808292530117262, "negative_log_marginal":
    0.6931471805599453, "quadratic_expected_gradient": "3/16", "cubic_expected_gradient":
    "9/32", "cubic_true_gradient": "3/16"}, "scope": "Finite curator examples and
    algebra; not author implementation, training, benchmark or general convergence
    proof."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T172717Z-autoregressive-belief.json
  accessed_at: '2026-10-11T17:28:04Z'
  support: supports
  summary: 'All 442 pinned AIO labels/scoped synonyms and 343 preceding native IDs/names/aliases
    were compared, with no normalized identity match. Both ignored- and hidden-inclusive
    full-checkout scans returned seven lines, identical after sorting. All six unique
    matched line contents were read in full: RWS component-model contrasts, its saved
    review and the prior component-model discovery lead. Thirteen exact AIO CLASS
    nodes with complete annotations and outgoing edges, and six full maintained neighbors,
    were inspected. Absence is bounded to this snapshot and semantic neighborhood.'
  search_scope: 'All 442 pinned AIO labels/scoped synonyms and 343 preceding native
    IDs/names/aliases were compared, with no normalized identity match. Both ignored-
    and hidden-inclusive full-checkout scans returned seven lines, identical after
    sorting. All six unique matched line contents were read in full: RWS component-model
    contrasts, its saved review and the prior component-model discovery lead. Thirteen
    exact AIO CLASS nodes with complete annotations and outgoing edges, and six full
    maintained neighbors, were inspected. Absence is bounded to this snapshot and
    semantic neighborhood.'
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Thirteen exact CLASS nodes with complete annotations and outgoing edges
    in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T17:28:04Z'
  support: supports
  summary: All 32 semantic label/scoped-synonym hits, thirteen exact AIO CLASS nodes
    including full annotations and outgoing edges, and six complete native neighboring
    records were read. SBN and original NADE each receive broad_match to BayesianNetwork,
    with the AIO target broader than their binary logistic or shared-neural-factor
    families. DARN receives related_match to BayesianNetwork for its directed generative
    component, since the whole identity includes a separate recognition network. BoltzmannMachineNetwork
    and RestrictedBoltzmannMachine are undirected model boundaries, not equivalent
    identities. DeepBeliefNetwork, AutoEncoderNetwork and VariationalAutoEncoder do
    not establish the particular identities, and their pretrained/latent conventions
    are not forced onto NADE. ProbabilisticGraphicalModel is task-level context; ProbabilisticHiddenLayer
    has a category-probability definition; SigmoidFunction is a component. AutoregressiveLanguageModel
    and AutoregressiveMovingAverage have language and time-series scope, respectively.
    DeepFeedForwardNetwork does not identify the factorization and latent distinctions.
    CausalGraphicalModel is not inferred from a DAG alone. Neighboring records provide
    boundaries, not fresh whole-record approvals.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T172717Z-autoregressive-belief.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T17:28:04Z'
  support: supports
  summary: Complete HelmholtzMachine, WakeSleepAlgorithm, ReweightedWakeSleep, NeuralVariationalInferenceAndLearning,
    StraightThroughEstimator and GibbsSampling records were read. They distinguish
    paired architectures, training objectives, importance updates, approximate inference,
    surrogate derivatives and full conditional resampling. Prior records and mappings
    are boundary context, not newly approved.
- evidence_id: source-host
  kind: primary_source
  reference: https://www.cs.toronto.edu/~bonner/
  accessed_at: '2026-10-11T17:27:48Z'
  support: supports
  summary: The university homepage identifies Anthony Bonner and lists CSC321 spring2016
    among his courses. This supports the third-party course-host attribution for the
    Neal scan. The specific course-index opening failed, and publisher byte equivalence
    is not asserted.
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/autoregressive-belief-boundaries.py
  locator: Binary encoding and posterior calculation; two-bit NADE product and recurrence;
    latent DARN free energy and quadratic/cubic estimator expectations
  accessed_at: '2026-10-11T17:28:04Z'
  snapshot_sha256: 23cdcb2ae4a3c4b9f541009381cc0b5be636ee50f4493f68a04955e0ac73c736
  support: supports
  summary: Finite sigmoid-network enumeration separates a forward prior from a posterior;
    binary-encoding transformations are checked. An original two-bit NADE instance
    normalizes, while the printed zero initialization and plus-factor interpretations
    do not. A small DARN model separates marginal likelihood from variational free
    energy, and its isolated-unit gradient estimator is checked on quadratic and cubic
    functions. These are curator calculations, not author-code tests or benchmarks.
- evidence_id: sigmoidbeliefnetwork-source-0
  kind: primary_source
  reference: https://www.cs.toronto.edu/~bonner/courses/2016s/csc321/readings/Connectionist%20learning%20of%20belief%20networks.pdf
  locator: Sections 3.1–3.2, Equations (8)–(9), printed pp.77–78 / PDF pp.7–8; Section
    4.1, Equations (11)–(17), pp.79–81 / PDF pp.9–11; Section 5.1, Equations (21)–(27),
    pp.82–84 / PDF pp.12–14
  accessed_at: '2026-10-11T17:14:17Z'
  snapshot_sha256: 4e4f40a92dced6ad1fbce4e464adca496e73991060d21a7d6d5bccef296a164a
  support: supports
  summary: Connectionist learning of belief networks. 43-page published scan, Artificial
    Intelligence 56 (1992):71–113, hosted in a University of Toronto course directory
    maintained by Anthony Bonner. This is a third-party course copy, not an author-hosted
    or byte-verified publisher download. Printed page = PDF page + 70. Actual paper
    and HTML reading scopes are declared in source_analysis; extraction, rendering
    and a full-text access label do not establish that every page was read.
- evidence_id: neuralautoregressivedistributionestimator-source-0
  kind: primary_source
  reference: https://proceedings.mlr.press/v15/larochelle11a/larochelle11a.pdf
  locator: Sections 3–5, Equations (3), (9)–(11), Figure 1 and Algorithm 1, printed
    pp.30–33 / PDF pp.2–5
  accessed_at: '2026-10-11T17:14:24Z'
  snapshot_sha256: b1fe502ea1b3f84875d5e13aefec479827b3a33ab1ebdcf3eb4a3d71a5a4ea9a
  support: supports
  summary: The Neural Autoregressive Distribution Estimator. AISTATS 2011, PMLR 15:29–37;
    nine-page publisher PDF. Printed page = PDF page + 28. Actual paper and HTML reading
    scopes are declared in source_analysis; extraction, rendering and a full-text
    access label do not establish that every page was read.
- evidence_id: deepautoregressivenetwork-source-0
  kind: primary_source
  reference: https://proceedings.mlr.press/v32/gregor14.pdf
  locator: Sections 2–4, Equations (1)–(15), PDF pp.2–5; marginal-likelihood scope,
    Section 5, p.5; Appendix A, Equations (17)–(24), pp.7–8
  accessed_at: '2026-10-11T17:14:27Z'
  snapshot_sha256: 6b917b288dc41b57972d86d1e86e7710e1d3ca55627cb0b8a0940d0ebb1dee89
  support: supports
  summary: Deep AutoRegressive Networks. ICML 2014, PMLR 32(2):1242–1250; nine-page
    publisher PDF with Appendix A on PDF pp.7–8. Printed proceedings page numbers
    are absent. Actual paper and HTML reading scopes are declared in source_analysis;
    extraction, rendering and a full-text access label do not establish that every
    page was read.
assessments:
- assessment_id: sigmoidbeliefnetwork
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:SigmoidBeliefNetwork
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - sigmoidbeliefnetwork-source-0
  summary: 'This is the sigmoid conditional family defined by Neal, including equivalent
    zero/one and minus-one/plus-one encodings. It is not a symmetric Boltzmann machine,
    a sigmoid activation function alone, or an arbitrary neural network containing
    sigmoid units. Hidden variables are permitted but not required; the fully visible
    autoregressive specialization is not treated as an alias for the whole family.
    Wake-sleep and other inference or learning procedures do not define the model
    identity. No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 343 preceding native IDs/names/aliases. Full-checkout fixed-string
    searches included ignored and hidden files in worktree and main, returning 7 and
    7 lines respectively. All 6 unique matched line contents were inspected in full:
    RWS component-model distinctions, its saved review and the carried sigmoid/autoregressive
    discovery lead, not existing candidate records. Exact checkout counts and differences
    are retained in the ledger. Thirteen exact AIO CLASS nodes with scoped synonyms/comments
    and outgoing edges and six full native neighboring records were inspected. Absence
    is bounded to this snapshot and semantic neighborhood.'
  details: 'Choose a topological ordering of binary nodes and directed connections
    from earlier parents to later nodes. In zero/one encoding let a_i=b_i+sum_j w_ij
    s_j over parents; then P(s_i=1|parents)=sigmoid(a_i) and P(s_i=0|parents)=1-sigmoid(a_i).
    Multiplying these locally normalized factors gives the joint distribution without
    an undirected global partition function. Ancestral sampling visits nodes in topological
    order. For the equivalent minus-one/plus-one encoding, divide each non-bias weight
    by two and add half the original incoming-weight sum to the original bias. Marginalizing
    hidden variables still requires a sum over their configurations, and a Gibbs full
    conditional uses both the node factor and factors of its children, rather than
    merely its forward conditional. In the inspected maximum-likelihood learning derivation,
    gradients of a visible-data log likelihood are posterior expectations of joint
    log-probability scores; Gibbs sampling is one approximation for those expectations,
    not a mandatory part of the architecture. Limits: Local normalization and exact
    ancestral draws do not make arbitrary posterior inference or hidden-variable marginal
    likelihood tractable. Clamping later observed nodes and using only forward conditionals
    does not generally sample the desired posterior. The two binary encodings require
    the stated weight and bias transformation; copying identical numerical parameters
    between them changes the distribution. The gradient identity requires appropriate
    posterior expectations. A finite Gibbs run need not provide exact equilibrium
    samples, rapid mixing or an unbiased implemented learning update. Acyclic probabilistic
    dependence is not by itself evidence for intervention-level causal interpretation,
    and the learned units need not represent human-interpretable propositions. No
    global training optimum, biological implementation or benchmark ranking is asserted.
    Only the declared portions of the 43-page source were inspected.'
  dimensions:
  - name: concept-kind
    value: architecture
    definition: A reusable directed probabilistic architecture, with stochastic-variable
      and deterministic-computation roles stated explicitly; not a trained instance
      or benchmark outcome.
    evidence_ids:
    - sigmoidbeliefnetwork-source-0
  - name: aio-assessment
    value: broad_match
    definition: All 32 semantic label/scoped-synonym hits, thirteen exact AIO CLASS
      nodes including full annotations and outgoing edges, and six complete native
      neighboring records were read. SBN and original NADE each receive broad_match
      to BayesianNetwork, with the AIO target broader than their binary logistic or
      shared-neural-factor families. DARN receives related_match to BayesianNetwork
      for its directed generative component, since the whole identity includes a separate
      recognition network. BoltzmannMachineNetwork and RestrictedBoltzmannMachine
      are undirected model boundaries, not equivalent identities. DeepBeliefNetwork,
      AutoEncoderNetwork and VariationalAutoEncoder do not establish the particular
      identities, and their pretrained/latent conventions are not forced onto NADE.
      ProbabilisticGraphicalModel is task-level context; ProbabilisticHiddenLayer
      has a category-probability definition; SigmoidFunction is a component. AutoregressiveLanguageModel
      and AutoregressiveMovingAverage have language and time-series scope, respectively.
      DeepFeedForwardNetwork does not identify the factorization and latent distinctions.
      CausalGraphicalModel is not inferred from a DAG alone. Neighboring records provide
      boundaries, not fresh whole-record approvals.
    evidence_ids:
    - mapping
- assessment_id: neuralautoregressivedistributionestimator
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:NeuralAutoregressiveDistributionEstimator
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - neuralautoregressivedistributionestimator-source-0
  summary: 'This record covers the original binary NADE construction of Larochelle
    and Murray. Its neural hidden activations are deterministic functions of the visible
    prefix, not stochastic latent variables to be summed out. Mean-field RBM calculations
    motivate the parameterization; NADE is a separately normalized directed model
    and does not require a pretrained RBM. Later order-agnostic, real-valued, document
    and conditional variants need their own scope assessments. No normalized identity
    match was found across all 442 pinned AIO labels/scoped synonyms and 343 preceding
    native IDs/names/aliases. Full-checkout fixed-string searches included ignored
    and hidden files in worktree and main, returning 7 and 7 lines respectively. All
    6 unique matched line contents were inspected in full: RWS component-model distinctions,
    its saved review and the carried sigmoid/autoregressive discovery lead, not existing
    candidate records. Exact checkout counts and differences are retained in the ledger.
    Thirteen exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges
    and six full native neighboring records were inspected. Absence is bounded to
    this snapshot and semantic neighborhood.'
  details: 'Fix an ordering of D binary observations. For each position i compute
    h_i=sigmoid(c+W[:,<i] x_<i) and r_i=P(x_i=1|x_<i)=sigmoid(b_i+V[i,:] h_i). The
    original motivation ties V to the transpose of W, while the paper explicitly also
    learns separate output weights V; sharing W and c across positions is retained.
    The joint probability is the product over i of r_i raised to x_i times (1-r_i)
    raised to (1-x_i). Initialize the hidden preactivation accumulator a_1=c and update
    a_(i+1)=a_i+W[:,i] x_i after evaluating position i. This reuses prefix work and
    supports O(DH) evaluation for the original one-hidden-layer construction with
    H hidden units. Train by differentiating the exact average negative log joint
    probability. Generate by sampling each visible bit from its prefix conditional
    in order; no stochastic hidden-state inference or RBM partition function is needed
    for these operations. Limits: Exact joint evaluation and ancestral generation
    are properties of the specified NADE distribution, not evidence that it equals
    an RBM distribution or the data-generating distribution. Arbitrary missing-variable
    conditionals are not all directly available as forward prefix conditionals. The
    variable ordering, hidden capacity and optimization affect the fitted model. Original
    single-hidden-layer complexity does not automatically apply to deeper or order-agnostic
    variants. The inspected publisher PDF contains inconsistent executable-looking
    notation: Algorithm 1 initializes a multiplicatively updated probability to zero
    and places a plus between the two Bernoulli factors; the displayed accumulator-difference
    equation on printed p.31 uses i+1 where the prefix difference requires i. The
    curated formulas follow the chain-rule definition, Equations (9)–(11), and the
    accumulator update in Algorithm 1. These are disclosed mathematical interpretations,
    not an audit of author software. The nonlinear hidden computation distinguishes
    NADE from a fully visible sigmoid belief network with only a logistic-linear conditional.
    Sigmoid hidden activations are the original choice, not a necessity for every
    valid neural conditional family. No universal density-estimation advantage, fitted-model
    accuracy or training convergence guarantee is asserted.'
  dimensions:
  - name: concept-kind
    value: architecture
    definition: A reusable directed probabilistic architecture, with stochastic-variable
      and deterministic-computation roles stated explicitly; not a trained instance
      or benchmark outcome.
    evidence_ids:
    - neuralautoregressivedistributionestimator-source-0
  - name: aio-assessment
    value: broad_match
    definition: All 32 semantic label/scoped-synonym hits, thirteen exact AIO CLASS
      nodes including full annotations and outgoing edges, and six complete native
      neighboring records were read. SBN and original NADE each receive broad_match
      to BayesianNetwork, with the AIO target broader than their binary logistic or
      shared-neural-factor families. DARN receives related_match to BayesianNetwork
      for its directed generative component, since the whole identity includes a separate
      recognition network. BoltzmannMachineNetwork and RestrictedBoltzmannMachine
      are undirected model boundaries, not equivalent identities. DeepBeliefNetwork,
      AutoEncoderNetwork and VariationalAutoEncoder do not establish the particular
      identities, and their pretrained/latent conventions are not forced onto NADE.
      ProbabilisticGraphicalModel is task-level context; ProbabilisticHiddenLayer
      has a category-probability definition; SigmoidFunction is a component. AutoregressiveLanguageModel
      and AutoregressiveMovingAverage have language and time-series scope, respectively.
      DeepFeedForwardNetwork does not identify the factorization and latent distinctions.
      CausalGraphicalModel is not inferred from a DAG alone. Neighboring records provide
      boundaries, not fresh whole-record approvals.
    evidence_ids:
    - mapping
- assessment_id: deepautoregressivenetwork
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:DeepAutoregressiveNetwork
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - deepautoregressivenetwork-source-0
  summary: 'This is the DARN family introduced by Gregor and colleagues, not every
    deep autoregressive model or a time-series forecasting method with a similar name.
    Its defining latent architecture differs from the fully visible original NADE
    model and extends paired encoder/decoder modeling with within-layer autoregression.
    The paper also permits deterministic layers, different conditional parameterizations,
    non-autoregressive recognition conditionals and an autoregression-free visible
    layer. Its zero-stochastic-hidden-layer limiting example is the fully visible
    sigmoid belief network. No normalized identity match was found across all 442
    pinned AIO labels/scoped synonyms and 343 preceding native IDs/names/aliases.
    Full-checkout fixed-string searches included ignored and hidden files in worktree
    and main, returning 7 and 7 lines respectively. All 6 unique matched line contents
    were inspected in full: RWS component-model distinctions, its saved review and
    the carried sigmoid/autoregressive discovery lead, not existing candidate records.
    Exact checkout counts and differences are retained in the ledger. Thirteen exact
    AIO CLASS nodes with scoped synonyms/comments and outgoing edges and six full
    native neighboring records were inspected. Absence is bounded to this snapshot
    and semantic neighborhood.'
  details: 'In the decoder, factor the top hidden prior along a fixed within-layer
    order. Each lower stochastic layer conditions each unit on the preceding units
    in that layer and the complete driving layer above, ending with the visible variables.
    The basic binary factors are logistic regressions; additional deterministic transformations
    or more expressive neural conditionals are optional. The recognition model proceeds
    bottom-up and can likewise be autoregressive within a layer, although the paper
    usually omits those recognition dependencies. Decoder ancestral sampling follows
    the top-down layer and within-layer orders and draws exact samples from the specified
    model; recognition sampling is exact for q but generally only approximate for
    the model posterior. Jointly train encoder and decoder toward the free-energy
    cost E_q[log q(h|x)-log p(x,h)], using the paper’s approximate gradient procedure
    through stochastic units. In Appendix A’s isolated Bernoulli calculation, with
    probability p depending on parameter theta and downstream f otherwise independent
    of theta, its final estimator is grad_theta(p) f-prime(h)/(2 q(h)), with h sampled
    from q. Its expectation equals grad_theta(p) times the average of the endpoint
    derivatives. This matches the finite-difference gradient for linear or quadratic
    f but need not for higher-order functions. The record distinguishes this approximation
    from the exact variational identity. Limits: Efficient ancestral sampling of the
    joint model does not imply tractable exact marginal likelihood or posterior inference.
    The source uses explicit latent enumeration for small models and importance estimates
    for larger ones. The practical estimator can be biased for non-quadratic downstream
    functions; a curator cubic example checks that boundary. The isolated-unit calculation
    does not certify all gradient paths of the complete multilayer implementation,
    variance reduction or convergence. A restricted recognition family may not contain
    the true posterior. Minimizing the variational objective within that family does
    not remove its approximation gap automatically. Within-layer autoregression is
    directed and ordered, not an undirected recurrent connection. Exact model samples
    do not establish causal semantics or fidelity to observed data. Equation (4) in
    the publisher PDF prints the visible dimension as the upper product index for
    recognition hidden variables; this record interprets the product over the declared
    hidden units, consistent with the surrounding definition and multilayer Equation
    (8). No author-code behavior is inferred. The supplement contains generated sample
    images, not the gradient derivation; Appendix A of the main paper supplies that
    derivation. No benchmark ranking, universal runtime advantage or trained-model
    result is curated.'
  dimensions:
  - name: concept-kind
    value: architecture
    definition: A reusable directed probabilistic architecture, with stochastic-variable
      and deterministic-computation roles stated explicitly; not a trained instance
      or benchmark outcome.
    evidence_ids:
    - deepautoregressivenetwork-source-0
  - name: aio-assessment
    value: related_match
    definition: All 32 semantic label/scoped-synonym hits, thirteen exact AIO CLASS
      nodes including full annotations and outgoing edges, and six complete native
      neighboring records were read. SBN and original NADE each receive broad_match
      to BayesianNetwork, with the AIO target broader than their binary logistic or
      shared-neural-factor families. DARN receives related_match to BayesianNetwork
      for its directed generative component, since the whole identity includes a separate
      recognition network. BoltzmannMachineNetwork and RestrictedBoltzmannMachine
      are undirected model boundaries, not equivalent identities. DeepBeliefNetwork,
      AutoEncoderNetwork and VariationalAutoEncoder do not establish the particular
      identities, and their pretrained/latent conventions are not forced onto NADE.
      ProbabilisticGraphicalModel is task-level context; ProbabilisticHiddenLayer
      has a category-probability definition; SigmoidFunction is a component. AutoregressiveLanguageModel
      and AutoregressiveMovingAverage have language and time-series scope, respectively.
      DeepFeedForwardNetwork does not identify the factorization and latent distinctions.
      CausalGraphicalModel is not inferred from a DAG alone. Neighboring records provide
      boundaries, not fresh whole-record approvals.
    evidence_ids:
    - mapping
- assessment_id: sbn-boundaries
  area: consistency
  topic: Locally normalized directed factors, binary encodings and conditional inference
  outcome: supported
  target_ids:
  - AIMech:SigmoidBeliefNetwork
  evidence_ids:
  - sigmoidbeliefnetwork-source-0
  - finite-conventions
  summary: Retain the binary logistic conditional model family.
  details: 'The inspected Neal definitions specify ordered directed factors. Zero/one
    to signed encoding halves non-bias weights and shifts biases by half the original
    weight sum; the finite example checks this equality. A parent-to-child forward
    factor is not a Gibbs full conditional or posterior: the binary example has prior1/2
    and posterior3/4 after observing the child. Exact joint ancestral generation and
    local normalization do not eliminate the hidden-state sum or guarantee Gibbs mixing.
    The native family is narrower than AIO BayesianNetwork, so broad_match direction
    is justified.'
- assessment_id: nade-boundaries
  area: consistency
  topic: Deterministic prefix features, normalized density and printed pseudocode
  outcome: supported
  target_ids:
  - AIMech:NeuralAutoregressiveDistributionEstimator
  evidence_ids:
  - neuralautoregressivedistributionestimator-source-0
  - finite-conventions
  summary: Retain original binary NADE separately from sigmoid-linear and latent models.
  details: 'The source’s neural hidden activations parameterize visible-prefix conditionals
    deterministically. The probability product is normalized independently of its
    RBM inspiration. Shared input weights and hidden biases permit prefix reuse, while
    output weights may be untied. The printed zero initialization and plus between
    Bernoulli factors in Algorithm1 conflict with the chain-rule density, and the
    preceding accumulator difference has an index conflict. These are disclosed and
    not transcribed as executable mechanism: the curator two-bit model has total mass1,
    zero-initialized accumulation yields0, and a plus-factor interpretation starting
    at1 yields mass9. The correct prefix update uses the just-observed variable i.
    No author-code defect or empirical failure is inferred.'
- assessment_id: darn-boundaries
  area: consistency
  topic: Autoregressive stochastic layers, recognition inference and approximate gradients
  outcome: supported
  target_ids:
  - AIMech:DeepAutoregressiveNetwork
  evidence_ids:
  - deepautoregressivenetwork-source-0
  - finite-conventions
  summary: Retain DARN as a distinct paired architecture.
  details: Ordered within-layer generative dependencies preserve acyclicity and permit
    exact model draws. The separately parameterized recognition model does not automatically
    equal the posterior. Optional deterministic layers and factorized recognition
    or visible variants are within the paper’s family; its zero-latent limiting case
    is explicitly identified without equating the main family to NADE. The variational
    free-energy identity remains exact under normalized distributions, while AppendixA’s
    isolated-unit endpoint-derivative estimator can be biased. At Bernoulli probability1/4
    a quadratic has expected and exact logit gradient3/16; a cubic has expected9/32
    versus exact3/16. The printed recognition-product dimension is interpreted over
    hidden units consistently with Eq8. The supplemental image page supplies no gradient
    proof.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Broad directed-model mappings and a paired-architecture component relation
  outcome: supported
  target_ids:
  - AIMech:SigmoidBeliefNetwork
  - AIMech:NeuralAutoregressiveDistributionEstimator
  - AIMech:DeepAutoregressiveNetwork
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain SBN and NADE broad mappings and DARN related mapping.
  details: All 32 semantic label/scoped-synonym hits, thirteen exact AIO CLASS nodes
    including full annotations and outgoing edges, and six complete native neighboring
    records were read. SBN and original NADE each receive broad_match to BayesianNetwork,
    with the AIO target broader than their binary logistic or shared-neural-factor
    families. DARN receives related_match to BayesianNetwork for its directed generative
    component, since the whole identity includes a separate recognition network. BoltzmannMachineNetwork
    and RestrictedBoltzmannMachine are undirected model boundaries, not equivalent
    identities. DeepBeliefNetwork, AutoEncoderNetwork and VariationalAutoEncoder do
    not establish the particular identities, and their pretrained/latent conventions
    are not forced onto NADE. ProbabilisticGraphicalModel is task-level context; ProbabilisticHiddenLayer
    has a category-probability definition; SigmoidFunction is a component. AutoregressiveLanguageModel
    and AutoregressiveMovingAverage have language and time-series scope, respectively.
    DeepFeedForwardNetwork does not identify the factorization and latent distinctions.
    CausalGraphicalModel is not inferred from a DAG alone. Neighboring records provide
    boundaries, not fresh whole-record approvals.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:SigmoidBeliefNetwork
  - AIMech:NeuralAutoregressiveDistributionEstimator
  - AIMech:DeepAutoregressiveNetwork
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - source-host
  - finite-conventions
  - sigmoidbeliefnetwork-source-0
  - neuralautoregressivedistributionestimator-source-0
  - deepautoregressivenetwork-source-0
  rationale: SBN is the binary logistic directed factor family. Original NADE uses
    deterministic shared neural prefix features to parameterize a fully visible distribution.
    DARN combines stochastic autoregressive hidden layers and a distinct recognition
    network. Shared directed factors or sigmoid components do not establish identity
    equivalence.
limitations:
- Author self-review only; all records remain DRAFT.
- The Neal file is a third-party university course scan; publisher-file byte equivalence
  was not established. NADE and DARN use the declared publisher PDFs.
- Only declared pages were read; full implementations, general convergence proofs
  and empirical comparisons were not audited.
- Printed formula discrepancies are qualified explicitly. Finite calculations illustrate
  boundaries and do not prove general performance or implementation behavior.
- There are 190 pending inspection leads plus unresolved dispositions; discovery remains
  active.
links: []
tags:
- native-concepts
- autoregressive-belief
- self-review
- discovery-ongoing
```
