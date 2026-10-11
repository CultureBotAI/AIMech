# Scientific self-review of five state-space foundation concepts

- Review: 20261011T043528Z-state-space-foundations
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T04:35:28Z
- Finished UTC: 2026-10-11T04:35:28Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All five scoped concepts have inspected primary-method support and explicit AIO mapping rationales. Family/operator distinctions, the unrelated HiPPO acronym and FlashConv execution versus layer scope are retained. Numerical, finite-dimension and printed-pseudocode limitations prevent overclaiming; no actionable unresolved defect was identified in the curated assertions.

## Scope And Provenance

Identity, definition, mechanism evidence, version metadata, limitations and mappings for five state-space foundation additions.

Selection: Exactly the five entries in the state-space-foundations discovery report; no sampling.
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base c50a9b8c808e05fc36af2e2d23652eb28dcbbff5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:S4D | data/curated/S4D.yaml | maintained | Diagonal structured state space model |
| AIMech:HiPPOProjection | data/curated/HiPPOProjection.yaml | maintained | High-order polynomial projection operators |
| AIMech:HiPPOLegS | data/curated/HiPPOLegS.yaml | maintained | Scaled Legendre HiPPO operator |
| AIMech:LinearStateSpaceLayer | data/curated/LinearStateSpaceLayer.yaml | maintained | Linear state-space layer |
| AIMech:FlashConv | data/curated/FlashConv.yaml | maintained | FlashConv |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:S4D, AIMech:HiPPOProjection, AIMech:HiPPOLegS, AIMech:LinearStateSpaceLayer, AIMech:FlashConv | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate | passed | True | AIMech:S4D, AIMech:HiPPOProjection, AIMech:HiPPOLegS, AIMech:LinearStateSpaceLayer, AIMech:FlashConv | Checked 442 record(s); 0 failed.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-curated | passed | True | AIMech:S4D, AIMech:HiPPOProjection, AIMech:HiPPOLegS, AIMech:LinearStateSpaceLayer, AIMech:FlashConv | Checked 90 curated concept record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli seed --check | passed | True | AIMech:S4D, AIMech:HiPPOProjection, AIMech:HiPPOLegS, AIMech:LinearStateSpaceLayer, AIMech:FlashConv | AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-history --base HEAD | passed | True | AIMech:S4D, AIMech:HiPPOProjection, AIMech:HiPPOLegS, AIMech:LinearStateSpaceLayer, AIMech:FlashConv | Checked 16 history record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python scripts/record_review.py check | passed | True | AIMech:S4D, AIMech:HiPPOProjection, AIMech:HiPPOLegS, AIMech:LinearStateSpaceLayer, AIMech:FlashConv | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 15,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class<br> |
| just check | passed | True | AIMech:S4D, AIMech:HiPPOProjection, AIMech:HiPPOLegS, AIMech:LinearStateSpaceLayer, AIMech:FlashConv | All checks passed!<br>........................................................................ [ 31%]<br>........................................................................ [ 63%]<br>........................................................................ [ 94%]<br>.........sss                                                             [100%]<br>225 passed, 3 skipped in 49.84s<br>Checked 442 record(s); 0 failed.<br>Checked 90 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 16 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 15,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:S4D, AIMech:HiPPOProjection, AIMech:HiPPOLegS, AIMech:LinearStateSpaceLayer, AIMech:FlashConv | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Concept identity, primary-method support and abstraction level

evidence: supported. Targets: AIMech:S4D.

S4D is the family defined by Gu and colleagues, distinguished from S4's diagonal-plus-low-rank construction. The paper separates the earlier DSS configuration and the S4D-LegS, S4D-Inv and S4D-Lin initialization choices rather than treating all diagonal models as identical.

Algebraic diagonalizability does not guarantee numerically stable representation or successful optimization; initialization and discretization remain explicit choices. S4D-LegS convergence to the corresponding S4 dynamics is an infinite-state-size statement, not exact equality of all finite S4D and S4 models. The inverse-law spectral asymptotics are presented as Conjecture 4, not a proved theorem. No universal performance advantage is asserted.

### Concept identity, primary-method support and abstraction level

evidence: supported. Targets: AIMech:HiPPOProjection.

