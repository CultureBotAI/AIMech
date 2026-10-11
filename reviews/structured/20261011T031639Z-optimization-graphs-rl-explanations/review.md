# Scientific self-review of eight optimization, graph, RL and explanation concepts

- Review: 20261011T031639Z-optimization-graphs-rl-explanations
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T03:16:39Z
- Finished UTC: 2026-10-11T03:16:39Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All eight selected definitions and mechanisms are supported by inspected primary methods and explicit mapping rationale. The revised GIN and GAT sources prevent carrying preliminary equations into the records. No unresolved finding remains within this scope; discovery continues.

## Scope And Provenance

Identity, narrow definition, mechanism evidence and AIO mapping direction for eight newly maintained concepts.

Selection: Exactly the eight added records in the optimization-graphs-rl-explanations discovery report, without sampling.
Coverage: full; 8 reviewed / 8 in the declared population.
Source: working_tree at Git base 945bd67d190e867ac379f8d4ebbc6d4ddec152a9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:Adam | data/curated/Adam.yaml | maintained | Adam |
| AIMech:ProximalPolicyOptimization | data/curated/ProximalPolicyOptimization.yaml | maintained | Proximal policy optimization |
| AIMech:SoftActorCritic | data/curated/SoftActorCritic.yaml | maintained | Soft actor-critic |
| AIMech:GraphSAGE | data/curated/GraphSAGE.yaml | maintained | GraphSAGE |
| AIMech:GraphAttentionNetwork | data/curated/GraphAttentionNetwork.yaml | maintained | Graph attention network |
| AIMech:GraphIsomorphismNetwork | data/curated/GraphIsomorphismNetwork.yaml | maintained | Graph isomorphism network |
| AIMech:SHAP | data/curated/SHAP.yaml | maintained | SHapley additive explanations |
| AIMech:LIME | data/curated/LIME.yaml | maintained | Local interpretable model-agnostic explanations |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| python -m aimech check-source | passed | True | AIMech:Adam, AIMech:ProximalPolicyOptimization, AIMech:SoftActorCritic, AIMech:GraphSAGE, AIMech:GraphAttentionNetwork, AIMech:GraphIsomorphismNetwork, AIMech:SHAP, AIMech:LIME | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a |
| python -m aimech validate | passed | True | AIMech:Adam, AIMech:ProximalPolicyOptimization, AIMech:SoftActorCritic, AIMech:GraphSAGE, AIMech:GraphAttentionNetwork, AIMech:GraphIsomorphismNetwork, AIMech:SHAP, AIMech:LIME | Checked 442 record(s); 0 failed. |
| python -m aimech seed --check | passed | True | AIMech:Adam, AIMech:ProximalPolicyOptimization, AIMech:SoftActorCritic, AIMech:GraphSAGE, AIMech:GraphAttentionNetwork, AIMech:GraphIsomorphismNetwork, AIMech:SHAP, AIMech:LIME | AIO: 442 records; 0 missing, 0 changed, 0 unexpected. |
| python -m aimech validate-curated | passed | True | AIMech:Adam, AIMech:ProximalPolicyOptimization, AIMech:SoftActorCritic, AIMech:GraphSAGE, AIMech:GraphAttentionNetwork, AIMech:GraphIsomorphismNetwork, AIMech:SHAP, AIMech:LIME | Checked 44 curated concept records; 0 errors. |
| PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check | passed | True | AIMech:Adam, AIMech:ProximalPolicyOptimization, AIMech:SoftActorCritic, AIMech:GraphSAGE, AIMech:GraphAttentionNetwork, AIMech:GraphIsomorphismNetwork, AIMech:SHAP, AIMech:LIME | 209 passed, 3 skipped; all 442 AIO and 44 native records valid; AIO byte reproduction exact; 6 history records valid; 2 prior review bundles valid. |
| just vendored-check | passed | True | AIMech:Adam, AIMech:ProximalPolicyOptimization, AIMech:SoftActorCritic, AIMech:GraphSAGE, AIMech:GraphAttentionNetwork, AIMech:GraphIsomorphismNetwork, AIMech:SHAP, AIMech:LIME | 22 governed artifacts match the pinned CLAW revision. |

## Scientific And Domain Assessments

### Full-text definition and mechanism support

evidence: supported. Targets: AIMech:Adam.

Stochastic gradient optimization using bias-corrected exponential estimates of first and second gradient moments to scale parameter updates. Adam specifies adaptive moment-based updates; the local SGD concept does not require these estimates. It is an optimizer, not a training task or a trained model.

An optimizer can implement parameter fitting, but the pinned TrainingStrategy definition uses a preprocessing genus; no subclass relationship is asserted. No universal convergence or benchmark superiority claim is curated. AdamW, AdaMax and other variants require their own identity assessment.

### Full-text definition and mechanism support

evidence: supported. Targets: AIMech:ProximalPolicyOptimization.

A family of policy-gradient algorithms alternating collected interaction data with repeated optimization of a surrogate objective using clipping or an adaptive KL penalty. PPO is a policy-optimization algorithm family. It is distinct from the broad reinforcement-learning task and from DPO's direct preference-fitting objective; PPO is not synonymous with its clipped variant alone.

PPO is a particular policy-gradient procedure within reinforcement-learning practice; the AIO class denotes the broader task. Clipping the surrogate objective is not an explicit hard bound on all policy changes. The record covers the original clipped and KL-penalized variants without asserting task-independent performance.

### Full-text definition and mechanism support

