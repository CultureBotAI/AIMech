# WIS-GTD, usage-based TD and accumulating Sarsa

2026-10-15T18:58:39Z

- AIMech:WISGTDLambda
- AIMech:UsageBasedTDLambda
- AIMech:UsageBasedTrueOnlineTDLambda
- AIMech:AccumulatingSarsaLambda

WIS-GTD(lambda) is the source-defined linear off-policy prediction host with an importance-weighted accumulating trace, usage-adapted main steps and a separate scalar auxiliary step. Both main and auxiliary right sides use old auxiliary weights. On-policy beta=0 reduction additionally needs a zero initial auxiliary vector; usage-step correspondence is not an arbitrary main-weight or objective-gradient equivalence.

Usage-based TD(lambda) combines the on-policy feature-usage schedule with ordinary accumulating TD. Usage-based true online TD(lambda) instead places the changing componentwise steps inside a scaled Dutch trace and uses the previous weight vector’s current-feature prediction. Their zero-decay agreement does not establish whole-method equivalence. Finite-horizon source-defined correspondence and endpoint algebra do not establish convergence, stable weights or exact Monte Carlo averaging for arbitrary histories.

Accumulating Sarsa(lambda) selects the corrected episodic tabular on-policy control procedure from Sutton and Barto 1998. Its next action is selected before the value update and carried forward. The separately acquired official errata moves trace zeroing inside the episode loop. Linked formula images have their own checksums; the neighboring replacing-display conflict is retained as context rather than used to redefine the selected accumulating rule.

The three WIS/usage records reuse one exact combined author paper artifact. The Sarsa record declares eight source rows: seven components of one monograph plus official errata. Across the cohort this is eleven declared rows, nine distinct artifacts and two primary works plus the errata document, not eleven independent publications. Source-local versions, acquisition times, partial reading scopes and hand analyses remain attributed. None of these records certifies source code, a complete proof or benchmark reproduction.

The accepted previews retain twenty-four source-linked claims, twenty-eight limitations and qualified related ReinforcementLearning mappings. Historical identity notes remain dated research evidence. The writer requires separate actual merged-base identity assessment and decisions, refreshes only identity notes and actual curation timestamps, and preserves every accepted scientific field. Owners 264 and 265 remain partial; neither source-family exhaustion nor independent approval is asserted.

Current source-lead assessment: The inspected 2015 paper separately specifies WIS-GTD, usage-based TD and usage-based true online TD; the inspected first-edition monograph and official errata support corrected episodic accumulating Sarsa. These are four distinct methods under existing owners264 and265. The subsequent WIS-TO-GTD dossier has located commit-pinned author implementation evidence and explicitly retains its correction-history, zero-reciprocal and episode-state differences from the printed algorithm; a qualified draft is being assessed separately, not asserted as a record or formal erratum here. General eligibility organization, soft-cut, other usage/importance-sampling and control variants and the owner266 precursor remain residual work. No new frontier leaf is needed for these bounded findings and no source-family exhaustion is claimed.

Existing owners 264 and 265 were updated in place and remain partially addressed. Their prior IDs and resolution objects, all 907 other main objects and all 393 nested objects remain unchanged. No frontier leaf was appended. Records remain DRAFT; no gate or formal-review completion is claimed.
