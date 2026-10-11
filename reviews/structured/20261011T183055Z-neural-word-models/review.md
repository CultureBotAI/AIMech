# Scientific self-review of FRBM, temporal FRBM and the original neural probabilistic language model

- Review: 20261011T183055Z-neural-word-models
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T18:28:02Z
- Finished UTC: 2026-10-11T18:30:55Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain three DRAFT word-prediction architectures with distinct latent-state and parameter-sharing scopes. The source equation conflict and approximation limits are explicit. No actionable curation finding remains within the declared scope.

## Scope And Provenance

All fields of three explicitly selected neural word-prediction architectures.

Selection: Three exact maintained IDs in the discovery ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 8c376b1a8e8079929cacaa4a75e360f5f068e898.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FactoredRestrictedBoltzmannMachineLanguageModel | data/curated/FactoredRestrictedBoltzmannMachineLanguageModel.yaml | maintained | Factored restricted Boltzmann machine language model |
| AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel | data/curated/TemporalFactoredRestrictedBoltzmannMachineLanguageModel.yaml | maintained | Temporal factored restricted Boltzmann machine language model |
| AIMech:NeuralProbabilisticLanguageModel | data/curated/NeuralProbabilisticLanguageModel.yaml | maintained | Neural probabilistic language model |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:FactoredRestrictedBoltzmannMachineLanguageModel, AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel, AIMech:NeuralProbabilisticLanguageModel | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 67.34s (0:01:07)<br>Checked 442 record(s); 0 failed.<br>Checked 361 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 101 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 98,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:FactoredRestrictedBoltzmannMachineLanguageModel, AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel, AIMech:NeuralProbabilisticLanguageModel | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:FactoredRestrictedBoltzmannMachineLanguageModel, AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel, AIMech:NeuralProbabilisticLanguageModel | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:FactoredRestrictedBoltzmannMachineLanguageModel, AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel, AIMech:NeuralProbabilisticLanguageModel | Command exited 0 with no output. |
| Language-architecture mathematical boundary calculations | passed | True | AIMech:FactoredRestrictedBoltzmannMachineLanguageModel, AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel, AIMech:NeuralProbabilisticLanguageModel | {"frbm": {"word_a_probability": 0.823529411764706, "wrong_printed_bias_probability": 0.5384615384615384, "hidden_bias_gradient": 0.03361344537815114, "output_weight_gradient": 0.15126050420168058, "one_gibbs_step_a_probability": 0.8299319727891156, "mean_hidden_reconstruction_a": 0.8368281586934104}, "temporal": {"exact_word_a_probability": 0.6944444444444444, "plug_in_word_a_probability": 0.7, "exact_current_hidden_posterior": 0.8400000000000001, "plug_in_hidden_posterior": 0.8571428571428572, "previous_hidden_posterior_after_current_word": 0.52}, "nplm": {"probabilities": [0.5945590235113032, 0.4054409764886967], "shared_input_embedding_gradient": 0.18145678133753995, "unused_input_embedding_likelihood_gradient": 0, "independent_output_bias_gradient": -0.5945590235113033, "optional_direct_and_order_checks": true}, "scope": "Finite conditional models and derivative checks only; no author-code or empirical certification."} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, source provenance and AIO mapping

evidence: supported. Targets: AIMech:FactoredRestrictedBoltzmannMachineLanguageModel.

This is Mnih and Hinton’s static FRBM language architecture. Factored refers to matrices G_i=R W_i with shared learned word features, not explicit part-of-speech or morphological factors. Its context words are conditioned on; their marginal distribution is not learned by this single conditional. Temporal FRBM adds directed hidden-state history, while LBL removes stochastic hidden variables and Replicated Softmax models an undirected document of a given length. All 442 pinned AIO labels/scoped synonyms and 358 preceding native IDs/names/aliases were compared, with no normalized identity match. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, returning 33 lines each. All 24 unique matched contents were read: LBL source references and model contrasts, discovery leads and saved review context. These do not constitute existing candidate records. All 85 semantic label/synonym hits and 22 exact AIO nodes were inspected, alongside corresponding generated records and four complete native neighbors. Previously read contextual files were checked for byte identity. Absence is bounded to this snapshot and inspected neighborhood.

Write r_w for the shared column embedding of word w. For context positions 1 through n-1 and candidate word w at position n, define t=b_h+sum_(i&lt;n) W_i^T r_context_i+W_n^T r_w and candidate bias a_w=b_r^T r_w+b_w. The conditional joint energy is E(w,h;context)=-t^T h-a_w. Summing binary h gives unnormalized word mass exp(a_w) times product_j(1+exp(t_j)); normalize these masses over candidate words. Given all words, hidden units are independent Bernoulli with probabilities sigmoid(t_j). Given h, the next word has softmax scores r_w^T W_n h+a_w. Exact conditional likelihood gradients use data-posterior statistics minus model expectations, whose vocabulary sum is explicit. The paper instead trains latent-variable models using finite contrastive divergence: start at the observed word, update hidden, word and hidden states, and contrast resulting statistics. Some runs replace the sampled one-hot word with its probability vector, a mean-field reconstruction variant. Limitations: Equation (5) prints negative candidate-bias terms, whereas exp(-E) from Equations (2)–(4) and the word conditional in Equation (9) require positive a_w. The curated marginal follows those defining equations and discloses the sign conflict; it does not infer author-code behavior. The conditional partition is tractable by summing the vocabulary after binary-hidden marginalization. Generic RBM partition-function intractability must not be copied unchanged into this clamped-context construction; the exact calculation can still be expensive for a large vocabulary. Finite-step contrastive divergence is not the exact conditional maximum-likelihood gradient. A deterministic probability-vector reconstruction is not a categorical Gibbs sample. Sharing word features across positions does not make sequence context permutation invariant because W_i depends on position. Low-rank factorization constrains the effective interaction matrices. No predictive ranking, semantic quality guarantee, global training convergence or implementation certification is asserted.

### Identity, definition, mechanism, limitations, source provenance and AIO mapping

evidence: supported. Targets: AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel.

This is the temporal FRBM in Mnih and Hinton’s 2007 language-model paper. It extends the factored categorical-word construction with shared hidden-to-hidden weights A. It is distinct from the static FRBM, the broader temporal RBM with additional visible-history connections, and deterministic recurrent language models. Its approximate filtering algorithm is not the exact latent-state model. All 442 pinned AIO labels/scoped synonyms and 358 preceding native IDs/names/aliases were compared, with no normalized identity match. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, returning 33 lines each. All 24 unique matched contents were read: LBL source references and model contrasts, discovery leads and saved review context. These do not constitute existing candidate records. All 85 semantic label/synonym hits and 22 exact AIO nodes were inspected, alongside corresponding generated records and four complete native neighbors. Previously read contextual files were checked for byte identity. Absence is bounded to this snapshot and inspected neighborhood.

