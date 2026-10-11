# Scientific self-review of TRBM, RTRBM and autoregressive CRBM

- Review: 20261011T184500Z-temporal-rbm
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T18:41:40Z
- Finished UTC: 2026-10-11T18:45:00Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain three DRAFT temporal neural architectures with distinct state and inference scopes. Source gradient and smoothing qualifications are explicit. No actionable curation finding remains within the declared scope.

## Scope And Provenance

All fields of three explicitly selected temporal RBM architectures.

Selection: Three exact maintained IDs in the discovery ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 64bf16408a2dda2e7d59a1536ec7fda0d90cab8f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:TemporalRestrictedBoltzmannMachine | data/curated/TemporalRestrictedBoltzmannMachine.yaml | maintained | Temporal restricted Boltzmann machine |
| AIMech:RecurrentTemporalRestrictedBoltzmannMachine | data/curated/RecurrentTemporalRestrictedBoltzmannMachine.yaml | maintained | Recurrent temporal restricted Boltzmann machine |
| AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine | data/curated/AutoregressiveConditionalRestrictedBoltzmannMachine.yaml | maintained | Autoregressive conditional restricted Boltzmann machine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:TemporalRestrictedBoltzmannMachine, AIMech:RecurrentTemporalRestrictedBoltzmannMachine, AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 86.59s (0:01:26)<br>Checked 442 record(s); 0 failed.<br>Checked 364 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 102 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 99,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:TemporalRestrictedBoltzmannMachine, AIMech:RecurrentTemporalRestrictedBoltzmannMachine, AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:TemporalRestrictedBoltzmannMachine, AIMech:RecurrentTemporalRestrictedBoltzmannMachine, AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:TemporalRestrictedBoltzmannMachine, AIMech:RecurrentTemporalRestrictedBoltzmannMachine, AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine | Command exited 0 with no output. |
| Temporal RBM mathematical boundary calculations | passed | True | AIMech:TemporalRestrictedBoltzmannMachine, AIMech:RecurrentTemporalRestrictedBoltzmannMachine, AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine | {"trbm": {"normalized_joint": 1.0, "filtered_h1": 0.6224593312018546, "smoothed_h1": 0.6345317477570805, "exact_next": 0.6422333146149961, "plug_mean_next": 0.643875827815082}, "rtrbm": {"log_probability": -1.9488424494893266, "gradient": [0.004070725210531423, -0.0012469383887315985, -0.06495525260501475, -0.03301346798390119], "direct_recurrent_term": -0.04118360278527837, "indirect_recurrent_term": 0.008170134801377182, "length_two_exact_recurrent_gradient": -0.07468599656772924, "length_two_recurrence_only_gradient": 0.0, "finite_differences_pass": true}, "crbm": {"log_density": -1.4784500342117175, "hidden_prior": 0.5174928576663897, "hidden_posterior": 0.31647910626368436, "visible_mean": 0.8639942861331118, "visible_variance": 1.1598041599556246, "gradient": [-1.0639942861331118, -0.2010137514027054, -0.7101618933357241, -0.7447960002931782, -0.14070962598189377], "missing_frame_filtered_mean": 0.0, "missing_frame_smoothed_mean": 0.8, "finite_differences_pass": true}} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, source provenance and AIO mapping

evidence: supported. Targets: AIMech:TemporalRestrictedBoltzmannMachine.

This record covers the original single-layer temporal RBM construction of Sutskever and Hinton, with its finite lag window and omitted-edge special cases. The full architecture has visible-to-visible, visible-to-hidden and hidden-to-hidden history connections. It is distinct from temporal FRBM’s factored categorical-word construction, RTRBM’s deterministic recurrent state, and the observed-history-only autoregressive CRBM. Multilayer stacking is an extension rather than part of this single-layer identity; a filtering algorithm does not define the latent probabilistic model. All 442 pinned AIO labels/scoped synonyms and 361 preceding native IDs/names/aliases were compared, with no normalized identity match. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, returning 24 lines each. All 18 unique matched contents were read: temporal FRBM source references, model contrasts, a discovery lead and saved review context, rather than existing candidate records. All 44 semantic label/synonym hits and 21 exact AIO nodes were inspected, alongside corresponding generated records and four complete native neighbors. Previously read contextual files were checked for byte identity. Absence is bounded to this snapshot and inspected neighborhood.