evidence: supported. Targets: AIMech:SoftActorCritic.

An off-policy actor-critic algorithm fitting a stochastic policy and soft value functions under a reward-plus-policy-entropy objective. SAC specifies an off-policy maximum-entropy actor-critic procedure. It is not a synonym for all reinforcement learning, for PPO, or for every entropy-regularized algorithm.

SAC is a particular algorithm for policy learning, whereas the pinned AIO target is a broad machine-learning task. The inspected 2018 method includes a state-value approximator; later variants are not automatically identical in implementation. Tabular soft-policy-iteration theory does not by itself certify convergence of arbitrary neural function approximators.

### Full-text definition and mechanism support

evidence: supported. Targets: AIMech:GraphSAGE.

An inductive graph representation architecture that learns neighborhood aggregation functions to generate node embeddings from features. GraphSAGE learns an embedding-generating function, unlike individually fitted transductive node embeddings. The broad AIO graph-convolutional category does not require the named sampling-and-aggregation framework.

Learned aggregation and transformation layers form an artificial neural network; this target is broader than the specific graph architecture. The pinned definition broadly describes learning on graph structure, but GraphSAGE has its own inductive sampling/aggregation construction; a narrower GCN algorithm is not equated with it. The paper describes multiple aggregators; no single mean or pooling variant defines the entire framework. Inductive construction does not guarantee accurate embeddings for every unseen graph or feature distribution.

### Full-text definition and mechanism support

evidence: supported. Targets: AIMech:GraphAttentionNetwork.

A graph neural architecture that updates node representations using learned attention weights over graph neighborhoods. The original GAT architecture is distinct from a generic attention layer and from graph-convolution methods that do not use its learned neighborhood attention. GATv2 and other revisions are outside this identity.

Graph attentional layers are learned neural computations, so the general artificial-neural-network target is broader. Both use graph structure, but the GAT paper defines a specific learned attention mechanism; the mapping does not equate named GAT and GCN algorithms. The record uses the revised ICLR 2018 paper, including its specified attention nonlinearity. Attention coefficients are computation weights; no general causal-explanation or benchmark-superiority claim is made.

### Full-text definition and mechanism support

evidence: supported. Targets: AIMech:GraphIsomorphismNetwork.

A graph neural architecture using multilayer perceptrons on sums of neighboring representations and a separately weighted self-representation. GIN is the named sum-and-MLP architecture, not the graph-isomorphism decision problem, all graph neural networks, or all architectures as expressive as a Weisfeiler–Lehman test.

The architecture uses learned multilayer perceptrons to transform graph-node states; the AIO neural-network category is broader. The AIO category describes graph-structured neural computation broadly; the GIN construction has a specific aggregation and self-weighting rule. The equation is taken from revised v3; the earlier v1 expression lacks the separately parameterized self weighting. No claim that GIN solves arbitrary graph isomorphism or that every trained finite network attains the theoretical expressivity bound is curated.

### Full-text definition and mechanism support

evidence: supported. Targets: AIMech:SHAP.

An additive feature-attribution framework assigning Shapley values to a prediction through a specified function for evaluating feature subsets. SHAP denotes the attribution framework, not the software package or any one estimator such as Kernel SHAP. LIME instead fits a locally weighted surrogate objective that need not recover these Shapley values.

The shared theme is explaining predictions, but SHAP is a general attribution framework and the AIO target is a type of language model; neither equivalence nor subclasshood is asserted. Feature-subset evaluation and dependence assumptions affect the interpretation; the paper distinguishes conditional expectations from independence approximations. Attribution values do not by themselves establish causal effects or that a model is safe to deploy.

### Full-text definition and mechanism support

evidence: supported. Targets: AIMech:LIME.

A prediction-explanation method fitting an interpretable surrogate to locally weighted samples of a model's behavior. LIME is a local surrogate explanation procedure, not an inherently explainable model, a guarantee of global fidelity, or the separate SP-LIME representative-selection method.

