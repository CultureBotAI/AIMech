# Scientific self-review of delayed, multiple-try and adaptive samplers

- Review: 20261011T073050Z-delayed-multiple-adaptive-sampling
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T07:28:37Z
- Finished UTC: 2026-10-11T07:30:50Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain six distinct algorithm identities and their qualified AIO related mappings. No actionable defect was found in the reviewed final records. Rejected paths, reference sets, conditional kernels, population anchors and adaptation remain explicit; all records stay DRAFT.

## Scope And Provenance

Six maintained delayed-rejection, multiple-try, population-optimization and robust adaptive sampling algorithms.

Selection: Exactly the six added IDs in the delayed-multiple-adaptive-sampling ledger; no sampling.
Coverage: full; 6 reviewed / 6 in the declared population.
Source: working_tree at Git base 224931eba7f9b047796ac30d130f8b754a03c9e6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:DelayedRejectionMetropolis | data/curated/DelayedRejectionMetropolis.yaml | maintained | Delayed-rejection Metropolis |
| AIMech:SymmetricDelayedRejection | data/curated/SymmetricDelayedRejection.yaml | maintained | Symmetric delayed rejection |
| AIMech:MultipleTryMetropolis | data/curated/MultipleTryMetropolis.yaml | maintained | Multiple-try Metropolis |
| AIMech:MultipleTryMetropolisWithinGibbs | data/curated/MultipleTryMetropolisWithinGibbs.yaml | maintained | Multiple-try Metropolis within Gibbs |
| AIMech:ConjugateGradientMonteCarlo | data/curated/ConjugateGradientMonteCarlo.yaml | maintained | Conjugate-gradient Monte Carlo |
| AIMech:RobustAdaptiveMetropolis | data/curated/RobustAdaptiveMetropolis.yaml | maintained | Robust adaptive Metropolis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:DelayedRejectionMetropolis, AIMech:SymmetricDelayedRejection, AIMech:MultipleTryMetropolis, AIMech:MultipleTryMetropolisWithinGibbs, AIMech:ConjugateGradientMonteCarlo, AIMech:RobustAdaptiveMetropolis | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 67.76s (0:01:07)<br>Checked 442 record(s); 0 failed.<br>Checked 181 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 35 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 35,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:DelayedRejectionMetropolis, AIMech:SymmetricDelayedRejection, AIMech:MultipleTryMetropolis, AIMech:MultipleTryMetropolisWithinGibbs, AIMech:ConjugateGradientMonteCarlo, AIMech:RobustAdaptiveMetropolis | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Identity, mechanism, limitations and mapping

evidence: supported. Targets: AIMech:DelayedRejectionMetropolis.

This is the path-reversal delayed-rejection construction in Mira Sections 2–3. Rejected internal candidates are auxiliary information; the chain remains at its original state until a candidate is accepted or the transition ends. It differs from across-iteration adaptive Metropolis and from independent repeated accept-reject generation. No normalized match was found across all 442 pinned AIO labels/scoped synonyms and 175 prior native IDs/names/aliases. Full-checkout searches included ignored and hidden files in both worktrees; the only text hit was an unrelated installed-package checksum substring. Existing general Metropolis-Hastings, Metropolis-within-Gibbs and random-walk records were inspected to resolve these specialization boundaries.

For current x with pi(x)&gt;0, propose y1 from q1(x,·) and use a1(x,y1)=min(1,pi(y1)q1(y1,x)/(pi(x)q1(x,y1))). If rejected, draw y2 from q2(x,y1,·). Accept y2 with min(1, [pi(y2)q1(y2,y1)q2(y2,y1,x)(1−a1(y2,y1))]/[pi(x)q1(x,y1)q2(x,y1,y2)(1−a1(x,y1))]). The zero reverse-path case has acceptance zero. A fixed two-stage implementation retains x if both tests reject. Higher stages require the corresponding reversed-path proposal and previous-rejection products; simply applying ordinary Metropolis to each retry omits those factors. Limitations: Proposal support and well-defined forward-path probabilities are required; formulas apply to reachable rejection paths. Irreducibility and convergence need further conditions beyond detailed balance. The record gives the explicit two-stage rule and identifies the higher-stage construction, not a claim that every history-dependent retry is valid. Extra stages cost proposal and target evaluations. Per-transition asymptotic-variance comparisons do not guarantee faster estimates per unit computation. A finite stage cap retains the original state after all rejections. Eventual acceptance is not guaranteed for unrestricted retry schemes.

### Identity, mechanism, limitations and mapping

evidence: supported. Targets: AIMech:SymmetricDelayedRejection.

This record is the fixed-kernel specialization in Mira Section 3. The next proposal depends on the last rejected point rather than being recentered on the unchanged chain state. Stage-dependent variances and generic symmetric proposals do not automatically satisfy the cancellations used by this simplified rule. No normalized match was found across all 442 pinned AIO labels/scoped synonyms and 175 prior native IDs/names/aliases. Full-checkout searches included ignored and hidden files in both worktrees; the only text hit was an unrelated installed-package checksum substring. Existing general Metropolis-Hastings, Metropolis-within-Gibbs and random-walk records were inspected to resolve these specialization boundaries.

Let q(a,b)=q(b,a) be the same kernel at every stage. Starting from x, propose y1 from q(x,·) and accept with min(1,pi(y1)/pi(x)). After i−1 rejections, propose yi from q(y(i−1),·), set M=max_{j&lt;i} pi(yj), and accept with min(1,max(0,(pi(yi)−M)/(pi(x)−M))). On a reachable rejection path, M&lt;pi(x). If a chosen finite stage limit is exhausted, retain x. Accepted candidates end the transition; rejected candidates do not become chain states. The formula follows cancellation of the forward and reverse path terms under the fixed symmetric-kernel assumption. Limitations: Figure 1 prints pi(x)/pi(y1) for its first-stage nontrivial acceptance region, reversing the correct pi(y1)/pi(x) in the preceding text. This record uses the text and general Metropolis formula; the figure discrepancy was visually inspected. The later suggestion to decrease variance by stage is not treated as permission to use this simplified acceptance with arbitrary changing q. Such proposals need the general delayed-rejection correction. A candidate whose target density is no larger than the maximum target density among previous rejected candidates is rejected. No finite-time eventual-acceptance or universal efficiency guarantee is asserted. Detailed balance is not a substitute for support, irreducibility and numerical-stability checks.

### Identity, mechanism, limitations and mapping

evidence: supported. Targets: AIMech:MultipleTryMetropolis.

This record covers Liu–Liang–Wong Section 2 finite-k MTM with one proposal kernel and a symmetric weight factor. It is not simple selection of the highest-density candidate, importance resampling without a correction, or the general auxiliary-variable extension in Section 3.1. No normalized match was found across all 442 pinned AIO labels/scoped synonyms and 175 prior native IDs/names/aliases. Full-checkout searches included ignored and hidden files in both worktrees; the only text hit was an unrelated installed-package checksum substring. Existing general Metropolis-Hastings, Metropolis-within-Gibbs and random-walk records were inspected to resolve these specialization boundaries.

Choose k≥1, a proposal T with T(a,b)&gt;0 iff T(b,a)&gt;0, and nonnegative symmetric lambda positive wherever T is positive. Define w(a,b)=pi(a)T(a,b)lambda(a,b). From current x, draw k independent yj from T(x,·), and select y with probabilities proportional to w(yj,x). Draw k−1 independent xj* from T(y,·), and append xk*=x. Accept y with min(1,sum_j w(yj,x)/sum_j w(xj*,y)); otherwise retain x. For k=1 the symmetric lambda cancels, recovering Metropolis-Hastings. Selection and the backward reference set are essential to this correction. Limitations: Weight sums must be finite and usable. If all forward candidates have zero target weight, the transition can be completed by retaining x; weighted selection is not performed with a zero denominator. The number of proposals and target evaluations grows with k. Larger k does not imply universal improvement per unit computation or independent retained draws. The auxiliary-variable extension in Section 3.1 prints selection weights with an argument order inconsistent with Section 2 and its own acceptance expression. That extension is not asserted by this record. Target invariance under the stated construction does not alone establish irreducibility or a mixing rate.