Apply shared FRBM parameters to successive overlapping word windows. Connect hidden state h_tau to h_(tau+1) so that the current hidden bias becomes b_h+A h_tau; conditional on that earlier state, the current word and hidden variables retain an FRBM joint with its own normalizer. Exact prediction must account for uncertainty in previous hidden states. The proposed online approximation instead substitutes their inferred probabilities p_tau, computes p_(tau+1)=sigmoid(b_h+A p_tau+sum_i W_i^T r_word_i) after observing the current window, and predicts the next word using the FRBM word distribution with the correspondingly shifted bias. Learning uses these approximate filtered probabilities, applies contrastive-divergence updates to individual model instances, and combines them. The temporal-weight update contrasts current hidden probabilities and their reconstruction, multiplied by the preceding filtered vector; it does not propagate an exact likelihood gradient through the full latent history. Limitations: Replacing an uncertain earlier hidden state by its mean inside a sigmoid or a context-dependent normalized word distribution is generally not exact marginalization. Observing a new word can also change the posterior over previous hidden states. The cited temporal-RBM source explicitly ignores future evidence for online learning and notes that changes in its parameter-dependent approximate posterior can decrease the variational bound. Approximate filtering plus finite CD therefore does not guarantee monotonic likelihood or bound improvement. The recurrent path permits dependence beyond the explicit context window, but does not guarantee faithful long-range memory, tractable exact filtering or a particular effective context length. This construction has directed temporal links and undirected current word–hidden interactions. It is not equivalent to a single unconditioned RBM, a pure directed Bayesian network parameterization, or a deep belief network merely because latent states are present. The static FRBM marginal’s printed bias-sign conflict remains qualified when its conditional prediction is reused. No implementation audit, empirical superiority or exact sequence-likelihood result is asserted.

### Identity, definition, mechanism, limitations, source provenance and AIO mapping

evidence: supported. Targets: AIMech:NeuralProbabilisticLanguageModel.

This record is scoped to Bengio, Ducharme, Vincent and Jauvin’s published 2003 architecture, especially its tanh feed-forward formulation with optional direct input-to-output weights. It does not designate every neural probabilistic model of language, or assert historical priority over the earlier work acknowledged by the paper. It differs from LBL’s tied bilinear output embeddings and Morin–Bengio’s tree-node-conditioned nonlinear predictor. All 442 pinned AIO labels/scoped synonyms and 358 preceding native IDs/names/aliases were compared, with no normalized identity match. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, returning 33 lines each. All 24 unique matched contents were read: LBL source references and model contrasts, discovery leads and saved review context. These do not constitute existing candidate records. All 85 semantic label/synonym hits and 22 exact AIO nodes were inspected, alongside corresponding generated records and four complete native neighbors. Previously read contextual files were checked for byte identity. Absence is bounded to this snapshot and inspected neighborhood.

Look up each preceding word in a shared matrix C and concatenate the n-1 context embeddings in their specified positions into x. Compute vocabulary logits y=b+W x+U tanh(d+H x), where direct weights W may be set to zero. Apply the vocabulary softmax and multiply next-word conditionals to obtain sequence probabilities under the chosen context convention. Jointly optimize the embeddings and network parameters by stochastic gradient ascent on the corpus log likelihood with regularization; a weight-decay term added to a maximized objective has the negative penalty sign. The input embedding lookup is shared across context positions, while the output matrices and biases are separately learned parameters. Contributions from repeated appearances of the same context word accumulate in its embedding row. The paper also discusses mixing the resulting predictions with an interpolated trigram model, which is an additional ensemble choice. Limitations: The specified feed-forward formulation has a finite context window and a fixed vocabulary. It is not a recurrent state model or a tree-normalized output architecture. The flat vocabulary softmax incurs vocabulary-dependent computation even when only the observed next-word likelihood is required. Joint learning is nonconvex and does not guarantee optimality or universally meaningful semantic distances. An input-embedding row absent from an example’s context has zero gradient from that example’s likelihood, even if its word is the target. This statement excludes regularization, which can still affect unused rows. Output-word parameters remain separate and can receive gradients. Sharing the lookup matrix does not discard context order: concatenation places embeddings in different slots with distinct subsequent weights. Optional direct weights change the parameterization but not probability normalization. The paper warns that regularizing W and H without C can permit a compensating growth of embedding scale. Smooth feature sharing motivates generalization, but does not prove correct probabilities for every unseen combination. No benchmark superiority or author-code behavior is certified.

### Conditional normalization, bias signs and approximate learning

consistency: supported. Targets: AIMech:FactoredRestrictedBoltzmannMachineLanguageModel.

Retain static FRBM as a conditional latent-word architecture.

The finite two-word, one-hidden-bit example gives next-word mass 14/17 using positive bias from exp(-E); the printed negative bias produces 7/13. Equations (2)–(4) and (9) support the positive convention, so the conflicting Equation (5) is qualified rather than silently adopted. Exact hidden-bias and output-weight gradients agree with finite differences. One Gibbs reconstruction gives 122/147 rather than equilibrium 14/17; mean-hidden reconstruction differs again. The vocabulary sum after hidden marginalization is tractable, although potentially expensive, and must not be conflated with a generic unconditioned RBM partition.

### Latent history versus plug-in filtering

consistency: supported. Targets: AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel.

Retain temporal FRBM separately from its approximation and from broader TRBM.

With two equally probable earlier hidden states, mixing normalized current-state conditionals gives next-word probability 25/36 and current hidden posterior 21/25. Substituting the earlier mean gives 7/10 and 6/7 instead. The new word also changes the posterior on the earlier hidden state to 13/25. This finite counterexample supports the limits of mean-field substitution and filtering without smoothing. The temporal-RBM background explicitly qualifies parameter-dependent approximate posterior changes and finite CD; those do not certify monotonically improving likelihood or an exact gradient through latent history.

### Joint lookup learning, independent output parameters and finite context

consistency: supported. Targets: AIMech:NeuralProbabilisticLanguageModel.

Retain the original 2003 nonlinear language architecture.

The paper specifies concatenated shared lookup embeddings, optional direct weights and logits b+Wx+U tanh(d+Hx). Finite differences confirm that repeated context occurrences accumulate into the same embedding gradient (0.1814567813 in the example). An absent input row has zero example-likelihood gradient despite a nonzero target-output bias gradient (-0.5945590235); regularization is explicitly excluded from the zero-gradient statement. Optional direct weights and context order affect probabilities while normalization remains exact. This differs from tied LBL output embeddings and from a recurrent state or tree-output architecture.

### Mapping scope and local identity

grounding: supported. Targets: AIMech:FactoredRestrictedBoltzmannMachineLanguageModel, AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel, AIMech:NeuralProbabilisticLanguageModel.

Retain three distinct architectures with explicit AIO mapping directions.

