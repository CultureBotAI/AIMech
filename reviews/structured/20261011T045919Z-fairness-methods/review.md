# Scientific self-review of five fairness methods

- Review: 20261011T045919Z-fairness-methods
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T04:59:19Z
- Finished UTC: 2026-10-11T04:59:19Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All five additions have inspected primary-method support and explicit related AIO mappings. Review checked procedure versus criterion identity, binary derived-predictor optimality, finite-population metric constraints, latent versus posterior-mean predictors, the working versus alternative causal models, and the published sensitivity optimizer’s covariance and local-optimization limitations. No actionable unresolved record defect was found.

## Scope And Provenance

Identity, mechanism, evidence versions, limitations and AIO mappings for three fairness learning/postprocessing algorithms and two sensitivity evaluation methods.

Selection: Exactly the five maintained targets in the fairness-methods discovery ledger, with no sampling.
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base afa7ae454a28b83b533b293bfc7689682035a00d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:EqualizedOddsBinaryPostprocessing | data/curated/EqualizedOddsBinaryPostprocessing.yaml | maintained | Equalized-odds postprocessing for binary predictors |
| AIMech:FairnessLP | data/curated/FairnessLP.yaml | maintained | Fairness LP |
| AIMech:FairLearning | data/curated/FairLearning.yaml | maintained | FAIRLEARNING |
| AIMech:BivariateCounterfactualFairnessSensitivity | data/curated/BivariateCounterfactualFairnessSensitivity.yaml | maintained | Bivariate counterfactual-fairness sensitivity analysis |
| AIMech:MaxCFU | data/curated/MaxCFU.yaml | maintained | MAXCFU |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:EqualizedOddsBinaryPostprocessing, AIMech:FairnessLP, AIMech:FairLearning, AIMech:BivariateCounterfactualFairnessSensitivity, AIMech:MaxCFU | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate | passed | True | AIMech:EqualizedOddsBinaryPostprocessing, AIMech:FairnessLP, AIMech:FairLearning, AIMech:BivariateCounterfactualFairnessSensitivity, AIMech:MaxCFU | Checked 442 record(s); 0 failed.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-curated | passed | True | AIMech:EqualizedOddsBinaryPostprocessing, AIMech:FairnessLP, AIMech:FairLearning, AIMech:BivariateCounterfactualFairnessSensitivity, AIMech:MaxCFU | Checked 104 curated concept record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli seed --check | passed | True | AIMech:EqualizedOddsBinaryPostprocessing, AIMech:FairnessLP, AIMech:FairLearning, AIMech:BivariateCounterfactualFairnessSensitivity, AIMech:MaxCFU | AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-history --base HEAD | passed | True | AIMech:EqualizedOddsBinaryPostprocessing, AIMech:FairnessLP, AIMech:FairLearning, AIMech:BivariateCounterfactualFairnessSensitivity, AIMech:MaxCFU | Checked 19 history record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python scripts/record_review.py check | passed | True | AIMech:EqualizedOddsBinaryPostprocessing, AIMech:FairnessLP, AIMech:FairLearning, AIMech:BivariateCounterfactualFairnessSensitivity, AIMech:MaxCFU | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 18,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class<br> |
| just check | passed | True | AIMech:EqualizedOddsBinaryPostprocessing, AIMech:FairnessLP, AIMech:FairLearning, AIMech:BivariateCounterfactualFairnessSensitivity, AIMech:MaxCFU | All checks passed!<br>........................................................................ [ 31%]<br>........................................................................ [ 63%]<br>........................................................................ [ 94%]<br>.........sss                                                             [100%]<br>225 passed, 3 skipped in 38.58s<br>Checked 442 record(s); 0 failed.<br>Checked 104 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 19 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 18,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:EqualizedOddsBinaryPostprocessing, AIMech:FairnessLP, AIMech:FairLearning, AIMech:BivariateCounterfactualFairnessSensitivity, AIMech:MaxCFU | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Method identity, optimization/model assumptions, source support and mapping direction

evidence: supported. Targets: AIMech:EqualizedOddsBinaryPostprocessing.

This record selects the Section 4.1 binary-input linear program. It is distinct from the EqualizedOdds criterion and from the continuous-score threshold construction in Section 4.2. Equal-opportunity-only constraints define a relaxation, not an alias here.

Optimality is over randomized predictors derived from the supplied binary prediction and group for the specified distribution and loss, not every possible predictor using raw features. Fitting needs target labels and group information; deployment needs group membership. Empirical estimates and distribution changes can invalidate population parity. The four-parameter statement assumes two groups and binary predictions; it does not assert that a general score-valued postprocessor has four parameters. Equal conditional error rates do not establish equal accuracy, individual fairness or a universal fairness judgment. The printed proof is not reproduced as implementation code.

### Method identity, optimization/model assumptions, source support and mapping direction

