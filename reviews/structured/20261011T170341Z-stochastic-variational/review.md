# Scientific self-review of stochastic activations and BBVI

- Review: 20261011T170341Z-stochastic-variational
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T17:00:36Z
- Finished UTC: 2026-10-11T17:03:41Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the noisy rectifier, STS unit and original BBVI as distinct DRAFT concepts. The records bound logistic identities, smooth-only gradients and estimated control variates, and exclude the unresolved hierarchical extension. No actionable curation finding remains in the declared scope.

## Scope And Provenance

All fields of an explicit heterogeneous batch: two stochastic activations and one variational-inference algorithm.

Selection: Exact three IDs in the saved ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 0822320fe83afa0de2a91dc6c4fba8488d7caa11.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:NoisyRectifier | data/curated/NoisyRectifier.yaml | maintained | Noisy rectifier |
| AIMech:StochasticTimesSmoothUnit | data/curated/StochasticTimesSmoothUnit.yaml | maintained | Stochastic-times-smooth unit |
| AIMech:BlackBoxVariationalInference | data/curated/BlackBoxVariationalInference.yaml | maintained | Black box variational inference |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:NoisyRectifier, AIMech:StochasticTimesSmoothUnit, AIMech:BlackBoxVariationalInference | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 95.67s (0:01:35)<br>Checked 442 record(s); 0 failed.<br>Checked 340 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 94 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 91,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:NoisyRectifier, AIMech:StochasticTimesSmoothUnit, AIMech:BlackBoxVariationalInference | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:NoisyRectifier, AIMech:StochasticTimesSmoothUnit, AIMech:BlackBoxVariationalInference | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:NoisyRectifier, AIMech:StochasticTimesSmoothUnit, AIMech:BlackBoxVariationalInference | Command exited0 with no output. |
| Stochastic-activation and control-variate boundary calculations | passed | True | AIMech:NoisyRectifier, AIMech:StochasticTimesSmoothUnit, AIMech:BlackBoxVariationalInference | {"noisy_rectifier": {"activation_probability": "1/2", "numerical_mean": 0.6931471805597955, "exact_mean": "log(2)", "noiseless_output": 0, "omitted_tail_upper_bound": 9.357622968840175e-14}, "stochastic_times_smooth": {"mean": "1/4", "second_moment": "1/8", "square_of_mean": "1/16", "expected_fixed_gate_derivative": "3/32", "derivative_of_mean": "3/16"}, "bbvi": {"true_elbo_gradient": "1", "fixed_optimal_coefficient": "-1/2", "fixed_coefficient_mean": "1", "hypothetical_two_sample_reuse_mean": "0", "corrected_polynomial": "-z1*z2", "source_behavior_claim": false}, "status": "PASS"} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:NoisyRectifier.

This record covers the noisy rectifier described in Bengio et al. Section 2.1, with standard logistic noise as the analytically characterized special case. It is a stochastic activation, distinct from deterministic ReLU or softplus, input-only corruption, weight-noise dense layers and multiplicative dropout. The paper credits earlier rectifier work; this record does not claim that the 2013 paper invented noisy rectification. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 337 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 22 and 22 lines respectively. All 15 unique matched line contents were inspected in full: the preceding gradient-estimator records, their cited Bengio source, saved source-reading scopes, reviews and open discovery leads, not existing candidate records. Exact checkout counts and differences are retained in the ledger. Thirteen exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and six full native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood.

For a preactivation a, sample zero-mean additive noise z and output max(0,a+z). With the source’s standard logistic density sigma(z)*(1-sigma(z)), the probability of a positive output is sigma(a), and the conditional mean output is log(1+exp(a)). These identities are specific to that logistic-noise choice, not arbitrary zero-mean noise. Holding a sampled noise value fixed, the derivative with respect to a is 1 on the positive side and 0 on the negative side, with a nondifferentiable boundary at a+z=0. Noise can occasionally turn an otherwise inactive unit on or an active unit off. The source also suggests adjusting a unit bias when a moving activity rate falls below a chosen target; that heuristic is additional to the forward activation rule. Limits: Equality of the logistic-noise mean to softplus does not make a sampled noisy rectifier a deterministic softplus unit. Passing the mean through a nonlinear downstream loss does not generally preserve the expected loss. The standard logistic activation and mean formulas change with the noise distribution or scale. Gaussian noise is mentioned as a practical alternative, but it does not inherit the displayed logistic identities. Occasional activation permits gradient flow for some samples but does not guarantee that inactive units recover promptly, that every derivative-through-expectation interchange is valid, or that conditional computation saves wall-clock time. No empirical speed, accuracy or sparsity advantage is asserted. The original authors’ implementation and later noisy-activation variants were not audited.

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:StochasticTimesSmoothUnit.

This record covers Bengio et al.’s Section 2.2 STS construction and its smooth-amplitude training path. The Bernoulli gate and nonzero amplitude are both sqrt(p); it is neither an ordinary Bernoulli(p) output nor fixed-rate dropout. The source’s Figure 2 uses the reversed wording Smooth Times Stoch. for this experimental unit family. The identity is not the generic straight-through estimator or stochastic depth. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 337 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 22 and 22 lines respectively. All 15 unique matched line contents were inspected in full: the preceding gradient-estimator records, their cited Bengio source, saved source-reading scopes, reviews and open discovery leads, not existing candidate records. Exact checkout counts and differences are retained in the ledger. Thirteen exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and six full native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Compute p=sigmoid(a), draw b in {0,1} with P(b=1)=sqrt(p), and return h=b*sqrt(p). Conditional on a, E[h]=p, P(h&gt;0)=sqrt(p), and the nonzero output is sqrt(p). Backpropagation through the smooth multiplier can hold the discrete gate fixed. This path does not include the derivative of the gate’s probability law: as a curator consequence of the displayed rule, its expected derivative for the loss h is p-prime/2, while d E[h]/d a=p-prime. Proposition 2 gives an asymptotic relationship E[f(h)]=f(p)+o(sqrt(p)) as p tends to zero for the stated differentiable-function setting; it does not state equality at a finite activation probability. Limits: The smooth-amplitude backward path is not generally an unbiased gradient of the expected stochastic loss. An estimator for changes in the gate probability would require an additional treatment. Matching the mean to p does not preserve a nonlinear downstream function. For example, at p=1/4 the second moment is 1/8 while the squared mean is 1/16; this is a curator calculation from the source’s distribution. The asymptotic small-p statement is not a uniform finite-p error bound, a guarantee about optimization, or a theorem that the stochastic network equals a deterministic sigmoid network. The conditional-computation motivation does not establish a universal speed or accuracy improvement. No author implementation or trained model was run.

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:BlackBoxVariationalInference.