All 85 semantic hits and 22 exact annotated AIO CLASS nodes with outgoing edges were read. Eighteen corresponding generated YAML files were previously fully read and verified byte-identical; the other four were read in this batch. Four full native neighbors were read and their bytes verified: Morin–Bengio, LBL, DocNADE and Replicated Softmax. All three new architectures broadly map to AutoregressiveLanguageModel through next-word conditional prediction; LanguageModel is a redundant broader target. Static and temporal FRBM additionally relate to RestrictedBoltzmannMachine through current word–hidden undirected interactions without asserting that the whole sequential construction is a single unconditioned RBM. FactoredLanguageModel describes linguistic factors and FactorizedLLM expert decomposition, not factorized word/hidden weight matrices. ImplicitLanguageModel and EnergyBasedLLM concern whole-sequence non-autoregressive energy models. RecurrentNeuralNetwork describes directed temporal networks and captures only part of temporal FRBM’s hybrid structure; RecurrentLayer is a component. DeepBeliefNetwork requires multilayer latent pretraining rather than merely an evolving hidden state. The source counts NPLM’s linear lookup and nonlinear hidden computation separately; no forced depth equivalence to DeepFeedForwardNetwork or DeepNeuralNetwork is asserted. Perceptron is a binary linear predictor. EmbeddingLayer, HiddenLayer, OutputLayer, SoftmaxLayer and ProbabilisticHiddenLayer are components. BayesianNetwork and task-scoped ProbabilisticGraphicalModel do not identify these parameterizations. Earlier native records provide scope boundaries, not fresh approvals.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:FactoredRestrictedBoltzmannMachineLanguageModel, AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel, AIMech:NeuralProbabilisticLanguageModel. Static FRBM factorizes context-conditioned latent-word weights; temporal FRBM adds uncertain hidden history; the original NPLM uses deterministic nonlinear prediction from jointly learned lookup embeddings with separate output parameters. Shared word features do not make their latent-state, normalization or learning mechanisms equivalent. Broad language-model and related RBM mappings retain those distinctions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T182734Z-neural-word-models.json | supports | All 442 pinned AIO labels/scoped synonyms and 358 preceding native IDs/names/aliases were compared, with no normalized identity match. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, returning 33 lines each. All 24 unique matched contents were read: LBL source references and model contrasts, discovery leads and saved review context. These do not constitute existing candidate records. All 85 semantic label/synonym hits and 22 exact AIO nodes were inspected, alongside corresponding generated records and four complete native neighbors. Previously read contextual files were checked for byte identity. Absence is bounded to this snapshot and inspected neighborhood. |
| mapping | sources/aio/aio.json; Twenty-two exact CLASS nodes with full annotations and outgoing edges in source_analysis.aio_mapping_inspection; corresponding generated records | supports | All 85 semantic hits and 22 exact annotated AIO CLASS nodes with outgoing edges were read. Eighteen corresponding generated YAML files were previously fully read and verified byte-identical; the other four were read in this batch. Four full native neighbors were read and their bytes verified: Morin–Bengio, LBL, DocNADE and Replicated Softmax. All three new architectures broadly map to AutoregressiveLanguageModel through next-word conditional prediction; LanguageModel is a redundant broader target. Static and temporal FRBM additionally relate to RestrictedBoltzmannMachine through current word–hidden undirected interactions without asserting that the whole sequential construction is a single unconditioned RBM. FactoredLanguageModel describes linguistic factors and FactorizedLLM expert decomposition, not factorized word/hidden weight matrices. ImplicitLanguageModel and EnergyBasedLLM concern whole-sequence non-autoregressive energy models. RecurrentNeuralNetwork describes directed temporal networks and captures only part of temporal FRBM’s hybrid structure; RecurrentLayer is a component. DeepBeliefNetwork requires multilayer latent pretraining rather than merely an evolving hidden state. The source counts NPLM’s linear lookup and nonlinear hidden computation separately; no forced depth equivalence to DeepFeedForwardNetwork or DeepNeuralNetwork is asserted. Perceptron is a binary linear predictor. EmbeddingLayer, HiddenLayer, OutputLayer, SoftmaxLayer and ProbabilisticHiddenLayer are components. BayesianNetwork and task-scoped ProbabilisticGraphicalModel do not identify these parameterizations. Earlier native records provide scope boundaries, not fresh approvals. |
| neighbors | research/discovery/20261011T182734Z-neural-word-models.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Four full native records were read and verified byte-identical: Morin–Bengio hierarchical neural LM, LBL, DocumentNADE and ReplicatedSoftmax. They supply node-conditioned, bilinear, additive document and undirected document boundaries, not renewed scientific approval. |
| finite-conventions | research/discovery/neural-word-models-boundaries.py; Conditional FRBM enumeration, source bias signs and gradients; uncertain-history marginalization versus mean substitution; NPLM lookup/output gradients and positional/direct-weight effects | supports | Original finite calculations enumerate a conditional FRBM, verify positive candidate biases from its energy, and check likelihood gradients. One Gibbs reconstruction and a mean-hidden reconstruction both differ from the exact conditional. A two-history temporal example compares exact mixtures of normalized conditionals with substituting the prior hidden mean, including posterior revision of the earlier state. NPLM checks verify repeated-input embedding gradients, zero likelihood gradient for an unused lookup row despite a nonzero output bias gradient, optional direct connections and order sensitivity. These are finite curator examples, not author-code or benchmark evidence. |
| factoredrestrictedboltzmannmachinelanguagemodel-source-0 | https://www.cs.utoronto.ca/~hinton/absps/threenew.pdf; Sections 2–2.2, Equations (1)–(10), Figure 1a and context-conditioning footnote, printed pp.642–644 / PDF pp.2–4; Equation (5) bias signs qualified against Equations (2)–(4) and (9) | supports | Three New Graphical Models for Statistical Language Modelling. ICML 2007 author-hosted eight-page paper, printed pp.641–648. Printed page equals PDF page plus 640. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |
| temporalfactoredrestrictedboltzmannmachinelanguagemodel-source-0 | https://www.cs.utoronto.ca/~hinton/absps/threenew.pdf; Sections 3–3.2, Figure 1a and Equations (10)–(12), printed pp.643–645 / PDF pp.3–5; static conditional prediction, Equations (2)–(5) and (9), pp.642–644 / PDF pp.2–4 | supports | Three New Graphical Models for Statistical Language Modelling. ICML 2007 author-hosted eight-page paper, printed pp.641–648. Printed page equals PDF page plus 640. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |
| temporalfactoredrestrictedboltzmannmachinelanguagemodel-source-1 | https://proceedings.mlr.press/v2/sutskever07a/sutskever07a.pdf; Sections 2.2–2.4, Equations (10)–(18), dynamic biases, conditional normalizers, approximate filtering and learning qualifications, PDF pp.3–5 | supports | Learning Multilevel Distributed Representations for High-Dimensional Sequences. AISTATS 2007 / PMLR 2:548–555 proceedings PDF, eight pages. No printed page numbers appear on inspected pages; use PDF-page locators. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |
| neuralprobabilisticlanguagemodel-source-0 | https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf; Section 2, Figure 1 and Equation (1), printed pp.1141–1143 / PDF pp.5–7; sequence factorization and context convention, p.1138 / PDF p.2; shared representation and prior-work scope, pp.1139–1141 / PDF pp.3–5 | supports | A Neural Probabilistic Language Model. JMLR 3 (February 2003):1137–1155, nineteen-page publisher PDF. Printed page equals PDF page plus 1136. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |

## Limits And Additional Notes

- Adversarial author self-review only; every target remains DRAFT.
- Inspected visual scopes: Mnih2007 pages 1–6, Sutskever2007 pages 1–6, Bengio2003 pages 1–7. Remaining pages were not certified as read.
- Mnih2007 uses a verified earlier retrieval; the Sutskever PDF has no printed page numbers on inspected pages. Exact hashes and actual PDF-page locators are retained.
- Finite calculations check stated examples and mathematical boundaries, not author code, benchmark performance, global convergence or all parameter values.
- 198 pending inspection leads plus unresolved dispositions remain; discovery is active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T183055Z-neural-word-models
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of FRBM, temporal FRBM and the original neural probabilistic
  language model
started_at: '2026-10-11T18:28:02Z'
finished_at: '2026-10-11T18:30:55Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially checked all fields against
    declared scopes of three primary PDFs, 22 exact AIO CLASS nodes and corresponding
    generated records, four complete native neighbors and finite curator calculations.
    Source bias signs, exact conditional normalization, latent-history marginalization,
    approximate filtering/learning and embedding/output gradients were examined. This
    is author self-review.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain three DRAFT word-prediction architectures with distinct latent-state
  and parameter-sharing scopes. The source equation conflict and approximation limits
  are explicit. No actionable curation finding remains within the declared scope.
