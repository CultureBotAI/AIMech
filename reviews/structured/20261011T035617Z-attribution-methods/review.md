# Scientific self-review of four attribution methods

- Review: 20261011T035617Z-attribution-methods
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T03:56:17Z
- Finished UTC: 2026-10-11T03:56:17Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The four methods have distinct identities and source-supported mechanisms. Baseline choice, propagation-rule variation, stochastic/numerical approximation and relevance leakage are preserved. No actionable unresolved finding was identified in the selected scope.

## Scope And Provenance

Identity, definition, mechanism, evidence provenance, qualifications and AIO related mappings of Integrated Gradients, DeepLIFT, SmoothGrad and LRP.

Selection: Exactly the four additions in the attribution-methods discovery report; no sampling.
Coverage: full; 4 reviewed / 4 in the declared population.
Source: working_tree at Git base 641f4dc5b5a39af410cee1077de0c105cb5f818a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:IntegratedGradients | data/curated/IntegratedGradients.yaml | maintained | Integrated gradients |
| AIMech:DeepLIFT | data/curated/DeepLIFT.yaml | maintained | DeepLIFT |
| AIMech:SmoothGrad | data/curated/SmoothGrad.yaml | maintained | SmoothGrad |
| AIMech:LayerWiseRelevancePropagation | data/curated/LayerWiseRelevancePropagation.yaml | maintained | Layer-wise relevance propagation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| python -m aimech check-source | passed | True | AIMech:IntegratedGradients, AIMech:DeepLIFT, AIMech:SmoothGrad, AIMech:LayerWiseRelevancePropagation | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a |
| python -m aimech validate | passed | True | AIMech:IntegratedGradients, AIMech:DeepLIFT, AIMech:SmoothGrad, AIMech:LayerWiseRelevancePropagation | Checked 442 record(s); 0 failed. |
| python -m aimech seed --check | passed | True | AIMech:IntegratedGradients, AIMech:DeepLIFT, AIMech:SmoothGrad, AIMech:LayerWiseRelevancePropagation | AIO: 442 records; 0 missing, 0 changed, 0 unexpected. |
| python -m aimech validate-curated | passed | True | AIMech:IntegratedGradients, AIMech:DeepLIFT, AIMech:SmoothGrad, AIMech:LayerWiseRelevancePropagation | Checked 68 curated concept record(s); 0 error(s). |
| python scripts/record_review.py check | passed | True | AIMech:IntegratedGradients, AIMech:DeepLIFT, AIMech:SmoothGrad, AIMech:LayerWiseRelevancePropagation | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 6,<br>  "coverage": "declared_scopes_only"<br>} |
| just check | passed | True | AIMech:IntegratedGradients, AIMech:DeepLIFT, AIMech:SmoothGrad, AIMech:LayerWiseRelevancePropagation | 220 passed, 3 skipped; 442 AIO records valid and exactly reproducible; 68 native records, 11 history sidecars and 6 prior review bundles valid. |
| just vendored-check | passed | True | AIMech:IntegratedGradients, AIMech:DeepLIFT, AIMech:SmoothGrad, AIMech:LayerWiseRelevancePropagation | All 22 governed artifacts match the immutable public CLAW pin. Initial sandbox execution could not resolve the public host; rerun with network access succeeded. |

## Scientific And Domain Assessments

### Attribution identity, mechanism, limits and mapping

evidence: supported. Targets: AIMech:IntegratedGradients.

Straight-path gradient integration differs from a gradient at one input, layer-wise contribution propagation and Shapley averaging across feature orderings.

Attributions depend on the baseline; an arbitrary zero-score baseline need not give a meaningful absence of signal. Numerical integration is approximate. This record makes no universal causal-faithfulness or superiority claim.

### Attribution identity, mechanism, limits and mapping

evidence: supported. Targets: AIMech:DeepLIFT.

This record covers the 2017 DeepLIFT method including distinct local rules; it is not identical to gradients, integrated gradients, Deep SHAP or the earlier Rescale-only formulation.