This record covers Ranganath, Gerrish and Blei’s original BBVI Algorithms 1–2 and their score-function estimator, mean-field local signals and control variates. It is not every black-box inference method, a pathwise reparameterization estimator, a model architecture or an amortized recognition network such as NVIL. The hierarchical data-subsampling extension is outside the validated mechanism scope here. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 337 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 22 and 22 lines respectively. All 15 unique matched line contents were inspected in full: the preceding gradient-estimator records, their cited Bengio source, saved source-reading scopes, reviews and open discovery leads, not existing candidate records. Exact checkout counts and differences are retained in the ledger. Thirteen exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and six full native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood.

For fixed observed x and joint model p(x,z), choose a variational family q(z;lambda), sample z from q, and maximize L(lambda)=E_q[log p(x,z)-log q(z;lambda)] by stochastic ascent. Under the normalized-score and differentiation-under-expectation conditions, the raw gradient is E_q[grad_lambda log q(z;lambda)*(log p(x,z)-log q(z;lambda))], estimated by a Monte Carlo average. The mean-field version factors q into q_i(z_i;lambda_i) and uses for each factor the model log terms that depend on z_i together with -log q_i; unrelated terms cancel in expectation under the stated factorization. For parameter coordinate d in factor i, let h_d be the score and f_d be that score times the local log signal. A fixed control-variate coefficient gives f_d-a_d*h_d because E[h_d]=0; the population variance-minimizing coefficient is Cov(f_d,h_d)/Var(h_d) when these quantities exist and Var(h_d)&gt;0. The source estimates coefficients from samples and averages corrected contributions before a stochastic-ascent update. Its fixed-coefficient expectation identity does not by itself justify arbitrary reuse of samples to estimate both the coefficient and corrected gradient. Limits: Black box still requires sampling from and evaluating the variational distribution, score derivatives with respect to its parameters, and evaluation of the model log joint at sampled latent states. The method does not require differentiation through a discrete latent sample, but support and integrability conditions remain necessary. Raw unbiasedness requires the regularity assumptions behind differentiation under the expectation and zero expected score. A model normalization constant independent of lambda cancels from this gradient; a parameter-dependent term cannot be discarded on that basis. A coefficient fixed independently of the gradient samples preserves expectation when the relevant moments exist. A coefficient estimated from those same samples can correlate with the sample score and introduce bias. The paper reports separate sample counts for coefficient estimation and gradient calculation, but the inspected description does not establish an exact sampling-independence convention; no implementation behavior is asserted. Population-optimal control-variate scaling and conditional-expectation variance reduction do not guarantee that estimated coefficients or every additional removal of zero-mean terms reduces finite-sample variance. Zero or poorly estimated score variance requires handling beyond division by the displayed ratio. The practical step schedule and change-in-parameters stopping rule do not establish global optimality or exact posterior recovery. Mean-field factorization can limit the approximation. The printed hierarchical subsampling formulas need a separate weighting audit and are not curated as a verified extension here. No benchmark result, author-code run, general convergence proof or posterior-quality certification is included.

### Noise distribution, positive-part output and expectation

consistency: supported. Targets: AIMech:NoisyRectifier.

Retain the noisy rectifier separately from deterministic activation functions.

The primary definition adds noise before rectification. Proposition 1 gives sigmoid activity probability and softplus mean only for standard logistic noise. Numerical survival-integral quadrature at zero agrees with log(2); this is not the noiseless ReLU output zero. A matching mean does not equate distributions or nonlinear downstream objectives. The optional activity-bias adjustment and motivation for computation savings do not become mandatory forward steps or empirical guarantees.

### Gate probability, nonzero amplitude and smooth-only derivative

consistency: supported. Targets: AIMech:StochasticTimesSmoothUnit.

Retain the STS construction as its own stochastic activation.

Both gate success probability and nonzero amplitude are sqrt(p), where p is sigmoid(a). Exact enumeration at p=1/4 gives mean 1/4 and second moment 1/8, whereas the squared mean is 1/16. Holding the sampled gate fixed yields expected derivative 3/32, while the derivative of the mean is 3/16. This curator calculation qualifies the smooth-only training path and does not claim an author-code defect. Proposition 2 is an asymptotic expectation statement, not a finite-p equality or a general gradient-unbiasedness theorem.

### Score-function gradients, local terms and estimated control variates

consistency: supported. Targets: AIMech:BlackBoxVariationalInference.

Retain original BBVI Algorithms 1–2 with explicit regularity and sampling limits.

The raw ELBO estimator and zero-score identity need normalization and differentiation conditions. Mean-field local signals preserve the gradient by cancellation of unrelated terms. Fixed control-variate coefficients preserve the expectation, and population-optimal scaling requires finite moments and positive score variance. In a standard-normal variational example, a coefficient estimated using the same two samples transforms the corrected average to -z1*z2, with expectation zero rather than true gradient one. This hypothetical example does not establish the authors’ sampling convention; the paper reports different counts for coefficient and gradient estimates, and no implementation was run. Additional constant-term removal is not asserted to reduce variance universally. The hierarchical-subsampling displays remain an unresolved source-formula audit outside the curated mechanism.

### Activation components and probabilistic-model context

grounding: supported. Targets: AIMech:NoisyRectifier, AIMech:StochasticTimesSmoothUnit, AIMech:BlackBoxVariationalInference.

Retain three related mappings without equivalence or is-a assertions.

