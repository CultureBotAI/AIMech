# Scientific self-review of five fairness criteria

- Review: 20261011T045259Z-fairness-criteria
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T04:52:59Z
- Finished UTC: 2026-10-11T04:52:59Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All five additions have inspected formal-definition support and explicit AIO related mappings. The review checked conditional versus marginal parity, positive-outcome scope, supplied metrics, distributional counterfactual equality, model misspecification and the assumptions in the later causal/parity analysis. The new criterion kind preserves the distinction from enforcement algorithms. No actionable unresolved defect was found.

## Scope And Provenance

Identity, formal definition, claim evidence, source versions, assumptions and AIO mappings for five fairness criteria; schema kind and documentation consistency.

Selection: Exactly the five maintained targets in the fairness-criteria discovery ledger, with no sampling.
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base 49a3c1addbeb156187282e43391c42994406da47.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:EqualizedOdds | data/curated/EqualizedOdds.yaml | maintained | Equalized odds |
| AIMech:EqualOpportunity | data/curated/EqualOpportunity.yaml | maintained | Equal opportunity in binary classification |
| AIMech:DemographicParity | data/curated/DemographicParity.yaml | maintained | Demographic parity |
| AIMech:LipschitzIndividualFairness | data/curated/LipschitzIndividualFairness.yaml | maintained | Lipschitz individual fairness |
| AIMech:CounterfactualFairness | data/curated/CounterfactualFairness.yaml | maintained | Counterfactual fairness |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:EqualizedOdds, AIMech:EqualOpportunity, AIMech:DemographicParity, AIMech:LipschitzIndividualFairness, AIMech:CounterfactualFairness | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate | passed | True | AIMech:EqualizedOdds, AIMech:EqualOpportunity, AIMech:DemographicParity, AIMech:LipschitzIndividualFairness, AIMech:CounterfactualFairness | Checked 442 record(s); 0 failed.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-curated | passed | True | AIMech:EqualizedOdds, AIMech:EqualOpportunity, AIMech:DemographicParity, AIMech:LipschitzIndividualFairness, AIMech:CounterfactualFairness | Checked 99 curated concept record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli seed --check | passed | True | AIMech:EqualizedOdds, AIMech:EqualOpportunity, AIMech:DemographicParity, AIMech:LipschitzIndividualFairness, AIMech:CounterfactualFairness | AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-history --base HEAD | passed | True | AIMech:EqualizedOdds, AIMech:EqualOpportunity, AIMech:DemographicParity, AIMech:LipschitzIndividualFairness, AIMech:CounterfactualFairness | Checked 18 history record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python scripts/record_review.py check | passed | True | AIMech:EqualizedOdds, AIMech:EqualOpportunity, AIMech:DemographicParity, AIMech:LipschitzIndividualFairness, AIMech:CounterfactualFairness | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 17,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class<br> |
| just check | passed | True | AIMech:EqualizedOdds, AIMech:EqualOpportunity, AIMech:DemographicParity, AIMech:LipschitzIndividualFairness, AIMech:CounterfactualFairness | All checks passed!<br>........................................................................ [ 31%]<br>........................................................................ [ 63%]<br>........................................................................ [ 94%]<br>.........sss                                                             [100%]<br>225 passed, 3 skipped in 49.01s<br>Checked 442 record(s); 0 failed.<br>Checked 99 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 18 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 17,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:EqualizedOdds, AIMech:EqualOpportunity, AIMech:DemographicParity, AIMech:LipschitzIndividualFairness, AIMech:CounterfactualFairness | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Criterion identity, conditioning/model assumptions, source support and mapping direction

evidence: supported. Targets: AIMech:EqualizedOdds.

This is the distributional criterion in Hardt, Price and Srebro's Definition 2.1, not their postprocessing algorithm, a bias type, demographic parity or a claim of overall social fairness. Equal opportunity is a weaker positive-outcome-only constraint. All 442 pinned AIO labels/scoped synonyms and 94 preceding native identities were compared, with ignored-inclusive text searches in both checkouts.

The conditioning outcome and protected groups must be specified, with estimable nonzero-probability conditioning strata for rate comparisons. Biased or unreliable outcome labels can undermine interpretation. Equal true-positive and false-positive rates do not require identical overall accuracy when group outcome prevalences differ. The record uses the formal conditional-independence definition, not the source's informal equal-accuracy wording. This is an oblivious distributional test: identical prediction/outcome/group statistics can arise from different underlying dependency structures. Satisfaction or violation alone is not conclusive evidence of overall fairness or unfairness. Finite-sample uncertainty, a tolerance and domain-specific interpretation are needed in an application; no empirical result, universal fairness guarantee or legal-compliance claim is asserted.

### Criterion identity, conditioning/model assumptions, source support and mapping direction

evidence: supported. Targets: AIMech:EqualOpportunity.

The identity is Hardt, Price and Srebro's Definition 2.2, with the positive target designated as the advantaged outcome. It is not the wider philosophical meaning of equal opportunity, the full equalized-odds condition, or a threshold-adjustment algorithm. Identity searches covered all 442 AIO labels and scoped synonyms, 94 preceding native records and ignored/hidden-inclusive text in both checkouts.

The definition depends on which target outcome is designated positive/advantaged; changing that designation changes the constrained population. Equal opportunity alone does not equalize false-positive rates, selection rates, predictive values or individual treatment. The criterion requires meaningful target labels and sufficiently supported group/positive-outcome strata. Finite-sample uncertainty is not eliminated by writing an equality. Like other oblivious criteria, this condition does not determine the causal process or establish overall social fairness, empirical utility or legal compliance.

### Criterion identity, conditioning/model assumptions, source support and mapping direction

evidence: supported. Targets: AIMech:DemographicParity.

