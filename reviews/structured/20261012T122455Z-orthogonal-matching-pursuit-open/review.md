# Scientific author self-review of Orthogonal matching pursuit

- Review: 20261012T122455Z-orthogonal-matching-pursuit-open
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T12:19:49Z
- Finished UTC: 2026-10-12T12:24:55Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two minor evidence defects require correction: an unused MP source rejected by validation, and an unaudited external selection-rule attribution. Core OMP identity, projection equations and mapping are supported.

## Scope And Provenance

Every field of one maintained pursuit algorithm.

Selection: Exact maintainedID AIMech:OrthogonalMatchingPursuit
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f0c4b81da07d6134ffc9e2eb69e9aa7582809fe9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:OrthogonalMatchingPursuit | data/curated/OrthogonalMatchingPursuit.yaml | maintained | Orthogonal matching pursuit |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | failed | True | AIMech:OrthogonalMatchingPursuit | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 98.05s (0:01:38)<br>Checked 442 record(s); 0 failed.<br>ERROR data/curated/OrthogonalMatchingPursuit.yaml: evidence_sources: uncited sources mallat1993<br>Checked 527 curated concept record(s); 1 error(s).<br>uv run --locked --extra dev python scripts/check.py<br>error: recipe &#96;check&#96; failed on line 10 with exit code 1<br> |
| just vendored-check | passed | True | AIMech:OrthogonalMatchingPursuit | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:OrthogonalMatchingPursuit | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:OrthogonalMatchingPursuit | Exitedwithoutoutput. |
| Exact pursuit counterexamples | passed | True | AIMech:OrthogonalMatchingPursuit | {"mp_three_steps": [{"atom": 1, "coefficient": "4/5", "residual": ["-12/25", "9/25"]}, {"atom": 0, "coefficient": "-12/25", "residual": ["0", "9/25"]}, {"atom": 1, "coefficient": "36/125", "residual": ["-108/625", "81/625"]}], "omp_two_steps": [{"selected": [1], "coefficients": ["4/5"], "residual": ["-12/25", "9/25"]}, {"selected": [1, 0], "coefficients": ["5/4", "-3/4"], "residual": ["0", "0"]}], "omp_nonminimal_support": [{"selected": [1], "coefficients": ["-4/9"], "residual": ["1/9", "0", "-1/9"]}, {"selected": [1, 0], "coefficients": ["-4/9", "1/9"], "residual": ["0", "0", "-1/9"]}, {"selected": [1, 0, 2], "coefficients": ["-4/9", "1/9", "-1/9"], "residual": ["0", "0", "0"]}], "minimum_possible_support": 2, "weak_selected_threshold_not_maximum": {"signal": ["1", "3/4"], "alpha": "1/2", "delta": "4/5"}, "scope": "Exact finite real unit dictionaries; deterministic lowest-index ties. Algebraic counterexamples, not empirical benchmarks."} |

## Scientific And Domain Assessments

### Distinct greedy approximation algorithms

identity: supported. Targets: AIMech:OrthogonalMatchingPursuit.

Retain the native algorithm identity.

A greedy fixed-dictionary approximation algorithm that selects an atom correlated with the current residual and recomputes the approximation as the orthogonal projection of the signal onto the span of all selected atoms. The record selects finite real unit-norm dictionaries and exact maximum-correlation selection, while describing the original weak-selection formulation separately. Orthogonal refers to the residual and selected-span projection; the supplied dictionary need not be orthogonal. It is distinct from single-atom matching pursuit, a minimum-L1 principle, and a globally optimal subset search. OMP is a source-supported local alias; same-token environment RDF prefixes do not denote this AI concept. All 442 AIO IDs, labels and scoped synonyms and 525 preceding native IDs, names and aliases were compared. The only normalized hit was MP, an exact MarkovChain synonym; the full MarkovChain record and node distinguish that stochastic model from pursuit. Ignored/hidden-inclusive searches of both checkouts found the prior pursuit source lead, Markov-chain context, author initials and unrelated environment tokens or RDF prefixes, not an existing pursuit record. The semantic comparison read 107 AIO name/synonym/definition rows and 148 native name/definition rows; nine full AIO CLASS nodes and incident edges and twelve contextual YAMLs were inspected. Basis pursuit specifies exact minimum-L1 reconstruction, least-angle regression follows an equiangular path, and NMF fits nonnegative factors. This is a bounded identity assessment of the inspected corpus.

### Fixed dictionary versus learned network

grounding: supported. Targets: AIMech:OrthogonalMatchingPursuit.

The related mapping preserves network and dictionary-learning scope differences.

The pinned target is a representation-learning network that finds sparse linear representations and identifies their elements, with exact sparse-coding and dictionary-learning synonyms. Pursuit constructs a representation using a supplied fixed dictionary, so the sparse-representation connection is direct. It does not learn dictionary elements or require a neural network; related_match preserves those scope differences without a subclass or equivalence assertion. RepresentationLearning and SparseAutoEncoder are different neural scopes. LassoRegression, LinearRegression and LeastsquaresAnalysis do not specify this atom-selection procedure. FeatureExtraction can be an application, and MathematicalFunction is too generic to identify it. MarkovChain is unrelated despite its MP synonym.

### select and refit

evidence: supported. Targets: AIMech:OrthogonalMatchingPursuit.

Supported within the stated finite-dictionary and source scope.

Starting from an empty selected set and residual y, choose an unselected unit atom maximizing absolute correlation with the current residual. Add it to the set, solve least squares over all selected columns and recompute the residual from that joint fit. In exact arithmetic the residual is orthogonal to the entire selected span. A nonzero correlated atom cannot already lie in that span. The method does not require the dictionary atoms to be mutually orthogonal. Locators: Sections 1–2.2, Equations 1–7 and algorithm Steps I–VII, PDF pp. 1–3 / printed pp. 40–42

