# Scientific author self-review of Communication Neural Network

- Review: 20261013T093513Z-communication-neural-network
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T09:30:32Z
- Finished UTC: 2026-10-13T09:35:13Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain CommNet as a DRAFT architecture broadly mapped to ArtificialNeuralNetwork. Six claims preserve continuous mean communication, formula edge cases, equivariance and mixed evaluation evidence; adversarial author self-review found no actionable defect.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:CommunicationNeuralNetwork
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 173128ca575a0f26129f1908d26f3b2ff4871a0e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CommunicationNeuralNetwork | data/curated/CommunicationNeuralNetwork.yaml | maintained | Communication Neural Network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:CommunicationNeuralNetwork | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 138.01s (0:02:18)<br>Checked 442 record(s); 0 failed.<br>Checked 599 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 259 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 258,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:CommunicationNeuralNetwork | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:CommunicationNeuralNetwork | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:CommunicationNeuralNetwork | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:CommunicationNeuralNetwork | {"hidden_states": ["2", "5", "11"], "exclude_self_means": ["8", "13/2", "7/2"], "chosen_step": ["28", "59/2", "65/2"], "inclusive_mean": "6", "local_receiver_zero": "5", "permutations_checked": 6, "singleton_formula_undefined": true, "mean_collision": [[2, 4], [1, 5]], "arithmetic_counts": [{"agents": 2, "naive_other_agent_terms": 2, "shared_total_additions": 1, "per_agent_subtractions": 2, "per_agent_divisions": 2}, {"agents": 4, "naive_other_agent_terms": 12, "shared_total_additions": 3, "per_agent_subtractions": 4, "per_agent_divisions": 4}, {"agents": 8, "naive_other_agent_terms": 56, "shared_total_additions": 7, "per_agent_subtractions": 8, "per_agent_divisions": 8}], "scope": "Exact tiny pooling examples; not training, physical communication cost, author-code behavior, independent actions, or empirical generalization evidence."} |

## Scientific And Domain Assessments

### Communication Neural Network

identity: supported. Targets: AIMech:CommunicationNeuralNetwork.

Retain this distinct DRAFT architecture.

CommNet is the named continuous mean-communication architecture. It is distinct from learned-distance VAIN, pairwise Interaction Network effects and GAT/GIN/GraphSAGE. Recurrence and neighborhood restrictions are optional extensions.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:CommunicationNeuralNetwork.

The declared broad AIO mapping is supported.

Four annotated AIO nodes, all incident edges and generated YAMLs were inspected. Shared learned neural modules support broad ArtificialNeuralNetwork. The base architecture does not require recurrent dynamics, named GCN computation or a conditional-dependence task.

### continuous-exclude-self-communication

evidence: supported. Targets: AIMech:CommunicationNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Equation1updates hidden states from currentcommunication; Eq2forms nextcommunication from otherupdatedstates. Initialcommunication0 and sharedagentmodules are explicit; layerweightsharing is not asserted. Baseactionhead andsampledactions matchp2.

### mean-and-empty-neighborhood-boundaries

evidence: supported. Targets: AIMech:CommunicationNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

J-1and&#124;N(j)&#124;denominators exclude statedemptycases without an implementation convention. Exact examples distinguish globalexclude-self,inclusiveandlocalmeans and showmean collisions. No artificial zero-neighbor behavior is invented.

### permutation-and-computation-boundaries

evidence: supported. Targets: AIMech:CommunicationNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

The block matrix commutes with agent permutation; corresponding output arrays permute. Constructed6permutations checkthis; they do not establish an unchanged orderedarray. Totalminusself is a direct algebraic aggregation optimization, not a physicalnetworkcost claim.

### extensions-and-training-boundaries

evidence: supported. Targets: AIMech:CommunicationNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Section2.2describes localmeans,skiporiginalencoding andtemporalrecurrentalternatives. Section3rejectsfixedpointnecessity. Continuouscommunication permitsbackprop butdiscreteaction samplingneedsappropriatetrainingsignals; the policygradientdiscretecommunicationbaseline remains separate.

### cooperative-task-evaluation

evidence: supported. Targets: AIMech:CommunicationNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Fullcooperationsharedreward isexplicit. Lever5from500 poolanddistinctcoverage,trafficfailure andcombatwinpercent are distinctprotocols. The fixed simulation,variantandseedsettingspreclude universalcoordinationclaims.

### global-answer-variant-and-evidence-limits

evidence: supported. Targets: AIMech:CommunicationNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

bAbIp8sumsfinalsentencehiddenstatesafterK2andusesglobalanswerhead. Table4CommNet7.1error exceedsMemN2N4.2andDMN+2.8; no universalbestclaim. PCA/brakingcorrelations are notcausalproof; heterogeneous/largepopulationsfutureworkexplicit.

