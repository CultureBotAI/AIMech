# Scientific author self-review of Liu modified discrete-state Gibbs sampler

- Review: 20261014T211738Z-liu-modified-gibbs-sampler
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T21:04:24.106232Z
- Finished UTC: 2026-10-14T21:17:38.677305Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the narrow Liu conditional update as DRAFT with related_match to MarkovChain. The displayed mechanism and local balance are supported; full-sweep variance ordering and universal convergence are excluded. The original Liu full-text gap and explicit scan-schedule qualifications remain limitations.

## Scope And Provenance

All maintained fields of the selected record. Actual source scope: Neal2004 PDF pages5,6,8 freshly read as extracted text after capture; pages5 and8 freshly inspected visually. Retained prior root reading covers all25 text pages and selected visual pages1,6–9; no original Liu1996 full-text reading is claimed.. Neal2004 PDF pages5,6,8 freshly read as extracted text after capture; pages5 and8 freshly inspected visually. Retained prior root reading covers all25 text pages and selected visual pages1,6–9; no original Liu1996 full-text reading is claimed. The exact source method and assumption boundaries support the maintained claims. Source access timestamps remain separate from this actual review reading time.

Selection: Exact maintained ID: AIMech:LiuModifiedGibbsSampler
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 09acb520b62acc87b8c9fc0ca24bff277d883851.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:LiuModifiedGibbsSampler | data/curated/LiuModifiedGibbsSampler.yaml | maintained | Liu modified discrete-state Gibbs sampler |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:LiuModifiedGibbsSampler | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 302.62s (0:05:02)<br>Checked 442 record(s); 0 failed.<br>Checked 706 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 395 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 397,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:LiuModifiedGibbsSampler | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| just render | passed | True | AIMech:LiuModifiedGibbsSampler | Rendered AIMech site under /private/tmp/aimech-discovery-recovery-worktree-20261012/pages<br>uv run --locked python scripts/render_pages.py<br> |
| just render-check | passed | True | AIMech:LiuModifiedGibbsSampler | pages/ is current<br>uv run --locked python scripts/render_pages.py --check<br> |
| uv run --locked aimech check-source | passed | True | AIMech:LiuModifiedGibbsSampler | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:LiuModifiedGibbsSampler | Actual command exited zero without output. |
| python3 research/discovery/gibbs-fiber-guided-walk-boundaries.py | passed | True | AIMech:LiuModifiedGibbsSampler | {<br>  "scope": "Original bounded rational illustrations and explicit analytic flow identities; no author/library runtime, benchmark replication, whole-repository gate or scientific approval.",<br>  "liu": {<br>    "supported_subspace_cases_including_zero_mass_categories": 116,<br>    "support_example": [<br>      [<br>        1,<br>        3<br>      ],<br>      [<br>        "2/3",<br>        "1/3"<br>      ],<br>      [<br>        [<br>          "1/2",<br>          "1/2"<br>        ],<br>        [<br>          "1",<br>          "0"<br>        ]<br>      ]<br>    ],<br>    "point_mass_example": [<br>      [<br>        2<br>      ],<br>      [<br>        "1"<br>      ],<br>      [<br>        [<br>          1<br>        ]<br>      ]<br>    ],<br>    "uniform_binary_period": 2,<br>    "sweep_counterexample": {<br>      "target_weights": [<br>        4,<br>        2,<br>        2,<br>        1<br>      ],<br>      "target": [<br>        "4/9",<br>        "2/9",<br>        "2/9",<br>        "1/9"<br>      ],<br>      "states": [<br>        [<br>          0,<br>          0<br>        ],<br>        [<br>          0,<br>          1<br>        ],<br>        [<br>          1,<br>          0<br>        ],<br>        [<br>          1,<br>          1<br>        ]<br>      ],<br>      "centered_observable": [<br>        1,<br>        -2,<br>        -2,<br>        4<br>      ],<br>      "exact_gibbs_sweep_kernel": [<br>        [<br>          "4/9",<br>          "2/9",<br>          "2/9",<br>          "1/9"<br>        ],<br>        [<br>          "4/9",<br>          "2/9",<br>          "2/9",<br>          "1/9"<br>        ],<br>        [<br>          "4/9",<br>          "2/9",<br>          "2/9",<br>          "1/9"<br>        ],<br>        [<br>          "4/9",<br>          "2/9",<br>          "2/9",<br>          "1/9"<br>        ]<br>      ],<br>      "liu_sweep_kernel": [<br>        [<br>          "1/4",<br>          "1/4",<br>          "1/4",<br>          "1/4"<br>        ],<br>        [<br>          "1/2",<br>          "0",<br>          "1/2",<br>          "0"<br>        ],<br>        [<br>          "1/2",<br>          "1/2",<br>          "0",<br>          "0"<br>        ],<br>        [<br>          "1",<br>          "0",<br>          "0",<br>          "0"<br>        ]<br>      ],<br>      "uniform_random_permutation_equals_fixed_sweep_here": true,<br>      "both_sweep_kernels_reversible_irreducible_aperiodic": true,<br>      "asymptotic_variance_per_full_sweep": {<br>        "liu": "20/3",<br>        "gibbs": "4"<br>      },<br>      "asymptotic_variance_per_single_fixed_random_scan_update": {<br>        "liu": "4/3",<br>        "gibbs": "4"<br>      },<br>      "failed_sweep_off_diagonal_domination": [<br>        {<br>          "from": [<br>            0,<br>            1<br>          ],<br>          "to": [<br>            1,<br>            1<br>          ],<br>          "modified": "0",<br>          "gibbs": "1/9"<br>        },<br>        {<br>          "from": [<br>            1,<br>            0<br>          ],<br>          "to": [<br>            1,<br>            1<br>          ],<br>          "modified": "0",<br>          "gibbs": "1/9"<br>        },<br>        {<br>          "from": [<br>            1,<br>            1<br>          ],<br>          "to": [<br>            0,<br>            1<br>          ],<br>          "modified": "0",<br>          "gibbs": "2/9"<br>        },<br>        {<br>          "from": [<br>            1,<br>            1<br>          ],<br>          "to": [<br>            1,<br>            0<br>          ],<br>          "modified": "0",<br>          "gibbs": "2/9"<br>        }<br>      ],<br>      "meaning": "Local Peskun ordering does not transfer automatically to full sweeps, including reversible uniform random-permutation sweeps. No wall-clock comparison."<br>    },<br>    "dependent_target_scan_check": {<br>      "weights": [<br>        1,<br>        2,<br>        3,<br>        4<br>      ],<br>      "systematic_invariant_nonreversible": true,<br>      "uniform_random_permutation_invariant_reversible": true,<br>      "state_dependent_selection_counterexample_after": [<br>        "1/5",<br>        "1/10",<br>        "3/5",<br>        "1/10"<br>      ]<br>    }<br>  },<br>  "dhn": {<br>    "construction": "Independent separate reversible MH-proposal and sign matrices composed then mixed; all exact, with explicit proposal involution check.",<br>    "degenerate_fiber_families": [<br>      {<br>        "family": "one_state",<br>        "positive_cases": 4,<br>        "states": 1,<br>        "signs": 2<br>      },<br>      {<br>        "family": "one_state_three_signs",<br>        "positive_cases": 16,<br>        "states": 1,<br>        "signs": 8<br>      },<br>      {<br>        "family": "one_line",<br>        "positive_cases": 16,<br>        "states": 3,<br>        "signs": 2<br>      },<br>      {<br>        "family": "overlapping_with_singletons",<br>        "positive_cases": 32,<br>        "states": 3,<br>        "signs": 4<br>      },<br>      {<br>        "family": "singleton_partition_plus_line",<br>        "positive_cases": 32,<br>        "states": 3,<br>        "signs": 4<br>      },<br>      {<br>        "family": "oppositely_ordered_duplicate_partition",<br>        "positive_cases": 32,<br>        "states": 3,<br>        "signs": 4<br>      },<br>      {<br>        "family": "grid",<br>        "positive_cases": 64,<br>        "states": 4,<br>        "signs": 4<br>      }<br>    ],<br>    "total_positive_cases": 196,<br>    "disconnected_partition_example": {<br>      "invariant": true,<br>      "irreducible": false<br>    },<br>    "zero_direction_selection_example": {<br>      "invariant": true,<br>      "irreducible": false,<br>      "reason": "An unselected sign remains frozen."<br>    },<br>    "theta_endpoints": [<br>      {<br>        "n": 1,<br>        "theta": "0",<br>        "invariant": true,<br>        "irreducible": true,<br>        "period": 2,<br>        "reachable_state_counts": [<br>          2<br>        ]<br>      },<br>      {<br>        "n": 1,<br>        "theta": "1",<br>        "invariant": true,<br>        "irreducible": false,<br>        "period": null,<br>        "reachable_state_counts": [<br>          1<br>        ]<br>      },<br>      {<br>        "n": 2,<br>        "theta": "0",<br>        "invariant": true,<br>        "irreducible": true,<br>        "period": 4,<br>        "reachable_state_counts": [<br>          4<br>        ]<br>      },<br>      {<br>        "n": 2,<br>        "theta": "1",<br>        "invariant": true,<br>        "irreducible": false,<br>        "period": null,<br>        "reachable_state_counts": [<br>          1,<br>          2<br>        ]<br>      },<br>      {<br>        "n": 3,<br>        "theta": "0",<br>        "invariant": true,<br>        "irreducible": true,<br>        "period": 6,<br>        "reachable_state_counts": [<br>          6<br>        ]<br>      },<br>      {<br>        "n": 3,<br>        "theta": "1",<br>        "invariant": true,<br>        "irreducible": false,<br>        "period": null,<br>        "reachable_state_counts": [<br>          1,<br>          2<br>        ]<br>      }<br>    ],<br>    "scope": "Singleton lines, redundant/overlapping partitions and one-state spaces are allowed by the tested finite construction. Positivity/connectivity/fixed-mixture assumptions must not be silently removed."<br>  },<br>  "gustafson": {<br>    "continuous_proposal_density": "r_sigma(s)=sqrt(2/pi)/sigma*exp(-s^2/(2 sigma^2)), s&gt;0. q((x,p),(y,-p))=r_sigma(&#124;y-x&#124;) when p(y-x)&gt;0; the reverse proposal has equal density.",<br>    "exact_density_identity": "For A_p(x)=integral_0^infinity r_sigma(s)*min(pi(x-p*s),pi(x)) ds, incoming acceptance density at(x,p) is A_p(x)/2 and incoming rejection density from(x,-p) is[pi(x)-A_p(x)]/2; total pi(x)/2. Assumes proper measurable target density and well-defined finite positive current density, fixed sigma&gt;0. Zero density outside support is included in the integral.",<br>    "uniform_target_incoming_example": {<br>      "x": 0.25,<br>      "sigma": 1.0,<br>      "half_normal_cdf_to_left_boundary": 0.19741265136584743,<br>      "accepted_incoming_plus_density": 0.09870632568292372,<br>      "rejection_from_minus_density": 0.4012936743170763,<br>      "correct_total_density": 0.5,<br>      "wrong_same_sign_rejection_density": 0.3253336780597919,<br>      "target_plus_density": 0.5,<br>      "numeric_scope": "math.erf floating evaluation only; the displayed analytic identity supplies exact cancellation."<br>    },<br>    "negative_control_distinction": "Keeping the old sign on both acceptance and rejection breaks the augmented target in this example. Omitting the final unconditional flip from the equivalent MH-plus-flip representation instead leaves a different valid reversible MH kernel: it is not the same negative control.",<br>    "nonreversibility_witness": "On a positive-density interval, accepted transitions from(x,+) to(y,+), y&gt;x, have positive density but their direct reverse with unchanged plus sign has zero density. The complete guided-walk kernel differs from reversible ordinary MH.",<br>    "support_note": "No reflection, clipping, rejection-resampling or connected-support assumption is needed for the invariance identity. The unbounded half-normal law can jump across zero-density gaps. This calculation does not certify general Harris recurrence, rates or a multivariate bookkeeping implementation.",<br>    "scale_endpoint": "sigma=0 lies outside the draft definition; then y=x and acceptance1 leaves both state/sign unchanged, giving an identity kernel."<br>  }<br>}<br> |
| python3 research/discovery/liu-modified-gibbs-boundaries.py | passed | True | AIMech:LiuModifiedGibbsSampler | {<br>  "scope": "Independent exact finite algebra checks, not author-code replication, scientific approval, floating-point/library execution or a general proof.",<br>  "positive_conditional_cases": 360,<br>  "checks": "Rows stochastic, conditional invariance, detailed balance, off-diagonal domination of the independent conditional draw, equality of proposal/acceptance and min-form kernels, equivalence of NumPyro 0.7.0 correction algebra under positive finite conditional weights.",<br>  "example": {<br>    "conditional": [<br>      "3/5",<br>      "3/10",<br>      "1/10"<br>    ],<br>    "kernel": [<br>      [<br>        "29/63",<br>        "3/7",<br>        "1/9"<br>      ],<br>      [<br>        "6/7",<br>        "2/63",<br>        "1/9"<br>      ],<br>      [<br>        "2/3",<br>        "1/3",<br>        "0"<br>      ]<br>    ],<br>    "rejection_probability_current_0": "29/63"<br>  },<br>  "point_mass_guard": {<br>    "target": [<br>      1<br>    ],<br>    "kernel": [<br>      [<br>        "1"<br>      ]<br>    ]<br>  },<br>  "uniform_binary_boundary": {<br>    "target": [<br>      "1/2",<br>      "1/2"<br>    ],<br>    "kernel": [<br>      [<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "1",<br>        "0"<br>      ]<br>    ],<br>    "period": 2,<br>    "interpretation": "Propose a different category does not guarantee an aperiodic chain; accepted moves can coexist with periodicity."<br>  },<br>  "scan_boundary": {<br>    "states": [<br>      [<br>        0,<br>        0<br>      ],<br>      [<br>        0,<br>        1<br>      ],<br>      [<br>        1,<br>        0<br>      ],<br>      [<br>        1,<br>        1<br>      ]<br>    ],<br>    "target": [<br>      "1/10",<br>      "1/5",<br>      "3/10",<br>      "2/5"<br>    ],<br>    "random_scan_invariant_reversible": true,<br>    "systematic_order_invariant": true,<br>    "systematic_order_reversible": false,<br>    "systematic_kernel": [<br>      [<br>        "0",<br>        "0",<br>        "0",<br>        "1"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "3/4",<br>        "1/4"<br>      ],<br>      [<br>        "0",<br>        "1/3",<br>        "0",<br>        "2/3"<br>      ],<br>      [<br>        "1/4",<br>        "1/4",<br>        "3/8",<br>        "1/8"<br>      ]<br>    ],<br>    "limitation": "Does not compare asymptotic variances of systematic or random-permutation scan against Gibbs."<br>  },<br>  "pymc_v5_9_0_code_negative_control": {<br>    "target": [<br>      "3/5",<br>      "3/10",<br>      "1/10"<br>    ],<br>    "equation_kernel": [<br>      [<br>        "7/60",<br>        "3/4",<br>        "2/15"<br>      ],<br>      [<br>        "6/7",<br>        "11/420",<br>        "7/60"<br>      ],<br>      [<br>        "2/3",<br>        "1/3",<br>        "0"<br>      ]<br>    ],<br>    "target_after_one_step": [<br>      "827/2100",<br>      "2063/4200",<br>      "23/200"<br>    ],<br>    "preserves_target": false,<br>    "binary_case": [<br>      [<br>        "1",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "1"<br>      ]<br>    ],<br>    "scope": "Exact algebraic interpretation of the inspected source overwriting probabilities before constructing its denominator. Actual PyMC/JAX runtime and floating-point behavior were not tested."<br>  }<br>}<br> |
| python3 research/discovery/dhn-fiber-boundaries.py | passed | True | AIMech:LiuModifiedGibbsSampler | {<br>  "scope": "Exact finite illustrations; not a general proof, convergence-rate computation, author replication, or independent scientific approval.",<br>  "directed_positive_target_cases": 351,<br>  "checks": "Stochastic rows, exact target invariance, irreducibility, positive self-loop (hence aperiodicity for each irreducible case), and failure of detailed balance for the one-dimensional cases.",<br>  "directed_example": {<br>    "weights": [<br>      1,<br>      2,<br>      4<br>    ],<br>    "theta": "1/5",<br>    "states": [<br>      [<br>        [<br>          -1<br>        ],<br>        0<br>      ],<br>      [<br>        [<br>          -1<br>        ],<br>        1<br>      ],<br>      [<br>        [<br>          -1<br>        ],<br>        2<br>      ],<br>      [<br>        [<br>          1<br>        ],<br>        0<br>      ],<br>      [<br>        [<br>          1<br>        ],<br>        1<br>      ],<br>      [<br>        [<br>          1<br>        ],<br>        2<br>      ]<br>    ],<br>    "transition": [<br>      [<br>        "1/5",<br>        "0",<br>        "0",<br>        "4/5",<br>        "0",<br>        "0"<br>      ],<br>      [<br>        "2/5",<br>        "1/10",<br>        "0",<br>        "1/10",<br>        "2/5",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "2/5",<br>        "1/10",<br>        "0",<br>        "1/10",<br>        "2/5"<br>      ],<br>      [<br>        "0",<br>        "1/5",<br>        "0",<br>        "0",<br>        "4/5",<br>        "0"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "1/5",<br>        "0",<br>        "0",<br>        "4/5"<br>      ],<br>      [<br>        "0",<br>        "0",<br>        "4/5",<br>        "0",<br>        "0",<br>        "1/5"<br>      ]<br>    ],<br>    "invariant": [<br>      "1/14",<br>      "1/7",<br>      "2/7",<br>      "1/14",<br>      "1/7",<br>      "2/7"<br>    ]<br>  },<br>  "theta_zero_uniform_boundary": {<br>    "period": 10,<br>    "cycle": [<br>      [<br>        [<br>          -1<br>        ],<br>        0<br>      ],<br>      [<br>        [<br>          1<br>        ],<br>        0<br>      ],<br>      [<br>        [<br>          1<br>        ],<br>        1<br>      ],<br>      [<br>        [<br>          1<br>        ],<br>        2<br>      ],<br>      [<br>        [<br>          1<br>        ],<br>        3<br>      ],<br>      [<br>        [<br>          1<br>        ],<br>        4<br>      ],<br>      [<br>        [<br>          -1<br>        ],<br>        4<br>      ],<br>      [<br>        [<br>          -1<br>        ],<br>        3<br>      ],<br>      [<br>        [<br>          -1<br>        ],<br>        2<br>      ],<br>      [<br>        [<br>          -1<br>        ],<br>        1<br>      ]<br>    ]<br>  },<br>  "theta_one_uniform_boundary": {<br>    "closed_classes": [<br>      [<br>        [<br>          [<br>            -1<br>          ],<br>          0<br>        ]<br>      ],<br>      [<br>        [<br>          [<br>            -1<br>          ],<br>          1<br>        ],<br>        [<br>          [<br>            1<br>          ],<br>          0<br>        ]<br>      ],<br>      [<br>        [<br>          [<br>            -1<br>          ],<br>          2<br>        ],<br>        [<br>          [<br>            1<br>          ],<br>          1<br>        ]<br>      ],<br>      [<br>        [<br>          [<br>            -1<br>          ],<br>          3<br>        ],<br>        [<br>          [<br>            1<br>          ],<br>          2<br>        ]<br>      ],<br>      [<br>        [<br>          [<br>            -1<br>          ],<br>          4<br>        ],<br>        [<br>          [<br>            1<br>          ],<br>          3<br>        ]<br>      ],<br>      [<br>        [<br>          [<br>            1<br>          ],<br>          4<br>        ]<br>      ]<br>    ]<br>  },<br>  "fiber_positive_target_cases": 64,<br>  "fiber_scope": "Two directions on a 2 by 2 grid, four persistent sign vectors, positive selection probabilities 1/3 and 2/3; checked invariance, irreducibility and aperiodicity.",<br>  "limitations": "No empirical results or total-variation/chi-square rate claims tested. Endpoint theta values illustrate why the reported ergodicity proposition uses 0&lt;theta&lt;1."<br>}<br> |