### recursive projection update

evidence: supported. Targets: AIMech:OrthogonalMatchingPursuit.

Supported within the stated finite-dictionary and source scope.

Let x_new=sum_i b_i*x_i+gamma, with gamma orthogonal to the old selected span. For a nonzero selected correlation, gamma is nonzero. In the real case the new coefficient is c=(r^T*x_new)/&#124;&#124;gamma&#124;&#124;^2, and each old coefficient changes from a_i to a_i-c*b_i. The squared residual decreases by abs(r^T*x_new)^2/&#124;&#124;gamma&#124;&#124;^2. The source’s recursive Gram-matrix implementation realizes this projection algebra; nearly dependent atoms can make finite-precision solves sensitive. Locators: Sections 2.1–2.3, Equations 4–12, PDF pp. 2–4 / printed pp. 41–43

### selected subset versus global optimum

evidence: supported. Targets: AIMech:OrthogonalMatchingPursuit.

Supported within the stated finite-dictionary and source scope.

Optimality of the least-squares fit is conditional on the selected subset; it is not optimal selection among all equally sized subsets. A curator example with unit columns [e1,e2,e3,b], b=(8/9,4/9,1/9), and y=e1-b selects e2 first, then e1 and e3 under lowest-index ties, requiring three atoms for zero residual. Yet e1-b is a two-atom representation, and no single atom is collinear with y. The documented fixed-cardinality and residual-tolerance objectives are approximation targets, not unconditional minimum-support guarantees. Locators: Section 2 opening paragraph and Section 2.2 remarks, PDF pp. 2–3 / printed pp. 41–42; curator-derived exact examples in research/discovery/pursuit-boundaries.py; Section 1.1.9, approximate fixed-cardinality and residual-tolerance objectives

### finite termination conditions

evidence: supported. Targets: AIMech:OrthogonalMatchingPursuit.

Supported within the stated finite-dictionary and source scope.

With exact arithmetic, a finite dictionary and no premature tolerance stop, each nonzero-correlation selection adds an independent direction; the process reaches the projection onto the full dictionary span in at most its rank steps. This rank bound sharpens the paper’s dictionary-size bound by the stated independence argument. Residual zero additionally requires y to lie in that span. Early stopping, numerical rank decisions and noisy observations change the practical result and do not establish recovery of a generating support. Locators: Section 2.2, Theorem 2.1 and remarks, PDF p. 3 / printed p. 42; curator finite-dimensional independence consequence

### weak selection and printing caveat

evidence: supported. Targets: AIMech:OrthogonalMatchingPursuit.

Supported within the stated finite-dictionary and source scope.

The original paper introduces a fixed-fraction correlation condition with 0&lt;alpha&lt;=1. Its page-3 algorithm box prints strict &gt; against alpha times the supremum even though the earlier condition is &gt;=; strict &gt; is impossible at alpha=1. This record uses the consistent non-strict condition and exact finite maximum convention, also described in the versioned implementation guide, and preserves the apparent source inconsistency. The paper’s selected-correlation threshold delta&gt;0 is an early-stop rule. Under weak selection, a selected correlation below delta need not mean that every available atom has correlation below delta. Locators: Section 1 correlation condition and Section 2.1 algorithm Steps II–III, PDF pp. 1,3 / printed pp. 40,42; curator-derived exact examples in research/discovery/pursuit-boundaries.py; Section 1.1.9, maximum-correlation selection

### runtime and method boundaries

evidence: concern. Targets: AIMech:OrthogonalMatchingPursuit.

Narrow one unsupported attribution to other methods.

The paper contrasts whole-span refitting with MP and gives selected wavelet-decomposition examples. Fewer iterations do not imply universally lower cost: refitting adds work, and the conclusion’s speed expectation for highly redundant dictionaries is explicitly a conjecture. The selection score is residual correlation with the original unit atom, not the projected-atom-normalized gain used by other orthogonal selection rules. An external orthogonal-least-squares algorithm and its identity require separate primary-source assessment. Locators: Sections 2.1–4, Figures 1–5 and conclusion, PDF pp. 3–5 / printed pp. 42–44

### Last-atom versus selected-span orthogonality

consistency: supported. Targets: AIMech:OrthogonalMatchingPursuit.

The two algorithms are not duplicates.

With b=(3/5,4/5) and y=e2, both first select b. MP subtracts e1 next and leaves (0,9/25), not orthogonal to b. OMP solves over both columns and changes the old coefficient from4/5to5/4, with newe1coefficient-3/4 and residual0. The optional finalMPbackprojection does not change the intervening greedy path. Orthogonal dictionary columns are not required.

### Selected-set least squares versus minimum support

consistency: supported. Targets: AIMech:OrthogonalMatchingPursuit.

Conditional fitting optimality does not imply optimal subset selection.

For unitdictionary[identity,b] withb=(8/9,4/9,1/9),y=e1-b, absolute first correlations selecte2; remainingidentityatoms tie and beatb. Lowest-index ties givee1thene3. OMPuses3atoms although a2-atom exactrepresentation exists; noncollinearity excludes1atom. In exactfinitearithmetic nonzero correlations add independentdirections, giving the stated rank bound, with residual outside dictionary span preserved.

### Printed inequalities and source versions

provenance: supported. Targets: AIMech:OrthogonalMatchingPursuit.

Apparent source inconsistencies remain visible.