Reference and local-rule choices affect attribution. The paper discusses cases favoring Rescale or RevealCancel rather than one universally superior rule. Contribution conservation is not a proof of causal feature importance or exact Shapley values for an arbitrary network.

### Attribution identity, mechanism, limits and mapping

evidence: supported. Targets: AIMech:SmoothGrad.

SmoothGrad is an averaging wrapper around a sensitivity-map method, not a new trained network, a training-noise procedure or an exact equivalent of its underlying gradient map.

The result depends on the base map, noise scale and sample count. The paper's visual-coherence comparisons and proposed explanation for noise do not establish universal attribution faithfulness.

### Attribution identity, mechanism, limits and mapping

evidence: supported. Targets: AIMech:LayerWiseRelevancePropagation.

LRP is a family of constrained relevance-propagation constructions, demonstrated for neural networks and kernel-based Bag-of-Words classifiers; it is not a single gradient formula or a classifier-training algorithm.

Conservation alone does not uniquely determine meaningful attributions; the original paper gives a counterexample. Bias terms and epsilon stabilization can absorb relevance, so exact conservation is not asserted for every practical rule.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:IntegratedGradients, AIMech:DeepLIFT, AIMech:SmoothGrad, AIMech:LayerWiseRelevancePropagation. Retain straight-path gradient integration, reference-relative contribution propagation, noisy-input map averaging and layer-wise relevance redistribution as distinct methods. Similar visualization outputs and shared neural-network applications do not establish identity.
- defer: AIMech:DeepLIFT, AIMech:LayerWiseRelevancePropagation. Potential separate rule records (Rescale/RevealCancel and LRP epsilon/alpha-beta) require their own identity and scope decisions. Current framework records explicitly retain variation without claiming a single universal rule.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity-search | research/discovery/20261011T035430Z-attribution-methods.json | supports | No duplicate native identity was found. Text hits were the previously saved discovery leads. One punctuation-equivalent LRP alias was removed after validation identified redundancy. |
| mapping | sources/aio/aio.json; AIO:ArtificialNeuralNetwork definition | supports | This target describes the neural networks directly analyzed in the defining methods. The related mappings preserve the distinction between an analysis method and its object; LRP retains additional kernel-classifier scope. |
| integratedgradients-method | https://proceedings.mlr.press/v70/sundararajan17a/sundararajan17a.pdf; Section 3, equation 1, PDF p. 3; Section 5, equation 3 and baseline selection, PDF pp. 5–6 | supports | Each feature receives its input-minus-baseline difference multiplied by the integral of that feature's partial derivative along the path; the paper approximates the integral with a finite gradient sum. Rendered pages actually inspected: 3, 5. |
| deeplift-method | https://proceedings.mlr.press/v70/shrikumar17a/shrikumar17a.pdf; Sections 3.1–3.5, equations 1–4 and Linear/Rescale/RevealCancel rules, PDF pp. 2–5 | supports | Reference inputs determine reference activations. Local contribution multipliers compose backward subject to summation-to-delta; Linear, Rescale and RevealCancel rules determine local allocation, with RevealCancel treating positive and negative differences separately. Rendered pages actually inspected: 3, 4, 5. |
| smoothgrad-method | https://arxiv.org/pdf/1706.03825v1; Section 2.2, PDF pp. 2–3; unnumbered SmoothGrad averaging equation on p. 3 | supports | Sample multiple noisy copies of the input, compute the selected sensitivity map on each, and average the maps to estimate a local smoothing of that map function. Rendered pages actually inspected: 3. |
| layerwiserelevancepropagation-method | https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0130140&amp;type=printable; Layer-wise relevance propagation, equation 2, PDF/printed pp. 3–4; Layer-wise relevance backpropagation, equations 55–62 and Algorithm 2, pp. 20–21 | supports | Starting from an output score, layer-specific rules allocate relevance messages to preceding units and sum incoming messages until the input is reached. The neural-network procedure supplies stabilized and positive/negative contribution rules. Rendered pages actually inspected: 4, 20, 21. |

## Limits And Additional Notes