Both concern explaining predictions, but LIME is a general post-hoc algorithm rather than a language-model class; the mapping makes no LLM-specific efficacy assertion. The source explicitly distinguishes local fidelity from global fidelity. Choice of interpretable representation, neighborhood and surrogate family is part of the method's scope; explanations are not a general certification of trustworthiness.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:Adam, AIMech:ProximalPolicyOptimization, AIMech:SoftActorCritic, AIMech:GraphSAGE, AIMech:GraphAttentionNetwork, AIMech:GraphIsomorphismNetwork, AIMech:SHAP, AIMech:LIME. Retain Adam moment estimation, PPO surrogate policy updates, SAC entropy-regularized off-policy learning, GraphSAGE neighborhood aggregation, GAT learned neighbor attention, GIN sum/MLP updates, SHAP attribution and LIME local surrogate fitting as distinct scoped concepts. PPO includes both original surrogate variants. SHAP is the framework rather than one estimator; LIME excludes SP-LIME selection.
- defer: AIMech:Adam, AIMech:ProximalPolicyOptimization, AIMech:SoftActorCritic, AIMech:GraphSAGE, AIMech:GraphAttentionNetwork, AIMech:GraphIsomorphismNetwork, AIMech:SHAP, AIMech:LIME. A complete fine-grained hierarchy and variants such as GATv2, AdamW, Kernel SHAP and later SAC implementations need separate source and identity assessments; the current related mappings do not force equivalence.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| mapping-source | sources/aio/aio.json; Labels, definitions and scoped synonyms for mapped classes and all candidate identity comparisons | supports | No existing concept has a matching normalized label or alias. Actual target definitions distinguish architectures, methods and tasks; mapping direction is explicit. |
| discovery | research/discovery/20261011T031353Z-optimization-graphs-rl-explanations.json | supports | Eight distinct supported additions after exact identity searches and primary-paper interpretation. Revised GIN/GAT equations and selected method pages were checked visually. |
| adam-paper | https://arxiv.org/pdf/1412.6980v9; Section 2 and Algorithm 1, PDF/printed p. 2 | supports | The abstract proposes adaptive lower-order moment estimates for stochastic optimization and reports favorable experiments. Those performance and convergence statements are not adopted as universal properties. Full method inspection: The update divides the bias-corrected first moment by the square root of the bias-corrected second raw moment plus a numerical stabilizer. Rendered PDF pages inspected: 2. |
| proximalpolicyoptimization-paper | https://arxiv.org/pdf/1707.06347v2; Sections 3–5, equations 7–8 and Algorithm 1, PDF/printed pp. 3–5 | supports | The abstract introduces surrogate objectives that allow repeated minibatch updates after environment sampling. Reported robotics and Atari comparisons are experiments, not defining properties. Full method inspection: The clipped variant takes the minimum of unclipped and clipped probability-ratio advantage terms; another variant uses an adaptive KL-divergence penalty, and the algorithm performs multiple minibatch epochs on collected trajectories. Rendered PDF pages inspected: 3. |
| softactorcritic-paper | https://arxiv.org/pdf/1801.01290v2; Section 3.2 equation 1 and section 4.2 equations 5–13 / Algorithm 1, PDF pp. 3–5 | supports | The abstract proposes off-policy actor-critic learning with an entropy-augmented objective and evaluates continuous control. Stability and benchmark advantages remain claims about those experiments. Full method inspection: Experience is retained in a replay buffer; value and policy networks are updated from sampled batches, with the policy objective balancing action value against log policy probability. Rendered PDF pages inspected: 5. |
| graphsage-paper | https://arxiv.org/pdf/1706.02216v4; Section 3.1, Algorithm 1 and Neighborhood definition, PDF/printed pp. 3–4 | supports | The abstract distinguishes an embedding-generating function from per-node transductive parameters and tests unseen nodes and graphs. Its benchmark results are not universal generalization guarantees. Full method inspection: At each depth, sampled neighbor representations are aggregated and combined with a node's current representation through learned transformations; parameters are shared across nodes. Rendered PDF pages inspected: 4. |
| graphattentionnetwork-paper | https://arxiv.org/pdf/1710.10903v3; Section 2.1, equations 1–6, PDF/printed pp. 3–4 | supports | The abstract proposes masked self-attention over graph neighborhoods and reports transductive and inductive experiments. Its architectural contribution is learned neighbor weighting, not proof that weights explain causality. Full method inspection: Shared transformations and a learned attention function produce neighborhood scores, softmax normalizes those scores, and their weighted feature combinations form updated node representations. Rendered PDF pages inspected: 3. |
| graphisomorphismnetwork-paper | https://arxiv.org/pdf/1810.00826v3; Section 4.1, Corollary 6 and equation 4.1, PDF/printed p. 5 of arXiv v3 | supports | The abstract analyzes neighborhood-aggregation expressivity and proposes an architecture connected to the Weisfeiler–Lehman test. The method is not an unrestricted graph-isomorphism solver. Full method inspection: Each update applies an MLP to the sum of neighbor states and (1 + epsilon) times the current node state, with epsilon fixed or learned. Rendered PDF pages inspected: 5. |
| shap-paper | https://proceedings.neurips.cc/paper/2017/file/8a20a8621978632d76c43dfd28b67767-Paper.pdf; Sections 3–4, equations 8–12 and Figure 1, PDF/printed pp. 4–5 | supports | The abstract unifies additive feature-attribution methods and introduces SHAP with proposed axioms and estimators. The framework should be distinguished from any single implementation or estimator. Full method inspection: In the paper's conditional-expectation formulation, feature attributions average marginal changes in expected model output across feature orderings and combine with a baseline prediction. Rendered PDF pages inspected: 5. |
| lime-paper | https://arxiv.org/pdf/1602.04938v3; Sections 3.1–3.3 and equation 1, PDF/printed p. 3 | supports | The abstract proposes local interpretable surrogates and separately introduces SP-LIME for representative explanations. User-study claims are distinct from the local fitting mechanism. Full method inspection: Perturbed interpretable inputs are mapped back to model inputs and labeled by model outputs; fitting balances a locality-weighted fidelity loss against surrogate complexity. Rendered PDF pages inspected: 3. |

## Limits And Additional Notes

- Scientific self-review of selected method claims, not independent peer review or experimental replication.
- The timestamps record this post-inspection assessment; PDF reading and curation occurred earlier in the documented session.
- Paper theorems and experiments are not promoted to universal convergence, expressivity, trustworthiness or safety guarantees.
- The ontology lacks fine-grained native categories for some methods; related mappings intentionally retain their abstraction differences.
- All records remain DRAFT. Eight new concepts were found and the discovery frontier remains nonempty.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T031639Z-optimization-graphs-rl-explanations
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of eight optimization, graph, RL and explanation concepts
started_at: '2026-10-11T03:16:39Z'
finished_at: '2026-10-11T03:16:39Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The reviewing agent also researched and curated these records;
    this is not an independent review.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All eight selected definitions and mechanisms are supported by inspected
  primary methods and explicit mapping rationale. The revised GIN and GAT sources
  prevent carrying preliminary equations into the records. No unresolved finding remains
  within this scope; discovery continues.