OMPintroprints&gt;=,algorithmStepIIprints&gt;whileallowingalpha1. The latter is impossible at the supremum; the record uses the consistent non-strict finite-max convention without inventing an erratum. MPenergyEq17 supplies squarednormidentity despite Eq35printing. Ambiguous examplecounts are not numerical performance claims.1993journalMP and cited1992preprint remain distinct versions.

### Complete record and scope

provenance: concern. Targets: AIMech:OrthogonalMatchingPursuit.

Every maintained field was read after capture; one bounded evidence attribution requires correction.

ReadID,label,aliases(ifpresent),kind,definition,identitynotes,definitionevidence,allclaims/locators,allsourceversions/access/hashes,mappingpin/relation/rationale,limitations,DRAFTstatus andactualUTCcuration. Sourcehashes and reportmirrors match. MPabbreviation is not an alias because it collides withMarkovChain. OMPalias matches its primarysource.463pendingand46partlyaddressedcohorts remain.

## Findings

### external-selection-attribution: Bound the OMP selection-score comparison to inspected evidence

minor / open / confirmed; issue key: aimech-omp-external-selection-attribution.

The runtime-and-method-boundaries claim attributes projected-atom-normalized gain to other orthogonal selection rules, but its cited Pati1993passages establish only OMPrawcorrelation and projection energy. The external orthogonal-least-squares source is expressly pending. Replace the unaudited attribution with the algebraic distinction between rawcorrelation selection and the displayed projection-energy decrease, or inspect and cite the external method. This is bounded evidence wording, not a defect in OMPidentity or its equations.

### uncited-source: Cite the MP contrast source in the OMP record

minor / open / confirmed; issue key: aimech-omp-uncited-mallat-source.

The maintained OMP record lists Mallat1993 without a claim-level citation, and validate-curated rejects the uncited source. The runtime contrast actually concerns MP versus OMP; attach a precise Mallat locator to that supported contrast, or remove the unused source if it is not used.

## Recommended Actions And Acceptance Checks

### narrow-selection-attribution

Narrow the maintained claim and report mirror to the inspected OMP equations, preserve external OLS as pending, append edit history and save a successor disposition.

- Claim compares rawcorrelation with the source-derived normalized projection-energy decrease without attributing an unaudited external algorithm.
- Report mirror and regenerated pages agree with the corrected YAML.
- Required gates pass and successor review retains the stable issue key and predecessor target.

### cite-contrast-source

Attach the inspected MP update and backprojection passages to the maintained MP-versus-OMP contrast and mirror the correction in the report.

- Every listed evidence source is cited by a supported definition or claim.
- Full validate-curated and just check pass.

## Category Boundaries

- retain: AIMech:OrthogonalMatchingPursuit. Single-atom MP and selected-span-refitting OMP differ on the explicit same-input example. Neither is the BPoptimizationprinciple, a learned dictionary, a neural architecture or a global subset optimizer.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T121936Z-matching-pursuits.json | supports | The record covers the finite real-dictionary algorithm and identifies the paper’s fixed-fraction weak-selection generalization. MP is used only as a contextual source abbreviation and is not an identity alias. It differs from orthogonal matching pursuit, which refits the whole selected span at every step. All 442 AIO IDs, labels and scoped synonyms and 525 preceding native IDs, names and aliases were compared. The only normalized hit was MP, an exact MarkovChain synonym; the full MarkovChain record and node distinguish that stochastic model from pursuit. Ignored/hidden-inclusive searches of both checkouts found the prior pursuit source lead, Markov-chain context, author initials and unrelated environment tokens or RDF prefixes, not an existing pursuit record. The semantic comparison read 107 AIO name/synonym/definition rows and 148 native name/definition rows; nine full AIO CLASS nodes and incident edges and twelve contextual YAMLs were inspected. Basis pursuit specifies exact minimum-L1 reconstruction, least-angle regression follows an equiangular path, and NMF fits nonnegative factors. This is a bounded identity assessment of the inspected corpus. |
| mapping | sources/aio/aio.json; Nine declared annotated CLASS nodes and incident edges; twelve contextual YAML inputs. | supports | The pinned target is a representation-learning network that finds sparse linear representations and identifies their elements, with exact sparse-coding and dictionary-learning synonyms. Pursuit constructs a representation using a supplied fixed dictionary, so the sparse-representation connection is direct. It does not learn dictionary elements or require a neural network; related_match preserves those scope differences without a subclass or equivalence assertion. RepresentationLearning and SparseAutoEncoder are different neural scopes. LassoRegression, LinearRegression and LeastsquaresAnalysis do not specify this atom-selection procedure. FeatureExtraction can be an application, and MathematicalFunction is too generic to identify it. MarkovChain is unrelated despite its MP synonym. |
| certificates | research/discovery/pursuit-boundaries.py | supports | Exact rational examples verify MP revisits, OMP joint-refit coefficients, a unit-dictionary OMP three-atom result when two suffice, and weak selected-threshold failure to bound the maximum correlation. |
| mallat1993 | https://www.di.ens.fr/~mallat/papiers/MallatPursuit93.pdf; IEEE Transactions on Signal Processing 41(12),3397–3415,December 1993. Actual 19-page author-hosted scan; all pages visually read, including Sections I–VIII, Appendices A–E, Figures 1–6 and 17 references. Printed page = PDF page + 3396. The separate 1992 preprint was not inspected. | supports | Source inspected as described. All19Mallatpages and all5Patipages visually read; centralMPpage3andOMPpages1–2 were reread after canonical capture. The versioned guide supports exact maximum-correlation/refit description and labels cardinality objectives approximate. External orthogonal-least-squares source remains uninspected. |
| pati1993 | https://www.ccs.neu.edu/home/eelhami/courses/EE290A/OMP_Krishnaprasad.pdf; Proceedings of the 27th Asilomar Conference on Signals, Systems and Computers,vol.1,40–44,1993. Actual five-page university-hosted paper; all pages visually read, including Sections 1–4, the algorithm box, Theorem 2.1, Figures 1–5 and three references. Printed page = PDF page + 39. | supports | Source inspected as described. All19Mallatpages and all5Patipages visually read; centralMPpage3andOMPpages1–2 were reread after canonical capture. The versioned guide supports exact maximum-correlation/refit description and labels cardinality objectives approximate. External orthogonal-least-squares source remains uninspected. |
| sklearn18 | https://scikit-learn.org/1.8/modules/linear_model.html#orthogonal-matching-pursuit-omp; scikit-learn 1.8.0, Section 1.1.9; versioned user-guide description inspected, not an execution or source-code audit. | supports | Source inspected as described. All19Mallatpages and all5Patipages visually read; centralMPpage3andOMPpages1–2 were reread after canonical capture. The versioned guide supports exact maximum-correlation/refit description and labels cardinality objectives approximate. External orthogonal-least-squares source remains uninspected. |

