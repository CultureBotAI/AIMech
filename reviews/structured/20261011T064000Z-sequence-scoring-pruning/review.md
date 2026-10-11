# Scientific self-review of sequence scoring, stopping and pruning

- Review: 20261011T064000Z-sequence-scoring-pruning
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T06:40:00Z
- Finished UTC: 2026-10-11T06:40:00Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All seven maintained identities, claim mechanisms and related AIO mappings are supported in their stated scopes. No actionable record finding remains. Source-domain and implementation uncertainties are retained without promoting DRAFT status.

## Scope And Provenance

Full review of one stopping decoder, four rescoring methods and two local beam-pruning procedures.

Selection: Exactly the seven native IDs in the sequence-scoring-pruning discovery ledger; no sampling.
Coverage: full; 7 reviewed / 7 in the declared population.
Source: working_tree at Git base 6a02d6325ce81796dbec9293f8bb4b49a3c87fbb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:OptimalStoppingBeamDecoding | data/curated/OptimalStoppingBeamDecoding.yaml | maintained | Beam decoding with a monotone-score stopping certificate |
| AIMech:BoundedLengthReward | data/curated/BoundedLengthReward.yaml | maintained | Bounded length reward for sequence scoring |
| AIMech:PredictedLengthBoundedReward | data/curated/PredictedLengthBoundedReward.yaml | maintained | Bounded word reward with predicted length |
| AIMech:BoundedAdaptiveReward | data/curated/BoundedAdaptiveReward.yaml | maintained | Bounded adaptive reward for sequence scoring |
| AIMech:BrevityPenaltyNormalization | data/curated/BrevityPenaltyNormalization.yaml | maintained | Brevity-penalty normalization for sequence scoring |
| AIMech:AbsoluteThresholdBeamPruning | data/curated/AbsoluteThresholdBeamPruning.yaml | maintained | Absolute threshold pruning for sequence beams |
| AIMech:PerNodeCandidateBeamPruning | data/curated/PerNodeCandidateBeamPruning.yaml | maintained | Maximum candidates per node in sequence beam pruning |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:OptimalStoppingBeamDecoding, AIMech:BoundedLengthReward, AIMech:PredictedLengthBoundedReward, AIMech:BoundedAdaptiveReward, AIMech:BrevityPenaltyNormalization, AIMech:AbsoluteThresholdBeamPruning, AIMech:PerNodeCandidateBeamPruning | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate | passed | True | AIMech:OptimalStoppingBeamDecoding, AIMech:BoundedLengthReward, AIMech:PredictedLengthBoundedReward, AIMech:BoundedAdaptiveReward, AIMech:BrevityPenaltyNormalization, AIMech:AbsoluteThresholdBeamPruning, AIMech:PerNodeCandidateBeamPruning | Checked 442 record(s); 0 failed.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-curated | passed | True | AIMech:OptimalStoppingBeamDecoding, AIMech:BoundedLengthReward, AIMech:PredictedLengthBoundedReward, AIMech:BoundedAdaptiveReward, AIMech:BrevityPenaltyNormalization, AIMech:AbsoluteThresholdBeamPruning, AIMech:PerNodeCandidateBeamPruning | Checked 153 curated concept record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli seed --check | passed | True | AIMech:OptimalStoppingBeamDecoding, AIMech:BoundedLengthReward, AIMech:PredictedLengthBoundedReward, AIMech:BoundedAdaptiveReward, AIMech:BrevityPenaltyNormalization, AIMech:AbsoluteThresholdBeamPruning, AIMech:PerNodeCandidateBeamPruning | AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-history --base HEAD | passed | True | AIMech:OptimalStoppingBeamDecoding, AIMech:BoundedLengthReward, AIMech:PredictedLengthBoundedReward, AIMech:BoundedAdaptiveReward, AIMech:BrevityPenaltyNormalization, AIMech:AbsoluteThresholdBeamPruning, AIMech:PerNodeCandidateBeamPruning | Checked 31 history record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python scripts/record_review.py check | passed | True | AIMech:OptimalStoppingBeamDecoding, AIMech:BoundedLengthReward, AIMech:PredictedLengthBoundedReward, AIMech:BoundedAdaptiveReward, AIMech:BrevityPenaltyNormalization, AIMech:AbsoluteThresholdBeamPruning, AIMech:PerNodeCandidateBeamPruning | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 31,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class<br> |
| just check | passed | True | AIMech:OptimalStoppingBeamDecoding, AIMech:BoundedLengthReward, AIMech:PredictedLengthBoundedReward, AIMech:BoundedAdaptiveReward, AIMech:BrevityPenaltyNormalization, AIMech:AbsoluteThresholdBeamPruning, AIMech:PerNodeCandidateBeamPruning | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 54.34s<br>Checked 442 record(s); 0 failed.<br>Checked 153 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 31 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 31,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:OptimalStoppingBeamDecoding, AIMech:BoundedLengthReward, AIMech:PredictedLengthBoundedReward, AIMech:BoundedAdaptiveReward, AIMech:BrevityPenaltyNormalization, AIMech:AbsoluteThresholdBeamPruning, AIMech:PerNodeCandidateBeamPruning | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| Score-coordinate and length-bound examples | passed | False | AIMech:BrevityPenaltyNormalization, AIMech:AbsoluteThresholdBeamPruning | Actual arithmetic assertions passed and results were saved. The examples establish their stated conditional differences only; neither is an author-code run. |

## Scientific And Domain Assessments

### Identity, scoring rule, stopping bound, pruning scope and AIO mapping

evidence: supported. Targets: AIMech:OptimalStoppingBeamDecoding.

This is Huang, Zhao and Ma’s 2017 optimal-ending procedure, with optimality explicitly limited by the retained beam. It differs from stopping on a completed top-ranked item without remembering earlier completions, from counting completed outputs, and from score-prioritized best-first expansion with per-length budgets. No normalized identity match was found across the 442 AIO and 146 prior native records; both checkout text searches included ignored and hidden files and returned no matches for the selected exact IDs, full labels, aliases and source titles.

The certificate concerns descendants of retained beam prefixes. It does not recover prefixes pruned by finite width or guarantee global MAP decoding. A non-increasing extension score and a stored completed incumbent are required. Length normalization or positive rewards can invalidate the raw-prefix bound and need a different certificate. The paper compares stopping times under the same beam evolution and a specific historical top-completed baseline. It does not establish universally fastest decoding or current software defaults. Better model score does not imply better translation quality; the source reports short-output problems under pure probability scoring. Finite resource limits, absent EOS completions, empty beams and tie conventions need explicit implementation policies. No unconditional finite-time termination claim is made.

### Identity, scoring rule, stopping bound, pruning scope and AIO mapping

evidence: supported. Targets: AIMech:BoundedLengthReward.

The cap limits how much reward can accumulate; it is not itself a maximum allowed output length. This is the bounded reward in Huang et al. 2017, called bounded word-reward by Yang et al. 2018. It differs from division by output length, an uncapped word reward and a reward rate recomputed from beam statistics. No normalized identity match was found across the 442 AIO and 146 prior native records; both checkout text searches included ignored and hidden files and returned no matches for the selected exact IDs, full labels, aliases and source titles.

The score is a decoding preference, not a probability distribution or an intrinsic translation-quality measure. The reward rate and length-cap estimate require specification. A development-set average length ratio need not transfer to every sentence or domain. The stopping bound assumes non-increasing log probability, nonnegative fixed reward and a fixed finite cap for the input; its beam-relative guarantee does not undo finite-width pruning. Reward saturation does not prohibit outputs longer than the cap. Tokenization, length counting and EOS handling must be specified in an implementation. No numerical BLEU improvement, universal quality advantage or current implementation behavior is asserted.

### Identity, scoring rule, stopping bound, pruning scope and AIO mapping

evidence: supported. Targets: AIMech:PredictedLengthBoundedReward.