## Scientific And Domain Assessments

### Liu modified discrete-state Gibbs sampler

identity: supported. Targets: AIMech:LiuModifiedGibbsSampler.

Retain the narrow DRAFT identity within the documented search scope.

The record identifies the finite categorical conditional update attributed to Liu 1996: exclude the present category in the conditional proposal and apply its precise Metropolis correction. Ordinary Gibbs draws directly from the full conditional; generic Metropolis-within-Gibbs allows many other proposals. Multiple-try Metropolis-within-Gibbs has a candidate-set/reference-set mechanism. Neal’s ordered-pair backtracking-suppression construction can use this update as an ingredient, but has a different full state and algorithm identity. The maintained scope is the local conditional update, with scan compositions explicitly qualified. Bare metropolized Gibbs, every modified Gibbs sampler, a whole library sampler class and Liu’s different 1996 independence-sampler paper are not exact aliases.

### Definition and source scope

evidence: supported. Targets: AIMech:LiuModifiedGibbsSampler.

The maintained definition is supported within its stated method scope.

The definition specifies a discrete conditional algorithm and its exclusion-plus-correction mechanism. Its detailed claims narrow the operation to a finite conditional and a supported current category, with a point-mass stay rule. It does not describe a nonreversible pair lift or promise that every iteration moves. Neal 2004 Section 3 PDF p. 5 attributes the modification to Liu and displays both the excluded-current proposal and Eq 9 acceptance; PDF p. 6 states scan-order qualifications. Section 4 Eq 16 supplies the min-form conditional kernel in the separate pair-chain application. Original Liu 1996 is known through inspected metadata/abstract but its full text was not obtained. No unseen original proof or author implementation is claimed. The record can use this inspected primary mathematical exposition while preserving the original-source access gap. The inspected source version is arXiv:math/0407281v1 / Technical Report 0406, cover 15 July 2004.

### Related Markov-process mapping

grounding: supported. Targets: AIMech:LiuModifiedGibbsSampler.

related_match expresses method-to-process association without equivalence or ontology inheritance.