source:
  git_revision: 945bd67d190e867ac379f8d4ebbc6d4ddec152a9
  state: working_tree
  inputs:
  - path: data/curated/Adam.yaml
    sha256: 046ba65058648699d78cf44191321a1d8f67e042d3cea6c15bc0f834ce6b1b86
    role: target
  - path: data/curated/GraphAttentionNetwork.yaml
    sha256: d0c81e5f4484619861b11d40a48c4ddd2a1b677b6ad8f01b2e92ba80648af860
    role: target
  - path: data/curated/GraphIsomorphismNetwork.yaml
    sha256: 936adcfec43e2cbea451d38c894be8ad2ad8e3a9c5554843880880f8e6fc3ad2
    role: target
  - path: data/curated/GraphSAGE.yaml
    sha256: e0dbe2987c5f44d0a9a0c13460e6db9a673322a652ea4d732380b2e4b843adfe
    role: target
  - path: data/curated/LIME.yaml
    sha256: ea51d5ef46c6549be1281c56531bab8d5e42ad117f6b5b55f9ed155f14252f87
    role: target
  - path: data/curated/ProximalPolicyOptimization.yaml
    sha256: 073aed5362b80546287548c4a1520105bb228b146a751cbccc879429f22b3661
    role: target
  - path: data/curated/SHAP.yaml
    sha256: b176dab17765d1ba042560bb102cce8bd496bff74d84912a5e8930d5566c1d5c
    role: target
  - path: data/curated/SoftActorCritic.yaml
    sha256: fd4dd468f1b4a139c0166eab39944608314e42e7cf4dc0f8d750d3cf4802fe85
    role: target
  - path: docs/record-review-profile.md
    sha256: 64ce9def82009730ad5b8de54de48771d3eb299a1da42ce8ab5973a9fcd55add
    role: context
  - path: research/discovery/20261011T031353Z-optimization-graphs-rl-explanations.json
    sha256: 3ff14c6070c548dcc3785e8a4ac394c6d50392dd313a6625ba6dad4299a5c0d0
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 1efe838d99526a85e5b678a70bad7b796edfcc922e7b912a9d4592da78843bbe
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: 529cb70f3fa95580d6197c1581e0b3ad62c17f128d3ed1ba848f54d184f4e312
    role: context
targets:
- target_id: AIMech:Adam
  path: data/curated/Adam.yaml
  label: Adam
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Adam.yaml
    role: maintained concept and evidence claims
- target_id: AIMech:ProximalPolicyOptimization
  path: data/curated/ProximalPolicyOptimization.yaml
  label: Proximal policy optimization
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ProximalPolicyOptimization.yaml
    role: maintained concept and evidence claims
- target_id: AIMech:SoftActorCritic
  path: data/curated/SoftActorCritic.yaml
  label: Soft actor-critic
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SoftActorCritic.yaml
    role: maintained concept and evidence claims
- target_id: AIMech:GraphSAGE
  path: data/curated/GraphSAGE.yaml
  label: GraphSAGE
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GraphSAGE.yaml
    role: maintained concept and evidence claims
- target_id: AIMech:GraphAttentionNetwork
  path: data/curated/GraphAttentionNetwork.yaml
  label: Graph attention network
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GraphAttentionNetwork.yaml
    role: maintained concept and evidence claims
- target_id: AIMech:GraphIsomorphismNetwork
  path: data/curated/GraphIsomorphismNetwork.yaml
  label: Graph isomorphism network
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GraphIsomorphismNetwork.yaml
    role: maintained concept and evidence claims
- target_id: AIMech:SHAP
  path: data/curated/SHAP.yaml
  label: SHapley additive explanations
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SHAP.yaml
    role: maintained concept and evidence claims
- target_id: AIMech:LIME
  path: data/curated/LIME.yaml
  label: Local interpretable model-agnostic explanations
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LIME.yaml
    role: maintained concept and evidence claims
scope:
  description: Identity, narrow definition, mechanism evidence and AIO mapping direction
    for eight newly maintained concepts.
  selection: Exactly the eight added records in the optimization-graphs-rl-explanations
    discovery report, without sampling.
  coverage: full
  population_size: 8
  reviewed_target_ids:
  - AIMech:Adam
  - AIMech:ProximalPolicyOptimization
  - AIMech:SoftActorCritic
  - AIMech:GraphSAGE
  - AIMech:GraphAttentionNetwork
  - AIMech:GraphIsomorphismNetwork
  - AIMech:SHAP
  - AIMech:LIME
  exclusions:
  - target: The other 36 native records and 442 AIO records
    reason: Other native records have a separate scoped review; AIO records are used
      as identity/mapping context.
  - target: Performance, global convergence and universal safety claims
    reason: No such claims are curated or experimentally tested in this review.
checks:
- check_id: pin-0
  name: python -m aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:Adam
  - AIMech:ProximalPolicyOptimization
  - AIMech:SoftActorCritic
  - AIMech:GraphSAGE
  - AIMech:GraphAttentionNetwork
  - AIMech:GraphIsomorphismNetwork
  - AIMech:SHAP
  - AIMech:LIME
  command: python -m aimech check-source
  exit_code: 0
  expected_exit_code: 0
  summary: Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a
  scope_note: Actual check against unchanged pinned AIO bytes and importer during
    this session; the subsequent full gate also reproduced all 442 records.
