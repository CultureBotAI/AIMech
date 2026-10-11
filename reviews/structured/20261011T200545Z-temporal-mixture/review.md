# Scientific self-review of hierarchical, mixed-memory and Boltzmann sequence models

- Review: 20261011T200545Z-temporal-mixture
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T20:01:50Z
- Finished UTC: 2026-10-11T20:05:45Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain three DRAFT model families with current-ancestor, mixture-parameterization and energy-graph boundaries. The linear HMM equivalence and IOHMM overlap are explicit. No actionable curation finding remains in the declared scope.

## Scope And Provenance

All fields of three explicitly selected temporal graphical model concepts.

Selection: Three exact maintained IDs in the discovery ledger: HiddenMarkovDecisionTree, MixedMemoryMarkovModel and BoltzmannChain; complete selected cohort, no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 240dbf5bf6f05abd55c9d7819fd7f2f03c46f52b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HiddenMarkovDecisionTree | data/curated/HiddenMarkovDecisionTree.yaml | maintained | Hidden Markov decision tree |
| AIMech:MixedMemoryMarkovModel | data/curated/MixedMemoryMarkovModel.yaml | maintained | Mixed memory Markov model |
| AIMech:BoltzmannChain | data/curated/BoltzmannChain.yaml | maintained | Boltzmann chain |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:HiddenMarkovDecisionTree, AIMech:MixedMemoryMarkovModel, AIMech:BoltzmannChain | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 89.55s (0:01:29)<br>Checked 442 record(s); 0 failed.<br>Checked 382 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 108 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 105,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:HiddenMarkovDecisionTree, AIMech:MixedMemoryMarkovModel, AIMech:BoltzmannChain | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:HiddenMarkovDecisionTree, AIMech:MixedMemoryMarkovModel, AIMech:BoltzmannChain | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:HiddenMarkovDecisionTree, AIMech:MixedMemoryMarkovModel, AIMech:BoltzmannChain | Command exited 0 with no output. |
| Temporal mixture and energy-model boundary calculations | passed | True | AIMech:HiddenMarkovDecisionTree, AIMech:MixedMemoryMarkovModel, AIMech:BoltzmannChain | {"scope": "Original finite fixed-parameter witnesses; not training or universal proofs", "hmdt_joint_mass": 1.0000000000000002, "hmdt_current_ancestor_transition_gap": 0.4, "mixed_memory_additive_contrast": 0.0, "xor_contrast": -2.0, "selector_responsibilities": [0.5894736842105263, 0.41052631578947374], "vector_marginal_dependence": 0.10126249999999998, "joint_count_product_of_marginals_gap": 0.2, "boltzmann_normalizer": 189.54544405729007, "elimination_error": 0.0, "clamped_minus_free_score": 0.028878135645728387, "score_finite_difference_error": 7.384540895438718e-12, "fixed_terminal_equivalence_error": 2.7755575615628914e-17, "unconditioned_endpoint_gap": 0.0031005879335272296, "terminal_reweighting_error": 1.3877787807814457e-17, "naive_local_normalization_gap": 0.029138660423105013} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, source provenance and AIO mapping

evidence: supported. Targets: AIMech:HiddenMarkovDecisionTree.

The Jordan–Ghahramani–Saul model uses probabilistic choices down a hierarchy and Markov persistence within each level. It is not a hard deterministic classification tree, an independent-chain factorial HMM, a tree-shaped index, or a particular variational inference algorithm. Current higher-level decisions influence lower-level decisions; independent factorial chains arise only under additional restrictions. The model conditions on an external input sequence. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 379 preceding native IDs/names/aliases for the four researched candidate names. Both full-checkout fixed-string searches included ignored and hidden files, with 7 and 7 matching lines. All 6 unique matched contents were read: pending leads and preceding source/review context, not existing records of these three new identities. Expanded source IDs, plurals, Gibbs-machine and mixture-transition terminology were included. All 63 semantic label/synonym hits, 17 exact fully annotated AIO CLASS nodes with outgoing edges, their generated YAMLs and six native neighbors were read or byte-verified after prior complete reading. Markov mixtures of experts substantially overlaps the existing IOHMM family, so no fourth ID or unconditional alias is created. Absence is bounded to the pinned vocabulary and inspected neighborhood.