For binary vectors v_t and h_t, set the visible bias a_t=a+sum_k A_k^T v_(t-k) and hidden bias b_t=b+sum_k B_k^T h_(t-k)+sum_k C_k^T v_(t-k). Define p(v_t,h_t&#124;history)=exp(v_t^T C_0 h_t+a_t^T v_t+b_t^T h_t)/Z_t(history), and multiply these normalized factors over time using shared parameters and the source’s learned initial contributions for unavailable earlier states. Conditional on observed current and previous visibles and known previous hidden states, the current hidden posterior factorizes with probabilities sigmoid(C_0^T v_t+b_t). Unknown previous hidden states generally require marginalization; the proposed online filter instead substitutes their inferred probability vectors in b_t. Learning treats these approximate filtered states as context and uses per-step contrastive-divergence updates. The original paper distinguishes this approximation from smoothing with future observations and from an exact likelihood gradient. Limitations: The conditional partition depends on history, including previous hidden states. It is not one sequence-independent global constant, and exact posterior Gibbs updates can require ratios of such partitions. A factorial posterior given known latent history does not imply factorial or exact filtering after uncertain history is marginalized. Mean substitution through nonlinear normalized factors is generally approximate, and future observations can revise earlier hidden-state posteriors. The paper explicitly notes that changing its parameter-dependent approximate posterior can reduce the variational bound. Finite CD, mean visible reconstructions and ignoring future evidence provide no monotonic bound or likelihood guarantee. TRBM-HH denotes the variant with hidden-to-hidden links omitted, not one retaining only those links. For fully observed visible sequences its hidden posterior is factorial; missing observations and multilayer compositions change that inference problem. The displayed construction has no past-hidden-to-current-visible links; a footnote mentions those as a possible extension. Gaussian visible units, deeper compositions and different lag structures require their own stated assumptions. No empirical ranking, long-memory guarantee or author-code behavior is certified.

### Identity, definition, mechanism, limitations, source provenance and AIO mapping

evidence: supported. Targets: AIMech:RecurrentTemporalRestrictedBoltzmannMachine.

This is Sutskever, Hinton and Taylor’s 2008 RTRBM, with a real-valued recurrent state and separate binary within-step RBM hidden variables. Replacing a sampled TRBM hidden state by a deterministic probability vector changes the generative model; exact inference in RTRBM is not exact inference in the original stochastic TRBM. The recurrent update and conditional RBM share weights in this architecture. The real-valued state must not be conflated with the binary hidden variables integrated out of each output RBM. All 442 pinned AIO labels/scoped synonyms and 361 preceding native IDs/names/aliases were compared, with no normalized identity match. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, returning 24 lines each. All 18 unique matched contents were read: temporal FRBM source references, model contrasts, a discovery lead and saved review context, rather than existing candidate records. All 44 semantic label/synonym hits and 21 exact AIO nodes were inspected, alongside corresponding generated records and four complete native neighbors. Previously read contextual files were checked for byte identity. Absence is bounded to this snapshot and inspected neighborhood.

Use column vectors, visible-by-hidden weights W and recurrent hidden-by-hidden weights U. Given r_(t-1), let the current binary RBM have joint mass proportional to exp(v_t^T W z_t+a^T v_t+(b+U r_(t-1))^T z_t), with binary z_t marginalized for the visible distribution. After observing or sampling v_t, set r_t=sigmoid(W^T v_t+b+U r_(t-1)); the first step uses the specified initial bias contribution. This update is deterministic by definition, so a fully observed visible sequence fixes the recurrent trajectory exactly and later observations cannot alter its already determined states. The visible-sequence log likelihood is the sum of the conditional RBM log marginals. Differentiate that objective through the recurrence and through each RBM’s direct parameter dependence. In particular, a recurrent weight affects the current output distribution through its hidden bias as well as later recurrent states. Backpropagation through time propagates these dependencies, while the paper approximates conditional RBM model expectations with contrastive divergence. A Gaussian-visible version replaces the binary visible base measure with a quadratic Gaussian term. Limitations: Exact deterministic-state inference requires the visible sequence to be observed. Missing observations require marginalizing uncertainty in visible values and induced recurrent states; the exact-inference statement does not automatically extend to that problem. Within-step binary hidden variables are stochastic even though the recurrent summary is deterministic. Exact state reconstruction does not make RBM partition functions, equilibrium sampling or finite-CD gradients exact or generally tractable. The printed Equation (12) local-score index differs from its surrounding next-step prose. Equation (13) displays a recurrence contribution but omits the direct current-RBM dependence through its dynamic hidden bias; a complete objective derivative must include it. The curated description follows the normalized generative definition and chain rule, checked by original finite differences, rather than treating Equations (12)–(14) as a verified implementation. No author-code defect or official erratum is asserted. A finite recurrent vector permits temporal dependence but does not guarantee successful learning of arbitrarily long dependencies. The source’s sample-quality comparisons do not establish universal superiority or exact likelihood learning. The source shares parameters between recurrence and output RBMs. A separate recurrent network that independently controls RBM parameters is a distinct neighboring construction; this record does not equate every RNN–RBM hybrid to RTRBM.

### Identity, definition, mechanism, limitations, source provenance and AIO mapping

evidence: supported. Targets: AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine.

This record is scoped to Taylor, Hinton and Roweis’s autoregressive CRBM construction for vector sequences, particularly its Gaussian-visible, binary-hidden formulation. The general label conditional RBM and acronym CRBM are not claimed as exclusive aliases because other conditional RBMs condition on arbitrary inputs or use different parameterizations. This is the observed-history specialization related to TRBM-HH; RTRBM and full TRBM also propagate hidden history. A stacked multilevel construction is not silently included in the single-layer record. All 442 pinned AIO labels/scoped synonyms and 361 preceding native IDs/names/aliases were compared, with no normalized identity match. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, returning 24 lines each. All 18 unique matched contents were read: temporal FRBM source references, model contrasts, a discovery lead and saved review context, rather than existing candidate records. All 44 semantic label/synonym hits and 21 exact AIO nodes were inspected, alongside corresponding generated records and four complete native neighbors. Previously read contextual files were checked for byte identity. Absence is bounded to this snapshot and inspected neighborhood.

Condition on preceding visible frames and compute dynamic biases d_t=c+sum_k A_k^T v_(t-k) and e_t=b+sum_k D_k^T v_(t-k), allowing different lag windows for the two sums. In the source’s unit-variance Gaussian formulation, E(v_t,h_t&#124;history)=one-half times &#124;&#124;v_t-d_t&#124;&#124; squared minus e_t^T h_t minus v_t^T W h_t. Thus hidden probabilities are sigmoid(e_t+W^T v_t), and visible coordinates given h_t are independent unit-variance Gaussians with mean d_t+W h_t. The partition is conditional on the fixed history. For fully observed frames the hidden posterior factorizes, and likelihood gradients contrast data and conditional-model statistics; the paper approximates them by CD while holding earlier frames fixed. Its implementation description samples positive-phase binary hidden states, uses hidden probabilities for negative-phase statistics, and uses mean visible reconstructions in place of Gaussian draws. Generation starts from supplied initial frames and repeatedly samples the current conditional RBM; the original conditional training does not model the first lag-window frames. Limitations: The single-layer visible conditional depends on the fixed observed lag window. Nonlinear hidden features do not introduce an unbounded latent temporal memory path; deeper stacked models are separate compositions. Sections 2–2.1 explicitly give exact factorial hidden inference for fully observed frames. Section 2.2’s broad statement about omitted smoothing must not override that graph-specific result: future factors contain no earlier hidden state once the visible sequence is fixed. Missing visible data and multilevel models can require smoothing; the reported online missing-data procedure is approximate. Replacing Gaussian visible samples by conditional means removes conditional sampling variance and is not exact Gibbs sampling from the stated Gaussian model. Finite CD is not an exact likelihood gradient or a convergence guarantee. The general energy in Equation (1) includes visible standard deviations and scaled interactions; the displayed mechanism deliberately adopts the source’s sigma_i=1 convention. Rescaling arbitrary variances without transforming weights changes the distribution. A conditional RBM is richer than a linear autoregression, although removing the hidden interactions leaves an autoregressive Gaussian special case. Initial-frame distributions, missing-data posterior integration, phase disambiguation and transition coverage need separate modeling assumptions. No benchmark ranking or author-code certification is asserted.

### Normalized conditional chain and latent-history inference

consistency: supported. Targets: AIMech:TemporalRestrictedBoltzmannMachine.

Retain single-layer TRBM with explicit filtering and smoothing limits.

The exact binary two-step joint sums to one. A hidden-state posterior of 0.6224593312 given the first observed frame changes to 0.6345317478 after the next frame. Mixing normalized conditionals gives next-frame probability 0.6422333146; substituting the filtered hidden mean gives 0.6438758278. The differences demonstrate that known-history factorial conditionals do not make uncertain-history filtering or smoothing exact. Dynamic visible and hidden biases, history-dependent partitions, learned initialization contributions and the no-HH variant are separately scoped. The source explicitly qualifies CD and parameter-dependent approximate posterior changes.

### Deterministic model state and complete likelihood differentiation

consistency: supported. Targets: AIMech:RecurrentTemporalRestrictedBoltzmannMachine.

Retain RTRBM as a distinct generative model, with printed-gradient qualifications.

The source makes the recurrent state deterministic and retains separate stochastic within-step hidden variables. The original finite calculation normalizes all length-three visible sequences and checks all four scalar parameter gradients by central differences. The recurrent-weight gradient is -0.0330134680, composed of direct conditional contribution -0.0411836028 and recurrence contribution 0.0081701348. In a two-step example the recurrence-only term is zero but the exact derivative is -0.0746859966. This exposes the missing direct term if printed Equation (13) is used alone; Equation (12) also has an index disagreement with adjacent prose. The record relies on the normalized objective and chain rule, without asserting an official erratum or author-code defect. Exact observed-state inference does not remove RBM partitions or CD approximation.

### Observed-history conditional model and missing-data distinction

consistency: supported. Targets: AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine.

Retain the autoregressive CRBM with a bounded alias and inference scope.

The scalar Gaussian example agrees with its explicit two-Gaussian mixture and all five parameter gradients pass finite differences. Its hidden posterior is 0.3164791063, visible mean 0.8639942861 and variance 1.1598041600. Future factors cancel from the hidden posterior when the intervening visible values are observed. In contrast, a zero-hidden-coupling linear-Gaussian example changes a missing-frame mean from 0 under filtering to 0.8 under smoothing. These checks clarify the paper’s broad no-smoothing statement against its exact fully observed single-layer graph. Mean Gaussian reconstructions remove conditional variance and are not exact Gibbs samples. The generic label CRBM remains outside the exclusive alias list.

### Mapping scope and local identity

grounding: supported. Targets: AIMech:TemporalRestrictedBoltzmannMachine, AIMech:RecurrentTemporalRestrictedBoltzmannMachine, AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine.

Retain three architectures with explicit broad neural and related RBM mappings.

All 44 semantic hits and 21 exact annotated AIO CLASS nodes with outgoing edges were read. Fourteen corresponding generated YAML files were previously fully read and verified byte-identical; seven were read in this batch. Four complete native neighbors were inspected: static and temporal FRBM (previous full reading with byte verification), sigmoid belief network and hidden Markov model (read this batch). TRBM and autoregressive CRBM broadly map to ArtificialNeuralNetwork; RTRBM broadly maps to RecurrentNeuralNetwork through its deterministic recurrence and RBM-output objective. All three relate to RestrictedBoltzmannMachine through their within-step conditional construction. BoltzmannMachineNetwork has a symmetric whole-network scope that does not cover directed temporal links unchanged. RecurrentLayer, HiddenLayer and ProbabilisticHiddenLayer are components, not whole sequence architectures. BayesianNetwork does not identify the mixed directed/undirected parameterization, and ProbabilisticGraphicalModel is task-scoped in this pin. MarkovChain does not identify the neural parameterization; marginal visible histories and hidden/state augmentation require explicit boundaries. DeepBeliefNetwork and DeepNeuralNetwork are not implied by a single hidden layer unrolled in time. AutoregressiveLanguageModel, CausalLLM, ControllableLLM, EnergyBasedLLM and ImplicitLanguageModel require language-specific scope. VectorAutoregression is linear; AutoregressiveDistributedLag does not identify a conditional energy model. GaussianNoiseLayer is training-time regularization, not a Gaussian visible conditional, and TemporalBias is a selection/sampling bias, not a dynamic neural bias. Previous native models provide boundaries without reassessing their own scientific approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:TemporalRestrictedBoltzmannMachine, AIMech:RecurrentTemporalRestrictedBoltzmannMachine, AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine. TRBM propagates stochastic hidden history, RTRBM defines a deterministic recurrent state tied to conditional RBM probabilities, and autoregressive CRBM conditions on a finite window of observed frames without hidden recurrence. Their shared RBM component does not equate whole-model identity, inference or learning. Generic conditional RBM remains broader than the autoregressive record’s alias scope.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T184102Z-temporal-rbm.json | supports | All 442 pinned AIO labels/scoped synonyms and 361 preceding native IDs/names/aliases were compared, with no normalized identity match. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, returning 24 lines each. All 18 unique matched contents were read: temporal FRBM source references, model contrasts, a discovery lead and saved review context, rather than existing candidate records. All 44 semantic label/synonym hits and 21 exact AIO nodes were inspected, alongside corresponding generated records and four complete native neighbors. Previously read contextual files were checked for byte identity. Absence is bounded to this snapshot and inspected neighborhood. |
| mapping | sources/aio/aio.json; Twenty-one exact CLASS nodes with full annotations and outgoing edges in source_analysis.aio_mapping_inspection; corresponding generated records | supports | All 44 semantic hits and 21 exact annotated AIO CLASS nodes with outgoing edges were read. Fourteen corresponding generated YAML files were previously fully read and verified byte-identical; seven were read in this batch. Four complete native neighbors were inspected: static and temporal FRBM (previous full reading with byte verification), sigmoid belief network and hidden Markov model (read this batch). TRBM and autoregressive CRBM broadly map to ArtificialNeuralNetwork; RTRBM broadly maps to RecurrentNeuralNetwork through its deterministic recurrence and RBM-output objective. All three relate to RestrictedBoltzmannMachine through their within-step conditional construction. BoltzmannMachineNetwork has a symmetric whole-network scope that does not cover directed temporal links unchanged. RecurrentLayer, HiddenLayer and ProbabilisticHiddenLayer are components, not whole sequence architectures. BayesianNetwork does not identify the mixed directed/undirected parameterization, and ProbabilisticGraphicalModel is task-scoped in this pin. MarkovChain does not identify the neural parameterization; marginal visible histories and hidden/state augmentation require explicit boundaries. DeepBeliefNetwork and DeepNeuralNetwork are not implied by a single hidden layer unrolled in time. AutoregressiveLanguageModel, CausalLLM, ControllableLLM, EnergyBasedLLM and ImplicitLanguageModel require language-specific scope. VectorAutoregression is linear; AutoregressiveDistributedLag does not identify a conditional energy model. GaussianNoiseLayer is training-time regularization, not a Gaussian visible conditional, and TemporalBias is a selection/sampling bias, not a dynamic neural bias. Previous native models provide boundaries without reassessing their own scientific approval. |
| neighbors | research/discovery/20261011T184102Z-temporal-rbm.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Four complete native records provide boundaries: static and temporal FRBM (previous full reading with byte verification), sigmoid belief network and hidden Markov model (fully read in this batch). They distinguish categorical-word factorization, stochastic temporal language modeling, pure directed logistic conditionals and state-dependent emissions, without renewed scientific approval. |
| finite-conventions | research/discovery/temporal-rbm-boundaries.py; TRBM smoothing and uncertain-history mixtures; exact RTRBM objective gradients and direct dynamic-bias dependence; Gaussian CRBM mixture, gradients and observed/missing-data inference | supports | Original finite calculations normalize a two-step stochastic TRBM, exhibit posterior smoothing and distinguish exact history mixtures from plug-in means. A binary RTRBM calculation differentiates the exact normalized sequence objective, checking every parameter against central finite differences and isolating the direct dynamic-bias contribution to recurrent weights. A two-step example has zero recurrence-only contribution but a nonzero exact recurrent-weight derivative. A scalar Gaussian CRBM is checked against its explicit Gaussian mixture and finite-difference gradients; fully observed hidden inference is invariant to the future factor, while a missing-visible Gaussian subcase requires smoothing. Mean visible reconstructions remove conditional sampling variance. These are curator calculations, not author-code or benchmark evidence. |
| temporalrestrictedboltzmannmachine-source-0 | https://proceedings.mlr.press/v2/sutskever07a/sutskever07a.pdf; Sections 2.1–2.4, Figure 2 and Equations (10)–(18), PDF pp.2–5; omitted-edge naming and exact no-HH special case, Section 3, p.5; multilayer qualifications, Sections 4.2–5, pp.7–8 | supports | Learning Multilevel Distributed Representations for High-Dimensional Sequences. AISTATS 2007 / PMLR 2:548–555 proceedings PDF, eight pages. No printed page numbers appear on the inspected pages; use PDF-page locators. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |
| temporalrestrictedboltzmannmachine-source-1 | https://proceedings.neurips.cc/paper_files/paper/2008/file/9ad6aaed513b73148b7d49f70afcfb32-Paper.pdf; Section 3, Equations (4)–(5) and discussion of posterior Gibbs updates and conditional partition ratios, PDF p.3 | supports | The Recurrent Temporal Restricted Boltzmann Machine. Eight-page proceedings PDF, Advances in Neural Information Processing Systems 21, conference NIPS 2008; author bibliography lists the volume publication in 2009. Use PDF-page locators. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |
| recurrenttemporalrestrictedboltzmannmachine-source-0 | https://proceedings.neurips.cc/paper_files/paper/2008/file/9ad6aaed513b73148b7d49f70afcfb32-Paper.pdf; Sections 2–4.3, Equations (1)–(14), Figure 2 and Algorithms 2–4, PDF pp.2–6; Equation (12) indexing and Equation (13) direct-parameter contribution qualified against Equations (6), (8)–(11); limitations and conclusion, pp.6–8 | supports | The Recurrent Temporal Restricted Boltzmann Machine. Eight-page proceedings PDF, Advances in Neural Information Processing Systems 21, conference NIPS 2008; author bibliography lists the volume publication in 2009. Use PDF-page locators. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |
| autoregressiveconditionalrestrictedboltzmannmachine-source-0 | https://papers.neurips.cc/paper/3078-modeling-human-motion-using-binary-latent-variables.pdf; Sections 2–2.2, Equations (1)–(7) and Figure 2, PDF pp.2–4; initialized generation and online missing-data procedure, Sections 4 and 4.4, pp.5–6; higher-level extension and scope limits, Sections 5–6, pp.7–8 | supports | Modeling Human Motion Using Binary Latent Variables. Eight-page proceedings PDF, Advances in Neural Information Processing Systems 19, conference NIPS 2006, volume published in 2007. The PDF has no visible printed page numbers; use PDF-page locators. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |
| autoregressiveconditionalrestrictedboltzmannmachine-source-1 | https://proceedings.mlr.press/v2/sutskever07a/sutskever07a.pdf; Section 3, TRBM-HH omitted-edge definition and exact-inference qualification, PDF p.5; Section 4.2, fully observed no-HH posterior qualification, p.7 | supports | Learning Multilevel Distributed Representations for High-Dimensional Sequences. AISTATS 2007 / PMLR 2:548–555 proceedings PDF, eight pages. No printed page numbers appear on the inspected pages; use PDF-page locators. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |

## Limits And Additional Notes

- Adversarial author self-review only; every target remains DRAFT.
- All eight PDF pages of Sutskever2007, RTRBM2008 and Taylor2006 were visually read. Other versions, code and frontier papers were not fully inspected in this review.
- Sutskever2007 retains its verified earlier retrieval timestamp. PDF-page locators and exact hashes distinguish unpaginated files and conference/proceedings publication years.
- Finite calculations check stated examples and mathematical boundaries, not author software, benchmark performance, global convergence or every parameter value.
- 200 pending inspection leads plus unresolved dispositions remain; discovery is active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T184500Z-temporal-rbm
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of TRBM, RTRBM and autoregressive CRBM
started_at: '2026-10-11T18:41:40Z'
finished_at: '2026-10-11T18:45:00Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially checked all target fields
    against three complete primary PDFs, 21 exact AIO CLASS nodes and corresponding
    generated records, four complete native neighbors and original finite calculations.
    Conditional partitions, latent filtering/smoothing, deterministic recurrence,
    direct parameter gradients, Gaussian conventions and mapping direction were examined.
    This is author self-review.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain three DRAFT temporal neural architectures with distinct state and
  inference scopes. Source gradient and smoothing qualifications are explicit. No
  actionable curation finding remains within the declared scope.
source:
  git_revision: 64bf16408a2dda2e7d59a1536ec7fda0d90cab8f
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/AutoregressiveDistributedLag.yaml
    sha256: ec96eff60d187277db7e53193e2a91671c047127c75a493ff764bb362521458e
    role: context
  - path: data/aio/AutoregressiveLanguageModel.yaml
    sha256: 1ee5824569635aab5df1b1f23eaabca463bd7ef87d1b22e9d9c42375a49ec800
    role: context
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/BoltzmannMachineNetwork.yaml
    sha256: 1152d2d85c5c1c408a0420e13f211ed109b12fb289c706ee7449864e91aece03
    role: context
  - path: data/aio/CausalLLM.yaml
    sha256: 8ec50ab9a625008567463f70b4a2a1e0cb2cf07c8053d38d6a88e12106dfce49
    role: context
  - path: data/aio/ControllableLLM.yaml
    sha256: 4bfc9c61281445ef5eef704b66539865f03b47d4929809f4c09759553007f2f2
    role: context
  - path: data/aio/DeepBeliefNetwork.yaml
    sha256: e6912732493adbfea3b48e01184d33682ad262dd73801757c094a2b160046a58
    role: context
  - path: data/aio/DeepNeuralNetwork.yaml
    sha256: f5c4c7764ea05631bb6396200141eb8ba124725d2dc27919c7efe89e5e30b19e
    role: context
  - path: data/aio/EnergyBasedLLM.yaml
    sha256: e9e29aa4f8400ad463dfe058fade876ef36c4a2637e1ebc4b42688116896310b
    role: context
  - path: data/aio/GaussianNoiseLayer.yaml
    sha256: 1d6c203daf9e9a5a450a85a7d7bf6e55bb9bffbeea7ceffcc1a8aefbd9629452
    role: context
  - path: data/aio/HiddenLayer.yaml
    sha256: 945f974c1d298a827086c3439ec3f9ae029380f6d2fa52378eb95ccad1f3b886
    role: context
  - path: data/aio/ImplicitLanguageModel.yaml
    sha256: 818c396b19757360dcdff6291a85d589c50638e0dc6d6bfcd96fdcb7bdf46ce9
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ProbabilisticHiddenLayer.yaml
    sha256: 610c29db815f7348c5bdcdc7e7460dd2dea9ea338f3727ebb1596c51b4af41da
    role: context
  - path: data/aio/RecurrentLayer.yaml
    sha256: d0aeaf40e9c0001883cce7f9b0bec41c75db8dbcafb8aea18eb1694816900de5
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/aio/RestrictedBoltzmannMachine.yaml
    sha256: 322fcb3b1f6064d944379ed79ffdcb7360fc2c3edd300c0a5a3f46be1f48df43
    role: context
  - path: data/aio/TemporalBias.yaml
    sha256: 37057ec37a0e18218b6e40aef6596314fb1a0feb6748a7c6db0006742b24bb44
    role: context
  - path: data/aio/VectorAutoregression.yaml
    sha256: 8a8e67b3efe79835eb5ce1edc437fe4fe9f6f6c95d7aeb22b602c97c38d3c211
    role: context
  - path: data/curated/AutoregressiveConditionalRestrictedBoltzmannMachine.yaml
    sha256: 90a1f5e24bc598fb27a121c50ede62b4917ebd9f5275853e54191eb81fe75e42
    role: target
  - path: data/curated/FactoredRestrictedBoltzmannMachineLanguageModel.yaml
    sha256: 29deb5941ba0aa7deaea89f413db49df90cd72240136a6a3eb92aba1b7557d64
    role: context
  - path: data/curated/HiddenMarkovModel.yaml
    sha256: 062a31bd525cb90e8077d4889c177f55cb7b29dea4e71c33be95bae9e72a5240
    role: context
  - path: data/curated/RecurrentTemporalRestrictedBoltzmannMachine.yaml
    sha256: 22e07ca591e3474e0dfc5f48d6af336a447089a343495888784fa670c50247ef
    role: target
  - path: data/curated/SigmoidBeliefNetwork.yaml
    sha256: 5fa2d037504b10f0d11db0ebdfef5b7d0f8175d4739d45a3abea789d00164c6a
    role: context
  - path: data/curated/TemporalFactoredRestrictedBoltzmannMachineLanguageModel.yaml
    sha256: 5a0e1352b13263fec8f7f3051db2c11acdb196410f302350d00510c5df4d51f9
    role: context
  - path: data/curated/TemporalRestrictedBoltzmannMachine.yaml
    sha256: 1bc9d5f9d0c420b3dad756c969f181cae7e97ef74bf139fed9c431b337465e62
    role: target
  - path: research/discovery/20261011T184102Z-temporal-rbm.json
    sha256: c61d340e5ca0145ec8e77c81a81d9f3906e2d188a519e976d82832cd3a945f51
    role: context
  - path: research/discovery/temporal-rbm-boundaries.py
    sha256: 856a611ef50b5cb50d6cd7d15e807b9621f54775a654eee74b37c87f7daf868b
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
- target_id: AIMech:TemporalRestrictedBoltzmannMachine
  path: data/curated/TemporalRestrictedBoltzmannMachine.yaml
  label: Temporal restricted Boltzmann machine
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TemporalRestrictedBoltzmannMachine.yaml
    role: maintained
- target_id: AIMech:RecurrentTemporalRestrictedBoltzmannMachine
  path: data/curated/RecurrentTemporalRestrictedBoltzmannMachine.yaml
  label: Recurrent temporal restricted Boltzmann machine
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RecurrentTemporalRestrictedBoltzmannMachine.yaml
    role: maintained
- target_id: AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine
  path: data/curated/AutoregressiveConditionalRestrictedBoltzmannMachine.yaml
  label: Autoregressive conditional restricted Boltzmann machine
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AutoregressiveConditionalRestrictedBoltzmannMachine.yaml
    role: maintained
scope:
  description: All fields of three explicitly selected temporal RBM architectures.
  selection: Three exact maintained IDs in the discovery ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:TemporalRestrictedBoltzmannMachine
  - AIMech:RecurrentTemporalRestrictedBoltzmannMachine
  - AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine
  exclusions:
  - target: Author code, general performance claims and other source versions
    reason: The three inspected PDFs and finite curator calculations do not certify
      software behavior, all variants or empirical rankings.
  - target: Prior records and the remaining discovery frontier
    reason: Prior records provide boundaries. Separate RNN output estimators, structured-output
      CRBMs and temporal autoencoding remain follow-up leads; earlier frontier dispositions
      are retained.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:TemporalRestrictedBoltzmannMachine
  - AIMech:RecurrentTemporalRestrictedBoltzmannMachine
  - AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 86.59s (0:01:26)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 364 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 102 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 99,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:TemporalRestrictedBoltzmannMachine
  - AIMech:RecurrentTemporalRestrictedBoltzmannMachine
  - AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine
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
  - AIMech:TemporalRestrictedBoltzmannMachine
  - AIMech:RecurrentTemporalRestrictedBoltzmannMachine
  - AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine
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
  - AIMech:TemporalRestrictedBoltzmannMachine
  - AIMech:RecurrentTemporalRestrictedBoltzmannMachine
  - AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Temporal RBM mathematical boundary calculations
  command: python3 research/discovery/temporal-rbm-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:TemporalRestrictedBoltzmannMachine
  - AIMech:RecurrentTemporalRestrictedBoltzmannMachine
  - AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine
  exit_code: 0
  expected_exit_code: 0
  summary: '{"trbm": {"normalized_joint": 1.0, "filtered_h1": 0.6224593312018546,
    "smoothed_h1": 0.6345317477570805, "exact_next": 0.6422333146149961, "plug_mean_next":
    0.643875827815082}, "rtrbm": {"log_probability": -1.9488424494893266, "gradient":
    [0.004070725210531423, -0.0012469383887315985, -0.06495525260501475, -0.03301346798390119],
    "direct_recurrent_term": -0.04118360278527837, "indirect_recurrent_term": 0.008170134801377182,
    "length_two_exact_recurrent_gradient": -0.07468599656772924, "length_two_recurrence_only_gradient":
    0.0, "finite_differences_pass": true}, "crbm": {"log_density": -1.4784500342117175,
    "hidden_prior": 0.5174928576663897, "hidden_posterior": 0.31647910626368436, "visible_mean":
    0.8639942861331118, "visible_variance": 1.1598041599556246, "gradient": [-1.0639942861331118,
    -0.2010137514027054, -0.7101618933357241, -0.7447960002931782, -0.14070962598189377],
    "missing_frame_filtered_mean": 0.0, "missing_frame_smoothed_mean": 0.8, "finite_differences_pass":
    true}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T184102Z-temporal-rbm.json
  accessed_at: '2026-10-11T18:41:40Z'
  support: supports
  summary: 'All 442 pinned AIO labels/scoped synonyms and 361 preceding native IDs/names/aliases
    were compared, with no normalized identity match. Full-checkout fixed-string searches
    included ignored and hidden files in both worktree and main, returning 24 lines
    each. All 18 unique matched contents were read: temporal FRBM source references,
    model contrasts, a discovery lead and saved review context, rather than existing
    candidate records. All 44 semantic label/synonym hits and 21 exact AIO nodes were
    inspected, alongside corresponding generated records and four complete native
    neighbors. Previously read contextual files were checked for byte identity. Absence
    is bounded to this snapshot and inspected neighborhood.'
  search_scope: 'All 442 pinned AIO labels/scoped synonyms and 361 preceding native
    IDs/names/aliases were compared, with no normalized identity match. Full-checkout
    fixed-string searches included ignored and hidden files in both worktree and main,
    returning 24 lines each. All 18 unique matched contents were read: temporal FRBM
    source references, model contrasts, a discovery lead and saved review context,
    rather than existing candidate records. All 44 semantic label/synonym hits and
    21 exact AIO nodes were inspected, alongside corresponding generated records and
    four complete native neighbors. Previously read contextual files were checked
    for byte identity. Absence is bounded to this snapshot and inspected neighborhood.'
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Twenty-one exact CLASS nodes with full annotations and outgoing edges in
    source_analysis.aio_mapping_inspection; corresponding generated records
  accessed_at: '2026-10-11T18:41:40Z'
  support: supports
  summary: 'All 44 semantic hits and 21 exact annotated AIO CLASS nodes with outgoing
    edges were read. Fourteen corresponding generated YAML files were previously fully
    read and verified byte-identical; seven were read in this batch. Four complete
    native neighbors were inspected: static and temporal FRBM (previous full reading
    with byte verification), sigmoid belief network and hidden Markov model (read
    this batch). TRBM and autoregressive CRBM broadly map to ArtificialNeuralNetwork;
    RTRBM broadly maps to RecurrentNeuralNetwork through its deterministic recurrence
    and RBM-output objective. All three relate to RestrictedBoltzmannMachine through
    their within-step conditional construction. BoltzmannMachineNetwork has a symmetric
    whole-network scope that does not cover directed temporal links unchanged. RecurrentLayer,
    HiddenLayer and ProbabilisticHiddenLayer are components, not whole sequence architectures.
    BayesianNetwork does not identify the mixed directed/undirected parameterization,
    and ProbabilisticGraphicalModel is task-scoped in this pin. MarkovChain does not
    identify the neural parameterization; marginal visible histories and hidden/state
    augmentation require explicit boundaries. DeepBeliefNetwork and DeepNeuralNetwork
    are not implied by a single hidden layer unrolled in time. AutoregressiveLanguageModel,
    CausalLLM, ControllableLLM, EnergyBasedLLM and ImplicitLanguageModel require language-specific
    scope. VectorAutoregression is linear; AutoregressiveDistributedLag does not identify
    a conditional energy model. GaussianNoiseLayer is training-time regularization,
    not a Gaussian visible conditional, and TemporalBias is a selection/sampling bias,
    not a dynamic neural bias. Previous native models provide boundaries without reassessing
    their own scientific approval.'
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T184102Z-temporal-rbm.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T18:41:40Z'
  support: supports
  summary: 'Four complete native records provide boundaries: static and temporal FRBM
    (previous full reading with byte verification), sigmoid belief network and hidden
    Markov model (fully read in this batch). They distinguish categorical-word factorization,
    stochastic temporal language modeling, pure directed logistic conditionals and
    state-dependent emissions, without renewed scientific approval.'
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/temporal-rbm-boundaries.py
  locator: TRBM smoothing and uncertain-history mixtures; exact RTRBM objective gradients
    and direct dynamic-bias dependence; Gaussian CRBM mixture, gradients and observed/missing-data
    inference
  accessed_at: '2026-10-11T18:41:40Z'
  snapshot_sha256: 856a611ef50b5cb50d6cd7d15e807b9621f54775a654eee74b37c87f7daf868b
  support: supports
  summary: Original finite calculations normalize a two-step stochastic TRBM, exhibit
    posterior smoothing and distinguish exact history mixtures from plug-in means.
    A binary RTRBM calculation differentiates the exact normalized sequence objective,
    checking every parameter against central finite differences and isolating the
    direct dynamic-bias contribution to recurrent weights. A two-step example has
    zero recurrence-only contribution but a nonzero exact recurrent-weight derivative.
    A scalar Gaussian CRBM is checked against its explicit Gaussian mixture and finite-difference
    gradients; fully observed hidden inference is invariant to the future factor,
    while a missing-visible Gaussian subcase requires smoothing. Mean visible reconstructions
    remove conditional sampling variance. These are curator calculations, not author-code
    or benchmark evidence.
- evidence_id: temporalrestrictedboltzmannmachine-source-0
  kind: primary_source
  reference: https://proceedings.mlr.press/v2/sutskever07a/sutskever07a.pdf
  locator: Sections 2.1–2.4, Figure 2 and Equations (10)–(18), PDF pp.2–5; omitted-edge
    naming and exact no-HH special case, Section 3, p.5; multilayer qualifications,
    Sections 4.2–5, pp.7–8
  accessed_at: '2026-10-11T18:17:21Z'
  snapshot_sha256: 8b8b19704c753dc7e52bcefb32eb218c87d84f772c390c3810445a644749897b
  support: supports
  summary: Learning Multilevel Distributed Representations for High-Dimensional Sequences.
    AISTATS 2007 / PMLR 2:548–555 proceedings PDF, eight pages. No printed page numbers
    appear on the inspected pages; use PDF-page locators. Actual visual reading scopes
    are declared in the ledger; retrieval and conversion do not certify reading of
    other pages.
- evidence_id: temporalrestrictedboltzmannmachine-source-1
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2008/file/9ad6aaed513b73148b7d49f70afcfb32-Paper.pdf
  locator: Section 3, Equations (4)–(5) and discussion of posterior Gibbs updates
    and conditional partition ratios, PDF p.3
  accessed_at: '2026-10-11T18:29:52Z'
  snapshot_sha256: 7ef2f7679831a4c8ac4079b47b622bb82cda8f8045148f436e6554c79d0137f1
  support: supports
  summary: The Recurrent Temporal Restricted Boltzmann Machine. Eight-page proceedings
    PDF, Advances in Neural Information Processing Systems 21, conference NIPS 2008;
    author bibliography lists the volume publication in 2009. Use PDF-page locators.
    Actual visual reading scopes are declared in the ledger; retrieval and conversion
    do not certify reading of other pages.
- evidence_id: recurrenttemporalrestrictedboltzmannmachine-source-0
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2008/file/9ad6aaed513b73148b7d49f70afcfb32-Paper.pdf
  locator: Sections 2–4.3, Equations (1)–(14), Figure 2 and Algorithms 2–4, PDF pp.2–6;
    Equation (12) indexing and Equation (13) direct-parameter contribution qualified
    against Equations (6), (8)–(11); limitations and conclusion, pp.6–8
  accessed_at: '2026-10-11T18:29:52Z'
  snapshot_sha256: 7ef2f7679831a4c8ac4079b47b622bb82cda8f8045148f436e6554c79d0137f1
  support: supports
  summary: The Recurrent Temporal Restricted Boltzmann Machine. Eight-page proceedings
    PDF, Advances in Neural Information Processing Systems 21, conference NIPS 2008;
    author bibliography lists the volume publication in 2009. Use PDF-page locators.
    Actual visual reading scopes are declared in the ledger; retrieval and conversion
    do not certify reading of other pages.
- evidence_id: autoregressiveconditionalrestrictedboltzmannmachine-source-0
  kind: primary_source
  reference: https://papers.neurips.cc/paper/3078-modeling-human-motion-using-binary-latent-variables.pdf
  locator: Sections 2–2.2, Equations (1)–(7) and Figure 2, PDF pp.2–4; initialized
    generation and online missing-data procedure, Sections 4 and 4.4, pp.5–6; higher-level
    extension and scope limits, Sections 5–6, pp.7–8
  accessed_at: '2026-10-11T18:29:53Z'
  snapshot_sha256: 7613916f0695ce3d8899550b6711f3fead075b0cfa8b06d1706fdb8c95b4e2c8
  support: supports
  summary: Modeling Human Motion Using Binary Latent Variables. Eight-page proceedings
    PDF, Advances in Neural Information Processing Systems 19, conference NIPS 2006,
    volume published in 2007. The PDF has no visible printed page numbers; use PDF-page
    locators. Actual visual reading scopes are declared in the ledger; retrieval and
    conversion do not certify reading of other pages.
- evidence_id: autoregressiveconditionalrestrictedboltzmannmachine-source-1
  kind: primary_source
  reference: https://proceedings.mlr.press/v2/sutskever07a/sutskever07a.pdf
  locator: Section 3, TRBM-HH omitted-edge definition and exact-inference qualification,
    PDF p.5; Section 4.2, fully observed no-HH posterior qualification, p.7
  accessed_at: '2026-10-11T18:17:21Z'
  snapshot_sha256: 8b8b19704c753dc7e52bcefb32eb218c87d84f772c390c3810445a644749897b
  support: supports
  summary: Learning Multilevel Distributed Representations for High-Dimensional Sequences.
    AISTATS 2007 / PMLR 2:548–555 proceedings PDF, eight pages. No printed page numbers
    appear on the inspected pages; use PDF-page locators. Actual visual reading scopes
    are declared in the ledger; retrieval and conversion do not certify reading of
    other pages.
assessments:
- assessment_id: temporalrestrictedboltzmannmachine
  area: evidence
  topic: Identity, definition, mechanism, limitations, source provenance and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:TemporalRestrictedBoltzmannMachine
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - temporalrestrictedboltzmannmachine-source-0
  - temporalrestrictedboltzmannmachine-source-1
  summary: 'This record covers the original single-layer temporal RBM construction
    of Sutskever and Hinton, with its finite lag window and omitted-edge special cases.
    The full architecture has visible-to-visible, visible-to-hidden and hidden-to-hidden
    history connections. It is distinct from temporal FRBM’s factored categorical-word
    construction, RTRBM’s deterministic recurrent state, and the observed-history-only
    autoregressive CRBM. Multilayer stacking is an extension rather than part of this
    single-layer identity; a filtering algorithm does not define the latent probabilistic
    model. All 442 pinned AIO labels/scoped synonyms and 361 preceding native IDs/names/aliases
    were compared, with no normalized identity match. Full-checkout fixed-string searches
    included ignored and hidden files in both worktree and main, returning 24 lines
    each. All 18 unique matched contents were read: temporal FRBM source references,
    model contrasts, a discovery lead and saved review context, rather than existing
    candidate records. All 44 semantic label/synonym hits and 21 exact AIO nodes were
    inspected, alongside corresponding generated records and four complete native
    neighbors. Previously read contextual files were checked for byte identity. Absence
    is bounded to this snapshot and inspected neighborhood.'
  details: 'For binary vectors v_t and h_t, set the visible bias a_t=a+sum_k A_k^T
    v_(t-k) and hidden bias b_t=b+sum_k B_k^T h_(t-k)+sum_k C_k^T v_(t-k). Define
    p(v_t,h_t|history)=exp(v_t^T C_0 h_t+a_t^T v_t+b_t^T h_t)/Z_t(history), and multiply
    these normalized factors over time using shared parameters and the source’s learned
    initial contributions for unavailable earlier states. Conditional on observed
    current and previous visibles and known previous hidden states, the current hidden
    posterior factorizes with probabilities sigmoid(C_0^T v_t+b_t). Unknown previous
    hidden states generally require marginalization; the proposed online filter instead
    substitutes their inferred probability vectors in b_t. Learning treats these approximate
    filtered states as context and uses per-step contrastive-divergence updates. The
    original paper distinguishes this approximation from smoothing with future observations
    and from an exact likelihood gradient. Limitations: The conditional partition
    depends on history, including previous hidden states. It is not one sequence-independent
    global constant, and exact posterior Gibbs updates can require ratios of such
    partitions. A factorial posterior given known latent history does not imply factorial
    or exact filtering after uncertain history is marginalized. Mean substitution
    through nonlinear normalized factors is generally approximate, and future observations
    can revise earlier hidden-state posteriors. The paper explicitly notes that changing
    its parameter-dependent approximate posterior can reduce the variational bound.
    Finite CD, mean visible reconstructions and ignoring future evidence provide no
    monotonic bound or likelihood guarantee. TRBM-HH denotes the variant with hidden-to-hidden
    links omitted, not one retaining only those links. For fully observed visible
    sequences its hidden posterior is factorial; missing observations and multilayer
    compositions change that inference problem. The displayed construction has no
    past-hidden-to-current-visible links; a footnote mentions those as a possible
    extension. Gaussian visible units, deeper compositions and different lag structures
    require their own stated assumptions. No empirical ranking, long-memory guarantee
    or author-code behavior is certified.'
  dimensions:
  - name: concept-kind
    value: architecture
    definition: Complete neural sequence architecture, distinguished by stochastic
      hidden history, deterministic recurrent state or observed-history conditioning.
    evidence_ids:
    - temporalrestrictedboltzmannmachine-source-0
    - temporalrestrictedboltzmannmachine-source-1
  - name: aio-assessment
    value: broad_match,related_match
    definition: 'All 44 semantic hits and 21 exact annotated AIO CLASS nodes with
      outgoing edges were read. Fourteen corresponding generated YAML files were previously
      fully read and verified byte-identical; seven were read in this batch. Four
      complete native neighbors were inspected: static and temporal FRBM (previous
      full reading with byte verification), sigmoid belief network and hidden Markov
      model (read this batch). TRBM and autoregressive CRBM broadly map to ArtificialNeuralNetwork;
      RTRBM broadly maps to RecurrentNeuralNetwork through its deterministic recurrence
      and RBM-output objective. All three relate to RestrictedBoltzmannMachine through
      their within-step conditional construction. BoltzmannMachineNetwork has a symmetric
      whole-network scope that does not cover directed temporal links unchanged. RecurrentLayer,
      HiddenLayer and ProbabilisticHiddenLayer are components, not whole sequence
      architectures. BayesianNetwork does not identify the mixed directed/undirected
      parameterization, and ProbabilisticGraphicalModel is task-scoped in this pin.
      MarkovChain does not identify the neural parameterization; marginal visible
      histories and hidden/state augmentation require explicit boundaries. DeepBeliefNetwork
      and DeepNeuralNetwork are not implied by a single hidden layer unrolled in time.
      AutoregressiveLanguageModel, CausalLLM, ControllableLLM, EnergyBasedLLM and
      ImplicitLanguageModel require language-specific scope. VectorAutoregression
      is linear; AutoregressiveDistributedLag does not identify a conditional energy
      model. GaussianNoiseLayer is training-time regularization, not a Gaussian visible
      conditional, and TemporalBias is a selection/sampling bias, not a dynamic neural
      bias. Previous native models provide boundaries without reassessing their own
      scientific approval.'
    evidence_ids:
    - mapping
- assessment_id: recurrenttemporalrestrictedboltzmannmachine
  area: evidence
  topic: Identity, definition, mechanism, limitations, source provenance and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:RecurrentTemporalRestrictedBoltzmannMachine
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - recurrenttemporalrestrictedboltzmannmachine-source-0
  summary: 'This is Sutskever, Hinton and Taylor’s 2008 RTRBM, with a real-valued
    recurrent state and separate binary within-step RBM hidden variables. Replacing
    a sampled TRBM hidden state by a deterministic probability vector changes the
    generative model; exact inference in RTRBM is not exact inference in the original
    stochastic TRBM. The recurrent update and conditional RBM share weights in this
    architecture. The real-valued state must not be conflated with the binary hidden
    variables integrated out of each output RBM. All 442 pinned AIO labels/scoped
    synonyms and 361 preceding native IDs/names/aliases were compared, with no normalized
    identity match. Full-checkout fixed-string searches included ignored and hidden
    files in both worktree and main, returning 24 lines each. All 18 unique matched
    contents were read: temporal FRBM source references, model contrasts, a discovery
    lead and saved review context, rather than existing candidate records. All 44
    semantic label/synonym hits and 21 exact AIO nodes were inspected, alongside corresponding
    generated records and four complete native neighbors. Previously read contextual
    files were checked for byte identity. Absence is bounded to this snapshot and
    inspected neighborhood.'
  details: 'Use column vectors, visible-by-hidden weights W and recurrent hidden-by-hidden
    weights U. Given r_(t-1), let the current binary RBM have joint mass proportional
    to exp(v_t^T W z_t+a^T v_t+(b+U r_(t-1))^T z_t), with binary z_t marginalized
    for the visible distribution. After observing or sampling v_t, set r_t=sigmoid(W^T
    v_t+b+U r_(t-1)); the first step uses the specified initial bias contribution.
    This update is deterministic by definition, so a fully observed visible sequence
    fixes the recurrent trajectory exactly and later observations cannot alter its
    already determined states. The visible-sequence log likelihood is the sum of the
    conditional RBM log marginals. Differentiate that objective through the recurrence
    and through each RBM’s direct parameter dependence. In particular, a recurrent
    weight affects the current output distribution through its hidden bias as well
    as later recurrent states. Backpropagation through time propagates these dependencies,
    while the paper approximates conditional RBM model expectations with contrastive
    divergence. A Gaussian-visible version replaces the binary visible base measure
    with a quadratic Gaussian term. Limitations: Exact deterministic-state inference
    requires the visible sequence to be observed. Missing observations require marginalizing
    uncertainty in visible values and induced recurrent states; the exact-inference
    statement does not automatically extend to that problem. Within-step binary hidden
    variables are stochastic even though the recurrent summary is deterministic. Exact
    state reconstruction does not make RBM partition functions, equilibrium sampling
    or finite-CD gradients exact or generally tractable. The printed Equation (12)
    local-score index differs from its surrounding next-step prose. Equation (13)
    displays a recurrence contribution but omits the direct current-RBM dependence
    through its dynamic hidden bias; a complete objective derivative must include
    it. The curated description follows the normalized generative definition and chain
    rule, checked by original finite differences, rather than treating Equations (12)–(14)
    as a verified implementation. No author-code defect or official erratum is asserted.
    A finite recurrent vector permits temporal dependence but does not guarantee successful
    learning of arbitrarily long dependencies. The source’s sample-quality comparisons
    do not establish universal superiority or exact likelihood learning. The source
    shares parameters between recurrence and output RBMs. A separate recurrent network
    that independently controls RBM parameters is a distinct neighboring construction;
    this record does not equate every RNN–RBM hybrid to RTRBM.'
  dimensions:
  - name: concept-kind
    value: architecture
    definition: Complete neural sequence architecture, distinguished by stochastic
      hidden history, deterministic recurrent state or observed-history conditioning.
    evidence_ids:
    - recurrenttemporalrestrictedboltzmannmachine-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: 'All 44 semantic hits and 21 exact annotated AIO CLASS nodes with
      outgoing edges were read. Fourteen corresponding generated YAML files were previously
      fully read and verified byte-identical; seven were read in this batch. Four
      complete native neighbors were inspected: static and temporal FRBM (previous
      full reading with byte verification), sigmoid belief network and hidden Markov
      model (read this batch). TRBM and autoregressive CRBM broadly map to ArtificialNeuralNetwork;
      RTRBM broadly maps to RecurrentNeuralNetwork through its deterministic recurrence
      and RBM-output objective. All three relate to RestrictedBoltzmannMachine through
      their within-step conditional construction. BoltzmannMachineNetwork has a symmetric
      whole-network scope that does not cover directed temporal links unchanged. RecurrentLayer,
      HiddenLayer and ProbabilisticHiddenLayer are components, not whole sequence
      architectures. BayesianNetwork does not identify the mixed directed/undirected
      parameterization, and ProbabilisticGraphicalModel is task-scoped in this pin.
      MarkovChain does not identify the neural parameterization; marginal visible
      histories and hidden/state augmentation require explicit boundaries. DeepBeliefNetwork
      and DeepNeuralNetwork are not implied by a single hidden layer unrolled in time.
      AutoregressiveLanguageModel, CausalLLM, ControllableLLM, EnergyBasedLLM and
      ImplicitLanguageModel require language-specific scope. VectorAutoregression
      is linear; AutoregressiveDistributedLag does not identify a conditional energy
      model. GaussianNoiseLayer is training-time regularization, not a Gaussian visible
      conditional, and TemporalBias is a selection/sampling bias, not a dynamic neural
      bias. Previous native models provide boundaries without reassessing their own
      scientific approval.'
    evidence_ids:
    - mapping
- assessment_id: autoregressiveconditionalrestrictedboltzmannmachine
  area: evidence
  topic: Identity, definition, mechanism, limitations, source provenance and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - autoregressiveconditionalrestrictedboltzmannmachine-source-0
  - autoregressiveconditionalrestrictedboltzmannmachine-source-1
  summary: 'This record is scoped to Taylor, Hinton and Roweis’s autoregressive CRBM
    construction for vector sequences, particularly its Gaussian-visible, binary-hidden
    formulation. The general label conditional RBM and acronym CRBM are not claimed
    as exclusive aliases because other conditional RBMs condition on arbitrary inputs
    or use different parameterizations. This is the observed-history specialization
    related to TRBM-HH; RTRBM and full TRBM also propagate hidden history. A stacked
    multilevel construction is not silently included in the single-layer record. All
    442 pinned AIO labels/scoped synonyms and 361 preceding native IDs/names/aliases
    were compared, with no normalized identity match. Full-checkout fixed-string searches
    included ignored and hidden files in both worktree and main, returning 24 lines
    each. All 18 unique matched contents were read: temporal FRBM source references,
    model contrasts, a discovery lead and saved review context, rather than existing
    candidate records. All 44 semantic label/synonym hits and 21 exact AIO nodes were
    inspected, alongside corresponding generated records and four complete native
    neighbors. Previously read contextual files were checked for byte identity. Absence
    is bounded to this snapshot and inspected neighborhood.'
  details: 'Condition on preceding visible frames and compute dynamic biases d_t=c+sum_k
    A_k^T v_(t-k) and e_t=b+sum_k D_k^T v_(t-k), allowing different lag windows for
    the two sums. In the source’s unit-variance Gaussian formulation, E(v_t,h_t|history)=one-half
    times ||v_t-d_t|| squared minus e_t^T h_t minus v_t^T W h_t. Thus hidden probabilities
    are sigmoid(e_t+W^T v_t), and visible coordinates given h_t are independent unit-variance
    Gaussians with mean d_t+W h_t. The partition is conditional on the fixed history.
    For fully observed frames the hidden posterior factorizes, and likelihood gradients
    contrast data and conditional-model statistics; the paper approximates them by
    CD while holding earlier frames fixed. Its implementation description samples
    positive-phase binary hidden states, uses hidden probabilities for negative-phase
    statistics, and uses mean visible reconstructions in place of Gaussian draws.
    Generation starts from supplied initial frames and repeatedly samples the current
    conditional RBM; the original conditional training does not model the first lag-window
    frames. Limitations: The single-layer visible conditional depends on the fixed
    observed lag window. Nonlinear hidden features do not introduce an unbounded latent
    temporal memory path; deeper stacked models are separate compositions. Sections
    2–2.1 explicitly give exact factorial hidden inference for fully observed frames.
    Section 2.2’s broad statement about omitted smoothing must not override that graph-specific
    result: future factors contain no earlier hidden state once the visible sequence
    is fixed. Missing visible data and multilevel models can require smoothing; the
    reported online missing-data procedure is approximate. Replacing Gaussian visible
    samples by conditional means removes conditional sampling variance and is not
    exact Gibbs sampling from the stated Gaussian model. Finite CD is not an exact
    likelihood gradient or a convergence guarantee. The general energy in Equation
    (1) includes visible standard deviations and scaled interactions; the displayed
    mechanism deliberately adopts the source’s sigma_i=1 convention. Rescaling arbitrary
    variances without transforming weights changes the distribution. A conditional
    RBM is richer than a linear autoregression, although removing the hidden interactions
    leaves an autoregressive Gaussian special case. Initial-frame distributions, missing-data
    posterior integration, phase disambiguation and transition coverage need separate
    modeling assumptions. No benchmark ranking or author-code certification is asserted.'
  dimensions:
  - name: concept-kind
    value: architecture
    definition: Complete neural sequence architecture, distinguished by stochastic
      hidden history, deterministic recurrent state or observed-history conditioning.
    evidence_ids:
    - autoregressiveconditionalrestrictedboltzmannmachine-source-0
    - autoregressiveconditionalrestrictedboltzmannmachine-source-1
  - name: aio-assessment
    value: broad_match,related_match
    definition: 'All 44 semantic hits and 21 exact annotated AIO CLASS nodes with
      outgoing edges were read. Fourteen corresponding generated YAML files were previously
      fully read and verified byte-identical; seven were read in this batch. Four
      complete native neighbors were inspected: static and temporal FRBM (previous
      full reading with byte verification), sigmoid belief network and hidden Markov
      model (read this batch). TRBM and autoregressive CRBM broadly map to ArtificialNeuralNetwork;
      RTRBM broadly maps to RecurrentNeuralNetwork through its deterministic recurrence
      and RBM-output objective. All three relate to RestrictedBoltzmannMachine through
      their within-step conditional construction. BoltzmannMachineNetwork has a symmetric
      whole-network scope that does not cover directed temporal links unchanged. RecurrentLayer,
      HiddenLayer and ProbabilisticHiddenLayer are components, not whole sequence
      architectures. BayesianNetwork does not identify the mixed directed/undirected
      parameterization, and ProbabilisticGraphicalModel is task-scoped in this pin.
      MarkovChain does not identify the neural parameterization; marginal visible
      histories and hidden/state augmentation require explicit boundaries. DeepBeliefNetwork
      and DeepNeuralNetwork are not implied by a single hidden layer unrolled in time.
      AutoregressiveLanguageModel, CausalLLM, ControllableLLM, EnergyBasedLLM and
      ImplicitLanguageModel require language-specific scope. VectorAutoregression
      is linear; AutoregressiveDistributedLag does not identify a conditional energy
      model. GaussianNoiseLayer is training-time regularization, not a Gaussian visible
      conditional, and TemporalBias is a selection/sampling bias, not a dynamic neural
      bias. Previous native models provide boundaries without reassessing their own
      scientific approval.'
    evidence_ids:
    - mapping
- assessment_id: trbm-boundaries
  area: consistency
  topic: Normalized conditional chain and latent-history inference
  outcome: supported
  target_ids:
  - AIMech:TemporalRestrictedBoltzmannMachine
  evidence_ids:
  - temporalrestrictedboltzmannmachine-source-0
  - temporalrestrictedboltzmannmachine-source-1
  - finite-conventions
  summary: Retain single-layer TRBM with explicit filtering and smoothing limits.
  details: The exact binary two-step joint sums to one. A hidden-state posterior of
    0.6224593312 given the first observed frame changes to 0.6345317478 after the
    next frame. Mixing normalized conditionals gives next-frame probability 0.6422333146;
    substituting the filtered hidden mean gives 0.6438758278. The differences demonstrate
    that known-history factorial conditionals do not make uncertain-history filtering
    or smoothing exact. Dynamic visible and hidden biases, history-dependent partitions,
    learned initialization contributions and the no-HH variant are separately scoped.
    The source explicitly qualifies CD and parameter-dependent approximate posterior
    changes.
- assessment_id: rtrbm-boundaries
  area: consistency
  topic: Deterministic model state and complete likelihood differentiation
  outcome: supported
  target_ids:
  - AIMech:RecurrentTemporalRestrictedBoltzmannMachine
  evidence_ids:
  - recurrenttemporalrestrictedboltzmannmachine-source-0
  - finite-conventions
  summary: Retain RTRBM as a distinct generative model, with printed-gradient qualifications.
  details: The source makes the recurrent state deterministic and retains separate
    stochastic within-step hidden variables. The original finite calculation normalizes
    all length-three visible sequences and checks all four scalar parameter gradients
    by central differences. The recurrent-weight gradient is -0.0330134680, composed
    of direct conditional contribution -0.0411836028 and recurrence contribution 0.0081701348.
    In a two-step example the recurrence-only term is zero but the exact derivative
    is -0.0746859966. This exposes the missing direct term if printed Equation (13)
    is used alone; Equation (12) also has an index disagreement with adjacent prose.
    The record relies on the normalized objective and chain rule, without asserting
    an official erratum or author-code defect. Exact observed-state inference does
    not remove RBM partitions or CD approximation.
- assessment_id: crbm-boundaries
  area: consistency
  topic: Observed-history conditional model and missing-data distinction
  outcome: supported
  target_ids:
  - AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine
  evidence_ids:
  - autoregressiveconditionalrestrictedboltzmannmachine-source-0
  - autoregressiveconditionalrestrictedboltzmannmachine-source-1
  - finite-conventions
  summary: Retain the autoregressive CRBM with a bounded alias and inference scope.
  details: The scalar Gaussian example agrees with its explicit two-Gaussian mixture
    and all five parameter gradients pass finite differences. Its hidden posterior
    is 0.3164791063, visible mean 0.8639942861 and variance 1.1598041600. Future factors
    cancel from the hidden posterior when the intervening visible values are observed.
    In contrast, a zero-hidden-coupling linear-Gaussian example changes a missing-frame
    mean from 0 under filtering to 0.8 under smoothing. These checks clarify the paper’s
    broad no-smoothing statement against its exact fully observed single-layer graph.
    Mean Gaussian reconstructions remove conditional variance and are not exact Gibbs
    samples. The generic label CRBM remains outside the exclusive alias list.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Mapping scope and local identity
  outcome: supported
  target_ids:
  - AIMech:TemporalRestrictedBoltzmannMachine
  - AIMech:RecurrentTemporalRestrictedBoltzmannMachine
  - AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain three architectures with explicit broad neural and related RBM mappings.
  details: 'All 44 semantic hits and 21 exact annotated AIO CLASS nodes with outgoing
    edges were read. Fourteen corresponding generated YAML files were previously fully
    read and verified byte-identical; seven were read in this batch. Four complete
    native neighbors were inspected: static and temporal FRBM (previous full reading
    with byte verification), sigmoid belief network and hidden Markov model (read
    this batch). TRBM and autoregressive CRBM broadly map to ArtificialNeuralNetwork;
    RTRBM broadly maps to RecurrentNeuralNetwork through its deterministic recurrence
    and RBM-output objective. All three relate to RestrictedBoltzmannMachine through
    their within-step conditional construction. BoltzmannMachineNetwork has a symmetric
    whole-network scope that does not cover directed temporal links unchanged. RecurrentLayer,
    HiddenLayer and ProbabilisticHiddenLayer are components, not whole sequence architectures.
    BayesianNetwork does not identify the mixed directed/undirected parameterization,
    and ProbabilisticGraphicalModel is task-scoped in this pin. MarkovChain does not
    identify the neural parameterization; marginal visible histories and hidden/state
    augmentation require explicit boundaries. DeepBeliefNetwork and DeepNeuralNetwork
    are not implied by a single hidden layer unrolled in time. AutoregressiveLanguageModel,
    CausalLLM, ControllableLLM, EnergyBasedLLM and ImplicitLanguageModel require language-specific
    scope. VectorAutoregression is linear; AutoregressiveDistributedLag does not identify
    a conditional energy model. GaussianNoiseLayer is training-time regularization,
    not a Gaussian visible conditional, and TemporalBias is a selection/sampling bias,
    not a dynamic neural bias. Previous native models provide boundaries without reassessing
    their own scientific approval.'
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:TemporalRestrictedBoltzmannMachine
  - AIMech:RecurrentTemporalRestrictedBoltzmannMachine
  - AIMech:AutoregressiveConditionalRestrictedBoltzmannMachine
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - temporalrestrictedboltzmannmachine-source-0
  - temporalrestrictedboltzmannmachine-source-1
  - recurrenttemporalrestrictedboltzmannmachine-source-0
  - autoregressiveconditionalrestrictedboltzmannmachine-source-0
  - autoregressiveconditionalrestrictedboltzmannmachine-source-1
  rationale: TRBM propagates stochastic hidden history, RTRBM defines a deterministic
    recurrent state tied to conditional RBM probabilities, and autoregressive CRBM
    conditions on a finite window of observed frames without hidden recurrence. Their
    shared RBM component does not equate whole-model identity, inference or learning.
    Generic conditional RBM remains broader than the autoregressive record’s alias
    scope.
limitations:
- Adversarial author self-review only; every target remains DRAFT.
- All eight PDF pages of Sutskever2007, RTRBM2008 and Taylor2006 were visually read.
  Other versions, code and frontier papers were not fully inspected in this review.
- Sutskever2007 retains its verified earlier retrieval timestamp. PDF-page locators
  and exact hashes distinguish unpaginated files and conference/proceedings publication
  years.
- Finite calculations check stated examples and mathematical boundaries, not author
  software, benchmark performance, global convergence or every parameter value.
- 200 pending inspection leads plus unresolved dispositions remain; discovery is active.
links: []
tags:
- native-concepts
- temporal-rbm
- self-review
- discovery-ongoing
```