This is Yang et al.’s predicted-length bounded word-reward variant. It changes the cap, while retaining a separately tuned reward rate r. It is not the beam-statistic adaptive reward or the brevity-penalty normalized score, and it is not a standalone trained length-predictor instance. No normalized identity match was found across the 442 AIO and 146 prior native records; both checkout text searches included ignored and hidden files and returned no matches for the selected exact IDs, full labels, aliases and source titles.

The method still requires a learned length predictor and a tuned reward rate; replacing the corpus ratio does not make the complete system parameter-free. Predicted length is a reward cap, not automatically an enforced maximum sequence length or an accurate target for every input. A usable nonnegative length prediction, tokenizer conventions and integration with the decoder must be specified. The paper passage does not provide a complete predictor training or calibration protocol. Finite beam width still prunes hypotheses. Neither accurate length prediction nor a stopping certificate implies globally optimal output or universally better translation quality. The empirical source scope is Chinese-to-English news translation; no numerical result is curated.

### Identity, scoring rule, stopping bound, pruning scope and AIO mapping

evidence: supported. Targets: AIMech:BoundedAdaptiveReward.

Yang et al.’s bounded adaptive-reward changes the reward rate with the decoding step, unlike fixed-r bounded word-reward. It is a beam-conditioned scoring method rather than a reinforcement-learning reward-training algorithm or a beam-independent probability model. No normalized identity match was found across the 442 AIO and 146 prior native records; both checkout text searches included ignored and hidden files and returned no matches for the selected exact IDs, full labels, aliases and source titles.

The reward sequence depends on the beam and model probabilities. Changing beam policy can change the score assigned to a completed hypothesis. Removing a manually tuned constant reward rate does not remove the trained translation model, length predictor, beam size or other implementation choices. The printed sum uses a predicted length as its upper limit without specifying a noninteger rounding policy. A discrete implementation must define the effective integer cap and EOS/token counting; the record does not assert an author-approved rounding convention. Equation (10) assumes b available beam entries and defined token log probabilities. Empty or shrunken beams and zero-probability tokens require an explicit policy. The stated stopping argument applies after reward saturation with a completed incumbent. It is limited to retained beam continuations, not global sequence optimality or guaranteed quality improvement.

### Identity, scoring rule, stopping bound, pruning scope and AIO mapping

evidence: supported. Targets: AIMech:BrevityPenaltyNormalization.

BP-Norm is Yang et al.’s predicted-length decoding score. It resembles the algebraic structure of BLEU’s brevity penalty but does not compute n-gram precision, use an actual reference translation at inference, or equal the BLEU evaluation metric. It differs from plain average log probability and additive word rewards. No normalized identity match was found across the 442 AIO and 146 prior native records; both checkout text searches included ignored and hidden files and returned no matches for the selected exact IDs, full labels, aliases and source titles.

Lpred is a prediction, not a reference length or a proven upper bound on output length. The S_t/R stopping bound requires that admissible completions actually have length at most R. The experiments set R to the predicted length. This supports the stopping guarantee only under an enforced length cap or another justification that all allowed completions obey that bound; a forecast alone is insufficient. The formula requires nonempty hypotheses and a valid length prediction. A BOS-only prefix needs separate handling; length and EOS conventions must be specified. The score is neither a normalized probability nor BLEU itself. Improved search score does not imply better human translation quality. The source’s hyperparameter-free comparison concerns removal of a separately tuned reward constant, not absence of trained models, a length predictor or decoding choices. Finite beam pruning remains approximate.

### Identity, scoring rule, stopping bound, pruning scope and AIO mapping

evidence: supported. Targets: AIMech:AbsoluteThresholdBeamPruning.

This is Freitag and Al-Onaizan’s absolute threshold pruning rule. It uses an additive score difference, unlike their relative-score and last-token relative thresholds. It is an additional local pruning step, not a stopping certificate or a method that automatically widens the beam. No normalized identity match was found across the 442 AIO and 146 prior native records; both checkout text searches included ignored and hidden files and returned no matches for the selected exact IDs, full labels, aliases and source titles.

The extra pruning can remove a prefix leading to the best eventual output. The paper explicitly reports search errors even where aggregate task metrics remain similar. The numerical margin depends on score scale, log base and model calibration. It is not a relative probability threshold. A positive margin is required to retain the best finite-scoring item under the printed non-strict inequality; a zero margin would discard even maximum-score candidates. The procedure is layered onto a decoder with its own EOS and width policy. It does not by itself specify the entire decoder or guarantee improved speed or quality. The separate relative-pruning equations have a score-scale ambiguity under negative log scores. No correction to those distinct variants is inferred from this additive rule.

### Identity, scoring rule, stopping bound, pruning scope and AIO mapping

evidence: supported. Targets: AIMech:PerNodeCandidateBeamPruning.

This is the Maximum Candidates per Node rule of Freitag and Al-Onaizan. Same history means the common predecessor prefix, not arbitrary semantic similarity between full sequences. It differs from an additive diversity penalty, grouping beams into separate searches or imposing a global frontier capacity. No normalized identity match was found across the 442 AIO and 146 prior native records; both checkout text searches included ignored and hidden files and returned no matches for the selected exact IDs, full labels, aliases and source titles.

A positive integer per-parent cap and deterministic tie handling must be specified. The source’s prose refers to better-scoring candidates without a complete tie policy. Limiting sibling extensions can remove the prefix of the best eventual sequence; this is not an exact or complete search guarantee. More varied parent prefixes do not guarantee semantic diversity or improved translation quality. The paper’s conclusion reports no translation-quality improvement from this diversity intervention. The inherited decoder determines EOS processing, generation length and changing active-beam width. The pruning rule alone is not a complete decoder implementation. No specific current library implementation, numeric quality gain or universal runtime benefit is asserted.

### Conditions needed for beam-relative stopping guarantees

scope: supported. Targets: AIMech:OptimalStoppingBeamDecoding, AIMech:BoundedLengthReward, AIMech:PredictedLengthBoundedReward, AIMech:BoundedAdaptiveReward, AIMech:BrevityPenaltyNormalization.

The records distinguish a raw monotone score bound, a fixed remaining reward bound, an input-conditioned reward cap, reward saturation after a beam-dependent sum, and the true maximum-length assumption for BP-Norm.

An incumbent is required before stopping. No certificate recovers width-pruned prefixes. Reward saturation does not prohibit long outputs, and a length forecast is not automatically a maximum. Integer cap/EOS conventions for the adaptive sum remain explicit implementation limitations rather than invented source details. Optimality refers to the adjusted scoring objective within retained beam continuations, not universal translation quality.

### Local pruning changes the candidate set without an exact-search guarantee

evidence: supported. Targets: AIMech:AbsoluteThresholdBeamPruning, AIMech:PerNodeCandidateBeamPruning.

Both added pruning rules follow the paper’s initial beam-size cut. Absolute pruning uses a positive additive score margin with the printed inclusive discard boundary; per-parent pruning limits sibling continuations.