evidence: supported. Targets: AIMech:FairnessLP.

The source names this optimization formulation Fairness LP. It is a procedure enforcing LipschitzIndividualFairness, not the criterion itself, a generic linear-program solver or a learned similarity metric. The two documented distribution-distance choices are retained as configurations of one formulation.

The individual metric and utility loss are inputs; solving the program does not establish that either is normatively appropriate. The cited polynomial-size result concerns a finite set of individuals and outcomes with the specified distribution distances, not arbitrary metrics on output distributions or an unrestricted population. Extrapolating from sampled individuals to unseen individuals is a separate challenge explicitly noted in Remark 2.1. Individual constraints do not automatically imply demographic parity without additional assumptions about the population and metric.

### Method identity, optimization/model assumptions, source support and mapping direction

evidence: supported. Targets: AIMech:FairLearning.

The named training algorithm is distinct from CounterfactualFairness, the causal model supplied to it and any particular fitted predictor. The source distinguishes the latent predictor from its posterior-averaged reported prediction; this record preserves that distinction.

A causal model is an input, and compatible observed distributions need not identify its counterfactual assumptions. Lemma 1 applies to functions of non-descendants in the posited model. This record does not turn that lemma into an unconditional guarantee for an arbitrary deployed posterior-mean predictor or a misspecified model. Posterior inference and Monte Carlo or optimization approximations introduce computational and estimation dependencies; no exact finite-sample guarantee is asserted. Protected attributes and descendant features can inform latent posterior inference even though the latent predictive function is restricted; excluding a raw feature alone is a different procedure.

### Method identity, optimization/model assumptions, source support and mapping direction

evidence: supported. Targets: AIMech:BivariateCounterfactualFairnessSensitivity.

This record denotes the paper’s two-error grid-based sensitivity procedure. The mean squared discrepancy is its output, not another fairness criterion. The multivariate MAXCFU optimizer is separately represented because it searches a matrix of correlations with a different algorithm.

Alternative Model B is a hypothetical data-generating model, not an identified causal ground truth; the sensitivity parameter and acceptable discrepancy require domain judgment. The inspected construction uses specified additive-noise structural functions, embeddings and Gaussian error covariance, rather than arbitrary hidden confounding. Fitting, covariance invertibility and numerical grid resolution matter. The record does not certify a global maximum over all admissible models or extrapolate the source’s bivariate boundary statement to multiple error terms. Squared prediction differences depend on the prediction scale and assessed sample; they are not automatically calibrated probabilities of discrimination or a universal fairness score.

### Method identity, optimization/model assumptions, source support and mapping direction

evidence: supported. Targets: AIMech:MaxCFU.

MAXCFU is the named optimization-based tool for multivariate confounding, distinct from the bivariate grid procedure, its CFU discrepancy and the counterfactual-fairness criterion. The record describes the published search procedure, not a certified optimizer.