source:
  git_revision: 8c376b1a8e8079929cacaa4a75e360f5f068e898
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
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
  - path: data/aio/DeepBeliefNetwork.yaml
    sha256: e6912732493adbfea3b48e01184d33682ad262dd73801757c094a2b160046a58
    role: context
  - path: data/aio/DeepFeedForwardNetwork.yaml
    sha256: d66c246318687598cf762fae4b54586a312b70d143735aba5c12b2606c45c8c9
    role: context
  - path: data/aio/DeepNeuralNetwork.yaml
    sha256: f5c4c7764ea05631bb6396200141eb8ba124725d2dc27919c7efe89e5e30b19e
    role: context
  - path: data/aio/EmbeddingLayer.yaml
    sha256: 1496ce1d75a70d75c8ffba951063cdb48c6507ed623aba45c0663260d0766343
    role: context
  - path: data/aio/EnergyBasedLLM.yaml
    sha256: e9e29aa4f8400ad463dfe058fade876ef36c4a2637e1ebc4b42688116896310b
    role: context
  - path: data/aio/FactoredLanguageModel.yaml
    sha256: d5e425f3c7cc5b57fdab859cdc777b62398077a6ac9312aef6a89af42c6eb421
    role: context
  - path: data/aio/FactorizedLLM.yaml
    sha256: f73a5e4d591e4d832f94bfa044d77c5645f585b042f07485f99920527d67b6d5
    role: context
  - path: data/aio/HiddenLayer.yaml
    sha256: 945f974c1d298a827086c3439ec3f9ae029380f6d2fa52378eb95ccad1f3b886
    role: context
  - path: data/aio/ImplicitLanguageModel.yaml
    sha256: 818c396b19757360dcdff6291a85d589c50638e0dc6d6bfcd96fdcb7bdf46ce9
    role: context
  - path: data/aio/LanguageModel.yaml
    sha256: 67c8faa6d8ac8fb5194931f662d513d1527cefb92ab1d7c283b2c8d1ddc20c4a
    role: context
  - path: data/aio/OutputLayer.yaml
    sha256: 86f80cc923b7eede14e564cb90529754a83650f506efed22e7e786207df8d10b
    role: context
  - path: data/aio/Perceptron.yaml
    sha256: 6b1cc7cb96bfe03ed8720cca04490657976eea656fab6674d7ef685c34216915
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
  - path: data/aio/SoftmaxLayer.yaml
    sha256: 9e95a3f0fc849fc08a3bd4165cd53b9e03d1a74f921a533e9159c053a3b2d193
    role: context
  - path: data/curated/DocumentNADE.yaml
    sha256: fd0969626c9aa10b8d5d876c3d537cbef1b317090c49944334e00131060b9d27
    role: context
  - path: data/curated/FactoredRestrictedBoltzmannMachineLanguageModel.yaml
    sha256: 29deb5941ba0aa7deaea89f413db49df90cd72240136a6a3eb92aba1b7557d64
    role: target
  - path: data/curated/HierarchicalProbabilisticNeuralNetworkLanguageModel.yaml
    sha256: 442acca95184d087a240472a584978cb74abd4be227ac225c4f8ab557b5a8c87
    role: context
  - path: data/curated/LogBilinearLanguageModel.yaml
    sha256: f23eb2c07544fd2567187f66a33038c38b015f36d914fff8c85237ade470404c
    role: context
  - path: data/curated/NeuralProbabilisticLanguageModel.yaml
    sha256: 113512fe907376bdc28c4806248b2276cfbdf0469168879f86c9129c0d9e2788
    role: target
  - path: data/curated/ReplicatedSoftmax.yaml
    sha256: 1a71debad5b7ac38c8e647ffb18c52f712300a7906b44efa5d348fb3488940cf
    role: context
  - path: data/curated/TemporalFactoredRestrictedBoltzmannMachineLanguageModel.yaml
    sha256: 5a0e1352b13263fec8f7f3051db2c11acdb196410f302350d00510c5df4d51f9
    role: target
  - path: research/discovery/20261011T182734Z-neural-word-models.json
    sha256: 5a98932012eba4d9578fbcb785d4c7d5b80eb2a8bc2c11ee0f2c18a215b70fd0
    role: context
  - path: research/discovery/neural-word-models-boundaries.py
    sha256: 8944a5f70fe2018d8244734f85ea597aabd1edbf2b14ea56bccc66f098d6fbb3
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
- target_id: AIMech:FactoredRestrictedBoltzmannMachineLanguageModel
  path: data/curated/FactoredRestrictedBoltzmannMachineLanguageModel.yaml
  label: Factored restricted Boltzmann machine language model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FactoredRestrictedBoltzmannMachineLanguageModel.yaml
    role: maintained
- target_id: AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel
  path: data/curated/TemporalFactoredRestrictedBoltzmannMachineLanguageModel.yaml
  label: Temporal factored restricted Boltzmann machine language model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TemporalFactoredRestrictedBoltzmannMachineLanguageModel.yaml
    role: maintained
- target_id: AIMech:NeuralProbabilisticLanguageModel
  path: data/curated/NeuralProbabilisticLanguageModel.yaml
  label: Neural probabilistic language model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NeuralProbabilisticLanguageModel.yaml
    role: maintained