The record denotes exact distributional parity, also called statistical parity in the inspected fairness literature. It is not equalized odds, equality of true-positive rates, an approximate disparity tolerance, or a complete fairness judgment. All 442 AIO identities/scoped synonyms, 94 native identities and ignored-inclusive text in both checkouts were searched. Conditional parity and parity for selected subgroups require separately stated conditioning and scope.

Matching group output rates does not ensure similar individuals receive similar treatment or that parity holds within every subgroup. If target outcomes have different prevalences by group, a perfectly accurate predictor can violate demographic parity. This statistical observation does not by itself choose which fairness criterion a domain should use. Exact independence is distinct from approximate parity within a specified tolerance; an empirical estimate needs uncertainty and population context. Connections to counterfactual fairness depend on causal-model assumptions and how the predictor/model is constructed. Shared population statistics do not make the two definitions interchangeable for a fixed causal model.

### Criterion identity, conditioning/model assumptions, source support and mapping direction

evidence: supported. Targets: AIMech:LipschitzIndividualFairness.

The record is the explicit (D,d)-Lipschitz condition in Dwork and colleagues' framework. It is narrower than every possible notion of individual fairness and separate from their loss-minimizing linear-program construction, metric-learning algorithms, differential privacy and group parity. Identity assessment covered 442 AIO labels/scoped synonyms, 94 preceding native identities and ignored-inclusive searches of both checkouts.

The task-specific distance and output-distance choice determine the constraint. The framework does not certify that a chosen similarity metric represents an appropriate social or domain judgment. A constant output distribution satisfies the condition; useful predictions require a separate utility objective. Criterion satisfaction alone does not guarantee predictive quality. The formulation over an inspected finite population does not itself guarantee generalization to unobserved individuals. Group-parity implications require additional conditions on the metric and group distributions. This record does not equate the criterion with all individual-fairness notions, certify the paper's full optimization/theorem results, or assert legal compliance.

### Criterion identity, conditioning/model assumptions, source support and mapping direction

evidence: supported. Targets: AIMech:CounterfactualFairness.

This is Kusner and colleagues' Definition 5, an equality of conditional counterfactual distributions. It is not merely changing an input feature while freezing its causal descendants, a group-level observational equality, the FAIRLEARNING algorithm, or a generic guarantee of social fairness. All 442 pinned AIO labels/scoped synonyms, 94 preceding native identities and ignored-inclusive text in both checkouts were searched. Later parity connections do not establish identity under an arbitrary fixed causal model.