- check_id: pin-1
  name: python -m aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:Adam
  - AIMech:ProximalPolicyOptimization
  - AIMech:SoftActorCritic
  - AIMech:GraphSAGE
  - AIMech:GraphAttentionNetwork
  - AIMech:GraphIsomorphismNetwork
  - AIMech:SHAP
  - AIMech:LIME
  command: python -m aimech validate
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 record(s); 0 failed.
  scope_note: Actual check against unchanged pinned AIO bytes and importer during
    this session; the subsequent full gate also reproduced all 442 records.
- check_id: pin-3
  name: python -m aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:Adam
  - AIMech:ProximalPolicyOptimization
  - AIMech:SoftActorCritic
  - AIMech:GraphSAGE
  - AIMech:GraphAttentionNetwork
  - AIMech:GraphIsomorphismNetwork
  - AIMech:SHAP
  - AIMech:LIME
  command: python -m aimech seed --check
  exit_code: 0
  expected_exit_code: 0
  summary: 'AIO: 442 records; 0 missing, 0 changed, 0 unexpected.'
  scope_note: Actual check against unchanged pinned AIO bytes and importer during
    this session; the subsequent full gate also reproduced all 442 records.
- check_id: curated
  name: python -m aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:Adam
  - AIMech:ProximalPolicyOptimization
  - AIMech:SoftActorCritic
  - AIMech:GraphSAGE
  - AIMech:GraphAttentionNetwork
  - AIMech:GraphIsomorphismNetwork
  - AIMech:SHAP
  - AIMech:LIME
  command: python -m aimech validate-curated
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 44 curated concept records; 0 errors.
- check_id: quality
  name: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check
  status: passed
  required: true
  target_ids:
  - AIMech:Adam
  - AIMech:ProximalPolicyOptimization
  - AIMech:SoftActorCritic
  - AIMech:GraphSAGE
  - AIMech:GraphAttentionNetwork
  - AIMech:GraphIsomorphismNetwork
  - AIMech:SHAP
  - AIMech:LIME
  command: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check
  exit_code: 0
  expected_exit_code: 0
  summary: 209 passed, 3 skipped; all 442 AIO and 44 native records valid; AIO byte
    reproduction exact; 6 history records valid; 2 prior review bundles valid.
- check_id: governance
  name: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:Adam
  - AIMech:ProximalPolicyOptimization
  - AIMech:SoftActorCritic
  - AIMech:GraphSAGE
  - AIMech:GraphAttentionNetwork
  - AIMech:GraphIsomorphismNetwork
  - AIMech:SHAP
  - AIMech:LIME
  command: just vendored-check
  exit_code: 0
  expected_exit_code: 0
  summary: 22 governed artifacts match the pinned CLAW revision.
evidence:
- evidence_id: mapping-source
  kind: record_content
  reference: sources/aio/aio.json
  locator: Labels, definitions and scoped synonyms for mapped classes and all candidate
    identity comparisons
  accessed_at: '2026-10-11T03:16:39Z'
  support: supports
  summary: No existing concept has a matching normalized label or alias. Actual target
    definitions distinguish architectures, methods and tasks; mapping direction is
    explicit.
- evidence_id: discovery
  kind: search
  reference: research/discovery/20261011T031353Z-optimization-graphs-rl-explanations.json
  accessed_at: '2026-10-11T03:16:39Z'
  support: supports
  summary: Eight distinct supported additions after exact identity searches and primary-paper
    interpretation. Revised GIN/GAT equations and selected method pages were checked
    visually.
  search_scope: Both the original checkout and isolated worktree were searched with
    rg --no-ignore --hidden -l -i -w -F; all 442 AIO and 36 then-existing native records
    were compared by normalized names and synonyms. Raw hits were a pending PPO mention
    and ignored dependency text. The report retains primary sources and nonempty follow-up
    leads.
- evidence_id: adam-paper
  kind: primary_source
  reference: https://arxiv.org/pdf/1412.6980v9
  locator: Section 2 and Algorithm 1, PDF/printed p. 2
  accessed_at: '2026-10-11T03:06:37Z'
  support: supports
  snapshot_sha256: eab9c73ae2ceda884b94830bda99312254bac4806f6c9f045cbab90721ecda31
  summary: 'The abstract proposes adaptive lower-order moment estimates for stochastic
    optimization and reports favorable experiments. Those performance and convergence
    statements are not adopted as universal properties. Full method inspection: The
    update divides the bias-corrected first moment by the square root of the bias-corrected
    second raw moment plus a numerical stabilizer. Rendered PDF pages inspected: 2.'
- evidence_id: proximalpolicyoptimization-paper
  kind: primary_source
  reference: https://arxiv.org/pdf/1707.06347v2
  locator: Sections 3–5, equations 7–8 and Algorithm 1, PDF/printed pp. 3–5
  accessed_at: '2026-10-11T03:06:38Z'
  support: supports
  snapshot_sha256: e78feadadbdbb0b601b3c2bcc81404722cd431a489b307545f9b7bea1e8c4f5b
  summary: 'The abstract introduces surrogate objectives that allow repeated minibatch
    updates after environment sampling. Reported robotics and Atari comparisons are
    experiments, not defining properties. Full method inspection: The clipped variant
    takes the minimum of unclipped and clipped probability-ratio advantage terms;
    another variant uses an adaptive KL-divergence penalty, and the algorithm performs
    multiple minibatch epochs on collected trajectories. Rendered PDF pages inspected:
    3.'