- Scientific self-review, not independent peer review or empirical replication.
- Review timestamps describe post-inspection assessment; the discovery report records earlier source access and curation.
- The original methods support the bounded mechanisms, not universal causal interpretation, exact practical conservation or a superiority ranking.
- Evaluation-literature counterpoints are preserved as pending sources; their abstracts are not treated as verified method-specific findings.
- All records remain DRAFT. Four distinct additions were found and the frontier remains nonempty.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T035617Z-attribution-methods
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of four attribution methods
started_at: '2026-10-11T03:56:17Z'
finished_at: '2026-10-11T03:56:17Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The same agent researched, curated and reviewed the four additions;
    this is not independent review.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The four methods have distinct identities and source-supported mechanisms.
  Baseline choice, propagation-rule variation, stochastic/numerical approximation
  and relevance leakage are preserved. No actionable unresolved finding was identified
  in the selected scope.
source:
  git_revision: 641f4dc5b5a39af410cee1077de0c105cb5f818a
  state: working_tree
  inputs:
  - path: data/curated/DeepLIFT.yaml
    sha256: f11a5bb68b95212dc3614fb8fc5c2ed9d6cf27e15e81980bf4c38db417e57651
    role: target
  - path: data/curated/IntegratedGradients.yaml
    sha256: 40106f0188563732af552aed5f1d61df7b3feaec6ff2963e6713b6d6e567ecfe
    role: target
  - path: data/curated/LayerWiseRelevancePropagation.yaml
    sha256: ab7127098b11c5c0049a10c5a646974f18edf9f955a725d5e937f6059a7a5faa
    role: target
  - path: data/curated/SmoothGrad.yaml
    sha256: 755b7d7358ae5f91f87993cd18677f0d51bb3ab1c8fbe04e502e5b07eede6ec3
    role: target
  - path: research/discovery/20261011T035430Z-attribution-methods.json
    sha256: 8d0137e23ddc9f28ed1c1026d6bcf6310b82a5a11ea447477e0165a98c446500
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: b9a87f14341119f89fffac2cfb29fab222d0fcc9ac999990650e349e06d9cfc3
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: dfcbacdcdeb7429bfa947d7c1c8431e5d0b886f593daaa359588273ba2a2c6e0
    role: context
targets:
- target_id: AIMech:IntegratedGradients
  path: data/curated/IntegratedGradients.yaml
  label: Integrated gradients
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IntegratedGradients.yaml
    role: maintained concept and claim evidence/mapping
- target_id: AIMech:DeepLIFT
  path: data/curated/DeepLIFT.yaml
  label: DeepLIFT
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DeepLIFT.yaml
    role: maintained concept and claim evidence/mapping
- target_id: AIMech:SmoothGrad
  path: data/curated/SmoothGrad.yaml
  label: SmoothGrad
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SmoothGrad.yaml
    role: maintained concept and claim evidence/mapping
- target_id: AIMech:LayerWiseRelevancePropagation
  path: data/curated/LayerWiseRelevancePropagation.yaml
  label: Layer-wise relevance propagation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LayerWiseRelevancePropagation.yaml
    role: maintained concept and claim evidence/mapping
scope:
  description: Identity, definition, mechanism, evidence provenance, qualifications
    and AIO related mappings of Integrated Gradients, DeepLIFT, SmoothGrad and LRP.
  selection: Exactly the four additions in the attribution-methods discovery report;
    no sampling.
  coverage: full
  population_size: 4
  reviewed_target_ids:
  - AIMech:IntegratedGradients
  - AIMech:DeepLIFT
  - AIMech:SmoothGrad
  - AIMech:LayerWiseRelevancePropagation
  exclusions:
  - target: Previously curated SHAP/LIME and generated AIO scientific claims
    reason: Identity/mapping context only; no new claim-by-claim reassessment of those
      records.
  - target: Evaluation ranking, universal faithfulness and empirical replication
    reason: No such claims are curated. Conflicting evaluation-source leads remain
      pending full-method inspection.
checks:
- check_id: required-0
  name: python -m aimech check-source
  command: python -m aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:IntegratedGradients
  - AIMech:DeepLIFT
  - AIMech:SmoothGrad
  - AIMech:LayerWiseRelevancePropagation
  exit_code: 0
  expected_exit_code: 0
  summary: Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a