The related_match to AIO:MarkovChain is supported. The algorithm constructs Markov transitions on a specified conditional or augmented state, supporting a method-to-process association. The pinned target is a stochastic process/model exported under Network, with a ProbabilisticHiddenLayer has-part assertion. Equivalence, subclass membership and inheritance of those assertions are not warranted. The dated identity/mapping handoff read eighteen complete exact CLASS contexts, all incident edges and their generated YAML: the target plus the seventeen alternatives documented here. This rationale concerns the pinned snapshot and manifest retained in the review inputs.
Alternatives:
AIO:Network: A target-invariant transition procedure is not a network architecture. A Markov graph representation does not establish an exact or broader-class mapping to Network.
AIO:ProbabilisticHiddenLayer: A retained sign, conditional category or auxiliary state is not a neural hidden layer that estimates probabilities. The MarkovChain has-part edge is context, not an inherited algorithm assertion.
AIO:Model: A target distribution or model may be an input or application; the maintained identity is the transition algorithm, not a fitted statistical or predictive model.
AIO:MachineLearningTask: These records specify operational sampling mechanisms, not a machine-learning problem or task definition.
AIO:TrainingStrategy: Use of a sampler during learning does not make its invariant transition rule a training strategy.
AIO:MathematicalFunction: Update equations describe the mechanism, but they do not make a randomized target-preserving procedure merely a mathematical input-output function.
AIO:BayesianNetwork: Bayesian inference is an application; no directed acyclic dependency graph is required by these transition rules.
AIO:ProbabilisticGraphicalModel: A graphical target distribution is optional. The pinned graph-factorization/task identity is distinct from a sampler acting on a specified target.
AIO:UnsupervisedLearning: No learning-from-unlabeled-data objective is needed to define these finite or continuous sampling kernels.
AIO:BoltzmannMachineNetwork: A Boltzmann machine may be a target/application, but no recurrent stochastic network architecture is required.
AIO:RestrictedBoltzmannMachine: Sampling a restricted Boltzmann machine does not make a general conditional update or direction-based kernel that model architecture.
AIO:EnergyBasedLLM: The exact pinned CLASS denotes an explicit token-sequence density language model. A broader related synonym does not replace that definition or make it a generic energy-target sampler.
AIO:ImplicitLanguageModel: Whole-sequence language-model scoring is not the identity of these sampling mechanisms.
AIO:Preprocessing: The methods construct target-invariant transitions rather than prepare raw data for analysis.
AIO:Layer: A transition stage or stored direction is not a neural-network layer.
AIO:HiddenLayer: Auxiliary direction memory is not a nonlinear hidden neural layer.
AIO:CausalGraphicalModel: These target distributions need not encode causal assumptions; a causal-model application is not algorithm identity.

### excluded-current-conditional-proposal

evidence: supported. Targets: AIMech:LiuModifiedGibbsSampler.

Supported within the stated assumptions and inspected passages.