- evidence_id: softactorcritic-paper
  kind: primary_source
  reference: https://arxiv.org/pdf/1801.01290v2
  locator: Section 3.2 equation 1 and section 4.2 equations 5–13 / Algorithm 1, PDF
    pp. 3–5
  accessed_at: '2026-10-11T03:09:20Z'
  support: supports
  snapshot_sha256: 5c33fae017d02f7025730f05198d4a6b103402822c8bbf48cbc5d8a0474c336a
  summary: 'The abstract proposes off-policy actor-critic learning with an entropy-augmented
    objective and evaluates continuous control. Stability and benchmark advantages
    remain claims about those experiments. Full method inspection: Experience is retained
    in a replay buffer; value and policy networks are updated from sampled batches,
    with the policy objective balancing action value against log policy probability.
    Rendered PDF pages inspected: 5.'
- evidence_id: graphsage-paper
  kind: primary_source
  reference: https://arxiv.org/pdf/1706.02216v4
  locator: Section 3.1, Algorithm 1 and Neighborhood definition, PDF/printed pp. 3–4
  accessed_at: '2026-10-11T03:09:20Z'
  support: supports
  snapshot_sha256: e1f354eb12011cde24af1eb500d72463fc971b09d26b55688c7f918a86e31ce8
  summary: 'The abstract distinguishes an embedding-generating function from per-node
    transductive parameters and tests unseen nodes and graphs. Its benchmark results
    are not universal generalization guarantees. Full method inspection: At each depth,
    sampled neighbor representations are aggregated and combined with a node''s current
    representation through learned transformations; parameters are shared across nodes.
    Rendered PDF pages inspected: 4.'
- evidence_id: graphattentionnetwork-paper
  kind: primary_source
  reference: https://arxiv.org/pdf/1710.10903v3
  locator: Section 2.1, equations 1–6, PDF/printed pp. 3–4
  accessed_at: '2026-10-11T03:09:20Z'
  support: supports
  snapshot_sha256: a7d811a44e1c65bf27da3a01859f23a8edbe33b8f96114b4b5066aedb078f284
  summary: 'The abstract proposes masked self-attention over graph neighborhoods and
    reports transductive and inductive experiments. Its architectural contribution
    is learned neighbor weighting, not proof that weights explain causality. Full
    method inspection: Shared transformations and a learned attention function produce
    neighborhood scores, softmax normalizes those scores, and their weighted feature
    combinations form updated node representations. Rendered PDF pages inspected:
    3.'
- evidence_id: graphisomorphismnetwork-paper
  kind: primary_source
  reference: https://arxiv.org/pdf/1810.00826v3
  locator: Section 4.1, Corollary 6 and equation 4.1, PDF/printed p. 5 of arXiv v3
  accessed_at: '2026-10-11T03:09:20Z'
  support: supports
  snapshot_sha256: a6ebf80c2790b8bac1fa378902993eae26020cc6d0d95e3964eea42b0c66a974
  summary: 'The abstract analyzes neighborhood-aggregation expressivity and proposes
    an architecture connected to the Weisfeiler–Lehman test. The method is not an
    unrestricted graph-isomorphism solver. Full method inspection: Each update applies
    an MLP to the sum of neighbor states and (1 + epsilon) times the current node
    state, with epsilon fixed or learned. Rendered PDF pages inspected: 5.'
- evidence_id: shap-paper
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper/2017/file/8a20a8621978632d76c43dfd28b67767-Paper.pdf
  locator: Sections 3–4, equations 8–12 and Figure 1, PDF/printed pp. 4–5
  accessed_at: '2026-10-11T03:06:38Z'
  support: supports
  snapshot_sha256: 32518459c313a57876ec1646f3266d54569d3b9a70152dd4f28e742eef05a5f3
  summary: 'The abstract unifies additive feature-attribution methods and introduces
    SHAP with proposed axioms and estimators. The framework should be distinguished
    from any single implementation or estimator. Full method inspection: In the paper''s
    conditional-expectation formulation, feature attributions average marginal changes
    in expected model output across feature orderings and combine with a baseline
    prediction. Rendered PDF pages inspected: 5.'
- evidence_id: lime-paper
  kind: primary_source
  reference: https://arxiv.org/pdf/1602.04938v3
  locator: Sections 3.1–3.3 and equation 1, PDF/printed p. 3
  accessed_at: '2026-10-11T03:06:39Z'
  support: supports
  snapshot_sha256: 365079753571d7d14180e9796cf5d8ae53c5ef157f0a585ef8030b2a126eeccb
  summary: 'The abstract proposes local interpretable surrogates and separately introduces
    SP-LIME for representative explanations. User-study claims are distinct from the
    local fitting mechanism. Full method inspection: Perturbed interpretable inputs
    are mapped back to model inputs and labeled by model outputs; fitting balances
    a locality-weighted fidelity loss against surrogate complexity. Rendered PDF pages
    inspected: 3.'