For level m and time t, its latent decision z_t^m is distributed conditional on the current input x_t, all current ancestor decisions z_t^1,...,z_t^(m-1), and its own preceding decision z_(t-1)^m. Initial decisions condition on the input and current ancestors without a preceding-time state. Multiplying these normalized conditional factors and one observation factor p(y_t&#124;x_t,z_t^1,...,z_t^M) per time gives a normalized directed model conditional on inputs. A latent path through the hierarchy selects an output expert. Exact inference may enumerate the joint states but grows exponentially with hierarchy depth. The paper explores three distinct approximations: a product of chain-path distributions that preserves temporal dependence within each level; a product over times of tree-structured distributions that preserves current ancestor dependence; and a point-mass path approximation. Its point-mass procedure optimizes one level’s path by a Viterbi subroutine while holding the other paths fixed. These are inference choices for the family, not alternative definitions of its identity. Limitations: Same-level temporal connections and current-ancestor dependencies are defining restrictions of the inspected construction. They do not cover arbitrary cross-time connections or all models whose names contain hidden Markov tree. The probabilistic hierarchy sums over decision paths; it is not necessarily a hard classification tree. Input conditioning and an output expert do not imply a causal interpretation of the graph. Independent latent chains, a single HMM and an ordinary hierarchical mixture arise under specific restrictions, not as unconditional aliases of this family. Forest-of-chains, forest-of-trees and point-mass inference discard different posterior dependencies. A coordinate Viterbi step finds the best path for one fixed-context chain, not a guaranteed global joint MAP path. The paper motivates hierarchical time scales but its synthetic runs did not always recover the intended hierarchy. No universal coarse-to-fine organization, general convergence guarantee, benchmark advantage or author-code reproduction is asserted. Detailed generic variational updates remain a separate source lead.

### Identity, definition, mechanism, limitations, source provenance and AIO mapping

evidence: supported. Targets: AIMech:MixedMemoryMarkovModel.

This record covers the mixed-memory construction of Saul and Jordan, including higher-order scalar, multicomponent first-order and hidden-state extensions. Mixed memory means a latent selector chooses one predecessor for a component distribution. It does not mean external neural memory, a mixture selecting an entire HMM, independent factorial chains, or an unrestricted full higher-order transition table. EM and coordinate Viterbi are estimation/inference procedures, not aliases for the model. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 379 preceding native IDs/names/aliases for the four researched candidate names. Both full-checkout fixed-string searches included ignored and hidden files, with 7 and 7 matching lines. All 6 unique matched contents were read: pending leads and preceding source/review context, not existing records of these three new identities. Expanded source IDs, plurals, Gibbs-machine and mixture-transition terminology were included. All 63 semantic label/synonym hits, 17 exact fully annotated AIO CLASS nodes with outgoing edges, their generated YAMLs and six native neighbors were read or byte-verified after prior complete reading. Markov mixtures of experts substantially overlaps the existing IOHMM family, so no fourth ID or unconditional alias is created. Absence is bounded to the pinned vocabulary and inspected neighborhood.

For a scalar k-order sequence, write p(i_t&#124;i_(t-1),...,i_(t-k))=sum_mu psi(mu) a_mu(i_t&#124;i_(t-mu)), with nonnegative selector weights summing to one and each transition table normalized over the current state. Given observed predecessor and current values, a selector responsibility is proportional to psi(mu) a_mu(i_t&#124;i_(t-mu)); parameter re-estimation can use these expected selector-weighted counts. For a vector state I_t with components nu, the first-order multicomponent form is p(I_t&#124;I_(t-1))=product_nu sum_mu psi_nu(mu) a_nu,mu(i_t^nu&#124;i_(t-1)^mu). Thus current components are conditionally independent given the complete previous vector, despite possible marginal dependence. The hidden extension uses this transition and an emission p(J_t&#124;I_t)=product_nu sum_mu phi_nu(mu) b_nu,mu(j_t^nu&#124;i_t^mu). Fully observed parameter counts scale quadratically rather than exponentially in the number of components for fixed alphabet size; exact hidden posterior inference can still be exponential. The paper instead illustrates a coordinate Viterbi approximation that fixes other hidden chains while optimizing one chain path. Limitations: A convex sum of single-predecessor effects cannot represent every higher-order interaction; for example an unrestricted XOR dependence on two binary predecessors is not additive in this way. Compact parameter counts do not establish universal expressiveness. The displayed vector transition explicitly assumes conditional independence of current components given the previous vector. The source’s broad wording about avoiding strong conditional-independence assumptions must not override its product factorization. Selector weights are properties of a fitted parameterization, not uniquely identified causal influence or a generally valid measure of correlation. Initial histories and observed-window boundaries must be specified when counting transitions. In the hidden extension, exact EM needs joint posterior expectations of selectors and hidden-state indicator products. Equations (20) and (22) display hidden indicators outside the expectation, which is not a general full-posterior EM formula; clamping a path changes the calculation. Equation (17) also reverses emission arguments relative to Equation (16). Coordinate Viterbi improves or preserves the joint path score under an exact single-chain update, but need not reach global MAP or optimize the marginal observed likelihood. Ties and stopping rules require care. The Bach example illustrates the authors’ approximate procedure. Figure 2 uses joint path log probability, not exact marginal likelihood. No accuracy, causal discovery, training reproduction or general scaling guarantee for hidden inference is curated.

### Identity, definition, mechanism, limitations, source provenance and AIO mapping

evidence: supported. Targets: AIMech:BoltzmannChain.

The Saul–Jordan construction includes a strictly linear categorical chain and specified coupled-parallel or looped variants. It denotes an energy parameterization and temporal graph family, not a sampled Monte Carlo chain, an RBM without hidden-hidden connections, or a generic directed factorial HMM. The linear positive-potential case overlaps HMM distributions under the terminal conditions established by MacKay; different parameter names alone do not establish additional distributional expressiveness. More complex source architectures are not automatically covered by that linear equivalence. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 379 preceding native IDs/names/aliases for the four researched candidate names. Both full-checkout fixed-string searches included ignored and hidden files, with 7 and 7 matching lines. All 6 unique matched contents were read: pending leads and preceding source/review context, not existing records of these three new identities. Expanded source IDs, plurals, Gibbs-machine and mixture-transition terminology were included. All 63 semantic label/synonym hits, 17 exact fully annotated AIO CLASS nodes with outgoing edges, their generated YAMLs and six native neighbors were read or byte-verified after prior complete reading. Markov mixtures of experts substantially overlaps the existing IOHMM family, so no fourth ID or unconditional alias is created. Absence is bounded to the pinned vocabulary and inspected neighborhood.

In the linear categorical case, for fixed length L and inverse temperature beta, assign joint probability proportional to exp(beta[Pi_(s_1)+sum_(t=1)^(L-1) A_(s_t,s_(t+1))+sum_(t=1)^L B_(s_t,y_t)]), normalized over all hidden paths and observation sequences by Z_L. A and B are tied across time and need not themselves be log-normalized transition or emission probabilities. Observed likelihood is the ratio of a clamped and a free partition function. A log-likelihood derivative with respect to a tied interaction is beta times its expected count under the clamped distribution minus its expected count under the free distribution. For the selected tractable graphs, exact variable elimination computes these quantities: pruning sums out leaves, decimation sums over an intermediate state, and parallel interactions combine additively in the energy. The paper uses particular coupled chains at different time resolutions and selected loops that preserve an eliminable structure; tractability depends on intermediate state-space size, not merely the presence of temporal edges. For the strictly linear finite-energy model, a positive eigenvector of the transfer matrix allows interaction weights to be transformed into normalized HMM parameters. A remaining factor depends only on the final hidden state. Conditioning both models on the same fixed terminal state removes that factor from normalized relative probabilities; more complex architectures are outside this equivalence result. Limitations: The model is globally normalized at each sequence length. Separately normalizing each energy table is generally not an equivalent model transformation. MacKay’s positive-matrix gauge transformation produces normalized HMM parameters plus a final-state factor. Equivalence requires the same constrained final state and normalization over that constrained sample space, or explicit handling of the terminal factor. It is not evidence that every unrestricted-terminal HMM and linear energy parameterization agree. The inspected equivalence proof assumes strictly positive transfer entries from finite energies. Reducible or zero-support cases need separate conditions. It does not cover every coupled or looped graph. Exact elimination can become exponential in graph width or state size. The source’s chosen chain/loop motifs do not establish efficient exact inference for arbitrary Boltzmann networks. First-order hidden dynamics can retain long-lag statistical correlations. The source’s wording about absent long-term dependence is not interpreted as zero correlation at all nonadjacent times; extra direct long-range links are a different structural property. The synthetic learning curves do not certify universal gains, real-data effectiveness or scalability. No author implementation, model fitting or benchmark was executed.

### Current hierarchy and temporal persistence

consistency: supported. Targets: AIMech:HiddenMarkovDecisionTree.

Retain HMDT as a hierarchical conditional sequence model.

Current ancestor decisions and same-level previous decisions enter distinct normalized factors. A two-level finite example normalizes over all paths and outputs and has a0.4 ancestor effect, distinguishing it from independent-chain dynamics. Forest-of-chains, forest-of-trees and point-mass methods approximate different posterior structure. Coordinate Viterbi is not global MAP. Markov mixtures of experts substantially overlap the existing IOHMM family with an explicit input-alignment distinction; that context does not warrant a fourth ID or unconditional alias.

### Compact mixtures versus arbitrary transition interactions

consistency: supported. Targets: AIMech:MixedMemoryMarkovModel.

Retain the mixed-memory parameterization and its inference limits.

Selector-weighted single-predecessor transitions are normalized convex mixtures. Their binary interaction contrast is zero, whereas XOR has contrast−2. Current vector components factorize conditionally on the complete preceding vector but can remain marginally dependent, as witnessed by0.1012625 in the finite example. Full hidden EM requires joint latent indicator expectations; a separate correlated-posterior witness gives a0.2 difference from a product of marginals. It is explicitly not claimed as a trained mixed-memory example. Reversed emission arguments and incomplete expected-count displays are qualified; coordinate path objectives and marginal likelihood are distinguished.

### Energy parameterization, exact elimination and endpoint scope

consistency: supported. Targets: AIMech:BoltzmannChain.

Retain the graph family with a qualified linear HMM overlap.

Tied undirected interaction weights, global fixed-length normalization and selected chain-derived graphs define the source family. The score is a clamped-minus-free sufficient-statistic expectation and agrees with finite differences to7.39e−12. MacKay’s positive transfer-matrix transform leaves a terminal-state factor: matched endpoint conditioning agrees to2.78e−17, while an unrestricted endpoint differs by0.00310059. Explicit terminal reweighting restores agreement; naive separate local normalization differs by0.02913866. The preprint is dated1995 and has three pages, not the four-page journal layout. No wider expressiveness follows solely from the energy parameterization, and positive-matrix equivalence does not certify all loopy/reducible cases.

### Model parents versus related tasks and temporal processes

grounding: supported. Targets: AIMech:HiddenMarkovDecisionTree, AIMech:MixedMemoryMarkovModel, AIMech:BoltzmannChain.

Retain the inspected directional AIO mappings.

Seventeen exact fully annotated AIO nodes and all63 semantic label/synonym hits were inspected. Fourteen generated YAMLs were byte-verified after prior full reading and three freshly read. Six native neighbors were read in this or the immediately preceding cohort. HMDT and mixed-memory models are finite directed conditional factorizations with broader BayesianNetwork mappings. HMDT has a related DecisionTree mapping: the AIO target is classification-scoped, while the sequence model need not classify. Mixed-memory models have a related MarkovChain mapping because higher-order scalar and hidden observed processes need not be first-order. Boltzmann chains have a broad BoltzmannMachineNetwork mapping and related MarkovChain association qualified by linear topology and terminal factors. RestrictedBoltzmannMachine lacks the temporal hidden-hidden interactions of the source construction, despite its broad abbreviated definition. ProbabilisticGraphicalModel and MachineLearningTask are task-scoped; TrainingStrategy is preprocessing-scoped. CausalGraphicalModel adds assumptions not supplied by a dependence graph. MixtureofExpertsLLM, MemoryAugmentedLLM, EnergyBasedLLM and ImplicitLanguageModel are language-specific; no generic identity is inferred from related synonyms. MemoryCellLayer and ProbabilisticHiddenLayer are components, not these models. ProbabilisticTopicModel is text/topic-specific. RecurrentNeuralNetwork is not forced as a generic parent of tabular probabilistic models. Native HMM, FHMM, IOHMM, PoHMM, structured FHMM inference and EM distinguish model structures, parameterizations and procedures; their context inspection is not renewed scientific approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:HiddenMarkovDecisionTree, AIMech:MixedMemoryMarkovModel, AIMech:BoltzmannChain. HMDT combines current hierarchical decisions with same-level temporal persistence. Mixed-memory models constrain transition distributions to convex mixtures of single-predecessor effects. Boltzmann chains specify a tied-energy undirected temporal graph family, with a qualified linear overlap with endpoint-conditioned HMMs. These model parameterizations and structures are distinct from their inference/learning procedures. Retain all three records and their explicit directional mappings.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T200108Z-temporal-mixture.json | supports | No normalized identity match was found across all442 pinned AIO labels/scoped synonyms and379 preceding native IDs/names/aliases for the four researched candidate names. Both full-checkout fixed-string searches included ignored and hidden files, with 7 and 7 matching lines. All6 unique matched contents were read: pending leads and preceding source/review context, not existing records of these three new identities. Expanded source IDs, plurals, Gibbs-machine and mixture-transition terminology were included. All63 semantic label/synonym hits,17 exact fully annotated AIO CLASS nodes with outgoing edges, their generated YAMLs and six native neighbors were read or byte-verified after prior complete reading. Markov mixtures of experts substantially overlaps the existing IOHMM family, so no fourth ID or unconditional alias is created. Absence is bounded to the pinned vocabulary and inspected neighborhood. |
| mapping | sources/aio/aio.json; Seventeen exact CLASS nodes with full annotations and outgoing edges in source_analysis.aio_mapping_inspection; corresponding generated records | supports | Seventeen exact fully annotated AIO nodes and all63 semantic label/synonym hits were inspected. Fourteen generated YAMLs were byte-verified after prior full reading and three freshly read. Six native neighbors were read in this or the immediately preceding cohort. HMDT and mixed-memory models are finite directed conditional factorizations with broader BayesianNetwork mappings. HMDT has a related DecisionTree mapping: the AIO target is classification-scoped, while the sequence model need not classify. Mixed-memory models have a related MarkovChain mapping because higher-order scalar and hidden observed processes need not be first-order. Boltzmann chains have a broad BoltzmannMachineNetwork mapping and related MarkovChain association qualified by linear topology and terminal factors. RestrictedBoltzmannMachine lacks the temporal hidden-hidden interactions of the source construction, despite its broad abbreviated definition. ProbabilisticGraphicalModel and MachineLearningTask are task-scoped; TrainingStrategy is preprocessing-scoped. CausalGraphicalModel adds assumptions not supplied by a dependence graph. MixtureofExpertsLLM, MemoryAugmentedLLM, EnergyBasedLLM and ImplicitLanguageModel are language-specific; no generic identity is inferred from related synonyms. MemoryCellLayer and ProbabilisticHiddenLayer are components, not these models. ProbabilisticTopicModel is text/topic-specific. RecurrentNeuralNetwork is not forced as a generic parent of tabular probabilistic models. Native HMM, FHMM, IOHMM, PoHMM, structured FHMM inference and EM distinguish model structures, parameterizations and procedures; their context inspection is not renewed scientific approval. |
| neighbors | research/discovery/20261011T200108Z-temporal-mixture.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Six complete native records were read for boundaries: HMM, FHMM, IOHMM, PoHMM, structured variational inference for FHMMs and EM. They distinguish single-state, factorial, conditional and undirected model families from inference and fitting procedures. This context does not renew scientific approval of older records. |
| finite-conventions | research/discovery/temporal-mixture-boundaries.py; HMDT normalization and current ancestors; mixed-memory interaction restrictions; Boltzmann elimination, score derivatives and endpoint-conditioned HMM equivalence | supports | Original fixed-parameter finite examples normalize a two-level HMDT over all paths and outputs, with a0.4 current-ancestor transition effect. Mixed-memory lag mixtures have zero additive binary interaction contrast while XOR has−2; selector responsibilities normalize. A vector example has conditional component independence but marginal dependence0.1012625. A separate correlated-posterior witness distinguishes joint latent counts from products of marginal expectations by0.2; it is not a trained hidden mixed-memory example. Linear Boltzmann elimination exactly matches the enumerated normalizer189.54544405729007, and clamped-minus-free tied-score derivatives agree with finite differences to7.39e−12. A positive-eigenvector HMM transform agrees after matched terminal conditioning to2.78e−17, while unconstrained endpoints differ by0.00310059. Explicit terminal reweighting agrees to1.39e−17; naive independent local normalization differs by0.02913866. These are bounded mathematical witnesses, not model fitting or universal proofs. |
| mme-overlap | https://proceedings.neurips.cc/paper/1995/file/6c340f25839e6acdc73414517203f5f0-Paper.pdf; Sections2–3, printed1004–1006 / PDF2–4; all seven pages read | supports | The fully read paper Section3 explicitly relates its input-sensitive Markov state and state-specific experts to the Bengio–Frasconi model. Its transition q(t+1)&#124;q(t),u(t) and output y(t)&#124;q(t),u(t) use different input alignment from the maintained IOHMM convention q(t)&#124;q(t-1),u(t). Supplying paired current/previous inputs can represent that factorization within the conditional IOHMM family; this does not justify adding an unconditional exact alias or another generic model ID. The particular robotics parameterization and geometric restrictions remain source context, not a standalone trained-instance record. |
| hiddenmarkovdecisiontree-source-0 | https://proceedings.neurips.cc/paper/1996/file/6c8dba7d0df1c4a79dd07646be9a26c8-Paper.pdf; Sections 2.1–2.3 and Figure 3, printed pp.502–504 / PDF pp.2–4; Sections 3.1–3.4 and Figures 4–5, pp.504–506 / PDF pp.4–6; Sections 4–5 and Table 1, pp.506–507 / PDF pp.6–7 | supports | Hidden Markov Decision Trees. NIPS 1996, Advances in Neural Information Processing Systems 9, proceedings 1997, pp.501–507. All seven publisher PDF pages visually read. Printed page=PDF page+500; first number absent. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |
| mixedmemorymarkovmodel-source-0 | https://proceedings.mlr.press/r1/saul97a/saul97a.pdf; Sections 2–3, Equations (1)–(15), printed pp.438–440 / PDF pp.2–4; Section 4, Equations (16)–(22) and Figures 2–3, pp.440–443 / PDF pp.4–7 | supports | Mixed memory Markov models. AISTATS 1997, pp.437–444; PMLR R1 reissue published 30 March 2021. All eight publisher PDF pages visually read; printed page=PDF page+436. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |
| boltzmannchain-source-0 | https://papers.neurips.cc/paper_files/paper/1994/file/4e0cb6fb5fb446d1c92ede2ed8780188-Paper.pdf; Sections 2.1–2.3, Equations (1)–(5), printed pp.436–438 / PDF pp.2–4; Section 3, Figure 2, pp.438–439 / PDF pp.4–5; Sections 4.1–4.2 and Figures 3–5, pp.439–442 / PDF pp.5–8 | supports | Boltzmann Chains and Hidden Markov Models. NIPS 1994, Advances in Neural Information Processing Systems 7, proceedings 1995, pp.435–442. All eight publisher PDF pages visually read; printed page=PDF page+434; first number absent. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |
| boltzmannchain-source-1 | https://www.inference.org.uk/mackay/jordan.pdf; Abstract and Equations (1)–(4), printed/PDF pp.1–2; positive-matrix proof and terminal pseudo-prior discussion, p.2; architectural scope discussion, p.3 | supports | Equivalence of Linear Boltzmann Chains and Hidden Markov Models. Author preprint dated 31 March 1995, To appear in Neural Computation. All three pages visually read; printed/PDF pages 1–3 agree. Distinct from the four-page1996 journal layout; no byte equivalence is claimed. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |

## Limits And Additional Notes

- Adversarial author self-review only; every target remains DRAFT.
- All33 pages across five downloaded PDFs were visually read, including the seven-page MME overlap source and three-page MacKay preprint. Conversion manifests alone do not attest reading.
- Some web/publisher access attempts failed. The author archive supplied the preprint legitimately; the journal layout was not inspected and no access control was bypassed.
- Source equation errors, conditional independence, approximate path inference and terminal conditions are qualified. Finite arithmetic is not model fitting, author-code execution or a universal proof.
- The initial history command failed due to unsupported option spellings and created no file. A corrected canonical invocation saved the actual curation event before history validation.
- 210 pending leads plus unresolved dispositions remain; discovery is active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T200545Z-temporal-mixture
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of hierarchical, mixed-memory and Boltzmann sequence
  models
started_at: '2026-10-11T20:01:50Z'
finished_at: '2026-10-11T20:05:45Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all fields of three
    new records against four complete proceedings PDFs and one complete author preprint,
    totaling33 visually read pages. Seventeen fully annotated AIO nodes and six native
    neighbors establish the inspected boundaries. Original fixed-probability examples
    check normalization, interaction restrictions, exact elimination, score identities
    and endpoint-conditioned equivalence. This is author self-review, not independent
    approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain three DRAFT model families with current-ancestor, mixture-parameterization
  and energy-graph boundaries. The linear HMM equivalence and IOHMM overlap are explicit.
  No actionable curation finding remains in the declared scope.
source:
  git_revision: 240dbf5bf6f05abd55c9d7819fd7f2f03c46f52b
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/BoltzmannMachineNetwork.yaml
    sha256: 1152d2d85c5c1c408a0420e13f211ed109b12fb289c706ee7449864e91aece03
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/DecisionTree.yaml
    sha256: 4c2a5ed08c585f8912d66e3629aaa20e93c46ab49cfb2d128001fcd019c81bfc
    role: context
  - path: data/aio/EnergyBasedLLM.yaml
    sha256: e9e29aa4f8400ad463dfe058fade876ef36c4a2637e1ebc4b42688116896310b
    role: context
  - path: data/aio/ImplicitLanguageModel.yaml
    sha256: 818c396b19757360dcdff6291a85d589c50638e0dc6d6bfcd96fdcb7bdf46ce9
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/MemoryAugmentedLLM.yaml
    sha256: 8727073cb355b965f54a2f0e58997f862f6b734c9143511008c26f9d31a965fd
    role: context
  - path: data/aio/MemoryCellLayer.yaml
    sha256: 290f04d7838e185381b29b22e67f8765de74242d687d23b0ffae2dad9d3f7237
    role: context
  - path: data/aio/MixtureofExpertsLLM.yaml
    sha256: d9c3edb18f624102f141d1daf27aa0cc055eaf9199faf30abf88d2b87fbc1520
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ProbabilisticHiddenLayer.yaml
    sha256: 610c29db815f7348c5bdcdc7e7460dd2dea9ea338f3727ebb1596c51b4af41da
    role: context
  - path: data/aio/ProbabilisticTopicModel.yaml
    sha256: a3ddfd23b511de967f562e99542d8a89109852359d286a4d707d784359ddfe32
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/aio/RestrictedBoltzmannMachine.yaml
    sha256: 322fcb3b1f6064d944379ed79ffdcb7360fc2c3edd300c0a5a3f46be1f48df43
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/BoltzmannChain.yaml
    sha256: 44e66487c4e82b9879fc7bef759ac15be42e3fcb13c9be7621e366f5aec933b4
    role: target
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: context
  - path: data/curated/FactorialHiddenMarkovModel.yaml
    sha256: f1474c3cbb78b2097ad6275f51c61291dfd1a11515df0e7ef56270c30ec4f68d
    role: context
  - path: data/curated/HiddenMarkovDecisionTree.yaml
    sha256: ee90a9296d1f3fa33b29c2f0160ae5b5d54787c02893fea2cbd516e6db535d18
    role: target
  - path: data/curated/HiddenMarkovModel.yaml
    sha256: 062a31bd525cb90e8077d4889c177f55cb7b29dea4e71c33be95bae9e72a5240
    role: context
  - path: data/curated/InputOutputHiddenMarkovModel.yaml
    sha256: 0b0273f47026fed64472356d1610aa2384e8bf89eecfafa109d07f5e8bcd3acf
    role: context
  - path: data/curated/MixedMemoryMarkovModel.yaml
    sha256: 3d85215830d8e12bae4b29ae645412aff678693cb56eb639dc93860d6baaed86
    role: target
  - path: data/curated/ProductOfHiddenMarkovModels.yaml
    sha256: 51fdf99954e91afb1d0ddda78bd60dc98991847715c2f1fe9ef2be4a7f46436e
    role: context
  - path: data/curated/StructuredVariationalInferenceForFactorialHMMs.yaml
    sha256: 236f080993e164f5768f1eb1a179ff3589b03344cf133091fea5d35cc3ce4918
    role: context
  - path: research/discovery/20261011T200108Z-temporal-mixture.json
    sha256: b768f048455c21544509d9529ebd467d8a5e19a16bbbd128ae13f6bd82a7a8e5
    role: context
  - path: research/discovery/temporal-mixture-boundaries.py
    sha256: d8be81f8a821785eedbf57592c798d77e4f8389084ab658f40c49138e947c0dd
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
- target_id: AIMech:HiddenMarkovDecisionTree
  path: data/curated/HiddenMarkovDecisionTree.yaml
  label: Hidden Markov decision tree
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HiddenMarkovDecisionTree.yaml
    role: maintained
- target_id: AIMech:MixedMemoryMarkovModel
  path: data/curated/MixedMemoryMarkovModel.yaml
  label: Mixed memory Markov model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MixedMemoryMarkovModel.yaml
    role: maintained
- target_id: AIMech:BoltzmannChain
  path: data/curated/BoltzmannChain.yaml
  label: Boltzmann chain
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BoltzmannChain.yaml
    role: maintained
scope:
  description: All fields of three explicitly selected temporal graphical model concepts.
  selection: 'Three exact maintained IDs in the discovery ledger: HiddenMarkovDecisionTree,
    MixedMemoryMarkovModel and BoltzmannChain; complete selected cohort, no sampling.'
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:HiddenMarkovDecisionTree
  - AIMech:MixedMemoryMarkovModel
  - AIMech:BoltzmannChain
  exclusions:
  - target: Author implementations, empirical performance and general convergence
      guarantees
    reason: Primary model definitions and finite witnesses do not certify author-code
      behavior, benchmarks or universal optimization results.
  - target: Prior records and remaining source leads
    reason: Six older records provide identity context without renewed scientific
      approval. Generic coupled models, controller mixtures, general structured inference
      and newly cited architectures remain unresolved.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:HiddenMarkovDecisionTree
  - AIMech:MixedMemoryMarkovModel
  - AIMech:BoltzmannChain
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 89.55s (0:01:29)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 382 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 108 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 105,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:HiddenMarkovDecisionTree
  - AIMech:MixedMemoryMarkovModel
  - AIMech:BoltzmannChain
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
  - AIMech:HiddenMarkovDecisionTree
  - AIMech:MixedMemoryMarkovModel
  - AIMech:BoltzmannChain
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
  - AIMech:HiddenMarkovDecisionTree
  - AIMech:MixedMemoryMarkovModel
  - AIMech:BoltzmannChain
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Temporal mixture and energy-model boundary calculations
  command: python3 research/discovery/temporal-mixture-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:HiddenMarkovDecisionTree
  - AIMech:MixedMemoryMarkovModel
  - AIMech:BoltzmannChain
  exit_code: 0
  expected_exit_code: 0
  summary: '{"scope": "Original finite fixed-parameter witnesses; not training or
    universal proofs", "hmdt_joint_mass": 1.0000000000000002, "hmdt_current_ancestor_transition_gap":
    0.4, "mixed_memory_additive_contrast": 0.0, "xor_contrast": -2.0, "selector_responsibilities":
    [0.5894736842105263, 0.41052631578947374], "vector_marginal_dependence": 0.10126249999999998,
    "joint_count_product_of_marginals_gap": 0.2, "boltzmann_normalizer": 189.54544405729007,
    "elimination_error": 0.0, "clamped_minus_free_score": 0.028878135645728387, "score_finite_difference_error":
    7.384540895438718e-12, "fixed_terminal_equivalence_error": 2.7755575615628914e-17,
    "unconditioned_endpoint_gap": 0.0031005879335272296, "terminal_reweighting_error":
    1.3877787807814457e-17, "naive_local_normalization_gap": 0.029138660423105013}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T200108Z-temporal-mixture.json
  accessed_at: '2026-10-11T20:01:50Z'
  support: supports
  summary: 'No normalized identity match was found across all442 pinned AIO labels/scoped
    synonyms and379 preceding native IDs/names/aliases for the four researched candidate
    names. Both full-checkout fixed-string searches included ignored and hidden files,
    with 7 and 7 matching lines. All6 unique matched contents were read: pending leads
    and preceding source/review context, not existing records of these three new identities.
    Expanded source IDs, plurals, Gibbs-machine and mixture-transition terminology
    were included. All63 semantic label/synonym hits,17 exact fully annotated AIO
    CLASS nodes with outgoing edges, their generated YAMLs and six native neighbors
    were read or byte-verified after prior complete reading. Markov mixtures of experts
    substantially overlaps the existing IOHMM family, so no fourth ID or unconditional
    alias is created. Absence is bounded to the pinned vocabulary and inspected neighborhood.'
  search_scope: 'No normalized identity match was found across all442 pinned AIO labels/scoped
    synonyms and379 preceding native IDs/names/aliases for the four researched candidate
    names. Both full-checkout fixed-string searches included ignored and hidden files,
    with 7 and 7 matching lines. All6 unique matched contents were read: pending leads
    and preceding source/review context, not existing records of these three new identities.
    Expanded source IDs, plurals, Gibbs-machine and mixture-transition terminology
    were included. All63 semantic label/synonym hits,17 exact fully annotated AIO
    CLASS nodes with outgoing edges, their generated YAMLs and six native neighbors
    were read or byte-verified after prior complete reading. Markov mixtures of experts
    substantially overlaps the existing IOHMM family, so no fourth ID or unconditional
    alias is created. Absence is bounded to the pinned vocabulary and inspected neighborhood.'
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Seventeen exact CLASS nodes with full annotations and outgoing edges in
    source_analysis.aio_mapping_inspection; corresponding generated records
  accessed_at: '2026-10-11T20:01:50Z'
  support: supports
  summary: 'Seventeen exact fully annotated AIO nodes and all63 semantic label/synonym
    hits were inspected. Fourteen generated YAMLs were byte-verified after prior full
    reading and three freshly read. Six native neighbors were read in this or the
    immediately preceding cohort. HMDT and mixed-memory models are finite directed
    conditional factorizations with broader BayesianNetwork mappings. HMDT has a related
    DecisionTree mapping: the AIO target is classification-scoped, while the sequence
    model need not classify. Mixed-memory models have a related MarkovChain mapping
    because higher-order scalar and hidden observed processes need not be first-order.
    Boltzmann chains have a broad BoltzmannMachineNetwork mapping and related MarkovChain
    association qualified by linear topology and terminal factors. RestrictedBoltzmannMachine
    lacks the temporal hidden-hidden interactions of the source construction, despite
    its broad abbreviated definition. ProbabilisticGraphicalModel and MachineLearningTask
    are task-scoped; TrainingStrategy is preprocessing-scoped. CausalGraphicalModel
    adds assumptions not supplied by a dependence graph. MixtureofExpertsLLM, MemoryAugmentedLLM,
    EnergyBasedLLM and ImplicitLanguageModel are language-specific; no generic identity
    is inferred from related synonyms. MemoryCellLayer and ProbabilisticHiddenLayer
    are components, not these models. ProbabilisticTopicModel is text/topic-specific.
    RecurrentNeuralNetwork is not forced as a generic parent of tabular probabilistic
    models. Native HMM, FHMM, IOHMM, PoHMM, structured FHMM inference and EM distinguish
    model structures, parameterizations and procedures; their context inspection is
    not renewed scientific approval.'
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T200108Z-temporal-mixture.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T20:01:50Z'
  support: supports
  summary: 'Six complete native records were read for boundaries: HMM, FHMM, IOHMM,
    PoHMM, structured variational inference for FHMMs and EM. They distinguish single-state,
    factorial, conditional and undirected model families from inference and fitting
    procedures. This context does not renew scientific approval of older records.'
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/temporal-mixture-boundaries.py
  locator: HMDT normalization and current ancestors; mixed-memory interaction restrictions;
    Boltzmann elimination, score derivatives and endpoint-conditioned HMM equivalence
  accessed_at: '2026-10-11T20:01:50Z'
  snapshot_sha256: d8be81f8a821785eedbf57592c798d77e4f8389084ab658f40c49138e947c0dd
  support: supports
  summary: Original fixed-parameter finite examples normalize a two-level HMDT over
    all paths and outputs, with a0.4 current-ancestor transition effect. Mixed-memory
    lag mixtures have zero additive binary interaction contrast while XOR has−2; selector
    responsibilities normalize. A vector example has conditional component independence
    but marginal dependence0.1012625. A separate correlated-posterior witness distinguishes
    joint latent counts from products of marginal expectations by0.2; it is not a
    trained hidden mixed-memory example. Linear Boltzmann elimination exactly matches
    the enumerated normalizer189.54544405729007, and clamped-minus-free tied-score
    derivatives agree with finite differences to7.39e−12. A positive-eigenvector HMM
    transform agrees after matched terminal conditioning to2.78e−17, while unconstrained
    endpoints differ by0.00310059. Explicit terminal reweighting agrees to1.39e−17;
    naive independent local normalization differs by0.02913866. These are bounded
    mathematical witnesses, not model fitting or universal proofs.
- evidence_id: mme-overlap
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper/1995/file/6c340f25839e6acdc73414517203f5f0-Paper.pdf
  locator: Sections2–3, printed1004–1006 / PDF2–4; all seven pages read
  accessed_at: '2026-10-11T19:46:53Z'
  snapshot_sha256: 810a8ade7644f3d7f8354b2236e2a836dd1f46b079f22d2754677dc38c139ce4
  support: supports
  summary: The fully read paper Section3 explicitly relates its input-sensitive Markov
    state and state-specific experts to the Bengio–Frasconi model. Its transition
    q(t+1)|q(t),u(t) and output y(t)|q(t),u(t) use different input alignment from
    the maintained IOHMM convention q(t)|q(t-1),u(t). Supplying paired current/previous
    inputs can represent that factorization within the conditional IOHMM family; this
    does not justify adding an unconditional exact alias or another generic model
    ID. The particular robotics parameterization and geometric restrictions remain
    source context, not a standalone trained-instance record.
- evidence_id: hiddenmarkovdecisiontree-source-0
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper/1996/file/6c8dba7d0df1c4a79dd07646be9a26c8-Paper.pdf
  locator: Sections 2.1–2.3 and Figure 3, printed pp.502–504 / PDF pp.2–4; Sections
    3.1–3.4 and Figures 4–5, pp.504–506 / PDF pp.4–6; Sections 4–5 and Table 1, pp.506–507
    / PDF pp.6–7
  accessed_at: '2026-10-11T19:46:51Z'
  snapshot_sha256: e073f1c78b487af707dece286f368179800c0a52a709ac98e425270836d7b02e
  support: supports
  summary: Hidden Markov Decision Trees. NIPS 1996, Advances in Neural Information
    Processing Systems 9, proceedings 1997, pp.501–507. All seven publisher PDF pages
    visually read. Printed page=PDF page+500; first number absent. Actual visual reading
    scopes are declared in the ledger; retrieval and conversion do not certify reading
    of other pages.
- evidence_id: mixedmemorymarkovmodel-source-0
  kind: primary_source
  reference: https://proceedings.mlr.press/r1/saul97a/saul97a.pdf
  locator: Sections 2–3, Equations (1)–(15), printed pp.438–440 / PDF pp.2–4; Section
    4, Equations (16)–(22) and Figures 2–3, pp.440–443 / PDF pp.4–7
  accessed_at: '2026-10-11T19:46:55Z'
  snapshot_sha256: a38f538362eff8bfb9087d36eab5dea0ac4ccb43a72acd862517914af8e1926a
  support: supports
  summary: Mixed memory Markov models. AISTATS 1997, pp.437–444; PMLR R1 reissue published
    30 March 2021. All eight publisher PDF pages visually read; printed page=PDF page+436.
    Actual visual reading scopes are declared in the ledger; retrieval and conversion
    do not certify reading of other pages.
- evidence_id: boltzmannchain-source-0
  kind: primary_source
  reference: https://papers.neurips.cc/paper_files/paper/1994/file/4e0cb6fb5fb446d1c92ede2ed8780188-Paper.pdf
  locator: Sections 2.1–2.3, Equations (1)–(5), printed pp.436–438 / PDF pp.2–4; Section
    3, Figure 2, pp.438–439 / PDF pp.4–5; Sections 4.1–4.2 and Figures 3–5, pp.439–442
    / PDF pp.5–8
  accessed_at: '2026-10-11T19:47:00Z'
  snapshot_sha256: 583d728c7adf54d75566445c06aa50f0a1ce1b60b203cc5bce68b9e72042bc70
  support: supports
  summary: Boltzmann Chains and Hidden Markov Models. NIPS 1994, Advances in Neural
    Information Processing Systems 7, proceedings 1995, pp.435–442. All eight publisher
    PDF pages visually read; printed page=PDF page+434; first number absent. Actual
    visual reading scopes are declared in the ledger; retrieval and conversion do
    not certify reading of other pages.
- evidence_id: boltzmannchain-source-1
  kind: primary_source
  reference: https://www.inference.org.uk/mackay/jordan.pdf
  locator: Abstract and Equations (1)–(4), printed/PDF pp.1–2; positive-matrix proof
    and terminal pseudo-prior discussion, p.2; architectural scope discussion, p.3
  accessed_at: '2026-10-11T19:56:20Z'
  snapshot_sha256: 30728362614b58a68e9f386bdcc9fc4b16c7b0e0847bd7608b00ea008afa25fa
  support: supports
  summary: Equivalence of Linear Boltzmann Chains and Hidden Markov Models. Author
    preprint dated 31 March 1995, To appear in Neural Computation. All three pages
    visually read; printed/PDF pages 1–3 agree. Distinct from the four-page1996 journal
    layout; no byte equivalence is claimed. Actual visual reading scopes are declared
    in the ledger; retrieval and conversion do not certify reading of other pages.
assessments:
- assessment_id: hiddenmarkovdecisiontree
  area: evidence
  topic: Identity, definition, mechanism, limitations, source provenance and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:HiddenMarkovDecisionTree
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - hiddenmarkovdecisiontree-source-0
  summary: 'The Jordan–Ghahramani–Saul model uses probabilistic choices down a hierarchy
    and Markov persistence within each level. It is not a hard deterministic classification
    tree, an independent-chain factorial HMM, a tree-shaped index, or a particular
    variational inference algorithm. Current higher-level decisions influence lower-level
    decisions; independent factorial chains arise only under additional restrictions.
    The model conditions on an external input sequence. No normalized identity match
    was found across all 442 pinned AIO labels/scoped synonyms and 379 preceding native
    IDs/names/aliases for the four researched candidate names. Both full-checkout
    fixed-string searches included ignored and hidden files, with 7 and 7 matching
    lines. All 6 unique matched contents were read: pending leads and preceding source/review
    context, not existing records of these three new identities. Expanded source IDs,
    plurals, Gibbs-machine and mixture-transition terminology were included. All 63
    semantic label/synonym hits, 17 exact fully annotated AIO CLASS nodes with outgoing
    edges, their generated YAMLs and six native neighbors were read or byte-verified
    after prior complete reading. Markov mixtures of experts substantially overlaps
    the existing IOHMM family, so no fourth ID or unconditional alias is created.
    Absence is bounded to the pinned vocabulary and inspected neighborhood.'
  details: 'For level m and time t, its latent decision z_t^m is distributed conditional
    on the current input x_t, all current ancestor decisions z_t^1,...,z_t^(m-1),
    and its own preceding decision z_(t-1)^m. Initial decisions condition on the input
    and current ancestors without a preceding-time state. Multiplying these normalized
    conditional factors and one observation factor p(y_t|x_t,z_t^1,...,z_t^M) per
    time gives a normalized directed model conditional on inputs. A latent path through
    the hierarchy selects an output expert. Exact inference may enumerate the joint
    states but grows exponentially with hierarchy depth. The paper explores three
    distinct approximations: a product of chain-path distributions that preserves
    temporal dependence within each level; a product over times of tree-structured
    distributions that preserves current ancestor dependence; and a point-mass path
    approximation. Its point-mass procedure optimizes one level’s path by a Viterbi
    subroutine while holding the other paths fixed. These are inference choices for
    the family, not alternative definitions of its identity. Limitations: Same-level
    temporal connections and current-ancestor dependencies are defining restrictions
    of the inspected construction. They do not cover arbitrary cross-time connections
    or all models whose names contain hidden Markov tree. The probabilistic hierarchy
    sums over decision paths; it is not necessarily a hard classification tree. Input
    conditioning and an output expert do not imply a causal interpretation of the
    graph. Independent latent chains, a single HMM and an ordinary hierarchical mixture
    arise under specific restrictions, not as unconditional aliases of this family.
    Forest-of-chains, forest-of-trees and point-mass inference discard different posterior
    dependencies. A coordinate Viterbi step finds the best path for one fixed-context
    chain, not a guaranteed global joint MAP path. The paper motivates hierarchical
    time scales but its synthetic runs did not always recover the intended hierarchy.
    No universal coarse-to-fine organization, general convergence guarantee, benchmark
    advantage or author-code reproduction is asserted. Detailed generic variational
    updates remain a separate source lead.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: Three temporal model families, distinguished from inference/learning
      algorithms, classification tasks, component processes and unrestricted parameterizations.
    evidence_ids:
    - hiddenmarkovdecisiontree-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: 'Seventeen exact fully annotated AIO nodes and all63 semantic label/synonym
      hits were inspected. Fourteen generated YAMLs were byte-verified after prior
      full reading and three freshly read. Six native neighbors were read in this
      or the immediately preceding cohort. HMDT and mixed-memory models are finite
      directed conditional factorizations with broader BayesianNetwork mappings. HMDT
      has a related DecisionTree mapping: the AIO target is classification-scoped,
      while the sequence model need not classify. Mixed-memory models have a related
      MarkovChain mapping because higher-order scalar and hidden observed processes
      need not be first-order. Boltzmann chains have a broad BoltzmannMachineNetwork
      mapping and related MarkovChain association qualified by linear topology and
      terminal factors. RestrictedBoltzmannMachine lacks the temporal hidden-hidden
      interactions of the source construction, despite its broad abbreviated definition.
      ProbabilisticGraphicalModel and MachineLearningTask are task-scoped; TrainingStrategy
      is preprocessing-scoped. CausalGraphicalModel adds assumptions not supplied
      by a dependence graph. MixtureofExpertsLLM, MemoryAugmentedLLM, EnergyBasedLLM
      and ImplicitLanguageModel are language-specific; no generic identity is inferred
      from related synonyms. MemoryCellLayer and ProbabilisticHiddenLayer are components,
      not these models. ProbabilisticTopicModel is text/topic-specific. RecurrentNeuralNetwork
      is not forced as a generic parent of tabular probabilistic models. Native HMM,
      FHMM, IOHMM, PoHMM, structured FHMM inference and EM distinguish model structures,
      parameterizations and procedures; their context inspection is not renewed scientific
      approval.'
    evidence_ids:
    - mapping
- assessment_id: mixedmemorymarkovmodel
  area: evidence
  topic: Identity, definition, mechanism, limitations, source provenance and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:MixedMemoryMarkovModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - mixedmemorymarkovmodel-source-0
  summary: 'This record covers the mixed-memory construction of Saul and Jordan, including
    higher-order scalar, multicomponent first-order and hidden-state extensions. Mixed
    memory means a latent selector chooses one predecessor for a component distribution.
    It does not mean external neural memory, a mixture selecting an entire HMM, independent
    factorial chains, or an unrestricted full higher-order transition table. EM and
    coordinate Viterbi are estimation/inference procedures, not aliases for the model.
    No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 379 preceding native IDs/names/aliases for the four researched candidate
    names. Both full-checkout fixed-string searches included ignored and hidden files,
    with 7 and 7 matching lines. All 6 unique matched contents were read: pending
    leads and preceding source/review context, not existing records of these three
    new identities. Expanded source IDs, plurals, Gibbs-machine and mixture-transition
    terminology were included. All 63 semantic label/synonym hits, 17 exact fully
    annotated AIO CLASS nodes with outgoing edges, their generated YAMLs and six native
    neighbors were read or byte-verified after prior complete reading. Markov mixtures
    of experts substantially overlaps the existing IOHMM family, so no fourth ID or
    unconditional alias is created. Absence is bounded to the pinned vocabulary and
    inspected neighborhood.'
  details: 'For a scalar k-order sequence, write p(i_t|i_(t-1),...,i_(t-k))=sum_mu
    psi(mu) a_mu(i_t|i_(t-mu)), with nonnegative selector weights summing to one and
    each transition table normalized over the current state. Given observed predecessor
    and current values, a selector responsibility is proportional to psi(mu) a_mu(i_t|i_(t-mu));
    parameter re-estimation can use these expected selector-weighted counts. For a
    vector state I_t with components nu, the first-order multicomponent form is p(I_t|I_(t-1))=product_nu
    sum_mu psi_nu(mu) a_nu,mu(i_t^nu|i_(t-1)^mu). Thus current components are conditionally
    independent given the complete previous vector, despite possible marginal dependence.
    The hidden extension uses this transition and an emission p(J_t|I_t)=product_nu
    sum_mu phi_nu(mu) b_nu,mu(j_t^nu|i_t^mu). Fully observed parameter counts scale
    quadratically rather than exponentially in the number of components for fixed
    alphabet size; exact hidden posterior inference can still be exponential. The
    paper instead illustrates a coordinate Viterbi approximation that fixes other
    hidden chains while optimizing one chain path. Limitations: A convex sum of single-predecessor
    effects cannot represent every higher-order interaction; for example an unrestricted
    XOR dependence on two binary predecessors is not additive in this way. Compact
    parameter counts do not establish universal expressiveness. The displayed vector
    transition explicitly assumes conditional independence of current components given
    the previous vector. The source’s broad wording about avoiding strong conditional-independence
    assumptions must not override its product factorization. Selector weights are
    properties of a fitted parameterization, not uniquely identified causal influence
    or a generally valid measure of correlation. Initial histories and observed-window
    boundaries must be specified when counting transitions. In the hidden extension,
    exact EM needs joint posterior expectations of selectors and hidden-state indicator
    products. Equations (20) and (22) display hidden indicators outside the expectation,
    which is not a general full-posterior EM formula; clamping a path changes the
    calculation. Equation (17) also reverses emission arguments relative to Equation
    (16). Coordinate Viterbi improves or preserves the joint path score under an exact
    single-chain update, but need not reach global MAP or optimize the marginal observed
    likelihood. Ties and stopping rules require care. The Bach example illustrates
    the authors’ approximate procedure. Figure 2 uses joint path log probability,
    not exact marginal likelihood. No accuracy, causal discovery, training reproduction
    or general scaling guarantee for hidden inference is curated.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: Three temporal model families, distinguished from inference/learning
      algorithms, classification tasks, component processes and unrestricted parameterizations.
    evidence_ids:
    - mixedmemorymarkovmodel-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: 'Seventeen exact fully annotated AIO nodes and all63 semantic label/synonym
      hits were inspected. Fourteen generated YAMLs were byte-verified after prior
      full reading and three freshly read. Six native neighbors were read in this
      or the immediately preceding cohort. HMDT and mixed-memory models are finite
      directed conditional factorizations with broader BayesianNetwork mappings. HMDT
      has a related DecisionTree mapping: the AIO target is classification-scoped,
      while the sequence model need not classify. Mixed-memory models have a related
      MarkovChain mapping because higher-order scalar and hidden observed processes
      need not be first-order. Boltzmann chains have a broad BoltzmannMachineNetwork
      mapping and related MarkovChain association qualified by linear topology and
      terminal factors. RestrictedBoltzmannMachine lacks the temporal hidden-hidden
      interactions of the source construction, despite its broad abbreviated definition.
      ProbabilisticGraphicalModel and MachineLearningTask are task-scoped; TrainingStrategy
      is preprocessing-scoped. CausalGraphicalModel adds assumptions not supplied
      by a dependence graph. MixtureofExpertsLLM, MemoryAugmentedLLM, EnergyBasedLLM
      and ImplicitLanguageModel are language-specific; no generic identity is inferred
      from related synonyms. MemoryCellLayer and ProbabilisticHiddenLayer are components,
      not these models. ProbabilisticTopicModel is text/topic-specific. RecurrentNeuralNetwork
      is not forced as a generic parent of tabular probabilistic models. Native HMM,
      FHMM, IOHMM, PoHMM, structured FHMM inference and EM distinguish model structures,
      parameterizations and procedures; their context inspection is not renewed scientific
      approval.'
    evidence_ids:
    - mapping
- assessment_id: boltzmannchain
  area: evidence
  topic: Identity, definition, mechanism, limitations, source provenance and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:BoltzmannChain
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - boltzmannchain-source-0
  - boltzmannchain-source-1
  summary: 'The Saul–Jordan construction includes a strictly linear categorical chain
    and specified coupled-parallel or looped variants. It denotes an energy parameterization
    and temporal graph family, not a sampled Monte Carlo chain, an RBM without hidden-hidden
    connections, or a generic directed factorial HMM. The linear positive-potential
    case overlaps HMM distributions under the terminal conditions established by MacKay;
    different parameter names alone do not establish additional distributional expressiveness.
    More complex source architectures are not automatically covered by that linear
    equivalence. No normalized identity match was found across all 442 pinned AIO
    labels/scoped synonyms and 379 preceding native IDs/names/aliases for the four
    researched candidate names. Both full-checkout fixed-string searches included
    ignored and hidden files, with 7 and 7 matching lines. All 6 unique matched contents
    were read: pending leads and preceding source/review context, not existing records
    of these three new identities. Expanded source IDs, plurals, Gibbs-machine and
    mixture-transition terminology were included. All 63 semantic label/synonym hits,
    17 exact fully annotated AIO CLASS nodes with outgoing edges, their generated
    YAMLs and six native neighbors were read or byte-verified after prior complete
    reading. Markov mixtures of experts substantially overlaps the existing IOHMM
    family, so no fourth ID or unconditional alias is created. Absence is bounded
    to the pinned vocabulary and inspected neighborhood.'
  details: 'In the linear categorical case, for fixed length L and inverse temperature
    beta, assign joint probability proportional to exp(beta[Pi_(s_1)+sum_(t=1)^(L-1)
    A_(s_t,s_(t+1))+sum_(t=1)^L B_(s_t,y_t)]), normalized over all hidden paths and
    observation sequences by Z_L. A and B are tied across time and need not themselves
    be log-normalized transition or emission probabilities. Observed likelihood is
    the ratio of a clamped and a free partition function. A log-likelihood derivative
    with respect to a tied interaction is beta times its expected count under the
    clamped distribution minus its expected count under the free distribution. For
    the selected tractable graphs, exact variable elimination computes these quantities:
    pruning sums out leaves, decimation sums over an intermediate state, and parallel
    interactions combine additively in the energy. The paper uses particular coupled
    chains at different time resolutions and selected loops that preserve an eliminable
    structure; tractability depends on intermediate state-space size, not merely the
    presence of temporal edges. For the strictly linear finite-energy model, a positive
    eigenvector of the transfer matrix allows interaction weights to be transformed
    into normalized HMM parameters. A remaining factor depends only on the final hidden
    state. Conditioning both models on the same fixed terminal state removes that
    factor from normalized relative probabilities; more complex architectures are
    outside this equivalence result. Limitations: The model is globally normalized
    at each sequence length. Separately normalizing each energy table is generally
    not an equivalent model transformation. MacKay’s positive-matrix gauge transformation
    produces normalized HMM parameters plus a final-state factor. Equivalence requires
    the same constrained final state and normalization over that constrained sample
    space, or explicit handling of the terminal factor. It is not evidence that every
    unrestricted-terminal HMM and linear energy parameterization agree. The inspected
    equivalence proof assumes strictly positive transfer entries from finite energies.
    Reducible or zero-support cases need separate conditions. It does not cover every
    coupled or looped graph. Exact elimination can become exponential in graph width
    or state size. The source’s chosen chain/loop motifs do not establish efficient
    exact inference for arbitrary Boltzmann networks. First-order hidden dynamics
    can retain long-lag statistical correlations. The source’s wording about absent
    long-term dependence is not interpreted as zero correlation at all nonadjacent
    times; extra direct long-range links are a different structural property. The
    synthetic learning curves do not certify universal gains, real-data effectiveness
    or scalability. No author implementation, model fitting or benchmark was executed.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: Three temporal model families, distinguished from inference/learning
      algorithms, classification tasks, component processes and unrestricted parameterizations.
    evidence_ids:
    - boltzmannchain-source-0
    - boltzmannchain-source-1
  - name: aio-assessment
    value: broad_match,related_match
    definition: 'Seventeen exact fully annotated AIO nodes and all63 semantic label/synonym
      hits were inspected. Fourteen generated YAMLs were byte-verified after prior
      full reading and three freshly read. Six native neighbors were read in this
      or the immediately preceding cohort. HMDT and mixed-memory models are finite
      directed conditional factorizations with broader BayesianNetwork mappings. HMDT
      has a related DecisionTree mapping: the AIO target is classification-scoped,
      while the sequence model need not classify. Mixed-memory models have a related
      MarkovChain mapping because higher-order scalar and hidden observed processes
      need not be first-order. Boltzmann chains have a broad BoltzmannMachineNetwork
      mapping and related MarkovChain association qualified by linear topology and
      terminal factors. RestrictedBoltzmannMachine lacks the temporal hidden-hidden
      interactions of the source construction, despite its broad abbreviated definition.
      ProbabilisticGraphicalModel and MachineLearningTask are task-scoped; TrainingStrategy
      is preprocessing-scoped. CausalGraphicalModel adds assumptions not supplied
      by a dependence graph. MixtureofExpertsLLM, MemoryAugmentedLLM, EnergyBasedLLM
      and ImplicitLanguageModel are language-specific; no generic identity is inferred
      from related synonyms. MemoryCellLayer and ProbabilisticHiddenLayer are components,
      not these models. ProbabilisticTopicModel is text/topic-specific. RecurrentNeuralNetwork
      is not forced as a generic parent of tabular probabilistic models. Native HMM,
      FHMM, IOHMM, PoHMM, structured FHMM inference and EM distinguish model structures,
      parameterizations and procedures; their context inspection is not renewed scientific
      approval.'
    evidence_ids:
    - mapping
- assessment_id: hierarchical-decisions
  area: consistency
  topic: Current hierarchy and temporal persistence
  outcome: supported
  target_ids:
  - AIMech:HiddenMarkovDecisionTree
  evidence_ids:
  - hiddenmarkovdecisiontree-source-0
  - finite-conventions
  - neighbors
  - mme-overlap
  summary: Retain HMDT as a hierarchical conditional sequence model.
  details: Current ancestor decisions and same-level previous decisions enter distinct
    normalized factors. A two-level finite example normalizes over all paths and outputs
    and has a0.4 ancestor effect, distinguishing it from independent-chain dynamics.
    Forest-of-chains, forest-of-trees and point-mass methods approximate different
    posterior structure. Coordinate Viterbi is not global MAP. Markov mixtures of
    experts substantially overlap the existing IOHMM family with an explicit input-alignment
    distinction; that context does not warrant a fourth ID or unconditional alias.
- assessment_id: mixed-memory
  area: consistency
  topic: Compact mixtures versus arbitrary transition interactions
  outcome: supported
  target_ids:
  - AIMech:MixedMemoryMarkovModel
  evidence_ids:
  - mixedmemorymarkovmodel-source-0
  - finite-conventions
  - neighbors
  summary: Retain the mixed-memory parameterization and its inference limits.
  details: Selector-weighted single-predecessor transitions are normalized convex
    mixtures. Their binary interaction contrast is zero, whereas XOR has contrast−2.
    Current vector components factorize conditionally on the complete preceding vector
    but can remain marginally dependent, as witnessed by0.1012625 in the finite example.
    Full hidden EM requires joint latent indicator expectations; a separate correlated-posterior
    witness gives a0.2 difference from a product of marginals. It is explicitly not
    claimed as a trained mixed-memory example. Reversed emission arguments and incomplete
    expected-count displays are qualified; coordinate path objectives and marginal
    likelihood are distinguished.
- assessment_id: boltzmann-equivalence
  area: consistency
  topic: Energy parameterization, exact elimination and endpoint scope
  outcome: supported
  target_ids:
  - AIMech:BoltzmannChain
  evidence_ids:
  - boltzmannchain-source-0
  - boltzmannchain-source-1
  - finite-conventions
  - neighbors
  summary: Retain the graph family with a qualified linear HMM overlap.
  details: 'Tied undirected interaction weights, global fixed-length normalization
    and selected chain-derived graphs define the source family. The score is a clamped-minus-free
    sufficient-statistic expectation and agrees with finite differences to7.39e−12.
    MacKay’s positive transfer-matrix transform leaves a terminal-state factor: matched
    endpoint conditioning agrees to2.78e−17, while an unrestricted endpoint differs
    by0.00310059. Explicit terminal reweighting restores agreement; naive separate
    local normalization differs by0.02913866. The preprint is dated1995 and has three
    pages, not the four-page journal layout. No wider expressiveness follows solely
    from the energy parameterization, and positive-matrix equivalence does not certify
    all loopy/reducible cases.'
- assessment_id: mapping-boundaries
  area: grounding
  topic: Model parents versus related tasks and temporal processes
  outcome: supported
  target_ids:
  - AIMech:HiddenMarkovDecisionTree
  - AIMech:MixedMemoryMarkovModel
  - AIMech:BoltzmannChain
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain the inspected directional AIO mappings.
  details: 'Seventeen exact fully annotated AIO nodes and all63 semantic label/synonym
    hits were inspected. Fourteen generated YAMLs were byte-verified after prior full
    reading and three freshly read. Six native neighbors were read in this or the
    immediately preceding cohort. HMDT and mixed-memory models are finite directed
    conditional factorizations with broader BayesianNetwork mappings. HMDT has a related
    DecisionTree mapping: the AIO target is classification-scoped, while the sequence
    model need not classify. Mixed-memory models have a related MarkovChain mapping
    because higher-order scalar and hidden observed processes need not be first-order.
    Boltzmann chains have a broad BoltzmannMachineNetwork mapping and related MarkovChain
    association qualified by linear topology and terminal factors. RestrictedBoltzmannMachine
    lacks the temporal hidden-hidden interactions of the source construction, despite
    its broad abbreviated definition. ProbabilisticGraphicalModel and MachineLearningTask
    are task-scoped; TrainingStrategy is preprocessing-scoped. CausalGraphicalModel
    adds assumptions not supplied by a dependence graph. MixtureofExpertsLLM, MemoryAugmentedLLM,
    EnergyBasedLLM and ImplicitLanguageModel are language-specific; no generic identity
    is inferred from related synonyms. MemoryCellLayer and ProbabilisticHiddenLayer
    are components, not these models. ProbabilisticTopicModel is text/topic-specific.
    RecurrentNeuralNetwork is not forced as a generic parent of tabular probabilistic
    models. Native HMM, FHMM, IOHMM, PoHMM, structured FHMM inference and EM distinguish
    model structures, parameterizations and procedures; their context inspection is
    not renewed scientific approval.'
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:HiddenMarkovDecisionTree
  - AIMech:MixedMemoryMarkovModel
  - AIMech:BoltzmannChain
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - mme-overlap
  - hiddenmarkovdecisiontree-source-0
  - mixedmemorymarkovmodel-source-0
  - boltzmannchain-source-0
  - boltzmannchain-source-1
  rationale: HMDT combines current hierarchical decisions with same-level temporal
    persistence. Mixed-memory models constrain transition distributions to convex
    mixtures of single-predecessor effects. Boltzmann chains specify a tied-energy
    undirected temporal graph family, with a qualified linear overlap with endpoint-conditioned
    HMMs. These model parameterizations and structures are distinct from their inference/learning
    procedures. Retain all three records and their explicit directional mappings.
limitations:
- Adversarial author self-review only; every target remains DRAFT.
- All33 pages across five downloaded PDFs were visually read, including the seven-page
  MME overlap source and three-page MacKay preprint. Conversion manifests alone do
  not attest reading.
- Some web/publisher access attempts failed. The author archive supplied the preprint
  legitimately; the journal layout was not inspected and no access control was bypassed.
- Source equation errors, conditional independence, approximate path inference and
  terminal conditions are qualified. Finite arithmetic is not model fitting, author-code
  execution or a universal proof.
- The initial history command failed due to unsupported option spellings and created
  no file. A corrected canonical invocation saved the actual curation event before
  history validation.
- 210 pending leads plus unresolved dispositions remain; discovery is active.
links: []
tags:
- native-concepts
- temporal-mixture
- self-review
- discovery-ongoing
```
