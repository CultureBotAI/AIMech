"""Curator arithmetic illustrations of score-domain and length-bound assumptions.

These calculations do not execute any author decoder or establish a source erratum.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import math

scores = [-1.0, -2.0, -3.0]
ratio = 0.6
literal_cutoff = ratio * max(scores)
literal_kept = [s for s in scores if s > literal_cutoff]
probability_kept = [s for s in scores if math.exp(s) > ratio * math.exp(max(scores))]
log_equivalent_kept = [s for s in scores if s > max(scores) + math.log(ratio)]
assert literal_kept == []
assert probability_kept == log_equivalent_kept == [-1.0]

def bp_norm(log_score, length, predicted_length):
    return log_score / length + min(1 - predicted_length / length, 0)

predicted_length = 5
prefix_length, prefix_log_score = 4, -10.0
incumbent_length, incumbent_log_score = 3, -3.4
completion_length, completion_log_score = 10, -10.1
incumbent = bp_norm(incumbent_log_score, incumbent_length, predicted_length)
assumed_bound = prefix_log_score / predicted_length
long_completion = bp_norm(completion_log_score, completion_length, predicted_length)
assert completion_log_score <= prefix_log_score
assert assumed_bound <= incumbent < long_completion

out = {
    'created_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'authorship': 'Curator arithmetic illustrations; not author code',
    'relative_threshold': {
        'source': 'https://aclanthology.org/W17-3207.pdf',
        'locator': 'Section 3 and Section 4 Equation (1), printed p. 57 / PDF p. 2',
        'log_scores': scores, 'ratio': ratio,
        'literal_log_score_cutoff': literal_cutoff,
        'literal_log_score_survivors': literal_kept,
        'probability_ratio_survivors_in_log_coordinates': probability_kept,
        'log_equivalent_cutoff': max(scores) + math.log(ratio),
        'interpretation': 'Multiplying a negative maximum log score by a ratio below one would remove every item under the printed non-strict discard rule. Applying that ratio to probabilities is different and keeps the best item in this example. The paper needs an explicit score-domain interpretation; this calculation does not establish which domain the authors implemented.'
    },
    'predicted_length_is_not_a_maximum': {
        'source': 'https://aclanthology.org/D18-1342.pdf',
        'locator': 'Section 5.2 Equation (13) and Section 6.1, printed pp. 3057–3058 / PDF pp. 4–5',
        'predicted_length': predicted_length,
        'prefix': {'length': prefix_length, 'log_score': prefix_log_score},
        'incumbent': {'length': incumbent_length, 'log_score': incumbent_log_score, 'bp_norm': incumbent},
        'longer_completion': {'length': completion_length, 'log_score': completion_log_score, 'bp_norm': long_completion},
        'bound_if_prediction_is_used_as_R': assumed_bound,
        'interpretation': 'Using predicted length as R would certify stopping here, yet an allowed longer completion can beat the incumbent despite lower raw log probability. If the decoder truly enforces R as its maximum permitted length, that longer completion is excluded and this example does not contradict the bound.'
    },
    'limitations': [
        'Arithmetic examples only; no author implementation, trained model, benchmark or full decoder was run.',
        'The relative-score calculation demonstrates a domain ambiguity, not a verified author bug or correction.',
        'The BP-Norm calculation concerns a forecast used without a genuine length cap; the valid maximum-length theorem is not challenged.',
        'Numerical values are illustrative curator inputs, not reported measurements.'
    ],
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
print(json.dumps(out, indent=2))