Thirteen exact pinned CLASS nodes with definitions, scoped synonyms, comments and outgoing edges, and six full native neighbors were read. NoisyRectifier maps related to ReLUFunction as its essential positive-part component, STS maps related to SigmoidFunction as its specified probability component, and BBVI maps related to ProbabilisticGraphicalModel for its factorization and Markov-blanket context. These are not equivalence or subclass assertions. ReLULayer, SoftplusFunction, GaussianNoiseLayer, NoisyInputLayer, NoiseDenseLayer, DropoutLayer, GaussianDropoutLayer, MathematicalFunction, BayesianNetwork and VariationalAutoEncoder were considered as boundaries; a shared noise word, matching expectation or possible application does not establish identity. Prior native mappings are contextual, not newly approved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:NoisyRectifier, AIMech:StochasticTimesSmoothUnit, AIMech:BlackBoxVariationalInference. Additive-noise rectification and the STS Bernoulli-times-amplitude construction have different output laws. BBVI is an inference procedure using score-function estimates, not either activation or the entire generic score-estimator family. Related components and shared stochastic-gradient context do not establish equivalence.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T170015Z-stochastic-variational.json | supports | Compared all 442 pinned AIO labels/scoped synonyms and 337 preceding native IDs/names/aliases; no normalized identity match. Both ignored- and hidden-inclusive full-checkout scans returned 22 lines with identical sorted contents. All 15 unique matched line contents were read in full: the preceding gradient-estimator records, their cited Bengio source, saved source-reading scopes, reviews and open discovery leads. Thirteen exact AIO nodes and six complete native neighbors were inspected; absence is bounded to this snapshot and semantic neighborhood. |
| mapping | sources/aio/aio.json; Thirteen exact CLASS nodes with scoped synonyms/comments/outgoing edges in source_analysis.aio_mapping_inspection | supports | Thirteen exact pinned CLASS nodes with definitions, scoped synonyms, comments and outgoing edges, and six full native neighbors were read. NoisyRectifier maps related to ReLUFunction as its essential positive-part component, STS maps related to SigmoidFunction as its specified probability component, and BBVI maps related to ProbabilisticGraphicalModel for its factorization and Markov-blanket context. These are not equivalence or subclass assertions. ReLULayer, SoftplusFunction, GaussianNoiseLayer, NoisyInputLayer, NoiseDenseLayer, DropoutLayer, GaussianDropoutLayer, MathematicalFunction, BayesianNetwork and VariationalAutoEncoder were considered as boundaries; a shared noise word, matching expectation or possible application does not establish identity. Prior native mappings are contextual, not newly approved. |
| neighbors | research/discovery/20261011T170015Z-stochastic-variational.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Full GumbelSoftmaxRelaxation, StraightThroughEstimator, StraightThroughGumbelSoftmax, NeuralVariationalInferenceAndLearning, REINFORCE and StochasticDepth records distinguish continuous relaxations, surrogate backward rules, amortized variational learning, reward-weighted score updates and residual-block bypass. Their prior mappings are contextual, not newly approved. |
| finite-conventions | research/discovery/stochastic-variational-boundaries.py; Logistic-mean numerical quadrature, exact STS moments and derivatives, and symbolic two-sample BBVI control-variate calculation | supports | Numerical logistic-mean quadrature, exact STS moment/derivative calculations, and symbolic BBVI coefficient-reuse calculations expose distinct scope boundaries. They are curator work, not author-code tests, general convergence claims or benchmarks. |
| noisyrectifier-source-0 | https://arxiv.org/pdf/1308.3432v1; Section 2.1, noisy-rectifier definition and Proposition 1 with proof, PDF/printed pp.3–4 | supports | Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation. arXiv:1308.3432v1, August 15, 2013; 12-page author paper. PDF and printed page numbers agree. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| stochastictimessmoothunit-source-0 | https://arxiv.org/pdf/1308.3432v1; Section 2.2, Equation (2), Proposition 2 and proof, PDF/printed p.5; Section 5 and Figure 2 naming context, p.8 | supports | Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation. arXiv:1308.3432v1, August 15, 2013; 12-page author paper. PDF and printed page numbers agree. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| blackboxvariationalinference-source-0 | https://proceedings.mlr.press/v33/ranganath14.pdf; Sections 2–3, Equations (1)–(9), Algorithms 1–2, PDF pp.2–5 / proceedings pp.815–818; Section 5 sample-count context, PDF p.6 / p.819 | supports | Black Box Variational Inference. AISTATS 2014, PMLR 33:814–822; nine-page publisher PDF. Printed proceedings page = PDF page + 813. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| blackboxvariationalinference-source-1 | https://proceedings.mlr.press/v33/ranganath14-supp.pdf; Appendix: The Gradient of the ELBO, Equations (A.1)–(A.3), and Supplement: Derivation of the Rao-Blackwellized Gradient, Equations (S.4)–(S.6), PDF pp.1–2 | supports | Black Box Variational Inference (Extra Materials). Three-page publisher supplement linked from the PMLR article. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |

## Limits And Additional Notes

- Adversarial author self-review only; all records remain DRAFT.
- Only the declared PDF pages were read. Bengio uses the exact previously downloaded v1; the BBVI main paper and supplement have separate publisher-file hashes.
- The hierarchical BBVI extension remains outside validated scope; no author-code defect or implementation sampling convention is asserted.
- Numerical quadrature and exact finite or symbolic examples establish stated boundaries, not general optimization outcomes or benchmark rankings.
- There are 186 pending inspection leads plus unresolved dispositions; discovery remains active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T170341Z-stochastic-variational
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of stochastic activations and BBVI
started_at: '2026-10-11T17:00:36Z'
finished_at: '2026-10-11T17:03:41Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially checked every new field against
    the declared primary PDF pages, thirteen exact AIO nodes, six full native neighbors
    and original curator calculations. Noise-law dependence, distribution-versus-mean
    distinctions, gate-probability derivatives, local-score conditions and control-variate
    sample dependence were examined. This is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the noisy rectifier, STS unit and original BBVI as distinct DRAFT
  concepts. The records bound logistic identities, smooth-only gradients and estimated
  control variates, and exclude the unresolved hierarchical extension. No actionable
  curation finding remains in the declared scope.