## Limits And Additional Notes

- Author self-review only; nativeDRAFTstatus remains.
- Two DRAFT algorithms added;527native and442unchangedAIOrecords.463pendingand46partlyaddressedcohorts plus other unresolved scopes mean discovery is ongoing.
- All24pages across the two1993primarypapers were visually read. The1992MPpreprint, external recovery results, orthogonal-least-squares and newsourcecohorts were not fully audited.
- No model training, empirical benchmark or author implementation was run. Exact rational counterexamples establish finite algebraic cases.
- Apparent source typography is explicitly preserved. DOIwebopens/IEEEbodyaccess failed; public Crossrefmetadata and actual inspected PDFs establish bibliographic identity.
- The OMPguide was read for Section1.1.9. Technicalreport2008abstract/openingtext is a lead, not a full method inspection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T122455Z-orthogonal-matching-pursuit-open
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Orthogonal matching pursuit
started_at: '2026-10-12T12:19:49Z'
finished_at: '2026-10-12T12:24:55Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent read both primarypapers in full, challenged
    update/optimality/threshold claims with rational examples, and reread every recordfield
    and centralprimarypages after canonical capture. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Two minor evidence defects require correction: an unused MP source rejected
  by validation, and an unaudited external selection-rule attribution. Core OMP identity,
  projection equations and mapping are supported.'
source:
  git_revision: f0c4b81da07d6134ffc9e2eb69e9aa7582809fe9
  state: working_tree
  inputs:
  - path: data/aio/FeatureExtraction.yaml
    sha256: d153b8bbe04e9abb7f1ec13e6219dbcd329235ac58bb9229d4a1f416216c07ef
    role: context
  - path: data/aio/LassoRegression.yaml
    sha256: c62e7ffd00a16f5a82d514687b094aee5f6796d19a7d16200bdb10498c024949
    role: context
  - path: data/aio/LeastsquaresAnalysis.yaml
    sha256: 666926bd17035ea825f0f521620b9c5538ff2a8695e7d37f96ab3b0cc8aa1d3c
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/RepresentationLearning.yaml
    sha256: bc7af756440437f60210019e17ad1e2dd15cd1c7cbfbc96312520934b7a5c7ca
    role: context
  - path: data/aio/SparseAutoEncoder.yaml
    sha256: 9bbb865ec227305e8ddbe8eab9546510048109d43ba3a733d25303e4780ec359
    role: context
  - path: data/aio/SparseLearning.yaml
    sha256: 0e45f464899bee39df6c8af85e3e0fccba4062f39c73e35c8e884113f78ce3c5
    role: context
  - path: data/curated/BasisPursuit.yaml
    sha256: 962cb52fb514105bea0b9296ad29569b0857a9fe8ecf437894dc1c1426010730
    role: context
  - path: data/curated/LeastAngleRegression.yaml
    sha256: 379431bca38c3bbac6653617a424e692fba98edc1cf7f8d25b388328e5fe7ab5
    role: context
  - path: data/curated/MatchingPursuit.yaml
    sha256: a24959ced5e8f39c3b861dd89fe7ab4407ac632f9187bc4bfa8f0cb1c30a5953
    role: context
  - path: data/curated/NonnegativeMatrixFactorization.yaml
    sha256: 3b79c0f7568f3cdc86f5779be7e9c3e2341c547682223e214a6b94031016df7b
    role: context
  - path: data/curated/OrthogonalMatchingPursuit.yaml
    sha256: 33c969903a6f584d047095cba703c20ebc71093af35f918d555c94713e2f6589
    role: target
  - path: research/discovery/20261012T121936Z-matching-pursuits.json
    sha256: 436612e87cda7f5e41e9fa31444b16f55997ed90789821541f412317e362305b
    role: context
  - path: research/discovery/pursuit-boundaries.py
    sha256: 4f2db17c42c39247fdaa44e966a35459ee09db82eb2c910edb3e5578b61c574e
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
- target_id: AIMech:OrthogonalMatchingPursuit
  path: data/curated/OrthogonalMatchingPursuit.yaml
  label: Orthogonal matching pursuit
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OrthogonalMatchingPursuit.yaml
    role: maintained