assessments:
- assessment_id: adam-mechanism
  area: evidence
  topic: Full-text definition and mechanism support
  outcome: supported
  target_ids:
  - AIMech:Adam
  evidence_ids:
  - adam-paper
  - mapping-source
  - discovery
  summary: Stochastic gradient optimization using bias-corrected exponential estimates
    of first and second gradient moments to scale parameter updates. Adam specifies
    adaptive moment-based updates; the local SGD concept does not require these estimates.
    It is an optimizer, not a training task or a trained model.
  details: An optimizer can implement parameter fitting, but the pinned TrainingStrategy
    definition uses a preprocessing genus; no subclass relationship is asserted. No
    universal convergence or benchmark superiority claim is curated. AdamW, AdaMax
    and other variants require their own identity assessment.
  dimensions:
  - name: evidence-access
    value: full_text with selected rendered-page inspection
    definition: The mechanism was checked in the cited primary PDF rather than inferred
      from its abstract.
    evidence_ids:
    - adam-paper
- assessment_id: proximalpolicyoptimization-mechanism
  area: evidence
  topic: Full-text definition and mechanism support
  outcome: supported
  target_ids:
  - AIMech:ProximalPolicyOptimization
  evidence_ids:
  - proximalpolicyoptimization-paper
  - mapping-source
  - discovery
  summary: A family of policy-gradient algorithms alternating collected interaction
    data with repeated optimization of a surrogate objective using clipping or an
    adaptive KL penalty. PPO is a policy-optimization algorithm family. It is distinct
    from the broad reinforcement-learning task and from DPO's direct preference-fitting
    objective; PPO is not synonymous with its clipped variant alone.
  details: PPO is a particular policy-gradient procedure within reinforcement-learning
    practice; the AIO class denotes the broader task. Clipping the surrogate objective
    is not an explicit hard bound on all policy changes. The record covers the original
    clipped and KL-penalized variants without asserting task-independent performance.
  dimensions:
  - name: evidence-access
    value: full_text with selected rendered-page inspection
    definition: The mechanism was checked in the cited primary PDF rather than inferred
      from its abstract.
    evidence_ids:
    - proximalpolicyoptimization-paper
- assessment_id: softactorcritic-mechanism
  area: evidence
  topic: Full-text definition and mechanism support
  outcome: supported
  target_ids:
  - AIMech:SoftActorCritic
  evidence_ids:
  - softactorcritic-paper
  - mapping-source
  - discovery
  summary: An off-policy actor-critic algorithm fitting a stochastic policy and soft
    value functions under a reward-plus-policy-entropy objective. SAC specifies an
    off-policy maximum-entropy actor-critic procedure. It is not a synonym for all
    reinforcement learning, for PPO, or for every entropy-regularized algorithm.
  details: SAC is a particular algorithm for policy learning, whereas the pinned AIO
    target is a broad machine-learning task. The inspected 2018 method includes a
    state-value approximator; later variants are not automatically identical in implementation.
    Tabular soft-policy-iteration theory does not by itself certify convergence of
    arbitrary neural function approximators.
  dimensions:
  - name: evidence-access
    value: full_text with selected rendered-page inspection
    definition: The mechanism was checked in the cited primary PDF rather than inferred
      from its abstract.
    evidence_ids:
    - softactorcritic-paper
- assessment_id: graphsage-mechanism
  area: evidence
  topic: Full-text definition and mechanism support
  outcome: supported
  target_ids:
  - AIMech:GraphSAGE
  evidence_ids:
  - graphsage-paper
  - mapping-source
  - discovery
  summary: An inductive graph representation architecture that learns neighborhood
    aggregation functions to generate node embeddings from features. GraphSAGE learns
    an embedding-generating function, unlike individually fitted transductive node
    embeddings. The broad AIO graph-convolutional category does not require the named
    sampling-and-aggregation framework.
  details: Learned aggregation and transformation layers form an artificial neural
    network; this target is broader than the specific graph architecture. The pinned
    definition broadly describes learning on graph structure, but GraphSAGE has its
    own inductive sampling/aggregation construction; a narrower GCN algorithm is not
    equated with it. The paper describes multiple aggregators; no single mean or pooling
    variant defines the entire framework. Inductive construction does not guarantee
    accurate embeddings for every unseen graph or feature distribution.
  dimensions:
  - name: evidence-access
    value: full_text with selected rendered-page inspection
    definition: The mechanism was checked in the cited primary PDF rather than inferred
      from its abstract.
    evidence_ids:
    - graphsage-paper
- assessment_id: graphattentionnetwork-mechanism
  area: evidence
  topic: Full-text definition and mechanism support
  outcome: supported
  target_ids:
  - AIMech:GraphAttentionNetwork
  evidence_ids:
  - graphattentionnetwork-paper
  - mapping-source
  - discovery
  summary: A graph neural architecture that updates node representations using learned
    attention weights over graph neighborhoods. The original GAT architecture is distinct
    from a generic attention layer and from graph-convolution methods that do not
    use its learned neighborhood attention. GATv2 and other revisions are outside
    this identity.
  details: Graph attentional layers are learned neural computations, so the general
    artificial-neural-network target is broader. Both use graph structure, but the
    GAT paper defines a specific learned attention mechanism; the mapping does not
    equate named GAT and GCN algorithms. The record uses the revised ICLR 2018 paper,
    including its specified attention nonlinearity. Attention coefficients are computation
    weights; no general causal-explanation or benchmark-superiority claim is made.
  dimensions:
  - name: evidence-access
    value: full_text with selected rendered-page inspection
    definition: The mechanism was checked in the cited primary PDF rather than inferred
      from its abstract.
    evidence_ids:
    - graphattentionnetwork-paper