### exclude-self means, empty-neighborhood formulas, per-agent equivariance, communication steps and task-specific variants

consistency: supported. Targets: AIMech:CommunicationNeuralNetwork.

Constructed calculations support the stated distinctions.

Exact rational chosen states distinguish exclude-self means from sums and inclusive/local means, demonstrate mean collisions, J1undefinedformula, all6permutations and shared-total arithmetic counts. No learned-network, physical-message-cost or benchmark replication claim.

### All maintained fields

provenance: supported. Targets: AIMech:CommunicationNeuralNetwork.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Read every maintained field and all four mapping YAMLs after capture. Reread communication timing and exclude-self normalization, block symmetry, optional extensions, training distinctions, evaluation tables and global question-answering readout. Recomputed exact rational examples.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T093019Z-communication-neural-network.json | supports | Compared all 442 pinned AIO and 598 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 8, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 24 AIO and 51 native definitions, with every matched definition read. 4 full annotated AIO node/edge/generated contexts and 5 full native records were inspected. CommNet is the named Communication Neural Net with shared agent modules and exclude-self mean communication. It differs from VAIN learned-distance weights, Interaction Network pair-specific learned effects, and the maintained GAT, GIN and GraphSAGE constructions. The neural architecture maps broadly to ANN; recurrence and local connectivity are extensions, not essential identity conditions. |
| mapping | sources/aio/aio.json | supports | Four annotated AIO nodes, all incident edges and generated YAMLs were inspected. Shared learned neural modules support broad ArtificialNeuralNetwork. The base architecture does not require recurrent dynamics, named GCN computation or a conditional-dependence task. |
| sukhbaatar2016 | https://papers.neurips.cc/paper/6398-learning-multiagent-communication-with-backpropagation.pdf; All nine main-paper PDF pages read before curation; selected method/evaluation pages reread after capture. Supplement, other versions and author code not inspected. No benchmark, training or runtime replication. | supports | NIPS2016 proceedings PDF, nine pages, all visually read including equations, figures, tables and references. Authors and proceedings identity agree with the primary landing page. Locators are PDF/printed pages1–9. Supplement, other manuscript versions and author code not inspected. |
| calculation | research/discovery/communication-network-boundaries.py | supports | Exact rational chosen states distinguish exclude-self means from sums and inclusive/local means, demonstrate mean collisions, J1undefinedformula, all6permutations and shared-total arithmetic counts. No learned-network, physical-message-cost or benchmark replication claim. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 599 native and 442 unchanged generated records. The 783-entry main frontier retains 477 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All nine main-paper pages read including figures,tables,formulas and references; supplement and author code not inspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T093513Z-communication-neural-network
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Communication Neural Network
started_at: '2026-10-13T09:30:32Z'
finished_at: '2026-10-13T09:35:13Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged exclude-self means, empty-neighborhood
    formulas, per-agent equivariance, communication steps and task-specific variants.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain CommNet as a DRAFT architecture broadly mapped to ArtificialNeuralNetwork.
  Six claims preserve continuous mean communication, formula edge cases, equivariance
  and mixed evaluation evidence; adversarial author self-review found no actionable
  defect.