scope:
  description: Every field of one maintained pursuit algorithm.
  selection: Exact maintainedID AIMech:OrthogonalMatchingPursuit
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:OrthogonalMatchingPursuit
  exclusions:
  - target: Contextual records
    reason: Identity/mapping context only, not broad scientific re-review.
  - target: External OLS, recovery results and new source cohorts
    reason: Full primary methods not audited.
  - target: Empirical execution
    reason: Only exact rational examples were run; no model training or benchmark.
  - target: Discovery frontier
    reason: 463pendingand46partlyaddressedcohorts remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: failed
  required: true
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  exit_code: 1
  expected_exit_code: 0
  summary: 'All checks passed!

    ........................................................................ [ 28%]

    ........................................................................ [ 57%]

    ........................................................................ [ 86%]

    ...............................sss                                       [100%]

    247 passed, 3 skipped in 98.05s (0:01:38)

    Checked 442 record(s); 0 failed.

    ERROR data/curated/OrthogonalMatchingPursuit.yaml: evidence_sources: uncited sources
    mallat1993

    Checked 527 curated concept record(s); 1 error(s).

    uv run --locked --extra dev python scripts/check.py

    error: recipe `check` failed on line 10 with exit code 1

    '
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
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
  - AIMech:OrthogonalMatchingPursuit
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
  - AIMech:OrthogonalMatchingPursuit
  exit_code: 0
  expected_exit_code: 0
  summary: Exitedwithoutoutput.
- check_id: certificates
  name: Exact pursuit counterexamples
  command: python3 research/discovery/pursuit-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  exit_code: 0
  expected_exit_code: 0
  summary: '{"mp_three_steps": [{"atom": 1, "coefficient": "4/5", "residual": ["-12/25",
    "9/25"]}, {"atom": 0, "coefficient": "-12/25", "residual": ["0", "9/25"]}, {"atom":
    1, "coefficient": "36/125", "residual": ["-108/625", "81/625"]}], "omp_two_steps":
    [{"selected": [1], "coefficients": ["4/5"], "residual": ["-12/25", "9/25"]}, {"selected":
    [1, 0], "coefficients": ["5/4", "-3/4"], "residual": ["0", "0"]}], "omp_nonminimal_support":
    [{"selected": [1], "coefficients": ["-4/9"], "residual": ["1/9", "0", "-1/9"]},
    {"selected": [1, 0], "coefficients": ["-4/9", "1/9"], "residual": ["0", "0", "-1/9"]},
    {"selected": [1, 0, 2], "coefficients": ["-4/9", "1/9", "-1/9"], "residual": ["0",
    "0", "0"]}], "minimum_possible_support": 2, "weak_selected_threshold_not_maximum":
    {"signal": ["1", "3/4"], "alpha": "1/2", "delta": "4/5"}, "scope": "Exact finite
    real unit dictionaries; deterministic lowest-index ties. Algebraic counterexamples,
    not empirical benchmarks."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T121936Z-matching-pursuits.json
  accessed_at: '2026-10-12T12:19:49Z'
  support: supports
  summary: The record covers the finite real-dictionary algorithm and identifies the
    paper’s fixed-fraction weak-selection generalization. MP is used only as a contextual
    source abbreviation and is not an identity alias. It differs from orthogonal matching
    pursuit, which refits the whole selected span at every step. All 442 AIO IDs,
    labels and scoped synonyms and 525 preceding native IDs, names and aliases were
    compared. The only normalized hit was MP, an exact MarkovChain synonym; the full
    MarkovChain record and node distinguish that stochastic model from pursuit. Ignored/hidden-inclusive
    searches of both checkouts found the prior pursuit source lead, Markov-chain context,
    author initials and unrelated environment tokens or RDF prefixes, not an existing
    pursuit record. The semantic comparison read 107 AIO name/synonym/definition rows
    and 148 native name/definition rows; nine full AIO CLASS nodes and incident edges
    and twelve contextual YAMLs were inspected. Basis pursuit specifies exact minimum-L1
    reconstruction, least-angle regression follows an equiangular path, and NMF fits
    nonnegative factors. This is a bounded identity assessment of the inspected corpus.
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Nine declared annotated CLASS nodes and incident edges; twelve contextual
    YAML inputs.
  accessed_at: '2026-10-12T12:19:49Z'
  support: supports
  summary: The pinned target is a representation-learning network that finds sparse
    linear representations and identifies their elements, with exact sparse-coding
    and dictionary-learning synonyms. Pursuit constructs a representation using a
    supplied fixed dictionary, so the sparse-representation connection is direct.
    It does not learn dictionary elements or require a neural network; related_match
    preserves those scope differences without a subclass or equivalence assertion.
    RepresentationLearning and SparseAutoEncoder are different neural scopes. LassoRegression,
    LinearRegression and LeastsquaresAnalysis do not specify this atom-selection procedure.
    FeatureExtraction can be an application, and MathematicalFunction is too generic
    to identify it. MarkovChain is unrelated despite its MP synonym.
- evidence_id: certificates
  kind: record_content
  reference: research/discovery/pursuit-boundaries.py
  accessed_at: '2026-10-12T12:19:49Z'
  snapshot_sha256: 4f2db17c42c39247fdaa44e966a35459ee09db82eb2c910edb3e5578b61c574e
  support: supports
  summary: Exact rational examples verify MP revisits, OMP joint-refit coefficients,
    a unit-dictionary OMP three-atom result when two suffice, and weak selected-threshold
    failure to bound the maximum correlation.
- evidence_id: mallat1993
  kind: primary_source
  reference: https://www.di.ens.fr/~mallat/papiers/MallatPursuit93.pdf
  locator: IEEE Transactions on Signal Processing 41(12),3397–3415,December 1993.
    Actual 19-page author-hosted scan; all pages visually read, including Sections
    I–VIII, Appendices A–E, Figures 1–6 and 17 references. Printed page = PDF page
    + 3396. The separate 1992 preprint was not inspected.
  accessed_at: '2026-10-12T12:05:23Z'
  snapshot_sha256: 5f0efe79b52470bcee30af82be8765402913a3e9c2bea6f2ef080938c22bebe7
  support: supports
  summary: Source inspected as described. All19Mallatpages and all5Patipages visually
    read; centralMPpage3andOMPpages1–2 were reread after canonical capture. The versioned
    guide supports exact maximum-correlation/refit description and labels cardinality
    objectives approximate. External orthogonal-least-squares source remains uninspected.
