# AOAS evidence-section heading finding

- Review: 20261013T200943Z-aoas-section-heading
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T20:08:24Z
- Finished UTC: 2026-10-13T20:09:43Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor source-heading wording error; no change to the cited section number or supported mechanism.

## Scope And Provenance

Exact source heading in the reported-evaluation-scope evidence locator.

Selection: Exact maintained ID AIMech:ANDORAbstractionSampling
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base dc741a357641a560541437a5d62b485d101ad23b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ANDORAbstractionSampling | data/curated/ANDORAbstractionSampling.yaml | maintained | AND/OR abstraction sampling |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corrected-input publication gates | skipped | True | AIMech:ANDORAbstractionSampling | The corrected record does not yet exist; full publication gates remain pending. |

## Scientific And Domain Assessments

### Exact heading in source citation

evidence: concern. Targets: AIMech:ANDORAbstractionSampling.

Correct the heading while preserving its correct number and pages.

The reported-evaluation-scope locator calls Section4 Experimental Evaluation, while the actual heading on PDFp6 / printedp4271 is Empirical Evaluation. The section number, page range and substantive claim are correct; the citation should use the source heading accurately.

## Findings

### F1: Correct the evaluation section heading in the AOAS citation

minor / open / confirmed; issue key: aoas-empirical-evaluation-section-heading.

The reported-evaluation-scope locator calls Section4 Experimental Evaluation, while the actual heading on PDFp6 / printedp4271 is Empirical Evaluation. The section number, page range and substantive claim are correct; the citation should use the source heading accurately.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained locator and report mirror, append edit history, regenerate the page, and save a linked successor review.

- The locator names Section4 Empirical Evaluation with the existing correct page range.
- Record/report mirror and rendered page agree.
- Corrected-input publication gates and linked successor review pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/curated/ANDORAbstractionSampling.yaml | supports | Complete maintained record read after capture; the evaluation locator misnames the heading. |
| paper | https://www.ijcai.org/proceedings/2020/0589.pdf; Section4 heading, PDFp6 / printedp4271. | supports | All9 proceedings pages read previously; after capture pages2–8 visually reread. The heading is Empirical Evaluation. |

## Limits And Additional Notes

- Partial author self-review; this minor wording correction does not change scientific scope. DRAFT remains.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T200943Z-aoas-section-heading
kind: record
repository: CultureBotAI/AIMech
title: AOAS evidence-section heading finding
started_at: '2026-10-13T20:08:24Z'
finished_at: '2026-10-13T20:09:43Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Author compared the maintained source locator with the visually
    inspected primary section heading; not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One minor source-heading wording error; no change to the cited section number
  or supported mechanism.
source:
  git_revision: dc741a357641a560541437a5d62b485d101ad23b
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/DecisionTree.yaml
    sha256: 4c2a5ed08c585f8912d66e3629aaa20e93c46ab49cfb2d128001fcd019c81bfc
    role: context
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/RecursiveLanguageModel.yaml
    sha256: 617d0f86964cea89a7259598acad60a111f6044fb10db598f060d42aaaecff02
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/SelectionAndSamplingBias.yaml
    sha256: 72d8ef34949942ddee1fe60d645806a2117b95207f681de923297b64f78cc477
    role: context
  - path: data/curated/ANDORAbstractionSampling.yaml
    sha256: a8b9f9a22e2baddb72cbf357168736426af5873f284f654b47942165752d764d
    role: target
  - path: data/curated/GenericTreeSampling.yaml
    sha256: c67305da11be269a32a696759643640d93cd7b2f46d148a73180edea8bff45e6
    role: context
  - path: data/curated/GibbsSampling.yaml
    sha256: 8175215986c0507e3664a3aedf8074fc067d85b4a89002091d1bcb9b637a522a
    role: context
  - path: data/curated/HeuristicTreeSampling.yaml
    sha256: a011848779d73ba8f15c0f5d1a12a911a0b3db30c0a9c378d1f2e74c3b9f9e76
    role: context
  - path: data/curated/KnuthBacktrackTreeEstimation.yaml
    sha256: 7230cf708f8e51b2094a37d7e4bc14c29ac63b8b1421ed41d529b08146564cc6
    role: context
  - path: data/curated/MarkovRandomField.yaml
    sha256: 03b1f2a66b2183a5bf5943bee7ec0619b9e07947d6c9187263e279ee475f9149
    role: context
  - path: research/discovery/20261013T200822Z-and-or-abstraction-sampling.json
    sha256: 3f8ebbb8f7b07663589f198dfe2011382fd4ee2f9307691fd2e9e63cd15d8c20
    role: context
  - path: research/discovery/and-or-abstraction-sampling-boundaries.py
    sha256: b03cb72f49a79df22adb11480e7de61a5b0837772bc5d7bf7fe0aef41087a33f
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
- target_id: AIMech:ANDORAbstractionSampling
  path: data/curated/ANDORAbstractionSampling.yaml
  label: AND/OR abstraction sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ANDORAbstractionSampling.yaml
    role: maintained