- assessment_id: graphisomorphismnetwork-mechanism
  area: evidence
  topic: Full-text definition and mechanism support
  outcome: supported
  target_ids:
  - AIMech:GraphIsomorphismNetwork
  evidence_ids:
  - graphisomorphismnetwork-paper
  - mapping-source
  - discovery
  summary: A graph neural architecture using multilayer perceptrons on sums of neighboring
    representations and a separately weighted self-representation. GIN is the named
    sum-and-MLP architecture, not the graph-isomorphism decision problem, all graph
    neural networks, or all architectures as expressive as a Weisfeiler–Lehman test.
  details: The architecture uses learned multilayer perceptrons to transform graph-node
    states; the AIO neural-network category is broader. The AIO category describes
    graph-structured neural computation broadly; the GIN construction has a specific
    aggregation and self-weighting rule. The equation is taken from revised v3; the
    earlier v1 expression lacks the separately parameterized self weighting. No claim
    that GIN solves arbitrary graph isomorphism or that every trained finite network
    attains the theoretical expressivity bound is curated.
  dimensions:
  - name: evidence-access
    value: full_text with selected rendered-page inspection
    definition: The mechanism was checked in the cited primary PDF rather than inferred
      from its abstract.
    evidence_ids:
    - graphisomorphismnetwork-paper
- assessment_id: shap-mechanism
  area: evidence
  topic: Full-text definition and mechanism support
  outcome: supported
  target_ids:
  - AIMech:SHAP
  evidence_ids:
  - shap-paper
  - mapping-source
  - discovery
  summary: An additive feature-attribution framework assigning Shapley values to a
    prediction through a specified function for evaluating feature subsets. SHAP denotes
    the attribution framework, not the software package or any one estimator such
    as Kernel SHAP. LIME instead fits a locally weighted surrogate objective that
    need not recover these Shapley values.
  details: The shared theme is explaining predictions, but SHAP is a general attribution
    framework and the AIO target is a type of language model; neither equivalence
    nor subclasshood is asserted. Feature-subset evaluation and dependence assumptions
    affect the interpretation; the paper distinguishes conditional expectations from
    independence approximations. Attribution values do not by themselves establish
    causal effects or that a model is safe to deploy.
  dimensions:
  - name: evidence-access
    value: full_text with selected rendered-page inspection
    definition: The mechanism was checked in the cited primary PDF rather than inferred
      from its abstract.
    evidence_ids:
    - shap-paper
- assessment_id: lime-mechanism
  area: evidence
  topic: Full-text definition and mechanism support
  outcome: supported
  target_ids:
  - AIMech:LIME
  evidence_ids:
  - lime-paper
  - mapping-source
  - discovery
  summary: A prediction-explanation method fitting an interpretable surrogate to locally
    weighted samples of a model's behavior. LIME is a local surrogate explanation
    procedure, not an inherently explainable model, a guarantee of global fidelity,
    or the separate SP-LIME representative-selection method.
  details: Both concern explaining predictions, but LIME is a general post-hoc algorithm
    rather than a language-model class; the mapping makes no LLM-specific efficacy
    assertion. The source explicitly distinguishes local fidelity from global fidelity.
    Choice of interpretable representation, neighborhood and surrogate family is part
    of the method's scope; explanations are not a general certification of trustworthiness.
  dimensions:
  - name: evidence-access
    value: full_text with selected rendered-page inspection
    definition: The mechanism was checked in the cited primary PDF rather than inferred
      from its abstract.
    evidence_ids:
    - lime-paper
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:Adam
  - AIMech:ProximalPolicyOptimization
  - AIMech:SoftActorCritic
  - AIMech:GraphSAGE
  - AIMech:GraphAttentionNetwork
  - AIMech:GraphIsomorphismNetwork
  - AIMech:SHAP
  - AIMech:LIME
  evidence_ids:
  - mapping-source
  - discovery
  - adam-paper
  - proximalpolicyoptimization-paper
  - softactorcritic-paper
  - graphsage-paper
  - graphattentionnetwork-paper
  - graphisomorphismnetwork-paper
  - shap-paper
  - lime-paper
  rationale: Retain Adam moment estimation, PPO surrogate policy updates, SAC entropy-regularized
    off-policy learning, GraphSAGE neighborhood aggregation, GAT learned neighbor
    attention, GIN sum/MLP updates, SHAP attribution and LIME local surrogate fitting
    as distinct scoped concepts. PPO includes both original surrogate variants. SHAP
    is the framework rather than one estimator; LIME excludes SP-LIME selection.
- action: defer
  target_ids:
  - AIMech:Adam
  - AIMech:ProximalPolicyOptimization
  - AIMech:SoftActorCritic
  - AIMech:GraphSAGE
  - AIMech:GraphAttentionNetwork
  - AIMech:GraphIsomorphismNetwork
  - AIMech:SHAP
  - AIMech:LIME
  evidence_ids:
  - mapping-source
  - discovery
  rationale: A complete fine-grained hierarchy and variants such as GATv2, AdamW,
    Kernel SHAP and later SAC implementations need separate source and identity assessments;
    the current related mappings do not force equivalence.
limitations:
- Scientific self-review of selected method claims, not independent peer review or
  experimental replication.
- The timestamps record this post-inspection assessment; PDF reading and curation
  occurred earlier in the documented session.
- Paper theorems and experiments are not promoted to universal convergence, expressivity,
  trustworthiness or safety guarantees.
- The ontology lacks fine-grained native categories for some methods; related mappings
  intentionally retain their abstraction differences.
- All records remain DRAFT. Eight new concepts were found and the discovery frontier
  remains nonempty.
tags:
- native-concepts
- primary-papers
- self-review
- discovery-ongoing
```