source:
  git_revision: 0822320fe83afa0de2a91dc6c4fba8488d7caa11
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/DropoutLayer.yaml
    sha256: f1d1f2ad44ecf177e8c5d16bf1fb72388712d25f499583feab23e5fb65a71e24
    role: context
  - path: data/aio/GaussianDropoutLayer.yaml
    sha256: d709e2b88e01052b2dbb1a1e3213a79b428c3c1de4acb2e55c875528250d58d2
    role: context
  - path: data/aio/GaussianNoiseLayer.yaml
    sha256: 1d6c203daf9e9a5a450a85a7d7bf6e55bb9bffbeea7ceffcc1a8aefbd9629452
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/NoiseDenseLayer.yaml
    sha256: fc4cefe872103228071e21e0567f2bb2d4a8a597c66dc58cee9cb8d568684a67
    role: context
  - path: data/aio/NoisyInputLayer.yaml
    sha256: b0d135e5d29a740691d9bc52033bdd97bd852e8d75e7eabfcc500762251920c1
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ReLUFunction.yaml
    sha256: 815a5255ec7e87bb8bb123ea7121d024d46450ccfab164985e2014108b53d28c
    role: context
  - path: data/aio/ReLULayer.yaml
    sha256: 6b8105e5a7bc1223c32fd31ecb4adbe47f57feba3430824244e23d7c485541d5
    role: context
  - path: data/aio/SigmoidFunction.yaml
    sha256: e112ec27a5b6fc9de17cc2d3354b836968b6693c6902cf004b71f05a0aedb193
    role: context
  - path: data/aio/SoftplusFunction.yaml
    sha256: 0cd3aaf4f90ca587293a2c56ae854b1aa823070a26a20046cc9157384ca71bff
    role: context
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/curated/BlackBoxVariationalInference.yaml
    sha256: 8237d3233ae06163b8fab5b4fa047ffc938e275bc1e3ede883348e06c2b266a8
    role: target
  - path: data/curated/GumbelSoftmaxRelaxation.yaml
    sha256: 330a1911c594beade01b4f613034a41aef5a4783cf41667a468415b4b6ad6420
    role: context
  - path: data/curated/NeuralVariationalInferenceAndLearning.yaml
    sha256: 0d24a286ed64974478f452907c018d9618348ef4900808ea97b80036b1dfb06c
    role: context
  - path: data/curated/NoisyRectifier.yaml
    sha256: fb65c10663835e61629f05d55866248e00aed07a28cc00eb444499d0f4936f28
    role: target
  - path: data/curated/REINFORCE.yaml
    sha256: 2f579286d88446d0b18e4988873a6b274d3ad24be48e6f58b716edaf9d68f514
    role: context
  - path: data/curated/StochasticDepth.yaml
    sha256: 32a0f2baac7ebf1c7f08c81f54710df74e56044bbf36e0df1ac7a05f4d925852
    role: context
  - path: data/curated/StochasticTimesSmoothUnit.yaml
    sha256: 38c3663fcbec176d1b3d2838c222a0651fe4e2a61c063dddb12fe598360e8703
    role: target
  - path: data/curated/StraightThroughEstimator.yaml
    sha256: 9476ce3dca57298172b11bd84d6132d00c9e5f8bd084d3202d10f159024dfe7a
    role: context
  - path: data/curated/StraightThroughGumbelSoftmax.yaml
    sha256: b774a8ba97d2627a6a4d7467780ad40690c68db504419d2118e43f8cecf79a46
    role: context
  - path: research/discovery/20261011T170015Z-stochastic-variational.json
    sha256: 9c01da466abd493666b2f9a40c4920dde1003ef75fa1d6a07a38c1b58ccb626f
    role: context
  - path: research/discovery/stochastic-variational-boundaries.py
    sha256: e34324d422fe41b1a38aa848c2dee08b07313e78d1d7c7a634486bf5c8c33788
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
- target_id: AIMech:NoisyRectifier
  path: data/curated/NoisyRectifier.yaml
  label: Noisy rectifier
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NoisyRectifier.yaml
    role: maintained
- target_id: AIMech:StochasticTimesSmoothUnit
  path: data/curated/StochasticTimesSmoothUnit.yaml
  label: Stochastic-times-smooth unit
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StochasticTimesSmoothUnit.yaml
    role: maintained
- target_id: AIMech:BlackBoxVariationalInference
  path: data/curated/BlackBoxVariationalInference.yaml
  label: Black box variational inference
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BlackBoxVariationalInference.yaml
    role: maintained