- check_id: required-1
  name: python -m aimech validate
  command: python -m aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:IntegratedGradients
  - AIMech:DeepLIFT
  - AIMech:SmoothGrad
  - AIMech:LayerWiseRelevancePropagation
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 record(s); 0 failed.
- check_id: required-2
  name: python -m aimech seed --check
  command: python -m aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:IntegratedGradients
  - AIMech:DeepLIFT
  - AIMech:SmoothGrad
  - AIMech:LayerWiseRelevancePropagation
  exit_code: 0
  expected_exit_code: 0
  summary: 'AIO: 442 records; 0 missing, 0 changed, 0 unexpected.'
- check_id: required-3
  name: python -m aimech validate-curated
  command: python -m aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:IntegratedGradients
  - AIMech:DeepLIFT
  - AIMech:SmoothGrad
  - AIMech:LayerWiseRelevancePropagation
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 68 curated concept record(s); 0 error(s).
- check_id: required-4
  name: python scripts/record_review.py check
  command: python scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:IntegratedGradients
  - AIMech:DeepLIFT
  - AIMech:SmoothGrad
  - AIMech:LayerWiseRelevancePropagation
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 6,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}"
- check_id: quality
  name: just check
  command: PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check
  status: passed
  required: true
  target_ids:
  - AIMech:IntegratedGradients
  - AIMech:DeepLIFT
  - AIMech:SmoothGrad
  - AIMech:LayerWiseRelevancePropagation
  exit_code: 0
  expected_exit_code: 0
  summary: 220 passed, 3 skipped; 442 AIO records valid and exactly reproducible;
    68 native records, 11 history sidecars and 6 prior review bundles valid.
- check_id: governance
  name: just vendored-check
  command: PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:IntegratedGradients
  - AIMech:DeepLIFT
  - AIMech:SmoothGrad
  - AIMech:LayerWiseRelevancePropagation
  exit_code: 0
  expected_exit_code: 0
  summary: All 22 governed artifacts match the immutable public CLAW pin. Initial
    sandbox execution could not resolve the public host; rerun with network access
    succeeded.
evidence:
- evidence_id: identity-search
  kind: search
  reference: research/discovery/20261011T035430Z-attribution-methods.json
  accessed_at: '2026-10-11T03:56:17Z'
  support: supports
  summary: No duplicate native identity was found. Text hits were the previously saved
    discovery leads. One punctuation-equivalent LRP alias was removed after validation
    identified redundancy.
  search_scope: Ignored-inclusive and hidden-inclusive searches of both checkouts,
    plus normalized comparison of all 442 AIO labels/scoped synonyms and 64 preceding
    native records.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: AIO:ArtificialNeuralNetwork definition
  accessed_at: '2026-10-11T03:56:17Z'
  support: supports
  summary: This target describes the neural networks directly analyzed in the defining
    methods. The related mappings preserve the distinction between an analysis method
    and its object; LRP retains additional kernel-classifier scope.
- evidence_id: integratedgradients-method
  kind: primary_source
  reference: https://proceedings.mlr.press/v70/sundararajan17a/sundararajan17a.pdf
  locator: Section 3, equation 1, PDF p. 3; Section 5, equation 3 and baseline selection,
    PDF pp. 5–6
  accessed_at: '2026-10-11T03:50:23Z'
  snapshot_sha256: b17d267e7b8f7c5e9198030932ef184d93d6c2dd90e47ab996ed395fd673443f
  support: supports
  summary: 'Each feature receives its input-minus-baseline difference multiplied by
    the integral of that feature''s partial derivative along the path; the paper approximates
    the integral with a finite gradient sum. Rendered pages actually inspected: 3,
    5.'