HiPPO denotes the general projection-and-coefficient framework, not one fixed state matrix, a complete recurrent neural network, or only the scaled-Legendre instantiation HiPPO-LegS. The qualified acronym distinguishes this operator family from the unrelated highlight-replay PPO method.

Optimality is relative to the chosen measure and finite polynomial subspace, not lossless recovery of arbitrary history or optimal downstream prediction. A tractable closed-form recurrence is not asserted for every arbitrary measure. The translated-Legendre sliding-window update additionally approximates the unavailable boundary value; numerical discretization adds its own approximation.

### Concept identity, primary-method support and abstraction level

evidence: supported. Targets: AIMech:HiPPOLegS.

HiPPO-LegS is the scaled-Legendre instantiation of the broader HiPPO framework. Its time-dependent operator differs from a fixed state matrix used to initialize a later S4 model and from the fixed-width translated-Legendre window.

The displayed differential formula contains 1/t and applies for positive t; an executable initialization at the time origin is not supplied by this record. Equation 4 illustrates an Euler discretization; the paper also uses bilinear and zero-order-hold schemes. The operator's approximation properties do not guarantee arbitrary downstream-network accuracy.

### Concept identity, primary-method support and abstraction level

evidence: supported. Targets: AIMech:LinearStateSpaceLayer.

LSSL denotes Gu and colleagues' component with state-space parameters and timescale, not the complete deep LSSL network, every recurrent network, or S4's later structured parameterization and kernel algorithm.

The simple convolution expression assumes zero initial state; a nonzero starting state contributes an additional term. The layer is linear; nonlinear expressive power of stacked networks is not a property of a single standalone LSSL. Efficient recurrent updates and kernel construction depend on the selected state-matrix structure.

### Concept identity, primary-method support and abstraction level

evidence: supported. Targets: AIMech:FlashConv.

FlashConv is the convolution-execution contribution in the H3 paper, distinct from the H3 layer and from FlashAttention's attention-computation algorithm.