The definitions do not imply automatic beam widening, refilling, semantic diversity or improved task quality. Search errors and the source’s negative diversity-quality conclusion are retained. Relative-score variants remain separate deferred candidates until their score domain is established.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:OptimalStoppingBeamDecoding, AIMech:BoundedLengthReward, AIMech:PredictedLengthBoundedReward, AIMech:BoundedAdaptiveReward, AIMech:BrevityPenaltyNormalization, AIMech:AbsoluteThresholdBeamPruning, AIMech:PerNodeCandidateBeamPruning. The raw stopping certificate, fixed capped reward, predicted cap, adaptive per-step reward, brevity-penalty normalization, additive score-gap pruning and per-parent candidate limit define different methods. Predicted-cap scoring specializes capped reward; this overlap is explicit and is not equivalence. The scoring formulas are mathematical methods, while traversal/stopping and candidate-removal procedures are algorithms. No local method is equated to the broad NLP task.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T063749Z-sequence-scoring-pruning.json | supports | No normalized identity match across all 442 pinned AIO labels/scoped synonyms and 146 preceding native IDs/names/aliases. Both full-checkout searches included ignored and hidden files and returned zero fixed-string matches for selected exact IDs, full labels, aliases and source titles. This is bounded to those terms, not an absence claim about every related phrase. Semantic scope comparisons distinguish the existing vanilla, FCFS, controlled-patience and per-length best-first decoders. |
| mapping | sources/aio/aio.json; Exact CLASS definitions, synonyms and incident edges for NaturalLanguageProcessing and MathematicalFunction; related model/layer definitions for DecoderLLM, EncoderDecoderLLM and RandomTranslationLayer | supports | All seven methods have related_match to NaturalLanguageProcessing, whose exact CLASS definition, NLP synonym and is_a MachineLearningTask edge were inspected. This is a method-to-domain relation grounded in the papers’ central neural-translation scope. DecoderLLM and EncoderDecoderLLM definitions denote learned model architectures, not the present search or scoring procedures. RandomTranslationLayer concerns image augmentation. MathematicalFunction was also inspected as a broad formula category; no equivalence to a generic function or exhaustive set of possible mappings is claimed. The four rescoring rules are typed mathematical_method, while the stopping decoder and two pruning procedures are algorithms. |
| optimalstoppingbeamdecoding-0 | https://aclanthology.org/D17-1227.pdf; Sections 2–3, Equations (1)–(2), Theorems 1–2, printed p. 2135 / PDF p. 2 | supports | A layer-based sequence beam decoder that retains the best completed hypothesis seen so far and stops when the highest current prefix score cannot exceed that incumbent under a score that never increases with extension. Version: EMNLP 2017, printed pp. 2134–2139; published six-page ACL Anthology PDF. Actually inspected rendered PDF pages: 2, 3, 4. |
| optimalstoppingbeamdecoding-1 | https://aclanthology.org/D17-1227.pdf; Section 4 and Section 5.2 discussion, printed pp. 2136 and 2138 / PDF pp. 3 and 5 | supports | The unmodified probability objective can favor short translations; the source therefore introduces bounded length rewards. The stopping certificate is a search-score statement, not a quality guarantee. Version: EMNLP 2017, printed pp. 2134–2139; published six-page ACL Anthology PDF. Actually inspected rendered PDF pages: 2, 3, 4. |
| boundedlengthreward-0 | https://aclanthology.org/D17-1227.pdf; Section 4, score definition and Equations (3)–(4), printed pp. 2136–2137 / PDF pp. 3–4 | supports | A sequence scoring rule that adds a fixed nonnegative reward per generated position up to a finite length cap, giving score S(y)+r·min(l,&#124;y&#124;) instead of rewarding every additional position without bound. Version: EMNLP 2017, printed pp. 2134–2139; published six-page ACL Anthology PDF. Actually inspected rendered PDF pages: 2, 3, 4. |
| boundedlengthreward-1 | https://aclanthology.org/D18-1342.pdf; Section 4.1 Equation (7) and Section 4.2, printed p. 3056 / PDF p. 3 | supports | The 2018 paper calls the fixed-rate capped rule bounded word-reward and distinguishes it from its predicted-length and adaptive-reward variants. Version: EMNLP 2018, printed pp. 3054–3059; published six-page ACL Anthology PDF. Actually inspected rendered PDF pages: 3, 4. |
| predictedlengthboundedreward-0 | https://aclanthology.org/D18-1342.pdf; Sections 4.2–4.2.1, Equations (8)–(9), printed p. 3056 / PDF p. 3 | supports | A sequence rescoring method that adds a fixed word reward only up to an input-specific length predicted from encoder states, replacing a corpus-level generation-ratio cap with Lpred(x). Version: EMNLP 2018, printed pp. 3054–3059; published six-page ACL Anthology PDF. Actually inspected rendered PDF pages: 3, 4. |
| boundedadaptivereward-0 | https://aclanthology.org/D18-1342.pdf; Section 4.2.2, Equations (10)–(11), and Section 5.2 final paragraph, printed pp. 3056–3057 / PDF pp. 3–4 | supports | A beam-dependent sequence rescoring rule that adds per-step rewards derived from the beam’s mean negative log token probability, accumulating them only up to a predicted output-length cap. Version: EMNLP 2018, printed pp. 3054–3059; published six-page ACL Anthology PDF. Actually inspected rendered PDF pages: 3, 4. |
| brevitypenaltynormalization-0 | https://aclanthology.org/D18-1342.pdf; Section 4.2.3 Equation (12), transformed score and Section 5.2 Equation (13), printed pp. 3056–3057 / PDF pp. 3–4 | supports | A sequence rescoring rule that adds a predicted-length brevity penalty in log space to average token log probability: S(x,y)/&#124;y&#124; + min(1−Lpred(x)/&#124;y&#124;,0). Version: EMNLP 2018, printed pp. 3054–3059; published six-page ACL Anthology PDF. Actually inspected rendered PDF pages: 3, 4. |
| brevitypenaltynormalization-1 | https://aclanthology.org/D18-1342.pdf; Sections 5.2 and 6.1, printed pp. 3057–3058 / PDF pp. 4–5 | supports | Equation (13) defines R as a maximum generation length, whereas the experiments identify it with predicted length. The bound is curated only when that value truly bounds the permitted completion lengths; prediction alone is not a mathematical upper bound. Version: EMNLP 2018, printed pp. 3054–3059; published six-page ACL Anthology PDF. Actually inspected rendered PDF pages: 3, 4. |
| absolutethresholdbeampruning-0 | https://aclanthology.org/W17-3207.pdf; Section 4, introductory paragraph and Absolute Threshold Pruning, Equation (2), printed p. 57 / PDF p. 2 | supports | A sequence-beam pruning procedure that first applies the beam-size cap, then discards candidates whose score is at least a specified positive margin below the best score in that capped candidate list. Version: First Workshop on Neural Machine Translation 2017, printed pp. 56–60; published five-page ACL Anthology PDF. Actually inspected rendered PDF pages: 2. |
| absolutethresholdbeampruning-1 | https://aclanthology.org/W17-3207.pdf; Section 5 discussion and Section 6, printed p. 58 / PDF p. 3 | supports | Additional pruning can change outputs by discarding a better-scoring hypothesis. The paper’s reported quality preservation and speed improvements are empirical outcomes in specific language-pair setups, not exact-search guarantees. Version: First Workshop on Neural Machine Translation 2017, printed pp. 56–60; published five-page ACL Anthology PDF. Actually inspected rendered PDF pages: 2. |
| pernodecandidatebeampruning-0 | https://aclanthology.org/W17-3207.pdf; Section 4, introductory paragraph and Maximum Candidates per Node, printed p. 57 / PDF p. 2 | supports | A sequence-beam pruning procedure that limits how many retained candidate extensions may come from the same predecessor hypothesis, discarding a candidate when the allowed number of better-scoring siblings is already retained. Version: First Workshop on Neural Machine Translation 2017, printed pp. 56–60; published five-page ACL Anthology PDF. Actually inspected rendered PDF pages: 2. |
| pernodecandidatebeampruning-1 | https://aclanthology.org/W17-3207.pdf; Introduction and Section 6, printed pp. 56 and 58 / PDF pp. 1 and 3 | supports | The source introduced a per-history candidate cap to diversify predecessor coverage, but its conclusion states that adding diversity did not improve translation quality in the evaluated settings. Version: First Workshop on Neural Machine Translation 2017, printed pp. 56–60; published five-page ACL Anthology PDF. Actually inspected rendered PDF pages: 2. |
| score-boundary-analysis | research/validation/20261011T063749Z-score-boundary-examples.json; Two arithmetic examples with declared score domains and length assumptions; companion script research/validation/20261011T063749Z-score-boundary-examples.py | supports | For negative log scores -1,-2,-3 and ratio 0.6, literal multiplicative log pruning retains nothing, while probability-ratio pruning retains the best item. A BP-Norm completion longer than a predicted R can beat an incumbent after the prediction-based inequality would stop. These illustrate necessary assumptions, not author-code bugs or benchmark measurements. |