The comparison depends on causal and counterfactual assumptions that observational data alone generally cannot establish. Specifying protected attributes and meaningful interventions requires domain interpretation. Ignoring protected attributes as explicit inputs is insufficient when other inputs carry their causal effects. Conversely, using a descendant is not categorically excluded if the relevant total dependence cancels, as the source qualifies its sufficient construction. A predictor satisfying the condition in an assumed model need not satisfy it under a model with omitted confounding; the inspected sensitivity paper studies this vulnerability in additive-noise models. The criterion constrains conditional output distributions, not necessarily pointwise equality for every unobserved state or usefulness of a predictor. Connections to demographic parity retain their model/independence assumptions.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:EqualizedOdds, AIMech:EqualOpportunity, AIMech:DemographicParity, AIMech:LipschitzIndividualFairness, AIMech:CounterfactualFairness. Retain equalized odds, its positive-outcome relaxation, marginal demographic parity, the supplied-metric Lipschitz condition and model-conditioned counterfactual fairness as distinct criteria. Different conditioning and model assumptions define different identities even when some predictors satisfy several criteria. Statistical parity is retained as an alias of demographic parity in the exact distributional sense.
- defer: AIMech:EqualizedOdds, AIMech:EqualOpportunity, AIMech:DemographicParity, AIMech:LipschitzIndividualFairness, AIMech:CounterfactualFairness. Postprocessing, fairness linear programs, FAIRLEARNING, sensitivity algorithms and further criteria need separately scoped primary-method assessments. The causal/parity paper does not justify merging the two definitions for an arbitrary fixed causal model.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity-search | research/discovery/20261011T044936Z-fairness-criteria.json | supports | All 442 AIO labels and scoped synonyms and 94 preceding native identities were compared, with ignored/hidden-inclusive text searches of both checkouts. No identity or full-text target hit was found in that searched scope. A separate ignored-inclusive worktree search found no preexisting evaluation_criterion key. Formal criteria are not bias types, trained models, or the algorithms that enforce them. |
| mapping | sources/aio/aio.json; Classification, BinaryClassification, CausalGraphicalModel, MetricLearning, Bias, SystemicBias, EvaluationBias and EthicalLLM | supports | Equalized odds, demographic parity and Lipschitz individual fairness related_match Classification; equal opportunity related_match BinaryClassification; counterfactual fairness related_match CausalGraphicalModel. These are direct relationships to the assessed task or necessary model assumptions, not subclass assertions. MetricLearning does not denote a supplied similarity constraint; Bias, SystemicBias, EvaluationBias and EthicalLLM do not denote these formal criteria. |
| equalizedodds-method | https://arxiv.org/pdf/1610.02413v1; Section 2, Definition 2.1, PDF p. 3; Sections 2.2–2.3, PDF p. 4; Section 6, PDF pp. 12–14; discussion of reliable targets and nonconclusive fairness tests, PDF pp. 20–21 | supports | A fairness criterion requiring a predictor's output to be conditionally independent of a specified protected attribute given the target outcome; for binary predictions and outcomes, it requires equal true-positive and false-positive rates across the compared groups. The cited formal definition and scoped limitations were inspected. Rendered pages actually inspected: 1, 2, 3, 4, 21. |
| equalopportunity-method | https://arxiv.org/pdf/1610.02413v1; Section 2.1, Definition 2.2, PDF p. 4; Section 2, Definition 2.1, PDF p. 3; Section 6, PDF pp. 12–14; reliable-target and interpretation discussion, PDF pp. 20–21 | supports | A binary-classification fairness criterion requiring equal probabilities of a positive prediction across specified protected groups among individuals whose target outcome is the designated positive outcome. The cited formal definition and scoped limitations were inspected. Rendered pages actually inspected: 1, 2, 3, 4, 21. |
| demographicparity-method | https://arxiv.org/pdf/1610.02413v1; Section 1, demographic-parity definition and limitations, PDF pp. 1–2 | supports | A group-level prediction criterion requiring the distribution of a decision or prediction to be independent of a specified protected attribute; for a binary decision, the positive-decision rate is equal across the compared groups. The cited formal definition and scoped limitations were inspected. Rendered pages actually inspected: 1, 2, 3, 4, 21. |
| demographicparity-method-statistical-parity-formulation | https://arxiv.org/pdf/1104.3913v2; Section 3, Definition 3.1, printed p. 7 / PDF p. 8; Section 3.1 examples, printed p. 8 / PDF p. 9 | supports | The statistical-parity formulation compares group output distributions by total variation with a stated tolerance; exact parity is its zero-tolerance case. The accompanying examples show that group parity can coexist with unequal treatment within groups and does not imply parity for all subgroups. This evidence supports the stated scope or limitation, not an unrestricted fairness guarantee. Rendered pages actually inspected: 1, 5, 8, 9. |
| demographicparity-method-causal-parity-analysis | https://arxiv.org/pdf/2208.03843v4; Related Work distinction between a fixed and freely constructed causal model, PDF p. 3; Criteria 3 and Theorems 4–5, PDF p. 4 | supports | Rosenblatt and Witter derive connections with counterfactual fairness using their Criteria 3 independence assumption. Their conversion from demographic parity introduces a causal model and latent-variable construction of their choice; they explicitly distinguish that setting from checking a predictor against a fixed causal model. These results do not justify treating the two criterion identities as synonyms. This evidence supports the stated scope or limitation, not an unrestricted fairness guarantee. Rendered pages actually inspected: 3, 4. |
| lipschitzindividualfairness-method | https://arxiv.org/pdf/1104.3913v2; Sections 1.1–1.2, printed pp. 1–3 / PDF pp. 2–4; Section 2, Definition 2.1 and equation (1), printed p. 4 / PDF p. 5; Section 2.1 probability metrics and Remark 2.1, printed p. 5 / PDF p. 6 | supports | An individual-fairness criterion requiring the distance between the output distributions assigned by a randomized classifier to any two individuals to be no greater than their task-specific similarity distance. The cited formal definition and scoped limitations were inspected. Rendered pages actually inspected: 1, 5, 6, 8, 9. |
| counterfactualfairness-method | https://arxiv.org/pdf/1703.06856v3; Section 2.2 and Section 3, Definition 5/equation (1), PDF p. 3; Section 3.2, Lemma 1 and its qualification, PDF p. 5; Sections 4.2–4.3, causal assumptions and interpretive limits, PDF p. 7 | supports | A fairness criterion in a specified causal model requiring a predictor's conditional output distribution, given an individual's observed attributes and protected-attribute value, to remain unchanged under counterfactual interventions that assign other attainable protected-attribute values. The cited formal definition and scoped limitations were inspected. Rendered pages actually inspected: 3, 5, 7. |
| counterfactualfairness-method-confounding-sensitivity | https://proceedings.mlr.press/v115/kilbertus20a/kilbertus20a.pdf; Section 2.1, PDF pp. 2–3 (volume pp. 617–618); Section 3.1 and Figure 1, PDF p. 4 (volume p. 619) | supports | The sensitivity study distinguishes a guessed model used to construct a fair predictor from a model allowing additional unobserved confounding through correlated errors. Fairness in the guessed model does not guarantee fairness under the alternative data-generating assumptions; the paper frames this as sensitivity analysis rather than identification of a uniquely correct hidden model. This evidence supports the stated scope or limitation, not an unrestricted fairness guarantee. Rendered pages actually inspected: 2, 3, 4. |
| counterfactualfairness-method-causal-parity-analysis | https://arxiv.org/pdf/2208.03843v4; Related Work distinction between a fixed and freely constructed causal model, PDF p. 3; Criteria 3 and Theorems 4–5, PDF p. 4 | supports | Rosenblatt and Witter's parity connections use their explicit independence criterion for latent and protected variables, and the demographic-parity-to-counterfactual-fairness direction constructs a causal model and latent representation. The paper distinguishes that setting from assessment with a fixed causal model; the relationship is not an unrestricted synonym assertion. This evidence supports the stated scope or limitation, not an unrestricted fairness guarantee. Rendered pages actually inspected: 3, 4. |

## Limits And Additional Notes

- Scientific adversarial self-review, not independent approval; all five records remain DRAFT.
- Formal-criterion satisfaction does not by itself establish overall fairness, normative suitability, predictive quality or legal compliance.
- The later parity analysis retains its explicit independence criterion and freedom to construct a causal model; the original counterfactual criterion is not merged with observational parity.
- The report includes a curator arithmetic counterexample showing equal error rates need not imply equal overall accuracy when prevalences differ. This is not an empirical benchmark.
- The downloaded Hardt and Dwork title-page dates differ from their arXiv version dates; both observations and exact PDF hashes are retained.
- Publisher DOI/PDF failures were resolved by opening the publisher landing page and using the public exact arXiv version. No unseen publisher PDF review is claimed.
- No full proof certification, benchmark reproduction or finite-data fairness audit was performed.
- All required checks passed, and discovery remains ongoing.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T045259Z-fairness-criteria
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of five fairness criteria
started_at: '2026-10-11T04:52:59Z'
finished_at: '2026-10-11T04:52:59Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed its own research
    and records; this is not independent scientific approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All five additions have inspected formal-definition support and explicit
  AIO related mappings. The review checked conditional versus marginal parity, positive-outcome
  scope, supplied metrics, distributional counterfactual equality, model misspecification
  and the assumptions in the later causal/parity analysis. The new criterion kind
  preserves the distinction from enforcement algorithms. No actionable unresolved
  defect was found.