The paper's 8K on-chip threshold concerns its stated A100 setting; no device-independent cutoff or wall-clock speedup is asserted. Block FFT may use more arithmetic than a conventional FFT while exploiting specialized matrix hardware. The printed Algorithm 2 mixes chunk variable names and its exact boundary indexing was not implemented or verified here. This record supports the execution strategy, not a certified literal transcription of the pseudocode.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:S4D, AIMech:HiPPOProjection, AIMech:HiPPOLegS, AIMech:LinearStateSpaceLayer, AIMech:FlashConv. Retain S4D as a model family, HiPPO as a projection-operator framework, HiPPO-LegS as its explicitly time-dependent scaled-Legendre instance, LSSL as a sequence layer and FlashConv as an execution algorithm. Broader/narrower scope and shared computational ingredients do not establish exact identity.
- defer: AIMech:S4D, AIMech:HiPPOProjection, AIMech:HiPPOLegS, AIMech:LinearStateSpaceLayer, AIMech:FlashConv. Additional S4D initialization records, translated HiPPO operators, complete LSSL networks, unrelated HiPPO acronyms and executable FlashConv indexing require separately scoped follow-up. The current records do not silently resolve those questions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity-search | research/discovery/20261011T043332Z-state-space-foundations.json | supports | All 442 AIO labels/scoped synonyms and 85 preceding native identities were compared, with hidden/ignored-inclusive text searches of both checkouts. Hits were source references, earlier leads, adjacent H3 material and incidental environment substrings. An initial broader HiPPO search found the distinct highlight-replay PPO lead; primary identity follow-up resolved the different authors, title and scope, and the new operator uses a qualified alias and descriptive ID. HiPPO-LegS is a named specific operator within the broader framework, not an exact duplicate. |
| mapping | sources/aio/aio.json; Model, MathematicalFunction, Layer, Convolution1DLayer and considered neighboring classes | supports | S4D broad_match Model; HiPPO projection and HiPPO-LegS broad_match MathematicalFunction as coefficient-valued operators; LSSL broad_match Layer; FlashConv related_match Convolution1DLayer because it computes the operation rather than denoting a layer. FeatureExtraction, DimensionalityReduction, MemoryCellLayer and recurrent-network concepts were considered as neighbors without asserting equivalent identities. |
| acronym-context | https://sai.jlu.edu.cn/info/1026/4980.htm; Article title and research summary, published 2025-01-25 | context_only | The author-university announcement confirms a distinct HiPPO highlight-replay PPO identity. It is used for acronym discrimination only, not unseen method evidence. Direct publisher open returned HTTP 403. |
| s4d-method | https://proceedings.neurips.cc/paper_files/paper/2022/file/e9a32fade47b906de908431991440f7c-Paper-Conference.pdf; Sections 3.1–3.4 and 4, equations 6–9 and Table 1, PDF/printed pp. 4–6 | supports | Discretize a diagonal continuous-time state model using bilinear or zero-order-hold rules. Kernel entries are sums of output and input coefficients multiplied by powers of the discretized diagonal state entries. Constrain the continuous state eigenvalue real parts using the chosen parameterization and initialize their spectrum according to the selected variant. Rendered pages actually inspected: 4, 5, 6. |
| hippoprojection-method | https://proceedings.neurips.cc/paper_files/paper/2020/file/102f0bb6efb3a6128a3c750dd16729be-Paper.pdf; Sections 2.1–2.4, Definition 1 and Figure 1, PDF/printed pp. 2–5 | supports | At each time, project the available signal history onto a polynomial subspace by minimizing the measure-weighted squared approximation error, then extract coefficients in the associated orthogonal basis. For the derived measure families, differentiating those coefficients yields linear differential dynamics that can be discretized as online recurrences. Rendered pages actually inspected: 3, 4, 5. |
| hippolegs-method | https://proceedings.neurips.cc/paper_files/paper/2020/file/102f0bb6efb3a6128a3c750dd16729be-Paper.pdf; Section 3, Theorem 2, equations 3–4 and footnote 3, with Sections 2.1–2.4 for projection context; PDF/printed pp. 3–5 | supports | Use the normalized uniform measure on [0,t] and the corresponding Legendre basis. For positive time, the coefficient derivative is minus A times the current coefficient vector divided by t, plus B times the current signal divided by t; the source specifies a lower-triangular A and a fixed B and derives discrete recurrences from these dynamics. Rendered pages actually inspected: 3, 4, 5. |
| linearstatespacelayer-method | https://proceedings.neurips.cc/paper_files/paper/2021/file/05546b0e38ab9175cd905eebcc6ebb76-Paper.pdf; Section 2 equations 3–5 and Sections 3.1–3.3, equations 6–7, PDF/printed pp. 4–6 | supports | Discretize the state dynamics using a step size to obtain a recurrent state update and linear output map. With zero initial state, powers of the discretized state matrix between input and output projections form the convolution kernel. Separate feature channels use their own broadcast input/output parameters and timescales; complete networks add further layers and connections. Rendered pages actually inspected: 4, 5, 6. |
| flashconv-method | https://arxiv.org/pdf/2212.14052v3; Sections 4.1–4.2 and Algorithm 2, PDF/printed pp. 6–7 | supports | Fuse the FFT, pointwise spectral product and inverse FFT to avoid intermediate off-chip transfers; factor the FFT into block matrix multiplications suited to specialized hardware. When the sequence exceeds the chosen on-chip working capacity, compute chunk convolutions and propagate the state-space boundary state between chunks. Rendered pages actually inspected: 6, 7. |

## Limits And Additional Notes

- Scientific self-review, not independent approval or benchmark reproduction.
- S4D spectral expressivity is not a finite-precision or optimization guarantee; a stated conjecture remains a conjecture.
- Projection optimality is conditional on measure and subspace. HiPPO-LegS positive-time dynamics are not an executable time-zero initialization rule.
- FlashConv literal pseudocode and state-boundary conventions are not certified; the high-level execution strategy is supported.
- S4D metadata follows the inspected PDF where landing-page author order/code-line-count differs.
- All records remain DRAFT and discovery has not saturated.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T043528Z-state-space-foundations
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of five state-space foundation concepts
started_at: '2026-10-11T04:35:28Z'
finished_at: '2026-10-11T04:35:28Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The same agent researched, authored and adversarially reviewed
    these records; not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All five scoped concepts have inspected primary-method support and explicit
  AIO mapping rationales. Family/operator distinctions, the unrelated HiPPO acronym
  and FlashConv execution versus layer scope are retained. Numerical, finite-dimension
  and printed-pseudocode limitations prevent overclaiming; no actionable unresolved
  defect was identified in the curated assertions.