## Limits And Additional Notes

- Adversarial author self-review, not independent approval; all seven records remain DRAFT.
- The scope is paper-defined methods, not reproduction of author implementations or current library behavior.
- No unconditional global sequence-optimality, runtime or quality guarantee is asserted. Finite beam pruning remains approximate.
- BP-Norm’s S_t/R bound requires a genuine maximum permitted length; the curator example only challenges substituting an unenforced forecast.
- Relative-score ambiguity and adaptive reward rounding/EOS details are preserved; no author-approved correction is claimed.
- Repeated citations to passages in the same primary paper are not independent studies.
- Minor terminology refinements were made before this saved assessment: method-to-domain mapping prose and exact non-increase under nonpositive log-probability increments.
- All required checks passed. This review covers only the seven declared targets and does not retire unrelated historical findings or establish search saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T064000Z-sequence-scoring-pruning
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of sequence scoring, stopping and pruning
started_at: '2026-10-11T06:40:00Z'
finished_at: '2026-10-11T06:40:00Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed its seven records
    and source assumptions. No independent reviewer or approval is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All seven maintained identities, claim mechanisms and related AIO mappings
  are supported in their stated scopes. No actionable record finding remains. Source-domain
  and implementation uncertainties are retained without promoting DRAFT status.
source:
  git_revision: 6a02d6325ce81796dbec9293f8bb4b49a3c87fbb
  state: working_tree
  inputs:
  - path: data/curated/AbsoluteThresholdBeamPruning.yaml
    sha256: 3b04701cf946e151944243eaf7f256880d2e005049e98b64584d9916370eebe1
    role: target
  - path: data/curated/BoundedAdaptiveReward.yaml
    sha256: e81e0c76b5844672bff5e6788d21f6803923dc6e9a03ec28f093a1c80889f0a8
    role: target
  - path: data/curated/BoundedLengthReward.yaml
    sha256: 56979d12b37f796257f81efd35d0cbadfa71a8be94bbfd47d2f599f5bf315bf2
    role: target
  - path: data/curated/BrevityPenaltyNormalization.yaml
    sha256: c498e33060d03ae6dff4212555ef7ba1e927155f07721bee5aeed5fdba71d4d0
    role: target
  - path: data/curated/OptimalStoppingBeamDecoding.yaml
    sha256: 4628e4f1e3af8f43de2c06afff4d0e9bb4a706203f10570389263a53f243bd7b
    role: target
  - path: data/curated/PerNodeCandidateBeamPruning.yaml
    sha256: 2a0397c8d7fa9706c1a7f554623b3b94682f0238e46443fe1d8398a169656fda
    role: target
  - path: data/curated/PredictedLengthBoundedReward.yaml
    sha256: 2cc91ba678ba43df06e13dd0c641e8938d0a06662f10da0697aca3a41518703d
    role: target
  - path: research/discovery/20261011T063749Z-sequence-scoring-pruning.json
    sha256: aa7b32db251de40854476e7db30cd6162f31275d457867be5f419b18483997cc
    role: context
  - path: research/validation/20261011T063749Z-score-boundary-examples.json
    sha256: 905f0aa74e921dfd3317c920e82509fac33356f1847b706dc2118ca4b05ea023
    role: context
  - path: research/validation/20261011T063749Z-score-boundary-examples.py
    sha256: 340252eb076ce85d9ecf94a16d2c6686c3963f34319619118f39791f726d60c3
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
- target_id: AIMech:OptimalStoppingBeamDecoding
  path: data/curated/OptimalStoppingBeamDecoding.yaml
  label: Beam decoding with a monotone-score stopping certificate
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OptimalStoppingBeamDecoding.yaml
    role: maintained_record
- target_id: AIMech:BoundedLengthReward
  path: data/curated/BoundedLengthReward.yaml
  label: Bounded length reward for sequence scoring
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BoundedLengthReward.yaml
    role: maintained_record
- target_id: AIMech:PredictedLengthBoundedReward
  path: data/curated/PredictedLengthBoundedReward.yaml
  label: Bounded word reward with predicted length
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PredictedLengthBoundedReward.yaml
    role: maintained_record
- target_id: AIMech:BoundedAdaptiveReward
  path: data/curated/BoundedAdaptiveReward.yaml
  label: Bounded adaptive reward for sequence scoring
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BoundedAdaptiveReward.yaml
    role: maintained_record
- target_id: AIMech:BrevityPenaltyNormalization
  path: data/curated/BrevityPenaltyNormalization.yaml
  label: Brevity-penalty normalization for sequence scoring
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BrevityPenaltyNormalization.yaml
    role: maintained_record
- target_id: AIMech:AbsoluteThresholdBeamPruning
  path: data/curated/AbsoluteThresholdBeamPruning.yaml
  label: Absolute threshold pruning for sequence beams
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AbsoluteThresholdBeamPruning.yaml
    role: maintained_record
- target_id: AIMech:PerNodeCandidateBeamPruning
  path: data/curated/PerNodeCandidateBeamPruning.yaml
  label: Maximum candidates per node in sequence beam pruning
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PerNodeCandidateBeamPruning.yaml
    role: maintained_record
scope:
  description: Full review of one stopping decoder, four rescoring methods and two
    local beam-pruning procedures.
  selection: Exactly the seven native IDs in the sequence-scoring-pruning discovery
    ledger; no sampling.
  coverage: full
  population_size: 7
  reviewed_target_ids:
  - AIMech:OptimalStoppingBeamDecoding
  - AIMech:BoundedLengthReward
  - AIMech:PredictedLengthBoundedReward
  - AIMech:BoundedAdaptiveReward
  - AIMech:BrevityPenaltyNormalization
  - AIMech:AbsoluteThresholdBeamPruning
  - AIMech:PerNodeCandidateBeamPruning
  exclusions:
  - target: Relative threshold and relative local threshold pruning
    reason: The printed multiplicative formula needs a resolved score domain before
      curating the intended procedure.
  - target: Author implementation behavior, current library defaults and numerical
      benchmark replication
    reason: No author code, trained model or benchmark was executed; the arithmetic
      examples are explicitly curator-authored.
  - target: Other new and older frontier candidates
    reason: Their primary-source and identity work remains recorded as pending.
checks:
- check_id: required-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:OptimalStoppingBeamDecoding
  - AIMech:BoundedLengthReward
  - AIMech:PredictedLengthBoundedReward
  - AIMech:BoundedAdaptiveReward
  - AIMech:BrevityPenaltyNormalization
  - AIMech:AbsoluteThresholdBeamPruning
  - AIMech:PerNodeCandidateBeamPruning
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
  - AIMech:OptimalStoppingBeamDecoding
  - AIMech:BoundedLengthReward
  - AIMech:PredictedLengthBoundedReward
  - AIMech:BoundedAdaptiveReward
  - AIMech:BrevityPenaltyNormalization
  - AIMech:AbsoluteThresholdBeamPruning
  - AIMech:PerNodeCandidateBeamPruning
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
  - AIMech:OptimalStoppingBeamDecoding
  - AIMech:BoundedLengthReward
  - AIMech:PredictedLengthBoundedReward
  - AIMech:BoundedAdaptiveReward
  - AIMech:BrevityPenaltyNormalization
  - AIMech:AbsoluteThresholdBeamPruning
  - AIMech:PerNodeCandidateBeamPruning
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 153 curated concept record(s); 0 error(s).

    '