- evidence_id: deeplift-method
  kind: primary_source
  reference: https://proceedings.mlr.press/v70/shrikumar17a/shrikumar17a.pdf
  locator: Sections 3.1–3.5, equations 1–4 and Linear/Rescale/RevealCancel rules,
    PDF pp. 2–5
  accessed_at: '2026-10-11T03:50:23Z'
  snapshot_sha256: bfdc8344354218d9f516e4dd15004ed522b6ef895cd59f3de9c7ee6867ddbbe6
  support: supports
  summary: 'Reference inputs determine reference activations. Local contribution multipliers
    compose backward subject to summation-to-delta; Linear, Rescale and RevealCancel
    rules determine local allocation, with RevealCancel treating positive and negative
    differences separately. Rendered pages actually inspected: 3, 4, 5.'
- evidence_id: smoothgrad-method
  kind: primary_source
  reference: https://arxiv.org/pdf/1706.03825v1
  locator: Section 2.2, PDF pp. 2–3; unnumbered SmoothGrad averaging equation on p.
    3
  accessed_at: '2026-10-11T03:50:25Z'
  snapshot_sha256: 5a018a58df31c4eb1091cbb671c02762d5af5fe57c20d0ea8cbdccc8df45e906
  support: supports
  summary: 'Sample multiple noisy copies of the input, compute the selected sensitivity
    map on each, and average the maps to estimate a local smoothing of that map function.
    Rendered pages actually inspected: 3.'
- evidence_id: layerwiserelevancepropagation-method
  kind: primary_source
  reference: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0130140&type=printable
  locator: Layer-wise relevance propagation, equation 2, PDF/printed pp. 3–4; Layer-wise
    relevance backpropagation, equations 55–62 and Algorithm 2, pp. 20–21
  accessed_at: '2026-10-11T03:50:24Z'
  snapshot_sha256: 212147782b3e3efe13b583d34a6ec414557863009232d43739179985a7cfa655
  support: supports
  summary: 'Starting from an output score, layer-specific rules allocate relevance
    messages to preceding units and sum incoming messages until the input is reached.
    The neural-network procedure supplies stabilized and positive/negative contribution
    rules. Rendered pages actually inspected: 4, 20, 21.'
assessments:
- assessment_id: integratedgradients-method
  area: evidence
  topic: Attribution identity, mechanism, limits and mapping
  outcome: supported
  target_ids:
  - AIMech:IntegratedGradients
  evidence_ids:
  - integratedgradients-method
  - identity-search
  - mapping
  summary: Straight-path gradient integration differs from a gradient at one input,
    layer-wise contribution propagation and Shapley averaging across feature orderings.
  details: Attributions depend on the baseline; an arbitrary zero-score baseline need
    not give a meaningful absence of signal. Numerical integration is approximate.
    This record makes no universal causal-faithfulness or superiority claim.
  dimensions:
  - name: evidence-access
    value: full_text with rendered-page inspection
    definition: Method passages were read and listed equation/algorithm pages visually
      inspected.
    evidence_ids:
    - integratedgradients-method
  - name: mapping-direction
    value: related_match to directly analyzed neural networks
    definition: The method attributes outputs of artificial neural networks to their
      inputs in the defining paper. This direct analysis relationship does not make
      the method a neural-network architecture.
    evidence_ids:
    - integratedgradients-method
    - mapping
- assessment_id: deeplift-method
  area: evidence
  topic: Attribution identity, mechanism, limits and mapping
  outcome: supported
  target_ids:
  - AIMech:DeepLIFT
  evidence_ids:
  - deeplift-method
  - identity-search
  - mapping
  summary: This record covers the 2017 DeepLIFT method including distinct local rules;
    it is not identical to gradients, integrated gradients, Deep SHAP or the earlier
    Rescale-only formulation.
  details: Reference and local-rule choices affect attribution. The paper discusses
    cases favoring Rescale or RevealCancel rather than one universally superior rule.
    Contribution conservation is not a proof of causal feature importance or exact
    Shapley values for an arbitrary network.
  dimensions:
  - name: evidence-access
    value: full_text with rendered-page inspection
    definition: Method passages were read and listed equation/algorithm pages visually
      inspected.
    evidence_ids:
    - deeplift-method
  - name: mapping-direction
    value: related_match to directly analyzed neural networks
    definition: The defining method propagates contributions through an artificial
      neural network. The related mapping identifies that direct analysis object,
      not architecture identity or subclasshood.
    evidence_ids:
    - deeplift-method
    - mapping