source:
  git_revision: c50a9b8c808e05fc36af2e2d23652eb28dcbbff5
  state: working_tree
  inputs:
  - path: data/curated/FlashConv.yaml
    sha256: 9361357934f34a8ba8aede408c352bdffa59dc000185d7dd912a8a86b15d119c
    role: target
  - path: data/curated/HiPPOLegS.yaml
    sha256: 3216de7984f51d3a0adf49572264845ed9cb8ed8d6b5369b0071bf82e1cfad34
    role: target
  - path: data/curated/HiPPOProjection.yaml
    sha256: 97e0821fa005dd0614842d2baffc5a09034c6d1b303e6062c880055bf26ecb08
    role: target
  - path: data/curated/LinearStateSpaceLayer.yaml
    sha256: 05d7d834a8c0db4c33613384cde4a250838290cce6960fda10e7209da318c151
    role: target
  - path: data/curated/S4D.yaml
    sha256: 631514e163f900cfb28d704acc2b87868a621db97b7501b7414b66c586cbae4a
    role: target
  - path: docs/curated-concepts.md
    sha256: ce644f9e755d9a1a3c105bde82a0e1b7defbf5e93e4c91f86ba050370cf74bc3
    role: context
  - path: research/discovery/20261011T043332Z-state-space-foundations.json
    sha256: 0e501ec4f26bcdbea69e47310b4965d39b3123f8422e8355937097c30d91c422
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 0600ec8ca628d2dac611f2a068074ebcd4b83b6b5f31832a32dbc4f4bfa35b06
    role: context
  - path: src/aimech/importer.py
    sha256: 7c2dd8e12f18b76cfb5ed4acc7e1901ae9a968b3a6c7a9d62cb260bc2f1ad3ab
    role: context
  - path: src/aimech/schema/aimech.yaml
    sha256: 5a54dafe2fc17bc027e14bc3a2829b265cbb34427ad58eef63fe99616e17b852
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: f47a2fa70fc2ff16a2bfdead30472068afa1133710819831b081b4bb6224825a
    role: context
targets:
- target_id: AIMech:S4D
  path: data/curated/S4D.yaml
  label: Diagonal structured state space model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/S4D.yaml
    role: maintained native concept
- target_id: AIMech:HiPPOProjection
  path: data/curated/HiPPOProjection.yaml
  label: High-order polynomial projection operators
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HiPPOProjection.yaml
    role: maintained native concept
- target_id: AIMech:HiPPOLegS
  path: data/curated/HiPPOLegS.yaml
  label: Scaled Legendre HiPPO operator
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HiPPOLegS.yaml
    role: maintained native concept
- target_id: AIMech:LinearStateSpaceLayer
  path: data/curated/LinearStateSpaceLayer.yaml
  label: Linear state-space layer
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LinearStateSpaceLayer.yaml
    role: maintained native concept
- target_id: AIMech:FlashConv
  path: data/curated/FlashConv.yaml
  label: FlashConv
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FlashConv.yaml
    role: maintained native concept
scope:
  description: Identity, definition, mechanism evidence, version metadata, limitations
    and mappings for five state-space foundation additions.
  selection: Exactly the five entries in the state-space-foundations discovery report;
    no sampling.
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - AIMech:S4D
  - AIMech:HiPPOProjection
  - AIMech:HiPPOLegS
  - AIMech:LinearStateSpaceLayer
  - AIMech:FlashConv
  exclusions:
  - target: Executable FlashConv pseudocode correctness and empirical performance
    reason: The record describes the inspected execution strategy and explicitly does
      not certify the printed indexing or hardware-independent speedups.
  - target: Separate acronym methods and uncurated named variants
    reason: The replay method lacks inspected full-method evidence here; additional
      variants retain pending identity/method scope.
checks:
- check_id: required-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:S4D
  - AIMech:HiPPOProjection
  - AIMech:HiPPOLegS
  - AIMech:LinearStateSpaceLayer
  - AIMech:FlashConv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