scope:
  description: All fields of three explicitly selected neural word-prediction architectures.
  selection: Three exact maintained IDs in the discovery ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:FactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:NeuralProbabilisticLanguageModel
  exclusions:
  - target: Author code, uninspected pages and empirical rankings
    reason: Only declared source pages and original finite calculations support this
      review. Source equation conflicts do not establish software defects.
  - target: Prior records and the remaining discovery frontier
    reason: Prior records provide boundaries. Broader TRBM and adaptive importance-sampling
      training are explicit follow-up leads; other frontier dispositions are retained.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:FactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:NeuralProbabilisticLanguageModel
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 67.34s (0:01:07)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 361 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 101 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 98,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:FactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:NeuralProbabilisticLanguageModel
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
  - AIMech:FactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:NeuralProbabilisticLanguageModel
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
  - AIMech:FactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:NeuralProbabilisticLanguageModel
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Language-architecture mathematical boundary calculations
  command: python3 research/discovery/neural-word-models-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:FactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:NeuralProbabilisticLanguageModel
  exit_code: 0
  expected_exit_code: 0
  summary: '{"frbm": {"word_a_probability": 0.823529411764706, "wrong_printed_bias_probability":
    0.5384615384615384, "hidden_bias_gradient": 0.03361344537815114, "output_weight_gradient":
    0.15126050420168058, "one_gibbs_step_a_probability": 0.8299319727891156, "mean_hidden_reconstruction_a":
    0.8368281586934104}, "temporal": {"exact_word_a_probability": 0.6944444444444444,
    "plug_in_word_a_probability": 0.7, "exact_current_hidden_posterior": 0.8400000000000001,
    "plug_in_hidden_posterior": 0.8571428571428572, "previous_hidden_posterior_after_current_word":
    0.52}, "nplm": {"probabilities": [0.5945590235113032, 0.4054409764886967], "shared_input_embedding_gradient":
    0.18145678133753995, "unused_input_embedding_likelihood_gradient": 0, "independent_output_bias_gradient":
    -0.5945590235113033, "optional_direct_and_order_checks": true}, "scope": "Finite
    conditional models and derivative checks only; no author-code or empirical certification."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T182734Z-neural-word-models.json
  accessed_at: '2026-10-11T18:28:02Z'
  support: supports
  summary: 'All 442 pinned AIO labels/scoped synonyms and 358 preceding native IDs/names/aliases
    were compared, with no normalized identity match. Full-checkout fixed-string searches
    included ignored and hidden files in both worktree and main, returning 33 lines
    each. All 24 unique matched contents were read: LBL source references and model
    contrasts, discovery leads and saved review context. These do not constitute existing
    candidate records. All 85 semantic label/synonym hits and 22 exact AIO nodes were
    inspected, alongside corresponding generated records and four complete native
    neighbors. Previously read contextual files were checked for byte identity. Absence
    is bounded to this snapshot and inspected neighborhood.'
  search_scope: 'All 442 pinned AIO labels/scoped synonyms and 358 preceding native
    IDs/names/aliases were compared, with no normalized identity match. Full-checkout
    fixed-string searches included ignored and hidden files in both worktree and main,
    returning 33 lines each. All 24 unique matched contents were read: LBL source
    references and model contrasts, discovery leads and saved review context. These
    do not constitute existing candidate records. All 85 semantic label/synonym hits
    and 22 exact AIO nodes were inspected, alongside corresponding generated records
    and four complete native neighbors. Previously read contextual files were checked
    for byte identity. Absence is bounded to this snapshot and inspected neighborhood.'
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Twenty-two exact CLASS nodes with full annotations and outgoing edges in
    source_analysis.aio_mapping_inspection; corresponding generated records
  accessed_at: '2026-10-11T18:28:02Z'
  support: supports
  summary: 'All 85 semantic hits and 22 exact annotated AIO CLASS nodes with outgoing
    edges were read. Eighteen corresponding generated YAML files were previously fully
    read and verified byte-identical; the other four were read in this batch. Four
    full native neighbors were read and their bytes verified: Morin–Bengio, LBL, DocNADE
    and Replicated Softmax. All three new architectures broadly map to AutoregressiveLanguageModel
    through next-word conditional prediction; LanguageModel is a redundant broader
    target. Static and temporal FRBM additionally relate to RestrictedBoltzmannMachine
    through current word–hidden undirected interactions without asserting that the
    whole sequential construction is a single unconditioned RBM. FactoredLanguageModel
    describes linguistic factors and FactorizedLLM expert decomposition, not factorized
    word/hidden weight matrices. ImplicitLanguageModel and EnergyBasedLLM concern
    whole-sequence non-autoregressive energy models. RecurrentNeuralNetwork describes
    directed temporal networks and captures only part of temporal FRBM’s hybrid structure;
    RecurrentLayer is a component. DeepBeliefNetwork requires multilayer latent pretraining
    rather than merely an evolving hidden state. The source counts NPLM’s linear lookup
    and nonlinear hidden computation separately; no forced depth equivalence to DeepFeedForwardNetwork
    or DeepNeuralNetwork is asserted. Perceptron is a binary linear predictor. EmbeddingLayer,
    HiddenLayer, OutputLayer, SoftmaxLayer and ProbabilisticHiddenLayer are components.
    BayesianNetwork and task-scoped ProbabilisticGraphicalModel do not identify these
    parameterizations. Earlier native records provide scope boundaries, not fresh
    approvals.'
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T182734Z-neural-word-models.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T18:28:02Z'
  support: supports
  summary: 'Four full native records were read and verified byte-identical: Morin–Bengio
    hierarchical neural LM, LBL, DocumentNADE and ReplicatedSoftmax. They supply node-conditioned,
    bilinear, additive document and undirected document boundaries, not renewed scientific
    approval.'
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/neural-word-models-boundaries.py
  locator: Conditional FRBM enumeration, source bias signs and gradients; uncertain-history
    marginalization versus mean substitution; NPLM lookup/output gradients and positional/direct-weight
    effects
  accessed_at: '2026-10-11T18:28:02Z'
  snapshot_sha256: 8944a5f70fe2018d8244734f85ea597aabd1edbf2b14ea56bccc66f098d6fbb3
  support: supports
  summary: Original finite calculations enumerate a conditional FRBM, verify positive
    candidate biases from its energy, and check likelihood gradients. One Gibbs reconstruction
    and a mean-hidden reconstruction both differ from the exact conditional. A two-history
    temporal example compares exact mixtures of normalized conditionals with substituting
    the prior hidden mean, including posterior revision of the earlier state. NPLM
    checks verify repeated-input embedding gradients, zero likelihood gradient for
    an unused lookup row despite a nonzero output bias gradient, optional direct connections
    and order sensitivity. These are finite curator examples, not author-code or benchmark
    evidence.
- evidence_id: factoredrestrictedboltzmannmachinelanguagemodel-source-0
  kind: primary_source
  reference: https://www.cs.utoronto.ca/~hinton/absps/threenew.pdf
  locator: Sections 2–2.2, Equations (1)–(10), Figure 1a and context-conditioning
    footnote, printed pp.642–644 / PDF pp.2–4; Equation (5) bias signs qualified against
    Equations (2)–(4) and (9)
  accessed_at: '2026-10-11T18:06:34Z'
  snapshot_sha256: d0709a4032488109a2398ba64438e8363bb73e7c7791cbbcfcfa2075d326ba0c
  support: supports
  summary: Three New Graphical Models for Statistical Language Modelling. ICML 2007
    author-hosted eight-page paper, printed pp.641–648. Printed page equals PDF page
    plus 640. Actual visual reading scopes are declared in the ledger; retrieval and
    conversion do not certify reading of other pages.
- evidence_id: temporalfactoredrestrictedboltzmannmachinelanguagemodel-source-0
  kind: primary_source
  reference: https://www.cs.utoronto.ca/~hinton/absps/threenew.pdf
  locator: Sections 3–3.2, Figure 1a and Equations (10)–(12), printed pp.643–645 /
    PDF pp.3–5; static conditional prediction, Equations (2)–(5) and (9), pp.642–644
    / PDF pp.2–4
  accessed_at: '2026-10-11T18:06:34Z'
  snapshot_sha256: d0709a4032488109a2398ba64438e8363bb73e7c7791cbbcfcfa2075d326ba0c
  support: supports
  summary: Three New Graphical Models for Statistical Language Modelling. ICML 2007
    author-hosted eight-page paper, printed pp.641–648. Printed page equals PDF page
    plus 640. Actual visual reading scopes are declared in the ledger; retrieval and
    conversion do not certify reading of other pages.
- evidence_id: temporalfactoredrestrictedboltzmannmachinelanguagemodel-source-1
  kind: primary_source
  reference: https://proceedings.mlr.press/v2/sutskever07a/sutskever07a.pdf
  locator: Sections 2.2–2.4, Equations (10)–(18), dynamic biases, conditional normalizers,
    approximate filtering and learning qualifications, PDF pp.3–5
  accessed_at: '2026-10-11T18:17:21Z'
  snapshot_sha256: 8b8b19704c753dc7e52bcefb32eb218c87d84f772c390c3810445a644749897b
  support: supports
  summary: Learning Multilevel Distributed Representations for High-Dimensional Sequences.
    AISTATS 2007 / PMLR 2:548–555 proceedings PDF, eight pages. No printed page numbers
    appear on inspected pages; use PDF-page locators. Actual visual reading scopes
    are declared in the ledger; retrieval and conversion do not certify reading of
    other pages.