- evidence_id: pati1993
  kind: primary_source
  reference: https://www.ccs.neu.edu/home/eelhami/courses/EE290A/OMP_Krishnaprasad.pdf
  locator: Proceedings of the 27th Asilomar Conference on Signals, Systems and Computers,vol.1,40–44,1993.
    Actual five-page university-hosted paper; all pages visually read, including Sections
    1–4, the algorithm box, Theorem 2.1, Figures 1–5 and three references. Printed
    page = PDF page + 39.
  accessed_at: '2026-10-12T12:05:32Z'
  snapshot_sha256: 8cb44738ff5756265a3935de64bf0afd8ef4d090a7980c715893ebf60374be6c
  support: supports
  summary: Source inspected as described. All19Mallatpages and all5Patipages visually
    read; centralMPpage3andOMPpages1–2 were reread after canonical capture. The versioned
    guide supports exact maximum-correlation/refit description and labels cardinality
    objectives approximate. External orthogonal-least-squares source remains uninspected.
- evidence_id: sklearn18
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/linear_model.html#orthogonal-matching-pursuit-omp
  locator: scikit-learn 1.8.0, Section 1.1.9; versioned user-guide description inspected,
    not an execution or source-code audit.
  accessed_at: '2026-10-12T12:15:49Z'
  snapshot_sha256: 358fa62c5481b2f90974d9ea42895548ffd796ae199fcf99ea43c4b57e65cf9b
  support: supports
  summary: Source inspected as described. All19Mallatpages and all5Patipages visually
    read; centralMPpage3andOMPpages1–2 were reread after canonical capture. The versioned
    guide supports exact maximum-correlation/refit description and labels cardinality
    objectives approximate. External orthogonal-least-squares source remains uninspected.
assessments:
- assessment_id: identity
  area: identity
  topic: Distinct greedy approximation algorithms
  outcome: supported
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  evidence_ids:
  - identity
  - mallat1993
  - pati1993
  summary: Retain the native algorithm identity.
  details: A greedy fixed-dictionary approximation algorithm that selects an atom
    correlated with the current residual and recomputes the approximation as the orthogonal
    projection of the signal onto the span of all selected atoms. The record selects
    finite real unit-norm dictionaries and exact maximum-correlation selection, while
    describing the original weak-selection formulation separately. Orthogonal refers
    to the residual and selected-span projection; the supplied dictionary need not
    be orthogonal. It is distinct from single-atom matching pursuit, a minimum-L1
    principle, and a globally optimal subset search. OMP is a source-supported local
    alias; same-token environment RDF prefixes do not denote this AI concept. All
    442 AIO IDs, labels and scoped synonyms and 525 preceding native IDs, names and
    aliases were compared. The only normalized hit was MP, an exact MarkovChain synonym;
    the full MarkovChain record and node distinguish that stochastic model from pursuit.
    Ignored/hidden-inclusive searches of both checkouts found the prior pursuit source
    lead, Markov-chain context, author initials and unrelated environment tokens or
    RDF prefixes, not an existing pursuit record. The semantic comparison read 107
    AIO name/synonym/definition rows and 148 native name/definition rows; nine full
    AIO CLASS nodes and incident edges and twelve contextual YAMLs were inspected.
    Basis pursuit specifies exact minimum-L1 reconstruction, least-angle regression
    follows an equiangular path, and NMF fits nonnegative factors. This is a bounded
    identity assessment of the inspected corpus.
- assessment_id: mapping
  area: grounding
  topic: Fixed dictionary versus learned network
  outcome: supported
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  evidence_ids:
  - mapping
  - mallat1993
  - pati1993
  summary: The related mapping preserves network and dictionary-learning scope differences.
  details: The pinned target is a representation-learning network that finds sparse
    linear representations and identifies their elements, with exact sparse-coding
    and dictionary-learning synonyms. Pursuit constructs a representation using a
    supplied fixed dictionary, so the sparse-representation connection is direct.
    It does not learn dictionary elements or require a neural network; related_match
    preserves those scope differences without a subclass or equivalence assertion.
    RepresentationLearning and SparseAutoEncoder are different neural scopes. LassoRegression,
    LinearRegression and LeastsquaresAnalysis do not specify this atom-selection procedure.
    FeatureExtraction can be an application, and MathematicalFunction is too generic
    to identify it. MarkovChain is unrelated despite its MP synonym.
- assessment_id: select-and-refit
  area: evidence
  topic: select and refit
  outcome: supported
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  evidence_ids:
  - pati1993
  - certificates
  summary: Supported within the stated finite-dictionary and source scope.
  details: 'Starting from an empty selected set and residual y, choose an unselected
    unit atom maximizing absolute correlation with the current residual. Add it to
    the set, solve least squares over all selected columns and recompute the residual
    from that joint fit. In exact arithmetic the residual is orthogonal to the entire
    selected span. A nonzero correlated atom cannot already lie in that span. The
    method does not require the dictionary atoms to be mutually orthogonal. Locators:
    Sections 1–2.2, Equations 1–7 and algorithm Steps I–VII, PDF pp. 1–3 / printed
    pp. 40–42'