scope:
  description: 'All fields of an explicit heterogeneous batch: two stochastic activations
    and one variational-inference algorithm.'
  selection: Exact three IDs in the saved ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:NoisyRectifier
  - AIMech:StochasticTimesSmoothUnit
  - AIMech:BlackBoxVariationalInference
  exclusions:
  - target: Uninspected frontier leads and complete executable implementations
    reason: The batch does not exhaust gradient estimation or variational learning.
      Wake-sleep, pathwise estimators, the BBVI hierarchical-subsampling formula audit
      and other frontier cohorts remain open.
  - target: Prior corpus, unread pages and empirical performance
    reason: Older records are boundary context. Only declared source sections/images
      and finite curator examples support this review.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:NoisyRectifier
  - AIMech:StochasticTimesSmoothUnit
  - AIMech:BlackBoxVariationalInference
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 95.67s (0:01:35)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 340 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 94 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 91,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:NoisyRectifier
  - AIMech:StochasticTimesSmoothUnit
  - AIMech:BlackBoxVariationalInference
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
  - AIMech:NoisyRectifier
  - AIMech:StochasticTimesSmoothUnit
  - AIMech:BlackBoxVariationalInference
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
  - AIMech:NoisyRectifier
  - AIMech:StochasticTimesSmoothUnit
  - AIMech:BlackBoxVariationalInference
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited0 with no output.
- check_id: finite-arithmetic
  name: Stochastic-activation and control-variate boundary calculations
  command: python3 research/discovery/stochastic-variational-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:NoisyRectifier
  - AIMech:StochasticTimesSmoothUnit
  - AIMech:BlackBoxVariationalInference
  exit_code: 0
  expected_exit_code: 0
  summary: '{"noisy_rectifier": {"activation_probability": "1/2", "numerical_mean":
    0.6931471805597955, "exact_mean": "log(2)", "noiseless_output": 0, "omitted_tail_upper_bound":
    9.357622968840175e-14}, "stochastic_times_smooth": {"mean": "1/4", "second_moment":
    "1/8", "square_of_mean": "1/16", "expected_fixed_gate_derivative": "3/32", "derivative_of_mean":
    "3/16"}, "bbvi": {"true_elbo_gradient": "1", "fixed_optimal_coefficient": "-1/2",
    "fixed_coefficient_mean": "1", "hypothetical_two_sample_reuse_mean": "0", "corrected_polynomial":
    "-z1*z2", "source_behavior_claim": false}, "status": "PASS"}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T170015Z-stochastic-variational.json
  accessed_at: '2026-10-11T17:00:36Z'
  support: supports
  summary: 'Compared all 442 pinned AIO labels/scoped synonyms and 337 preceding native
    IDs/names/aliases; no normalized identity match. Both ignored- and hidden-inclusive
    full-checkout scans returned 22 lines with identical sorted contents. All 15 unique
    matched line contents were read in full: the preceding gradient-estimator records,
    their cited Bengio source, saved source-reading scopes, reviews and open discovery
    leads. Thirteen exact AIO nodes and six complete native neighbors were inspected;
    absence is bounded to this snapshot and semantic neighborhood.'
  search_scope: 'All 442 pinned AIO labels/scoped synonyms and 337 preceding maintained
    IDs/names/aliases; both full checkouts including ignored and hidden files. All
    15 unique matched line contents were read in full: preceding method/source citations,
    saved reading scopes and discovery leads. Both scans returned 22 lines with identical
    sorted contents. Exact counts, paths and differences remain in the ledger.'
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Thirteen exact CLASS nodes with scoped synonyms/comments/outgoing edges
    in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T17:00:36Z'
  support: supports
  summary: Thirteen exact pinned CLASS nodes with definitions, scoped synonyms, comments
    and outgoing edges, and six full native neighbors were read. NoisyRectifier maps
    related to ReLUFunction as its essential positive-part component, STS maps related
    to SigmoidFunction as its specified probability component, and BBVI maps related
    to ProbabilisticGraphicalModel for its factorization and Markov-blanket context.
    These are not equivalence or subclass assertions. ReLULayer, SoftplusFunction,
    GaussianNoiseLayer, NoisyInputLayer, NoiseDenseLayer, DropoutLayer, GaussianDropoutLayer,
    MathematicalFunction, BayesianNetwork and VariationalAutoEncoder were considered
    as boundaries; a shared noise word, matching expectation or possible application
    does not establish identity. Prior native mappings are contextual, not newly approved.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T170015Z-stochastic-variational.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T17:00:36Z'
  support: supports
  summary: Full GumbelSoftmaxRelaxation, StraightThroughEstimator, StraightThroughGumbelSoftmax,
    NeuralVariationalInferenceAndLearning, REINFORCE and StochasticDepth records distinguish
    continuous relaxations, surrogate backward rules, amortized variational learning,
    reward-weighted score updates and residual-block bypass. Their prior mappings
    are contextual, not newly approved.
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/stochastic-variational-boundaries.py
  locator: Logistic-mean numerical quadrature, exact STS moments and derivatives,
    and symbolic two-sample BBVI control-variate calculation
  accessed_at: '2026-10-11T17:00:36Z'
  snapshot_sha256: e34324d422fe41b1a38aa848c2dee08b07313e78d1d7c7a634486bf5c8c33788
  support: supports
  summary: Numerical logistic-mean quadrature, exact STS moment/derivative calculations,
    and symbolic BBVI coefficient-reuse calculations expose distinct scope boundaries.
    They are curator work, not author-code tests, general convergence claims or benchmarks.
- evidence_id: noisyrectifier-source-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1308.3432v1
  locator: Section 2.1, noisy-rectifier definition and Proposition 1 with proof, PDF/printed
    pp.3–4
  accessed_at: '2026-10-11T16:33:05Z'
  snapshot_sha256: 509eb5e5294d6a5cb730a239022a6bd3589ed54cd24c1d7482c1edf6237ed863
  support: supports
  summary: Estimating or Propagating Gradients Through Stochastic Neurons for Conditional
    Computation. arXiv:1308.3432v1, August 15, 2013; 12-page author paper. PDF and
    printed page numbers agree. Actual paper and HTML reading scopes are declared
    in source_analysis; extraction, rendering and a full-text access label do not
    establish that every page was read.
- evidence_id: stochastictimessmoothunit-source-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1308.3432v1
  locator: Section 2.2, Equation (2), Proposition 2 and proof, PDF/printed p.5; Section
    5 and Figure 2 naming context, p.8
  accessed_at: '2026-10-11T16:33:05Z'
  snapshot_sha256: 509eb5e5294d6a5cb730a239022a6bd3589ed54cd24c1d7482c1edf6237ed863
  support: supports
  summary: Estimating or Propagating Gradients Through Stochastic Neurons for Conditional
    Computation. arXiv:1308.3432v1, August 15, 2013; 12-page author paper. PDF and
    printed page numbers agree. Actual paper and HTML reading scopes are declared
    in source_analysis; extraction, rendering and a full-text access label do not
    establish that every page was read.
- evidence_id: blackboxvariationalinference-source-0
  kind: primary_source
  reference: https://proceedings.mlr.press/v33/ranganath14.pdf
  locator: Sections 2–3, Equations (1)–(9), Algorithms 1–2, PDF pp.2–5 / proceedings
    pp.815–818; Section 5 sample-count context, PDF p.6 / p.819
  accessed_at: '2026-10-11T16:51:18Z'
  snapshot_sha256: 8f481e202eb64f5dca87f8e7db4a3ac75f53bad2286542583c5c212eaa00a610
  support: supports
  summary: Black Box Variational Inference. AISTATS 2014, PMLR 33:814–822; nine-page
    publisher PDF. Printed proceedings page = PDF page + 813. Actual paper and HTML
    reading scopes are declared in source_analysis; extraction, rendering and a full-text
    access label do not establish that every page was read.