For a supported current category a, p_a&lt;1 permits normalization over the remaining categories: q(c&#124;a)=p_c/(1-p_a). Zero-mass categories are never proposed. At p_a=1, the only supported state stays without evaluating the undefined proposal. This matches the explicit point-mass exception below Neal 2004 Eq 9. The original calculator’s strictly positive-domain check is supplemented by 116 input vectors with zero masses, evaluated on their positive support; no outgoing rule from an unsupported current state is invented.

### conditional-metropolis-correction

evidence: supported. Targets: AIMech:LiuModifiedGibbsSampler.

Supported within the stated assumptions and inspected passages.

Multiplying q(c&#124;a) by min(1,(1-p_a)/(1-p_c)) yields the stated min-form off-diagonal entry. The diagonal is rejection mass, not a requirement to change category on every step. Both masses in the correction are the original conditional probabilities. The supported equation differs from any expression that mistakenly substitutes the renormalized proposal probability. No unrelated library-runtime behavior is used as positive evidence.

### conditional-balance-and-joint-invariance

evidence: supported. Targets: AIMech:LiuModifiedGibbsSampler.

Supported within the stated assumptions and inspected passages.

For distinct supported a,c, p_a*U(a,c) is symmetric in a,c; row completion then yields local detailed balance. Each denominator is at most one, so U(a,c)&gt;=p_c. Conditioning on the other variables gives joint-target invariance without a persistent sign or previous joint state. This off-diagonal domination concerns the local transition, not an arbitrary composite update or its mixing time. The equal-mass binary kernel has period two, which prevents inferring aperiodicity merely from invariance.

### scan-schedule-and-comparison-boundary

evidence: supported. Targets: AIMech:LiuModifiedGibbsSampler.

Supported within the stated assumptions and inspected passages.

A mixture with fixed component-selection probabilities preserves reversibility and the joint target; a sequential composition preserves invariance but can fail detailed balance. A uniform mixture over all permutation sweeps is reversible because reverse-order compositions pair as adjoints, but local Peskun domination still need not order the full-sweep matrices. The bounded counterexample has independent binary target weights (4,2,2,1)/9 and centered observable (1,-2,-2,4). Its modified full sweep has asymptotic variance 20/3 versus 4 for exact-Gibbs full sweeps; both are reversible, irreducible and aperiodic, and uniform random-permutation equals the fixed sweep here. The corresponding single-coordinate fixed random scan gives 4/3 versus 4. These are different per-transition units, not a wall-clock comparison or a general superiority claim. They justify the record’s cautious scan boundary.

### local-update-versus-pair-state-construction

evidence: supported. Targets: AIMech:LiuModifiedGibbsSampler.

Supported within the stated assumptions and inspected passages.

Neal introduces the Liu update before the separate ordered-pair swap/update construction. Its role as an ingredient does not equate the locally reversible conditional kernel with the augmented nonreversible chain. A proposal excludes the current category but rejection can retain it; older revisits are also possible. The record correctly separates these meanings of suppression.

### finite supported conditional, correct excluded-current normalization, point-mass guard, local reversibility, explicit scan schedule and local-versus-pair-chain identity

consistency: supported. Targets: AIMech:LiuModifiedGibbsSampler.

Mechanism, scan/parameter limits and identity boundaries remain qualified.

No new general Peskun theorem, arbitrary joint scan/adaptation guarantee, continuous nonatomic improvement, universal efficiency, author-code replication or library-runtime certification. The original Liu full-text access gap remains explicit and Neal 2024 variants remain an open source-assessment lead.

### All captured maintained fields

provenance: supported. Targets: AIMech:LiuModifiedGibbsSampler.

Root reassessed the complete current record after canonical capture; DRAFT remains.

Full maintained record and all five claim/source locators reread after capture. Equation9 proposal and acceptance use original conditional masses; Eq16 min form and diagonal rejection agree. Supported-current/point-mass guards, local detailed balance, joint invariance, fixed-mixture reversibility and composition limitations are sound. The exact full-sweep counterexample and binary periodicity support the qualifications without transferring local Peskun ordering to arbitrary sweeps. Alias absence and distinct local versus ordered-pair identity remain appropriate. All remaining maintained fields, identity notes, source version/access/hash, AIO pin and related mapping, limitations, DRAFT status and curation metadata were assessed. Root reread the complete assessment configuration after capture and agrees within its stated bounds. Root retained the earlier full18AIO-context reading and seven nearest-native readings; broader182semantic/19native assessment remains attributed to the supporting source agent. Current integrity checks confirm no prior canonical bytes changed. The corrected mathematical audit and original erroneous15-versus21July metadata lineage were inspected; the15July successor governs, with unchanged scientific content. Root also read the actual-content supporting audit, which identifies no required correction and remains part of the same author workflow. Rereads: Neal2004 PDF pages5,6,8 freshly read as extracted text after capture; pages5 and8 freshly inspected visually. Retained prior root reading covers all25 text pages and selected visual pages1,6–9; no original Liu1996 full-text reading is claimed.

### Original and corrected mathematical audit lineage

provenance: supported. Targets: AIMech:LiuModifiedGibbsSampler.

The bibliographic correction is explicit and scientific audit content is unchanged.

Original created_at, draft inputs, findings and calculation audit are retained. The corrected successor governs; no future review/gate is inferred from the correction.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T210245Z-gibbs-fiber-guided-walk.json; identity_search and identity_assessment | supports | Whole-corpus normalized checks cover every ID, name, alias and scoped synonym in 442 pinned AIO and 703 native records; four complete checkouts, including ignored and hidden files, are searched for final identities and researched labels. The finite excluded-current conditional proposal with its specific acceptance correction is distinct from exact Gibbs, generic Metropolis-within-Gibbs, multiple-try updates and Neal’s full ordered-pair construction. Bare metropolized Gibbs is a search probe, not an exact alias. Existing source-frontier references are resolved in place. Related AIO:MarkovChain is supported at a different abstraction level; all 18 candidate class contexts and 19 nearest native records are preserved. |
| mapping | research/discovery/20261014T210245Z-gibbs-fiber-guided-walk.json; mapping_context nodes, native_neighbors, semantic_rows and mapping_assessment | supports | The related_match to AIO:MarkovChain is supported. The algorithm constructs Markov transitions on a specified conditional or augmented state, supporting a method-to-process association. The pinned target is a stochastic process/model exported under Network, with a ProbabilisticHiddenLayer has-part assertion. Equivalence, subclass membership and inheritance of those assertions are not warranted. The dated identity/mapping handoff read eighteen complete exact CLASS contexts, all incident edges and their generated YAML: the target plus the seventeen alternatives documented here. This rationale concerns the pinned snapshot and manifest retained in the review inputs. |
| actual-record-reading | data/curated/LiuModifiedGibbsSampler.yaml | supports | Full maintained record and all five claim/source locators reread after capture. Equation9 proposal and acceptance use original conditional masses; Eq16 min form and diagonal rejection agree. Supported-current/point-mass guards, local detailed balance, joint invariance, fixed-mixture reversibility and composition limitations are sound. The exact full-sweep counterexample and binary periodicity support the qualifications without transferring local Peskun ordering to arbitrary sweeps. Alias absence and distinct local versus ordered-pair identity remain appropriate. All remaining maintained fields, identity notes, source version/access/hash, AIO pin and related mapping, limitations, DRAFT status and curation metadata were assessed. Root reread the complete assessment configuration after capture and agrees within its stated bounds. Root retained the earlier full18AIO-context reading and seven nearest-native readings; broader182semantic/19native assessment remains attributed to the supporting source agent. Current integrity checks confirm no prior canonical bytes changed. The corrected mathematical audit and original erroneous15-versus21July metadata lineage were inspected; the15July successor governs, with unchanged scientific content. Root also read the actual-content supporting audit, which identifies no required correction and remains part of the same author workflow. Actual post-capture source reread: Neal2004 PDF pages5,6,8 freshly read as extracted text after capture; pages5 and8 freshly inspected visually. Retained prior root reading covers all25 text pages and selected visual pages1,6–9; no original Liu1996 full-text reading is claimed. |
| neal2004 | https://arxiv.org/pdf/math/0407281v1; Section 3, PDF p. 5, Liu conditional proposal and Equation 9; Section 3, PDF p. 5, paragraph preceding Equation 9 and point-mass exception below it; Section 3, PDF p. 5, Equation 9; Section 4, PDF p. 8, Equation 16 and diagonal completion; Section 3, PDF pp. 5–6, Equation 9 and ensuing off-diagonal comparison; Section 4, PDF p. 8, Equation 16; Section 3, PDF pp. 5–6, Peskun qualifications and scan-order discussion; Section 3 conclusion and Section 4, PDF pp. 6–8, Equations 10–16 | supports | arXiv:math/0407281v1, submitted 15 July 2004; Technical Report 0406, dated 15 July 2004; 25 PDF pages. Actual root reading: Neal2004 PDF pages5,6,8 freshly read as extracted text after capture; pages5 and8 freshly inspected visually. Retained prior root reading covers all25 text pages and selected visual pages1,6–9; no original Liu1996 full-text reading is claimed. The exact source method and assumption boundaries support the maintained claims. Source access timestamps remain separate from this actual review reading time. |
| calculation | research/discovery/gibbs-fiber-guided-walk-boundaries.py; Combined result section liu | supports | Original bounded checks: exact rational finite transitions and scan examples; analytic continuous cancellation with separately labeled floating erf illustration. Not author-code replication or a general convergence theorem. Selected result: {"supported_subspace_cases_including_zero_mass_categories": 116, "support_example": [[1, 3], ["2/3", "1/3"], [["1/2", "1/2"], ["1", "0"]]], "point_mass_example": [[2], ["1"], [[1]]], "uniform_binary_period": 2, "sweep_counterexample": {"target_weights": [4, 2, 2, 1], "target": ["4/9", "2/9", "2/9", "1/9"], "states": [[0, 0], [0, 1], [1, 0], [1, 1]], "centered_observable": [1, -2, -2, 4], "exact_gibbs_sweep_kernel": [["4/9", "2/9", "2/9", "1/9"], ["4/9", "2/9", "2/9", "1/9"], ["4/9", "2/9", "2/9", "1/9"], ["4/9", "2/9", "2/9", "1/9"]], "liu_sweep_kernel": [["1/4", "1/4", "1/4", "1/4"], ["1/2", "0", "1/2", "0"], ["1/2", "1/2", "0", "0"], ["1", "0", "0", "0"]], "uniform_random_permutation_equals_fixed_sweep_here": true, "both_sweep_kernels_reversible_irreducible_aperiodic": true, "asymptotic_variance_per_full_sweep": {"liu": "20/3", "gibbs": "4"}, "asymptotic_variance_per_single_fixed_random_scan_update": {"liu": "4/3", "gibbs": "4"}, "failed_sweep_off_diagonal_domination": [{"from": [0, 1], "to": [1, 1], "modified": "0", "gibbs": "1/9"}, {"from": [1, 0], "to": [1, 1], "modified": "0", "gibbs": "1/9"}, {"from": [1, 1], "to": [0, 1], "modified": "0", "gibbs": "2/9"}, {"from": [1, 1], "to": [1, 0], "modified": "0", "gibbs": "2/9"}], "meaning": "Local Peskun ordering does not transfer automatically to full sweeps, including reversible uniform random-permutation sweeps. No wall-clock comparison."}, "dependent_target_scan_check": {"weights": [1, 2, 3, 4], "systematic_invariant_nonreversible": true, "uniform_random_permutation_invariant_reversible": true, "state_dependent_selection_counterexample_after": ["1/5", "1/10", "3/5", "1/10"]}} |
| supporting-math-audit | research/discovery/20261014T203348Z-gibbs-fiber-guided-walk-supporting-math-audit.json | supports | Root assessed the corrected bounded mathematical audit; supporting agents belong to the same author workflow and provide no independent scientific approval. |
| metadata-correction-lineage | research/discovery/20261014T210245Z-gibbs-fiber-guided-walk.json; supporting_math_audit_correction_lineage and source_analysis.bounded_math_audit | supports | The original audit incorrectly dated Neal v1 as 21 July 2004. The explicitly corrected successor uses 15 July; original object/hash, actual correction metadata and unchanged scientific sections are preserved. |

## Limits And Additional Notes

- Author self-review, not independent scientific approval or DRAFT promotion.
- No new general Peskun theorem, arbitrary joint scan/adaptation guarantee, continuous nonatomic improvement, universal efficiency, author-code replication or library-runtime certification. The original Liu full-text access gap remains explicit and Neal 2024 variants remain an open source-assessment lead.
- The bounded calculators illustrate local identities and finite scan counterexamples; they do not replace primary evidence or required repository checks.
- Neither a reversible random-permutation sweep nor a systematic sweep automatically inherits local off-diagonal dominance.
- Original Liu 1996 full PDF was not obtained: publisher/author access attempts are preserved in source handoff. The curated method uses inspected Neal 2004 equations, not unseen original proofs or an abstract as method evidence.
- DHN source is the 5 June 1997 author technical report; the 2000 journal PDF was not obtained or read. Source reading is selective and does not establish inspection of every spectral proof.
- Gustafson journal-layout PDF came from the observed public Studyres mirror. Publisher-download byte equivalence was not established; no redistribution license is inferred. PDF bytes are not copied to the repository.
- Gustafson Example 2 and Example 4/Figure 2 disagree on two numerical performance labels. Those numerals and the experimental first-hit criterion are not adopted as performance or general convergence claims.
- Empty findings reflect actual root assessment of this selected captured record only; no unrelated finding closure or literature saturation is asserted.
- A metadata correction in the supporting audit is retained as provenance, not fabricated maintained-record finding lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T211738Z-liu-modified-gibbs-sampler
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Liu modified discrete-state Gibbs sampler
started_at: '2026-10-14T21:04:24.106232Z'
finished_at: '2026-10-14T21:17:38.677305Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Root author reassessment with supporting source, mathematical
    and integrity agents in the same author workflow; no independent scientific approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the narrow Liu conditional update as DRAFT with related_match to MarkovChain.
  The displayed mechanism and local balance are supported; full-sweep variance ordering
  and universal convergence are excluded. The original Liu full-text gap and explicit
  scan-schedule qualifications remain limitations.
source:
  git_revision: 09acb520b62acc87b8c9fc0ca24bff277d883851
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/BoltzmannMachineNetwork.yaml
    sha256: 1152d2d85c5c1c408a0420e13f211ed109b12fb289c706ee7449864e91aece03
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/EnergyBasedLLM.yaml
    sha256: e9e29aa4f8400ad463dfe058fade876ef36c4a2637e1ebc4b42688116896310b
    role: context
  - path: data/aio/HiddenLayer.yaml
    sha256: 945f974c1d298a827086c3439ec3f9ae029380f6d2fa52378eb95ccad1f3b886
    role: context
  - path: data/aio/ImplicitLanguageModel.yaml
    sha256: 818c396b19757360dcdff6291a85d589c50638e0dc6d6bfcd96fdcb7bdf46ce9
    role: context
  - path: data/aio/Layer.yaml
    sha256: 46b533d2f0afcbdeadb7c35f8c382d66e51e0f5edf90b0c3552767687d34fa87
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
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/Network.yaml
    sha256: ec24eb397241fe903137b2d8c8f4081d0f9d246c296c247864f199e160a3ee30
    role: context
  - path: data/aio/Preprocessing.yaml
    sha256: 2c4a30f4f829a757be1feabf78d15780eedf93681a62eede3e76b2304f21bb7a
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ProbabilisticHiddenLayer.yaml
    sha256: 610c29db815f7348c5bdcdc7e7460dd2dea9ea338f3727ebb1596c51b4af41da
    role: context
  - path: data/aio/RestrictedBoltzmannMachine.yaml
    sha256: 322fcb3b1f6064d944379ed79ffdcb7360fc2c3edd300c0a5a3f46be1f48df43
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/AnnealedImportanceSampling.yaml
    sha256: 94c7b8e597f3551b2b804778e11385d6ec9137515bc44a9c9d429268869f7e68
    role: context
  - path: data/curated/BarkerAcceptanceRule.yaml
    sha256: e81a763ba4f2eb2c7e51f3e520311bd111d269f45cdf2417055d72a4ddd4d08c
    role: context
  - path: data/curated/DiaconisHolmesNealFiberSampler.yaml
    sha256: 2c9a3659fe85b5cb71cc22d7e9198c732aa3bdaed398f2b25793d514eeb0f3a6
    role: context
  - path: data/curated/FastPersistentContrastiveDivergence.yaml
    sha256: 3049a144e2c5e8c8afeda5182d1cdcd4da5a3e2d2a75257c10d7f9f5b85236b4
    role: context
  - path: data/curated/GibbsSampling.yaml
    sha256: 8175215986c0507e3664a3aedf8074fc067d85b4a89002091d1bcb9b637a522a
    role: context
  - path: data/curated/GustafsonGuidedWalkMetropolis.yaml
    sha256: 839d08e76d362a34ead45d72c7e4d31bfbb29833b8638f31ff7c32d26ff5e67d
    role: context
  - path: data/curated/HamiltonianMonteCarlo.yaml
    sha256: 28367594dbc36a8357c33a4e639aeb0fefdd47adc8c46e2b3d5feb96b67e84ca
    role: context
  - path: data/curated/IndependenceMetropolisHastings.yaml
    sha256: ca1390f00edca43e94f897e2398b3f7d8edddefadc0a5780e0b470816a7754df
    role: context
  - path: data/curated/LiuModifiedGibbsSampler.yaml
    sha256: b3736d9f8dfb1e8b7e218d2b8fc075f413a719dc1c11cee951af8fa3b4542e54
    role: target
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
  - path: data/curated/MultipleTryMetropolisWithinGibbs.yaml
    sha256: 539c4d93eff27f5e064abb16fe3e892406ad5dc3d3a6bceb314f4eee37b2a727
    role: context
  - path: data/curated/NealBacktrackingSuppressedMCMC.yaml
    sha256: 1da524622ec40d25aac45313cdbd6412adf1376c6c8b78eeecaded8eb561a0be
    role: context
  - path: data/curated/NonreversibleMetropolisUniformUpdate.yaml
    sha256: 27dbec2b01a48103d709df4b9ab94bba36083bd27acb69af1e3bc70ab6ab4ecd
    role: context
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
  - path: research/discovery/20261014T203348Z-gibbs-fiber-guided-walk-supporting-math-audit.json
    sha256: cb907256334387fed3a86d5904ed0f07e44222547c109db88d2aab6a24f8555a
    role: context
  - path: research/discovery/20261014T210245Z-gibbs-fiber-guided-walk.json
    sha256: bde6dea6594397164fdc8aba5e816bdda108127b374885acb694adeb9912acf7
    role: context
  - path: research/discovery/20261014T210245Z-gibbs-fiber-guided-walk.md
    sha256: ecaeed923a355ae9f03964dba3702aebbc4fc0b1ce2940ebebdfb26b2f59532a
    role: context
  - path: research/discovery/dhn-fiber-boundaries.py
    sha256: ff0d94688ced02279037b39d64e5dc653ff937495f50b0a361a3a41a85b9c59b
    role: context
  - path: research/discovery/gibbs-fiber-guided-walk-boundaries.py
    sha256: f4605a688ade559b75acbd2272dc574ee876e765eee0287107640ff552e2b889
    role: context
  - path: research/discovery/liu-modified-gibbs-boundaries.py
    sha256: 34271c625003992c2a4799b4b9a6a517cce9cc2c6614389c43971e7785012f44
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
  - path: src/aimech/history.py
    sha256: 4ff83e818c7f50ea25bfc6b8f2cae7ab29c814310b8b361a6f7af8160055aa91
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
- target_id: AIMech:LiuModifiedGibbsSampler
  path: data/curated/LiuModifiedGibbsSampler.yaml
  label: Liu modified discrete-state Gibbs sampler
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LiuModifiedGibbsSampler.yaml
    role: maintained
scope:
  description: 'All maintained fields of the selected record. Actual source scope:
    Neal2004 PDF pages5,6,8 freshly read as extracted text after capture; pages5 and8
    freshly inspected visually. Retained prior root reading covers all25 text pages
    and selected visual pages1,6–9; no original Liu1996 full-text reading is claimed..
    Neal2004 PDF pages5,6,8 freshly read as extracted text after capture; pages5 and8
    freshly inspected visually. Retained prior root reading covers all25 text pages
    and selected visual pages1,6–9; no original Liu1996 full-text reading is claimed.
    The exact source method and assumption boundaries support the maintained claims.
    Source access timestamps remain separate from this actual review reading time.'
  selection: 'Exact maintained ID: AIMech:LiuModifiedGibbsSampler'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:LiuModifiedGibbsSampler
  exclusions:
  - target: Other batch entries and neighboring identities
    reason: Read as identity/mapping context, not formal review targets.
  - target: Uninspected source versions, general convergence and runtime claims
    reason: No new general Peskun theorem, arbitrary joint scan/adaptation guarantee,
      continuous nonatomic improvement, universal efficiency, author-code replication
      or library-runtime certification. The original Liu full-text access gap remains
      explicit and Neal 2024 variants remain an open source-assessment lead.
  - target: Author implementation and benchmark replication
    reason: Only bounded original calculations and project checks were executed.
checks:
- check_id: gate-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 302.62s (0:05:02)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 706 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 395 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 397,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
  scope_note: Actual execution completed 2026-10-14T21:14:47.131289Z; this generator
    executes no recorded commands.
- check_id: vendor-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
  scope_note: Actual execution completed 2026-10-14T21:05:40.367219Z; this generator
    executes no recorded commands.
- check_id: render-2
  name: just render
  command: just render
  status: passed
  required: true
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  exit_code: 0
  expected_exit_code: 0
  summary: 'Rendered AIMech site under /private/tmp/aimech-discovery-recovery-worktree-20261012/pages

    uv run --locked python scripts/render_pages.py

    '
  scope_note: Actual execution completed 2026-10-14T21:05:06.047854Z; this generator
    executes no recorded commands.
- check_id: render-3
  name: just render-check
  command: just render-check
  status: passed
  required: true
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  exit_code: 0
  expected_exit_code: 0
  summary: 'pages/ is current

    uv run --locked python scripts/render_pages.py --check

    '
  scope_note: Actual execution completed 2026-10-14T21:05:18.844048Z; this generator
    executes no recorded commands.
- check_id: additional-4
  name: uv run --locked aimech check-source
  command: uv run --locked aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
  scope_note: Actual execution completed 2026-10-14T21:05:34.553412Z; this generator
    executes no recorded commands.
- check_id: additional-5
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  exit_code: 0
  expected_exit_code: 0
  summary: Actual command exited zero without output.
  scope_note: Actual execution completed 2026-10-14T21:05:35.583960Z; this generator
    executes no recorded commands.
- check_id: calculation-6
  name: python3 research/discovery/gibbs-fiber-guided-walk-boundaries.py
  command: python3 research/discovery/gibbs-fiber-guided-walk-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"scope\": \"Original bounded rational illustrations and explicit\
    \ analytic flow identities; no author/library runtime, benchmark replication,\
    \ whole-repository gate or scientific approval.\",\n  \"liu\": {\n    \"supported_subspace_cases_including_zero_mass_categories\"\
    : 116,\n    \"support_example\": [\n      [\n        1,\n        3\n      ],\n\
    \      [\n        \"2/3\",\n        \"1/3\"\n      ],\n      [\n        [\n  \
    \        \"1/2\",\n          \"1/2\"\n        ],\n        [\n          \"1\",\n\
    \          \"0\"\n        ]\n      ]\n    ],\n    \"point_mass_example\": [\n\
    \      [\n        2\n      ],\n      [\n        \"1\"\n      ],\n      [\n   \
    \     [\n          1\n        ]\n      ]\n    ],\n    \"uniform_binary_period\"\
    : 2,\n    \"sweep_counterexample\": {\n      \"target_weights\": [\n        4,\n\
    \        2,\n        2,\n        1\n      ],\n      \"target\": [\n        \"\
    4/9\",\n        \"2/9\",\n        \"2/9\",\n        \"1/9\"\n      ],\n      \"\
    states\": [\n        [\n          0,\n          0\n        ],\n        [\n   \
    \       0,\n          1\n        ],\n        [\n          1,\n          0\n  \
    \      ],\n        [\n          1,\n          1\n        ]\n      ],\n      \"\
    centered_observable\": [\n        1,\n        -2,\n        -2,\n        4\n  \
    \    ],\n      \"exact_gibbs_sweep_kernel\": [\n        [\n          \"4/9\",\n\
    \          \"2/9\",\n          \"2/9\",\n          \"1/9\"\n        ],\n     \
    \   [\n          \"4/9\",\n          \"2/9\",\n          \"2/9\",\n          \"\
    1/9\"\n        ],\n        [\n          \"4/9\",\n          \"2/9\",\n       \
    \   \"2/9\",\n          \"1/9\"\n        ],\n        [\n          \"4/9\",\n \
    \         \"2/9\",\n          \"2/9\",\n          \"1/9\"\n        ]\n      ],\n\
    \      \"liu_sweep_kernel\": [\n        [\n          \"1/4\",\n          \"1/4\"\
    ,\n          \"1/4\",\n          \"1/4\"\n        ],\n        [\n          \"\
    1/2\",\n          \"0\",\n          \"1/2\",\n          \"0\"\n        ],\n  \
    \      [\n          \"1/2\",\n          \"1/2\",\n          \"0\",\n         \
    \ \"0\"\n        ],\n        [\n          \"1\",\n          \"0\",\n         \
    \ \"0\",\n          \"0\"\n        ]\n      ],\n      \"uniform_random_permutation_equals_fixed_sweep_here\"\
    : true,\n      \"both_sweep_kernels_reversible_irreducible_aperiodic\": true,\n\
    \      \"asymptotic_variance_per_full_sweep\": {\n        \"liu\": \"20/3\",\n\
    \        \"gibbs\": \"4\"\n      },\n      \"asymptotic_variance_per_single_fixed_random_scan_update\"\
    : {\n        \"liu\": \"4/3\",\n        \"gibbs\": \"4\"\n      },\n      \"failed_sweep_off_diagonal_domination\"\
    : [\n        {\n          \"from\": [\n            0,\n            1\n       \
    \   ],\n          \"to\": [\n            1,\n            1\n          ],\n   \
    \       \"modified\": \"0\",\n          \"gibbs\": \"1/9\"\n        },\n     \
    \   {\n          \"from\": [\n            1,\n            0\n          ],\n  \
    \        \"to\": [\n            1,\n            1\n          ],\n          \"\
    modified\": \"0\",\n          \"gibbs\": \"1/9\"\n        },\n        {\n    \
    \      \"from\": [\n            1,\n            1\n          ],\n          \"\
    to\": [\n            0,\n            1\n          ],\n          \"modified\":\
    \ \"0\",\n          \"gibbs\": \"2/9\"\n        },\n        {\n          \"from\"\
    : [\n            1,\n            1\n          ],\n          \"to\": [\n      \
    \      1,\n            0\n          ],\n          \"modified\": \"0\",\n     \
    \     \"gibbs\": \"2/9\"\n        }\n      ],\n      \"meaning\": \"Local Peskun\
    \ ordering does not transfer automatically to full sweeps, including reversible\
    \ uniform random-permutation sweeps. No wall-clock comparison.\"\n    },\n   \
    \ \"dependent_target_scan_check\": {\n      \"weights\": [\n        1,\n     \
    \   2,\n        3,\n        4\n      ],\n      \"systematic_invariant_nonreversible\"\
    : true,\n      \"uniform_random_permutation_invariant_reversible\": true,\n  \
    \    \"state_dependent_selection_counterexample_after\": [\n        \"1/5\",\n\
    \        \"1/10\",\n        \"3/5\",\n        \"1/10\"\n      ]\n    }\n  },\n\
    \  \"dhn\": {\n    \"construction\": \"Independent separate reversible MH-proposal\
    \ and sign matrices composed then mixed; all exact, with explicit proposal involution\
    \ check.\",\n    \"degenerate_fiber_families\": [\n      {\n        \"family\"\
    : \"one_state\",\n        \"positive_cases\": 4,\n        \"states\": 1,\n   \
    \     \"signs\": 2\n      },\n      {\n        \"family\": \"one_state_three_signs\"\
    ,\n        \"positive_cases\": 16,\n        \"states\": 1,\n        \"signs\"\
    : 8\n      },\n      {\n        \"family\": \"one_line\",\n        \"positive_cases\"\
    : 16,\n        \"states\": 3,\n        \"signs\": 2\n      },\n      {\n     \
    \   \"family\": \"overlapping_with_singletons\",\n        \"positive_cases\":\
    \ 32,\n        \"states\": 3,\n        \"signs\": 4\n      },\n      {\n     \
    \   \"family\": \"singleton_partition_plus_line\",\n        \"positive_cases\"\
    : 32,\n        \"states\": 3,\n        \"signs\": 4\n      },\n      {\n     \
    \   \"family\": \"oppositely_ordered_duplicate_partition\",\n        \"positive_cases\"\
    : 32,\n        \"states\": 3,\n        \"signs\": 4\n      },\n      {\n     \
    \   \"family\": \"grid\",\n        \"positive_cases\": 64,\n        \"states\"\
    : 4,\n        \"signs\": 4\n      }\n    ],\n    \"total_positive_cases\": 196,\n\
    \    \"disconnected_partition_example\": {\n      \"invariant\": true,\n     \
    \ \"irreducible\": false\n    },\n    \"zero_direction_selection_example\": {\n\
    \      \"invariant\": true,\n      \"irreducible\": false,\n      \"reason\":\
    \ \"An unselected sign remains frozen.\"\n    },\n    \"theta_endpoints\": [\n\
    \      {\n        \"n\": 1,\n        \"theta\": \"0\",\n        \"invariant\"\
    : true,\n        \"irreducible\": true,\n        \"period\": 2,\n        \"reachable_state_counts\"\
    : [\n          2\n        ]\n      },\n      {\n        \"n\": 1,\n        \"\
    theta\": \"1\",\n        \"invariant\": true,\n        \"irreducible\": false,\n\
    \        \"period\": null,\n        \"reachable_state_counts\": [\n          1\n\
    \        ]\n      },\n      {\n        \"n\": 2,\n        \"theta\": \"0\",\n\
    \        \"invariant\": true,\n        \"irreducible\": true,\n        \"period\"\
    : 4,\n        \"reachable_state_counts\": [\n          4\n        ]\n      },\n\
    \      {\n        \"n\": 2,\n        \"theta\": \"1\",\n        \"invariant\"\
    : true,\n        \"irreducible\": false,\n        \"period\": null,\n        \"\
    reachable_state_counts\": [\n          1,\n          2\n        ]\n      },\n\
    \      {\n        \"n\": 3,\n        \"theta\": \"0\",\n        \"invariant\"\
    : true,\n        \"irreducible\": true,\n        \"period\": 6,\n        \"reachable_state_counts\"\
    : [\n          6\n        ]\n      },\n      {\n        \"n\": 3,\n        \"\
    theta\": \"1\",\n        \"invariant\": true,\n        \"irreducible\": false,\n\
    \        \"period\": null,\n        \"reachable_state_counts\": [\n          1,\n\
    \          2\n        ]\n      }\n    ],\n    \"scope\": \"Singleton lines, redundant/overlapping\
    \ partitions and one-state spaces are allowed by the tested finite construction.\
    \ Positivity/connectivity/fixed-mixture assumptions must not be silently removed.\"\
    \n  },\n  \"gustafson\": {\n    \"continuous_proposal_density\": \"r_sigma(s)=sqrt(2/pi)/sigma*exp(-s^2/(2\
    \ sigma^2)), s>0. q((x,p),(y,-p))=r_sigma(|y-x|) when p(y-x)>0; the reverse proposal\
    \ has equal density.\",\n    \"exact_density_identity\": \"For A_p(x)=integral_0^infinity\
    \ r_sigma(s)*min(pi(x-p*s),pi(x)) ds, incoming acceptance density at(x,p) is A_p(x)/2\
    \ and incoming rejection density from(x,-p) is[pi(x)-A_p(x)]/2; total pi(x)/2.\
    \ Assumes proper measurable target density and well-defined finite positive current\
    \ density, fixed sigma>0. Zero density outside support is included in the integral.\"\
    ,\n    \"uniform_target_incoming_example\": {\n      \"x\": 0.25,\n      \"sigma\"\
    : 1.0,\n      \"half_normal_cdf_to_left_boundary\": 0.19741265136584743,\n   \
    \   \"accepted_incoming_plus_density\": 0.09870632568292372,\n      \"rejection_from_minus_density\"\
    : 0.4012936743170763,\n      \"correct_total_density\": 0.5,\n      \"wrong_same_sign_rejection_density\"\
    : 0.3253336780597919,\n      \"target_plus_density\": 0.5,\n      \"numeric_scope\"\
    : \"math.erf floating evaluation only; the displayed analytic identity supplies\
    \ exact cancellation.\"\n    },\n    \"negative_control_distinction\": \"Keeping\
    \ the old sign on both acceptance and rejection breaks the augmented target in\
    \ this example. Omitting the final unconditional flip from the equivalent MH-plus-flip\
    \ representation instead leaves a different valid reversible MH kernel: it is\
    \ not the same negative control.\",\n    \"nonreversibility_witness\": \"On a\
    \ positive-density interval, accepted transitions from(x,+) to(y,+), y>x, have\
    \ positive density but their direct reverse with unchanged plus sign has zero\
    \ density. The complete guided-walk kernel differs from reversible ordinary MH.\"\
    ,\n    \"support_note\": \"No reflection, clipping, rejection-resampling or connected-support\
    \ assumption is needed for the invariance identity. The unbounded half-normal\
    \ law can jump across zero-density gaps. This calculation does not certify general\
    \ Harris recurrence, rates or a multivariate bookkeeping implementation.\",\n\
    \    \"scale_endpoint\": \"sigma=0 lies outside the draft definition; then y=x\
    \ and acceptance1 leaves both state/sign unchanged, giving an identity kernel.\"\
    \n  }\n}\n"
  scope_note: Actual execution completed 2026-10-14T21:05:34.530320Z; this generator
    executes no recorded commands.
- check_id: calculation-7
  name: python3 research/discovery/liu-modified-gibbs-boundaries.py
  command: python3 research/discovery/liu-modified-gibbs-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"scope\": \"Independent exact finite algebra checks, not author-code\
    \ replication, scientific approval, floating-point/library execution or a general\
    \ proof.\",\n  \"positive_conditional_cases\": 360,\n  \"checks\": \"Rows stochastic,\
    \ conditional invariance, detailed balance, off-diagonal domination of the independent\
    \ conditional draw, equality of proposal/acceptance and min-form kernels, equivalence\
    \ of NumPyro 0.7.0 correction algebra under positive finite conditional weights.\"\
    ,\n  \"example\": {\n    \"conditional\": [\n      \"3/5\",\n      \"3/10\",\n\
    \      \"1/10\"\n    ],\n    \"kernel\": [\n      [\n        \"29/63\",\n    \
    \    \"3/7\",\n        \"1/9\"\n      ],\n      [\n        \"6/7\",\n        \"\
    2/63\",\n        \"1/9\"\n      ],\n      [\n        \"2/3\",\n        \"1/3\"\
    ,\n        \"0\"\n      ]\n    ],\n    \"rejection_probability_current_0\": \"\
    29/63\"\n  },\n  \"point_mass_guard\": {\n    \"target\": [\n      1\n    ],\n\
    \    \"kernel\": [\n      [\n        \"1\"\n      ]\n    ]\n  },\n  \"uniform_binary_boundary\"\
    : {\n    \"target\": [\n      \"1/2\",\n      \"1/2\"\n    ],\n    \"kernel\"\
    : [\n      [\n        \"0\",\n        \"1\"\n      ],\n      [\n        \"1\"\
    ,\n        \"0\"\n      ]\n    ],\n    \"period\": 2,\n    \"interpretation\"\
    : \"Propose a different category does not guarantee an aperiodic chain; accepted\
    \ moves can coexist with periodicity.\"\n  },\n  \"scan_boundary\": {\n    \"\
    states\": [\n      [\n        0,\n        0\n      ],\n      [\n        0,\n \
    \       1\n      ],\n      [\n        1,\n        0\n      ],\n      [\n     \
    \   1,\n        1\n      ]\n    ],\n    \"target\": [\n      \"1/10\",\n     \
    \ \"1/5\",\n      \"3/10\",\n      \"2/5\"\n    ],\n    \"random_scan_invariant_reversible\"\
    : true,\n    \"systematic_order_invariant\": true,\n    \"systematic_order_reversible\"\
    : false,\n    \"systematic_kernel\": [\n      [\n        \"0\",\n        \"0\"\
    ,\n        \"0\",\n        \"1\"\n      ],\n      [\n        \"0\",\n        \"\
    0\",\n        \"3/4\",\n        \"1/4\"\n      ],\n      [\n        \"0\",\n \
    \       \"1/3\",\n        \"0\",\n        \"2/3\"\n      ],\n      [\n       \
    \ \"1/4\",\n        \"1/4\",\n        \"3/8\",\n        \"1/8\"\n      ]\n   \
    \ ],\n    \"limitation\": \"Does not compare asymptotic variances of systematic\
    \ or random-permutation scan against Gibbs.\"\n  },\n  \"pymc_v5_9_0_code_negative_control\"\
    : {\n    \"target\": [\n      \"3/5\",\n      \"3/10\",\n      \"1/10\"\n    ],\n\
    \    \"equation_kernel\": [\n      [\n        \"7/60\",\n        \"3/4\",\n  \
    \      \"2/15\"\n      ],\n      [\n        \"6/7\",\n        \"11/420\",\n  \
    \      \"7/60\"\n      ],\n      [\n        \"2/3\",\n        \"1/3\",\n     \
    \   \"0\"\n      ]\n    ],\n    \"target_after_one_step\": [\n      \"827/2100\"\
    ,\n      \"2063/4200\",\n      \"23/200\"\n    ],\n    \"preserves_target\": false,\n\
    \    \"binary_case\": [\n      [\n        \"1\",\n        \"0\"\n      ],\n  \
    \    [\n        \"0\",\n        \"1\"\n      ]\n    ],\n    \"scope\": \"Exact\
    \ algebraic interpretation of the inspected source overwriting probabilities before\
    \ constructing its denominator. Actual PyMC/JAX runtime and floating-point behavior\
    \ were not tested.\"\n  }\n}\n"
  scope_note: Actual execution completed 2026-10-14T21:05:35.044896Z; this generator
    executes no recorded commands.
- check_id: calculation-8
  name: python3 research/discovery/dhn-fiber-boundaries.py
  command: python3 research/discovery/dhn-fiber-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"scope\": \"Exact finite illustrations; not a general proof, convergence-rate\
    \ computation, author replication, or independent scientific approval.\",\n  \"\
    directed_positive_target_cases\": 351,\n  \"checks\": \"Stochastic rows, exact\
    \ target invariance, irreducibility, positive self-loop (hence aperiodicity for\
    \ each irreducible case), and failure of detailed balance for the one-dimensional\
    \ cases.\",\n  \"directed_example\": {\n    \"weights\": [\n      1,\n      2,\n\
    \      4\n    ],\n    \"theta\": \"1/5\",\n    \"states\": [\n      [\n      \
    \  [\n          -1\n        ],\n        0\n      ],\n      [\n        [\n    \
    \      -1\n        ],\n        1\n      ],\n      [\n        [\n          -1\n\
    \        ],\n        2\n      ],\n      [\n        [\n          1\n        ],\n\
    \        0\n      ],\n      [\n        [\n          1\n        ],\n        1\n\
    \      ],\n      [\n        [\n          1\n        ],\n        2\n      ]\n \
    \   ],\n    \"transition\": [\n      [\n        \"1/5\",\n        \"0\",\n   \
    \     \"0\",\n        \"4/5\",\n        \"0\",\n        \"0\"\n      ],\n    \
    \  [\n        \"2/5\",\n        \"1/10\",\n        \"0\",\n        \"1/10\",\n\
    \        \"2/5\",\n        \"0\"\n      ],\n      [\n        \"0\",\n        \"\
    2/5\",\n        \"1/10\",\n        \"0\",\n        \"1/10\",\n        \"2/5\"\n\
    \      ],\n      [\n        \"0\",\n        \"1/5\",\n        \"0\",\n       \
    \ \"0\",\n        \"4/5\",\n        \"0\"\n      ],\n      [\n        \"0\",\n\
    \        \"0\",\n        \"1/5\",\n        \"0\",\n        \"0\",\n        \"\
    4/5\"\n      ],\n      [\n        \"0\",\n        \"0\",\n        \"4/5\",\n \
    \       \"0\",\n        \"0\",\n        \"1/5\"\n      ]\n    ],\n    \"invariant\"\
    : [\n      \"1/14\",\n      \"1/7\",\n      \"2/7\",\n      \"1/14\",\n      \"\
    1/7\",\n      \"2/7\"\n    ]\n  },\n  \"theta_zero_uniform_boundary\": {\n   \
    \ \"period\": 10,\n    \"cycle\": [\n      [\n        [\n          -1\n      \
    \  ],\n        0\n      ],\n      [\n        [\n          1\n        ],\n    \
    \    0\n      ],\n      [\n        [\n          1\n        ],\n        1\n   \
    \   ],\n      [\n        [\n          1\n        ],\n        2\n      ],\n   \
    \   [\n        [\n          1\n        ],\n        3\n      ],\n      [\n    \
    \    [\n          1\n        ],\n        4\n      ],\n      [\n        [\n   \
    \       -1\n        ],\n        4\n      ],\n      [\n        [\n          -1\n\
    \        ],\n        3\n      ],\n      [\n        [\n          -1\n        ],\n\
    \        2\n      ],\n      [\n        [\n          -1\n        ],\n        1\n\
    \      ]\n    ]\n  },\n  \"theta_one_uniform_boundary\": {\n    \"closed_classes\"\
    : [\n      [\n        [\n          [\n            -1\n          ],\n         \
    \ 0\n        ]\n      ],\n      [\n        [\n          [\n            -1\n  \
    \        ],\n          1\n        ],\n        [\n          [\n            1\n\
    \          ],\n          0\n        ]\n      ],\n      [\n        [\n        \
    \  [\n            -1\n          ],\n          2\n        ],\n        [\n     \
    \     [\n            1\n          ],\n          1\n        ]\n      ],\n     \
    \ [\n        [\n          [\n            -1\n          ],\n          3\n     \
    \   ],\n        [\n          [\n            1\n          ],\n          2\n   \
    \     ]\n      ],\n      [\n        [\n          [\n            -1\n         \
    \ ],\n          4\n        ],\n        [\n          [\n            1\n       \
    \   ],\n          3\n        ]\n      ],\n      [\n        [\n          [\n  \
    \          1\n          ],\n          4\n        ]\n      ]\n    ]\n  },\n  \"\
    fiber_positive_target_cases\": 64,\n  \"fiber_scope\": \"Two directions on a 2\
    \ by 2 grid, four persistent sign vectors, positive selection probabilities 1/3\
    \ and 2/3; checked invariance, irreducibility and aperiodicity.\",\n  \"limitations\"\
    : \"No empirical results or total-variation/chi-square rate claims tested. Endpoint\
    \ theta values illustrate why the reported ergodicity proposition uses 0<theta<1.\"\
    \n}\n"
  scope_note: Actual execution completed 2026-10-14T21:05:35.661263Z; this generator
    executes no recorded commands.
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T210245Z-gibbs-fiber-guided-walk.json
  locator: identity_search and identity_assessment
  accessed_at: '2026-10-14T21:07:49.727182Z'
  snapshot_sha256: bde6dea6594397164fdc8aba5e816bdda108127b374885acb694adeb9912acf7
  support: supports
  summary: Whole-corpus normalized checks cover every ID, name, alias and scoped synonym
    in 442 pinned AIO and 703 native records; four complete checkouts, including ignored
    and hidden files, are searched for final identities and researched labels. The
    finite excluded-current conditional proposal with its specific acceptance correction
    is distinct from exact Gibbs, generic Metropolis-within-Gibbs, multiple-try updates
    and Neal’s full ordered-pair construction. Bare metropolized Gibbs is a search
    probe, not an exact alias. Existing source-frontier references are resolved in
    place. Related AIO:MarkovChain is supported at a different abstraction level;
    all 18 candidate class contexts and 19 nearest native records are preserved.
  search_scope: Canonical ID/name/alias/all-scoped-synonym checks and retained four
    complete-checkout searches include ignored and hidden files. Bounded corpus scope,
    not universal absence.
- evidence_id: mapping
  kind: record_content
  reference: research/discovery/20261014T210245Z-gibbs-fiber-guided-walk.json
  locator: mapping_context nodes, native_neighbors, semantic_rows and mapping_assessment
  accessed_at: '2026-10-14T21:07:49.727182Z'
  snapshot_sha256: bde6dea6594397164fdc8aba5e816bdda108127b374885acb694adeb9912acf7
  support: supports
  summary: 'The related_match to AIO:MarkovChain is supported. The algorithm constructs
    Markov transitions on a specified conditional or augmented state, supporting a
    method-to-process association. The pinned target is a stochastic process/model
    exported under Network, with a ProbabilisticHiddenLayer has-part assertion. Equivalence,
    subclass membership and inheritance of those assertions are not warranted. The
    dated identity/mapping handoff read eighteen complete exact CLASS contexts, all
    incident edges and their generated YAML: the target plus the seventeen alternatives
    documented here. This rationale concerns the pinned snapshot and manifest retained
    in the review inputs.'
- evidence_id: actual-record-reading
  kind: record_content
  reference: data/curated/LiuModifiedGibbsSampler.yaml
  accessed_at: '2026-10-14T21:07:49.727182Z'
  snapshot_sha256: b3736d9f8dfb1e8b7e218d2b8fc075f413a719dc1c11cee951af8fa3b4542e54
  support: supports
  summary: 'Full maintained record and all five claim/source locators reread after
    capture. Equation9 proposal and acceptance use original conditional masses; Eq16
    min form and diagonal rejection agree. Supported-current/point-mass guards, local
    detailed balance, joint invariance, fixed-mixture reversibility and composition
    limitations are sound. The exact full-sweep counterexample and binary periodicity
    support the qualifications without transferring local Peskun ordering to arbitrary
    sweeps. Alias absence and distinct local versus ordered-pair identity remain appropriate.
    All remaining maintained fields, identity notes, source version/access/hash, AIO
    pin and related mapping, limitations, DRAFT status and curation metadata were
    assessed. Root reread the complete assessment configuration after capture and
    agrees within its stated bounds. Root retained the earlier full18AIO-context reading
    and seven nearest-native readings; broader182semantic/19native assessment remains
    attributed to the supporting source agent. Current integrity checks confirm no
    prior canonical bytes changed. The corrected mathematical audit and original erroneous15-versus21July
    metadata lineage were inspected; the15July successor governs, with unchanged scientific
    content. Root also read the actual-content supporting audit, which identifies
    no required correction and remains part of the same author workflow. Actual post-capture
    source reread: Neal2004 PDF pages5,6,8 freshly read as extracted text after capture;
    pages5 and8 freshly inspected visually. Retained prior root reading covers all25
    text pages and selected visual pages1,6–9; no original Liu1996 full-text reading
    is claimed.'
- evidence_id: neal2004
  kind: primary_source
  reference: https://arxiv.org/pdf/math/0407281v1
  locator: Section 3, PDF p. 5, Liu conditional proposal and Equation 9; Section 3,
    PDF p. 5, paragraph preceding Equation 9 and point-mass exception below it; Section
    3, PDF p. 5, Equation 9; Section 4, PDF p. 8, Equation 16 and diagonal completion;
    Section 3, PDF pp. 5–6, Equation 9 and ensuing off-diagonal comparison; Section
    4, PDF p. 8, Equation 16; Section 3, PDF pp. 5–6, Peskun qualifications and scan-order
    discussion; Section 3 conclusion and Section 4, PDF pp. 6–8, Equations 10–16
  accessed_at: '2026-10-14T19:41:47Z'
  snapshot_sha256: b3f451ce72fb992aac2c98c7e3da317c34b0ba96ffacbff65f765632481b2eb3
  support: supports
  summary: 'arXiv:math/0407281v1, submitted 15 July 2004; Technical Report 0406, dated
    15 July 2004; 25 PDF pages. Actual root reading: Neal2004 PDF pages5,6,8 freshly
    read as extracted text after capture; pages5 and8 freshly inspected visually.
    Retained prior root reading covers all25 text pages and selected visual pages1,6–9;
    no original Liu1996 full-text reading is claimed. The exact source method and
    assumption boundaries support the maintained claims. Source access timestamps
    remain separate from this actual review reading time.'
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/gibbs-fiber-guided-walk-boundaries.py
  locator: Combined result section liu
  accessed_at: '2026-10-14T21:07:49.727182Z'
  snapshot_sha256: f4605a688ade559b75acbd2272dc574ee876e765eee0287107640ff552e2b889
  support: supports
  summary: 'Original bounded checks: exact rational finite transitions and scan examples;
    analytic continuous cancellation with separately labeled floating erf illustration.
    Not author-code replication or a general convergence theorem. Selected result:
    {"supported_subspace_cases_including_zero_mass_categories": 116, "support_example":
    [[1, 3], ["2/3", "1/3"], [["1/2", "1/2"], ["1", "0"]]], "point_mass_example":
    [[2], ["1"], [[1]]], "uniform_binary_period": 2, "sweep_counterexample": {"target_weights":
    [4, 2, 2, 1], "target": ["4/9", "2/9", "2/9", "1/9"], "states": [[0, 0], [0, 1],
    [1, 0], [1, 1]], "centered_observable": [1, -2, -2, 4], "exact_gibbs_sweep_kernel":
    [["4/9", "2/9", "2/9", "1/9"], ["4/9", "2/9", "2/9", "1/9"], ["4/9", "2/9", "2/9",
    "1/9"], ["4/9", "2/9", "2/9", "1/9"]], "liu_sweep_kernel": [["1/4", "1/4", "1/4",
    "1/4"], ["1/2", "0", "1/2", "0"], ["1/2", "1/2", "0", "0"], ["1", "0", "0", "0"]],
    "uniform_random_permutation_equals_fixed_sweep_here": true, "both_sweep_kernels_reversible_irreducible_aperiodic":
    true, "asymptotic_variance_per_full_sweep": {"liu": "20/3", "gibbs": "4"}, "asymptotic_variance_per_single_fixed_random_scan_update":
    {"liu": "4/3", "gibbs": "4"}, "failed_sweep_off_diagonal_domination": [{"from":
    [0, 1], "to": [1, 1], "modified": "0", "gibbs": "1/9"}, {"from": [1, 0], "to":
    [1, 1], "modified": "0", "gibbs": "1/9"}, {"from": [1, 1], "to": [0, 1], "modified":
    "0", "gibbs": "2/9"}, {"from": [1, 1], "to": [1, 0], "modified": "0", "gibbs":
    "2/9"}], "meaning": "Local Peskun ordering does not transfer automatically to
    full sweeps, including reversible uniform random-permutation sweeps. No wall-clock
    comparison."}, "dependent_target_scan_check": {"weights": [1, 2, 3, 4], "systematic_invariant_nonreversible":
    true, "uniform_random_permutation_invariant_reversible": true, "state_dependent_selection_counterexample_after":
    ["1/5", "1/10", "3/5", "1/10"]}}'
- evidence_id: supporting-math-audit
  kind: record_content
  reference: research/discovery/20261014T203348Z-gibbs-fiber-guided-walk-supporting-math-audit.json
  accessed_at: '2026-10-14T21:07:49.727182Z'
  snapshot_sha256: cb907256334387fed3a86d5904ed0f07e44222547c109db88d2aab6a24f8555a
  support: supports
  summary: Root assessed the corrected bounded mathematical audit; supporting agents
    belong to the same author workflow and provide no independent scientific approval.
- evidence_id: metadata-correction-lineage
  kind: record_content
  reference: research/discovery/20261014T210245Z-gibbs-fiber-guided-walk.json
  locator: supporting_math_audit_correction_lineage and source_analysis.bounded_math_audit
  accessed_at: '2026-10-14T21:07:49.727182Z'
  snapshot_sha256: bde6dea6594397164fdc8aba5e816bdda108127b374885acb694adeb9912acf7
  support: supports
  summary: The original audit incorrectly dated Neal v1 as 21 July 2004. The explicitly
    corrected successor uses 15 July; original object/hash, actual correction metadata
    and unchanged scientific sections are preserved.
assessments:
- assessment_id: identity
  area: identity
  topic: Liu modified discrete-state Gibbs sampler
  outcome: supported
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  evidence_ids:
  - identity
  - neal2004
  summary: Retain the narrow DRAFT identity within the documented search scope.
  details: 'The record identifies the finite categorical conditional update attributed
    to Liu 1996: exclude the present category in the conditional proposal and apply
    its precise Metropolis correction. Ordinary Gibbs draws directly from the full
    conditional; generic Metropolis-within-Gibbs allows many other proposals. Multiple-try
    Metropolis-within-Gibbs has a candidate-set/reference-set mechanism. Neal’s ordered-pair
    backtracking-suppression construction can use this update as an ingredient, but
    has a different full state and algorithm identity. The maintained scope is the
    local conditional update, with scan compositions explicitly qualified. Bare metropolized
    Gibbs, every modified Gibbs sampler, a whole library sampler class and Liu’s different
    1996 independence-sampler paper are not exact aliases.'
- assessment_id: definition
  area: evidence
  topic: Definition and source scope
  outcome: supported
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  evidence_ids:
  - neal2004
  - actual-record-reading
  summary: The maintained definition is supported within its stated method scope.
  details: The definition specifies a discrete conditional algorithm and its exclusion-plus-correction
    mechanism. Its detailed claims narrow the operation to a finite conditional and
    a supported current category, with a point-mass stay rule. It does not describe
    a nonreversible pair lift or promise that every iteration moves. Neal 2004 Section
    3 PDF p. 5 attributes the modification to Liu and displays both the excluded-current
    proposal and Eq 9 acceptance; PDF p. 6 states scan-order qualifications. Section
    4 Eq 16 supplies the min-form conditional kernel in the separate pair-chain application.
    Original Liu 1996 is known through inspected metadata/abstract but its full text
    was not obtained. No unseen original proof or author implementation is claimed.
    The record can use this inspected primary mathematical exposition while preserving
    the original-source access gap. The inspected source version is arXiv:math/0407281v1
    / Technical Report 0406, cover 15 July 2004.
- assessment_id: mapping
  area: grounding
  topic: Related Markov-process mapping
  outcome: supported
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  evidence_ids:
  - mapping
  - neal2004
  summary: related_match expresses method-to-process association without equivalence
    or ontology inheritance.
  details: 'The related_match to AIO:MarkovChain is supported. The algorithm constructs
    Markov transitions on a specified conditional or augmented state, supporting a
    method-to-process association. The pinned target is a stochastic process/model
    exported under Network, with a ProbabilisticHiddenLayer has-part assertion. Equivalence,
    subclass membership and inheritance of those assertions are not warranted. The
    dated identity/mapping handoff read eighteen complete exact CLASS contexts, all
    incident edges and their generated YAML: the target plus the seventeen alternatives
    documented here. This rationale concerns the pinned snapshot and manifest retained
    in the review inputs.

    Alternatives:

    AIO:Network: A target-invariant transition procedure is not a network architecture.
    A Markov graph representation does not establish an exact or broader-class mapping
    to Network.

    AIO:ProbabilisticHiddenLayer: A retained sign, conditional category or auxiliary
    state is not a neural hidden layer that estimates probabilities. The MarkovChain
    has-part edge is context, not an inherited algorithm assertion.

    AIO:Model: A target distribution or model may be an input or application; the
    maintained identity is the transition algorithm, not a fitted statistical or predictive
    model.

    AIO:MachineLearningTask: These records specify operational sampling mechanisms,
    not a machine-learning problem or task definition.

    AIO:TrainingStrategy: Use of a sampler during learning does not make its invariant
    transition rule a training strategy.

    AIO:MathematicalFunction: Update equations describe the mechanism, but they do
    not make a randomized target-preserving procedure merely a mathematical input-output
    function.

    AIO:BayesianNetwork: Bayesian inference is an application; no directed acyclic
    dependency graph is required by these transition rules.

    AIO:ProbabilisticGraphicalModel: A graphical target distribution is optional.
    The pinned graph-factorization/task identity is distinct from a sampler acting
    on a specified target.

    AIO:UnsupervisedLearning: No learning-from-unlabeled-data objective is needed
    to define these finite or continuous sampling kernels.

    AIO:BoltzmannMachineNetwork: A Boltzmann machine may be a target/application,
    but no recurrent stochastic network architecture is required.

    AIO:RestrictedBoltzmannMachine: Sampling a restricted Boltzmann machine does not
    make a general conditional update or direction-based kernel that model architecture.

    AIO:EnergyBasedLLM: The exact pinned CLASS denotes an explicit token-sequence
    density language model. A broader related synonym does not replace that definition
    or make it a generic energy-target sampler.

    AIO:ImplicitLanguageModel: Whole-sequence language-model scoring is not the identity
    of these sampling mechanisms.

    AIO:Preprocessing: The methods construct target-invariant transitions rather than
    prepare raw data for analysis.

    AIO:Layer: A transition stage or stored direction is not a neural-network layer.

    AIO:HiddenLayer: Auxiliary direction memory is not a nonlinear hidden neural layer.

    AIO:CausalGraphicalModel: These target distributions need not encode causal assumptions;
    a causal-model application is not algorithm identity.'
- assessment_id: excluded-current-conditional-proposal
  area: evidence
  topic: excluded-current-conditional-proposal
  outcome: supported
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  evidence_ids:
  - neal2004
  - calculation
  summary: Supported within the stated assumptions and inspected passages.
  details: 'For a supported current category a, p_a<1 permits normalization over the
    remaining categories: q(c|a)=p_c/(1-p_a). Zero-mass categories are never proposed.
    At p_a=1, the only supported state stays without evaluating the undefined proposal.
    This matches the explicit point-mass exception below Neal 2004 Eq 9. The original
    calculator’s strictly positive-domain check is supplemented by 116 input vectors
    with zero masses, evaluated on their positive support; no outgoing rule from an
    unsupported current state is invented.'
- assessment_id: conditional-metropolis-correction
  area: evidence
  topic: conditional-metropolis-correction
  outcome: supported
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  evidence_ids:
  - neal2004
  - calculation
  summary: Supported within the stated assumptions and inspected passages.
  details: Multiplying q(c|a) by min(1,(1-p_a)/(1-p_c)) yields the stated min-form
    off-diagonal entry. The diagonal is rejection mass, not a requirement to change
    category on every step. Both masses in the correction are the original conditional
    probabilities. The supported equation differs from any expression that mistakenly
    substitutes the renormalized proposal probability. No unrelated library-runtime
    behavior is used as positive evidence.
- assessment_id: conditional-balance-and-joint-invariance
  area: evidence
  topic: conditional-balance-and-joint-invariance
  outcome: supported
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  evidence_ids:
  - neal2004
  - calculation
  summary: Supported within the stated assumptions and inspected passages.
  details: For distinct supported a,c, p_a*U(a,c) is symmetric in a,c; row completion
    then yields local detailed balance. Each denominator is at most one, so U(a,c)>=p_c.
    Conditioning on the other variables gives joint-target invariance without a persistent
    sign or previous joint state. This off-diagonal domination concerns the local
    transition, not an arbitrary composite update or its mixing time. The equal-mass
    binary kernel has period two, which prevents inferring aperiodicity merely from
    invariance.
- assessment_id: scan-schedule-and-comparison-boundary
  area: evidence
  topic: scan-schedule-and-comparison-boundary
  outcome: supported
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  evidence_ids:
  - neal2004
  - calculation
  summary: Supported within the stated assumptions and inspected passages.
  details: A mixture with fixed component-selection probabilities preserves reversibility
    and the joint target; a sequential composition preserves invariance but can fail
    detailed balance. A uniform mixture over all permutation sweeps is reversible
    because reverse-order compositions pair as adjoints, but local Peskun domination
    still need not order the full-sweep matrices. The bounded counterexample has independent
    binary target weights (4,2,2,1)/9 and centered observable (1,-2,-2,4). Its modified
    full sweep has asymptotic variance 20/3 versus 4 for exact-Gibbs full sweeps;
    both are reversible, irreducible and aperiodic, and uniform random-permutation
    equals the fixed sweep here. The corresponding single-coordinate fixed random
    scan gives 4/3 versus 4. These are different per-transition units, not a wall-clock
    comparison or a general superiority claim. They justify the record’s cautious
    scan boundary.
- assessment_id: local-update-versus-pair-state-construction
  area: evidence
  topic: local-update-versus-pair-state-construction
  outcome: supported
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  evidence_ids:
  - neal2004
  summary: Supported within the stated assumptions and inspected passages.
  details: Neal introduces the Liu update before the separate ordered-pair swap/update
    construction. Its role as an ingredient does not equate the locally reversible
    conditional kernel with the augmented nonreversible chain. A proposal excludes
    the current category but rejection can retain it; older revisits are also possible.
    The record correctly separates these meanings of suppression.
- assessment_id: scope-and-boundaries
  area: consistency
  topic: finite supported conditional, correct excluded-current normalization, point-mass
    guard, local reversibility, explicit scan schedule and local-versus-pair-chain
    identity
  outcome: supported
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  evidence_ids:
  - neal2004
  - calculation
  - supporting-math-audit
  summary: Mechanism, scan/parameter limits and identity boundaries remain qualified.
  details: No new general Peskun theorem, arbitrary joint scan/adaptation guarantee,
    continuous nonatomic improvement, universal efficiency, author-code replication
    or library-runtime certification. The original Liu full-text access gap remains
    explicit and Neal 2024 variants remain an open source-assessment lead.
- assessment_id: actual-maintained-fields
  area: provenance
  topic: All captured maintained fields
  outcome: supported
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  evidence_ids:
  - actual-record-reading
  - identity
  - mapping
  - neal2004
  summary: Root reassessed the complete current record after canonical capture; DRAFT
    remains.
  details: 'Full maintained record and all five claim/source locators reread after
    capture. Equation9 proposal and acceptance use original conditional masses; Eq16
    min form and diagonal rejection agree. Supported-current/point-mass guards, local
    detailed balance, joint invariance, fixed-mixture reversibility and composition
    limitations are sound. The exact full-sweep counterexample and binary periodicity
    support the qualifications without transferring local Peskun ordering to arbitrary
    sweeps. Alias absence and distinct local versus ordered-pair identity remain appropriate.
    All remaining maintained fields, identity notes, source version/access/hash, AIO
    pin and related mapping, limitations, DRAFT status and curation metadata were
    assessed. Root reread the complete assessment configuration after capture and
    agrees within its stated bounds. Root retained the earlier full18AIO-context reading
    and seven nearest-native readings; broader182semantic/19native assessment remains
    attributed to the supporting source agent. Current integrity checks confirm no
    prior canonical bytes changed. The corrected mathematical audit and original erroneous15-versus21July
    metadata lineage were inspected; the15July successor governs, with unchanged scientific
    content. Root also read the actual-content supporting audit, which identifies
    no required correction and remains part of the same author workflow. Rereads:
    Neal2004 PDF pages5,6,8 freshly read as extracted text after capture; pages5 and8
    freshly inspected visually. Retained prior root reading covers all25 text pages
    and selected visual pages1,6–9; no original Liu1996 full-text reading is claimed.'
- assessment_id: audit-date-correction
  area: provenance
  topic: Original and corrected mathematical audit lineage
  outcome: supported
  target_ids:
  - AIMech:LiuModifiedGibbsSampler
  evidence_ids:
  - metadata-correction-lineage
  summary: The bibliographic correction is explicit and scientific audit content is
    unchanged.
  details: Original created_at, draft inputs, findings and calculation audit are retained.
    The corrected successor governs; no future review/gate is inferred from the correction.
findings: []
actions: []
limitations:
- Author self-review, not independent scientific approval or DRAFT promotion.
- No new general Peskun theorem, arbitrary joint scan/adaptation guarantee, continuous
  nonatomic improvement, universal efficiency, author-code replication or library-runtime
  certification. The original Liu full-text access gap remains explicit and Neal 2024
  variants remain an open source-assessment lead.
- The bounded calculators illustrate local identities and finite scan counterexamples;
  they do not replace primary evidence or required repository checks.
- Neither a reversible random-permutation sweep nor a systematic sweep automatically
  inherits local off-diagonal dominance.
- 'Original Liu 1996 full PDF was not obtained: publisher/author access attempts are
  preserved in source handoff. The curated method uses inspected Neal 2004 equations,
  not unseen original proofs or an abstract as method evidence.'
- DHN source is the 5 June 1997 author technical report; the 2000 journal PDF was
  not obtained or read. Source reading is selective and does not establish inspection
  of every spectral proof.
- Gustafson journal-layout PDF came from the observed public Studyres mirror. Publisher-download
  byte equivalence was not established; no redistribution license is inferred. PDF
  bytes are not copied to the repository.
- Gustafson Example 2 and Example 4/Figure 2 disagree on two numerical performance
  labels. Those numerals and the experimental first-hit criterion are not adopted
  as performance or general convergence claims.
notes:
- Empty findings reflect actual root assessment of this selected captured record only;
  no unrelated finding closure or literature saturation is asserted.
- A metadata correction in the supporting audit is retained as provenance, not fabricated
  maintained-record finding lineage.
tags:
- native-concepts
- self-review
- discovery-ongoing
- mcmc
```