- check_id: required-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:OptimalStoppingBeamDecoding
  - AIMech:BoundedLengthReward
  - AIMech:PredictedLengthBoundedReward
  - AIMech:BoundedAdaptiveReward
  - AIMech:BrevityPenaltyNormalization
  - AIMech:AbsoluteThresholdBeamPruning
  - AIMech:PerNodeCandidateBeamPruning
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
  - AIMech:OptimalStoppingBeamDecoding
  - AIMech:BoundedLengthReward
  - AIMech:PredictedLengthBoundedReward
  - AIMech:BoundedAdaptiveReward
  - AIMech:BrevityPenaltyNormalization
  - AIMech:AbsoluteThresholdBeamPruning
  - AIMech:PerNodeCandidateBeamPruning
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 31 history record(s); 0 error(s).

    '
- check_id: required-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:OptimalStoppingBeamDecoding
  - AIMech:BoundedLengthReward
  - AIMech:PredictedLengthBoundedReward
  - AIMech:BoundedAdaptiveReward
  - AIMech:BrevityPenaltyNormalization
  - AIMech:AbsoluteThresholdBeamPruning
  - AIMech:PerNodeCandidateBeamPruning
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 31,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\ntopClass is deprecated - use top_class\n"
- check_id: required-6
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:OptimalStoppingBeamDecoding
  - AIMech:BoundedLengthReward
  - AIMech:PredictedLengthBoundedReward
  - AIMech:BoundedAdaptiveReward
  - AIMech:BrevityPenaltyNormalization
  - AIMech:AbsoluteThresholdBeamPruning
  - AIMech:PerNodeCandidateBeamPruning
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 54.34s\nChecked 442 record(s); 0 failed.\n\
    Checked 153 curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing,\
    \ 0 changed, 0 unexpected.\nChecked 31 history record(s); 0 error(s).\n{\n  \"\
    repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 31,\n  \"coverage\"\
    : \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-7
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:OptimalStoppingBeamDecoding
  - AIMech:BoundedLengthReward
  - AIMech:PredictedLengthBoundedReward
  - AIMech:BoundedAdaptiveReward
  - AIMech:BrevityPenaltyNormalization
  - AIMech:AbsoluteThresholdBeamPruning
  - AIMech:PerNodeCandidateBeamPruning
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: curator-arithmetic
  name: Score-coordinate and length-bound examples
  command: python3 research/validation/20261011T063749Z-score-boundary-examples.py
  status: passed
  required: false
  target_ids:
  - AIMech:BrevityPenaltyNormalization
  - AIMech:AbsoluteThresholdBeamPruning
  exit_code: 0
  expected_exit_code: 0
  summary: Actual arithmetic assertions passed and results were saved. The examples
    establish their stated conditional differences only; neither is an author-code
    run.
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T063749Z-sequence-scoring-pruning.json
  accessed_at: '2026-10-11T06:40:00Z'
  support: supports
  summary: No normalized identity match across all 442 pinned AIO labels/scoped synonyms
    and 146 preceding native IDs/names/aliases. Both full-checkout searches included
    ignored and hidden files and returned zero fixed-string matches for selected exact
    IDs, full labels, aliases and source titles. This is bounded to those terms, not
    an absence claim about every related phrase. Semantic scope comparisons distinguish
    the existing vanilla, FCFS, controlled-patience and per-length best-first decoders.
  search_scope: All 442 AIO labels/scoped synonyms and 146 preceding native IDs/names/aliases;
    both updated checkouts with ignored and hidden files included.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Exact CLASS definitions, synonyms and incident edges for NaturalLanguageProcessing
    and MathematicalFunction; related model/layer definitions for DecoderLLM, EncoderDecoderLLM
    and RandomTranslationLayer
  accessed_at: '2026-10-11T06:40:00Z'
  support: supports
  summary: All seven methods have related_match to NaturalLanguageProcessing, whose
    exact CLASS definition, NLP synonym and is_a MachineLearningTask edge were inspected.
    This is a method-to-domain relation grounded in the papers’ central neural-translation
    scope. DecoderLLM and EncoderDecoderLLM definitions denote learned model architectures,
    not the present search or scoring procedures. RandomTranslationLayer concerns
    image augmentation. MathematicalFunction was also inspected as a broad formula
    category; no equivalence to a generic function or exhaustive set of possible mappings
    is claimed. The four rescoring rules are typed mathematical_method, while the
    stopping decoder and two pruning procedures are algorithms.
- evidence_id: optimalstoppingbeamdecoding-0
  kind: primary_source
  reference: https://aclanthology.org/D17-1227.pdf
  locator: Sections 2–3, Equations (1)–(2), Theorems 1–2, printed p. 2135 / PDF p.
    2
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 7b9ed5e8c84207dbfdd8dbeaf9508f143ed72c2579856d7e72626e8f7d6d88c9
  support: supports
  summary: 'A layer-based sequence beam decoder that retains the best completed hypothesis
    seen so far and stops when the highest current prefix score cannot exceed that
    incumbent under a score that never increases with extension. Version: EMNLP 2017,
    printed pp. 2134–2139; published six-page ACL Anthology PDF. Actually inspected
    rendered PDF pages: 2, 3, 4.'
- evidence_id: optimalstoppingbeamdecoding-1
  kind: primary_source
  reference: https://aclanthology.org/D17-1227.pdf
  locator: Section 4 and Section 5.2 discussion, printed pp. 2136 and 2138 / PDF pp.
    3 and 5
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 7b9ed5e8c84207dbfdd8dbeaf9508f143ed72c2579856d7e72626e8f7d6d88c9
  support: supports
  summary: 'The unmodified probability objective can favor short translations; the
    source therefore introduces bounded length rewards. The stopping certificate is
    a search-score statement, not a quality guarantee. Version: EMNLP 2017, printed
    pp. 2134–2139; published six-page ACL Anthology PDF. Actually inspected rendered
    PDF pages: 2, 3, 4.'
- evidence_id: boundedlengthreward-0
  kind: primary_source
  reference: https://aclanthology.org/D17-1227.pdf
  locator: Section 4, score definition and Equations (3)–(4), printed pp. 2136–2137
    / PDF pp. 3–4
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 7b9ed5e8c84207dbfdd8dbeaf9508f143ed72c2579856d7e72626e8f7d6d88c9
  support: supports
  summary: 'A sequence scoring rule that adds a fixed nonnegative reward per generated
    position up to a finite length cap, giving score S(y)+r·min(l,|y|) instead of
    rewarding every additional position without bound. Version: EMNLP 2017, printed
    pp. 2134–2139; published six-page ACL Anthology PDF. Actually inspected rendered
    PDF pages: 2, 3, 4.'
- evidence_id: boundedlengthreward-1
  kind: primary_source
  reference: https://aclanthology.org/D18-1342.pdf
  locator: Section 4.1 Equation (7) and Section 4.2, printed p. 3056 / PDF p. 3
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 019ba14d74adfb3781eaa0211756f92dfbbf971ccdd9055daa4f20102ff8038f
  support: supports
  summary: 'The 2018 paper calls the fixed-rate capped rule bounded word-reward and
    distinguishes it from its predicted-length and adaptive-reward variants. Version:
    EMNLP 2018, printed pp. 3054–3059; published six-page ACL Anthology PDF. Actually
    inspected rendered PDF pages: 3, 4.'
- evidence_id: predictedlengthboundedreward-0
  kind: primary_source
  reference: https://aclanthology.org/D18-1342.pdf
  locator: Sections 4.2–4.2.1, Equations (8)–(9), printed p. 3056 / PDF p. 3
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 019ba14d74adfb3781eaa0211756f92dfbbf971ccdd9055daa4f20102ff8038f
  support: supports
  summary: 'A sequence rescoring method that adds a fixed word reward only up to an
    input-specific length predicted from encoder states, replacing a corpus-level
    generation-ratio cap with Lpred(x). Version: EMNLP 2018, printed pp. 3054–3059;
    published six-page ACL Anthology PDF. Actually inspected rendered PDF pages: 3,
    4.'
- evidence_id: boundedadaptivereward-0
  kind: primary_source
  reference: https://aclanthology.org/D18-1342.pdf
  locator: Section 4.2.2, Equations (10)–(11), and Section 5.2 final paragraph, printed
    pp. 3056–3057 / PDF pp. 3–4
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 019ba14d74adfb3781eaa0211756f92dfbbf971ccdd9055daa4f20102ff8038f
  support: supports
  summary: 'A beam-dependent sequence rescoring rule that adds per-step rewards derived
    from the beam’s mean negative log token probability, accumulating them only up
    to a predicted output-length cap. Version: EMNLP 2018, printed pp. 3054–3059;
    published six-page ACL Anthology PDF. Actually inspected rendered PDF pages: 3,
    4.'
- evidence_id: brevitypenaltynormalization-0
  kind: primary_source
  reference: https://aclanthology.org/D18-1342.pdf
  locator: Section 4.2.3 Equation (12), transformed score and Section 5.2 Equation
    (13), printed pp. 3056–3057 / PDF pp. 3–4
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 019ba14d74adfb3781eaa0211756f92dfbbf971ccdd9055daa4f20102ff8038f
  support: supports
  summary: 'A sequence rescoring rule that adds a predicted-length brevity penalty
    in log space to average token log probability: S(x,y)/|y| + min(1−Lpred(x)/|y|,0).
    Version: EMNLP 2018, printed pp. 3054–3059; published six-page ACL Anthology PDF.
    Actually inspected rendered PDF pages: 3, 4.'
- evidence_id: brevitypenaltynormalization-1
  kind: primary_source
  reference: https://aclanthology.org/D18-1342.pdf
  locator: Sections 5.2 and 6.1, printed pp. 3057–3058 / PDF pp. 4–5
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 019ba14d74adfb3781eaa0211756f92dfbbf971ccdd9055daa4f20102ff8038f
  support: supports
  summary: 'Equation (13) defines R as a maximum generation length, whereas the experiments
    identify it with predicted length. The bound is curated only when that value truly
    bounds the permitted completion lengths; prediction alone is not a mathematical
    upper bound. Version: EMNLP 2018, printed pp. 3054–3059; published six-page ACL
    Anthology PDF. Actually inspected rendered PDF pages: 3, 4.'
- evidence_id: absolutethresholdbeampruning-0
  kind: primary_source
  reference: https://aclanthology.org/W17-3207.pdf
  locator: Section 4, introductory paragraph and Absolute Threshold Pruning, Equation
    (2), printed p. 57 / PDF p. 2
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 7d157efa8f645f2de375076d3422891355ea921eb88ad35a38a1fa5070989ca0
  support: supports
  summary: 'A sequence-beam pruning procedure that first applies the beam-size cap,
    then discards candidates whose score is at least a specified positive margin below
    the best score in that capped candidate list. Version: First Workshop on Neural
    Machine Translation 2017, printed pp. 56–60; published five-page ACL Anthology
    PDF. Actually inspected rendered PDF pages: 2.'
- evidence_id: absolutethresholdbeampruning-1
  kind: primary_source
  reference: https://aclanthology.org/W17-3207.pdf
  locator: Section 5 discussion and Section 6, printed p. 58 / PDF p. 3
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 7d157efa8f645f2de375076d3422891355ea921eb88ad35a38a1fa5070989ca0
  support: supports
  summary: 'Additional pruning can change outputs by discarding a better-scoring hypothesis.
    The paper’s reported quality preservation and speed improvements are empirical
    outcomes in specific language-pair setups, not exact-search guarantees. Version:
    First Workshop on Neural Machine Translation 2017, printed pp. 56–60; published
    five-page ACL Anthology PDF. Actually inspected rendered PDF pages: 2.'
- evidence_id: pernodecandidatebeampruning-0
  kind: primary_source
  reference: https://aclanthology.org/W17-3207.pdf
  locator: Section 4, introductory paragraph and Maximum Candidates per Node, printed
    p. 57 / PDF p. 2
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 7d157efa8f645f2de375076d3422891355ea921eb88ad35a38a1fa5070989ca0
  support: supports
  summary: 'A sequence-beam pruning procedure that limits how many retained candidate
    extensions may come from the same predecessor hypothesis, discarding a candidate
    when the allowed number of better-scoring siblings is already retained. Version:
    First Workshop on Neural Machine Translation 2017, printed pp. 56–60; published
    five-page ACL Anthology PDF. Actually inspected rendered PDF pages: 2.'
- evidence_id: pernodecandidatebeampruning-1
  kind: primary_source
  reference: https://aclanthology.org/W17-3207.pdf
  locator: Introduction and Section 6, printed pp. 56 and 58 / PDF pp. 1 and 3
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 7d157efa8f645f2de375076d3422891355ea921eb88ad35a38a1fa5070989ca0
  support: supports
  summary: 'The source introduced a per-history candidate cap to diversify predecessor
    coverage, but its conclusion states that adding diversity did not improve translation
    quality in the evaluated settings. Version: First Workshop on Neural Machine Translation
    2017, printed pp. 56–60; published five-page ACL Anthology PDF. Actually inspected
    rendered PDF pages: 2.'
- evidence_id: score-boundary-analysis
  kind: record_content
  reference: research/validation/20261011T063749Z-score-boundary-examples.json
  locator: Two arithmetic examples with declared score domains and length assumptions;
    companion script research/validation/20261011T063749Z-score-boundary-examples.py
  accessed_at: '2026-10-11T06:40:00Z'
  snapshot_sha256: 905f0aa74e921dfd3317c920e82509fac33356f1847b706dc2118ca4b05ea023
  support: supports
  summary: For negative log scores -1,-2,-3 and ratio 0.6, literal multiplicative
    log pruning retains nothing, while probability-ratio pruning retains the best
    item. A BP-Norm completion longer than a predicted R can beat an incumbent after
    the prediction-based inequality would stop. These illustrate necessary assumptions,
    not author-code bugs or benchmark measurements.
assessments:
- assessment_id: optimalstoppingbeamdecoding
  area: evidence
  topic: Identity, scoring rule, stopping bound, pruning scope and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:OptimalStoppingBeamDecoding
  evidence_ids:
  - identity
  - mapping
  - optimalstoppingbeamdecoding-0
  - optimalstoppingbeamdecoding-1
  summary: This is Huang, Zhao and Ma’s 2017 optimal-ending procedure, with optimality
    explicitly limited by the retained beam. It differs from stopping on a completed
    top-ranked item without remembering earlier completions, from counting completed
    outputs, and from score-prioritized best-first expansion with per-length budgets.
    No normalized identity match was found across the 442 AIO and 146 prior native
    records; both checkout text searches included ignored and hidden files and returned
    no matches for the selected exact IDs, full labels, aliases and source titles.
  details: The certificate concerns descendants of retained beam prefixes. It does
    not recover prefixes pruned by finite width or guarantee global MAP decoding.
    A non-increasing extension score and a stored completed incumbent are required.
    Length normalization or positive rewards can invalidate the raw-prefix bound and
    need a different certificate. The paper compares stopping times under the same
    beam evolution and a specific historical top-completed baseline. It does not establish
    universally fastest decoding or current software defaults. Better model score
    does not imply better translation quality; the source reports short-output problems
    under pure probability scoring. Finite resource limits, absent EOS completions,
    empty beams and tie conventions need explicit implementation policies. No unconditional
    finite-time termination claim is made.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: The maintained definition denotes either a specified algorithm or
      a mathematical rescoring method, not a trained model instance or an empirical
      result.
    evidence_ids:
    - optimalstoppingbeamdecoding-0
    - optimalstoppingbeamdecoding-1
  - name: aio-assessment
    value: 'related_match: NaturalLanguageProcessing'
    definition: All mappings are non-hierarchical method-to-domain relationships grounded
      in the primary papers’ central natural-language generation setting.
    evidence_ids:
    - mapping
    - identity
- assessment_id: boundedlengthreward
  area: evidence
  topic: Identity, scoring rule, stopping bound, pruning scope and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:BoundedLengthReward
  evidence_ids:
  - identity
  - mapping
  - boundedlengthreward-0
  - boundedlengthreward-1
  summary: The cap limits how much reward can accumulate; it is not itself a maximum
    allowed output length. This is the bounded reward in Huang et al. 2017, called
    bounded word-reward by Yang et al. 2018. It differs from division by output length,
    an uncapped word reward and a reward rate recomputed from beam statistics. No
    normalized identity match was found across the 442 AIO and 146 prior native records;
    both checkout text searches included ignored and hidden files and returned no
    matches for the selected exact IDs, full labels, aliases and source titles.
  details: The score is a decoding preference, not a probability distribution or an
    intrinsic translation-quality measure. The reward rate and length-cap estimate
    require specification. A development-set average length ratio need not transfer
    to every sentence or domain. The stopping bound assumes non-increasing log probability,
    nonnegative fixed reward and a fixed finite cap for the input; its beam-relative
    guarantee does not undo finite-width pruning. Reward saturation does not prohibit
    outputs longer than the cap. Tokenization, length counting and EOS handling must
    be specified in an implementation. No numerical BLEU improvement, universal quality
    advantage or current implementation behavior is asserted.
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: The maintained definition denotes either a specified algorithm or
      a mathematical rescoring method, not a trained model instance or an empirical
      result.
    evidence_ids:
    - boundedlengthreward-0
    - boundedlengthreward-1
  - name: aio-assessment
    value: 'related_match: NaturalLanguageProcessing'
    definition: All mappings are non-hierarchical method-to-domain relationships grounded
      in the primary papers’ central natural-language generation setting.
    evidence_ids:
    - mapping
    - identity
- assessment_id: predictedlengthboundedreward
  area: evidence
  topic: Identity, scoring rule, stopping bound, pruning scope and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:PredictedLengthBoundedReward
  evidence_ids:
  - identity
  - mapping
  - predictedlengthboundedreward-0
  summary: This is Yang et al.’s predicted-length bounded word-reward variant. It
    changes the cap, while retaining a separately tuned reward rate r. It is not the
    beam-statistic adaptive reward or the brevity-penalty normalized score, and it
    is not a standalone trained length-predictor instance. No normalized identity
    match was found across the 442 AIO and 146 prior native records; both checkout
    text searches included ignored and hidden files and returned no matches for the
    selected exact IDs, full labels, aliases and source titles.
  details: The method still requires a learned length predictor and a tuned reward
    rate; replacing the corpus ratio does not make the complete system parameter-free.
    Predicted length is a reward cap, not automatically an enforced maximum sequence
    length or an accurate target for every input. A usable nonnegative length prediction,
    tokenizer conventions and integration with the decoder must be specified. The
    paper passage does not provide a complete predictor training or calibration protocol.
    Finite beam width still prunes hypotheses. Neither accurate length prediction
    nor a stopping certificate implies globally optimal output or universally better
    translation quality. The empirical source scope is Chinese-to-English news translation;
    no numerical result is curated.
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: The maintained definition denotes either a specified algorithm or
      a mathematical rescoring method, not a trained model instance or an empirical
      result.
    evidence_ids:
    - predictedlengthboundedreward-0
  - name: aio-assessment
    value: 'related_match: NaturalLanguageProcessing'
    definition: All mappings are non-hierarchical method-to-domain relationships grounded
      in the primary papers’ central natural-language generation setting.
    evidence_ids:
    - mapping
    - identity
- assessment_id: boundedadaptivereward
  area: evidence
  topic: Identity, scoring rule, stopping bound, pruning scope and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:BoundedAdaptiveReward
  evidence_ids:
  - identity
  - mapping
  - boundedadaptivereward-0
  summary: Yang et al.’s bounded adaptive-reward changes the reward rate with the
    decoding step, unlike fixed-r bounded word-reward. It is a beam-conditioned scoring
    method rather than a reinforcement-learning reward-training algorithm or a beam-independent
    probability model. No normalized identity match was found across the 442 AIO and
    146 prior native records; both checkout text searches included ignored and hidden
    files and returned no matches for the selected exact IDs, full labels, aliases
    and source titles.
  details: The reward sequence depends on the beam and model probabilities. Changing
    beam policy can change the score assigned to a completed hypothesis. Removing
    a manually tuned constant reward rate does not remove the trained translation
    model, length predictor, beam size or other implementation choices. The printed
    sum uses a predicted length as its upper limit without specifying a noninteger
    rounding policy. A discrete implementation must define the effective integer cap
    and EOS/token counting; the record does not assert an author-approved rounding
    convention. Equation (10) assumes b available beam entries and defined token log
    probabilities. Empty or shrunken beams and zero-probability tokens require an
    explicit policy. The stated stopping argument applies after reward saturation
    with a completed incumbent. It is limited to retained beam continuations, not
    global sequence optimality or guaranteed quality improvement.
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: The maintained definition denotes either a specified algorithm or
      a mathematical rescoring method, not a trained model instance or an empirical
      result.
    evidence_ids:
    - boundedadaptivereward-0
  - name: aio-assessment
    value: 'related_match: NaturalLanguageProcessing'
    definition: All mappings are non-hierarchical method-to-domain relationships grounded
      in the primary papers’ central natural-language generation setting.
    evidence_ids:
    - mapping
    - identity
- assessment_id: brevitypenaltynormalization
  area: evidence
  topic: Identity, scoring rule, stopping bound, pruning scope and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:BrevityPenaltyNormalization
  evidence_ids:
  - identity
  - mapping
  - brevitypenaltynormalization-0
  - brevitypenaltynormalization-1
  summary: BP-Norm is Yang et al.’s predicted-length decoding score. It resembles
    the algebraic structure of BLEU’s brevity penalty but does not compute n-gram
    precision, use an actual reference translation at inference, or equal the BLEU
    evaluation metric. It differs from plain average log probability and additive
    word rewards. No normalized identity match was found across the 442 AIO and 146
    prior native records; both checkout text searches included ignored and hidden
    files and returned no matches for the selected exact IDs, full labels, aliases
    and source titles.
  details: Lpred is a prediction, not a reference length or a proven upper bound on
    output length. The S_t/R stopping bound requires that admissible completions actually
    have length at most R. The experiments set R to the predicted length. This supports
    the stopping guarantee only under an enforced length cap or another justification
    that all allowed completions obey that bound; a forecast alone is insufficient.
    The formula requires nonempty hypotheses and a valid length prediction. A BOS-only
    prefix needs separate handling; length and EOS conventions must be specified.
    The score is neither a normalized probability nor BLEU itself. Improved search
    score does not imply better human translation quality. The source’s hyperparameter-free
    comparison concerns removal of a separately tuned reward constant, not absence
    of trained models, a length predictor or decoding choices. Finite beam pruning
    remains approximate.
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: The maintained definition denotes either a specified algorithm or
      a mathematical rescoring method, not a trained model instance or an empirical
      result.
    evidence_ids:
    - brevitypenaltynormalization-0
    - brevitypenaltynormalization-1
  - name: aio-assessment
    value: 'related_match: NaturalLanguageProcessing'
    definition: All mappings are non-hierarchical method-to-domain relationships grounded
      in the primary papers’ central natural-language generation setting.
    evidence_ids:
    - mapping
    - identity
- assessment_id: absolutethresholdbeampruning
  area: evidence
  topic: Identity, scoring rule, stopping bound, pruning scope and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:AbsoluteThresholdBeamPruning
  evidence_ids:
  - identity
  - mapping
  - absolutethresholdbeampruning-0
  - absolutethresholdbeampruning-1
  summary: This is Freitag and Al-Onaizan’s absolute threshold pruning rule. It uses
    an additive score difference, unlike their relative-score and last-token relative
    thresholds. It is an additional local pruning step, not a stopping certificate
    or a method that automatically widens the beam. No normalized identity match was
    found across the 442 AIO and 146 prior native records; both checkout text searches
    included ignored and hidden files and returned no matches for the selected exact
    IDs, full labels, aliases and source titles.
  details: The extra pruning can remove a prefix leading to the best eventual output.
    The paper explicitly reports search errors even where aggregate task metrics remain
    similar. The numerical margin depends on score scale, log base and model calibration.
    It is not a relative probability threshold. A positive margin is required to retain
    the best finite-scoring item under the printed non-strict inequality; a zero margin
    would discard even maximum-score candidates. The procedure is layered onto a decoder
    with its own EOS and width policy. It does not by itself specify the entire decoder
    or guarantee improved speed or quality. The separate relative-pruning equations
    have a score-scale ambiguity under negative log scores. No correction to those
    distinct variants is inferred from this additive rule.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: The maintained definition denotes either a specified algorithm or
      a mathematical rescoring method, not a trained model instance or an empirical
      result.
    evidence_ids:
    - absolutethresholdbeampruning-0
    - absolutethresholdbeampruning-1
  - name: aio-assessment
    value: 'related_match: NaturalLanguageProcessing'
    definition: All mappings are non-hierarchical method-to-domain relationships grounded
      in the primary papers’ central natural-language generation setting.
    evidence_ids:
    - mapping
    - identity
- assessment_id: pernodecandidatebeampruning
  area: evidence
  topic: Identity, scoring rule, stopping bound, pruning scope and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:PerNodeCandidateBeamPruning
  evidence_ids:
  - identity
  - mapping
  - pernodecandidatebeampruning-0
  - pernodecandidatebeampruning-1
  summary: This is the Maximum Candidates per Node rule of Freitag and Al-Onaizan.
    Same history means the common predecessor prefix, not arbitrary semantic similarity
    between full sequences. It differs from an additive diversity penalty, grouping
    beams into separate searches or imposing a global frontier capacity. No normalized
    identity match was found across the 442 AIO and 146 prior native records; both
    checkout text searches included ignored and hidden files and returned no matches
    for the selected exact IDs, full labels, aliases and source titles.
  details: A positive integer per-parent cap and deterministic tie handling must be
    specified. The source’s prose refers to better-scoring candidates without a complete
    tie policy. Limiting sibling extensions can remove the prefix of the best eventual
    sequence; this is not an exact or complete search guarantee. More varied parent
    prefixes do not guarantee semantic diversity or improved translation quality.
    The paper’s conclusion reports no translation-quality improvement from this diversity
    intervention. The inherited decoder determines EOS processing, generation length
    and changing active-beam width. The pruning rule alone is not a complete decoder
    implementation. No specific current library implementation, numeric quality gain
    or universal runtime benefit is asserted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: The maintained definition denotes either a specified algorithm or
      a mathematical rescoring method, not a trained model instance or an empirical
      result.
    evidence_ids:
    - pernodecandidatebeampruning-0
    - pernodecandidatebeampruning-1
  - name: aio-assessment
    value: 'related_match: NaturalLanguageProcessing'
    definition: All mappings are non-hierarchical method-to-domain relationships grounded
      in the primary papers’ central natural-language generation setting.
    evidence_ids:
    - mapping
    - identity
- assessment_id: adversarial-stopping
  area: scope
  topic: Conditions needed for beam-relative stopping guarantees
  outcome: supported
  target_ids:
  - AIMech:OptimalStoppingBeamDecoding
  - AIMech:BoundedLengthReward
  - AIMech:PredictedLengthBoundedReward
  - AIMech:BoundedAdaptiveReward
  - AIMech:BrevityPenaltyNormalization
  evidence_ids:
  - optimalstoppingbeamdecoding-0
  - boundedlengthreward-0
  - predictedlengthboundedreward-0
  - boundedadaptivereward-0
  - brevitypenaltynormalization-0
  - brevitypenaltynormalization-1
  - score-boundary-analysis
  summary: The records distinguish a raw monotone score bound, a fixed remaining reward
    bound, an input-conditioned reward cap, reward saturation after a beam-dependent
    sum, and the true maximum-length assumption for BP-Norm.
  details: An incumbent is required before stopping. No certificate recovers width-pruned
    prefixes. Reward saturation does not prohibit long outputs, and a length forecast
    is not automatically a maximum. Integer cap/EOS conventions for the adaptive sum
    remain explicit implementation limitations rather than invented source details.
    Optimality refers to the adjusted scoring objective within retained beam continuations,
    not universal translation quality.
- assessment_id: adversarial-pruning
  area: evidence
  topic: Local pruning changes the candidate set without an exact-search guarantee
  outcome: supported
  target_ids:
  - AIMech:AbsoluteThresholdBeamPruning
  - AIMech:PerNodeCandidateBeamPruning
  evidence_ids:
  - absolutethresholdbeampruning-0
  - absolutethresholdbeampruning-1
  - pernodecandidatebeampruning-0
  - pernodecandidatebeampruning-1
  - score-boundary-analysis
  summary: Both added pruning rules follow the paper’s initial beam-size cut. Absolute
    pruning uses a positive additive score margin with the printed inclusive discard
    boundary; per-parent pruning limits sibling continuations.
  details: The definitions do not imply automatic beam widening, refilling, semantic
    diversity or improved task quality. Search errors and the source’s negative diversity-quality
    conclusion are retained. Relative-score variants remain separate deferred candidates
    until their score domain is established.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:OptimalStoppingBeamDecoding
  - AIMech:BoundedLengthReward
  - AIMech:PredictedLengthBoundedReward
  - AIMech:BoundedAdaptiveReward
  - AIMech:BrevityPenaltyNormalization
  - AIMech:AbsoluteThresholdBeamPruning
  - AIMech:PerNodeCandidateBeamPruning
  evidence_ids:
  - identity
  - mapping
  - optimalstoppingbeamdecoding-0
  - optimalstoppingbeamdecoding-1
  - boundedlengthreward-0
  - boundedlengthreward-1
  - predictedlengthboundedreward-0
  - boundedadaptivereward-0
  - brevitypenaltynormalization-0
  - brevitypenaltynormalization-1
  - absolutethresholdbeampruning-0
  - absolutethresholdbeampruning-1
  - pernodecandidatebeampruning-0
  - pernodecandidatebeampruning-1
  - score-boundary-analysis
  rationale: The raw stopping certificate, fixed capped reward, predicted cap, adaptive
    per-step reward, brevity-penalty normalization, additive score-gap pruning and
    per-parent candidate limit define different methods. Predicted-cap scoring specializes
    capped reward; this overlap is explicit and is not equivalence. The scoring formulas
    are mathematical methods, while traversal/stopping and candidate-removal procedures
    are algorithms. No local method is equated to the broad NLP task.
limitations:
- Adversarial author self-review, not independent approval; all seven records remain
  DRAFT.
- The scope is paper-defined methods, not reproduction of author implementations or
  current library behavior.
- No unconditional global sequence-optimality, runtime or quality guarantee is asserted.
  Finite beam pruning remains approximate.
- BP-Norm’s S_t/R bound requires a genuine maximum permitted length; the curator example
  only challenges substituting an unenforced forecast.
- Relative-score ambiguity and adaptive reward rounding/EOS details are preserved;
  no author-approved correction is claimed.
- Repeated citations to passages in the same primary paper are not independent studies.
- 'Minor terminology refinements were made before this saved assessment: method-to-domain
  mapping prose and exact non-increase under nonpositive log-probability increments.'
- All required checks passed. This review covers only the seven declared targets and
  does not retire unrelated historical findings or establish search saturation.
tags:
- native-concepts
- sequence-decoding
- rescoring
- pruning
- primary-papers
- self-review
- discovery-ongoing
```