- evidence_id: neuralprobabilisticlanguagemodel-source-0
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf
  locator: Section 2, Figure 1 and Equation (1), printed pp.1141–1143 / PDF pp.5–7;
    sequence factorization and context convention, p.1138 / PDF p.2; shared representation
    and prior-work scope, pp.1139–1141 / PDF pp.3–5
  accessed_at: '2026-10-11T18:17:19Z'
  snapshot_sha256: 0bddf9a608d62da449a6413d86cbf6e8b206212595efe0e0a14da0d79d5f4976
  support: supports
  summary: A Neural Probabilistic Language Model. JMLR 3 (February 2003):1137–1155,
    nineteen-page publisher PDF. Printed page equals PDF page plus 1136. Actual visual
    reading scopes are declared in the ledger; retrieval and conversion do not certify
    reading of other pages.
assessments:
- assessment_id: factoredrestrictedboltzmannmachinelanguagemodel
  area: evidence
  topic: Identity, definition, mechanism, limitations, source provenance and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:FactoredRestrictedBoltzmannMachineLanguageModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - factoredrestrictedboltzmannmachinelanguagemodel-source-0
  summary: 'This is Mnih and Hinton’s static FRBM language architecture. Factored
    refers to matrices G_i=R W_i with shared learned word features, not explicit part-of-speech
    or morphological factors. Its context words are conditioned on; their marginal
    distribution is not learned by this single conditional. Temporal FRBM adds directed
    hidden-state history, while LBL removes stochastic hidden variables and Replicated
    Softmax models an undirected document of a given length. All 442 pinned AIO labels/scoped
    synonyms and 358 preceding native IDs/names/aliases were compared, with no normalized
    identity match. Full-checkout fixed-string searches included ignored and hidden
    files in both worktree and main, returning 33 lines each. All 24 unique matched
    contents were read: LBL source references and model contrasts, discovery leads
    and saved review context. These do not constitute existing candidate records.
    All 85 semantic label/synonym hits and 22 exact AIO nodes were inspected, alongside
    corresponding generated records and four complete native neighbors. Previously
    read contextual files were checked for byte identity. Absence is bounded to this
    snapshot and inspected neighborhood.'
  details: 'Write r_w for the shared column embedding of word w. For context positions
    1 through n-1 and candidate word w at position n, define t=b_h+sum_(i<n) W_i^T
    r_context_i+W_n^T r_w and candidate bias a_w=b_r^T r_w+b_w. The conditional joint
    energy is E(w,h;context)=-t^T h-a_w. Summing binary h gives unnormalized word
    mass exp(a_w) times product_j(1+exp(t_j)); normalize these masses over candidate
    words. Given all words, hidden units are independent Bernoulli with probabilities
    sigmoid(t_j). Given h, the next word has softmax scores r_w^T W_n h+a_w. Exact
    conditional likelihood gradients use data-posterior statistics minus model expectations,
    whose vocabulary sum is explicit. The paper instead trains latent-variable models
    using finite contrastive divergence: start at the observed word, update hidden,
    word and hidden states, and contrast resulting statistics. Some runs replace the
    sampled one-hot word with its probability vector, a mean-field reconstruction
    variant. Limitations: Equation (5) prints negative candidate-bias terms, whereas
    exp(-E) from Equations (2)–(4) and the word conditional in Equation (9) require
    positive a_w. The curated marginal follows those defining equations and discloses
    the sign conflict; it does not infer author-code behavior. The conditional partition
    is tractable by summing the vocabulary after binary-hidden marginalization. Generic
    RBM partition-function intractability must not be copied unchanged into this clamped-context
    construction; the exact calculation can still be expensive for a large vocabulary.
    Finite-step contrastive divergence is not the exact conditional maximum-likelihood
    gradient. A deterministic probability-vector reconstruction is not a categorical
    Gibbs sample. Sharing word features across positions does not make sequence context
    permutation invariant because W_i depends on position. Low-rank factorization
    constrains the effective interaction matrices. No predictive ranking, semantic
    quality guarantee, global training convergence or implementation certification
    is asserted.'
  dimensions:
  - name: concept-kind
    value: architecture
    definition: Complete next-word architecture, distinguished by latent variables,
      temporal history and neural parameterization.
    evidence_ids:
    - factoredrestrictedboltzmannmachinelanguagemodel-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: 'All 85 semantic hits and 22 exact annotated AIO CLASS nodes with
      outgoing edges were read. Eighteen corresponding generated YAML files were previously
      fully read and verified byte-identical; the other four were read in this batch.
      Four full native neighbors were read and their bytes verified: Morin–Bengio,
      LBL, DocNADE and Replicated Softmax. All three new architectures broadly map
      to AutoregressiveLanguageModel through next-word conditional prediction; LanguageModel
      is a redundant broader target. Static and temporal FRBM additionally relate
      to RestrictedBoltzmannMachine through current word–hidden undirected interactions
      without asserting that the whole sequential construction is a single unconditioned
      RBM. FactoredLanguageModel describes linguistic factors and FactorizedLLM expert
      decomposition, not factorized word/hidden weight matrices. ImplicitLanguageModel
      and EnergyBasedLLM concern whole-sequence non-autoregressive energy models.
      RecurrentNeuralNetwork describes directed temporal networks and captures only
      part of temporal FRBM’s hybrid structure; RecurrentLayer is a component. DeepBeliefNetwork
      requires multilayer latent pretraining rather than merely an evolving hidden
      state. The source counts NPLM’s linear lookup and nonlinear hidden computation
      separately; no forced depth equivalence to DeepFeedForwardNetwork or DeepNeuralNetwork
      is asserted. Perceptron is a binary linear predictor. EmbeddingLayer, HiddenLayer,
      OutputLayer, SoftmaxLayer and ProbabilisticHiddenLayer are components. BayesianNetwork
      and task-scoped ProbabilisticGraphicalModel do not identify these parameterizations.
      Earlier native records provide scope boundaries, not fresh approvals.'
    evidence_ids:
    - mapping