source:
  git_revision: 173128ca575a0f26129f1908d26f3b2ff4871a0e
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/GraphConvolutionalNetwork.yaml
    sha256: 644b6187436c10693cb547dbaa809b8c00c97ad198db201342e5bc0780c78d44
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/curated/CommunicationNeuralNetwork.yaml
    sha256: 6da13aca3d17822181f43ddfb796a62170d2cdbb28a2e01a5d541c9a1ff8d813
    role: target
  - path: data/curated/GraphAttentionNetwork.yaml
    sha256: d0c81e5f4484619861b11d40a48c4ddd2a1b677b6ad8f01b2e92ba80648af860
    role: context
  - path: data/curated/GraphIsomorphismNetwork.yaml
    sha256: 936adcfec43e2cbea451d38c894be8ad2ad8e3a9c5554843880880f8e6fc3ad2
    role: context
  - path: data/curated/GraphSAGE.yaml
    sha256: e0dbe2987c5f44d0a9a0c13460e6db9a673322a652ea4d732380b2e4b843adfe
    role: context
  - path: data/curated/InteractionNetwork.yaml
    sha256: 4d20b7990c1854c6d10b0a35d95d81095b2842c94af14b3cee7fe3c198e7b3d0
    role: context
  - path: data/curated/VertexAttentionInteractionNetwork.yaml
    sha256: 2bb93bb8bc9f67a49a58fd62a87702e5989192466aa1ebffda0d8192b84b7317
    role: context
  - path: research/discovery/20261013T093019Z-communication-neural-network.json
    sha256: f8f9e666520fcbf89a0e969acf8f9949c5b6a996ee303ae694f4194fbeb12efd
    role: context
  - path: research/discovery/communication-network-boundaries.py
    sha256: 6d8ceed5f7d0a1d8854c949ee634deb3055bdca4fa3b8a196d547ff5e1edbd66
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
- target_id: AIMech:CommunicationNeuralNetwork
  path: data/curated/CommunicationNeuralNetwork.yaml
  label: Communication Neural Network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CommunicationNeuralNetwork.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:CommunicationNeuralNetwork'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:CommunicationNeuralNetwork
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All nine main-paper PDF pages read before curation; selected method/evaluation
      pages reread after capture. Supplement, other versions and author code not inspected.
      No benchmark, training or runtime replication.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:CommunicationNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 138.01s (0:02:18)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 599 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 259 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 258,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:CommunicationNeuralNetwork
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
  - AIMech:CommunicationNeuralNetwork
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
  - AIMech:CommunicationNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/communication-network-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CommunicationNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: '{"hidden_states": ["2", "5", "11"], "exclude_self_means": ["8", "13/2",
    "7/2"], "chosen_step": ["28", "59/2", "65/2"], "inclusive_mean": "6", "local_receiver_zero":
    "5", "permutations_checked": 6, "singleton_formula_undefined": true, "mean_collision":
    [[2, 4], [1, 5]], "arithmetic_counts": [{"agents": 2, "naive_other_agent_terms":
    2, "shared_total_additions": 1, "per_agent_subtractions": 2, "per_agent_divisions":
    2}, {"agents": 4, "naive_other_agent_terms": 12, "shared_total_additions": 3,
    "per_agent_subtractions": 4, "per_agent_divisions": 4}, {"agents": 8, "naive_other_agent_terms":
    56, "shared_total_additions": 7, "per_agent_subtractions": 8, "per_agent_divisions":
    8}], "scope": "Exact tiny pooling examples; not training, physical communication
    cost, author-code behavior, independent actions, or empirical generalization evidence."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T093019Z-communication-neural-network.json
  accessed_at: '2026-10-13T09:30:32Z'
  support: supports
  summary: Compared all 442 pinned AIO and 598 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    8, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered
    24 AIO and 51 native definitions, with every matched definition read. 4 full annotated
    AIO node/edge/generated contexts and 5 full native records were inspected. CommNet
    is the named Communication Neural Net with shared agent modules and exclude-self
    mean communication. It differs from VAIN learned-distance weights, Interaction
    Network pair-specific learned effects, and the maintained GAT, GIN and GraphSAGE
    constructions. The neural architecture maps broadly to ANN; recurrence and local
    connectivity are extensions, not essential identity conditions.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T09:30:32Z'
  support: supports
  summary: Four annotated AIO nodes, all incident edges and generated YAMLs were inspected.
    Shared learned neural modules support broad ArtificialNeuralNetwork. The base
    architecture does not require recurrent dynamics, named GCN computation or a conditional-dependence
    task.
- evidence_id: sukhbaatar2016
  kind: primary_source
  reference: https://papers.neurips.cc/paper/6398-learning-multiagent-communication-with-backpropagation.pdf
  locator: All nine main-paper PDF pages read before curation; selected method/evaluation
    pages reread after capture. Supplement, other versions and author code not inspected.
    No benchmark, training or runtime replication.
  accessed_at: '2026-10-13T09:04:13Z'
  snapshot_sha256: db09430a0aeb9c17de8dbd3409ce30804de20b3f31a3e289c7da2eb1da8aa354
  support: supports
  summary: NIPS2016 proceedings PDF, nine pages, all visually read including equations,
    figures, tables and references. Authors and proceedings identity agree with the
    primary landing page. Locators are PDF/printed pages1–9. Supplement, other manuscript
    versions and author code not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/communication-network-boundaries.py
  accessed_at: '2026-10-13T09:31:36Z'
  snapshot_sha256: 6d8ceed5f7d0a1d8854c949ee634deb3055bdca4fa3b8a196d547ff5e1edbd66
  support: supports
  summary: Exact rational chosen states distinguish exclude-self means from sums and
    inclusive/local means, demonstrate mean collisions, J1undefinedformula, all6permutations
    and shared-total arithmetic counts. No learned-network, physical-message-cost
    or benchmark replication claim.
assessments:
- assessment_id: identity
  area: identity
  topic: Communication Neural Network
  outcome: supported
  target_ids:
  - AIMech:CommunicationNeuralNetwork
  evidence_ids:
  - identity
  - sukhbaatar2016
  summary: Retain this distinct DRAFT architecture.
  details: CommNet is the named continuous mean-communication architecture. It is
    distinct from learned-distance VAIN, pairwise Interaction Network effects and
    GAT/GIN/GraphSAGE. Recurrence and neighborhood restrictions are optional extensions.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:CommunicationNeuralNetwork
  evidence_ids:
  - mapping
  - sukhbaatar2016
  summary: The declared broad AIO mapping is supported.
  details: Four annotated AIO nodes, all incident edges and generated YAMLs were inspected.
    Shared learned neural modules support broad ArtificialNeuralNetwork. The base
    architecture does not require recurrent dynamics, named GCN computation or a conditional-dependence
    task.