- assessment_id: recursive-projection-update
  area: evidence
  topic: recursive projection update
  outcome: supported
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  evidence_ids:
  - pati1993
  - certificates
  summary: Supported within the stated finite-dictionary and source scope.
  details: 'Let x_new=sum_i b_i*x_i+gamma, with gamma orthogonal to the old selected
    span. For a nonzero selected correlation, gamma is nonzero. In the real case the
    new coefficient is c=(r^T*x_new)/||gamma||^2, and each old coefficient changes
    from a_i to a_i-c*b_i. The squared residual decreases by abs(r^T*x_new)^2/||gamma||^2.
    The source’s recursive Gram-matrix implementation realizes this projection algebra;
    nearly dependent atoms can make finite-precision solves sensitive. Locators: Sections
    2.1–2.3, Equations 4–12, PDF pp. 2–4 / printed pp. 41–43'
- assessment_id: selected-subset-versus-global-optimum
  area: evidence
  topic: selected subset versus global optimum
  outcome: supported
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  evidence_ids:
  - pati1993
  - sklearn18
  - certificates
  summary: Supported within the stated finite-dictionary and source scope.
  details: 'Optimality of the least-squares fit is conditional on the selected subset;
    it is not optimal selection among all equally sized subsets. A curator example
    with unit columns [e1,e2,e3,b], b=(8/9,4/9,1/9), and y=e1-b selects e2 first,
    then e1 and e3 under lowest-index ties, requiring three atoms for zero residual.
    Yet e1-b is a two-atom representation, and no single atom is collinear with y.
    The documented fixed-cardinality and residual-tolerance objectives are approximation
    targets, not unconditional minimum-support guarantees. Locators: Section 2 opening
    paragraph and Section 2.2 remarks, PDF pp. 2–3 / printed pp. 41–42; curator-derived
    exact examples in research/discovery/pursuit-boundaries.py; Section 1.1.9, approximate
    fixed-cardinality and residual-tolerance objectives'
- assessment_id: finite-termination-conditions
  area: evidence
  topic: finite termination conditions
  outcome: supported
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  evidence_ids:
  - pati1993
  - certificates
  summary: Supported within the stated finite-dictionary and source scope.
  details: 'With exact arithmetic, a finite dictionary and no premature tolerance
    stop, each nonzero-correlation selection adds an independent direction; the process
    reaches the projection onto the full dictionary span in at most its rank steps.
    This rank bound sharpens the paper’s dictionary-size bound by the stated independence
    argument. Residual zero additionally requires y to lie in that span. Early stopping,
    numerical rank decisions and noisy observations change the practical result and
    do not establish recovery of a generating support. Locators: Section 2.2, Theorem
    2.1 and remarks, PDF p. 3 / printed p. 42; curator finite-dimensional independence
    consequence'
- assessment_id: weak-selection-and-printing-caveat
  area: evidence
  topic: weak selection and printing caveat
  outcome: supported
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  evidence_ids:
  - pati1993
  - sklearn18
  - certificates
  summary: Supported within the stated finite-dictionary and source scope.
  details: 'The original paper introduces a fixed-fraction correlation condition with
    0<alpha<=1. Its page-3 algorithm box prints strict > against alpha times the supremum
    even though the earlier condition is >=; strict > is impossible at alpha=1. This
    record uses the consistent non-strict condition and exact finite maximum convention,
    also described in the versioned implementation guide, and preserves the apparent
    source inconsistency. The paper’s selected-correlation threshold delta>0 is an
    early-stop rule. Under weak selection, a selected correlation below delta need
    not mean that every available atom has correlation below delta. Locators: Section
    1 correlation condition and Section 2.1 algorithm Steps II–III, PDF pp. 1,3 /
    printed pp. 40,42; curator-derived exact examples in research/discovery/pursuit-boundaries.py;
    Section 1.1.9, maximum-correlation selection'
- assessment_id: runtime-and-method-boundaries
  area: evidence
  topic: runtime and method boundaries
  outcome: concern
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  evidence_ids:
  - pati1993
  - certificates
  summary: Narrow one unsupported attribution to other methods.
  details: 'The paper contrasts whole-span refitting with MP and gives selected wavelet-decomposition
    examples. Fewer iterations do not imply universally lower cost: refitting adds
    work, and the conclusion’s speed expectation for highly redundant dictionaries
    is explicitly a conjecture. The selection score is residual correlation with the
    original unit atom, not the projected-atom-normalized gain used by other orthogonal
    selection rules. An external orthogonal-least-squares algorithm and its identity
    require separate primary-source assessment. Locators: Sections 2.1–4, Figures
    1–5 and conclusion, PDF pp. 3–5 / printed pp. 42–44'
- assessment_id: adversarial-projections
  area: consistency
  topic: Last-atom versus selected-span orthogonality
  outcome: supported
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  evidence_ids:
  - mallat1993
  - pati1993
  - certificates
  summary: The two algorithms are not duplicates.
  details: With b=(3/5,4/5) and y=e2, both first select b. MP subtracts e1 next and
    leaves (0,9/25), not orthogonal to b. OMP solves over both columns and changes
    the old coefficient from4/5to5/4, with newe1coefficient-3/4 and residual0. The
    optional finalMPbackprojection does not change the intervening greedy path. Orthogonal
    dictionary columns are not required.
- assessment_id: adversarial-optimality
  area: consistency
  topic: Selected-set least squares versus minimum support
  outcome: supported
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  evidence_ids:
  - pati1993
  - certificates
  summary: Conditional fitting optimality does not imply optimal subset selection.
  details: For unitdictionary[identity,b] withb=(8/9,4/9,1/9),y=e1-b, absolute first
    correlations selecte2; remainingidentityatoms tie and beatb. Lowest-index ties
    givee1thene3. OMPuses3atoms although a2-atom exactrepresentation exists; noncollinearity
    excludes1atom. In exactfinitearithmetic nonzero correlations add independentdirections,
    giving the stated rank bound, with residual outside dictionary span preserved.