### Identity, mechanism, limitations and mapping

evidence: supported. Targets: AIMech:MultipleTryMetropolisWithinGibbs.

This is the MTM-Gibbs construction in Liu–Liang–Wong Section 5.2, a specific multiple-candidate Metropolis-within-Gibbs kernel. It need not draw exactly from a full conditional in one update and does not replace that conditional with a gridded interpolation. No normalized match was found across all 442 pinned AIO labels/scoped synonyms and 175 prior native IDs/names/aliases. Full-checkout searches included ignored and hidden files in both worktrees; the only text hit was an unrelated installed-package checksum substring. Existing general Metropolis-Hastings, Metropolis-within-Gibbs and random-walk records were inspected to resolve these specialization boundaries.

For a chosen coordinate i, fix x_−i and use the unnormalized scalar target pi_i(z)=pi(x_−i,z). Draw k independent yj from T(x_i,·), compute w(yj,x_i)=pi_i(yj)T(yj,x_i)lambda(yj,x_i), and select y in proportion to these weights. Draw k−1 reference values from T(y,·), append the old x_i, and accept using the forward-to-reference total-weight ratio of MTM. On acceptance replace only coordinate i; otherwise keep the full state. T may depend on the fixed remaining coordinates; its forward/reverse support and symmetric lambda requirements hold within that conditional update. Limitations: This is conditional target invariance, not an exact independent conditional draw or independence of successive full states. Use the complete backward-reference correction. Keeping only the weighted candidate selection defines a different procedure. Zero forward total weight is handled by retaining the current coordinate; finite, meaningful target/proposal weights are required. Support, coordinate scheduling and irreducibility determine whether the full chain can explore the target. No benchmark advantage over Gibbs or other conditional kernels is asserted.

### Identity, mechanism, limitations and mapping

evidence: supported. Targets: AIMech:ConjugateGradientMonteCarlo.

This is Liu–Liang–Wong Section 4.2 CGMC, not the conjugate-gradient linear solver or direct optimization as a substitute for sampling. Its anchor comes from a different stream. The product target is an invariant population law, not a statement that transient streams are independent. No normalized match was found across all 442 pinned AIO labels/scoped synonyms and 175 prior native IDs/names/aliases. Full-checkout searches included ignored and hidden files in both worktrees; the only text hit was an unrelated installed-package checksum substring. Existing general Metropolis-Hastings, Metropolis-within-Gibbs and random-walk records were inspected to resolve these specialization boundaries.

Maintain m≥2 population members targeting a product of pi. Choose a reference member x_r uniformly at random, and deterministically optimize along a gradient or conjugate-gradient direction of log pi to obtain anchor A=g(x_r). Choose x_c uniformly among the other members. For A≠x_c, define e=(A−x_c)/&#124;&#124;A−x_c&#124;&#124; and the scalar line target f(r) proportional to &#124;r&#124;^(d−1)pi(A+r e), r on the whole real line. Apply a valid MTM transition along this line, starting at the scalar coordinate of x_c, and replace x_c by A+r_new e while retaining the other members. A scalar proposal and weight construction must respect the same unoriented line when traversed in reverse; a centered Gaussian scalar random-walk proposal of fixed variance with MTM-II target-density selection weights is a concrete compatible choice. The source’s product-invariance argument uses the anchor’s independence from the moved member under the product target. Limitations: The factor &#124;r&#124;^(d−1) is essential for an anchor line selected through the current point. Replacing the line target with pi(A+r e) alone is not this construction. The optimization anchor must be independent of the moved member under the product stationary law. Optimizing that same member and copying this acceptance scheme is not justified. The zero-length line A=x_c requires a defined degenerate-case policy; the displayed normalized direction is not evaluated at zero. Differentiability and the chosen deterministic optimization procedure have their own requirements. The compatible scalar-proposal statement is an explicit implementation constraint inferred from reversing the unoriented line, not a new algorithm attributed to the source. Invariance does not guarantee population exploration, convergence, independent transient streams or universally reliable convergence diagnostics. Optimization and multiple trials add cost.

### Identity, mechanism, limitations and mapping

evidence: supported. Targets: AIMech:RobustAdaptiveMetropolis.

This is Vihola’s RAM update, which avoids estimating the target covariance. It differs from covariance-based adaptive Metropolis, scale-only adaptation and a fixed random-walk kernel. RAM here denotes this sampler, not computer memory. The history-dependent state sequence is not assumed to be a homogeneous Markov chain. No normalized match was found across all 442 pinned AIO labels/scoped synonyms and 175 prior native IDs/names/aliases. Full-checkout searches included ignored and hidden files in both worktrees; the only text hit was an unrelated installed-package checksum substring. Existing general Metropolis-Hastings, Metropolis-within-Gibbs and random-walk records were inspected to resolve these specialization boundaries.