- assessment_id: temporalfactoredrestrictedboltzmannmachinelanguagemodel
  area: evidence
  topic: Identity, definition, mechanism, limitations, source provenance and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - temporalfactoredrestrictedboltzmannmachinelanguagemodel-source-0
  - temporalfactoredrestrictedboltzmannmachinelanguagemodel-source-1
  summary: 'This is the temporal FRBM in Mnih and Hinton’s 2007 language-model paper.
    It extends the factored categorical-word construction with shared hidden-to-hidden
    weights A. It is distinct from the static FRBM, the broader temporal RBM with
    additional visible-history connections, and deterministic recurrent language models.
    Its approximate filtering algorithm is not the exact latent-state model. All 442
    pinned AIO labels/scoped synonyms and 358 preceding native IDs/names/aliases were
    compared, with no normalized identity match. Full-checkout fixed-string searches
    included ignored and hidden files in both worktree and main, returning 33 lines
    each. All 24 unique matched contents were read: LBL source references and model
    contrasts, discovery leads and saved review context. These do not constitute existing
    candidate records. All 85 semantic label/synonym hits and 22 exact AIO nodes were
    inspected, alongside corresponding generated records and four complete native
    neighbors. Previously read contextual files were checked for byte identity. Absence
    is bounded to this snapshot and inspected neighborhood.'
  details: 'Apply shared FRBM parameters to successive overlapping word windows. Connect
    hidden state h_tau to h_(tau+1) so that the current hidden bias becomes b_h+A
    h_tau; conditional on that earlier state, the current word and hidden variables
    retain an FRBM joint with its own normalizer. Exact prediction must account for
    uncertainty in previous hidden states. The proposed online approximation instead
    substitutes their inferred probabilities p_tau, computes p_(tau+1)=sigmoid(b_h+A
    p_tau+sum_i W_i^T r_word_i) after observing the current window, and predicts the
    next word using the FRBM word distribution with the correspondingly shifted bias.
    Learning uses these approximate filtered probabilities, applies contrastive-divergence
    updates to individual model instances, and combines them. The temporal-weight
    update contrasts current hidden probabilities and their reconstruction, multiplied
    by the preceding filtered vector; it does not propagate an exact likelihood gradient
    through the full latent history. Limitations: Replacing an uncertain earlier hidden
    state by its mean inside a sigmoid or a context-dependent normalized word distribution
    is generally not exact marginalization. Observing a new word can also change the
    posterior over previous hidden states. The cited temporal-RBM source explicitly
    ignores future evidence for online learning and notes that changes in its parameter-dependent
    approximate posterior can decrease the variational bound. Approximate filtering
    plus finite CD therefore does not guarantee monotonic likelihood or bound improvement.
    The recurrent path permits dependence beyond the explicit context window, but
    does not guarantee faithful long-range memory, tractable exact filtering or a
    particular effective context length. This construction has directed temporal links
    and undirected current word–hidden interactions. It is not equivalent to a single
    unconditioned RBM, a pure directed Bayesian network parameterization, or a deep
    belief network merely because latent states are present. The static FRBM marginal’s
    printed bias-sign conflict remains qualified when its conditional prediction is
    reused. No implementation audit, empirical superiority or exact sequence-likelihood
    result is asserted.'
  dimensions:
  - name: concept-kind
    value: architecture
    definition: Complete next-word architecture, distinguished by latent variables,
      temporal history and neural parameterization.
    evidence_ids:
    - temporalfactoredrestrictedboltzmannmachinelanguagemodel-source-0
    - temporalfactoredrestrictedboltzmannmachinelanguagemodel-source-1
  - name: aio-assessment
    value: broad_match,related_match
    definition: 'All 85 semantic hits and 22 exact annotated AIO CLASS nodes with
      outgoing edges were read. Eighteen corresponding generated YAML files were previously
      fully read and verified byte-identical; the other four were read in this batch.
      Four full native neighbors were read and their bytes verified: Morin–Bengio,
      LBL, DocNADE and Replicated Softmax. All three new architectures broadly map
      to AutoregressiveLanguageModel through next-word conditional prediction; LanguageModel
      is a redundant broader target. Static and temporal FRBM additionally relate
      to RestrictedBoltzmannMachine through current word–hidden undirected interactions
      without asserting that the whole sequential construction is a single unconditioned
      RBM. FactoredLanguageModel describes linguistic factors and FactorizedLLM expert
      decomposition, not factorized word/hidden weight matrices. ImplicitLanguageModel
      and EnergyBasedLLM concern whole-sequence non-autoregressive energy models.
      RecurrentNeuralNetwork describes directed temporal networks and captures only
      part of temporal FRBM’s hybrid structure; RecurrentLayer is a component. DeepBeliefNetwork
      requires multilayer latent pretraining rather than merely an evolving hidden
      state. The source counts NPLM’s linear lookup and nonlinear hidden computation
      separately; no forced depth equivalence to DeepFeedForwardNetwork or DeepNeuralNetwork
      is asserted. Perceptron is a binary linear predictor. EmbeddingLayer, HiddenLayer,
      OutputLayer, SoftmaxLayer and ProbabilisticHiddenLayer are components. BayesianNetwork
      and task-scoped ProbabilisticGraphicalModel do not identify these parameterizations.
      Earlier native records provide scope boundaries, not fresh approvals.'
    evidence_ids:
    - mapping
- assessment_id: neuralprobabilisticlanguagemodel
  area: evidence
  topic: Identity, definition, mechanism, limitations, source provenance and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:NeuralProbabilisticLanguageModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - neuralprobabilisticlanguagemodel-source-0
  summary: 'This record is scoped to Bengio, Ducharme, Vincent and Jauvin’s published
    2003 architecture, especially its tanh feed-forward formulation with optional
    direct input-to-output weights. It does not designate every neural probabilistic
    model of language, or assert historical priority over the earlier work acknowledged
    by the paper. It differs from LBL’s tied bilinear output embeddings and Morin–Bengio’s
    tree-node-conditioned nonlinear predictor. All 442 pinned AIO labels/scoped synonyms
    and 358 preceding native IDs/names/aliases were compared, with no normalized identity
    match. Full-checkout fixed-string searches included ignored and hidden files in
    both worktree and main, returning 33 lines each. All 24 unique matched contents
    were read: LBL source references and model contrasts, discovery leads and saved
    review context. These do not constitute existing candidate records. All 85 semantic
    label/synonym hits and 22 exact AIO nodes were inspected, alongside corresponding
    generated records and four complete native neighbors. Previously read contextual
    files were checked for byte identity. Absence is bounded to this snapshot and
    inspected neighborhood.'
  details: 'Look up each preceding word in a shared matrix C and concatenate the n-1
    context embeddings in their specified positions into x. Compute vocabulary logits
    y=b+W x+U tanh(d+H x), where direct weights W may be set to zero. Apply the vocabulary
    softmax and multiply next-word conditionals to obtain sequence probabilities under
    the chosen context convention. Jointly optimize the embeddings and network parameters
    by stochastic gradient ascent on the corpus log likelihood with regularization;
    a weight-decay term added to a maximized objective has the negative penalty sign.
    The input embedding lookup is shared across context positions, while the output
    matrices and biases are separately learned parameters. Contributions from repeated
    appearances of the same context word accumulate in its embedding row. The paper
    also discusses mixing the resulting predictions with an interpolated trigram model,
    which is an additional ensemble choice. Limitations: The specified feed-forward
    formulation has a finite context window and a fixed vocabulary. It is not a recurrent
    state model or a tree-normalized output architecture. The flat vocabulary softmax
    incurs vocabulary-dependent computation even when only the observed next-word
    likelihood is required. Joint learning is nonconvex and does not guarantee optimality
    or universally meaningful semantic distances. An input-embedding row absent from
    an example’s context has zero gradient from that example’s likelihood, even if
    its word is the target. This statement excludes regularization, which can still
    affect unused rows. Output-word parameters remain separate and can receive gradients.
    Sharing the lookup matrix does not discard context order: concatenation places
    embeddings in different slots with distinct subsequent weights. Optional direct
    weights change the parameterization but not probability normalization. The paper
    warns that regularizing W and H without C can permit a compensating growth of
    embedding scale. Smooth feature sharing motivates generalization, but does not
    prove correct probabilities for every unseen combination. No benchmark superiority
    or author-code behavior is certified.'
  dimensions:
  - name: concept-kind
    value: architecture
    definition: Complete next-word architecture, distinguished by latent variables,
      temporal history and neural parameterization.
    evidence_ids:
    - neuralprobabilisticlanguagemodel-source-0
  - name: aio-assessment
    value: broad_match
    definition: 'All 85 semantic hits and 22 exact annotated AIO CLASS nodes with
      outgoing edges were read. Eighteen corresponding generated YAML files were previously
      fully read and verified byte-identical; the other four were read in this batch.
      Four full native neighbors were read and their bytes verified: Morin–Bengio,
      LBL, DocNADE and Replicated Softmax. All three new architectures broadly map
      to AutoregressiveLanguageModel through next-word conditional prediction; LanguageModel
      is a redundant broader target. Static and temporal FRBM additionally relate
      to RestrictedBoltzmannMachine through current word–hidden undirected interactions
      without asserting that the whole sequential construction is a single unconditioned
      RBM. FactoredLanguageModel describes linguistic factors and FactorizedLLM expert
      decomposition, not factorized word/hidden weight matrices. ImplicitLanguageModel
      and EnergyBasedLLM concern whole-sequence non-autoregressive energy models.
      RecurrentNeuralNetwork describes directed temporal networks and captures only
      part of temporal FRBM’s hybrid structure; RecurrentLayer is a component. DeepBeliefNetwork
      requires multilayer latent pretraining rather than merely an evolving hidden
      state. The source counts NPLM’s linear lookup and nonlinear hidden computation
      separately; no forced depth equivalence to DeepFeedForwardNetwork or DeepNeuralNetwork
      is asserted. Perceptron is a binary linear predictor. EmbeddingLayer, HiddenLayer,
      OutputLayer, SoftmaxLayer and ProbabilisticHiddenLayer are components. BayesianNetwork
      and task-scoped ProbabilisticGraphicalModel do not identify these parameterizations.
      Earlier native records provide scope boundaries, not fresh approvals.'
    evidence_ids:
    - mapping