source:
  git_revision: 49a3c1addbeb156187282e43391c42994406da47
  state: working_tree
  inputs:
  - path: data/curated/CounterfactualFairness.yaml
    sha256: 552311fbde194bd5b29821e0568ac33bdec4663c5c835422dddafbd7d656af63
    role: target
  - path: data/curated/DemographicParity.yaml
    sha256: a47602b50b2fd0faa31a5f7901a1912c911e756db17a5b1459fd13026924f1e9
    role: target
  - path: data/curated/EqualOpportunity.yaml
    sha256: e868e1952c8c04a5ac1a7ad6602b464482e423d7711cb011b9a203ea4e7a1ced
    role: target
  - path: data/curated/EqualizedOdds.yaml
    sha256: 0ed350441f0608a833f5b1acc74ac07f1a498af2d22279d646bb8cf76434bfba
    role: target
  - path: data/curated/LipschitzIndividualFairness.yaml
    sha256: fb1a6bbab907abb97dea7512d1e8c88a39cd9174ec601096e62110e6577751fe
    role: target
  - path: docs/curated-concepts.md
    sha256: c574580df592c437b965bee9a3a171f8e9dbdb9a26595a6cc238cadd55168456
    role: context
  - path: research/discovery/20261011T044936Z-fairness-criteria.json
    sha256: c716eb4e670430e0dd1d5e86fc69825d7f7fff866fa40f0f8c130fdd73e58ea0
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
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:EqualizedOdds
  path: data/curated/EqualizedOdds.yaml
  label: Equalized odds
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/EqualizedOdds.yaml
    role: maintained native concept
- target_id: AIMech:EqualOpportunity
  path: data/curated/EqualOpportunity.yaml
  label: Equal opportunity in binary classification
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/EqualOpportunity.yaml
    role: maintained native concept
- target_id: AIMech:DemographicParity
  path: data/curated/DemographicParity.yaml
  label: Demographic parity
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DemographicParity.yaml
    role: maintained native concept
- target_id: AIMech:LipschitzIndividualFairness
  path: data/curated/LipschitzIndividualFairness.yaml
  label: Lipschitz individual fairness
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LipschitzIndividualFairness.yaml
    role: maintained native concept
- target_id: AIMech:CounterfactualFairness
  path: data/curated/CounterfactualFairness.yaml
  label: Counterfactual fairness
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CounterfactualFairness.yaml
    role: maintained native concept
scope:
  description: Identity, formal definition, claim evidence, source versions, assumptions
    and AIO mappings for five fairness criteria; schema kind and documentation consistency.
  selection: Exactly the five maintained targets in the fairness-criteria discovery
    ledger, with no sampling.
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - AIMech:EqualizedOdds
  - AIMech:EqualOpportunity
  - AIMech:DemographicParity
  - AIMech:LipschitzIndividualFairness
  - AIMech:CounterfactualFairness
  exclusions:
  - target: Benchmark results, appendix proof verification and executable implementation
      correctness
    reason: Records describe the inspected methods and bounded theoretical limitations;
      no such validation is asserted.
  - target: Enforcement algorithms, sensitivity-analysis algorithms and additional
      fairness criteria
    reason: These remain separately scoped frontier items rather than automatic duplicates
      or additions.
checks:
- check_id: required-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:EqualizedOdds
  - AIMech:EqualOpportunity
  - AIMech:DemographicParity
  - AIMech:LipschitzIndividualFairness
  - AIMech:CounterfactualFairness
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
  - AIMech:EqualizedOdds
  - AIMech:EqualOpportunity
  - AIMech:DemographicParity
  - AIMech:LipschitzIndividualFairness
  - AIMech:CounterfactualFairness
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
  - AIMech:EqualizedOdds
  - AIMech:EqualOpportunity
  - AIMech:DemographicParity
  - AIMech:LipschitzIndividualFairness
  - AIMech:CounterfactualFairness
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 99 curated concept record(s); 0 error(s).

    '
- check_id: required-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:EqualizedOdds
  - AIMech:EqualOpportunity
  - AIMech:DemographicParity
  - AIMech:LipschitzIndividualFairness
  - AIMech:CounterfactualFairness
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
  - AIMech:EqualizedOdds
  - AIMech:EqualOpportunity
  - AIMech:DemographicParity
  - AIMech:LipschitzIndividualFairness
  - AIMech:CounterfactualFairness
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 18 history record(s); 0 error(s).

    '
