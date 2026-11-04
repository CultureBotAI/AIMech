# Cycle 1 Stage 4 Category Review of First-Native-Cohort and Curated Provenance/Mapping Targets (38 Maintained AIMech Concepts)

- Review: 20261104T112600Z-c1s4-curated-provenance-mapping-review
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-11-04T11:06:00Z
- Finished UTC: 2026-11-04T11:26:00Z
- Reviewer: Antigravity (AIMech C1S4 record_review agent) (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full-coverage scientific category review of 38 maintained CuratedAIConcept records at frozen source revision 7ad7d92709e8816ab33bc8979d7187dec109a1ab: the 33 classic AI concepts from the 2026-10-11T03:01:34Z first native cohort that previously had only deterministic validation review coverage, plus 5 additional curated records (AIMech:BarlowTwins, AIMech:VICReg, AIMech:CLARANSClustering, AIMech:LargeMarginNearestNeighbor, AIMech:RelevantComponentAnalysis) surfaced by whole-corpus provenance and identity-note hygiene diagnostics across all 1,487 curated records. All 38 concepts have distinct AI method identities and valid primary mechanism claims and are retained. Three actionable minor findings covering 14 records are persisted as open for Stage 5 (resolve_review_findings): F-C1S4-001 (missing PDF sha256/pdf_reading, #page= URL fragments, and missing DOI on ExpectationMaximization, MarkovDecisionProcess, PartiallyObservableMarkovDecisionProcess), F-C1S4-002 (missing sha256 digests on 7 documentation sources across Apriori, Eclat, GeneticAlgorithm, HiddenMarkovModel, BarlowTwins, VICReg), and F-C1S4-003 (undifferentiated multi-target aio_mappings rationales in GloVe, candidate-proposal phrasing in MarkovRandomField, and batch-discovery diary text in CLARANSClustering, LargeMarginNearestNeighbor, and RelevantComponentAnalysis).

## Scope And Provenance

38 maintained CuratedAIConcept records under data/curated/*.yaml comprising the 33 classic concepts from 20261011T030803Z-first-native-cohort.json and 5 curated records flagged by whole-corpus provenance/mapping diagnostics.

Selection: All 33 first-native-cohort records lacking a prior scientific_review=true entry plus all curated records flagged by whole-corpus source-sha256 and identity_notes/aio_mappings hygiene checks.
Coverage: full; 38 reviewed / 38 in the declared population.
Source: working_tree at Git base 7ad7d92709e8816ab33bc8979d7187dec109a1ab.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AdaBoost | data/curated/AdaBoost.yaml | maintained | AdaBoost |
| AIMech:Apriori | data/curated/Apriori.yaml | maintained | Apriori |
| AIMech:BIRCH | data/curated/BIRCH.yaml | maintained | BIRCH |
| AIMech:Bagging | data/curated/Bagging.yaml | maintained | Bagging |
| AIMech:BarlowTwins | data/curated/BarlowTwins.yaml | maintained | Barlow Twins |
| AIMech:Boosting | data/curated/Boosting.yaml | maintained | Boosting |
| AIMech:C45 | data/curated/C45.yaml | maintained | C4.5 |
| AIMech:CART | data/curated/CART.yaml | maintained | CART |
| AIMech:CLARANSClustering | data/curated/CLARANSClustering.yaml | maintained | CLARANS clustering |
| AIMech:DBSCAN | data/curated/DBSCAN.yaml | maintained | DBSCAN |
| AIMech:Eclat | data/curated/Eclat.yaml | maintained | Eclat |
| AIMech:ElasticNet | data/curated/ElasticNet.yaml | maintained | Elastic net |
| AIMech:ExpectationMaximization | data/curated/ExpectationMaximization.yaml | maintained | Expectation maximization |
| AIMech:GaussianProcessRegression | data/curated/GaussianProcessRegression.yaml | maintained | Gaussian process regression |
| AIMech:GeneticAlgorithm | data/curated/GeneticAlgorithm.yaml | maintained | Genetic algorithm |
| AIMech:GloVe | data/curated/GloVe.yaml | maintained | GloVe |
| AIMech:GradientBoosting | data/curated/GradientBoosting.yaml | maintained | Gradient boosting machine |
| AIMech:HDBSCAN | data/curated/HDBSCAN.yaml | maintained | HDBSCAN |
| AIMech:HiddenMarkovModel | data/curated/HiddenMarkovModel.yaml | maintained | Hidden Markov model |
| AIMech:ID3 | data/curated/ID3.yaml | maintained | ID3 |
| AIMech:KMeans | data/curated/KMeans.yaml | maintained | k-means |
| AIMech:LargeMarginNearestNeighbor | data/curated/LargeMarginNearestNeighbor.yaml | maintained | Large margin nearest neighbor |
| AIMech:LeastAngleRegression | data/curated/LeastAngleRegression.yaml | maintained | Least-angle regression |
| AIMech:LinearDiscriminantAnalysis | data/curated/LinearDiscriminantAnalysis.yaml | maintained | Linear discriminant analysis |
| AIMech:LoRA | data/curated/LoRA.yaml | maintained | Low-rank adaptation |
| AIMech:MarkovDecisionProcess | data/curated/MarkovDecisionProcess.yaml | maintained | Markov decision process |
| AIMech:MarkovRandomField | data/curated/MarkovRandomField.yaml | maintained | Markov random field |
| AIMech:MeanShift | data/curated/MeanShift.yaml | maintained | Mean shift |
| AIMech:NaiveBayes | data/curated/NaiveBayes.yaml | maintained | Naive Bayes |
| AIMech:OPTICS | data/curated/OPTICS.yaml | maintained | OPTICS |
| AIMech:PartialLeastSquaresRegression | data/curated/PartialLeastSquaresRegression.yaml | maintained | Partial least squares regression |
| AIMech:PartiallyObservableMarkovDecisionProcess | data/curated/PartiallyObservableMarkovDecisionProcess.yaml | maintained | Partially observable Markov decision process |
| AIMech:QuadraticDiscriminantAnalysis | data/curated/QuadraticDiscriminantAnalysis.yaml | maintained | Quadratic discriminant analysis |
| AIMech:RelevantComponentAnalysis | data/curated/RelevantComponentAnalysis.yaml | maintained | Relevant component analysis |
| AIMech:Stacking | data/curated/Stacking.yaml | maintained | Stacking |
| AIMech:StochasticGradientDescent | data/curated/StochasticGradientDescent.yaml | maintained | Stochastic gradient descent |
| AIMech:VICReg | data/curated/VICReg.yaml | maintained | VICReg |
| AIMech:VotingClassifier | data/curated/VotingClassifier.yaml | maintained | Voting classifier |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema, semantic validator, and frozen-inventory provenance/mapping audit | passed | True | AIMech:AdaBoost, AIMech:Apriori, AIMech:BIRCH, AIMech:Bagging, AIMech:BarlowTwins, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:CLARANSClustering, AIMech:DBSCAN, AIMech:Eclat, AIMech:ElasticNet, AIMech:ExpectationMaximization, AIMech:GaussianProcessRegression, AIMech:GeneticAlgorithm, AIMech:GloVe, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:HiddenMarkovModel, AIMech:ID3, AIMech:KMeans, AIMech:LargeMarginNearestNeighbor, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:MarkovDecisionProcess, AIMech:MarkovRandomField, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:QuadraticDiscriminantAnalysis, AIMech:RelevantComponentAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VICReg, AIMech:VotingClassifier | Verified all 38 maintained records against src/aimech/schema/curated_concept.yaml and executed whole-corpus provenance and mapping diagnostics in research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.py. |

## Scientific And Domain Assessments

### Concept identity, boundary distinctness, and primary claim support across all 38 curated targets

identity: supported. Targets: AIMech:AdaBoost, AIMech:Apriori, AIMech:BIRCH, AIMech:Bagging, AIMech:BarlowTwins, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:CLARANSClustering, AIMech:DBSCAN, AIMech:Eclat, AIMech:ElasticNet, AIMech:ExpectationMaximization, AIMech:GaussianProcessRegression, AIMech:GeneticAlgorithm, AIMech:GloVe, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:HiddenMarkovModel, AIMech:ID3, AIMech:KMeans, AIMech:LargeMarginNearestNeighbor, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:MarkovDecisionProcess, AIMech:MarkovRandomField, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:QuadraticDiscriminantAnalysis, AIMech:RelevantComponentAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VICReg, AIMech:VotingClassifier.

All 38 maintained CuratedAIConcept records denote distinct AI algorithms, models, objectives, or representations absent from pinned AIO 2026-07-22 and ground their definitions and mechanism claims in primary publications or versioned implementation documentation.

### Source content digest and locator completeness on 29 of 38 curated targets

provenance: supported. Targets: AIMech:AdaBoost, AIMech:BIRCH, AIMech:Bagging, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:CLARANSClustering, AIMech:DBSCAN, AIMech:ElasticNet, AIMech:GaussianProcessRegression, AIMech:GloVe, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:ID3, AIMech:KMeans, AIMech:LargeMarginNearestNeighbor, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:MarkovRandomField, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:QuadraticDiscriminantAnalysis, AIMech:RelevantComponentAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VotingClassifier.

29 of the 38 reviewed curated records include complete sha256 content digests, version identifiers, and exact section/line locators on all evidence_sources entries.

### Missing sha256 content digests, #page= URL fragments, and missing DOI on 9 curated targets

provenance: concern. Targets: AIMech:Apriori, AIMech:BarlowTwins, AIMech:Eclat, AIMech:ExpectationMaximization, AIMech:GeneticAlgorithm, AIMech:HiddenMarkovModel, AIMech:MarkovDecisionProcess, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:VICReg.

3 full_text PDF records (ExpectationMaximization, MarkovDecisionProcess, PartiallyObservableMarkovDecisionProcess) omit evidence_sources[0].sha256 and pdf_reading records, embed #page= viewer fragments in url, and omit doi:10.1016/S0004-3702(98)00023-X on MDP/POMDP; 6 records (Apriori, Eclat, GeneticAlgorithm, HiddenMarkovModel, BarlowTwins, VICReg) omit sha256 on 7 access_level=documentation sources.

### Target-specific AIO mapping rationales and clean identity_notes on 33 of 38 curated targets

grounding: supported. Targets: AIMech:AdaBoost, AIMech:Apriori, AIMech:BIRCH, AIMech:Bagging, AIMech:BarlowTwins, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:DBSCAN, AIMech:Eclat, AIMech:ElasticNet, AIMech:ExpectationMaximization, AIMech:GaussianProcessRegression, AIMech:GeneticAlgorithm, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:HiddenMarkovModel, AIMech:ID3, AIMech:KMeans, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:MarkovDecisionProcess, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:QuadraticDiscriminantAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VICReg, AIMech:VotingClassifier.

33 of the 38 reviewed curated records state target-specific AIO mapping rationales and concise concept-boundary identity_notes free of proposal or discovery-diary boilerplate.

### Undifferentiated multi-mapping rationales in GloVe and proposal/discovery-diary carryover in MarkovRandomField, CLARANSClustering, LargeMarginNearestNeighbor, and RelevantComponentAnalysis

grounding: concern. Targets: AIMech:CLARANSClustering, AIMech:GloVe, AIMech:LargeMarginNearestNeighbor, AIMech:MarkovRandomField, AIMech:RelevantComponentAnalysis.

AIMech:GloVe repeats one undifferentiated identity_notes string across all 3 aio_mappings[].rationale targets; AIMech:MarkovRandomField retains 'this candidate specifically uses an undirected graph' in identity_notes and aio_mappings[0].rationale; and AIMech:CLARANSClustering, AIMech:LargeMarginNearestNeighbor, and AIMech:RelevantComponentAnalysis retain batch-discovery process diary sentences ('No normalized identity match for this candidate was found... 79 worktree and 79 main-checkout matching lines; these concern BIRCH...') in identity_notes.

## Findings

### F-C1S4-001: Record PDF content digests, canonical URLs, and DOI metadata for the three full-text PDF concepts in the first native cohort

minor / open / confirmed; issue key: aimech-first-native-cohort-pdf-provenance.

Three maintained records from the 2026-10-11T03:01:34Z first native cohort (AIMech:ExpectationMaximization, AIMech:MarkovDecisionProcess, AIMech:PartiallyObservableMarkovDecisionProcess) cite PDF primary sources with access_level=full_text (Bilmes 1998 TR-97-021 and Kaelbling, Littman &amp; Cassandra 1998 Artificial Intelligence 101:99-134) while omitting evidence_sources[0].sha256 and pdf_reading entries in research/discovery/20261011T030803Z-first-native-cohort.json, embedding single-page #page= viewer fragment anchors in evidence_sources[0].url (even where the locator spans multiple pages), and omitting persistent_id (doi:10.1016/S0004-3702(98)00023-X) on MarkovDecisionProcess.yaml and PartiallyObservableMarkovDecisionProcess.yaml.

### F-C1S4-002: Populate or explicitly qualify missing sha256 content digests on seven curated documentation evidence sources across six maintained records

minor / open / confirmed; issue key: aimech-curated-documentation-missing-sha256.

Six maintained curated records (AIMech:Apriori, AIMech:Eclat, AIMech:GeneticAlgorithm, AIMech:HiddenMarkovModel, AIMech:BarlowTwins, AIMech:VICReg; seven documentation source entries total) are the only curated records whose access_level=documentation evidence_sources omit sha256 content digests (borgelt.net/apriori.html, borgelt.net/eclat.html, deap.readthedocs.io/en/stable/api/algo.html#deap.algorithms.eaSimple, hmmlearn.readthedocs.io/en/0.3.3/tutorial.html, and the secondary PyTorch 2.14 documentation entries in BarlowTwins.yaml and VICReg.yaml).

### F-C1S4-003: Differentiate target-specific AIO mapping rationales in GloVe.yaml and remove candidate-proposal / batch-discovery diary text from MarkovRandomField, CLARANSClustering, LargeMarginNearestNeighbor, and RelevantComponentAnalysis

minor / open / confirmed; issue key: aimech-curated-identity-mapping-proposal-diary-carryover.

AIMech:GloVe (data/curated/GloVe.yaml) is the only multi-mapping record in data/curated/*.yaml that repeats one undifferentiated identity_notes sentence verbatim across all three distinct aio_mappings[].rationale targets (AIO:RepresentationLearning, AIO:word2vecCBOW, AIO:word2vecSkipGram); AIMech:MarkovRandomField (data/curated/MarkovRandomField.yaml) retains candidate-proposal phrasing ('this candidate specifically uses an undirected graph') in identity_notes and aio_mappings[0].rationale; and AIMech:CLARANSClustering, AIMech:LargeMarginNearestNeighbor, and AIMech:RelevantComponentAnalysis retain batch-discovery diary text ('No normalized identity match for this candidate was found across all 442 pinned AIO labels/scoped synonyms and 227 preceding native IDs/names/aliases. The same search identified BIRCH as an existing native record... with 79 worktree and 79 main-checkout matching lines...') inside identity_notes.

## Recommended Actions And Acceptance Checks

### A-C1S4-001

In Stage 5 (resolve_review_findings), inspect the primary PDFs for ExpectationMaximization (Bilmes 1998 TR-97-021) and MarkovDecisionProcess/PartiallyObservableMarkovDecisionProcess (Kaelbling et al. 1998 AIJ 101:99-134), record sha256 digests, canonicalize evidence_sources[0].url without #page= fragments, add persistent_id doi:10.1016/S0004-3702(98)00023-X on MDP and POMDP, and record history sidecars via just new-history.

- python -m aimech validate
- python scripts/record_review.py check --require-reviews --base main

### A-C1S4-002

In Stage 5 (resolve_review_findings), verify and populate sha256 content digests (or record explicit versioned snapshot provenance) for the 7 access_level=documentation sources in Apriori.yaml, Eclat.yaml, GeneticAlgorithm.yaml, HiddenMarkovModel.yaml, BarlowTwins.yaml, and VICReg.yaml with append-only history sidecars.

- python -m aimech validate
- python scripts/record_review.py check --require-reviews --base main

### A-C1S4-003

In Stage 5 (resolve_review_findings), write target-specific aio_mappings[].rationale statements in GloVe.yaml, replace 'this candidate specifically uses an undirected graph' in MarkovRandomField.yaml, remove the batch-discovery diary tail from identity_notes in CLARANSClustering.yaml, LargeMarginNearestNeighbor.yaml, and RelevantComponentAnalysis.yaml, and record history sidecars.

- python -m aimech validate
- python scripts/record_review.py check --require-reviews --base main

## Category Boundaries

- retain: AIMech:AdaBoost, AIMech:Apriori, AIMech:BIRCH, AIMech:Bagging, AIMech:BarlowTwins, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:CLARANSClustering, AIMech:DBSCAN, AIMech:Eclat, AIMech:ElasticNet, AIMech:ExpectationMaximization, AIMech:GaussianProcessRegression, AIMech:GeneticAlgorithm, AIMech:GloVe, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:HiddenMarkovModel, AIMech:ID3, AIMech:KMeans, AIMech:LargeMarginNearestNeighbor, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:MarkovDecisionProcess, AIMech:MarkovRandomField, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:QuadraticDiscriminantAnalysis, AIMech:RelevantComponentAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VICReg, AIMech:VotingClassifier. All 38 maintained CuratedAIConcept records represent distinct AI methods, models, objectives, or representations absent from pinned AIO release 2026-07-22; open findings F-C1S4-001..F-C1S4-003 concern source digest provenance and mapping/identity-note wording rather than concept-boundary duplication.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E-CURATED-SCHEMA | src/aimech/schema/curated_concept.yaml; CuratedAIConcept, EvidenceSource, AIOMapping, and ConceptClaim classes | supports | Native LinkML schema governing maintained AIMech concepts, evidence sources, AIO mapping assessments, and curation metadata. |
| E-FIRST-COHORT-DISCOVERY | research/discovery/20261011T030803Z-first-native-cohort.json; records[0..35] and pdf_reading[0..3] | partial | Discovery artifact for the 36-record first native cohort showing that pdf_reading entries were recorded only for the 4 modern PDFs (DPO, FlashAttention, LoRA, Mamba) and omitted for Bilmes 1998 (EM) and Kaelbling et al. 1998 (MDP, POMDP). |
| E-C1S4-AUDIT | research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.json; diagnostic_probes and findings F-C1S4-001..F-C1S4-003 | supports | Whole-corpus Stage 4 audit identifying all curated full_text and documentation sources without sha256 digests, undifferentiated multi-mapping rationales, and candidate/discovery-diary phrasing in identity_notes. |

## Limits And Additional Notes

- Per Stage 4 (record_review) non-mutation policy, curated YAML records are not edited in this stage; open findings F-C1S4-001, F-C1S4-002, and F-C1S4-003 are carried forward to Stage 5 (resolve_review_findings).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T112600Z-c1s4-curated-provenance-mapping-review
kind: category
repository: CultureBotAI/AIMech
title: Cycle 1 Stage 4 Category Review of First-Native-Cohort and Curated Provenance/Mapping
  Targets (38 Maintained AIMech Concepts)
started_at: '2026-11-04T11:06:00Z'
finished_at: '2026-11-04T11:26:00Z'
reviewer:
  identity: Antigravity (AIMech C1S4 record_review agent)
  kind: agent
  model: Claude Opus 4.6
  independence: self_review
  independence_basis: Repository-local Stage 4 (record_review) frozen-inventory category
    audit prior to independent adversarial PR review.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: retain_38_needs_curation_14
scientific_review: true
summary: 'Full-coverage scientific category review of 38 maintained CuratedAIConcept
  records at frozen source revision 7ad7d92709e8816ab33bc8979d7187dec109a1ab: the
  33 classic AI concepts from the 2026-10-11T03:01:34Z first native cohort that previously
  had only deterministic validation review coverage, plus 5 additional curated records
  (AIMech:BarlowTwins, AIMech:VICReg, AIMech:CLARANSClustering, AIMech:LargeMarginNearestNeighbor,
  AIMech:RelevantComponentAnalysis) surfaced by whole-corpus provenance and identity-note
  hygiene diagnostics across all 1,487 curated records. All 38 concepts have distinct
  AI method identities and valid primary mechanism claims and are retained. Three
  actionable minor findings covering 14 records are persisted as open for Stage 5
  (resolve_review_findings): F-C1S4-001 (missing PDF sha256/pdf_reading, #page= URL
  fragments, and missing DOI on ExpectationMaximization, MarkovDecisionProcess, PartiallyObservableMarkovDecisionProcess),
  F-C1S4-002 (missing sha256 digests on 7 documentation sources across Apriori, Eclat,
  GeneticAlgorithm, HiddenMarkovModel, BarlowTwins, VICReg), and F-C1S4-003 (undifferentiated
  multi-target aio_mappings rationales in GloVe, candidate-proposal phrasing in MarkovRandomField,
  and batch-discovery diary text in CLARANSClustering, LargeMarginNearestNeighbor,
  and RelevantComponentAnalysis).'
source:
  git_revision: 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  state: working_tree
  snapshot_id: aio-2026-07-22@397851c547d1c4d8f06ef184f63c1d40bc86937a
  inputs:
  - path: data/curated/AdaBoost.yaml
    sha256: 3a638260e1acaae439b1daaee4ce515cd7420df5fafa2f34a3df03ce14120105
    role: target
  - path: data/curated/Apriori.yaml
    sha256: ecdb6f7857fe97ae313e2e6c95984852213e1647bc4b4ab81a30e81a989c71a6
    role: target
  - path: data/curated/BIRCH.yaml
    sha256: c1baee35bb4c6352d9060c5594cd62cb41100dbc929a8d58fa836928d1d70d83
    role: target
  - path: data/curated/Bagging.yaml
    sha256: c7860fed789012e17dd1f696a44dbc71be12fe393fa1dec96a3245940ec86d81
    role: target
  - path: data/curated/BarlowTwins.yaml
    sha256: d94a944d2e8e50185b7171f5461e515708eced1b732bac61b1e420f6a367643a
    role: target
  - path: data/curated/Boosting.yaml
    sha256: eedf8d5bf384aa6fc25f823b4fe9847b8b9d26fa0d850acdf2b435296e17a3e0
    role: target
  - path: data/curated/C45.yaml
    sha256: b58efdbb4ec07063fd6e5fd3d0baab4686259af6016c4d718aa82152d3726fbc
    role: target
  - path: data/curated/CART.yaml
    sha256: 7c462535877d208fb47c6e418f7c9bdd0305b51cada89db1388fad19845f0178
    role: target
  - path: data/curated/CLARANSClustering.yaml
    sha256: 79f58a8839bf69a36304f21e1eb5ec94fb0ae829a08839a0f4e3d7de74428e16
    role: target
  - path: data/curated/DBSCAN.yaml
    sha256: de7d744d1f7761af64ce963cf5759853d70a586b4188eea757751357e5035f44
    role: target
  - path: data/curated/Eclat.yaml
    sha256: 9e293cd6daaa774fde31780d488b42194477c9f4284857697a74f2d34ce46aac
    role: target
  - path: data/curated/ElasticNet.yaml
    sha256: b441d7068b074ed4e86fb51f24130cb3a9fb1eaff86e4fc318e619c21699ce6c
    role: target
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: target
  - path: data/curated/GaussianProcessRegression.yaml
    sha256: d83d0de4a152e7db689636928f41eb5d3663281285585d835f2a5535403d6a0d
    role: target
  - path: data/curated/GeneticAlgorithm.yaml
    sha256: d40bf1a03e29a3ca6bf88f6553f18c6b1559baf56da6a21d63b54163f4752ceb
    role: target
  - path: data/curated/GloVe.yaml
    sha256: 4a37b142c697215fe20f195a762e8dfbae2727b945c14732b9de8d0a2dfbfd92
    role: target
  - path: data/curated/GradientBoosting.yaml
    sha256: 2e89ee7d292a071d6d4b8aecf81cd57cae84a50a2d167cc69ffee2cebf4dffe5
    role: target
  - path: data/curated/HDBSCAN.yaml
    sha256: 46232d726b6e52f2373481fe18f52e3c9721aee83700311012ad07e3cc2704f3
    role: target
  - path: data/curated/HiddenMarkovModel.yaml
    sha256: 062a31bd525cb90e8077d4889c177f55cb7b29dea4e71c33be95bae9e72a5240
    role: target
  - path: data/curated/ID3.yaml
    sha256: 5d0bbbe3eff68ad1b163c763d7b73ea7aa9535851096c5be4ec32b9dc34eab01
    role: target
  - path: data/curated/KMeans.yaml
    sha256: 50fc1d8d18403a8f314636f68b6812ffd15fec2dfaaf4c32aaad423dfa7ffa03
    role: target
  - path: data/curated/LargeMarginNearestNeighbor.yaml
    sha256: f17ce62722a0b1aaf9629bbb196e67249c1853edd31d220bfff76019d3e3295e
    role: target
  - path: data/curated/LeastAngleRegression.yaml
    sha256: 379431bca38c3bbac6653617a424e692fba98edc1cf7f8d25b388328e5fe7ab5
    role: target
  - path: data/curated/LinearDiscriminantAnalysis.yaml
    sha256: cb194468de3c200a57f1d6338e13b604775ce8a10b5517966459242410752b6a
    role: target
  - path: data/curated/LoRA.yaml
    sha256: 8642959e7dd4ca6630720e78771b6e7b825336c967f0663f125c1a23aee7ae49
    role: target
  - path: data/curated/MarkovDecisionProcess.yaml
    sha256: 9db1ed4a4b01f70cffafe2bcabe7be214779adacf4d7b31c9348ed5f9f54b907
    role: target
  - path: data/curated/MarkovRandomField.yaml
    sha256: 03b1f2a66b2183a5bf5943bee7ec0619b9e07947d6c9187263e279ee475f9149
    role: target
  - path: data/curated/MeanShift.yaml
    sha256: 3e6868e9d4786ef56fc10af3e1b9e8fd8a3cd15fa8e63d058ba99a3d9567448a
    role: target
  - path: data/curated/NaiveBayes.yaml
    sha256: 99caf757d49a76920b59c60591beeaf1f019ec0d1acb7ae5944ea0f5f7339b61
    role: target
  - path: data/curated/OPTICS.yaml
    sha256: 538df2beab3517c798e773114cdaa01889642464b896623dd978cd02e3cc536a
    role: target
  - path: data/curated/PartialLeastSquaresRegression.yaml
    sha256: 3d34b3313b0580f1aa7316f588cc38589056e8b58711d1944b346f8a0c394ea4
    role: target
  - path: data/curated/PartiallyObservableMarkovDecisionProcess.yaml
    sha256: 2930142265ec082e972e8ccd05cff84685d611596a58af2af39c4f7b80a16577
    role: target
  - path: data/curated/QuadraticDiscriminantAnalysis.yaml
    sha256: 31a1b7c08a1bae221d571e26441b4690456524b409a33df84427ff929cb4dd3e
    role: target
  - path: data/curated/RelevantComponentAnalysis.yaml
    sha256: b90fe3dd50da413f6f66c6ea26ecd2eb937b2aec43b4c1eb1f4635dc4609094f
    role: target
  - path: data/curated/Stacking.yaml
    sha256: 5271ce4094a5beec8dc87500e64d9c779ec4aec9bbcb20d0efcc22d26e62706b
    role: target
  - path: data/curated/StochasticGradientDescent.yaml
    sha256: 5c57fc809ae8667d5be8cda421cc9f0bd1f0c668f64ba3d7b23d788528b46e97
    role: target
  - path: data/curated/VICReg.yaml
    sha256: c04e41d11984e1be0efaf723b1cccc4bef0f0712acdd28f6004cf9287bf276af
    role: target
  - path: data/curated/VotingClassifier.yaml
    sha256: 648ff71f5b9e964aea0fcab2e0430be345884c9c98c8250f76e1ad9a396903cf
    role: target
  - path: docs/curated-concepts.md
    sha256: 79c497b615b9ba703d67ccfc1a925f5d5c3c527aff6ab323cd271aec8e5a40dc
    role: context
  - path: docs/record-review-profile.md
    sha256: 2d3e3a73264523c78930d17b0812e2d22887e25423fe7c38e0ddce922d9cec9d
    role: context
  - path: research/discovery/20261011T030803Z-first-native-cohort.json
    sha256: 5b4c66fe530b2cad8a9c8cafef989a0b34c4ebb78ad790511013787c4a3a9225
    role: context
  - path: research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.json
    sha256: 01b0f4973c4bad5333d1ae3e6d7ae326711b7ac2c72ea0c39486e223a8434666
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: 3826f6a7643d6a0140cf60bb52a1d3ac2fbab4811b4fd8d1d178a13c3341fa3f
    role: context
scope:
  description: 38 maintained CuratedAIConcept records under data/curated/*.yaml comprising
    the 33 classic concepts from 20261011T030803Z-first-native-cohort.json and 5 curated
    records flagged by whole-corpus provenance/mapping diagnostics.
  selection: All 33 first-native-cohort records lacking a prior scientific_review=true
    entry plus all curated records flagged by whole-corpus source-sha256 and identity_notes/aio_mappings
    hygiene checks.
  coverage: full
  population_size: 38
  reviewed_target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:BarlowTwins
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:CLARANSClustering
  - AIMech:DBSCAN
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LargeMarginNearestNeighbor
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:RelevantComponentAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VICReg
  - AIMech:VotingClassifier
targets:
- target_id: AIMech:AdaBoost
  path: data/curated/AdaBoost.yaml
  label: AdaBoost
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 3a638260e1acaae439b1daaee4ce515cd7420df5fafa2f34a3df03ce14120105
    description: Exact file SHA-256 digest of data/curated/AdaBoost.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AdaBoost.yaml
    role: maintained_record
- target_id: AIMech:Apriori
  path: data/curated/Apriori.yaml
  label: Apriori
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: ecdb6f7857fe97ae313e2e6c95984852213e1647bc4b4ab81a30e81a989c71a6
    description: Exact file SHA-256 digest of data/curated/Apriori.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Apriori.yaml
    role: maintained_record
- target_id: AIMech:BIRCH
  path: data/curated/BIRCH.yaml
  label: BIRCH
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: c1baee35bb4c6352d9060c5594cd62cb41100dbc929a8d58fa836928d1d70d83
    description: Exact file SHA-256 digest of data/curated/BIRCH.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BIRCH.yaml
    role: maintained_record
- target_id: AIMech:Bagging
  path: data/curated/Bagging.yaml
  label: Bagging
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: c7860fed789012e17dd1f696a44dbc71be12fe393fa1dec96a3245940ec86d81
    description: Exact file SHA-256 digest of data/curated/Bagging.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Bagging.yaml
    role: maintained_record
- target_id: AIMech:BarlowTwins
  path: data/curated/BarlowTwins.yaml
  label: Barlow Twins
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: d94a944d2e8e50185b7171f5461e515708eced1b732bac61b1e420f6a367643a
    description: Exact file SHA-256 digest of data/curated/BarlowTwins.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BarlowTwins.yaml
    role: maintained_record
- target_id: AIMech:Boosting
  path: data/curated/Boosting.yaml
  label: Boosting
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: eedf8d5bf384aa6fc25f823b4fe9847b8b9d26fa0d850acdf2b435296e17a3e0
    description: Exact file SHA-256 digest of data/curated/Boosting.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Boosting.yaml
    role: maintained_record
- target_id: AIMech:C45
  path: data/curated/C45.yaml
  label: C4.5
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b58efdbb4ec07063fd6e5fd3d0baab4686259af6016c4d718aa82152d3726fbc
    description: Exact file SHA-256 digest of data/curated/C45.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/C45.yaml
    role: maintained_record
- target_id: AIMech:CART
  path: data/curated/CART.yaml
  label: CART
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7c462535877d208fb47c6e418f7c9bdd0305b51cada89db1388fad19845f0178
    description: Exact file SHA-256 digest of data/curated/CART.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CART.yaml
    role: maintained_record
- target_id: AIMech:CLARANSClustering
  path: data/curated/CLARANSClustering.yaml
  label: CLARANS clustering
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 79f58a8839bf69a36304f21e1eb5ec94fb0ae829a08839a0f4e3d7de74428e16
    description: Exact file SHA-256 digest of data/curated/CLARANSClustering.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CLARANSClustering.yaml
    role: maintained_record
- target_id: AIMech:DBSCAN
  path: data/curated/DBSCAN.yaml
  label: DBSCAN
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: de7d744d1f7761af64ce963cf5759853d70a586b4188eea757751357e5035f44
    description: Exact file SHA-256 digest of data/curated/DBSCAN.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DBSCAN.yaml
    role: maintained_record
- target_id: AIMech:Eclat
  path: data/curated/Eclat.yaml
  label: Eclat
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 9e293cd6daaa774fde31780d488b42194477c9f4284857697a74f2d34ce46aac
    description: Exact file SHA-256 digest of data/curated/Eclat.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Eclat.yaml
    role: maintained_record
- target_id: AIMech:ElasticNet
  path: data/curated/ElasticNet.yaml
  label: Elastic net
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b441d7068b074ed4e86fb51f24130cb3a9fb1eaff86e4fc318e619c21699ce6c
    description: Exact file SHA-256 digest of data/curated/ElasticNet.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ElasticNet.yaml
    role: maintained_record
- target_id: AIMech:ExpectationMaximization
  path: data/curated/ExpectationMaximization.yaml
  label: Expectation maximization
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    description: Exact file SHA-256 digest of data/curated/ExpectationMaximization.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ExpectationMaximization.yaml
    role: maintained_record
- target_id: AIMech:GaussianProcessRegression
  path: data/curated/GaussianProcessRegression.yaml
  label: Gaussian process regression
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: d83d0de4a152e7db689636928f41eb5d3663281285585d835f2a5535403d6a0d
    description: Exact file SHA-256 digest of data/curated/GaussianProcessRegression.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GaussianProcessRegression.yaml
    role: maintained_record
- target_id: AIMech:GeneticAlgorithm
  path: data/curated/GeneticAlgorithm.yaml
  label: Genetic algorithm
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: d40bf1a03e29a3ca6bf88f6553f18c6b1559baf56da6a21d63b54163f4752ceb
    description: Exact file SHA-256 digest of data/curated/GeneticAlgorithm.yaml at
      7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GeneticAlgorithm.yaml
    role: maintained_record
- target_id: AIMech:GloVe
  path: data/curated/GloVe.yaml
  label: GloVe
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 4a37b142c697215fe20f195a762e8dfbae2727b945c14732b9de8d0a2dfbfd92
    description: Exact file SHA-256 digest of data/curated/GloVe.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GloVe.yaml
    role: maintained_record
- target_id: AIMech:GradientBoosting
  path: data/curated/GradientBoosting.yaml
  label: Gradient boosting machine
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 2e89ee7d292a071d6d4b8aecf81cd57cae84a50a2d167cc69ffee2cebf4dffe5
    description: Exact file SHA-256 digest of data/curated/GradientBoosting.yaml at
      7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GradientBoosting.yaml
    role: maintained_record
- target_id: AIMech:HDBSCAN
  path: data/curated/HDBSCAN.yaml
  label: HDBSCAN
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 46232d726b6e52f2373481fe18f52e3c9721aee83700311012ad07e3cc2704f3
    description: Exact file SHA-256 digest of data/curated/HDBSCAN.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HDBSCAN.yaml
    role: maintained_record
- target_id: AIMech:HiddenMarkovModel
  path: data/curated/HiddenMarkovModel.yaml
  label: Hidden Markov model
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 062a31bd525cb90e8077d4889c177f55cb7b29dea4e71c33be95bae9e72a5240
    description: Exact file SHA-256 digest of data/curated/HiddenMarkovModel.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HiddenMarkovModel.yaml
    role: maintained_record
- target_id: AIMech:ID3
  path: data/curated/ID3.yaml
  label: ID3
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 5d0bbbe3eff68ad1b163c763d7b73ea7aa9535851096c5be4ec32b9dc34eab01
    description: Exact file SHA-256 digest of data/curated/ID3.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ID3.yaml
    role: maintained_record
- target_id: AIMech:KMeans
  path: data/curated/KMeans.yaml
  label: k-means
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 50fc1d8d18403a8f314636f68b6812ffd15fec2dfaaf4c32aaad423dfa7ffa03
    description: Exact file SHA-256 digest of data/curated/KMeans.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/KMeans.yaml
    role: maintained_record
- target_id: AIMech:LargeMarginNearestNeighbor
  path: data/curated/LargeMarginNearestNeighbor.yaml
  label: Large margin nearest neighbor
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: f17ce62722a0b1aaf9629bbb196e67249c1853edd31d220bfff76019d3e3295e
    description: Exact file SHA-256 digest of data/curated/LargeMarginNearestNeighbor.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LargeMarginNearestNeighbor.yaml
    role: maintained_record
- target_id: AIMech:LeastAngleRegression
  path: data/curated/LeastAngleRegression.yaml
  label: Least-angle regression
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 379431bca38c3bbac6653617a424e692fba98edc1cf7f8d25b388328e5fe7ab5
    description: Exact file SHA-256 digest of data/curated/LeastAngleRegression.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LeastAngleRegression.yaml
    role: maintained_record
- target_id: AIMech:LinearDiscriminantAnalysis
  path: data/curated/LinearDiscriminantAnalysis.yaml
  label: Linear discriminant analysis
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: cb194468de3c200a57f1d6338e13b604775ce8a10b5517966459242410752b6a
    description: Exact file SHA-256 digest of data/curated/LinearDiscriminantAnalysis.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LinearDiscriminantAnalysis.yaml
    role: maintained_record
- target_id: AIMech:LoRA
  path: data/curated/LoRA.yaml
  label: Low-rank adaptation
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 8642959e7dd4ca6630720e78771b6e7b825336c967f0663f125c1a23aee7ae49
    description: Exact file SHA-256 digest of data/curated/LoRA.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LoRA.yaml
    role: maintained_record
- target_id: AIMech:MarkovDecisionProcess
  path: data/curated/MarkovDecisionProcess.yaml
  label: Markov decision process
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 9db1ed4a4b01f70cffafe2bcabe7be214779adacf4d7b31c9348ed5f9f54b907
    description: Exact file SHA-256 digest of data/curated/MarkovDecisionProcess.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MarkovDecisionProcess.yaml
    role: maintained_record
- target_id: AIMech:MarkovRandomField
  path: data/curated/MarkovRandomField.yaml
  label: Markov random field
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 03b1f2a66b2183a5bf5943bee7ec0619b9e07947d6c9187263e279ee475f9149
    description: Exact file SHA-256 digest of data/curated/MarkovRandomField.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MarkovRandomField.yaml
    role: maintained_record
- target_id: AIMech:MeanShift
  path: data/curated/MeanShift.yaml
  label: Mean shift
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 3e6868e9d4786ef56fc10af3e1b9e8fd8a3cd15fa8e63d058ba99a3d9567448a
    description: Exact file SHA-256 digest of data/curated/MeanShift.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MeanShift.yaml
    role: maintained_record
- target_id: AIMech:NaiveBayes
  path: data/curated/NaiveBayes.yaml
  label: Naive Bayes
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 99caf757d49a76920b59c60591beeaf1f019ec0d1acb7ae5944ea0f5f7339b61
    description: Exact file SHA-256 digest of data/curated/NaiveBayes.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NaiveBayes.yaml
    role: maintained_record
- target_id: AIMech:OPTICS
  path: data/curated/OPTICS.yaml
  label: OPTICS
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 538df2beab3517c798e773114cdaa01889642464b896623dd978cd02e3cc536a
    description: Exact file SHA-256 digest of data/curated/OPTICS.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OPTICS.yaml
    role: maintained_record
- target_id: AIMech:PartialLeastSquaresRegression
  path: data/curated/PartialLeastSquaresRegression.yaml
  label: Partial least squares regression
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 3d34b3313b0580f1aa7316f588cc38589056e8b58711d1944b346f8a0c394ea4
    description: Exact file SHA-256 digest of data/curated/PartialLeastSquaresRegression.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PartialLeastSquaresRegression.yaml
    role: maintained_record
- target_id: AIMech:PartiallyObservableMarkovDecisionProcess
  path: data/curated/PartiallyObservableMarkovDecisionProcess.yaml
  label: Partially observable Markov decision process
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 2930142265ec082e972e8ccd05cff84685d611596a58af2af39c4f7b80a16577
    description: Exact file SHA-256 digest of data/curated/PartiallyObservableMarkovDecisionProcess.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PartiallyObservableMarkovDecisionProcess.yaml
    role: maintained_record
- target_id: AIMech:QuadraticDiscriminantAnalysis
  path: data/curated/QuadraticDiscriminantAnalysis.yaml
  label: Quadratic discriminant analysis
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 31a1b7c08a1bae221d571e26441b4690456524b409a33df84427ff929cb4dd3e
    description: Exact file SHA-256 digest of data/curated/QuadraticDiscriminantAnalysis.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/QuadraticDiscriminantAnalysis.yaml
    role: maintained_record
- target_id: AIMech:RelevantComponentAnalysis
  path: data/curated/RelevantComponentAnalysis.yaml
  label: Relevant component analysis
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b90fe3dd50da413f6f66c6ea26ecd2eb937b2aec43b4c1eb1f4635dc4609094f
    description: Exact file SHA-256 digest of data/curated/RelevantComponentAnalysis.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RelevantComponentAnalysis.yaml
    role: maintained_record
- target_id: AIMech:Stacking
  path: data/curated/Stacking.yaml
  label: Stacking
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 5271ce4094a5beec8dc87500e64d9c779ec4aec9bbcb20d0efcc22d26e62706b
    description: Exact file SHA-256 digest of data/curated/Stacking.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Stacking.yaml
    role: maintained_record
- target_id: AIMech:StochasticGradientDescent
  path: data/curated/StochasticGradientDescent.yaml
  label: Stochastic gradient descent
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 5c57fc809ae8667d5be8cda421cc9f0bd1f0c668f64ba3d7b23d788528b46e97
    description: Exact file SHA-256 digest of data/curated/StochasticGradientDescent.yaml
      at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StochasticGradientDescent.yaml
    role: maintained_record
- target_id: AIMech:VICReg
  path: data/curated/VICReg.yaml
  label: VICReg
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: c04e41d11984e1be0efaf723b1cccc4bef0f0712acdd28f6004cf9287bf276af
    description: Exact file SHA-256 digest of data/curated/VICReg.yaml at 7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/VICReg.yaml
    role: maintained_record
- target_id: AIMech:VotingClassifier
  path: data/curated/VotingClassifier.yaml
  label: Voting classifier
  record_class: CuratedAIConcept
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 648ff71f5b9e964aea0fcab2e0430be345884c9c98c8250f76e1ad9a396903cf
    description: Exact file SHA-256 digest of data/curated/VotingClassifier.yaml at
      7ad7d92709e8816ab33bc8979d7187dec109a1ab
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/VotingClassifier.yaml
    role: maintained_record
checks:
- check_id: CHK-CURATED-VALIDATE-AND-AUDIT
  name: LinkML schema, semantic validator, and frozen-inventory provenance/mapping
    audit
  status: passed
  required: true
  summary: Verified all 38 maintained records against src/aimech/schema/curated_concept.yaml
    and executed whole-corpus provenance and mapping diagnostics in research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.py.
  target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:BarlowTwins
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:CLARANSClustering
  - AIMech:DBSCAN
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LargeMarginNearestNeighbor
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:RelevantComponentAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VICReg
  - AIMech:VotingClassifier
  command: python -m aimech validate && python research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - E-CURATED-SCHEMA
  - E-FIRST-COHORT-DISCOVERY
  - E-C1S4-AUDIT
evidence:
- evidence_id: E-CURATED-SCHEMA
  kind: authority
  reference: src/aimech/schema/curated_concept.yaml
  locator: CuratedAIConcept, EvidenceSource, AIOMapping, and ConceptClaim classes
  accessed_at: '2026-11-04T11:08:00Z'
  support: supports
  summary: Native LinkML schema governing maintained AIMech concepts, evidence sources,
    AIO mapping assessments, and curation metadata.
  snapshot_sha256: 3826f6a7643d6a0140cf60bb52a1d3ac2fbab4811b4fd8d1d178a13c3341fa3f
- evidence_id: E-FIRST-COHORT-DISCOVERY
  kind: record_content
  reference: research/discovery/20261011T030803Z-first-native-cohort.json
  locator: records[0..35] and pdf_reading[0..3]
  accessed_at: '2026-11-04T11:10:00Z'
  support: partial
  summary: Discovery artifact for the 36-record first native cohort showing that pdf_reading
    entries were recorded only for the 4 modern PDFs (DPO, FlashAttention, LoRA, Mamba)
    and omitted for Bilmes 1998 (EM) and Kaelbling et al. 1998 (MDP, POMDP).
  snapshot_sha256: 5b4c66fe530b2cad8a9c8cafef989a0b34c4ebb78ad790511013787c4a3a9225
- evidence_id: E-C1S4-AUDIT
  kind: validation
  reference: research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.json
  locator: diagnostic_probes and findings F-C1S4-001..F-C1S4-003
  accessed_at: '2026-11-04T11:20:00Z'
  support: supports
  summary: Whole-corpus Stage 4 audit identifying all curated full_text and documentation
    sources without sha256 digests, undifferentiated multi-mapping rationales, and
    candidate/discovery-diary phrasing in identity_notes.
  snapshot_sha256: 01b0f4973c4bad5333d1ae3e6d7ae326711b7ac2c72ea0c39486e223a8434666
assessments:
- assessment_id: ASM-CURATED-IDENTITY-AND-CLAIMS
  area: identity
  topic: Concept identity, boundary distinctness, and primary claim support across
    all 38 curated targets
  outcome: supported
  summary: All 38 maintained CuratedAIConcept records denote distinct AI algorithms,
    models, objectives, or representations absent from pinned AIO 2026-07-22 and ground
    their definitions and mechanism claims in primary publications or versioned implementation
    documentation.
  target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:BarlowTwins
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:CLARANSClustering
  - AIMech:DBSCAN
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LargeMarginNearestNeighbor
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:RelevantComponentAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VICReg
  - AIMech:VotingClassifier
  evidence_ids:
  - E-CURATED-SCHEMA
  - E-C1S4-AUDIT
- assessment_id: ASM-CURATED-PROVENANCE-SUPPORTED
  area: provenance
  topic: Source content digest and locator completeness on 29 of 38 curated targets
  outcome: supported
  summary: 29 of the 38 reviewed curated records include complete sha256 content digests,
    version identifiers, and exact section/line locators on all evidence_sources entries.
  target_ids:
  - AIMech:AdaBoost
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:CLARANSClustering
  - AIMech:DBSCAN
  - AIMech:ElasticNet
  - AIMech:GaussianProcessRegression
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LargeMarginNearestNeighbor
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:RelevantComponentAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VotingClassifier
  evidence_ids:
  - E-CURATED-SCHEMA
  - E-C1S4-AUDIT
- assessment_id: ASM-CURATED-PROVENANCE-CONCERN
  area: provenance
  topic: 'Missing sha256 content digests, #page= URL fragments, and missing DOI on
    9 curated targets'
  outcome: concern
  summary: '3 full_text PDF records (ExpectationMaximization, MarkovDecisionProcess,
    PartiallyObservableMarkovDecisionProcess) omit evidence_sources[0].sha256 and
    pdf_reading records, embed #page= viewer fragments in url, and omit doi:10.1016/S0004-3702(98)00023-X
    on MDP/POMDP; 6 records (Apriori, Eclat, GeneticAlgorithm, HiddenMarkovModel,
    BarlowTwins, VICReg) omit sha256 on 7 access_level=documentation sources.'
  target_ids:
  - AIMech:Apriori
  - AIMech:BarlowTwins
  - AIMech:Eclat
  - AIMech:ExpectationMaximization
  - AIMech:GeneticAlgorithm
  - AIMech:HiddenMarkovModel
  - AIMech:MarkovDecisionProcess
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:VICReg
  evidence_ids:
  - E-FIRST-COHORT-DISCOVERY
  - E-C1S4-AUDIT
- assessment_id: ASM-CURATED-GROUNDING-SUPPORTED
  area: grounding
  topic: Target-specific AIO mapping rationales and clean identity_notes on 33 of
    38 curated targets
  outcome: supported
  summary: 33 of the 38 reviewed curated records state target-specific AIO mapping
    rationales and concise concept-boundary identity_notes free of proposal or discovery-diary
    boilerplate.
  target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:BarlowTwins
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:DBSCAN
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:MarkovDecisionProcess
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VICReg
  - AIMech:VotingClassifier
  evidence_ids:
  - E-CURATED-SCHEMA
  - E-C1S4-AUDIT
- assessment_id: ASM-CURATED-GROUNDING-CONCERN
  area: grounding
  topic: Undifferentiated multi-mapping rationales in GloVe and proposal/discovery-diary
    carryover in MarkovRandomField, CLARANSClustering, LargeMarginNearestNeighbor,
    and RelevantComponentAnalysis
  outcome: concern
  summary: AIMech:GloVe repeats one undifferentiated identity_notes string across
    all 3 aio_mappings[].rationale targets; AIMech:MarkovRandomField retains 'this
    candidate specifically uses an undirected graph' in identity_notes and aio_mappings[0].rationale;
    and AIMech:CLARANSClustering, AIMech:LargeMarginNearestNeighbor, and AIMech:RelevantComponentAnalysis
    retain batch-discovery process diary sentences ('No normalized identity match
    for this candidate was found... 79 worktree and 79 main-checkout matching lines;
    these concern BIRCH...') in identity_notes.
  target_ids:
  - AIMech:CLARANSClustering
  - AIMech:GloVe
  - AIMech:LargeMarginNearestNeighbor
  - AIMech:MarkovRandomField
  - AIMech:RelevantComponentAnalysis
  evidence_ids:
  - E-CURATED-SCHEMA
  - E-C1S4-AUDIT
findings:
- finding_id: F-C1S4-001
  issue_key: aimech-first-native-cohort-pdf-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Record PDF content digests, canonical URLs, and DOI metadata for the three
    full-text PDF concepts in the first native cohort
  description: 'Three maintained records from the 2026-10-11T03:01:34Z first native
    cohort (AIMech:ExpectationMaximization, AIMech:MarkovDecisionProcess, AIMech:PartiallyObservableMarkovDecisionProcess)
    cite PDF primary sources with access_level=full_text (Bilmes 1998 TR-97-021 and
    Kaelbling, Littman & Cassandra 1998 Artificial Intelligence 101:99-134) while
    omitting evidence_sources[0].sha256 and pdf_reading entries in research/discovery/20261011T030803Z-first-native-cohort.json,
    embedding single-page #page= viewer fragment anchors in evidence_sources[0].url
    (even where the locator spans multiple pages), and omitting persistent_id (doi:10.1016/S0004-3702(98)00023-X)
    on MarkovDecisionProcess.yaml and PartiallyObservableMarkovDecisionProcess.yaml.'
  target_ids:
  - AIMech:ExpectationMaximization
  - AIMech:MarkovDecisionProcess
  - AIMech:PartiallyObservableMarkovDecisionProcess
  field_paths:
  - evidence_sources[0].sha256
  - evidence_sources[0].url
  - evidence_sources[0].persistent_id
  evidence_ids:
  - E-FIRST-COHORT-DISCOVERY
  - E-C1S4-AUDIT
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ExpectationMaximization.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/MarkovDecisionProcess.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/PartiallyObservableMarkovDecisionProcess.yaml
    role: maintained_record
- finding_id: F-C1S4-002
  issue_key: aimech-curated-documentation-missing-sha256
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Populate or explicitly qualify missing sha256 content digests on seven curated
    documentation evidence sources across six maintained records
  description: Six maintained curated records (AIMech:Apriori, AIMech:Eclat, AIMech:GeneticAlgorithm,
    AIMech:HiddenMarkovModel, AIMech:BarlowTwins, AIMech:VICReg; seven documentation
    source entries total) are the only curated records whose access_level=documentation
    evidence_sources omit sha256 content digests (borgelt.net/apriori.html, borgelt.net/eclat.html,
    deap.readthedocs.io/en/stable/api/algo.html#deap.algorithms.eaSimple, hmmlearn.readthedocs.io/en/0.3.3/tutorial.html,
    and the secondary PyTorch 2.14 documentation entries in BarlowTwins.yaml and VICReg.yaml).
  target_ids:
  - AIMech:Apriori
  - AIMech:BarlowTwins
  - AIMech:Eclat
  - AIMech:GeneticAlgorithm
  - AIMech:HiddenMarkovModel
  - AIMech:VICReg
  field_paths:
  - evidence_sources[0].sha256
  - evidence_sources[1].sha256
  - evidence_sources[2].sha256
  evidence_ids:
  - E-CURATED-SCHEMA
  - E-C1S4-AUDIT
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Apriori.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/BarlowTwins.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/Eclat.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/GeneticAlgorithm.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/HiddenMarkovModel.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/VICReg.yaml
    role: maintained_record
- finding_id: F-C1S4-003
  issue_key: aimech-curated-identity-mapping-proposal-diary-carryover
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Differentiate target-specific AIO mapping rationales in GloVe.yaml and remove
    candidate-proposal / batch-discovery diary text from MarkovRandomField, CLARANSClustering,
    LargeMarginNearestNeighbor, and RelevantComponentAnalysis
  description: AIMech:GloVe (data/curated/GloVe.yaml) is the only multi-mapping record
    in data/curated/*.yaml that repeats one undifferentiated identity_notes sentence
    verbatim across all three distinct aio_mappings[].rationale targets (AIO:RepresentationLearning,
    AIO:word2vecCBOW, AIO:word2vecSkipGram); AIMech:MarkovRandomField (data/curated/MarkovRandomField.yaml)
    retains candidate-proposal phrasing ('this candidate specifically uses an undirected
    graph') in identity_notes and aio_mappings[0].rationale; and AIMech:CLARANSClustering,
    AIMech:LargeMarginNearestNeighbor, and AIMech:RelevantComponentAnalysis retain
    batch-discovery diary text ('No normalized identity match for this candidate was
    found across all 442 pinned AIO labels/scoped synonyms and 227 preceding native
    IDs/names/aliases. The same search identified BIRCH as an existing native record...
    with 79 worktree and 79 main-checkout matching lines...') inside identity_notes.
  target_ids:
  - AIMech:CLARANSClustering
  - AIMech:GloVe
  - AIMech:LargeMarginNearestNeighbor
  - AIMech:MarkovRandomField
  - AIMech:RelevantComponentAnalysis
  field_paths:
  - identity_notes
  - aio_mappings[0..2].rationale
  evidence_ids:
  - E-CURATED-SCHEMA
  - E-C1S4-AUDIT
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CLARANSClustering.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/GloVe.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/LargeMarginNearestNeighbor.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/MarkovRandomField.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/RelevantComponentAnalysis.yaml
    role: maintained_record
actions:
- action_id: A-C1S4-001
  description: 'In Stage 5 (resolve_review_findings), inspect the primary PDFs for
    ExpectationMaximization (Bilmes 1998 TR-97-021) and MarkovDecisionProcess/PartiallyObservableMarkovDecisionProcess
    (Kaelbling et al. 1998 AIJ 101:99-134), record sha256 digests, canonicalize evidence_sources[0].url
    without #page= fragments, add persistent_id doi:10.1016/S0004-3702(98)00023-X
    on MDP and POMDP, and record history sidecars via just new-history.'
  finding_ids:
  - F-C1S4-001
  target_ids:
  - AIMech:ExpectationMaximization
  - AIMech:MarkovDecisionProcess
  - AIMech:PartiallyObservableMarkovDecisionProcess
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ExpectationMaximization.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/MarkovDecisionProcess.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/PartiallyObservableMarkovDecisionProcess.yaml
    role: maintained_record
  acceptance_checks:
  - python -m aimech validate
  - python scripts/record_review.py check --require-reviews --base main
- action_id: A-C1S4-002
  description: In Stage 5 (resolve_review_findings), verify and populate sha256 content
    digests (or record explicit versioned snapshot provenance) for the 7 access_level=documentation
    sources in Apriori.yaml, Eclat.yaml, GeneticAlgorithm.yaml, HiddenMarkovModel.yaml,
    BarlowTwins.yaml, and VICReg.yaml with append-only history sidecars.
  finding_ids:
  - F-C1S4-002
  target_ids:
  - AIMech:Apriori
  - AIMech:BarlowTwins
  - AIMech:Eclat
  - AIMech:GeneticAlgorithm
  - AIMech:HiddenMarkovModel
  - AIMech:VICReg
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Apriori.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/BarlowTwins.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/Eclat.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/GeneticAlgorithm.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/HiddenMarkovModel.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/VICReg.yaml
    role: maintained_record
  acceptance_checks:
  - python -m aimech validate
  - python scripts/record_review.py check --require-reviews --base main
- action_id: A-C1S4-003
  description: In Stage 5 (resolve_review_findings), write target-specific aio_mappings[].rationale
    statements in GloVe.yaml, replace 'this candidate specifically uses an undirected
    graph' in MarkovRandomField.yaml, remove the batch-discovery diary tail from identity_notes
    in CLARANSClustering.yaml, LargeMarginNearestNeighbor.yaml, and RelevantComponentAnalysis.yaml,
    and record history sidecars.
  finding_ids:
  - F-C1S4-003
  target_ids:
  - AIMech:CLARANSClustering
  - AIMech:GloVe
  - AIMech:LargeMarginNearestNeighbor
  - AIMech:MarkovRandomField
  - AIMech:RelevantComponentAnalysis
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CLARANSClustering.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/GloVe.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/LargeMarginNearestNeighbor.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/MarkovRandomField.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: data/curated/RelevantComponentAnalysis.yaml
    role: maintained_record
  acceptance_checks:
  - python -m aimech validate
  - python scripts/record_review.py check --require-reviews --base main
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:BarlowTwins
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:CLARANSClustering
  - AIMech:DBSCAN
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LargeMarginNearestNeighbor
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:RelevantComponentAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VICReg
  - AIMech:VotingClassifier
  rationale: All 38 maintained CuratedAIConcept records represent distinct AI methods,
    models, objectives, or representations absent from pinned AIO release 2026-07-22;
    open findings F-C1S4-001..F-C1S4-003 concern source digest provenance and mapping/identity-note
    wording rather than concept-boundary duplication.
  evidence_ids:
  - E-CURATED-SCHEMA
  - E-FIRST-COHORT-DISCOVERY
  - E-C1S4-AUDIT
limitations:
- Per Stage 4 (record_review) non-mutation policy, curated YAML records are not edited
  in this stage; open findings F-C1S4-001, F-C1S4-002, and F-C1S4-003 are carried
  forward to Stage 5 (resolve_review_findings).
tags:
- cycle-1
- stage-4
- record-review
- curated-provenance
```