- assessment_id: frbm-boundaries
  area: consistency
  topic: Conditional normalization, bias signs and approximate learning
  outcome: supported
  target_ids:
  - AIMech:FactoredRestrictedBoltzmannMachineLanguageModel
  evidence_ids:
  - factoredrestrictedboltzmannmachinelanguagemodel-source-0
  - finite-conventions
  summary: Retain static FRBM as a conditional latent-word architecture.
  details: The finite two-word, one-hidden-bit example gives next-word mass 14/17
    using positive bias from exp(-E); the printed negative bias produces 7/13. Equations
    (2)–(4) and (9) support the positive convention, so the conflicting Equation (5)
    is qualified rather than silently adopted. Exact hidden-bias and output-weight
    gradients agree with finite differences. One Gibbs reconstruction gives 122/147
    rather than equilibrium 14/17; mean-hidden reconstruction differs again. The vocabulary
    sum after hidden marginalization is tractable, although potentially expensive,
    and must not be conflated with a generic unconditioned RBM partition.
- assessment_id: temporal-boundaries
  area: consistency
  topic: Latent history versus plug-in filtering
  outcome: supported
  target_ids:
  - AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel
  evidence_ids:
  - temporalfactoredrestrictedboltzmannmachinelanguagemodel-source-0
  - temporalfactoredrestrictedboltzmannmachinelanguagemodel-source-1
  - finite-conventions
  summary: Retain temporal FRBM separately from its approximation and from broader
    TRBM.
  details: With two equally probable earlier hidden states, mixing normalized current-state
    conditionals gives next-word probability 25/36 and current hidden posterior 21/25.
    Substituting the earlier mean gives 7/10 and 6/7 instead. The new word also changes
    the posterior on the earlier hidden state to 13/25. This finite counterexample
    supports the limits of mean-field substitution and filtering without smoothing.
    The temporal-RBM background explicitly qualifies parameter-dependent approximate
    posterior changes and finite CD; those do not certify monotonically improving
    likelihood or an exact gradient through latent history.
- assessment_id: nplm-boundaries
  area: consistency
  topic: Joint lookup learning, independent output parameters and finite context
  outcome: supported
  target_ids:
  - AIMech:NeuralProbabilisticLanguageModel
  evidence_ids:
  - neuralprobabilisticlanguagemodel-source-0
  - finite-conventions
  summary: Retain the original 2003 nonlinear language architecture.
  details: The paper specifies concatenated shared lookup embeddings, optional direct
    weights and logits b+Wx+U tanh(d+Hx). Finite differences confirm that repeated
    context occurrences accumulate into the same embedding gradient (0.1814567813
    in the example). An absent input row has zero example-likelihood gradient despite
    a nonzero target-output bias gradient (-0.5945590235); regularization is explicitly
    excluded from the zero-gradient statement. Optional direct weights and context
    order affect probabilities while normalization remains exact. This differs from
    tied LBL output embeddings and from a recurrent state or tree-output architecture.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Mapping scope and local identity
  outcome: supported
  target_ids:
  - AIMech:FactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:NeuralProbabilisticLanguageModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain three distinct architectures with explicit AIO mapping directions.
  details: 'All 85 semantic hits and 22 exact annotated AIO CLASS nodes with outgoing
    edges were read. Eighteen corresponding generated YAML files were previously fully
    read and verified byte-identical; the other four were read in this batch. Four
    full native neighbors were read and their bytes verified: Morin–Bengio, LBL, DocNADE
    and Replicated Softmax. All three new architectures broadly map to AutoregressiveLanguageModel
    through next-word conditional prediction; LanguageModel is a redundant broader
    target. Static and temporal FRBM additionally relate to RestrictedBoltzmannMachine
    through current word–hidden undirected interactions without asserting that the
    whole sequential construction is a single unconditioned RBM. FactoredLanguageModel
    describes linguistic factors and FactorizedLLM expert decomposition, not factorized
    word/hidden weight matrices. ImplicitLanguageModel and EnergyBasedLLM concern
    whole-sequence non-autoregressive energy models. RecurrentNeuralNetwork describes
    directed temporal networks and captures only part of temporal FRBM’s hybrid structure;
    RecurrentLayer is a component. DeepBeliefNetwork requires multilayer latent pretraining
    rather than merely an evolving hidden state. The source counts NPLM’s linear lookup
    and nonlinear hidden computation separately; no forced depth equivalence to DeepFeedForwardNetwork
    or DeepNeuralNetwork is asserted. Perceptron is a binary linear predictor. EmbeddingLayer,
    HiddenLayer, OutputLayer, SoftmaxLayer and ProbabilisticHiddenLayer are components.
    BayesianNetwork and task-scoped ProbabilisticGraphicalModel do not identify these
    parameterizations. Earlier native records provide scope boundaries, not fresh
    approvals.'
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:FactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel
  - AIMech:NeuralProbabilisticLanguageModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - factoredrestrictedboltzmannmachinelanguagemodel-source-0
  - temporalfactoredrestrictedboltzmannmachinelanguagemodel-source-0
  - temporalfactoredrestrictedboltzmannmachinelanguagemodel-source-1
  - neuralprobabilisticlanguagemodel-source-0
  rationale: Static FRBM factorizes context-conditioned latent-word weights; temporal
    FRBM adds uncertain hidden history; the original NPLM uses deterministic nonlinear
    prediction from jointly learned lookup embeddings with separate output parameters.
    Shared word features do not make their latent-state, normalization or learning
    mechanisms equivalent. Broad language-model and related RBM mappings retain those
    distinctions.
limitations:
- Adversarial author self-review only; every target remains DRAFT.
- 'Inspected visual scopes: Mnih2007 pages 1–6, Sutskever2007 pages 1–6, Bengio2003
  pages 1–7. Remaining pages were not certified as read.'
- Mnih2007 uses a verified earlier retrieval; the Sutskever PDF has no printed page
  numbers on inspected pages. Exact hashes and actual PDF-page locators are retained.
- Finite calculations check stated examples and mathematical boundaries, not author
  code, benchmark performance, global convergence or all parameter values.
- 198 pending inspection leads plus unresolved dispositions remain; discovery is active.
links: []
tags:
- native-concepts
- neural-word-models
- self-review
- discovery-ongoing
```