- assessment_id: smoothgrad-method
  area: evidence
  topic: Attribution identity, mechanism, limits and mapping
  outcome: supported
  target_ids:
  - AIMech:SmoothGrad
  evidence_ids:
  - smoothgrad-method
  - identity-search
  - mapping
  summary: SmoothGrad is an averaging wrapper around a sensitivity-map method, not
    a new trained network, a training-noise procedure or an exact equivalent of its
    underlying gradient map.
  details: The result depends on the base map, noise scale and sample count. The paper's
    visual-coherence comparisons and proposed explanation for noise do not establish
    universal attribution faithfulness.
  dimensions:
  - name: evidence-access
    value: full_text with rendered-page inspection
    definition: Method passages were read and listed equation/algorithm pages visually
      inspected.
    evidence_ids:
    - smoothgrad-method
  - name: mapping-direction
    value: related_match to directly analyzed neural networks
    definition: The defining method smooths sensitivity maps of artificial-neural-network
      outputs. This direct analysis relationship is not an assertion that SmoothGrad
      is itself a network.
    evidence_ids:
    - smoothgrad-method
    - mapping
- assessment_id: layerwiserelevancepropagation-method
  area: evidence
  topic: Attribution identity, mechanism, limits and mapping
  outcome: supported
  target_ids:
  - AIMech:LayerWiseRelevancePropagation
  evidence_ids:
  - layerwiserelevancepropagation-method
  - identity-search
  - mapping
  summary: LRP is a family of constrained relevance-propagation constructions, demonstrated
    for neural networks and kernel-based Bag-of-Words classifiers; it is not a single
    gradient formula or a classifier-training algorithm.
  details: Conservation alone does not uniquely determine meaningful attributions;
    the original paper gives a counterexample. Bias terms and epsilon stabilization
    can absorb relevance, so exact conservation is not asserted for every practical
    rule.
  dimensions:
  - name: evidence-access
    value: full_text with rendered-page inspection
    definition: Method passages were read and listed equation/algorithm pages visually
      inspected.
    evidence_ids:
    - layerwiserelevancepropagation-method
  - name: mapping-direction
    value: related_match to directly analyzed neural networks
    definition: The paper explicitly constructs LRP for artificial neural networks.
      This related mapping records that supported analysis relationship while retaining
      LRP's additional kernel-classifier scope; it asserts neither equivalence nor
      exclusive applicability.
    evidence_ids:
    - layerwiserelevancepropagation-method
    - mapping
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:IntegratedGradients
  - AIMech:DeepLIFT
  - AIMech:SmoothGrad
  - AIMech:LayerWiseRelevancePropagation
  evidence_ids:
  - identity-search
  - mapping
  - integratedgradients-method
  - deeplift-method
  - smoothgrad-method
  - layerwiserelevancepropagation-method
  rationale: Retain straight-path gradient integration, reference-relative contribution
    propagation, noisy-input map averaging and layer-wise relevance redistribution
    as distinct methods. Similar visualization outputs and shared neural-network applications
    do not establish identity.
- action: defer
  target_ids:
  - AIMech:DeepLIFT
  - AIMech:LayerWiseRelevancePropagation
  evidence_ids:
  - deeplift-method
  - layerwiserelevancepropagation-method
  rationale: Potential separate rule records (Rescale/RevealCancel and LRP epsilon/alpha-beta)
    require their own identity and scope decisions. Current framework records explicitly
    retain variation without claiming a single universal rule.
limitations:
- Scientific self-review, not independent peer review or empirical replication.
- Review timestamps describe post-inspection assessment; the discovery report records
  earlier source access and curation.
- The original methods support the bounded mechanisms, not universal causal interpretation,
  exact practical conservation or a superiority ranking.
- Evaluation-literature counterpoints are preserved as pending sources; their abstracts
  are not treated as verified method-specific findings.
- All records remain DRAFT. Four distinct additions were found and the frontier remains
  nonempty.
tags:
- native-concepts
- primary-papers
- attribution
- self-review
- discovery-ongoing
```