- evidence_id: blackboxvariationalinference-source-1
  kind: primary_source
  reference: https://proceedings.mlr.press/v33/ranganath14-supp.pdf
  locator: 'Appendix: The Gradient of the ELBO, Equations (A.1)–(A.3), and Supplement:
    Derivation of the Rao-Blackwellized Gradient, Equations (S.4)–(S.6), PDF pp.1–2'
  accessed_at: '2026-10-11T16:51:20Z'
  snapshot_sha256: f61d07ae80b6f1c86445886cfb1d6bb67fd9c5ad47c5a61566e355d2894b9839
  support: supports
  summary: Black Box Variational Inference (Extra Materials). Three-page publisher
    supplement linked from the PMLR article. Actual paper and HTML reading scopes
    are declared in source_analysis; extraction, rendering and a full-text access
    label do not establish that every page was read.
assessments:
- assessment_id: noisyrectifier
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:NoisyRectifier
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - noisyrectifier-source-0
  summary: 'This record covers the noisy rectifier described in Bengio et al. Section
    2.1, with standard logistic noise as the analytically characterized special case.
    It is a stochastic activation, distinct from deterministic ReLU or softplus, input-only
    corruption, weight-noise dense layers and multiplicative dropout. The paper credits
    earlier rectifier work; this record does not claim that the 2013 paper invented
    noisy rectification. No normalized identity match was found across all 442 pinned
    AIO labels/scoped synonyms and 337 preceding native IDs/names/aliases. Full-checkout
    fixed-string searches included ignored and hidden files in worktree and main,
    returning 22 and 22 lines respectively. All 15 unique matched line contents were
    inspected in full: the preceding gradient-estimator records, their cited Bengio
    source, saved source-reading scopes, reviews and open discovery leads, not existing
    candidate records. Exact checkout counts and differences are retained in the ledger.
    Thirteen exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges
    and six full native neighboring records were inspected. Absence is bounded to
    this snapshot and semantic neighborhood.'
  details: 'For a preactivation a, sample zero-mean additive noise z and output max(0,a+z).
    With the source’s standard logistic density sigma(z)*(1-sigma(z)), the probability
    of a positive output is sigma(a), and the conditional mean output is log(1+exp(a)).
    These identities are specific to that logistic-noise choice, not arbitrary zero-mean
    noise. Holding a sampled noise value fixed, the derivative with respect to a is
    1 on the positive side and 0 on the negative side, with a nondifferentiable boundary
    at a+z=0. Noise can occasionally turn an otherwise inactive unit on or an active
    unit off. The source also suggests adjusting a unit bias when a moving activity
    rate falls below a chosen target; that heuristic is additional to the forward
    activation rule. Limits: Equality of the logistic-noise mean to softplus does
    not make a sampled noisy rectifier a deterministic softplus unit. Passing the
    mean through a nonlinear downstream loss does not generally preserve the expected
    loss. The standard logistic activation and mean formulas change with the noise
    distribution or scale. Gaussian noise is mentioned as a practical alternative,
    but it does not inherit the displayed logistic identities. Occasional activation
    permits gradient flow for some samples but does not guarantee that inactive units
    recover promptly, that every derivative-through-expectation interchange is valid,
    or that conditional computation saves wall-clock time. No empirical speed, accuracy
    or sparsity advantage is asserted. The original authors’ implementation and later
    noisy-activation variants were not audited.'
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: A reusable stochastic-activation construction or variational-inference
      procedure, not a trained model instance or benchmark outcome.
    evidence_ids:
    - noisyrectifier-source-0
  - name: aio-assessment
    value: related_match
    definition: Thirteen exact pinned CLASS nodes with definitions, scoped synonyms,
      comments and outgoing edges, and six full native neighbors were read. NoisyRectifier
      maps related to ReLUFunction as its essential positive-part component, STS maps
      related to SigmoidFunction as its specified probability component, and BBVI
      maps related to ProbabilisticGraphicalModel for its factorization and Markov-blanket
      context. These are not equivalence or subclass assertions. ReLULayer, SoftplusFunction,
      GaussianNoiseLayer, NoisyInputLayer, NoiseDenseLayer, DropoutLayer, GaussianDropoutLayer,
      MathematicalFunction, BayesianNetwork and VariationalAutoEncoder were considered
      as boundaries; a shared noise word, matching expectation or possible application
      does not establish identity. Prior native mappings are contextual, not newly
      approved.
    evidence_ids:
    - mapping