Let q be a spherical density, S a lower-triangular factor with positive diagonal, x satisfy pi(x)&gt;0, eta_n lie in (0,1] and decay to zero, and alpha_star lie in (0,1). Draw U from q and propose y=x+S U. Set alpha=min(1,pi(y)/pi(x)), accept y with this probability or retain x. Whether accepted or rejected, choose the next positive-diagonal Cholesky factor S_new satisfying S_new S_new^T=S[I+eta_n(alpha−alpha_star)UU^T/&#124;&#124;U&#124;&#124;²]S^T. The update uses the acceptance probability, not the binary acceptance outcome; the normalized direction U determines the rank-one adjustment. It expands that component when alpha exceeds the target and contracts it when alpha is smaller. Limitations: Spherical continuous proposals make U=0 a null event; numerical implementations still need a zero-norm guard and stable factor updates. Positive definiteness of each update does not prove long-run stability. The source’s strong-law result assumes target/proposal regularity and step-size conditions and holds on an event where shape eigenvalues stay bounded away from zero and infinity. The paper explicitly leaves unrestricted stability unproved. Enforcing fixed eigenvalue bounds by rejecting a proposed shape update is a separate safeguard that can alter the limiting shape. A chosen acceptance rate is a tuning target, not a universal optimum or convergence diagnostic. Strong multimodality can remain difficult; no benchmark or arbitrary-heavy-tail convergence guarantee is asserted. The exact inspected arXiv v2 bytes have a later title-page footer date. This record does not claim to have inspected the later journal version.

### General and fixed symmetric delayed rejection

scope: supported. Targets: AIMech:DelayedRejectionMetropolis, AIMech:SymmetricDelayedRejection.

Retain the general path-corrected procedure and its explicitly fixed symmetric-kernel specialization.

Revisited Mira Equation (2) and maximum-density Equation (8) visually. The second-stage numerator includes reverse q1, reverse q2 and the reverse rejection probability; denominator uses the actually traversed forward path. The simplified rule uses the same symmetric q through the last rejected candidate. Figure 1 reverses the first acceptance ratio relative to the text; the record documents this and uses the consistent text. Stage-dependent variances cannot be silently substituted into the simplified rule. Capping stages leaves residual rejection mass at the original state.

### Candidate selection, reverse reference sets and conditional specialization

scope: supported. Targets: AIMech:MultipleTryMetropolis, AIMech:MultipleTryMetropolisWithinGibbs.

Retain core MTM and MTM-Gibbs as distinct general and coordinate-update procedures.

Visually rechecked Section 2 and Section 5.2. w(a,b)=pi(a)T(a,b)lambda(a,b), selection uses w(y_j,x), and the backward set contains the old x. With k=1 symmetric lambda cancels to the ordinary MH ratio. The zero-weight retention caveat is a boundary completion of the displayed weighted-selection rule. The conditional specialization holds the rest fixed and preserves that conditional without independently drawing it. The inconsistent auxiliary-variable weight order in Section 3.1 is documented and excluded from the asserted extension scope.

### Optimization anchors, radial Jacobian and population invariance

scope: supported. Targets: AIMech:ConjugateGradientMonteCarlo.

CGMC combines an anchor computed from a different population member with a properly adjusted line transition.

Visually revisited steps 1–3, Equation (11), Theorem 2 and Lemma 1. Under the product stationary law the reference member and the moved member are independent, allowing A=g(x_r). The line target includes &#124;r&#124;^(d−1), and changing line orientation must leave the scalar transition compatible. The record labels this compatibility statement as an implementation inference and gives a reflection-compatible Gaussian random-walk/MTM-II choice. A uniform state-independent choice of distinct members is explicit. No assertion of independent transient streams or universal convergence is made.

### RAM probability-driven shape adaptation and conditional strong law

scope: supported. Targets: AIMech:RobustAdaptiveMetropolis.

The RAM record preserves both the exact rank-one update and the limits of its validity analysis.

Visually revisited R1–R3 and Theorem 17/Remark 19. Adaptation uses alpha rather than an acceptance indicator and occurs after either outcome. The rank-one factor remains positive definite for eta in (0,1] and alpha_star in (0,1), but this does not bound the infinite sequence of shapes. The strong law is conditional on target/proposal and step-size assumptions and the eigenvalue stability event. The mapping explicitly refers to the fixed-shape kernels being adapted, not an unsupported homogeneous Markov claim for the sampled-state history. The version and later PDF footer are both preserved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:DelayedRejectionMetropolis, AIMech:SymmetricDelayedRejection, AIMech:MultipleTryMetropolis, AIMech:MultipleTryMetropolisWithinGibbs, AIMech:ConjugateGradientMonteCarlo, AIMech:RobustAdaptiveMetropolis. Preserve the general delayed-rejection rule and its fixed symmetric specialization, core MTM and its conditional-coordinate specialization, population optimization anchors with a radial line target, and probability-driven RAM adaptation. Their different state, candidate and adaptation constructions justify distinct scopes. Related AIO mappings preserve algorithm-to-process differences, including the non-homogeneous adaptive history caveat.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T072809Z-delayed-multiple-adaptive-sampling.json | supports | No normalized match among 442 AIO labels/scoped synonyms and 175 native IDs/names/aliases. Both full checkout searches included ignored/hidden files. The discovery checkout had no hits; main had one unrelated checksum substring in an installed sphinxcontrib package RECORD, inspected and excluded. Existing Metropolis-Hastings, Metropolis-within-Gibbs and random-walk YAMLs were read to distinguish general kernels from these specialized algorithms. |
| mapping | sources/aio/aio.json; Exact MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction CLASS nodes and incident edges | supports | All six receive related_match to AIO:MarkovChain. Its exact node, scoped synonyms, Network parent and hidden-layer edge were inspected, alongside BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction definitions/edges. These algorithms are not network subclasses. RAM explicitly maps through the fixed-shape kernels it adapts; its sampled-state history is not asserted homogeneous Markov. CGMC uses the population state. No source pin or generated record changes. |
| existing-samplers | data/curated/MetropolisHastings.yaml; Definition, identity and mechanism; also MetropolisWithinGibbs and RandomWalkMetropolisHastings YAMLs | supports | The existing records describe general Metropolis correction, conditional invariant transitions and fixed additive proposals. The new methods specialize rejected-path correction, finite candidate/reference sets, population anchor lines or history-dependent shape adaptation. Shared Metropolis components do not establish equivalence. |
| delayedrejectionmetropolis-source | https://www.dss.uniroma1.it/RePec/mtn/articoli/2001-LIX-3_4-16.pdf; Section 2, Equations (1)–(4), printed pp. 232–234 / PDF pp. 2–4; Section 4, pp. 238–240 / PDF pp. 8–10 | supports | A Metropolis-Hastings sampling procedure that can propose another candidate after rejection within the same transition, correcting acceptance for the probabilities of the forward and reversed rejected paths. Version: Metron LIX (3–4), 2001, pp. 231–241; eleven-page publisher PDF. Read text/OCR pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11. Actually viewed image pages: 3, 6, 7. MTM text is OCR-assisted; no numerical benchmark claims are assessed. |
| symmetricdelayedrejection-source | https://www.dss.uniroma1.it/RePec/mtn/articoli/2001-LIX-3_4-16.pdf; Section 3, displayed fixed-kernel assumption and Equations (6)–(9), printed pp. 234–236 / PDF pp. 4–6; Figure 1 and continuation discussion, pp. 237–238 / PDF pp. 7–8 | supports | The delayed-rejection specialization using the same symmetric proposal kernel at every stage, centered through the last rejected candidate, with acceptance determined by the largest previous rejected target density. Version: Metron LIX (3–4), 2001, pp. 231–241; eleven-page publisher PDF. Read text/OCR pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11. Actually viewed image pages: 3, 6, 7. MTM text is OCR-assisted; no numerical benchmark claims are assessed. |
| multipletrymetropolis-source | https://www.stat.purdue.edu/~fmliang/papers/2000/Mtry.pdf; Section 2, Equations (2)–(5), numbered algorithm and Theorem 1, printed p. 122 / PDF p. 2; Section 7 discussion, p. 133 / PDF p. 13; Section 3.1 weight-order discrepancy, p. 123 / PDF p. 3 | supports | A Metropolis sampling algorithm that selects a candidate from several weighted forward proposals, draws a backward reference set containing the original state, and corrects acceptance using the ratio of their total weights. Version: Journal of the American Statistical Association 95(449), 2000, pp. 121–134; fourteen-page author-hosted published scan. Read text/OCR pages: 2, 3, 4, 5, 6, 13, 14. Actually viewed image pages: 1, 2, 3, 4, 5, 6. MTM text is OCR-assisted; no numerical benchmark claims are assessed. |
| multipletrymetropoliswithingibbs-source | https://www.stat.purdue.edu/~fmliang/papers/2000/Mtry.pdf; Section 5.2, MTM-Gibbs steps 1–3, printed p. 126 / PDF p. 6, with Section 2 Equation (3), p. 122 / PDF p. 2 | supports | A coordinate-update sampler that applies a multiple-try Metropolis transition to a conditional target while holding all other coordinates fixed. Version: Journal of the American Statistical Association 95(449), 2000, pp. 121–134; fourteen-page author-hosted published scan. Read text/OCR pages: 2, 3, 4, 5, 6, 13, 14. Actually viewed image pages: 1, 2, 3, 4, 5, 6. MTM text is OCR-assisted; no numerical benchmark claims are assessed. |
| conjugategradientmontecarlo-source | https://www.stat.purdue.edu/~fmliang/papers/2000/Mtry.pdf; Sections 4.1–4.2, CGMC steps 1–3, Equation (11), Theorem 2 and Lemma 1, printed pp. 124–125 / PDF pp. 4–5; population diagnostic caveat and discussion, p. 133 / PDF p. 13; Section 2 MTM-II choice, p. 122 / PDF p. 2 | supports | A population Markov sampler that obtains a local-optimization anchor from one population member and updates another member along the anchor line with a multiple-try transition targeting a radial-Jacobian-adjusted density. Version: Journal of the American Statistical Association 95(449), 2000, pp. 121–134; fourteen-page author-hosted published scan. Read text/OCR pages: 2, 3, 4, 5, 6, 13, 14. Actually viewed image pages: 1, 2, 3, 4, 5, 6. MTM text is OCR-assisted; no numerical benchmark claims are assessed. |
| robustadaptivemetropolis-source | https://arxiv.org/pdf/1011.4381v2; Section 2, steps R1–R3 and Equation (1), Proposition 1 and Remarks 2–4, PDF pp. 3–5; Section 4, Assumptions 12–16, Theorem 17 and Remark 19, pp. 11–13; Section 6, pp. 16–17 | supports | An adaptive random-walk Metropolis algorithm that updates the proposal shape factor by a rank-one transformation driven by the proposal direction and the difference between its acceptance probability and a chosen target rate. Version: arXiv:1011.4381v2, submitted 2011-05-27; 21-page PDF with title-page footer dated 2018-10-23; inspected bytes identified by hash. Read text/OCR pages: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17. Actually viewed image pages: 3, 12. MTM text is OCR-assisted; no numerical benchmark claims are assessed. |

## Limits And Additional Notes

- Adversarial author self-review only; all six records remain DRAFT.
- Only declared source text/OCR and image pages were read. No full visual inspection of every page is claimed.
- Source formula inconsistencies are recorded; no separate published erratum is asserted.
- The CGMC line-reversal compatibility example and zero-weight retention completion are explicitly interpreted from the verified core kernels.
- AM/DRAM original-method access and auxiliary MTM discrepancies remain research work, not resolved concepts.
- No numerical experiment, implementation reproduction or universal performance claim is included.
- All required repository and immutable-vendor checks passed; six positive discoveries do not establish saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T073050Z-delayed-multiple-adaptive-sampling
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of delayed, multiple-try and adaptive samplers
started_at: '2026-10-11T07:28:37Z'
finished_at: '2026-10-11T07:30:50Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all six actual YAMLs
    against primary method equations, assumptions, source discrepancies, neighboring
    native records and exact AIO mappings. Key Mira, MTM, CGMC and RAM pages were
    visually revisited. No independent reviewer or approval is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain six distinct algorithm identities and their qualified AIO related
  mappings. No actionable defect was found in the reviewed final records. Rejected
  paths, reference sets, conditional kernels, population anchors and adaptation remain
  explicit; all records stay DRAFT.
source:
  git_revision: 224931eba7f9b047796ac30d130f8b754a03c9e6
  state: working_tree
  inputs:
  - path: data/curated/ConjugateGradientMonteCarlo.yaml
    sha256: 59c29605048365b38ef298fdd3401bf00a8beb522fc9d4b3c8fe868d6946fa4f
    role: target
  - path: data/curated/DelayedRejectionMetropolis.yaml
    sha256: c6a2c94f7bde235ed1a79ff91fbf615920ff3d5710c1e6f90769648ad403c8cd
    role: target
  - path: data/curated/MetropolisHastings.yaml
    sha256: 01cb22a25242e8564e2a7bb839ecb46da1bc49eb09b3c85200f9a596e05b99b4
    role: context
  - path: data/curated/MetropolisWithinGibbs.yaml
    sha256: 0e9cfedc93c7e46cc6316809d5a9ec9488b33891a9c9862f914a0adf8f7cb140
    role: context
  - path: data/curated/MultipleTryMetropolis.yaml
    sha256: f1d607b598a1baf993a7b4de78e82953fd86a9bb9d367e02553aeda4fe2e354b
    role: target
  - path: data/curated/MultipleTryMetropolisWithinGibbs.yaml
    sha256: 539c4d93eff27f5e064abb16fe3e892406ad5dc3d3a6bceb314f4eee37b2a727
    role: target
  - path: data/curated/RandomWalkMetropolisHastings.yaml
    sha256: aeff822517db546b4e3dee3421a54d5887ed178f3b9e6e3df46283eceb39677d
    role: context
  - path: data/curated/RobustAdaptiveMetropolis.yaml
    sha256: 5f0feccd0c8d7eda90fabacbc27e1a98cf2582e865081190bb1c3955d4db04f4
    role: target
  - path: data/curated/SymmetricDelayedRejection.yaml
    sha256: e4cb88db36220fe96e697d8b3d42bbdb34e27f8a9a5886a901d299686e389281
    role: target
  - path: research/discovery/20261011T072809Z-delayed-multiple-adaptive-sampling.json
    sha256: f7eb519c98799c02ec01160c5c6dd2496b207118231609b9d219849694f4db73
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
- target_id: AIMech:DelayedRejectionMetropolis
  path: data/curated/DelayedRejectionMetropolis.yaml
  label: Delayed-rejection Metropolis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DelayedRejectionMetropolis.yaml
    role: maintained_record
- target_id: AIMech:SymmetricDelayedRejection
  path: data/curated/SymmetricDelayedRejection.yaml
  label: Symmetric delayed rejection
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SymmetricDelayedRejection.yaml
    role: maintained_record
- target_id: AIMech:MultipleTryMetropolis
  path: data/curated/MultipleTryMetropolis.yaml
  label: Multiple-try Metropolis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MultipleTryMetropolis.yaml
    role: maintained_record
- target_id: AIMech:MultipleTryMetropolisWithinGibbs
  path: data/curated/MultipleTryMetropolisWithinGibbs.yaml
  label: Multiple-try Metropolis within Gibbs
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MultipleTryMetropolisWithinGibbs.yaml
    role: maintained_record
- target_id: AIMech:ConjugateGradientMonteCarlo
  path: data/curated/ConjugateGradientMonteCarlo.yaml
  label: Conjugate-gradient Monte Carlo
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ConjugateGradientMonteCarlo.yaml
    role: maintained_record
- target_id: AIMech:RobustAdaptiveMetropolis
  path: data/curated/RobustAdaptiveMetropolis.yaml
  label: Robust adaptive Metropolis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RobustAdaptiveMetropolis.yaml
    role: maintained_record
scope:
  description: Six maintained delayed-rejection, multiple-try, population-optimization
    and robust adaptive sampling algorithms.
  selection: Exactly the six added IDs in the delayed-multiple-adaptive-sampling ledger;
    no sampling.
  coverage: full
  population_size: 6
  reviewed_target_ids:
  - AIMech:DelayedRejectionMetropolis
  - AIMech:SymmetricDelayedRejection
  - AIMech:MultipleTryMetropolis
  - AIMech:MultipleTryMetropolisWithinGibbs
  - AIMech:ConjugateGradientMonteCarlo
  - AIMech:RobustAdaptiveMetropolis
  exclusions:
  - target: AM, DRAM, auxiliary-variable MTM, random-ray and original adaptive direction
      algorithms
    reason: Full visual method inspection or source discrepancy resolution remains
      incomplete. These candidates remain in the frontier.
  - target: Sampler execution and benchmark reproduction
    reason: No sampler or numerical experiment was run.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:DelayedRejectionMetropolis
  - AIMech:SymmetricDelayedRejection
  - AIMech:MultipleTryMetropolis
  - AIMech:MultipleTryMetropolisWithinGibbs
  - AIMech:ConjugateGradientMonteCarlo
  - AIMech:RobustAdaptiveMetropolis
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 67.76s (0:01:07)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 181 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 35 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 35,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:DelayedRejectionMetropolis
  - AIMech:SymmetricDelayedRejection
  - AIMech:MultipleTryMetropolis
  - AIMech:MultipleTryMetropolisWithinGibbs
  - AIMech:ConjugateGradientMonteCarlo
  - AIMech:RobustAdaptiveMetropolis
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T072809Z-delayed-multiple-adaptive-sampling.json
  accessed_at: '2026-10-11T07:28:37Z'
  support: supports
  summary: No normalized match among 442 AIO labels/scoped synonyms and 175 native
    IDs/names/aliases. Both full checkout searches included ignored/hidden files.
    The discovery checkout had no hits; main had one unrelated checksum substring
    in an installed sphinxcontrib package RECORD, inspected and excluded. Existing
    Metropolis-Hastings, Metropolis-within-Gibbs and random-walk YAMLs were read to
    distinguish general kernels from these specialized algorithms.
  search_scope: All 442 AIO labels/scoped synonyms and 175 preceding native IDs/names/aliases;
    both full checkouts include ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-11T07:28:37Z'
  support: supports
  locator: Exact MarkovChain, BayesianNetwork, ProbabilisticGraphicalModel and MathematicalFunction
    CLASS nodes and incident edges
  summary: All six receive related_match to AIO:MarkovChain. Its exact node, scoped
    synonyms, Network parent and hidden-layer edge were inspected, alongside BayesianNetwork,
    ProbabilisticGraphicalModel and MathematicalFunction definitions/edges. These
    algorithms are not network subclasses. RAM explicitly maps through the fixed-shape
    kernels it adapts; its sampled-state history is not asserted homogeneous Markov.
    CGMC uses the population state. No source pin or generated record changes.
- evidence_id: existing-samplers
  kind: record_content
  reference: data/curated/MetropolisHastings.yaml
  accessed_at: '2026-10-11T07:28:37Z'
  support: supports
  locator: Definition, identity and mechanism; also MetropolisWithinGibbs and RandomWalkMetropolisHastings
    YAMLs
  summary: The existing records describe general Metropolis correction, conditional
    invariant transitions and fixed additive proposals. The new methods specialize
    rejected-path correction, finite candidate/reference sets, population anchor lines
    or history-dependent shape adaptation. Shared Metropolis components do not establish
    equivalence.
- evidence_id: delayedrejectionmetropolis-source
  kind: primary_source
  reference: https://www.dss.uniroma1.it/RePec/mtn/articoli/2001-LIX-3_4-16.pdf
  locator: Section 2, Equations (1)–(4), printed pp. 232–234 / PDF pp. 2–4; Section
    4, pp. 238–240 / PDF pp. 8–10
  accessed_at: '2026-10-11T07:18:11Z'
  snapshot_sha256: cd857ff8d7f74887797c2959ddc626ea30cdf2eadad4756c781bce91776e01ff
  support: supports
  summary: 'A Metropolis-Hastings sampling procedure that can propose another candidate
    after rejection within the same transition, correcting acceptance for the probabilities
    of the forward and reversed rejected paths. Version: Metron LIX (3–4), 2001, pp.
    231–241; eleven-page publisher PDF. Read text/OCR pages: 1, 2, 3, 4, 5, 6, 7,
    8, 9, 10, 11. Actually viewed image pages: 3, 6, 7. MTM text is OCR-assisted;
    no numerical benchmark claims are assessed.'
- evidence_id: symmetricdelayedrejection-source
  kind: primary_source
  reference: https://www.dss.uniroma1.it/RePec/mtn/articoli/2001-LIX-3_4-16.pdf
  locator: Section 3, displayed fixed-kernel assumption and Equations (6)–(9), printed
    pp. 234–236 / PDF pp. 4–6; Figure 1 and continuation discussion, pp. 237–238 /
    PDF pp. 7–8
  accessed_at: '2026-10-11T07:18:11Z'
  snapshot_sha256: cd857ff8d7f74887797c2959ddc626ea30cdf2eadad4756c781bce91776e01ff
  support: supports
  summary: 'The delayed-rejection specialization using the same symmetric proposal
    kernel at every stage, centered through the last rejected candidate, with acceptance
    determined by the largest previous rejected target density. Version: Metron LIX
    (3–4), 2001, pp. 231–241; eleven-page publisher PDF. Read text/OCR pages: 1, 2,
    3, 4, 5, 6, 7, 8, 9, 10, 11. Actually viewed image pages: 3, 6, 7. MTM text is
    OCR-assisted; no numerical benchmark claims are assessed.'
- evidence_id: multipletrymetropolis-source
  kind: primary_source
  reference: https://www.stat.purdue.edu/~fmliang/papers/2000/Mtry.pdf
  locator: Section 2, Equations (2)–(5), numbered algorithm and Theorem 1, printed
    p. 122 / PDF p. 2; Section 7 discussion, p. 133 / PDF p. 13; Section 3.1 weight-order
    discrepancy, p. 123 / PDF p. 3
  accessed_at: '2026-10-11T07:17:23Z'
  snapshot_sha256: 5329c50b3760ba8ae6eafcec205ae0e62ab42c56f4a63d0609162c86cf065cdb
  support: supports
  summary: 'A Metropolis sampling algorithm that selects a candidate from several
    weighted forward proposals, draws a backward reference set containing the original
    state, and corrects acceptance using the ratio of their total weights. Version:
    Journal of the American Statistical Association 95(449), 2000, pp. 121–134; fourteen-page
    author-hosted published scan. Read text/OCR pages: 2, 3, 4, 5, 6, 13, 14. Actually
    viewed image pages: 1, 2, 3, 4, 5, 6. MTM text is OCR-assisted; no numerical benchmark
    claims are assessed.'
- evidence_id: multipletrymetropoliswithingibbs-source
  kind: primary_source
  reference: https://www.stat.purdue.edu/~fmliang/papers/2000/Mtry.pdf
  locator: Section 5.2, MTM-Gibbs steps 1–3, printed p. 126 / PDF p. 6, with Section
    2 Equation (3), p. 122 / PDF p. 2
  accessed_at: '2026-10-11T07:17:23Z'
  snapshot_sha256: 5329c50b3760ba8ae6eafcec205ae0e62ab42c56f4a63d0609162c86cf065cdb
  support: supports
  summary: 'A coordinate-update sampler that applies a multiple-try Metropolis transition
    to a conditional target while holding all other coordinates fixed. Version: Journal
    of the American Statistical Association 95(449), 2000, pp. 121–134; fourteen-page
    author-hosted published scan. Read text/OCR pages: 2, 3, 4, 5, 6, 13, 14. Actually
    viewed image pages: 1, 2, 3, 4, 5, 6. MTM text is OCR-assisted; no numerical benchmark
    claims are assessed.'
- evidence_id: conjugategradientmontecarlo-source
  kind: primary_source
  reference: https://www.stat.purdue.edu/~fmliang/papers/2000/Mtry.pdf
  locator: Sections 4.1–4.2, CGMC steps 1–3, Equation (11), Theorem 2 and Lemma 1,
    printed pp. 124–125 / PDF pp. 4–5; population diagnostic caveat and discussion,
    p. 133 / PDF p. 13; Section 2 MTM-II choice, p. 122 / PDF p. 2
  accessed_at: '2026-10-11T07:17:23Z'
  snapshot_sha256: 5329c50b3760ba8ae6eafcec205ae0e62ab42c56f4a63d0609162c86cf065cdb
  support: supports
  summary: 'A population Markov sampler that obtains a local-optimization anchor from
    one population member and updates another member along the anchor line with a
    multiple-try transition targeting a radial-Jacobian-adjusted density. Version:
    Journal of the American Statistical Association 95(449), 2000, pp. 121–134; fourteen-page
    author-hosted published scan. Read text/OCR pages: 2, 3, 4, 5, 6, 13, 14. Actually
    viewed image pages: 1, 2, 3, 4, 5, 6. MTM text is OCR-assisted; no numerical benchmark
    claims are assessed.'
- evidence_id: robustadaptivemetropolis-source
  kind: primary_source
  reference: https://arxiv.org/pdf/1011.4381v2
  locator: Section 2, steps R1–R3 and Equation (1), Proposition 1 and Remarks 2–4,
    PDF pp. 3–5; Section 4, Assumptions 12–16, Theorem 17 and Remark 19, pp. 11–13;
    Section 6, pp. 16–17
  accessed_at: '2026-10-11T07:17:23Z'
  snapshot_sha256: dc508f247e17005930079c2fefc789f936b9217eb7038de48d96195c2c170a93
  support: supports
  summary: 'An adaptive random-walk Metropolis algorithm that updates the proposal
    shape factor by a rank-one transformation driven by the proposal direction and
    the difference between its acceptance probability and a chosen target rate. Version:
    arXiv:1011.4381v2, submitted 2011-05-27; 21-page PDF with title-page footer dated
    2018-10-23; inspected bytes identified by hash. Read text/OCR pages: 1, 2, 3,
    4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17. Actually viewed image pages: 3, 12.
    MTM text is OCR-assisted; no numerical benchmark claims are assessed.'
assessments:
- assessment_id: delayedrejectionmetropolis
  area: evidence
  topic: Identity, mechanism, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:DelayedRejectionMetropolis
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - delayedrejectionmetropolis-source
  summary: This is the path-reversal delayed-rejection construction in Mira Sections
    2–3. Rejected internal candidates are auxiliary information; the chain remains
    at its original state until a candidate is accepted or the transition ends. It
    differs from across-iteration adaptive Metropolis and from independent repeated
    accept-reject generation. No normalized match was found across all 442 pinned
    AIO labels/scoped synonyms and 175 prior native IDs/names/aliases. Full-checkout
    searches included ignored and hidden files in both worktrees; the only text hit
    was an unrelated installed-package checksum substring. Existing general Metropolis-Hastings,
    Metropolis-within-Gibbs and random-walk records were inspected to resolve these
    specialization boundaries.
  details: 'For current x with pi(x)>0, propose y1 from q1(x,·) and use a1(x,y1)=min(1,pi(y1)q1(y1,x)/(pi(x)q1(x,y1))).
    If rejected, draw y2 from q2(x,y1,·). Accept y2 with min(1, [pi(y2)q1(y2,y1)q2(y2,y1,x)(1−a1(y2,y1))]/[pi(x)q1(x,y1)q2(x,y1,y2)(1−a1(x,y1))]).
    The zero reverse-path case has acceptance zero. A fixed two-stage implementation
    retains x if both tests reject. Higher stages require the corresponding reversed-path
    proposal and previous-rejection products; simply applying ordinary Metropolis
    to each retry omits those factors. Limitations: Proposal support and well-defined
    forward-path probabilities are required; formulas apply to reachable rejection
    paths. Irreducibility and convergence need further conditions beyond detailed
    balance. The record gives the explicit two-stage rule and identifies the higher-stage
    construction, not a claim that every history-dependent retry is valid. Extra stages
    cost proposal and target evaluations. Per-transition asymptotic-variance comparisons
    do not guarantee faster estimates per unit computation. A finite stage cap retains
    the original state after all rejections. Eventual acceptance is not guaranteed
    for unrestricted retry schemes.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined sampling or adaptation procedure; not a trained model, graphical
      probability model or benchmark result.
    evidence_ids:
    - delayedrejectionmetropolis-source
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The procedure defines target-invariant Markov transitions under its
      stated assumptions. AIO MarkovChain describes a stochastic process/model and
      is exported beneath Network. This method-to-process related match is not equivalence,
      an is-a assertion or a claim of independent samples or a trained network.
    evidence_ids:
    - identity
    - mapping
- assessment_id: symmetricdelayedrejection
  area: evidence
  topic: Identity, mechanism, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:SymmetricDelayedRejection
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - symmetricdelayedrejection-source
  summary: This record is the fixed-kernel specialization in Mira Section 3. The next
    proposal depends on the last rejected point rather than being recentered on the
    unchanged chain state. Stage-dependent variances and generic symmetric proposals
    do not automatically satisfy the cancellations used by this simplified rule. No
    normalized match was found across all 442 pinned AIO labels/scoped synonyms and
    175 prior native IDs/names/aliases. Full-checkout searches included ignored and
    hidden files in both worktrees; the only text hit was an unrelated installed-package
    checksum substring. Existing general Metropolis-Hastings, Metropolis-within-Gibbs
    and random-walk records were inspected to resolve these specialization boundaries.
  details: 'Let q(a,b)=q(b,a) be the same kernel at every stage. Starting from x,
    propose y1 from q(x,·) and accept with min(1,pi(y1)/pi(x)). After i−1 rejections,
    propose yi from q(y(i−1),·), set M=max_{j<i} pi(yj), and accept with min(1,max(0,(pi(yi)−M)/(pi(x)−M))).
    On a reachable rejection path, M<pi(x). If a chosen finite stage limit is exhausted,
    retain x. Accepted candidates end the transition; rejected candidates do not become
    chain states. The formula follows cancellation of the forward and reverse path
    terms under the fixed symmetric-kernel assumption. Limitations: Figure 1 prints
    pi(x)/pi(y1) for its first-stage nontrivial acceptance region, reversing the correct
    pi(y1)/pi(x) in the preceding text. This record uses the text and general Metropolis
    formula; the figure discrepancy was visually inspected. The later suggestion to
    decrease variance by stage is not treated as permission to use this simplified
    acceptance with arbitrary changing q. Such proposals need the general delayed-rejection
    correction. A candidate whose target density is no larger than the maximum target
    density among previous rejected candidates is rejected. No finite-time eventual-acceptance
    or universal efficiency guarantee is asserted. Detailed balance is not a substitute
    for support, irreducibility and numerical-stability checks.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined sampling or adaptation procedure; not a trained model, graphical
      probability model or benchmark result.
    evidence_ids:
    - symmetricdelayedrejection-source
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The procedure defines target-invariant Markov transitions under its
      stated assumptions. AIO MarkovChain describes a stochastic process/model and
      is exported beneath Network. This method-to-process related match is not equivalence,
      an is-a assertion or a claim of independent samples or a trained network.
    evidence_ids:
    - identity
    - mapping
- assessment_id: multipletrymetropolis
  area: evidence
  topic: Identity, mechanism, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:MultipleTryMetropolis
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - multipletrymetropolis-source
  summary: This record covers Liu–Liang–Wong Section 2 finite-k MTM with one proposal
    kernel and a symmetric weight factor. It is not simple selection of the highest-density
    candidate, importance resampling without a correction, or the general auxiliary-variable
    extension in Section 3.1. No normalized match was found across all 442 pinned
    AIO labels/scoped synonyms and 175 prior native IDs/names/aliases. Full-checkout
    searches included ignored and hidden files in both worktrees; the only text hit
    was an unrelated installed-package checksum substring. Existing general Metropolis-Hastings,
    Metropolis-within-Gibbs and random-walk records were inspected to resolve these
    specialization boundaries.
  details: 'Choose k≥1, a proposal T with T(a,b)>0 iff T(b,a)>0, and nonnegative symmetric
    lambda positive wherever T is positive. Define w(a,b)=pi(a)T(a,b)lambda(a,b).
    From current x, draw k independent yj from T(x,·), and select y with probabilities
    proportional to w(yj,x). Draw k−1 independent xj* from T(y,·), and append xk*=x.
    Accept y with min(1,sum_j w(yj,x)/sum_j w(xj*,y)); otherwise retain x. For k=1
    the symmetric lambda cancels, recovering Metropolis-Hastings. Selection and the
    backward reference set are essential to this correction. Limitations: Weight sums
    must be finite and usable. If all forward candidates have zero target weight,
    the transition can be completed by retaining x; weighted selection is not performed
    with a zero denominator. The number of proposals and target evaluations grows
    with k. Larger k does not imply universal improvement per unit computation or
    independent retained draws. The auxiliary-variable extension in Section 3.1 prints
    selection weights with an argument order inconsistent with Section 2 and its own
    acceptance expression. That extension is not asserted by this record. Target invariance
    under the stated construction does not alone establish irreducibility or a mixing
    rate.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined sampling or adaptation procedure; not a trained model, graphical
      probability model or benchmark result.
    evidence_ids:
    - multipletrymetropolis-source
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The procedure defines target-invariant Markov transitions under its
      stated assumptions. AIO MarkovChain describes a stochastic process/model and
      is exported beneath Network. This method-to-process related match is not equivalence,
      an is-a assertion or a claim of independent samples or a trained network.
    evidence_ids:
    - identity
    - mapping
- assessment_id: multipletrymetropoliswithingibbs
  area: evidence
  topic: Identity, mechanism, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:MultipleTryMetropolisWithinGibbs
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - multipletrymetropoliswithingibbs-source
  summary: This is the MTM-Gibbs construction in Liu–Liang–Wong Section 5.2, a specific
    multiple-candidate Metropolis-within-Gibbs kernel. It need not draw exactly from
    a full conditional in one update and does not replace that conditional with a
    gridded interpolation. No normalized match was found across all 442 pinned AIO
    labels/scoped synonyms and 175 prior native IDs/names/aliases. Full-checkout searches
    included ignored and hidden files in both worktrees; the only text hit was an
    unrelated installed-package checksum substring. Existing general Metropolis-Hastings,
    Metropolis-within-Gibbs and random-walk records were inspected to resolve these
    specialization boundaries.
  details: 'For a chosen coordinate i, fix x_−i and use the unnormalized scalar target
    pi_i(z)=pi(x_−i,z). Draw k independent yj from T(x_i,·), compute w(yj,x_i)=pi_i(yj)T(yj,x_i)lambda(yj,x_i),
    and select y in proportion to these weights. Draw k−1 reference values from T(y,·),
    append the old x_i, and accept using the forward-to-reference total-weight ratio
    of MTM. On acceptance replace only coordinate i; otherwise keep the full state.
    T may depend on the fixed remaining coordinates; its forward/reverse support and
    symmetric lambda requirements hold within that conditional update. Limitations:
    This is conditional target invariance, not an exact independent conditional draw
    or independence of successive full states. Use the complete backward-reference
    correction. Keeping only the weighted candidate selection defines a different
    procedure. Zero forward total weight is handled by retaining the current coordinate;
    finite, meaningful target/proposal weights are required. Support, coordinate scheduling
    and irreducibility determine whether the full chain can explore the target. No
    benchmark advantage over Gibbs or other conditional kernels is asserted.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined sampling or adaptation procedure; not a trained model, graphical
      probability model or benchmark result.
    evidence_ids:
    - multipletrymetropoliswithingibbs-source
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The procedure defines target-invariant Markov transitions under its
      stated assumptions. AIO MarkovChain describes a stochastic process/model and
      is exported beneath Network. This method-to-process related match is not equivalence,
      an is-a assertion or a claim of independent samples or a trained network.
    evidence_ids:
    - identity
    - mapping
- assessment_id: conjugategradientmontecarlo
  area: evidence
  topic: Identity, mechanism, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:ConjugateGradientMonteCarlo
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - conjugategradientmontecarlo-source
  summary: This is Liu–Liang–Wong Section 4.2 CGMC, not the conjugate-gradient linear
    solver or direct optimization as a substitute for sampling. Its anchor comes from
    a different stream. The product target is an invariant population law, not a statement
    that transient streams are independent. No normalized match was found across all
    442 pinned AIO labels/scoped synonyms and 175 prior native IDs/names/aliases.
    Full-checkout searches included ignored and hidden files in both worktrees; the
    only text hit was an unrelated installed-package checksum substring. Existing
    general Metropolis-Hastings, Metropolis-within-Gibbs and random-walk records were
    inspected to resolve these specialization boundaries.
  details: 'Maintain m≥2 population members targeting a product of pi. Choose a reference
    member x_r uniformly at random, and deterministically optimize along a gradient
    or conjugate-gradient direction of log pi to obtain anchor A=g(x_r). Choose x_c
    uniformly among the other members. For A≠x_c, define e=(A−x_c)/||A−x_c|| and the
    scalar line target f(r) proportional to |r|^(d−1)pi(A+r e), r on the whole real
    line. Apply a valid MTM transition along this line, starting at the scalar coordinate
    of x_c, and replace x_c by A+r_new e while retaining the other members. A scalar
    proposal and weight construction must respect the same unoriented line when traversed
    in reverse; a centered Gaussian scalar random-walk proposal of fixed variance
    with MTM-II target-density selection weights is a concrete compatible choice.
    The source’s product-invariance argument uses the anchor’s independence from the
    moved member under the product target. Limitations: The factor |r|^(d−1) is essential
    for an anchor line selected through the current point. Replacing the line target
    with pi(A+r e) alone is not this construction. The optimization anchor must be
    independent of the moved member under the product stationary law. Optimizing that
    same member and copying this acceptance scheme is not justified. The zero-length
    line A=x_c requires a defined degenerate-case policy; the displayed normalized
    direction is not evaluated at zero. Differentiability and the chosen deterministic
    optimization procedure have their own requirements. The compatible scalar-proposal
    statement is an explicit implementation constraint inferred from reversing the
    unoriented line, not a new algorithm attributed to the source. Invariance does
    not guarantee population exploration, convergence, independent transient streams
    or universally reliable convergence diagnostics. Optimization and multiple trials
    add cost.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined sampling or adaptation procedure; not a trained model, graphical
      probability model or benchmark result.
    evidence_ids:
    - conjugategradientmontecarlo-source
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: The procedure defines target-invariant Markov transitions under its
      stated assumptions, including a population state for CGMC. AIO MarkovChain describes
      a stochastic process/model and is exported beneath Network. This method-to-process
      related match is not equivalence, an is-a assertion or a claim of independent
      samples or a trained network.
    evidence_ids:
    - identity
    - mapping
- assessment_id: robustadaptivemetropolis
  area: evidence
  topic: Identity, mechanism, limitations and mapping
  outcome: supported
  target_ids:
  - AIMech:RobustAdaptiveMetropolis
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - robustadaptivemetropolis-source
  summary: This is Vihola’s RAM update, which avoids estimating the target covariance.
    It differs from covariance-based adaptive Metropolis, scale-only adaptation and
    a fixed random-walk kernel. RAM here denotes this sampler, not computer memory.
    The history-dependent state sequence is not assumed to be a homogeneous Markov
    chain. No normalized match was found across all 442 pinned AIO labels/scoped synonyms
    and 175 prior native IDs/names/aliases. Full-checkout searches included ignored
    and hidden files in both worktrees; the only text hit was an unrelated installed-package
    checksum substring. Existing general Metropolis-Hastings, Metropolis-within-Gibbs
    and random-walk records were inspected to resolve these specialization boundaries.
  details: 'Let q be a spherical density, S a lower-triangular factor with positive
    diagonal, x satisfy pi(x)>0, eta_n lie in (0,1] and decay to zero, and alpha_star
    lie in (0,1). Draw U from q and propose y=x+S U. Set alpha=min(1,pi(y)/pi(x)),
    accept y with this probability or retain x. Whether accepted or rejected, choose
    the next positive-diagonal Cholesky factor S_new satisfying S_new S_new^T=S[I+eta_n(alpha−alpha_star)UU^T/||U||²]S^T.
    The update uses the acceptance probability, not the binary acceptance outcome;
    the normalized direction U determines the rank-one adjustment. It expands that
    component when alpha exceeds the target and contracts it when alpha is smaller.
    Limitations: Spherical continuous proposals make U=0 a null event; numerical implementations
    still need a zero-norm guard and stable factor updates. Positive definiteness
    of each update does not prove long-run stability. The source’s strong-law result
    assumes target/proposal regularity and step-size conditions and holds on an event
    where shape eigenvalues stay bounded away from zero and infinity. The paper explicitly
    leaves unrestricted stability unproved. Enforcing fixed eigenvalue bounds by rejecting
    a proposed shape update is a separate safeguard that can alter the limiting shape.
    A chosen acceptance rate is a tuning target, not a universal optimum or convergence
    diagnostic. Strong multimodality can remain difficult; no benchmark or arbitrary-heavy-tail
    convergence guarantee is asserted. The exact inspected arXiv v2 bytes have a later
    title-page footer date. This record does not claim to have inspected the later
    journal version.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined sampling or adaptation procedure; not a trained model, graphical
      probability model or benchmark result.
    evidence_ids:
    - robustadaptivemetropolis-source
  - name: aio-assessment
    value: 'related_match: MarkovChain'
    definition: RAM adapts a family of random-walk Metropolis transition kernels,
      each target-invariant at a fixed shape. Its history-dependent sampled-state
      sequence is not assumed to be a homogeneous Markov chain. AIO MarkovChain describes
      the underlying process/model concept beneath Network, so this is a related method-to-process
      mapping, not equivalence, a subclass assertion or a proof of adaptive convergence.
    evidence_ids:
    - identity
    - mapping
- assessment_id: rejected-path-correction
  area: scope
  topic: General and fixed symmetric delayed rejection
  outcome: supported
  target_ids:
  - AIMech:DelayedRejectionMetropolis
  - AIMech:SymmetricDelayedRejection
  evidence_ids:
  - delayedrejectionmetropolis-source
  - symmetricdelayedrejection-source
  summary: Retain the general path-corrected procedure and its explicitly fixed symmetric-kernel
    specialization.
  details: Revisited Mira Equation (2) and maximum-density Equation (8) visually.
    The second-stage numerator includes reverse q1, reverse q2 and the reverse rejection
    probability; denominator uses the actually traversed forward path. The simplified
    rule uses the same symmetric q through the last rejected candidate. Figure 1 reverses
    the first acceptance ratio relative to the text; the record documents this and
    uses the consistent text. Stage-dependent variances cannot be silently substituted
    into the simplified rule. Capping stages leaves residual rejection mass at the
    original state.
- assessment_id: multiple-candidates-and-conditionals
  area: scope
  topic: Candidate selection, reverse reference sets and conditional specialization
  outcome: supported
  target_ids:
  - AIMech:MultipleTryMetropolis
  - AIMech:MultipleTryMetropolisWithinGibbs
  evidence_ids:
  - multipletrymetropolis-source
  - multipletrymetropoliswithingibbs-source
  - existing-samplers
  summary: Retain core MTM and MTM-Gibbs as distinct general and coordinate-update
    procedures.
  details: Visually rechecked Section 2 and Section 5.2. w(a,b)=pi(a)T(a,b)lambda(a,b),
    selection uses w(y_j,x), and the backward set contains the old x. With k=1 symmetric
    lambda cancels to the ordinary MH ratio. The zero-weight retention caveat is a
    boundary completion of the displayed weighted-selection rule. The conditional
    specialization holds the rest fixed and preserves that conditional without independently
    drawing it. The inconsistent auxiliary-variable weight order in Section 3.1 is
    documented and excluded from the asserted extension scope.
- assessment_id: population-line-kernel
  area: scope
  topic: Optimization anchors, radial Jacobian and population invariance
  outcome: supported
  target_ids:
  - AIMech:ConjugateGradientMonteCarlo
  evidence_ids:
  - conjugategradientmontecarlo-source
  - multipletrymetropolis-source
  summary: CGMC combines an anchor computed from a different population member with
    a properly adjusted line transition.
  details: Visually revisited steps 1–3, Equation (11), Theorem 2 and Lemma 1. Under
    the product stationary law the reference member and the moved member are independent,
    allowing A=g(x_r). The line target includes |r|^(d−1), and changing line orientation
    must leave the scalar transition compatible. The record labels this compatibility
    statement as an implementation inference and gives a reflection-compatible Gaussian
    random-walk/MTM-II choice. A uniform state-independent choice of distinct members
    is explicit. No assertion of independent transient streams or universal convergence
    is made.
- assessment_id: adaptive-validity
  area: scope
  topic: RAM probability-driven shape adaptation and conditional strong law
  outcome: supported
  target_ids:
  - AIMech:RobustAdaptiveMetropolis
  evidence_ids:
  - robustadaptivemetropolis-source
  - mapping
  summary: The RAM record preserves both the exact rank-one update and the limits
    of its validity analysis.
  details: Visually revisited R1–R3 and Theorem 17/Remark 19. Adaptation uses alpha
    rather than an acceptance indicator and occurs after either outcome. The rank-one
    factor remains positive definite for eta in (0,1] and alpha_star in (0,1), but
    this does not bound the infinite sequence of shapes. The strong law is conditional
    on target/proposal and step-size assumptions and the eigenvalue stability event.
    The mapping explicitly refers to the fixed-shape kernels being adapted, not an
    unsupported homogeneous Markov claim for the sampled-state history. The version
    and later PDF footer are both preserved.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:DelayedRejectionMetropolis
  - AIMech:SymmetricDelayedRejection
  - AIMech:MultipleTryMetropolis
  - AIMech:MultipleTryMetropolisWithinGibbs
  - AIMech:ConjugateGradientMonteCarlo
  - AIMech:RobustAdaptiveMetropolis
  evidence_ids:
  - identity
  - mapping
  - existing-samplers
  - delayedrejectionmetropolis-source
  - symmetricdelayedrejection-source
  - multipletrymetropolis-source
  - multipletrymetropoliswithingibbs-source
  - conjugategradientmontecarlo-source
  - robustadaptivemetropolis-source
  rationale: Preserve the general delayed-rejection rule and its fixed symmetric specialization,
    core MTM and its conditional-coordinate specialization, population optimization
    anchors with a radial line target, and probability-driven RAM adaptation. Their
    different state, candidate and adaptation constructions justify distinct scopes.
    Related AIO mappings preserve algorithm-to-process differences, including the
    non-homogeneous adaptive history caveat.
limitations:
- Adversarial author self-review only; all six records remain DRAFT.
- Only declared source text/OCR and image pages were read. No full visual inspection
  of every page is claimed.
- Source formula inconsistencies are recorded; no separate published erratum is asserted.
- The CGMC line-reversal compatibility example and zero-weight retention completion
  are explicitly interpreted from the verified core kernels.
- AM/DRAM original-method access and auxiliary MTM discrepancies remain research work,
  not resolved concepts.
- No numerical experiment, implementation reproduction or universal performance claim
  is included.
- All required repository and immutable-vendor checks passed; six positive discoveries
  do not establish saturation.
tags:
- native-concepts
- mcmc
- delayed-rejection
- multiple-try
- adaptive-mcmc
- self-review
- discovery-ongoing
```
