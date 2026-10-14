# Scientific author self-review of Nonreversible Metropolis uniform update

- Review: 20261014T204029Z-nonreversible-metropolis-uniform-update
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T20:24:25Z
- Finished UTC: 2026-10-14T20:40:29Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the persistent signed-threshold algorithm as DRAFT with a related Markov-process mapping. Its invariant construction is supported under the explicit proposal and target assumptions; ergodicity, transient acceptance and universal efficiency remain outside the claim.

## Scope And Provenance

All maintained fields of the selected record; Root evidence scope: all 14 pages of the author-hosted Neal 2020 report, including references and appendix scripts, with visual method/figure pages 2,4,5,6. No journal version is involved; byte equivalence to the arXiv PDF was not established.

Selection: Exact maintained ID: AIMech:NonreversibleMetropolisUniformUpdate
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ac6b62150c25ab02e880b50008cbfb5a56a109f8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:NonreversibleMetropolisUniformUpdate | data/curated/NonreversibleMetropolisUniformUpdate.yaml | maintained | Nonreversible Metropolis uniform update |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:NonreversibleMetropolisUniformUpdate | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 421.69s (0:07:01)<br>Checked 442 record(s); 0 failed.<br>Checked 703 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 394 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 395,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:NonreversibleMetropolisUniformUpdate | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:NonreversibleMetropolisUniformUpdate | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:NonreversibleMetropolisUniformUpdate | Actual command exited 0 without output. |
| just render | passed | True | AIMech:NonreversibleMetropolisUniformUpdate | Rendered AIMech site under /private/tmp/aimech-discovery-recovery-worktree-20261012/pages<br>uv run --locked python scripts/render_pages.py<br> |
| just render-check | passed | True | AIMech:NonreversibleMetropolisUniformUpdate | pages/ is current<br>uv run --locked python scripts/render_pages.py --check<br> |
| python3 research/discovery/nonreversible-boundaries.py | passed | True | AIMech:NonreversibleMetropolisUniformUpdate | {<br>  "scope": "Exact deterministic original calculations, not author implementation, empirical reproduction, general proof, or independent scientific approval.",<br>  "neal2020": {<br>    "assumptions": "Positive finite target, symmetric stochastic proposal independent of signed v; exact continuous piecewise densities; shift/noise independent of v. Endpoint choices have measure zero.",<br>    "target": [<br>      "1/3",<br>      "2/3"<br>    ],<br>    "proposal": [<br>      [<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "1",<br>        "0"<br>      ]<br>    ],<br>    "derived_correct_joint_density": [<br>      [<br>        0,<br>        "-1",<br>        "1",<br>        "1/6"<br>      ],<br>      [<br>        1,<br>        "-1",<br>        "1",<br>        "1/3"<br>      ]<br>    ],<br>    "derived_omitted_rescale_first_density": [<br>      [<br>        0,<br>        "-1/2",<br>        "1/2",<br>        "1/3"<br>      ],<br>      [<br>        1,<br>        "-1",<br>        "-1/2",<br>        "1/2"<br>      ],<br>      [<br>        1,<br>        "-1/2",<br>        "1/2",<br>        "1/6"<br>      ],<br>      [<br>        1,<br>        "1/2",<br>        "1",<br>        "1/2"<br>      ]<br>    ],<br>    "derived_omitted_rescale_second_density": [<br>      [<br>        0,<br>        "-1/2",<br>        "1/2",<br>        "1/6"<br>      ],<br>      [<br>        1,<br>        "-1",<br>        "-1/2",<br>        "1/2"<br>      ],<br>      [<br>        1,<br>        "-1/2",<br>        "1/2",<br>        "1/3"<br>      ],<br>      [<br>        1,<br>        "1/2",<br>        "1",<br>        "1/2"<br>      ]<br>    ],<br>    "omitted_rescale_second_state0_mass": "1/6",<br>    "half_period_composition_flux": {<br>      "A": [<br>        [<br>          0,<br>          "0",<br>          "1/4",<br>          "1/6"<br>        ]<br>      ],<br>      "B": [<br>        [<br>          1,<br>          "-1/2",<br>          "-3/8",<br>          "1/3"<br>        ]<br>      ],<br>      "A_to_B": "1/24",<br>      "B_to_A": "0"<br>    },<br>    "full_refresh_composition_flux": {<br>      "A": [<br>        [<br>          0,<br>          "0",<br>          "1/4",<br>          "1/6"<br>        ]<br>      ],<br>      "B": [<br>        [<br>          1,<br>          "0",<br>          "1/8",<br>          "1/3"<br>        ]<br>      ],<br>      "A_to_B": "1/192",<br>      "B_to_A": "1/384"<br>    },<br>    "asymmetric_proposal_negative_control": {<br>      "proposal": [<br>        [<br>          "1/2",<br>          "1/2"<br>        ],<br>        [<br>          "1",<br>          "0"<br>        ]<br>      ],<br>      "output_density": [<br>        [<br>          0,<br>          "-1",<br>          "1",<br>          "1/4"<br>        ],<br>        [<br>          1,<br>          "-1",<br>          "-1/2",<br>          "1/3"<br>        ],<br>        [<br>          1,<br>          "-1/2",<br>          "1/2",<br>          "1/6"<br>        ],<br>        [<br>          1,<br>          "1/2",<br>          "1",<br>          "1/3"<br>        ]<br>      ],<br>      "state0_mass": "1/2"<br>    },<br>    "joint_invariance_family_cases": 576,<br>    "boundary": "A half-period wrapped translation is reversible by itself, yet translation-then-accept can be nonreversible. Full uniform refresh recovers ordinary Metropolis for x, but does not ensure augmented-chain detailed balance. Zero shift/no noise leaves the under-density height fixed and supplies no ergodicity guarantee."<br>  },<br>  "neal2004": {<br>    "assumptions": "Finite reversible baseline, positive invariant mass, positive-support pair states; Liu conditional point-mass boundary handled explicitly. The variance calculation is applied only after verifying expanded irreducibility.",<br>    "triangle": {<br>      "base": [<br>        [<br>          "0",<br>          "1/2",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "0",<br>          "1/2"<br>        ],<br>        [<br>          "1/2",<br>          "1/2",<br>          "0"<br>        ]<br>      ],<br>      "pi": [<br>        "1/3",<br>        "1/3",<br>        "1/3"<br>      ],<br>      "expanded_states": [<br>        [<br>          0,<br>          1<br>        ],<br>        [<br>          0,<br>          2<br>        ],<br>        [<br>          1,<br>          0<br>        ],<br>        [<br>          1,<br>          2<br>        ],<br>        [<br>          2,<br>          0<br>        ],<br>        [<br>          2,<br>          1<br>        ]<br>      ],<br>      "expanded_invariant": [<br>        "1/6",<br>        "1/6",<br>        "1/6",<br>        "1/6",<br>        "1/6",<br>        "1/6"<br>      ],<br>      "expanded_transition": [<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "1",<br>          "0"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "0",<br>          "0",<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "closed_classes": [<br>        [<br>          [<br>            0,<br>            1<br>          ],<br>          [<br>            1,<br>            2<br>          ],<br>          [<br>            2,<br>            0<br>          ]<br>        ],<br>        [<br>          [<br>            0,<br>            2<br>          ],<br>          [<br>            1,<br>            0<br>          ],<br>          [<br>            2,<br>            1<br>          ]<br>        ]<br>      ],<br>      "boundary": "Base is irreducible (also aperiodic); the lift has two closed orientation cycles. Each class in this example still has the correct projected marginal; this refutes automatic expanded irreducibility, not projected correctness for this particular example."<br>    },<br>    "point_mass_conditional": {<br>      "expanded_states": [<br>        [<br>          0,<br>          1<br>        ],<br>        [<br>          1,<br>          0<br>        ]<br>      ],<br>      "expanded_transition": [<br>        [<br>          "0",<br>          "1"<br>        ],<br>        [<br>          "1",<br>          "0"<br>        ]<br>      ],<br>      "expanded_invariant": [<br>        "1/2",<br>        "1/2"<br>      ]<br>    },<br>    "printed_fast_simulator": {<br>      "conditional": [<br>        "3/5",<br>        "3/10",<br>        "1/10"<br>      ],<br>      "current_index": 0,<br>      "proposal_index": 1,<br>      "printed_acceptance": "10/7",<br>      "equation16_conditional_row": [<br>        "29/63",<br>        "3/7",<br>        "1/9"<br>      ],<br>      "clipped_transition": "3/10",<br>      "equation16_transition": "3/7",<br>      "boundary": "Neal2004 p.9 probability exceeds one as printed; clipping fails to implement p.8 Eq.(16). The conditional-proposal construction implements Eq.(16), but can be costly if the excluded mass is near one."<br>    },<br>    "positive_conductance_family_cases": 54,<br>    "single_coordinate_variance_comparisons": 162,<br>    "strict_variance_improvements": 162,<br>    "first_family_example": {<br>      "base": [<br>        [<br>          "1/3",<br>          "1/3",<br>          "1/3"<br>        ],<br>        [<br>          "1/3",<br>          "1/3",<br>          "1/3"<br>        ],<br>        [<br>          "1/3",<br>          "1/3",<br>          "1/3"<br>        ]<br>      ],<br>      "pi": [<br>        "1/3",<br>        "1/3",<br>        "1/3"<br>      ],<br>      "indicator_comparisons": [<br>        {<br>          "coordinate_indicator": 0,<br>          "baseline_asymptotic_variance": "2/9",<br>          "expanded_asymptotic_variance": "2/27"<br>        },<br>        {<br>          "coordinate_indicator": 1,<br>          "baseline_asymptotic_variance": "2/9",<br>          "expanded_asymptotic_variance": "2/27"<br>        },<br>        {<br>          "coordinate_indicator": 2,<br>          "baseline_asymptotic_variance": "2/9",<br>          "expanded_asymptotic_variance": "2/27"<br>        }<br>      ]<br>    },<br>    "boundary": "The finite checks illustrate invariance, local balance, suppression, and the corrected variance boundary; they are not a general theorem or a speed claim."<br>  }<br>}<br> |

## Scientific And Domain Assessments

### Nonreversible Metropolis uniform update

identity: supported. Targets: AIMech:NonreversibleMetropolisUniformUpdate.

Retain the distinct DRAFT algorithm within the searched corpus and scope.

Retain a distinct algorithm identity for persistent signed acceptance-threshold memory plus the required accepted-state density rescaling. This is not a new name for general Metropolis–Hastings, a random-walk proposal, Barker’s scalar acceptance function, or a generic nonreversible sampler. Shared under-density augmentation does not equate it with fresh-height slice sampling. The momentum application is distinct from HMC and position-only MALA; the latter has an asymmetric proposal correction that this simple ratio cannot replace. Persistent contrastive-divergence particles evolve during model learning and do not supply this fixed-target identity. AIS and tempered transitions may use related kernels but have different path and estimator identities. Generic terminology and broad paper titles are broader than this algorithm and do not justify exact aliases.

### Related Markov-process mapping

grounding: supported. Targets: AIMech:NonreversibleMetropolisUniformUpdate.

The related_match assessment is supported without equivalence or inherited ontology assertions.

Retain only related_match to AIO:MarkovChain. Each algorithm constructs a first-order Markov transition on an augmented state and preserves a specified original-state marginal, so a method-to-process relationship has mechanistic support. The pinned target is exported as a stochastic model under Network, with a ProbabilisticHiddenLayer has-part assertion. Neither equivalence, subclass status nor inheritance of those assertions is warranted. The source/mapping handoff inspected twelve complete CLASS contexts, incident edges and generated records, including the target and the eleven alternatives documented here.
Alternative target decisions:
AIO:Network: A network architecture or interconnected-entity system is not the identity of either transition algorithm. A graph representation of a Markov process does not establish equivalence or a broader-class mapping to Network.
AIO:ProbabilisticHiddenLayer: Neither construction is a neural-network hidden layer estimating category probabilities. The exported MarkovChain has-part edge is contextual ontology structure, not an inherited claim about these local algorithms.
AIO:MathematicalFunction: Both identities include a stochastic state evolution, auxiliary memory and an invariant distribution. The presence of update equations does not make either merely an input-output mathematical function or justify a broad_match.
AIO:Model: The target statistical distribution is an input to the procedure. The transition algorithm is distinct from a statistical model family or explanatory system model.
AIO:BoltzmannMachineNetwork: A Boltzmann machine can be a sampling application, but no recurrent neural-network or Boltzmann-machine architecture is required by either mechanism.
AIO:BayesianNetwork: Neither mechanism requires a directed acyclic dependency graph. Bayesian inference applications, including the 2020 Bayesian neural network, do not identify a Bayesian-network DAG.
AIO:ProbabilisticGraphicalModel: A graphical target distribution is optional. The generic transition construction is not the pinned graphical-model task/model identity.
AIO:Normalization: The pinned class concerns data scaling or formatting. The 2020 auxiliary-variable rescaling and stochastic-row normalization are different mathematical operations.
AIO:SelectionAndSamplingBias: Representativeness bias in data selection is not the identity of a target-preserving MCMC transition. Temporal dependence and stationary-measure correctness do not supply this mapping.
AIO:DataPreparation: The procedures simulate from fixed target distributions; they do not specify raw-data cleaning, assembly or preprocessing.
AIO:ReinforcementLearning: Neither method defines learning from rewards, a policy objective or an exploration/exploitation learning problem. Directional state movement in MCMC is insufficient.

### joint-target-and-wrapped-update

evidence: supported. Targets: AIMech:NonreversibleMetropolisUniformUpdate.

Supported within the stated assumptions, inspected passages and finite-calculation scope.

The product target is justified by the change from height s to normalized magnitude abs(v); signed v retains the direction needed by the wrapped update. A fixed translation on the circle has unit Jacobian, and a mixture of translations whose noise law does not depend on current v preserves conditional uniform measure. This supports invariance of that substep, not irreducibility or detailed balance of every full composition. This regular construction assumes a proper positive target on its proposal state space.

### accepted-state-rescaling

evidence: supported. Targets: AIMech:NonreversibleMetropolisUniformUpdate.

Supported within the stated assumptions, inspected passages and finite-calculation scope.

For an accepted x-to-y move, the inverse Jacobian of v_new=v_old*pi(x)/pi(y) is pi(y)/pi(x). Joint input density pi(x)/2 times q(x,y) therefore becomes pi(y)*q(x,y)/2, matching the reverse contribution under symmetric q independent of v. Rejection retains both state components. Omitting the rescaling breaks the product joint law even when a one-step x-marginal check happens to pass. The independent-of-v assumption matters because the reverse state has a rescaled threshold. The explicit asymmetric-proposal counterexample prevents extending the target-ratio rule to arbitrary Metropolis–Hastings or MALA proposals.

### composition-and-stationary-acceptance

evidence: supported. Targets: AIMech:NonreversibleMetropolisUniformUpdate.

Supported within the stated assumptions, inspected passages and finite-calculation scope.

The finite stationary set-flux examples distinguish substep and composition properties: half-period shift followed by accept/rescale gives fluxes 1/24 and 0, and full refresh followed by accept/rescale gives 1/192 and 1/384. Thus a reversible threshold kernel does not certify augmented-chain detailed balance. Full refresh recovers ordinary Metropolis only for the x projection. With no shift, noise or other state updates, accepted rescaling and rejection both conserve the height; this obstructs a general ergodicity claim. Equal mean acceptance follows at stationarity from integrating a uniform threshold against the same proposal kernel, and is not a guarantee about transient acceptance or clustering.

### augmented-momentum-and-interleaving-scope

evidence: supported. Targets: AIMech:NonreversibleMetropolisUniformUpdate.

Supported within the stated assumptions, inspected passages and finite-calculation scope.

The cited position/momentum example retains the partial refresh, one leapfrog step, proposal momentum negation, acceptance and final negation. The proposal correction is justified on the reversible volume-preserving augmented state, using its full density; it is not a position-only asymmetric Gaussian proposal. An x update that ignores v and preserves pi also preserves the product target, which supports the interleaving statement without asserting that all such compositions are reversible or equally efficient.

### exact-finite-boundary-checks

evidence: supported. Targets: AIMech:NonreversibleMetropolisUniformUpdate.

Supported within the stated assumptions, inspected passages and finite-calculation scope.

The shared original calculator derives transported piecewise joint densities with exact rational arithmetic. The two-state flip gives the correct product target with rescaling, but state-0 mass 1/6 after two unrescaled steps rather than 1/3. For proposal rows (1/2,1/2) and (1,0), the ratio-only negative control gives mass 1/2. Its 576 specified positive-target/symmetric-proposal drift/noise cases preserve the full joint density, and its set-flux cases establish the stated nonreversibility counterexamples. These are exact finite constructions with a continuous auxiliary variable; they are not general convergence proofs or empirical performance estimates. The counts and values have only the specified shared-calculator scope.

### efficiency-and-source-limits

evidence: supported. Targets: AIMech:NonreversibleMetropolisUniformUpdate.

Supported within the stated assumptions, inspected passages and finite-calculation scope.

The source’s finite-density noise warning is narrower than a universal need for noise and does not turn continuous variation into a deterministic-mixing theorem. Historical Gaussian, mixed and Bayesian neural-network experiments use particular observables, tuning grids and computational accounting. The draft appropriately omits numerical superiority claims and keeps the neural-network result preliminary. Appendix scripts are source evidence only; neither reading them nor the curator calculations constitutes their execution or replication.

### proper positive target support, proposal symmetry and independence from v, mandatory accepted-state rescaling, threshold-substep versus full-composition reversibility, stationary mean acceptance and finite-example scope

consistency: supported. Targets: AIMech:NonreversibleMetropolisUniformUpdate.

The guarded mechanisms and counterexamples support the maintained boundaries.

The shared original calculator derives transported piecewise joint densities with exact rational arithmetic. The two-state flip gives the correct product target with rescaling, but state-0 mass 1/6 after two unrescaled steps rather than 1/3. For proposal rows (1/2,1/2) and (1,0), the ratio-only negative control gives mass 1/2. Its 576 specified positive-target/symmetric-proposal drift/noise cases preserve the full joint density, and its set-flux cases establish the stated nonreversibility counterexamples. These are exact finite constructions with a continuous auxiliary variable; they are not general convergence proofs or empirical performance estimates. The counts and values have only the specified shared-calculator scope.

### Actual captured record and source scope

provenance: supported. Targets: AIMech:NonreversibleMetropolisUniformUpdate.

The author assessed all maintained fields in the current captured record; DRAFT remains.

After canonical capture, root read both complete maintained YAML records, including all six claims each, definition evidence, source identifiers/version/access/hash, absent exact aliases, searched identity scope, AIO pin and related mapping rationale, limitations, DRAFT status and actual curation times. Source and mapping context hashes remain those assessed in the discovery report. The twelve inspected AIO contexts and eleven rejected targets justify only a method-to-process related_match to MarkovChain; no Network or hidden-layer inheritance is asserted. The full config and its preparation-to-assessment polish were read and reassessed against actual fields. Root read the immutable supporting mathematical and actual-record audits, created and assessed the issue356 fix receipt, and read the corrected report Markdown. The report-only metadata correction preserves both records and raw handoffs; it is not a record-finding resolution or a claim of independent approval. The signed variable is essential to wrapped motion, the proposal must be symmetric and independent of v, and every accepted move rescales v by the density ratio. The claims distinguish stationary mean acceptance from temporal dependence, and threshold-substep reversibility from full composition. Fixed-height obstruction includes the absence of other state updates. Augmented momentum proposals use the joint density; arbitrary position-only MALA is excluded. The exact finite calculator and negative controls support the bounded numerical statements; source experiments do not support universal efficiency. Actual post-capture source reread: After the20:24:25Z capture, reread Neal2020 extracted text PDFpages2,3,5 and visually rechecked page2 Equations1–2. Section6 page8 was freshly read before capture while correcting report terminology. The prior complete14-page reading and visual2,4,5,6 ledger is retained; no new complete-paper read or author-code execution is implied.

### Normalized source metadata correction

provenance: supported. Targets: AIMech:NonreversibleMetropolisUniformUpdate.

The report-only terminology correction is supported; this is not a maintained-record finding.

The current report and receipt hashes match. Reversing only the corrected download wording and added correction metadata recovers the exact audited original report hash. The raw handoff objects and the maintained record claims, sources and mappings remain unchanged. The correction names the Bayesian neural network described by Neal 2020 Section 6, PDF p. 8; it does not assert a Bayesian-network DAG application.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T201921Z-nonreversible-mcmc.json; identity_search, identity_assessment and entries[id=AIMech:NonreversibleMetropolisUniformUpdate] | supports | Compared both candidate identities with all 442 pinned AIO and 701 native IDs, names, aliases and generated synonyms of every scope using the repository Unicode-aware normalizer; no normalized collisions. All 1143 current record hashes were refreshed and verified unchanged from the assessed inventory immediately before this write. Full ignored- and hidden-inclusive searches of three checkouts were completed without access errors; the 52-group frontier follow-up and 6 fixed-string groups were read in full. The semantic assessment read all 359 selected definitions/identity fields (86 AIO, 273 native), 12 complete pinned AIO CLASS contexts and 15 full native neighbors. Root separately assessed the handoffs, retained byte-verified AIO contexts and documented primary pages. Signed threshold memory and previous/current state-pair memory define separate algorithms; neither is a general Markov-process model, hidden/observed pairwise model, Gibbs sampler or persistent contrastive-divergence training method. The mapping is related_match to AIO:MarkovChain, without equivalence or inherited network/hidden-layer assertions. Absence is bounded to this snapshot, maintained corpus and the documented searches. |
| mapping | research/discovery/20261014T201921Z-nonreversible-mcmc.json; mapping_context, mapping_assessment and rejected_mappings | supports | Retain only related_match to AIO:MarkovChain. Each algorithm constructs a first-order Markov transition on an augmented state and preserves a specified original-state marginal, so a method-to-process relationship has mechanistic support. The pinned target is exported as a stochastic model under Network, with a ProbabilisticHiddenLayer has-part assertion. Neither equivalence, subclass status nor inheritance of those assertions is warranted. The source/mapping handoff inspected twelve complete CLASS contexts, incident edges and generated records, including the target and the eleven alternatives documented here. |
| actual-record-reading | data/curated/NonreversibleMetropolisUniformUpdate.yaml | supports | After canonical capture, root read both complete maintained YAML records, including all six claims each, definition evidence, source identifiers/version/access/hash, absent exact aliases, searched identity scope, AIO pin and related mapping rationale, limitations, DRAFT status and actual curation times. Source and mapping context hashes remain those assessed in the discovery report. The twelve inspected AIO contexts and eleven rejected targets justify only a method-to-process related_match to MarkovChain; no Network or hidden-layer inheritance is asserted. The full config and its preparation-to-assessment polish were read and reassessed against actual fields. Root read the immutable supporting mathematical and actual-record audits, created and assessed the issue356 fix receipt, and read the corrected report Markdown. The report-only metadata correction preserves both records and raw handoffs; it is not a record-finding resolution or a claim of independent approval. The signed variable is essential to wrapped motion, the proposal must be symmetric and independent of v, and every accepted move rescales v by the density ratio. The claims distinguish stationary mean acceptance from temporal dependence, and threshold-substep reversibility from full composition. Fixed-height obstruction includes the absence of other state updates. Augmented momentum proposals use the joint density; arbitrary position-only MALA is excluded. The exact finite calculator and negative controls support the bounded numerical statements; source experiments do not support universal efficiency. Actual source reread: After the20:24:25Z capture, reread Neal2020 extracted text PDFpages2,3,5 and visually rechecked page2 Equations1–2. Section6 page8 was freshly read before capture while correcting report terminology. The prior complete14-page reading and visual2,4,5,6 ledger is retained; no new complete-paper read or author-code execution is implied. |
| neal2020 | https://glizen.com/radfordneal/ftp/nrevu.pdf; Section 2, PDF p. 2, Equations 1–2 and the augmented-state derivation; Section 2, PDF p. 2, under-density augmentation and Equation 1; Section 2, PDF p. 2, acceptance paragraph and Equation 2; symmetric Gaussian random-walk proposal, Section 3, p. 3; proposal-domain qualification and exact counterexample in research/discovery/nonreversible-boundaries.py; Section 2, PDF pp. 2–3, invariance, noise and acceptance-rate discussion; composition counterexamples derived in research/discovery/nonreversible-boundaries.py; Section 2 continuation, PDF p. 3; Section 4, p. 5, Equation 3 and Steps 1–4; Section 2, PDF p. 2, Equations 1–2; independently authored curator calculations in research/discovery/nonreversible-boundaries.py; Section 2, PDF p. 2; experiments and discussion, Sections 3–7, pp. 3–8; appendix scripts, pp. 9–14 | supports | Author-hosted technical report dated 31 January 2020, 14 pages. Author abstract links arXiv:2001.11950; arXiv metadata has only v1, submitted 31 January 2020 16:57:53 UTC. Exact PDF byte equivalence to arXiv was not tested. Root text pages 1,2,3,4,5,6,7,8,9,10,11,12,13,14; visual pages 2,4,5,6. Entire main report, six references and Appendix scripts read. Figure extraction in the first whole-file output was truncated; pages5 and7 were read separately, page6 was read with whitespace normalized, and figures4/6 were inspected visually. No author script executed. Conditional joint preservation, required rescaling, independent symmetric proposal and augmented Hamiltonian context assessed. No numerical historical-superiority claim planned. Author reading scope: After the20:24:25Z capture, reread Neal2020 extracted text PDFpages2,3,5 and visually rechecked page2 Equations1–2. Section6 page8 was freshly read before capture while correcting report terminology. The prior complete14-page reading and visual2,4,5,6 ledger is retained; no new complete-paper read or author-code execution is implied. |
| calculation | research/discovery/nonreversible-boundaries.py; Shared calculator result section neal2020 | supports | The shared script covers both candidates; this record assessment uses its neal2020 section. Exact original finite calculations, not author-code replication, benchmark execution or a general theorem. Selected result: {"assumptions": "Positive finite target, symmetric stochastic proposal independent of signed v; exact continuous piecewise densities; shift/noise independent of v. Endpoint choices have measure zero.", "target": ["1/3", "2/3"], "proposal": [["0", "1"], ["1", "0"]], "derived_correct_joint_density": [[0, "-1", "1", "1/6"], [1, "-1", "1", "1/3"]], "derived_omitted_rescale_first_density": [[0, "-1/2", "1/2", "1/3"], [1, "-1", "-1/2", "1/2"], [1, "-1/2", "1/2", "1/6"], [1, "1/2", "1", "1/2"]], "derived_omitted_rescale_second_density": [[0, "-1/2", "1/2", "1/6"], [1, "-1", "-1/2", "1/2"], [1, "-1/2", "1/2", "1/3"], [1, "1/2", "1", "1/2"]], "omitted_rescale_second_state0_mass": "1/6", "half_period_composition_flux": {"A": [[0, "0", "1/4", "1/6"]], "B": [[1, "-1/2", "-3/8", "1/3"]], "A_to_B": "1/24", "B_to_A": "0"}, "full_refresh_composition_flux": {"A": [[0, "0", "1/4", "1/6"]], "B": [[1, "0", "1/8", "1/3"]], "A_to_B": "1/192", "B_to_A": "1/384"}, "asymmetric_proposal_negative_control": {"proposal": [["1/2", "1/2"], ["1", "0"]], "output_density": [[0, "-1", "1", "1/4"], [1, "-1", "-1/2", "1/3"], [1, "-1/2", "1/2", "1/6"], [1, "1/2", "1", "1/3"]], "state0_mass": "1/2"}, "joint_invariance_family_cases": 576, "boundary": "A half-period wrapped translation is reversible by itself, yet translation-then-accept can be nonreversible. Full uniform refresh recovers ordinary Metropolis for x, but does not ensure augmented-chain detailed balance. Zero shift/no noise leaves the under-density height fixed and supplies no ergodicity guarantee."} |
| supporting-math-audit | research/discovery/20261014T195934Z-nonreversible-supporting-math-audit.json | supports | The author assessed the retained bounded source/math audit and its candidate-specific qualifications. Supporting agents are within the same workflow, not independent scientific approval; source inconsistencies are retained as record limits. |
| actual-record-audit | research/discovery/20261014T202221Z-nonreversible-actual-record-audit.json | supports | Bounded supporting audit of both actual records and the original report. Its one minor finding concerns report download metadata terminology, not a record claim. The original report and record hashes remain preserved in the audit. |
| report-correction | research/discovery/20261014T202307Z-nonreversible-report-fix.json | supports | Issue #356 corrected the normalized report description from Bayesian-network experiment to Bayesian neural-network experiment. The exact before/after report hashes and correction annotation preserve raw handoffs; both maintained records are unchanged. The receipt establishes working-tree resolution, not issue closure. |

## Limits And Additional Notes

- Author self-review; no independent scientific approval or DRAFT status promotion.
- No arbitrary asymmetric or threshold-dependent proposal extension, zero-support implementation, numerical reversibility audit, general ergodicity proof, author-code execution or benchmark replication. This algorithm is one member of an open nonreversible-MCMC discovery cohort.
- Supporting mathematical and draft audits remain part of the author workflow; they do not constitute independent scientific approval.
- Exact finite density-transport calculations are not author-code execution, benchmark replication or a general convergence proof.
- Neal 2020 author-hosted PDF was read; byte equivalence with arXiv 2001.11950 was not established.
- Neal 2004 method evidence uses the versioned arXiv v1 PDF; uninspected author-hosted byte equivalence is not claimed.
- Diaconis–Miclo 2013 reading is selective, as explicitly separated for source agent, root and math agent; no full spectral-paper review is claimed.
- No author-code execution, model training, paid provider or benchmark replication occurred.
- Frontier source leads may be abstract-, bibliography- or search-result-only and do not certify unseen methods.
- The empty findings list is the actual author assessment of this selected current record, not a closure of unrelated historical issues or a literature-saturation claim.
- The supporting audit’s report-only finding and issue #356 correction are retained as evidence and provenance assessment, without inventing record-finding lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T204029Z-nonreversible-metropolis-uniform-update
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Nonreversible Metropolis uniform update
started_at: '2026-10-14T20:24:25Z'
finished_at: '2026-10-14T20:40:29Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author reassessed proper positive target support, proposal
    symmetry and independence from v, mandatory accepted-state rescaling, threshold-substep
    versus full-composition reversibility, stationary mean acceptance and finite-example
    scope. Bounded supporting source, math and draft agents remain within the same
    model/provider workflow; this is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the persistent signed-threshold algorithm as DRAFT with a related
  Markov-process mapping. Its invariant construction is supported under the explicit
  proposal and target assumptions; ergodicity, transient acceptance and universal
  efficiency remain outside the claim.
source:
  git_revision: ac6b62150c25ab02e880b50008cbfb5a56a109f8
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/BoltzmannMachineNetwork.yaml
    sha256: 1152d2d85c5c1c408a0420e13f211ed109b12fb289c706ee7449864e91aece03
    role: context
  - path: data/aio/DataPreparation.yaml
    sha256: 99aebfc324b628969407ddc7591312e992db1469e7ef8fb3ad28e4b62d3bb359
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/Network.yaml
    sha256: ec24eb397241fe903137b2d8c8f4081d0f9d246c296c247864f199e160a3ee30
    role: context
  - path: data/aio/Normalization.yaml
    sha256: ecdbd41476b6125c670855f1f00090047acd61f5ee16d71384f6b9ed86bea2bb
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ProbabilisticHiddenLayer.yaml
    sha256: 610c29db815f7348c5bdcdc7e7460dd2dea9ea338f3727ebb1596c51b4af41da
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/SelectionAndSamplingBias.yaml
    sha256: 72d8ef34949942ddee1fe60d645806a2117b95207f681de923297b64f78cc477
    role: context
  - path: data/curated/AnnealedImportanceSampling.yaml
    sha256: 94c7b8e597f3551b2b804778e11385d6ec9137515bc44a9c9d429268869f7e68
    role: context
  - path: data/curated/BarkerAcceptanceRule.yaml
    sha256: e81a763ba4f2eb2c7e51f3e520311bd111d269f45cdf2417055d72a4ddd4d08c
    role: context
  - path: data/curated/FastPersistentContrastiveDivergence.yaml
    sha256: 3049a144e2c5e8c8afeda5182d1cdcd4da5a3e2d2a75257c10d7f9f5b85236b4
    role: context
  - path: data/curated/GibbsSampling.yaml
    sha256: 8175215986c0507e3664a3aedf8074fc067d85b4a89002091d1bcb9b637a522a
    role: context
  - path: data/curated/HamiltonianMonteCarlo.yaml
    sha256: 28367594dbc36a8357c33a4e639aeb0fefdd47adc8c46e2b3d5feb96b67e84ca
    role: context
  - path: data/curated/MetropolisAdjustedLangevinAlgorithm.yaml
    sha256: 6e815be8054929061e44ef8ddd5a63c5b1361d8c518fb3ec5fd7f9bba884b6f7
    role: context
  - path: data/curated/MetropolisHastings.yaml
    sha256: 01cb22a25242e8564e2a7bb839ecb46da1bc49eb09b3c85200f9a596e05b99b4
    role: context
  - path: data/curated/MetropolisWithinGibbs.yaml
    sha256: 0e9cfedc93c7e46cc6316809d5a9ec9488b33891a9c9862f914a0adf8f7cb140
    role: context
  - path: data/curated/MixedMemoryMarkovModel.yaml
    sha256: 3d85215830d8e12bae4b29ae645412aff678693cb56eb639dc93860d6baaed86
    role: context
  - path: data/curated/NealBacktrackingSuppressedMCMC.yaml
    sha256: 1da524622ec40d25aac45313cdbd6412adf1376c6c8b78eeecaded8eb561a0be
    role: context
  - path: data/curated/NonreversibleMetropolisUniformUpdate.yaml
    sha256: 27dbec2b01a48103d709df4b9ab94bba36083bd27acb69af1e3bc70ab6ab4ecd
    role: target
  - path: data/curated/PairwiseMarkovChain.yaml
    sha256: 87196baeddf19e49cb4c7e3804336980a1bbdaa222e70815040d53f1aa222a9e
    role: context
  - path: data/curated/PersistentContrastiveDivergence.yaml
    sha256: 6cc8bf6977132bfa801fffba08986446faf7b6250ff5b8f38ca0de965673441f
    role: context
  - path: data/curated/RandomWalkMetropolisHastings.yaml
    sha256: aeff822517db546b4e3dee3421a54d5887ed178f3b9e6e3df46283eceb39677d
    role: context
  - path: data/curated/SliceSampling.yaml
    sha256: a87319788a5d2966dd1484b6672a968642fb5514cc6f81184908576304bf6aaa
    role: context
  - path: data/curated/TemperedTransitions.yaml
    sha256: d0f1d74d46bcd92995467e13b3552cdf5637cd0a81c8e88fd8a3c52b8bd1af79
    role: context
  - path: data/curated/TripletMarkovChain.yaml
    sha256: 1b73a91285250e23b2d488d78e1dd79d4451e4943b8d0efc4dca33df619995ec
    role: context
  - path: research/discovery/20261014T195934Z-nonreversible-supporting-math-audit.json
    sha256: c6c093ca3c783f7061a71517e8987964b3eee7210de2037356950728ea53e826
    role: context
  - path: research/discovery/20261014T201921Z-nonreversible-mcmc.json
    sha256: 5434c69b950d537e0102ebf0156aa379af6396edb63793428843f0c2cf4e2b22
    role: context
  - path: research/discovery/20261014T201921Z-nonreversible-mcmc.md
    sha256: dc14b912b1de11a334b57d3e60071c8b25e9638dd523a0fa8ac2f0a7dae0cdbe
    role: context
  - path: research/discovery/20261014T202221Z-nonreversible-actual-record-audit.json
    sha256: 8bf37a22c8e268a0e34b79d66ad0527ac2b2337d69677606c1378a9a00aaae00
    role: context
  - path: research/discovery/20261014T202307Z-nonreversible-report-fix.json
    sha256: 8cf3f7f5ef7ce2bc46c8736b7f1bf3ce2a5d7f04f5482b64e6b66786f12bc984
    role: context
  - path: research/discovery/nonreversible-boundaries.py
    sha256: 75ad60f06adf1a11400932ac7bf6c3e578446d14d7de84f1c6f35bb680471945
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
  - path: src/aimech/importer.py
    sha256: 7c2dd8e12f18b76cfb5ed4acc7e1901ae9a968b3a6c7a9d62cb260bc2f1ad3ab
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
  - path: src/aimech/validation.py
    sha256: 274ed5e6bc97440515a1964b9b21927135a2e9a5a4808ae8daebccd3e172ffcc
    role: context
targets:
- target_id: AIMech:NonreversibleMetropolisUniformUpdate
  path: data/curated/NonreversibleMetropolisUniformUpdate.yaml
  label: Nonreversible Metropolis uniform update
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NonreversibleMetropolisUniformUpdate.yaml
    role: maintained
scope:
  description: 'All maintained fields of the selected record; Root evidence scope:
    all 14 pages of the author-hosted Neal 2020 report, including references and appendix
    scripts, with visual method/figure pages 2,4,5,6. No journal version is involved;
    byte equivalence to the arXiv PDF was not established.'
  selection: 'Exact maintained ID: AIMech:NonreversibleMetropolisUniformUpdate'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  exclusions:
  - target: Other batch entry, neighboring AIO and native records
    reason: Identity/mapping and shared-calculator context; this formal review selects
      one maintained target.
  - target: Uninspected source versions and general implementation guarantees
    reason: No arbitrary asymmetric or threshold-dependent proposal extension, zero-support
      implementation, numerical reversibility audit, general ergodicity proof, author-code
      execution or benchmark replication. This algorithm is one member of an open
      nonreversible-MCMC discovery cohort.
  - target: Author-code execution, model training and benchmark replication
    reason: Only original finite curator calculations and actual project checks were
      performed.
checks:
- check_id: gate-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 421.69s (0:07:01)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 703 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 394 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 395,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
  scope_note: Actual result completed at 2026-10-14T20:39:20Z; no command executed
    by this generator.
- check_id: vendor-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
  scope_note: Actual result completed at 2026-10-14T20:25:41Z; no command executed
    by this generator.
- check_id: additional-2
  name: uv run --locked aimech check-source
  command: uv run --locked aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
  scope_note: Actual result completed at 2026-10-14T20:25:00Z; no command executed
    by this generator.
- check_id: additional-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  exit_code: 0
  expected_exit_code: 0
  summary: Actual command exited 0 without output.
  scope_note: Actual result completed at 2026-10-14T20:25:01Z; no command executed
    by this generator.
- check_id: render-4
  name: just render
  command: just render
  status: passed
  required: true
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  exit_code: 0
  expected_exit_code: 0
  summary: 'Rendered AIMech site under /private/tmp/aimech-discovery-recovery-worktree-20261012/pages

    uv run --locked python scripts/render_pages.py

    '
  scope_note: Actual result completed at 2026-10-14T20:25:08Z; no command executed
    by this generator.
- check_id: render-5
  name: just render-check
  command: just render-check
  status: passed
  required: true
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  exit_code: 0
  expected_exit_code: 0
  summary: 'pages/ is current

    uv run --locked python scripts/render_pages.py --check

    '
  scope_note: Actual result completed at 2026-10-14T20:25:31Z; no command executed
    by this generator.
- check_id: calculation-6
  name: python3 research/discovery/nonreversible-boundaries.py
  command: python3 research/discovery/nonreversible-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"scope\": \"Exact deterministic original calculations, not author\
    \ implementation, empirical reproduction, general proof, or independent scientific\
    \ approval.\",\n  \"neal2020\": {\n    \"assumptions\": \"Positive finite target,\
    \ symmetric stochastic proposal independent of signed v; exact continuous piecewise\
    \ densities; shift/noise independent of v. Endpoint choices have measure zero.\"\
    ,\n    \"target\": [\n      \"1/3\",\n      \"2/3\"\n    ],\n    \"proposal\"\
    : [\n      [\n        \"0\",\n        \"1\"\n      ],\n      [\n        \"1\"\
    ,\n        \"0\"\n      ]\n    ],\n    \"derived_correct_joint_density\": [\n\
    \      [\n        0,\n        \"-1\",\n        \"1\",\n        \"1/6\"\n     \
    \ ],\n      [\n        1,\n        \"-1\",\n        \"1\",\n        \"1/3\"\n\
    \      ]\n    ],\n    \"derived_omitted_rescale_first_density\": [\n      [\n\
    \        0,\n        \"-1/2\",\n        \"1/2\",\n        \"1/3\"\n      ],\n\
    \      [\n        1,\n        \"-1\",\n        \"-1/2\",\n        \"1/2\"\n  \
    \    ],\n      [\n        1,\n        \"-1/2\",\n        \"1/2\",\n        \"\
    1/6\"\n      ],\n      [\n        1,\n        \"1/2\",\n        \"1\",\n     \
    \   \"1/2\"\n      ]\n    ],\n    \"derived_omitted_rescale_second_density\":\
    \ [\n      [\n        0,\n        \"-1/2\",\n        \"1/2\",\n        \"1/6\"\
    \n      ],\n      [\n        1,\n        \"-1\",\n        \"-1/2\",\n        \"\
    1/2\"\n      ],\n      [\n        1,\n        \"-1/2\",\n        \"1/2\",\n  \
    \      \"1/3\"\n      ],\n      [\n        1,\n        \"1/2\",\n        \"1\"\
    ,\n        \"1/2\"\n      ]\n    ],\n    \"omitted_rescale_second_state0_mass\"\
    : \"1/6\",\n    \"half_period_composition_flux\": {\n      \"A\": [\n        [\n\
    \          0,\n          \"0\",\n          \"1/4\",\n          \"1/6\"\n     \
    \   ]\n      ],\n      \"B\": [\n        [\n          1,\n          \"-1/2\",\n\
    \          \"-3/8\",\n          \"1/3\"\n        ]\n      ],\n      \"A_to_B\"\
    : \"1/24\",\n      \"B_to_A\": \"0\"\n    },\n    \"full_refresh_composition_flux\"\
    : {\n      \"A\": [\n        [\n          0,\n          \"0\",\n          \"1/4\"\
    ,\n          \"1/6\"\n        ]\n      ],\n      \"B\": [\n        [\n       \
    \   1,\n          \"0\",\n          \"1/8\",\n          \"1/3\"\n        ]\n \
    \     ],\n      \"A_to_B\": \"1/192\",\n      \"B_to_A\": \"1/384\"\n    },\n\
    \    \"asymmetric_proposal_negative_control\": {\n      \"proposal\": [\n    \
    \    [\n          \"1/2\",\n          \"1/2\"\n        ],\n        [\n       \
    \   \"1\",\n          \"0\"\n        ]\n      ],\n      \"output_density\": [\n\
    \        [\n          0,\n          \"-1\",\n          \"1\",\n          \"1/4\"\
    \n        ],\n        [\n          1,\n          \"-1\",\n          \"-1/2\",\n\
    \          \"1/3\"\n        ],\n        [\n          1,\n          \"-1/2\",\n\
    \          \"1/2\",\n          \"1/6\"\n        ],\n        [\n          1,\n\
    \          \"1/2\",\n          \"1\",\n          \"1/3\"\n        ]\n      ],\n\
    \      \"state0_mass\": \"1/2\"\n    },\n    \"joint_invariance_family_cases\"\
    : 576,\n    \"boundary\": \"A half-period wrapped translation is reversible by\
    \ itself, yet translation-then-accept can be nonreversible. Full uniform refresh\
    \ recovers ordinary Metropolis for x, but does not ensure augmented-chain detailed\
    \ balance. Zero shift/no noise leaves the under-density height fixed and supplies\
    \ no ergodicity guarantee.\"\n  },\n  \"neal2004\": {\n    \"assumptions\": \"\
    Finite reversible baseline, positive invariant mass, positive-support pair states;\
    \ Liu conditional point-mass boundary handled explicitly. The variance calculation\
    \ is applied only after verifying expanded irreducibility.\",\n    \"triangle\"\
    : {\n      \"base\": [\n        [\n          \"0\",\n          \"1/2\",\n    \
    \      \"1/2\"\n        ],\n        [\n          \"1/2\",\n          \"0\",\n\
    \          \"1/2\"\n        ],\n        [\n          \"1/2\",\n          \"1/2\"\
    ,\n          \"0\"\n        ]\n      ],\n      \"pi\": [\n        \"1/3\",\n \
    \       \"1/3\",\n        \"1/3\"\n      ],\n      \"expanded_states\": [\n  \
    \      [\n          0,\n          1\n        ],\n        [\n          0,\n   \
    \       2\n        ],\n        [\n          1,\n          0\n        ],\n    \
    \    [\n          1,\n          2\n        ],\n        [\n          2,\n     \
    \     0\n        ],\n        [\n          2,\n          1\n        ]\n      ],\n\
    \      \"expanded_invariant\": [\n        \"1/6\",\n        \"1/6\",\n       \
    \ \"1/6\",\n        \"1/6\",\n        \"1/6\",\n        \"1/6\"\n      ],\n  \
    \    \"expanded_transition\": [\n        [\n          \"0\",\n          \"0\"\
    ,\n          \"0\",\n          \"1\",\n          \"0\",\n          \"0\"\n   \
    \     ],\n        [\n          \"0\",\n          \"0\",\n          \"0\",\n  \
    \        \"0\",\n          \"0\",\n          \"1\"\n        ],\n        [\n  \
    \        \"0\",\n          \"1\",\n          \"0\",\n          \"0\",\n      \
    \    \"0\",\n          \"0\"\n        ],\n        [\n          \"0\",\n      \
    \    \"0\",\n          \"0\",\n          \"0\",\n          \"1\",\n          \"\
    0\"\n        ],\n        [\n          \"1\",\n          \"0\",\n          \"0\"\
    ,\n          \"0\",\n          \"0\",\n          \"0\"\n        ],\n        [\n\
    \          \"0\",\n          \"0\",\n          \"1\",\n          \"0\",\n    \
    \      \"0\",\n          \"0\"\n        ]\n      ],\n      \"closed_classes\"\
    : [\n        [\n          [\n            0,\n            1\n          ],\n   \
    \       [\n            1,\n            2\n          ],\n          [\n        \
    \    2,\n            0\n          ]\n        ],\n        [\n          [\n    \
    \        0,\n            2\n          ],\n          [\n            1,\n      \
    \      0\n          ],\n          [\n            2,\n            1\n         \
    \ ]\n        ]\n      ],\n      \"boundary\": \"Base is irreducible (also aperiodic);\
    \ the lift has two closed orientation cycles. Each class in this example still\
    \ has the correct projected marginal; this refutes automatic expanded irreducibility,\
    \ not projected correctness for this particular example.\"\n    },\n    \"point_mass_conditional\"\
    : {\n      \"expanded_states\": [\n        [\n          0,\n          1\n    \
    \    ],\n        [\n          1,\n          0\n        ]\n      ],\n      \"expanded_transition\"\
    : [\n        [\n          \"0\",\n          \"1\"\n        ],\n        [\n   \
    \       \"1\",\n          \"0\"\n        ]\n      ],\n      \"expanded_invariant\"\
    : [\n        \"1/2\",\n        \"1/2\"\n      ]\n    },\n    \"printed_fast_simulator\"\
    : {\n      \"conditional\": [\n        \"3/5\",\n        \"3/10\",\n        \"\
    1/10\"\n      ],\n      \"current_index\": 0,\n      \"proposal_index\": 1,\n\
    \      \"printed_acceptance\": \"10/7\",\n      \"equation16_conditional_row\"\
    : [\n        \"29/63\",\n        \"3/7\",\n        \"1/9\"\n      ],\n      \"\
    clipped_transition\": \"3/10\",\n      \"equation16_transition\": \"3/7\",\n \
    \     \"boundary\": \"Neal2004 p.9 probability exceeds one as printed; clipping\
    \ fails to implement p.8 Eq.(16). The conditional-proposal construction implements\
    \ Eq.(16), but can be costly if the excluded mass is near one.\"\n    },\n   \
    \ \"positive_conductance_family_cases\": 54,\n    \"single_coordinate_variance_comparisons\"\
    : 162,\n    \"strict_variance_improvements\": 162,\n    \"first_family_example\"\
    : {\n      \"base\": [\n        [\n          \"1/3\",\n          \"1/3\",\n  \
    \        \"1/3\"\n        ],\n        [\n          \"1/3\",\n          \"1/3\"\
    ,\n          \"1/3\"\n        ],\n        [\n          \"1/3\",\n          \"\
    1/3\",\n          \"1/3\"\n        ]\n      ],\n      \"pi\": [\n        \"1/3\"\
    ,\n        \"1/3\",\n        \"1/3\"\n      ],\n      \"indicator_comparisons\"\
    : [\n        {\n          \"coordinate_indicator\": 0,\n          \"baseline_asymptotic_variance\"\
    : \"2/9\",\n          \"expanded_asymptotic_variance\": \"2/27\"\n        },\n\
    \        {\n          \"coordinate_indicator\": 1,\n          \"baseline_asymptotic_variance\"\
    : \"2/9\",\n          \"expanded_asymptotic_variance\": \"2/27\"\n        },\n\
    \        {\n          \"coordinate_indicator\": 2,\n          \"baseline_asymptotic_variance\"\
    : \"2/9\",\n          \"expanded_asymptotic_variance\": \"2/27\"\n        }\n\
    \      ]\n    },\n    \"boundary\": \"The finite checks illustrate invariance,\
    \ local balance, suppression, and the corrected variance boundary; they are not\
    \ a general theorem or a speed claim.\"\n  }\n}\n"
  scope_note: Actual result completed at 2026-10-14T20:24:59Z; no command executed
    by this generator.
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T201921Z-nonreversible-mcmc.json
  locator: identity_search, identity_assessment and entries[id=AIMech:NonreversibleMetropolisUniformUpdate]
  accessed_at: '2026-10-14T20:27:19Z'
  snapshot_sha256: 5434c69b950d537e0102ebf0156aa379af6396edb63793428843f0c2cf4e2b22
  support: supports
  summary: Compared both candidate identities with all 442 pinned AIO and 701 native
    IDs, names, aliases and generated synonyms of every scope using the repository
    Unicode-aware normalizer; no normalized collisions. All 1143 current record hashes
    were refreshed and verified unchanged from the assessed inventory immediately
    before this write. Full ignored- and hidden-inclusive searches of three checkouts
    were completed without access errors; the 52-group frontier follow-up and 6 fixed-string
    groups were read in full. The semantic assessment read all 359 selected definitions/identity
    fields (86 AIO, 273 native), 12 complete pinned AIO CLASS contexts and 15 full
    native neighbors. Root separately assessed the handoffs, retained byte-verified
    AIO contexts and documented primary pages. Signed threshold memory and previous/current
    state-pair memory define separate algorithms; neither is a general Markov-process
    model, hidden/observed pairwise model, Gibbs sampler or persistent contrastive-divergence
    training method. The mapping is related_match to AIO:MarkovChain, without equivalence
    or inherited network/hidden-layer assertions. Absence is bounded to this snapshot,
    maintained corpus and the documented searches.
  search_scope: Selected native identity in the combined discovery report. Unicode-aware
    canonical ID/name/alias/scoped-synonym comparison and the report’s bounded semantic
    assessment; the retained full-checkout searches explicitly include ignored and
    hidden files. The current inventory refresh and collision results are preserved
    in identity_search. This is not a claim of universal ontology or literature absence.
- evidence_id: mapping
  kind: record_content
  reference: research/discovery/20261014T201921Z-nonreversible-mcmc.json
  locator: mapping_context, mapping_assessment and rejected_mappings
  accessed_at: '2026-10-14T20:27:19Z'
  snapshot_sha256: 5434c69b950d537e0102ebf0156aa379af6396edb63793428843f0c2cf4e2b22
  support: supports
  summary: Retain only related_match to AIO:MarkovChain. Each algorithm constructs
    a first-order Markov transition on an augmented state and preserves a specified
    original-state marginal, so a method-to-process relationship has mechanistic support.
    The pinned target is exported as a stochastic model under Network, with a ProbabilisticHiddenLayer
    has-part assertion. Neither equivalence, subclass status nor inheritance of those
    assertions is warranted. The source/mapping handoff inspected twelve complete
    CLASS contexts, incident edges and generated records, including the target and
    the eleven alternatives documented here.
- evidence_id: actual-record-reading
  kind: record_content
  reference: data/curated/NonreversibleMetropolisUniformUpdate.yaml
  accessed_at: '2026-10-14T20:27:19Z'
  snapshot_sha256: 27dbec2b01a48103d709df4b9ab94bba36083bd27acb69af1e3bc70ab6ab4ecd
  support: supports
  summary: 'After canonical capture, root read both complete maintained YAML records,
    including all six claims each, definition evidence, source identifiers/version/access/hash,
    absent exact aliases, searched identity scope, AIO pin and related mapping rationale,
    limitations, DRAFT status and actual curation times. Source and mapping context
    hashes remain those assessed in the discovery report. The twelve inspected AIO
    contexts and eleven rejected targets justify only a method-to-process related_match
    to MarkovChain; no Network or hidden-layer inheritance is asserted. The full config
    and its preparation-to-assessment polish were read and reassessed against actual
    fields. Root read the immutable supporting mathematical and actual-record audits,
    created and assessed the issue356 fix receipt, and read the corrected report Markdown.
    The report-only metadata correction preserves both records and raw handoffs; it
    is not a record-finding resolution or a claim of independent approval. The signed
    variable is essential to wrapped motion, the proposal must be symmetric and independent
    of v, and every accepted move rescales v by the density ratio. The claims distinguish
    stationary mean acceptance from temporal dependence, and threshold-substep reversibility
    from full composition. Fixed-height obstruction includes the absence of other
    state updates. Augmented momentum proposals use the joint density; arbitrary position-only
    MALA is excluded. The exact finite calculator and negative controls support the
    bounded numerical statements; source experiments do not support universal efficiency.
    Actual source reread: After the20:24:25Z capture, reread Neal2020 extracted text
    PDFpages2,3,5 and visually rechecked page2 Equations1–2. Section6 page8 was freshly
    read before capture while correcting report terminology. The prior complete14-page
    reading and visual2,4,5,6 ledger is retained; no new complete-paper read or author-code
    execution is implied.'
- evidence_id: neal2020
  kind: primary_source
  reference: https://glizen.com/radfordneal/ftp/nrevu.pdf
  locator: Section 2, PDF p. 2, Equations 1–2 and the augmented-state derivation;
    Section 2, PDF p. 2, under-density augmentation and Equation 1; Section 2, PDF
    p. 2, acceptance paragraph and Equation 2; symmetric Gaussian random-walk proposal,
    Section 3, p. 3; proposal-domain qualification and exact counterexample in research/discovery/nonreversible-boundaries.py;
    Section 2, PDF pp. 2–3, invariance, noise and acceptance-rate discussion; composition
    counterexamples derived in research/discovery/nonreversible-boundaries.py; Section
    2 continuation, PDF p. 3; Section 4, p. 5, Equation 3 and Steps 1–4; Section 2,
    PDF p. 2, Equations 1–2; independently authored curator calculations in research/discovery/nonreversible-boundaries.py;
    Section 2, PDF p. 2; experiments and discussion, Sections 3–7, pp. 3–8; appendix
    scripts, pp. 9–14
  accessed_at: '2026-10-14T19:41:48Z'
  snapshot_sha256: 633fee302304649f2bf3a13c919c04773a5f30cfda2343a945249f27f4dae7bc
  support: supports
  summary: 'Author-hosted technical report dated 31 January 2020, 14 pages. Author
    abstract links arXiv:2001.11950; arXiv metadata has only v1, submitted 31 January
    2020 16:57:53 UTC. Exact PDF byte equivalence to arXiv was not tested. Root text
    pages 1,2,3,4,5,6,7,8,9,10,11,12,13,14; visual pages 2,4,5,6. Entire main report,
    six references and Appendix scripts read. Figure extraction in the first whole-file
    output was truncated; pages5 and7 were read separately, page6 was read with whitespace
    normalized, and figures4/6 were inspected visually. No author script executed.
    Conditional joint preservation, required rescaling, independent symmetric proposal
    and augmented Hamiltonian context assessed. No numerical historical-superiority
    claim planned. Author reading scope: After the20:24:25Z capture, reread Neal2020
    extracted text PDFpages2,3,5 and visually rechecked page2 Equations1–2. Section6
    page8 was freshly read before capture while correcting report terminology. The
    prior complete14-page reading and visual2,4,5,6 ledger is retained; no new complete-paper
    read or author-code execution is implied.'
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/nonreversible-boundaries.py
  locator: Shared calculator result section neal2020
  accessed_at: '2026-10-14T20:27:19Z'
  snapshot_sha256: 75ad60f06adf1a11400932ac7bf6c3e578446d14d7de84f1c6f35bb680471945
  support: supports
  summary: 'The shared script covers both candidates; this record assessment uses
    its neal2020 section. Exact original finite calculations, not author-code replication,
    benchmark execution or a general theorem. Selected result: {"assumptions": "Positive
    finite target, symmetric stochastic proposal independent of signed v; exact continuous
    piecewise densities; shift/noise independent of v. Endpoint choices have measure
    zero.", "target": ["1/3", "2/3"], "proposal": [["0", "1"], ["1", "0"]], "derived_correct_joint_density":
    [[0, "-1", "1", "1/6"], [1, "-1", "1", "1/3"]], "derived_omitted_rescale_first_density":
    [[0, "-1/2", "1/2", "1/3"], [1, "-1", "-1/2", "1/2"], [1, "-1/2", "1/2", "1/6"],
    [1, "1/2", "1", "1/2"]], "derived_omitted_rescale_second_density": [[0, "-1/2",
    "1/2", "1/6"], [1, "-1", "-1/2", "1/2"], [1, "-1/2", "1/2", "1/3"], [1, "1/2",
    "1", "1/2"]], "omitted_rescale_second_state0_mass": "1/6", "half_period_composition_flux":
    {"A": [[0, "0", "1/4", "1/6"]], "B": [[1, "-1/2", "-3/8", "1/3"]], "A_to_B": "1/24",
    "B_to_A": "0"}, "full_refresh_composition_flux": {"A": [[0, "0", "1/4", "1/6"]],
    "B": [[1, "0", "1/8", "1/3"]], "A_to_B": "1/192", "B_to_A": "1/384"}, "asymmetric_proposal_negative_control":
    {"proposal": [["1/2", "1/2"], ["1", "0"]], "output_density": [[0, "-1", "1", "1/4"],
    [1, "-1", "-1/2", "1/3"], [1, "-1/2", "1/2", "1/6"], [1, "1/2", "1", "1/3"]],
    "state0_mass": "1/2"}, "joint_invariance_family_cases": 576, "boundary": "A half-period
    wrapped translation is reversible by itself, yet translation-then-accept can be
    nonreversible. Full uniform refresh recovers ordinary Metropolis for x, but does
    not ensure augmented-chain detailed balance. Zero shift/no noise leaves the under-density
    height fixed and supplies no ergodicity guarantee."}'
- evidence_id: supporting-math-audit
  kind: record_content
  reference: research/discovery/20261014T195934Z-nonreversible-supporting-math-audit.json
  accessed_at: '2026-10-14T20:27:19Z'
  snapshot_sha256: c6c093ca3c783f7061a71517e8987964b3eee7210de2037356950728ea53e826
  support: supports
  summary: The author assessed the retained bounded source/math audit and its candidate-specific
    qualifications. Supporting agents are within the same workflow, not independent
    scientific approval; source inconsistencies are retained as record limits.
- evidence_id: actual-record-audit
  kind: record_content
  reference: research/discovery/20261014T202221Z-nonreversible-actual-record-audit.json
  accessed_at: '2026-10-14T20:27:19Z'
  snapshot_sha256: 8bf37a22c8e268a0e34b79d66ad0527ac2b2337d69677606c1378a9a00aaae00
  support: supports
  summary: Bounded supporting audit of both actual records and the original report.
    Its one minor finding concerns report download metadata terminology, not a record
    claim. The original report and record hashes remain preserved in the audit.
- evidence_id: report-correction
  kind: record_content
  reference: research/discovery/20261014T202307Z-nonreversible-report-fix.json
  accessed_at: '2026-10-14T20:27:19Z'
  snapshot_sha256: 8cf3f7f5ef7ce2bc46c8736b7f1bf3ce2a5d7f04f5482b64e6b66786f12bc984
  support: supports
  summary: 'Issue #356 corrected the normalized report description from Bayesian-network
    experiment to Bayesian neural-network experiment. The exact before/after report
    hashes and correction annotation preserve raw handoffs; both maintained records
    are unchanged. The receipt establishes working-tree resolution, not issue closure.'
assessments:
- assessment_id: identity
  area: identity
  topic: Nonreversible Metropolis uniform update
  outcome: supported
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  evidence_ids:
  - identity
  - neal2020
  summary: Retain the distinct DRAFT algorithm within the searched corpus and scope.
  details: Retain a distinct algorithm identity for persistent signed acceptance-threshold
    memory plus the required accepted-state density rescaling. This is not a new name
    for general Metropolis–Hastings, a random-walk proposal, Barker’s scalar acceptance
    function, or a generic nonreversible sampler. Shared under-density augmentation
    does not equate it with fresh-height slice sampling. The momentum application
    is distinct from HMC and position-only MALA; the latter has an asymmetric proposal
    correction that this simple ratio cannot replace. Persistent contrastive-divergence
    particles evolve during model learning and do not supply this fixed-target identity.
    AIS and tempered transitions may use related kernels but have different path and
    estimator identities. Generic terminology and broad paper titles are broader than
    this algorithm and do not justify exact aliases.
- assessment_id: mapping
  area: grounding
  topic: Related Markov-process mapping
  outcome: supported
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  evidence_ids:
  - mapping
  - neal2020
  summary: The related_match assessment is supported without equivalence or inherited
    ontology assertions.
  details: 'Retain only related_match to AIO:MarkovChain. Each algorithm constructs
    a first-order Markov transition on an augmented state and preserves a specified
    original-state marginal, so a method-to-process relationship has mechanistic support.
    The pinned target is exported as a stochastic model under Network, with a ProbabilisticHiddenLayer
    has-part assertion. Neither equivalence, subclass status nor inheritance of those
    assertions is warranted. The source/mapping handoff inspected twelve complete
    CLASS contexts, incident edges and generated records, including the target and
    the eleven alternatives documented here.

    Alternative target decisions:

    AIO:Network: A network architecture or interconnected-entity system is not the
    identity of either transition algorithm. A graph representation of a Markov process
    does not establish equivalence or a broader-class mapping to Network.

    AIO:ProbabilisticHiddenLayer: Neither construction is a neural-network hidden
    layer estimating category probabilities. The exported MarkovChain has-part edge
    is contextual ontology structure, not an inherited claim about these local algorithms.

    AIO:MathematicalFunction: Both identities include a stochastic state evolution,
    auxiliary memory and an invariant distribution. The presence of update equations
    does not make either merely an input-output mathematical function or justify a
    broad_match.

    AIO:Model: The target statistical distribution is an input to the procedure. The
    transition algorithm is distinct from a statistical model family or explanatory
    system model.

    AIO:BoltzmannMachineNetwork: A Boltzmann machine can be a sampling application,
    but no recurrent neural-network or Boltzmann-machine architecture is required
    by either mechanism.

    AIO:BayesianNetwork: Neither mechanism requires a directed acyclic dependency
    graph. Bayesian inference applications, including the 2020 Bayesian neural network,
    do not identify a Bayesian-network DAG.

    AIO:ProbabilisticGraphicalModel: A graphical target distribution is optional.
    The generic transition construction is not the pinned graphical-model task/model
    identity.

    AIO:Normalization: The pinned class concerns data scaling or formatting. The 2020
    auxiliary-variable rescaling and stochastic-row normalization are different mathematical
    operations.

    AIO:SelectionAndSamplingBias: Representativeness bias in data selection is not
    the identity of a target-preserving MCMC transition. Temporal dependence and stationary-measure
    correctness do not supply this mapping.

    AIO:DataPreparation: The procedures simulate from fixed target distributions;
    they do not specify raw-data cleaning, assembly or preprocessing.

    AIO:ReinforcementLearning: Neither method defines learning from rewards, a policy
    objective or an exploration/exploitation learning problem. Directional state movement
    in MCMC is insufficient.'
- assessment_id: joint-target-and-wrapped-update
  area: evidence
  topic: joint-target-and-wrapped-update
  outcome: supported
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  evidence_ids:
  - neal2020
  - calculation
  summary: Supported within the stated assumptions, inspected passages and finite-calculation
    scope.
  details: The product target is justified by the change from height s to normalized
    magnitude abs(v); signed v retains the direction needed by the wrapped update.
    A fixed translation on the circle has unit Jacobian, and a mixture of translations
    whose noise law does not depend on current v preserves conditional uniform measure.
    This supports invariance of that substep, not irreducibility or detailed balance
    of every full composition. This regular construction assumes a proper positive
    target on its proposal state space.
- assessment_id: accepted-state-rescaling
  area: evidence
  topic: accepted-state-rescaling
  outcome: supported
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  evidence_ids:
  - neal2020
  - calculation
  summary: Supported within the stated assumptions, inspected passages and finite-calculation
    scope.
  details: For an accepted x-to-y move, the inverse Jacobian of v_new=v_old*pi(x)/pi(y)
    is pi(y)/pi(x). Joint input density pi(x)/2 times q(x,y) therefore becomes pi(y)*q(x,y)/2,
    matching the reverse contribution under symmetric q independent of v. Rejection
    retains both state components. Omitting the rescaling breaks the product joint
    law even when a one-step x-marginal check happens to pass. The independent-of-v
    assumption matters because the reverse state has a rescaled threshold. The explicit
    asymmetric-proposal counterexample prevents extending the target-ratio rule to
    arbitrary Metropolis–Hastings or MALA proposals.
- assessment_id: composition-and-stationary-acceptance
  area: evidence
  topic: composition-and-stationary-acceptance
  outcome: supported
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  evidence_ids:
  - neal2020
  - calculation
  summary: Supported within the stated assumptions, inspected passages and finite-calculation
    scope.
  details: 'The finite stationary set-flux examples distinguish substep and composition
    properties: half-period shift followed by accept/rescale gives fluxes 1/24 and
    0, and full refresh followed by accept/rescale gives 1/192 and 1/384. Thus a reversible
    threshold kernel does not certify augmented-chain detailed balance. Full refresh
    recovers ordinary Metropolis only for the x projection. With no shift, noise or
    other state updates, accepted rescaling and rejection both conserve the height;
    this obstructs a general ergodicity claim. Equal mean acceptance follows at stationarity
    from integrating a uniform threshold against the same proposal kernel, and is
    not a guarantee about transient acceptance or clustering.'
- assessment_id: augmented-momentum-and-interleaving-scope
  area: evidence
  topic: augmented-momentum-and-interleaving-scope
  outcome: supported
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  evidence_ids:
  - neal2020
  summary: Supported within the stated assumptions, inspected passages and finite-calculation
    scope.
  details: The cited position/momentum example retains the partial refresh, one leapfrog
    step, proposal momentum negation, acceptance and final negation. The proposal
    correction is justified on the reversible volume-preserving augmented state, using
    its full density; it is not a position-only asymmetric Gaussian proposal. An x
    update that ignores v and preserves pi also preserves the product target, which
    supports the interleaving statement without asserting that all such compositions
    are reversible or equally efficient.
- assessment_id: exact-finite-boundary-checks
  area: evidence
  topic: exact-finite-boundary-checks
  outcome: supported
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  evidence_ids:
  - neal2020
  - calculation
  summary: Supported within the stated assumptions, inspected passages and finite-calculation
    scope.
  details: The shared original calculator derives transported piecewise joint densities
    with exact rational arithmetic. The two-state flip gives the correct product target
    with rescaling, but state-0 mass 1/6 after two unrescaled steps rather than 1/3.
    For proposal rows (1/2,1/2) and (1,0), the ratio-only negative control gives mass
    1/2. Its 576 specified positive-target/symmetric-proposal drift/noise cases preserve
    the full joint density, and its set-flux cases establish the stated nonreversibility
    counterexamples. These are exact finite constructions with a continuous auxiliary
    variable; they are not general convergence proofs or empirical performance estimates.
    The counts and values have only the specified shared-calculator scope.
- assessment_id: efficiency-and-source-limits
  area: evidence
  topic: efficiency-and-source-limits
  outcome: supported
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  evidence_ids:
  - neal2020
  summary: Supported within the stated assumptions, inspected passages and finite-calculation
    scope.
  details: The source’s finite-density noise warning is narrower than a universal
    need for noise and does not turn continuous variation into a deterministic-mixing
    theorem. Historical Gaussian, mixed and Bayesian neural-network experiments use
    particular observables, tuning grids and computational accounting. The draft appropriately
    omits numerical superiority claims and keeps the neural-network result preliminary.
    Appendix scripts are source evidence only; neither reading them nor the curator
    calculations constitutes their execution or replication.
- assessment_id: mathematical-boundaries
  area: consistency
  topic: proper positive target support, proposal symmetry and independence from v,
    mandatory accepted-state rescaling, threshold-substep versus full-composition
    reversibility, stationary mean acceptance and finite-example scope
  outcome: supported
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  evidence_ids:
  - neal2020
  - calculation
  - supporting-math-audit
  summary: The guarded mechanisms and counterexamples support the maintained boundaries.
  details: The shared original calculator derives transported piecewise joint densities
    with exact rational arithmetic. The two-state flip gives the correct product target
    with rescaling, but state-0 mass 1/6 after two unrescaled steps rather than 1/3.
    For proposal rows (1/2,1/2) and (1,0), the ratio-only negative control gives mass
    1/2. Its 576 specified positive-target/symmetric-proposal drift/noise cases preserve
    the full joint density, and its set-flux cases establish the stated nonreversibility
    counterexamples. These are exact finite constructions with a continuous auxiliary
    variable; they are not general convergence proofs or empirical performance estimates.
    The counts and values have only the specified shared-calculator scope.
- assessment_id: all-maintained-fields
  area: provenance
  topic: Actual captured record and source scope
  outcome: supported
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  evidence_ids:
  - actual-record-reading
  - identity
  - mapping
  - neal2020
  summary: The author assessed all maintained fields in the current captured record;
    DRAFT remains.
  details: 'After canonical capture, root read both complete maintained YAML records,
    including all six claims each, definition evidence, source identifiers/version/access/hash,
    absent exact aliases, searched identity scope, AIO pin and related mapping rationale,
    limitations, DRAFT status and actual curation times. Source and mapping context
    hashes remain those assessed in the discovery report. The twelve inspected AIO
    contexts and eleven rejected targets justify only a method-to-process related_match
    to MarkovChain; no Network or hidden-layer inheritance is asserted. The full config
    and its preparation-to-assessment polish were read and reassessed against actual
    fields. Root read the immutable supporting mathematical and actual-record audits,
    created and assessed the issue356 fix receipt, and read the corrected report Markdown.
    The report-only metadata correction preserves both records and raw handoffs; it
    is not a record-finding resolution or a claim of independent approval. The signed
    variable is essential to wrapped motion, the proposal must be symmetric and independent
    of v, and every accepted move rescales v by the density ratio. The claims distinguish
    stationary mean acceptance from temporal dependence, and threshold-substep reversibility
    from full composition. Fixed-height obstruction includes the absence of other
    state updates. Augmented momentum proposals use the joint density; arbitrary position-only
    MALA is excluded. The exact finite calculator and negative controls support the
    bounded numerical statements; source experiments do not support universal efficiency.
    Actual post-capture source reread: After the20:24:25Z capture, reread Neal2020
    extracted text PDFpages2,3,5 and visually rechecked page2 Equations1–2. Section6
    page8 was freshly read before capture while correcting report terminology. The
    prior complete14-page reading and visual2,4,5,6 ledger is retained; no new complete-paper
    read or author-code execution is implied.'
- assessment_id: report-only-correction
  area: provenance
  topic: Normalized source metadata correction
  outcome: supported
  target_ids:
  - AIMech:NonreversibleMetropolisUniformUpdate
  evidence_ids:
  - actual-record-audit
  - report-correction
  summary: The report-only terminology correction is supported; this is not a maintained-record
    finding.
  details: The current report and receipt hashes match. Reversing only the corrected
    download wording and added correction metadata recovers the exact audited original
    report hash. The raw handoff objects and the maintained record claims, sources
    and mappings remain unchanged. The correction names the Bayesian neural network
    described by Neal 2020 Section 6, PDF p. 8; it does not assert a Bayesian-network
    DAG application.
findings: []
actions: []
limitations:
- Author self-review; no independent scientific approval or DRAFT status promotion.
- No arbitrary asymmetric or threshold-dependent proposal extension, zero-support
  implementation, numerical reversibility audit, general ergodicity proof, author-code
  execution or benchmark replication. This algorithm is one member of an open nonreversible-MCMC
  discovery cohort.
- Supporting mathematical and draft audits remain part of the author workflow; they
  do not constitute independent scientific approval.
- Exact finite density-transport calculations are not author-code execution, benchmark
  replication or a general convergence proof.
- Neal 2020 author-hosted PDF was read; byte equivalence with arXiv 2001.11950 was
  not established.
- Neal 2004 method evidence uses the versioned arXiv v1 PDF; uninspected author-hosted
  byte equivalence is not claimed.
- Diaconis–Miclo 2013 reading is selective, as explicitly separated for source agent,
  root and math agent; no full spectral-paper review is claimed.
- No author-code execution, model training, paid provider or benchmark replication
  occurred.
- Frontier source leads may be abstract-, bibliography- or search-result-only and
  do not certify unseen methods.
notes:
- The empty findings list is the actual author assessment of this selected current
  record, not a closure of unrelated historical issues or a literature-saturation
  claim.
- 'The supporting audit’s report-only finding and issue #356 correction are retained
  as evidence and provenance assessment, without inventing record-finding lineage.'
tags:
- native-concepts
- self-review
- discovery-ongoing
- nonreversible-mcmc
```