- check_id: required-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate
  status: passed
  required: true
  target_ids:
  - AIMech:S4D
  - AIMech:HiPPOProjection
  - AIMech:HiPPOLegS
  - AIMech:LinearStateSpaceLayer
  - AIMech:FlashConv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 442 record(s); 0 failed.

    '
- check_id: required-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:S4D
  - AIMech:HiPPOProjection
  - AIMech:HiPPOLegS
  - AIMech:LinearStateSpaceLayer
  - AIMech:FlashConv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 90 curated concept record(s); 0 error(s).

    '
- check_id: required-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:S4D
  - AIMech:HiPPOProjection
  - AIMech:HiPPOLegS
  - AIMech:LinearStateSpaceLayer
  - AIMech:FlashConv
  exit_code: 0
  expected_exit_code: 0
  summary: 'AIO: 442 records; 0 missing, 0 changed, 0 unexpected.

    '
- check_id: required-4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-history --base HEAD
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-history --base HEAD
  status: passed
  required: true
  target_ids:
  - AIMech:S4D
  - AIMech:HiPPOProjection
  - AIMech:HiPPOLegS
  - AIMech:LinearStateSpaceLayer
  - AIMech:FlashConv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 16 history record(s); 0 error(s).

    '
- check_id: required-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:S4D
  - AIMech:HiPPOProjection
  - AIMech:HiPPOLegS
  - AIMech:LinearStateSpaceLayer
  - AIMech:FlashConv
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 15,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\ntopClass is deprecated - use top_class\n"
- check_id: required-6
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:S4D
  - AIMech:HiPPOProjection
  - AIMech:HiPPOLegS
  - AIMech:LinearStateSpaceLayer
  - AIMech:FlashConv
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 31%]\n........................................................................\
    \ [ 63%]\n........................................................................\
    \ [ 94%]\n.........sss                                                       \
    \      [100%]\n225 passed, 3 skipped in 49.84s\nChecked 442 record(s); 0 failed.\n\
    Checked 90 curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing,\
    \ 0 changed, 0 unexpected.\nChecked 16 history record(s); 0 error(s).\n{\n  \"\
    repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 15,\n  \"coverage\"\
    : \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-7
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:S4D
  - AIMech:HiPPOProjection
  - AIMech:HiPPOLegS
  - AIMech:LinearStateSpaceLayer
  - AIMech:FlashConv
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity-search
  kind: search
  reference: research/discovery/20261011T043332Z-state-space-foundations.json
  accessed_at: '2026-10-11T04:35:28Z'
  support: supports
  summary: All 442 AIO labels/scoped synonyms and 85 preceding native identities were
    compared, with hidden/ignored-inclusive text searches of both checkouts. Hits
    were source references, earlier leads, adjacent H3 material and incidental environment
    substrings. An initial broader HiPPO search found the distinct highlight-replay
    PPO lead; primary identity follow-up resolved the different authors, title and
    scope, and the new operator uses a qualified alias and descriptive ID. HiPPO-LegS
    is a named specific operator within the broader framework, not an exact duplicate.
  search_scope: All 442 AIO labels and scoped synonyms, 85 preceding native identities
    and ignored/hidden-inclusive text searches of both checkouts.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Model, MathematicalFunction, Layer, Convolution1DLayer and considered neighboring
    classes
  accessed_at: '2026-10-11T04:35:28Z'
  support: supports
  summary: S4D broad_match Model; HiPPO projection and HiPPO-LegS broad_match MathematicalFunction
    as coefficient-valued operators; LSSL broad_match Layer; FlashConv related_match
    Convolution1DLayer because it computes the operation rather than denoting a layer.
    FeatureExtraction, DimensionalityReduction, MemoryCellLayer and recurrent-network
    concepts were considered as neighbors without asserting equivalent identities.
- evidence_id: acronym-context
  kind: primary_source
  reference: https://sai.jlu.edu.cn/info/1026/4980.htm
  locator: Article title and research summary, published 2025-01-25
  accessed_at: '2026-10-11T04:35:28Z'
  support: context_only
  summary: The author-university announcement confirms a distinct HiPPO highlight-replay
    PPO identity. It is used for acronym discrimination only, not unseen method evidence.
    Direct publisher open returned HTTP 403.
- evidence_id: s4d-method
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2022/file/e9a32fade47b906de908431991440f7c-Paper-Conference.pdf
  locator: Sections 3.1–3.4 and 4, equations 6–9 and Table 1, PDF/printed pp. 4–6
  accessed_at: '2026-10-11T04:28:33Z'
  snapshot_sha256: 95b3596262fa4bd7d853b25d3a43e1f221f3bd1ee1ac960e767414982f484aa9
  support: supports
  summary: 'Discretize a diagonal continuous-time state model using bilinear or zero-order-hold
    rules. Kernel entries are sums of output and input coefficients multiplied by
    powers of the discretized diagonal state entries. Constrain the continuous state
    eigenvalue real parts using the chosen parameterization and initialize their spectrum
    according to the selected variant. Rendered pages actually inspected: 4, 5, 6.'
- evidence_id: hippoprojection-method
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2020/file/102f0bb6efb3a6128a3c750dd16729be-Paper.pdf
  locator: Sections 2.1–2.4, Definition 1 and Figure 1, PDF/printed pp. 2–5
  accessed_at: '2026-10-11T04:28:33Z'
  snapshot_sha256: e99e0063517ac2e8d6e04aa8f7e621c958fcf3429697eddaa56cf934628a831a
  support: supports
  summary: 'At each time, project the available signal history onto a polynomial subspace
    by minimizing the measure-weighted squared approximation error, then extract coefficients
    in the associated orthogonal basis. For the derived measure families, differentiating
    those coefficients yields linear differential dynamics that can be discretized
    as online recurrences. Rendered pages actually inspected: 3, 4, 5.'
- evidence_id: hippolegs-method
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2020/file/102f0bb6efb3a6128a3c750dd16729be-Paper.pdf
  locator: Section 3, Theorem 2, equations 3–4 and footnote 3, with Sections 2.1–2.4
    for projection context; PDF/printed pp. 3–5
  accessed_at: '2026-10-11T04:28:33Z'
  snapshot_sha256: e99e0063517ac2e8d6e04aa8f7e621c958fcf3429697eddaa56cf934628a831a
  support: supports
  summary: 'Use the normalized uniform measure on [0,t] and the corresponding Legendre
    basis. For positive time, the coefficient derivative is minus A times the current
    coefficient vector divided by t, plus B times the current signal divided by t;
    the source specifies a lower-triangular A and a fixed B and derives discrete recurrences
    from these dynamics. Rendered pages actually inspected: 3, 4, 5.'
- evidence_id: linearstatespacelayer-method
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2021/file/05546b0e38ab9175cd905eebcc6ebb76-Paper.pdf
  locator: Section 2 equations 3–5 and Sections 3.1–3.3, equations 6–7, PDF/printed
    pp. 4–6
  accessed_at: '2026-10-11T04:28:33Z'
  snapshot_sha256: 32c1802b55e5c3f1d29d3509c544e3e58b52fbc68a4b50dcef2c70c5bb17ec5e
  support: supports
  summary: 'Discretize the state dynamics using a step size to obtain a recurrent
    state update and linear output map. With zero initial state, powers of the discretized
    state matrix between input and output projections form the convolution kernel.
    Separate feature channels use their own broadcast input/output parameters and
    timescales; complete networks add further layers and connections. Rendered pages
    actually inspected: 4, 5, 6.'
- evidence_id: flashconv-method
  kind: primary_source
  reference: https://arxiv.org/pdf/2212.14052v3
  locator: Sections 4.1–4.2 and Algorithm 2, PDF/printed pp. 6–7
  accessed_at: '2026-10-11T04:20:57Z'
  snapshot_sha256: de923022ffc5e53d430f0af72286cec26f32d03c9e2fd3686938a5d62811eae2
  support: supports
  summary: 'Fuse the FFT, pointwise spectral product and inverse FFT to avoid intermediate
    off-chip transfers; factor the FFT into block matrix multiplications suited to
    specialized hardware. When the sequence exceeds the chosen on-chip working capacity,
    compute chunk convolutions and propagate the state-space boundary state between
    chunks. Rendered pages actually inspected: 6, 7.'
assessments:
- assessment_id: s4d-method
  area: evidence
  topic: Concept identity, primary-method support and abstraction level
  outcome: supported
  target_ids:
  - AIMech:S4D
  evidence_ids:
  - s4d-method
  - identity-search
  - mapping
  summary: S4D is the family defined by Gu and colleagues, distinguished from S4's
    diagonal-plus-low-rank construction. The paper separates the earlier DSS configuration
    and the S4D-LegS, S4D-Inv and S4D-Lin initialization choices rather than treating
    all diagonal models as identical.
  details: Algebraic diagonalizability does not guarantee numerically stable representation
    or successful optimization; initialization and discretization remain explicit
    choices. S4D-LegS convergence to the corresponding S4 dynamics is an infinite-state-size
    statement, not exact equality of all finite S4D and S4 models. The inverse-law
    spectral asymptotics are presented as Conjecture 4, not a proved theorem. No universal
    performance advantage is asserted.
  dimensions:
  - name: concept-kind
    value: model_family
    definition: The source-defined level of abstraction, including family versus specific
      operator and layer versus execution algorithm.
    evidence_ids:
    - s4d-method
  - name: mapping-direction
    value: broad_match to AIO:Model
    definition: This is a parameterized family of linear sequence models; Model is
      broader and does not conflate the core with the nonlinear architectures built
      from it.
    evidence_ids:
    - s4d-method
    - mapping
- assessment_id: hippoprojection-method
  area: evidence
  topic: Concept identity, primary-method support and abstraction level
  outcome: supported
  target_ids:
  - AIMech:HiPPOProjection
  evidence_ids:
  - hippoprojection-method
  - identity-search
  - mapping
  - acronym-context
  summary: HiPPO denotes the general projection-and-coefficient framework, not one
    fixed state matrix, a complete recurrent neural network, or only the scaled-Legendre
    instantiation HiPPO-LegS. The qualified acronym distinguishes this operator family
    from the unrelated highlight-replay PPO method.
  details: Optimality is relative to the chosen measure and finite polynomial subspace,
    not lossless recovery of arbitrary history or optimal downstream prediction. A
    tractable closed-form recurrence is not asserted for every arbitrary measure.
    The translated-Legendre sliding-window update additionally approximates the unavailable
    boundary value; numerical discretization adds its own approximation.
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: The source-defined level of abstraction, including family versus specific
      operator and layer versus execution algorithm.
    evidence_ids:
    - hippoprojection-method
  - name: mapping-direction
    value: broad_match to AIO:MathematicalFunction
    definition: Definition 1 and the coefficient/projection composition define operators
      mapping an input function to coefficient values through time. MathematicalFunction
      is broader than this specific family of mathematical rules; no complete neural-network
      identity is asserted.
    evidence_ids:
    - hippoprojection-method
    - mapping
- assessment_id: hippolegs-method
  area: evidence
  topic: Concept identity, primary-method support and abstraction level
  outcome: supported
  target_ids:
  - AIMech:HiPPOLegS
  evidence_ids:
  - hippolegs-method
  - identity-search
  - mapping
  summary: HiPPO-LegS is the scaled-Legendre instantiation of the broader HiPPO framework.
    Its time-dependent operator differs from a fixed state matrix used to initialize
    a later S4 model and from the fixed-width translated-Legendre window.
  details: The displayed differential formula contains 1/t and applies for positive
    t; an executable initialization at the time origin is not supplied by this record.
    Equation 4 illustrates an Euler discretization; the paper also uses bilinear and
    zero-order-hold schemes. The operator's approximation properties do not guarantee
    arbitrary downstream-network accuracy.
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: The source-defined level of abstraction, including family versus specific
      operator and layer versus execution algorithm.
    evidence_ids:
    - hippolegs-method
  - name: mapping-direction
    value: broad_match to AIO:MathematicalFunction
    definition: This specific scaled-Legendre projection maps signal history to a
      coefficient-valued function. It is a mathematical operator, not itself a complete
      neural network or external memory store.
    evidence_ids:
    - hippolegs-method
    - mapping
- assessment_id: linearstatespacelayer-method
  area: evidence
  topic: Concept identity, primary-method support and abstraction level
  outcome: supported
  target_ids:
  - AIMech:LinearStateSpaceLayer
  evidence_ids:
  - linearstatespacelayer-method
  - identity-search
  - mapping
  summary: LSSL denotes Gu and colleagues' component with state-space parameters and
    timescale, not the complete deep LSSL network, every recurrent network, or S4's
    later structured parameterization and kernel algorithm.
  details: The simple convolution expression assumes zero initial state; a nonzero
    starting state contributes an additional term. The layer is linear; nonlinear
    expressive power of stacked networks is not a property of a single standalone
    LSSL. Efficient recurrent updates and kernel construction depend on the selected
    state-matrix structure.
  dimensions:
  - name: concept-kind
    value: layer
    definition: The source-defined level of abstraction, including family versus specific
      operator and layer versus execution algorithm.
    evidence_ids:
    - linearstatespacelayer-method
  - name: mapping-direction
    value: broad_match to AIO:Layer
    definition: The source defines a sequence-representation transformation with a
      standard layer interface and separately composes complete networks. AIO Layer
      is the broader component class.
    evidence_ids:
    - linearstatespacelayer-method
    - mapping
- assessment_id: flashconv-method
  area: evidence
  topic: Concept identity, primary-method support and abstraction level
  outcome: supported
  target_ids:
  - AIMech:FlashConv
  evidence_ids:
  - flashconv-method
  - identity-search
  - mapping
  summary: FlashConv is the convolution-execution contribution in the H3 paper, distinct
    from the H3 layer and from FlashAttention's attention-computation algorithm.
  details: The paper's 8K on-chip threshold concerns its stated A100 setting; no device-independent
    cutoff or wall-clock speedup is asserted. Block FFT may use more arithmetic than
    a conventional FFT while exploiting specialized matrix hardware. The printed Algorithm
    2 mixes chunk variable names and its exact boundary indexing was not implemented
    or verified here. This record supports the execution strategy, not a certified
    literal transcription of the pseudocode.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: The source-defined level of abstraction, including family versus specific
      operator and layer versus execution algorithm.
    evidence_ids:
    - flashconv-method
  - name: mapping-direction
    value: related_match to AIO:Convolution1DLayer
    definition: FlashConv computes one-dimensional sequence convolutions, an operation
      used by this AIO layer. The algorithm concerns execution and state passing rather
      than denoting the layer itself, so the mapping is related rather than broader-class
      membership.
    evidence_ids:
    - flashconv-method
    - mapping
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:S4D
  - AIMech:HiPPOProjection
  - AIMech:HiPPOLegS
  - AIMech:LinearStateSpaceLayer
  - AIMech:FlashConv
  evidence_ids:
  - identity-search
  - mapping
  - acronym-context
  - s4d-method
  - hippoprojection-method
  - hippolegs-method
  - linearstatespacelayer-method
  - flashconv-method
  rationale: Retain S4D as a model family, HiPPO as a projection-operator framework,
    HiPPO-LegS as its explicitly time-dependent scaled-Legendre instance, LSSL as
    a sequence layer and FlashConv as an execution algorithm. Broader/narrower scope
    and shared computational ingredients do not establish exact identity.
- action: defer
  target_ids:
  - AIMech:S4D
  - AIMech:HiPPOProjection
  - AIMech:HiPPOLegS
  - AIMech:LinearStateSpaceLayer
  - AIMech:FlashConv
  evidence_ids:
  - acronym-context
  - s4d-method
  - hippoprojection-method
  - hippolegs-method
  - linearstatespacelayer-method
  - flashconv-method
  rationale: Additional S4D initialization records, translated HiPPO operators, complete
    LSSL networks, unrelated HiPPO acronyms and executable FlashConv indexing require
    separately scoped follow-up. The current records do not silently resolve those
    questions.
limitations:
- Scientific self-review, not independent approval or benchmark reproduction.
- S4D spectral expressivity is not a finite-precision or optimization guarantee; a
  stated conjecture remains a conjecture.
- Projection optimality is conditional on measure and subspace. HiPPO-LegS positive-time
  dynamics are not an executable time-zero initialization rule.
- FlashConv literal pseudocode and state-boundary conventions are not certified; the
  high-level execution strategy is supported.
- S4D metadata follows the inspected PDF where landing-page author order/code-line-count
  differs.
- All records remain DRAFT and discovery has not saturated.
tags:
- native-concepts
- primary-papers
- state-space
- self-review
- discovery-ongoing
```