- assessment_id: adversarial-source
  area: provenance
  topic: Printed inequalities and source versions
  outcome: supported
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  evidence_ids:
  - mallat1993
  - pati1993
  summary: Apparent source inconsistencies remain visible.
  details: OMPintroprints>=,algorithmStepIIprints>whileallowingalpha1. The latter
    is impossible at the supremum; the record uses the consistent non-strict finite-max
    convention without inventing an erratum. MPenergyEq17 supplies squarednormidentity
    despite Eq35printing. Ambiguous examplecounts are not numerical performance claims.1993journalMP
    and cited1992preprint remain distinct versions.
- assessment_id: all-fields
  area: provenance
  topic: Complete record and scope
  outcome: concern
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  evidence_ids:
  - identity
  - mapping
  - mallat1993
  - pati1993
  - certificates
  summary: Every maintained field was read after capture; one bounded evidence attribution
    requires correction.
  details: ReadID,label,aliases(ifpresent),kind,definition,identitynotes,definitionevidence,allclaims/locators,allsourceversions/access/hashes,mappingpin/relation/rationale,limitations,DRAFTstatus
    andactualUTCcuration. Sourcehashes and reportmirrors match. MPabbreviation is
    not an alias because it collides withMarkovChain. OMPalias matches its primarysource.463pendingand46partlyaddressedcohorts
    remain.
findings:
- finding_id: external-selection-attribution
  issue_key: aimech-omp-external-selection-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Bound the OMP selection-score comparison to inspected evidence
  description: The runtime-and-method-boundaries claim attributes projected-atom-normalized
    gain to other orthogonal selection rules, but its cited Pati1993passages establish
    only OMPrawcorrelation and projection energy. The external orthogonal-least-squares
    source is expressly pending. Replace the unaudited attribution with the algebraic
    distinction between rawcorrelation selection and the displayed projection-energy
    decrease, or inspect and cite the external method. This is bounded evidence wording,
    not a defect in OMPidentity or its equations.
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  field_paths:
  - claims[claim_id=runtime-and-method-boundaries].statement
  - entries[id=AIMech:OrthogonalMatchingPursuit].claims
  evidence_ids:
  - pati1993
  - certificates
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OrthogonalMatchingPursuit.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261012T121936Z-matching-pursuits.json
    role: discovery_report
- finding_id: uncited-source
  issue_key: aimech-omp-uncited-mallat-source
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Cite the MP contrast source in the OMP record
  description: The maintained OMP record lists Mallat1993 without a claim-level citation,
    and validate-curated rejects the uncited source. The runtime contrast actually
    concerns MP versus OMP; attach a precise Mallat locator to that supported contrast,
    or remove the unused source if it is not used.
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  field_paths:
  - evidence_sources[source_id=mallat1993]
  - claims[claim_id=runtime-and-method-boundaries].evidence
  evidence_ids:
  - mallat1993
  - pati1993
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OrthogonalMatchingPursuit.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261012T121936Z-matching-pursuits.json
    role: discovery_report
actions:
- action_id: narrow-selection-attribution
  description: Narrow the maintained claim and report mirror to the inspected OMP
    equations, preserve external OLS as pending, append edit history and save a successor
    disposition.
  finding_ids:
  - external-selection-attribution
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OrthogonalMatchingPursuit.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261012T121936Z-matching-pursuits.json
    role: discovery_report
  acceptance_checks:
  - Claim compares rawcorrelation with the source-derived normalized projection-energy
    decrease without attributing an unaudited external algorithm.
  - Report mirror and regenerated pages agree with the corrected YAML.
  - Required gates pass and successor review retains the stable issue key and predecessor
    target.
- action_id: cite-contrast-source
  description: Attach the inspected MP update and backprojection passages to the maintained
    MP-versus-OMP contrast and mirror the correction in the report.
  finding_ids:
  - uncited-source
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OrthogonalMatchingPursuit.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261012T121936Z-matching-pursuits.json
    role: discovery_report
  acceptance_checks:
  - Every listed evidence source is cited by a supported definition or claim.
  - Full validate-curated and just check pass.
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:OrthogonalMatchingPursuit
  evidence_ids:
  - identity
  - mapping
  - mallat1993
  - pati1993
  - certificates
  rationale: Single-atom MP and selected-span-refitting OMP differ on the explicit
    same-input example. Neither is the BPoptimizationprinciple, a learned dictionary,
    a neural architecture or a global subset optimizer.
limitations:
- Author self-review only; nativeDRAFTstatus remains.
- Two DRAFT algorithms added;527native and442unchangedAIOrecords.463pendingand46partlyaddressedcohorts
  plus other unresolved scopes mean discovery is ongoing.
- All24pages across the two1993primarypapers were visually read. The1992MPpreprint,
  external recovery results, orthogonal-least-squares and newsourcecohorts were not
  fully audited.
- No model training, empirical benchmark or author implementation was run. Exact rational
  counterexamples establish finite algebraic cases.
- Apparent source typography is explicitly preserved. DOIwebopens/IEEEbodyaccess failed;
  public Crossrefmetadata and actual inspected PDFs establish bibliographic identity.
- The OMPguide was read for Section1.1.9. Technicalreport2008abstract/openingtext
  is a lead, not a full method inspection.
related_reviews: []
links: []
tags:
- native-concepts
- matching-pursuit
- self-review
- discovery-ongoing
```