The published off-diagonal tanh transformation gives a symmetric unit-diagonal matrix with bounded entries but explicitly does not guarantee positive semidefiniteness. A resulting matrix is therefore not automatically a valid correlation matrix. Nested fitting and the outer search are nonconvex; local optimization, initialization and differentiation through fitting matter. No certified global worst-case value is asserted. Sensitivity is conditional on the assumed structural model, predictor, intervention, confounding budget and sample. It does not identify the true hidden confounding or establish overall fairness. The sparse clique parameterization is discussed but not exercised in the paper’s experiments, and its expressivity and numerical constraints are not certified here.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:EqualizedOddsBinaryPostprocessing, AIMech:FairnessLP, AIMech:FairLearning, AIMech:BivariateCounterfactualFairnessSensitivity, AIMech:MaxCFU. Retain the binary-output parity postprocessor, finite supplied-metric fairness program, causal posterior learning algorithm, bivariate confounding grid procedure and multivariate sensitivity optimizer as distinct procedures. The last two share a discrepancy and modeling setup but differ in search construction and supported scope. None is an alias of a fairness criterion.
- defer: AIMech:EqualizedOddsBinaryPostprocessing, AIMech:FairnessLP, AIMech:FairLearning, AIMech:BivariateCounterfactualFairnessSensitivity, AIMech:MaxCFU. Continuous-score and equal-opportunity postprocessing, path-specific sensitivity and fairness representation methods remain separate candidates; overlap of fairness goals does not establish identical concepts.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity-search | research/discovery/20261011T045749Z-fairness-methods.json | supports | All 442 AIO labels/scoped synonyms and 99 preceding native identities were compared; no identity match was found. Both checkouts were searched with hidden and ignored files included. The 46 worktree text hits were existing criterion descriptions, shared source citations, review text and discovery-frontier mentions; none denoted an existing algorithm identity. Main-checkout text search returned zero hits at that time, before its round13 fast-forward. |
| mapping | sources/aio/aio.json; Classification, BinaryClassification, CausalGraphicalModel, MetricLearning, Bias, SystemicBias, EvaluationBias and EthicalLLM | supports | Binary postprocessing related_match BinaryClassification; Fairness LP related_match Classification; FAIRLEARNING and both sensitivity methods related_match CausalGraphicalModel. These are method-to-task/model relationships, not subclass claims. MetricLearning, Bias, SystemicBias, EvaluationBias and EthicalLLM were inspected and do not denote these methods. |
| equalizedoddsbinarypostprocessing-method | https://arxiv.org/pdf/1610.02413v1; Section 4, Definition 4.1 and Section 4.1, equations (4.1)–(4.3), Proposition 4.4, PDF pp. 5–7; Section 6 and Discussion for distributional limitations | supports | A randomized postprocessing algorithm that uses a binary predictor and protected-group membership to minimize expected label loss subject to equal false-positive and true-positive rates across groups, within predictors derived from those inputs. The cited method construction and scoped limitations were inspected. Rendered pages actually inspected: 6, 7. |
| fairnesslp-method | https://arxiv.org/pdf/1104.3913v2; Section 2 and Section 2.1, Figure 1 equations (2)–(4), Lemmas 2.1–2.2 and Remark 2.1, PDF pp. 5–6 (printed pp. 4–5) | supports | A finite-population optimization procedure that assigns outcome distributions to individuals to minimize expected loss under pairwise Lipschitz similarity constraints, expressible as a linear program for the total-variation or relative-infinity distribution distances used by Dwork et al. The cited method construction and scoped limitations were inspected. Rendered pages actually inspected: 5, 6. |
| fairlearning-method | https://arxiv.org/pdf/1703.06856v3; Section 3.2 Lemma 1, Section 4.1 FAIRLEARNING pseudocode and prediction rule, Section 4.2 causal-model assumptions, PDF pp. 5–7 | supports | A causal-model-dependent learning procedure that minimizes predictive loss averaged over inferred background variables, restricting the latent predictor to those variables and observed non-descendants of protected attributes. The cited method construction and scoped limitations were inspected. Rendered pages actually inspected: 5, 6, 7. |
| bivariatecounterfactualfairnesssensitivity-method | https://proceedings.mlr.press/v115/kilbertus20a/kilbertus20a.pdf; Section 3, Tool #1: grid-based; Sections 3.1–3.4, equations (2)–(6), PDF pp. 3–6; Section 5, PDF p. 8 for grid use | supports | A model-based sensitivity procedure that varies the correlation between two structural error terms and measures how a predictor built under an unconfounded additive-noise model changes on counterfactual data generated under the alternative confounded model. The cited method construction and scoped limitations were inspected. Rendered pages actually inspected: 4, 5, 6, 8. |
| maxcfu-method | https://proceedings.mlr.press/v115/kilbertus20a/kilbertus20a.pdf; Sections 4.1–4.3, equation (7) and Algorithm 1 MAXCFU, PDF pp. 6–8; Section 3.4 equation (6) for the discrepancy | supports | A multivariate sensitivity algorithm that uses gradient ascent through fitted additive-noise models to search for large counterfactual prediction discrepancies under bounded correlations of structural error terms. The cited method construction and scoped limitations were inspected. Rendered pages actually inspected: 6, 7, 8. |
| maxcfu-method-supplement | https://proceedings.mlr.press/v115/kilbertus20a/kilbertus20a-supp.pdf; Supplementary material, Appendices A–B, PDF p. 1 | supports | The supplement identifies nested local likelihood fitting and a nonconvex sensitivity objective as computational obstacles. Its matrix counterexample shows that setting all allowed correlations to the same bound can produce an invalid covariance structure; it does not supply a general global-optimization guarantee. This evidence supports the stated scope or limitation, not an unrestricted fairness guarantee. Rendered pages actually inspected: 1. |

## Limits And Additional Notes

- Scientific adversarial author self-review, not independent approval; all five records remain DRAFT.
- The binary postprocessor’s optimality domain is derived predictors with the specified inputs and distribution; no general population guarantee follows from empirical fitting.
- Fairness LP uses a supplied metric and a finite population; extrapolation is a separate question.
- FAIRLEARNING’s latent predictive function and posterior-mean report are distinguished; the non-descendant lemma is not treated as an unconditional deployment theorem.
- MAXCFU’s published correlation transform explicitly lacks positive-semidefiniteness guarantees, and its optimization is not a certified global worst-case computation. These are preserved source limitations, not hidden record defects.
- The source PDF version/date discrepancies and reused download timestamps are retained. Render manifests do not themselves certify scientific reading.
- No implementation execution, benchmark reproduction, legal fairness conclusion or full proof certification was performed.
- All required checks passed. Prior and new frontier items remain active, so discovery has not saturated.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T045919Z-fairness-methods
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of five fairness methods
started_at: '2026-10-11T04:59:19Z'
finished_at: '2026-10-11T04:59:19Z'
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
summary: All five additions have inspected primary-method support and explicit related
  AIO mappings. Review checked procedure versus criterion identity, binary derived-predictor
  optimality, finite-population metric constraints, latent versus posterior-mean predictors,
  the working versus alternative causal models, and the published sensitivity optimizer’s
  covariance and local-optimization limitations. No actionable unresolved record defect
  was found.