- check_id: required-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:EqualizedOdds
  - AIMech:EqualOpportunity
  - AIMech:DemographicParity
  - AIMech:LipschitzIndividualFairness
  - AIMech:CounterfactualFairness
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 17,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\ntopClass is deprecated - use top_class\n"
- check_id: required-6
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:EqualizedOdds
  - AIMech:EqualOpportunity
  - AIMech:DemographicParity
  - AIMech:LipschitzIndividualFairness
  - AIMech:CounterfactualFairness
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 31%]\n........................................................................\
    \ [ 63%]\n........................................................................\
    \ [ 94%]\n.........sss                                                       \
    \      [100%]\n225 passed, 3 skipped in 49.01s\nChecked 442 record(s); 0 failed.\n\
    Checked 99 curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing,\
    \ 0 changed, 0 unexpected.\nChecked 18 history record(s); 0 error(s).\n{\n  \"\
    repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 17,\n  \"coverage\"\
    : \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-7
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:EqualizedOdds
  - AIMech:EqualOpportunity
  - AIMech:DemographicParity
  - AIMech:LipschitzIndividualFairness
  - AIMech:CounterfactualFairness
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity-search
  kind: search
  reference: research/discovery/20261011T044936Z-fairness-criteria.json
  accessed_at: '2026-10-11T04:52:59Z'
  support: supports
  summary: All 442 AIO labels and scoped synonyms and 94 preceding native identities
    were compared, with ignored/hidden-inclusive text searches of both checkouts.
    No identity or full-text target hit was found in that searched scope. A separate
    ignored-inclusive worktree search found no preexisting evaluation_criterion key.
    Formal criteria are not bias types, trained models, or the algorithms that enforce
    them.
  search_scope: All 442 AIO labels and scoped synonyms, 94 preceding native identities,
    and hidden/ignored-inclusive text searches of both checkouts.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Classification, BinaryClassification, CausalGraphicalModel, MetricLearning,
    Bias, SystemicBias, EvaluationBias and EthicalLLM
  accessed_at: '2026-10-11T04:52:59Z'
  support: supports
  summary: Equalized odds, demographic parity and Lipschitz individual fairness related_match
    Classification; equal opportunity related_match BinaryClassification; counterfactual
    fairness related_match CausalGraphicalModel. These are direct relationships to
    the assessed task or necessary model assumptions, not subclass assertions. MetricLearning
    does not denote a supplied similarity constraint; Bias, SystemicBias, EvaluationBias
    and EthicalLLM do not denote these formal criteria.
- evidence_id: equalizedodds-method
  kind: primary_source
  reference: https://arxiv.org/pdf/1610.02413v1
  locator: Section 2, Definition 2.1, PDF p. 3; Sections 2.2–2.3, PDF p. 4; Section
    6, PDF pp. 12–14; discussion of reliable targets and nonconclusive fairness tests,
    PDF pp. 20–21
  accessed_at: '2026-10-11T04:44:05Z'
  snapshot_sha256: e92b4f5791803e22e9f39703a161c3e710b6bf77ae04fb5d62f9d6938a5601b8
  support: supports
  summary: 'A fairness criterion requiring a predictor''s output to be conditionally
    independent of a specified protected attribute given the target outcome; for binary
    predictions and outcomes, it requires equal true-positive and false-positive rates
    across the compared groups. The cited formal definition and scoped limitations
    were inspected. Rendered pages actually inspected: 1, 2, 3, 4, 21.'
- evidence_id: equalopportunity-method
  kind: primary_source
  reference: https://arxiv.org/pdf/1610.02413v1
  locator: Section 2.1, Definition 2.2, PDF p. 4; Section 2, Definition 2.1, PDF p.
    3; Section 6, PDF pp. 12–14; reliable-target and interpretation discussion, PDF
    pp. 20–21
  accessed_at: '2026-10-11T04:44:05Z'
  snapshot_sha256: e92b4f5791803e22e9f39703a161c3e710b6bf77ae04fb5d62f9d6938a5601b8
  support: supports
  summary: 'A binary-classification fairness criterion requiring equal probabilities
    of a positive prediction across specified protected groups among individuals whose
    target outcome is the designated positive outcome. The cited formal definition
    and scoped limitations were inspected. Rendered pages actually inspected: 1, 2,
    3, 4, 21.'
- evidence_id: demographicparity-method
  kind: primary_source
  reference: https://arxiv.org/pdf/1610.02413v1
  locator: Section 1, demographic-parity definition and limitations, PDF pp. 1–2
  accessed_at: '2026-10-11T04:44:05Z'
  snapshot_sha256: e92b4f5791803e22e9f39703a161c3e710b6bf77ae04fb5d62f9d6938a5601b8
  support: supports
  summary: 'A group-level prediction criterion requiring the distribution of a decision
    or prediction to be independent of a specified protected attribute; for a binary
    decision, the positive-decision rate is equal across the compared groups. The
    cited formal definition and scoped limitations were inspected. Rendered pages
    actually inspected: 1, 2, 3, 4, 21.'
- evidence_id: demographicparity-method-statistical-parity-formulation
  kind: primary_source
  reference: https://arxiv.org/pdf/1104.3913v2
  locator: Section 3, Definition 3.1, printed p. 7 / PDF p. 8; Section 3.1 examples,
    printed p. 8 / PDF p. 9
  accessed_at: '2026-10-11T04:44:05Z'
  snapshot_sha256: 0a5afde6e5a29b3013a8d899d0abd4a6ce929d3be8c68e5f7cea7abfe54d1805
  support: supports
  summary: 'The statistical-parity formulation compares group output distributions
    by total variation with a stated tolerance; exact parity is its zero-tolerance
    case. The accompanying examples show that group parity can coexist with unequal
    treatment within groups and does not imply parity for all subgroups. This evidence
    supports the stated scope or limitation, not an unrestricted fairness guarantee.
    Rendered pages actually inspected: 1, 5, 8, 9.'
- evidence_id: demographicparity-method-causal-parity-analysis
  kind: primary_source
  reference: https://arxiv.org/pdf/2208.03843v4
  locator: Related Work distinction between a fixed and freely constructed causal
    model, PDF p. 3; Criteria 3 and Theorems 4–5, PDF p. 4
  accessed_at: '2026-10-11T04:45:58Z'
  snapshot_sha256: ebc09da1ee780fdc7bdc26f5d4e16fdd15fc2f98c081ab1af0ddcce990d35969
  support: supports
  summary: 'Rosenblatt and Witter derive connections with counterfactual fairness
    using their Criteria 3 independence assumption. Their conversion from demographic
    parity introduces a causal model and latent-variable construction of their choice;
    they explicitly distinguish that setting from checking a predictor against a fixed
    causal model. These results do not justify treating the two criterion identities
    as synonyms. This evidence supports the stated scope or limitation, not an unrestricted
    fairness guarantee. Rendered pages actually inspected: 3, 4.'
- evidence_id: lipschitzindividualfairness-method
  kind: primary_source
  reference: https://arxiv.org/pdf/1104.3913v2
  locator: Sections 1.1–1.2, printed pp. 1–3 / PDF pp. 2–4; Section 2, Definition
    2.1 and equation (1), printed p. 4 / PDF p. 5; Section 2.1 probability metrics
    and Remark 2.1, printed p. 5 / PDF p. 6
  accessed_at: '2026-10-11T04:44:05Z'
  snapshot_sha256: 0a5afde6e5a29b3013a8d899d0abd4a6ce929d3be8c68e5f7cea7abfe54d1805
  support: supports
  summary: 'An individual-fairness criterion requiring the distance between the output
    distributions assigned by a randomized classifier to any two individuals to be
    no greater than their task-specific similarity distance. The cited formal definition
    and scoped limitations were inspected. Rendered pages actually inspected: 1, 5,
    6, 8, 9.'
- evidence_id: counterfactualfairness-method
  kind: primary_source
  reference: https://arxiv.org/pdf/1703.06856v3
  locator: Section 2.2 and Section 3, Definition 5/equation (1), PDF p. 3; Section
    3.2, Lemma 1 and its qualification, PDF p. 5; Sections 4.2–4.3, causal assumptions
    and interpretive limits, PDF p. 7
  accessed_at: '2026-10-11T04:44:06Z'
  snapshot_sha256: 2d7371209e44943bcb2852f23a889b710e2903b2d8830295ff98ab8f730db5bf
  support: supports
  summary: 'A fairness criterion in a specified causal model requiring a predictor''s
    conditional output distribution, given an individual''s observed attributes and
    protected-attribute value, to remain unchanged under counterfactual interventions
    that assign other attainable protected-attribute values. The cited formal definition
    and scoped limitations were inspected. Rendered pages actually inspected: 3, 5,
    7.'
- evidence_id: counterfactualfairness-method-confounding-sensitivity
  kind: primary_source
  reference: https://proceedings.mlr.press/v115/kilbertus20a/kilbertus20a.pdf
  locator: Section 2.1, PDF pp. 2–3 (volume pp. 617–618); Section 3.1 and Figure 1,
    PDF p. 4 (volume p. 619)
  accessed_at: '2026-10-11T04:45:31Z'
  snapshot_sha256: f7083ab492a2afafe2eb6e44d7b42f72971be8080c95eef4c05d23ad326cc815
  support: supports
  summary: 'The sensitivity study distinguishes a guessed model used to construct
    a fair predictor from a model allowing additional unobserved confounding through
    correlated errors. Fairness in the guessed model does not guarantee fairness under
    the alternative data-generating assumptions; the paper frames this as sensitivity
    analysis rather than identification of a uniquely correct hidden model. This evidence
    supports the stated scope or limitation, not an unrestricted fairness guarantee.
    Rendered pages actually inspected: 2, 3, 4.'
- evidence_id: counterfactualfairness-method-causal-parity-analysis
  kind: primary_source
  reference: https://arxiv.org/pdf/2208.03843v4
  locator: Related Work distinction between a fixed and freely constructed causal
    model, PDF p. 3; Criteria 3 and Theorems 4–5, PDF p. 4
  accessed_at: '2026-10-11T04:45:58Z'
  snapshot_sha256: ebc09da1ee780fdc7bdc26f5d4e16fdd15fc2f98c081ab1af0ddcce990d35969
  support: supports
  summary: 'Rosenblatt and Witter''s parity connections use their explicit independence
    criterion for latent and protected variables, and the demographic-parity-to-counterfactual-fairness
    direction constructs a causal model and latent representation. The paper distinguishes
    that setting from assessment with a fixed causal model; the relationship is not
    an unrestricted synonym assertion. This evidence supports the stated scope or
    limitation, not an unrestricted fairness guarantee. Rendered pages actually inspected:
    3, 4.'
assessments:
- assessment_id: equalizedodds-method
  area: evidence
  topic: Criterion identity, conditioning/model assumptions, source support and mapping
    direction
  outcome: supported
  target_ids:
  - AIMech:EqualizedOdds
  evidence_ids:
  - equalizedodds-method
  - identity-search
  - mapping
  summary: This is the distributional criterion in Hardt, Price and Srebro's Definition
    2.1, not their postprocessing algorithm, a bias type, demographic parity or a
    claim of overall social fairness. Equal opportunity is a weaker positive-outcome-only
    constraint. All 442 pinned AIO labels/scoped synonyms and 94 preceding native
    identities were compared, with ignored-inclusive text searches in both checkouts.
  details: 'The conditioning outcome and protected groups must be specified, with
    estimable nonzero-probability conditioning strata for rate comparisons. Biased
    or unreliable outcome labels can undermine interpretation. Equal true-positive
    and false-positive rates do not require identical overall accuracy when group
    outcome prevalences differ. The record uses the formal conditional-independence
    definition, not the source''s informal equal-accuracy wording. This is an oblivious
    distributional test: identical prediction/outcome/group statistics can arise from
    different underlying dependency structures. Satisfaction or violation alone is
    not conclusive evidence of overall fairness or unfairness. Finite-sample uncertainty,
    a tolerance and domain-specific interpretation are needed in an application; no
    empirical result, universal fairness guarantee or legal-compliance claim is asserted.'
  dimensions:
  - name: concept-kind
    value: evaluation_criterion
    definition: A condition used to assess predictions, distinct from a procedure
      for estimating or enforcing it.
    evidence_ids:
    - equalizedodds-method
  - name: mapping-direction
    value: related_match to AIO:Classification
    definition: The criterion constrains classifier predictions and error rates in
      its central binary setting. Classification denotes the prediction task; equalized
      odds denotes a condition used to assess its outputs, so this is a direct task/criterion
      relationship rather than equivalence or subclassing.
    evidence_ids:
    - equalizedodds-method
    - mapping
- assessment_id: equalopportunity-method
  area: evidence
  topic: Criterion identity, conditioning/model assumptions, source support and mapping
    direction
  outcome: supported
  target_ids:
  - AIMech:EqualOpportunity
  evidence_ids:
  - equalopportunity-method
  - identity-search
  - mapping
  summary: The identity is Hardt, Price and Srebro's Definition 2.2, with the positive
    target designated as the advantaged outcome. It is not the wider philosophical
    meaning of equal opportunity, the full equalized-odds condition, or a threshold-adjustment
    algorithm. Identity searches covered all 442 AIO labels and scoped synonyms, 94
    preceding native records and ignored/hidden-inclusive text in both checkouts.
  details: The definition depends on which target outcome is designated positive/advantaged;
    changing that designation changes the constrained population. Equal opportunity
    alone does not equalize false-positive rates, selection rates, predictive values
    or individual treatment. The criterion requires meaningful target labels and sufficiently
    supported group/positive-outcome strata. Finite-sample uncertainty is not eliminated
    by writing an equality. Like other oblivious criteria, this condition does not
    determine the causal process or establish overall social fairness, empirical utility
    or legal compliance.
  dimensions:
  - name: concept-kind
    value: evaluation_criterion
    definition: A condition used to assess predictions, distinct from a procedure
      for estimating or enforcing it.
    evidence_ids:
    - equalopportunity-method
  - name: mapping-direction
    value: related_match to AIO:BinaryClassification
    definition: The criterion directly constrains true-positive rates of binary classifiers.
      BinaryClassification is the task on which the condition is evaluated; it is
      not a broader class of fairness criteria or an equivalent identity.
    evidence_ids:
    - equalopportunity-method
    - mapping
- assessment_id: demographicparity-method
  area: evidence
  topic: Criterion identity, conditioning/model assumptions, source support and mapping
    direction
  outcome: supported
  target_ids:
  - AIMech:DemographicParity
  evidence_ids:
  - demographicparity-method
  - identity-search
  - mapping
  - demographicparity-method-statistical-parity-formulation
  - demographicparity-method-causal-parity-analysis
  summary: The record denotes exact distributional parity, also called statistical
    parity in the inspected fairness literature. It is not equalized odds, equality
    of true-positive rates, an approximate disparity tolerance, or a complete fairness
    judgment. All 442 AIO identities/scoped synonyms, 94 native identities and ignored-inclusive
    text in both checkouts were searched. Conditional parity and parity for selected
    subgroups require separately stated conditioning and scope.
  details: Matching group output rates does not ensure similar individuals receive
    similar treatment or that parity holds within every subgroup. If target outcomes
    have different prevalences by group, a perfectly accurate predictor can violate
    demographic parity. This statistical observation does not by itself choose which
    fairness criterion a domain should use. Exact independence is distinct from approximate
    parity within a specified tolerance; an empirical estimate needs uncertainty and
    population context. Connections to counterfactual fairness depend on causal-model
    assumptions and how the predictor/model is constructed. Shared population statistics
    do not make the two definitions interchangeable for a fixed causal model.
  dimensions:
  - name: concept-kind
    value: evaluation_criterion
    definition: A condition used to assess predictions, distinct from a procedure
      for estimating or enforcing it.
    evidence_ids:
    - demographicparity-method
  - name: mapping-direction
    value: related_match to AIO:Classification
    definition: Demographic parity directly constrains the distribution of classifier
      decisions across groups. Classification is a task to which this output criterion
      applies, not an equivalent criterion or a bias type; the mapping does not limit
      the mathematical independence condition to binary outputs.
    evidence_ids:
    - demographicparity-method
    - mapping
- assessment_id: lipschitzindividualfairness-method
  area: evidence
  topic: Criterion identity, conditioning/model assumptions, source support and mapping
    direction
  outcome: supported
  target_ids:
  - AIMech:LipschitzIndividualFairness
  evidence_ids:
  - lipschitzindividualfairness-method
  - identity-search
  - mapping
  summary: The record is the explicit (D,d)-Lipschitz condition in Dwork and colleagues'
    framework. It is narrower than every possible notion of individual fairness and
    separate from their loss-minimizing linear-program construction, metric-learning
    algorithms, differential privacy and group parity. Identity assessment covered
    442 AIO labels/scoped synonyms, 94 preceding native identities and ignored-inclusive
    searches of both checkouts.
  details: The task-specific distance and output-distance choice determine the constraint.
    The framework does not certify that a chosen similarity metric represents an appropriate
    social or domain judgment. A constant output distribution satisfies the condition;
    useful predictions require a separate utility objective. Criterion satisfaction
    alone does not guarantee predictive quality. The formulation over an inspected
    finite population does not itself guarantee generalization to unobserved individuals.
    Group-parity implications require additional conditions on the metric and group
    distributions. This record does not equate the criterion with all individual-fairness
    notions, certify the paper's full optimization/theorem results, or assert legal
    compliance.
  dimensions:
  - name: concept-kind
    value: evaluation_criterion
    definition: A condition used to assess predictions, distinct from a procedure
      for estimating or enforcing it.
    evidence_ids:
    - lipschitzindividualfairness-method
  - name: mapping-direction
    value: related_match to AIO:Classification
    definition: 'The condition directly constrains randomized classifiers'' outcome
      distributions. Classification denotes the task while this local concept denotes
      a constraint on its mapping, so related_match preserves the abstraction difference.
      MetricLearning is not a substitute: the defining criterion assumes a task metric
      rather than specifying a neural procedure that learns one.'
    evidence_ids:
    - lipschitzindividualfairness-method
    - mapping
- assessment_id: counterfactualfairness-method
  area: evidence
  topic: Criterion identity, conditioning/model assumptions, source support and mapping
    direction
  outcome: supported
  target_ids:
  - AIMech:CounterfactualFairness
  evidence_ids:
  - counterfactualfairness-method
  - identity-search
  - mapping
  - counterfactualfairness-method-confounding-sensitivity
  - counterfactualfairness-method-causal-parity-analysis
  summary: This is Kusner and colleagues' Definition 5, an equality of conditional
    counterfactual distributions. It is not merely changing an input feature while
    freezing its causal descendants, a group-level observational equality, the FAIRLEARNING
    algorithm, or a generic guarantee of social fairness. All 442 pinned AIO labels/scoped
    synonyms, 94 preceding native identities and ignored-inclusive text in both checkouts
    were searched. Later parity connections do not establish identity under an arbitrary
    fixed causal model.
  details: The comparison depends on causal and counterfactual assumptions that observational
    data alone generally cannot establish. Specifying protected attributes and meaningful
    interventions requires domain interpretation. Ignoring protected attributes as
    explicit inputs is insufficient when other inputs carry their causal effects.
    Conversely, using a descendant is not categorically excluded if the relevant total
    dependence cancels, as the source qualifies its sufficient construction. A predictor
    satisfying the condition in an assumed model need not satisfy it under a model
    with omitted confounding; the inspected sensitivity paper studies this vulnerability
    in additive-noise models. The criterion constrains conditional output distributions,
    not necessarily pointwise equality for every unobserved state or usefulness of
    a predictor. Connections to demographic parity retain their model/independence
    assumptions.
  dimensions:
  - name: concept-kind
    value: evaluation_criterion
    definition: A condition used to assess predictions, distinct from a procedure
      for estimating or enforcing it.
    evidence_ids:
    - counterfactualfairness-method
  - name: mapping-direction
    value: related_match to AIO:CausalGraphicalModel
    definition: The criterion is defined and assessed using a structural causal model
      that encodes the data-generating assumptions. AIO CausalGraphicalModel describes
      that supporting model type; the criterion itself is neither a graphical model
      nor an equivalent causal graph.
    evidence_ids:
    - counterfactualfairness-method
    - mapping
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:EqualizedOdds
  - AIMech:EqualOpportunity
  - AIMech:DemographicParity
  - AIMech:LipschitzIndividualFairness
  - AIMech:CounterfactualFairness
  evidence_ids:
  - identity-search
  - mapping
  - equalizedodds-method
  - equalopportunity-method
  - demographicparity-method
  - demographicparity-method-statistical-parity-formulation
  - demographicparity-method-causal-parity-analysis
  - lipschitzindividualfairness-method
  - counterfactualfairness-method
  - counterfactualfairness-method-confounding-sensitivity
  - counterfactualfairness-method-causal-parity-analysis
  rationale: Retain equalized odds, its positive-outcome relaxation, marginal demographic
    parity, the supplied-metric Lipschitz condition and model-conditioned counterfactual
    fairness as distinct criteria. Different conditioning and model assumptions define
    different identities even when some predictors satisfy several criteria. Statistical
    parity is retained as an alias of demographic parity in the exact distributional
    sense.
- action: defer
  target_ids:
  - AIMech:EqualizedOdds
  - AIMech:EqualOpportunity
  - AIMech:DemographicParity
  - AIMech:LipschitzIndividualFairness
  - AIMech:CounterfactualFairness
  evidence_ids:
  - equalizedodds-method
  - equalopportunity-method
  - demographicparity-method
  - demographicparity-method-statistical-parity-formulation
  - demographicparity-method-causal-parity-analysis
  - lipschitzindividualfairness-method
  - counterfactualfairness-method
  - counterfactualfairness-method-confounding-sensitivity
  - counterfactualfairness-method-causal-parity-analysis
  rationale: Postprocessing, fairness linear programs, FAIRLEARNING, sensitivity algorithms
    and further criteria need separately scoped primary-method assessments. The causal/parity
    paper does not justify merging the two definitions for an arbitrary fixed causal
    model.
limitations:
- Scientific adversarial self-review, not independent approval; all five records remain
  DRAFT.
- Formal-criterion satisfaction does not by itself establish overall fairness, normative
  suitability, predictive quality or legal compliance.
- The later parity analysis retains its explicit independence criterion and freedom
  to construct a causal model; the original counterfactual criterion is not merged
  with observational parity.
- The report includes a curator arithmetic counterexample showing equal error rates
  need not imply equal overall accuracy when prevalences differ. This is not an empirical
  benchmark.
- The downloaded Hardt and Dwork title-page dates differ from their arXiv version
  dates; both observations and exact PDF hashes are retained.
- Publisher DOI/PDF failures were resolved by opening the publisher landing page and
  using the public exact arXiv version. No unseen publisher PDF review is claimed.
- No full proof certification, benchmark reproduction or finite-data fairness audit
  was performed.
- All required checks passed, and discovery remains ongoing.
tags:
- native-concepts
- fairness
- formal-criteria
- primary-papers
- self-review
- discovery-ongoing
```