- assessment_id: continuous-exclude-self-communication
  area: evidence
  topic: continuous-exclude-self-communication
  outcome: supported
  target_ids:
  - AIMech:CommunicationNeuralNetwork
  evidence_ids:
  - sukhbaatar2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equation1updates hidden states from currentcommunication; Eq2forms nextcommunication
    from otherupdatedstates. Initialcommunication0 and sharedagentmodules are explicit;
    layerweightsharing is not asserted. Baseactionhead andsampledactions matchp2.
- assessment_id: mean-and-empty-neighborhood-boundaries
  area: evidence
  topic: mean-and-empty-neighborhood-boundaries
  outcome: supported
  target_ids:
  - AIMech:CommunicationNeuralNetwork
  evidence_ids:
  - sukhbaatar2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: J-1and|N(j)|denominators exclude statedemptycases without an implementation
    convention. Exact examples distinguish globalexclude-self,inclusiveandlocalmeans
    and showmean collisions. No artificial zero-neighbor behavior is invented.
- assessment_id: permutation-and-computation-boundaries
  area: evidence
  topic: permutation-and-computation-boundaries
  outcome: supported
  target_ids:
  - AIMech:CommunicationNeuralNetwork
  evidence_ids:
  - sukhbaatar2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The block matrix commutes with agent permutation; corresponding output
    arrays permute. Constructed6permutations checkthis; they do not establish an unchanged
    orderedarray. Totalminusself is a direct algebraic aggregation optimization, not
    a physicalnetworkcost claim.
- assessment_id: extensions-and-training-boundaries
  area: evidence
  topic: extensions-and-training-boundaries
  outcome: supported
  target_ids:
  - AIMech:CommunicationNeuralNetwork
  evidence_ids:
  - sukhbaatar2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section2.2describes localmeans,skiporiginalencoding andtemporalrecurrentalternatives.
    Section3rejectsfixedpointnecessity. Continuouscommunication permitsbackprop butdiscreteaction
    samplingneedsappropriatetrainingsignals; the policygradientdiscretecommunicationbaseline
    remains separate.
- assessment_id: cooperative-task-evaluation
  area: evidence
  topic: cooperative-task-evaluation
  outcome: supported
  target_ids:
  - AIMech:CommunicationNeuralNetwork
  evidence_ids:
  - sukhbaatar2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Fullcooperationsharedreward isexplicit. Lever5from500 poolanddistinctcoverage,trafficfailure
    andcombatwinpercent are distinctprotocols. The fixed simulation,variantandseedsettingspreclude
    universalcoordinationclaims.
- assessment_id: global-answer-variant-and-evidence-limits
  area: evidence
  topic: global-answer-variant-and-evidence-limits
  outcome: supported
  target_ids:
  - AIMech:CommunicationNeuralNetwork
  evidence_ids:
  - sukhbaatar2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: bAbIp8sumsfinalsentencehiddenstatesafterK2andusesglobalanswerhead. Table4CommNet7.1error
    exceedsMemN2N4.2andDMN+2.8; no universalbestclaim. PCA/brakingcorrelations are
    notcausalproof; heterogeneous/largepopulationsfutureworkexplicit.
- assessment_id: constructed-boundaries
  area: consistency
  topic: exclude-self means, empty-neighborhood formulas, per-agent equivariance,
    communication steps and task-specific variants
  outcome: supported
  target_ids:
  - AIMech:CommunicationNeuralNetwork
  evidence_ids:
  - sukhbaatar2016
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact rational chosen states distinguish exclude-self means from sums and
    inclusive/local means, demonstrate mean collisions, J1undefinedformula, all6permutations
    and shared-total arithmetic counts. No learned-network, physical-message-cost
    or benchmark replication claim.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:CommunicationNeuralNetwork
  evidence_ids:
  - identity
  - mapping
  - sukhbaatar2016
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Read every maintained field and all four mapping
    YAMLs after capture. Reread communication timing and exclude-self normalization,
    block symmetry, optional extensions, training distinctions, evaluation tables
    and global question-answering readout. Recomputed exact rational examples.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 599 native and 442 unchanged generated records.
  The 783-entry main frontier retains 477 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All nine main-paper pages read including figures,tables,formulas and references;
  supplement and author code not inspected.
- No author code, training, paid service, hardware measurement or empirical replication.
  Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