source:
  git_revision: afa7ae454a28b83b533b293bfc7689682035a00d
  state: working_tree
  inputs:
  - path: data/curated/BivariateCounterfactualFairnessSensitivity.yaml
    sha256: 3d65faa795a07e4ea0c8634920ed01abfa61a2d7b7f8e5e2e838bf20c80b304c
    role: target
  - path: data/curated/EqualizedOddsBinaryPostprocessing.yaml
    sha256: 5b85bc483d30fd3b79c7b7ac64f130550429a7ce51575e467a626941e40e42f4
    role: target
  - path: data/curated/FairLearning.yaml
    sha256: 0cc2bb8f337e1d3c6e1ae1866aa7075120c9077686a03f571b004347d5341ef8
    role: target
  - path: data/curated/FairnessLP.yaml
    sha256: 20637202612330d2069f91a032ed45c388b2e345dadc8397680530ae28743b54
    role: target
  - path: data/curated/MaxCFU.yaml
    sha256: 44ed065c45c2acf860cd2ab1699797e18f4559758abf54514d7333bd8083c1df
    role: target
  - path: docs/curated-concepts.md
    sha256: c574580df592c437b965bee9a3a171f8e9dbdb9a26595a6cc238cadd55168456
    role: context
  - path: research/discovery/20261011T045749Z-fairness-methods.json
    sha256: 38de8180bdc40f92f6643e6955cd4a7ff646e723759702c7dfb2ee1747c555d4
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
- target_id: AIMech:EqualizedOddsBinaryPostprocessing
  path: data/curated/EqualizedOddsBinaryPostprocessing.yaml
  label: Equalized-odds postprocessing for binary predictors
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/EqualizedOddsBinaryPostprocessing.yaml
    role: maintained native concept
- target_id: AIMech:FairnessLP
  path: data/curated/FairnessLP.yaml
  label: Fairness LP
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FairnessLP.yaml
    role: maintained native concept
- target_id: AIMech:FairLearning
  path: data/curated/FairLearning.yaml
  label: FAIRLEARNING
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FairLearning.yaml
    role: maintained native concept
- target_id: AIMech:BivariateCounterfactualFairnessSensitivity
  path: data/curated/BivariateCounterfactualFairnessSensitivity.yaml
  label: Bivariate counterfactual-fairness sensitivity analysis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BivariateCounterfactualFairnessSensitivity.yaml
    role: maintained native concept
- target_id: AIMech:MaxCFU
  path: data/curated/MaxCFU.yaml
  label: MAXCFU
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MaxCFU.yaml
    role: maintained native concept
scope:
  description: Identity, mechanism, evidence versions, limitations and AIO mappings
    for three fairness learning/postprocessing algorithms and two sensitivity evaluation
    methods.
  selection: Exactly the five maintained targets in the fairness-methods discovery
    ledger, with no sampling.
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - AIMech:EqualizedOddsBinaryPostprocessing
  - AIMech:FairnessLP
  - AIMech:FairLearning
  - AIMech:BivariateCounterfactualFairnessSensitivity
  - AIMech:MaxCFU
  exclusions:
  - target: Executable algorithm implementations, benchmarks and complete proof certification
    reason: The records curate published methods and their limitations; these additional
      validations were not performed.
  - target: Score-valued threshold methods, path-specific variants and new representation-learning
      candidates
    reason: Retained as separately scoped frontier items needing primary-method assessment.
checks:
- check_id: required-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:EqualizedOddsBinaryPostprocessing
  - AIMech:FairnessLP
  - AIMech:FairLearning
  - AIMech:BivariateCounterfactualFairnessSensitivity
  - AIMech:MaxCFU
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
  - AIMech:EqualizedOddsBinaryPostprocessing
  - AIMech:FairnessLP
  - AIMech:FairLearning
  - AIMech:BivariateCounterfactualFairnessSensitivity
  - AIMech:MaxCFU
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
  - AIMech:EqualizedOddsBinaryPostprocessing
  - AIMech:FairnessLP
  - AIMech:FairLearning
  - AIMech:BivariateCounterfactualFairnessSensitivity
  - AIMech:MaxCFU
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 104 curated concept record(s); 0 error(s).

    '