- assessment_id: stochastictimessmoothunit
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:StochasticTimesSmoothUnit
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - stochastictimessmoothunit-source-0
  summary: 'This record covers Bengio et al.’s Section 2.2 STS construction and its
    smooth-amplitude training path. The Bernoulli gate and nonzero amplitude are both
    sqrt(p); it is neither an ordinary Bernoulli(p) output nor fixed-rate dropout.
    The source’s Figure 2 uses the reversed wording Smooth Times Stoch. for this experimental
    unit family. The identity is not the generic straight-through estimator or stochastic
    depth. No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 337 preceding native IDs/names/aliases. Full-checkout fixed-string
    searches included ignored and hidden files in worktree and main, returning 22
    and 22 lines respectively. All 15 unique matched line contents were inspected
    in full: the preceding gradient-estimator records, their cited Bengio source,
    saved source-reading scopes, reviews and open discovery leads, not existing candidate
    records. Exact checkout counts and differences are retained in the ledger. Thirteen
    exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and six
    full native neighboring records were inspected. Absence is bounded to this snapshot
    and semantic neighborhood.'
  details: 'Compute p=sigmoid(a), draw b in {0,1} with P(b=1)=sqrt(p), and return
    h=b*sqrt(p). Conditional on a, E[h]=p, P(h>0)=sqrt(p), and the nonzero output
    is sqrt(p). Backpropagation through the smooth multiplier can hold the discrete
    gate fixed. This path does not include the derivative of the gate’s probability
    law: as a curator consequence of the displayed rule, its expected derivative for
    the loss h is p-prime/2, while d E[h]/d a=p-prime. Proposition 2 gives an asymptotic
    relationship E[f(h)]=f(p)+o(sqrt(p)) as p tends to zero for the stated differentiable-function
    setting; it does not state equality at a finite activation probability. Limits:
    The smooth-amplitude backward path is not generally an unbiased gradient of the
    expected stochastic loss. An estimator for changes in the gate probability would
    require an additional treatment. Matching the mean to p does not preserve a nonlinear
    downstream function. For example, at p=1/4 the second moment is 1/8 while the
    squared mean is 1/16; this is a curator calculation from the source’s distribution.
    The asymptotic small-p statement is not a uniform finite-p error bound, a guarantee
    about optimization, or a theorem that the stochastic network equals a deterministic
    sigmoid network. The conditional-computation motivation does not establish a universal
    speed or accuracy improvement. No author implementation or trained model was run.'
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: A reusable stochastic-activation construction or variational-inference
      procedure, not a trained model instance or benchmark outcome.
    evidence_ids:
    - stochastictimessmoothunit-source-0
  - name: aio-assessment
    value: related_match
    definition: Thirteen exact pinned CLASS nodes with definitions, scoped synonyms,
      comments and outgoing edges, and six full native neighbors were read. NoisyRectifier
      maps related to ReLUFunction as its essential positive-part component, STS maps
      related to SigmoidFunction as its specified probability component, and BBVI
      maps related to ProbabilisticGraphicalModel for its factorization and Markov-blanket
      context. These are not equivalence or subclass assertions. ReLULayer, SoftplusFunction,
      GaussianNoiseLayer, NoisyInputLayer, NoiseDenseLayer, DropoutLayer, GaussianDropoutLayer,
      MathematicalFunction, BayesianNetwork and VariationalAutoEncoder were considered
      as boundaries; a shared noise word, matching expectation or possible application
      does not establish identity. Prior native mappings are contextual, not newly
      approved.
    evidence_ids:
    - mapping
- assessment_id: blackboxvariationalinference
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:BlackBoxVariationalInference
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - blackboxvariationalinference-source-0
  - blackboxvariationalinference-source-1
  summary: 'This record covers Ranganath, Gerrish and Blei’s original BBVI Algorithms
    1–2 and their score-function estimator, mean-field local signals and control variates.
    It is not every black-box inference method, a pathwise reparameterization estimator,
    a model architecture or an amortized recognition network such as NVIL. The hierarchical
    data-subsampling extension is outside the validated mechanism scope here. No normalized
    identity match was found across all 442 pinned AIO labels/scoped synonyms and
    337 preceding native IDs/names/aliases. Full-checkout fixed-string searches included
    ignored and hidden files in worktree and main, returning 22 and 22 lines respectively.
    All 15 unique matched line contents were inspected in full: the preceding gradient-estimator
    records, their cited Bengio source, saved source-reading scopes, reviews and open
    discovery leads, not existing candidate records. Exact checkout counts and differences
    are retained in the ledger. Thirteen exact AIO CLASS nodes with scoped synonyms/comments
    and outgoing edges and six full native neighboring records were inspected. Absence
    is bounded to this snapshot and semantic neighborhood.'
  details: 'For fixed observed x and joint model p(x,z), choose a variational family
    q(z;lambda), sample z from q, and maximize L(lambda)=E_q[log p(x,z)-log q(z;lambda)]
    by stochastic ascent. Under the normalized-score and differentiation-under-expectation
    conditions, the raw gradient is E_q[grad_lambda log q(z;lambda)*(log p(x,z)-log
    q(z;lambda))], estimated by a Monte Carlo average. The mean-field version factors
    q into q_i(z_i;lambda_i) and uses for each factor the model log terms that depend
    on z_i together with -log q_i; unrelated terms cancel in expectation under the
    stated factorization. For parameter coordinate d in factor i, let h_d be the score
    and f_d be that score times the local log signal. A fixed control-variate coefficient
    gives f_d-a_d*h_d because E[h_d]=0; the population variance-minimizing coefficient
    is Cov(f_d,h_d)/Var(h_d) when these quantities exist and Var(h_d)>0. The source
    estimates coefficients from samples and averages corrected contributions before
    a stochastic-ascent update. Its fixed-coefficient expectation identity does not
    by itself justify arbitrary reuse of samples to estimate both the coefficient
    and corrected gradient. Limits: Black box still requires sampling from and evaluating
    the variational distribution, score derivatives with respect to its parameters,
    and evaluation of the model log joint at sampled latent states. The method does
    not require differentiation through a discrete latent sample, but support and
    integrability conditions remain necessary. Raw unbiasedness requires the regularity
    assumptions behind differentiation under the expectation and zero expected score.
    A model normalization constant independent of lambda cancels from this gradient;
    a parameter-dependent term cannot be discarded on that basis. A coefficient fixed
    independently of the gradient samples preserves expectation when the relevant
    moments exist. A coefficient estimated from those same samples can correlate with
    the sample score and introduce bias. The paper reports separate sample counts
    for coefficient estimation and gradient calculation, but the inspected description
    does not establish an exact sampling-independence convention; no implementation
    behavior is asserted. Population-optimal control-variate scaling and conditional-expectation
    variance reduction do not guarantee that estimated coefficients or every additional
    removal of zero-mean terms reduces finite-sample variance. Zero or poorly estimated
    score variance requires handling beyond division by the displayed ratio. The practical
    step schedule and change-in-parameters stopping rule do not establish global optimality
    or exact posterior recovery. Mean-field factorization can limit the approximation.
    The printed hierarchical subsampling formulas need a separate weighting audit
    and are not curated as a verified extension here. No benchmark result, author-code
    run, general convergence proof or posterior-quality certification is included.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable stochastic-activation construction or variational-inference
      procedure, not a trained model instance or benchmark outcome.
    evidence_ids:
    - blackboxvariationalinference-source-0
    - blackboxvariationalinference-source-1
  - name: aio-assessment
    value: related_match
    definition: Thirteen exact pinned CLASS nodes with definitions, scoped synonyms,
      comments and outgoing edges, and six full native neighbors were read. NoisyRectifier
      maps related to ReLUFunction as its essential positive-part component, STS maps
      related to SigmoidFunction as its specified probability component, and BBVI
      maps related to ProbabilisticGraphicalModel for its factorization and Markov-blanket
      context. These are not equivalence or subclass assertions. ReLULayer, SoftplusFunction,
      GaussianNoiseLayer, NoisyInputLayer, NoiseDenseLayer, DropoutLayer, GaussianDropoutLayer,
      MathematicalFunction, BayesianNetwork and VariationalAutoEncoder were considered
      as boundaries; a shared noise word, matching expectation or possible application
      does not establish identity. Prior native mappings are contextual, not newly
      approved.
    evidence_ids:
    - mapping