scope:
  description: Exact source heading in the reported-evaluation-scope evidence locator.
  selection: Exact maintained ID AIMech:ANDORAbstractionSampling
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - AIMech:ANDORAbstractionSampling
  exclusions:
  - target: Corrected-input complete review
    reason: Pending the narrow citation edit and publication gates.
checks:
- check_id: corrected-publication
  name: Corrected-input publication gates
  status: skipped
  required: true
  target_ids:
  - AIMech:ANDORAbstractionSampling
  summary: The corrected record does not yet exist; full publication gates remain
    pending.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/curated/ANDORAbstractionSampling.yaml
  accessed_at: '2026-10-13T20:09:43Z'
  snapshot_sha256: a8b9f9a22e2baddb72cbf357168736426af5873f284f654b47942165752d764d
  support: supports
  summary: Complete maintained record read after capture; the evaluation locator misnames
    the heading.
- evidence_id: paper
  kind: primary_source
  reference: https://www.ijcai.org/proceedings/2020/0589.pdf
  accessed_at: '2026-10-13T19:31:53Z'
  snapshot_sha256: 5ad89392088b4b257dd654b4f1078ea232271c72913246cd1340de1dc510955e
  support: supports
  locator: Section4 heading, PDFp6 / printedp4271.
  summary: All9 proceedings pages read previously; after capture pages2–8 visually
    reread. The heading is Empirical Evaluation.
assessments:
- assessment_id: section-heading
  area: evidence
  topic: Exact heading in source citation
  outcome: concern
  target_ids:
  - AIMech:ANDORAbstractionSampling
  evidence_ids:
  - record
  - paper
  summary: Correct the heading while preserving its correct number and pages.
  details: The reported-evaluation-scope locator calls Section4 Experimental Evaluation,
    while the actual heading on PDFp6 / printedp4271 is Empirical Evaluation. The
    section number, page range and substantive claim are correct; the citation should
    use the source heading accurately.
findings:
- finding_id: F1
  issue_key: aoas-empirical-evaluation-section-heading
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the evaluation section heading in the AOAS citation
  description: The reported-evaluation-scope locator calls Section4 Experimental Evaluation,
    while the actual heading on PDFp6 / printedp4271 is Empirical Evaluation. The
    section number, page range and substantive claim are correct; the citation should
    use the source heading accurately.
  target_ids:
  - AIMech:ANDORAbstractionSampling
  field_paths:
  - claims[reported-evaluation-scope].evidence[0].locator
  evidence_ids:
  - record
  - paper
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ANDORAbstractionSampling.yaml
    role: maintained
actions:
- action_id: A1
  description: Correct the maintained locator and report mirror, append edit history,
    regenerate the page, and save a linked successor review.
  finding_ids:
  - F1
  target_ids:
  - AIMech:ANDORAbstractionSampling
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ANDORAbstractionSampling.yaml
    role: maintained
  acceptance_checks:
  - The locator names Section4 Empirical Evaluation with the existing correct page
    range.
  - Record/report mirror and rendered page agree.
  - Corrected-input publication gates and linked successor review pass.
limitations:
- Partial author self-review; this minor wording correction does not change scientific
  scope. DRAFT remains.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- citation-provenance
```