- check_id: required-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:EqualizedOddsBinaryPostprocessing
  - AIMech:FairnessLP
  - AIMech:FairLearning
  - AIMech:BivariateCounterfactualFairnessSensitivity
  - AIMech:MaxCFU
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
  - AIMech:EqualizedOddsBinaryPostprocessing
  - AIMech:FairnessLP
  - AIMech:FairLearning
  - AIMech:BivariateCounterfactualFairnessSensitivity
  - AIMech:MaxCFU
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 19 history record(s); 0 error(s).

    '
- check_id: required-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:EqualizedOddsBinaryPostprocessing
  - AIMech:FairnessLP
  - AIMech:FairLearning
  - AIMech:BivariateCounterfactualFairnessSensitivity
  - AIMech:MaxCFU
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 18,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\ntopClass is deprecated - use top_class\n"
- check_id: required-6
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:EqualizedOddsBinaryPostprocessing
  - AIMech:FairnessLP
  - AIMech:FairLearning
  - AIMech:BivariateCounterfactualFairnessSensitivity
  - AIMech:MaxCFU
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 31%]\n........................................................................\
    \ [ 63%]\n........................................................................\
    \ [ 94%]\n.........sss                                                       \
    \      [100%]\n225 passed, 3 skipped in 38.58s\nChecked 442 record(s); 0 failed.\n\
    Checked 104 curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing,\
    \ 0 changed, 0 unexpected.\nChecked 19 history record(s); 0 error(s).\n{\n  \"\
    repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 18,\n  \"coverage\"\
    : \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-7
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:EqualizedOddsBinaryPostprocessing
  - AIMech:FairnessLP
  - AIMech:FairLearning
  - AIMech:BivariateCounterfactualFairnessSensitivity
  - AIMech:MaxCFU
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity-search
  kind: search
  reference: research/discovery/20261011T045749Z-fairness-methods.json
  accessed_at: '2026-10-11T04:59:19Z'
  support: supports
  summary: All 442 AIO labels/scoped synonyms and 99 preceding native identities were
    compared; no identity match was found. Both checkouts were searched with hidden
    and ignored files included. The 46 worktree text hits were existing criterion
    descriptions, shared source citations, review text and discovery-frontier mentions;
    none denoted an existing algorithm identity. Main-checkout text search returned
    zero hits at that time, before its round13 fast-forward.
  search_scope: All 442 AIO labels and scoped synonyms, 99 preceding native identities,
    and hidden/ignored-inclusive text searches of both checkouts.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Classification, BinaryClassification, CausalGraphicalModel, MetricLearning,
    Bias, SystemicBias, EvaluationBias and EthicalLLM
  accessed_at: '2026-10-11T04:59:19Z'
  support: supports
  summary: Binary postprocessing related_match BinaryClassification; Fairness LP related_match
    Classification; FAIRLEARNING and both sensitivity methods related_match CausalGraphicalModel.
    These are method-to-task/model relationships, not subclass claims. MetricLearning,
    Bias, SystemicBias, EvaluationBias and EthicalLLM were inspected and do not denote
    these methods.
- evidence_id: equalizedoddsbinarypostprocessing-method
  kind: primary_source
  reference: https://arxiv.org/pdf/1610.02413v1
  locator: Section 4, Definition 4.1 and Section 4.1, equations (4.1)–(4.3), Proposition
    4.4, PDF pp. 5–7; Section 6 and Discussion for distributional limitations
  accessed_at: '2026-10-11T04:44:05Z'
  snapshot_sha256: e92b4f5791803e22e9f39703a161c3e710b6bf77ae04fb5d62f9d6938a5601b8
  support: supports
  summary: 'A randomized postprocessing algorithm that uses a binary predictor and
    protected-group membership to minimize expected label loss subject to equal false-positive
    and true-positive rates across groups, within predictors derived from those inputs.
    The cited method construction and scoped limitations were inspected. Rendered
    pages actually inspected: 6, 7.'
- evidence_id: fairnesslp-method
  kind: primary_source
  reference: https://arxiv.org/pdf/1104.3913v2
  locator: Section 2 and Section 2.1, Figure 1 equations (2)–(4), Lemmas 2.1–2.2 and
    Remark 2.1, PDF pp. 5–6 (printed pp. 4–5)
  accessed_at: '2026-10-11T04:44:05Z'
  snapshot_sha256: 0a5afde6e5a29b3013a8d899d0abd4a6ce929d3be8c68e5f7cea7abfe54d1805
  support: supports
  summary: 'A finite-population optimization procedure that assigns outcome distributions
    to individuals to minimize expected loss under pairwise Lipschitz similarity constraints,
    expressible as a linear program for the total-variation or relative-infinity distribution
    distances used by Dwork et al. The cited method construction and scoped limitations
    were inspected. Rendered pages actually inspected: 5, 6.'
- evidence_id: fairlearning-method
  kind: primary_source
  reference: https://arxiv.org/pdf/1703.06856v3
  locator: Section 3.2 Lemma 1, Section 4.1 FAIRLEARNING pseudocode and prediction
    rule, Section 4.2 causal-model assumptions, PDF pp. 5–7
  accessed_at: '2026-10-11T04:44:06Z'
  snapshot_sha256: 2d7371209e44943bcb2852f23a889b710e2903b2d8830295ff98ab8f730db5bf
  support: supports
  summary: 'A causal-model-dependent learning procedure that minimizes predictive
    loss averaged over inferred background variables, restricting the latent predictor
    to those variables and observed non-descendants of protected attributes. The cited
    method construction and scoped limitations were inspected. Rendered pages actually
    inspected: 5, 6, 7.'
- evidence_id: bivariatecounterfactualfairnesssensitivity-method
  kind: primary_source
  reference: https://proceedings.mlr.press/v115/kilbertus20a/kilbertus20a.pdf
  locator: 'Section 3, Tool #1: grid-based; Sections 3.1–3.4, equations (2)–(6), PDF
    pp. 3–6; Section 5, PDF p. 8 for grid use'
  accessed_at: '2026-10-11T04:45:31Z'
  snapshot_sha256: f7083ab492a2afafe2eb6e44d7b42f72971be8080c95eef4c05d23ad326cc815
  support: supports
  summary: 'A model-based sensitivity procedure that varies the correlation between
    two structural error terms and measures how a predictor built under an unconfounded
    additive-noise model changes on counterfactual data generated under the alternative
    confounded model. The cited method construction and scoped limitations were inspected.
    Rendered pages actually inspected: 4, 5, 6, 8.'
- evidence_id: maxcfu-method
  kind: primary_source
  reference: https://proceedings.mlr.press/v115/kilbertus20a/kilbertus20a.pdf
  locator: Sections 4.1–4.3, equation (7) and Algorithm 1 MAXCFU, PDF pp. 6–8; Section
    3.4 equation (6) for the discrepancy
  accessed_at: '2026-10-11T04:45:31Z'
  snapshot_sha256: f7083ab492a2afafe2eb6e44d7b42f72971be8080c95eef4c05d23ad326cc815
  support: supports
  summary: 'A multivariate sensitivity algorithm that uses gradient ascent through
    fitted additive-noise models to search for large counterfactual prediction discrepancies
    under bounded correlations of structural error terms. The cited method construction
    and scoped limitations were inspected. Rendered pages actually inspected: 6, 7,
    8.'
- evidence_id: maxcfu-method-supplement
  kind: primary_source
  reference: https://proceedings.mlr.press/v115/kilbertus20a/kilbertus20a-supp.pdf
  locator: Supplementary material, Appendices A–B, PDF p. 1
  accessed_at: '2026-10-11T04:54:54Z'
  snapshot_sha256: 238a9527530e02c625fda2006fe3a190e4159e5da75ad19b5ce88580747d552e
  support: supports
  summary: 'The supplement identifies nested local likelihood fitting and a nonconvex
    sensitivity objective as computational obstacles. Its matrix counterexample shows
    that setting all allowed correlations to the same bound can produce an invalid
    covariance structure; it does not supply a general global-optimization guarantee.
    This evidence supports the stated scope or limitation, not an unrestricted fairness
    guarantee. Rendered pages actually inspected: 1.'
assessments:
- assessment_id: equalizedoddsbinarypostprocessing-method
  area: evidence
  topic: Method identity, optimization/model assumptions, source support and mapping
    direction
  outcome: supported
  target_ids:
  - AIMech:EqualizedOddsBinaryPostprocessing
  evidence_ids:
  - equalizedoddsbinarypostprocessing-method
  - identity-search
  - mapping
  summary: This record selects the Section 4.1 binary-input linear program. It is
    distinct from the EqualizedOdds criterion and from the continuous-score threshold
    construction in Section 4.2. Equal-opportunity-only constraints define a relaxation,
    not an alias here.
  details: Optimality is over randomized predictors derived from the supplied binary
    prediction and group for the specified distribution and loss, not every possible
    predictor using raw features. Fitting needs target labels and group information;
    deployment needs group membership. Empirical estimates and distribution changes
    can invalidate population parity. The four-parameter statement assumes two groups
    and binary predictions; it does not assert that a general score-valued postprocessor
    has four parameters. Equal conditional error rates do not establish equal accuracy,
    individual fairness or a universal fairness judgment. The printed proof is not
    reproduced as implementation code.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A learning/postprocessing algorithm or a procedure for evaluating
      sensitivity, distinct from the criterion it targets.
    evidence_ids:
    - equalizedoddsbinarypostprocessing-method
  - name: mapping-direction
    value: related_match to AIO:BinaryClassification
    definition: Postprocesses binary classification decisions; the algorithm and the
      task are related at different abstraction levels, so this is not an equivalence
      or subclass assertion.
    evidence_ids:
    - equalizedoddsbinarypostprocessing-method
    - mapping
- assessment_id: fairnesslp-method
  area: evidence
  topic: Method identity, optimization/model assumptions, source support and mapping
    direction
  outcome: supported
  target_ids:
  - AIMech:FairnessLP
  evidence_ids:
  - fairnesslp-method
  - identity-search
  - mapping
  summary: The source names this optimization formulation Fairness LP. It is a procedure
    enforcing LipschitzIndividualFairness, not the criterion itself, a generic linear-program
    solver or a learned similarity metric. The two documented distribution-distance
    choices are retained as configurations of one formulation.
  details: The individual metric and utility loss are inputs; solving the program
    does not establish that either is normatively appropriate. The cited polynomial-size
    result concerns a finite set of individuals and outcomes with the specified distribution
    distances, not arbitrary metrics on output distributions or an unrestricted population.
    Extrapolating from sampled individuals to unseen individuals is a separate challenge
    explicitly noted in Remark 2.1. Individual constraints do not automatically imply
    demographic parity without additional assumptions about the population and metric.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A learning/postprocessing algorithm or a procedure for evaluating
      sensitivity, distinct from the criterion it targets.
    evidence_ids:
    - fairnesslp-method
  - name: mapping-direction
    value: related_match to AIO:Classification
    definition: Computes a randomized classification assignment. Classification denotes
      the task, while this record denotes its constrained optimization procedure;
      MetricLearning instead learns representations and does not denote this supplied-metric
      program.
    evidence_ids:
    - fairnesslp-method
    - mapping
- assessment_id: fairlearning-method
  area: evidence
  topic: Method identity, optimization/model assumptions, source support and mapping
    direction
  outcome: supported
  target_ids:
  - AIMech:FairLearning
  evidence_ids:
  - fairlearning-method
  - identity-search
  - mapping
  summary: The named training algorithm is distinct from CounterfactualFairness, the
    causal model supplied to it and any particular fitted predictor. The source distinguishes
    the latent predictor from its posterior-averaged reported prediction; this record
    preserves that distinction.
  details: A causal model is an input, and compatible observed distributions need
    not identify its counterfactual assumptions. Lemma 1 applies to functions of non-descendants
    in the posited model. This record does not turn that lemma into an unconditional
    guarantee for an arbitrary deployed posterior-mean predictor or a misspecified
    model. Posterior inference and Monte Carlo or optimization approximations introduce
    computational and estimation dependencies; no exact finite-sample guarantee is
    asserted. Protected attributes and descendant features can inform latent posterior
    inference even though the latent predictive function is restricted; excluding
    a raw feature alone is a different procedure.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A learning/postprocessing algorithm or a procedure for evaluating
      sensitivity, distinct from the criterion it targets.
    evidence_ids:
    - fairlearning-method
  - name: mapping-direction
    value: related_match to AIO:CausalGraphicalModel
    definition: Requires a causal graphical model to infer background variables and
      identify non-descendants. It is a learning algorithm using the model, not a
      causal model family or an AIO subclass claim.
    evidence_ids:
    - fairlearning-method
    - mapping
- assessment_id: bivariatecounterfactualfairnesssensitivity-method
  area: evidence
  topic: Method identity, optimization/model assumptions, source support and mapping
    direction
  outcome: supported
  target_ids:
  - AIMech:BivariateCounterfactualFairnessSensitivity
  evidence_ids:
  - bivariatecounterfactualfairnesssensitivity-method
  - identity-search
  - mapping
  summary: This record denotes the paper’s two-error grid-based sensitivity procedure.
    The mean squared discrepancy is its output, not another fairness criterion. The
    multivariate MAXCFU optimizer is separately represented because it searches a
    matrix of correlations with a different algorithm.
  details: Alternative Model B is a hypothetical data-generating model, not an identified
    causal ground truth; the sensitivity parameter and acceptable discrepancy require
    domain judgment. The inspected construction uses specified additive-noise structural
    functions, embeddings and Gaussian error covariance, rather than arbitrary hidden
    confounding. Fitting, covariance invertibility and numerical grid resolution matter.
    The record does not certify a global maximum over all admissible models or extrapolate
    the source’s bivariate boundary statement to multiple error terms. Squared prediction
    differences depend on the prediction scale and assessed sample; they are not automatically
    calibrated probabilities of discrimination or a universal fairness score.
  dimensions:
  - name: concept-kind
    value: evaluation_method
    definition: A learning/postprocessing algorithm or a procedure for evaluating
      sensitivity, distinct from the criterion it targets.
    evidence_ids:
    - bivariatecounterfactualfairnesssensitivity-method
  - name: mapping-direction
    value: related_match to AIO:CausalGraphicalModel
    definition: Evaluates predictor sensitivity using alternative causal graphical
      models and their counterfactuals. This evaluation procedure is not itself a
      causal model family or a type of bias.
    evidence_ids:
    - bivariatecounterfactualfairnesssensitivity-method
    - mapping
- assessment_id: maxcfu-method
  area: evidence
  topic: Method identity, optimization/model assumptions, source support and mapping
    direction
  outcome: supported
  target_ids:
  - AIMech:MaxCFU
  evidence_ids:
  - maxcfu-method
  - identity-search
  - mapping
  - maxcfu-method-supplement
  summary: MAXCFU is the named optimization-based tool for multivariate confounding,
    distinct from the bivariate grid procedure, its CFU discrepancy and the counterfactual-fairness
    criterion. The record describes the published search procedure, not a certified
    optimizer.
  details: The published off-diagonal tanh transformation gives a symmetric unit-diagonal
    matrix with bounded entries but explicitly does not guarantee positive semidefiniteness.
    A resulting matrix is therefore not automatically a valid correlation matrix.
    Nested fitting and the outer search are nonconvex; local optimization, initialization
    and differentiation through fitting matter. No certified global worst-case value
    is asserted. Sensitivity is conditional on the assumed structural model, predictor,
    intervention, confounding budget and sample. It does not identify the true hidden
    confounding or establish overall fairness. The sparse clique parameterization
    is discussed but not exercised in the paper’s experiments, and its expressivity
    and numerical constraints are not certified here.
  dimensions:
  - name: concept-kind
    value: evaluation_method
    definition: A learning/postprocessing algorithm or a procedure for evaluating
      sensitivity, distinct from the criterion it targets.
    evidence_ids:
    - maxcfu-method
  - name: mapping-direction
    value: related_match to AIO:CausalGraphicalModel
    definition: Uses counterfactuals from parameterized causal graphical models to
      assess prediction sensitivity. The evaluation algorithm and the model class
      are related, without an equivalence or subclass assertion.
    evidence_ids:
    - maxcfu-method
    - mapping
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:EqualizedOddsBinaryPostprocessing
  - AIMech:FairnessLP
  - AIMech:FairLearning
  - AIMech:BivariateCounterfactualFairnessSensitivity
  - AIMech:MaxCFU
  evidence_ids:
  - identity-search
  - mapping
  - equalizedoddsbinarypostprocessing-method
  - fairnesslp-method
  - fairlearning-method
  - bivariatecounterfactualfairnesssensitivity-method
  - maxcfu-method
  - maxcfu-method-supplement
  rationale: Retain the binary-output parity postprocessor, finite supplied-metric
    fairness program, causal posterior learning algorithm, bivariate confounding grid
    procedure and multivariate sensitivity optimizer as distinct procedures. The last
    two share a discrepancy and modeling setup but differ in search construction and
    supported scope. None is an alias of a fairness criterion.
- action: defer
  target_ids:
  - AIMech:EqualizedOddsBinaryPostprocessing
  - AIMech:FairnessLP
  - AIMech:FairLearning
  - AIMech:BivariateCounterfactualFairnessSensitivity
  - AIMech:MaxCFU
  evidence_ids:
  - equalizedoddsbinarypostprocessing-method
  - fairnesslp-method
  - fairlearning-method
  - bivariatecounterfactualfairnesssensitivity-method
  - maxcfu-method
  - maxcfu-method-supplement
  rationale: Continuous-score and equal-opportunity postprocessing, path-specific
    sensitivity and fairness representation methods remain separate candidates; overlap
    of fairness goals does not establish identical concepts.
limitations:
- Scientific adversarial author self-review, not independent approval; all five records
  remain DRAFT.
- The binary postprocessor’s optimality domain is derived predictors with the specified
  inputs and distribution; no general population guarantee follows from empirical
  fitting.
- Fairness LP uses a supplied metric and a finite population; extrapolation is a separate
  question.
- FAIRLEARNING’s latent predictive function and posterior-mean report are distinguished;
  the non-descendant lemma is not treated as an unconditional deployment theorem.
- MAXCFU’s published correlation transform explicitly lacks positive-semidefiniteness
  guarantees, and its optimization is not a certified global worst-case computation.
  These are preserved source limitations, not hidden record defects.
- The source PDF version/date discrepancies and reused download timestamps are retained.
  Render manifests do not themselves certify scientific reading.
- No implementation execution, benchmark reproduction, legal fairness conclusion or
  full proof certification was performed.
- All required checks passed. Prior and new frontier items remain active, so discovery
  has not saturated.
tags:
- native-concepts
- fairness
- learning-algorithms
- sensitivity-analysis
- primary-papers
- self-review
- discovery-ongoing
```