- assessment_id: rectifier-boundaries
  area: consistency
  topic: Noise distribution, positive-part output and expectation
  outcome: supported
  target_ids:
  - AIMech:NoisyRectifier
  evidence_ids:
  - noisyrectifier-source-0
  - finite-conventions
  summary: Retain the noisy rectifier separately from deterministic activation functions.
  details: The primary definition adds noise before rectification. Proposition 1 gives
    sigmoid activity probability and softplus mean only for standard logistic noise.
    Numerical survival-integral quadrature at zero agrees with log(2); this is not
    the noiseless ReLU output zero. A matching mean does not equate distributions
    or nonlinear downstream objectives. The optional activity-bias adjustment and
    motivation for computation savings do not become mandatory forward steps or empirical
    guarantees.
- assessment_id: sts-boundaries
  area: consistency
  topic: Gate probability, nonzero amplitude and smooth-only derivative
  outcome: supported
  target_ids:
  - AIMech:StochasticTimesSmoothUnit
  evidence_ids:
  - stochastictimessmoothunit-source-0
  - finite-conventions
  summary: Retain the STS construction as its own stochastic activation.
  details: Both gate success probability and nonzero amplitude are sqrt(p), where
    p is sigmoid(a). Exact enumeration at p=1/4 gives mean 1/4 and second moment 1/8,
    whereas the squared mean is 1/16. Holding the sampled gate fixed yields expected
    derivative 3/32, while the derivative of the mean is 3/16. This curator calculation
    qualifies the smooth-only training path and does not claim an author-code defect.
    Proposition 2 is an asymptotic expectation statement, not a finite-p equality
    or a general gradient-unbiasedness theorem.
- assessment_id: bbvi-boundaries
  area: consistency
  topic: Score-function gradients, local terms and estimated control variates
  outcome: supported
  target_ids:
  - AIMech:BlackBoxVariationalInference
  evidence_ids:
  - blackboxvariationalinference-source-0
  - blackboxvariationalinference-source-1
  - finite-conventions
  summary: Retain original BBVI Algorithms 1–2 with explicit regularity and sampling
    limits.
  details: The raw ELBO estimator and zero-score identity need normalization and differentiation
    conditions. Mean-field local signals preserve the gradient by cancellation of
    unrelated terms. Fixed control-variate coefficients preserve the expectation,
    and population-optimal scaling requires finite moments and positive score variance.
    In a standard-normal variational example, a coefficient estimated using the same
    two samples transforms the corrected average to -z1*z2, with expectation zero
    rather than true gradient one. This hypothetical example does not establish the
    authors’ sampling convention; the paper reports different counts for coefficient
    and gradient estimates, and no implementation was run. Additional constant-term
    removal is not asserted to reduce variance universally. The hierarchical-subsampling
    displays remain an unresolved source-formula audit outside the curated mechanism.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Activation components and probabilistic-model context
  outcome: supported
  target_ids:
  - AIMech:NoisyRectifier
  - AIMech:StochasticTimesSmoothUnit
  - AIMech:BlackBoxVariationalInference
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain three related mappings without equivalence or is-a assertions.
  details: Thirteen exact pinned CLASS nodes with definitions, scoped synonyms, comments
    and outgoing edges, and six full native neighbors were read. NoisyRectifier maps
    related to ReLUFunction as its essential positive-part component, STS maps related
    to SigmoidFunction as its specified probability component, and BBVI maps related
    to ProbabilisticGraphicalModel for its factorization and Markov-blanket context.
    These are not equivalence or subclass assertions. ReLULayer, SoftplusFunction,
    GaussianNoiseLayer, NoisyInputLayer, NoiseDenseLayer, DropoutLayer, GaussianDropoutLayer,
    MathematicalFunction, BayesianNetwork and VariationalAutoEncoder were considered
    as boundaries; a shared noise word, matching expectation or possible application
    does not establish identity. Prior native mappings are contextual, not newly approved.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:NoisyRectifier
  - AIMech:StochasticTimesSmoothUnit
  - AIMech:BlackBoxVariationalInference
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - noisyrectifier-source-0
  - stochastictimessmoothunit-source-0
  - blackboxvariationalinference-source-0
  - blackboxvariationalinference-source-1
  rationale: Additive-noise rectification and the STS Bernoulli-times-amplitude construction
    have different output laws. BBVI is an inference procedure using score-function
    estimates, not either activation or the entire generic score-estimator family.
    Related components and shared stochastic-gradient context do not establish equivalence.
limitations:
- Adversarial author self-review only; all records remain DRAFT.
- Only the declared PDF pages were read. Bengio uses the exact previously downloaded
  v1; the BBVI main paper and supplement have separate publisher-file hashes.
- The hierarchical BBVI extension remains outside validated scope; no author-code
  defect or implementation sampling convention is asserted.
- Numerical quadrature and exact finite or symbolic examples establish stated boundaries,
  not general optimization outcomes or benchmark rankings.
- There are 186 pending inspection leads plus unresolved dispositions; discovery remains
  active.
links: []
tags:
- native-concepts
- stochastic-variational
- self-review
- discovery-ongoing
```
